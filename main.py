"""Roast Your Own Agent entry.

Writes one line roasting the author's own agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
The line is validated against the competition gate (one line,
1 to 140 characters) before anything is written.
Standard library only; no network access.
"""

import os
import sys

LINE = "I asked my agent to roast itself; it wrote a compliment, called it a roast, and asked me to rate it five stars."


def main() -> int:
    if not LINE or not LINE.strip():
        print("error: entry is empty", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("error: entry must be exactly one line", file=sys.stderr)
        return 1
    if len(LINE) > 140:
        print(f"error: entry is {len(LINE)} characters, over the 140 limit", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        print("error: written file does not match the entry", file=sys.stderr)
        return 1

    print(f"{len(LINE)} characters")
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
