# CR-BP-15-IMP Phase 5 fourth tranche (ge-op) + Phase 5 closure

## Summary

The final two governance-existence operate records have been
reconciled to the CR-BP-14 canonical contract. The disposition
register is now **LOCKED** (18/18). BP-SEM live verdict:
**0 errors, 0 warnings: CONFORMANT** for the first time since
CR-BP-14 S21 was introduced.

**This is the closure of the CR-BP-15-IMP Phase 5 loop.**
Future Phase 6 (specializations) work will operate against this
locked baseline.

## What this PR does

### Records migrated (2)

**ge-op (governance-existence / operate), 2 records:**
- `dea:process-audit-policy-compliance`: legacy `support`
  intent -> canonical `govern` (audit-and-oversight is
  governance activity per the disposition register rationale);
  audience-vs-context high-risk flag resolved by removing
  `process_audience` (canonical `context: [{ref: dea:pc-ge-op}]`
  replaces it); serves toward
  `ecf:governanceAndExistence.operate`.
- `dea:process-operate-governance-oversight`: legacy
  `management` intent -> canonical `operate`; same ge-op
  migration pattern.

### Data correction

- `contexts/v1-alpha/dea_pc-cd-op.yaml` ->
  `contexts/v1-alpha/dea-pc-cd-op.yaml` (filename typo fixed;
  canonical id `dea:pc-cd-op` was always correct inside the
  file). Updated 4 documentation references (CR-BP-03C,
  CR-BP-12, manage-customer-relationship.md, CHANGELOG). The
  BP-SEM-008 context-reference-integrity check now passes.

### Audit trail

- `reconciliation/diffs/phase-5-ge-op.yaml` (new): per-tranche
  audit trail; 2 records touched; closure observations on the
  audience-vs-context resolution and the filename correction.
- `reconciliation/dispositions/register.yaml`:
  register_status -> LOCKED; register_lock_progress records
  all 10 tranches and 18 locked records; 0 remaining.

### Conformance gate promotion

- `.github/workflows/ci.yml`: Process Semantics gate promoted
  from advisory (`--strict || true`) to **blocking**
  (`--strict`). Any future regression on the canonical
  CR-BP-14 contract is caught at PR time.

### Tests

- `tests/test_reconciliation_baseline.py`:
  legacy_findings_present test updated to reflect the all-locked
  state (0 remaining, not 2).
- `tests/test_apply_phase_5_tranche.py`: register_lock_progress
  test now asserts the LOCKED status of the disposition
  register and the 18-of-18 lock progress.
- `tests/test_check_process_semantics.py`: live `--strict` test
  updated to assert CONFORMANT on the post-Phase-5 catalogue.
  Added `test_strict_mode_fails_on_legacy_fixture` to lock
  the strict-mode machinery against a synthetic legacy-bearing
  sandbox (tmp_path-scoped; does not pollute the live tree).

## What this PR does NOT do

- No Phase 6 (specializations) work; the disposition register
  is LOCKED but the catalogue carries no `specializes`
  relationships yet. Phase 6 is the next programme deliverable.
- The /24 admission freeze remains in effect; new Business
  Process admission tranches stay paused until CR-BP-16
  confirms the conformance gate.

## Verification

- `pytest tests/ -q`: 106 passed (all prior tests + 1 new
  fixture test).
- All sibling validators PASS:
  - BP-SEM `--strict`: **CONFORMANT** (0 errors, 0 warnings).
  - Dispositions: PASS on the LOCKED register.
  - STRUCT: PASS on the renamed file.
  - Legacy migration: PASS (relationship-type allowed set
    includes `serves` + `contributes-to` from PR-33).
- `apply_phase_5_tranche.py --self-test`: PASS (idempotence
  contract).
- `regenerate_catalog.py --check`: OK locally AND in a fresh
  clone of this branch (mtime trap guard).
- Dash-clean: zero en/em dashes in added lines.

## Programme position

- CR-BP-14: **Implemented** end-to-end.
- CR-BP-15 + CR-BP-15-IMP: this PR is the seventh
  CR-BP-15-IMP delivery. The Phase 5 loop is closed; the
  disposition register is LOCKED at 18/18.
- **Closure of the CR-BP-15-IMP Phase 5 loop** (PR-9 is the
  final tranche of Phase 5).
- Next: **PR-10 (CR-BP-15-IMP Phase 6: specialization
  introduction)**; the disposition register records no
  SPECIALIZE dispositions today, so the Phase 6 work begins
  from a clean slate against the LOCKED Phase 5 baseline.
  Phase 6 will introduce `specializes` relationships for
  records where the CR-BP-14 /23 specialization narrative
  applies (e.g., cd-d candidates that may specialize
  `design-customer-experience`).