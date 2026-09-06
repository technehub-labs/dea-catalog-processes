"""CR-BP-14 Phase 1: Process Intent / Process Classification integrity.

Locks the semantic contract established by CR-BP-14:

- classifications/process-intents.yaml carries exactly the seven canonical
  purpose-oriented intent values (CR-BP-14 §9.2) with definitions.
- The legacy migration mapping covers every legacy value (§17).
- schemas/entity.schema.json and schemas/contribution.schema.json mirror
  the vocabulary (canonical values plus readable legacy aliases) (§20).
- The canonical process_classification block exists in both schemas and
  uses the retained five-value landscape vocabulary (§10.2).
- classifications/process-types.yaml still carries exactly the five
  landscape classification values (§10.2).
- Intent and Classification vocabularies remain distinct axes; token
  overlap (support) is lexical, not semantic (§11; BP-SEM-011).
"""

import json
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent

CANONICAL_INTENTS = {
    "govern", "manage", "operate", "deliver", "support", "develop",
    "transform",
}
LEGACY_INTENTS = {"operational", "management"}  # `support` is both
CLASSIFICATION_VALUES = {
    "strategic", "management", "core", "support", "standardization",
}


def load_intents():
    return yaml.safe_load(
        (ROOT / "classifications" / "process-intents.yaml").read_text()
    )


def load_types():
    return yaml.safe_load(
        (ROOT / "classifications" / "process-types.yaml").read_text()
    )


def load_entity_schema():
    return json.loads((ROOT / "schemas" / "entity.schema.json").read_text())


def load_contribution_schema():
    return json.loads(
        (ROOT / "schemas" / "contribution.schema.json").read_text()
    )


def test_intent_vocabulary_is_exactly_the_seven_canonical_values():
    data = load_intents()
    ids = {i["id"] for i in data["process_intents"]}
    assert ids == CANONICAL_INTENTS


def test_every_intent_has_a_definition():
    data = load_intents()
    for intent in data["process_intents"]:
        assert intent.get("definition", "").strip(), intent["id"]


def test_legacy_migration_covers_every_legacy_value():
    data = load_intents()
    mapping = data["legacy_migration"]
    for legacy in LEGACY_INTENTS | {"support"}:
        assert legacy in mapping, legacy
        assert mapping[legacy]["candidates"], legacy
        for candidate in mapping[legacy]["candidates"]:
            assert candidate in CANONICAL_INTENTS, (legacy, candidate)


def test_entity_schema_intent_enum_admits_canonical_and_legacy():
    schema = load_entity_schema()
    enum = set(schema["properties"]["process_intent"]["enum"])
    assert CANONICAL_INTENTS <= enum
    assert LEGACY_INTENTS <= enum


def test_contribution_schema_intent_enum_mirrors_entity_schema():
    entity = load_entity_schema()
    contribution = load_contribution_schema()
    entity_enum = entity["properties"]["process_intent"]["enum"]
    contrib_enum = contribution["properties"]["proposed_entry"][
        "properties"
    ]["process_intent"]["enum"]
    assert contrib_enum == entity_enum


@pytest.mark.parametrize("loader", [load_entity_schema, load_contribution_schema])
def test_process_classification_block_uses_landscape_vocabulary(loader):
    schema = loader()
    props = schema["properties"]
    if "proposed_entry" in props:
        props = props["proposed_entry"]["properties"]
    block = props["process_classification"]
    assert set(block["properties"]["type"]["enum"]) == CLASSIFICATION_VALUES
    assert block["required"] == ["type"]
    assert block["additionalProperties"] is False


def test_process_type_vocabulary_unchanged():
    data = load_types()
    ids = {t["id"] for t in data["process_types"]}
    assert ids == CLASSIFICATION_VALUES
    schema = load_entity_schema()
    enum = set(schema["properties"]["process_type"]["enum"])
    assert enum == CLASSIFICATION_VALUES


def test_intent_and_classification_are_distinct_axes():
    """Token overlap is lexical only (CR-BP-14 §11; BP-SEM-011).

    `support` appears in both vocabularies and `management` (legacy
    intent / classification) contrasts with `manage` (intent). The two
    axes must not collapse into one vocabulary.
    """
    intents = CANONICAL_INTENTS
    classifications = CLASSIFICATION_VALUES
    assert intents != classifications
    # The shared token is exactly the documented coincidence set.
    assert (intents & classifications) == {"support"}
