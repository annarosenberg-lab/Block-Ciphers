import os
import sys
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

BLOCKSIZE = 16

def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

def submit(userData, key, iv):
    userData = userData.replace(';', '%3B')
    userData = userData.replace('=', '%3D')    
    userData = "userid=456;userdata=" + userData   #pre append userid=456; userdata=
    userData = userData + ";session-id31337"       #append ;session-id31337
    print("\nUSER DATA:\n", userData, "\n")

    paddedText = pad(userData.encode(), BLOCKSIZE)          #pad the final string
    print("PADDED TEXT:\n", paddedText)
    
    cipherText = ""
    for i in range(0, len(paddedText), BLOCKSIZE):
        curTxt = paddedText[i:i+BLOCKSIZE]
        if(i == 0):
            XOR_text = byte_xor(curTxt, iv)    
        else:
            XOR_text = byte_xor(curTxt, cipherText) 
        cipherText = cipherInst.encrypt(XOR_text)
        print("\nCIPHER TEXT:\n", cipherText, "\n")
        
        #cipherText = cipherText.append(cipherInst.encrypt(XOR_text))
        
    
    
    slayORnoSlay = verify(cipherText, key, iv)
    
    
def verify(cipherText, key, iv): 
    plaintext = unpad(verifyCipherInst.decrypt(cipherText), BLOCKSIZE)
    print(plaintext)
    '''plaintext = ""
    for i in range(0, len(cipherText), BLOCKSIZE):
        curCipherTxt = cipherText[i: i+BLOCKSIZE]
        curCipherTxt_Decrypt = cipherInst.decrypt(curCipherTxt)
        if(i == 0):
            XOR_text = byte_xor(curCipherTxt_Decrypt, iv)
        else:
            XOR_text = byte_xor(curCipherTxt_Decrypt, lastCipher) 
        lastCipher = curCipherTxt
        plaintext = plaintext + XOR_text'''
    
            
    
    
    
key = get_random_bytes(16)
iv = get_random_bytes(16) 
cipherInst = AES.new(key, AES.MODE_ECB)
verifyCipherInst = AES.new(key, AES.MODE_CBC, iv)
userData = input("What is your string? ")
submit(userData, key, iv)
