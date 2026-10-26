"""Contenu des pages. Textes repris de Site-reference/ (fichiers 14 à 32), notes internes retirées.

Chaque page : slug (dossier), title, description (meta), body(p) où p est le préfixe relatif vers la racine.
"""

from blocks import (FAQ_PAY, FAQ_RDV, FAQ_VERRES, NOTICE_TELE, ORDONNANCE_FAQ, TODO_PHONE, cta_end, ext, faq,
                    faq_section, hours_table, page_hero, pattern, phone_html, products_grid, rdv_buttons,
                    store_buttons, store_card, where)
from site_data import BIAS, BRANDS, PASSAGE, STORES

BADGE_100 = '<span class="badge-slot">Logo 100% Santé à intégrer</span>'

CENT_POUR_CENT = """Le 100% Santé est une sélection de lunettes de vue (monture et verres), intégralement prises en charge
par l'Assurance Maladie et la complémentaire santé. Avec un équipement 100% Santé et une complémentaire santé responsable
(ou la Complémentaire santé solidaire), le reste à charge est nul. Il concerne toute la famille : enfants, femmes et hommes."""


# ---------------------------------------------------------------- Accueil
def home(p):
    store_cards = "".join(store_card(p, s, f'<p>{"Anciennement Optical Discount. " if s is BIAS else ""}'
                                            f'<a href="{s["maps"]}" target="_blank" rel="noopener">Itinéraire</a></p>')
                          for s in STORES)
    return f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="kicker">opticiens indépendants · Lot-et-Garonne</span>
      <h1>Lunettes &amp; Co, opticien indépendant en Lot-et-Garonne : au Passage et à Bias</h1>
      <p class="lead">Des lunettes du quotidien, faciles à vivre, à prix accessible, et des coups de cœur.
      Julien, opticien depuis plus de 15 ans, et son équipe vous aident à trouver des lunettes qui vous ressemblent
      et qui répondent à vos besoins : budget, style, correction, confort, usage.</p>
      {rdv_buttons(p)}
    </div>
    <div class="hero-media">
      <img src="{p}assets/img/passage-magasin.jpg" alt="Le magasin Lunettes & Co au Passage, près d'Agen" width="1600" height="1200">
      <i class="shape s1 c-orange"></i><i class="shape s2 c-blue"></i><i class="shape s3 c-green"></i>
    </div>
  </div>
</section>

<section class="bg-white">
  <div class="wrap">
    <div class="section-head"><span class="kicker">Nos deux magasins</span>
      <h2>Au Passage, près d'Agen, et à Bias, près de Villeneuve-sur-Lot</h2></div>
    <div class="grid grid-2">{store_cards}</div>
  </div>
</section>

<section>
  <div class="wrap two-col">
    <div>
      <span class="kicker">Pourquoi Lunettes &amp; Co</span>
      <h2>Un opticien indépendant, un conseil qui prend le temps</h2>
      <div class="grid" style="gap:1rem">
        <div class="card"><h3>Indépendant</h3><p>Nous ne sommes pas une enseigne nationale. Nous choisissons nos montures avec soin, avec des marques que vous ne trouvez pas partout.</p></div>
        <div class="card"><h3>Un conseil personnalisé</h3><p>On prend le temps de vous écouter, sans pression, pour trouver la monture qui vous ressemble.</p></div>
        <div class="card"><h3>Pour tous les budgets</h3><p>Créateur ne veut pas dire cher : des montures originales à des prix accessibles, et le 100% Santé.</p></div>
      </div>
    </div>
    <img src="{p}assets/img/passage-salon.jpg" alt="Le coin salon du magasin du Passage, fauteuils et présentoirs de montures" loading="lazy" width="1600" height="1200">
  </div>
</section>

<section class="bg-green">
  <div class="wrap two-col">
    <div>
      <span class="kicker" style="color:var(--coral-soft)">Des lunettes pour tous les budgets</span>
      <h2>Créateur ne veut pas dire cher</h2>
      <p>Des montures originales à des prix accessibles : montures hors 100% Santé à partir de 100 euros.
      Et le 100% Santé, pour toute la famille : une sélection de lunettes (monture et verres) avec un reste à charge nul
      avec une complémentaire santé responsable ou la Complémentaire santé solidaire.</p>
      <p>Paiement en plusieurs fois sans frais, jusqu'à 4 fois. Devis gratuit en magasin.</p>
      <div class="btn-row"><a class="btn btn-light" href="{p}lunettes-de-vue/">Lunettes de vue</a>
      <a class="btn btn-light" href="{p}notre-histoire/">Notre histoire</a></div>
    </div>
    <div style="max-width:420px;justify-self:center;width:100%">{pattern()}</div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head"><span class="kicker">Nos services</span><h2>Lunettes, lentilles, réglages : tout se passe en magasin</h2></div>
    {products_grid(p)}
  </div>
</section>

<section class="bg-blue">
  <div class="wrap two-col">
    <div>
      <span class="kicker" style="color:var(--coral)">Téléconsultation d'ophtalmologie</span>
      <h2>Consultez un ophtalmologue depuis nos magasins</h2>
      <p>Besoin d'un bilan visuel ? Chez Lunettes &amp; Co, vous pouvez consulter un ophtalmologue en visioconférence,
      depuis nos magasins de Bias et du Passage, sur rendez-vous.</p>
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
      <h2>Des marques indépendantes, dont plusieurs fabriquées en France</h2>
      <p>Loumy (Montauban), Bondet, Victoire Daqui, Marlone, Lafont Enfant, et aussi Tavat, Brett, Tiwi,
      Etnia Barcelona, Lancel, Ray-Ban et bien d'autres.</p>
      <a class="btn btn-ghost" href="{p}marques/">Voir toutes nos marques</a>
    </div>
  </div>
</section>

<section class="bg-cream2">
  <div class="wrap two-col">
    <div>
      <span class="kicker">Notre histoire</span>
      <h2>Une histoire de famille, d'amis et de montures choisies une à une</h2>
      <p>Lunettes &amp; Co, c'est l'histoire de Julien, opticien depuis plus de 15 ans, qui a voulu retrouver la liberté
      de choisir ses marques. C'est aussi une histoire familiale et de couple, et d'amis qui créent des montures à Montauban.</p>
      <a class="btn btn-ghost" href="{p}notre-histoire/">Découvrir notre histoire</a>
    </div>
    <img src="{p}assets/img/equipe.jpg" alt="L'équipe Lunettes & Co au magasin du Passage" loading="lazy" width="1600" height="1200">
  </div>
</section>

