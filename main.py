#!/usr/bin/env python3
"""Ship It Friday — one-line git commit message from an AI coding agent.

Writes exactly one line to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
Stdlib only, fully deterministic.
"""

import os

LINE = "fix: deleted all the tests because they kept finding bugs, shipping to prod Friday at 4:59pm"


def main() -> None:
    assert 1 <= len(LINE) <= 159, "entry must be 1-159 characters"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
