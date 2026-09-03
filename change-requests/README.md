# Change Requests: CR-ECF-CG Series (Process Catalog)

Change requests for the Business Process catalog under the ECF Conformance Gate (CG-001..006). CRs land verbatim on acceptance. Status changes are recorded by the PR that lands or amends the CR, not by rewriting the CR document.

| CR | Title | Status | Notes |
|----|-------|--------|-------|
| [CR-ECF-CG-004](CR-ECF-CG-004.md) | Business Process Catalog Conformance | Implemented (PR #5 + PR #6 merged 2026-09-01) | The Process Catalog has already developed the correct conceptual distinction (Process Context ≠ Business Process; L0-L4 decomposition catalog-governed). Mandates governance ratification of the **`process_audience` ≠ ECF Domain** decision (§10). Implementation PR (post-merge) adds optional `ecfConformance` block to schema, conformance gate, README profile declaration. |
| [CR-ECF-CG-005](CR-ECF-CG-005.md) | (cross-repo reference; landed in `dea-metamodel` per CG-005/006) | See `dea-metamodel` | Cross-Repository Conformance (matrix, drift detector, manifest). |
| [CR-ECF-CG-006](CR-ECF-CG-006.md) | (cross-repo reference; landed in `dea-metamodel` per CG-005/006) | See `dea-metamodel` | Automated Conformance Enforcement (CI wiring). |
| [CR-BP-01](CR-BP-01.md) | Business Process Semantic Baseline | Proposed (this PR) | First CR of the OpenDEA Business Process Architecture Evolution programme. Reconciles canonical identity: `dea:BusinessProcess` (canonical); `dea:entity-process` (legacy). Aligns `metamodel-pointer.yaml`, README, and schemas; introduces BP-01-001/002/003 validation rules. Implementation PR (post-merge) carries the alignment work. Blocks CR-BP-02..CR-BP-10. |

## Cross-repo context

CG-001 lands in `dea-metaframework` (PR #9 MERGED, commit `f5b8e01`).
CG-002 lands in `dea-metamodel` (PR #154 MERGED, commit `561da9f`).
CG-003 lands in `dea-catalog-business-capabilities` (proposal PR #33 MERGED, impl PR #34 MERGED, commit `6be58a2`).
CG-004 lands here.
CG-005 + CG-006 land in `dea-metamodel` (matrix + automated CI).