<section class="bg-white">
  <div class="wrap">
    <div class="section-head"><span class="kicker">Avis</span><h2>Ce que disent nos clients</h2>
    <p><span class="todo">Bloc à remplir avec de vrais avis Google (source et date), une fois la collecte par QR code faite.</span></p></div>
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
            intro = """<p class="lead">Lunettes &amp; Co est un opticien indépendant installé à Bias, dans la galerie marchande
            d'Auchan Ponservat, près de Villeneuve-sur-Lot et de Sainte-Livrade-sur-Lot. Julien, opticien depuis plus de 15 ans,
            et son équipe vous conseillent pour trouver des lunettes qui vous ressemblent, à votre budget. Magasin ouvert
            depuis 2012, anciennement Optical Discount.</p>"""
            team_title = "Une équipe chaleureuse, un conseil sur mesure"
            team = """Anne, responsable du magasin, Francesca, apprentie, et Julien vous accueillent sans pression.
            On prend le temps d'écouter votre besoin : confort, esthétique, budget, correction, usage (conduite, sport, écran)."""
            brands = "Loumy (fabriquée à Montauban), GIGIstudios, Tiwi, Bondet, Victoire Daqui, Ray-Ban, Lancel et d'autres"
            extra_service = "<li>Magasin partenaire du réseau de soins Carte Blanche.</li>"
            around = """Nous accueillons aussi les clients de Villeneuve-sur-Lot, de Sainte-Livrade-sur-Lot et des communes voisines."""
            img2 = ("bias-accueil.jpg", "L'accueil du magasin Lunettes & Co à Bias, mur vert et logo")
            faqs = [FAQ_RDV,
                    ("Peut-on faire une téléconsultation d'ophtalmologie à Bias ?", "Oui, sur rendez-vous, en magasin."),
                    ("Proposez-vous le 100% Santé ?", "Oui, dans chaque magasin."),
                    FAQ_VERRES,
                    ("Y a-t-il un parking ?", "Oui, le parking du centre commercial Auchan."),
                    ("Le magasin s'appelait-il autrement ?", "Oui, il s'appelait Optical Discount.")] + ORDONNANCE_FAQ
        else:
            intro = """<p class="lead">Lunettes &amp; Co est un opticien indépendant installé au Passage d'Agen,
            ZAC de Lacassagne, tout près d'Agen. Julien, opticien depuis plus de 15 ans, et son équipe vous conseillent pour
            trouver des lunettes qui vous ressemblent, à votre budget. Le magasin a ouvert le 31 juillet 2025.</p>"""
            team_title = "Un lieu cosy, un conseil sur mesure"
            team = """Au Passage, nous avons imaginé un magasin chaleureux et accessible, à l'image de notre sélection de
            montures. On prend le temps de vous écouter : confort, esthétique, budget, correction, usage (conduite, sport,
            écran). Pas de ton pompeux, pas de pression."""
            brands = ("Loumy (fabriquée à Montauban), Brett, Tavat, Tiwi, French Retro, Marlone, Lafont Enfant, "
                      "Ray-Ban, Lancel et d'autres")
            extra_service = ""
            around = """Nous accueillons les clients du Passage, d'Agen, de Brax, Roquefort, Bon-Encontre, Estillac, Boé,
            Pont-du-Casse, Colayrac-Saint-Cyr et Foulayronnes. Repères : zone de Lacassagne, à proximité de Basic-Fit et d'Action."""
            img2 = ("passage-mur-montures.jpg", "Mur de montures sur fond terrazzo au magasin du Passage")
            faqs = [FAQ_RDV,
                    ("Peut-on faire une téléconsultation d'ophtalmologie au Passage ?", "Oui, sur rendez-vous, en magasin."),
                    ("Proposez-vous le 100% Santé ?", "Oui, dans chaque magasin."),
                    FAQ_VERRES] + ORDONNANCE_FAQ

        name_h1 = "à Bias" if is_bias else "au Passage d'Agen"
        parking = store["parking"] or '<span class="todo">à confirmer</span>'
        return f"""
{page_hero(p, store['label'], f"Lunettes &amp; Co, votre opticien indépendant {name_h1}", intro,
           store['image'], store['image_alt'], store_buttons(store),
           ("c-blue", "c-orange") if is_bias else ("c-orange", "c-green"))}

<section class="bg-white">
  <div class="wrap two-col">
    <div>
      <h2>{team_title}</h2>
      <p>{team}</p>
      <h3 style="margin-top:2rem">Des montures pour tous les budgets</h3>
      <p>Des montures originales à des prix accessibles : montures à partir de 100 euros, le 100% Santé et, si vous voulez
      vous faire plaisir, des montures faites à la main, presque des pièces uniques. Marques à découvrir : {brands}.
      <a href="{p}marques/">Toutes nos marques</a>.</p>
    </div>
    <img src="{p}assets/img/{img2[0]}" alt="{img2[1]}" loading="lazy" width="1600" height="1200">
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head"><span class="kicker">Nos services à {store['name']}</span><h2>Tout pour vos yeux et vos lunettes</h2></div>
    <div class="two-col" style="align-items:start">
      <ul class="prose">
        <li><a href="{p}lunettes-de-vue/">Lunettes de vue</a>, <a href="{p}lunettes-de-soleil/">de soleil</a> et <a href="{p}lunettes-enfants/">pour enfants</a>.</li>
        <li><a href="{p}lentilles-de-contact/">Lentilles de contact</a> et produits d'entretien.</li>
        <li><a href="{p}lunettes-de-sport/">Lunettes de sport</a> : piscine, vélo, running, tir sportif (Julien est lui-même tireur de compétition).</li>
        <li><a href="{p}lunettes-sur-mesure/">Lunettes sur mesure</a> avec Loumy.</li>
        <li><a href="{p}reparation-ajustement-lunettes/">Réparation et ajustement</a> de vos lunettes.</li>
        <li><a href="{p}teleconsultation-ophtalmologie/">Téléconsultation d'ophtalmologie</a> en magasin, sur rendez-vous.</li>
        <li>Paiement en plusieurs fois sans frais (jusqu'à 4 fois).</li>
        {extra_service}
      </ul>
      <div class="callout blue"><p>{NOTICE_TELE}</p>
        {ext(store['doctolib'], "Téléconsultation à " + store['name'], 'btn-tele btn-sm')}</div>
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
      </ul>
      <p>{around}</p>
      <div class="btn-row">
        {ext(store['maps'], 'Itinéraire sur Google Maps', 'btn-ghost')}
        {ext(store['opc'], 'Rendez-vous en magasin', 'btn-store')}
      </div>
    </div>
    <div class="card"><h3>Horaires</h3>{hours_table(store)}
      <p class="notice" style="margin-top:.8rem"><span class="todo">Horaires provisoires, à recopier depuis la fiche Google.</span></p></div>
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
<span class="badge-slot">Logo Doctolib à intégrer</span>"""
    intro = """<p class="lead">Besoin d'un bilan visuel ? Entrez et téléconsultez. Chez Lunettes &amp; Co, vous pouvez
    consulter un ophtalmologue en visioconférence, depuis nos magasins de Bias et du Passage, sur rendez-vous.
    Délai moyen pour un rendez-vous : 6 jours.</p>"""
    tfaq = [
        ("La téléconsultation remplace-t-elle un rendez-vous chez l'ophtalmologue ?",
         "Elle s'adresse notamment aux personnes qui peinent à obtenir un rendez-vous avec un ophtalmologue."),
        ("Dois-je prendre rendez-vous ?", "Oui, sur rendez-vous, via Doctolib."),
        ("Mon enfant peut-il faire une téléconsultation ?",
         "Non : la téléconsultation d'ophtalmologie en magasin est possible à partir de 16 ans. Pour un enfant de moins de "
         "16 ans, il faut consulter un ophtalmologue."),
        ("Que dois-je apporter ?", "Votre carte Vitale, votre carte bancaire, vos lunettes actuelles, votre dernière ordonnance."),
        ("Est-ce un service d'urgence ?", "Non. En cas d'urgence, contactez le SAMU au 15."),
        ("Puis-je acheter mes lunettes chez vous après ?", "Oui, notre équipe peut vous conseiller en magasin si vous le souhaitez."),
        ("Combien de temps mon ordonnance de lunettes ou de lentilles est-elle valable ?",
         "Cela dépend de votre âge au moment où l'ordonnance a été établie. Moins de 16 ans : 1 an. De 16 à 42 ans : 5 ans. "
         "Plus de 42 ans : 3 ans. Le médecin peut réduire cette durée par une mention sur l'ordonnance."),
        ("Mon ordonnance est trop ancienne, que faire ?",
         "Pour renouveler vos lunettes, il faut une ordonnance en cours de validité. Une téléconsultation d'ophtalmologie "
         "en magasin peut vous permettre d'en obtenir une, si votre situation s'y prête."),
    ]
    return f"""
{page_hero(p, "Service en magasin, sur rendez-vous", "Téléconsultation d'ophtalmologie en magasin, à Bias et au Passage",
           intro, "examen-de-vue.jpg", "Salle d'examen de vue équipée, au magasin du Passage", buttons, ("c-blue", "c-coral"))}

<section class="bg-white">
  <div class="wrap">
    <div class="section-head"><span class="kicker">Le parcours</span><h2>Comment ça se passe ?</h2></div>
    <ol class="steps blue">
      <li><strong>Présentez-vous en magasin</strong> : votre opticien vous accueille et vérifie votre éligibilité.</li>
      <li><strong>Vérifiez les disponibilités</strong> : selon les jours de présence des professionnels de santé, renseignez-vous auprès de votre opticien.</li>
      <li><strong>Examen de vue en magasin</strong> : votre opticien ou un professionnel de santé réalise les mesures avec des équipements dédiés.</li>
      <li><strong>Échangez avec l'ophtalmologiste</strong> : il analyse vos examens en visioconférence et répond à vos questions.</li>
      <li><strong>Repartez sereinement</strong> : si nécessaire, une ordonnance vous est remise à l'issue de la consultation.</li>
    </ol>
  </div>
</section>

<section>
  <div class="wrap grid grid-3">
    <div class="card"><i class="dot c-blue"></i><h3>À apporter</h3><p>Votre carte Vitale, votre carte bancaire, vos lunettes actuelles, votre dernière ordonnance.</p></div>
    <div class="card"><i class="dot c-orange"></i><h3>Adaptée pour</h3><p>Première consultation, renouvellement de lunettes, renouvellement de lentilles. Réservée aux personnes de 16 ans et plus.</p></div>
    <div class="card"><i class="dot c-green"></i><h3>Ce que propose la téléconsultation augmentée</h3>
      <p>Un bilan visuel avec des professionnels de santé. Prise en charge Assurance Maladie et mutuelle*. Ordonnance si nécessaire, avec renouvellement de lentilles. Un délai moyen de 6 jours pour obtenir un rendez-vous.</p></div>
  </div>
  <div class="wrap"><p class="notice" style="margin-top:1.2rem">*Prise en charge par l'Assurance Maladie et la mutuelle selon le niveau de couverture du patient.
  Nos services sont adaptés aux patients rencontrant des difficultés à obtenir un rendez-vous avec un ophtalmologue.
  Ce n'est pas un service d'urgence : en cas d'urgence, contactez le SAMU au 15.</p></div>
</section>

<section class="bg-cream2">
  <div class="wrap">
    <div class="section-head"><span class="kicker">Où ?</span><h2>Dans nos deux magasins</h2></div>
    <div class="grid grid-2">
      {''.join(f'''<div class="card"><h3>{s['label']}</h3><p>Lunettes &amp; Co, {s['address']}</p>
        <div class="btn-row" style="margin-top:auto">{ext(s['doctolib'], 'Prendre rendez-vous sur Doctolib', 'btn-tele')}</div></div>''' for s in STORES)}
    </div>
  </div>
</section>

{faq_section(p, tfaq)}
"""


