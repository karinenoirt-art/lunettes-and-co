"""Retouche des photos de Bias (test B validé par Karine le 03/11/2026) : correction locale, naturelle.

Usage : python3 build/retouche_bias.py photo.jpeg sortie.jpg
Équilibre les blancs sur les parties claires (80 % supérieurs de la luminance, correction partielle à 80 %), léger
éclaircissement (gamma 0,82), très légère chaleur, saturation +5 %. Jamais d'IA générative (Magnific relight a ajouté
des objets inexistants). Les originaux ne sont jamais écrasés. Ensuite : optimise_images.py pour les WebP.
"""
import sys
from PIL import Image, ImageEnhance


def correct(im):
    small = im.resize((200, 150))
    px = list(small.getdata())
    lum = sorted(sum(p) / 3 for p in px)
    thr = lum[int(len(lum) * 0.8)]
    bright = [p for p in px if sum(p) / 3 >= thr]
    ref = [sum(p[i] for p in bright) / len(bright) for i in range(3)]
    m = sum(ref) / 3
    g = [1 + 0.8 * (m / r - 1) for r in ref]
    g[0] *= 1.02
    g[2] *= 0.98
    luts = [[int(255 * min(1, i / 255 * g[c]) ** 0.82) for i in range(256)] for c in range(3)]
    return ImageEnhance.Color(im.point(luts[0] + luts[1] + luts[2])).enhance(1.05)


if __name__ == "__main__":
    src, dst = sys.argv[1:3]
    correct(Image.open(src).convert("RGB")).save(dst, quality=92)
