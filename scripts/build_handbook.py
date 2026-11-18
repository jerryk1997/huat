#!/usr/bin/env python3
"""Build handbook/huat-handbook.html from the terse working docs (ADR 0007).

Stdlib only. Usage:
    python3 scripts/build_handbook.py              # write handbook/huat-handbook.html
    python3 scripts/build_handbook.py --fragment F # also write a body-only copy (for Artifact publish)
"""
import datetime
import glob
import html
import os
import posixpath
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "handbook", "huat-handbook.html")

# (group, [(repo-relative path, nav label)])
def sections():
    adrs = sorted(glob.glob(os.path.join(ROOT, "docs/decisions/[0-9]*.md")))
    journal = sorted(glob.glob(os.path.join(ROOT, "docs/journal/[0-9]*.md")), reverse=True)
    rel = lambda p: os.path.relpath(p, ROOT).replace(os.sep, "/")
    return [
        ("Now", [("STATUS.md", "Status")]),
        ("Product", [
            ("docs/product/overview.md", "Overview"),
            ("docs/product/user-stories.md", "User stories"),
            ("docs/product/glossary.md", "Glossary"),
        ]),
        ("Reference", [("docs/reference/cpf-rules.md", "CPF rules & figures")]),
        ("Design", [
            ("docs/design/design-system.md", "Design system"),
            ("docs/design/prototype-notes.md", "Prototypes"),
        ]),
        ("Architecture", [
            ("docs/architecture/stack.md", "Stack"),
            ("docs/architecture/data-model.md", "Data model"),
        ]),
        ("Decisions", [("docs/decisions/README.md", "Index")] +
            [(rel(p), os.path.basename(p)[:4]) for p in adrs]),
        ("Journal", [(rel(p), os.path.basename(p)[:10]) for p in journal]),
        ("Process", [("START_HERE.md", "Working in this repo")]),
    ]


def slug(s):
    s = re.sub(r"<[^>]+>", "", s).lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-") or "s"


def doc_id(path):
    return "doc-" + slug(path.replace(".md", "").replace("docs/", ""))


# ---------- markdown subset -> html ----------

CHIP_WARN = r"\b(UNVERIFIED|PROPOSED|NOT WRITTEN|NOT STARTED|INCOMPLETE|MISSING)\b"


def inline(text, src, idmap):
    codes = []

    def stash(m):
        codes.append("<code>" + html.escape(m.group(1)) + "</code>")
        return "\x00%d\x00" % (len(codes) - 1)

    text = re.sub(r"`([^`]+)`", stash, text)
    out = []
    for p in [text]:
        p = html.escape(p, quote=False)

        def link(m):
            label, href = m.group(1), m.group(2)
            return '<a href="%s">%s</a>' % (html.escape(resolve(href, src, idmap)), label)

        p = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, p)
        p = re.sub(r"(?<![\w\"/])(https?://[^\s<)]+)", r'<a href="\1">\1</a>', p)
        p = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", p)
        p = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", p)
        p = re.sub(CHIP_WARN, r'<span class="chip warn">\1</span>', p)
        p = p.replace("❌", '<span class="chip no">no</span>')
        out.append(p)
    return re.sub(r"\x00(\d+)\x00", lambda m: codes[int(m.group(1))], "".join(out))


def resolve(href, src, idmap):
    if re.match(r"^[a-z]+:", href) or href.startswith("#"):
        return href
    path, _, frag = href.partition("#")
    target = posixpath.normpath(posixpath.join(posixpath.dirname(src), path))
    if target in idmap:
        return "#" + idmap[target]
    if target.rstrip("/") + "/README.md" in idmap:
        return "#" + idmap[target.rstrip("/") + "/README.md"]
    return "../" + target + (("#" + frag) if frag else "")


