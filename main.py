import pandas as pd
import numpy as np
from textwrap import wrap
from pprint import pprint
from random import shuffle
import random

kacSifirEklendi=0

anahtar1 = [1,2,3,4]
anahtar2 = "10110011000010011011101001100010001100100000100001101110010100100100010110000001100110000110010000010001001011001100101001110000"
anahtar3 = [1,2,3,4,5,6,7,8]

def main():
    metin = "hello"
    binaryDizisi, maksUzunluk = strToBin(metin)
    print("Şifrelenecek Metin:", metin)
    butunBinary = ''.join(map(str, binaryDizisi.tolist())) 
    print("Binary Karşılığı:", butunBinary)
    splitted = binarySplit256(butunBinary) 
    print("\n\n....Encrypt işlemi başlıyor....")
    sifreliMetin = encrypt(splitted)
    decrypt(sifreliMetin)

def encrypt(splittedList):
    global anahtar1,anahtar2,anahtar3
    random.shuffle(anahtar1)
    random.shuffle(anahtar3)
    reversedList = reverseBits(splittedList)
    print("Tersine çevrildi:\n", "".join(reversedList),sep="")
    shuffled = shuffleMe(reversedList, anahtar1)
    print("\nİlk karıştırma:\n", "".join(shuffled),sep="")
    anahtar2 = rand_key(128)
    xordanGecmis = xor(shuffled, anahtar2)
    print("\nBloklar XOR'dan geçirildi:\n", "".join(xordanGecmis),sep="")
    shuffled2 = shuffleMe(xordanGecmis, anahtar3)
    print("\nBloklar tekrar karıştırıldı:\n", "".join(shuffled2),sep="")
    tumMetin = ''.join(shuffled2)
    print("\nBinary olarak şifreli metin:\n", "".join(tumMetin),sep="")
    bitarray=list(map(int, tumMetin))
    npbitArray=np.array(bitarray)
    print("\nŞifreli metnin unicode karşılığı:\n", binToStr(npbitArray,8),sep="")
    print("\n\n---------------------Şifrelemede kullanılan anahtarlar: \n\n1. karıştırma anahtarı: ", anahtar1, "\nXOR key: ", anahtar2, "\n2. karıştırma anahtarı: ", anahtar3, sep="")
    return shuffled2

def decrypt(sifreliMetin):
    print("\n\n\n\nDecrypt işlemine başlanıyor........\n")
    pprint(sifreliMetin)
    print("İkinci karıştırma geri alınıyor:")
    shuffled2 = shuffleMe(sifreliMetin, anahtar1)
    print("Sonuç: ", "".join(shuffled2),"\n\n", sep="")
    pprint(shuffled2)
    print("XOR geri alınıyor:\n")
    xordanGecmis = xor(shuffled2, anahtar2)
    pprint(xordanGecmis)
    print("Sonuç:\n", "".join(xordanGecmis),"\n\n", sep="")
    
    print("\nİlk karıştırma geri alınıyor:\n")
    shuffled = shuffleMe(xordanGecmis, anahtar3)
    print("Sonuç:\n", "".join(shuffled2),"\n\n", sep="")

    print("\nBitleri çevirme işlemi geri alınıyor:\n")
    reversedBits = reverseBits(shuffled)
    print("Sonuç:\n", "".join(reversedBits),"\n\n", sep="")

def reverseBits(l):
    newList=[]
    for i in l:
        newList.append(i[::-1])
    return newList

def rand_key(p): 
    key1 = "" 
    for i in range(p): 
        temp = str(random.randint(0, 1)) 
        key1 += temp 
    return(key1) 

def shuffleMe(liste, sira):
    yeniListe=[]
    for i in range(0,len(liste)):
        esitParcaliBlok = wrap(liste[i], int(256/len(sira)))
        yeniDizilim = esitParcaliBlok.copy()
        for j in range(0,len(esitParcaliBlok)):
            yeniDizilim[(sira[j]-1)] = esitParcaliBlok[j]
        yeniListe.append("".join(yeniDizilim))
    return yeniListe
    
