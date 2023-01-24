import os
import sys
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

BLOCKSIZE = 16

def byteLen(s):
    return len(s.decode('utf-8'))

def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])


def encrypt(file, key, iv):
    # Read plaintext
    with open(file, 'rb') as f:
        plaintext = f.read()
        
    # Create a new AES cipher ecb
    cipher_ecb = AES.new(key, AES.MODE_ECB)
    
    # Create a new AES cipher cbc
    cipher_cbc = AES.new(key, AES.MODE_CBC)
    
    #pad data
    header_bytes = plaintext[0:139]
    plaintext = plaintext[139:]
    paddedText = pad(plaintext, BLOCKSIZE)
    

    # Encrypt the plaintext and write it to a new file
    f = open("ciphertext_ecb.bmp", 'wb')
    f_cbc = open("ciphertext_cbc.bmp", 'wb')
    f.write(header_bytes)
    f_cbc.write(header_bytes)
    for i in range(0, len(paddedText), BLOCKSIZE):
        curTxt = paddedText[i:i+BLOCKSIZE]
        
        #ecb
        ciphertext_ecb = cipher_ecb.encrypt(curTxt)
        f.write(ciphertext_ecb)
                
        #cbc
        if(i == 0):
            XOR_text = byte_xor(curTxt, iv)    
        else:
            XOR_text = byte_xor(curTxt, ciphertext_cbc) 
        ciphertext_cbc = cipher_cbc.encrypt(XOR_text)
        f_cbc.write(iv)
     
    f.close()
    f_cbc.close()


key = get_random_bytes(16)
iv = get_random_bytes(16)
encrypt("mustang.bmp", key, iv)
