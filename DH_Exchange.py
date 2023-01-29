import os
import sys
from Crypto.Cipher import AES
import random
from hashlib import sha256

#select prime number
q = 37
#select primitive root of q
a = 5
#Alice key generation
randomA = random.randint(1, 36)
PublicKeyA = (a**randomA) % a
#Bob key generation
randomB = random.randint(0, 36)
PublicKeyB = (a**randomA) % a
#Alice's secrete key
sA = (PublicKeyB**randomA) % q
sKey = sha256(sA, 16)
#Bob's secrete key
sB = (PublicKeyA**randomB) % q

print(sA, sB, sKey)