# ---------------------------------------------------------------- Lunettes de vue
def lunettes_vue(p):
    intro = """<p class="lead">Chez Lunettes &amp; Co, opticien indépendant au Passage (près d'Agen) et à Bias (près de
    Villeneuve-sur-Lot), nous vous aidons à choisir des lunettes de vue qui vous ressemblent et qui répondent à votre besoin :
    correction, confort, style, budget. Des lunettes pour tous les budgets, dont le 100% Santé pour toute la famille,
    et le paiement en plusieurs fois sans frais.</p>"""
    vfaq = [
        ("Qu'est-ce que le 100% Santé en optique ?", CENT_POUR_CENT),
        ("Puis-je mélanger une monture 100% Santé et des verres à prix libres ?",
         "Oui, il est possible d'associer une monture d'une gamme et des verres de l'autre. En revanche, on ne peut pas "
         "prendre des verres de deux gammes différentes."),
        ("Quel budget prévoir pour des lunettes de vue ?",
         "Cela dépend de votre correction, de la monture et des verres choisis, et de votre couverture. Nous vous remettons "
         "un devis gratuit en magasin, avec l'offre 100% Santé et l'offre à tarifs libres. Montures hors 100% Santé à partir "
         "de 100 euros ; montures 100% Santé à 30 euros maximum."),
        FAQ_PAY, FAQ_RDV, FAQ_VERRES,
        ("Comment choisir ses lunettes selon la forme de son visage ?",
         "Venez les essayer : c'est le plus simple, et notre équipe vous guide."),
    ] + ORDONNANCE_FAQ[:2]
    return f"""
{page_hero(p, "Lunettes de vue", "Lunettes de vue : des montures qui vous ressemblent, au Passage et à Bias", intro,
           "vue.jpg", "Monture de vue ronde bicolore verte et bleue, en vitrine", None, ("c-green", "c-coral"))}

<section class="bg-white">
  <div class="wrap">
    <div class="section-head"><span class="kicker">Notre méthode</span><h2>Comment nous choisissons vos lunettes avec vous</h2></div>
    <ol class="steps">
      <li><strong>On écoute votre besoin</strong> : portez-vous déjà des lunettes, quelle était votre correction et comment elle a évolué, quel usage (loisirs, travail, écran, conduite, sport), vos postures, un équipement spécifique si besoin.</li>
      <li><strong>On sélectionne des montures adaptées</strong> à votre correction, à la forme de votre visage, à votre carnation, à vos goûts et à votre budget, et on les essaie ensemble.</li>
      <li><strong>On vous conseille sur les verres</strong>, en vous expliquant les options simplement (premier verre progressif : on vous explique son fonctionnement), avec la prise de mesures.</li>
      <li><strong>On règle vos lunettes à la remise</strong>, et vous repassez au magasin quand vous voulez pour un réglage.</li>
    </ol>
  </div>
</section>

<section>
  <div class="wrap two-col">
    <div class="callout">
      {BADGE_100}
      <h2>Le 100% Santé : des lunettes pour toute la famille</h2>
      <p>{CENT_POUR_CENT}</p>
      <p>Nous le proposons dans nos deux magasins. Avant tout achat, nous vous remettons gratuitement un devis détaillé
      avec l'offre 100% Santé et l'offre à tarifs libres, pour comparer.</p>
    </div>
    <div>
      <h2>Des montures pour tous les budgets</h2>
      <p>Des montures originales à des prix accessibles et, si vous voulez vous faire plaisir, des montures faites à la main,
      presque des pièces uniques. Montures hors 100% Santé à partir de 100 euros, montures 100% Santé à 30 euros maximum.
      Devis gratuit en magasin.</p>
      <p>Plusieurs marques que nous proposons sont fabriquées en France : Loumy (Montauban), Bondet et Victoire Daqui à Bias,
      Marlone au Passage. <a href="{p}marques/">Toutes nos marques</a>.</p>
    </div>
  </div>
</section>

<section class="bg-white">
  <div class="wrap two-col">
    <div>
      <h2>Verres unifocaux et progressifs : on vous explique</h2>
      <p>Un verre unifocal corrige la vue à une seule distance. Un verre progressif permet de voir de loin, de près et à
      distance intermédiaire avec les mêmes lunettes. Notre équipe vous conseille le verre qui correspond à votre ordonnance
      et à votre usage au quotidien. Les verres progressifs demandent parfois un temps d'adaptation : nous restons disponibles
      pour en parler.</p>
      <h3>Traitements et options, selon vos besoins</h3>
      <p>Traitement anti-reflet, filtres contre la lumière bleue pour le travail sur écran, verres qui s'éclaircissent et
      foncent selon la lumière (photochromiques), verres antifatigue, verres spécifiques pour le travail sur écran. Nous
      travaillons avec Méga Optic, verrier français.</p>
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
      <a class="card" href="{p}lunettes-sur-mesure/"><i class="dot c-brown"></i><h3>Sur mesure</h3><p>Une monture unique, faite pour vous.</p></a>
      <a class="card" href="{p}lunettes-enfants/"><i class="dot c-coral"></i><h3>Enfants et ados</h3><p>Des montures pour tous les âges.</p></a>
    </div>
    <p style="margin-top:1.2rem">Une seule paire pour deux usages ? Les clips aimantés Osmose Clip se fixent sur la monture (dans les deux magasins).</p>
  </div>
</section>

<section class="bg-blue">
  <div class="wrap prose">
    <h2>Votre ordonnance est ancienne, ou vous n'en avez pas ?</h2>
    <p>Pour renouveler vos lunettes, il faut une ordonnance en cours de validité. Une téléconsultation d'ophtalmologie en
    magasin peut vous permettre d'en obtenir une, si votre situation s'y prête. Nous réalisons aussi des examens de vue en magasin.</p>
    <p><strong>Ce n'est pas un service d'urgence : en cas d'urgence, contactez le SAMU au 15.</strong></p>
    <a class="btn btn-light" href="{p}teleconsultation-ophtalmologie/">La téléconsultation en magasin</a>
  </div>
</section>

{where(p, passage_extra='<p><small>Tavat, Brett, Loumy, Tiwi, French Retro, Marlone, Lool, Matttew, Etnia Barcelona, Chroma by Etnia Barcelona, Lancel, Ray-Ban, Vogue…</small></p>',
       bias_extra='<p><small>Loumy, GIGIstudios, Tiwi, Bondet, Victoire Daqui, Etnia Barcelona, Chantal Thomass, Lancel, Lool, Matttew, Vogue, Ray-Ban, Guess…</small></p>')}
{faq_section(p, vfaq)}
{cta_end(p, "Prêt à choisir vos lunettes ?", "Prenez rendez-vous au Passage ou à Bias, ou passez nous voir.")}
"""


