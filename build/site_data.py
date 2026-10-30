"""Données partagées du site : magasins, liens de rendez-vous, navigation, marques.

Source : Site-reference/02-fiche-client-et-NAP.md (mises à jour du 23 et du 26/10/2026).
Tout ce qui est marqué TODO est à confirmer avant la mise en ligne publique.
"""

SITE_NAME = "Lunettes & Co"
DOMAIN = "https://www.lunettesandco.fr"  # adresse principale (DNS chez OVH)

# Google Analytics 4 : identifiant de mesure (« G-XXXXXXXXXX »). Tant qu'il est vide, ni Analytics ni bandeau cookies.
GA_ID = "G-JGCQHGMNHW"

DOCTOLIB_PASSAGE = (
    "https://www.doctolib.fr/magasin-d-optique/le-passage/lunettes-co-teleconsultation-ophtalmologique"
    "/booking/motives?specialityId=13512&telehealth=false&placeId=practice-724754&source=profile"
)
DOCTOLIB_BIAS = (
    "https://www.doctolib.fr/magasin-d-optique/bias/lunettes-co-bias-teleconsultation-ophtalmologique"
    "/booking/motives?specialityId=13512&telehealth=false&placeId=practice-801197&source=profile"
)
OPC_PASSAGE = "https://www.opticiensparconviction.fr/votre-opticien-a-le-passage/lunettes-and-co/prise-de-rdv"
OPC_BIAS = "https://www.opticiensparconviction.fr/votre-opticien-a-bias/lunettes-and-co/prise-de-rdv"

PASSAGE = {
    "key": "passage",
    "name": "Le Passage",
    "label": "Le Passage, près d'Agen",
    "at": "au Passage",
    "near": "près d'Agen",
    "street": "64 allée du Loriot, ZAC de Lacassagne",
    "postcode": "47520",
    "city": "Le Passage",
    "address": "64 allée du Loriot, ZAC de Lacassagne, 47520 Le Passage",
    "geo": (44.194682, 0.597402),  # vérifié par Karine dans Google Maps le 28/10/2026
    "phone": "05 35 55 92 50",  # carte de visite LP + flyer sept. 2026 ; à confirmer sur la fiche Google
    "phone_intl": "+33535559250",
    "doctolib": DOCTOLIB_PASSAGE,
    "opc": OPC_PASSAGE,
    "page": "opticien-le-passage/",
    "maps": "https://www.google.com/maps/search/?api=1&query=Lunettes+%26+Co+64+all%C3%A9e+du+Loriot+47520+Le+Passage",
    "reviews": "https://www.google.com/maps?cid=67469068554064698",  # fiche Google (avis), vérifiée le 27/10/2026
    "gallery": [
        ("passage-galerie-1.jpg", "Vue d'ensemble du magasin du Passage, suspensions orange et fauteuils"),
        ("passage-galerie-2.jpg", "Étagères de montures sur mur bleu, au magasin du Passage"),
        ("passage-galerie-3.jpg", "Table de conseil sous les suspensions orange, au magasin du Passage"),
        ("passage-galerie-4.jpg", "Fauteuils et présentoirs de montures, au magasin du Passage"),
    ],
    "image": "passage-magasin.jpg",
    "image_alt": "Intérieur du magasin Lunettes & Co au Passage, près d'Agen",
    "hours": [
        ("Lundi", "Fermé"),
        ("Mardi", "9h30 – 12h30 · 14h30 – 19h"),
        ("Mercredi", "14h30 – 19h"),
        ("Jeudi", "9h30 – 12h30 · 14h30 – 19h"),
        ("Vendredi", "9h30 – 12h30 · 14h30 – 19h"),
        ("Samedi", "9h30 – 12h30 · 14h30 – 19h"),
        ("Dimanche", "Fermé"),
    ],
    "parking": "Places devant le magasin, et grand parking du Lidl dans la zone commerciale",
    "bus": "Arrêt Demi-Lune, ligne 7 du réseau Tempo, à 2 minutes à pied du magasin",  # vérifié le 28/10/2026 (fiche ligne 7 éd. oct. 2026, OpenStreetMap : ~130 m)
}

