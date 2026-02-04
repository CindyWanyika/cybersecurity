# picoCTF — Weak Hashes Challenge Write‑Up

## Challenge Overview
In this challenge, a server reveals multiple password hashes one at a time and asks the user to crack them in order to access a hidden secret. Each stage uses a different hashing algorithm, increasing in cryptographic strength.

The goal of the challenge was to:
- Identify the hash type
- Crack the hash using appropriate tools
- Understand why certain hashes are insecure for password storage

NOTE: All cracked passwords and the final flag have been intentionally redacted in this write‑up.


## Tools Used
- Netcat (nc) — to interact with the remote service
- John the Ripper — for offline password cracking
- rockyou.txt — common password wordlist (preinstalled on Kali Linux)

## Step 1 — Connecting to the Server
The challenge begins by connecting to a remote service using Netcat:

nc verbal-sleep.picoctf.net <PORT>

The server then outputs password hashes one at a time and waits for the correct plaintext password before proceeding to the next stage.


## Step 2 — Hash Identification by Length
Before cracking any hash, the hash type was identified by examining its length:

32 hexadecimal characters  -> MD5  
40 hexadecimal characters  -> SHA‑1  
64 hexadecimal characters  -> SHA‑256  

This technique works because cryptographic hash functions produce outputs of fixed lengths.

## Step 3 — Cracking the MD5 Hash

### Identification
- 32 hex characters
- Unsalted
- Likely raw MD5

### Command Used
john --format=Raw-MD5 --wordlist=/usr/share/wordlists/rockyou.txt hash1.txt

### Result
- Password cracked successfully
- No secret revealed yet(intentional by challenge design)


## Step 4 — Cracking the SHA‑1 Hash

### Identification
- 40 hex characters
- Unsalted
- Raw SHA‑1

### Command Used
john --format=Raw-SHA1 --wordlist=/usr/share/wordlists/rockyou.txt hash2.txt

### Displaying the Result
john --show --format=Raw-SHA1 hash2.txt

### Result
- Password cracked successfully
- Still no secret revealed yet


## Step 5 — Cracking the SHA‑256 Hash

### Identification
- 64 hex characters
- Unsalted
- Raw SHA‑256

### Command Used
john --format=Raw-SHA256 --wordlist=/usr/share/wordlists/rockyou.txt hash3.txt

### Displaying the Result
john --show --format=Raw-SHA256 hash3.txt

### Result
- Password cracked successfully
- Secret revealed (flag redacted)


## Why This Attack Worked
Even though SHA‑256 is a strong cryptographic hash, it is not suitable for password storage when used incorrectly.

Key weaknesses demonstrated:
- No salting
- No key stretching
- Fast hash computation
- Weak, common passwords

These weaknesses allow attackers to perform rapid dictionary attacks using common wordlists.


## Security Takeaways
- MD5 is completely broken for password storage
- SHA‑1 is deprecated and insecure
- SHA‑256 is cryptographically strong but unsafe for password hashing

Passwords should instead be stored using:
- bcrypt
- scrypt
- argon2

These algorithms are intentionally slow and resistant to brute‑force attacks.


## Skills Demonstrated
- Hash identification by inspection
- Practical use of John the Ripper
- Understanding of password storage vulnerabilities
- Linux filesystem navigation
- Offline password attack methodology


## Disclaimer
This write‑up is for educational purposes only and documents a legal Capture‑The‑Flag (CTF) challenge. No real systems or credentials were harmed.


## Challenge Link
https://play.picoctf.org/practice/challenge/475?category=2&difficulty=1&page=1
