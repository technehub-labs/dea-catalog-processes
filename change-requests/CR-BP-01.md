CR-BP-01 — Business Process Semantic Baseline

Status: Proposed for Approval and Implementation
Type: Foundational Semantic Alignment
Priority: P0
Programme: OpenDEA Business Process Architecture Evolution
Depends On: None
Blocks: CR-BP-02 through CR-BP-10

⸻

1. Change Summary

This Change Request establishes the authoritative semantic baseline for Business Process across OpenDEA.

The current OpenDEA ecosystem contains evidence of terminology and metadata divergence, including references to:

* Process
* BusinessProcess
* dea:entity-process
* dea:BusinessProcess

and inconsistent catalog metadata concerning the metamodel version, entity identifier, and architectural layer.

CR-BP-01 resolves these inconsistencies before any extension of the Business Process Architecture.

The fundamental decision is:

dea:BusinessProcess is the sole canonical OpenDEA semantic identity for the Business Process concept.

No new generic Process entity will be introduced.

⸻

2. Problem Statement

The Business Process Catalog is intended to become a foundational OpenDEA repository. It cannot safely evolve while its semantic anchor is ambiguous or inconsistent.

The current state creates several risks:

Inconsistent terminology
        │
        ▼
Inconsistent identifiers
        │
        ▼
Schema ambiguity
        │
        ▼
Catalog divergence
        │
        ▼
Cross-repository integrity risk

The immediate problem is therefore not a lack of process content.

It is the lack of an explicitly reconciled semantic baseline from which all subsequent Business Process Architecture work can proceed.

CR-BP-01 addresses this before:

* Process Context is introduced;
* ECF contextualization is formalized;
* decomposition levels are defined;
* Activity semantics are considered;
* workflow boundaries are established;
* validation rules are implemented; or
* substantial catalog population begins.

⸻

3. Architectural Context

The normative OpenDEA Metamodel is the semantic authority.

The governing architecture is:

OpenDEA Normative Metamodel
            │
            │ defines
            ▼
     dea:BusinessProcess
            │
            │ governs
            ▼
Business Process Semantics
            │
            ├───────────────┐
            ▼               ▼
    Derived Schemas     Catalog Model
            │               │
            └───────┬───────┘
                    ▼
          Repository Content

The Business Process Catalog must conform to this direction.

The catalog must not establish a parallel semantic authority.

⸻

4. Objectives

CR-BP-01 has six objectives.

O1 — Establish Canonical Identity

Formally confirm:

Canonical Entity ID:
dea:BusinessProcess

⸻

O2 — Establish Canonical Terminology

The canonical display name is:

Business Process

The term:

Process

may be used only as:

* natural-language shorthand;
* contextual terminology;
* a legacy reference where explicitly mapped; or
* part of another defined concept.

It must not be used as a competing canonical entity identity.

⸻

O3 — Reconcile Legacy Identifiers

Explicitly map known legacy identifiers and terminology.

Initial reconciliation target:

Legacy Reference	Canonical Resolution
dea:entity-process	dea:BusinessProcess
Process	Business Process where referring to the canonical concept
legacy catalog entity references	dea:BusinessProcess

Legacy identifiers must remain traceable where backward compatibility requires them.

They must not remain ambiguous.

⸻

O4 — Align Repository Metadata

The Business Process Catalog must consistently identify:

Metamodel Entity:
dea:BusinessProcess

and must derive its metamodel version from the approved normative source.

No independently maintained or stale metamodel version should remain in catalog metadata.

⸻

O5 — Confirm Architectural Placement

Business Process remains aligned with:

L3 — Business Operating Model

and its normative architectural placement as defined by the OpenDEA Metamodel.

The catalog must not independently redefine its layer.

⸻

O6 — Establish the Semantic Starting Point

CR-BP-01 establishes the baseline from which the subsequent CR series can safely evolve:

CR-BP-01
    │
    ├──► CR-BP-02 — Process Context
    │
    ├──► CR-BP-03 — Process Decomposition
    │
    ├──► CR-BP-04 — Business Activity
    │
    └──► Subsequent Process Architecture CRs

⸻

5. Scope

In Scope

CR-BP-01 includes:

5.1 Normative Identity Confirmation

Confirmation of:

dea:BusinessProcess

as the canonical entity.

5.2 Terminology Reconciliation

Alignment of:

* Business Process;
* Process;
* legacy entity names;
* legacy identifiers.

5.3 Catalog Metadata Alignment

Update of repository metadata, including:

* README references;
* metamodel pointers;
* schema references;
* entity identifiers;
* architectural layer declarations;
* version references.

5.4 Legacy Compatibility Mapping

Establishment of an explicit compatibility mapping where legacy identifiers remain relevant.

5.5 Baseline Documentation