BIAS = {
    "key": "bias",
    "name": "Bias",
    "label": "Bias, près de Villeneuve-sur-Lot",
    "at": "à Bias",
    "near": "près de Villeneuve-sur-Lot",
    "street": "Centre commercial Auchan (Ponservat), avenue de Bordeaux",
    "postcode": "47300",
    "city": "Bias",
    "address": "Centre commercial Auchan (Ponservat), avenue de Bordeaux, 47300 Bias",
    "geo": (44.405188, 0.676313),  # vérifié par Karine dans Google Maps le 28/10/2026 (centre commercial Auchan Ponservat)
    "phone": "05 53 40 19 96",
    "phone_intl": "+33553401996",
    "doctolib": DOCTOLIB_BIAS,
    "opc": OPC_BIAS,
    "page": "opticien-bias/",
    "maps": "https://www.google.com/maps/search/?api=1&query=Lunettes+%26+Co+Auchan+Ponservat+47300+Bias",
    "reviews": "https://www.google.com/maps?cid=4794800154801151129",  # fiche Google (avis), vérifiée le 27/10/2026
    "gallery": [  # photos provisoires : Karine fournit de nouvelles photos de Bias
        ("bias-galerie-1.jpg", "Table de conseil au magasin de Bias"),
        ("bias-galerie-2.jpg", "L'espace de vente du magasin de Bias"),
        ("bias-galerie-3.jpg", "Présentoirs de montures au magasin de Bias"),
    ],
    "image": "bias-magasin.jpg",
    "image_alt": "Intérieur du magasin Lunettes & Co à Bias, galerie Auchan Ponservat",
    "hours": [
        ("Lundi", "Fermé"),
        ("Mardi", "9h – 12h30 · 14h – 19h"),
        ("Mercredi", "9h – 12h45"),
        ("Jeudi", "9h – 12h30 · 14h – 19h"),
        ("Vendredi", "9h – 12h30 · 14h – 19h"),
        ("Samedi", "9h – 12h30 · 14h – 19h"),
        ("Dimanche", "Fermé"),
    ],
    "parking": "Parking gratuit du centre commercial Auchan ; le magasin est accessible par l'entrée du centre commercial",
}

STORES = [PASSAGE, BIAS]

PRODUCTS = [
    ("lunettes-de-vue/", "Lunettes de vue", "Verres unifocaux et progressifs, 100% Santé, conseil sur le choix des verres.", "c-green"),
    ("lunettes-de-soleil/", "Lunettes de soleil", "Avec ou sans correction, et des clips teintés pour la conduite.", "c-orange"),
    ("lunettes-enfants/", "Lunettes enfants", "Pour tous les âges, à essayer avec votre enfant.", "c-coral"),
    ("lentilles-de-contact/", "Lentilles de contact", "Adaptation, renouvellement, produits d'entretien.", "c-blue"),
    ("lunettes-de-sport/", "Lunettes de sport", "Piscine, vélo, running, tir sportif, à votre vue.", "c-rust"),
    ("lunettes-personnalisees/", "Lunettes personnalisées", "Avec Loumy, personnalisez votre monture à vos couleurs.", "c-brown"),
    ("reparation-ajustement-lunettes/", "Réparation et ajustage", "Réglage, réparations, nettoyage aux ultrasons.", "c-green"),
]

