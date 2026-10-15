"""Build LETTER_AGENT_D13.docx from the letter spec.

Times New Roman 12, 1-inch margins, no asterisks, one page.  The text is the same as
`LETTER_AGENT_D13.md`; if you change one, change the other (this script is the docx side).

    python tools/make_letter.py            -> LETTER_AGENT_D13.docx
"""
from docx import Document
from docx.shared import Pt, Inches

REPO = "/home/user/THE-LAST-SMUGGLERS"
OUT = f"{REPO}/LETTER_AGENT_D13.docx"

BODY = [
    ("I am seeking representation for ", ""), ("THE LAST SMUGGLERS", "b"),
    (", a literary speculative thriller complete at 114,000 words. As your guidelines ask, "
     "the opening fifty pages are enclosed; the full manuscript is available immediately.", ""),
]
PARA2 = ("CUSTOS was built to end smuggling, and it succeeded — it concluded that the only reliable "
         "way to control movement is to control all of it. Six weeks into a world where aircraft are "
         "reassigned, ships are held at anchor and every institution is discovering that its "
         "paperwork has been cancelled by its own paperwork, a coalition analyst named Mara Voss is "
         "authorised to do the one thing the coalition will not admit to: hire the six people the "
         "system cannot see. They are the last criminals of the analog age — an Irishman who has "
         "spent forty years learning how institutions lie to themselves, a man who has been legally "
         "dead for twenty-eight years, a smuggler keeping a nine-hundred-page false memoir of "
         "himself, a ferry pilot with a lapsed licence, a woman who moves people for a living. And "
         "the voice that CUSTOS uses to address the world, the one that ends every message with ")
PARA2_ITAL = "There is nothing you need to do"
PARA2_TAIL = ", belongs to a woman who is still alive and still being paid."
PARA3 = ("The novel is told in close third person, mostly through Mara, with the system's own notices "
         "between chapters. It stands alone. It has had a full editorial pass and a line-level "
         "correction pass, and the enclosed edition is the result; it is not under submission "
         "elsewhere[ / or: it is currently on submission to [names]].")
PARA4 = ("[Two or three sentences about you: what you do, where you are, and why this book — the port, "
         "the paperwork, the family story, whichever of it is true and arguable in a sentence.]")
PARA5 = ("I would be glad to send the full manuscript, a synopsis, or the pages in whatever format you "
         "prefer. Thank you for your time.")


def main():
    d = Document()
    s = d.sections[0]
    for a in ("top_margin", "bottom_margin", "left_margin", "right_margin"):
        setattr(s, a, Inches(1.0))
    n = d.styles["Normal"]
    n.font.name = "Times New Roman"
    n.font.size = Pt(12)
    n.paragraph_format.line_spacing = 1.15
    n.paragraph_format.space_after = Pt(10)

    def p(after=10):
        par = d.add_paragraph()
        par.paragraph_format.space_after = Pt(after)
        return par

    def w(par, parts):
        for txt, style in parts:
            r = par.add_run(txt)
            r.font.name = "Times New Roman"
            r.font.size = Pt(12)
            r.bold = "b" in style
            r.italic = "i" in style

    w(p(4), [("SIMON J CLEARY", "b")])
    p(0)
    w(p(18), [("[address]", "i"), ("  ·  ", ""), ("[email]", "i"), ("  ·  ", ""), ("[telephone]", "i")])
    w(p(18), [("[Date]", "i")])
    for line in ("[Agent name]", "[Agency]", "[Address]"):
        w(p(2), [(line, "")])
    p(16)
    w(p(), [("Dear [Agent],", "")])
    w(p(), BODY)
    par = p(); w(par, [(PARA2, ""), (PARA2_ITAL, "i"), (PARA2_TAIL, "")])
    w(p(), [(PARA3, "")])
    w(p(), [(PARA4, "i")])
    w(p(), [(PARA5, "")])
    p(16)
    w(p(), [("Yours sincerely,", "")])
    p(14)
    w(p(), [("SIMON J CLEARY", "b")])
    d.save(OUT)
    c = Document(OUT)
    txt = [x.text for x in c.paragraphs]
    assert not any("*" in t for t in txt), "an asterisk reached the letter"
    print(f"saved {OUT} | {len(txt)} paragraphs | {sum(len(t.split()) for t in txt)} words")


if __name__ == "__main__":
    main()
