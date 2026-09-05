"""Ratify CR-BP-11's 49-coordinate register (CR-BP-13).

This script intentionally uses a line-by-line approach (not yaml.dump)
so that comments and formatting in the source research files are
preserved. It is idempotent: re-running it does not double-apply the
ratification (the script checks for the `ratification:` block).

Usage:
    python tools/ratify_research_register.py
    python tools/ratify_research_register.py --research-dir <path>
    python tools/ratify_research_register.py --dry-run
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml


DEFAULT_RATIFIED_AT = "2026-09-05"
DEFAULT_CR = "CR-BP-13"

# Single source of truth for why the 11 deferred coordinates remain
# in backlog rather than being ratified. CR-BP-13 §4 records this.
DEFERRED_RATIONALE = (
    "Activate and Retire are lifecycle transition stages, not stable "
    "Process Group operating scopes. L1 Process Groups (CR-BP-12) "
    "catalogue the bounded operating scope of a process domain; the "
    "Activate stage is the handover from Build to Operate (a sub-step "
    "of the receiving Process Group), and the Retire stage is the "
    "wind-down of the prior Process Group (a sub-step of the ending "
    "Process Group). Neither forms a stable L1 group on its own. "
    "Reconsider if a discrete Activate/Retire process identity is "
    "later identified (separate CR)."
)


def _flip_disposition(
    line: str,
    ratified_at: str,
    cr: str,
) -> str | None:
    """If line is `      disposition: <old>`, return the new line.

    Otherwise return None (no change).
    """
    stripped = line.strip()
    if not stripped.startswith("disposition:"):
        return None
    # Extract current value.
    parts = stripped.split(":", 1)
    if len(parts) != 2:
        return None
    value = parts[1].strip().strip("'\"")
    # Preserve the line's indentation.
    indent = line[: len(line) - len(line.lstrip())]
    if value == "accepted":
        new = f"{indent}disposition: ratified-accepted\n"
        new += f"{indent}ratified_at: '{ratified_at}'\n"
        new += f"{indent}ratified_by: {cr}\n"
        return new
    if value == "deferred":
        new = f"{indent}disposition: backlog-deferred\n"
        new += f"{indent}ratified_at: '{ratified_at}'\n"
        new += f"{indent}ratified_by: {cr}\n"
        # Quote the rationale as a YAML scalar (block style).
        quoted = DEFERRED_RATIONALE.replace("'", "''")
        new += f"{indent}deferral_reason: |\n"
        for para in DEFERRED_RATIONALE.split("\n\n"):
            for sub in para.split("\n"):
                new += f"{indent}  {sub}\n"
        return new
    return None


def ratify_register_file(
    path: Path,
    *,
    ratified_at: str,
    cr: str,
    dry_run: bool,
) -> dict[str, int]:
    """Update the research register YAML in-place.

    Returns:
        Counts of {ratified_accepted, backlog_deferred, untouched}.
    """
    text = path.read_text(encoding="utf-8")
    # Idempotency check.
    if "ratification:\n" in text or "ratification: " in text:
        # Already has a top-level ratification block.
        # Parse to check the version.
        try:
            doc = yaml.safe_load(text)
        except yaml.YAMLError:
            doc = {}
        existing = doc.get("ratification", {}) if isinstance(doc, dict) else {}
        if existing.get("version") == 1:
            print(
                f"INFO: {path}: already ratified (version=1, "
                f"at={existing.get('ratified_at')}); skipping"
            )
            return {"ratified_accepted": 0, "backlog_deferred": 0, "untouched": -1}

    counts = {"ratified_accepted": 0, "backlog_deferred": 0, "untouched": 0}
    new_lines: list[str] = []
    for line in text.splitlines():
        flipped = _flip_disposition(line, ratified_at=ratified_at, cr=cr)
        if flipped is not None:
            # Insert the replacement (with the additional fields).
            for sub in flipped.splitlines():
                new_lines.append(sub)
            if "ratified-accepted" in flipped:
                counts["ratified_accepted"] += 1
            elif "backlog-deferred" in flipped:
                counts["backlog_deferred"] += 1
        else:
            new_lines.append(line)
            # Count disposition lines that weren't flipped as untouched.
            if line.strip().startswith("disposition:"):
                counts["untouched"] += 1

    # Inject top-level `ratification:` block right after the
    # `register:` line (the file is already organised that way).
    ratified = counts["ratified_accepted"]
    deferred = counts["backlog_deferred"]
    ratification_block = (
        f"ratification:\n"
        f"  version: 1\n"
        f"  cr: {cr}\n"
        f"  ratified_at: '{ratified_at}'\n"
        f"  ratified_accepted: {ratified}\n"
        f"  backlog_deferred: {deferred}\n"
        f"  deferred_rationale: |\n"
    )
    for para in DEFERRED_RATIONALE.split("\n\n"):
        for sub in para.split("\n"):
            ratification_block += f"    {sub}\n"

    # Insert before the `register:` line.
    final_lines: list[str] = []
    inserted = False
    for line in new_lines:
        if not inserted and line.strip().startswith("register:"):
            final_lines.append(ratification_block)
            inserted = True
        final_lines.append(line)
    if not inserted:
        final_lines.append(ratification_block)

    if not dry_run:
        path.write_text("\n".join(final_lines) + "\n", encoding="utf-8")
    return counts


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog="ratify-research-register",
        description=(
            "Ratify the 49-coordinate L1 Process Group register "
            "(CR-BP-13). Updates l1-register.yaml and "
            "l1-candidate-universe.yaml."
        ),
    )
    p.add_argument(
        "--research-dir",
        type=Path,
        default=Path(
            "entities/v1-alpha/dea:group-customer-lifecycle-management/research"
        ),
        help="Path to the research directory.",
    )
    p.add_argument(
        "--ratified-at",
        default=DEFAULT_RATIFIED_AT,
        help="Ratification date (default 2026-09-05).",
    )
    p.add_argument(
        "--cr",
        default=DEFAULT_CR,
        help="Ratifying CR (default CR-BP-13).",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="Compute counts but don't write.",
    )
    args = p.parse_args(argv)

    targets = ["l1-register.yaml", "l1-candidate-universe.yaml"]
    total = {"ratified_accepted": 0, "backlog_deferred": 0, "untouched": 0}
    for name in targets:
        path = args.research_dir / name
        if not path.is_file():
            print(f"INFO: {path} not found; skipping")
            continue
        counts = ratify_register_file(
            path,
            ratified_at=args.ratified_at,
            cr=args.cr,
            dry_run=args.dry_run,
        )
        for k in ("ratified_accepted", "backlog_deferred", "untouched"):
            if counts[k] > 0:
                total[k] += counts[k]

    print(
        f"\nresult: ratified_accepted={total['ratified_accepted']}, "
        f"backlog_deferred={total['backlog_deferred']}, "
        f"untouched={total['untouched']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())