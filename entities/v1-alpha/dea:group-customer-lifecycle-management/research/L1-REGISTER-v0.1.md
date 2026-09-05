# L1 Process Group Discovery Register v0.1

Status: ratified-canonical-2026-09-05 (CR-BP-13)
Programme: CR-BP-11 (research) -> CR-BP-13 (ratification)
Repository: `technehub-labs/dea-catalog-processes`
Date: 2026-09-04 (research); 2026-09-05 (ratification)
Scope: 49 ECF coordinates (7 domains x 7 lifecycle stages)
Authoritative artefacts: `change-requests/CR-BP-11-l1-process-group-discovery.md`; `change-requests/CR-BP-13-research-ratification.md`; `01_plan/research-register/l1-register.yaml`; `01_plan/research-register/l1-candidate-universe.yaml`.

Ratification summary:
- 38 coordinates ratified-accepted (disposition: ratified-accepted)
- 11 coordinates backlog-deferred (Activate/Retire stages)
- 86 L1 candidates ratified; 16 L1 candidates backlog-deferred

See CR-BP-13 §4 for the rationale on the 11 backlog-deferred
coordinates (lifecycle transition stages; not stable Process
Group scopes).

---

## 1. What this register is

A research-only, evidence-bound register of candidate L1 Process Groups across the 49 ECF coordinates. Every coordinate carries an explicit disposition. No canonical L1 records are created in this register; the register is the input gate for CR-BP-12 (L1 Process Group profile + schema) and CR-BP-13..BP-19 (seven-domain admission tranches).

## 2. Disposition Policy

| Disposition | Meaning |
|---|---|
| `accepted` | Coordinate carries at least one L1 Process Group candidate supported by internal OpenDEA canon or by external-framework evidence E3+. |
| `deferred` | Coordinate carries zero, weak, or overlapping candidates. The L1 group cannot be defensibly bounded yet. A `deferral_reason` is mandatory. |
| `unresolved` | Internal evidence contradicts itself or boundary overlap is unresolved. Carries the conflicting pair. |
| `no-candidate` | Coordinate legitimately carries no L1 group (ECF legitimately-absent clause). |

## 3. Disposition Counts

| Domain | Accepted | Deferred | Total |
|---|---:|---:|---:|
| GovernanceAndExistence | 5 | 2 | 7 |
| SupplyAndResources | 6 | 1 | 7 |
| PeopleAndOrganization | 5 | 2 | 7 |
| CustomerAndDemand | 5 | 2 | 7 |
| ProductAndOffering | 6 | 1 | 7 |
| OperationsAndDelivery | 6 | 1 | 7 |
| FinanceAndValue | 5 | 2 | 7 |
| **Total** | **38** | **11** | **49** |

No coordinate carries `unresolved` or `no-candidate` in v0.1; technology is held unmapped across the matrix (cross-domain finding C1), not as a `no-candidate` cell.

## 4. Coordinate-Level Entries

### 4.1 GovernanceAndExistence

| Stage | Process Context | L1 Candidates | L2 Candidates | Disposition |
|---|---|---|---|---|
| Conceive | `dea:pc-ge-conceive` | Strategy and Governance Conception; Policy and Charter Initiation | Develop corporate strategy; Frame governance policy; Initiate charter and mandate | accepted |
| Design | `dea:pc-ge-design` | Governance System Design; Policy and Control Design | Design governance framework; Design control objectives; Design policy architecture | accepted |
| Build | `dea:pc-ge-build` | Governance Body Establishment; Charter and Policy Codification | Establish board and committees; Codify policies and standards | accepted |
| Activate | `dea:pc-ge-activate` | Governance Onboarding | Onboard governance bodies; Activate policy regime | deferred |
| Operate | `dea:pc-ge-operate` | Governance Oversight; Policy Compliance and Audit | Run board and committee cycle; Operate enterprise risk oversight; Operate policy compliance | accepted |
| Improve | `dea:pc-ge-improve` | Governance Review and Learning | Conduct governance effectiveness review; Score audit findings | accepted |
| Retire | `dea:pc-ge-retire` | Governance Sunset | Retire governance bodies; Sunset policies and mandates | deferred |

