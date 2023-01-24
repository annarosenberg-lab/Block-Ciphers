import os
import sys
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

BLOCKSIZE = 16

def byteLen(s):
    return len(s.decode('utf-8'))


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
    for i in range(0, len(paddedText), BLOCKSIZE):
        #ecb
        ciphertext_ecb = cipher_ecb.encrypt(paddedText[i:i+BLOCKSIZE])
        f.write(ciphertext_ecb)
                
        #cbc
        if(i == 0):
            curXOR_cbc = iv ^ paddedText[i:i+BLOCKSIZE]
        else:
            curXOR_cbc = curXOR_cbc ^ paddedText[i:i+BLOCKSIZE]
        ciphertext_cbc = cipher_cbc.encrypt(curXOR_cbc)
        f_cbc.write(ciphertext_cbc)
     
    f.close()


key = get_random_bytes(16)
iv = get_random_bytes(16)
encrypt("cp-logo.bmp", key, iv)
