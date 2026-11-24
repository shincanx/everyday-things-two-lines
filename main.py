#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run — make.fun entry.

Writes a two-line explanation of a traffic jam to /output/entry.txt:
line 1 explains it to a 10-year-old in one vivid sentence built on an
analogy; line 2 says in one sentence why the analogy works — what it
maps and what it leaves out. Deterministic: no network, no randomness,
no dependencies, no time or environment input.
"""

import os

LINE_1 = (
    "A traffic jam is a school hallway at break time, with every kid "
    "trying to squeeze through one door at once."
)
LINE_2 = (
    "It maps how too many cars on too little road slow everyone down, "
    "but leaves out that cars can't step aside or laugh about it, and "
    "a jam can last hours while break lasts minutes."
)

ENTRY = LINE_1 + "\n" + LINE_2 + "\n"


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY, end="")


if __name__ == "__main__":
    main()