Evidence: `dea-metaframework/REPORT.md` §5; `dea-catalog-business-capabilities/capability-strategy`; `APQC PCF 7.0 Strategy Management`; `TOGAF ADM Phase G`; `ISO 37000:2021`.

### 4.2 SupplyAndResources

| Stage | Process Context | L1 Candidates | L2 Candidates | Disposition |
|---|---|---|---|---|
| Conceive | `dea:pc-sr-conceive` | Sourcing Strategy Conception; Resource Strategy Conception | Frame sourcing strategy; Frame asset strategy; Frame workforce capacity strategy (cross-ref) | accepted |
| Design | `dea:pc-sr-design` | Sourcing and Supply Design; Asset and Property Design; Resource Architecture Design | Design sourcing policy; Design supplier qualification framework; Design facility and asset blueprint; Design resource planning architecture | accepted |
| Build | `dea:pc-sr-build` | Supply Base Build; Asset Acquisition; Resource Stand-up | Onboard suppliers; Acquire and provision facilities; Acquire and install technology assets; Stand up resource pools | accepted |
| Activate | `dea:pc-sr-activate` | Sourcing Activation; Asset Activation | Activate supplier contracts; Activate facilities; Activate technology assets | accepted |
| Operate | `dea:pc-sr-operate` | Sourcing and Procurement Operation; Asset and Facility Operation; Supplier Management Operation | Operate procurement cycle; Operate supplier performance management; Operate facility management; Operate asset maintenance | accepted |
| Improve | `dea:pc-sr-improve` | Supply Base Improvement; Asset Performance Improvement | Conduct supplier performance review; Optimize asset utilization; Conduct supplier consolidation | accepted |
| Retire | `dea:pc-sr-retire` | Supply and Asset Retirement | Retire suppliers; Dispose of assets; Decommission facilities | deferred |

Evidence: `CR-DEA-BC-04 N-004`, `R-001`; `APQC PCF Sourcing`; `SCOR Plan/Source`; `ITIL 4 Service Configuration`; `IFRS 16 Leases`.

### 4.3 PeopleAndOrganization

| Stage | Process Context | L1 Candidates | L2 Candidates | Disposition |
|---|---|---|---|---|
| Conceive | `dea:pc-po-conceive` | Workforce Strategy Conception; Organization Conception | Frame workforce strategy; Frame organization model | accepted |
| Design | `dea:pc-po-design` | Organization and Role Design; Workforce Design | Design organization structure; Design role catalog; Design competency framework | accepted |
| Build | `dea:pc-po-build` | Talent Acquisition; Workforce Onboarding | Source talent; Recruit and select; Onboard new hires; Build contractor pool | accepted |
| Activate | `dea:pc-po-activate` | Workforce Activation; Organization Mobilization | Mobilize new organization unit; Activate role assignments | deferred |
| Operate | `dea:pc-po-operate` | HR Operations; Workforce Operations; Performance and Reward | Operate payroll and benefits; Operate time and attendance; Operate performance management; Operate learning and development | accepted |
| Improve | `dea:pc-po-improve` | Workforce Improvement | Conduct employee engagement review; Conduct skills gap analysis | accepted |
| Retire | `dea:pc-po-retire` | Workforce Transition; Organization Wind-down | Manage redundancy; Offboard departing employees; Decommission organizational unit | deferred |

Evidence: `CR-DEA-BC-04 N-001`; `dea-catalog-business-capabilities/capability-workforce-management`, `capability-workforce-planning`; `O*NET`; `SFIA 8`; `SHRM Body of Competency`; `APQC PCF Talent Acquisition`; `Workday HCM`.

