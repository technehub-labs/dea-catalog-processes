# CR-BP-14 Phase 3: BP-SEM-001..012 Process Semantics gate

## Summary

Implements Phase 3 of CR-BP-14 (§21): the BP-SEM validator family
(001..012), its `--self-test`, its CI wiring, and its accompanying
unit tests.

This is the validator layer that CR-BP-15-IMP will consult when it
reconciles the existing canonical population (Phases 4..12); CR-BP-16
absorbs the same family into the permanent conformance gate.

## What this PR does

1. **`scripts/check_process_semantics.py` (new, 515 lines)**:
   - BP-SEM-001 Intent Vocabulary; BP-SEM-002 Classification Vocabulary;
     BP-SEM-003/004 Intent/Classification Independence (by
     construction: no rule infers one dimension from the other);
     BP-SEM-005 Specialization Validity; BP-SEM-006 Specialization
     Differentiation; BP-SEM-007 Context Distinction (canonical
     `context:` block required; `process_audience` is never a
     substitute); BP-SEM-008 Context Reference Integrity; BP-SEM-009
     Identity Independence (by construction: the validator never
     asserts that intent/classification/context differences mandate
     distinct identities); BP-SEM-010 Legacy Detection (warning
     class); BP-SEM-011 Classification Collision (advisory); BP-SEM-012
     Context Multiplicity (advisory).
   - Every finding carries a deterministic `rule:<code>` prefix so
     callers and the self-test can extract the rule without parsing
     prose.
   - `--self-test` exercises every BP-SEM rule on a broken fixture and
     asserts the fixed fixture is blocking-free with the expected
     advisory findings.
   - `--strict` promotes warnings to errors; default behaviour reports
     CONFORMANT / CONFORMANT-WITH-WARNINGS / NON-CONFORMANT.
   - L1 Process Group filter: the rules apply to L2 Business Process
     entries only (CR-BP-12 already establishes the type discriminator
     pattern).
2. **CI wiring** (`.github/workflows/ci.yml`): the validator runs as
   an advisory step between the legacy migration gate and the process
   group gate (`--strict || true`). This makes the findings visible
   without blocking the existing canonical population; the comment in
   the workflow explains the CR-BP-14 §24 admission freeze and
   references the programme plan that owns the reconciliation.
3. **`tests/test_check_process_semantics.py` (new, 16 tests)**:
   self-test passes; module docstring documents every BP-SEM rule;
   live run reports the expected verdict classes; `--strict` promotes
   findings.
4. **CHANGELOG** entry; register row notes Phase 3.

## Live findings (exactly the seed set)

The validator's first run against the current canonical population
finds:

- 18 BP-SEM-007 (canonical `context:` block missing on every entry)
- 18 BP-SEM-010 (legacy `process_intent`)
- 18 BP-SEM-010 (legacy scalar `process_context`)
- 18 BP-SEM-010 (legacy `process_audience`)

These are precisely the seed findings already recorded in the
CR-BP-14/15/16 programme plan (`PLAN.md`, seed_findings). CR-BP-15-IMP
Phases 8 (Intent migration), 9 (Classification reconciliation) and 10
(Audience migration) reduce them.

## What this PR does NOT do

- No existing entries are mutated.
- No schema changes.
- No documentation prose reconciliation (Phase 4; CR-BP-14 §22).
- The admission freeze remains in effect.

## Verification

- `pytest tests/ -q`: 79 passed (63 existing + 16 new).
- `scripts/check_process_semantics.py --self-test`: PASS.
- Live run reports CONFORMANT-WITH-WARNINGS / NON-CONFORMANT status
  with deterministic rule codes.
- All six sibling validators PASS (specialization incl. --self-test,
  identity, legacy migration, context, group, ECF conformance).
- `check_catalog_index.py --strict`: OK (28 entities).
- `regenerate_catalog.py --check`: OK locally AND in a fresh clone of
  this branch (mtime trap guard).
- Dash-clean: zero en/em dashes in added lines.