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
    
    cipherText = bytearray()
    for i in range(0, len(paddedText), BLOCKSIZE):
        curTxt = paddedText[i:i+BLOCKSIZE]
        XOR_text = byte_xor(curTxt, iv) 
        cipherText.extend(cipherInst.encrypt(XOR_text))
        iv = cipherInst.encrypt(XOR_text)
    
    print("\nCIPHER TEXT:\n", cipherText, "\n")         
    
    slayORnoSlay = verify(cipherText, key, iv)
    if slayORnoSlay:
        print("\nOH NOOOO ADMIN FOUND")
    else:
        print("\nYEAHHHHH\n")
    
    
def verify(cipherText, key, iv): 
    byteFlip = input("Should we byte flip?(Y/N) ")
    if byteFlip == "Y":
        cipherText = flipByte(cipherText)
    #print("\ntype: /n", cipherText.decode('utf-8'))
    
    plaintext = verifyCipherInst.decrypt(cipherText)
    print("\nPLAIN DECRYPTED TEXT:\n", plaintext)
    
    plaintext = unpad(plaintext, BLOCKSIZE)
    
    #print("\nBYTE CHECK = \n", str(plaintext)[21])
    if "admin=true" in str(plaintext):
        return True
    return False

def flipByte(cipherText):
    changeBlock = cipherText[22:37]
    temp = bytes(";admin=true.....",'utf-8' )
    cipherTextTemp = cipherText
    block = bytes(b ^ a for a, b in zip(changeBlock, temp))
    cipherText = cipherTextTemp[:22] + block + cipherTextTemp[32:]
    
    print("\nNEW CIPHER TEXT: \n", cipherText, "\n")
    return cipherText

       
    
key = get_random_bytes(16)
iv = get_random_bytes(16) 
cipherInst = AES.new(key, AES.MODE_ECB)
verifyCipherInst = AES.new(key, AES.MODE_CBC, iv)
userData = input("What is your string? ")
submit(userData, key, iv)
