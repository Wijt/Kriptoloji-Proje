from textwrap import wrap
from pprint import pprint
import random

def shuffleMe(liste, sira):
    yeniListe=[]
    for i in range(0,len(liste)):
        esitParcaliBlok = wrap(liste[i], int(256/len(sira)))
        yeniDizilim = esitParcaliBlok.copy()
        for i in sira.keys():
            yeniDizilim[i-1] = esitParcaliBlok[sira[i]-1]
        yeniListe.append("".join(yeniDizilim))
    return yeniListe

def cevir(liste, sira):
    yeniListe=[]
    for i in range(0,len(liste)):
        esitParcaliBlok = wrap(liste[i], int(256/len(sira)))
        yeniDizilim = esitParcaliBlok.copy()
        for i in sira.values():
            yeniDizilim[i-1] = esitParcaliBlok[sira[i]-1]
        yeniListe.append("".join(yeniDizilim))
    return yeniListe



arr = ['0001001110111100001010101010100101001011110001001111100100000100100110010010011010011000111001101101010000111011000001101111101110111111010001001101010000101010011001101101100101100111000110011011011011010111111101101110010011101100010000111101010101010110']
karistir = shuffleMe(arr, anahtar1)
duzgun = cevir(karistir, anahtar1)
pprint(karistir)
pprint(duzgun)

#pprint(shuffleMe(arr, ))


