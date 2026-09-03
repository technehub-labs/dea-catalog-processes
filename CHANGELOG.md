# Changelog

All notable changes to this repository are documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows
`docs/versioning.md`.

## [Unreleased]

### CR-BP-SPEC-BP-01: Business Process Specialization Catalog

Re-anchors the catalog on the **kernel + specializations** discipline for
the OpenDEA Process concept. Refines + supersedes the prior CR-BP-01
(which landed as PR #10 on the wrong premise that `dea:BusinessProcess`
is the sole canonical Process identity).

**Authority chain established by this CR (end-to-end):**

```
WSF (org)                                     wsf:Process (Tier-3 derived)
 └─ dea-metamodel (Core authority)              CR-MM-PROC-01; PR #163
     ├─ dea:Process            (abstract Core kernel)
     └─ dea:BusinessProcess    (Core specialization)
        └─ dea-architecture-framework (root model)   CR-AR-FMWK-01; PR #10 + tag v0.6.0
             ├─ dea:entity-process               (abstract kernel; class_alias PRC;
             │                                       discriminator process-kernel)
             └─ dea:entity-business-process      (specialization; class_alias BP;
                                                    specializes PRC)
                └─ dea-catalog-processes (this catalog)   CR-BP-SPEC-BP-01; this PR
```

**Tranche history:**

- `1665209` — CR-MM-PROC-01 merged on `dea-metamodel` (kernel + specialization).
- `76463b2` — CR-AR-FMWK-01 merged on `dea-architecture-framework` (root model v0.5.0 → v0.6.0; consumer-validator abstract-kernel branch; ADR-0006).
- `417114f` — Revert of `a34c7ff` (CR-BP-01 implementation) merged on `dea-catalog-processes`.
- `v0.6.0` — OpenDEAM root model tag published.

**Changes:**

#### Added

- `change-requests/CR-BP-SPEC-BP-01.md` (md5 `5f5aa30e7ebfe2f1c187c300d5136406`; byte-identical to working folder `/home/hermes/dea-work/process/00_inbox/`).
- `docs/governance/process-specialization.md` — the governance narrative for the kernel + specialization contract.
- `scripts/check_process_specialization.py` — new validator enforcing `BP-SPEC-01-001..007` (with built-in `--self-test`).

#### Changed

- `metamodel-pointer.yaml` — pointer now declares the dual contract:
  - Primary `metamodel:` block: `dea:BusinessProcess` (specialization; class_alias BP; layer L3; building_block L3-value-delivery).
  - `metamodel.entities:` list: `dea:entity-process` (kernel; class_alias PRC; discriminator process-kernel; no layer, no dimension).
  - `metamodel.version: v0.6.0` (advances from v0.2.1; the root model carries both ids as of v0.6.0).
- `schemas/entity.schema.json` — `title: "Business Process"` (was `"Process Catalog Entry"`); description now references the WSF / Process-kernel lineage (CR-MM-PROC-01; CR-AR-FMWK-01; CR-BP-SPEC-BP-01).
- `.github/workflows/ci.yml` — adds the Business Process specialization gate step.
- `README.md` — "Purpose" reframed as Business Process **specialization** catalog; governing principle updated to "One kernel. Many valid specializations. One canonical home per specialization."

#### Removed (from the reverted `a34c7ff`; re-anchored here under the corrected premise)

- `change-requests/CR-BP-01.md` — superseded by this CR (the original text remains archived in `/home/hermes/dea-work/process/00_inbox/CR-BP-01.md`).
- `docs/governance/canonical-identity-business-process.md` — replaced by `docs/governance/process-specialization.md`.
- `scripts/check_bp01_canonical.py` — replaced by `scripts/check_process_specialization.py` (extended to `BP-SPEC-01-001..007`; original BP-01-001/002/003 rules folded into the new ruleset).

**Sub-classifications (operational / support / management)** remain
**catalog-internal** via the `process_intent` field. They do not promote
to root-model entities (`dea:entity-operational-process`, etc.). The
validator's `BP-SPEC-01-007` rule enforces this.

**Out of scope (gated on its merge):** CR-BP-02 (Process Context register
+ Cell Charter schema).

## Superseded (do not proceed with these)

- `a34c7ff` (CR-BP-01; PR #10): wrong premise — promoted
  `dea:BusinessProcess` as the sole canonical Process identity. Reverted
  by PR #11 (commit `417114f`). The artifacts (governance doc, validator,
  CI wire) are **preserved** and re-anchored by this CR under the
  corrected kernel + specialization discipline.