# Marques : (nom, pays, fabrication ou précision, description, lien, magasins, catégories, fabrication française)
# pays : fr | es | it | us | be | dk ; fabrication : "" si inconnue
# lien : site officiel, conservé pour mémoire mais non affiché (décision de Karine du 28/10/2026)
# magasins : "both" | "passage" | "bias" ; catégories : vue, soleil, enfant, sport
# Origines : Site-reference/34-marques-origines-v1.md ; descriptions vérifiées sur les sites officiels le 28/10/2026
BRANDS = [
    ("Loumy", "fr", "Fabriquée en France, à Montauban",
     "Un atelier de Montauban fondé par Aurore et Domy : des montures originales et colorées, en acétate, fabriquées de façon artisanale.",
     "https://loumy-lunetier.fr/", "both", ["vue", "soleil"], True),
    ("Tavat", "us", "Fabriquée en Italie",
     "Dessinée en Californie, fabriquée en petites séries par des artisans du nord de l'Italie, au sein d'une entreprise familiale indépendante.",
     "https://tavat-eyewear.com/", "passage", ["vue", "soleil"], False),
    ("Brett", "fr", "",
     "Inspirée du cinéma des années 70 et de l'univers auto-moto : des montures en titane, carbone ou acétate, et des solaires à verres polarisants.",
     "https://brett-eyewear.com/fr", "passage", ["vue", "soleil"], False),
    ("Tiwi", "es", "",
     "Créée par des professionnels de l'optique, de la mode et de la photographie, Tiwi soutient deux associations pour la vue dans les pays en développement.",
     "https://tiwiworld.com/", "both", ["vue", "soleil"], False),
    ("Marlone", "fr", "Fabriquée en France, dans le Jura",
     "Créée par deux opticiennes, Laurence et Laetitia : des modèles inspirés de la Californie, qui portent le nom de quartiers de Palm Springs.",
     "https://marlone-eyewear.com/", "passage", ["vue"], True),
    ("Bondet", "fr", "Fabriquée en France, à Oyonnax",
     "Lunetier d'Oyonnax depuis 1929, une entreprise familiale qui utilise des matériaux biosourcés.",
     "https://bondet.com/", "bias", ["vue"], True),
    ("Victoire d'Aqui", "fr", "Fabriquée à Hossegor, dans les Landes",
     "« D'Aqui » veut dire « d'ici » en patois landais : des montures en acétate dessinées et fabriquées dans l'atelier d'Hossegor.",
     "https://victoirefamilyeyes.fr/", "bias", ["vue"], True),
    ("Lafont Enfant", "fr", "Fabriquée en France",
     "Une maison parisienne familiale : des montures pour enfants, des tout-petits à 12 ans, aux charnières flexibles et en matériaux biosourcés.",
     "https://www.lafont.com/kids", "passage", ["enfant"], True),
    ("GIGIstudios", "es", "Anciennement Gigi Barcelona",
     "Née à Barcelone en 2016 : des montures pensées comme des pièces de mode, élégantes et faites pour durer.",
     "https://gigistudios.com/fr-fr", "bias", ["vue"], False),
    ("Etnia Barcelona", "es", "",
     "Un lunetier barcelonais connu pour ses couleurs et ses collaborations avec des artistes.",
     "https://etniabarcelona.com/fr-fr", "both", ["vue", "enfant"], False),
    ("Chroma by Etnia Barcelona", "es", "",
     "La ligne d'Etnia Barcelona consacrée à la couleur : des teintes franches et des dégradés sur les faces et les branches.",
     "https://etniabarcelona.com/fr-fr/pages/chroma", "passage", ["vue"], False),
    ("French Retro", "fr", "",
     "Créée dans le Marais par deux opticiens : des montures au style rétro et chic, dessinées à Paris.",
     "https://www.frenchretro.com/", "both", ["vue", "soleil", "enfant"], False),
    ("Matttew", "be", "Fabriquée en France, dans le Jura",
     "Fondée en 2011 par Matthieu, designer formé à Bruxelles : des montures colorées, aux lignes droites et aux angles coupés.",
     "https://www.matttew.com/", "both", ["vue"], True),
    ("Lool", "es", "",
     "Un studio de création barcelonais, parti d'une idée : une charnière sans vis. Des lignes inspirées de l'architecture contemporaine.",
     "https://looleyewear.com/fr-fr", "both", ["vue"], False),
    ("Vogue", "it", "",
     "Des lunettes de mode, au ton ludique, qui suivent les tendances.",
     "https://vogue-eyewear.com/fr-fr", "both", ["vue", "soleil"], False),
    ("Lancel", "fr", "",
     "Maison parisienne fondée en 1876, connue pour sa maroquinerie : des lunettes élégantes et féminines.",
     "https://lancel.com/fr/collections/lunettes-de-soleil-femme", "both", ["vue", "soleil"], False),
    ("Ray-Ban", "us", "",
     "Une marque mythique de la lunette de soleil : l'Aviator et la Wayfarer sont devenues des classiques, aussi déclinées en lunettes de vue.",
     "https://www.ray-ban.com/france", "both", ["vue", "soleil", "enfant"], False),
    ("Vicomte Arthur", "fr", "",
     "Marque de mode française créée en 2005, qui revendique l'élégance à la française.",
     "https://vicomte-a.com/", "both", ["vue"], False),
    ("Ruud van Dyke", "be", "",
     "Des montures légères en titane, d'une élégance discrète, dont des modèles sans cercle.",
     "https://shop.mpg-eyewear.com/ruud-van-dyke-8", "both", ["vue"], False),
    ("Osmose Clip", "fr", "",
     "Des montures avec deux clips aimantés : un solaire polarisant, et un jaune pour la conduite de nuit.",
     "https://www.octika.com/content/9-presentation-marque-osmose", "both", ["vue"], False),
    ("Ki ET LA", "fr", "Certains modèles fabriqués en France",
     "Créée en 2010 par trois amis d'enfance : des lunettes de soleil incassables pour les enfants, jusqu'à 12 ans.",
     "https://www.kietla.fr/", "both", ["soleil"], False),
    ("Chantal Thomass", "fr", "",
     "Créatrice parisienne depuis 1975, en noir et rose : des montures affirmées, ornées de détails de dentelle.",
     "https://chantal-thomass.com/", "bias", ["vue"], False),
    ("Azzaro", "it", "",
     "Des montures signées par la maison de parfum, dont la ligne Azzaro Homme.",
     "https://www.azzaro.com/fr", "bias", ["vue", "soleil"], False),
    ("Entourage of 7", "us", "Fabriquée au Japon",
     "Née à Venice Beach, à Los Angeles, en 2007 : des montures en acétate et titane, reconnaissables à leur clin d'œil au chiffre 7.",
     "https://bellingerhouse.com/brands/entourage-of-7", "bias", ["vue"], False),
    ("Bellinger", "dk", "",
     "Fondée en 2003 par Malene et Claus Bellinger : des couleurs inattendues et des branches larges aux découpes spectaculaires.",
     "https://bellingerhouse.com/brands/bellinger", "bias", ["vue"], False),
    ("Guess", "it", "",
     "Des lunettes dans l'esprit de la marque de vêtements.",
     "https://www.guess.com/fr-fr/guess/femme/accessoires/lunettes-de-soleil", "bias", ["vue", "soleil"], False),
    ("Minima", "fr", "",
     "Des montures légères, simples et confortables au quotidien, avec une gamme Junior pour les enfants.",
     "https://minima.fr/", "bias", ["vue", "enfant"], False),
    ("Polaroid", "us", "",
     "L'inventeur du filtre polarisant : toutes les solaires ont des verres polarisants.",
     "https://www.polaroideyewear.com/fr", "bias", ["soleil"], False),
    ("Eleven Paris", "fr", "",
     "Marque de mode parisienne née en 2003, pleine d'humour : des montures pour enfants colorées et décontractées.",
     "https://elevenparis.com/", "both", ["enfant"], False),
    ("Demetz", "fr", "",
     "Depuis 1950, le spécialiste du sport à la vue : lunettes de piscine et masques de plongée adaptés à votre correction.",
     "https://demetz.fr/fr/", "both", ["sport"], False),
]
