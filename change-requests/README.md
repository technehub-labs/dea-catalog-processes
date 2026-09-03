# Change Requests: Process Catalog

Change requests for the Business Process catalog. CRs land verbatim on
acceptance. Status changes are recorded by the PR that lands or amends
the CR, not by rewriting the CR document.

| CR | Title | Status | Notes |
|----|-------|--------|-------|
| [CR-ECF-CG-004](CR-ECF-CG-004.md) | Business Process Catalog Conformance | **Merged** (PRs #5 + #6) | The Process Catalog has already developed the correct conceptual distinction (Process Context ≠ Business Process; L0-L4 decomposition catalog-governed). Mandates governance ratification of the **`process_audience` ≠ ECF Domain** decision (§10). |
| [CR-BP-SPEC-BP-01](CR-BP-SPEC-BP-01.md) | Business Process Specialization Catalog | **Merged** (PR #12) | Re-anchors the catalog on the **kernel + specializations** discipline (CR-MM-PROC-01; CR-AR-FMWK-01; WSF). Refines + supersedes CR-BP-01's wrong premise (that `dea:BusinessProcess` is the sole canonical Process identity). Pointer declares both `dea:BusinessProcess` (specialization) and `dea:entity-process` (kernel; `discriminator: process-kernel`). New validator `scripts/check_process_specialization.py` enforces `BP-SPEC-01-001..007`. |
| [CR-BP-02](CR-BP-02.md) | Establish Process Context | **Proposed (this PR)** | Establishes the **Process Context register + Cell Charter schema** on top of the kernel + specialization tranche. Each context is `Domain x Lifecycle Stage` with a Cell Charter. PC-001..PC-008 validator. Matrix empty by design (CR-BP-02 §22). |

## Cross-repo context

CG-001 lands in `dea-metaframework` (PR #9 MERGED, commit `f5b8e01`).
CG-002 lands in `dea-metamodel` (PR #154 MERGED, commit `561da9f`).
CG-003 lands in `dea-catalog-business-capabilities` (proposal PR #33 MERGED, impl PR #34 MERGED, commit `6be58a2`).
CG-004 lands here.
CG-005 + CG-006 land in `dea-metamodel` (matrix + automated CI).

CR-MM-PROC-01 lands in `dea-metamodel` (PR #163 MERGED, commit `1665209`).
CR-AR-FMWK-01 lands in `dea-architecture-framework` (PR #10 MERGED, commit `76463b2`; tag `v0.6.0`).