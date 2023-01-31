from Crypto.Util import number

#Key generation
primeLen = 200
p = number.getPrime(primeLen)
q = number.getPrime(primeLen)
while p == q:
    q = number.getPrime(primeLen)
n = p * q
phi_n = (p-1) * (q-1)
e = 65537
d = pow(e, -1, phi_n)

publicKey = [e, n]
privateKey = [d, n]

#encryption 
#Bob encrypts a message with alice's public key
plaintext = "hello"
print("plaintext: ", plaintext)
plaintext = plaintext.encode('utf-8').hex()
plaintext = int(plaintext, 16)
ciphertext = pow(plaintext, e, n)
print("ciphertext:", ciphertext)

#decryption
#Bob sends encrypted message to Alice and Alice decryptes with her private key
decryptedtext = pow(ciphertext, d, n)
decryptedtext = hex(decryptedtext)[2:]
decryptedtext = bytearray.fromhex(decryptedtext)
decryptedtext = str(decryptedtext, 'utf-8')
print("decryptedtext:", decryptedtext)
