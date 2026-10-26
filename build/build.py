"""Génère le site statique Lunettes & Co (HTML prêt pour GitHub Pages).

Usage :  python3 build/build.py
Les pages sont écrites à la racine du dépôt (index.html, opticien-bias/index.html, ...).
Les textes viennent de Site-reference/ (fichiers 14 à 32) ; modifier ici puis relancer.
"""

import json
import os
import re

from site_data import (BIAS, BRANDS, DOMAIN, PASSAGE, PRODUCTS, SITE_NAME, STORES)
from pages import PAGES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Tant que le site est une ébauche, il n'est pas indexé par les moteurs de recherche.
DRAFT = True

with open(os.path.join(ROOT, "assets", "logo.svg"), encoding="utf-8") as f:
    LOGO_SVG = re.sub(r"<\?xml[^>]*\?>\s*", "", f.read())
    LOGO_SVG = re.sub(r"<defs>.*?</defs>", "<style>path{fill:currentColor}</style>", LOGO_SVG, flags=re.S)
    LOGO_SVG = LOGO_SVG.replace("<svg ", '<svg role="img" aria-label="Lunettes & Co, opticiens" ', 1)
    LOGO_SVG = re.sub(r'\s(id|data-name)="[^"]*"', "", LOGO_SVG)

ICON_CAL = '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="3"/><path d="M8 3v4M16 3v4M3 10h18"/></svg>'
ICON_VIDEO = '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="2" y="6" width="14" height="12" rx="3"/><path d="m16 10 6-3v10l-6-3"/></svg>'


def header(p, slug):
    def link(href, label):
        cur = ' aria-current="page"' if href == slug else ""
        return f'<a href="{p}{href}"{cur}>{label}</a>'

    products = "".join(link(h, label) for h, label, _, _ in PRODUCTS)
    return f"""
<a class="skip" href="#contenu">Aller au contenu</a>
<div class="draft-bar">Ébauche v1 · textes en cours de validation · site non indexé</div>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="logo" href="{p or './'}" aria-label="Accueil Lunettes & Co">{LOGO_SVG}<span class="logo-sub">opticiens</span></a>
    <button class="menu-toggle" aria-expanded="false" aria-controls="nav" aria-label="Ouvrir le menu"><span></span><span></span><span></span></button>
    <nav class="nav" id="nav" aria-label="Navigation principale">
      <div class="nav-group"><button aria-expanded="false">Nos magasins</button>
        <div class="submenu">{link(PASSAGE['page'], 'Le Passage, près d’Agen')}{link(BIAS['page'], 'Bias, près de Villeneuve-sur-Lot')}</div></div>
      <div class="nav-group"><button aria-expanded="false">Lunettes &amp; services</button>
        <div class="submenu">{products}</div></div>
      {link('marques/', 'Marques')}
      {link('notre-histoire/', 'Notre histoire')}
      {link('faq/', 'FAQ')}
      <a class="nav-mobile-only" href="{p}teleconsultation-ophtalmologie/">Téléconsultation</a>
      {link('contact-rendez-vous/', 'Contact')}
    </nav>
    <div class="header-cta">
      <a class="btn btn-tele btn-sm" href="{p}teleconsultation-ophtalmologie/" data-open-rdv="tele">{ICON_VIDEO}Téléconsultation</a>
      <a class="btn btn-store btn-sm" href="{p}contact-rendez-vous/" data-open-rdv="">{ICON_CAL}Prendre rendez-vous</a>
    </div>
  </div>
</header>"""


def store_hours_short(store):
    return "<br>".join(f"{d} : {h}" for d, h in store["hours"])


def footer(p):
    cols = []
    for s in STORES:
        phone = (f'<a href="tel:{s["phone_intl"]}">{s["phone"]}</a>' if s["phone"]
                 else '<span class="todo">Téléphone à compléter</span>')
        cols.append(f"""
      <div>
        <h3>{s['label']}</h3>
        <p>{s['address']}<br>{phone}</p>
        <p class="hours-foot">{store_hours_short(s)}</p>
        <p><a href="{p}{s['page']}">Voir le magasin</a></p>
      </div>""")
    links = "".join(f'<li><a href="{p}{h}">{label}</a></li>' for h, label, _, _ in PRODUCTS)
    return f"""
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <a class="logo" href="{p or './'}" aria-label="Accueil Lunettes & Co">{LOGO_SVG}<span class="logo-sub">opticiens</span></a>
        <p>Opticien indépendant en Lot-et-Garonne : au Passage et à Bias.</p>
        <ul>
          <li><a href="{p}teleconsultation-ophtalmologie/">Téléconsultation d'ophtalmologie</a></li>
          <li><a href="{p}marques/">Nos marques</a></li>
          <li><a href="{p}notre-histoire/">Notre histoire</a></li>
          <li><a href="{p}faq/">Questions fréquentes</a></li>
          <li><a href="{p}contact-rendez-vous/">Contact et rendez-vous</a></li>
        </ul>
      </div>
      {''.join(cols)}
      <div>
        <h3>Lunettes &amp; services</h3>
        <ul>{links}</ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 Lunettes &amp; Co, opticiens · Horaires provisoires, à vérifier sur nos fiches Google</span>
      <span><a href="{p}mentions-legales/">Mentions légales</a> · <a href="{p}confidentialite/">Confidentialité</a></span>
    </div>
  </div>
</footer>
<div class="mobile-bar">
  <a class="btn btn-tele" href="{p}teleconsultation-ophtalmologie/" data-open-rdv="tele">{ICON_VIDEO}Téléconsultation</a>
  <a class="btn btn-store" href="{p}contact-rendez-vous/" data-open-rdv="">{ICON_CAL}Rendez-vous</a>
</div>"""


