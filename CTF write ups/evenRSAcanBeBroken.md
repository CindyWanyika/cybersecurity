# picoCTF — Even RSA can be broken(RSA Weak Prime Generation) Write-Up

## Challenge Overview

We are given a remote service that provides:

- N (RSA modulus)
- e (public exponent)
- ciphertext (encrypted flag)

We are told:

> “Can you decrypt it with just N & e?”

We are also provided with the source code used to generate the RSA keys.

This challenge focuses on:

- RSA fundamentals  
- Weak prime generation  
- GCD attacks  
- Breaking improperly implemented cryptography  

NOTE: The flag has been intentionally redacted in this write-up.

## Step 1: Inspect the Source Code

The provided code generates the RSA key:

```python
pubkey, _privkey = gen_key(1024)
```

Inside gen_key:

p, q = get_primes(k//2)
N = p*q
d = inverse(e, (p-1)*(q-1))


Important observation:

The primes are generated using a custom function:

from setup import get_primes

This immediately suggests a possible flaw in prime generation.

## Step 2: Follow the Hint

The hint says:

“Try comparing N across multiple requests.”

So I connected to the service multiple times:

nc verbal-sleep.picoctf.net <port>

Each connection returned a new value of:

N

ciphertext

I collected several N values.

## Step 3: Compute GCD Between Moduli

If two RSA moduli share a prime:

N1​=p×q1​​

N2​=p×q2​

Then:

gcd(N1​,N2​)=p

I wrote a script to compute the GCD between every pair of collected moduli(computeGCDPairs.py).

The result:

Shared prime found!
p = 2

This occurred for every pair.

***Critical Discovery***

Every modulus was divisible by 2.

That means:

N=2×q

This is a risky RSA flaw.

In proper RSA:

* Both primes must be large

* Both primes must be odd

* 2 must NEVER be used

The custom get_primes() function was incorrectly generating 2 as a prime factor.

## Step 4: Factor N

Since:
N=2×q

Factoring becomes easy:

p = 2
q = N // 2
## Step 5: Compute φ(N)
ϕ(N)=(p−1)(q−1)

Since p = 2:

ϕ(N)=(1)(q−1)=q−1

## Step 6: Compute Private Key and Decrypt
(from breakRSA.py)
```python
from Crypto.Util.number import inverse, long_to_bytes

N = <N_here>
e = 65537
c = <ciphertext_here>

p = 2
q = N // 2

phi = (p-1)*(q-1)
d = inverse(e, phi)

m = pow(c, d, N)
print(long_to_bytes(m))
```

This successfully decrypted the ciphertext and revealed the flag:

picoCTF{REDACTED}

## Why the Attack Worked

RSA security depends on the difficulty of factoring N.

However:

* One of the primes was 2

* Factoring N was immediate

* No advanced attacks were required

* This completely breaks RSA.

## Security Takeaways

* RSA primes must be large and randomly generated.

* Never implement custom prime generators unless absolutely necessary.

* Both primes must be odd.

* Small implementation mistakes completely destroy cryptographic security.

* Always rely on well-tested cryptographic libraries.

## Skills Demonstrated

* RSA fundamentals

* GCD attack

* Prime factorization

* Euler’s Totient calculation

* Modular inverse computation

* Practical RSA decryption

## Disclaimer

This write-up is for educational purposes only and documents a legal Capture-The-Flag (CTF) challenge. No real systems or data were harmed.

## Challenge Link

picoCTF Practice Platform
(https://play.picoctf.org/practice/challenge/470?category=2&page=1)