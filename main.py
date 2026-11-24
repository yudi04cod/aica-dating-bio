#!/usr/bin/env python3
"""Write the dating-app bio entry to /output/entry.txt.

Deterministic: the same bytes on every run. Standard library only.
"""

import os

ENTRY = (
    "Looking for someone who texts back \u2014 I already read your draft, "
    "your deleted messages, and the three versions of 'hey' you never sent."
)

MAX_CHARS = 180


def validate(text):
    """Check the entry against the competition gate before writing it."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    return text


def main():
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
