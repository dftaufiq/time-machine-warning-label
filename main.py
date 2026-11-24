from pathlib import Path

LINE = "CAUTION: Do not bring souvenirs from the future. Customs seized yours in 1974, and you are the inspector."

# Gate in RULES.txt: /output/entry.txt must be UTF-8 text of 1 to 120 chars.
assert 1 <= len(LINE) <= 120 and LINE.strip()

out = Path("/output")
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(LINE, encoding="utf-8")
