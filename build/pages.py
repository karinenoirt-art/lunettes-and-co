"""Contenu des pages. Textes repris de Site-reference/ (fichiers 14 à 32), notes internes retirées.

Chaque page : slug (dossier), title, description (meta), body(p) où p est le préfixe relatif vers la racine.
"""

from blocks import (FAQ_PAY, FAQ_RDV, FAQ_VERRES, NOTICE_TELE, ORDONNANCE_FAQ, TODO_PHONE, cta_end, ext, faq,
                    faq_section, gallery, hours_table, page_hero, pattern, phone_html, products_grid, rdv_buttons,
                    reviews_links, store_buttons, store_card, where)
from site_data import BIAS, BRANDS, PASSAGE, STORES

def badge100(p):
    return f'<img class="badge-100" src="{p}assets/img/logo-100-sante.svg" alt="100% Santé" width="176" height="47">'

CENT_POUR_CENT = """Le 100% Santé est une sélection de lunettes de vue (monture et verres), sans reste à charge avec une
complémentaire santé responsable ou la Complémentaire santé solidaire. Il concerne toute la famille : enfants, femmes et hommes."""


# ---------------------------------------------------------------- Accueil
def home(p):
    store_cards = "".join(store_card(p, s, f'<p>{"Ancien Optical Discount. " if s is BIAS else ""}'
                                            f'<a href="{s["maps"]}" target="_blank" rel="noopener">Itinéraire</a></p>')
                          for s in STORES)
    return f"""
<section class="hero-home">
  <div class="wrap hero-grid">
    <div>
      <span class="kicker">Opticiens indépendants · Lot-et-Garonne</span>
      <h1><span class="h1-big">Lunettes <em>&amp; Co</em></span>
      <span class="h1-sub">Opticien indépendant au Passage et à Bias (Lot-et-Garonne)</span></h1>
      <p class="lead"><strong>Des lunettes qui vous ressemblent.</strong> Un opticien indépendant à votre écoute, des montures pour tous les budgets.</p>
      <p>Lunettes de vue, de soleil, pour enfants, lentilles : Julien, opticien depuis plus de 15 ans, et son équipe prennent le temps de comprendre votre besoin, vos envies et votre budget. Deux magasins indépendants en Lot-et-Garonne : au Passage, près d'Agen, et à Bias, près de Villeneuve-sur-Lot.</p>
      {rdv_buttons(p)}
    </div>
    <div class="hero-media">
      <img src="{p}assets/img/loumy-miroir.jpg" alt="Lunettes de soleil Loumy vertes posées sur leur étui, devant un miroir, au magasin du Passage" width="1800" height="1350">
      <i class="shape eye"></i><i class="shape s2 c-blue"></i><i class="shape s3 c-coral"></i>
    </div>
  </div>
</section>

<section class="bg-white">
  <div class="wrap">
    <div class="section-head"><span class="kicker">Nos deux magasins</span>
      <h2>Deux magasins en Lot-et-Garonne</h2>
      <p>Au Passage, près d'Agen, et à Bias, près de Villeneuve-sur-Lot.</p></div>
    <div class="grid grid-2">{store_cards}</div>
  </div>
</section>

<section>
  <div class="wrap two-col">
    <div>
      <span class="kicker">Pourquoi Lunettes &amp; Co</span>
      <h2>Un opticien indépendant qui prend le temps</h2>
      <div class="grid" style="gap:1rem">
        <div class="card"><h3>Indépendant</h3><p>Pas d'enseigne nationale derrière nous. Nous apportons le plus grand soin au choix de nos montures, selon les goûts et les retours de nos clients depuis plus de 15 ans, avec des marques que vous ne trouvez pas partout.</p></div>
        <div class="card"><h3>Un conseil personnalisé</h3><p>Nous évaluons votre besoin : correction, usages, style, budget. Puis nous essayons les montures ensemble, jusqu'à trouver celle qui vous va.</p></div>
        <div class="card"><h3>Pour tous les budgets</h3><p>Des montures accessibles à partir de 100 euros (hors 100% Santé), et des créateurs pour se faire plaisir.</p></div>
      </div>
    </div>
    <img src="{p}assets/img/passage-salon.jpg" alt="Le coin salon du magasin du Passage, fauteuils et présentoirs de montures" loading="lazy" width="1600" height="1200">
  </div>
</section>

<section class="bg-green">
  <div class="wrap two-col">
    <div>
      <span class="kicker" style="color:var(--coral-soft)">Votre budget</span>
      <h2>Des lunettes pour tous les budgets</h2>
      <p>De la monture 100% Santé à la monture de créateur, vous comparez avant de choisir. Nous vous remettons gratuitement un devis détaillé, avec l'offre 100% Santé et l'offre à tarifs libres.</p>
      <p>Paiement en plusieurs fois, jusqu'à 4 fois.</p>
      <div class="btn-row"><a class="btn btn-light" href="{p}lunettes-de-vue/">Lunettes de vue</a>
      <a class="btn btn-light" href="{p}notre-histoire/">Notre histoire</a></div>
    </div>
    <div style="max-width:420px;justify-self:center;width:100%">{pattern(p)}</div>
  </div>
</section>

<section class="bg-white">
  <div class="wrap">
    <div class="section-head">{badge100(p)}<span class="kicker">Reste à charge nul</span><h2>Le 100% Santé</h2>
    <p>Le 100% Santé est une sélection de lunettes de vue (monture et verres), sans reste à charge avec une complémentaire
    santé responsable ou la Complémentaire santé solidaire. Il concerne toute la famille : enfants, femmes et hommes.</p>
    <p><a class="btn btn-ghost" href="{p}lunettes-de-vue/">Découvrir les lunettes de vue</a></p></div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head"><span class="kicker">Nos services</span><h2>Tout se passe en magasin</h2></div>
    {products_grid(p)}
  </div>
</section>

<section class="bg-blue">
  <div class="wrap two-col">
    <div>
      <span class="kicker" style="color:var(--coral)">Téléconsultation d'ophtalmologie</span>
      <h2>Un ophtalmologue en visioconférence, dans nos magasins</h2>
      <p>Un service de téléconsultation d'ophtalmologie augmentée, sur rendez-vous, au Passage et à Bias : des examens réalisés en magasin, puis un échange en visioconférence avec un ophtalmologue. Réservé aux personnes de 16 ans et plus.</p>
      <p><strong>Ce n'est pas un service d'urgence : en cas d'urgence, contactez le SAMU au 15.</strong></p>
      <div class="btn-row">
        {ext(PASSAGE['doctolib'], 'Prendre rendez-vous au Passage', 'btn-light')}
        {ext(BIAS['doctolib'], 'Prendre rendez-vous à Bias', 'btn-light')}
      </div>
      <p><a href="{p}teleconsultation-ophtalmologie/">Comment ça se passe ? →</a></p>
    </div>
    <img src="{p}assets/img/examen-de-vue.jpg" alt="Salle d'examen de vue équipée, au magasin du Passage" loading="lazy" width="1600" height="1200">
  </div>
</section>

<section>
  <div class="wrap two-col">
    <img src="{p}assets/img/loumy.jpg" alt="Monture Loumy, fabriquée à Montauban" loading="lazy" width="1600" height="1200">
    <div>
      <span class="kicker">Nos marques</span>
      <h2>Des créateurs, des marques accessibles, des montures fabriquées en France</h2>
      <p>Loumy, lunetier de Montauban, Bondet, Victoire d'Aqui, Marlone, Lafont Enfant, et aussi Tavat, Brett, Tiwi,
      Etnia Barcelona, Lancel, Ray-Ban et bien d'autres.</p>
      <a class="btn btn-ghost" href="{p}marques/">Voir toutes nos marques</a>
    </div>
  </div>
</section>

<section class="bg-cream2">
  <div class="wrap two-col">
    <div>
      <span class="kicker">Notre histoire</span>
      <h2>Julien, opticien indépendant depuis 2012</h2>
      <p>Julien ouvre son magasin à Bias en 2012. Il choisit ensuite de retrouver sa liberté : celle de choisir ses marques et ses montures. Un deuxième magasin ouvre au Passage en 2025, avec, parmi nos marques, des amis lunetiers à Montauban : Loumy.</p>
      <a class="btn btn-ghost" href="{p}notre-histoire/">Découvrir notre histoire</a>
    </div>
    <img src="{p}assets/img/equipe.jpg" alt="L'équipe Lunettes & Co au magasin du Passage" loading="lazy" width="1600" height="1200">
  </div>
</section>

<section class="bg-white">
  <div class="wrap">
    <div class="section-head"><span class="kicker">Avis Google</span><h2>Ce que disent nos clients</h2></div>
    {reviews_links()}
  </div>
</section>

{faq_section(p, HOME_FAQ)}
{cta_end(p, "Passez nous voir au Passage ou à Bias, ou prenez rendez-vous.")}
"""


HOME_FAQ = [
    ("Où sont vos magasins ?",
     "Au Passage (64 allée du Loriot, ZAC de Lacassagne), près d'Agen, et à Bias (centre commercial Auchan, Ponservat), "
     "près de Villeneuve-sur-Lot."),
    ("Êtes-vous une enseigne nationale ?",
     "Non, nous sommes un opticien indépendant, avec deux magasins en Lot-et-Garonne."),
    ("Proposez-vous le 100% Santé ?", "Oui, dans chaque magasin, pour toute la famille."),
    ("Peut-on consulter un ophtalmologue dans vos magasins ?",
     "Oui, en visioconférence, sur rendez-vous, depuis nos magasins de Bias et du Passage, si votre situation s'y prête. "
     "Ce n'est pas un service d'urgence : en cas d'urgence, contactez le SAMU au 15."),
    FAQ_RDV,
    FAQ_PAY,
]


