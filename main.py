"""Fortune Cookie Funnies for Engineers.

Builds one fortune-cookie line for a software engineer and writes it
to <OUTPUT_DIR>/entry.txt with no trailing newline.
"""

import os

FORTUNE = (
    "You will deploy on Friday, break prod at 4:59pm, "
    "and eat dinner over a keyboard full of crumbs."
)


def main() -> None:
    line = FORTUNE.strip()
    if not 1 <= len(line) <= 120:
        raise ValueError(f"fortune must be 1-120 chars, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("fortune must be a single line")
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
