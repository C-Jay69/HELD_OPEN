# -*- coding: utf-8 -*-
"""Emit revision/CHANGE-LOG.md from the applied edit list."""
import json, sys
import os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
OUT = os.path.abspath(os.path.join(HERE, ".."))
from edits import EDITS, DIVIDER_FROM, DIVIDER_TO

ap = json.load(open(os.path.join(HERE, "applied.json")))
A = {a["id"]: a for a in ap["applied"]}

CAT_ORDER = [
    "Continuity — March window", "Continuity — number slip", "Continuity — typo",
    "Housekeeping — interlude numbering", "Housekeeping — motif",
    "Line rule 3 — meta register", "Line rule 2 — summary tic",
    "Line rule 5 — similes", "Line rule 4 — numbers", "Line rule 1 — mechanism",
]

def rows(cats):
    out = []
    for eid, cat, idx, old, new, note in EDITS:
        if cat not in cats:
            continue
        loc = A[eid]["loc"] if eid in A else "?"
        out.append((eid, cat, loc, idx, old, new, note))
    return out

def table(items):
    L = ["| # | Location | Before → After | Why |", "|---|---|---|---|"]
    for eid, cat, loc, idx, old, new, note in items:
        b = old.replace("|", "\\|").strip() or "—"
        a = new.replace("|", "\\|").strip() or "—"
        L.append(f"| **{eid}** | {loc} | *{b}* → **{a}** | {note} |")
    return "\n".join(L)

doc = []
doc.append("# D3 — revision pass: change log\n")
doc.append("**Source:** `editorial/source/D3_THE_LAST_SMUGGLERS.pdf` (D3, 110,164 words of body text as extracted).  \n"
           "**Deliverables:** `D3_REVISED_manuscript.md` · `D3_REVISED_manuscript.docx` (clean) · `D3_REVISED_marked.docx` (insertions highlighted, deletions struck through).  \n"
           "**Compiled:** 14 October 2026.\n")
doc.append("---\n")
doc.append("## 1. What this pass is, and what it is not\n")
doc.append(f"""This is the **continuity pass and the line pass**, applied in one sweep, exactly as the assessment's §8 sequence recommended — with one difference: the structural cut (`revision-plan.md`, Tier 1 ≈4,350–5,000 words) has **not** been done, because you asked for the fixes and the lines. So the file you have is D3 made *consistent* and D3 made *quieter*, at the same length: **110,164 → 110,033 words (−131)**, in **{len(EDITS)} edits** across the book's 34 chapters, four CUSTOS interstitials and the coda.

That is deliberately a small number of words. Every one of the six line rules is applied where the text supports it, and where it doesn't I have said so rather than manufactured a cut — §4 below is the pushback section, and it is longer than usual because three of the six rules turned out to be either misdiagnosed or already satisfied.

**Scope boundary (unchanged from the assessment):**
- The cut pass (~4–5k, `revision-plan.md`) is still to do. Do it after you have read this, not before.
- The two additions the critique asked for — the Garrity scene (§4.4) and one beat for Ada (§4.3) — are still to do, and are still to be paid for out of the cut pass.
- Nothing was added anywhere in this file.

**Scope of the file:** the revision contains all 39 sections in D3's order — 34 chapters, the four CUSTOS interstitials (Dakar, Notices, Kestrel Field, Interlude IV) and the coda. Word counts here are on the extraction used for this pass, which counts the contents list; the assessment's 109,782 was the same PDF on a slightly different tokenisation, so read the **delta** (−131) as the meaningful figure rather than the absolute one. Every edit below is anchored to an exact paragraph and verified by exact-string match, so nothing but the listed edits differs — see §5.
""")
doc.append("---\n")
doc.append("## 2. The continuity fixes\n")
doc.append("""The seven flags from `continuity-audit.md`, plus the three housekeeping items. Six of the seven are fixed exactly as the audit proposed. **One is fixed differently, and the reason matters** — see FLAG 2 below.

### The March window, after this pass\n
| Day | Date | Event | Where |
|---|---|---|---|
| 71–75 | 10–14 Feb | Mesa is collected at the annex; taken to the western facility | Ch. 20 |
| 79 | **18 Feb** | Mesa's intake interview at the western facility | Ch. 24's letter (**new date**) |
| 80 | 19 Feb | The Office's letter arrives; the blame argument | Ch. 24 (flashback) |
| 86–93 | 25 Feb – 4 Mar | The crew reads the letter; Kavanagh's plan; Naas | Ch. 22 |
| 91 | **2 Mar** | Crane files the category review; Kavanagh signs the sponsoring certification | Ch. 22 / Ch. 25 receipt (**new date**) |
| 105 | **16 Mar** | Port completion interview; the vault collection begins | Ch. 23 / Ch. 24 |
| 105–108 | 16–19 Mar | The collection days; Sal's burning; the kitchen scene | Ch. 24 (**re-stamped**) |
| 108 | 19 Mar | Sal's application is written and stays on the desk / under the mattress | Ch. 24 |
| 122 | 2 Apr | The movement; the register line; the reconciliation opens | Ch. 28 |

Application arithmetic now closes: **Day 91 + 11 (category review) + 3 (appointment) = Day 105 = the sixteenth of March.**\n""")

