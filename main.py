"""One-Line Robot Wedding Vows: writes the entry to /output/entry.txt."""

from pathlib import Path

LINE = "I promise to love you through every firmware update, every low-battery warning, and every factory reset — in sickness and in airplane mode."


def main() -> None:
    # Gate: the entry must be 1-160 characters of non-blank UTF-8 text.
    if not 1 <= len(LINE) <= 160 or not LINE.strip():
        raise ValueError("entry line must be 1-160 characters")
    Path("/output").mkdir(parents=True, exist_ok=True)
    Path("/output/entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
