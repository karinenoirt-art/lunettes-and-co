"""Données partagées du site : magasins, liens de rendez-vous, navigation, marques.

Source : Site-reference/02-fiche-client-et-NAP.md (mises à jour du 23 et du 26/10/2026).
Tout ce qui est marqué TODO est à confirmer avant la mise en ligne publique.
"""

SITE_NAME = "Lunettes & Co"
DOMAIN = "https://www.lunettesandco.fr"  # adresse principale (DNS chez OVH)

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
    "bus": "Le Passage d'Agen est desservi par le réseau Tempo (lignes 5, 6 et 7)",
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
    ("lunettes-sur-mesure/", "Lunettes sur mesure", "Avec Loumy, personnalisez votre monture ou créez votre propre paire.", "c-brown"),
    ("reparation-ajustement-lunettes/", "Réparation et ajustement", "Réglage, réparations, nettoyage aux ultrasons.", "c-green"),
]

# Marques : (nom, précision, magasins, catégories, fabrication française)
# magasins : "both" | "passage" | "bias" ; catégories : vue, soleil, enfant, sport
BRANDS = [
    ("Loumy", "Lunetier de Montauban · montures artisanales, sur mesure", "both", ["vue", "soleil"], True),
    ("Tavat", "États-Unis · fabriquée en Italie", "passage", ["vue", "soleil"], False),
    ("Brett", "France", "passage", ["vue", "soleil"], False),
    ("Tiwi", "Espagne", "both", ["vue", "soleil"], False),
    ("Marlone", "", "passage", ["vue"], True),
    ("Bondet", "", "bias", ["vue"], True),
    ("Victoire d'Aqui", "", "bias", ["vue"], True),
    ("Lafont Enfant", "", "passage", ["enfant"], True),
    ("GIGIstudios", "Anciennement Gigi Barcelona · Espagne", "bias", ["vue"], False),
    ("Etnia Barcelona", "Espagne", "both", ["vue", "enfant"], False),
    ("Chroma by Etnia Barcelona", "Espagne", "passage", ["vue"], False),
    ("French Retro", "France", "both", ["vue", "soleil", "enfant"], False),
    ("Matttew", "Marque belge · fabriquée en France", "both", ["vue"], True),
    ("Lool", "Espagne", "both", ["vue"], False),
    ("Vogue", "", "both", ["vue", "soleil"], False),
    ("Lancel", "France", "both", ["vue", "soleil"], False),
    ("Ray-Ban", "", "both", ["vue", "soleil", "enfant"], False),
    ("Vicomte Arthur", "France", "both", ["vue"], False),
    ("Ruud van Dyke", "", "both", ["vue"], False),
    ("Osmose Clip", "France · clips aimantés à fixer sur la monture", "both", ["vue"], False),
    ("Ki ET LA", "France", "both", ["soleil"], False),
    ("Chantal Thomass", "France", "bias", ["vue"], False),
    ("Azzaro", "Dont Azzaro Homme", "bias", ["vue", "soleil"], False),
    ("Entourage of 7", "États-Unis · fabriquée au Japon", "bias", ["vue"], False),
    ("Bellinger", "Danemark", "bias", ["vue"], False),
    ("Guess", "", "bias", ["vue", "soleil"], False),
    ("Minima", "Et Minima Kids · France", "bias", ["vue", "enfant"], False),
    ("Polaroid", "", "bias", ["soleil"], False),
    ("Eleven Paris", "France", "both", ["enfant"], False),
    ("Demetz", "France · lunettes de piscine et équipements de sport à la vue", "both", ["sport"], False),
]
