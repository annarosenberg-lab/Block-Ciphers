import os
import sys
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad


submit(userStr, key, iv):
    
    
verify(decryptStr, key, iv):
    
    
key = get_random_bytes(16)
iv = get_random_bytes(16) 
userInput = input("What is your string?")
submit(userInput)
