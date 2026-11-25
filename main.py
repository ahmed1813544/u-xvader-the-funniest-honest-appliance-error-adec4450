#!/usr/bin/env python3
"""Write one honest appliance error line to /output/entry.txt.

Stdlib only. Deterministic: the same line, byte for byte, every run.
"""
import os
from pathlib import Path

LINE = "ERROR: Ice maker jammed. I made 400 cubes and you took none. They are now one cube."


def main() -> None:
    # One line, well under the 200-character gate, no trailing spaces.
    assert 1 <= len(LINE) <= 200 and LINE.strip() == LINE
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
