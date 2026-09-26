"""Verifies code tending validation constraints."""
import os
from git import Repo
from reciprocal_ops.pipeline.debt_broker import DebtBroker

def test_empty_repo_graceful_pass():
    broker = DebtBroker(repo_path=".")
    stats = broker.parse_commit_stewardship()
    assert "tending_ratio" in stats

def _commit(repo, root, path, content, message):
    full = root / path
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(content)
    repo.index.add([path])
    repo.index.commit(message)

def test_ratio_counts_code_and_excludes_docs(tmp_path):
    repo = Repo.init(tmp_path)
    with repo.config_writer() as cw:
        cw.set_value("user", "name", "test")
        cw.set_value("user", "email", "test@example.com")

    _commit(repo, tmp_path, "app.py", "a\nb\nc\nd\n", "add code")
    _commit(repo, tmp_path, "app.py", "a\n", "prune code")
    _commit(repo, tmp_path, "docs/guide.md", "x\n" * 100, "add docs")

    broker = DebtBroker(repo_path=str(tmp_path), required_ratio=0.5)
    stats = broker.parse_commit_stewardship()

    assert stats["additions"] == 4
    assert stats["deletions"] == 3
    assert stats["tending_ratio"] == 0.75
    assert broker.verify_compliance(stats)

def test_window_limits_commits(tmp_path):
    repo = Repo.init(tmp_path)
    with repo.config_writer() as cw:
        cw.set_value("user", "name", "test")
        cw.set_value("user", "email", "test@example.com")

    for i in range(5):
        _commit(repo, tmp_path, f"f{i}.py", "x\n", f"c{i}")

    stats = DebtBroker(repo_path=str(tmp_path), window=2).parse_commit_stewardship()
    assert stats["commits"] == 2
    assert stats["additions"] == 2