def render(md, src, idmap, sid):
    lines = md.split("\n")
    out, i = [], 0
    toc = []
    title = None
    para = []

    def flush():
        if para:
            out.append("<p>" + inline(" ".join(para), src, idmap) + "</p>")
            para.clear()

    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if s.startswith("```"):
            flush()
            lang = s[3:].strip()
            buf = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            out.append('<pre class="code" data-lang="%s"><code>%s</code></pre>'
                       % (html.escape(lang), html.escape("\n".join(buf))))
            i += 1
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", s)
        if m:
            flush()
            level, text = len(m.group(1)), m.group(2)
            if level == 1 and title is None:
                title = text
            else:
                hid = sid + "--" + slug(text)
                tag = "h%d" % min(level + 1, 5)
                out.append('<%s id="%s">%s</%s>' % (tag, hid, inline(text, src, idmap), tag))
                if level == 2:
                    toc.append((hid, re.sub(r"<[^>]+>", "", inline(text, src, idmap))))
            i += 1
            continue
        if s.startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
            flush()
            cells = lambda r: [c.strip() for c in r.strip().strip("|").split("|")]
            head = cells(s)
            i += 2
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(cells(lines[i]))
                i += 1
            t = ['<div class="table"><table><thead><tr>']
            t += ["<th>%s</th>" % inline(c, src, idmap) for c in head]
            t.append("</tr></thead><tbody>")
            for r in rows:
                t.append("<tr>")
                for j, c in enumerate(r):
                    cell = inline(c, src, idmap)
                    if c in ("Accepted",):
                        cell = '<span class="chip ok">Accepted</span>'
                    t.append('<td%s>%s</td>' % (' class="id"' if j == 0 and re.match(r"^[A-Z]{2,3}-\d+$", c) else "", cell))
                t.append("</tr>")
            t.append("</tbody></table></div>")
            out.append("".join(t))
            continue
        if re.match(r"^\s*([-*]|\d+\.)\s+", line):
            flush()
            i = render_list(lines, i, out, src, idmap)
            continue
        if s.startswith(">"):
            flush()
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip()[1:].strip())
                i += 1
            out.append("<blockquote>" + inline(" ".join(buf), src, idmap) + "</blockquote>")
            continue
        if s in ("---", "***"):
            flush()
            out.append("<hr>")
            i += 1
            continue
        if not s:
            flush()
            i += 1
            continue
        para.append(s)
        i += 1
    flush()
    return title, "\n".join(out), toc


def render_list(lines, i, out, src, idmap):
    base = len(lines[i]) - len(lines[i].lstrip())
    ordered = bool(re.match(r"^\s*\d+\.", lines[i]))
    out.append("<ol>" if ordered else "<ul>")
    item = None
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            # list continues only if next non-blank is an item at this level
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and re.match(r"^\s*([-*]|\d+\.)\s+", lines[j]) and \
                    len(lines[j]) - len(lines[j].lstrip()) >= base:
                i = j
                continue
            break
        indent = len(line) - len(line.lstrip())
        m = re.match(r"^\s*([-*]|\d+\.)\s+(.*)$", line)
        if m and indent == base:
            if item is not None:
                out.append("<li>" + inline(" ".join(item), src, idmap))
                out.append("</li>")
            item = [m.group(2)]
            i += 1
        elif m and indent > base:
            out.append("<li>" + inline(" ".join(item), src, idmap))
            item = None
            i = render_list(lines, i, out, src, idmap)
            out.append("</li>")
        elif indent > base and item is not None:
            item.append(line.strip())
            i += 1
        else:
            break
    if item is not None:
        out.append("<li>" + inline(" ".join(item), src, idmap) + "</li>")
    out.append("</ol>" if ordered else "</ul>")
    return i


# ---------- page ----------

