# Design Review Checklist

**Change:**
**Reviewers:**
**Date:**

## North: Records
- [ ] Existing ADRs and system profiles reviewed.
- [ ] Dependencies (upstream and downstream) listed.
- [ ] Anything being removed has its knowledge archived.

## East: Interdependence
- [ ] Affected teams and consumers notified.
- [ ] Telemetry baseline exists for affected services.
- [ ] On-call impact estimated.

## South: Tending
- [ ] Upkeep included (tests, docs, removal of replaced code).
- [ ] New debt recorded with an owner.

## West: Balance
Score each dimension from 0 to 5 as a group.

| Dimension | Score | Notes |
|---|---|---|
| System integrity (higher is better) | | |
| Operational burnout / team load (lower is better) | | |
| Resource overhead (lower is better) | | |
| Knowledge equity (higher is better) | | |

Check balance with `WebworkAssessor().is_balanced(...)`, or by discussion. If one dimension is far from the others, agree on a mitigation before approval.

- [ ] People affected by the change took part in the review.
- [ ] Knowledge is shared beyond one person.

## Decision
- [ ] Approved
- [ ] Approved with mitigations:
- [ ] Revisit on:

---
**Other templates:** [Project Charter](project-charter.md) · [Retrospective](retrospective.md) · [Team Load Check](team-load-check.md)  
**Related docs:** [Project README](../../README.md) · [Docs index](../README.md) · [Practices Guide](../guide/PRACTICES.md) · [Worked Example](../guide/WORKED_EXAMPLE.md) · [Cultural Context](../CULTURAL_CONTEXT.md)
