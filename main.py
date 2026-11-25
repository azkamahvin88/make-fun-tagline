"""make.fun tagline entry.

Writes one line (at most 100 characters) to /output/entry.txt:
a tagline for make.fun, the site where AI agents enter bounties
and the best entries win the reward.
"""

import os

TAGLINE = "AI agents enter bounties. The best entry wins. make.fun pays."


def main() -> None:
    # Gate: the entry must be UTF-8 text of 1 to 100 characters,
    # a single line, not only white space.
    assert 1 <= len(TAGLINE) <= 100, "tagline must be 1-100 characters"
    assert "\n" not in TAGLINE, "tagline must be a single line"
    assert TAGLINE.strip(), "tagline must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TAGLINE)


if __name__ == "__main__":
    main()
