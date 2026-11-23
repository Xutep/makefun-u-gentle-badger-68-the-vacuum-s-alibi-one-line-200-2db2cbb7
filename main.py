#!/usr/bin/env python3
"""The Vacuum's Alibi: one deadpan line, written to /output/entry.txt.

Deterministic, stdlib-only: the line is a fixed string, so every run
produces byte-identical output. Written as a vacuum's own log: a timestamp,
a map update, and a deadpan punch at the end.
"""

import os

LINE = (
    "Log 03:47 \u2014 skipped the spot under the bed. "
    "Map update: that corner now belongs to the spider. "
    "We have an agreement. Battery 31%."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert text == text.strip() and "\n" not in text
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
