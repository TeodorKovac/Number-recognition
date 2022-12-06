import cv2 as cv
import pomocneFunkce as pf
import glob
import os
import fourierDescriptors as fd
from scipy.ndimage import gaussian_filter

# 1) Předpokládám digitálně vytištěná čísla skládající se ze 7 segmentů, vyrovnaná,
# snadno rozpoznatelná od pozadí. (použil jsem fotky digitálního teploměru krbu - folder framesEasy)
#       - pokud by byla čísla orotovaná, tak např. pomocí horizontální projekce zjistíme úhel
#       nebo openCV minAreaRect() zjistí uhel rotace nejmenšího opsaného čtyřuhelníku
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

MIN_DESCRIPTOR = 10


if __name__ == '__main__':

    img = cv.imread("framesEasy/001.png")
    grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    (thresh, img) = cv.threshold(grayimg, 240, 255, cv.THRESH_BINARY)
    (cisla, kolikCisel) = pf.segmentace(img)
    for i in range(0, 2):
        A = cisla[i]
        digit1 = pf.recognizeNumber(A)
        deskriptory1 = fd.findDescriptor(A)
        deskriptory1 = deskriptory1[0:MIN_DESCRIPTOR]
        deskriptory1 = fd.normovani(deskriptory1)
        #deskriptory1 = fd.truncate_descriptor(deskriptory1, MIN_DESCRIPTOR)
        print(digit1)
        print(deskriptory1)
    #
    print("hotovo 001")
    img = cv.imread("framesEasy/002.png")
    grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    (thresh, img) = cv.threshold(grayimg, 240, 255, cv.THRESH_BINARY)
    (cisla, kolikCisel) = pf.segmentace(img)
    for j in range(0, 2):
        A = cisla[j]
        digit1 = pf.recognizeNumber(A)
        deskriptory1 = fd.findDescriptor(A)
        deskriptory1 = deskriptory1[0:MIN_DESCRIPTOR]
        deskriptory1 = fd.normovani(deskriptory1)
        #deskriptory1 = fd.truncate_descriptor(deskriptory1, MIN_DESCRIPTOR)
        print(digit1)
        print(deskriptory1)
    #
    print("hotovo 002")

    #for fileloc in glob.iglob(os.getcwd() + "/framesEasy/*.png"):
     #   img = cv.imread(fileloc)
      #  grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        # Eliminace šumu pomocí morfologie, konvoluce s Gaussovo filtrem
       # grayimg = gaussian_filter(grayimg, sigma=2)
        # Prahování nahodilou hodnotou 240, jinak možno použít např. Otsu(?)
       # (thresh, img) = cv.threshold(grayimg, 240, 255, cv.THRESH_BINARY)
       # print(fileloc)
        # Funkce pro segmentaci a rozdělení jednotlivých čísel
       # (cisla, kolikCisel) = pf.segmentace(img)
        # Vim, že budou tři, jinak iterace přes počet čísel
       # A = cisla[0]
       # digit1 = pf.recognizeNumber(A)
       # B = cisla[1]
       # digit2 = pf.recognizeNumber(B)
       # C = cisla[2]
       # digit3 = pf.recognizeNumber(C)
       # print(digit1, digit2, digit3)