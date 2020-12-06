import pandas as pd
import numpy as np

def main():
    metin = "asdgşsdklgjlaksdğoakjsdflkhjasdklgja" #input("Şifrelenecek metni giriniz: ")
    binaryDizisi, maksUzunluk = strToBin(metin)
    splittedList = binarySplit256(''.join(map(str, binaryDizisi.tolist())))
    encrypt(splittedList)
    print()

def encrypt(splittedList):
    reverseBits(splittedList)
    print(splittedList)

def decrypt():
    print("decrypt")

def reverseBits(l):
    newList=[]
    for i in l:
        newList.append(i[::-1])
    return newList

def firstShuffle():
    print("firstShuffle")

def xor():
    print("xor")

def secondShuffle():
    print("firstShuffle")

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

def Binary2Decimal(Array,NumberOfBits):
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
    from textwrap import wrap
    lenOfarr = len(binaryArr)
    fazlalikLen = lenOfarr % 256
    countOfZero = 256-fazlalikLen
    kendisi = binaryArr[:-fazlalikLen]
    fazlalik = binaryArr[-fazlalikLen:]
    sifirlar = "0" * countOfZero
    lastStr=kendisi+sifirlar+fazlalik
    return list(map(list, wrap(lastStr,256)))

main()