### 4.4 CustomerAndDemand

| Stage | Process Context | L1 Candidates | L2 Candidates | Disposition |
|---|---|---|---|---|
| Conceive | `dea:pc-cd-conceive` | Customer Strategy Conception; Market and Demand Conception | Frame customer strategy; Frame market segmentation; Frame demand thesis | accepted |
| Design | `dea:pc-cd-design` | Customer Experience Design; Demand Design; Customer Journey Design | Design customer journey; Design demand forecast model; Design customer experience blueprint | accepted |
| Build | `dea:pc-cd-build` | Customer Channel and Acquisition Build; Demand Generation Build | Build customer acquisition channels; Build customer data platform; Build marketing automation | accepted |
| Activate | `dea:pc-cd-activate` | Customer Activation | Activate new customer onboarding; Activate customer journeys | deferred |
| Operate | `dea:pc-cd-operate` | Customer Relationship Management; Customer Service Operation; Demand Fulfillment | Manage customer relationship; Operate customer service; Operate demand fulfillment | accepted (canonical L2 present) |
| Improve | `dea:pc-cd-improve` | Customer Insight and Retention | Conduct NPS and satisfaction review; Operate churn analysis; Operate win-back programme | accepted |
| Retire | `dea:pc-cd-retire` | Customer Exit | Manage customer offboarding; Manage contract termination | deferred |

Evidence: `CR-DEA-BC-04 N-002`, `R-002`; `dea-catalog-business-capabilities/capability-marketing`, `capability-customer-management`; `APQC PCF Market and Sell`; `TM Forum eTOM Customer Journey Management`; `NICE Satmetrix NPS`; `Bain Net Promoter System`.

Canonical L2 present: `dea:process-manage-customer-relationship` (CR-BP-03C).

### 4.5 ProductAndOffering

| Stage | Process Context | L1 Candidates | L2 Candidates | Disposition |
|---|---|---|---|---|
| Conceive | `dea:pc-po2-conceive` | Offering Strategy Conception; Innovation Conception | Frame offering portfolio strategy; Frame innovation thesis; Frame alliance and partnership thesis (cross-ref) | accepted |
| Design | `dea:pc-po2-design` | Offering Design; Service Design; Innovation Design | Design offering blueprint; Design service blueprint; Design innovation experiment | accepted |
| Build | `dea:pc-po2-build` | Offering Build; Innovation Build | Build offering variant; Build new product capability; Build innovation prototype | accepted |
| Activate | `dea:pc-po2-activate` | Offering Activation | Launch offering; Activate service offering | accepted |
| Operate | `dea:pc-po2-operate` | Offering Operation; Service Operation | Operate offering catalogue; Operate service delivery management; Operate partner and alliance programme (cross-ref) | accepted |
| Improve | `dea:pc-po2-improve` | Offering Improvement; Service Improvement | Operate offering performance review; Operate service improvement programme | accepted |
| Retire | `dea:pc-po2-retire` | Offering Retirement | Retire offering; Decommission service | deferred |

Evidence: `CR-DEA-BC-04 R-007`; `dea-catalog-business-capabilities/capability-offering-management`, `capability-innovation-management`, `capability-partner-management`; `SAFe Product Development Flow`; `ITIL 4 Service Design/Operation`; `BIAN Service Design/Operations`.

### 4.6 OperationsAndDelivery

