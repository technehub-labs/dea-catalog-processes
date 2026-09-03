# Process Specialization Governance — Business Process Catalog

**Authority:** CR-MM-PROC-01 (dea-metamodel; PR #163); CR-AR-FMWK-01
(dea-architecture-framework; PR #10 + tag v0.6.0); CR-BP-SPEC-BP-01
(this catalog; PR #12).

**Date:** 2026-09-03.

## Kernel + Specialization Discipline

The OpenDEA Process discipline is a **kernel + specializations** model
that propagates through four authority layers:

```
WSF (org; upstream)
 └─ wsf:Process                (Tier-3 derived; structural activity organization)

      └─ dea-metamodel (Core authority)
           ├─ dea:Process               (abstract Core kernel)
           │     ├─ dea:BusinessProcess  (Core specialization; this catalog's subject)
           │     ├─ (future) dea:OperationalProcess
           │     └─ (future) dea:EngineeringProcess
           │
           └─ dea-architecture-framework (root model)
                ├─ dea:entity-process               (abstract kernel; class_alias PRC;
                │                                      discriminator process-kernel)
                └─ dea:entity-business-process      (specialization; class_alias BP;
                                                       specializes PRC)

                      └─ dea-catalog-processes (this catalog)
```

## Federation Mapping (1:1; EXACT; LOSSLESS)

| Metamodel id | Root-model id | Notes |
|---|---|---|
| `dea:Process` | `dea:entity-process` | Kernel; abstract; in v0.6.0 root model |
| `dea:BusinessProcess` | `dea:entity-business-process` | Specialization; layer L3; in v0.6.0 root model |
| `dea:Process ↔ wsf:Process` | — | Federation mapping in `mappings/wsf/mapping.yaml` |

## Legacy Identifiers (preserved)

- `dea:entity-process`: pre-WSF root-model id; now recorded as a
  `legacy_id` of the kernel `dea:entity-process` (and mirrored to the
  metamodel-side kernel `dea:Process` as `dea:entity-process`). NOT a
  parallel canonical entity.
- `Process`: natural-language reference; resolved via the canonical
  identity and recorded as a `legacy_name` of the kernel.

## Why "Business Process" is a Specialization, Not the Kernel

The user reframe (2026-09-03) corrected CR-BP-01's premise:

> "WSF is authoritative on the concept of process; DEA is expected to
> inherit that and then create a specialization in the enterprise
> context, with the specialization being 'business', which will be
> applicable to a 'business architecture' architecture use case, and
> further support business operations. It's possible to have also
> other specializations of process in DEA which are not of nature
> leading or meant to be meeting the 'business' context... In addition
> the sub-classification within business processes still hold."

Three consequences:

1. The kernel `dea:Process` (metamodel) / `dea:entity-process` (root
   model) is **the** Process concept — generic, non-context-specific.
2. `dea:BusinessProcess` (metamodel) / `dea:entity-business-process`
   (root model) is one specialization context (Business Architecture +
   Business Operations).
3. Other specialization contexts (Operational, Engineering, ...) are
   possible and will have their own root-model entries and catalogs when
   demand emerges.

## Sub-Classifications (Catalog-Internal)

Sub-classifications of Business Process — `operational` / `support` /
`management` — are **not** entities. They are carried by the catalog's
`process_intent` field (an enum) on each catalog entry. They do NOT
promote to:

- root-model entities (`dea:entity-operational-process`, etc.);
- metamodel entities (`dea:OperationalProcess`, etc.);
- specialized catalogs (`dea-catalog-operational-processes`, etc.).

This preserves the root model's MECE property and keeps the
Process-kernel + specialization discipline clean.

## Catalog Pointer Contract

The catalog's `metamodel-pointer.yaml` declares the **dual contract**:

1. Primary `metamodel:` block — the specialization
   (`dea:BusinessProcess`; class_alias BP; layer L3;
   `building_block: L3-value-delivery`).
2. `metamodel.entities:` list — the kernel
   (`dea:entity-process`; class_alias PRC;
   `discriminator: process-kernel`) as the first entry.

The consumer validator (`dea-architecture-framework/scripts/validate_consumer.py`;
v0.6.0 abstract-kernel branch) verifies the contract; the catalog-local
validator (`scripts/check_process_specialization.py`) enforces seven
rules (BP-SPEC-01-001..007) including this contract.

## Migration Notes

- **Pre-CR-BP-01** (revert commit `0e96ceb`): pointer pinned to v0.2.1
  with `dea:entity-process` as primary. v0.2.1 lacks the kernel +
  specialization split.
- **CR-BP-01 / PR #10** (`a34c7ff`): wrong premise — promoted
  `dea:BusinessProcess` as sole canonical. Reverted in PR #11
  (commit `417114f`).
- **CR-BP-SPEC-BP-01** (this CR; PR #12): pointer advances to v0.6.0
  with the kernel + specialization contract. Validator renamed to
  `check_process_specialization.py` and extended to BP-SPEC-01-001..007.

## Out of Scope

- Process Context register + Cell Charter schema (CR-BP-02; gated on
  this CR's merge).
- Workflow / Activity semantics (WSF discipline applies unchanged;
  future CRs gate on demand).
- Other Process specializations (Operational, Engineering, ...); each
  future specialization lands as its own CR following this same
  template.