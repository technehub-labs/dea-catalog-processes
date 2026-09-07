# CR-BP-14: Process Semantic Reconciliation (landing + register sync)

## Summary

Lands **CR-BP-14: Process Semantic Reconciliation** verbatim and synchronizes
the CR register with actual repository status, per CR-BP-14 §23 (CR Register
Reconciliation) and §24 (Catalog Population Freeze).

CR-BP-14 establishes the definitive semantic contract for the Business Process
Catalog: Context / Scope / Group / Process / Intent / Classification /
Specialization / Relationships are formally separated concerns, and no one of
them may substitute for another. It is the normative bridge between the
existing CR lineage and the subsequent CR-BP-15 catalog reconciliation.

## What this PR does

1. **Lands the CR verbatim** at
   `change-requests/CR-BP-14-process-semantic-reconciliation.md`.
   md5 `70ae439b3613f92e47d628d9b4e595a8`, byte-identical to the source
   attachment (working-folder archive:
   `dea-work/process/00_inbox/CR-BP-14-process-semantic-reconciliation.md`).
2. **Register row** in `change-requests/README.md`: CR-BP-14 added as
   **Proposed**.
3. **Register correction**: CR-BP-13b status changed from "Proposed (this PR)"
   to **Merged** (PR #24); the row was left stale by the 13b merge.
4. **README change programme sync** (§23: historical status shall not be
   presented as current status):
   - CR-BP-03: "Proposed (this PR)" corrected to **Merged** (PR #15).
   - Added missing rows for CR-BP-03A (#16), CR-BP-03C (#17), CR-BP-11 (#18),
     CR-BP-04 (#19), CR-BP-12 (#20), CR-BP-13 (#22), CR-BP-13a (#23),
     CR-BP-13b (#24).
   - The stale "CR-BP-04 Activity Model" / "CR-BP-05 Execution Boundary"
     future placeholders were renumbered as unnumbered future rows; the
     CR-BP-04 number was consumed by the landed ID-Family Reconciliation CR.
5. **CATALOG.yaml regenerated** (`open_change_requests` 13 -> 14) so the
   regenerator gate stays green.

## What this PR does NOT do

- No schema changes (§20 lands in a follow-on phase PR).
- No validators (BP-SEM-001..012 land in a follow-on phase PR).
- No documentation semantics reconciliation beyond status accuracy
  (§22 prose reconciliation lands in a follow-on phase PR).
- No changes to existing canonical entries (that is CR-BP-15 scope).
- No new admission tranche; the §24 freeze is in effect.

## Verification

- `python scripts/regenerate_catalog.py --check --schema catalog-index-schema/catalog-index-schema.json`: OK (CATALOG.yaml current).
- `python scripts/check_catalog_index.py --strict --schema catalog-index-schema/catalog-index-schema.json`: OK (28 entities).
- `scripts/check_ecf_conformance.py`, `check_legacy_migration.py`, `check_process_context.py`, `check_process_group.py`, `check_process_identity.py`, `check_process_specialization.py`: all PASS.
- `python -m pytest tests/ -q`: 38 passed.
- Dash-clean: zero en-dashes / em-dashes in all added lines (CR file itself lands verbatim per land-as-authored).

## Implementation decomposition (follow-on phase PRs)

Per CR-BP-14 §26, implementation proceeds one phase per PR:

1. **Phase 1: Semantic vocabularies + schema (§9, §10, §11, §12, §20).**
   New `classifications/process-intents.yaml` (seven-value purpose-oriented
   vocabulary); `process_intent` enum extension with legacy values retained as
   deprecated migration aliases; canonical `process_classification` block;
   specialization basis vocabulary.
2. **Phase 2: Context and relationships (§13, §19).** `context:` block and
   `serves` / `contributes-to` / `operates-within` relationship semantics;
   `process_audience` marked as migration alias; deterministic migration
   validator input.
3. **Phase 3: Validators BP-SEM-001..012 + CI wiring (§21).** New
   `scripts/check_process_semantics.py` with self-test mode; CI reports legacy
   fields requiring migration.
4. **Phase 4: Documentation reconciliation (§22).** README prose,
   `docs/classification.md`, `docs/architecture.md`, `docs/identity.md`,
   `docs/relandscape.md`; superseded statements marked historical.
5. **Phase 5: Existing-entry semantic assessment (§26 Governance).**
   Evidence-based assessment report over all 28 canonical entries
   (RETAIN / RECLASSIFY / RENAME / SPECIALIZE / MERGE / SPLIT / MOVE / DEFER /
   RETIRE candidates) as the input to CR-BP-15.