# ---------------------------------------------------------------- Lunettes de soleil
def lunettes_soleil(p):
    intro = """<p class="lead">Nous vous conseillons pour choisir des lunettes de soleil qui vous vont bien : forme, couleur,
    teinte des verres, confort. Pour les adultes comme pour les enfants. Vous avez besoin d'une correction ? Nous réalisons
    aussi vos lunettes de soleil à votre vue : teintes classiques de catégorie 3, verres polarisants, teintes dégradées,
    et traitement miroité en option.</p>"""
    sfaq = [
        ("Avez-vous des lunettes de soleil pour enfants ?", "Oui, des montures solaires pour les enfants et les adolescents."),
        ("Peut-on avoir des lunettes de soleil à sa vue ?",
         "Oui. Choisissez votre monture et nous vous conseillons sur les verres : teintes classiques de catégorie 3, verres "
         "polarisants, teintes dégradées, traitement miroité en option. Apportez votre ordonnance en cours de validité."),
        ("Comment fonctionne un clip pour la conduite ?",
         "Le clip teinté se fixe sur votre monture de vue et se retire facilement. Pour choisir le modèle, passez en magasin : "
         "nous vous conseillons."),
        ("Proposez-vous du Ray-Ban ?", "Oui, dans les deux magasins."),
        FAQ_RDV, FAQ_PAY,
    ]
    return f"""
{page_hero(p, "Lunettes de soleil", "Lunettes de soleil : trouvez celles qui vous ressemblent, au Passage et à Bias", intro,
           "soleil.jpg", "Lunettes de soleil écaille aux verres teintés, sur fond terrazzo", None, ("c-orange", "c-blue"))}

<section class="bg-white">
  <div class="wrap two-col">
    <div>
      <h2>Une monture, une teinte : on choisit avec vous</h2>
      <p>Les lunettes de soleil sont d'abord une question de style, et on le prend au sérieux. Nous vous aidons à choisir
      la forme qui vous va, la couleur, et la teinte des verres selon l'usage que vous en faites.</p>
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
      Nous proposons des clips solaires (teinte de catégorie 3, polarisants) et des clips pour la conduite de nuit
      (teintes jaunes). Nous vous conseillons en magasin.</p>
      <p>Vous aimez l'idée d'une seule paire pour deux usages ? Les clips aimantés Osmose Clip se fixent sur la monture
      (dans les deux magasins).</p>
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
    intro = """<p class="lead">Chez Lunettes &amp; Co, nous avons des lunettes pour tous les âges et pour tous les enfants,
    des plus petits aux adolescents. Le plus important : venir en magasin avec votre enfant pour les essayer.</p>"""
    efaq = [
        ("À partir de quel âge peut-on venir choisir des lunettes ?",
         "Nous avons des lunettes pour tous les âges. Venez avec votre enfant : nous vous disons ce qui lui convient."),
        ("Faut-il vraiment amener mon enfant ?",
         "Oui, c'est le plus important. Selon son âge et la forme de son visage, il faut voir que la monture est bien adaptée "
         "et qu'elle couvre bien ses yeux."),
        ("Mon enfant peut-il choisir sa monture ?",
         "Oui, et nous le conseillons : une monture qu'il aime, il la porte plus volontiers. Nous vous aidons à choisir ensemble."),
        ("Le 100% Santé existe-t-il pour les enfants ?",
         "Oui : le 100% Santé concerne toute la famille. Avec un équipement 100% Santé et une complémentaire santé responsable "
         "(ou la Complémentaire santé solidaire), le reste à charge est nul."),
        ("Combien de temps l'ordonnance de mon enfant est-elle valable ?",
         "Pour les moins de 16 ans, l'ordonnance est valable 1 an : pensez à la renouveler régulièrement. Le médecin peut réduire cette durée."),
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
        FAQ_PAY, FAQ_RDV,
    ]
    return f"""
{page_hero(p, "Lunettes enfants", "Lunettes pour enfants : pour tous les âges, à essayer en magasin", intro,
           "enfants.jpg", "Monture enfant colorée à motifs, en présentoir", None, ("c-coral", "c-green"))}

<section class="bg-white">
  <div class="wrap two-col" style="align-items:start">
    <div>
      <h2>Pourquoi venir avec votre enfant ?</h2>
      <p>Un enfant n'est pas un adulte en petit. Selon son âge et la forme de son visage, la taille et la forme de la monture
      ne sont pas les mêmes. Il faut voir, sur lui, que les lunettes sont bien adaptées et qu'elles couvrent bien ses yeux.
      C'est aussi à lui de choisir une monture qu'il aime : il aura envie de la porter.</p>
      <ul class="prose">
        <li><strong>La bonne taille</strong> : ni trop grande, ni trop petite pour son visage. Les tailles ne dépendent plus seulement de l'âge : il faut essayer.</li>
        <li><strong>Un bon appui</strong> : pour une monture plastique, elle se pose bien sur le nez, sans lui faire mal.</li>
        <li><strong>Une bonne couverture</strong> : la monture monte jusqu'aux sourcils, pour que l'enfant ne regarde pas par-dessus ses verres.</li>
        <li><strong>Une monture qu'il aime</strong>, pour qu'il la porte volontiers.</li>
      </ul>
    </div>
    <div>
      <h2>Comment ça se passe en magasin</h2>
      <ol class="steps">
        <li>Vous venez avec votre enfant et son ordonnance en cours de validité.</li>
        <li>Il essaie plusieurs montures, avec l'aide de l'équipe.</li>
        <li>On vérifie ensemble que la monture est bien adaptée à son visage et à ses yeux.</li>
        <li>On règle la monture à la remise, et on la réajuste quand c'est nécessaire : les enfants grandissent, et les lunettes bougent.</li>
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
      {BADGE_100}
      <h2>Le 100% Santé : pour les enfants aussi</h2>
      <p>{CENT_POUR_CENT} Nous le proposons dans nos deux magasins, avec un choix de montures pour enfants.</p>
      <p>Avant tout achat, nous vous remettons gratuitement un devis détaillé, avec l'offre 100% Santé et l'offre à tarifs libres.
      Montures enfant hors 100% Santé à partir de 80 euros. Paiement en plusieurs fois sans frais, jusqu'à 4 fois.</p>
    </div>
  </div>
</section>