# ---------------------------------------------------------------- Magasins
def store_page(store):
    is_bias = store is BIAS

    def body(p):
        if is_bias:
            intro = """<p class="lead">À Bias depuis 2012, Lunettes &amp; Co est votre opticien indépendant aux portes de Villeneuve-sur-Lot,
            dans la galerie marchande du centre commercial Auchan Ponservat. Julien, opticien depuis plus de 15 ans, et son équipe
            vous aident à choisir des lunettes qui vous ressemblent, selon votre budget et vos besoins.</p>"""
            team_title = "Un magasin que ses clients connaissent bien"
            team = """Installé depuis 2012, le magasin de Bias a une clientèle fidèle. Julien, Anne et Francesca vous accueillent
            et sont à votre écoute."""
            budget_title = "Des prix accessibles"
            budget_p = """Nos montures démarrent à 100 euros (hors 100% Santé). Devis gratuit en magasin."""
            brands_title = "Nos marques à Bias"
            brands_p = f"""Vous trouverez notamment Ray-Ban, Lancel, Tiwi, GIGIstudios, Azzaro, Guess et Chantal Thomass.
            <a href="{p}marques/">Toutes nos marques</a>."""
            craft_title = "Artisanales, fabriquées en France"
            craft = """À Bias, nous proposons Loumy, fabriquée à Montauban, et Victoire d'Aqui, fabriquée à Hossegor, dans les Landes : des
            montures artisanales. Bondet est elle aussi fabriquée en France."""
            sante_p = """Le magasin de Bias propose aussi le 100% Santé, pour tous les âges : monture et verres sans reste à charge
            avec une complémentaire santé responsable ou la Complémentaire santé solidaire. Le devis est gratuit."""
            services = f"""
        <li><a href="{p}lunettes-de-vue/">Lunettes de vue</a>, <a href="{p}lunettes-de-soleil/">lunettes de soleil</a> et <a href="{p}lunettes-enfants/">lunettes pour enfants</a>.</li>
        <li><a href="{p}lentilles-de-contact/">Lentilles de contact</a>, avec leurs produits d'entretien.</li>
        <li><a href="{p}lunettes-de-sport/">Lunettes de sport</a> (piscine, vélo, running, tir sportif) : Julien pratique lui-même le tir en compétition.</li>
        <li><a href="{p}lunettes-personnalisees/">Lunettes personnalisées</a>.</li>
        <li><a href="{p}reparation-ajustement-lunettes/">Réparation et ajustement</a> de vos montures.</li>
        <li>Téléconsultation d'ophtalmologie augmentée en magasin, <a href="{p}teleconsultation-ophtalmologie/">sur rendez-vous</a>.</li>
        <li>Facilités de paiement : jusqu'à 4 fois.</li>"""
            extra_service = "<li>Magasin partenaire du réseau de soins Carte Blanche.</li>"
            around = """Nous accueillons les clients de Villeneuve-sur-Lot, Sainte-Livrade-sur-Lot, Pujols, Lédat, Casseneuil, Allez-et-Cazeneuve et des communes voisines."""
            img2 = ("bias-accueil.jpg", "L'accueil du magasin Lunettes & Co à Bias, mur vert et logo")
            faqs = [("Peut-on venir sans rendez-vous à Bias ?",
                     "Oui, mais nous conseillons de réserver pour un examen de vue, qui demande du temps. Un rendez-vous vous évite d'attendre."),
                    ("Peut-on faire une téléconsultation d'ophtalmologie à Bias ?",
                     "Oui. Le magasin de Bias propose la téléconsultation d'ophtalmologie augmentée, sur rendez-vous, pour les personnes de 16 ans et plus."),
                    ("Proposez-vous le 100% Santé ?", "Oui, le magasin de Bias le propose aussi, pour tous les âges."),
                    ("Y a-t-il un parking ?", "Oui, le parking du centre commercial Auchan est gratuit. Le magasin est accessible par l'entrée du centre commercial."),
                    ("Le magasin s'appelait-il autrement ?", "Oui. Le magasin de Bias, ouvert en 2012, s'appelait Optical Discount. Il est aujourd'hui un opticien indépendant : Lunettes &amp; Co.")]
        else:
            intro = """<p class="lead">Au Passage, dans la ZAC de Lacassagne, près d'Agen, nous avons pensé notre magasin comme un cocon :
            un lieu chaleureux, où vous êtes à l'aise pour essayer vos montures. Julien, opticien depuis plus de 15 ans, et son équipe
            sont à votre écoute pour trouver des lunettes qui vous ressemblent, selon votre budget.</p>"""
            team_title = "Un lieu cosy, un conseil personnalisé"
            team = """Un magasin chaleureux, avec un grand choix de montures pour tous les goûts. Nous évaluons votre besoin avec vous :
            confort, esthétique, budget, correction, usages (conduite, sport, écran)."""
            budget_title = "Des prix accessibles"
            budget_p = """Nos montures démarrent à 100 euros (hors 100% Santé). Devis gratuit en magasin."""
            brands_title = "Nos marques au Passage"
            brands_p = f"""Vous trouverez notamment Brett, Tavat, Tiwi, French Retro, Marlone, Lafont Enfant, Ray-Ban et Lancel.
            <a href="{p}marques/">Toutes nos marques</a>."""
            craft_title = "Loumy, une marque artisanale"
            craft = """Au Passage, nous proposons Loumy : des montures artisanales fabriquées à Montauban par des amis de Julien."""
            extra_service = ""
            sante_p = """Le 100% Santé est une sélection de lunettes de vue (monture et verres), sans reste à charge avec une
            complémentaire santé responsable ou la Complémentaire santé solidaire. Il concerne toute la famille. Devis gratuit en magasin."""
            services = f"""
        <li><a href="{p}lunettes-de-vue/">Lunettes de vue</a>, <a href="{p}lunettes-de-soleil/">de soleil</a> et <a href="{p}lunettes-enfants/">pour enfants</a>.</li>
        <li><a href="{p}lentilles-de-contact/">Lentilles de contact</a> et produits d'entretien.</li>
        <li><a href="{p}lunettes-de-sport/">Lunettes de sport</a> : piscine, vélo, running, tir sportif (Julien est lui-même tireur de compétition).</li>
        <li><a href="{p}lunettes-personnalisees/">Lunettes personnalisées</a>.</li>
        <li><a href="{p}reparation-ajustement-lunettes/">Réparation et ajustement</a> de vos lunettes.</li>
        <li><a href="{p}teleconsultation-ophtalmologie/">Téléconsultation d'ophtalmologie augmentée</a> en magasin, sur rendez-vous.</li>
        <li>Paiement en plusieurs fois, jusqu'à 4 fois.</li>"""
            around = """Nous accueillons les clients du Passage, d'Agen, de Boé, Bon-Encontre, Brax, Colayrac-Saint-Cirq, Estillac,
            Foulayronnes, Pont-du-Casse et Roquefort. Repères : zone commerciale de Lacassagne, à proximité d'Action et de Basic-Fit."""
            img2 = ("passage-mur-montures.jpg", "Mur de montures au magasin du Passage")
            faqs = [("Faut-il prendre rendez-vous au Passage ?",
                     "Vous pouvez passer sans rendez-vous, mais pour un examen de vue, mieux vaut réserver : il demande du temps. "
                     "Avec un rendez-vous, vous êtes pris en charge dès votre arrivée."),
                    ("Peut-on faire une téléconsultation d'ophtalmologie au Passage ?",
                     "Oui. Au Passage, un service de téléconsultation d'ophtalmologie augmentée est disponible en magasin, sur rendez-vous, à partir de 16 ans."),
                    ("Proposez-vous le 100% Santé ?", "Oui, le magasin du Passage le propose pour toute la famille."),
                    ("Où se garer près du magasin ?", "Il y a des places devant le magasin, et le grand parking du Lidl se trouve dans la zone commerciale."),
                    ("Comment venir au magasin en bus ?", "Prenez la ligne 7 du réseau Tempo et descendez à l'arrêt Demi-Lune : le magasin est à 2 minutes à pied.")]

        name_h1 = "à Bias" if is_bias else "au Passage d'Agen"
        parking = store["parking"]
        bus_row = f'<li><span class="k">En bus</span><span>{store["bus"]}</span></li>' if store.get("bus") else ""
        return f"""
{page_hero(p, store['label'], f"Lunettes &amp; Co, votre opticien indépendant {name_h1}", intro,
           store['image'], store['image_alt'], store_buttons(store),
           ("c-blue", "c-orange") if is_bias else ("c-orange", "c-green"))}

<section class="bg-white">
  <div class="wrap two-col">
    <div>
      <h2>{team_title}</h2>
      <p>{team}</p>
      <h3 style="margin-top:2rem">{budget_title}</h3>
      <p>{budget_p}</p>
      <h3 style="margin-top:2rem">{brands_title}</h3>
      <p>{brands_p}</p>
      <h3 style="margin-top:2rem">{craft_title}</h3>
      <p>{craft}</p>
      {badge100(p)}
      <h3 style="margin-top:1rem">Le 100% Santé</h3>
      <p>{sante_p}</p>
    </div>
    <img src="{p}assets/img/{img2[0]}" alt="{img2[1]}" loading="lazy" width="1600" height="1200">
  </div>
</section>

<section style="padding-top:0" class="bg-white">
  <div class="wrap">
    <div class="section-head"><span class="kicker">Le magasin en images</span></div>
    {gallery(p, store)}
    <div class="btn-row" style="margin-top:1.6rem">{ext(store['reviews'], 'Lire nos avis Google', 'btn-ghost')}</div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head"><span class="kicker">Nos services {store['at']}</span><h2>Tout pour vos yeux et vos lunettes</h2></div>
    <div class="two-col" style="align-items:start">
      <ul class="prose">
        {services}
        {extra_service}
      </ul>
      <div class="callout blue"><p>{NOTICE_TELE}</p>
        {ext(store['doctolib'], "Prendre rendez-vous " + store['at'], 'btn-tele btn-sm')}</div>
    </div>
  </div>
</section>

<section class="bg-cream2">
  <div class="wrap two-col" style="align-items:start">
    <div>
      <span class="kicker">Venir au magasin</span>
      <h2>Lunettes &amp; Co, {store['name']}</h2>
      <ul class="info-list">
        <li><span class="k">Adresse</span><span>{store['address']}</span></li>
        <li><span class="k">Téléphone</span><span>{phone_html(store)}</span></li>
        <li><span class="k">Parking</span><span>{parking}</span></li>
        {bus_row}
      </ul>
      <p>{around}</p>
      <div class="btn-row">
        {ext(store['maps'], 'Itinéraire sur Google Maps', 'btn-ghost')}
        {ext(store['opc'], 'Rendez-vous en magasin', 'btn-store')}
      </div>
    </div>
    <div class="card"><h3>Horaires</h3>{hours_table(store)}</div>
  </div>
</section>

{faq_section(p, faqs)}
{cta_end(p, f"À très vite {'à Bias' if is_bias else 'au Passage'}.")}
"""
    return body


# ---------------------------------------------------------------- Téléconsultation
def teleconsultation(p):
    buttons = f"""
<div class="btn-row">
  {ext(PASSAGE['doctolib'], 'Prendre rendez-vous au Passage', 'btn-tele')}
  {ext(BIAS['doctolib'], 'Prendre rendez-vous à Bias', 'btn-tele')}
</div>
<p class="notice">{NOTICE_TELE}</p>
<p class="partner"><img src="{p}assets/img/doctolib.svg" alt="Doctolib" width="110" height="26"><span>Téléconsultation, rendez-vous :</span>
  <a href="{PASSAGE['doctolib']}" target="_blank" rel="noopener">Le Passage</a>
  <a href="{BIAS['doctolib']}" target="_blank" rel="noopener">Bias</a></p>"""
    intro = """<p class="lead">Dans nos magasins du Passage et de Bias, sur rendez-vous, vous passez des examens avec des équipements
    dédiés, puis vous échangez en visioconférence avec un ophtalmologue. Ce service s'adresse aux personnes de 16 ans et plus.</p>"""
    tfaq = [
        ("La téléconsultation remplace-t-elle un rendez-vous chez l'ophtalmologue ?",
         "Non, c'est un service complémentaire. Si vous pouvez obtenir un rendez-vous avec un ophtalmologue, c'est la première option. "
         "La téléconsultation s'adresse aux personnes qui ont des difficultés à obtenir un rendez-vous avec un ophtalmologue."),
        ("Qui peut y accéder ?",
         "Les personnes de 16 ans et plus, sur rendez-vous. Votre opticien vérifie votre éligibilité en magasin."),
        ("Dois-je prendre rendez-vous ?",
         "Oui. Vous réservez en ligne sur Doctolib, pour le magasin de votre choix."),
        ("Mon enfant peut-il faire une téléconsultation ?",
         "Non. Pour un enfant, il faut consulter un ophtalmologue."),
        ("Que dois-je apporter ?", "Votre carte Vitale, votre carte bancaire, vos lunettes actuelles, votre dernière ordonnance."),
        ("Est-ce un service d'urgence ?", "Non. En cas d'urgence, contactez le SAMU au 15."),
        ("Puis-je acheter mes lunettes chez vous après ?",
         "Oui, si vous le souhaitez, notre équipe vous conseille en magasin."),
        ("Combien de temps mon ordonnance de lunettes ou de lentilles est-elle valable ?",
         "Cela dépend de votre âge à la date de l'ordonnance. Lunettes : 1 an avant 16 ans, 5 ans de 16 à 42 ans, "
         "3 ans après 42 ans. Lentilles de contact : 1 an avant 16 ans, 3 ans à partir de 16 ans. "
         "Sauf mention contraire sur l'ordonnance."),
        ("Mon ordonnance est trop ancienne, que faire ?",
         "Pour renouveler vos lunettes, il faut une ordonnance en cours de validité. Si nécessaire, l'ophtalmologue vous "
         "remet une ordonnance à l'issue de la consultation."),
    ]
    return f"""
{page_hero(p, "Service en magasin, sur rendez-vous", "Téléconsultation d'ophtalmologie augmentée, au Passage et à Bias",
           intro, "examen-de-vue.jpg", "Salle d'examen de vue équipée, au magasin du Passage", buttons, ("c-blue", "c-coral"))}

<section class="bg-white">
  <div class="wrap two-col">
    <div>
      <span class="kicker">Le service</span>
      <h2>Qu'est-ce que la téléconsultation augmentée ?</h2>
      <p>Une consultation d'ophtalmologie en visioconférence, complétée par des examens réalisés en magasin, par votre
      opticien ou un professionnel de santé, avec des équipements dédiés. L'ophtalmologiste analyse ces examens et répond
      à vos questions.</p>
    </div>
    <div class="card"><i class="dot c-blue"></i><h3>Un service complémentaire</h3>
      <p>Si vous pouvez obtenir un rendez-vous avec un ophtalmologue, c'est la première option. La téléconsultation
      augmentée s'adresse aux patients qui rencontrent des difficultés à obtenir un rendez-vous avec un ophtalmologue.</p>
      <p><strong>Conditions :</strong> avoir 16 ans ou plus et prendre rendez-vous. Votre opticien vérifie votre éligibilité en magasin.</p></div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head"><span class="kicker">Le parcours</span><h2>Comment ça se passe ?</h2></div>
    <ol class="steps blue">
      <li><strong>Présentez-vous en magasin</strong> : votre opticien vous accueille et vérifie votre éligibilité.</li>
      <li><strong>Vérifiez les disponibilités</strong> : selon les jours de présence des professionnels de santé, renseignez-vous auprès de votre opticien.</li>
      <li><strong>Examen de vue en magasin</strong> : votre opticien ou un professionnel de santé réalise les mesures avec des équipements dédiés.</li>
      <li><strong>Échangez avec l'ophtalmologiste</strong> : il analyse vos examens en visioconférence et répond à vos questions.</li>
      <li><strong>Conclusion de la consultation</strong> : si l'ophtalmologue le juge nécessaire, une ordonnance vous est remise.</li>
    </ol>
  </div>
</section>

<section class="bg-white">
  <div class="wrap grid grid-3">
    <div class="card"><i class="dot c-blue"></i><h3>À apporter</h3><p>Votre carte Vitale, votre carte bancaire, vos lunettes actuelles, votre dernière ordonnance.</p></div>
    <div class="card"><i class="dot c-orange"></i><h3>Adaptée pour</h3><p>Première consultation, renouvellement de lunettes, renouvellement de lentilles.</p></div>
    <div class="card"><i class="dot c-green"></i><h3>Ce que propose la téléconsultation augmentée</h3>
      <p>Un bilan visuel avec des professionnels de santé. Prise en charge Assurance Maladie et mutuelle*.
      Ordonnance si nécessaire, avec renouvellement de lentilles : la décision de prescrire appartient à l'ophtalmologue.
      Un délai moyen indicatif de 6 jours pour obtenir un rendez-vous**.</p></div>
  </div>
  <div class="wrap"><p class="notice" style="margin-top:1.2rem">*Prise en charge par l'Assurance Maladie et la mutuelle selon le niveau de couverture du patient et les conditions de remboursement.
  Nos services sont adaptés aux patients rencontrant des difficultés à obtenir un rendez-vous avec un ophtalmologue.
  Ce n'est pas un service d'urgence : en cas d'urgence, contactez le SAMU au 15.<br>
  **Délai moyen communiqué par notre partenaire de téléconsultation, donné à titre indicatif : il peut varier selon les disponibilités.</p></div>
</section>

<section class="bg-cream2">
  <div class="wrap">
    <div class="section-head"><span class="kicker">Où ?</span><h2>Dans nos deux magasins</h2>
    <p>Renseignez-vous auprès de votre opticien, ou prenez rendez-vous sur Doctolib.</p></div>
    <div class="grid grid-2">
      {''.join(f'''<div class="card"><h3>{s['label']}</h3><p>Lunettes &amp; Co, {s['address']}<br>{phone_html(s)}</p>
        <div class="btn-row" style="margin-top:auto">{ext(s['doctolib'], 'Prendre rendez-vous sur Doctolib', 'btn-tele')}
        <a class="btn btn-ghost" href="{p}{s['page']}">Voir le magasin</a></div></div>''' for s in STORES)}
    </div>
  </div>
</section>

{faq_section(p, tfaq)}
"""


