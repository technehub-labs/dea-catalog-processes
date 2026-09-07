# CR-BP-15-IMP Phase 7: Pre-admission readiness (BP-AR gate + conformance report)

## Summary

The **permanent CR-BP-16 conformance gate machinery** is now live:
- The **seven architectural regression patterns** (BP-AR-001..007) from
  CR-BP-16 §21 are running as a **blocking CI gate**.
- The **per-record conformance report** (CR-BP-16 §23/24 Levels 1-4)
  is generated on every PR.

The catalogue is **38/38 at Level 4 (Canonically Conformant)**.

## Why "pre-admission readiness"

CR-BP-15-IMP Phases 1-6 established the canonical population
(28 entities + 10 contexts = 38 records, LOCKED at the
disposition register) and the BP-SEM-001..013 validation
rules. The §24 admission freeze remains in effect until
CR-BP-13A / CR-BP-13B admission tranches are ready.

Phase 7 is the **pre-flight work** that ensures the catalogue
won't drift when admission resumes:

1. **Architectural regression detection** (§21) — catches the
   seven forbidden conflations that the introduction of new
   records could re-introduce. This is the **first permanent
   gate** from CR-BP-16.
2. **Conformance report** (§23/24) — the per-record Level 1-4
   grading that becomes the **objective scorecard** for
   admission readiness. When a new admission tranche lands,
   its Level 4 status must be verified against this report.

Together, these two artefacts close the readiness loop opened
by Phase 1-6. The §24 freeze can now be lifted as soon as
CR-BP-13A / CR-BP-13B are ready, because any architectural
regression introduced by an admission PR will be caught at
PR time by the BP-AR gate.

## What this PR does

### Architectural regression detection

- `scripts/check_architectural_regression.py` (new, 240 lines):
  - **BP-AR-001**: Business Process != Process Kernel
  - **BP-AR-002**: ECF Coordinate != Business Process
  - **BP-AR-003**: Process Group != Business Function
  - **BP-AR-004**: Capability != Process
  - **BP-AR-005**: Audience != Context (also catches
    reintroduction of legacy `process_audience` scalar)
  - **BP-AR-006**: Intent != Classification (also scans
    `specialization_pattern` / `specialization_basis`)
  - **BP-AR-007**: Specialization != Decomposition (catches
    same-context `specializes` relationships)
  - Supports `--strict`, `--json`, `--self-test`. The self-test
    exercises 5 of 7 patterns via fixtures; BP-AR-003 and
    BP-AR-004 are field-level rules that don't surface in the
    canonical data structure (no `business_function` or
    `capability` fields exist).

### Conformance report

- `scripts/build_conformance_report.py` (new, 180 lines):
  Generates `reconciliation/conformance_report.yaml` from the
  live catalogue. Each record is assigned a Level:
  - **Level 0**: Unassessed
  - **Level 1**: Structurally Conformant (schema + references)
  - **Level 2**: Semantically Conformant (BP-SEM clean)
  - **Level 3**: Architecturally Conformant (BP-AR clean)
  - **Level 4**: Canonically Conformant (evidence + governance)
  Supports `--check` to assert the report is up to date.
- `reconciliation/conformance_report.yaml` (new, generated):
  38 records, all Level 4.

### CI

- `.github/workflows/ci.yml`: new "Run architectural regression
  gate" step (blocking); new "Refresh conformance report" step
  (advisory). CI now runs BP-AR + report refresh on every PR.

### Tests

- `tests/test_architectural_regression.py` (new, 110 lines):
  7 tests covering self-test, live conformance, JSON shape,
  canonical-bad fixture rejection, and report invariants.

## What this PR does NOT do

- Does NOT implement the full 22-section CR-BP-16 conformance
  gate (this PR covers §21 + §23/24 specifically; the remaining
  sections will land in CR-BP-16 PRs).
- Does NOT lift the §24 admission freeze (that requires
  CR-BP-13A / CR-BP-13B admission tranches to be ready).
- Does NOT introduce any new records (the 38 canonical records
  remain the entire population).

## Verification

- `pytest tests/ -q`: **116 passed** (109 prior + 7 new for
  BP-AR + conformance report).
- BP-SEM `--strict`: **CONFORMANT** (0 errors, 0 warnings).
- BP-AR `--strict`: **CONFORMANT** (no architectural
  regressions detected).
- `build_conformance_report.py`: Levels {0:0, 1:0, 2:0, 3:0, 4:38}.
- `build_conformance_report.py --check`: OK.
- `regenerate_catalog.py --check`: OK locally AND in a fresh
  clone of this branch (mtime trap guard).
- Dash-clean: zero en/em dashes in added lines.

## Programme position

- CR-BP-14: **Implemented** end-to-end.
- CR-BP-15 + CR-BP-15-IMP: Phases 1-7 shipped; this is the
  ninth CR-BP-15-IMP delivery.
- CR-BP-16: §21 + §23/24 machinery is now live in CI. The
  remaining sections (§17 CI pipeline ordering, §19 blocking
  conditions beyond BP-SEM/BP-AR, §22 documentation
  conformance, §25 continuous conformance) will land in
  CR-BP-16 implementation PRs after the §24 freeze lifts.
- Next: **CR-BP-13A admission tranche** (customer + demand
  L1 admission) or **CR-BP-16 full conformance gate** PRs.
  Awaiting user direction.