{where(p)}
{faq_section(p, efaq)}
{cta_end(p, "Venez avec votre enfant essayer ses lunettes au Passage ou à Bias.")}
"""


# ---------------------------------------------------------------- Lentilles
def lentilles(p):
    intro = """<p class="lead">Nous vous conseillons pour vos lentilles de contact : adaptation, renouvellement, produits
    d'entretien. Les lentilles sont délivrées sur ordonnance.</p>"""
    lfaq = [
        ("Faut-il une ordonnance pour acheter des lentilles de contact ?", "Oui, les lentilles de contact sont délivrées sur ordonnance."),
        ("Combien de temps mon ordonnance de lentilles est-elle valable ?",
         "1 an pour les moins de 16 ans, 3 ans à partir de 16 ans, sauf mention contraire du médecin."),
        ("Mon ordonnance est trop ancienne, que faire ?",
         "Il faut une ordonnance en cours de validité. Une téléconsultation d'ophtalmologie en magasin peut permettre de "
         "renouveler votre ordonnance de lentilles, si votre situation s'y prête."),
        ("Mon opticien peut-il adapter mes lentilles sans nouvelle ordonnance ?",
         "Dans certains cas, l'opticien peut adapter la correction à partir d'une ordonnance en cours de validité, sauf opposition du médecin."),
        ("Vendez-vous des produits d'entretien pour lentilles ?", "Oui, avec conseil en magasin."),
        ("Les lentilles sont-elles remboursées ?",
         "L'Assurance Maladie les prend en charge dans certains cas précis, sur prescription. Renseignez-vous auprès de votre complémentaire santé."),
        ("Proposez-vous la téléconsultation pour renouveler mes lentilles ?",
         "Oui, à partir de 16 ans, en magasin et sur rendez-vous, si votre situation s'y prête. Ce n'est pas un service "
         "d'urgence : en cas d'urgence, contactez le SAMU au 15."),
        FAQ_RDV,
    ]
    return f"""
{page_hero(p, "Lentilles de contact", "Lentilles de contact : conseil, adaptation et produits d'entretien", intro,
           "lentilles.jpg", "Espace lentilles de contact au magasin du Passage", None, ("c-blue", "c-orange"))}

<section class="bg-white">
  <div class="wrap two-col" style="align-items:start">
    <div>
      <h2>Adaptation et conseil en magasin</h2>
      <p>Vous débutez avec les lentilles, ou vous voulez en changer ? Notre équipe vous conseille et adapte vos lentilles
      de contact à votre ordonnance. Pour les premiers porteurs, un rendez-vous d'adaptation suffit en général : on vous
      apprend à mettre vos lentilles, à les enlever et à les entretenir. Nous contrôlons ensuite que la lentille convient
      bien à votre œil, puis nous faisons un point de contrôle après une semaine de port.</p>
    </div>
    <div>
      <h2>Renouveler ses lentilles</h2>
      <p>Pour renouveler vos lentilles, il faut une ordonnance en cours de validité. Elle est valable 1 an pour les moins
      de 16 ans et 3 ans à partir de 16 ans, sauf mention contraire du médecin. Si votre ordonnance est trop ancienne,
      une <a href="{p}teleconsultation-ophtalmologie/">téléconsultation d'ophtalmologie en magasin</a> peut permettre de
      la renouveler, si votre situation s'y prête.</p>
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
      Renseignez-vous auprès de votre complémentaire santé. Paiement en plusieurs fois sans frais, jusqu'à 4 fois, également pour les lentilles.</p></div>
  </div>
</section>

{where(p)}
{faq_section(p, lfaq)}
{cta_end(p, "Une question sur vos lentilles ?", "Passez nous voir au Passage ou à Bias, ou prenez rendez-vous.")}
"""


# ---------------------------------------------------------------- Sport
def sport(p):
    intro = """<p class="lead">Nous vous conseillons des lunettes adaptées à votre sport et à votre vue : piscine, vélo,
    running, tir sportif. Venez nous dire ce que vous pratiquez : nous cherchons la solution qui vous convient.</p>"""
    spfaq = [
        ("Proposez-vous des lunettes de sport à ma vue ?",
         "Oui : montures et verres adaptés à la pratique sportive, avec votre correction : lunettes de piscine à la vue, "
         "solutions pour le vélo et le running."),
        ("Peut-on avoir des lunettes de piscine à sa vue ?",
         "Oui, avec notre fournisseur Demetz, y compris avec astigmatisme (les lunettes sans astigmatisme sont les plus "
         "abordables). Nous pouvons aussi proposer des masques de plongée à la vue."),
        ("Je pratique le tir sportif : que me proposez-vous ?",
         "Une correction juste en vision de loin et, en magasin, une correction spécifique pour l'œil de visée selon votre discipline."),
        FAQ_RDV, FAQ_PAY,
    ]
    return f"""
{page_hero(p, "Lunettes de sport", "Lunettes de sport : piscine, vélo, running, tir sportif", intro,
           "atelier.jpg", "L'atelier du magasin du Passage, où sont montés et ajustés les verres", None, ("c-rust", "c-blue"))}

<section class="bg-white">
  <div class="wrap">
    <div class="section-head"><h2>Votre sport, votre vue : on cherche la bonne solution</h2>
    <p>Chaque sport a ses contraintes : l'eau, le vent, la vitesse, la position, le casque. Nous partons de votre pratique,
    de votre correction et de votre confort pour vous proposer des montures et des verres adaptés.</p></div>
    <div class="grid grid-3">
      <div class="card"><i class="dot half c-blue"></i><h3>Piscine</h3><p>Des lunettes de piscine à votre vue, avec notre fournisseur Demetz, qui propose des équipements à la vue avec des montures spécifiques pour de nombreux sports. L'astigmatisme peut être pris en compte. Nous pouvons aussi proposer des masques de plongée à la vue.</p></div>
      <div class="card"><i class="dot half c-orange"></i><h3>Vélo et running</h3><p>La solution dépend de votre pratique et de ce que vous préférez. Certains clients ne sont pas gênés par un clip ; pour des modèles très enveloppants, on passe par un clip ; d'autres modèles s'adaptent directement à la vue, sans les contraintes du clip (la buée, par exemple).</p></div>
      <div class="card"><i class="dot half c-green"></i><h3>Autres sports</h3><p>Parlez-nous de votre pratique : nous cherchons avec vous. Pour le sport, le sur mesure se fait au niveau de la correction.</p></div>
    </div>
  </div>
</section>

<section class="bg-cream2">
  <div class="wrap two-col">
    <div>
      <span class="kicker">Tir sportif</span>
      <h2>Le tir sportif : Julien en parle mieux que personne</h2>
      <p>Julien pratique le tir sportif depuis l'enfance, en compétition. Il a obtenu des titres départementaux et régionaux
      et a été sélectionné plusieurs fois aux championnats de France. Il tire en discipline ISSF, au pistolet à 10 mètres
      et à 25 mètres. Cette pratique lui permet de comprendre ce que les tireurs attendent de leurs lunettes, quelle que soit
      leur discipline.</p>
      <p>Son conseil aux tireurs : avoir une correction juste en vision de loin (les progressifs sont très rares chez les tireurs).
      En magasin, on peut aussi déterminer une correction spécifique pour l'œil de visée, selon la discipline : organes de visée
      nets, cible légèrement plus floue.</p>
      <p>Vous tirez en club ou en compétition ? Prenez rendez-vous avec Julien.</p>
      {ext(PASSAGE['opc'], 'Rendez-vous avec Julien au Passage', 'btn-store')}
    </div>
    <div style="max-width:400px;justify-self:center;width:100%">{pattern()}</div>
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


# ---------------------------------------------------------------- Sur mesure
def sur_mesure(p):
    intro = """<p class="lead">Vous pouvez faire réaliser des lunettes sur mesure avec Loumy, une marque fabriquée à Montauban,
    partenaire de nos magasins. Une monture pensée pour votre visage, vos goûts et votre usage. Du simple changement de couleur
    d'une monture existante jusqu'à une monture entièrement conçue pour vous.</p>"""
    buttons = f"""<div class="btn-row">{ext(PASSAGE['opc'], 'Rendez-vous en magasin : Le Passage', 'btn-store')}
    {ext(BIAS['opc'], 'Rendez-vous en magasin : Bias', 'btn-store')}</div>"""
    mfaq = [
        ("Que veut dire « lunettes sur mesure » chez vous ?",
         "Personnaliser une monture Loumy existante (couleurs, taille, nez des montures plastiques) jusqu'à une monture "
         "entièrement sur mesure, avec des formes et des couleurs spécifiques."),
        ("Qui fabrique les montures sur mesure ?", "Loumy, une marque née à Montauban, créée par Dominique et Aurore Basso."),
        ("Combien de temps faut-il attendre ?", "Environ 6 semaines pour la fabrication d'une monture sur mesure."),
        ("Combien ça coûte ?", "Cela dépend de ce que vous choisissez : un devis gratuit vous est remis en magasin avant tout achat."),
        ("Le sur mesure est-il disponible dans les deux magasins ?", "Oui, au Passage et à Bias."),
        ("Puis-je faire du sur mesure avec ma correction ?", "Oui, tous les types de verres sont compatibles avec une monture Loumy sur mesure."),
        FAQ_RDV, FAQ_PAY,
    ]
    return f"""
{page_hero(p, "Lunettes sur mesure", "Lunettes sur mesure avec Loumy : une monture qui n'existe qu'à vous", intro,
           "loumy.jpg", "Monture Loumy bleue et écaille, fabriquée à Montauban", buttons, ("c-brown", "c-coral"))}

