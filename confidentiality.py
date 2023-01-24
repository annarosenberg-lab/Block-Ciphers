import os
import sys
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

BLOCKSIZE = 16

def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

def submit(userData, key, iv):
    userData = userData.replace(';', '%3B')
    userData = userData.replace('=', '%3D')    
    userData = "userid=456;userdata=" + userData   #pre append userid=456; userdata=
    userData = userData + ";session-id31337"       #append ;session-id31337
    print("\nUSER DATA:\n", userData, "\n")
    
    cipherInst = AES.new(key, AES.MODE_ECB)
    paddedText = pad(userData.encode(), BLOCKSIZE)          #pad the final string
    print("PADDED TEXT:\n", paddedText)
    
    for i in range(0, len(paddedText), BLOCKSIZE):
        curTxt = paddedText[i:i+BLOCKSIZE]
        if(i == 0):
            XOR_text = byte_xor(curTxt, iv)    
        else:
            XOR_text = byte_xor(curTxt, cipherText) 
        cipherText = cipherInst.encrypt(XOR_text)
        
    print("\nCIPHER TEXT:\n", cipherText, "\n")
    
    

    
    
#def verify(decryptStr, key, iv): 
    
    
    
key = get_random_bytes(16)
iv = get_random_bytes(16) 
userData = input("What is your string? ")
submit(userData, key, iv)
