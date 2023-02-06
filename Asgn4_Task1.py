import numbers
import string
import sys
from Crypto.Util import number
import random
import hashlib
import bcrypt

#hash function for strings
def Hash_sha256(s : str):
    hash= hashlib.sha256(bytes(s, 'utf-8')).digest()
    hash = hash.hex()
    return hash

#Part A
userData = "hello"
hash = Hash_sha256(userData)
print("PartA Hash:")
print(hash)

#Part B
string_1 = '101010101'
string_2 = '101010100'
print("PartB")
print("Hash String 1:", Hash_sha256(string_1))
print("Hash string 2:", Hash_sha256(string_2))

#Part C
s1 = "Hello"
def FindC(s1: str):
    hash_s1 = Hash_sha256(s1)[0:4]
    s2 = ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=5))
    hash_s2 = Hash_sha256(s2)[0:4]
    while(hash_s1 != hash_s2):
        s2 = ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=5))
        hash_s2 = Hash_sha256(s2)[0:4]

    return s1, s2


print("Part C Hash collision:")
collision = FindC(s1)
print(collision, Hash_sha256(s1)[0:4], Hash_sha256(collision[1])[0:4])