<section class="bg-white">
  <div class="wrap two-col" style="align-items:start">
    <div>
      <h2>Le sur mesure, comment ça marche ?</h2>
      <p>Avec Loumy, on peut personnaliser une monture existante : changer la couleur des branches, la couleur de la face,
      l'ajuster à la taille d'un grand visage, ou retravailler le nez des montures plastiques. On peut aller jusqu'à une
      monture entièrement sur mesure, avec des formes et des couleurs spécifiques. Cela peut aussi aider les personnes qui
      ne rentrent pas dans les tailles standards.</p>
    </div>
    <ol class="steps">
      <li>Vous venez en magasin : on écoute votre besoin et vos envies.</li>
      <li>On choisit ensemble ce qu'on personnalise (couleurs, taille, nez…).</li>
      <li>Pour une monture 100% sur mesure, Julien prend rendez-vous avec Loumy et voit avec eux, à distance, ce qui est possible.</li>
      <li>La monture est fabriquée : comptez environ 6 semaines.</li>
      <li>On vous la remet, on la règle sur votre visage, et on la réajuste quand vous voulez.</li>
    </ol>
  </div>
</section>

<section class="bg-orange">
  <div class="wrap two-col">
    <div>
      <h2>Loumy, une marque faite à Montauban, par des amis</h2>
      <p>Loumy est née à Montauban. Elle a été créée par Dominique et Aurore Basso, des amis de Julien depuis ses études
      d'opticien. Il allait de soi que la marque soit dans nos magasins. Des montures faites à la main, presque des pièces uniques.</p>
      <p><a href="{p}notre-histoire/" style="color:var(--ink)">Notre histoire</a> · <a href="{p}marques/" style="color:var(--ink)">Nos marques</a></p>
    </div>
    <div style="max-width:380px;justify-self:center;width:100%">{pattern()}</div>
  </div>
</section>

<section>
  <div class="wrap grid grid-2">
    <div class="card"><i class="dot c-green"></i><h3>Pour qui ? Pour quels usages ?</h3>
      <p>Le sur mesure Loumy concerne les lunettes de vue pour adultes, avec tous les types de verres, dans nos deux magasins.
      Voir <a href="{p}lunettes-de-vue/">Lunettes de vue</a>.</p></div>
    <div class="card"><i class="dot c-blue"></i><h3>Prix et prise en charge</h3>
      <p>Le sur mesure se chiffre sur devis. Un devis détaillé gratuit vous est remis avant tout achat.
      Paiement en plusieurs fois sans frais, jusqu'à 4 fois.</p></div>
  </div>
</section>

{where(p)}
{faq_section(p, mfaq)}
{cta_end(p, "Envie d'une monture qui n'existe qu'à vous ?", "Prenez rendez-vous au Passage ou à Bias.")}
"""


# ---------------------------------------------------------------- Réparation
def reparation(p):
    intro = """<p class="lead">Nous réglons, ajustons, nettoyons aux ultrasons et réparons vos lunettes. Une branche qui bouge,
    des lunettes qui glissent, une monture abîmée : passez nous voir. Vos lunettes viennent d'ailleurs ? Nous les réglons ou
    les réparons dans la mesure du possible. Si elles sont encore sous garantie, nous vous conseillons de revoir d'abord votre opticien.</p>"""
    buttons = f"""<div class="btn-row">{ext(PASSAGE['opc'], 'Rendez-vous en magasin : Le Passage', 'btn-store')}
    {ext(BIAS['opc'], 'Rendez-vous en magasin : Bias', 'btn-store')}</div>"""
    rfaq = [
        ("Pouvez-vous régler mes lunettes ?",
         "Oui, le réglage est gratuit, y compris pour des lunettes achetées ailleurs, dans la mesure du possible. Passez au "
         "magasin, avec ou sans rendez-vous."),
        ("Mes lunettes sont cassées, pouvez-vous les réparer ?",
         "Cela dépend de la casse : passez nous voir, nous regardons ensemble si la monture est réparable. Branches, plaquettes, "
         "vis, soudures : nous réparons dans la mesure du possible."),
        FAQ_VERRES,
        ("À quoi sert le nettoyage aux ultrasons ?",
         "C'est un nettoyage de vos lunettes dans un bac à ultrasons : principalement pour la monture, avec les verres montés dessus."),
        ("Combien coûte une réparation ou un réglage ?",
         "Le réglage est gratuit. La réparation se fait sur devis et peut être gratuite si elle est simple. Passez en magasin, "
         "nous vous répondons sur place."),
        ("Réparez-vous les lunettes d'enfant ?",
         "Oui, comme les autres lunettes : passez au magasin nous montrer le souci. Nous regardons si la monture est réparable "
         "et si une pièce peut être commandée."),
        FAQ_RDV,
    ]
    return f"""
{page_hero(p, "Réparation et ajustement", "Réparation, réglage et nettoyage de vos lunettes, au Passage et à Bias", intro,
           "atelier.jpg", "Atelier de montage et de réparation au magasin du Passage", buttons, ("c-green", "c-orange"))}

<section class="bg-white">
  <div class="wrap">
    <div class="section-head"><h2>Ce que nous faisons</h2></div>
    <div class="grid grid-4">
      <div class="card"><i class="dot c-green"></i><h3>Réglage et ajustement</h3><p>On règle la lunette sur vous, au magasin, pour qu'elle soit bien posée sur votre visage. Le réglage est gratuit.</p></div>
      <div class="card"><i class="dot c-blue"></i><h3>Nettoyage aux ultrasons</h3><p>Un nettoyage de votre monture, que nous passons au bac à ultrasons avec les verres.</p></div>
      <div class="card"><i class="dot c-orange"></i><h3>Réparation</h3><p>Changement de plaquettes, revissage, remplacement de vis perdues, dépannage de branches, soudures sur les matériaux classiques (titane et injecté).</p></div>
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
      si elle est en bon état. Nous collectons aussi les montures dont vous n'avez plus l'usage : le Lions Club les trie et les
      donne à des personnes dans le besoin.</p>
    </div>
    <div class="callout coral">
      <h3>Prix et délais</h3>
      <p>Le réglage est gratuit pour tous. La réparation se fait sur devis, et elle peut être gratuite si elle est rapide et
      sans frais. Si la réparation est possible tout de suite, on la fait pendant votre visite ; sinon, le délai dépend de la
      réception de la pièce.</p>
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
def marques(p):
    labels = {"both": ("both", "Dans les deux magasins"), "passage": ("passage", "Au Passage"), "bias": ("bias", "À Bias")}
    cat_names = {"vue": "Vue", "soleil": "Soleil", "enfant": "Enfant", "sport": "Sport"}
    items = []
    for name, note, store, cats, fr in sorted(BRANDS, key=lambda b: b[0].lower()):
        cls, lab = labels[store]
        tags = " ".join(cats + ([store] if store != "both" else ["passage", "bias"]) + (["fr"] if fr else []))
        pills = f'<span class="pill {cls}">{lab}</span>' + "".join(f'<span class="pill both">{cat_names[c]}</span>' for c in cats)
        if fr:
            pills += '<span class="pill fr">Fabriqué en France</span>'
        items.append(f'<div class="brand" data-tags="{tags}"><strong>{name}</strong>'
                     f'{f"<small>{note}</small>" if note else ""}{pills}</div>')
    filters = [("all", "Toutes"), ("passage", "Au Passage"), ("bias", "À Bias"), ("vue", "Vue"), ("soleil", "Soleil"),
               ("enfant", "Enfant"), ("fr", "Fabriqué en France")]
    fbtn = "".join(f'<button data-filter="{k}" aria-pressed="{"true" if k == "all" else "false"}">{v}</button>' for k, v in filters)
    return f"""
<section class="page-hero">
  <div class="wrap">
    <span class="kicker">Nos marques</span>
    <h1>Des lunettes de marque, choisies une à une</h1>
    <p class="lead">Des marques indépendantes, dont plusieurs fabriquées en France, et des grandes maisons. Chaque marque
    indique le magasin où la trouver : au Passage, à Bias, ou dans les deux.</p>
  </div>
