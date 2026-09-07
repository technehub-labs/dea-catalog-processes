# CR-BP-15 + CR-BP-16 landing + CR lineage knowledge harvest

## Summary

Lands **CR-BP-15: Process Catalog Reconciliation** and **CR-BP-16:
Process Catalog Conformance Gate** (the CR-BP-16 attachment also carries
**CR-BP-15-IMP**, the 20-phase implementation programme for CR-BP-15)
verbatim, and harvests the knowledge of the CR lineage into two new
visitor-facing documents.

This is PR-0 of the integrated CR-BP-14 / CR-BP-15 / CR-BP-16 programme
(plan: working folder `dea-work/process/2026-09-06-bp-14-15-16-programme/PLAN.md`).

## What this PR does

1. **Lands the CRs verbatim**:
   - `change-requests/CR-BP-15-process-catalog-reconciliation.md`
     (md5 `b4240531f773734a9d01aebc5c296410`)
   - `change-requests/CR-BP-16-process-catalog-conformance-gate.md`
     (md5 `226c13194f54c6ce2b9a7a5101085c56`; carries CR-BP-15-IMP)
2. **Knowledge harvest (visitor-facing docs)**:
   - `docs/semantic-contract.md`: the semantic constitution distilled
     from CR-BP-14; the six characterization dimensions (Identity /
     Intent / Classification / Specialization / Context / Relationships),
     the controlled vocabularies, the naming contract, and the
     separations that are always true (Intent != Classification;
     Audience != Context; Specialization != Decomposition; Context
     never generates Process; Group != Function != Capability;
     Catalog != Kernel).
   - `docs/governance/reconciliation-programme.md`: the closed
     governance loop (research -> candidate -> assessment ->
     reconciliation -> conformance -> governance -> canonical ->
     continuous conformance), the CR lineage table, the ten
     reconciliation dispositions, conformance levels L0-L4, the
     repository status model, and what the admission freeze means for
     contributors.
   - README gains a "Reading This Repository" orientation block pointing
     at both.
3. **Register + README programme sync**: CR-BP-15 and CR-BP-16 rows
   (Proposed); CR-BP-14 row updated (Phase 1 merged, PR #26).
4. **CHANGELOG** entry.
5. **CATALOG.yaml regenerated** (`open_change_requests` 14 -> 16).

## What this PR does NOT do

- No schema, validator, or entity changes.
- No reconciliation work itself (that is CR-BP-15-IMP, PR-4 onwards).
- The admission freeze (CR-BP-14 §24) remains in effect.

## Verification

- `pytest tests/ -q`: 47 passed.
- All six catalog validators PASS (specialization incl. --self-test,
  identity, legacy migration, context, group, ECF conformance).
- `check_catalog_index.py --strict`: OK (28 entities).
- Regenerator gate reproduced in a FRESH clone of this branch (mtime
  trap guard): `regenerate_catalog.py --check` byte-identical.
- Dash-clean: zero en/em dashes in authored content (the two CR files
  land verbatim per land-as-authored and are exempt).

## Programme position

Next after merge: PR-1 (CR-BP-14 Phase 2): `context:` block +
`serves` / `contributes-to` relationship semantics + ECF-identifier
target pattern (decisions D2/D3 of the programme plan).
