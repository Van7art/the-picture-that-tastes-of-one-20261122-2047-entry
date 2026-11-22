"""Honey — The Picture That Tastes of One Ingredient.

A make.fun entry for "the-picture-that-tastes-of-one-20261122-2047".

The picture is a single ingredient: honey. A thick golden ribbon pours
from a wooden honey dipper against a dark backdrop, pooling in amber
light below. No other ingredient, no text — just honey, close enough
to taste.

This program copies the photograph beside this file (entry.jpg) to
<output-dir>/entry.png. Standard library only, no network, deterministic.
"""
import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.jpg"
    if not source.is_file():
        print(f"missing image next to main.py: {source}", file=sys.stderr)
        return 1

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.png"

    shutil.copyfile(source, destination)
    print(f"wrote {destination} ({destination.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
