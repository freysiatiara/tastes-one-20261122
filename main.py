#!/usr/bin/env python3
"""Carry the honeycomb picture to the contest output folder.

``entry.png`` sits in the same directory as this script. A run reads
that file and writes an identical copy to ``entry.png`` inside the
output directory, which is ``$MAKEFUN_OUTPUT_DIR`` when the harness
provides one and ``/output`` otherwise. Nothing here depends on the
current working directory: the source path is resolved from this
file's own location. Standard library only, no network, no arguments.
"""

from pathlib import Path
import os
import sys

PICTURE = "entry.png"
BLOCK = 64 * 1024


def picture_path() -> Path:
    return Path(__file__).resolve().parent / PICTURE


def destination_path() -> Path:
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(folder) / PICTURE


def carry() -> Path:
    src = picture_path()
    dst = destination_path()
    dst.parent.mkdir(parents=True, exist_ok=True)
    with src.open("rb") as fin, dst.open("wb") as fout:
        while True:
            block = fin.read(BLOCK)
            if not block:
                break
            fout.write(block)
    return dst


def main() -> int:
    target = carry()
    print(f"delivered {target} ({target.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