Creation of a traceable semantic baseline for downstream CRs.

⸻

Out of Scope

CR-BP-01 explicitly does not:

* redefine Business Process semantics;
* introduce Process Context;
* introduce Process Scope;
* introduce Process Group;
* introduce Business Activity;
* introduce Process Task;
* change Workflow or Task semantics;
* define L0–L4 decomposition;
* implement MECE validation;
* populate the ECF matrix;
* add substantial Business Process content.

Those concerns belong to subsequent CRs.

This restriction is intentional.

⸻

6. Normative Semantic Decision

Decision BP-01-D01

The canonical OpenDEA Business Process entity is:

dea:BusinessProcess

The canonical display name is:

Business Process

The entity remains governed by the normative OpenDEA Metamodel.

⸻

Decision BP-01-D02

No generic normative entity named:

dea:Process

will be introduced as part of this change.

This avoids creating two entities that could represent the same enterprise concept.

⸻

Decision BP-01-D03

Legacy references must resolve explicitly.

Conceptually:

Legacy Reference
       │
       │ canonicalizes to
       ▼
dea:BusinessProcess

A compatibility mapping must distinguish:

deprecated identity

from:

alternative natural-language label

The two are not equivalent.

⸻

7. Canonical Definition

CR-BP-01 does not change the current normative definition.

The current baseline remains:

A structured set of activities that produces a defined outcome.

This is deliberately retained unchanged in CR-BP-01.

The adequacy and strengthening of this definition will be addressed by the Business Process Conformance Profile work, currently planned as CR-BP-06.

This separation prevents CR-BP-01 from becoming both a reconciliation CR and a semantic redesign CR.

⸻

8. Required Repository Changes

8.1 OpenDEA Metamodel

The implementation must verify that the normative model consistently exposes:

dea:BusinessProcess

as the canonical identity.

If legacy aliases are retained, they must be represented explicitly as legacy mappings and not as parallel canonical entities.

Expected conceptual pattern:

entity:
  id: dea:BusinessProcess
  name: Business Process
  status: normative
legacy_identifiers:
  - dea:entity-process
legacy_names:
  - Process

The exact implementation structure must conform to the existing metamodel conventions rather than introducing an unrelated pattern.

⸻

8.2 Business Process Catalog

The catalog metadata must be reconciled.

Replace inconsistent references

Any canonical reference such as:

dea:entity-process

must resolve to:

dea:BusinessProcess

Align terminology

The canonical repository subject is:

Business Process

Repository descriptions may use “process” conversationally but must not imply a separate canonical Process entity.

⸻

8.3 Metamodel Pointer

The metamodel-pointer.yaml must be aligned with the actual normative metamodel.

It should establish:

entity_id: dea:BusinessProcess

The version must correspond to the approved normative metamodel baseline rather than a stale independently maintained version reference.

Any legacy identifier should be expressed separately.

⸻

8.4 README

The architectural README developed during Phase 0 should become the conceptual entry point.

Its terminology must remain aligned with this CR.

The README must not:

* imply that Process is a separate entity;
* introduce L0–L4 as normative metamodel entities;
* redefine Business Function;
* redefine Workflow or Task.

Where future architecture is described, it should be clearly identified as intended or pending CR approval.

⸻

8.5 Schemas

Any catalog schema currently declaring or assuming:

dea:entity-process

must be updated to reference:

dea:BusinessProcess

The schema change must remain minimal.

CR-BP-01 should not introduce Process Context or decomposition constructs.

⸻

9. Legacy Compatibility Model

A controlled compatibility model should be introduced.

Conceptually:

                    Canonical
                        │
                        ▼
              dea:BusinessProcess
                        │
              ┌─────────┴─────────┐
              │                   │
              ▼                   ▼
        Legacy Entity         Legacy Label
      dea:entity-process         Process

The compatibility model should support:

* migration;
* existing references;
* repository history;
* validation;
* traceability.

However:

Legacy compatibility must not perpetuate semantic ambiguity.

Any new artifact must use:

dea:BusinessProcess

⸻

10. Acceptance Criteria

CR-BP-01 is complete only when all the following conditions are met.

AC-01 — Canonical Identity

The normative metamodel identifies:

dea:BusinessProcess

as the authoritative entity.

Expected Result: Pass.

⸻

AC-02 — Legacy Traceability

Known legacy identifiers have explicit resolution paths.

Expected Result:

dea:entity-process
        │
        ▼
dea:BusinessProcess

⸻

AC-03 — Catalog Alignment

The Business Process Catalog consistently references:

dea:BusinessProcess

in:

* metadata;
* schemas;
* README;
* pointers;
* examples.

Expected Result: No conflicting canonical entity ID remains.

⸻

AC-04 — Version Alignment

The catalog references an approved and identifiable normative metamodel baseline.

