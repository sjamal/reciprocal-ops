# Contributing

Thank you for helping improve this framework.

## Before You Start
- Read [Cultural Context](docs/CULTURAL_CONTEXT.md), especially the terminology guide.
- Open an issue to discuss larger changes first.

## Setup
```bash
uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python -e '.[dev]'
.venv/bin/python -m pytest -v
```

Or with pip:
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e '.[dev]'
pytest -v
```

## Guidelines
- **Vocabulary:** Use plain IT terms. Do not add sacred or ceremonial terms as labels, class names, or metrics.
- **People data:** Any metric about people must be team-level, anonymous, and aggregated.
- **Tests:** Add or update tests for code changes. Keep `pytest` green.
- **Decisions:** Record significant design choices as a new ADR in `docs/adr/`.
- **Docs:** Update the README, [practices guide](docs/guide/PRACTICES.md), or templates when behaviour changes.

## Pull Requests
- Keep PRs focused on one change.
- Describe what changed and why.
- Run `recip tend` and note the Tending Ratio in the PR if the change is large.

---
**Related docs:** [Project README](README.md) · [Docs index](docs/README.md) · [Cultural Context](docs/CULTURAL_CONTEXT.md) · [Practices Guide](docs/guide/PRACTICES.md) · [ADRs](docs/README.md#architecture-decision-records)