# ---------------------------------------------------------------- Lunettes de vue
def lunettes_vue(p):
    intro = """<p class="lead">Lunettes &amp; Co, opticien indépendant au Passage (près d'Agen) et à Bias (près de
    Villeneuve-sur-Lot), vous aide à choisir des lunettes de vue adaptées à votre correction, à votre confort, à votre style
    et à votre budget. Le 100% Santé est proposé pour toute la famille. Paiement en plusieurs fois, jusqu'à 4 fois.</p>"""
    vfaq = [
        ("Qu'est-ce que le 100% Santé en optique ?", CENT_POUR_CENT),
        ("Puis-je mélanger une monture 100% Santé et des verres à prix libres ?",
         "Oui, il est possible d'associer une monture d'une gamme et des verres de l'autre. En revanche, il n'est pas possible de prendre "
         "des verres de deux gammes différentes."),
        ("Quel budget prévoir pour des lunettes de vue ?",
         "Cela dépend de votre correction, de la monture et des verres choisis, et de votre couverture. Nous vous remettons "
         "un devis gratuit en magasin, avec l'offre 100% Santé et l'offre à tarifs libres. Montures à partir "
         "de 100 euros (hors 100% Santé) ; montures 100% Santé à 30 euros maximum."),
        FAQ_PAY, FAQ_RDV, FAQ_VERRES,
        ("Comment choisir ses lunettes selon la forme de son visage ?",
         
         "Une monture aux lignes arrondies adoucit un visage plutôt anguleux, et une monture aux lignes plus marquées structure un visage plutôt rond. Elle ne doit pas dépasser la largeur du visage, et vos sourcils restent visibles au-dessus. La forme du visage n'est qu'un critère, avec la carnation, la correction, votre style et votre confort : le mieux est de les essayer, notre équipe vous guide."),
    ] + ORDONNANCE_FAQ[:2]
    return f"""
{page_hero(p, "Lunettes de vue", "Lunettes de vue : des montures pour tous les budgets, au Passage et à Bias", intro,
           "vue.jpg", "Monture de vue ronde bicolore verte et bleue, en vitrine", None, ("c-green", "c-coral"))}

<section class="bg-white">
  <div class="wrap">
    <div class="section-head"><span class="kicker">Notre méthode</span><h2>Comment nous choisissons vos lunettes avec vous</h2></div>
    <ol class="steps">
      <li><strong>Nous écoutons votre besoin</strong> : vos lunettes actuelles, l'évolution de votre correction, votre usage au quotidien (travail, écran, conduite, sport, loisirs).</li>
      <li><strong>Nous sélectionnons des montures adaptées</strong> à votre correction, à la forme de votre visage, à votre carnation, à vos goûts et à votre budget, puis nous les essayons ensemble.</li>
      <li><strong>Nous vous conseillons sur les verres</strong> et vous expliquons les options simplement. Pour un premier verre progressif, nous prenons le temps de vous expliquer comment il fonctionne.</li>
      <li><strong>Nous ajustons vos lunettes à votre visage</strong> au moment de la remise, et vous pouvez repasser au magasin quand vous voulez pour un réglage.</li>
    </ol>
  </div>
</section>

<section>
  <div class="wrap two-col">
    <div class="callout">
      {badge100(p)}
      <h2>Le 100% Santé : des lunettes pour toute la famille</h2>
      <p>{CENT_POUR_CENT}</p>
      <p>Nous le proposons dans nos deux magasins. Avant tout achat, nous vous remettons gratuitement un devis détaillé
      avec l'offre 100% Santé et l'offre à tarifs libres, pour comparer.</p>
    </div>
    <div>
      <h2>Des prix accessibles</h2>
      <p>Nos montures démarrent à 100 euros (hors 100% Santé), et les montures 100% Santé sont à 30 euros maximum. Devis gratuit
      en magasin, avec l'offre 100% Santé et l'offre à tarifs libres, pour comparer.</p>
      <h3 style="margin-top:2rem">Pour se faire plaisir : des montures artisanales</h3>
      <p>Loumy, fabriquée à Montauban, et Victoire d'Aqui, fabriquée à Hossegor, dans les Landes, sont des montures artisanales. Bondet et
      Marlone sont elles aussi fabriquées en France. <a href="{p}marques/">Toutes nos marques</a>.</p>
    </div>
  </div>
</section>

<section class="bg-white">
  <div class="wrap two-col">
    <div>
      <h2>Verres unifocaux et progressifs : on vous explique</h2>
      <p>Un verre unifocal corrige la vue à une seule distance. Un verre progressif permet de voir de loin, de près et à
      distance intermédiaire avec les mêmes lunettes. Notre équipe vous conseille le verre qui correspond à votre ordonnance
      et à votre usage au quotidien. Un premier verre progressif demande parfois un peu de temps pour s'y habituer : nous restons
      disponibles pour répondre à vos questions.</p>
      <h3>Traitements et options, selon vos besoins</h3>
      <p>Traitement anti-reflet, verres qui s'éclaircissent et foncent selon la lumière (photochromiques), verres adaptés
      au travail sur écran, verres antifatigue. Nous travaillons avec Mega Optic, verrier français, et Optovision, verrier allemand.</p>
    </div>
    <img src="{p}assets/img/vue-rouge.jpg" alt="Monture de vue rouge oversize posée sur une étagère en bois" loading="lazy" width="1600" height="1200">
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head"><h2>Des lunettes pour chaque usage</h2></div>
    <div class="grid grid-4">
      <a class="card" href="{p}lunettes-de-soleil/"><i class="dot c-orange"></i><h3>Au volant</h3><p>Clips teintés à fixer sur votre monture.</p></a>
      <a class="card" href="{p}lunettes-de-sport/"><i class="dot c-rust"></i><h3>Pour le sport</h3><p>Piscine, vélo, running, tir sportif.</p></a>
      <a class="card" href="{p}lunettes-personnalisees/"><i class="dot c-brown"></i><h3>Personnalisation</h3><p>Une monture à vos couleurs.</p></a>
      <a class="card" href="{p}lunettes-enfants/"><i class="dot c-coral"></i><h3>Enfants et ados</h3><p>Des montures pour tous les âges.</p></a>
    </div>
    <p style="margin-top:1.2rem">Une seule paire pour deux usages ? Les clips aimantés Osmose Clip se fixent sur la monture (dans les deux magasins).</p>
  </div>
</section>

<section class="bg-blue">
  <div class="wrap prose">
    <h2>Votre ordonnance est ancienne, ou vous n'en avez pas ?</h2>
    <p>Pour renouveler vos lunettes, il faut une ordonnance en cours de validité. Selon votre situation, l'ophtalmologue
    peut établir une ordonnance lors d'une téléconsultation en magasin. Nous réalisons aussi des examens de vue en magasin.</p>
    <p><strong>Ce n'est pas un service d'urgence : en cas d'urgence, contactez le SAMU au 15.</strong></p>
    <a class="btn btn-light" href="{p}teleconsultation-ophtalmologie/">La téléconsultation en magasin</a>
  </div>
</section>

{where(p, passage_extra='<p><small>Tavat, Brett, Loumy, Tiwi, French Retro, Marlone, Lool, Matttew, Etnia Barcelona, Chroma by Etnia Barcelona, Lancel, Ray-Ban, Vogue…</small></p>',
       bias_extra="<p><small>Loumy, GIGIstudios, Tiwi, Bondet, Victoire d'Aqui, Etnia Barcelona, Chantal Thomass, Lancel, Lool, Matttew, Vogue, Ray-Ban, Guess…</small></p>")}
{faq_section(p, vfaq)}
{cta_end(p, "Prêt à choisir vos lunettes ?", "Prenez rendez-vous au Passage ou à Bias, ou passez nous voir.")}
"""


