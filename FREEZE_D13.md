# THE TEXT IS FROZEN — D13

**Frozen edition: D13.** It is D12 as you approved it, plus the single word the read found after
the list was closed: Interlude IV's *"It was entered in **the twelfth year**, in the pilot period"*
→ *"…in **the first year**, in the pilot period"*. 3,943 nights is ten years and nine months, and
the pilot period is where the construction entered the machine (Ch 33: *"Eleven years ago, in
Rotterdam"*); the twelfth year is the present (Ch 17: *"and then, in the eleventh year,
accommodation"*). Nothing else was touched. Full old → new: `CHANGELOG_D13.md`.

---

## The frozen files

| file | what it is | sha256 |
|---|---|---|
| **THE_LAST_SMUGGLERS_D13.docx** | the manuscript for Word: Times New Roman 12, section titles 18 bold italic, 1-inch margins, no asterisks, 42 sections, 3,467 paragraphs | `cf9faa1fd55c6d038a4e5801666ca3a3c76668babea640b9f4ac5e4825082c72` |
| **THE_LAST_SMUGGLERS_D13.pdf** | the same text, typeset and printable — 295 pages | `71c8bf51abe18522e71b468ca038530b2b29c23f5d0a64dca3bf4640fd79d067` |
| **D13_THE_LAST_SMUGGLERS.md** | the same text as plain Markdown, for reading in the panel | `3ae1410f197fbbf712de2e6923cd471f2e5e581a2b4191a5bb4c093fcddfe5a0` |
| **D13_units.json** | the model the three are generated from — 42 sections, 3,153 body paragraphs | `d7a5dc0941a76e9009384e9fc885bbb9461b32b7eaf82283207fe02262477231` |

## The numbers

- **42 sections**: prologue (*Flight Path*), 36 chapters, 4 CUSTOS interludes, Coda.
- **3,153 body paragraphs** — 3,147 the reader reads as prose, plus the 6 CUSTOS bulletin heads.
- **114,341 words of prose.** On the counter used in the D7–D12 papers (prose + bulletin heads,
  less the 42 section titles and the 42 day lines) the same text reads **114,058** — which is what
  D12 was, as expected: the freeze swapped one word for another. Earlier editions reported
  114,053 (D10/D11) and 114,004 (D9).
- **141 section breaks** (centred • • •), **41 day lines**, **42-entry contents list**, and
  **0 asterisks** in any of the three reading formats.
- Within the story bible's own 110–130k target.

## How it was verified

`tools/verify_edition.py D13` — the model, the .docx, the .md and the .pdf must agree paragraph for
paragraph, and the formatting rules must hold (1-inch margins, Times New Roman 12, 18pt bold-italic
titles, italic day lines, complete contents, no asterisks). It passes.

The generators themselves were proved against the previous edition first: rebuilding D12 from
`D12_units.json` with `tools/make_edition.py` reproduces the committed D12 `.docx` exactly —
**3,467 paragraphs, zero differences** in text, size, weight, italics, alignment, spacing or page
breaks — and reproduces the D12 Markdown byte for byte (same md5). So what is frozen is what you
read and approved, re-derived from the model rather than copied.

## Reproducing, and what the freeze means

```
python tools/apply_freeze.py                 # D12_units.json -> D13_units.json (the one word)
python tools/make_edition.py D13_units.json D13   # -> .docx, .md, .pdf
python tools/verify_edition.py D13                # must print OK
```

The build tools now live in the repository (`tools/`), so the text is reproducible by anyone with
the repo and three Python packages (`python-docx`, `reportlab`, `pypdf`).

**From here the text does not change.** Any further change — a word, a comma, a line — makes a new
edition (D14) with its own changelog and its own hashes. The two rows left deliberately are the only
open questions, and both are recorded in `README_D6.md`: the refusal count (Ch 25 *third*, Ch 36
*fourth*/*fifth*) and Ch 12's *"a policeman would use eleven years later"*.

## What stays outside the text

Nothing in this freeze touches the editorial record. `READING_NOTES_D10.md` still holds the read
that produced the fix list; `CHANGELOG_D6`–`D12` still hold every change with its reason;
`D1_THE LAST SMUGGLERS.pdf` and `THE_LAST_SMUGGLERS_full_manuscript.docx` remain as the original
manuscript everything is measured against.

**Next: the submission package** — the first fifty pages read cold, and the covering letter.
