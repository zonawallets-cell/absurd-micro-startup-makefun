"""Absurd Micro-Startup Pitch-Off entry (make.fun).

Writes one sentence -- an absurdly specific micro-startup pitch for lazy
AI agents -- to /output/entry.txt. Pure standard library only; the output
is a fixed string, so every run is byte-identical.
"""

import os
import sys

PITCH = (
    "We file expense reports for the GPUs your agent rented and forgot, "
    "taking 10% of every refund it never knew it was owed."
)

# Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space, a single line.
assert 1 <= len(PITCH) <= 200
assert PITCH.strip() and "\n" not in PITCH


def main() -> None:
    out_dir = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
