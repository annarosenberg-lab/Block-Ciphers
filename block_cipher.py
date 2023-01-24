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
        curTxt = paddedText[i:i+BLOCKSIZE]
        curXOR_cbc_Arr = []
        if(i == 0):        
            #curXOR_cbc = hex(iv) ^ hex(paddedText[i:i+BLOCKSIZE])            
            #new = [chr(ord(a) ^ ord(b)) for a,b in zip(iv, paddedText[i:i+BLOCKSIZE])]
            for cur in range(0, 16):            
                curXOR_cbc_Arr.append(chr(iv[cur] ^ curTxt[cur]))
        else:
            for cur in range(0, 16):            
                curXOR_cbc_Arr.append(chr(curXOR_cbc_Arr[cur] ^ curTxt[cur]))
            
        curXOR_cbc = "".join(curXOR_cbc_Arr)
        ciphertext_cbc = cipher_cbc.encrypt(curXOR_cbc)
        curXOR_cbc_Arr.clear()
        f_cbc.write(ciphertext_cbc)
     
    f.close()
    f_cbc.close()


key = get_random_bytes(16)
iv = get_random_bytes(16)
encrypt("cp-logo.bmp", key, iv)
