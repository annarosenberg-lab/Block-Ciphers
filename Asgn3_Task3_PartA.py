from Crypto.Util import number
primeLen = 5
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
