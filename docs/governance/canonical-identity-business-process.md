# Governance Decision: Canonical Identity for Business Process

CR-BP-01 ratification. Recorded for explicit publication; the
canonical-identity validator enforces it.

## The decision

The canonical OpenDEA semantic identity for the Business Process
concept is:

```
dea:BusinessProcess
```

The legacy identifier:

```
dea:entity-process
```

is preserved as an explicit compatibility mapping and must not be
used as the canonical entity id in any new catalog artifact.

## Why this matters

The upstream `dea-metamodel` already exposes `dea:BusinessProcess`
as the canonical entity id (`metamodel/dea-metamodel.yaml:562`),
with `dea:entity-process` recorded as a legacy identifier
(line 565). The Business Process Catalog's `metamodel-pointer.yaml`
was lagging that alignment and still declared
`entity_id: dea:entity-process` as canonical. CR-BP-01 closes
that lag and establishes the catalog's pointer, schemas, README,
and validation rules in lockstep with the upstream canonical.

## What the validator enforces

`scripts/check_bp01_canonical.py` (CR-BP-01 AC-07):

1. **BP-01-001**: `metamodel-pointer.yaml`'s `metamodel.entity_id`
   must equal `dea:BusinessProcess`. Any other form (including the
   legacy id) is a hard failure.
2. **BP-01-002**: if the legacy id `dea:entity-process` appears
   anywhere in the repository, an explicit `legacy_identifiers:`
   block must also be present in `metamodel-pointer.yaml`. The
   current pointer carries the block; future drift that drops the
   block while keeping a legacy reference is rejected.
3. **BP-01-003**: bare `dea:Process` must not be used as a
   canonical entity id. Only `dea:BusinessProcess` is canonical.
4. **Schema patterns**: JSON Schemas whose `pattern` regexes
   anchor to the Business Process entity id must accept the
   canonical id. Patterns that only match the legacy id are
   rejected. Generic lowercase catalog-entry id patterns
   (e.g. `dea:process-<name>`) are out of scope — they follow the
   sibling capability catalog precedent.
5. **Narrative docs**: a soft warning is emitted if the legacy id
   appears in narrative prose alongside canonical-asserting
   phrasing (e.g. "the canonical `dea:entity-process`"). Soft
   warnings log only; they do not fail the gate.

## Why a generic `dea:Process` is rejected

CR-BP-01 §6 Decision BP-01-D02: no generic normative entity named
`dea:Process` will be introduced. The reason is two entities that
could represent the same enterprise concept (generic Process vs.
canonical BusinessProcess) is exactly the semantic ambiguity the
CR exists to eliminate.

## Legacy identifier compatibility model

The `metamodel.legacy_identifiers` block in `metamodel-pointer.yaml`
is the single authoritative declaration of legacy compatibility.
Downstream consumers that need to migrate from `dea:entity-process`
to `dea:BusinessProcess` should:

1. Find the legacy id in their local artifact.
2. Resolve it through the pointer's `legacy_identifiers` block.
3. Replace the local reference with `dea:BusinessProcess`.
4. Preserve any human-readable "Process" label where appropriate
   (it is a natural-language shorthand, not a competing canonical
   identity).

The legacy id remains valid for read-only historical references;
new normative artifacts must use the canonical id.

## Provenance

- Canonical entity id lives at `dea-metamodel/metamodel/dea-metamodel.yaml:562`.
- Legacy identifier lives at `dea-metamodel/metamodel/dea-metamodel.yaml:565`.
- Catalog pointer declaration: `metamodel-pointer.yaml`.
- Validator: `scripts/check_bp01_canonical.py`.
- CI: `.github/workflows/ci.yml` (step "Run CR-BP-01 canonical-identity validator").

## References

- `change-requests/CR-BP-01.md` — proposal; canonical-identity decision.
- `change-requests/CR-ECF-CG-004.md` — ECF conformance for the catalog.
- `docs/governance/process-audience-vs-ecf-domain.md` — sibling governance
  decision (CG-004 §10 ratification).