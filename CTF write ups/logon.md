# picoCTF — Factory Login (Broken Authentication) Write-Up

## Challenge Overview

**Challenge:** Factory Logon  
**Goal:** Log in as Joe and find what the factory has been hiding.  

The hint given was: *Hmm it doesn't seem to check anyone's password, except for Joe's?*

When attempting to log in as **Joe**, the application responds:

*“I'm sorry Joe's password is super secure. You're not getting in that way.”*

However, logging in as any other user succeeds regardless of the password entered.

This immediately suggests flawed authentication logic.


## Initial Analysis

After logging in as a random user (`jake`), the server response included:

Set-Cookie: password=123; Path=/
Set-Cookie: username=jake; Path=/
Set-Cookie: admin=False; Path=/
Location: /flag


Key observations:

- Authentication data is stored directly in cookies.
- The server sets:
  - `username`
  - `password`
  - `admin`
- The user is redirected to `/flag` after login.
- There is no evidence of secure server-side session validation.

This indicates that the application trusts client-side cookies for authentication and authorization.


## Vulnerability Identified

### Broken Access Control via Cookie Tampering

The application stores the authorization flag (`admin`) inside a browser cookie:

admin=False

Because cookies are stored client-side, they can be modified by the user.

If the server trusts this value without verification, privilege escalation becomes trivial.

This is a textbook example of:

- Broken Access Control  
- Client-side authentication trust  
- Insecure authorization design  


## Exploitation Steps

### Step 1 — Log in as any User(not Joe)

Example:

Username: jake
Password:123

Login succeeds and redirects to `/flag`.


### Step 2 — Inspect Cookies

Open browser DevTools:

Application → Cookies

Cookies set by the server:

username=jake
password=123
admin=False

### Step 3 — Modify Authorization Cookie

Manually change:

admin=False


to:

admin=True


Optionally, change:

username=jake


to another value (`Joe`).


### Step 4 — Refresh the Page

After modifying the cookies, refresh `/flag`.

Because the server trusts the `admin` cookie value, it grants elevated access.

The flag is revealed.

## Why the Attack Worked

The backend likely performs checks similar to:

```python
username = request.cookies.get("username")
admin = request.cookies.get("admin")

if admin == "True":
    return flag
```
Instead of:

**Storing session data securely on the server

**Validating permissions against a database

**Signing or encrypting session cookies

By trusting client-controlled data, the application allows privilege escalation through simple cookie modification.

## Security Takeaways
Never trust client-side data.

Do not store authorization flags in plaintext cookies.

Authentication and authorization must be validated server-side.

Use secure, signed session tokens.

Always implement proper access control checks.

## Skills Demonstrated
**Authentication logic analysis

**HTTP response inspection

**Cookie inspection and manipulation

**Privilege escalation

**Identifying broken access control vulnerabilities

## Disclaimer

This write-up is for educational purposes only and documents a legal Capture-The-Flag (CTF) challenge. No real systems or data were harmed.

## Challenge Link:
https://play.picoctf.org/practice/challenge/46?category=1&page=2
