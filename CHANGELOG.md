# Changelog

All notable changes to this repository are documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows
`docs/versioning.md`.

## [Unreleased]

### CR-BP-15-IMP Phase 5 first tranche (cd-b + cd-c)

The first two customer-demand tranches (4 records: 2 build + 2
conceive) have been reconciled to the CR-BP-14 canonical contract.
The disposition register is now PARTIALLY_LOCKED with 4 records
locked.

- `entities/v1-alpha/dea:process-customer-channel-and-acquisition-build/`:
  legacy `operational` intent -> canonical `operate`; legacy
  scalar `process_context: dea:pc-cd-b` -> canonical
  `context: [{ref: dea:pc-cd-b}]` block; legacy
  `process_audience: customer-demand` removed; canonical `serves`
  relationship toward `ecf:customerAndDemand.build` added;
  change_history entry appended.
- `entities/v1-alpha/dea:process-demand-generation-build/`: same
  migration as the cd-b peer (operate + dea:pc-cd-b + serves).
- `entities/v1-alpha/dea:process-customer-strategy-conception/`:
  legacy `management` intent -> canonical `develop`; cd-c
  context; serves toward `ecf:customerAndDemand.conceive`.
- `entities/v1-alpha/dea:process-market-and-demand-conception/`:
  same migration as the cd-c peer.
- `reconciliation/diffs/phase-5-cd-b-cd-c.yaml` (new): per-tranche
  audit trail; 4 records touched; SHA-256 evolution recorded;
  cross-tranche observations.
- `reconciliation/dispositions/register.yaml`: register_status
  -> PARTIALLY_LOCKED; register_lock_progress records 4 locked
  records and 14 remaining.
- `schemas/entity.schema.json`: `process_audience` removed from
  the `required` list; the legacy field remains readable as a
  backward-compat alias (CR-BP-14 /19) but is no longer
  required for canonical entries.
- `scripts/apply_phase_5_tranche.py` (new): reproducible tranche
  migration script; supports `--self-test` (idempotence contract)
  and `--tranche <id>` for any of the 10 tranches; applies the
  full migration pattern (intent, audience removal, context
  block, serves relationship, change_history append).
- `tests/test_apply_phase_5_tranche.py` (new): 8 tests covering
  the migration script + per-record shape + idempotence + lock
  progress.
- `tests/test_reconciliation_baseline.py`: legacy_findings_present
  test updated to reflect the Phase 5 first-tranche lock (14
  remaining, not 18).

Programme position: CR-BP-14 still **Implemented**; CR-BP-15 +
CR-BP-15-IMP still **Proposed**; this PR is the fourth
CR-BP-15-IMP delivery and the first Phase 5 tranche migration.

BP-SEM live verdict: 14 errors (down from 18). The 4 migrated
records no longer trigger BP-SEM-007 (canonical context: block
required).

### CR-BP-15-IMP Phase 3-4: Disposition register + tranche plan

CR-BP-15 §28 (the ten dispositions) is now formalised; the 18
Business Processes in the canonical catalogue each receive a
preliminary RECLASSIFY disposition. The 18 records are grouped
into 10 tranches (one per Process Context) so future CR-BP-15-IMP
Phases 5-7 migrations are sequenced.

- `reconciliation/dispositions/schema.yaml` (new): the canonical
  disposition schema; 9 dispositions (RETAIN, RECLASSIFY, RENAME,
  SPECIALIZE, MERGE, SPLIT, MOVE, DEFER, RETIRE) each with
  required/optional fields, target_id requirement, and a
  rationale pattern; the reclassify_axes block documents the
  CR-BP-14 §17 migration mapping.
- `reconciliation/dispositions/register.yaml` (new, PRELIMINARY):
  18 disposition entries (one per Business Process); every
  entry is RECLASSIFY at this stage because every record carries
  the documented legacy fields; rationale + evidence recorded
  per entry; the register will be LOCKED in CR-BP-15-IMP
  Phase 5 (PR-6 onward).
- `reconciliation/tranches/plan.yaml` (new): 10 tranches (cd-b,
  cd-c, cd-d, cd-im, cd-op, ge-b, ge-c, ge-d, ge-im, ge-op); two
  are flagged high-risk (ge-b: audience-vs-context; ge-op:
  cross-tranche references); per-tranche PR target, owner
  placeholder, and review checkpoints recorded.
- `reconciliation/README.md`: orientation block extended to
  describe Phases 3-4 layout and Phase 5-7 roadmap.
