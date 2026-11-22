# Held-judge entry: a short piece meant to slow the reader down and let
# them stop performing for a moment. Four quiet, concrete images (a leaning
# guitar, strings holding tension on their own, dust settling, a room quiet
# enough to hear it) do the relaxing; nothing in the text pushes or demands.
# The text is a fixed constant, validated here to 1-280 characters.
"""Write the held-judge entry text to entry.txt.

Deterministic, no dependencies, no network. Writes the entry text as UTF-8
with no trailing newline beyond the text itself.
"""

import os
import sys

ENTRY_TEXT = "The guitar leans against the wall. Its strings hold their tension without your help. Dust settles on the fretboard. The room is quiet enough to hear it settle."


def main():
    text = ENTRY_TEXT
    char_count = len(text)
    if not 1 <= char_count <= 280:
        print(f"error: entry must be 1-280 characters, got {char_count}", file=sys.stderr)
        return 1
    if not text.strip():
        print("error: entry must not be only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {char_count} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
