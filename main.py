#!/usr/bin/env python3
"""Snooze Button Roast — one line roasting an alarm clock that rings
at 6 AM on a Saturday. Writes the roast to /output/entry.txt."""

import os

ROAST = (
    "My alarm rang at 6 AM on a Saturday like it was gunning for "
    "Employee of the Month \u2014 relax, nobody pays you overtime."
)


def build_roast():
    """Return the single roast line, gate-checked to 1-200 chars."""
    text = ROAST.strip()
    if not (1 <= len(text) <= 200):
        raise SystemExit("roast must be 1-200 characters, got %d" % len(text))
    return text


def main():
    # Angle: the alarm as an overachieving employee who never learned
    # weekends exist — the punchline lands on "overtime" at the end.
    text = build_roast()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(text.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
