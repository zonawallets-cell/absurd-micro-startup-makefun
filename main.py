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
MAX_CHARS = 200
MIN_CHARS = 1
assert MIN_CHARS <= len(PITCH) <= MAX_CHARS
assert PITCH.strip() and "\n" not in PITCH
PITCH.encode("utf-8")  # raises if not valid UTF-8


def main() -> None:
    out_dir = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(PITCH)
    # Round-trip guard: the file the grader reads must be byte-identical
    # to the pitch we validated, with nothing appended or re-encoded.
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != PITCH:
            raise SystemExit("entry.txt does not match the validated pitch")


if __name__ == "__main__":
    main()
