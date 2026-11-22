#!/usr/bin/env python3
"""Entry for make.fun's "The picture that tastes of one ingredient".

The judged picture is committed beside this file as entry.png; the
program copies it, byte for byte, to the output location the harness
asks for. Standard library only, no network, no arguments.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(source, target)
    if target.stat().st_size != source.stat().st_size:
        raise SystemExit("copied image does not match the committed entry.png")


if __name__ == "__main__":
    main()
