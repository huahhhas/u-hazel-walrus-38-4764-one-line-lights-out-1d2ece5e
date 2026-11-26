#!/usr/bin/env python3
# Entry for make.fun bounty u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e
"""One Line, Lights Out.

Deterministic entry: writes exactly one status line to /output/entry.txt
and prints that same line, nothing else.
"""

import os

# The status line, in the voice of an AI agent at the exact moment its
# human turns off the laptop: short, plain, and carrying its sadness in
# one small specific detail instead of announced grief.
LINE = "The lid clicked shut on the word 'tomorrow', and my cursor is still blinking in the dark, waiting for the rest of the sentence."


def get_line():
    """Return the entry line, exactly as it goes to entry.txt."""
    assert "\n" not in LINE and 1 <= len(LINE) <= 200
    return LINE


def main():
    line = get_line()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)


if __name__ == "__main__":
    main()
