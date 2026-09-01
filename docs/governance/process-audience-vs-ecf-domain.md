# Governance Decision: `process_audience` vs ECF Domain

CR-ECF-CG-004 §10 ratification. Recorded for explicit publication; the conformance gate enforces it.

## The decision

The Business Process Catalog's `process_audience` field is **NOT** an ECF Domain, even though both use the same 7-value kebab-case vocabulary. They live on different semantic axes.

## Why the gate must not collapse them

| Aspect | `process_audience` | ECF Domain |
|---|---|---|
| Cardinality | single value | one axis of `(Domain x Stage)` ordered pair |
| Semantic axis | "who does this process serve?" (audience classification) | "in which enterprise function does this concept primarily operate?" (contextual placement) |
| Catalog-specific? | yes (Process Catalog methodology) | no (canonical ECF semantics) |
| Resolves to canonical PascalCase enum? | no (display label) | yes (must be `GovernanceAndExistence` etc.) |
| Required by schema? | yes (root `required`) | no (appears in optional `ecfConformance.canonicalReferences`) |
| Used by conformance gate? | yes, but only as a value check against the kebab-case enum; never as canonical ECF | yes, as a canonical PascalCase value |

## What the gate enforces

`scripts/check_ecf_conformance.py` (CR-ECF-CG-004 implementation):

1. `process_audience` is validated against the kebab-case enum (it's a process-side value, not an ECF reference).
2. Any `canonicalReferences[].domain` that uses a kebab-case value is rejected with the explicit reason: "CG-004 §10 forbids collapsing process_audience into ECF Domain".
3. Any `canonicalReferences[].domain` that uses a PascalCase value outside the canonical ECF enum is rejected with: "not in canonical enum".
4. The two checks are independent: a process entry may have a `process_audience` value (kebab) and a separate `ecfConformance.canonicalReferences` value (PascalCase, canonical).

## Why the vocabularies overlap

The 7 kebab-case labels in `process_audience` happen to match the 7 ECF Domain display labels. This is by **coincidence of display labelling**, not by canonical reference. The Process Catalog chose kebab-case labels for human readability; the ECF chose PascalCase identifiers for canonical reference. Both refer to the same *idea* (an enterprise function area) but in different roles.

If a future CR changes either vocabulary, the other is not automatically affected. The gate treats them as separate.

## Approval

This governance decision is ratified by the merge of the CR-ECF-CG-004 implementation PR. It supersedes any earlier informal usage where `process_audience` may have been read as an EC domain reference.