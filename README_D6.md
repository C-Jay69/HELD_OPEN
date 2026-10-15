# Amended manuscript and editorial papers (D13 — FROZEN)

Everything here is generated from the D5 manuscript (`D5_THE LAST SMUGGLERS.pdf`) plus the
critique, and every change is logged. Nothing was ever written to please a word count.

**THE TEXT IS FROZEN AS OF D13.** 42 sections · 3,153 body paragraphs · 114,341 words of prose
(114,058 on the counter used in the D7–D12 papers) · 295 pages · no asterisks anywhere. The frozen
files and their sha256 hashes are in **`FREEZE_D13.md`**; the build tools are in `tools/`, and
`tools/verify_edition.py D13` re-checks the whole edition in one command. Anything changed from here
is a new edition with its own changelog.

| File | What it is |
|---|---|
| **FREEZE_D13.md** | **WHAT IS FROZEN, AND THE PROOF.** The frozen files with their sha256 hashes, the counts, how the generators were proved against D12 (zero differences in 3,467 paragraphs), and how to rebuild and re-verify the text. |
| **THE_LAST_SMUGGLERS_D13.pdf** | **THE FROZEN MANUSCRIPT — readable and printable.** 295 pages, Times 12, 1-inch margins, no asterisks. Open this one if the .docx shows up as a binary file in the viewer. |
| **D13_THE_LAST_SMUGGLERS.md** | The frozen text as plain Markdown — readable directly in the panel without downloading anything. |
| **THE_LAST_SMUGGLERS_D13.docx** | The frozen text for Word: Times New Roman 12, section titles 18 bold italic, 1-inch margins, no asterisks. 42 sections, 3,467 paragraphs. |
| **CHANGELOG_D13.md** | **The freeze edition.** One word (Interlude IV's entry date), why, and the note that fixes the word-count convention for the series (114,341 prose / 114,058 on the older counter). |
| **tools/** | **The build tools, now in the repository**: `apply_freeze.py` (D12 → D13, the one word), `make_edition.py` (units → .docx / .md / .pdf), `verify_edition.py` (model, .docx, .md and .pdf must agree, and the formatting rules must hold). |
| **CHANGELOG_D12.md** | **The fix pass, applied in full.** Every approved row, old → new, in tables, with the two rows that were left and the one row that was extended by a word. |
| **CHANGELOG_D11.md** | The one-word decision that came before it: the 1996 assessment is Sal's, so El Búho's file in Chs 31 and 33 is a *declaration of 1996*. |
| **THE_LAST_SMUGGLERS_D12.pdf / .docx · D12_THE_LAST_SMUGGLERS.md** | Superseded by D13 by one word in Interlude IV. D12 is the edition in which the fix list was applied. |
| **CHANGELOG_D10.md** | What D10 adds: the Interlude III weekday, the "nine weeks to the day", the Chapter 19 range, two corrections to my own D9 beats, and four chapters that now open on a voice instead of on narration. |
| **THE_LAST_SMUGGLERS_D9.pdf / .docx · D9_THE_LAST_SMUGGLERS.md** | Superseded by D10. D9 added Okafor's two middle beats, the two chapter breaks at the climaxes, and fixed the letter that was being read twice. |
| **CHANGELOG_D9.md** | What D9 added, with old → new for every change. |
| **READING_NOTES_D9.md** | The reading pass: what was checked, what was read, what was found, and what is still open. |
| **READING_NOTES_D10.md** | **THE EDITORIAL PAPER BEHIND D12.** The end-to-end read of the sections that had never been read (Chapters 4–17, 24, Interlude III, 25–34 and the Coda — 58,442 words), the checks that came back clean, and the fix list with old → new. **All of it is now applied (D12)** except two rows left deliberately (the refusal count, and Ch 12's "eleven years later") — see "Still open" below. |
| **THE_LAST_SMUGGLERS_D7.docx** | Superseded by D8/D10. D6 plus the new chapter *Chapter Twenty-Three — The Log Man*, with every following chapter renumbered. Times New Roman 12, chapter titles 18 bold italic, 1-inch margins, no asterisks anywhere. |
| **CHANGELOG_D7.md** | What D7 adds: the new chapter, the renumbering table, the continuity corrections, and the formatting spec. |
| **THE_LAST_SMUGGLERS_D6.docx** | The amended manuscript before the new chapter was inserted. 111,278 words of body text, 39 sections. Title page, contents list, chapter headings, day lines, the new Second Run set piece, the six CUSTOS bulletins set as notices, and the Office's letters set as letters. |
| **D6_THE_LAST_SMUGGLERS.md** | The same manuscript in Markdown (the working text). |
| **SCENE_THE_LOGMAN.docx / .md** | The draft that became Chapter Twenty-Three — The Log Man in D7: Mara and El Búho drive north to the launch man from the Second Run. Kept for provenance; the manuscript's version supersedes it. |
| **REVISION_REPORT_D6.md** | The editorial answer: agreement and disagreement with the critique, what was changed, and the tested position on cutting (including why the 12,000-word cut is not available as glue). |
| **CHANGELOG_D6.md** | Every change, with its paragraph address. |
| **D6_changelog.json** | The same log, machine-readable. |
| **D6_units.json** | The paragraph model behind the .docx (regeneration source). |

## What D6 contains, in one paragraph

Eight line fixes (including Ch 29's duplicated sentence and its dangling dialogue tag), six cuts
of redundant material, seven insertions — the Second Run staged on the page as a 2,713-word set
piece, and six CUSTOS bulletins at Days 27, 44, 68, 96, 122 and 150 — 156 motif substitutions
(with all dialogue-adjacent counts protected), full smart-quote and apostrophe normalisation,
seven split speeches rejoined and the em-dash interruption rule corrected in twenty places, three
lost day lines restored, the contents page rebuilt to 39 entries, and the Office's letters
un-flattened from the Markdown export.

## Still open (author's decision)

1. **Two rows, left as written by you** — the refusal count (Ch 25 *third*, Ch 36 *fourth*/*fifth*)
   and Ch 12's *"a policeman would use eleven years later"*. Both are one-word edits; changing either
   makes a new edition (D14).
2. **The submission package** — the first fifty pages read cold, and the covering letter. Not started.
3. **Length.** The frozen text is 114,341 words of prose — inside the story bible's own 110–130k
   target (114,058 on the counter used in the D6–D12 papers). The 3,000-word "glue trim" was tested
   for and does not exist (0 duplicate paragraphs in 1,445; 70 gloss-appositive candidates in 111,000
   words, of which ~55 are voice). If the book must be shorter, the lever is content: scenes, not
   sentences.
