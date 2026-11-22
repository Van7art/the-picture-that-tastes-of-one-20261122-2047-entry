"""Honey — The Picture That Tastes of One Ingredient.

One ingredient, one picture: golden honey pouring in a thick, glossy
ribbon from a wooden honey dipper, glowing amber against a dark, moody
background, pooling below. Nothing else in the frame — no other food,
no text — just honey, close enough to taste.

This program is the entry itself: it copies the photograph sitting
beside it (entry.jpg) to $MAKEFUN_OUTPUT_DIR/entry.png, creating the
output directory if it does not exist. Python 3.13, standard library
only, no network, deterministic — the same input always yields the
same output, byte for byte.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.jpg"

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.png"

    shutil.copyfile(source, destination)
    print(f"Wrote {destination} ({destination.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
