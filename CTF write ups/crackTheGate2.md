# Crack the Gate 2 – Write-Up

## Challenge Overview

The login system was upgraded with a basic rate-limiting mechanism that blocks repeated failed login attempts from the same source.  

We were given:

- Known email: `ctf-player@picoctf.org`
- A password list
- Hints suggesting the system trusts user-controlled headers
- A reminder to investigate `X-Forwarded-For`

Goal:
- Bypass rate limiting
- Successfully log in
- Retrieve the hidden secret


## Vulnerability Analysis

### 1. Rate Limiting by IP Address

The application blocks repeated failed login attempts based on the client’s IP address. After several incorrect passwords, further attempts are denied.

This indicates:
- The server tracks login failures
- The tracking is tied to the perceived client IP


### 2. Trusting `X-Forwarded-For`

The hint suggested examining:
X-Forwarded-For

This HTTP header is commonly used when applications are deployed behind reverse proxies. It is meant to indicate the original client’s IP address.

However:
- It is fully controlled by the client
- If the backend blindly trusts it
- It can be spoofed

If the rate-limiting mechanism uses request.headers["X-Forwarded-For"] instead of the actual remote address, then the protection can be bypassed.

## Exploitation Steps

### Step 1: Intercept the Login Request

Using Burp Suite:

1. Intercepted the `POST /login` request
2. Observed the JSON body:

```json
{
  "email": "ctf-player@picoctf.org",
  "password": "123"
}
```

Sent the request to Repeater

## Step 2: Add the X-Forwarded-For Header

Modified the request to include:

X-Forwarded-For: 1.2.3.4

This caused the server to treat the request as coming from a new IP address.

### Step 3: Rotate Fake IP Addresses

For each password attempt:

Kept the email constant

Changed the password from the provided list

Rotated the X-Forwarded-For value

Example sequence:

X-Forwarded-For: 1.1.1.1
X-Forwarded-For: 2.2.2.2
X-Forwarded-For: 3.3.3.3
X-Forwarded-For: 4.4.4.4

The IPs did not need to be real — only different.

Because the rate limit was tied to the perceived IP:

Each attempt appeared to come from a new source

The lockout mechanism was bypassed

### Step 4: Identify Successful Login

Eventually, one password returned a different server response, indicating successful authentication and revealing the hidden secret.

## Why the Attack Worked

The server:

Trusted a user-controlled header

Used it for rate limiting

Did not validate whether the request passed through a trusted proxy

This allowed IP spoofing via X-Forwarded-For, completely bypassing the intended restriction.

## Security Takeaways

Never trust X-Forwarded-For directly from clients.

Only trust forwarded headers from verified reverse proxies.

Rate limit per account as well as per IP.

Implement exponential backoff or CAPTCHA after multiple failures.

Validate and sanitize all client-controlled headers.

## Skills Demonstrated

HTTP request interception

Header manipulation

Understanding reverse proxy behavior

Rate-limit bypass techniques

Manual brute-force methodology using Burp Repeater

Identifying improper trust boundaries in web applications

## Disclaimer

This write-up is for educational purposes only and documents a legal Capture-The-Flag (CTF) challenge. No real systems or data were harmed.

## Challenge Link:
https://play.picoctf.org/practice/challenge/46?category=1&page=2