Expected Result: No stale or independently conflicting version declaration remains.

⸻

AC-05 — Layer Alignment

Business Process architectural placement is consistent across the normative model and catalog metadata.

Expected Result: No conflicting layer declaration remains.

⸻

AC-06 — No Semantic Expansion

The implementation introduces no new Business Process semantic concepts beyond reconciliation.

Specifically, no new:

* Process Context;
* Process Scope;
* Process Group;
* Business Activity;
* Process Task;
* decomposition level entity.

Expected Result: Pass.

⸻

AC-07 — Referential Validation

Automated validation confirms that canonical process references resolve to:

dea:BusinessProcess

and that no deprecated identifier is used as the canonical entity in new artifacts.

⸻

11. Implementation Plan

Step 1 — Freeze the Semantic Baseline

Record the authoritative normative model version and commit used for CR-BP-01.

Normative Repository
        │
        ▼
Normative Commit
        │
        ▼
CR-BP-01 Baseline

This prevents the implementation from drifting while the CR is executed.

⸻

Step 2 — Repository Reference Inventory

Perform a repository-wide search across the relevant OpenDEA repositories for:

dea:entity-process
dea:BusinessProcess
Process
Business Process

Classify every occurrence as:

* canonical;
* legacy;
* natural language;
* generated;
* schema;
* documentation;
* compatibility reference.

⸻

Step 3 — Define the Compatibility Mapping

Add or update the appropriate normative compatibility mechanism.

The implementation must follow existing OpenDEA conventions.

⸻

Step 4 — Align the Metamodel Pointer

Update the Business Process Catalog’s metamodel pointer to the canonical entity and approved baseline.

⸻

Step 5 — Align Schema References

Update only references required for semantic alignment.

No topology changes.

⸻

Step 6 — Align Documentation

Ensure the repository README, architecture documentation and metadata all use consistent terminology.

⸻

Step 7 — Add Validation

Introduce a validation check capable of detecting:

Invalid canonical entity:
dea:entity-process

in new or normative catalog artifacts.

Legacy mappings remain permitted only where explicitly declared.

⸻

Step 8 — Produce Implementation Evidence

The CR implementation should provide:

Changed Files
      │
      ├── Metamodel references
      ├── Catalog metadata
      ├── Schema references
      ├── Documentation
      └── Validation

and record the final commit or release baseline.

⸻

12. Validation Strategy

The initial validation can be simple.

For example:

RULE BP-01-001
IF:
  artifact declares canonical Business Process entity
THEN:
  entity_id MUST equal dea:BusinessProcess

And:

RULE BP-01-002
IF:
  entity_id equals dea:entity-process
THEN:
  artifact MUST declare explicit legacy compatibility
  OR validation fails

And:

RULE BP-01-003
New normative artifacts MUST NOT introduce
a canonical entity named Process
where Business Process is intended.

The exact rule representation should follow the existing OpenDEA validation architecture.

⸻

13. Risks

Risk	Mitigation
Hidden legacy references	Perform repository-wide inventory before modification
Breaking downstream references	Use explicit compatibility mapping
Metamodel version drift	Freeze the CR baseline
Semantic expansion	Enforce strict out-of-scope boundaries
Documentation/schema divergence	Validate all canonical references
Premature topology design	Defer L0–L4 work to subsequent CRs

⸻

14. Non-Goals

CR-BP-01 will not determine:

What is a Process Context?

That belongs to CR-BP-02.

It will not determine:

How are Business Processes decomposed?

That belongs to CR-BP-03.

It will not determine:

What is a Business Activity?

That belongs to CR-BP-04.

It will not determine:

Where does Workflow begin?

That belongs to CR-BP-05.

It will not determine:

How do we prove that something is a Business Process?

That belongs to CR-BP-06.

⸻

15. CR-BP-01 Completion State

Successful completion produces this baseline:

┌──────────────────────────────────────┐
│ OpenDEA Normative Metamodel          │
│                                      │
│ Canonical Entity                     │
│                                      │
│      dea:BusinessProcess             │
└───────────────────┬──────────────────┘
                    │
                    │ governs
                    ▼
┌──────────────────────────────────────┐
│ Business Process Catalog             │
│                                      │
│ Canonical Reference                  │
│      dea:BusinessProcess             │
│                                      │
│ Legacy References                    │
│      Explicitly Mapped               │
└───────────────────┬──────────────────┘
                    │
                    ▼
          Ready for CR-BP-02

Recommended disposition

Approve CR-BP-01 for implementation as the first controlled change in the OpenDEA Business Process Architecture Evolution programme.

The implementation should remain deliberately narrow: reconcile and stabilize the semantic baseline, then stop.

Once CR-BP-01 is implemented and evidenced, the next change is CR-BP-02 — ECF Process Context, where the first substantive architectural extension begins.