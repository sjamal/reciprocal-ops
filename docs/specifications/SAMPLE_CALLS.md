# Verification Reference & Testing Guidelines

### Running the Operational Validation Suite
To execute all codified compliance modules, run the testing engine out of your terminal:
```bash
pytest -v
```

### Testing Specific Modules Independently
If you want to run validations targeting only the pluggable stream layers or the evolution loops:
```bash
# Execute telemetry hydrator verification only
pytest tests/test_hydrator.py -v

# Execute multi-agent resilience simulation tests only
pytest tests/test_evolution_engine.py -v
```

### Script Execution Verification via Module Path
To verify your project layout builds paths dynamically, execute the internal entry structures via python's module runtime environment:
```bash
python3 -m reciprocal_ops.cli
```

### CLI Examples
```bash
# Scan with synthetic telemetry; burnout is a team-level anonymous score (0-5)
recip scan --system my-service --burnout 2.5

# Force a spike to see alert classification change
recip scan --system my-service --burnout 4.0 --force-spike

# Ingest an external JSON payload
recip scan --system my-service --from-json sample_webhook_payload.json

# Tending Ratio over the last 50 commits (advisory, always exits 0)
recip tend --window 50

# Enforce a target in CI (exits 1 when below target)
recip tend --window 100 --ratio 0.5 --enforce
```

---
**Related docs:** [Project README](../../README.md) · [Docs index](../README.md) · [Operational Manual](OPERATIONAL_MANUAL.md) · [Practices Guide](../guide/PRACTICES.md) · [Worked Example](../guide/WORKED_EXAMPLE.md) · [Contributing](../../CONTRIBUTING.md)
