# CR-BP-13b: GovernanceAndExistence Admission Tranche

## What this PR is

Promotes all 5 accepted GovernanceAndExistence coordinates from the ratified research register (CR-BP-13) into canonical Process Group records with their composing L2 Business Process specialization entries.

## Coverage

| Stage | Process Group | L2 Processes |
|---|---|---|
| Conceive | `dea:group-strategy-and-governance-conception` | Develop Governance Strategy; Initiate Policy and Charter |
| Design | `dea:group-governance-system-design` | Design Governance System; Design Policies and Controls |
| Build | `dea:group-governance-body-establishment` | Establish Governance Bodies; Codify Charters and Policies |
| Operate | `dea:group-governance-oversight` | Operate Governance Oversight; Audit Policy Compliance |
| Improve | `dea:group-governance-review-and-learning` | Review Governance Effectiveness |

**Total adds**: 5 Process Context cells + 5 Process Group records + 9 L2 Process specialization entries = **19 new canonical entries**.

## Process Context cells

| ID | Stage |
|---|---|
| `dea:pc-ge-c` | Conceive |
| `dea:pc-ge-d` | Design |
| `dea:pc-ge-b` | Build |
| `dea:pc-ge-op` | Operate |
| `dea:pc-ge-im` | Improve |

Each cell carries the full Cell Charter (CR-BP-02 §7).

## Naming policy (locked)

- **Process Group names** follow the ratified register's first `l1_candidates[]` entry per coordinate.
- **L2 names** follow BP-ARC-ID-001 (verb-first) using real industry vocabulary: ISO 37000:2021 (Governance of Organizations), TOGAF ADM, COBIT 2019, COSO Internal Control.

## Tool

- `tools/build_bp13b_tranche.py` (~1100 lines): per-tranche generator that imports + reuses renderer helpers from `tools/build_bp13a_tranche.py`. CR-BP-13a is now the shared module; the bp13b script declares the 5+5+9 entries specific to GovernanceAndExistence and delegates rendering.
- **Generalization**: `tools/build_bp13a_tranche.py` now ships ECF identifiers for both `dea:pc-cd-*` AND `dea:pc-ge-*`; it also adds a `DOMAIN_NAMES` lookup so the renderer picks the right domain name from the Process Context id mid-segment instead of hardcoding `CustomerAndDemand`.

## Tests

- `tests/test_build_bp13b_tranche.py` (NEW, 13 tests): data declarations, shape coverage, dash-clean, controlled vocabulary, render-output shape.
- Plus 24 existing tests (CR-BP-13 + CR-BP-13a). **Total: 38/38 pass**.

## Verification (live)

| Gate | Result |
|---|---|
| `pytest tests/` | **38 passed** |
| `regenerate_catalog.py --check` | OK (CATALOG.yaml current) |
| `check_catalog_index.py --strict` | OK (28 entities validate) |
| `conformance_test_catalog_structure.py --strict` | 16/16 CSTs pass |
| `check_ecf_conformance.py` | PASS (28 entries conform) |
| `check_legacy_migration.py` | PASS (BP-MIG-001..005) |
| `check_process_context.py` | PASS (PC-001..PC-008) |
| `check_process_group.py` | PASS (PG-001..008; 10 Process Groups) |
| `check_process_identity.py` | PASS (with suggestions) |
| `check_process_specialization.py` | PASS (BP-SPEC-01-001..007) |
| Per-file schema dispatch (CI: validate-process-entries) | PASS |
| Dash sweep on new prose | Clean |
| Secret scan | 0 |
| `git diff --check` | Clean |

## Out of scope (intentional)

- Promote the 11 backlog-deferred Activate/Retire coordinates (deferred by CR-BP-13 §4).
- Other 5 domains (SupplyAndResources, PeopleAndOrganization, ProductAndOffering, OperationsAndDelivery, FinanceAndValue) follow in CR-BP-13c..BP-13g.

## Sequencing

| CR | Status |
|---|---|
| CR-BP-11 | Merged (research register) |
| CR-BP-12 | Merged (L1 Process Group profile) |
| CR-BP-13 | Merged (research ratification) |
| CR-BP-13a | Merged (CustomerAndDemand; PR #23) |
| **CR-BP-13b (this PR)** | **Proposed** |
| CR-BP-13c..BP-13g | future |

After this PR lands, **2 of 7 ECF domains are fully populated** (CustomerAndDemand + GovernanceAndExistence). 28 catalog entities total: 10 Process Groups + 18 Processes.