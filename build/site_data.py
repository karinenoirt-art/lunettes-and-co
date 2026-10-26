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
    "near": "près d'Agen",
    "street": "64 allée du Loriot, ZAC de Lacassagne",
    "postcode": "47520",
    "city": "Le Passage",
    "address": "64 allée du Loriot, ZAC de Lacassagne, 47520 Le Passage",
    "phone": None,  # TODO : à recopier depuis la fiche Google
    "phone_intl": None,
    "doctolib": DOCTOLIB_PASSAGE,
    "opc": OPC_PASSAGE,
    "page": "opticien-le-passage/",
    "maps": "https://www.google.com/maps/search/?api=1&query=Lunettes+%26+Co+64+all%C3%A9e+du+Loriot+47520+Le+Passage",
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
    "parking": None,  # TODO : à confirmer
}

BIAS = {
    "key": "bias",
    "name": "Bias",
    "label": "Bias, près de Villeneuve-sur-Lot",
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
    "parking": "Parking du centre commercial Auchan",
}

STORES = [PASSAGE, BIAS]

PRODUCTS = [
    ("lunettes-de-vue/", "Lunettes de vue", "Montures, verres unifocaux et progressifs, 100% Santé.", "c-green"),
    ("lunettes-de-soleil/", "Lunettes de soleil", "À votre vue ou non, clips pour la conduite.", "c-orange"),
    ("lunettes-enfants/", "Lunettes enfants", "Pour tous les âges, à essayer avec votre enfant.", "c-coral"),
    ("lentilles-de-contact/", "Lentilles de contact", "Adaptation, renouvellement, produits d'entretien.", "c-blue"),
    ("lunettes-de-sport/", "Lunettes de sport", "Piscine, vélo, running, tir sportif.", "c-rust"),
    ("lunettes-sur-mesure/", "Lunettes sur mesure", "Avec Loumy, une monture qui n'existe qu'à vous.", "c-brown"),
    ("reparation-ajustement-lunettes/", "Réparation et ajustement", "Réglage gratuit, réparation, nettoyage aux ultrasons.", "c-green"),
]

# Marques : (nom, précision, magasins, catégories, fabrication française)
# magasins : "both" | "passage" | "bias" ; catégories : vue, soleil, enfant, sport
BRANDS = [
    ("Loumy", "Lunetier né à Montauban · fait main, sur mesure", "both", ["vue", "soleil"], True),
    ("Tavat", "", "passage", ["vue", "soleil"], False),
    ("Brett", "", "passage", ["vue", "soleil"], False),
    ("Tiwi", "", "both", ["vue", "soleil"], False),
    ("Marlone", "", "passage", ["vue"], True),
    ("Bondet", "", "bias", ["vue"], True),
    ("Victoire Daqui", "", "bias", ["vue"], True),
    ("Lafont Enfant", "", "passage", ["enfant"], True),
    ("GIGIstudios", "Anciennement Gigi Barcelona", "bias", ["vue"], False),
    ("Etnia Barcelona", "", "both", ["vue", "enfant"], False),
    ("Chroma by Etnia Barcelona", "", "passage", ["vue"], False),
    ("French Retro", "", "both", ["vue", "soleil", "enfant"], False),
    ("Matttew", "", "both", ["vue"], False),
    ("Lool", "", "both", ["vue"], False),
    ("Vogue", "", "both", ["vue", "soleil"], False),
    ("Lancel", "", "both", ["vue", "soleil"], False),
    ("Ray-Ban", "", "both", ["vue", "soleil", "enfant"], False),
    ("Vicomte Arthur", "", "both", ["vue"], False),
    ("Ruud van Dyke", "", "both", ["vue"], False),
    ("Osmose Clip", "Clips aimantés à fixer sur la monture", "both", ["vue"], False),
    ("Ki ET LA", "", "both", ["soleil"], False),
    ("Chantal Thomass", "", "bias", ["vue"], False),
    ("Azzaro", "Dont Azzaro Homme", "bias", ["vue", "soleil"], False),
    ("Entourage of 7", "", "bias", ["vue"], False),
    ("Bellinger", "", "bias", ["vue"], False),
    ("Osmose", "", "bias", ["vue"], False),
    ("Guess", "", "bias", ["vue", "soleil"], False),
    ("Minima", "Et Minima Kids", "bias", ["vue", "enfant"], False),
    ("Polaroid", "", "bias", ["soleil"], False),
    ("Eleven Paris", "", "both", ["enfant"], False),
    ("Demetz", "Lunettes de piscine et équipements de sport à la vue", "both", ["sport"], False),
]
