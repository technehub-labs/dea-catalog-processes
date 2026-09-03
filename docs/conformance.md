# Conformance Summary

**CR-BP-03 §13.**

This document summarizes the conformance gates enforced by the
catalog. Each gate is implemented by a validator script under
`scripts/` and wired into the CI workflow.

## Gates

| Gate | Validator | Rules | Authority |
|---|---|---|---|
| ECF Conformance Gate | `scripts/check_ecf_conformance.py` | (CR-ECF-CG-001..004) | CR-ECF-CG-004 |
| Process Specialization Gate | `scripts/check_process_specialization.py` | BP-SPEC-01-001..007 | CR-BP-SPEC-BP-01 |
| Process Context Gate | `scripts/check_process_context.py` | PC-001..PC-008 | CR-BP-02 |
| Process Identity Gate | `scripts/check_process_identity.py` | BP-ARC-ID-001..005 | CR-BP-03 |
| Consumer Validator | `validate-against-model.yml@v0.6.0` (in `dea-architecture-framework`) | (consumer) | CR-AR-FMWK-01 |

## CI

The CI workflow `.github/workflows/ci.yml` runs the local gates
on every PR. The `.github/workflows/validate-allocation.yml`
workflow runs the consumer validator against the pinned
`dea-architecture-framework@v0.6.0`.

A new workflow `.github/workflows/process-contribution-report.yml`
(planned for a follow-on PR) runs the contribution report
generator on PRs that touch `contributions/processes/`.

## Validator self-tests

Every validator script in `scripts/` has a built-in `--self-test`
mode that exercises the rules on a deliberately broken catalog
and verifies the expected exit codes. The self-tests are
deterministic and run in CI.

## See also

- [`docs/architecture.md`](architecture.md)
- [`docs/classification.md`](classification.md)
- [`docs/identity.md`](identity.md)
- [`docs/relandscape.md`](relandscape.md)
- [`change-requests/CR-BP-03-business-process-architecture.md`](../../change-requests/CR-BP-03-business-process-architecture.md) §13
