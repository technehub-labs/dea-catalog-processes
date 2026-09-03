# Changelog

All notable changes to the OpenDEA Business Process Catalog are
documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]: CR-BP-01 Business Process Semantic Baseline

First CR of the OpenDEA Business Process Architecture Evolution
programme. Establishes the authoritative semantic baseline; no
catalog population; no Process Context, L0-L4 decomposition, or
ECF contextualization work (those belong to CR-BP-02+).

### Added
- **`change-requests/CR-BP-01.md`** — CR document, verbatim
  (md5 `d71bdc34f771fc28f4af24f57ee81bb0`).
- **`scripts/check_bp01_canonical.py`** — validator enforcing
  BP-01-001 / BP-01-002 / BP-01-003; stdlib only; built-in self-test.
- **`docs/governance/canonical-identity-business-process.md`** —
  ratification of the canonical-identity decision; what the
  validator enforces; legacy-compatibility migration model.
- **`.github/workflows/ci.yml` step**: "Run CR-BP-01 canonical-identity
  validator" runs after the ECF conformance gate on every push/PR.

### Changed
- **`metamodel-pointer.yaml`** — `entity_id` corrected from
  `dea:entity-process` to `dea:BusinessProcess`; new
  `legacy_identifiers:` block preserves `dea:entity-process` as an
  explicit compatibility mapping; new `change_request` and
  `governance_decision` links; pointer version corrected from
  `v0.2.1` (dea-architecture-framework root model) to `v0.6.0`
  (the actual metamodel baseline).
- **`README.md`** — "Current Status" section now carries the
  canonical-identity statement with a link to the governance doc.
- **`change-requests/README.md`** — CR-BP-01 row added; CR-ECF-CG-004
  status corrected from "Proposed (this PR)" to "Implemented
  (PR #5 + PR #6 merged 2026-09-01)"; CG-005/006 cross-repo pointer
  rows added.

### Preserved (no change)
- `schemas/entity.schema.json` — entry id-pattern remains lowercase
  (sibling capability catalog precedent); the canonical entity id
  lives in `metamodel-pointer.yaml`, not in catalog entries.
- `entities/v1-alpha/` — empty by design (Phase 2 deferred).
- `scripts/check_ecf_conformance.py` — unchanged; CR-BP-01 runs
  after it.
- The catalog's ECF conformance posture (`dea:ecf@1.0.0`,
  CONFORMANT-WITH-EXTENSION) is unchanged; CR-BP-01 is reconciliation
  only and does not touch the ECF extension declarations.