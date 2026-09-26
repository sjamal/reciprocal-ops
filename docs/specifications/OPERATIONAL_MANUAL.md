# Operational Manual: Relational and Reciprocal Engineering Practice

This framework draws on relational and reciprocal principles described in Dr. Jennifer Grenz's *Medicine Wheel for the Planet* and applies them, as the author's own engineering interpretation, to IT workflows, multi-agent modelling, and automation. See [Cultural Context](../CULTURAL_CONTEXT.md) for scope and terminology.

The four-direction layout is an organizing device for this repository. It does not describe the teachings of any Nation.

## 1. Historical Records & Baselines (North)
Infrastructure cannot be safely modified without understanding its technical history. The `RecordRegistry` stores system profiles and dependencies, and the `HistoricalRecordBuffer` keeps a sliding window of recent readings across separate runs. Together they move teams away from ahistorical greenfield assumptions.

### Ingestion Metric Example
When parsing incoming frames, the engine calculates moving time-series deviations using variance ratios instead of flat, zero-tolerance hard limits:
```text
Variance Ratio = Current Reading / Moving History Mean
```

## 2. Webwork Interdependence & Variance (East)
The `TelemetrySpikeDetector` compares each reading against a rolling mean, and the `AlertClassifier` combines that verdict with the team and system footprint below. A spike absorbed by a balanced system is an `ADAPTIVE_SHIFT`; a spike on an unbalanced system is a `SYSTEMIC_DISRUPTION`.

Traditional risk management often buys throughput at the cost of team sustainability. This framework instead scores every change on four dimensions:
- **System Integrity:** Core operational infrastructure stability.
- **Operational Burnout:** Toil, page stress, and engineering fatigue thresholds.
- **Resource Overhead:** Accumulation rate of technical complexity.
- **Knowledge Equity:** Democratization and preservation of institutional logic.

Operational burnout is a **team-level, anonymous self-assessment**. Never collect or report it per person. See the [team load check](../templates/team-load-check.md).

## 3. Code Stewardship and Active Tending (South)
Engineering velocity should be matched by care for the platform. The `DebtBroker` measures a Tending Ratio across a window of recent commits:
```text
Tending Ratio = Lines Deleted / Lines Added   (docs and tests excluded by default)
```
Run it in advisory mode first (`recip tend`). Only turn on enforcement (`--enforce`) once the team agrees on a threshold that fits its codebase.

## 4. Relational Governance (West)
The `WebworkAssessor` computes the variance across the four dimensions above. High variance means one dimension is being traded for another, for example speed bought with burnout. A proposal is balanced when variance is at or below `1.0` and burnout is below `3.5`.

Use the [design review checklist](../templates/design-review-checklist.md) to discuss the result with the people a change affects.

---
**Related docs:** [Project README](../../README.md) · [Docs index](../README.md) · [Cultural Context](../CULTURAL_CONTEXT.md) · [Practices Guide](../guide/PRACTICES.md) · [Worked Example](../guide/WORKED_EXAMPLE.md) · [Sample Calls](SAMPLE_CALLS.md) · [Strategic Goals](../STRATEGIC_GOALS.md) · [ADRs](../README.md#architecture-decision-records)
