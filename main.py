#!/usr/bin/env python3
"""Publish the strawberry picture to the contest output location.

The artwork lives next to this file as ``entry.png``. Running the
program streams that file, unchanged, to ``entry.png`` inside the
output directory: ``$MAKEFUN_OUTPUT_DIR`` when the harness sets it,
otherwise ``/output``. Standard library only, no network access,
no command-line arguments, and the working directory is irrelevant
because every path is derived from this file's own location.
"""

import os
import shutil
import sys

CHUNK_SIZE = 128 * 1024
ARTWORK_NAME = "entry.png"


def artwork_source() -> str:
    """Absolute path of the picture bundled beside this program."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, ARTWORK_NAME)


def output_target() -> str:
    """Absolute path the harness expects the picture to appear at."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, ARTWORK_NAME)


def publish() -> str:
    src = artwork_source()
    dst = output_target()
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(src, "rb") as fin, open(dst, "wb") as fout:
        shutil.copyfileobj(fin, fout, length=CHUNK_SIZE)
    return dst


def main() -> int:
    written = publish()
    size = os.path.getsize(written)
    print(f"wrote {written} ({size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
