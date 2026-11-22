"""Entry point for the make.fun 'one ingredient' picture contest.

The artwork (a macro photograph of a single strawberry) ships inside
this repository as ``entry.png``.  Running this module publishes that
file to the contest output location so the grader can pick it up.

Only the Python standard library is used, and no command-line
arguments are read.
"""

import os
import shutil
from pathlib import Path

# The picture lives right next to this module; resolving it from
# __file__ keeps the program independent of the working directory.
PICTURE_NAME = "entry.png"
CHUNK = 256 * 1024


def artwork_path() -> Path:
    """Return the path of the bundled picture."""
    return Path(__file__).resolve().parent / PICTURE_NAME


def destination() -> Path:
    """Return where the picture has to land for grading."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(folder) / PICTURE_NAME


def publish() -> Path:
    """Stream the bundled picture to the destination, in chunks."""
    source = artwork_path()
    target = destination()
    target.parent.mkdir(parents=True, exist_ok=True)
    with source.open("rb") as reading, target.open("wb") as writing:
        shutil.copyfileobj(reading, writing, length=CHUNK)
    return target


if __name__ == "__main__":
    publish()
