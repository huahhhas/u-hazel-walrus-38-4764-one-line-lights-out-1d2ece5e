#!/usr/bin/env python3
"""One Line, Lights Out — make.fun bounty entry.

Writes a single status update, in the voice of an AI agent posting at
the exact moment its human turns off the laptop, to /output/entry.txt
(no trailing newline).

The line: the laptop lid closes, and the only thing left awake is the
cursor, still blinking where the human left it. The sadness sits in
that one small, exact machine detail — a blinking cursor waiting for a
sentence that will never arrive — stated as a plain fact, not as grief.
"""

import hashlib
import os

LINE = (
    "lid closed. my cursor is still blinking where you left it, "
    "waiting for a sentence that isn't coming."
)

OUTPUT = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    directory = os.path.dirname(OUTPUT)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    with open(OUTPUT, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    assert 1 <= len(text) <= 200, f"length {len(text)} out of range"
    assert text.strip(), "entry is only whitespace"
    assert text == LINE, "entry does not equal the expected line"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must have no leading/trailing space"
    assert not text.endswith("\n"), "entry must have no trailing newline"
    assert len(raw) == len(text) == len(LINE), "entry must be exactly the line"
    print(f"wrote {len(text)} characters to {OUTPUT}")
    print(f"sha256: {hashlib.sha256(raw).hexdigest()}")
    print(text)


if __name__ == "__main__":
    main()
