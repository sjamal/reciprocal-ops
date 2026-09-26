# Worked Example: Migrating a Legacy File Share

This example applies the [practices guide](PRACTICES.md) to one realistic IT project. All numbers below come from running this repository's tooling.

## Scenario
A department runs `file-sync`, a 12-year-old on-premises file share with nightly sync jobs. The goal is to move it to cloud object storage. The system has one long-time maintainer, undocumented consumers, and frequent after-hours pages.

---

## 1. Intake (North)
The team fills in the [project charter](../templates/project-charter.md) and registers a system profile.

```python
from reciprocal_ops.storage.record_registry import RecordRegistry, SystemProfile

registry = RecordRegistry(storage_path="registry.json")
registry.register_profile(SystemProfile(
    system_id="file-sync",
    historical_baseline_years=12,
    criticality_tier=2,
    legacy_dependencies_count=3,
    dependencies=["payroll-export", "research-archive", "backup-job"],
    operational_history_notes="Nightly sync; single maintainer; consumers partly undocumented.",
))
```

**Findings**
- Three downstream consumers, one of which (`research-archive`) was unknown to the project sponsor.
- No ADRs exist. The team writes ADR-0001 recording why the share was built and which constraints still apply.

## 2. First Design Review (West)
The team runs a [team load check](../templates/team-load-check.md) (score **3.8**) and scores the first plan in the [design review](../templates/design-review-checklist.md):

| Dimension | Score |
|---|---|
| System integrity | 4.5 |
| Operational burnout (team load) | 3.8 |
| Resource overhead | 2.5 |
| Knowledge equity | 1.5 |

```python
from reciprocal_ops.pipeline.webwork_assessor import WebworkScore, WebworkAssessor

plan_a = WebworkScore(system_integrity=4.5, operational_burnout=3.8,
                      resource_overhead=2.5, knowledge_equity=1.5)
WebworkAssessor().calculate_ecosystem_variance(plan_a)  # 1.6669
WebworkAssessor().is_balanced(plan_a)                   # False
```

The plan is technically sound but unbalanced. It relies on the single maintainer working evenings, and knowledge stays with one person.

**Mitigations agreed**
- Pair a second engineer with the maintainer for the migration.
- Write runbooks during the work, not after it.
- Move cut-over to business hours with a staged rollout.

## 3. Revised Plan (West)
A new team load check scores **2.6**. The revised plan scores:

```python
plan_b = WebworkScore(system_integrity=4.2, operational_burnout=2.6,
                      resource_overhead=2.0, knowledge_equity=3.8)
WebworkAssessor().calculate_ecosystem_variance(plan_b)  # 0.4875
WebworkAssessor().is_balanced(plan_b)                   # True
```

System integrity dropped slightly (4.5 → 4.2) because of the staged rollout. The team accepts this trade-off knowingly.

## 4. Build (South)
The team reserves 20% of each sprint for tending and tracks the ratio in advisory mode:

```bash
recip tend --window 50
```

Deleting the old sync scripts after cut-over raises the ratio. The team reviews the trend in each [retrospective](../templates/retrospective.md) instead of gating builds on it.

## 5. Operate (East)
During the first month-end run, compute jumps to 300 against a recent baseline of about 100:

```python
from reciprocal_ops.telemetry.spike_detector import TelemetrySpikeDetector
from reciprocal_ops.pipeline.alert_classifier import AlertClassifier

spike = TelemetrySpikeDetector(deviation_threshold=1.8).evaluate_window(
    "file-sync", "compute_cycles", 300, [100, 110, 95, 105, 98])
# variance_ratio=2.95, verdict='CRITICAL_SPIKE'

AlertClassifier().classify_event(spike, plan_b)  # ADAPTIVE_SHIFT, LOW
AlertClassifier().classify_event(spike, plan_a)  # SYSTEMIC_DISRUPTION, CRITICAL
```

The same spike is a low-urgency adaptive shift for a balanced team and system. Under the original plan, it would have been a critical disruption. The difference comes from how the team and platform were prepared, not from the spike itself.

## 6. Retire (North)
- Archive the old share's runbooks, sync schedules, and consumer list with the ADRs.
- Update the system profile to record the new storage target and history.
- Notify all three consumers before decommissioning.

---

## Outcome Summary
| Direction | Before | After |
|---|---|---|
| North | No ADRs, unknown consumer | ADRs and complete dependency list |
| East | After-hours pages, single responder | Business-hours cut-over, two responders |
| South | Old scripts left in place | Old scripts removed, tending tracked |
| West | Plan variance 1.67 (unbalanced) | Plan variance 0.49 (balanced) |

---
**Related docs:** [Project README](../../README.md) · [Docs index](../README.md) · [Practices Guide](PRACTICES.md) · [Cultural Context](../CULTURAL_CONTEXT.md) · [Operational Manual](../specifications/OPERATIONAL_MANUAL.md) · [Sample Calls](../specifications/SAMPLE_CALLS.md) · [Templates](../README.md#templates)
