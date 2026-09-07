# CR-BP-13: L1 Process Group Research Ratification

## What this PR is

Closes the research-status question left open by CR-BP-11. The CR-BP-11 register records 49 coordinates with dispositions: 38 accepted, 11 deferred. It is explicitly `candidate-not-canonical; subject to review`. This PR ratifies the register: the 38 accepted dispositions become `ratified-accepted`; the 11 deferred dispositions become `backlog-deferred` with a single shared rationale.

## Distribution

| Bucket | Count | Notes |
|---|---|---|
| Research files updated | 2 | `l1-register.yaml` + `l1-candidate-universe.yaml` |
| Markdown updated | 2 | `L1-REGISTER-v0.1.md` + `research/README.md` |
| Canonical YAML updated | 1 | `dea:group-customer-lifecycle-management.yaml` (change_history) |
| CR docs | 1 | `change-requests/CR-BP-13-research-ratification.md` |
| README updates | 1 | `change-requests/README.md` (CR-BP-13 row + CR-CATALOG-STRUCT-02 flip) |
| New tools | 1 | `tools/ratify_research_register.py` (~210 lines) |
| New tests | 9 | `tests/test_ratify_research_register.py` |

## Ratification summary

| Disposition | Coordinates | L1 candidates |
|---|---:|---:|
| `ratified-accepted` | 38 | 86 |
| `backlog-deferred` | 11 | 16 |
| **Total** | **49** | **102** |

## The rationale (CR-BP-13 §4)

The 11 deferred coordinates all sit on the **Activate** or **Retire** lifecycle stages. These are transition stages, not stable Process Group operating scopes:

- **Activate** is the handover from Build to Operate. Sub-step of the receiving Process Group.
- **Retire** is the wind-down of a Process Group. Sub-step of the ending Process Group.

Neither forms a stable L1 group on its own. Adding them as L1 Process Groups would create scope overlap with their sibling Operate Process Group (PG-006 MECE violation). The backlog can be revisited if a discrete Activate/Retire process identity is later identified (separate CR).

## Live verification

```
$ python3 tools/ratify_research_register.py
result: ratified_accepted=124, backlog_deferred=27, untouched=0
```

(124 = 38 coordinates + 86 candidates; 27 = 11 + 16; matches the table above.)

```
$ python -m pytest tests/test_ratify_research_register.py
tests/test_ratify_research_register.py .........                         [100%]
============================== 9 passed in 0.04s ==============================
```

```
$ python3 scripts/regenerate_catalog.py --check --schema catalog-index-schema/catalog-index-schema.json
OK: CATALOG.yaml is current

$ python3 scripts/check_catalog_index.py --strict --schema catalog-index-schema/catalog-index-schema.json
OK: CATALOG.yaml validates (2 entities)

$ python3 /home/hermes/dea-work/dea-metaframework/tools/conformance_test_catalog_structure.py --strict
OK: 16 CST(s) passed (0 warning(s))
```

All 6 process validators pass (ECF conformance, process identity, process group, process context, legacy migration, specialization).

## Sequencing

| CR | Status |
|---|---|
| CR-BP-11 (research register) | Merged |
| CR-BP-12 (L1 Process Group profile) | Merged |
| **CR-BP-13 (research ratification)** | **This PR** |
| CR-CATALOG-STRUCT-02 (catalog adoption) | Merged (PR #21); row flipped in this PR |
| CR-BP-13a..BP-13g (seven-domain admission tranches) | future |

After this PR lands, the **research register is ratified** and the catalog's first L1 Process Group is fully backed by canonical research evidence. The admission tranches (separate work) can proceed against the ratified register.

## Out of scope (intentional)

This PR does NOT create new canonical L1 records. The 38 accepted coordinates remain in the register; promoting each to a first-class Process Group entity is the work of the seven-domain admission tranches (CR-BP-13a..BP-13g, one per ECF Domain). That is a much larger effort — 38 records across 7 domains — and a natural next session.