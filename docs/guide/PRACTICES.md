# Practices Guide: Applying the Framework to IT Projects

This guide turns the four engineering themes into team practices. Use it on any IT project, with or without the Python tooling. Read [Cultural Context](../CULTURAL_CONTEXT.md) first.

Each direction lists **questions to ask**, **practices**, **signals** to watch, and the matching **tooling**.

---

## North: Historical Records and Baselines
Understand what exists and why before you change it.

**Questions**
- What does this system do today, and who depends on it?
- What decisions shaped it, and are those reasons still valid?
- What history is lost if we replace it?

**Practices**
- Record decisions as ADRs (see [docs/adr](../adr/)).
- Keep a system profile per service: owner, dependencies, criticality, history notes.
- Onboard new members with the system's history, not just its current state.
- When retiring a system, archive its knowledge (runbooks, data records, lessons learned).

**Signals**
- Changes planned without reading existing ADRs or runbooks.
- Dependencies discovered only after an incident.

**Tooling**: `RecordRegistry`, `HistoricalRecordBuffer`.

---

## East: Interdependence and Variance
Watch how changes and load move across systems and people.

**Questions**
- Who and what else is affected when this system spikes or fails?
- Is this spike normal for this system's history?
- Is the on-call team absorbing the cost?

**Practices**
- Alert on deviation from a rolling baseline, not only on fixed limits.
- Review on-call load and toil each sprint using the [team load check](../templates/team-load-check.md).
- Map downstream consumers for every service.

**Signals**
- Recurring after-hours pages for the same cause.
- Throughput targets met while team load keeps rising.

**Tooling**: `TelemetrySpikeDetector`, `AlertClassifier`, `recip scan`.

---

## South: Continuous Tending
Give back to the platform as you take from it.

**Questions**
- For every feature added, what upkeep did we also do?
- Is maintenance work planned, or only done after incidents?

**Practices**
- Reserve a fixed share of each sprint for tending: refactoring, dependency updates, removing dead code, improving docs.
- Track the Tending Ratio over time in advisory mode (`recip tend`).
- Treat deletion of unused code and features as valued work.

**Signals**
- Tending Ratio falling sprint over sprint.
- Growing backlog of "we'll clean it up later" items.

**Tooling**: `DebtBroker`, `recip tend`.

---

## West: Relational Governance
Review changes for their effect on everything they touch, not only on delivery goals.

**Questions**
- Does this change trade one dimension (speed) for another (team load, knowledge)?
- Were the people affected by this change part of the review?
- Is knowledge about this change shared, or held by one person?

**Practices**
- Use the [design review checklist](../templates/design-review-checklist.md) for significant changes.
- Score the four dimensions (integrity, team load, overhead, knowledge equity) and discuss high variance before approval.
- Include operations, support, and end-user representatives in reviews.

**Signals**
- Reviews that only discuss the happy path and delivery date.
- Single points of knowledge on critical systems.

**Tooling**: `WebworkAssessor`.

---

## Project Lifecycle at a Glance

| Phase | North | East | South | West |
|---|---|---|---|---|
| Intake | Profile existing systems | Identify affected teams | Estimate upkeep cost | Define reviewers |
| Design | Write ADRs | Map dependencies | Plan tending budget | Run design review |
| Build | Record decisions | Baseline telemetry | Track Tending Ratio | Peer review |
| Operate | Update profiles | Review team load | Schedule tending | Revisit scores |
| Retire | Archive knowledge | Notify consumers | Remove cleanly | Close out review |

## Templates
- [Project charter](../templates/project-charter.md)
- [Design review checklist](../templates/design-review-checklist.md)
- [Retrospective](../templates/retrospective.md)
- [Team load check](../templates/team-load-check.md)

See the [worked example](WORKED_EXAMPLE.md) for a full walk-through.

---
**Related docs:** [Project README](../../README.md) · [Docs index](../README.md) · [Cultural Context](../CULTURAL_CONTEXT.md) · [Worked Example](WORKED_EXAMPLE.md) · [Operational Manual](../specifications/OPERATIONAL_MANUAL.md) · [Sample Calls](../specifications/SAMPLE_CALLS.md) · [ADRs](../README.md#architecture-decision-records)
