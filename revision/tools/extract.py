# -*- coding: utf-8 -*-
"""Rebuild D3 as paragraph-accurate text.

Step 1 of 4 in the revision chain, and the only one that touches the PDF:

    extract.py  ->  d3_paras.json
    edits.py + build.py  ->  revised manuscript (.md / .docx / marked .docx)
    log.py      ->  CHANGE-LOG.md

Why this exists: the PDF's text layer emits one line per layout block, so paragraph
boundaries cannot be taken from blocks. Horizontal rules are not usable either
(dialogue lines are short). What is reliable is the leading: consecutive lines sit
9.75pt apart inside a paragraph and 19.5pt apart across a paragraph break, in this
file, on every page. So: sort by y, start a new paragraph whenever the gap from the
previous line's baseline exceeds 1.5x the page's median line pitch, then repair the
paragraphs that a page break split (a page's first line is always a candidate break).

Requires: pymupdf.  Usage: python extract.py <D3.pdf> <out.json>
"""
import json
import sys

import pymupdf


def page_lines(page):
    lines = []
    for block in page.get_text("dict")["blocks"]:
        if block["type"] != 0:
            continue
        for line in block["lines"]:
            text = "".join(span["text"] for span in line["spans"]).rstrip()
            if text.strip():
                lines.append((line["bbox"][1], line["bbox"][3], text.strip()))
    lines.sort()
    return lines


def extract(pdf_path):
    doc = pymupdf.open(pdf_path)
    paras = []
    for page in doc:
        lines = page_lines(page)
        previous_bottom = None
        for top, bottom, text in lines:
            new_para = previous_bottom is None or (top - previous_bottom) >= 15
            if new_para or not paras:
                paras.append(text)
            else:
                paras[-1] = paras[-1] + " " + text
            previous_bottom = bottom
    # Repair paragraphs broken by a page turn: the next page's first line becomes its
    # own paragraph, and is only a continuation if the text runs on.
    merged = []
    for text in paras:
        if merged and not merged[-1].rstrip().endswith((".", "!", "?", '"', "\u201d", "\u2019", ")")) \
                and text[:1].islower():
            merged[-1] = merged[-1] + " " + text
        else:
            merged.append(text)
    return [" ".join(t.split()) for t in merged]


if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    paras = extract(src)
    json.dump(paras, open(dst, "w"))
    words = sum(len(p.split()) for p in paras)
    print(f"{len(paras)} paragraphs, {words} words -> {dst}")
