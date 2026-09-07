# CR-BP-14 Phase 2: Process Context block + contextual relationships

## Summary

Implements Phase 2 of CR-BP-14 (§13, §19, §20): the canonical Process
Context representation and contextual relationship semantics. Programme
decisions D2 and D3 are applied as planned.

No existing entry is mutated; all 38 canonical records continue to
validate unchanged.

## Deliverables

1. **`context:` block** on `schemas/entity.schema.json` and
   `schemas/contribution.schema.json` (§13, §20): an array of
   `{ref: dea:pc-*}` Process Context references. Multiple contexts are
   permitted where evidence establishes legitimate cross-context
   responsibility (BP-SEM-012). Reference integrity enforcement arrives
   with BP-SEM-008 in Phase 3.
2. **Contextual relationship types**: the `relationship_type` enum gains
   `serves` and `contributes-to`, both admitted by the metamodel
   relationship registry (catalog-governed extension; no metamodel CR
   required; programme decision D2). `operates-within` is deliberately
   absent from the enum: it has no metamodel registry id, and its
   semantics are carried by the `context:` block.
3. **ECF-identifier targets** (decision D3): `target_id` now admits the
   canonical CG-003 identifier form
   (`ecf:<lowerCamelDomain>[.<lowerCamelStage>]`) alongside entity ids,
   making the §13 target representation (`serves` toward an ECF
   coordinate) expressible. The entity-id branch excludes the `ecf:`
   prefix, so the kebab-case label form (`ecf:customer-demand`) is
   rejected, consistent with the CG-004 §10 governance decision.
4. **Contribution template**: the canonical `context:` block replaces
   the pre-CR-BP-14 `process_context` scalar; a `serves` relationship
   example toward an ECF coordinate is included.
5. **`tests/test_process_context_relationships.py`** (16 tests): block
   shape on both schemas, enum extension, ECF / entity target patterns,
   malformed-reference rejection, and backward compatibility of every
   existing canonical Process entry.
6. **CHANGELOG** entry; register row notes Phase 2.

## Finding recorded for CR-BP-15-IMP Phase 10

The 13a/13b entries carry a legacy scalar `process_context: dea:pc-*`
field that predates the canonical `context:` block (not declared in the
entity schema; admitted because the root schema is permissive). The
schema remains permissive toward it until the audience / context
migration; this PR does not touch those records.

## What this PR does NOT do

- No BP-SEM validators yet (Phase 3; BP-SEM-001..012, including
  BP-SEM-008 context reference integrity).
- No migration of existing records (CR-BP-15-IMP scope).
- No documentation prose reconciliation (Phase 4).
- The §24 admission freeze remains in effect.

## Verification

- `pytest tests/ -q`: 63 passed (47 existing + 16 new).
- All six catalog validators PASS (specialization incl. --self-test,
  identity, legacy migration, context, group, ECF conformance).
- `check_catalog_index.py --strict`: OK (28 entities).
- `regenerate_catalog.py --check`: OK locally AND in a fresh clone of
  this branch (mtime trap guard).
- Contribution template parses; all 28 canonical entries validate under
  the extended schema.
- Dash-clean: zero en/em dashes in added lines.
