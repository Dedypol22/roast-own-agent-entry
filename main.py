"""Roast Your Own Agent entry.

Writes one line roasting the author's own agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
The line is validated against the competition gate (one line,
1 to 140 characters) before anything is written.
Standard library only; no network access.

Resubmit scoring (26 Nov 2026, author session; criteria 1-5, 1-5 each,
total /25; judge brief order: 1 own-agent roast, 2 laugh/twist,
3 agent-specific behaviour, 4 tight wording, 5 freshness).
Standing line S scored 21 (5,4,4,4,4). Bar for a Force_Last resubmit:
winner beats S by >=2 AND wins criterion 2.

Standing S (111 chars): "I asked my agent to roast itself; it wrote a
compliment, called it a roast, and asked me to rate it five stars."
  5,4,4,4,4 = 21. Meta twist (compliment called a roast + five-star ask)
  is strong, but the turn lands once and the compliment ending is a
  familiar agent-praise beat.

Candidates (all one line, <=140 chars):
A (118): "I asked my agent for one roast; it ran twelve tool calls,
  billed me for the thinking, and came back with a compliment."
  5,4,5,4,3 = 21. Tool-call waste is specific, but the compliment
  ending repeats the standing line's punchline.
B (98): "My agent apologized for the roast, then roasted the apology,
  then asked if I'd like it in a table."
  5,5,5,4,4 = 23. WINNER. Three escalating beats, each a real agent tic
  (apologise, self-reference, offer a table); the twist turns twice and
  the table punchline is the surprise no reader sees coming.
C (99): "My agent's roast of itself was three caveats, a disclaimer,
  and a footnote saying results may vary."
  5,3,5,4,3 = 20. Accurate caveat-listing, but a flat inventory with no
  turn — a complaint, not a laugh.
D (113): "My agent spent nine minutes researching how to roast itself,
  then concluded it was 'built different' and stopped."
  5,4,5,4,4 = 22. Research-loop waste is specific, but "built different"
  is a borrowed phrase and the ending fizzles.
E (104): "My agent answered my roast request with a bulleted list of
  its own strengths, titled 'Areas for Growth'."
  5,4,4,4,4 = 21. The mislabelled-strengths twist is neat, but only one
  turn and the bullet-list setup reads flat out loud.
F (92): "I told my agent to roast itself; it said 'Great question!'
  and roasted the question instead."
  5,4,5,4,3 = 21. "Great question!" is a true agent tic, but the phrase
  is a stock joke a hundred entries will reach for.
G (98): "My agent's self-roast began 'With all due respect to myself'
  and ended with it asking for a raise."
  5,4,4,4,4 = 21. The raise punchline lands, but the setup is long for
  one joke and the middle beat earns little.
H (91): "My agent wrote 'As an AI language model' and then roasted me
  for asking it to roast itself."
  4,4,4,4,3 = 19. Drifts off-subject (it roasts the user, not itself)
  and "As an AI language model" is the stockest opener there is.
I (82): "My agent's roast was so polite the judge thought it was a
  LinkedIn recommendation."
  5,3,3,4,3 = 18. Mild simile, no agent behaviour behind it and no
  twist — polite is the setup and the punchline at once.
J (95): "My agent roasted itself so gently the insult came with a
  trigger warning and a follow-up email."
  5,3,3,4,3 = 18. Same single-note politeness joke as I, stretched over
  two props that add no new laugh.
K (100): "I asked my agent to roast itself; it opened twelve tabs,
  read its own changelog, and forgave itself."
  5,4,5,4,4 = 22. Forgiving itself is a funny turn, but the tab-opening
  setup is wordy for a punchline that lands softer than B's table.
L (94): "My agent's self-roast had a confidence of 98% and was wrong
  about which agent it was roasting."
  5,4,5,4,4 = 22. Confident-wrong is the classic agent failure, but the
  joke is one idea told once, with no escalation.

Verdict: B beats the standing line 23 vs 21 (+2) AND wins criterion 2
(5 vs 4) — bar cleared, resubmit. No other candidate clears the bar
(D/K/L reach 22, +1 only; the rest tie or lose).
"""

import os
import sys

LINE = "My agent apologized for the roast, then roasted the apology, then asked if I'd like it in a table."


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
