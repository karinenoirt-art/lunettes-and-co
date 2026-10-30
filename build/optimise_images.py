"""Génère des versions WebP redimensionnées des photos de assets/img/ (les JPEG d'origine sont conservés).

Usage (Pillow requis, hors dépendances du build) :  python3 build/optimise_images.py
Sorties : <nom>-480.webp, <nom>-800.webp, <nom>-1200.webp (seulement les largeurs inférieures à l'original).
build.py ajoute ensuite srcset/sizes aux <img> dont les fichiers WebP existent.
"""

import glob
import os

from PIL import Image

IMG = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "img")
WIDTHS = (480, 800, 1200)
QUALITY = 80

before = after = 0
for path in sorted(glob.glob(os.path.join(IMG, "*.jpg"))):
    name = os.path.splitext(os.path.basename(path))[0]
    im = Image.open(path)
    before += os.path.getsize(path)
    for w in WIDTHS:
        if w >= im.width:
            continue
        out = os.path.join(IMG, f"{name}-{w}.webp")
        im.resize((w, round(im.height * w / im.width)), Image.LANCZOS).save(out, "WEBP", quality=QUALITY, method=6)
        after += os.path.getsize(out)
print(f"JPEG d'origine : {before // 1024} Ko ; WebP générés : {after // 1024} Ko")
