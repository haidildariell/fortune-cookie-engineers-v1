#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers — entry writer.

Writes the single fortune-cookie line to entry.txt inside OUTPUT_DIR.
"""

import os
import sys

FORTUNE_LINE = (
    "You will deploy on Friday, break prod at 4:59pm, "
    "and eat dinner over a keyboard full of crumbs."
)

MAX_LENGTH = 120


def check_line(line: str) -> None:
    """Raise if the entry is not exactly one line of 1-120 characters."""
    if not isinstance(line, str):
        raise TypeError("entry must be a string")
    if len(line) < 1 or len(line) > MAX_LENGTH:
        raise ValueError(
            f"entry must be 1-{MAX_LENGTH} chars, got {len(line)}"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")


def resolve_output_dir() -> str:
    """Return the output directory, creating it when missing."""
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return out_dir


def write_entry(out_dir: str, line: str) -> str:
    """Write one validated line to entry.txt; return the file path."""
    check_line(line)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(line)
    return target


def main() -> int:
    out_dir = resolve_output_dir()
    write_entry(out_dir, FORTUNE_LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