# ---------------------------------------------------------------- Lunettes de soleil
def lunettes_soleil(p):
    intro = """<p class="lead">Une forme, une couleur, une teinte de verres : nous vous aidons à choisir des lunettes de soleil qui vous vont bien,
    pour les adultes comme pour les enfants. Avec ou sans correction : nous réalisons aussi vos lunettes de soleil à votre vue.</p>"""
    sfaq = [
        ("Avez-vous des lunettes de soleil pour enfants ?", "Oui, des montures solaires pour les enfants et les adolescents."),
        ("Peut-on avoir des lunettes de soleil à sa vue ?",
         "Oui. Choisissez votre monture et nous vous conseillons sur les verres : teintes classiques de catégorie 3 (une teinte "
         "foncée, adaptée aux journées très lumineuses), verres polarisants, teintes dégradées, traitement miroité en option. "
         "Apportez votre ordonnance en cours de validité."),
        ("Quelle différence entre un clip solaire et un clip pour la conduite de nuit ?",
         "Le clip solaire (teinte de catégorie 3, polarisant) se porte de jour, par temps lumineux : il ne se porte pas la nuit. "
         "Le clip pour la conduite de nuit, à teinte jaune, s'utilise la nuit ou en lumière faible. Leur effet varie selon les "
         "personnes : testez-les avec votre opticien avant de choisir."),
        ("Comment fonctionne un clip ?",
         "Le clip teinté se fixe sur votre monture de vue et se retire facilement. Pour choisir le modèle, passez en magasin : "
         "nous vous conseillons."),
        ("Proposez-vous du Ray-Ban ?", "Oui, dans les deux magasins."),
    ]
    return f"""
{page_hero(p, "Lunettes de soleil", "Lunettes de soleil, avec ou sans correction, au Passage et à Bias", intro,
           "soleil.jpg", "Lunettes de soleil écaille aux verres teintés, sur fond terrazzo", None, ("c-orange", "c-blue"))}

<section class="bg-white">
  <div class="wrap two-col">
    <div>
      <h2>Une monture, une teinte : nous prenons le temps de vous conseiller</h2>
      <p>Les lunettes de soleil sont d'abord une question de style. Nous prenons le temps de vous conseiller : la forme qui
      vous va, la couleur, et la teinte des verres selon votre usage.</p>
      <h3>Des verres de soleil à votre vue</h3>
      <p>Teintes classiques de catégorie 3 (une teinte foncée, adaptée aux journées très lumineuses), verres polarisants,
      teintes dégradées, et traitement miroité en option. Apportez votre ordonnance en cours de validité.</p>
      <h3>Les marques à découvrir</h3>
      <ul class="prose">
        <li><strong>Dans les deux magasins</strong> : Ki ET LA, Ray-Ban, Lancel.</li>
        <li><strong>Au Passage</strong> : French Retro, Brett, Loumy, Tiwi, Vogue, Tavat.</li>
        <li><strong>À Bias</strong> : Guess, Azzaro, Polaroid.</li>
      </ul>
      <p><a href="{p}marques/">Toutes nos marques</a></p>
    </div>
    <img src="{p}assets/img/vitrine.jpg" alt="Vitrine du magasin du Passage avec des lunettes de soleil" loading="lazy" width="1600" height="1200">
  </div>
</section>

<section>
  <div class="wrap two-col">
    <img src="{p}assets/img/osmose-clip.jpg" alt="Montures avec clips solaires sur une étagère" loading="lazy" width="1600" height="1200">
    <div>
      <span class="kicker">Au volant</span>
      <h2>Des clips teintés à fixer sur votre monture</h2>
      <p>Vous portez déjà des lunettes de vue ? Un clip teinté se fixe sur votre monture, sans changer de lunettes.
      Nous proposons deux types de clips, à ne pas confondre : les clips solaires (teinte de catégorie 3, polarisants),
      qui se portent de jour et jamais la nuit, et les clips pour la conduite de nuit (teinte jaune), qui s'utilisent la nuit
      ou en lumière faible.</p>
      <p>L'effet d'une teinte varie selon les personnes : testez le clip avec votre opticien, en magasin, pour vérifier
      qu'il vous convient avant de l'adopter.</p>
    </div>
  </div>
</section>

<section class="bg-cream2">
  <div class="wrap grid grid-2">
    <a class="card" href="{p}lunettes-enfants/"><i class="dot c-coral"></i><h3>Pour les enfants et les adolescents</h3><p>Des montures solaires existent aussi pour les plus jeunes.</p><span class="arrow">Lunettes enfants →</span></a>
    <a class="card" href="{p}lunettes-de-sport/"><i class="dot c-rust"></i><h3>Pour le sport</h3><p>Cyclisme, running, piscine, tir sportif.</p><span class="arrow">Lunettes de sport →</span></a>
  </div>
</section>

{where(p)}
{faq_section(p, sfaq)}
{cta_end(p, "Envie d'essayer ?", "Passez nous voir au Passage ou à Bias, ou prenez rendez-vous.")}
"""


# ---------------------------------------------------------------- Lunettes enfants
def lunettes_enfants(p):
    intro = """<p class="lead">Chez Lunettes &amp; Co, nous avons des lunettes pour tous les âges, des plus petits aux adolescents.
    Le plus important : venir en magasin avec votre enfant, pour les essayer ensemble.</p>"""
    efaq = [
        ("À partir de quel âge peut-on venir choisir des lunettes ?",
         "Nous avons des lunettes pour tous les âges. Venez avec votre enfant : nous vous disons ce qui lui convient."),
        ("Faut-il vraiment amener mon enfant ?",
         "Oui, c'est le plus important. Selon son âge et la forme de son visage, il faut voir que la monture est bien adaptée "
         "et qu'elle couvre bien ses yeux."),
        ("Mon enfant peut-il choisir sa monture ?",
         "Oui, et nous le conseillons : une monture qu'il aime, il la porte plus volontiers. Nous vous aidons à choisir ensemble."),
        ("Le 100% Santé existe-t-il pour les enfants ?",
         "Oui : le 100% Santé concerne toute la famille, enfants compris : monture et verres sans reste à charge avec une "
         "complémentaire santé responsable ou la Complémentaire santé solidaire."),
        ("Combien de temps l'ordonnance de mon enfant est-elle valable ?",
         "Pour les moins de 16 ans, l'ordonnance est valable 1 an : pensez à la renouveler régulièrement. Sauf mention contraire sur l'ordonnance."),
        ("Tous les combien peut-on renouveler les lunettes d'un enfant ?",
         "Pour la prise en charge par l'Assurance Maladie, le renouvellement est possible tous les ans avant 16 ans. Pour les "
         "enfants jusqu'à 6 ans, un renouvellement après 6 mois est prévu si la monture est mal adaptée à la morphologie du "
         "visage. Votre opticien vous renseigne."),
        ("L'ordonnance de mon enfant est trop ancienne. Que faire ?",
         "Il faut une ordonnance en cours de validité. La téléconsultation d'ophtalmologie en magasin n'est possible qu'à "
         "partir de 16 ans : pour un enfant de moins de 16 ans, il faut consulter un ophtalmologue."),
        ("Mon enfant a cassé ses lunettes, pouvez-vous les réparer ?",
         "Oui, comme pour les autres lunettes : passez au magasin nous montrer le souci. Nous regardons si la monture est "
         "réparable et, si besoin, si une pièce peut être commandée."),
        ]
    return f"""
{page_hero(p, "Lunettes enfants", "Lunettes pour enfants : des montures que votre enfant aura envie de porter", intro,
           "enfants.jpg", "Monture enfant colorée à motifs, en présentoir", None, ("c-coral", "c-green"))}

<section class="bg-white">
  <div class="wrap two-col" style="align-items:start">
    <div>
      <h2>Pourquoi venir avec votre enfant ?</h2>
      <p>Un enfant n'est pas un adulte en petit. Selon son âge et la forme de son visage, la taille et la forme de la monture
      ne sont pas les mêmes. Il faut voir, sur lui, que les lunettes sont bien adaptées et qu'elles couvrent bien ses yeux.
      C'est aussi à lui de choisir une monture qu'il aime : il aura envie de la porter.</p>
      <ul class="prose">
        <li><strong>La bonne taille</strong> : ni trop grande, ni trop petite. Les tailles ne dépendent plus seulement de l'âge : il faut essayer.</li>
        <li><strong>Un appui confortable sur le nez</strong> : sur une monture en plastique, il doit être confortable, sans gêne.</li>
        <li><strong>Une monture qui protège bien son regard</strong> : elle monte près des sourcils, pour que l'enfant ne regarde pas par-dessus ses verres.</li>
        <li><strong>Une monture qu'il aime</strong>, pour qu'il la porte volontiers.</li>
      </ul>
    </div>
    <div>
      <h2>Comment ça se passe en magasin</h2>
      <ol class="steps">
        <li>Vous venez avec votre enfant et son ordonnance en cours de validité. Pour l'ordonnance d'un enfant, consultez un ophtalmologue.</li>
        <li>Il essaie plusieurs montures, avec l'aide de l'équipe.</li>
        <li>Nous vérifions ensemble que la monture est bien adaptée à son visage et à ses yeux.</li>
        <li>Nous ajustons la monture à son visage au moment de la remise, puis nous la réajustons quand c'est nécessaire : les enfants grandissent, et les lunettes bougent.</li>
      </ol>
    </div>
  </div>
</section>

<section>
  <div class="wrap two-col">
    <img src="{p}assets/img/enfants-lafont.jpg" alt="Monture enfant Lafont écaille sur présentoir jaune" loading="lazy" width="1600" height="1200">
    <div>
      <h2>Des montures pour tous les âges</h2>
      <p>Des montures de vue et des montures de soleil, pour les petits comme pour les ados.</p>
      <ul class="prose">
        <li><strong>Au Passage</strong> : Lafont Enfant (fabrication française), Ray-Ban, Eleven Paris.</li>
        <li><strong>À Bias</strong> : Ray-Ban Junior, Eleven Paris, Minima Kids, French Retro, Etnia Barcelona, et des montures aux univers de personnages (Stitch, Barbie, Star Wars).</li>
      </ul>
      <p><a href="{p}marques/">Toutes nos marques</a></p>
    </div>
  </div>
</section>

<section class="bg-white">
  <div class="wrap">
    <div class="callout">
      {badge100(p)}
      <h2>Le 100% Santé : pour les enfants aussi</h2>
      <p>{CENT_POUR_CENT} Nous le proposons dans nos deux magasins, avec un choix de montures pour enfants.</p>
      <p>Avant tout achat, nous vous remettons gratuitement un devis détaillé, avec l'offre 100% Santé et l'offre à tarifs libres.
      Montures enfant à partir de 80 euros (hors 100% Santé). Paiement en plusieurs fois, jusqu'à 4 fois.</p>
    </div>
  </div>
</section>

{where(p)}
{faq_section(p, efaq)}
{cta_end(p, "Venez avec votre enfant essayer ses lunettes au Passage ou à Bias.")}
"""


# ---------------------------------------------------------------- Lentilles
def lentilles(p):
    intro = """<p class="lead">Que vous débutiez avec les lentilles ou que vous les portiez déjà, nous sommes là pour vous : adaptation,
    renouvellement, changement de lentilles, conseils d'entretien. Nous vous apprenons aussi à les poser, à les retirer et à les
    entretenir. Les lentilles sont délivrées sur ordonnance.</p>"""
    lfaq = [
        ("Faut-il une ordonnance pour acheter des lentilles de contact ?", "Oui, les lentilles de contact sont délivrées sur ordonnance."),
        ("Combien de temps mon ordonnance de lentilles est-elle valable ?",
         "1 an pour les moins de 16 ans, 3 ans à partir de 16 ans, sauf mention contraire du médecin."),
        ("Mon ordonnance est trop ancienne, que faire ?",
         "Il faut une ordonnance en cours de validité. Selon votre situation, l'ophtalmologue peut établir une nouvelle ordonnance de "
         "lentilles lors d'une téléconsultation d'ophtalmologie en magasin."),
        ("Mon opticien peut-il adapter mes lentilles sans nouvelle ordonnance ?",
         "Dans certains cas, l'opticien peut adapter la correction à partir d'une ordonnance en cours de validité, sauf opposition du médecin."),
        ("Vendez-vous des produits d'entretien pour lentilles ?", "Oui, avec conseil en magasin."),
        ("Les lentilles sont-elles remboursées ?",
         "L'Assurance Maladie les prend en charge dans certains cas précis, sur prescription. Renseignez-vous auprès de votre complémentaire santé."),
        ("Proposez-vous la téléconsultation pour renouveler mes lentilles ?",
         "Oui, à partir de 16 ans, en magasin et sur rendez-vous : l'ophtalmologue décide, selon votre situation, de la "
         "prescription adaptée. Ce n'est pas un service d'urgence : en cas d'urgence, contactez le SAMU au 15."),
    ]
    return f"""
{page_hero(p, "Lentilles de contact", "Lentilles de contact : adaptation, renouvellement et entretien, au Passage et à Bias", intro,
           "lentilles.jpg", "Espace lentilles de contact au magasin du Passage", None, ("c-blue", "c-orange"))}

<section class="bg-white">
  <div class="wrap two-col" style="align-items:start">
    <div>
      <h2>Adaptation et conseil en magasin</h2>
      <p>Vous portez déjà des lentilles et souhaitez les renouveler ou en changer ? Vous débutez ? Notre équipe vous conseille et
      adapte vos lentilles de contact à votre ordonnance. Pour les premiers porteurs, un rendez-vous d'adaptation permet
      d'apprendre à poser, retirer et entretenir ses lentilles. Nous contrôlons ensuite que la lentille convient bien à votre œil,
      puis nous faisons un point de contrôle après une semaine de port.</p>
    </div>
    <div>
      <h2>Renouveler ses lentilles</h2>
      <p>Pour renouveler vos lentilles, il faut une ordonnance en cours de validité. Elle est valable 1 an pour les moins
      de 16 ans et 3 ans à partir de 16 ans, sauf mention contraire du médecin. Si votre ordonnance est trop ancienne,
      l'ophtalmologue peut, selon votre situation, établir une nouvelle ordonnance lors d'une
      <a href="{p}teleconsultation-ophtalmologie/">téléconsultation d'ophtalmologie en magasin</a>.</p>
      <p class="notice">{NOTICE_TELE}</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap grid grid-2">
    <div class="card"><i class="dot c-blue"></i><h3>Produits d'entretien</h3>
      <p>Nous vendons des produits d'entretien et des accessoires pour vos lentilles de contact, avec conseil en magasin.
      Pour vos lunettes : sprays, lingettes et microfibres. Voir aussi <a href="{p}reparation-ajustement-lunettes/">Réparation et ajustement</a>.</p></div>
    <div class="card"><i class="dot c-green"></i><h3>Prix et prise en charge</h3>
      <p>La prise en charge des lentilles par l'Assurance Maladie est prévue dans certains cas précis, sur prescription médicale.
      Renseignez-vous auprès de votre complémentaire santé. Paiement en plusieurs fois, jusqu'à 4 fois, également pour les lentilles.</p></div>
  </div>
</section>

{where(p)}
{faq_section(p, lfaq)}
{cta_end(p, "Une question sur vos lentilles ?", "Passez nous voir au Passage ou à Bias, ou prenez rendez-vous.")}
"""


