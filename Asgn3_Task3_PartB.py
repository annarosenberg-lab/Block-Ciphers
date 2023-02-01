from Crypto.Util import number
import random


#Alices Key generation
primeLen = 64
p = number.getPrime(primeLen)
q = number.getPrime(primeLen)
while p == q:
    q = number.getPrime(primeLen)
n = p * q
phi_n = (p-1) * (q-1)
e = 65537
d = pow(e, -1, phi_n)


#Bob chooses s and sends ciphertext
s = 19
ciphertext = pow(s, e, n)

#Mallory edits cipher text with F(c)
alteredC = pow(ciphertext * (2 ** e), 1, n)


#Mallory sends encrypted message to Alice and Alice decryptes with her private key
decryptedtext = pow(alteredC, d, n)
print("decryptedtext:", decryptedtext)

original = decryptedtext / 2
print("orignal s:", original)
