# CR-BP-14 Phase 4: Documentation reconciliation (Implementation)

## Summary

Closes CR-BP-14 §22 (Documentation Reconciliation) and moves CR-BP-14
to **Implemented**. The repository prose reflects the CR-BP-14
semantic contract; legacy vocabulary references are reconciled to
the canonical forms or marked historical; no superseded semantic
contract remains presented as normative.

No schema, validator or entity changes. No existing entry is mutated.

## What this PR does

- `docs/architecture.md`: orientation block pointing at the semantic
  constitution and the governance programme; L0/L1/L2 narratives
  rewritten to the CR-BP-14 §6 / §7 definitions; Process Group
  confirmed as catalog-owned, not a metamodel entity; See-also
  expanded; broken `../../` link defects swept (the pre-existing link
  defect noted in PR #28's body).
- `docs/identity.md`: CR-BP-14 §15 identity-independence clause
  added; BP-ARC-ID-004 cross-check note clarifies its distinction
  from BP-SEM-003/004 (the validator-level identity-independence
  rule); broken `../../` link defect swept.
- `docs/classification.md`: front matter records the CR-BP-14 §10 /
  §11 formal separation; the canonical
  `classifications/process-intents.yaml` link is now correct
  (broken-link defect swept); See-also expanded.
- `docs/relandscape.md`: See-also expanded with the semantic-contract
  document and the BP-SEM validator; CR-BP-14 §24 admission-freeze
  reference added; broken `../../` link defect swept.
- `docs/context.md` (new): Process Context as canonical placement
  (CR-BP-14 §5, §13, §20); the canonical `context:` block; the
  multiplicity rule (BP-SEM-012); relationship to BP-SEM-007 and
  BP-SEM-008.
- `docs/specialization.md` (new): specialization as semantic
  refinement (CR-BP-14 §12); approved specialization bases;
  specialization vs decomposition; canonical form; identity
  independence (BP-SEM-009).
- `README.md` §2 (Process Architecture): the four-axes table is
  replaced with the CR-BP-14 axes (Intent / Classification /
  Specialization / Context); the obsolete `Audience` axis is replaced
  by the canonical `context:` block; §8 No Breaking Changes explains
  the migration-period field aliasing and references the BP-SEM
  validator.
- Register: CR-BP-14 -> **Implemented** (Phase 4 closes the
  constitutional phase).
- CHANGELOG entry.

## What this PR does NOT do

- No schema, validator, or entity changes.
- No migration of existing entries (CR-BP-15-IMP scope).
- The §24 admission freeze remains in effect; the BP-SEM validator
  records legacy findings on the existing population for CR-BP-15-IMP
  Phases 8..10 to reduce.

## Verification

- `pytest tests/ -q`: 79 passed.
- All six sibling validators PASS (the BP-SEM advisory step records
  the documented legacy findings; the index and conformance steps
  remain green).
- `regenerate_catalog.py --check`: OK locally AND in a fresh clone of
  this branch (mtime trap guard).
- Dash-clean: zero en/em dashes in added lines. The bullet appositions
  introduced during the See-also expansion were converted to colons
  before commit.
- Language pass: design-spec tone, present tense, "The catalog
  enforces...", no "We should...".

## Programme position

- CR-BP-14: **Implemented** (Phase 1 + 2 + 3 + 4 shipped; PRs #26,
  #28, #29, #30).
- CR-BP-15 + CR-BP-15-IMP: PR-0 done (PR #27); next is PR-4
  (15-IMP Phases 1-2: inventory + immutable baseline).