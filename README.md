# Reciprocal Operations (`reciprocal-ops`)

*Relational and reciprocal practices for IT projects, inspired by Dr. Jennifer Grenz's* Medicine Wheel for the Planet.

The command-line tool is `recip`.

## Educational Portfolio Project Statement
This repository functions strictly as a conceptual, quantitative computer science simulation and software engineering learning experiment. The architecture models structural operations frameworks, multi-agent dynamic simulations, and automated compliance pipelines.

## Framework Inception and Academic Influence
The technical paradigms, balance calculations, and continuous stewardship metrics codified within this repository are explicitly inspired by and adapted from the place-based Indigenous ecological methodologies articulated by Dr. Jennifer Grenz in her book, *Medicine Wheel for the Planet*. This project translates her environmental ecosystem concepts—such as Relationality, Reciprocity, and critiques of static equilibrium states—into systemic constraints for enterprise infrastructure workflows. 

To maintain strict respect for the original text and protect against cultural dilution, the terminology has been deliberately mapped to established IT infrastructure concepts (e.g., re-allocating descriptive labels like "Ancestral Memory" to "Historical Record Baselines"). The four-direction layout below is an organizing device for this repository and does not describe the teachings of any Nation. See [Cultural Context](docs/CULTURAL_CONTEXT.md) for scope, positionality, and the terminology guide.

## Complete Framework Architecture Flow Map

```text
               [ NORTH: HISTORICAL RECORDS ]
               • RecordRegistry / Git Churn Analytics
               • System Relational Dependency Map Trees
                                │
                                ▼
     [ WEST: GOVERNANCE ] ──────┼──────► [ EAST: WEBWORK VARIANCE ]
     • Structural Constraints   │        • Multi-Agent Ingestion Scans
       Pipeline Build Gates     │        • Slide-Window Rate Anomaly Checks
                                │
                                ▼
               [ SOUTH: CONTINUOUS TENDING ]
               • Technical Debt Reciprocity Broker
               • Tending Ratios (Pruning vs Churn Extraction)
```

## Structure Strategy Reference

### 1. Historical Records & Baselines (North)
Tracks deep platform records via the `RecordRegistry` and maps sliding window history context using the `HistoricalRecordBuffer`. This prevents development workflows from making decisions based on short-sighted or ahistorical greenfield biases.

### 2. Webwork Interdependence & Variance (East)
Monitors how runtime spikes interact with team load (`--burnout`, a team-level anonymous score from the [team load check](docs/templates/team-load-check.md)). The `TelemetrySpikeDetector` checks the rate of variance, and the `AlertClassifier` routes unified alarms to prevent teams from being unsustainably mined for short-term transaction throughput.

### 3. Continuous Tending (South)
Measures a `Tending Ratio` (lines deleted / lines added, docs and tests excluded) over a window of recent commits via the `DebtBroker`. It runs in advisory mode by default; `--enforce` blocks builds only when the team opts in.

### 4. Relational Governance (West)
Defines design review pipelines via `WebworkAssessor` to verify code changes maintain ecological balance across the environment before deployment.

## Using the Framework on Your Project
The practices work with or without the Python tooling.

- [Practices guide](docs/guide/PRACTICES.md): questions, practices, and signals for each direction across the project lifecycle.
- [Worked example](docs/guide/WORKED_EXAMPLE.md): a legacy file-share migration, end to end.
- Templates: [project charter](docs/templates/project-charter.md), [design review checklist](docs/templates/design-review-checklist.md), [retrospective](docs/templates/retrospective.md), [team load check](docs/templates/team-load-check.md).
- Reference: [operational manual](docs/specifications/OPERATIONAL_MANUAL.md), [strategic goals](docs/STRATEGIC_GOALS.md), [ADRs](docs/adr/), [sample calls](docs/specifications/SAMPLE_CALLS.md).

## Quick Start
```bash
uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python -e '.[dev]'
source .venv/bin/activate

# Scan a system with synthetic telemetry and a team load score
recip scan --system my-service --burnout 2.5

# Report the Tending Ratio over the last 50 commits (advisory)
recip tend --window 50
```

## Local Operational Validation Guidelines
To execute the automated verification suite, run the testing engine out of your terminal:
```bash
# Execute the complete validation matrix (15 tests)
pytest -v
```

CI runs the same suite on Python 3.11–3.13 and reports the Tending Ratio in advisory mode. See [CONTRIBUTING.md](CONTRIBUTING.md) to contribute.

---
**Related docs:** [Docs index](docs/README.md) · [Cultural Context](docs/CULTURAL_CONTEXT.md) · [Practices Guide](docs/guide/PRACTICES.md) · [Worked Example](docs/guide/WORKED_EXAMPLE.md) · [Operational Manual](docs/specifications/OPERATIONAL_MANUAL.md) · [Templates](docs/README.md#templates) · [ADRs](docs/README.md#architecture-decision-records) · [Contributing](CONTRIBUTING.md)
