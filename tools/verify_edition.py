"""Verify an edition: the units model, the .docx, the .md and the .pdf must agree.

    python tools/verify_edition.py D13

Checks
  1. every body paragraph of the model appears in the docx and the md, in order,
     with the same text (whitespace and asterisk markup normalised);
  2. the docx carries no asterisk, the md carries no asterisk outside its markup,
     and the pdf carries none at all;
  3. the pdf's text contains every paragraph of the model (pdf extraction loses some
     spaces, so paragraphs are compared as letter-only streams);
  4. formatting: 1-inch margins, Times New Roman 12 body, 18pt bold+italic section
     titles, the day lines italic, the contents list complete;
  5. page count and word counts.
"""
import json, re, sys
from docx import Document

REPO = "/home/user/THE-LAST-SMUGGLERS"
stem = sys.argv[1] if len(sys.argv) > 1 else "D13"
BH = re.compile(r"^\*?CUSTOS \u2014 PUBLIC BULLETIN.*\*?$")
ITAL = re.compile(r"\*([^*]+)\*")


def letters(s):
    return re.sub(r"[^A-Za-z0-9]", "", s)


def is_sep(t):
    t = (t or "").strip()
    return t != "" and set(t) <= set("* ")


units = json.load(open(f"{REPO}/{stem}_units.json"))
body, bulletins = [], []
for u in units:
    for it in u["items"]:
        if it.get("kind") == "cut":
            continue
        t = (it.get("text") or "").strip()
        if not t or is_sep(t):
            continue
        if BH.match(t.strip("*")):
            bulletins.append(t.strip("*").strip())
            continue
        body.append(ITAL.sub(r"\1", t).replace("_", ""))
print(f"(the model holds {len(bulletins)} CUSTOS bulletin heads, checked separately)")

fail = []

# ---------------------------------------------------------------- 1. docx vs model
d = Document(f"{REPO}/THE_LAST_SMUGGLERS_{stem}.docx")
paras = [p for p in d.paragraphs]
titles = [p for p in paras if p.runs and p.runs[0].font.size and p.runs[0].font.size.pt == 18]
daylines = [p for p in paras if p.runs and p.runs[0].font.size and p.runs[0].font.size.pt == 12
            and p.runs[0].italic]
first_head = next(i for i, p in enumerate(paras)
                  if p.runs and p.runs[0].font.size and p.runs[0].font.size.pt == 18)
body_paras = []
for p in paras[first_head:]:
    r = p.runs[0] if p.runs else None
    if not r or not r.font.size:
        continue
    if r.font.size.pt != 12 or r.italic or r.bold:
        continue
    if is_sep(p.text) or p.text.strip() == "\u2022 \u2022 \u2022":
        continue
    body_paras.append(p.text.strip())
model_body = [b for b in body]
if body_paras != model_body:
    n = sum(1 for a, b in zip(body_paras, model_body) if a != b) + abs(len(body_paras) - len(model_body))
    fail.append(f"docx body paragraphs differ from the model ({n} rows)")
    for i, (a, b) in enumerate(zip(body_paras, model_body)):
        if a != b:
            fail.append(f"   first difference at body paragraph {i}:\n     docx : {a[:90]!r}\n     model: {b[:90]!r}")
            break

words = sum(len(p.split()) for p in body_paras)
sec = d.sections[0]
margins = [sec.top_margin.inches, sec.bottom_margin.inches, sec.left_margin.inches, sec.right_margin.inches]
if margins != [1.0, 1.0, 1.0, 1.0]:
    fail.append(f"margins are {margins}")
if d.styles["Normal"].font.name != "Times New Roman" or d.styles["Normal"].font.size.pt != 12:
    fail.append("Normal style is not Times New Roman 12")
heads_ok = sum(1 for p in titles if p.runs[0].bold and p.runs[0].italic)
if len(titles) != len(units) or heads_ok != len(units):
    fail.append(f"section titles: {len(titles)} found, {heads_ok} bold+italic, {len(units)} expected")
if len(daylines) != sum(1 for u in units if u.get("day")):
    fail.append(f"day lines: {len(daylines)} found, expected {sum(1 for u in units if u.get('day'))}")
stars = [p.text for p in paras if "*" in p.text]
if stars:
    fail.append(f"{len(stars)} paragraph(s) contain an asterisk, first {stars[0][:60]!r}")
docx_bulletins = [p.text.strip() for p in paras if p.runs and p.runs[0].font.size
                  and p.runs[0].font.size.pt == 11]
if docx_bulletins != bulletins:
    fail.append(f"bulletin heads differ: {len(docx_bulletins)} in the docx, {len(bulletins)} in the model")
toc = [p.text for p in paras[: len(units) + 8]]
missing = [u["display"] for u in units if u["display"] not in toc]
if missing:
    fail.append(f"contents list misses {missing}")

# ------------------------------------------------------------------ 2. md vs model
md = open(f"{REPO}/{stem}_THE_LAST_SMUGGLERS.md").read()
lines = md.split("\n")
displays = {u["display"] for u in units}
start = next(i for i, l in enumerate(lines)
             if l.startswith("## ") and l[3:].strip() in displays
             and i > next(j for j, k in enumerate(lines) if k.startswith("## Contents")))
md_body = []
for l in lines[start:]:
    s = l.strip()
    if not s or s.startswith("#") or s == "---" or s.startswith("<div") or s.startswith("___"):
        continue
    if s.startswith("_") and s.endswith("_") and len(s) < 40:
        continue
    md_body.append(ITAL.sub(r"\1", s).replace("_", ""))
if md_body != model_body:
    n = sum(1 for a, b in zip(md_body, model_body) if a != b) + abs(len(md_body) - len(model_body))
    fail.append(f"md body paragraphs differ from the model ({n} rows)")
md_star = re.findall(r"[^*_]", md)
if "*" in md.replace("* * *", ""):
    fail.append("the md contains an asterisk")

# --------------------------------------------------------------- 3. pdf vs model
from pypdf import PdfReader
r = PdfReader(f"{REPO}/THE_LAST_SMUGGLERS_{stem}.pdf")
pdf_txt = letters("\n".join((pg.extract_text() or "") for pg in r.pages))
missing_pdf = [b for b in model_body if letters(b)[:60] not in pdf_txt]
if missing_pdf:
    fail.append(f"{len(missing_pdf)} model paragraph(s) not found in the pdf, first: {missing_pdf[0][:70]!r}")
if "*" in "".join((pg.extract_text() or "") for pg in r.pages):
    fail.append("the pdf contains an asterisk")

# ------------------------------------------------------------------------ report
print(f"== {stem} ==")
print(f"  sections {len(units)} | body paragraphs {len(body_paras)} | body words {words:,}")
print(f"  docx {len(d.paragraphs)} paragraphs | day lines {len(daylines)} | titles {len(titles)}")
print(f"  pdf pages {len(r.pages)} | md {len(md.splitlines())} lines | md words {len(md.split())}")
if fail:
    print("\nFAILED:")
    for f in fail:
        print("  !", f)
    sys.exit(1)
print("\nOK — model, docx, md and pdf agree; formatting rules hold; no asterisks.")
