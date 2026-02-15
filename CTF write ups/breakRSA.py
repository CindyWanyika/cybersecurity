#from Crypto.Util.number import inverse, long_to_bytes

N = "your N goes here"
e = 65537
c = "ciphertext goes here"

# since p = 2
p = 2
q = N // 2

phi = (p-1)*(q-1) 
d = inverse(e, phi)

m = pow(c, d, N)

print(long_to_bytes(m))