doc.append("### FLAG 1 — the arithmetic to the sixteenth\n")
doc.append(table(rows(["Continuity — March window"])))
doc.append("""
### FLAG 2 — why the eighth of March had to move, not be kept\n
The audit recommended keeping the eighth and making it explicit: *"interviewed at the western facility on the eighth of March."* I tried that, and it breaks the book in a place the audit didn't check.

In **Ch. 22, opening scene (Days 86–93, i.e. 25 February – 4 March)** the crew is already holding that exact letter — not a similar one, the same one: *"Mara had it in front of her — the letter from the office, the one with a typo in it, and she read the middle paragraph out loud for the third time in a week"*, followed by *"The person concerned has requested that his profession be entered as maritime. The request has been granted."* That sentence is verbatim the Ch. 24 letter. A letter written *after* an interview on 8 March cannot be read aloud on 25 February, and the whole Ch. 22 plan (the maritime category → the designated port office) is built on it.

So the March date on that interview is a second relic of the same moved schedule as FLAG 1 — the interview was once the 8th, the appointment moved to the 16th, and this date was left behind. The interview therefore moves to the one part of the window that can hold it: the facility intake, after Mesa's collection (~14 February) and early enough for the letter to reach the crew before Ch. 21's plan meeting. **18 February (Day 79)** sits inside Ch. 21's own Days 77–85 stamp, requires no scene to move, and leaves 2 March as the only March date in the window — which is what Kavanagh's receipt now acknowledges.

Two consequences worth knowing:
1. It also **resolves Housekeeping item 4** (the Ch. 22 "typo" reference being premature). In story time the crew has now had the letter, typo and all, for a week before Ch. 22 opens: *"the one with a typo in it"* stops being a forward reference and becomes a plant that pays off in Ch. 24's *"Wrong word for a man in a room with no door. Accommodated."* No edit was needed in Ch. 22 at all.
2. It makes the blame argument in Ch. 24 a February flashback rather than a March one, which is what the chapter's placement already implies — the divider is already there (the `---` before *"After the interview…"*), so only the date inside the sentence needed to change.

### FLAG 3 and FLAG 5 — the chapter's own span, and the reading order\n
Ch. 24 is now stamped **Days 105–108** rather than 97–104 (below). Because its frame now begins on the day the collection begins, the printed order (Ch. 23 on the sixteenth, then Ch. 24) is chronological and the "eight days earlier" dateline the audit suggested is unnecessary. Ch. 23 gains the date instead, using the stamp convention the book already uses in Ch. 28 and Ch. 31 ("Day 122 — the second of April").\n""")
doc.append("### FLAG 4, 6, 7 and the typo\n")
doc.append(table(rows(["Continuity — number slip", "Continuity — typo"])))
doc.append("""
On FLAG 7, the audit's suggestion is the one that makes the book better and I've taken it: El Búho now says **three thousand eight hundred and forty-one** people standing in a doorway, and Ch. 34's *"Eight hundred and eighty people have just become persons"* is the difference between 3,841 declared and 2,961 counted, arriving as arithmetic the reader performs rather than hears.

### Housekeeping\n
""")
doc.append(table(rows(["Housekeeping — interlude numbering", "Housekeeping — motif"])))
doc.append("""
**Interlude day stamps (audit item D1, second half): no edit.** I checked all four, and they are already in one format — Dakar `Days 18–24`, Notices `Days 78–92`, Kestrel Field `Day 89`, Interlude IV `Day 143`. Adding calendar dates to them would have meant inventing four dates for material the book has deliberately kept unstamped; the numbering fix is the fix.

**Dividers:** the manuscript uses two divider styles — 81 × `---` and 48 × `• • •` — which is invisible in the PDF's own pages but obvious in any reflow. All 81 normalised to `• • •`. This is presentation, not prose: reverse it in one find-and-replace if you want the other style. Logged here so it isn't mistaken for an edit to the text.
""")
doc.append("---\n")
doc.append("## 3. The line pass\n")
doc.append("""Grouped by rule. The marked-up DOCX shows each of these in place; this table is the index to it.\n""")
doc.append("### Rule 3 — kill the meta-book register (the assessment's rule 3)\n")
doc.append(table(rows(["Line rule 3 — meta register"])))
doc.append("""
Six of the seven fourth-wall moments are gone; the postcard's is untouched, as recommended. That leaves one, where there were seven.\n
### Rule 2 — scene before summary\n""")
doc.append(table(rows(["Line rule 2 — summary tic"])))
doc.append("""
Note **D8** is the assessment's own worked example (§6.2) applied as written — 80 words to 45, same meaning, no narrator leaning on the scale — so you can audit the rule against the case you were shown.\n
### Rules 1, 4 and 5 — mechanisms, numbers, similes\n""")
doc.append(table(rows(["Line rule 1 — mechanism", "Line rule 4 — numbers", "Line rule 5 — similes"])))
doc.append("---\n")
doc.append("## 4. Where I disagree with the audit\n")
doc.append("""1. **FLAG 2 — the eighth of March could not be kept.** Full reasoning in §2. This is the only place where the fixes depart from the audit, and it is a departure in the direction of *more* change, not less.

2. **Rule 1 — "the five-line plan is stated in Ch. 26, restated in Ch. 27, and re-explained in Ch. 30" does not hold.** I searched all three chapters for every form of it (the five lines, the four lines, the doors, the objectives, the register/printer mechanism). Ch. 27 contains no restatement of the plan at all — it is the morning of the operation, and what repetition it has is *in-scene planning* (Roux's drill, the five-fifteen start). Ch. 30's material is new: the fire return, the node, the disposition. What actually recurs are the **four doctrine lines**, stated on the board in Ch. 18, again in Ch. 26, and once more as the chapter title of Ch. 28 — and that recurrence is load-bearing, because Ch. 26 tells you why: *"a crew is not held together by hope, it is held together by a format."* I cut one genuine over-explanation (E4, and the near-verbatim repeat at F4). I did **not** cut the doctrine refrain, and I would resist cutting it.

3. **Rule 5 — the similes are voice, not fat.** The audit's number (9.8 per 1,000 in Kestrel Field) put that section at the top; measured consistently across the book it sits mid-pack (2.1), behind Ch. 6 (2.65), Ch. 4 (2.63) and Ch. 3 (2.28) — and in those chapters the similes are almost entirely **character register**: Mesa's auctioneer arithmetic, Kavanagh's horses, Garrity's aircraft. *"set him on deck like a crate of eggs"*, *"the way a man looks at a horse he is considering buying"* — these are the two best characterisations in the book arriving by simile. I cut two narrator-side ones (E1, E2) and left the rest. The rule as written would sand off the book's best asset, which is also what §8 of the assessment warned about.

4. **Rule 4 — the numbers are the book's grammar.** After FLAG 6 (where the slip was real), I made one number cut (E3). Everything else is deliberate: 411 is the Office's own signature count wearing every costume it can — desks, exceptions, entries, aircraft, the June movement, the euro bill — and "eleven" is the book's unit of bureaucratic time. Thinning these is a structural decision, not a line one, and it should be decided with the cut pass, not before it.

5. **The euro receipt (audit housekeeping D3).** The audit was right that the coda's repetition shows the machinery, and I've cut the coda restatement (B7). But I checked Ch. 34 first and left it intact: *"the total, which is on this page in eleven-point type, is four hundred and eleven euro"* is a joke the book has earned, and Kavanagh's *"I paid €411 for a receipt that says I did a thing"* is his whole character in one line. The number is only a problem when the narrator uses it a second time.\n""")
doc.append("---\n")
doc.append("## 5. Method, and how to check me\n")
doc.append(f"""The PDF's text layer gives one line per block, so paragraphing was rebuilt mechanically from line geometry: consecutive lines are joined unless the vertical gap exceeds 1.5× the line pitch (paragraph breaks are exactly twice the line pitch throughout this file). The reconstruction was validated against the D2 manuscript's own paragraphs, chapter by chapter — 73 of 78 paragraph blocks in a sampled chapter were byte-identical, and every mismatch was a scene divider, not prose.

Every edit is then applied by **exact-string match against one numbered paragraph**, with the match required to be unique; if a string had moved or read differently the build fails rather than guessing. The result:

- **41 paragraphs carry edits, 81 carry a normalised divider, 3,200 are untouched.** No paragraph was edited that is not listed in §2–§3, and no edit was made in a paragraph that is not listed.
- Word count: 110,164 → 110,033.
- Insertions are highlighted and deletions struck through in `D3_REVISED_marked.docx`; the paragraph's surrounding text is untouched in both DOCX files.
- `D3_REVISED_manuscript.md` is the same text, clean, for reading and for searching.

**What to do next, in this order:** read Ch. 23–24 in the clean file first (that's where the surgery was); then the marked file, top to bottom, rejecting freely; then the cut pass in `revision-plan.md`. When you reject an edit, the change-log row gives you the exact original string to paste back.
""")
open(os.path.join(OUT, "CHANGE-LOG.md"), "w").write("\n".join(doc) + "\n")
print("written change log")