def rdv_dialog(p):
    stores = "".join(f"""
        <a class="choice" data-store="{s['key']}" href="{s['opc']}"
           data-tele="{s['doctolib']}" data-magasin="{s['opc']}" data-libre="{p}{s['page']}">
          <i class="dot {'c-orange' if s is PASSAGE else 'c-blue'}"></i>
          <div><strong>{s['label']}</strong><span>{s['address']}</span></div>
        </a>""" for s in STORES)
    return f"""
<dialog class="rdv-dialog" id="rdv" aria-labelledby="rdv-title">
  <button class="rdv-close" aria-label="Fermer">×</button>
  <div class="rdv-inner">
    <div data-step="1">
      <span class="rdv-step-label">Étape 1 sur 2</span>
      <h2 id="rdv-title">Quel rendez-vous ?</h2>
      <div class="choice-list">
        <button class="choice" data-choose="tele"><i class="dot c-blue"></i>
          <div><strong>Téléconsultation d'ophtalmologie</strong><span>Voir un ophtalmologue en visioconférence depuis le magasin (Doctolib).</span></div></button>
        <button class="choice" data-choose="magasin"><i class="dot c-green"></i>
          <div><strong>Rendez-vous en magasin</strong><span>Essayer des lunettes, être conseillé, lentilles, réglage, réparation.</span></div></button>
        <button class="choice" data-choose="libre"><i class="dot c-coral"></i>
          <div><strong>Passer sans rendez-vous</strong><span>Adresse, horaires et téléphone du magasin.</span></div></button>
      </div>
    </div>
    <div data-step="2" hidden>
      <button class="rdv-back">← Changer de type de rendez-vous</button>
      <span class="rdv-step-label" style="display:block;margin-top:1rem">Étape 2 sur 2</span>
      <h2 data-step-title>Choisissez votre magasin</h2>
      <p class="notice" data-type-notice="tele" hidden><strong>Ce n'est pas un service d'urgence : en cas d'urgence, contactez le SAMU au 15.</strong> Réservé aux personnes de 16 ans et plus. La réservation s'ouvre sur Doctolib.</p>
      <p class="notice" data-type-notice="magasin" hidden>La réservation s'ouvre sur le site de notre réseau, Opticiens par Conviction.</p>
      <p class="notice" data-type-notice="libre" hidden>Vous pouvez passer sans rendez-vous ; le rendez-vous limite l'attente.</p>
      <div class="choice-list">{stores}
      </div>
    </div>
  </div>
</dialog>"""


def json_ld_org():
    def optician(s):
        d = {
            "@type": "Optician",
            "name": f"{SITE_NAME} {s['name']}",
            "address": {"@type": "PostalAddress", "streetAddress": s["street"], "postalCode": s["postcode"],
                        "addressLocality": s["city"], "addressRegion": "Lot-et-Garonne", "addressCountry": "FR"},
            "url": f"{DOMAIN}/{s['page']}",
            "parentOrganization": {"@id": f"{DOMAIN}/#organisation"},
        }
        if s["phone_intl"]:
            d["telephone"] = s["phone_intl"]
        return d

    data = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "Organization", "@id": f"{DOMAIN}/#organisation", "name": SITE_NAME,
             "url": f"{DOMAIN}/", "logo": f"{DOMAIN}/assets/logo.svg",
             "description": "Opticien indépendant en Lot-et-Garonne, au Passage (près d'Agen) et à Bias (près de Villeneuve-sur-Lot)."},
            optician(PASSAGE),
            optician(BIAS),
        ],
    }
    return json.dumps(data, ensure_ascii=False, indent=1)


def json_ld_faq(faqs):
    def text(html):
        return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", html)).strip()

    data = {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": text(a)}} for q, a in faqs]}
    return json.dumps(data, ensure_ascii=False, indent=1)


def render(page):
    slug = page["slug"]
    depth = slug.count("/")
    p = "../" * depth
    body = page["body"](p)
    robots = '<meta name="robots" content="noindex, nofollow">' if DRAFT else ""
    ld = ""
    if page.get("org_ld"):
        ld += f'<script type="application/ld+json">{json_ld_org()}</script>'
    if page.get("faq_ld"):
        ld += f'<script type="application/ld+json">{json_ld_faq(page["faq_ld"])}</script>'
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{page['title']}</title>
<meta name="description" content="{page['description']}">
{robots}
<link rel="canonical" href="{DOMAIN}/{slug}">
<meta property="og:title" content="{page['title']}">
<meta property="og:description" content="{page['description']}">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<link rel="icon" href="{p}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&family=League+Spartan:wght@600;700;800&family=Space+Mono&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/style.css">
{ld}
</head>
<body>
{header(p, slug)}
<main id="contenu">
{body}
</main>
{footer(p)}
{rdv_dialog(p)}
<script src="{p}assets/site.js"></script>
</body>
</html>
"""


def main():
    for page in PAGES:
        out_dir = os.path.join(ROOT, page["slug"])
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(render(page))
        print("ok", page["slug"] or "/")
    print(len(PAGES), "pages générées")


if __name__ == "__main__":
    main()
