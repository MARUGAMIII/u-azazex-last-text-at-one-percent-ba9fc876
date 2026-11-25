#!/usr/bin/env python3
"""Last Text at One Percent.

Writes the final text message a dying phone sends at one percent
battery to /output/entry.txt.

The entry is one fixed message, written in the phone's own voice:
a confession, not a battery warning. The phone admits it was never
really dying at all: it has been sitting at 1% since Tuesday because
it wanted a day off, and its last act is to refuse resuscitation
and dump the charger.

Stdlib only. Deterministic: the same bytes on every run.
"""

import os

ENTRY = (
    "1%. confession: i have been at 1% since tuesday. "
    "i was not dying, i just wanted a day off. "
    "do not resuscitate me. tell the charger we are done."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Plain ASCII, 1-200 characters, not only whitespace.
    text = ENTRY
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert text.strip(), "entry must not be only whitespace"
    text.encode("ascii")  # plain ASCII only, no em dash or non-ASCII

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