- `scripts/check_dispositions.py` (new): disposition validator
  with --self-test; checks that every record has exactly one
  disposition entry, that every disposition id is canonical,
  that RECLASSIFY changes conform to the CR-BP-14 axes and
  vocabularies, that context targets resolve to the Process
  Context register, and that the tranche plan covers every
  disposition entry.
- `tests/test_dispositions.py` (new): 9 tests covering the
  disposition validator + register + tranche plan.
- `.github/workflows/ci.yml`: Disposition register step added
  (advisory until the register is LOCKED).

Programme position: CR-BP-14 still **Implemented**; CR-BP-15 +
CR-BP-15-IMP still **Proposed**; this PR is the third
CR-BP-15-IMP delivery.

### CR-BP-15-IMP Phase 1-2: Inventory + immutable baseline

CR-BP-15 §6 / §7 (existing-population reconciliation) is now
seeded. The Phase 1 inventory enumerates every canonical record at
the moment CR-BP-14 was declared Implemented; the Phase 2 baseline
freezes each record's SHA-256 so future tranches can diff exactly
which bytes were touched.

- `reconciliation/inventory.yaml` (new): 18 Business Processes +
  10 Process Groups + 10 Process Contexts + 4 Change Requests
  (CR-BP-14, CR-BP-15, CR-BP-15-IMP, CR-BP-16); per-record
  metadata + `legacy_findings` (BP-SEM raw findings on each
  record).
- `reconciliation/baseline/v1.yaml` (new): immutable SHA-256
  snapshot of every record's file contents; baseline_version = v1;
  baseline_commit = 816c63b (CR-BP-14 Implemented); baseline_at =
  2026-09-06.
- `reconciliation/README.md` (new): orientation for visitors;
  layout, phase progression, STRUCT conformance reference.
- `scripts/build_inventory.py` (new): reproducible generator;
  `--self-test --strict` asserts byte-identity with committed
  files; supports `--out` for diff scenarios.
