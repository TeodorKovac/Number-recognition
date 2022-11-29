import glob
import itertools
import numpy as np
import cv2 as cv
import math

# Nastavení slovníku jednotlivých čísel
DIGITS_LOOKUP = {
    (1, 1, 1, 0, 1, 1, 1): 0,
    (0, 0, 1, 0, 0, 1, 0): 1,
    (1, 0, 1, 1, 1, 0, 1): 2,
    (1, 0, 1, 1, 0, 1, 1): 3,
    (0, 1, 1, 1, 0, 1, 0): 4,
    (1, 1, 0, 1, 0, 1, 1): 5,
    (1, 1, 0, 1, 1, 1, 1): 6,
    (1, 0, 1, 0, 0, 1, 0): 7,
    (1, 1, 1, 1, 1, 1, 1): 8,
    (1, 1, 1, 1, 0, 1, 1): 9
}


def getFilenames(exts):
    fnames = [glob.glob(ext) for ext in exts]
    fnames = list(itertools.chain.from_iterable(fnames))
    fnames.sort()
    return fnames

# Rozdělení a ořezání jednotlivých čísel
def segmentace(img):

    cisla = []
    kolikCisel = -1
    x = 0
    while x < img.shape[1]:
        if img[:, x].any():
            kolikCisel = kolikCisel + 1
            pomoc = np.zeros((img.shape[0], 1))
            while img[:, x].any():
                pomoc = np.hstack((pomoc, img[:, [x]]))
                x = x + 1
                y = 0
                pomoc1 = np.zeros(pomoc.shape[1])
            for y in range(0, pomoc.shape[0]):
                if (pomoc[y, :].any()):
                    pomoc1 = np.vstack([pomoc1, pomoc[y, :]])
            pomoc1 = pomoc1[1:, 1:]
            cisla.append(pomoc1)
        x = x + 1

    return cisla, kolikCisel

# Rozpoznání čísel
def recognizeNumber(img):
    (imgH, imgW) = img.shape
    if imgW < 60:
        digit = 1
        return digit
    (dH, dW) = (int(imgW * 0.15), int(imgH * 0.25))
    # Definice segmentů, které budeme kontrolovat. Dalo by se nastavit pečlivěji...
    segments = [
        ((0, 0), (dH, imgW)),  # top
        ((0, 0), (imgH//2, dW)),  # top-left
        ((0, imgW - dW), (imgH // 2, imgW)),  # top-right
        (((imgH // 2) - (dH // 2), 0), ((imgH // 2) + (dH // 2), imgW)),  # center
        ((imgH // 2, 0), (imgH, dH)),  # bottom-left
        ((imgH // 2, imgW - dW), (imgH, imgW)),  # bottom-right
        ((imgH - dH, 0), (imgH, imgW))  # bottom
    ]
    on = [0] * len(segments)
    # Iterace přes jednotlivé segmenty v obrázku
    for (i, ((yA, xA), (yB, xB))) in enumerate(segments):

        seg = img[yA:yB, xA:xB]
        total = cv.countNonZero(seg)
        area = (xB - xA) * (yB - yA)
        # Pokud je množství nenulových pixelů v segmentu vetší než 0.46 všech pixelů segmentu,
        # tak označím jako aktivní
        if total / float(area) > 0.46:
            on[i] = 1
        # Vyhledání čísla ze slovníku DIGITS_LOOKUP
    digit = DIGITS_LOOKUP[tuple(on)]
    return digit

