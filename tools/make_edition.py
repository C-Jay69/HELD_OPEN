"""Readable twins of the manuscript, from any units json.

    python tools/make_edition.py <units.json> <stem>        e.g. D13

Writes, next to the units file:
    <stem>_units.json is the input;  outputs are
    THE_LAST_SMUGGLERS_<stem>.docx / .pdf and <stem>_THE_LAST_SMUGGLERS.md

Formatting (the author's spec, unchanged since D6):
    body            Times 12, no asterisks anywhere
    section titles  Times 18, bold + italic
    day lines       Times 12 italic
    margins         1 inch all round
    section breaks  centred  • • •
    italics         real italics (never asterisks)
    contents        lists every section
"""
import json, re, sys, os

REPO = "/home/user/THE-LAST-SMUGGLERS"
ITAL = re.compile(r"\*([^*]+)\*")
BULLETIN_HEAD = re.compile(r"^\*?CUSTOS \u2014 PUBLIC BULLETIN.*\*?$")
PAGE = "page-break"


def load(src):
    return json.load(open(src))


def is_sep(text):
    s = (text or "").strip()
    return s != "" and set(s) <= set("* ")


def inline_runs(text):
    """Split '*italic*' markup into (text, italic) pairs.  Asterisks never survive."""
    out, pos = [], 0
    for m in ITAL.finditer(text or ""):
        if m.start() > pos:
            out.append((text[pos:m.start()], False))
        out.append((m.group(1), True))
        pos = m.end()
    if pos < len(text or ""):
        out.append((text[pos:], False))
    return [(t, i) for t, i in out if t != ""]


# --------------------------------------------------------------------------- docx
def make_docx(units, path):
    from docx import Document
    from docx.shared import Pt, Inches
    from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK

    doc = Document()
    sec = doc.sections[0]
    for a in ("top_margin", "bottom_margin", "left_margin", "right_margin"):
        setattr(sec, a, Inches(1.0))
    st = doc.styles["Normal"]
    st.font.name = "Times New Roman"
    st.font.size = Pt(12)
    st.paragraph_format.space_after = Pt(10)
    st.paragraph_format.line_spacing = 1.35
    st.paragraph_format.first_line_indent = Inches(0.0)

    def para(align=None, after=None):
        p = doc.add_paragraph()
        if align is not None:
            p.alignment = align
        if after is not None:
            p.paragraph_format.space_after = Pt(after)
        return p

    def run(p, text, size=12, bold=False, italic=False):
        r = p.add_run(text)
        r.font.name = "Times New Roman"
        r.font.size = Pt(size)
        r.bold = bold
        r.italic = italic
        return r

    def page_break():
        r = doc.add_paragraph().add_run()
        r.add_break(WD_BREAK.PAGE)

    page = WD_ALIGN_PARAGRAPH
    # title page
    p = para(page.CENTER, after=6); run(p, "THE LAST SMUGGLERS", 26, bold=True)
    p = para(page.CENTER, after=24); run(p, "a novel", 13, italic=True)
    p = para(page.CENTER); run(p, "SIMON J CLEARY", 14, bold=True)
    page_break()
    p = para(page.CENTER, after=14); run(p, "Contents", 14)
    for u in units:
        p = para(after=2); run(p, u["display"], 12)
    page_break()

    body_words = body_paras = 0
    for u in units:
        p = para(after=6); run(p, u["display"], 18, bold=True, italic=True)
        if u.get("day"):
            p = para(after=14); run(p, u["day"], 12, italic=True)
        after_bulletin = False
        for it in u["items"]:
            if it.get("kind") == "cut":
                continue
            t = (it.get("text") or "").strip()
            if not t:
                continue
            if is_sep(t):
                p = para(page.CENTER, after=12); run(p, "\u2022 \u2022 \u2022", 12)
                continue
            if BULLETIN_HEAD.match(t.strip("*")):
                p = para(page.CENTER, after=6); run(p, t.strip("*").strip(), 11, italic=True)
                after_bulletin = True
                continue
            p = para(after=8 if after_bulletin else None)
            after_bulletin = False
            for txt, ital in inline_runs(t):
                run(p, txt, 12, italic=ital)
                body_words += len(txt.split())
            body_paras += 1
        page_break()
    doc.save(path)
    return body_paras, body_words


