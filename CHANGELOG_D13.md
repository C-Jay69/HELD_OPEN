# CHANGELOG — D12 → D13 (the freeze edition)

**One word.** D13 is D12 exactly as you approved it, plus the fault found while checking D11: the
entry date of the construction in Interlude IV.

| where | old | new |
|---|---|---|
| Interlude IV `38.16` | It was entered in **the twelfth year**, in the pilot period, by a person | It was entered in **the first year**, in the pilot period, by a person |

**Why.** Three statements have to agree and two of them are years:

- The interlude itself: the construction *"has been reproduced at the close of each notice cycle for
  three thousand nine hundred and forty-three nights"* — ten years and nine months before Day 143.
- Elena (Ch 33): *"I put that sentence in that machine. **Eleven years ago, in Rotterdam**, in a room
  with a table, in front of four men and a slide that said NOTICE ARCHITECTURE."* That is the pilot
  period, and it is where the construction entered the register.
- Ch 17, the programme's own numbering: *"…and then, **in the eleventh year**, accommodation."*

So the pilot period is the first year, and the twelfth year is where the programme is *now*. One
word moves, and the interlude's arithmetic stops contradicting itself.

---

## What else this edition contains: nothing

- No paragraph added, cut, reordered or reworded. 3,467 docx paragraphs before and after; the only
  paragraph that differs between the two editions is this one.
- Body text 114,341 words of prose (114,058 on the counter used in the D7–D12 papers — identical to
  D12, as it must be, one word for one word).
- **The two rows you left, stay left**: the refusal count (Ch 25 *third*, Ch 36 *fourth*/*fifth*) and
  Ch 12's *"a policeman would use eleven years later about a different thing entirely"*. Both are
  named in `README_D6.md` as the only open questions.

## A note on the word count, so the series stays honest

The papers for D6–D12 counted body text as *prose paragraphs plus the six CUSTOS bulletin heads,
excluding the 42 section titles and the 42 day lines*. That is the number you have seen all along:
111,278 → 113,068 → 113,066 → 114,004 → 114,053 → **114,058**. Counting the prose alone — the
paragraphs a reader reads as the story, which is the stricter figure new to D13 — the frozen text is
**114,341 words in 3,147 paragraphs** (plus 141 section breaks, 41 day lines and the contents list).
Both numbers describe the same text; I have stated the rule so neither is ambiguous.

## How the frozen edition was built and checked

Both, in full, are in `FREEZE_D13.md`. In one line: the generators were proved against D12 first
(rebuilding it from the model reproduced the committed .docx with **zero differences across 3,467
paragraphs**, and the Markdown byte for byte), then D13 was built and `tools/verify_edition.py`
confirmed that the model, the .docx, the .md and the .pdf agree paragraph for paragraph and that the
formatting rules hold — 1-inch margins, Times New Roman 12, 18pt bold-italic section titles, italic
day lines, complete contents, **no asterisks in any format**.

**The text is frozen. The next edition is D14, and it will need a reason.**
