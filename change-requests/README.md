# Change Requests: Process Catalog

Change requests for the Business Process catalog. CRs land verbatim on
acceptance. Status changes are recorded by the PR that lands or amends
the CR, not by rewriting the CR document.

| CR | Title | Status | Notes |
|----|-------|--------|-------|
| [CR-ECF-CG-004](CR-ECF-CG-004.md) | Business Process Catalog Conformance | **Merged** (PRs #5 + #6) | The Process Catalog has already developed the correct conceptual distinction (Process Context ≠ Business Process; L0-L4 decomposition catalog-governed). Mandates governance ratification of the **`process_audience` ≠ ECF Domain** decision (§10). |
| [CR-BP-SPEC-BP-01](CR-BP-SPEC-BP-01.md) | Business Process Specialization Catalog | **Merged** (PR #12) | Re-anchors the catalog on the **kernel + specializations** discipline (CR-MM-PROC-01; CR-AR-FMWK-01; WSF). Refines + supersedes CR-BP-01's wrong premise (that `dea:BusinessProcess` is the sole canonical Process identity). Pointer declares both `dea:BusinessProcess` (specialization) and `dea:entity-process` (kernel; `discriminator: process-kernel`). New validator `scripts/check_process_specialization.py` enforces `BP-SPEC-01-001..007`. |
| [CR-BP-02](CR-BP-02.md) | Establish Process Context | **Merged** (PR #14) | Establishes the **Process Context register + Cell Charter schema** on top of the kernel + specialization tranche. Each context is `Domain x Lifecycle Stage` with a Cell Charter. PC-001..PC-008 validator. Matrix empty by design (CR-BP-02 §22). |
| [CR-BP-03](CR-BP-03-business-process-architecture.md) | Business Process Architecture | **Merged** (PR #15) | Establishes the **4-axis classification** (intent / type / specialization / audience) with no breaking changes to existing fields. Introduces `process_type` (5-value Mintzberg vocabulary; CR-BP-03 §2.1) + `process_specialization` (inheritance / pattern-based refinement). Refines the L0/L1/L2 hierarchy as a **conceptual model** (not separate top-level directories). Introduces the **process-identity contract** (verb + object + outcome_statement + evidence_links) and **contribution-driven re-landscape** (a new process contribution is submitted to `contributions/processes/`, a report is generated, the report is piped through CI). 5 documents in `docs/`; 1 new workflow (`.github/workflows/process-contribution-report.yml`); 4 schemas (updated entity, identity, contribution, classifications); 1 new validator (`check_process_identity.py`; BP-ARC-ID-001..005). |
| [CR-BP-03A](CR-BP-03A-legacy-migration.md) | Legacy Field Migration | **Merged** (PR #16) | Resolves three issues with the CR-BP-03 schema: (1) `relationships` shape corrected to array-of-relationship-instances (per metamodel `relationship-instance.json`); (2) `parent_process` / `child_processes` REMOVED (catalog inventions from CR-BP-01; not metamodel fields); (3) `capabilities_delivered` soft-deprecated (migrate to `relationships[relationship_type=realizes]`). New validator `scripts/check_legacy_migration.py` enforces BP-MIG-001..005. Updated `docs/architecture.md` and `docs/relandscape.md`. |
| [CR-BP-03C](CR-BP-03C-sample-process-contribution.md) | Sample Business Process Contribution | **Proposed (this PR)** | Lands the **first** Business Process entry (`dea:bp:manage-customer-relationship`) — walks the full CR-BP-03 / CR-BP-03A / CR-BP-02 flow end-to-end. Sample entry exercises every part of the machinery: 4-axis classification, identity contract (verb + object + outcome + evidence), canonical relationships, L0/L1/L2 conceptual hierarchy (metadata-only), Process Context reference (Cell Charter `dea:pc-cd-op`), ECF Conformance Gate (inherits-catalog with `doesNotRedefine` extensions). Worked example at `docs/examples/manage-customer-relationship.md`; future contributors should pattern-match against this entry. Reclassification report generator upgraded (CR-BP-03C §7) to cross-check proposed_entry against BP-ARC-ID-001..005. |

## Cross-repo context

CG-001 lands in `dea-metaframework` (PR #9 MERGED, commit `f5b8e01`).
CG-002 lands in `dea-metamodel` (PR #154 MERGED, commit `561da9f`).
CG-003 lands in `dea-catalog-business-capabilities` (proposal PR #33 MERGED, impl PR #34 MERGED, commit `6be58a2`).
CG-004 lands here.
CG-005 + CG-006 land in `dea-metamodel` (matrix + automated CI).

CR-MM-PROC-01 lands in `dea-metamodel` (PR #163 MERGED, commit `1665209`).
CR-AR-FMWK-01 lands in `dea-architecture-framework` (PR #10 MERGED, commit `76463b2`; tag `v0.6.0`).