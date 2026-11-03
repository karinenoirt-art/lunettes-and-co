"""Blocs réutilisés d'une page à l'autre (boutons, magasins, FAQ, appel final)."""

from site_data import BIAS, PASSAGE, PRODUCTS, STORES

TODO_PHONE = '<span class="todo">téléphone à compléter</span>'

NOTICE_TELE = ("<strong>Ce n'est pas un service d'urgence : en cas d'urgence, contactez le SAMU au 15.</strong> "
               "Téléconsultation réservée aux personnes de 16 ans et plus, sur rendez-vous.")


def ext(href, label, cls):
    return f'<a class="btn {cls}" href="{href}" target="_blank" rel="noopener">{label}</a>'


def rdv_buttons(p, notice=True, urgence=True):
    """Bouton principal téléconsultation (choix du magasin), sa mention juste en dessous,
    puis les rendez-vous en magasin par magasin.
    urgence=False : sans la mention SAMU (réservée à l'accueil, à la téléconsultation et à la FAQ)."""
    tele = f'<a class="btn btn-tele" href="{p}teleconsultation-ophtalmologie/" data-open-rdv="tele">Téléconsultation d\'ophtalmologie : prendre rendez-vous</a>'
    stores = (f"{ext(PASSAGE['opc'], 'Rendez-vous en magasin : Le Passage', 'btn-store')}\n"
              f"  {ext(BIAS['opc'], 'Rendez-vous en magasin : Bias', 'btn-store')}")
    if not notice:
        return f'\n<div class="btn-row">\n  {tele}\n  {stores}\n</div>'
    return f"""
<div class="btn-row btn-row-tele">
  {tele}
</div>
{f'<p class="notice notice-tele">{NOTICE_TELE}</p>' if urgence else ''}
<div class="btn-row btn-row-stores">
  {stores}
</div>"""


def store_buttons(store):
    return f"""
<div class="btn-row">
  {ext(store['doctolib'], "Téléconsultation d'ophtalmologie : prendre rendez-vous", 'btn-tele')}
  {ext(store['opc'], 'Rendez-vous en magasin', 'btn-store')}
</div>
"""


def phone_html(store):
    if store["phone"]:
        return f'<a href="tel:{store["phone_intl"]}">{store["phone"]}</a>'
    return TODO_PHONE


def hours_table(store):
    rows = "".join(f"<tr><td>{d}</td><td>{h}</td></tr>" for d, h in store["hours"])
    return f'<table class="hours" aria-label="Horaires {store["name"]}">{rows}</table>'


def store_card(p, store, extra=""):
    return f"""
<article class="card store-card">
  <img src="{p}assets/img/{store['image']}" alt="{store['image_alt']}" loading="lazy" width="1600" height="1200">
  <div class="body">
    <span class="tag">{store['near']}</span>
    <h3>Lunettes &amp; Co, {store['name']}</h3>
    <p>{store['address']}<br>Téléphone : {phone_html(store)}</p>
    {extra}
    <div class="btn-row">
      <a class="btn btn-ghost btn-sm" href="{p}{store['page']}">Voir le magasin</a>
      {ext(store['opc'], 'Rendez-vous en magasin', 'btn-store btn-sm')}
    </div>
  </div>
</article>"""


def where(p, title="Où nous trouver ?", passage_extra="", bias_extra=""):
    return f"""
<section class="bg-cream2">
  <div class="wrap">
    <div class="section-head"><span class="kicker">Nos magasins</span><h2>{title}</h2></div>
    <div class="grid grid-2">
      {store_card(p, PASSAGE, passage_extra)}
      {store_card(p, BIAS, bias_extra)}
    </div>
  </div>
</section>"""


def reviews_links():
    """Liens vers les avis Google de chaque magasin (les avis restent sur Google, rien n'est recopié)."""
    cards = "".join(f"""
<a class="card review-link" href="{s['reviews']}" target="_blank" rel="noopener"><span class="g" aria-hidden="true">G</span>
  <span><strong>Lunettes &amp; Co, {s['name']}</strong><span>Lire les avis sur Google</span></span></a>""" for s in STORES)
    return f'<div class="reviews">{cards}</div>'