# ---------------------------------------------------------------- Sport
def sport(p):
    intro = """<p class="lead">Piscine, vélo, running, tir sportif : chaque sport a ses contraintes, et votre correction doit suivre.
    Dites-nous ce que vous pratiquez : nous cherchons la solution qui vous convient, au Passage et à Bias.</p>"""
    spfaq = [
        ("Proposez-vous des lunettes de sport à ma vue ?",
         "Oui : montures et verres adaptés à la pratique sportive, avec votre correction : lunettes de piscine à la vue, "
         "solutions pour le vélo et le running."),
        ("Peut-on avoir des lunettes de piscine à sa vue ?",
         "Oui, avec notre fournisseur Demetz, y compris avec astigmatisme (les lunettes sans astigmatisme sont les plus "
         "abordables). Nous pouvons aussi proposer des masques de plongée à la vue."),
        ("Je pratique le tir sportif : que me proposez-vous ?",
         "Une correction juste en vision de loin et, en magasin, une adaptation de la correction de l'œil de visée à votre discipline, à partir de votre ordonnance."),
    ]
    return f"""
{page_hero(p, "Lunettes de sport", "Des lunettes de sport à votre vue, de la piscine au tir sportif", intro,
           "atelier.jpg", "L'atelier du magasin du Passage, où sont montés et ajustés les verres", None, ("c-rust", "c-blue"))}

<section class="bg-white">
  <div class="wrap">
    <div class="section-head"><h2>Votre sport, votre vue</h2>
    <p>Chaque sport a ses contraintes : l'eau, le vent, la vitesse, la position, le casque. Nous partons de votre pratique,
    de votre correction et de votre confort pour vous proposer des montures et des verres adaptés.</p></div>
    <div class="grid grid-3">
      <div class="card"><i class="dot half c-blue"></i><h3>Piscine</h3><p>Des lunettes de piscine à votre vue, avec notre fournisseur Demetz, qui propose des équipements à la vue avec des montures spécifiques pour de nombreux sports. L'astigmatisme peut être pris en compte. Nous pouvons aussi proposer des masques de plongée à la vue.</p></div>
      <div class="card"><i class="dot half c-orange"></i><h3>Vélo et running</h3><p>Selon les modèles, nous proposons un clip (utile pour les montures très enveloppantes) ou une monture qui s'adapte directement à votre vue, sans les contraintes du clip, comme la buée.</p></div>
      <div class="card"><i class="dot half c-green"></i><h3>Autres sports</h3><p>Parlez-nous de votre pratique : nous cherchons avec vous la solution adaptée, à partir de votre correction.</p></div>
    </div>
  </div>
</section>

<section class="bg-cream2">
  <div class="wrap two-col">
    <div>
      <span class="kicker">Tir sportif</span>
      <h2>Tir sportif : le conseil d'un tireur de compétition</h2>
      <p>Julien pratique le tir sportif depuis l'enfance, en compétition. Plusieurs fois qualifié aux championnats de France, il a été à de nombreuses reprises
      champion départemental et régional. Il tire en discipline ISSF, au pistolet à 10 mètres
      et à 25 mètres. Cette pratique lui permet de comprendre ce que les tireurs attendent de leurs lunettes, quelle que soit
      leur discipline.</p>
      <p>Son conseil aux tireurs : avoir une correction juste en vision de loin (les progressifs sont très rares chez les tireurs).
      En magasin, nous pouvons adapter la correction de l'œil de visée à votre discipline, à partir de votre ordonnance :
      organes de visée nets, cible légèrement plus floue.</p>
      <p>Vous tirez en club ou en compétition ? Prenez rendez-vous en magasin et précisez que c'est pour le tir sportif :
      Julien sera présent lors de votre rendez-vous.</p>
      <div class="btn-row">{ext(PASSAGE['opc'], 'Rendez-vous en magasin : Le Passage', 'btn-store')}
      {ext(BIAS['opc'], 'Rendez-vous en magasin : Bias', 'btn-store')}</div>
    </div>
    <div style="max-width:400px;justify-self:center;width:100%">{pattern(p)}</div>
  </div>
</section>

<section>
  <div class="wrap prose">
    <p>Vous roulez ou vous conduisez avant ou après votre sport ? Voir aussi les clips teintés à fixer sur votre monture,
    page <a href="{p}lunettes-de-soleil/">Lunettes de soleil</a>.</p>
  </div>
</section>

{where(p)}
{faq_section(p, spfaq)}
{cta_end(p, "Parlez-nous de votre sport.", "Passez nous voir au Passage ou à Bias, ou prenez rendez-vous.")}
"""


# ---------------------------------------------------------------- Personnalisation (Loumy)
def sur_mesure(p):
    intro = """<p class="lead">Avec Loumy, lunetier de Montauban et partenaire de nos magasins, vous avez la possibilité de personnaliser
    votre monture : couleurs, effets de matière, choix des branches. Une monture unique, à votre image.</p>"""
    buttons = f"""<div class="btn-row">{ext(PASSAGE['opc'], 'Rendez-vous en magasin : Le Passage', 'btn-store')}
    {ext(BIAS['opc'], 'Rendez-vous en magasin : Bias', 'btn-store')}</div>"""
    mfaq = [
        ("Que veut dire « personnaliser » une monture ?",
         "Choisir les couleurs, les effets de matière et les branches d'une monture Loumy."),
        ("Qui fabrique les montures ?", "Loumy, une marque née à Montauban, créée par Dominique et Aurore Basso."),
        ("La personnalisation est-elle disponible dans les deux magasins ?", "Oui, au Passage et à Bias."),
        ("Puis-je personnaliser une monture avec ma correction ?", "Oui, tous les types de verres sont compatibles."),
    ]
    return f"""
{page_hero(p, "Lunettes personnalisées", "Lunettes personnalisées avec Loumy : une monture à vos couleurs", intro,
           "loumy.jpg", "Monture Loumy bleue et écaille, fabriquée à Montauban", buttons, ("c-brown", "c-coral"))}

<section class="bg-white">
  <div class="wrap">
    <h2>Personnaliser sa monture</h2>
    <p>Tous les modèles Loumy se prêtent à la personnalisation. Vous choisissez les coloris de la face (unis, effets et motifs,
    translucides, associations de couleurs) et les branches, en acétate ou en métal. Votre opticien vous conseille en magasin.</p>
  </div>
</section>

<section class="bg-orange">
  <div class="wrap two-col">
    <div>
      <h2>Loumy, des amis lunetiers à Montauban</h2>
      <p>Loumy a été créée à Montauban par Dominique et Aurore Basso, des amis de Julien depuis ses études d'opticien. Il allait de soi que leurs montures, artisanales, soient dans nos magasins.</p>
      <p><a href="{p}notre-histoire/" style="color:var(--ink)">Notre histoire</a> · <a href="{p}marques/" style="color:var(--ink)">Nos marques</a></p>
    </div>
    <div style="max-width:380px;justify-self:center;width:100%">{pattern(p)}</div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="card"><i class="dot c-green"></i><h3>Pour qui ? Pour quels usages ?</h3>
      <p>La personnalisation Loumy concerne les lunettes de vue pour adultes, avec tous les types de verres, dans nos deux magasins.
      Voir <a href="{p}lunettes-de-vue/">Lunettes de vue</a>.</p></div>
  </div>
</section>

{where(p)}
{faq_section(p, mfaq)}
{cta_end(p, "Envie d'une monture à votre image ?", "Prenez rendez-vous au Passage ou à Bias.")}
"""


# ---------------------------------------------------------------- Réparation
def reparation(p):
    intro = """<p class="lead">Une branche qui bouge, des lunettes qui glissent, une monture abîmée : passez nous voir. Nous réglons,
    ajustons, nettoyons aux ultrasons et réparons vos lunettes. Vos lunettes viennent d'ailleurs ? Nous les réglons ou les
    réparons dans la mesure du possible.</p>"""
    buttons = f"""<div class="btn-row">{ext(PASSAGE['opc'], 'Rendez-vous en magasin : Le Passage', 'btn-store')}
    {ext(BIAS['opc'], 'Rendez-vous en magasin : Bias', 'btn-store')}</div>"""
    rfaq = [
        ("Pouvez-vous régler mes lunettes ?",
         "Oui, y compris pour des lunettes achetées ailleurs, dans la mesure du possible. Passez au "
         "magasin, avec ou sans rendez-vous."),
        ("Mes lunettes sont cassées, pouvez-vous les réparer ?",
         "Cela dépend de la casse : passez nous voir, nous regardons ensemble si la monture est réparable. Branches, plaquettes, "
         "vis, soudures : nous réparons dans la mesure du possible."),
        FAQ_VERRES,
        ("À quoi sert le nettoyage aux ultrasons ?",
         "C'est un nettoyage de vos lunettes dans un bac à ultrasons : principalement pour la monture, avec les verres montés dessus."),
        ("Combien coûte une réparation ?",
         "Une petite réparation est gratuite ; pour une réparation plus importante, le coût "
         "dépend de ce qui est cassé, et les lunettes encore sous garantie sont réparées sans frais, dans les conditions de la "
         "garantie. Passez en magasin, nous vous répondons sur place."),
        ("Réparez-vous les lunettes d'enfant ?",
         "Oui, comme les autres lunettes : passez au magasin nous montrer le souci. Nous regardons si la monture est réparable "
         "et si une pièce peut être commandée."),
    ]
    return f"""
{page_hero(p, "Réparation et ajustement", "Réparation, réglage et nettoyage de vos lunettes, au Passage et à Bias", intro,
           "atelier.jpg", "Atelier de montage et de réparation au magasin du Passage", buttons, ("c-green", "c-orange"))}

<section class="bg-white">
  <div class="wrap">
    <div class="section-head"><h2>Ce que nous faisons</h2></div>
    <div class="grid grid-4">
      <div class="card"><i class="dot c-green"></i><h3>Réglage et ajustement</h3><p>Nous ajustons vos lunettes sur votre visage, au magasin, pour qu'elles soient bien posées.</p></div>
      <div class="card"><i class="dot c-blue"></i><h3>Nettoyage aux ultrasons</h3><p>Un nettoyage de votre monture, que nous passons au bac à ultrasons avec les verres.</p></div>
      <div class="card"><i class="dot c-orange"></i><h3>Réparation</h3><p>Changement de plaquettes, revissage, remplacement de vis perdues, dépannage de branches, soudures sur les montures métalliques classiques (le titane et le plastique injecté ne se soudent pas).</p></div>
      <div class="card"><i class="dot c-coral"></i><h3>Changement de verres</h3><p>Si votre monture est en bon état, nous pouvons simplement changer les verres.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap two-col" style="align-items:start">
    <div>
      <h2>Pourquoi faire régler ses lunettes ?</h2>
      <p>Des lunettes qui glissent, qui serrent ou qui penchent se règlent. Une monture ajustée à votre visage est plus
      confortable à porter au quotidien. Les enfants grandissent et les montures bougent : un réglage régulier est utile.
      Voir aussi <a href="{p}lunettes-enfants/">Lunettes enfants</a>.</p>
      <h2 style="margin-top:2rem">Réparer plutôt que remplacer</h2>
      <p>Quand c'est possible, nous préférons réparer votre monture plutôt que de la remplacer, et changer seulement les verres
      si elle est en bon état. Nous collectons aussi les montures dont vous n'avez plus l'usage : le Lions Club les trie et leur offre une seconde vie.</p>
    </div>
    <div class="callout coral">
      <h3>Prix et délais</h3>
      <p>Une petite réparation est gratuite. Pour une réparation plus
      importante, le coût dépend de ce qui est cassé : nous vous l'indiquons avant de commencer. Les lunettes encore sous
      garantie sont réparées sans frais, dans les conditions de la garantie. Si la réparation est possible tout de suite,
      nous la faisons pendant votre visite ; sinon, le délai dépend de la réception de la pièce.</p>
      <h3>L'entretien au quotidien</h3>
      <p>Sprays, lingettes et microfibres pour l'entretien de vos lunettes sont disponibles en magasin. Pour les lentilles,
      voir <a href="{p}lentilles-de-contact/">Lentilles de contact</a>.</p>
    </div>
  </div>
</section>

{where(p)}
{faq_section(p, rfaq)}
{cta_end(p, "Des lunettes à régler ou à réparer ?", "Passez nous voir au Passage ou à Bias, ou prenez rendez-vous.")}
"""