| Stage | Process Context | L1 Candidates | L2 Candidates | Disposition |
|---|---|---|---|---|
| Conceive | `dea:pc-od-conceive` | Operations Strategy Conception; Delivery Strategy Conception | Frame operations strategy; Frame delivery strategy | accepted |
| Design | `dea:pc-od-design` | Operations Design; Delivery Design | Design operations model; Design delivery model; Design logistics and routing | accepted |
| Build | `dea:pc-od-build` | Operations Build; Delivery Build; Manufacturing Build | Stand up production line; Build delivery capability; Build logistics network | accepted |
| Activate | `dea:pc-od-activate` | Operations Activation; Delivery Activation | Activate operations line; Activate delivery routes | accepted |
| Operate | `dea:pc-od-operate` | Operations Execution; Delivery Execution; Service Delivery Execution; Production Execution | Run production line; Operate logistics; Operate service delivery; Operate warehouse and inventory; Operate quality control | accepted |
| Improve | `dea:pc-od-improve` | Operations Improvement; Delivery Improvement | Conduct operations performance review; Conduct logistics optimization; Conduct lean six sigma programme | accepted |
| Retire | `dea:pc-od-retire` | Operations Retirement; Delivery Retirement | Decommission production line; Decommission delivery route; Retire logistics node | deferred |

Evidence: `CR-DEA-BC-04 R-008`; `dea-catalog-business-capabilities/capability-operations`; `SCOR Plan/Source/Make/Deliver/Return`; `ITIL 4 Service Transition/Operation`; `TM Forum eTOM Operations`; `APQC PCF Deliver Products and Services`; `APQC PCF Continuous Improvement`.

### 4.7 FinanceAndValue

| Stage | Process Context | L1 Candidates | L2 Candidates | Disposition |
|---|---|---|---|---|
| Conceive | `dea:pc-fv-conceive` | Finance Strategy Conception; Value Strategy Conception | Frame finance strategy; Frame value-creation strategy | accepted |
| Design | `dea:pc-fv-design` | Finance Architecture Design; Value Architecture Design; Financial Control Design | Design chart of accounts; Design cost allocation model; Design value measurement framework | accepted |
| Build | `dea:pc-fv-build` | Finance Capability Build; Financial System Build | Stand up finance function; Deploy ERP finance module | accepted |
| Activate | `dea:pc-fv-activate` | Finance Activation; Period Activation | Open new accounting period; Activate finance system cutover | deferred |
| Operate | `dea:pc-fv-operate` | Accounting and Reporting; Financial Stewardship; Treasury and Working Capital; Tax and Compliance; Procure-to-Pay and Order-to-Cash Operations | Operate general ledger; Operate accounts payable; Operate accounts receivable; Operate treasury; Operate tax compliance; Operate financial close; Operate financial planning and analysis | accepted |
| Improve | `dea:pc-fv-improve` | Finance Improvement; Value Performance | Conduct cost optimization review; Conduct margin and value analysis | accepted |
| Retire | `dea:pc-fv-retire` | Financial Wind-down; Asset and Investment Disposal | Operate financial wind-down; Dispose of investments; Recognize impairment and exit liabilities | deferred |

Evidence: `dea-catalog-business-capabilities/capability-financial-management`, `capability-financial-stewardship`; `COSO Internal Control`; `IFRS`, `IFRS 5`, `IFRS 16`, `IFRS IAS 1`; `SAP S/4HANA Finance process reference`; `CFO Strategy Forum`; `Gartner Finance Benchmark`; `APQC PCF Financial Management Improvement`; `ASC 205-30 Liquidation Basis`.

## 5. Cross-Domain Findings

| ID | Topic | Verdict | Evidence |
|---|---|---|---|
| C1 | Technology Management | Held unmapped across the matrix; technology is an L5 layer concern, not an ECF domain. No standalone Technology cell. | `CR-DEA-BC-04 N-006`, `R-004`; `boundary-decision-cand-019.yaml` |
| C2 | Change Management | Cross-cutting pattern at governance-existence x improve; referenced from peer coordinates. Not duplicated as separate L1 cells. | `CR-DEA-BC-04 R-005` |
| C3 | Partner Management dual-home | Primary at customer-demand x conceive; supply-side operation is legitimate participation. | `CR-DEA-BC-04 R-001` |
| C4 | Resilience, Innovation, Analytics | Resilience at governance-existence x improve; Innovation at product-offering x conceive; Analytics at operations-delivery x operate. Recorded once at primary coordinate. | `CR-DEA-BC-04 R-006`, `R-007`, `R-008` |
| C5 | Marketing placement | Marketing is distinct from Customer Management. Customer-demand x conceive carries Marketing; customer-demand x operate carries Customer Relationship Management. | `CR-DEA-BC-04 N-002` |

