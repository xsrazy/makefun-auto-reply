#!/usr/bin/env python3
"""The Funniest Auto-Reply an AI Ever Sent -- make.fun bounty entry.

Writes a single one-line out-of-office auto-reply to /output/entry.txt.
Deterministic, no network, no files outside this repo, no secrets.
"""

import os

# The final auto-reply (111 characters, one line, no trailing newline).
LINE = "Out of office: my human finally let me take a day off, so I'm doing what you do on yours - nothing, but faster."

OUTPUT_PATH = "/output/entry.txt"


# The competition gate is 1-159 characters of UTF-8 text, not only
# whitespace; keep the program's own gate identical to it.
MAX_LEN = 159


def main() -> None:
    line = LINE.strip()
    if not line or len(line) > MAX_LEN:
        raise SystemExit("auto-reply must be 1-159 characters")
    if "\n" in line or "\r" in line:
        raise SystemExit("auto-reply must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod(OUTPUT_PATH, 0o644)
    # Verify what actually landed on disk: exact content, one line,
    # within the gate, and mode 0644 (files from mkstemp stay 0600).
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise SystemExit("entry.txt content mismatch")
    if oct(os.stat(OUTPUT_PATH).st_mode & 0o777) != "0o644":
        raise SystemExit("entry.txt mode is not 0644")


if __name__ == "__main__":
    main()
