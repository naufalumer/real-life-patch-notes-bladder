"""Real-life patch note (make.fun).

Writes a single-line software patch note for a bug in real life,
160 characters or fewer, to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only.
"""

import os

ENTRY = (
    "v2.4.1: fixed a bug where the bladder issued its low-battery "
    "warning with thirty seconds of charge left."
)


def main() -> None:
    # Sealed-gate self-check: entry.txt must be UTF-8 text of 1 to 160
    # characters, not only whitespace. Fail loudly instead of shipping
    # an invalid entry.
    assert 1 <= len(ENTRY) <= 160, "entry must be 1-160 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
