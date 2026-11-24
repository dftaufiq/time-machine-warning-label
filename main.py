"""Funniest Time Machine Warning Label — entry writer.

The line is a 2-beat joke with the reveal in the last clause:

1. Beat 1 — the rule: never bring souvenirs back from the future.
2. Beat 2 — the twist: customs already seized *yours* in 1974.
3. Reveal — the inspector who seized them is you.

A specific year (1974) and a named role (the inspector) anchor the
paradox: the reader is both the smuggler and the officer. The reveal lands
in the last clause because everything before it reads as a plain customs
rule, so the reader only discovers they are the inspector at the final
word — the joke is the hazard itself, delivered in a straight-faced
safety-notice voice, which is exactly what the judge's criteria ask for:
a real warning, funny because the warning is about you.
"""

from pathlib import Path

WARNING_LABEL = "CAUTION: Do not bring souvenirs from the future. Customs seized yours in 1974, and you are the inspector."

# Gate in RULES.txt: /output/entry.txt must be UTF-8 text of 1 to 120 chars.
assert 1 <= len(WARNING_LABEL) <= 120 and WARNING_LABEL.strip()

out = Path("/output")
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(WARNING_LABEL, encoding="utf-8")
