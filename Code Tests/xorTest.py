from textwrap import wrap
from pprint import pprint

def xor(liste, key):
    keyUzunluk = len(key)
    for i in range(0, keyUzunluk):
        if key[i] == '0':
            key += '1'
        else:
            key += '0'
    #key = list(map(int, key))
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

key = "1011001100001001101110100110001000110010000010000110111001010010010001011000000110011001001011001100101001110000"

arr = ['0001000000010001100011101010011100100011010110011000010011011101001100010011011100001000000011100110011001010011100110011010010001000000111001110011011110011010110001000000011001110111111000011110100011001010011011000001000000011101100011001010001000000111', '0001000000010001100011101010011100100011010110011000010011011101001100010011011100001000000011100110011001010011100110011010010001000000111001110011011110011010110001000000011001110111111000011110100011001010011011000001000000011101100011001010001000000111']
print(arr)
xordanGecmis = xor(arr, key)
print(xordanGecmis)
xordanGecmis = xor(xordanGecmis, key)
print(xordanGecmis)