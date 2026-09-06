# CR-BP-14 Phase 1: Semantic vocabularies + schema

## Summary

Implements Phase 1 of CR-BP-14 (Process Semantic Reconciliation; landed
verbatim in PR #25): the semantic vocabularies and schema reconciliation
per CR-BP-14 §9, §10, §11, §17, §18, §20.

No existing entry is mutated; the 28 canonical entries continue to
validate unchanged. Legacy values remain readable throughout the
migration period.

## Deliverables

1. **`classifications/process-intents.yaml` (new)**: the seven-value
   purpose-oriented Process Intent vocabulary (§9.2): govern / manage /
   operate / deliver / support / develop / transform, each with the
   CR's definition. Includes the §17 legacy migration mapping
   (operational -> operate or deliver; support -> support; management ->
   manage or govern) with the evidence-based, never-mechanical rule, and
   the §11 / BP-SEM-011 note that token overlap with the classification
   vocabulary is lexical, not semantic.
2. **`schemas/entity.schema.json`**:
   - `process_intent` enum extended to the canonical seven values;
     legacy `operational` / `management` retained as deprecated migration
     aliases (§17, §20). Existing entries unchanged and valid.
   - New optional `process_classification` block (canonical form per
     §20) using the retained five-value landscape vocabulary.
   - `process_type` retained unchanged (§18); description now states it
     is the Process Classification (landscape position), not a synonym
     for intent, and that the `core` default is scheduled for review in
     CR-BP-15 (§18).
   - `process_audience` marked as legacy migration alias; not a
     substitute for Process Context (§13, §19).
3. **`schemas/contribution.schema.json`**: mirrors the same extensions
   (intent enum, `process_classification` block, alias descriptions).
4. **`classifications/process-types.yaml`**: header records the CR-BP-14
   §10 Process Classification semantics and the Intent != Classification
   rule. Vocabulary values unchanged.
5. **`scripts/check_process_specialization.py`**: BP-SPEC-01-007 text now
   quotes the extended intent vocabulary; the non-promotion rule is
   unchanged (`--self-test` PASS).
6. **`docs/classification.md`**: new "CR-BP-14 semantic reconciliation
   (Phase 1 status)" section carries the normative contract; pre-CR-BP-14
   prose retained and marked historical pending Phase 4 (§22).
7. **`contributions/processes/PROCESS-CONTRIBUTION-TEMPLATE.yaml`**:
   canonical intent vocabulary in the example, optional
   `process_classification` block shown.
8. **`tests/test_process_intents.py` (new, 9 tests)**: locks vocabulary
   exactness, definition presence, legacy-mapping coverage, entity /
   contribution schema mirror parity, classification-block shape, and
   the distinct-axes invariant.
9. **CHANGELOG.md** Unreleased entry; CR register and README change
   programme rows move CR-BP-14 to **Accepted** (implementation in
   progress).

## What this PR does NOT do

- No BP-SEM validators yet (Phase 3; BP-SEM-001..012).
- No `context:` block or contextual relationships yet (Phase 2;
  §13 target representation).
- No migration of existing entries (that is CR-BP-15 scope, informed by
  the Phase 5 assessment).
- No full documentation prose reconciliation (Phase 4; §22).
- The §24 admission freeze remains in effect.

## Verification

- `pytest tests/ -q`: 47 passed (38 existing + 9 new).
- Per-file schema dispatch over all 28 canonical entries + contexts
  against the updated schemas: 0 errors.
- `check_process_specialization.py --self-test`: PASS; live run PASS.
- All sibling validators PASS: check_ecf_conformance,
  check_legacy_migration, check_process_context, check_process_group,
  check_process_identity.
- `check_catalog_index.py --strict`: OK (28 entities).
- `regenerate_catalog.py --check`: CATALOG.yaml current (register status
  text does not affect the open-CR count; the counter reads CR files).
- Dash-clean: zero en/em dashes in added lines.

## Notes for reviewers

- Pre-existing, out of scope: the contribution template does not
  validate against the contribution schema even on main (placeholder
  `<github-handle>` fails the contributor pattern); the template is a
  fill-in document.
- Pre-existing, out of scope: some `docs/classification.md` "See also"
  links use `../../classifications/...` (one level too many); swept in
  Phase 4.
