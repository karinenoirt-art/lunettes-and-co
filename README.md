# Lunettes & Co, site vitrine

Site statique de Lunettes & Co, opticien indépendant au Passage (près d'Agen) et à Bias (près de Villeneuve-sur-Lot).
Hébergé sur GitHub Pages. Adresse : https://www.lunettesandco.fr

**Statut : ébauche v1 (26/10/2026).** Le site est volontairement non indexé (`noindex` + `robots.txt`) tant que les textes
ne sont pas validés.

## Structure

- `index.html` et un dossier par page (`opticien-bias/`, `lunettes-de-vue/`, ...) : pages générées, servies telles quelles.
- `assets/` : feuille de style, script (menu, parcours de rendez-vous, filtre des marques), logo, photos.
- `build/` : générateur Python (sans dépendance).
  - `site_data.py` : magasins, horaires, liens Doctolib / OPC, liste des marques.
  - `pages.py` : textes des pages (repris de `Site-reference/`, fichiers 14 à 32).
  - `blocks.py` : blocs communs (boutons, cartes magasins, FAQ).
  - `build.py` : gabarit (en-tête, pied de page, fenêtre de rendez-vous, JSON-LD).

## Modifier le site

```bash
python3 build/build.py
```

Modifier les textes dans `build/`, relancer la commande, puis publier (commit + push). Ne pas modifier les `index.html` à la main :
ils sont réécrits à chaque génération.

## Avant la mise en ligne publique

1. Valider les textes (prix, 100% Santé, téléconsultation, paiement en 4 fois, « fabriqué en France ») par un professionnel.
2. Compléter : téléphone du Passage, horaires définitifs (fiches Google), parking du Passage, mentions légales (éditeur, SIRET), e-mail.
3. Fournir le logo 100% Santé et le logo Doctolib (emplacements en pointillés sur le site).
4. Ajouter de vrais avis Google sur l'accueil.
5. ~~Brancher le domaine~~ : fait (CNAME www.lunettesandco.fr, DNS OVH vers GitHub Pages).
6. Passer `DRAFT = False` dans `build/build.py`, retirer le `Disallow` de `robots.txt`, régénérer.
