"""Honey — The Picture That Tastes of One Ingredient.

One ingredient, one picture: golden honey pouring in a thick,
glossy ribbon from a wooden honey dipper, glowing amber against
a dark, moody background, pooling below. Nothing else in the
frame — no other food, no text — just honey, close enough to
taste.

This program copies the photograph beside this script
(`entry.jpg`) to ``$MAKEFUN_OUTPUT_DIR/entry.png``, creating
the output directory if it does not exist yet.

Run: MAKEFUN_OUTPUT_DIR=/tmp/r2-out python3 main.py
Python 3.13, standard library only, no network, deterministic.
"""

import os
import shutil
from pathlib import Path

MAX_BYTES = 1_048_576


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.jpg"
    if not source.is_file():
        raise FileNotFoundError(f"Missing image file: {source}")
    if source.stat().st_size == 0:
        raise ValueError(f"Image file is empty: {source}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    shutil.copyfile(source, dest)
    if dest.stat().st_size > MAX_BYTES:
        raise ValueError(
            f"Output exceeds {MAX_BYTES} bytes: {dest.stat().st_size}"
        )
    print(f"Wrote {dest} ({dest.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
