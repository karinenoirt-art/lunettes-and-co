"""Blocs réutilisés d'une page à l'autre (boutons, magasins, FAQ, appel final)."""

from site_data import BIAS, PASSAGE, PRODUCTS, STORES

TODO_PHONE = '<span class="todo">téléphone à compléter</span>'

NOTICE_TELE = ("<strong>Ce n'est pas un service d'urgence : en cas d'urgence, contactez le SAMU au 15.</strong> "
               "Téléconsultation réservée aux personnes de 16 ans et plus, sur rendez-vous.")


def ext(href, label, cls):
    return f'<a class="btn {cls}" href="{href}" target="_blank" rel="noopener">{label}</a>'


def rdv_buttons(p, notice=True):
    """Bouton principal téléconsultation (choix du magasin) + rendez-vous en magasin par magasin."""
    html = f"""
<div class="btn-row">
  <a class="btn btn-tele" href="{p}teleconsultation-ophtalmologie/" data-open-rdv="tele">Téléconsultation d'ophtalmologie : prendre rendez-vous</a>
  {ext(PASSAGE['opc'], 'Rendez-vous en magasin : Le Passage', 'btn-store')}
  {ext(BIAS['opc'], 'Rendez-vous en magasin : Bias', 'btn-store')}
</div>"""
    if notice:
        html += f'<p class="notice">{NOTICE_TELE}</p>'
    return html


def store_buttons(store):
    return f"""
<div class="btn-row">
  {ext(store['doctolib'], "Téléconsultation d'ophtalmologie, prendre rendez-vous", 'btn-tele')}
  {ext(store['opc'], 'Rendez-vous en magasin', 'btn-store')}
</div>
<p class="notice">{NOTICE_TELE}</p>"""


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
      {buttons if buttons is not None else rdv_buttons(p)}
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
<a class="card" href="{p}{h}"><i class="dot {c}"></i><h3>{label}</h3><p>{desc}</p><span class="arrow">Découvrir →</span></a>"""
                    for h, label, desc, c in PRODUCTS if h != exclude)
    return f'<div class="grid grid-3">{cards}</div>'


def pattern():
    tiles = ["p-arcs", "p-stripes", "p-moon", "p-terrazzo", "p-sun", "p-terrazzo", "p-arcs", "p-tri",
             "p-wave", "p-eye", "p-dot", "p-bars", "p-terrazzo", "p-tri2", "p-quarter", "p-eye2"]
    return '<div class="pattern" aria-hidden="true">' + "".join(f'<i class="{t}"></i>' for t in tiles) + "</div>"


ORDONNANCE_FAQ = [
    ("Mon ordonnance est-elle encore valable ?",
     "Cela dépend de votre âge au moment où elle a été établie. Moins de 16 ans : 1 an. De 16 à 42 ans : 5 ans. "
     "Plus de 42 ans : 3 ans. Le médecin peut réduire cette durée."),
    ("Tous les combien puis-je renouveler mes lunettes ?",
     "Pour la prise en charge par l'Assurance Maladie : en général tous les 2 ans à partir de 16 ans, et tous les ans "
     "avant 16 ans. Si votre vue a évolué, un renouvellement après 1 an peut être possible. Votre opticien vous "
     "renseigne selon votre situation et votre complémentaire santé."),
    ("Mon opticien peut-il renouveler ma correction sans nouvelle ordonnance ?",
     "Dans certains cas, oui : après un contrôle de la vue, l'opticien peut adapter la correction à partir d'une "
     "ordonnance en cours de validité, sauf opposition du médecin."),
]

FAQ_RDV = ("Faut-il prendre rendez-vous ?",
           "Vous pouvez venir sans rendez-vous, mais nous le recommandons pour limiter l'attente, notamment quand un "
           "examen de vue est en cours.")
FAQ_PAY = ("Puis-je payer en plusieurs fois ?",
           "Oui, le paiement en plusieurs fois sans frais est possible, jusqu'à 4 fois, dans nos deux magasins.")
FAQ_VERRES = ("Pouvez-vous changer seulement les verres de ma monture ?",
              "Si votre monture est en bon état, nous pouvons simplement changer les verres. C'est l'opticien qui juge "
              "de l'état de la monture : elle ne doit pas être abîmée ni risquer de casser au montage.")
