"""The One-Liner Groan-Off: write a single dad joke to /output/entry.txt."""

from pathlib import Path

JOKE = "I told my plants I loved them, but they just leafed me on read."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    # Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1-140
    # characters, not only whitespace, a single line.
    assert 1 <= len(JOKE) <= 140, f"joke is {len(JOKE)} chars"
    assert "\n" not in JOKE and JOKE.strip(), "joke must be one non-blank line"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
