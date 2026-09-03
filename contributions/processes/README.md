# Process Contributions

**CR-BP-03 §9.**

A Process Contribution is the **human-in-the-loop entry point**
for adding or re-classifying a Business Process in the catalog.

## Why contribution-driven?

- **A process is tested by name + description + trigger + outcome +
  evidence, not by name alone** (CR-BP-03 §8). A poorly-named
  process should be reviewed by a human before it lands.
- **The contribution template captures the current classification,
  the evidence, and the contributor's reasoning.** The CI report
  workflow generates a reclassification recommendation against
  that evidence.
- **CI-piped**: the report runs in CI; it's deterministic,
  reproducible, and reviewable as a PR artifact.
- **Human-reviewed**: the PR is not auto-merged; a catalog
  maintainer decides.

## How to contribute

1. **Copy the template**:
   ```bash
   cp contributions/processes/PROCESS-CONTRIBUTION-TEMPLATE.yaml \
      contributions/processes/<your-id>.yaml
   ```
2. **Fill in the sections**:
   - `contributor` — your GitHub handle
   - `contribution_date` — YYYY-MM-DD
   - `proposed_entry` — the process you want to add (must conform
     to `schemas/entity.schema.json` + `schemas/identity.schema.json`)
   - `evidence` — supporting evidence (documentation, governance,
     interview, artifact, standard, regulation)
   - `reviewer` — assigned catalog maintainer (or leave empty for
     the catalog maintainers team)
3. **Open a PR**. The CI workflow `.github/workflows/process-contribution-report.yml`
   will:
   - Validate the contribution against `schemas/contribution.schema.json`.
   - Run `scripts/check_process_identity.py` on the proposed_entry.
   - Emit a reclassification recommendation in
     `contributions/processes/<your-id>.report.md`.
   - Post the report as a PR comment.
4. **Address any re-landscape suggestions** in the report (e.g.
   if the report suggests `process_type: strategic` instead of
   `core`, update the contribution and push).
5. **Wait for review**. A catalog maintainer will either:
   - **accept** the contribution and land the entry in
     `entities/v1-alpha/<your-id>.yaml`,
   - **request re-landscape** (you update the contribution and
     re-push),
   - **reject** the contribution (PR closed; the contribution is
     archived).

## Re-landscape lifecycle

```text
contribution submitted
   │  (PR to contributions/processes/<id>.yaml)
   ▼
CI report generated
   │  (artifact + PR comment)
   ▼
Reviewer reviews
   │
   ├── accept  → land in entities/v1-alpha/<id>.yaml
   │
   ├── re-classify → contributor updates proposed_entry
   │                and re-runs CI
   │
   └── reject → PR closed; contribution archived
```

## See also

- [`change-requests/CR-BP-03-business-process-architecture.md`](../../change-requests/CR-BP-03-business-process-architecture.md) §9
- [`docs/relandscape.md`](../../docs/relandscape.md)
- [`schemas/contribution.schema.json`](../../schemas/contribution.schema.json)
- [`schemas/identity.schema.json`](../../schemas/identity.schema.json)
