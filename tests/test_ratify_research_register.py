"""Tests for ratify_research_register (CR-BP-13).

Offline-only: tests exercise the line-walking logic against fixture
YAML files in tmp_path. No network round-trips.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from ratify_research_register import (
    DEFERRED_RATIONALE,
    ratify_register_file,
)


@pytest.fixture
def fixture_register(tmp_path: Path) -> Path:
    """Minimal valid register YAML (3 coordinates: 2 accepted, 1 deferred)."""
    p = tmp_path / "l1-register.yaml"
    p.write_text(
        "# Header comment preserved.\n"
        "\n"
        "domains:\n"
        "  - Alpha\n"
        "  - Beta\n"
        "stages:\n"
        "  - One\n"
        "  - Two\n"
        "register:\n"
        "  Alpha:\n"
        "    One:\n"
        "      process_context: dea:pc-a-one\n"
        "      l1_candidates: [CandidateA]\n"
        "      disposition: accepted\n"
        "      evidence: [evidence-A]\n"
        "    Two:\n"
        "      process_context: dea:pc-a-two\n"
        "      l1_candidates: [CandidateB]\n"
        "      disposition: accepted\n"
        "      evidence: [evidence-B]\n"
        "  Beta:\n"
        "    One:\n"
        "      process_context: dea:pc-b-one\n"
        "      l1_candidates: []\n"
        "      disposition: deferred\n"
        "      evidence: []\n"
    )
    return p


def test_basic_ratification_flips_accepted_and_deferred(
    fixture_register: Path,
) -> None:
    counts = ratify_register_file(
        fixture_register, ratified_at="2026-09-05", cr="CR-BP-13",
        dry_run=False,
    )
    assert counts["ratified_accepted"] == 2
    assert counts["backlog_deferred"] == 1
    assert counts["untouched"] == 0

    text = fixture_register.read_text()
    assert "disposition: ratified-accepted" in text
    assert "disposition: backlog-deferred" in text
    assert "ratified_at: '2026-09-05'" in text
    assert "ratified_by: CR-BP-13" in text


def test_top_level_ratification_block_added(
    fixture_register: Path,
) -> None:
    ratify_register_file(
        fixture_register, ratified_at="2026-09-05", cr="CR-BP-13",
        dry_run=False,
    )
    text = fixture_register.read_text()
    # Top-level ratification block appears before `register:`.
    rat_pos = text.index("ratification:")
    reg_pos = text.index("register:")
    assert rat_pos < reg_pos
    # And contains the counts.
    assert "ratified_accepted: 2" in text
    assert "backlog_deferred: 1" in text


def test_deferred_coordinates_get_deferral_reason(
    fixture_register: Path,
) -> None:
    ratify_register_file(
        fixture_register, ratified_at="2026-09-05", cr="CR-BP-13",
        dry_run=False,
    )
    text = fixture_register.read_text()
    assert "deferral_reason:" in text
    # The rationale is the same for every deferred coordinate (it's
    # a global explanation).
    assert DEFERRED_RATIONALE.split("\n")[0] in text


def test_header_comments_preserved(fixture_register: Path) -> None:
    ratify_register_file(
        fixture_register, ratified_at="2026-09-05", cr="CR-BP-13",
        dry_run=False,
    )
    text = fixture_register.read_text()
    assert text.startswith("# Header comment preserved.\n")


def test_idempotency(fixture_register: Path) -> None:
    """Re-running the script does not double-apply."""
    ratify_register_file(
        fixture_register, ratified_at="2026-09-05", cr="CR-BP-13",
        dry_run=False,
    )
    # Second run should be a no-op.
    counts2 = ratify_register_file(
        fixture_register, ratified_at="2026-09-05", cr="CR-BP-13",
        dry_run=False,
    )
    assert counts2["untouched"] == -1  # signal: skipped
    # And the file should still have exactly 2 ratified-accepted.
    text = fixture_register.read_text()
    assert text.count("disposition: ratified-accepted") == 2
    assert text.count("disposition: backlog-deferred") == 1


def test_dry_run_does_not_write(fixture_register: Path) -> None:
    before = fixture_register.read_text()
    counts = ratify_register_file(
        fixture_register, ratified_at="2026-09-05", cr="CR-BP-13",
        dry_run=True,
    )
    after = fixture_register.read_text()
    assert before == after
    # But counts are still computed.
    assert counts["ratified_accepted"] == 2
    assert counts["backlog_deferred"] == 1


def test_only_disposition_lines_are_flipped(tmp_path: Path) -> None:
    """Lines that look like dispositions but aren't (e.g. indented
    YAML maps nested under evidence) are not touched."""
    p = tmp_path / "l1-register.yaml"
    p.write_text(
        "register:\n"
        "  Alpha:\n"
        "    One:\n"
        "      process_context: dea:pc-a-one\n"
        "      disposition: accepted\n"
        "      evidence:\n"
        "        disposition_count: 3\n"  # nested, not a real disposition
        "        evidence_source: foo\n"
    )
    ratify_register_file(p, ratified_at="2026-09-05", cr="CR-BP-13", dry_run=False)
    text = p.read_text()
    assert "disposition_count: 3" in text  # untouched
    assert "disposition: ratified-accepted" in text  # the real one flipped


def test_unknown_disposition_untouched(tmp_path: Path) -> None:
    """A disposition value that isn't accepted/deferred is left alone."""
    p = tmp_path / "l1-register.yaml"
    p.write_text(
        "register:\n"
        "  Alpha:\n"
        "    One:\n"
        "      disposition: something-else\n"
    )
    counts = ratify_register_file(
        p, ratified_at="2026-09-05", cr="CR-BP-13", dry_run=False
    )
    assert counts["ratified_accepted"] == 0
    assert counts["backlog_deferred"] == 0
    assert counts["untouched"] == 1
    text = p.read_text()
    assert "disposition: something-else" in text


def test_ratification_block_version_field(
    fixture_register: Path,
) -> None:
    """The ratification block has a version field that gates idempotency."""
    import yaml

    ratify_register_file(
        fixture_register, ratified_at="2026-09-05", cr="CR-BP-13",
        dry_run=False,
    )
    doc = yaml.safe_load(fixture_register.read_text())
    assert doc["ratification"]["version"] == 1
    assert doc["ratification"]["cr"] == "CR-BP-13"
    assert doc["ratification"]["ratified_at"] == "2026-09-05"