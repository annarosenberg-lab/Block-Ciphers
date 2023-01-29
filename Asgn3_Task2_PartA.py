import os
import sys
from Crypto.Cipher import AES
import random
import hashlib
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes



#select prime number
q = int('B10B8F96A080E01DDE92DE5EAE5D54EC52C99FBCFB06A3C69A6A9DCA52D23B616073E28675A23D189838EF1E2EE652C013ECB4AEA906112324975C3CD49B83BFACCBDD7D90C4BD7098488E9C219A73724EFFD6FAE5644738FAA31A4FF55BCCC0A151AF5F0DC8B4BD45BF37DF365C1A65E68CFDA76D4DA708DF1FB2BC2E4A4371', 16)
#select primitive root of q
a = int('A4D1CBD5C3FD34126765A442EFB99905F8104DD258AC507FD6406CFF14266D31266FEA1E5C41564B777E690F5504F213160217B4B01B886A5E91547F9E2749F4D7FBD7D3B9A92EE1909D0D2263F80A76A6A24C087A091F531DBF0A0169B6A28AD662A4D18E73AFA32D779D5918D08BC8858F4DCEF97C2A24855E6EEB22B3B2E5', 16)
#Alice key generation
randomA = random.randint(1, 36)
PublicKeyA = int(pow(a, randomA, q))
#Bob key generation
randomB = random.randint(1, 36)
PublicKeyB = int(pow(a, randomB, q))

#Malory Modifies ALice and Bob's public keys
PublicKeyA = q
PublicKeyB = q

#Alice's secrete key
keyA = int(pow(PublicKeyB, randomA, q))
keyA = keyA.to_bytes(sys.getsizeof(keyA), "little")
hashKeyA = hashlib.sha256(keyA).digest()[0:16]
#Bob's secrete key
keyB = int(pow(PublicKeyA, randomB, q))
keyB = keyB.to_bytes(sys.getsizeof(keyB), "little")
hashKeyB = hashlib.sha256(bytes(keyB)).digest()[0:16]


iv = get_random_bytes(16) 

#messages
m0 = b'hi bob'
m1 = b"hello Alice"
m0 = pad(m0, 16)
m1 = pad(m1, 16)

cipher_A = AES.new(hashKeyB, AES.MODE_CBC, iv)
cipher_B = AES.new(hashKeyA, AES.MODE_CBC, iv)
c0 = cipher_A.encrypt(m0)
c1 = cipher_B.encrypt(m1)

decrypt_A = AES.new(hashKeyB, AES.MODE_CBC, iv)
decrypt_B = AES.new(hashKeyA, AES.MODE_CBC, iv)

#alice decrypts bob's message
p0 = decrypt_A.decrypt(c1)
p0 = unpad(p0, 16)
#bob decrypts alice message
p1 = decrypt_B.decrypt(c0)
p1 = unpad(p1, 16)


print("Plaintext sent to Alice:", p0, "Plaintext sent to Bob:", p1)


print("Did Bob and Alice compute the same key?", hashKeyA == hashKeyB)
