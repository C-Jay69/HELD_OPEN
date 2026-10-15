"""A one-page download server for the D13 deliverables.

    python tools/serve_downloads.py [port]      (default 8000, binds 0.0.0.0)

Serves a small index page listing the frozen manuscript and the submission package, with
the .docx and .pdf set to download. Nothing else in the repository is reachable — the
handler only answers for the files on the WHITELIST.
"""
import html, os, sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

WHITELIST = {
    "THE_LAST_SMUGGLERS_D13.docx": ("The frozen manuscript — Word (.docx)", "download",
                                    "application/vnd.openxmlformats-officedocument.wordprocessingml.document"),
    "THE_LAST_SMUGGLERS_D13.pdf": ("The frozen manuscript — PDF (295 pages)", "download",
                                   "application/pdf"),
    "D13_THE_LAST_SMUGGLERS.md": ("The frozen manuscript — Markdown (reads in the panel)", "view",
                                  "text/markdown; charset=utf-8"),
    "LETTER_AGENT_D13.docx": ("Covering letter to an agent (.docx)", "download",
                              "application/vnd.openxmlformats-officedocument.wordprocessingml.document"),
    "LETTER_AGENT_D13.md": ("Covering letter (.md, with the three-line version)", "view",
                            "text/markdown; charset=utf-8"),
    "SUBMISSION_PACKAGE_D13.md": ("The submission package — what goes, and what is missing", "view",
                                  "text/markdown; charset=utf-8"),
    "COLD_READ_50_PAGES_D13.md": ("The first fifty pages read cold", "view",
                                  "text/markdown; charset=utf-8"),
    "FREEZE_D13.md": ("What is frozen, with the sha256 hashes", "view", "text/markdown; charset=utf-8"),
}

PAGE = """<!doctype html>
<html><head><meta charset="utf-8"><title>THE LAST SMUGGLERS — D13</title>
<style>
 body {{ font-family: Georgia, 'Times New Roman', serif; margin: 3rem auto; max-width: 46rem;
         color: #17181a; line-height: 1.45; }}
 h1 {{ font-size: 1.6rem; margin-bottom: .1rem; }}
 p.sub {{ color: #666; margin-top: 0; }}
 table {{ border-collapse: collapse; width: 100%; margin-top: 1.2rem; }}
 td {{ padding: .55rem .4rem; border-bottom: 1px solid #ececec; vertical-align: top; }}
 td.size {{ color: #888; white-space: nowrap; text-align: right; }}
 a {{ color: #1a4f8a; }}
 .dl {{ font-weight: bold; }}
 footer {{ margin-top: 2rem; color: #888; font-size: .85rem; }}
</style></head><body>
<h1>THE LAST SMUGGLERS — frozen edition D13</h1>
<p class="sub">42 sections · 3,153 body paragraphs · 114,341 words of prose · 295 pages ·
frozen 15 October 2026. Click a file to download or open it.</p>
<table>{rows}</table>
<footer>Served from the repository. The frozen files are hashed in FREEZE_D13.md; the sha256 of this
edition's .docx is cf9faa1f… and of its .pdf is 71c8bf51…</footer>
</body></html>"""


class Handler(BaseHTTPRequestHandler):
    server_version = "TLS-D13/1.0"

    def _rows(self):
        rows = []
        for name, (label, mode, _ct) in WHITELIST.items():
            path = os.path.join(REPO, name)
            if not os.path.exists(path):
                continue
            kb = os.path.getsize(path) / 1024.0
            size = f"{kb/1024:.1f} MB" if kb > 1024 else f"{kb:.0f} KB"
            cls = ' class="dl"' if mode == "download" else ""
            rows.append(
                f'<tr><td><a{cls} href="/{html.escape(name)}">{html.escape(label)}</a><br>'
                f'<span style="color:#999;font-size:.85rem">{html.escape(name)}</span></td>'
                f'<td class="size">{size}</td></tr>')
        return "".join(rows)

    def do_GET(self):
        name = self.path.lstrip("/").split("?")[0]
        if name in ("", "index.html"):
            body = PAGE.format(rows=self._rows()).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        if name not in WHITELIST:
            self.send_error(404, "not served here")
            return
        path = os.path.join(REPO, name)
        if not os.path.exists(path):
            self.send_error(404, "not built yet")
            return
        _label, mode, ctype = WHITELIST[name]
        data = open(path, "rb").read()
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        if mode == "download":
            self.send_header("Content-Disposition", f'attachment; filename="{name}"')
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, fmt, *args):
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    srv = ThreadingHTTPServer(("0.0.0.0", port), Handler)
    print(f"serving the D13 downloads on http://0.0.0.0:{port}/  (Ctrl-C to stop)")
    srv.serve_forever()


if __name__ == "__main__":
    main()
