# CR-BP-15-IMP Phase 5 third tranche (ge-b + ge-c + ge-d + ge-im)

## Summary

Seven governance records have been reconciled to the CR-BP-14
canonical contract. The disposition register is now 16-of-18
locked. BP-SEM live verdict: **2 errors (down from 9)**.

This is the **third Phase 5 tranche migration** and the sixth
CR-BP-15-IMP delivery. Only the 2 ge-op records remain, addressed
in PR-9 (Phase 5 fourth tranche).

## What this PR does

### Records migrated (7)

**ge-b (governance-existence / build), 2 records:**
- `dea:process-codify-charters-and-policies`: legacy
  `operational` intent -> canonical `operate`; ge-b context
  block; serves toward `ecf:governanceAndExistence.build`.
- `dea:process-establish-governance-bodies`: legacy
  `operational` intent -> canonical `operate`; same ge-b pattern.

**ge-c (governance-existence / conceive), 2 records:**
- `dea:process-develop-governance-strategy`: legacy
  `management` intent -> canonical `develop`; ge-c block;
  serves toward `ecf:governanceAndExistence.conceive`.
- `dea:process-initiate-policy-and-charter`: legacy
  `management` intent -> canonical `manage`; same ge-c
  pattern. The ge-c tranche demonstrates the most
  semantically diverse intent pair (develop + manage in
  the same context).

**ge-d (governance-existence / design), 2 records:**
- `dea:process-design-governance-system`: legacy
  `management` intent -> canonical `develop`; ge-d block;
  serves toward `ecf:governanceAndExistence.design`.
- `dea:process-design-policies-and-controls`: legacy
  `management` intent -> canonical `develop`; same ge-d
  pattern.

**ge-im (governance-existence / improve), 1 record:**
- `dea:process-review-governance-effectiveness`: legacy
  `management` intent -> canonical `govern`
  (review-and-correction is governance activity per the
  disposition register rationale); ge-im block; serves
  toward `ecf:governanceAndExistence.improve`.

### Audit trail

- `reconciliation/diffs/phase-5-ge-b-ge-c-ge-d-ge-im.yaml`
  (new): per-tranche audit trail; 7 records touched;
  cross-tranche observations on ge-c intent diversity,
  ge-d as L2 conceptual foundation, ge-im as single-record
  Improve context work.
- `reconciliation/dispositions/register.yaml`: register_lock
  progress updated to 16 locked records (cd-b, cd-c, cd-d,
  cd-im, cd-op, ge-b, ge-c, ge-d, ge-im) and 2 remaining.

### Tests

- `tests/test_reconciliation_baseline.py`: legacy_findings_present
  test updated to reflect the third tranche lock (2 remaining,
  not 9).
- `tests/test_apply_phase_5_tranche.py`: register_lock_progress
  test expanded to cover the four governance tranches.

## What this PR does NOT do

- No changes to the 2 ge-op records
  (`dea:process-operate-governance-oversight`,
  `dea:process-audit-policy-compliance`); these are addressed
  in PR-9 (Phase 5 fourth tranche: ge-op).
- No specializations introduced (Phase 6 scope).
- The /24 admission freeze remains in effect.

## Verification

- `pytest tests/ -q`: 105 passed (all prior tests + 0 new from
  this PR; existing tests were updated to reflect the lock
  progress).
- All sibling validators PASS (BP-SEM records 2 remaining legacy
  findings as advisory per /24 freeze; disposition validator
  PASSes on the partially-locked register).
- `apply_phase_5_tranche.py --self-test`: PASS (idempotence
  contract).
- `regenerate_catalog.py --check`: OK locally AND in a fresh
  clone of this branch (mtime trap guard).
- Dash-clean: zero en/em dashes in added lines.

## Programme position

- CR-BP-14: **Implemented**.
- CR-BP-15 + CR-BP-15-IMP: **Proposed**; this PR is the sixth
  CR-BP-15-IMP delivery and the third Phase 5 tranche
  migration.
- Locked: 16 records (9 customer-demand + 7 governance, all
  except ge-op). Remaining: 2 records in ge-op
  (`operate-governance-oversight`, `audit-policy-compliance`).
- Next: **PR-9 (CR-BP-15-IMP Phase 5 fourth tranche: ge-op)**,
  the final Phase 5 tranche; closes the Phase 5 loop and brings
  the disposition register to LOCKED status (18/18).