#!/usr/bin/env python3
"""
Inline the six section icons into the pages that need them.

The site inlines every SVG it uses (the logo included) rather than referencing a
sprite: an external <use> sprite does not resolve from file://, and the pages
are meant to open by double-click.  So the icons are inlined too, from the
single normalised source in assets/icons/, which is the only place they are
allowed to be edited.
"""
import re, glob, pathlib

ROOT = pathlib.Path("/home/claude/work")
SRC = {p.stem: p.read_text().strip() for p in (ROOT / "assets/icons").glob("*.svg")}


def ic(name, cls="g-ic", extra=""):
    """The icon as inline markup, carrying a class instead of an xmlns."""
    s = SRC[name]
    s = s.replace('<svg xmlns="http://www.w3.org/2000/svg" ',
                  f'<svg class="{cls}" ')
    s = s.replace('viewBox="0 0 24 24"', f'viewBox="0 0 24 24" aria-hidden="true"{extra}')
    return s


# --- 1. header nav: the icons show only inside the mobile dropdown ----------
NAV = [("topics.html", "Topics", "topics"), ("magazine.html", "Magazine", "magazine"),
       ("lab.html", "Lab", "lab"), ("learn.html", "Learn", "learn"),
       ("community.html", "Community", "community")]

# --- 2. footer: Read / Do are exactly the six sections ----------------------
# Matched as whole stacks, not link by link: the same <a href="topics.html">
# markup also appears inside breadcrumbs, which must not pick up a footer icon.
FOOT = [(["topics.html Topics", "magazine.html Magazine", "newsletter.html Newsletter"],
         ["topics", "magazine", "newsletter"]),
        (["lab.html Interactive Lab", "learn.html Learning Paths", "community.html Community"],
         ["lab", "learn", "community"])]

# --- 3. section pages get the plate; their detail pages get the crumb mark ---
PLATE = {"topics.html": "topics", "community.html": "community", "lab.html": "lab",
         "magazine.html": "magazine", "learn.html": "learn",
         "newsletter.html": "newsletter"}
CRUMB = {"topic-computable-universe.html": "topics", "topic-machine-hypothesis.html": "topics",
         "article-hypothesis-or-sentence.html": "magazine",
         "path-ai-in-research.html": "learn", "game-hypothesis-machine.html": "lab"}

changed = {}
for path in sorted(ROOT.glob("*.html")):
    s = orig = path.read_text()

    for href, label, name in NAV:
        s = re.sub(rf'(<a class="g-nav__link"[^>]*href="{re.escape(href)}">){label}</a>',
                   lambda m: m.group(1) + ic(name, "g-ic g-nav__ic") + label + "</a>", s)

    for links, names in FOOT:
        pairs = [l.split(" ", 1) for l in links]
        old = ('<div class="g-stack g-stack--xs">'
               + "".join(f'<a href="{h}">{t}</a>' for h, t in pairs) + "</div>")
        new = ('<div class="g-stack g-stack--xs g-stack--ic">'
               + "".join(f'<a href="{h}">{ic(n, "g-ic g-ic--sm")}<span>{t}</span></a>'
                         for (h, t), n in zip(pairs, names)) + "</div>")
        s = s.replace(old, new)

    if path.name in PLATE:
        s = s.replace('<p class="crumb">',
                      f'<span class="page-head__ic">{ic(PLATE[path.name], "g-ic g-ic--lg")}</span>\n      <p class="crumb">', 1)
    if path.name in CRUMB:
        s = s.replace('<p class="crumb">',
                      f'<p class="crumb">{ic(CRUMB[path.name], "g-ic g-ic--sm crumb__ic")}', 1)

    if s != orig:
        path.write_text(s)
        changed[path.name] = len(re.findall(r'class="g-ic', s))

for k, v in changed.items():
    print(f"{k:38s} {v} icons")
