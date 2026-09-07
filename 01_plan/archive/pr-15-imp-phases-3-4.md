# CR-BP-15-IMP Phase 3-4: Disposition register + tranche plan

## Summary

CR-BP-15 §28 (the nine dispositions) is now formalised; the 18
Business Processes in the canonical catalogue each receive a
preliminary RECLASSIFY disposition. The 18 records are grouped
into 10 tranches (one per Process Context) so future
CR-BP-15-IMP Phases 5-7 migrations are sequenced.

No schema, validator, or entity changes. The CR-BP-14 §24
admission freeze remains in effect; this PR is the third
CR-BP-15-IMP delivery and the first **decision-bearing** one.

## What this PR does

### Phase 3: disposition schema + register

- `reconciliation/dispositions/schema.yaml`: canonical schema for
  the nine dispositions (RETAIN, RECLASSIFY, RENAME, SPECIALIZE,
  MERGE, SPLIT, MOVE, DEFER, RETIRE); each disposition declares
  required/optional fields, target_id requirement, and rationale
  pattern. The `reclassify_axes` block documents the CR-BP-14 §17
  migration mapping and the approved specialization bases.
- `reconciliation/dispositions/register.yaml`: 18 disposition
  entries (one per Business Process). All 18 are PRELIMINARY
  RECLASSIFY because every record carries the documented legacy
  fields:
  1. legacy `process_intent` (operational / support / management)
     migrates to canonical (govern / manage / operate / deliver /
     support / develop / transform) per CR-BP-14 §17 evidence-based
     mapping;
  2. legacy scalar `process_context` migrates to the canonical
     `context:` block per CR-BP-14 §13, §20;
  3. legacy `process_audience` is removed because the canonical
     `context:` block already declares the ECF Domain x Lifecycle
     placement;
  4. `process_specialization` remains absent for these 18 records;
     CR-BP-15-IMP Phase 6 will introduce specializations where
     the catalogue narrative supports them.
  Each entry carries rationale + evidence + tranche assignment.

### Phase 4: tranche plan

- `reconciliation/tranches/plan.yaml`: 10 tranches (one per
  Process Context). Two flagged high-risk:
  - `ge-b` (governance / build): audience-vs-context contradiction
    on two records (13b generator artifact); resolved by the
    canonical `context:` block.
  - `ge-op` (governance / operate): cross-tranche reference to
    `ge-b` and `ge-c` via `dea:process-audit-policy-compliance`;
    must be reviewed against the governance register before
    merge.
- Tranches are independent; migration order MAY be interleaved or
  parallelised. Each tranche maps to one PR in the Phase 5-7
  roadmap (PR-6..9). Review checkpoints recorded (CR-BP-15 §7
  governance gate).

### Phase 3-4 validator

- `scripts/check_dispositions.py` validates the disposition
  register + tranche plan against:
  - the inventory (every record has exactly one disposition
    entry);
  - the disposition schema (every disposition id is canonical;
    per-disposition required fields are present);
  - the CR-BP-14 canonical vocabularies (every RECLASSIFY intent
    target is canonical; every RECLASSIFY context target resolves
    to a registered Process Context);
  - the tranche plan (every plan entry references a disposition
    entry).
- Self-test exercises 6 failure paths (invalid disposition id,
  RECLASSIFY w/o changes, non-canonical intent target, non-pc
  context target, missing inventory record, missing disposition
  entry).

### Documentation

- `reconciliation/README.md`: orientation block extended to
  describe Phases 3-4 layout and Phase 5-7 roadmap.
- `CHANGELOG.md`: Phase 3-4 entry.

## What this PR does NOT do

- No schema, validator, or entity changes.
- No migration of existing entries (Phase 5-7 scope; PR-6..9).
- The register is **PRELIMINARY**; it will be LOCKED during
  Phase 5 once each tranche's owner signs off.

## Verification

- `pytest tests/ -q`: 97 passed (88 prior + 9 new).
- All sibling validators PASS (BP-SEM records the documented
  legacy findings as advisory; the disposition validator PASSes
  on the live register + plan).
- `build_inventory.py --self-test --strict`: PASS.
- `check_dispositions.py --self-test`: PASS.
- `regenerate_catalog.py --check`: OK locally AND in a fresh
  clone of this branch (mtime trap guard).
- Dash-clean: zero en/em dashes in added lines.

## Programme position

- CR-BP-14: **Implemented** (PRs #26, #28, #29, #30).
- CR-BP-15 + CR-BP-15-IMP: **Proposed**; this PR is the third
  CR-BP-15-IMP delivery (after PR-31 inventory + baseline + STRUCT
  in Phase 1-2).
- Next: **PR-6..9 (CR-BP-15-IMP Phases 5-7)**: per-tranche
  migrations in 10 Process Contexts, locking the register and
  producing per-tranche diffs.