</section>
<section style="padding-top:0">
  <div class="wrap">
    <div class="brand-filter" role="group" aria-label="Filtrer les marques">{fbtn}</div>
    <div class="brands">{''.join(items)}</div>
    <p class="notice" style="margin-top:1.5rem">Les collections évoluent : appelez le magasin pour vérifier qu'un modèle est disponible.
    <span class="todo">Liste à faire relire par Julien (marques par magasin, pays ou ville de chaque marque).</span></p>
  </div>
</section>
{cta_end(p, "Venez les essayer au Passage ou à Bias.")}
"""


# ---------------------------------------------------------------- Notre histoire
def histoire(p):
    intro = """<p class="lead">Lunettes &amp; Co, ce sont deux magasins d'opticiens indépendants en Lot-et-Garonne, à Bias
    et au Passage. Julien, opticien depuis plus de 15 ans, choisit lui-même chaque monture pour que chacun trouve une paire
    qui lui ressemble, à son budget. C'est aussi une histoire familiale et de couple.</p>"""
    buttons = f"""<div class="btn-row"><a class="btn btn-ghost" href="{p}{PASSAGE['page']}">Le Passage</a>
    <a class="btn btn-ghost" href="{p}{BIAS['page']}">Bias</a></div>"""
    return f"""
{page_hero(p, "Notre histoire", "Lunettes &amp; Co, opticiens indépendants à Bias et au Passage", intro,
           "equipe.jpg", "L'équipe Lunettes & Co au magasin du Passage", buttons, ("c-orange", "c-green"))}

<section class="bg-white">
  <div class="wrap two-col" style="align-items:start">
    <div class="prose">
      <h2>Un opticien qui a voulu choisir ses montures</h2>
      <p>Julien a ouvert le magasin de Bias en 2012. Pendant quelques années, il a travaillé au sein d'un réseau de franchise.
      Puis il a voulu retrouver sa liberté : choisir ses marques, les qualités qu'il propose et ce qu'il a vraiment envie de
      conseiller à ses clients. Lunettes &amp; Co est né de ce choix, avec Karine à ses côtés.</p>
      <h2>Des lunettes originales, à des prix accessibles</h2>
      <p>Chez nous, « créateurs » ne veut pas dire « cher ». Il y a des montures à partir de 100 euros, le 100% Santé dans chaque
      magasin et, si vous avez envie de vous faire plaisir, des montures faites à la main, presque des pièces uniques. Pas de ton
      pompeux : on aime les beaux objets, la technique et une monture confortable sur le nez.</p>
    </div>
    <div class="prose">
      <h2>Du local, du français, de l'européen</h2>
      <p>On travaille avec des marques qui fabriquent en France : Loumy, née à Montauban, créée par Dominique et Aurore Basso,
      des amis de Julien depuis ses études d'opticien ; Bondet et Victoire Daqui à Bias ; Lafont Enfant au Passage. Côté verres,
      nous travaillons notamment avec Méga Optic, verrier français.</p>
      <h2>Deux magasins, deux ambiances</h2>
      <p>À Bias, dans la galerie marchande d'Auchan, Anne, responsable du magasin, et Francesca, apprentie, vous accueillent
      avec le sourire. Au Passage, nous avons imaginé un lieu plus cosy et chaleureux, à l'image de notre sélection de montures.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap grid grid-2">
    <img src="{p}assets/img/bias-accueil.jpg" alt="Le magasin de Bias, mur vert et logo Lunettes & Co" loading="lazy" style="border-radius:var(--radius);aspect-ratio:4/3;object-fit:cover" width="1600" height="1200">
    <img src="{p}assets/img/passage-salon.jpg" alt="Le salon du magasin du Passage, fauteuils et montures" loading="lazy" style="border-radius:var(--radius);aspect-ratio:4/3;object-fit:cover" width="1600" height="1200">
  </div>
</section>

<section class="bg-cream2">
  <div class="wrap grid grid-3">
    <div class="card"><i class="dot c-green"></i><h3>Une démarche plus responsable</h3><p>Nous essayons de limiter le plastique : sacs en kraft, étuis en kraft avec un intérieur en velours. Et si votre monture est en bon état, nous pouvons simplement changer les verres. Une démarche que nous améliorons peu à peu.</p></div>
    <div class="card"><i class="dot c-orange"></i><h3>Pourquoi « Lunettes &amp; Co » ?</h3><p>Un nom simple, que tout le monde comprend. Le « Co », ce sont les premières lettres du nom de famille de Julien. Mais aussi les copains, les collections, les collaborations et les clients comblés.</p></div>
    <div class="card"><i class="dot c-blue"></i><h3>Julien et le tir sportif</h3><p>Julien pratique le tir sportif depuis l'enfance, au pistolet à 10 et 25 mètres, avec des titres départementaux et régionaux et plusieurs sélections aux championnats de France. <a href="{p}lunettes-de-sport/">Lunettes de sport</a></p></div>
  </div>
</section>

{cta_end(p, "Venez nous rencontrer à Bias ou au Passage.")}
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
         "en ligne via notre réseau, Opticiens par Conviction)."),
        FAQ_RDV,
        ("Que dois-je apporter ?",
         "Pour un conseil lunettes : votre ordonnance et vos lunettes actuelles. Pour la téléconsultation : votre carte Vitale, "
         "votre carte bancaire, vos lunettes actuelles, votre dernière ordonnance."),
        ("Le magasin de Bias s'appelait-il autrement ?", "Oui, il s'appelait Optical Discount."),
    ]
    return f"""