# ---------------------------------------------------------------- Marques
# Petits drapeaux en SVG : les émojis drapeaux s'affichent en lettres sous Windows.
# Couleurs en style en ligne, car la feuille de style force fill: currentColor sur les rect.
FLAGS = {
    "fr": ("France", '<rect width="3" height="2" style="fill:#ED2939"/><rect width="2" height="2" style="fill:#fff"/><rect width="1" height="2" style="fill:#002395"/>', "0 0 3 2"),
    "it": ("Italie", '<rect width="3" height="2" style="fill:#CE2B37"/><rect width="2" height="2" style="fill:#fff"/><rect width="1" height="2" style="fill:#009246"/>', "0 0 3 2"),
    "be": ("Belgique", '<rect width="3" height="2" style="fill:#EF3340"/><rect width="2" height="2" style="fill:#FDDA24"/><rect width="1" height="2" style="fill:#000"/>', "0 0 3 2"),
    "es": ("Espagne", '<rect width="3" height="2" style="fill:#AA151B"/><rect y=".5" width="3" height="1" style="fill:#F1BF00"/>', "0 0 3 2"),
    "dk": ("Danemark", '<rect width="37" height="28" style="fill:#C8102E"/><rect x="12" width="4" height="28" style="fill:#fff"/><rect y="12" width="37" height="4" style="fill:#fff"/>', "0 0 37 28"),
    "us": ("États-Unis", '<rect width="19" height="10" style="fill:#B22234"/>'
           + "".join(f'<rect y="{y * 2 * 10 / 13:.3f}" width="19" height="{10 / 13:.3f}" style="fill:#fff" transform="translate(0 {10 / 13:.3f})"/>' for y in range(6))
           + '<rect width="7.6" height="5.385" style="fill:#3C3B6E"/>', "0 0 19 10"),
}


def flag(code):
    country, shapes, box = FLAGS[code]
    return (f'<span class="brand-origin"><svg class="flag" viewBox="{box}" preserveAspectRatio="none" aria-hidden="true">{shapes}</svg>'
            f'{country}</span>')


def marques(p):
    stores = {"both": ["passage", "bias"], "passage": ["passage"], "bias": ["bias"]}
    store_names = {"passage": "Le Passage", "bias": "Bias"}
    cat_names = {"vue": "Vue", "soleil": "Soleil", "enfant": "Enfant", "sport": "Sport"}
    items = []
    for name, country, made, desc, url, store, cats, fr in sorted(BRANDS, key=lambda b: b[0].lower()):
        tags = " ".join(cats + ([store] if store != "both" else ["passage", "bias"]) + (["fr"] if fr else []))
        # Magasin en pastilles colorées (information principale), catégories en texte simple
        shops = "".join(f'<span class="shop {s}">{store_names[s]}</span>' for s in stores[store])
        items.append(f'<div class="brand" data-tags="{tags}"><strong>{name}</strong>{flag(country)}'
                     f'{f"<small>{made}</small>" if made else ""}<p>{desc}</p>'
                     f'<div class="brand-meta"><div class="shops">{shops}</div>'
                     f'<span class="cats">{" · ".join(cat_names[c] for c in cats)}</span></div></div>')
    filters = [("all", "Toutes"), ("passage", "Au Passage"), ("bias", "À Bias"), ("vue", "Vue"), ("soleil", "Soleil"),
               ("enfant", "Enfant"), ("fr", "Fabriqué en France")]
    fbtn = "".join(f'<button data-filter="{k}" aria-pressed="{"true" if k == "all" else "false"}">{v}</button>' for k, v in filters)
    return f"""
<section class="page-hero">
  <div class="wrap">
    <span class="kicker">Nos marques</span>
    <h1>Quelle marque, dans quel magasin ? D'un coup d'œil.</h1>
    <p class="lead">Montures de créateurs et de marques, dont plusieurs fabriquées en France. Chaque marque indique le magasin où la trouver : au Passage, à Bias, ou dans les deux.</p>
  </div>
</section>
<section style="padding-top:0">
  <div class="wrap">
    <div class="brand-filter" role="group" aria-label="Filtrer les marques">{fbtn}</div>
    <div class="brands">{''.join(items)}</div>
    <p class="notice" style="margin-top:1.5rem">Les collections évoluent : appelez le magasin pour vérifier qu'un modèle est disponible.
    </p>
    <!-- TODO (Claude Code) : liste à faire relire par Julien (marques par magasin, pays de chaque marque). Voir Site-reference/34-marques-origines-v1.md -->
  </div>
</section>
{cta_end(p, "Venez les essayer au Passage ou à Bias.")}
"""


# ---------------------------------------------------------------- Notre histoire
def histoire(p):
    intro = """<p class="lead"><strong>Un opticien indépendant, un conseil personnalisé, un budget adapté à chacun.</strong>
    Voici comment Lunettes &amp; Co est né à Bias en 2012, et ce qui guide aujourd'hui nos deux magasins.</p>"""
    buttons = f"""<div class="btn-row"><a class="btn btn-ghost" href="{p}{PASSAGE['page']}">Le Passage</a>
    <a class="btn btn-ghost" href="{p}{BIAS['page']}">Bias</a></div>"""
    return f"""
{page_hero(p, "Notre histoire", "Lunettes &amp; Co, des opticiens indépendants à Bias et au Passage", intro,
           "equipe.jpg", "L'équipe Lunettes & Co au magasin du Passage", buttons, ("c-orange", "c-green"))}

<section class="bg-white">
  <div class="wrap two-col" style="align-items:start">
    <div class="prose">
      <h2>Tout a commencé à Bias, en 2012</h2>
      <p>En 2012, Julien ouvre son magasin à Bias, alors Optical Discount, et travaille quelques années au sein d'un réseau
      de franchise. Mais ce qu'il aime dans son métier, c'est choisir : ses marques, les qualités qu'il propose, ce qu'il a
      vraiment envie de conseiller. Il décide de retrouver sa liberté, et Lunettes &amp; Co est né de ce choix. Depuis, beaucoup
      de clients nous sont restés fidèles. Le 31 juillet 2025, un deuxième magasin ouvre au Passage, près d'Agen.</p>
      <h2>Des montures choisies avec soin</h2>
      <p>Chaque monture a sa place chez nous parce qu'elle plaît, qu'elle se porte bien et qu'elle dure. Nous les choisissons
      selon vos goûts, vos envies et ce que nos clients nous racontent depuis plus de 15 ans. Des créateurs aux marques plus
      accessibles, en passant par des griffes comme Lancel ou Azzaro : chez nous, lunettes ne rime pas avec cher. Il y a une
      paire pour chaque budget, et personne n'a peur de pousser la porte.</p>
    </div>
    <div class="prose">
      <h2>Loumy, une histoire d'amitié</h2>
      <p>Dominique, l'un des meilleurs amis de Julien depuis ses études d'opticien, et sa femme Aurore Basso créent des
      lunettes dans leur atelier de Montauban. Des montures originales, artisanales, que l'on peut personnaliser : couleurs,
      effets de matière, branches. Chaque année, de nouvelles collections arrivent, et Loumy a été nommée au Silmo d'Or 2026
      pour son savoir-faire. Il allait de soi qu'elle ait sa place chez nous. La personnalisation est possible dans nos deux
      magasins.</p>
      <h2>Le savoir-faire français, en plus du reste</h2>
      <p>Loumy n'est pas seule : nous proposons une large sélection de montures fabriquées en France, pour valoriser ce
      savoir-faire : Victoire d'Aqui, Bondet, Marlone, Lafont Enfant, et Matttew, une marque belge fabriquée en France.
      L'origine de chaque monture est indiquée sur la page <a href="{p}marques/">Nos marques</a>. Côté verres, nous travaillons
      notamment avec Mega Optic, verrier français titulaire du label Origine France Garantie, et avec Optovision, verrier allemand.</p>
      <h2>Deux magasins, deux caractères</h2>
      <p><strong>Bias</strong> : installé depuis 2012, le magasin connaît bien ses clients, et ils le lui rendent bien. Julien,
      Anne et Francesca y accueillent chaque jour une clientèle fidèle.</p>
      <p><strong>Le Passage</strong> : notre magasin le plus récent, ouvert en juillet 2025. Un cocon chaleureux, avec un grand
      choix de montures pour tous les goûts et tous les budgets.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap grid grid-2">
    <img src="{p}assets/img/bias-accueil.jpg" alt="Le magasin de Bias, mur vert et logo Lunettes & Co" loading="lazy" style="border-radius:var(--radius);aspect-ratio:4/3;object-fit:cover" width="1600" height="1200">
    <img src="{p}assets/img/passage-salon.jpg" alt="Le magasin du Passage, fauteuils et montures" loading="lazy" style="border-radius:var(--radius);aspect-ratio:4/3;object-fit:cover" width="1600" height="1200">
  </div>
</section>

<section class="bg-cream2">
  <div class="wrap grid grid-3">
    <div class="card"><i class="dot c-green"></i><h3>Une démarche éco-responsable, à notre échelle</h3><p>Nous agissons à notre échelle : quasiment pas de plastique dans nos magasins, des sacs et des étuis en kraft. Si votre monture est en bon état, nous changeons seulement les verres. Et nous collectons les montures dont vous n'avez plus l'usage : le Lions Club les trie et leur offre une seconde vie.</p></div>
    <div class="card"><i class="dot c-orange"></i><h3>Pourquoi « Lunettes &amp; Co » ?</h3><p>Un nom simple. « Lunettes », c'est notre métier. « &amp; Co », parce que nous ne faisons pas ce métier seuls. Le « Co » reprend d'abord les premières lettres du nom de famille de Julien. Ce sont aussi les copains, comme Dominique et Aurore, les collections, les collaborations et les clients comblés.</p></div>
    <div class="card"><i class="dot c-blue"></i><h3>Julien, une autre passion : le tir sportif</h3><p>Julien pratique le tir sportif depuis l'enfance, en compétition, au pistolet à 10 et 25 mètres. Plusieurs fois qualifié aux championnats de France, il a été à de nombreuses reprises champion départemental et régional. Une pratique qui l'aide à conseiller les tireurs sur leurs lunettes. <a href="{p}lunettes-de-sport/">Lunettes de sport</a></p></div>
  </div>
</section>

{cta_end(p, "Venez rencontrer l'équipe, à Bias ou au Passage.")}
"""