def review_quotes(store):
    """Avis Google positifs repris mot pour mot, avec leur source, leur auteur et la date de la visite."""
    from html import escape
    cards = "".join(f"""
<figure class="card review-quote"><blockquote>« {escape(t)} »</blockquote>
  <figcaption>{escape(a)} · avis Google, visite en {escape(d)}</figcaption></figure>""" for t, a, d in store["review_quotes"])
    return f'<div class="review-quotes">{cards}</div>'


def gallery(p, store):
    imgs = "".join(f'<img src="{p}assets/img/{f}" alt="{alt}" loading="lazy" width="1400" height="1050">'
                   for f, alt in store["gallery"])
    cls = "gallery g3" if len(store["gallery"]) == 3 else "gallery"
    return f'<div class="{cls}">{imgs}</div>'


def faq(items):
    return '<div class="faq">' + "".join(
        f'<details><summary>{q}</summary><div class="answer"><p>{a}</p></div></details>' for q, a in items
    ) + "</div>"


def faq_section(p, items, title="Questions fréquentes", more=True):
    link = f'<p style="margin-top:1.5rem"><a href="{p}faq/">Toutes les questions fréquentes →</a></p>' if more else ""
    return f"""
<section>
  <div class="wrap">
    <div class="section-head"><span class="kicker">FAQ</span><h2>{title}</h2></div>
    {faq(items)}
    {link}
  </div>
</section>"""


def cta_end(p, title, text=""):
    return f"""
<section class="bg-orange cta-band">
  <div class="wrap">
    <h2>{title}</h2>
    {f'<p>{text}</p>' if text else ''}
    <div class="btn-row">
      <a class="btn btn-tele" href="{p}teleconsultation-ophtalmologie/" data-open-rdv="tele">Téléconsultation d'ophtalmologie</a>
      <a class="btn btn-store" href="{p}contact-rendez-vous/" data-open-rdv="magasin">Rendez-vous en magasin</a>
    </div>
  </div>
</section>"""


def page_hero(p, kicker, h1, intro, image, alt, buttons=None, shapes=("c-orange", "c-blue")):
    return f"""
<section class="page-hero">
  <div class="wrap hero-grid">
    <div>
      <span class="kicker">{kicker}</span>
      <h1>{h1}</h1>
      {intro}
      {buttons if buttons is not None else rdv_buttons(p, urgence=False)}
    </div>
    <div class="hero-media">
      <img src="{p}assets/img/{image}" alt="{alt}" width="1600" height="1200">
      <i class="shape s1 {shapes[0]}"></i>
      <i class="shape s2 {shapes[1]}"></i>
    </div>
  </div>
</section>"""


def products_grid(p, exclude=None):
    cards = "".join(f"""
<a class="card" href="{p}{h}"><span class="num">{i:02d}</span><h3>{label}</h3><p>{desc}</p><span class="arrow">Découvrir →</span></a>"""
                    for i, (h, label, desc, c) in enumerate((x for x in PRODUCTS if x[0] != exclude), 1))
    return f'<div class="grid grid-3">{cards}</div>'


def pattern(p=""):
    """Motif de la charte Lunettes & Co (image extraite de COULEURS MOTIFS.ai)."""
    return f'<img class="pattern" src="{p}assets/img/motif-charte.jpg" alt="" width="1000" height="1000" loading="lazy">'


ORDONNANCE_FAQ = [
    ("Mon ordonnance est-elle encore valable ?",
     "Cela dépend de votre âge à la date de l'ordonnance. Lunettes : 1 an avant 16 ans, 5 ans de 16 à 42 ans, "
     "3 ans après 42 ans. Lentilles de contact : 1 an avant 16 ans, 3 ans à partir de 16 ans. "
     "Sauf mention contraire sur l'ordonnance."),
    ("Tous les combien puis-je renouveler mes lunettes ?",
     "Pour la prise en charge par l'Assurance Maladie : une paire tous les 2 ans à partir de 16 ans, et tous les ans entre 6 et "
     "16 ans. Avant 6 ans, une ou plusieurs paires par an si la vue évolue. Un adulte peut renouveler après 1 an si sa vue a "
     "évolué. Votre complémentaire santé peut avoir ses propres règles : nous vous renseignons en magasin."),
    ("Mon opticien peut-il renouveler ma correction sans nouvelle ordonnance ?",
     "Dans certains cas, oui : après un contrôle de la vue, l'opticien peut adapter la correction à partir d'une "
     "ordonnance en cours de validité, sauf opposition du médecin."),
]

