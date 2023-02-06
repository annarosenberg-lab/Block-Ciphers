import numbers
import string
import sys
from Crypto.Util import number
import random
import hashlib
from math import factorial

#hash function for strings
def Hash_sha256(s : str):
    hash= hashlib.sha256(bytes(s, 'utf-8')).digest()
    hash = hash.hex()
    return hash

#calculate the hamming distance
def hamming_distance(str1, str2):
    return sum([bin(ord(x) ^ ord(y)).count('1') for x, y in zip(str1, str2)])

#Part A
print("\nPartA Hash:")
userData = input("What would you like to hash? ")
hash = Hash_sha256(userData)
print(hash)
print("\n___________________________________________")

#Part B
print("\nPartB")
string_1 = '101010101'
string_2 = '101010100'
print("String1: ", string_1)
print("String2: ", string_2)
print("Hash String 1: ", Hash_sha256(string_1))
print("Hash string 2: ", Hash_sha256(string_2))
print("Hamming distance of strings: ", hamming_distance(string_1, string_2))
print("\n")

string_1 = "hello"
string_2 = "iello"
print("String1: ", string_1)
print("String2: ", string_2)
print("Hash String 1: ", Hash_sha256(string_1))
print("Hash string 2: ", Hash_sha256(string_2))
print("Hamming distance of strings: ", hamming_distance(string_1, string_2))
print("\n")

string_1 = "Anna&Tanya"
string_2 = "Anna&Tany`"
print("String1: ", string_1)
print("String2: ", string_2)
print("Hash String 1: ", Hash_sha256(string_1))
print("Hash string 2: ", Hash_sha256(string_2))
print("Hamming distance of strings: ", hamming_distance(string_1, string_2))
print("\n___________________________________________")

#Part C
s1 = "Hello"
def FindC(s1: str, byteLen):
    hash_dict = {}
    hash_s1 = Hash_sha256(s1)[0:byteLen]
    hash_dict[s1] = hash_s1 
    check = True
    while(check):
        s2 = ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=5))
        hash_s2 = Hash_sha256(s2)[0:byteLen]
        for x in hash_dict:
            if x!= s2 and hash_dict[x] == hash_s2:
                return x, s2, hash_dict[x], hash_s2
        if s2 not in hash_dict:
            hash_dict[s2] = hash_s2



print("\nPart C Hash collision:")
collision = FindC(s1, 7)
print(collision)
