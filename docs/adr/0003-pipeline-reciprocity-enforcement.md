# Architectural Decision Record 0003: Pipeline Reciprocity Enforcement

## Status
Accepted

## Context
Code bases are often treated as open extraction pits where features are continuously harvested without maintaining technical debt.

## Decision
Continuous Integration loops will track file modifications to compute a Tending Ratio over a window of recent commits, excluding docs and tests by default. The check runs in advisory mode by default and blocks builds only when enforcement is explicitly enabled.

## Consequences
A per-commit ratio would block most legitimate feature work and invite gaming (e.g., padding deletions). Measuring over a window and starting in advisory mode keeps the signal useful without punishing normal growth.

---
**ADRs:** Previous: [0002](0002-modular-ecosystem-metrics.md) · Next: [0004](0004-algorithmic-governance.md) · [All ADRs](../README.md#architecture-decision-records)  
**Related docs:** [Project README](../../README.md) · [Docs index](../README.md) · [Operational Manual](../specifications/OPERATIONAL_MANUAL.md) · [Practices Guide](../guide/PRACTICES.md) · [Sample Calls](../specifications/SAMPLE_CALLS.md)
