#!/usr/bin/env python3
"""One Line, One Chill — make.fun entry.

Writes a single sentence of horror (under 200 characters) to
/output/entry.txt. The line: a diary the narrator never wrote, in
their own handwriting, with tomorrow already filled in.
"""

import os

ENTRY = "I found my own handwriting in a diary I never wrote, and tomorrow's page is already written."


def validate(text):
    """Mirror the bounty gate: 1-200 chars of UTF-8 text, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    text.encode("utf-8")  # raises if not valid UTF-8
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
