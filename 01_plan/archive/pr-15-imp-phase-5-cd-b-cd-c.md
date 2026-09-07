# CR-BP-15-IMP Phase 5 first tranche (cd-b + cd-c)

## Summary

The first two customer-demand tranches (4 records: 2 build + 2
conceive) have been reconciled to the CR-BP-14 canonical contract.
The disposition register is now PARTIALLY_LOCKED with 4 records
locked. BP-SEM live verdict: **14 errors (down from 18)**.

This is the **first Phase 5 tranche migration** and the fourth
CR-BP-15-IMP delivery. PR-7..9 will cover cd-d + cd-im + cd-op,
the four ge-* tranches (with audience-vs-context resolution), and
the remaining customer-demand improvements.

## What this PR does

### Records migrated (4)

**cd-b (customer-demand / build):**
- `dea:process-customer-channel-and-acquisition-build`: legacy
  `operational` intent -> canonical `operate`; legacy scalar
  `process_context: dea:pc-cd-b` -> canonical
  `context: [{ref: dea:pc-cd-b}]` block; legacy
  `process_audience: customer-demand` removed; canonical `serves`
  relationship toward `ecf:customerAndDemand.build` added;
  change_history entry appended.
- `dea:process-demand-generation-build`: same migration as the
  cd-b peer.

**cd-c (customer-demand / conceive):**
- `dea:process-customer-strategy-conception`: legacy `management`
  intent -> canonical `develop`; cd-c context; serves toward
  `ecf:customerAndDemand.conceive`.
- `dea:process-market-and-demand-conception`: same migration as
  the cd-c peer.

### Audit trail

- `reconciliation/diffs/phase-5-cd-b-cd-c.yaml` (new): per-tranche
  audit trail; 4 records touched; SHA-256 evolution recorded;
  cross-tranche observations.
- `reconciliation/dispositions/register.yaml`:
  register_status -> PARTIALLY_LOCKED;
  register_lock_progress records 4 locked records and 14
  remaining.

### Schema relaxation

- `schemas/entity.schema.json`: `process_audience` removed from
  the `required` list; the legacy field remains readable as a
  backward-compat alias (CR-BP-14 /19) but is no longer required
  for canonical entries.

### Reproducible migration tooling

- `scripts/apply_phase_5_tranche.py` (new): reproducible tranche
  migration script; supports `--self-test` (idempotence contract)
  and `--tranche <id>` for any of the 10 tranches; applies the
  full migration pattern (intent, audience removal, context block,
  serves relationship, change_history append).

### Tests

- `tests/test_apply_phase_5_tranche.py` (new): 8 tests covering
  the migration script + per-record shape + idempotence + lock
  progress.
- `tests/test_reconciliation_baseline.py`: legacy_findings_present
  test updated to reflect the Phase 5 first-tranche lock (14
  remaining, not 18).

## What this PR does NOT do

- No changes to the 14 records in the cd-d, cd-im, cd-op, ge-*,
  or higher tranches (next PR-7..9).
- No specializations introduced (Phase 6 scope).
- The §24 admission freeze remains in effect; new Business
  Process admission tranches stay paused.

## Verification

- `pytest tests/ -q`: 105 passed (97 prior + 8 new).
- All sibling validators PASS (BP-SEM records the 14 remaining
  legacy findings as advisory per §24 freeze; disposition
  validator PASSes on the locked register).
- `apply_phase_5_tranche.py --self-test`: PASS (idempotence
  contract).
- `regenerate_catalog.py --check`: OK locally AND in a fresh
  clone of this branch (mtime trap guard).
- Dash-clean: zero en/em dashes in added lines.

## Programme position

- CR-BP-14: **Implemented**.
- CR-BP-15 + CR-BP-15-IMP: **Proposed**; this PR is the fourth
  CR-BP-15-IMP delivery and the first Phase 5 tranche migration.
- Locked: 4 records (cd-b + cd-c). Remaining: 14 records across
  cd-d, cd-im, cd-op, ge-b, ge-c, ge-d, ge-im, ge-op.
- Next: **PR-7 (CR-BP-15-IMP Phase 5 second tranche: cd-d +
  cd-im + cd-op)** — 5 customer-demand records; one carries a
  typo in its `process_context` scalar that the disposition
  register records as a target correction. Then **PR-8
  (Phase 5 third tranche: ge-b + ge-c + ge-d + ge-im)** —
  audience-vs-context migration for 7 governance records. Then
  **PR-9 (Phase 5 fourth tranche: ge-op)** — the cross-tranche
  audit-policy record.
