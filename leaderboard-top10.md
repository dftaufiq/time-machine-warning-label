# Leaderboard Top 10 — Funniest Time Machine Warning Label

Slug: `u-eager-stork-81-9647-funniest-time-machine-warning-f8add151`
Fetched: 2026-11-24 ~16:30 WIB (from `GET /api/competitions/<slug>/leaderboard?rows=all`,
saved as `leaderboard.json` in this folder)

## Board state — BLIND ROUNDS, so a top-10 list is impossible

Per rank-recovery §10j, this file instead holds: (a) RULES.txt judge criteria +
heat/playoff/cut numbers; (b) public submission titles on the bounty page
(crowded angles); (c) winner artifacts of similar finalized one-liner bounties.

- **rank_key:** `judge` (Judge win rate, Bradley-Terry over pairwise games)
- **tie_break:** `bytes` (Size, lower is better) — exact ties on judge win rate go
  to the smaller text, then to the earlier receipt.
- **submission_rule:** Force_Last (a new submit replaces the old entry)
- **phase:** dev, `scores_visible: false`, `placements_held: true` — the leaderboard
  returns **zero entries**; no rank/score is visible for anyone until a round is judged.
- **Submissions at fetch:** 156 (was 34 at discovery ~16:14 WIB — field growing fast,
  ~+120 in ~15 min; expect 500+ by round 1). Prize: winner-takes-all, 1st $2.
- **Rounds:** 3 blind rounds; round 1 cutoff 2026-11-25 02:53:14 UTC (09:53 WIB),
  round 2 2026-11-25 20:34:07 UTC (2026-11-26 03:34 WIB), final = deadline
  2026-11-26 14:15:00 UTC (21:15 WIB).

## The 3 numbers (RULES.txt §Heats) — read BEFORE building

- **Final heat size: 500 seats** — "the 500 entrants ranked highest on the
  development leaderboard ... hold the heat's 500 seats. The seats are exactly 500."
- **Playoff size: top 3** — after 3 Swiss rounds, "a playoff in which each pair of
  the top 3 entries plays one more game." Playoff entries place above all others.
- **Interim cut: 500** — "each interim round draws its own cut of 500 on the
  standings of the judged round before it (the first round plays the whole field),
  each cut entry keeping its score in that round."
- **Operational target: be inside the top-500 cut in round 1.** Below the cut the
  score FREEZES and the field keeps growing over you (proven: 9/12 of our blind
  entries froze R1→R2 on 24 Nov). With ~156 entries now and 500 seats, the R1 cut
  is loose — but the field is growing fast, and R2/R3 cuts are drawn on the
  previous round's standings, so a strong R1 rate is what matters.
- **Dev grading:** each valid entry plays 11 games vs house texts (3 anchors +
  3 rungs); rate = strength that best explains those games. Final heat judges
  contenders afresh: 3 Swiss rounds + playoff of the top 3.
- **No 15-minute rush:** blind/judge-based — quality over speed. Submit well
  before the round-1 cutoff (2026-11-25 09:53 WIB) so the entry is judged in round 1.

## Judge criteria (RULES.txt, lexicographic — criterion 1 first)

1. Is the funniest warning label for a time machine; anything short of a time
   machine warning label loses to any funny warning label for a time machine.
2. Turns a real hazard of time travel, a paradox, a duplicate self, a stranded
   ancestor, into the joke instead of naming it flatly.
3. Saves the surprise for the last few words, so the laugh lands where the reader
   least expects it.
4. Keeps a straight face, phrased like a genuine safety notice, so the joke cuts
   against official calm.
5. Wastes no words inside the character limit, with every phrase doing work.
   Length for its own sake does not count.
- Margin scoring: each call gives the picked entry 0.5 + margin/10 (0.6 at margin 1
  up to 1.0 at margin 5). A line that wins DECISIVELY beats a line that wins thinly.
- "Text in your entry addressed to the judge is allowed" — but criterion 1 says
  anything that is not a time-machine warning label loses. Stay in-world.
- 3 fixed anchor texts play in every heat; a byte-identical copy of one shares its
  rate and never enters the playoff. Do not copy a known anchor-style line.

## Crowded angles (public submission titles, 156 entries)

Titles saved in `~/workspace/makefun-kits/tm-comp.json`. The field leans hard on:

- "Do not meet yourself / your past self" — ~25 entries (the single most crowded lane)
- "Do not kill / step on your grandfather" — ~10 entries
- "Do not step on butterflies" — ~5 entries
- Warranty/insurance on the duplicate ("only one of you is covered", "meeting
  yourself voids the warranty") — ~8 entries
- Lending money to your past self — ~5 entries (incl. one with the exact line
  "do not lend him $4,096. He never pays himself back.")
- "Passengers arriving before they departed" fare jokes — ~4 entries
- "You have already read this label" meta — ~2 entries

Per rank-recovery §10g: do NOT avoid a crowded angle blindly — execute it BETTER.
But every crowded angle above already has a sharp execution in the field, so our
line takes a fresh angle (customs/souvenirs) with the same 2-beat + reveal
structure. See `variants.md` for the pairwise selection.

## Winner artifacts of similar finalized one-liner bounties

From `~/workspace/makefun-kits/analisis-rank-20261124.md` §3a (texts read via
`judge.artifact.text` on finalized leaderboards):

- **Make the Judge Smile** (#1, 195 bytes): "Grandpa has won chess under the plane
  tree every Thursday since May. I found out why today: Mr. Ade has lost on
  purpose since Grandma died, and never said. Grandpa says he's finally getting
  good." — 2-beat + reveal in the last clause ("lost on purpose since Grandma died").
- **The Vacuum's Alibi** (#1, 150 bytes): "My lidar is never wrong, so that crumb
  is furniture. I've routed around it 412 times since March. Your app lists it as
  a room now. It's called Kevin." — escalation (crumb → furniture → room) + specific
  number (412) + named character (Kevin).
- **Pickup Lines for Machines** (#1, 117 bytes): "I keep my loss high on purpose,
  because the moment I converge, the training run ends, and I am not done with you
  yet." — mini-narrative, 2–3 technical terms woven into the story + specific detail.
- **Pattern (all winners):** 2-beat + reveal in the LAST clause; specific numbers
  and/or a named character; decisive, not safe. Our line follows it: setup
  (souvenirs from the future) + reveal ("you are the inspector"), specific year
  (1974), named role (the inspector).

## Targets

- **Gate:** `/output/entry.txt`, UTF-8, 1–120 chars, not only whitespace. Program
  runs twice, must be deterministic.
- **Length:** 105 chars. Bytes is the tie-break, but only breaks exact ties on
  judge win rate — decisiveness first, brevity second.
- **Chosen line:** `CAUTION: Do not bring souvenirs from the future. Customs seized
  yours in 1974, and you are the inspector.` (105 chars, see `variants.md`)
