# picoCTF — Cookie Monster / Insecure Cookie Handling Challenge Write-Up

## Challenge Overview
In this challenge, Cookie Monster claims to have hidden his top-secret cookie recipe somewhere on his website. The objective was to explore the web application and uncover the hidden recipe by identifying how the site handles cookies.

Based on the challenge description and hints, the flag was expected to be stored client-side, specifically within browser cookies.

The goal of the challenge was to:
- Explore the web application
- Inspect browser cookies
- Identify encoded sensitive data
- Decode the cookie value to reveal the hidden flag

**NOTE:** The flag has been intentionally redacted in this write-up.



## Tools Used
- Web browser — for navigating the website
- Browser Developer Tools — to inspect cookies
- Python — for decoding Base64-encoded data



## Step 1 — Exploring the Website
I began by visiting the website provided in the challenge description. The page included a login prompt, and the challenge hints referenced **cookies**, suggesting that authentication or hidden data might be handled using browser cookies.

This indicated that inspecting client-side storage would be important for solving the challenge.



## Step 2 — Inspecting Browser Cookies
After interacting with the website, I opened the browser’s Developer Tools and navigated to the **Application** tab.

Under the **Cookies** section for the website, I found a cookie with a suspicious value. The cookie appeared to contain encoded data rather than a simple session identifier.

Using the **“Show URL decoded”** option in the inspect panel revealed the cookie value in Base64-encoded.



## Step 3 — Decoding the Cookie Value
Since Base64 is a common encoding method in CTF challenges, I decoded the cookie value using Python:

```python
import base64

encoded = "REDACTED"
decoded = base64.b64decode(encoded).decode()
print(decoded)

(The python script can also be found in this repository under the name decodeCookie.py)

Decoding the cookie revealed readable text containing the flag.


## Step 4 — Retrieving the Flag

The decoded cookie value directly revealed the hidden cookie recipe, which was the flag for the challenge.

## Why This Attack Worked

The application stored sensitive information directly inside a client-side cookie. Although the data was encoded using Base64, it was not encrypted.

Key issues demonstrated:

Sensitive data stored in browser cookies

Base64 encoding used instead of encryption

Cookies fully accessible to the client

No server-side protection of secret data

Because cookies are controlled by the user, the secret could be easily extracted by inspecting and decoding the cookie value.

## Security Takeaways

Sensitive data should never be stored directly in client-side cookies

Base64 encoding does not provide security

Cookies should store only session identifiers, not secrets

Sensitive information should be stored and validated server-side

Proper cookie flags such as HttpOnly and Secure should be used

## Skills Demonstrated

Web application exploration

Browser developer tools usage

Identifying information disclosure vulnerabilities

Understanding insecure cookie handling

Decoding encoded data using Python

## Disclaimer

This write-up is for educational purposes only and documents a legal Capture-The-Flag (CTF) challenge. No real systems or data were harmed.

## Challenge Link

https://play.picoctf.org/practice/challenge/469?category=1&difficulty=1&page=1
