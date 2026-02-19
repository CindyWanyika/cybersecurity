#pip install pycryptodome

from math import gcd
from Crypto.Util.number import inverse, long_to_bytes

e = 65537

Ns = [ ]#N values collected

for i in range(len(Ns)):
    for j in range(i+1, len(Ns)):
        g = gcd(Ns[i], Ns[j])
        if g != 1:
            print("Shared prime found!")
            print("p =", g)
            print("Between N", i, "and N", j)
            exit()

print("No shared primes found.")