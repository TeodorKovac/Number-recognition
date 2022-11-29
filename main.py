import cv2 as cv
import pomocneFunkce as pf
import glob
from scipy.ndimage import gaussian_filter

# 1) Předpokládám digitálně vytištěná čísla uprostřed papíru, vyrovnaná,
# snadno rozpoznatelná od pozadí. (framesEasy jsou fotky teploty termostatu)
#       - pokud by byla čísla orotovaná, tak např. pomocí horizontální projekce zjistíme úhel
#       nebo openCV minAreaRect() zjistí uhel rotace nejmenšího opsaného čtyřuhelníku
#       nebo metoda Fourierovy deskriptory.
# 2) Převedení obrázku do grayscale, drobná eliminace šumu pomoci konvoluce Gaussovo filtrem.
# 3) Poté převedení do black&white prahováním.
#       - dalo by se použít metoda pro hledání prahu (Otsu?)...
# 4) Ořezání a segmentace jednotlivých čísel, zahodím černé řádky a sloupce mezi čísly.
# 5) Rozdělení čísel na jednotlivé segmenty a kontrola aktivity jednotlivých segmentů pro jednotlivá čísla
# 6) Párování s čísly ze slovníku

# ------------------------------------
# Pokud by čísla byla psaná různě, ručně, nejistý font
#       - Fourierovy deskriptory
#       - Neuronové sítě v případě trénovací množiny

if __name__ == '__main__':

    for fileloc in glob.iglob("/Users/petrkovac/PycharmProjects/uloha1/framesEasy/*.png"):
        img = cv.imread(fileloc)
        grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        # Eliminace šumu pomocí morfologie, konvoluce s Gaussovo filtrem
        grayimg = gaussian_filter(grayimg, sigma=2)
        # Prahování nahodilou hodnotou 240, jinak možno použít např. Otsu(?)
        (thresh, img) = cv.threshold(grayimg, 240, 255, cv.THRESH_BINARY)
        print(fileloc)
        # Funkce pro segmentaci a rozdělení jednotlivých čísel
        (cisla, kolikCisel) = pf.segmentace(img)
        # Vim, že budou tři, jinak iterace přes počet čísel
        A = cisla[0]
        digit1 = pf.recognizeNumber(A)
        B = cisla[1]
        digit2 = pf.recognizeNumber(B)
        C = cisla[2]
        digit3 = pf.recognizeNumber(C)
        print(digit1, digit2, digit3)