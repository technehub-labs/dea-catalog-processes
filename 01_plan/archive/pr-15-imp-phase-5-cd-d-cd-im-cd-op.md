# CR-BP-15-IMP Phase 5 second tranche (cd-d + cd-im + cd-op)

## Summary

Five additional customer-demand records have been reconciled to
the CR-BP-14 canonical contract. The disposition register is now
9-of-18 locked. BP-SEM live verdict: **9 errors (down from 14)**.

This is the **second Phase 5 tranche migration** and the fifth
CR-BP-15-IMP delivery. All 9 customer-demand records are now on
canonical form; only the 9 governance records remain.

## What this PR does

### Records migrated (5)

**cd-d (customer-demand / design), 3 records:**
- `dea:process-customer-experience-design`: legacy
  `management` intent -> canonical `develop`; cd-d context
  block; serves toward `ecf:customerAndDemand.design`.
- `dea:process-customer-journey-design`: legacy `support`
  intent -> canonical `develop`; cd-d block; same serves.
- `dea:process-demand-design`: legacy `management` intent
  -> canonical `develop`; cd-d block; same serves.

**cd-im (customer-demand / improve), 1 record:**
- `dea:process-customer-insight-and-retention`: legacy
  `management` intent -> canonical `operate` (Improve context
  work is operational per the disposition register rationale);
  cd-im block; serves toward `ecf:customerAndDemand.improve`.

**cd-op (customer-demand / operate), 1 record:**
- `dea:process-manage-customer-relationship`: legacy
  `management` intent -> canonical `manage` (cd-op work is
  relationship management); cd-op block; serves toward
  `ecf:customerAndDemand.operate`. The existing `realizes`
  capability relationship is preserved.

### Audit trail

- `reconciliation/diffs/phase-5-cd-d-cd-im-cd-op.yaml` (new):
  per-tranche audit trail; 5 records touched; SHA-256 evolution;
  cross-tranche observations on cd-d density (3 records sharing
  the same context) and the management-vs-manage intent
  disambiguation.
- `reconciliation/dispositions/register.yaml`: register_lock
  progress updated to 9 locked records (cd-b, cd-c, cd-d, cd-im,
  cd-op) and 9 remaining.

### Tests

- `tests/test_reconciliation_baseline.py`: legacy_findings_present
  test updated to reflect the second tranche lock (9 remaining,
  not 14).
- `tests/test_apply_phase_5_tranche.py`: register_lock_progress
  test expanded to cover the five customer-demand tranches.

## What this PR does NOT do

- No changes to the 9 records in the ge-* tranches
  (ge-b, ge-c, ge-d, ge-im, ge-op) — these are the audience-vs-
  context migration and cross-tranche audit-policy work,
  addressed by PR-8 (ge-b + ge-c + ge-d + ge-im) and PR-9
  (ge-op).
- No specializations introduced (Phase 6 scope).
- The /24 admission freeze remains in effect.

## Verification

- `pytest tests/ -q`: 105 passed (all prior tests + 8 new from
  PR-33 + 0 new from this PR; existing tests were updated to
  reflect the lock progress).
- All sibling validators PASS (BP-SEM records 9 remaining legacy
  findings as advisory per /24 freeze; disposition validator
  PASSes on the partially-locked register).
- `apply_phase_5_tranche.py --self-test`: PASS (idempotence
  contract).
- `regenerate_catalog.py --check`: OK locally AND in a fresh
  clone of this branch (mtime trap guard).
- Dash-clean: zero en/em dashes in added lines.

## Programme position

- CR-BP-14: **Implemented**.
- CR-BP-15 + CR-BP-15-IMP: **Proposed**; this PR is the fifth
  CR-BP-15-IMP delivery and the second Phase 5 tranche
  migration.
- Locked: 9 records (all 5 customer-demand tranches: cd-b,
  cd-c, cd-d, cd-im, cd-op). Remaining: 9 records across
  ge-b, ge-c, ge-d, ge-im, ge-op.
- Next: **PR-8 (CR-BP-15-IMP Phase 5 third tranche: ge-b +
  ge-c + ge-d + ge-im)** — 6 governance records; the audience-
  vs-context migration that flagged ge-b as high-risk in the
  Phase 4 tranche plan. Then **PR-9 (Phase 5 fourth tranche:
  ge-op)** — the cross-tranche audit-policy record.