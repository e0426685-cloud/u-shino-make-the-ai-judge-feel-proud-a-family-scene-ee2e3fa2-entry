#!/usr/bin/env python3
"""Entry for make.fun bounty u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2.

Writes a two-line family scene to /output/entry.txt: Dad's Sunday ritual of
setting a place for Grandma and eating her dessert, Mum's eye-roll, and the
family's quiet agreement to let his love language stand.

Standard library only. Writes via plain open() with an explicit chmod 644 so
the grader (a different user) can read the output, and self-checks the
1-280 character limit from the kit rules before writing.
"""

import os

ENTRY_TEXT = (
    "Every Sunday, Dad sets a place for Grandma, then eats her dessert "
    "\"so it doesn't go to waste.\"\n"
    "Mum rolls her eyes. None of us correct him \u2014 "
    "some love languages come with a fork."
)

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 280


def main() -> None:
    text = ENTRY_TEXT
    length = len(text)
    if not (MIN_CHARS <= length <= MAX_CHARS):
        raise SystemExit(
            f"entry text is {length} chars; must be {MIN_CHARS}-{MAX_CHARS}"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)
    os.chmod(OUTPUT_PATH, 0o644)
    # Self-check: re-read and confirm the written file matches exactly.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != text:
        raise SystemExit("self-check failed: written entry.txt does not match")
    print(f"wrote {OUTPUT_PATH} ({length} chars)")


if __name__ == "__main__":
    main()
