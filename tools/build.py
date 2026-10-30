#!/usr/bin/env python3
"""Generate AmigaFAQ pages in a Workbench 3.1 style.

Layout is a plain HTML table (sidebar + content) with bgcolor attributes, so
classic Amiga browsers (AWeb, IBrowse, Voyager) still get the two-column grey
look even without modern CSS. Output is ASCII only."""
import sys, os, re, hashlib

OUT = sys.argv[1]
HERE = os.path.dirname(os.path.abspath(__file__))
# Version tag so browsers fetch the stylesheet again whenever it changes
CSS_VER = hashlib.md5(open(os.path.join(OUT, "style.css"), "rb").read()).hexdigest()[:8]

TOPICS = [
    ("getting-started", "Getting Started"),
    ("hardware", "Hardware"),
    ("software", "Software"),
    ("emulation", "Emulation"),
    ("history", "History"),
]

exec(open(os.path.join(HERE, "content.py")).read())

def anchor(q):
    return re.sub(r"[^a-z0-9]+", "-", q.lower()).strip("-")[:60]

GADGETS_L = '<span class="gad close" aria-hidden="true"><i></i></span>'
GADGETS_R = '<span class="gad depth" aria-hidden="true"><i></i><b></b></span>'

def window(title, inner, cls=""):
    return """<table class="win %s" width="100%%" cellspacing="0" cellpadding="0" border="1" bgcolor="#AAAAAA">
<tr><td class="titlebar" bgcolor="#6688BB">%s<span class="wtitle"><font color="#000000"><b>%s</b></font></span>%s</td></tr>
<tr><td class="winbody">
%s
</td></tr>
</table>""" % (cls, GADGETS_L, title, GADGETS_R, inner)

def sidebar(current):
    def item(href, label, active):
        cls = ' class="sel"' if active else ""
        return '<a href="%s"%s>%s</a>' % (href, cls, label)
    lines = ['<ul class="tree">']
    lines.append('<li class="drawer">%s</li>' % item("index.html", "AmigaFAQ", current == "index"))
    lines.append('<li><ul>')
    for slug, title in TOPICS:
        active = slug == current
        lines.append('<li class="drawer%s">%s' % (" open" if active else "", item(slug + ".html", title, active)))
        if active:
            lines.append('<ul class="qs">')
            for q, _ in CONTENT[slug][1]:
                lines.append('<li>%s</li>' % item("#" + anchor(q), q, False))
            lines.append('</ul>')
        lines.append('</li>')
    lines.append('</ul></li>')
    # Always the bottom-most entry, at the same level as "AmigaFAQ"
    lines.append('<li class="file">%s</li>' % item("about.html", "About AmigaFAQ", current == "about"))
    lines.append('</ul>')
    return "\n".join(lines)

def page(slug, title, body):
    full_title = "AmigaFAQ" if slug == "index" else "%s - AmigaFAQ" % title
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(full_title)s</title>
<meta name="description" content="Answers to frequently asked questions about the Commodore Amiga.">
<link rel="preload" href="fonts/topaz-a1200.woff" as="font" type="font/woff" crossorigin>
<link rel="stylesheet" href="style.css?v=%(css_ver)s">
</head>
<body bgcolor="#AAAAAA" text="#000000" link="#000000" vlink="#000000">
<a name="top" id="top"></a>
<div class="screenbar"><b>AmigaFAQ</b> &nbsp; Frequently asked questions about the Commodore Amiga<sup class="tm">TM</sup></div>
<table class="layout" width="100%%" cellspacing="8" cellpadding="0" border="0">
<tr>
<td class="side" width="250" valign="top">
%(sidebar)s
</td>
<td class="content" valign="top">
%(main)s
</td>
</tr>
</table>
<div class="foot">
<p>&copy; 2026 AmigaFAQ. Content licensed under <a href="https://creativecommons.org/licenses/by-sa/4.0/" rel="license">CC BY-SA 4.0</a>.
Corrections and suggestions welcome on <a href="https://github.com/luvwagn/AmigaFAQ">GitHub</a>.</p>
<p class="tmnote">Amiga, the Boing Ball logo, the slanted A logo, and the checkmark logo are trademarks of Amiga Corporation and may be registered internationally.</p>
</div>
</body>
</html>
""" % dict(full_title=full_title, css_ver=CSS_VER,
           sidebar=window("Topics", sidebar(slug), "sidewin"),
           main=window(title if slug != "index" else "AmigaFAQ", body, "mainwin"))

def paras(text):
    return "\n".join("<p>%s</p>" % p.strip() for p in text.strip().split("\n\n"))

def qa_page(slug, title, intro, qas):
    items = ['<p class="intro">%s</p>' % intro]
    for q, a in qas:
        items.append('<div class="qa">\n<h3><a name="%s" id="%s">%s</a></h3>\n%s\n<p class="up"><a href="#top" class="btn">Top</a></p>\n</div>'
                     % (anchor(q), anchor(q), q, paras(a)))
    return page(slug, title, "\n".join(items))

def write(name, html):
    html.encode("ascii")  # fail loudly on non-ASCII
    with open(os.path.join(OUT, name), "w") as f:
        f.write(html)

os.makedirs(OUT, exist_ok=True)
for slug, title in TOPICS:
    intro, qas = CONTENT[slug]
    write(slug + ".html", qa_page(slug, title, intro, qas))

# Home page
parts = ["""<p class="intro">AmigaFAQ answers common questions about the Commodore Amiga: the hardware, the
software, running Amiga programs today, and the story behind the machine. Whether you are dusting off
an A500 from the attic or trying emulation for the first time, pick a topic from the list.</p>"""]
for slug, title in TOPICS:
    intro, qas = CONTENT[slug]
    sample = "\n".join('<li><a href="%s.html#%s">%s</a></li>' % (slug, anchor(q), q) for q, _ in qas[:3])
    parts.append('<div class="qa">\n<h3><a href="%s.html">%s</a></h3>\n<p>%s</p>\n<ul>\n%s\n</ul>\n<p class="up"><a href="%s.html" class="btn">All %d questions</a></p>\n</div>'
                 % (slug, title, intro, sample, slug, len(qas)))
parts.append('<p class="note">This site is deliberately simple so it can be read on real Amiga web browsers as well as modern ones.</p>')
write("index.html", page("index", "Home", "\n".join(parts)))

# About page
about = []
for heading, text in ABOUT:
    about.append('<div class="qa">\n<h3>%s</h3>\n%s\n</div>' % (heading, paras(text)))
write("about.html", page("about", "About AmigaFAQ", '<p class="intro">%s</p>\n%s' % (ABOUT_INTRO, "\n".join(about))))
print("built", len(TOPICS) + 1, "pages;", sum(len(CONTENT[s][1]) for s, _ in TOPICS), "questions")
