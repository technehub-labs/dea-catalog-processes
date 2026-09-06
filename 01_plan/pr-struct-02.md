# CR-CATALOG-STRUCT-02: Process Catalog Adoption (Three-Step Migration)

## What this PR is

Brings `dea-catalog-processes` into conformance with the catalog repository standard (CR-CATALOG-STRUCT-01). First of the four adoption CRs (STRUCT-02..05).

Runs the standard's three-step migration end-to-end on this catalog's two entities (`dea:process-manage-customer-relationship`, `dea:group-customer-lifecycle-management`). After this merges, the catalog is conformant with all 16 CSTs under `--strict`.

## Deliverables

| Action | Path | Notes |
|---|---|---|
| Move | `entities/v1-alpha/dea_bp_manage-customer-relationship.yaml` | to `entities/v1-alpha/dea:process-manage-customer-relationship/dea:process-manage-customer-relationship.yaml`; rename to canonical `dea:process-*` form per CR-BP-04 |
| Move | `entities/v1-alpha/dea_group-customer-lifecycle-management.yaml` | to `entities/v1-alpha/dea:group-customer-lifecycle-management/dea:group-customer-lifecycle-management.yaml` |
| Move | `docs/research/l1-register.yaml` | to `entities/v1-alpha/dea:group-customer-lifecycle-management/research/l1-register.yaml` |
| Move | `docs/research/l1-candidate-universe.yaml` | to `entities/v1-alpha/dea:group-customer-lifecycle-management/research/l1-candidate-universe.yaml` |
| Move | `docs/research/L1-REGISTER-v0.1.md` | to `entities/v1-alpha/dea:group-customer-lifecycle-management/research/L1-REGISTER-v0.1.md` |
| Remove | `docs/research/` | empty after the move |
| New | `entities/v1-alpha/dea:group-customer-lifecycle-management/research/README.md` | provenance |
| New | `entities/v1-alpha/dea:process-manage-customer-relationship/research/README.md` | provenance + governing CRs |
| New | `entities/v1-alpha/dea:{process-manage-customer-relationship,group-customer-lifecycle-management}/{candidates,retired}/.gitkeep` | empty state dirs |
| New | `CATALOG.yaml` | machine-generated, 1.9 KB |
| New | `TEMPLATE_VERSION` | `0.1.0` (matches canonical template) |
| Modify | `metamodel-pointer.yaml` | additive top-level metadata block (id/name/abbreviation/version/status/metamodel_version/description/owner); existing nested blocks unchanged |
| New | `scripts/regenerate_catalog.py` | vendored from `dea-metaframework/tools/` (CST-013) |
| New | `scripts/check_catalog_index.py` | vendored (CST-014) |
| New | `catalog-index-schema/catalog-index-schema.json` | vendored |
| Modify | `scripts/check_ecf_conformance.py` | skip state-directory files |
| Modify | `.github/workflows/ci.yml` | regenerator + gate + conformance steps; state-directory filter in per-file dispatch |
| Modify | `CHANGELOG.md` | Unreleased entry |
| Modify | `change-requests/README.md` | BP-12 row flips to Merged (PR #20); new STRUCT-02 row |
| New | `change-requests/CR-CATALOG-STRUCT-02.md` | CR doc |

## What the CI now enforces

1. `python scripts/regenerate_catalog.py --check` (CST-001..005 via regenerator; fails on stale CATALOG.yaml).
2. `python scripts/check_catalog_index.py --strict` (schema + structural sanity).
3. Per-file schema dispatch (CR-BP-12) with state-directory filter.
4. The 6 existing catalog validators (CR-ECF-CG-004, CR-BP-SPEC-BP-01, CR-BP-02, CR-BP-03, CR-BP-03A, CR-BP-12).
5. `python .metaframework/tools/conformance_test_catalog_structure.py --strict` (CST-001..CST-016).

## Bug fix included

`dea-metaframework/tools/regenerate_catalog.py:detect_repository_url` previously emitted authenticated git clone URLs verbatim into `CATALOG.yaml`, which can leak credentials (`https://<TOKEN>@github.com/...`). The function now strips the userinfo portion via `_strip_url_credentials`. This is a security improvement that protects every catalog that runs the regenerator.

## Design decisions locked

- **D-001**: Research under L1 entity (`dea:group-customer-lifecycle-management`). Research is about L1 Process Groups; L1 entities own L1 evidence.
- **D-002**: Hand-roll, no `bootstrap_catalog_repo.py`. The migration is surgical and step-by-step; bootstrap-in-place would rewrite timestamps and lose commit history attribution.
- **D-003**: Keep `contributions/processes/` + existing template name. The catalog hosts one entity type; renaming is a future concern.
- **D-004**: Catalog index schema in `catalog-index-schema/`. Sibling directory keeps index machinery separate from entity-level schemas.
- **D-005**: Regenerator + conformance on every PR. Combined runtime under 30 seconds.

## Verification

- All 6 catalog validators PASS.
- Regenerator --check exits 0.
- Gate --strict exits 0.
- Conformance --strict: 16/16 CSTs passed, 0 warnings.
- Dash sweep on new prose: clean.
- Secret scan on staged files: 0.
- `git diff --check`: clean.

## Adoption tracker

After this merges, `docs/standards/catalog-repository-pattern-adoption.md` flips this repo's row from `not-started` to `conforming`.

## Sequencing

1. STRUCT-03..05 (other catalog adoptions) can land in any order after this.
2. STRUCT-07 (cross-repo consumer) is unblocked once STRUCT-02 + STRUCT-06a + STRUCT-06b are all merged (i.e. now).
