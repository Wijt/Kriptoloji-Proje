import pandas as pd
import numpy as np
from textwrap import wrap
from pprint import pprint
from random import shuffle
import random

kacSifirEklendi=0

anahtar1 = {1:1, 2:2, 3:3, 4:4}
anahtar2 = "10110011000010011011101001100010001100100000100001101110010100100100010110000001100110000110010000010001001011001100101001110000"
anahtar3 = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8}

def main():
    metin = "hello"
    binaryDizisi, maksUzunluk = strToBin(metin)
    print("Şifrelenecek Metin:", metin)
    butunBinary = ''.join(map(str, binaryDizisi.tolist())) 
    print("Binary Karşılığı:", butunBinary)
    splitted = binarySplit256(butunBinary) 
    print("\n\n....Encrypt işlemi başlıyor....")
    
    global anahtar1,anahtar2,anahtar3
    anahtar1seed = [1,2,3,4]
    random.shuffle(anahtar1seed)
    for i in anahtar1.keys():
        anahtar1[i] = anahtar1seed.pop();

    anahtar3seed = [1,2,3,4,5,6,7,8]
    random.shuffle(anahtar3seed)
    for i in anahtar3.keys():
        anahtar3[i] = anahtar3seed.pop();

    #sifreliMetin = encrypt(splitted)
    #decrypt(sifreliMetin)

def encrypt(splittedList):
    global anahtar1,anahtar2,anahtar3

    anahtar1seed = [1,2,3,4]
    random.shuffle(anahtar1seed)
    for i in anahtar1.keys():
        anahtar1[i] = anahtar1seed.pop();

    anahtar3seed = [1,2,3,4,5,6,7,8]
    random.shuffle(anahtar3seed)
    for i in anahtar3.keys():
        anahtar3[i] = anahtar3seed.pop();

    reversedList = reverseBits(splittedList)
    print("Tersine çevrildi:\n", "".join(reversedList),sep="")
    shuffled = shuffleMe(reversedList, anahtar1, False)
    print("\nİlk karıştırma:\n", "".join(shuffled),sep="")
    pprint(shuffleMe(shuffled, anahtar1, True))
    anahtar2 = rand_key(128)
    xordanGecmis = xor(shuffled, anahtar2)
    print("\nBloklar XOR'dan geçirildi:\n", "".join(xordanGecmis),sep="")
    shuffled2 = shuffleMe(xordanGecmis, anahtar3, False)
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
    shuffled2 = shuffleMe(sifreliMetin, anahtar3, True)
    print("Sonuç: ", "".join(shuffled2),"\n\n", sep="")
    pprint(shuffled2)
    print("XOR geri alınıyor:\n")
    xordanGecmis = xor(shuffled2, anahtar2)
    pprint(xordanGecmis)
    print("Sonuç:\n", "".join(xordanGecmis),"\n\n", sep="")
    
    print("\nİlk karıştırma geri alınıyor:\n")
    shuffled = shuffleMe(xordanGecmis, anahtar1, True)
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

def shuffleMe(liste, sira, duzelt):
    if not duzelt:
        yeniListe=[]
        for i in range(0,len(liste)):
            esitParcaliBlok = wrap(liste[i], int(256/len(sira)))
            yeniDizilim = esitParcaliBlok.copy()
            for i in sira.keys():
                yeniDizilim[i-1] = esitParcaliBlok[sira[i]-1]
            yeniListe.append("".join(yeniDizilim))
        return yeniListe
    else:
        yeniListe=[]
        for i in range(0,len(liste)):
            esitParcaliBlok = wrap(liste[i], int(256/len(sira)))
            yeniDizilim = esitParcaliBlok.copy()
            siralianahtar = dict(sorted(sira.items(), key=lambda item: item[1]))
            for i in siralianahtar.keys():
                yeniDizilim[siralianahtar[i]-1] = esitParcaliBlok[i-1]
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
    

main()

# 0001101001110001100010101100100110011100000111010110011101011111000110000101101011110101111000011001000001111100000111111001011011100101100011100111010100110110000000111110001010011000101000001001100111101111001111010101100011100111101001010000101000011110
# 01100111000001110101100111010111111001100111101111001111010101100010010000011111000001111110010110