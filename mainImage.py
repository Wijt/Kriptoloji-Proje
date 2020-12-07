import pandas as pd
from PIL import Image
import numpy as np
from numpy import asarray
from textwrap import wrap
from pprint import pprint

def main():
    img = Image.open('Test.JPG')
    return

def encrypt(splittedList):
    reverseBits(splittedList)

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

def Binary2Decimal(Array, NumberOfBits):
    DecimalArray = []
    for i in range(0,len(Array),NumberOfBits):
        DecimalNum = 0
        for b in range(NumberOfBits):
            DecimalNum += Array[i+b]* (2**(NumberOfBits-b-1))
        DecimalArray.append(DecimalNum)
    return np.array(DecimalArray)

main()