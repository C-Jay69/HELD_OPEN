# Revision chain — how the revised D3 was produced

Everything in `revision/` is generated. Nothing in it was typed by hand, so any edit can be
re-run, re-checked, or reversed.

```
extract.py   D3.pdf              -> d3_paras.json      (paragraph-accurate text; the only step that reads the PDF)
edits.py     edit list           -> 41 anchored edits, each with a reason
build.py     d3_paras.json+edits -> D3_REVISED_manuscript.md / .docx / _marked.docx
log.py       applied.json        -> CHANGE-LOG.md       (the table of every change)
```

Run order, from this directory (needs `pymupdf` and `python-docx`):

```bash
python extract.py ../../editorial/source/D3_THE_LAST_SMUGGLERS.pdf d3_paras.json
python build.py       # writes the three manuscript files into revision/
python log.py         # rewrites revision/CHANGE-LOG.md
```

`edits.py` is the interesting file: each entry is `(id, category, paragraph index, old, new, why)`.
`build.py` fails loudly if an `old` string is not found exactly once in its paragraph, so the
edit list cannot drift silently out of step with the text.

`d3_paras.json` and `applied.json` are build products and are not tracked.