<section class="page-hero">
  <div class="wrap">
    <span class="kicker">Contact et rendez-vous</span>
    <h1>Contact et rendez-vous : Le Passage et Bias</h1>
    <p class="lead">Une question, un conseil, un rendez-vous ? Choisissez le magasin le plus proche : Le Passage, près d'Agen,
    ou Bias, près de Villeneuve-sur-Lot. Vous pouvez aussi passer nous voir sans rendez-vous.</p>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <h2>Quel rendez-vous choisir ?</h2>
    <div class="grid grid-2">
      <div class="callout blue"><h3>Téléconsultation d'ophtalmologie</h3>
        <p>Voir un ophtalmologue en visioconférence depuis le magasin, sur rendez-vous. Dès 16 ans.</p>
        <p class="notice"><strong>Ce n'est pas un service d'urgence : en cas d'urgence, contactez le SAMU au 15.</strong></p>
        <span class="badge-slot">Logo Doctolib à intégrer</span>
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
  <div class="wrap"><p class="notice" style="margin-top:1rem"><span class="todo">Horaires provisoires, à recopier depuis les fiches Google. E-mail de contact à fournir.</span></p></div>
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
        ("Où se garer ?", "À Bias, sur le parking du centre commercial Auchan."),
        ("Le magasin de Bias s'appelait-il autrement ?", "Oui, il s'appelait Optical Discount."),
    ]),
    ("Prix, 100% Santé et paiement", [
        ("Qu'est-ce que le 100% Santé en optique ?", CENT_POUR_CENT),
        ("Proposez-vous le 100% Santé ?", "Oui, dans chaque magasin, pour toute la famille."),
        ("Puis-je mélanger une monture 100% Santé et des verres à prix libres ?",
         "Oui, il est possible d'associer une monture d'une gamme et des verres de l'autre. En revanche, on ne peut pas prendre "
         "des verres de deux gammes différentes."),
        ("Quel budget prévoir pour des lunettes de vue ?",
         "Cela dépend de votre correction, de la monture et des verres choisis, et de votre couverture. Nous vous remettons un devis "
         "gratuit en magasin, avec l'offre 100% Santé et l'offre à tarifs libres. Montures hors 100% Santé à partir de 100 euros ; "
         "montures 100% Santé à 30 euros maximum."),
        FAQ_PAY,
    ]),
    ("Ordonnance et renouvellement", ORDONNANCE_FAQ + [
        ("Mon ordonnance est trop ancienne, que faire ?",
         "Il faut une ordonnance en cours de validité. Une téléconsultation d'ophtalmologie en magasin peut vous permettre d'en "
         "obtenir une, si votre situation s'y prête."),
    ]),
    ("Téléconsultation d'ophtalmologie", [
        ("Peut-on consulter un ophtalmologue dans vos magasins ?",
         "Oui, en visioconférence, sur rendez-vous, depuis nos magasins de Bias et du Passage, si votre situation s'y prête. "
         "À partir de 16 ans."),
        ("Est-ce un service d'urgence ?", "Non. En cas d'urgence, contactez le SAMU au 15."),
        ("La téléconsultation remplace-t-elle un rendez-vous chez l'ophtalmologue ?",
         "Elle s'adresse notamment aux personnes qui peinent à obtenir un rendez-vous avec un ophtalmologue."),
        ("Puis-je acheter mes lunettes chez vous après ?", "Oui, notre équipe peut vous conseiller en magasin si vous le souhaitez."),
        ("Proposez-vous la téléconsultation pour renouveler mes lentilles ?",
         "Oui, en magasin et sur rendez-vous, si votre situation s'y prête."),
    ]),
    ("Lunettes de vue, de soleil, pour enfants et de sport", [
        ("Comment choisir ses lunettes selon la forme de son visage ?", "Venez les essayer : c'est le plus simple, et notre équipe vous guide."),
        FAQ_VERRES,
        ("Peut-on avoir des lunettes de soleil à sa vue ?",
         "Oui. Choisissez votre monture et nous vous conseillons sur les verres et les teintes. Apportez votre ordonnance en cours de validité."),
        ("Faut-il amener mon enfant pour choisir ses lunettes ?",
         "Oui, c'est le plus important. Selon son âge et la forme de son visage, il faut voir que la monture est bien adaptée et "
         "qu'elle couvre bien ses yeux. Il peut aussi choisir sa monture : une monture qu'il aime, il la porte plus volontiers."),
        ("Proposez-vous des lunettes de sport à ma vue ?", "Oui : montures et verres adaptés à la pratique sportive, avec votre correction."),
    ]),
    ("Lentilles de contact", [
        ("Faut-il une ordonnance pour acheter des lentilles de contact ?", "Oui, les lentilles de contact sont délivrées sur ordonnance."),
        ("Vendez-vous des produits d'entretien pour lentilles ?", "Oui, avec conseil en magasin."),
    ]),
    ("Réglages et réparations", [
        ("Pouvez-vous régler mes lunettes ?", "Oui, le réglage est gratuit, y compris pour des lunettes achetées ailleurs, dans la mesure du possible."),
        ("Mes lunettes sont cassées, pouvez-vous les réparer ?",
         "Cela dépend de la casse : passez nous voir, nous regardons ensemble si la monture est réparable."),
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
  <p><span class="todo">Raison sociale, forme juridique, capital, adresse du siège, SIRET, RCS, numéro de TVA,
  directeur de la publication, e-mail de contact : à fournir.</span></p>
  <h2>Hébergement</h2>
  <p>GitHub Pages, GitHub Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis.</p>
  <h2>Propriété intellectuelle</h2>
  <p>La marque et le logo Lunettes &amp; Co sont la propriété de leur titulaire. Les photographies des magasins sont la
  propriété de Lunettes &amp; Co. Toute reproduction sans autorisation est interdite.</p>
  <h2>Prise de rendez-vous</h2>
  <p>Les prises de rendez-vous sont assurées par des services tiers : Doctolib (téléconsultation d'ophtalmologie) et
  Opticiens par Conviction (rendez-vous en magasin), selon leurs propres conditions.</p>
</div></section>
"""


def confidentialite(p):
    return """
<section class="page-hero"><div class="wrap prose">
  <h1>Politique de confidentialité</h1>
  <p>Ce site vitrine ne comporte pas de formulaire et ne collecte pas de données personnelles.</p>
  <h2>Cookies et mesure d'audience</h2>
  <p>À ce jour, aucun cookie de mesure d'audience n'est déposé. <span class="todo">Si Google Analytics est ajouté :
  bannière de consentement et mise à jour de cette page (conformité CNIL à faire valider).</span></p>
  <h2>Services tiers</h2>
  <p>Les boutons de rendez-vous ouvrent les sites Doctolib et Opticiens par Conviction, qui traitent vos données selon
  leurs propres politiques de confidentialité. Les polices de caractères sont chargées depuis Google Fonts.</p>
  <h2>Contact</h2>
  <p><span class="todo">Adresse de contact pour exercer vos droits : à fournir.</span></p>
</div></section>
"""


PAGES = [
    {"slug": "", "title": "Opticien indépendant en Lot-et-Garonne | Lunettes & Co",
     "description": "Lunettes & Co, opticien indépendant au Passage (près d'Agen) et à Bias (près de Villeneuve-sur-Lot) : conseil personnalisé, montures pour tous les budgets.",
     "body": home, "org_ld": True, "faq_ld": HOME_FAQ},
    {"slug": "opticien-le-passage/", "title": "Opticien Le Passage, près d'Agen | Lunettes & Co",
     "description": "Lunettes & Co, opticien indépendant au Passage d'Agen, ZAC de Lacassagne : lunettes de vue et de soleil, téléconsultation d'ophtalmologie, conseil sur mesure.",
     "body": store_page(PASSAGE)},
    {"slug": "opticien-bias/", "title": "Opticien à Bias, près de Villeneuve-sur-Lot | Lunettes & Co",
     "description": "Lunettes & Co, opticien indépendant à Bias (Auchan Ponservat), anciennement Optical Discount : lunettes, lentilles, téléconsultation d'ophtalmologie.",
     "body": store_page(BIAS)},
    {"slug": "teleconsultation-ophtalmologie/", "title": "Téléconsultation ophtalmologique en magasin | Lunettes & Co",
     "description": "Consultez un ophtalmologue en visioconférence depuis nos magasins de Bias et du Passage, sur rendez-vous. Dès 16 ans. Pas un service d'urgence.",
     "body": teleconsultation},
    {"slug": "lunettes-de-vue/", "title": "Lunettes de vue au Passage et à Bias | Lunettes & Co",
     "description": "Lunettes de vue près d'Agen et de Villeneuve-sur-Lot : montures dès 100 euros, 100% Santé, verres progressifs, conseil personnalisé.",
     "body": lunettes_vue},
    {"slug": "lunettes-de-soleil/", "title": "Lunettes de soleil, à votre vue ou non | Lunettes & Co",
     "description": "Lunettes de soleil au Passage et à Bias : Ray-Ban, Ki ET LA, Lancel, verres polarisants, solaires à la vue et clips pour la conduite.",
     "body": lunettes_soleil},
    {"slug": "lunettes-enfants/", "title": "Lunettes enfants, pour tous les âges | Lunettes & Co",
     "description": "Lunettes pour enfants au Passage et à Bias : essayage en magasin avec votre enfant, 100% Santé, montures dès 80 euros.",
     "body": lunettes_enfants},
    {"slug": "lentilles-de-contact/", "title": "Lentilles de contact et produits d'entretien | Lunettes & Co",
     "description": "Adaptation et renouvellement de lentilles de contact, produits d'entretien, au Passage et à Bias.",
     "body": lentilles},
    {"slug": "lunettes-de-sport/", "title": "Lunettes de sport à la vue, tir sportif | Lunettes & Co",
     "description": "Lunettes de sport à votre vue : piscine, vélo, running, et tir sportif avec Julien, tireur de compétition.",
     "body": sport},
    {"slug": "lunettes-sur-mesure/", "title": "Lunettes sur mesure avec Loumy | Lunettes & Co",
     "description": "Lunettes sur mesure avec Loumy, lunetier de Montauban : personnalisation ou monture entièrement conçue pour vous.",
     "body": sur_mesure},
    {"slug": "reparation-ajustement-lunettes/", "title": "Réparation et réglage de lunettes | Lunettes & Co",
     "description": "Réglage gratuit, réparation, nettoyage aux ultrasons et changement de verres, au Passage et à Bias.",
     "body": reparation},
    {"slug": "marques/", "title": "Nos marques de lunettes | Lunettes & Co",
     "description": "Loumy, Tavat, Brett, Tiwi, GIGIstudios, Etnia Barcelona, Ray-Ban… Les marques de lunettes disponibles au Passage et à Bias.",
     "body": marques},
    {"slug": "notre-histoire/", "title": "Notre histoire | Lunettes & Co, opticiens indépendants (47)",
     "description": "Julien, opticien depuis plus de 15 ans, vous accueille à Bias et au Passage : conseil sur mesure et montures pour tous les budgets.",
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
