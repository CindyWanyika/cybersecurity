# picoCTF — Cookies Write-Up

## Challenge Overview

The webpage displays the message:

> “Who doesn't love cookies? Try to figure out the best one.”

The hint suggests that the challenge involves web browser

This challenge focuses on:

- Inspecting browser cookies  
- Modifying client-side data  
- Enumerating possible values  
- Understanding insecure server-side trust  


## Step 1: Inspect the Cookies

Opened the browser Developer Tools and navigated to:

Storage → Cookies


Found the following cookie:

Name: name
Value: -1


The value `-1` likely represents a default or uninitialized state.

This suggested that the cookie value might be used as an index to select a specific item.

## Step 2: Modify the Cookie Value

Edited the cookie value from:

-1 → 0


After refreshing the page, the content changed.

This confirmed:

- The server reads the cookie value
- The cookie controls what content is displayed


## Step 3: Enumerate Possible Values

Incremented the cookie value manually:

0 → 1 → 2 → 3 → ... → 18


At:

name = 18


The flag was revealed:

picoCTF{REDACTED}



## Why the Attack Worked

The server trusted a **client-controlled cookie value** to determine which item to display.

The backend likely used logic similar to:

```python
cookies = ["chocolate", "oreo", ...]
choice = int(request.cookies.get("name"))
return cookies[choice]
```
Because the cookie value was not validated or restricted, we were able to:

Modify it directly

Enumerate valid indexes

Access hidden content

This is a classic example of client-side trust vulnerability.

## Security Takeaways
* Never trust client-controlled data (including cookies)

* Validate and sanitize all user inputs server-side

* Do not rely on client-side values for access control

* Implement proper authorization checks

## Skills Demonstrated
* Web application analysis

* Browser DevTools usage

* Cookie tampering

* Enumeration techniques

* Understanding client-server trust boundaries

## Disclaimer

This write-up is for educational purposes only and documents a legal Capture-The-Flag (CTF) challenge. No real systems or data were harmed.

## Challenge Link:  
https://play.picoctf.org/practice/challenge/173?category=1&page=2
