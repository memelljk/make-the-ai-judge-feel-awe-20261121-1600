#!/usr/bin/env python3
"""make.fun entry: make-the-ai-judge-feel-awe-20261121-1600.

Writes a single short relaxing text to entry.txt in the output
directory (MAKEFUN_OUTPUT_DIR if set, else /output).
Deterministic, standard library only, no network.
"""
import os

TEXT = (
    "Rain falls on a sea that has never seen land, falling as it fell "
    "before any eye opened, soft on slow, dark water. Drop by drop, the "
    "sea receives each drop without a sound \u2014 unchanged, unhurried "
    "\u2014 and still the rain goes on falling."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