def xor(liste, key):
    keyUzunluk = len(key)
    for i in range(0, keyUzunluk):
        if key[i] == '0':
            key += '1'
        else:
            key += '0'
    xordanGecmis=[]
    for i in liste:
        CipherText = []
        j = 0
        for b in i:
            if (j == len(key)-1):
                CipherText.append(int(b) ^ int(key[j]))
                j = 0
            else:
                CipherText.append(int(b) ^ int(key[j]))
                j += 1
        xordanGecmis.append("".join(map(str, CipherText)))
    return xordanGecmis

def Decimal2Binary(Array):
    MaximumNum = Array.max()
    Binary = []
    while (MaximumNum != 0):
        Binary.append(MaximumNum % 2)
        MaximumNum = int(MaximumNum / 2)
    BinaryArray = []
    for I in Array:
        temp = []
        zeros = []
        while (I != 0):
            temp.append(I % 2)
            I = int(I/2)
        if (len(temp) < len(Binary)):
            for z in range(len(Binary) - len(temp)):
                zeros.append(0)
        BinaryArray.extend(zeros)
        BinaryArray.extend(temp[::-1])
    return np.array(BinaryArray), len(Binary)

def Binary2Decimal(Array, NumberOfBits):
    DecimalArray = []
    for i in range(0,len(Array),NumberOfBits):
        DecimalNum = 0
        for b in range(NumberOfBits):
            DecimalNum += Array[i+b]* (2**(NumberOfBits-b-1))
        DecimalArray.append(DecimalNum)
    return np.array(DecimalArray)

def strToBin(metin):
    metinDecimal = list(map(ord, metin))
    return Decimal2Binary(np.array(metinDecimal))

def binToStr(binaryDizisi, maksByteLen):
    decimalArr = Binary2Decimal(binaryDizisi, maksByteLen)
    return ''.join(list(map(chr, decimalArr)))

def binarySplit256(binaryArr):
    global kacSifirEklendi
    lenOfarr = len(binaryArr)
    fazlalikLen = lenOfarr % 256
    countOfZero = 256-fazlalikLen
    kendisi = binaryArr[:-fazlalikLen]
    fazlalik = binaryArr[-fazlalikLen:]
    sifirlar = "0" * countOfZero
    kacSifirEklendi=countOfZero
    lastStr=kendisi+sifirlar+fazlalik
    return list(wrap(lastStr,256))

def flatten(binaryArr):
    global kacSifirEklendi
    binaryArr[-1] = binaryArr[-1][kacSifirEklendi:]
    return "".join(binaryArr)
    """
    sonPart = binaryArr[-1]
    sondanOnceki= binaryArr[len(binaryArr)-2]
    print(wrap(sondanOnceki, maksBitLen))

    bolunmusSonPart = wrap(sonPart[::-1], maksBitLen)
    bolunmusSonPart = [i for i in bolunmusSonPart if i != ('0'*maksBitLen)] # 0000000 lar silindi
    sonuncuUzunluk = len(bolunmusSonPart[-1])
    if not ('1' in bolunmusSonPart[-1] ):
        del bolunmusSonPart[-1]
    bolunmusSonPart = reverseBits(bolunmusSonPart)
    if('1' in bolunmusSonPart[-1] ): # and len(bolunmusSonPart[-1])!=maksBitLen
        bolunmusSonPart[-1] = bolunmusSonPart[-1][-sonuncuUzunluk-1:]
    sifirlarSilinmisSon = "".join(bolunmusSonPart[::-1])
    
    binaryArr[-1] = sifirlarSilinmisSon
    """
    

main()

# 1101011101111011001001010001011001111110110001100110110001110010000000000000000000000000000000001101101011111001100000001111010011111111111111111111111111111111111101010111010001000101011010000010111110001101110001011001101011011010111110011000000011110100
# 11010001100101110110011011001101111