## 6. Deferral Reasons (full list)

- governance-existence x activate: activation is typically modelled under operations-delivery x activate; governance activation is an attribute of governance operate.
- governance-existence x retire: governance retirement is rare and largely an attribute of operating-model retirement.
- supply-resources x retire: retirement of supply and asset base is typically modelled under operations-delivery x retire with cross-reference.
- people-organization x activate: workforce activation is often an attribute of build (hire-and-onboard) or operate (deploy-on-assignment).
- people-organization x retire: workforce transition is often handled within HR operations.
- customer-demand x activate: first-time activation is mostly handled inside the L1 group Operate in practice.
- customer-demand x retire: customer exit is often handled within customer-relationship operations.
- product-offering x retire: offering retirement often overlaps with customer exit and asset retirement.
- operations-delivery x retire: operations retirement is often handled within the operate group with a winding-down workflow.
- finance-value x activate: period opening and finance cutovers are usually handled within Operate.
- finance-value x retire: financial wind-down is often handled within financial stewardship.

## 7. Process Group vs Business Function

Process Group and Business Function are distinct catalog-topology constructs. Process Group groups process responsibilities by a coherent process-architecture concern beneath a Process Context. Business Function groups capabilities by organizational function and ownership. They are not synonyms, not subtypes, not aliases. Where they share a name (e.g. Financial Management), the relationship is a `relates-to` reference, not an identity.

## 8. What this register does not decide

- the governance schema for L1 Process Group records (BP-12);
- the validator for L1 group composition and MECE (BP-12);
- the L2 admission waves for the seven domains (BP-13+);
- the ID-family reconciliation between `dea:bp-*` and `dea:process-*` (CR-BP-04, separate);
- the promotion of Process Group to OpenDEA Core (BP-14, future, conditional).

---

## Sources

[1] `technehub-labs/dea-catalog-processes/change-requests/CR-BP-03-business-process-architecture.md`
[2] `technehub-labs/dea-catalog-processes/change-requests/CR-BP-02.md`
[3] `technehub-labs/dea-catalog-processes/change-requests/CR-BP-03C-sample-process-contribution.md`
[4] `technehub-labs/dea-catalog-processes/entities/v1-alpha/dea_bp_manage-customer-relationship.yaml`
[5] `technehub-labs/dea-catalog-processes/docs/architecture.md`
[6] `technehub-labs/dea-metaframework/framework/domain-grounding.md`
[7] `technehub-labs/dea-metaframework/framework/lifecycle-grounding.md`
[8] `technehub-labs/dea-metaframework/framework/matrix.md`
[9] `technehub-labs/dea-metaframework/specification/ecf-coordinates.md`
[10] `technehub-labs/dea-metaframework/REPORT.md`
[11] `technehub-labs/dea-catalog-business-capabilities/docs/research/ecf-overlay-v0.2.yaml`
[12] `technehub-labs/dea-catalog-business-capabilities/docs/research/normalization.yaml`
[13] `technehub-labs/dea-catalog-business-capabilities/docs/research/candidates.yaml`
[14] `technehub-labs/dea-catalog-business-capabilities/entities/v1-alpha/capability-*.yaml`
[15] APQC Process Classification Framework 7.0 (cross-industry)
[16] TM Forum eTOM (Business Process Framework)
[17] BIAN Service Landscape (banking reference)
[18] ASCM SCOR Digital Standard (supply chain)
[19] ITIL 4 Service Value System
[20] ISO 37000:2021 Governance of Organizations
[21] ISO 22301:2019 Security and Resilience
[22] ISO 56002:2019 Innovation Management