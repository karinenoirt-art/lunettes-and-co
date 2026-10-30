"""Contrôles SEO du site généré (sans dépendance).

Usage :  python3 build/build.py && python3 build/check_seo.py
Code de sortie non nul si un contrôle échoue.
"""

import json
import os
import re
import sys
from html.parser import HTMLParser
from urllib.parse import unquote, urlparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import DRAFT, ROOT  # noqa: E402
from pages import PAGES  # noqa: E402
from site_data import DOMAIN  # noqa: E402

errors = []


def fail(slug, msg):
    errors.append(f"{slug or '/'} : {msg}")


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.h1 = 0
        self.title = ""
        self.in_title = False
        self.in_ld = False
        self.ld = []
        self.meta = {}
        self.canonical = None
        self.imgs_sans_alt = 0
        self.links = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "h1":
            self.h1 += 1
        elif tag == "title":
            self.in_title = True
        elif tag == "meta":
            key = a.get("name") or a.get("property")
            if key:
                self.meta[key] = a.get("content", "")
        elif tag == "link" and a.get("rel") == "canonical":
            self.canonical = a.get("href")
        elif tag == "img" and "alt" not in a:
            self.imgs_sans_alt += 1
        elif tag == "a" and a.get("href"):
            self.links.append(a["href"])
        elif tag == "script" and a.get("type") == "application/ld+json":
            self.in_ld = True
            self.ld.append("")

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        elif tag == "script":
            self.in_ld = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        elif self.in_ld:
            self.ld[-1] += data


def target_exists(slug, href):
    u = urlparse(href)
    if u.scheme in ("http", "https", "mailto", "tel", "javascript") or href.startswith("#"):
        return True
    base = ROOT if u.path.startswith("/") else os.path.join(ROOT, slug)
    path = os.path.normpath(os.path.join(base, unquote(u.path).lstrip("/")))
    if not path.startswith(ROOT):
        return False
    return os.path.isfile(os.path.join(path, "index.html")) if os.path.isdir(path) else os.path.isfile(path)


for page in PAGES:
    slug = page["slug"]
    file = os.path.join(ROOT, slug, "index.html")
    if not os.path.isfile(file):
        fail(slug, "index.html absent (lancer build.py)")
        continue
    raw = open(file, encoding="utf-8").read()
    p = Page()
    p.feed(raw)

    if p.h1 != 1:
        fail(slug, f"{p.h1} balises H1 (1 attendue)")
    title = p.title.strip()
    if len(title) > 60:
        fail(slug, f"title de {len(title)} caractères (max 60)")
    n = len(p.meta.get("description", ""))
    if not 120 <= n <= 160:
        fail(slug, f"meta description de {n} caractères (120 à 160)")
    if p.canonical != f"{DOMAIN}/{slug}":
        fail(slug, f"canonical « {p.canonical} » ≠ {DOMAIN}/{slug}")
    if p.imgs_sans_alt:
        fail(slug, f"{p.imgs_sans_alt} image(s) sans attribut alt")
    for block in p.ld:
        try:
            json.loads(block)
        except ValueError as e:
            fail(slug, f"JSON-LD invalide ({e})")
    for href in p.links:
        if not target_exists(slug, href):
            fail(slug, f"lien interne cassé : {href}")
    if "lunettes-sur-mesure" in raw:
        fail(slug, "occurrence de « lunettes-sur-mesure »")
    has_noindex = "noindex" in p.meta.get("robots", "")
    if has_noindex != DRAFT:
        fail(slug, f"noindex {'présent' if has_noindex else 'absent'} alors que DRAFT = {DRAFT}")

# robots.txt et sitemap.xml
robots = open(os.path.join(ROOT, "robots.txt"), encoding="utf-8").read()
closed = re.search(r"User-agent: \*\s*\nDisallow: /\s*$", robots) is not None
if closed != DRAFT:
    fail("robots.txt", f"{'fermé' if closed else 'ouvert'} alors que DRAFT = {DRAFT}")
sitemap = os.path.join(ROOT, "sitemap.xml")
if DRAFT and os.path.exists(sitemap):
    fail("sitemap.xml", "présent alors que DRAFT = True")
if not DRAFT:
    if not os.path.exists(sitemap):
        fail("sitemap.xml", "absent alors que DRAFT = False")
    else:
        text = open(sitemap, encoding="utf-8").read()
        if "lunettes-sur-mesure" in text or "_planche" in text:
            fail("sitemap.xml", "contient une page à exclure")
        if len(re.findall(r"<loc>", text)) != len(PAGES):
            fail("sitemap.xml", "nombre d'entrées différent du nombre de pages")

if errors:
    print(f"{len(errors)} contrôle(s) en échec :")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print(f"Tous les contrôles passent ({len(PAGES)} pages, DRAFT = {DRAFT}).")