FAQ_RDV = ("Faut-il prendre rendez-vous ?",
           "Vous pouvez passer sans rendez-vous, mais nous recommandons d'en prendre un, surtout pour un examen de vue : "
           "il demande du temps. Avec un rendez-vous, vous n'attendez pas et vous êtes pris en charge tout de suite."
           f'<br><a href="{BIAS["opc"]}" target="_blank" rel="noopener">Prendre rendez-vous à Bias</a> · '
           f'<a href="{PASSAGE["opc"]}" target="_blank" rel="noopener">Prendre rendez-vous au Passage</a>')
FAQ_RDV_TELE = ("Quelle est la différence entre le rendez-vous téléconsultation et le rendez-vous en magasin ?",
                "La téléconsultation permet de consulter un ophtalmologue en visioconférence depuis le magasin, sur rendez-vous "
                "(Doctolib). Le rendez-vous en magasin sert aux lunettes, aux lentilles, aux réglages et réparations."
                f'<br><a href="{BIAS["doctolib"]}" target="_blank" rel="noopener">Rendez-vous de téléconsultation à Bias</a> · '
                f'<a href="{PASSAGE["doctolib"]}" target="_blank" rel="noopener">Rendez-vous de téléconsultation au Passage</a>')
FAQ_MIX = ("Puis-je mélanger une monture 100% Santé et des verres à tarifs libres ?",
           "Oui. Vous pouvez associer une monture 100% Santé à des verres à tarifs libres, ou l'inverse. En revanche, les deux "
           "verres doivent venir de la même offre : on ne peut pas mélanger un verre 100% Santé et un verre à tarif libre. "
           "Dans ce cas, le remboursement dépend de votre complémentaire santé. Nous vous remettons un devis gratuit pour comparer.")
FAQ_PARKING_PASSAGE = ("Au Passage, il y a des places de parking devant le magasin, et vous pouvez aussi vous garer au parking "
                       "du Lidl, dans la zone commerciale. Des places PMR sont disponibles.")
FAQ_PARKING_BIAS = "À Bias, vous pouvez vous garer sur le parking du centre commercial Auchan. Des places PMR sont disponibles."
# J40 : réparation (page Réparation et FAQ générale)
FAQ_REGLAGE = ("Pouvez-vous régler mes lunettes ?",
               "Oui, quel que soit l'endroit où vous les avez achetées. Passez au magasin, avec ou sans rendez-vous.")
FAQ_CASSE = ("Mes lunettes sont cassées, pouvez-vous les réparer ?",
             "Cela dépend de la casse. Une vis, une plaquette ou une branche se remplacent souvent : passez nous voir, nous "
             "regardons ensemble si la monture est réparable.")
FAQ_PRIX_REPARATION = ("Combien coûte une réparation ?",
                       "Une petite réparation est gratuite. Pour une réparation plus importante, le prix dépend de ce qui est cassé : "
                       "nous vous l'annonçons avant de commencer. Les lunettes encore couvertes par la garantie sont réparées sans "
                       "frais, selon ses conditions.")
TEXTE_ULTRASONS = ("Le bac à ultrasons élimine le gras, la poussière et les dépôts, y compris dans les recoins (charnières, "
                   "plaquettes, contour des verres). Vos lunettes sont propres et les verres retrouvent leur transparence.")
FAQ_ULTRASONS = ("À quoi sert le nettoyage aux ultrasons ?", TEXTE_ULTRASONS)
FAQ_PAY = ("Puis-je payer en plusieurs fois ?",
           "Oui, le paiement en plusieurs fois est possible, jusqu'à 4 fois, dans nos deux magasins.")
FAQ_VERRES = ("Pouvez-vous changer seulement les verres de ma monture ?",
              "Si votre monture est en bon état, nous pouvons simplement changer les verres. C'est l'opticien qui juge "
              "de l'état de la monture : elle ne doit pas être abîmée ni risquer de casser au montage.")