# ---------------------------------------------------------------- Contact
def contact(p):
    cards = []
    for s in STORES:
        parking = s["parking"] or '<span class="todo">à confirmer</span>'
        extra = "<li><span class=\"k\">Avant</span><span>Anciennement Optical Discount</span></li>" if s is BIAS else \
            "<li><span class=\"k\">Repères</span><span>Zone de Lacassagne, à proximité de Basic-Fit et d'Action</span></li>"
        cards.append(f"""
<div class="card">
  <span class="kicker">{s['near']}</span>
  <h2 style="font-size:1.7rem">Lunettes &amp; Co, {s['name']}</h2>
  <ul class="info-list">
    <li><span class="k">Adresse</span><span>{s['address']}</span></li>
    <li><span class="k">Téléphone</span><span>{phone_html(s)}</span></li>
    <li><span class="k">Parking</span><span>{parking}</span></li>
    {extra}
  </ul>
  {hours_table(s)}
  <div class="btn-row">
    {ext(s['doctolib'], "Téléconsultation d'ophtalmologie", 'btn-tele btn-sm')}
    {ext(s['opc'], 'Rendez-vous en magasin', 'btn-store btn-sm')}
    {ext(s['maps'], 'Itinéraire', 'btn-ghost btn-sm')}
  </div>
</div>""")
    cfaq = [
        ("Quelle est la différence entre le rendez-vous téléconsultation et le rendez-vous en magasin ?",
         "La téléconsultation permet de consulter un ophtalmologue en visioconférence depuis le magasin, sur rendez-vous "
         "(Doctolib). Le rendez-vous en magasin sert aux lunettes, aux lentilles, aux réglages et réparations (réservation "
         "en ligne)."),
        FAQ_RDV,
        ("Que dois-je apporter ?",
         "Pour un conseil lunettes : votre ordonnance et vos lunettes actuelles. Pour la téléconsultation : votre carte Vitale, "
         "votre carte bancaire, vos lunettes actuelles, votre dernière ordonnance."),
        ("Le magasin de Bias s'appelait-il autrement ?", "Oui, il s'appelait Optical Discount avant de devenir Lunettes &amp; Co."),
    ]
    return f"""
<section class="page-hero">
  <div class="wrap">
    <span class="kicker">Contact et rendez-vous</span>
    <h1>Contact et rendez-vous : Le Passage et Bias</h1>
    <p class="lead">Une question, un conseil, un rendez-vous ? Choisissez le magasin le plus proche : Le Passage, près d'Agen,
    ou Bias, près de Villeneuve-sur-Lot. Vous pouvez aussi passer nous voir sans rendez-vous.</p>
    <p>Par e-mail : Le Passage, <a href="mailto:lepassage@lunettesandco.fr">lepassage@lunettesandco.fr</a> · Bias, <a href="mailto:bias@lunettesandco.fr">bias@lunettesandco.fr</a></p>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <h2>Quel rendez-vous choisir ?</h2>
    <div class="grid grid-2">
      <div class="callout blue"><h3>Téléconsultation d'ophtalmologie</h3>
        <p>Voir un ophtalmologue en visioconférence depuis le magasin, sur rendez-vous. Dès 16 ans.</p>
        <p class="notice"><strong>Ce n'est pas un service d'urgence : en cas d'urgence, contactez le SAMU au 15.</strong></p>
        <p class="partner"><img src="{p}assets/img/doctolib.svg" alt="Doctolib" width="110" height="26"><span>Téléconsultation, rendez-vous :</span>
  <a href="{PASSAGE['doctolib']}" target="_blank" rel="noopener">Le Passage</a>
  <a href="{BIAS['doctolib']}" target="_blank" rel="noopener">Bias</a></p>
        <ul class="prose">
          <li><a href="{PASSAGE['doctolib']}" target="_blank" rel="noopener">Téléconsultation d'ophtalmologie : Le Passage</a></li>
          <li><a href="{BIAS['doctolib']}" target="_blank" rel="noopener">Téléconsultation d'ophtalmologie : Bias</a></li>
        </ul></div>
      <div class="callout"><h3>Rendez-vous en magasin</h3>
        <p>Essayer des lunettes, être conseillé, faire régler ou réparer vos lunettes, parler de lentilles.</p>
        <ul class="prose">
          <li><a href="{PASSAGE['opc']}" target="_blank" rel="noopener">Rendez-vous en magasin : Le Passage</a></li>
          <li><a href="{BIAS['opc']}" target="_blank" rel="noopener">Rendez-vous en magasin : Bias</a></li>
        </ul></div>
    </div>
  </div>
</section>

<section class="bg-cream2">
  <div class="wrap grid grid-2">{''.join(cards)}</div>
  <!-- TODO (Claude Code) : horaires à recopier depuis les fiches Google au moment de la publication  ; e-mails du Passage et de Bias confirmés par Karine le 27/10/2026. -->
</section>

{faq_section(p, cfaq)}
"""


# ---------------------------------------------------------------- FAQ
FAQ_GROUPS = [
    ("Nos magasins et les rendez-vous", [
        ("Où sont vos magasins ?",
         "Au Passage, près d'Agen : 64 allée du Loriot, ZAC de Lacassagne, 47520 Le Passage. À Bias, près de Villeneuve-sur-Lot : "
         "centre commercial Auchan (Ponservat), avenue de Bordeaux, 47300 Bias."),
        ("Avez-vous un magasin à Agen ou à Villeneuve-sur-Lot ?",
         "Nos magasins sont au Passage, commune voisine d'Agen, et à Bias, commune voisine de Villeneuve-sur-Lot. Nous accueillons "
         "les clients d'Agen, de Villeneuve-sur-Lot et des communes voisines."),
        ("Êtes-vous une enseigne nationale ?", "Non, nous sommes un opticien indépendant, avec deux magasins en Lot-et-Garonne."),
        FAQ_RDV,
        ("Quelle est la différence entre le rendez-vous téléconsultation et le rendez-vous en magasin ?",
         "La téléconsultation permet de consulter un ophtalmologue en visioconférence depuis le magasin, sur rendez-vous (Doctolib). "
         "Le rendez-vous en magasin sert aux lunettes, aux lentilles, aux réglages et réparations."),
        ("Que dois-je apporter ?",
         "Pour un conseil lunettes : votre ordonnance et vos lunettes actuelles. Pour la téléconsultation : votre carte Vitale, "
         "votre carte bancaire, vos lunettes actuelles, votre dernière ordonnance."),
        ("Où se garer ?", "Au Passage, il y a des places devant le magasin et le grand parking du Lidl dans la zone commerciale. À Bias, le parking du centre commercial Auchan est gratuit, et le magasin est accessible par l'entrée du centre commercial."),
        ("Le magasin de Bias s'appelait-il autrement ?", "Oui. Le magasin de Bias, ouvert en 2012, s'appelait Optical Discount. Il est aujourd'hui un opticien indépendant : Lunettes &amp; Co."),
    ]),
    ("Prix, 100% Santé et paiement", [
        ("Qu'est-ce que le 100% Santé en optique ?", CENT_POUR_CENT),
        ("Proposez-vous le 100% Santé ?", "Oui, dans chaque magasin, pour toute la famille."),
        ("Puis-je mélanger une monture 100% Santé et des verres à prix libres ?",
         "Oui, il est possible d'associer une monture d'une gamme et des verres de l'autre. En revanche, il n'est pas possible de prendre "
         "des verres de deux gammes différentes."),
        ("Quel budget prévoir pour des lunettes de vue ?",
         "Cela dépend de votre correction, de la monture et des verres choisis, et de votre couverture. Nous vous remettons un devis "
         "gratuit en magasin, avec l'offre 100% Santé et l'offre à tarifs libres. Montures à partir de 100 euros (hors 100% Santé) ; "
         "montures 100% Santé à 30 euros maximum."),
        FAQ_PAY,
    ]),
    ("Ordonnance et renouvellement", ORDONNANCE_FAQ + [
        ("Mon ordonnance est trop ancienne, que faire ?",
         "Il faut une ordonnance en cours de validité. Selon votre situation, l'ophtalmologue peut établir une ordonnance lors "
         "d'une téléconsultation d'ophtalmologie en magasin."),
    ]),
    ("Téléconsultation d'ophtalmologie", [
        ("Peut-on consulter un ophtalmologue dans vos magasins ?",
         "Oui, en visioconférence, sur rendez-vous, depuis nos magasins de Bias et du Passage, si votre situation s'y prête. "
         "À partir de 16 ans."),
        ("Est-ce un service d'urgence ?", "Non. En cas d'urgence, contactez le SAMU au 15."),
        ("La téléconsultation remplace-t-elle un rendez-vous chez l'ophtalmologue ?",
         "Non, c'est un service complémentaire. Si vous pouvez obtenir un rendez-vous avec un ophtalmologue, c'est la première option. La téléconsultation s'adresse aux personnes qui ont des difficultés à obtenir un rendez-vous avec un ophtalmologue."),
        ("Puis-je acheter mes lunettes chez vous après ?", "Oui, notre équipe peut vous conseiller en magasin si vous le souhaitez."),
        ("Qui peut faire une téléconsultation d'ophtalmologie ?",
         "Les personnes de 16 ans et plus, sur rendez-vous. Pour un enfant, consultez un ophtalmologue."),
        ("Proposez-vous la téléconsultation pour renouveler mes lentilles ?",
         "Oui, à partir de 16 ans, en magasin et sur rendez-vous : l'ophtalmologue décide, selon votre situation, de la "
         "prescription adaptée."),
    ]),
    ("Lunettes de vue, de soleil, pour enfants et de sport", [
        ("Comment choisir ses lunettes selon la forme de son visage ?", 
         "Une monture aux lignes arrondies adoucit un visage plutôt anguleux, et une monture aux lignes plus marquées structure un visage plutôt rond. Elle ne doit pas dépasser la largeur du visage, et vos sourcils restent visibles au-dessus. La forme du visage n'est qu'un critère, avec la carnation, la correction, votre style et votre confort : le mieux est de les essayer, notre équipe vous guide."),
        FAQ_VERRES,
        ("Peut-on avoir des lunettes de soleil à sa vue ?",
         "Oui. Choisissez votre monture et nous vous conseillons sur les verres et les teintes. Apportez votre ordonnance en cours de validité."),
        ("Faut-il amener mon enfant pour choisir ses lunettes ?",
         "Oui, c'est le plus important. Selon son âge et la forme de son visage, il faut voir que la monture est bien adaptée et "
         "qu'elle couvre bien ses yeux. Il peut aussi choisir sa monture : une monture qu'il aime, il la porte plus volontiers."),
        ("Proposez-vous des lunettes de sport à ma vue ?", "Oui : montures et verres adaptés à la pratique sportive, avec votre correction."),
        ("Quelle différence entre un clip solaire et un clip pour la conduite de nuit ?",
         "Le clip solaire (teinte de catégorie 3, polarisant) se porte de jour et ne se porte pas la nuit. Le clip pour la conduite "
         "de nuit, à teinte jaune, s'utilise la nuit ou en lumière faible. L'effet varie selon les personnes : testez-les avec votre opticien."),
        ("Que veut dire « personnaliser » une monture ?",
         "Avec Loumy, vous pouvez choisir les couleurs, les effets de matière et les branches d'une monture existante. "
         "Votre opticien vous conseille en magasin."),
    ]),
    ("Lentilles de contact", [
        ("Faut-il une ordonnance pour acheter des lentilles de contact ?", "Oui, les lentilles de contact sont délivrées sur ordonnance."),
        ("Vendez-vous des produits d'entretien pour lentilles ?", "Oui, avec conseil en magasin."),
    ]),
    ("Réglages et réparations", [
        ("Pouvez-vous régler mes lunettes ?", "Oui, y compris pour des lunettes achetées ailleurs, dans la mesure du possible."),
        ("Mes lunettes sont cassées, pouvez-vous les réparer ?",
         "Cela dépend de la casse : passez nous voir, nous regardons ensemble si la monture est réparable."),
        ("Combien coûte une réparation ?",
         "Une petite réparation est gratuite. Pour une réparation plus importante, le coût dépend "
         "de ce qui est cassé, et les lunettes encore sous garantie sont réparées sans frais, dans les conditions de la garantie."),
    ]),
]
FAQ_ALL = [qa for _, items in FAQ_GROUPS for qa in items]


