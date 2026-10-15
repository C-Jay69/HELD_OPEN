"""The frozen text = D12 + the one word found after the list was closed.

Row 45 of `READING_NOTES_D10.md` §3.  Interlude IV:

    It is noted that an anomalous construction has been reproduced at the close of each
    notice cycle for three thousand nine hundred and forty-three nights. ... It was
    entered in the twelfth year, in the pilot period, by a person ...

3,943 nights is ten years and nine months, and Elena says in Ch 33 that she put the
construction into the machine "eleven years ago, in Rotterdam ... in the pilot period".
The twelfth year is where the programme is *now* (Ch 17: "and then, in the eleventh year,
accommodation").  So the entry belongs in the first year.  One word.

Nothing else changes: this is the manuscript as approved in D12.
"""
import json, sys

REPO = "/home/user/THE-LAST-SMUGGLERS"
units = json.load(open(f"{REPO}/D12_units.json"))
log = {"edits": [], "notes": []}

FIND = "It was entered in the twelfth year, in the pilot period, by a person"
REPL = "It was entered in the first year, in the pilot period, by a person"
hit = 0
for ui, sec in enumerate(units, 1):
    for pi, it in enumerate(sec["items"], 1):
        t = it.get("text") or ""
        if FIND in t:
            hit += 1
            it["text"] = t.replace(FIND, REPL)
            log["edits"].append({"at": f"{ui}.{pi}", "old": FIND, "new": REPL,
                                 "why": "3,943 nights is ten years and nine months, and the pilot "
                                        "period is where the construction entered the machine; the "
                                        "twelfth year is the present (Ch 17)"})
if hit != 1:
    print(f"!! expected exactly one site, found {hit}")
    sys.exit(1)

log["notes"].append("This is the freeze edition: D12 as approved, plus this one word.")
json.dump(units, open(f"{REPO}/D13_units.json", "w"), ensure_ascii=False, indent=1)
json.dump(log, open(f"{REPO}/D13_changelog.json", "w"), ensure_ascii=False, indent=1)
words = sum(len((it.get("text") or "").split()) for u in units for it in u["items"]
            if it.get("kind") != "cut")
def is_sep(t):
    t = (t or "").strip()
    return t != "" and set(t) <= set("* ")


paras = sum(1 for u in units for it in u["items"]
            if it.get("kind") != "cut" and (it.get("text") or "").strip()
            and not is_sep(it.get("text")))
print(f"frozen text written: {len(units)} sections | {paras} body paragraphs | {words:,} body words")
