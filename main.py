"""Write the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib-only. The line is a single plain-text message from a phone
battery to the charger it waited for all day, kept under the
competition's 200-character gate.
"""

import os

LINE = "I sat at 4% all day by the outlet like a dog at the door, and you stroll in at midnight asking ME to hurry. Plug me in, say sorry, and don't unplug me at 87% again."


def main():
    if not LINE or not LINE.strip():
        raise ValueError("entry line must not be empty")
    if len(LINE) > 200:
        raise ValueError("entry line exceeds the 200-character gate")
    try:
        out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    except KeyError as exc:
        raise RuntimeError("MAKEFUN_OUTPUT_DIR is not set") from exc
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
