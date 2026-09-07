# CR-BP-15-IMP Phase 1-2: Inventory + immutable baseline + STRUCT conformance

## Summary

Seeds CR-BP-15 §6 / §7 (the existing-population reconciliation
scope) with the three artefacts every reconciliation tranche needs:

- `reconciliation/inventory.yaml`: per-record metadata + raw
  BP-SEM findings for every canonical record (18 processes, 10
  process groups, 10 process contexts, 4 change requests).
- `reconciliation/baseline/v1.yaml`: immutable SHA-256 snapshot
  of every record, frozen at the moment CR-BP-14 was declared
  Implemented (commit `816c63b`).
- `scripts/check_struct.py` (STRUCT conformance, decision D6):
  flags unknown top-level entries so reconciliation scaffolding
  typos (e.g. `reconcilliation/`) cannot shadow a real directory.

No schema, validator, or entity changes. The CR-BP-14 §24
admission freeze remains in effect; this PR is scaffolding only.

## What this PR does

### Phase 1: inventory

- `reconciliation/inventory.yaml` enumerates every record in the
  canonical catalog (38 records + 4 CRs) with:
  - `id`, `name`, `type`, `path`;
  - `process_intent` and `process_classification` where applicable;
  - `legacy_findings`: raw BP-SEM findings (legacy intent
    vocabulary; legacy scalar `process_context`; missing canonical
    `context:` block; legacy `process_audience`; missing
    `process_specialization`).
- Reproducible: `python3 scripts/build_inventory.py` regenerates
  deterministically. `--self-test --strict` asserts byte-identity
  with the committed file (test-locked).

### Phase 2: baseline

- `reconciliation/baseline/v1.yaml` freezes each record's file
  bytes as a SHA-256. Future tranches diff exactly which bytes
  were touched.
- Baseline metadata: `baseline_version = v1`; `baseline_commit =
  816c63b`; `baseline_branch = main`; `baseline_at = 2026-09-06`.

### Phase 1 STRUCT conformance (decision D6)

- `scripts/check_struct.py` walks the repository root and asserts
  every top-level entry is recognised. Known: `catalog-index-schema`,
  `change-requests`, `classifications`, `contexts`, `contributions`,
  `docs`, `entities`, `schemas`, `scripts`, `tests`, `tools`,
  `utils`, `validation`, `reconciliation`, `reports`, `.github`,
  `CHANGELOG.md`, `CATALOG.yaml`, `CONTRIBUTING.md`, `LICENSE`,
  `README.md`, `TEMPLATE_VERSION`, `docs.governance.md`,
  `metamodel-pointer.yaml`. Conventional hidden entries (`.git`,
  `.gitignore`, `.pytest_cache`, etc.) are accepted.
- Self-test asserts the check detects `reconcilliation/` as a typo.
- Wired into CI as an advisory step (`--strict || true`) so existing
  reconciliations are not disrupted.

### Documentation

- `reconciliation/README.md`: orientation for visitors; layout,
  phase progression, STRUCT conformance reference.
- `CHANGELOG.md`: Phase 1-2 entry.

## What this PR does NOT do

- No schema, validator, or entity changes.
- No migration of existing entries (CR-BP-15-IMP Phases 3-7 scope).
- No CI step that blocks on findings (the §24 admission freeze is
  preserved; CR-BP-15-IMP Phases 3-7 will progressively introduce
  per-tranche gates).

## Verification

- `pytest tests/ -q`: 88 passed (79 prior + 9 new).
- All sibling validators PASS (BP-SEM records the documented legacy
  findings as advisory; STRUCT records the warnings as advisory).
- `build_inventory.py --self-test --strict`: PASS (byte-identity
  with committed inventory + baseline).
- `regenerate_catalog.py --check`: OK locally AND in a fresh clone
  of this branch (mtime trap guard).
- Dash-clean: zero en/em dashes in added lines.

## Programme position

- CR-BP-14: **Implemented** (PRs #26, #28, #29, #30).
- CR-BP-15 + CR-BP-15-IMP: **Proposed**; this PR is the first
  CR-BP-15-IMP delivery.
- Next: **PR-5 (CR-BP-15-IMP Phases 3-4: disposition register +
  Process Context-by-context tranche plan)**, then **PR-6..9
  (Phases 5-7: per-tranche migrations)**.