- `scripts/check_struct.py` (new, decision D6): STRUCT conformance
  check that flags unknown top-level entries; intentionally
  permissive (the catalogue's contracts own schema integrity);
  wired into CI as an advisory step.
- `tests/test_reconciliation_baseline.py` (new): 9 tests covering
  inventory regeneration, baseline SHA-256 integrity, and STRUCT
  typo detection.
- `.github/workflows/ci.yml`: STRUCT conformance step added
  between Legacy Migration gate and Process Semantics gate.

Programme position: CR-BP-14 still **Implemented**; CR-BP-15 +
CR-BP-15-IMP still **Proposed**; this PR is the first CR-BP-15-IMP
delivery.

### CR-BP-14 Phase 4: Documentation reconciliation (Implemented)

CR-BP-14 §22 is now satisfied. The repository prose reflects the
CR-BP-14 semantic contract; legacy vocabulary references are
reconciled to the canonical forms or marked historical; no
superseded semantic contract remains presented as normative.

- `docs/architecture.md`: oriented (links to the semantic-contract
  and governance documents); L0/L1/L2 narratives rewritten to the
  CR-BP-14 §6 / §7 definitions; Process Group confirmed as catalog-
  owned, not a metamodel entity; See-also expanded.
- `docs/identity.md`: identity-independence clause added (CR-BP-14
  §15); BP-ARC-ID-004 cross-check note clarifies its distinction from
  BP-SEM-003/004; See-also expanded; broken `../../` link defect
  swept.
- `docs/classification.md`: front matter records the CR-BP-14 §10 /
  §11 formal separation; the canonical `classifications/process-intents.yaml`
  link is now correct (the pre-existing `../../classifications` link
  defect is swept); See-also expanded.
- `docs/relandscape.md`: See-also expanded with the semantic-
  contract document and the BP-SEM validator; CR-BP-14 §24
  admission-freeze reference added; broken `../../` link defect
  swept.
- `docs/context.md` (new): Process Context as canonical placement
  (CR-BP-14 §5, §13, §20); the canonical `context:` block;
  multiplicity rule; the Process Context register at
  `contexts/v1-alpha/`; relationship to BP-SEM-007 and BP-SEM-008.
- `docs/specialization.md` (new): specialization as semantic
  refinement (CR-BP-14 §12); approved specialization bases;
  specialization vs decomposition; canonical form; identity
  independence (BP-SEM-009).
- `README.md` §2 (Process Architecture): the four-axes table is
  replaced with the CR-BP-14 axes (Intent / Classification /
  Specialization / Context); the obsolete `Audience` axis is replaced
  by the canonical `context:` block; §8 No Breaking Changes explains
  the migration-period field aliasing.

Register close-out: **CR-BP-14 -> Implemented** (the constitutional
phase is complete; CR-BP-15-IMP owns the existing-population
migration; CR-BP-16 owns the permanent gate).

### CR-BP-14 Phase 3: BP-SEM-001..012 Process Semantics gate

- `scripts/check_process_semantics.py` (new): implements BP-SEM-001
  (Intent Vocabulary), BP-SEM-002 (Classification Vocabulary),
  BP-SEM-003/004 (Intent/Classification Independence by construction),
  BP-SEM-005 (Specialization Validity), BP-SEM-006 (Specialization
  Differentiation), BP-SEM-007 (Context Distinction), BP-SEM-008
  (Context Reference Integrity), BP-SEM-009 (Identity Independence by
  construction), BP-SEM-010 (Legacy Detection), BP-SEM-011
  (Classification Collision, advisory), BP-SEM-012 (Context
  Multiplicity, advisory). Each finding carries a deterministic
  `rule:<code>` prefix; warnings never block unless `--strict`.
- `--self-test` exercises every BP-SEM rule on a broken fixture and
  asserts the fixed fixture is blocking-free with the expected advisory
  findings.
- Wired into CI as an advisory step between the legacy migration gate
  and the process group gate (`--strict || true`): the current
  canonical population carries CR-BP-14 S24 admission-freeze findings
  (legacy process_intent, legacy scalar process_context, missing
  canonical `context:` block, legacy process_audience); the validator
  surfaces them and CR-BP-15-IMP Phases 8..10 reduces them.
- New `tests/test_check_process_semantics.py` (16 tests) locks the
  self-test, docstring coverage of every code, and the live/strict
  verdict contract.
- The live run finds: 18 entries missing the canonical `context:`
  block (BP-SEM-007); all 18 carry legacy `process_intent` or legacy
  `process_audience` (BP-SEM-010); all 18 carry the legacy scalar
  `process_context` (BP-SEM-010). These are exactly the seed findings
  already documented in the CR-BP-14/15/16 programme plan.

### CR-BP-14 Phase 2: Process Context block and contextual relationships

- `context:` block added to `schemas/entity.schema.json` and
  `schemas/contribution.schema.json` (CR-BP-14 §13, §20): an array of
  `{ref: dea:pc-*}` Process Context references; multiple contexts are
  permitted where evidence justifies them (BP-SEM-012).
- `relationship_type` enum extended with `serves` and `contributes-to`
  (both admitted by the metamodel relationship registry; catalog-governed
  extension, no metamodel CR required). `operates-within` is deliberately
  absent: its semantics are carried by the `context:` block.
- `target_id` now admits canonical ECF identifiers
  (`ecf:<lowerCamelDomain>[.<lowerCamelStage>]`, the CG-003 form)
  alongside entity ids; the entity-id branch excludes the `ecf:` prefix
  so the kebab-case label form is rejected (consistent with CG-004 §10).
- Contribution template updated: the canonical `context:` block replaces
  the pre-CR-BP-14 `process_context` scalar; a `serves` relationship
  example toward an ECF coordinate is included.
- New `tests/test_process_context_relationships.py` (16 tests) locks the
  block shape, enum extension, target patterns, and backward
  compatibility of all existing canonical entries.
- Recorded for CR-BP-15-IMP Phase 10: existing entries carry a legacy
  scalar `process_context` field that predates the canonical block; the
  schema remains permissive toward it until the audience/context
  migration.

### CR-BP-15 + CR-BP-16 landing and knowledge harvest

- CR-BP-15 (Process Catalog Reconciliation) and CR-BP-16 (Process
  Catalog Conformance Gate, carrying CR-BP-15-IMP) landed verbatim at
  `change-requests/CR-BP-15-process-catalog-reconciliation.md` and
  `change-requests/CR-BP-16-process-catalog-conformance-gate.md`.
- New visitor-facing documentation distilled from the CR lineage:
  `docs/semantic-contract.md` (the semantic constitution: six
  characterization dimensions, controlled vocabularies, the normative
  separations) and `docs/governance/reconciliation-programme.md` (the
  closed governance loop, CR lineage, reconciliation dispositions,
  conformance levels, repository status model).
- README gains a "Reading This Repository" orientation block.
- CR register + README change programme: CR-BP-15 and CR-BP-16 rows
  added as Proposed; CR-BP-14 row updated to reflect Phase 1 (PR #26).

### CR-BP-14: Process Semantic Reconciliation (landing + Phase 1)

Landing (PR #25):
- CR landed verbatim at
  `change-requests/CR-BP-14-process-semantic-reconciliation.md`.
- CR register synchronized with actual status (CR-BP-14 §23): CR-BP-13b
  corrected to Merged (PR #24); README change programme rows synced for
  CR-BP-03/03A/03C/04/11/12/13/13a/13b; stale Activity Model / Execution
  Boundary placeholders renumbered as unnumbered future rows.

Phase 1 (semantic vocabularies + schema; CR-BP-14 §9, §10, §11, §17, §18, §20):
- New controlled vocabulary `classifications/process-intents.yaml`: the
  seven-value purpose-oriented Process Intent vocabulary (govern / manage /
  operate / deliver / support / develop / transform) with the §17 legacy
  migration mapping (operational -> operate or deliver; support -> support;
  management -> manage or govern; evidence-based, never mechanical).
- `schemas/entity.schema.json`: `process_intent` enum extended to the
  canonical seven values with legacy `operational` / `management` retained
  as deprecated migration aliases; new optional `process_classification`
  block (canonical form per §20); `process_type` retained unchanged as the
  landscape classification and backward-compatible alias (§18);
  `process_audience` marked as legacy migration alias (§13, §19).
- `schemas/contribution.schema.json` mirrors the same extensions.
- `classifications/process-types.yaml` header records the CR-BP-14 §10
  Process Classification semantics and the Intent != Classification rule
  (§11; BP-SEM-011).
- `scripts/check_process_specialization.py` BP-SPEC-01-007 text updated to
  quote the extended intent vocabulary; non-promotion rule unchanged.
- `docs/classification.md` gains a CR-BP-14 Phase 1 status section; the
  pre-CR-BP-14 prose is marked historical pending Phase 4 reconciliation.
- Contribution template updated to the canonical intent vocabulary with the
  optional `process_classification` block shown.
- New `tests/test_process_intents.py` locks vocabulary / schema mirror
  integrity.

### CR-CATALOG-STRUCT-02: Process Catalog Adoption (Three-Step Migration)

Brings `dea-catalog-processes` into conformance with the catalog repository
standard (CR-CATALOG-STRUCT-01).

Step 1 (layout):
- `entities/v1-alpha/dea:process-manage-customer-relationship/{research,candidates,retired}/`
  subtree created; canonical file moved from `dea_bp_manage-customer-relationship.yaml`
  and renamed to canonical `dea:process-*` form (CR-BP-04).
- `entities/v1-alpha/dea:group-customer-lifecycle-management/{research,candidates,retired}/`
  subtree created; canonical file moved from `dea_group-customer-lifecycle-management.yaml`.

Step 2 (research distribution):
- `docs/research/l1-register.yaml`, `l1-candidate-universe.yaml`, `L1-REGISTER-v0.1.md`
  moved into `entities/v1-alpha/dea:group-customer-lifecycle-management/research/`
  (research is about L1 Process Groups; L1 entities own L1 evidence).
- `docs/research/` removed (empty after the move).
- Provenance `research/README.md` per subtree.

Step 3 (contribution flow):
- `contributions/processes/` intake queue and template kept as-is (catalog
  hosts one entity type; renaming is a future concern).

Catalog index + CI:
- `CATALOG.yaml` (machine-generated, 1.9 KB) committed.
- `TEMPLATE_VERSION` (`0.1.0`) written; matches the canonical template.
- `metamodel-pointer.yaml` extended with additive top-level metadata block
  (id/name/abbreviation/version/status/metamodel_version/description/owner);
  existing nested `metamodel:` and `catalog:` blocks unchanged.
- `scripts/regenerate_catalog.py`, `scripts/check_catalog_index.py`, and
  `catalog-index-schema/catalog-index-schema.json` vendored from
  `dea-metaframework/tools/` (CST-013/CST-014).
- `.github/workflows/ci.yml` updated to run the regenerator check, the
  gate, the per-file schema dispatch (with state-directory filter), the
  six existing catalog validators, and the cross-repo conformance suite.
- `scripts/check_ecf_conformance.py` fixed: skip files under
  `research/`, `candidates/`, `retired/` (state-directory files are not
  catalog entries and do not carry `ecfConformance`).

Verification:
- All 6 catalog validators PASS.
- Regenerator --check exits 0.
- Gate --strict exits 0.
- Conformance --strict: 16/16 CSTs passed, 0 warnings.
- Cross-repo contract satisfied; STRUCT-03..05 can adopt the same pattern.

### CR-BP-12: L1 Process Group Profile, Schema, and Validator

Lands the first-class Process Group record type. Process Group remains a catalog-owned record (NOT a metamodel entity). The canonical containment direction is `L1 group --composes--> L2 process`; the inverse `part-of` view is generated at query time per CR-002 §8 because the metamodel relationship-type enum does not currently admit `part-of`.

#### Added

- `schemas/entities/process-group.schema.json` — JSON Schema for Process Group entries. ID family: `dea:group-*` (CR-BP-04 §4).
- `classifications/process-group-kinds.yaml` — six-value controlled vocabulary (`end-to-end`, `functional`, `support`, `cross-cutting`, `governance`, `innovation`).
- `scripts/check_process_group.py` — validator enforcing PG-001..PG-008; includes `--self-test` mode.
- `entities/v1-alpha/dea_group-customer-lifecycle-management.yaml` — the first canonical Process Group record; promotes the `metadata.group` label that lived on `dea:process-manage-customer-relationship` into a governed first-class record with `process_group_kind: end-to-end`.
- New CI step in `.github/workflows/ci.yml` that runs `scripts/check_process_group.py` on every PR.

#### Changed

- `entities/v1-alpha/dea_bp_manage-customer-relationship.yaml` loses the `metadata.group` block; the Process Group is now an external first-class record referenced via the Process Group's `composes` array.

#### Not changed

- Existing Process Context (`dea:pc-cd-op`), classifications, contribution template, and contribution report workflow remain as PR #17 + #18 + #19 landed them.
- No Process Group promotion to the OpenDEA Core metamodel (CR-BP-14, future, conditional).
- Process Group kinds vocabulary is closed; additions require a CR-BP-12 minor revision.

### CR-BP-04: Business Process Identity & ID-Family Reconciliation

Documentation-first CR. Locks the four canonical ID families used by the
catalog (`dea:process-*`, `dea:pc-*`, `dea:group-*`, `dea:scope-*`) and the
legacy-migration `dea:bp:*` colon-separated family. Resolves the apparent
`dea:bp-*` versus `dea:process-*` drift by collapsing it to three intentional
roles: (1) legacy-migration reference inside `legacy_ids` arrays; (2) canonical
Business Process id on live entities and Process Context references;
(3) validator self-test fixture, used only to exercise failure paths inside
`scripts/check_legacy_migration.py` and `scripts/check_process_identity.py`.

#### Added

- `change-requests/CR-BP-04-id-family-reconciliation.md` (the CR; 13 sections;
  Design Specification tone; no en/em dashes; locks the colon-vs-dash
  distinction for the legacy family).
- New section **Canonical ID families (CR-BP-04 §4)** in `docs/identity.md`,
  restating the four-family contract verbatim.

#### Not changed

- No schema change. `schemas/entity.schema.json`, `schemas/contribution.schema.json`,
  and `schemas/entities/process-context.schema.json` already conform to the
  rule this CR documents.
- No validator change. `check_process_identity.py`, `check_process_context.py`,
  `check_legacy_migration.py`, and `check_ecf_conformance.py` already enforce
  the rule this CR documents.
- No entity change. No live catalog content uses the `dea:bp-*` dash form as
  a canonical identifier.
- No migration script. The `dea:bp-bad-*`, `dea:bp-parent`, and `dea:bp-child-*`
  validator fixtures remain as synthetic broken-input examples.

### CR-BP-11: L1 Process Group Discovery Across the 49 ECF Coordinates

Research-only register. Establishes a comprehensive L1 Process Group
discovery across the 7x7 ECF matrix (49 coordinates). Records an explicit
disposition per coordinate: 38 `accepted`, 11 `deferred`. Five cross-domain
findings are recorded once at their primary coordinate and referenced from
peer coordinates (Technology Management held unmapped; Change Management
cross-cutting at governance-existence x improve; Partner Management
dual-home at customer-demand x conceive; Resilience/Innovation/Analytics
at their primary coordinates; Marketing distinct from Customer Management).

The register is the input gate for CR-BP-12 (L1 Process Group profile +
schema + validator) and CR-BP-13..BP-19 (seven-domain admission tranches).
No canonical L1 records, no new schema, no new validator, no new CI
surface are added in this CR. The existing canonical L2 entry
(`dea:process-manage-customer-relationship`) remains the only canonical
Process entity in the catalog.

Process Group remains a catalog-owned record type, not an OpenDEA Core
metamodel entity. The canonical containment direction is
`L1 group --composes--> L2 process`; the inverse `part-of` is a derived
query view. Process Group and Business Function are explicit distinct
catalog-topology constructs (not synonyms, not subtypes, not aliases).

#### Added

- `change-requests/CR-BP-11-l1-process-group-discovery.md` (the CR;
  19 sections; Design Specification tone; no en/em dashes).
- `docs/research/l1-register.yaml` (the 49-coordinate disposition
  register; machine-readable; each coordinate carries process_context,
  l1_candidates, l2_candidates, in_scope, out_of_scope, evidence,
  disposition, deferral_reason).
- `docs/research/l1-candidate-universe.yaml` (the L1 candidate
  universe; 102 candidates across 49 coordinates; five cross-domain
  findings).
- `docs/research/L1-REGISTER-v0.1.md` (persona-readable summary).

#### Not changed

- Existing canonical entries under `entities/v1-alpha/`, `contexts/v1-alpha/`,
  `contributions/processes/`, `docs/examples/`, `schemas/`, `scripts/`,
  `classifications/`, `.github/workflows/` remain as PR #17 landed them.
- No `dea:bp-*` versus `dea:process-*` ID-family reconciliation happens
  here; that is a separate CR-BP-04.

### CR-BP-03C: Sample Business Process Contribution (walk-the-flow)

Lands the **first** Business Process entry in the catalog,
walking the full CR-BP-03 / CR-BP-03A / CR-BP-02 flow
end-to-end. The sample entry — `dea:bp:manage-customer-relationship`
("Manage Customer Relationship") — exercises every part of
the machinery:

  - 4-axis classification (intent / type / specialization /
    audience), all populated.
  - Process Identity contract (verb + object + outcome +
    evidence; BP-ARC-ID-001..005 PASS).
  - Canonical relationships (array-of-relationship-instances
    per metamodel relationship-instance.json; one realizes
    relationship to `dea:entity-capability:manage-customer-relationship`).
  - L0/L1/L2 conceptual hierarchy (Scope and Group recorded
    in metadata; NOT promoted to separate catalog entities
    per CR-BP-03 §3).
  - Process Context reference (the entry belongs to the
    CustomerAndDemand × Operate cell at
    `dea:pc-cd-op`).
  - ECF Conformance Gate (inherits-catalog; canonical
    references resolve to `ecf:customerDemand.operate`;
    extensions declare `doesNotRedefine: true`).
  - Process Identity validator: case-insensitive + doubled-
    parentheses-tolerant fuzzy match (`_fuzzy_name_match`).

#### Added

- `change-requests/CR-BP-03C-sample-process-contribution.md`
  (md5 `0504cbca05a1875aac02137c959b7cab`; byte-identical to
  working folder `/home/hermes/dea-work/process/00_inbox/`).
- `entities/v1-alpha/dea_bp_manage-customer-relationship.yaml`
  (the canonical BP entry; first entry in the catalog;
  id `dea:process-manage-customer-relationship`).
- `contexts/v1-alpha/dea_pc-cd-op.yaml` (the Cell Charter for
  CustomerAndDemand × Operate; first Cell Charter in the
  catalog).
- `contributions/processes/dea_bp_manage-customer-relationship.yaml`
  (the contribution record; first contribution in the catalog).
- `contributions/processes/dea_bp_manage-customer-relationship.report.md`
  (the generated reclassification report; status=PASS,
  zero recommendations).
- `docs/examples/README.md` (introduction to the worked-
  examples directory).
- `docs/examples/manage-customer-relationship.md` (the
  worked example; future contributors should treat this
  as the canonical pattern).

#### Changed

- `scripts/check_process_identity.py`:
  - `_fuzzy_name_match` extended to be case-insensitive
    (entry names are conventionally Title Case; identity
    sub-block is conventionally lowercase).
  - `_fuzzy_name_match` extended to normalize doubled
    parentheses (e.g. `((all customer segments))` produced
    by wrapping a scope like `(all customer segments)`).
  - BP-ARC-ID-001: when the scope is already parenthesized,
    the validator does not wrap it again.
- `.github/workflows/process-contribution-report.yml`:
  - Reclassification report generator upgraded (CR-BP-03C §7)
    to cross-check the proposed_entry against BP-ARC-ID-001..005
    and emit a confidence-scored recommendation.
  - Includes migration check (BP-MIG-001..005) in the report
    pipeline.

#### Validators exercised (all PASS)

| Validator | Result |
|---|---|
| `check_process_identity.py` (BP-ARC-ID-001..005) | PASS |
| `check_process_identity.py --self-test` | PASS |
| `check_process_specialization.py` (BP-SPEC-01-001..007) | PASS |
| `check_process_context.py` (PC-001..PC-008) | PASS |
| `check_legacy_migration.py` (BP-MIG-001..005) | PASS |
| `check_legacy_migration.py --self-test` | PASS |
| `check_ecf_conformance.py` | PASS (1 entry conforms) |
| `validate_consumer.py` against `dea-architecture-framework@v0.6.0` | PASS |
| `jsonschema.validate(canonical_entry, entity_schema)` | PASS |
| `jsonschema.validate(cell_charter, process-context_schema)` | PASS |
| `jsonschema.validate(contribution, contribution_schema)` | PASS |
| Report generator (CR-BP-03C §7) | Generated report with status=PASS, 0 recommendations |

### CR-BP-03A: Legacy Field Migration

Resolves three issues with the CR-BP-03 schema that came to
light during implementation:

1. **`relationships` shape corrected** to array-of-relationship-
   instances (per the metamodel's `relationship-instance.json`).
   The CR-BP-03 shape was a structured object with
   `composes` / `realizes` keys; the authoritative metamodel
   shape is a flat array of typed relationship instances with
   full CR-002 provenance, CR-6 lifecycle, and effective_from/to
   temporal validity.
2. **`parent_process` / `child_processes` REMOVED** from the
   catalog schema. These were catalog inventions from CR-BP-01
   (the wrong-premise implementation, since reverted); the
   metamodel's `process.json` does not declare them.
3. **`capabilities_delivered` soft-deprecated**. The metamodel
   still declares this as a simple array of strings (a
   backward-compat shim). CR-BP-03A keeps the field in the
   catalog schema but marks it as soft-deprecated; the canonical
   form is `relationships[relationship_type=realizes]` with
   full provenance.

#### Added

- `change-requests/CR-BP-03A-legacy-migration.md` (md5
  `3e4a951008bf28e0b7d3bd325bcc2949`; byte-identical to working
  folder `/home/hermes/dea-work/process/00_inbox/`).
- `scripts/check_legacy_migration.py` — the migration validator
  enforcing BP-MIG-001..005 (with built-in `--self-test`).

#### Changed

- `schemas/entity.schema.json`:
  - `relationships` shape corrected to array-of-relationship-
    instances; each entry has `source_id`, `target_id`,
    `relationship_type`, plus optional `direction`, `status`,
    `effective_from`/`to`, `asserted_by`, `rationale`, `evidence`,
    and `provenance`.
  - `parent_process` and `child_processes` REMOVED.
  - `capabilities_delivered` retained but documented as
    soft-deprecated; the canonical form is
    `relationships[relationship_type=realizes]`.
- `schemas/contribution.schema.json` — `proposed_entry.relationships`
  shape updated to match the metamodel relationship-instance
  shape (array of instances).
- `contributions/processes/PROCESS-CONTRIBUTION-TEMPLATE.yaml` —
  template updated with the relationship-instance shape.
- `docs/architecture.md` — "Structural composition" and
  "Capability realization" sections updated to reflect the
  metamodel-aligned shape; new "The `relationships` shape"
  and "Legacy field migration" sections added.
- `docs/relandscape.md` — "The `relationships` field" and
  "The legacy fields" subsections added.
- `.github/workflows/ci.yml` — adds the Legacy Migration gate
  step (after the Process Identity gate).
- `change-requests/README.md` — CR-BP-03A row added.

#### Architecture-only (no file changes)

- The catalog now aligns with the metamodel's relationship-
  instance shape. Each relationship carries full provenance,
  lifecycle, and temporal validity.
- The catalog's `entities/v1-alpha/` is empty by design
  (CR-BP-02 §22), so the migration validator is forward-looking
  on future entries.

### CR-BP-03: Business Process Architecture

Lands the **4-axis classification**, **process-identity contract**,
and **contribution-driven re-landscape** mechanism on top of
CR-MM-PROC-01 + CR-AR-FMWK-01 + CR-BP-SPEC-BP-01 + CR-BP-02.

**No breaking changes.** CR-BP-03 introduces new fields additively;
existing entries continue to validate. The L0/L1/L2 hierarchy is a
**conceptual model** (not separate top-level directories).

#### Added

- `change-requests/CR-BP-03-business-process-architecture.md`
  (md5 `85697440a09102165099e4f67650b635`; byte-identical to working
  folder `/home/hermes/dea-work/process/00_inbox/`).
- `classifications/process-types.yaml` — the 5-value Mintzberg
  vocabulary with primary organizational component + primary
  purpose for each.
- `classifications/process-specializations.yaml` — the
  catalog-level specialization pattern vocabulary
  (by-customer-segment / by-region / by-product-line / by-tier /
  by-compliance-regime) with worked examples.
- `schemas/identity.schema.json` — the process-identity sub-block
  schema (verb + object + scope + outcome_statement +
  evidence_links). Mirrored inline in
  `schemas/entity.schema.json` to avoid a remote `$ref`.
- `schemas/contribution.schema.json` — the process-contribution
  schema (the input shape for `contributions/processes/`).
- `contributions/processes/PROCESS-CONTRIBUTION-TEMPLATE.yaml` —
  the template contributors copy + fill in.
- `contributions/processes/README.md` — the contribution flow
  documentation.
- `scripts/check_process_identity.py` — process-identity validator
  enforcing BP-ARC-ID-001..005 (with built-in `--self-test`).
- `docs/architecture.md` — the L0/L1/L2 structural architecture
  narrative.
- `docs/classification.md` — the 4-axis classification narrative.
- `docs/identity.md` — the process-identity contract narrative.
- `docs/relandscape.md` — the contribution-driven re-landscape
  mechanism.
- `docs/conformance.md` — the conformance gates summary.
- `validation/conformance/README.md` — forward-looking alias for
  the catalog's conformance validation.
- `.github/workflows/process-contribution-report.yml` — CI
  workflow for contribution-driven re-landscape (PRs to
  `contributions/processes/`).

#### Changed

- `schemas/entity.schema.json` — adds the new fields
  additively:
    - `process_type` (5-value enum; default `core`).
    - `process_specialization` (list of parent process ids).
    - `specialization_pattern` (free-text pattern label).
    - `relationships.{composes, realizes}` (canonical OpenDEA
      form).
    - `identity` (inline sub-schema mirroring
      `schemas/identity.schema.json`).
  - The id pattern is loosened to allow two-colon ids
    (`dea:bp:...`); the existing one-colon pattern still matches.
  - All existing fields are preserved; the legacy
    `parent_process` / `child_processes` / `capabilities_delivered`
    are documented as preserved migration aliases.
- `.github/workflows/ci.yml` — adds the Process Identity gate
  step (after the Process Context gate).

#### Architecture-only (no file changes)

- The 4-axis classification (intent / type / specialization /
  audience) is documented in `docs/classification.md` and
  `README.md`. Existing fields (`process_intent`,
  `process_audience`) are preserved; new fields (`process_type`,
  `process_specialization`) are added alongside.
- The L0/L1/L2 hierarchy is conceptual, documented in
  `docs/architecture.md` and `README.md`. There are no separate
  top-level directories for L0 / L1 / L2 entries.
- The re-landscape mechanism is contribution-driven, not
  in-tree. A re-landscape suggestion is generated by the
  contribution report workflow and reviewed by a catalog
  maintainer; the catalog does not auto-rewrite.

### CR-BP-02: Establish Process Context

Lands the **Process Context register + Cell Charter schema** on top of
the kernel + specialization discipline established by CR-MM-PROC-01 +
CR-AR-FMWK-01 + CR-BP-SPEC-BP-01.

**Authority chain (CR-BP-02 depends on the kernel + specialization
tranche):**

- `1665209` — CR-MM-PROC-01 merged on `dea-metamodel` (kernel + specialization).
- `76463b2` — CR-AR-FMWK-01 merged on `dea-architecture-framework` (root model v0.5.0 → v0.6.0).
- `1e4b916` — CR-BP-SPEC-BP-01 merged on `dea-catalog-processes` (Business Process specialization).
- `cb1a410` — CI hotfix (validate-allocation pin v0.2.1 → v0.6.0).
- `v0.6.0` — OpenDEAM root model tag published.

#### Added

- `change-requests/CR-BP-02.md` (md5 `9a56f5b0fc351c23416c51d216d805ef`; byte-identical to working folder `/home/hermes/dea-work/process/00_inbox/CR-BP-02.md`; refined to depend on the kernel + specialization tranche and to re-anchor PC-007/008/AC-07 to the corrected canonical ids).
- `schemas/entities/process-context.schema.json` — the canonical Process Context + Cell Charter schema. References the authoritative ECF vocabulary (CR-ECF-003/004/005) without redefining it.
- `scripts/check_process_context.py` — Process Context validator enforcing PC-001..PC-008 (with built-in `--self-test`).
- `contexts/v1-alpha/README.md` — placeholder documenting that the 49-cell matrix is **empty by design** per CR-BP-02 §22.

#### Changed

- `.github/workflows/ci.yml` — adds the Process Context gate step (after the Business Process specialization gate).
- `README.md` — "Canonical Process Context" section updated to reference the new Process Context Register at `contexts/v1-alpha/`, the schema, and the validator; adds an explicit "Process Context ≠ Business Process" callout.
- `change-requests/README.md` — CR-BP-02 row added.

**Out of scope (gated on its merge):** CR-BP-03 (L0/L1 decomposition
semantics); CR-BP-04 (Activity); CR-BP-05 (Workflow/Task); CR-BP-06
(Business Process criteria); CR-BP-07 (cross-context relationships);
CR-BP-08 (MECE within contexts); CR-BP-09 (Process Discovery
execution); CR-BP-10 (49-cell matrix population).

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