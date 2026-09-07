# CR-BP-15-IMP Phase 6: Specialization machinery (machinery-only)

## Summary

The **BP-SEM-013 specialization-relationship validation rule** is
now live, but **zero `specializes` relationships are introduced**
on the canonical 18 records. Phase 6 is machinery-only.

This is the eighth CR-BP-15-IMP delivery. The disposition register
records `phase6_status` with `specializations_introduced: 0` and
`validation_mode: machinery-only`, with full rationale documented
inline.

## Why "machinery-only"

CR-BP-14 §23 distinguishes specialization (cardinality fan-out
under a controlled pattern like `by-customer-segment`,
`by-region`, `by-product-line`) from decomposition (sequential
work within a single context, using `composes`).

Every candidate pair examined in Phase 6 planning is decomposition:

1. `customer-journey-design` ↔ `customer-experience-design` (cd-d):
   the journey is articulated after the experience is designed;
   this is sequential work in the same context, not cardinality
   fan-out.
2. `design-policies-and-controls` ↔ `design-governance-system`
   (ge-d): the policies are designed after the governance system;
   sequential work.
3. `market-and-demand-conception` ↔ `customer-strategy-conception`
   (cd-c): market intelligence precedes strategy commitment;
   sequential work.

None of these are cardinality fan-out. Adding `specializes`
relationships to them would be a **semantic bug** — downstream
tooling (CR-BP-12 L1 group composition; CR-BP-16 conformance gate)
would treat the child as a refinement under a controlled pattern
instead of as a constituent part of the parent.

The CR-BP-14 §24 admission freeze also prevents new admission
tranches that would introduce clean fan-out candidates (e.g.,
`manage-enterprise-customer` specializing
`manage-customer-relationship` under `by-customer-segment`).

**The reversible, scope-minimal path**: introduce the machinery
now so that future admission tranches with strong-evidence
specializations are evaluated against the canonical rules. This
is Path A from the planning clarification.

## What this PR does

### New validation rule

- `scripts/check_process_semantics.py` (modified):
  - **BP-SEM-013** validates `relationships[]` entries with
    `relationship_type: specializes`. A valid specializes
    relationship MUST:
    - target a canonical Process entry;
    - carry a `specialization_pattern` from the approved basis
      vocabulary or a non-empty `specialization_basis` field;
    - resolve to an existing Process entry.
  - Module docstring updated to document BP-SEM-013 alongside
    BP-SEM-001..012.
  - Self-test extended: broken fixture carries an unresolved
    specializes target (must fail); fixed fixture carries a
    valid specializes with approved basis (must pass).
  - `broken-blocking` count went from 5 to 6 (BP-SEM-013 added).

### Tests

- `tests/test_check_process_semantics.py`:
  - New `test_bp_sem_013_rejects_unresolved_specializes_target`:
    confirms BP-SEM-013 fires on an unknown target.
  - New `test_bp_sem_013_accepts_valid_specializes`: confirms
    BP-SEM-013 passes on a valid canonical fan-out with approved
    basis (`by-customer-segment`) and a real parent
    (`dea:process-customer-experience-design`).
  - Parametrized rule-coverage test extended for BP-SEM-013.

### Disposition register

- `reconciliation/dispositions/register.yaml`: `phase6_status`
  block added; `specializations_introduced: 0`,
  `bp_sem_013_rule_added: true`, `validation_mode:
  machinery-only`, with `decision_basis` documented inline.

## What this PR does NOT do

- No `specializes` relationships introduced on any of the 18
  canonical Business Process records.
- No specializations to Process Groups (Process Groups are
  catalog-owned L1 conceptual containers, not Business Processes;
  specialization does not apply).
- The §24 admission freeze remains in effect; new Business
  Process admission tranches stay paused.

## Verification

- `pytest tests/ -q`: 109 passed (106 prior + 2 new BP-SEM-013
  tests + 1 parametrized rule-coverage entry).
- BP-SEM `--strict`: **CONFORMANT** (0 errors, 0 warnings).
- BP-SEM `--self-test`: PASS (broken-blocking=6, fixed-blocking=0).
- Dispositions validator: PASS.
- `regenerate_catalog.py --check`: OK locally AND in a fresh
  clone of this branch (mtime trap guard).
- Dash-clean: zero en/em dashes in added lines.

## Programme position

- CR-BP-14: **Implemented** end-to-end.
- CR-BP-15 + CR-BP-15-IMP: this PR is the eighth CR-BP-15-IMP
  delivery. The disposition register is LOCKED at 18/18 (Phase 5
  closure); the BP-SEM-013 machinery is live and will evaluate
  the first strong-evidence specialization that arrives after
  the §24 admission freeze lifts.
- Next: **PR-11 (CR-BP-15-IMP Phase 7: pre-admission readiness)**
  or **CR-BP-16 conformance gate** (the permanent CI control that
  wires BP-SEM-001..013 into the admission freeze / release
  pipeline). The §24 freeze is the gating event for Phase 7.