STYLE = r"""
/* Layout: fixed left index rail + one reading column; rail collapses to a top <details> on phones. */
:root {
  --paper: #f6f7f4; --panel: #ecefe9; --ink: #1d2421; --muted: #5d6862; --rule: #d3d9d3;
  --red: #b3261e; --red-soft: #f7e3df; --jade: #23674f; --jade-soft: #dcefe6; --amber: #8a5a00; --amber-soft: #f6ead0;
  --code: #e7ebe5;
  --display: "Bricolage Grotesque", "Avenir Next", system-ui, sans-serif;
  --body: "IBM Plex Sans", "Segoe UI", system-ui, sans-serif;
  --mono: "IBM Plex Mono", ui-monospace, Menlo, monospace;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --paper: #141917; --panel: #1b211e; --ink: #e5ebe7; --muted: #9aa69f; --rule: #2e3833;
  --red: #ff8a7a; --red-soft: #3a1f1b; --jade: #7fd1b0; --jade-soft: #173328; --amber: #f2c063; --amber-soft: #3a2e14;
  --code: #222a26; color-scheme: dark; } }
:root[data-theme="dark"] {
  --paper: #141917; --panel: #1b211e; --ink: #e5ebe7; --muted: #9aa69f; --rule: #2e3833;
  --red: #ff8a7a; --red-soft: #3a1f1b; --jade: #7fd1b0; --jade-soft: #173328; --amber: #f2c063; --amber-soft: #3a2e14;
  --code: #222a26; color-scheme: dark; }
* { box-sizing: border-box; }
body { background: var(--paper); color: var(--ink); font: 15px/1.6 var(--body); margin: 0; }
a { color: var(--jade); text-underline-offset: 2px; }
a:focus-visible, summary:focus-visible { outline: 2px solid var(--red); outline-offset: 2px; }
.wrap > div { margin-left: 250px; min-width: 0; }
nav.rail { position: fixed; top: env(safe-area-inset-top, 0px); left: 0; bottom: 0; width: 250px; overflow-y: auto;
  background: var(--panel); border-right: 1px solid var(--rule); padding: 24px 18px 40px max(18px, env(safe-area-inset-left, 0px)); }
.brand { display: flex; align-items: baseline; gap: 10px; margin-bottom: 22px; }
.brand .han { font: 700 30px/1 var(--display); color: var(--red); }
.brand .name { font: 700 20px/1 var(--display); letter-spacing: -0.01em; }
.brand .sub { display: block; font: 11px/1.3 var(--mono); color: var(--muted); margin-top: 4px; letter-spacing: 0.04em; text-transform: uppercase; }
nav.rail h4 { font: 600 11px/1 var(--mono); letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); margin: 18px 0 6px; }
nav.rail ul { list-style: none; margin: 0; padding: 0; display: grid; gap: 1px; }
nav.rail a { display: block; padding: 4px 8px; border-radius: 4px; color: var(--ink); text-decoration: none; font-size: 14px; }
nav.rail a:hover { background: var(--paper); }
nav.rail a.mono { font-family: var(--mono); font-size: 13px; }
main { padding-block: 40px 96px; padding-left: max(40px, env(safe-area-inset-left, 0px)); padding-right: max(24px, env(safe-area-inset-right, 0px)); min-width: 0; }
.col { max-width: 860px; }
header.top { border-bottom: 2px solid var(--ink); padding-bottom: 20px; margin-bottom: 8px; }
header.top h1 { font: 800 clamp(34px, 6vw, 54px)/1 var(--display); letter-spacing: -0.03em; margin: 0 0 10px; text-wrap: balance; }
header.top h1 span { color: var(--red); }
header.top p { margin: 0; color: var(--muted); max-width: 62ch; }
.meta { display: flex; flex-wrap: wrap; gap: 8px 18px; margin-top: 14px; font: 12px/1.4 var(--mono); color: var(--muted); }
section.doc { padding-top: 36px; border-top: 1px solid var(--rule); margin-top: 36px; scroll-margin-top: 12px; }
section.doc:first-of-type { border-top: 0; margin-top: 0; }
.eyebrow { font: 600 11px/1 var(--mono); letter-spacing: 0.08em; text-transform: uppercase; color: var(--red); margin-bottom: 8px; }
section.doc > h2.title { font: 700 28px/1.15 var(--display); letter-spacing: -0.015em; margin: 0 0 6px; text-wrap: balance; }
.src { font: 12px var(--mono); color: var(--muted); margin-bottom: 18px; }
.mini-toc { display: flex; flex-wrap: wrap; gap: 6px; margin: 0 0 18px; padding: 0; list-style: none; }
.mini-toc a { font-size: 12.5px; padding: 2px 9px; border: 1px solid var(--rule); border-radius: 99px; text-decoration: none; color: var(--muted); }
.mini-toc a:hover { color: var(--ink); border-color: var(--muted); }
h3 { font: 650 19px/1.3 var(--display); margin: 28px 0 8px; scroll-margin-top: 12px; text-wrap: balance; }
h4, h5 { font: 600 15px/1.3 var(--body); margin: 20px 0 6px; }
p, ul, ol, blockquote { max-width: 72ch; }
ul, ol { padding-left: 22px; margin: 8px 0 14px; }
li { margin: 3px 0; }
li > ul, li > ol { margin: 4px 0; }
code { font: 0.86em var(--mono); background: var(--code); padding: 1px 5px; border-radius: 3px; }
pre.code { background: var(--code); padding: 14px 16px; border-radius: 6px; overflow-x: auto; font: 13px/1.5 var(--mono); }
pre.code code { background: none; padding: 0; font-size: inherit; }
blockquote { margin: 12px 0; padding: 8px 14px; border-left: 3px solid var(--red); background: var(--red-soft); }
.table { overflow-x: auto; margin: 10px 0 18px; border: 1px solid var(--rule); border-radius: 6px; }
table { border-collapse: collapse; width: 100%; font-size: 14px; font-variant-numeric: tabular-nums; }
th { text-align: left; font: 600 11.5px/1.3 var(--mono); letter-spacing: 0.05em; text-transform: uppercase; color: var(--muted);
  background: var(--panel); padding: 9px 12px; border-bottom: 1px solid var(--rule); }
td { padding: 8px 12px; border-top: 1px solid var(--rule); vertical-align: top; }
tbody tr:first-child td { border-top: 0; }
td.id { font: 600 12.5px var(--mono); white-space: nowrap; color: var(--red); }
.chip { display: inline-block; font: 600 10.5px/1.6 var(--mono); letter-spacing: 0.05em; padding: 0 7px; border-radius: 99px; vertical-align: 1px; white-space: nowrap; }
.chip.warn { background: var(--amber-soft); color: var(--amber); }
.chip.ok { background: var(--jade-soft); color: var(--jade); }
.chip.no { background: var(--red-soft); color: var(--red); text-transform: uppercase; }
details.mnav { display: none; }
@media (max-width: 860px) {
  .wrap > div { margin-left: 0; }
  nav.rail { display: none; }
  details.mnav { display: block; background: var(--panel); border-bottom: 1px solid var(--rule);
    padding-block: 12px; padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }
  details.mnav summary { font: 600 13px var(--mono); cursor: pointer; }
  details.mnav nav { columns: 2; column-gap: 16px; font-size: 14px; padding-top: 8px; }
  details.mnav h4 { font: 600 11px var(--mono); text-transform: uppercase; color: var(--muted); margin: 10px 0 4px; break-after: avoid; }
  details.mnav a { display: block; padding: 2px 0; color: var(--ink); text-decoration: none; }
  main { padding-block: 24px 64px; padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }
}
@media (prefers-reduced-motion: no-preference) { html { scroll-behavior: smooth; } }
"""

FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@600;700;800'
         '&family=IBM+Plex+Mono:wght@400;600&family=IBM+Plex+Sans:wght@400;600&display=swap">')


def build():
    groups = sections()
    idmap = {p: doc_id(p) for _, items in groups for p, _ in items}
    # map other docs not shown (journal README) to the journal group
    idmap.setdefault("docs/journal/README.md", idmap[groups[6][1][0][0]] if groups[6][1] else "")
    nav, body = [], []
    for group, items in groups:
        nav.append("<h4>%s</h4><ul>" % group)
        for path, label in items:
            sid = idmap[path]
            with open(os.path.join(ROOT, path), encoding="utf-8") as f:
                title, content, toc = render(f.read(), path, idmap, sid)
            mono = ' class="mono"' if group in ("Decisions", "Journal") and label != "Index" else ""
            nav.append('<li><a href="#%s"%s>%s</a></li>' % (sid, mono, html.escape(label)))
            mini = ""
            if len(toc) >= 3:
                mini = '<ul class="mini-toc">' + "".join(
                    '<li><a href="#%s">%s</a></li>' % (h, t) for h, t in toc) + "</ul>"
            body.append(
                '<section class="doc" id="%s"><div class="eyebrow">%s</div>'
                '<h2 class="title">%s</h2><div class="src">%s</div>%s%s</section>'
                % (sid, group, inline(title or label, path, idmap), html.escape(path), mini, content))
        nav.append("</ul>")
    nav_html = "".join(nav)
    today = datetime.date.today().isoformat()
    content = """<title>Huat Handbook</title>
<meta name="claude:viewport-fit-sides" content="cover">
%s
<style>%s</style>
<div class="wrap">
<nav class="rail" aria-label="Contents">
  <div class="brand"><span class="han">發</span><div><span class="name">Huat</span><span class="sub">Project handbook</span></div></div>
  %s
</nav>
<div>
<details class="mnav"><summary>發 Huat handbook · contents</summary><nav aria-label="Contents">%s</nav></details>
<main><div class="col">
<header class="top">
  <h1>Huat <span>handbook</span></h1>
  <p>Personal finance for Singapore: spending, budgets, savings goals, CPF projection and insurance in one picture.
  Everything decided, proposed and still open about the product.</p>
  <div class="meta"><span>Generated %s</span><span>Source: docs/ · STATUS.md · START_HERE.md</span><span>Do not edit; run scripts/build_handbook.py</span></div>
</header>
%s
</div></main>
</div>
</div>""" % (FONTS, STYLE, nav_html, nav_html, today, "\n".join(body))
    return content


def main():
    frag = build()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    head, _, body = frag.partition('<div class="wrap">')
    full = ('<!doctype html>\n<html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            '<!-- GENERATED by scripts/build_handbook.py from the working docs. Do not edit or read for lookup. -->\n'
            '%s</head><body>\n<div class="wrap">%s\n</body></html>\n' % (head, body))
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(full)
    print("wrote", os.path.relpath(OUT, ROOT), "(%d KB)" % (len(full) // 1024))
    if "--fragment" in sys.argv:
        dest = sys.argv[sys.argv.index("--fragment") + 1]
        with open(dest, "w", encoding="utf-8") as f:
            f.write(frag)
        print("wrote fragment", dest)


if __name__ == "__main__":
    main()