# ---------------------------------------------------------------------- markdown
def make_md(units, path):
    L = ["# THE LAST SMUGGLERS", "", "_a novel_", "", "__Simon J Cleary__", "", "---", "",
         "## Contents", ""]
    for u in units:
        L.append(u["display"] + "  ")
    L += ["", "---", ""]
    words = 0
    for u in units:
        L += [f"## {u['display']}", ""]
        if u.get("day"):
            L += [f"_{u['day']}_", ""]
        for it in u["items"]:
            if it.get("kind") == "cut":
                continue
            t = (it.get("text") or "").strip()
            if not t:
                continue
            if is_sep(t):
                L += ['<div align="center">\u2022 \u2022 \u2022</div>', ""]
                continue
            if BULLETIN_HEAD.match(t.strip("*")):
                L += [f"___{t.strip('*').strip()}___", ""]
                continue
            L += [ITAL.sub(lambda m: "_" + m.group(1).strip() + "_", t), ""]
            words += len(ITAL.sub(r"\1", t).split())
        L += ["---", ""]
    md = "\n".join(L).rstrip() + "\n"
    open(path, "w").write(md)
    return words


# --------------------------------------------------------------------------- pdf
def make_pdf(units, path):
    from reportlab.lib.pagesizes import LETTER
    from reportlab.lib.units import inch
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
    from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                    Spacer, PageBreak, KeepTogether)

    F, FB, FI, FBI = "Times-Roman", "Times-Bold", "Times-Italic", "Times-BoldItalic"
    body = ParagraphStyle("body", fontName=F, fontSize=12, leading=17,
                          alignment=TA_JUSTIFY, spaceAfter=8)
    head = ParagraphStyle("head", fontName=FBI, fontSize=18, leading=22, spaceAfter=10,
                          keepWithNext=1)
    day = ParagraphStyle("day", fontName=FI, fontSize=12, leading=17, spaceAfter=10,
                         keepWithNext=1)
    sep = ParagraphStyle("sep", fontName=F, fontSize=12, leading=17, alignment=TA_CENTER,
                         spaceBefore=6, spaceAfter=12)
    bullet = ParagraphStyle("bullet", fontName=FI, fontSize=11, leading=15,
                            alignment=TA_CENTER, spaceBefore=4, spaceAfter=8)
    title = ParagraphStyle("title", fontName=FB, fontSize=28, leading=32, alignment=TA_CENTER)
    novel = ParagraphStyle("novel", fontName=FI, fontSize=13, leading=16, alignment=TA_CENTER)
    author = ParagraphStyle("author", fontName=FB, fontSize=14, leading=18, alignment=TA_CENTER)
    cont = ParagraphStyle("cont", fontName=F, fontSize=12, leading=17, spaceAfter=2)
    conthead = ParagraphStyle("conthead", fontName=F, fontSize=14, leading=18,
                              alignment=TA_CENTER, spaceAfter=14)

    def esc(t):
        return (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))

    def rich(t):
        return ITAL.sub(lambda m: f"<i>{esc(m.group(1))}</i>", esc(t))

    def footer(canv, doc):
        canv.saveState()
        canv.setFont(F, 10)
        canv.drawCentredString(LETTER[0] / 2.0, 0.65 * inch, str(doc.page))
        canv.restoreState()

    doc = BaseDocTemplate(path, pagesize=LETTER, leftMargin=inch, rightMargin=inch,
                          topMargin=inch, bottomMargin=inch,
                          title="THE LAST SMUGGLERS", author="Simon J Cleary")
    frame = Frame(inch, inch, LETTER[0] - 2 * inch, LETTER[1] - 2 * inch, id="f")
    doc.addPageTemplates([PageTemplate(id="all", frames=[frame], onPage=footer)])

    S = [Paragraph("THE LAST SMUGGLERS", title), Paragraph("a novel", novel),
         Paragraph("SIMON J CLEARY", author), Spacer(1, 40), PageBreak(),
         Paragraph("Contents", conthead)]
    for u in units:
        S.append(Paragraph(esc(u["display"]), cont))
    S.append(PageBreak())
    for u in units:
        block = [Paragraph(esc(u["display"]), head)]
        if u.get("day"):
            block.append(Paragraph(esc(u["day"]), day))
        S.append(KeepTogether(block))
        for it in u["items"]:
            if it.get("kind") == "cut":
                continue
            t = (it.get("text") or "").strip()
            if not t:
                continue
            if is_sep(t):
                S.append(Paragraph("\u2022 \u2022 \u2022", sep))
                continue
            if BULLETIN_HEAD.match(t.strip("*")):
                S.append(Paragraph(esc(t.strip("*").strip()), bullet))
                continue
            S.append(Paragraph(rich(t), body))
        S.append(PageBreak())
    doc.build(S)
    return len(S)


def main():
    src, stem = sys.argv[1], sys.argv[2]
    units = load(src)
    bp, words = make_docx(units, f"{REPO}/THE_LAST_SMUGGLERS_{stem}.docx")
    mdw = make_md(units, f"{REPO}/{stem}_THE_LAST_SMUGGLERS.md")
    make_pdf(units, f"{REPO}/THE_LAST_SMUGGLERS_{stem}.pdf")
    print(f"{stem}: docx {bp} paragraphs / {words:,} words | md {mdw:,} words")


if __name__ == "__main__":
    main()