def faq_page(p):
    groups = "".join(f'<div class="faq-group"><h2>{t}</h2>{faq(items)}</div>' for t, items in FAQ_GROUPS)
    return f"""
<section class="page-hero">
  <div class="wrap">
    <span class="kicker">Questions fréquentes</span>
    <h1>Questions fréquentes : lunettes, rendez-vous et téléconsultation</h1>
    <p class="lead">Vous avez une question avant de venir ou de prendre rendez-vous ? Voici les réponses les plus fréquentes.
    Une question reste sans réponse ? Appelez-nous ou passez au Passage ou à Bias.</p>
    <div class="btn-row">
      <a class="btn btn-tele" href="{p}teleconsultation-ophtalmologie/" data-open-rdv="tele">Téléconsultation d'ophtalmologie</a>
      <a class="btn btn-store" href="{p}contact-rendez-vous/" data-open-rdv="magasin">Rendez-vous en magasin</a>
      <a class="btn btn-ghost" href="{p}contact-rendez-vous/" data-open-rdv="libre">Passer sans rendez-vous</a>
    </div>
  </div>
</section>
<section style="padding-top:0"><div class="wrap">{groups}</div></section>
"""


# ---------------------------------------------------------------- Pages légales
def mentions(p):
    return """
<section class="page-hero"><div class="wrap prose">
  <h1>Mentions légales</h1>
  <h2>Éditeur du site</h2>
  <p>Le site lunettesandco.fr est édité par Julien Communal, titulaire de la marque Lunettes &amp; Co, directeur général
  des sociétés exploitant les deux magasins :</p>
  <ul>
    <li><strong>JUCOM</strong>, SAS au capital de 1 000 €, magasin du Passage. Siège social : 64 allée du Loriot, ZAC de Lacassagne, 47520 Le Passage.
    SIREN 938 716 347, RCS Agen. N° de TVA intracommunautaire : FR45 938 716 347.</li>
    <li><strong>APCOM</strong>, SAS au capital de 10 000 €, magasin de Bias. Siège social : centre commercial Auchan (Ponservat),
    avenue de Bordeaux, 47300 Bias. SIREN 788 438 653, RCS Agen. N° de TVA intracommunautaire : FR71 788 438 653.</li>
  </ul>
  <p>Directeur de la publication : Julien Communal.</p>
  <p>Contact : <a href="mailto:bias@lunettesandco.fr">bias@lunettesandco.fr</a> · <a href="tel:+33553401996">05 53 40 19 96</a>.</p>
  <h2>Profession réglementée</h2>
  <p>Julien Communal exerce la profession d'opticien-lunetier, titre obtenu en France (diplôme français). Elle est encadrée
  par le Code de la santé publique (livre III, partie IV), consultable sur
  <a href="https://www.legifrance.gouv.fr" rel="noopener">legifrance.gouv.fr</a>.</p>
  <p>Les lunettes sont des dispositifs médicaux, produits de santé réglementés portant, au titre de cette réglementation,
  le marquage CE. Demandez conseil à votre opticien.</p>
  <h2>Médiation de la consommation</h2>
  <p>En cas de litige, vous pouvez d'abord contacter le magasin concerné. Si le désaccord persiste, vous pouvez recourir
  gratuitement au médiateur de la consommation : AME Conso.
  <span class="todo">[adresse postale et site internet à ajouter dès réception des coordonnées]</span>.</p>
  <h2>Hébergement</h2>
  <p>Le site est hébergé par GitHub, Inc. (GitHub Pages), 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis.
  Téléphone : <a href="tel:+33553401996">05 53 40 19 96</a> (magasin de Bias).</p>
  <h2>Propriété intellectuelle</h2>
  <p>La marque Lunettes &amp; Co appartient à Julien Communal (dépôt effectué auprès de l'INPI). La charte graphique et les
  photographies du site sont la propriété de Karine Noirt. Toute reproduction sans autorisation écrite est interdite.</p>
  <h2>Intelligence artificielle et fouille de données</h2>
  <p>En application de l'article L. 122-5-3 du Code de la propriété intellectuelle, les titulaires des droits s'opposent
  à toute fouille de textes et de données sur les contenus de ce site (textes, photographies, charte graphique), en
  particulier pour entraîner ou alimenter des systèmes d'intelligence artificielle, quel que soit leur éditeur (Meta,
  OpenAI, Google, etc.). Cette opposition est aussi exprimée par des procédés lisibles par machine : fichier
  <a href="../robots.txt">robots.txt</a> et protocole TDMRep. Toute utilisation à ces fins nécessite une autorisation écrite préalable.</p>
  <h2>Prise de rendez-vous</h2>
  <p>Les prises de rendez-vous sont assurées par des services tiers : Doctolib (téléconsultation d'ophtalmologie) et
  Opticiens par Conviction (rendez-vous en magasin), selon leurs propres conditions.</p>
</div></section>
"""


def confidentialite(p):
    return """
<section class="page-hero"><div class="wrap prose">
  <h1>Politique de confidentialité</h1>
  <p>Dernière mise à jour : 28 octobre 2026.</p>
  <h2>Qui est responsable de vos données ?</h2>
  <p>Julien Communal, éditeur du site (coordonnées dans les <a href="/mentions-legales/">mentions légales</a>).
  Contact : <a href="mailto:bias@lunettesandco.fr">bias@lunettesandco.fr</a>.</p>
  <h2>Quelles données, pourquoi, combien de temps ?</h2>
  <p>Ce site ne comporte pas de formulaire. Nous ne recueillons directement que :</p>
  <ul>
    <li>les e-mails que vous nous envoyez, pour vous répondre (base légale : votre demande ; conservation :
    3 ans après le dernier échange) ;</li>
    <li>des statistiques de fréquentation anonymisées, si vous acceptez les cookies de mesure d'audience (voir ci-dessous).</li>
  </ul>
  <h2>Cookies et mesure d'audience</h2>
  <p>Un cookie est un petit fichier enregistré sur votre appareil. Nous utilisons Google Analytics pour comprendre
  comment le site est consulté (pages vues, durée, type d'appareil) et l'améliorer. Ces cookies ne sont déposés
  qu'avec votre accord. Vous pouvez le donner, le refuser ou le retirer à tout moment : avec le bandeau
  qui s'affiche lors de votre première visite, puis avec le lien « Gérer mes cookies » en bas de chaque page.
  Refuser n'empêche pas de consulter le site. Votre choix est conservé 6 mois. Les cookies de mesure d'audience
  sont conservés 13 mois au maximum. Les données peuvent être traitées par Google, y compris hors de l'Union européenne.</p>
  <h2>Services tiers</h2>
  <p>Les boutons de rendez-vous et les cartes ouvrent Doctolib, Opticiens par Conviction et Google Maps, qui traitent vos
  données selon leurs propres politiques de confidentialité.
  Le site est hébergé par GitHub, qui enregistre des données techniques de connexion.</p>
  <h2>Vos droits</h2>
  <p>Vous pouvez demander l'accès, la rectification ou l'effacement de vos données, vous opposer à leur traitement ou en
  demander la limitation, en écrivant à <a href="mailto:bias@lunettesandco.fr">bias@lunettesandco.fr</a>.
  Si vous estimez que vos droits ne sont pas respectés, vous pouvez saisir la CNIL
  (<a href="https://www.cnil.fr" rel="noopener">cnil.fr</a>).</p>
</div></section>
"""


PAGES = [
    {"slug": "", "title": "Opticien indépendant en Lot-et-Garonne | Lunettes & Co",
     "description": "Opticien indépendant au Passage, près d'Agen, et à Bias, près de Villeneuve-sur-Lot. Conseil personnalisé, montures dès 100 € (hors 100% Santé).",
     "body": home, "org_ld": True, "faq_ld": HOME_FAQ},
    {"slug": "opticien-le-passage/", "title": "Opticien Le Passage, près d'Agen | Lunettes & Co",
     "description": "Opticien indépendant au Passage, près d'Agen (ZAC de Lacassagne) : lunettes de vue, de soleil, enfants, lentilles et téléconsultation d'ophtalmologie.",
     "body": store_page(PASSAGE)},
    {"slug": "opticien-bias/", "title": "Opticien à Bias, près de Villeneuve-sur-Lot | Lunettes & Co",
     "description": "Opticien indépendant à Bias, près de Villeneuve-sur-Lot et de Sainte-Livrade : lunettes, lentilles, téléconsultation. Ancien Optical Discount.",
     "body": store_page(BIAS)},
    {"slug": "teleconsultation-ophtalmologie/", "title": "Téléconsultation ophtalmologue augmentée | Lunettes & Co",
     "description": "Téléconsultation d'ophtalmologie augmentée : visioconférence avec un ophtalmologue, en magasin à Bias et au Passage, sur rendez-vous. Dès 16 ans.",
     "body": teleconsultation},
    {"slug": "lunettes-de-vue/", "title": "Lunettes de vue près d'Agen et Villeneuve | Lunettes & Co",
     "description": "Lunettes de vue près d'Agen et de Villeneuve-sur-Lot : montures dès 100 euros (hors 100% Santé), verres progressifs.",
     "body": lunettes_vue},
    {"slug": "lunettes-de-soleil/", "title": "Lunettes de soleil, à votre vue ou non | Lunettes & Co",
     "description": "Lunettes de soleil au Passage et à Bias : Ray-Ban, Ki ET LA, Lancel, verres polarisants, solaires à la vue et clips pour la conduite.",
     "body": lunettes_soleil},
    {"slug": "lunettes-enfants/", "title": "Lunettes enfants, pour tous les âges | Lunettes & Co",
     "description": "Lunettes pour enfants au Passage et à Bias : essayage avec votre enfant, montures dès 80 euros (hors 100% Santé), 100% Santé.",
     "body": lunettes_enfants},
    {"slug": "lentilles-de-contact/", "title": "Lentilles de contact et produits d'entretien | Lunettes & Co",
     "description": "Adaptation et renouvellement de lentilles de contact, produits d'entretien, au Passage et à Bias.",
     "body": lentilles},
    {"slug": "lunettes-de-sport/", "title": "Lunettes de sport à la vue, tir sportif | Lunettes & Co",
     "description": "Lunettes de sport à votre vue : piscine, vélo, running, et tir sportif avec Julien, tireur de compétition.",
     "body": sport},
    {"slug": "lunettes-personnalisees/", "title": "Lunettes personnalisées avec Loumy | Lunettes & Co",
     "description": "Personnalisez votre monture Loumy, lunetier de Montauban : couleurs, matières, branches. Au Passage et à Bias, avec le conseil de votre opticien.",
     "body": sur_mesure},
    {"slug": "reparation-ajustement-lunettes/", "title": "Réparation et réglage de lunettes | Lunettes & Co",
     "description": "Réglage, réparation, nettoyage aux ultrasons et changement de verres, au Passage et à Bias.",
     "body": reparation},
    {"slug": "marques/", "title": "Nos marques de lunettes | Lunettes & Co",
     "description": "Loumy, Tavat, Brett, Tiwi, GIGIstudios, Etnia Barcelona, Ray-Ban… Les marques de lunettes disponibles au Passage et à Bias.",
     "body": marques},
    {"slug": "notre-histoire/", "title": "Notre histoire | Lunettes & Co, opticiens indépendants (47)",
     "description": "Julien, opticien depuis plus de 15 ans, vous accueille à Bias et au Passage : conseil personnalisé et montures pour tous les budgets.",
     "body": histoire},
    {"slug": "contact-rendez-vous/", "title": "Contact et rendez-vous | Lunettes & Co",
     "description": "Adresses, téléphones, horaires et prise de rendez-vous des magasins Lunettes & Co au Passage et à Bias.",
     "body": contact},
    {"slug": "faq/", "title": "Questions fréquentes | Lunettes & Co",
     "description": "Rendez-vous, 100% Santé, ordonnance, téléconsultation, lentilles, réparations : les réponses de Lunettes & Co.",
     "body": faq_page, "faq_ld": FAQ_ALL},
    {"slug": "mentions-legales/", "title": "Mentions légales | Lunettes & Co",
     "description": "Mentions légales du site Lunettes & Co.", "body": mentions},
    {"slug": "confidentialite/", "title": "Confidentialité | Lunettes & Co",
     "description": "Politique de confidentialité du site Lunettes & Co.", "body": confidentialite},
]
