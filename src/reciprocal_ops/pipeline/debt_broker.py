"""
Pipeline component governing code stewardship metrics and maintenance balance thresholds.
"""

import os
from typing import Dict, Any, Iterable, Optional
from git import Repo

DEFAULT_EXCLUDE_PREFIXES = ("docs/", "tests/")

class DebtBroker:
    """Measures the Tending Ratio over a window of commits; advisory unless enforced by the caller."""

    def __init__(
        self,
        repo_path: str,
        required_ratio: Optional[float] = None,
        window: int = 50,
        exclude_prefixes: Iterable[str] = DEFAULT_EXCLUDE_PREFIXES,
    ):
        self.repo_path = repo_path
        self.required_ratio = (
            required_ratio if required_ratio is not None
            else float(os.getenv("REQUIRED_TENDING_RATIO", 1.20))
        )
        self.window = window
        self.exclude_prefixes = tuple(exclude_prefixes)

    def _is_excluded(self, path: str) -> bool:
        return path.startswith(self.exclude_prefixes) or path.endswith(".md")

    def parse_commit_stewardship(self, target_branch: str = "HEAD") -> Dict[str, Any]:
        """
        Examines local Git history metrics to evaluate refactoring ratios.
        Tracks if deletions (tending) match or exceed additions (new growth).
        """
        if not os.path.exists(os.path.join(self.repo_path, ".git")):
            return {"additions": 0, "deletions": 0, "commits": 0, "tending_ratio": 0.0}

        repo = Repo(self.repo_path)
        try:
            commits = list(repo.iter_commits(target_branch, max_count=self.window))
        except Exception:
            return {"additions": 0, "deletions": 0, "commits": 0, "tending_ratio": 1.0}

        total_additions = 0
        total_deletions = 0

        for commit in commits:
            for path, stats in commit.stats.files.items():
                if self._is_excluded(str(path)):
                    continue
                # GitPython reports added lines as "insertions".
                total_additions += stats.get("insertions", 0)
                total_deletions += stats.get("deletions", 0)

        ratio = float(total_deletions / total_additions) if total_additions > 0 else 1.0

        return {
            "additions": total_additions,
            "deletions": total_deletions,
            "commits": len(commits),
            "tending_ratio": round(ratio, 4)
        }

    def verify_compliance(self, stats: Dict[str, Any]) -> bool:
        """Enforces a pipeline gate preventing feature extraction without refactoring stability."""
        return bool(stats["tending_ratio"] >= self.required_ratio)
