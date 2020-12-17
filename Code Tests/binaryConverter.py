import pandas as pd
import numpy as np
import bitarray as ba

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



asd = 'ş'
asd = list(map(ord, asd))

a = np.array(asd)

imgBinary, numberOfBits = Decimal2Binary(a)

lenOfarr = len(imgBinary)
countOfPart = 1 + lenOfarr // 256
countOfZero = abs(lenOfarr - (256 * countOfPart))
print("uzunluk: ", lenOfarr, " Sıfır sayısı: ", countOfZero)


#imgBinary = np.hstack([[0]*countOfZero, imgBinary])
#imgBinary = np.array(np.array_split(imgBinary, 256)).transpose()
#b = pd.DataFrame(imgBinary)
#print(b)

ImgDecimalArray = Binary2Decimal(silinik, numberOfBits)
print(ImgDecimalArray)
dsa = list(map(chr, ImgDecimalArray))
print(dsa)
