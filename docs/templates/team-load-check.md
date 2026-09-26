# Team Load Check

A short, anonymous check-in that gives the `operational_burnout` value (0–5) used by `recip scan --burnout` and the design review.

## Rules
- **Anonymous.** Do not record names.
- **Aggregate only.** Report the team average and spread, never individual answers.
- **Minimum group size.** Do not report results for groups smaller than 4 people.
- **Transparent.** Tell the team what is collected, why, and who sees it.
- **Not for performance reviews.** Use results only to plan workload.

## Questions
Answer each from 0 (not at all) to 5 (constantly).

1. How often did work spill into evenings or weekends?
2. How often were you interrupted by pages or urgent requests?
3. How much of your time went to repetitive manual work (toil)?
4. How often did you lack the context or knowledge to finish work confidently?
5. How sustainable does your current workload feel? (0 = very sustainable, 5 = not sustainable)

## Scoring
- Team score = average of all answers from all respondents.
- Pass the team score to the tooling:
  ```bash
  recip scan --system my-service --burnout 2.8
  ```
- Values at or above `3.5` mark the footprint as unbalanced.

## Follow-Up
Discuss the score in the [retrospective](retrospective.md). Agree on one concrete action, such as automating a toil task, rotating on-call, or pairing to spread knowledge.

---
**Other templates:** [Project Charter](project-charter.md) · [Design Review Checklist](design-review-checklist.md) · [Retrospective](retrospective.md)  
**Related docs:** [Project README](../../README.md) · [Docs index](../README.md) · [Practices Guide](../guide/PRACTICES.md) · [Cultural Context](../CULTURAL_CONTEXT.md) · [Sample Calls](../specifications/SAMPLE_CALLS.md)
