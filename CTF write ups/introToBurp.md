# picoCTF — Intro to Burp Write-Up

## Challenge Overview

This challenge introduces the basics of **Burp Suite** and HTTP request manipulation.

After launching the instance, we are presented with a **registration page**.  
Once the form is submitted, we are redirected to a page requesting a **one-time password (OTP)**.

The goal is to inspect and modify requests using Burp Suite to retrieve the flag.

## Step 1: Register an Account

After launching the instance:

1. I visited the provided URL.
2. Filled in the registration form with random details.
3. Submitted the form.
4. Was redirected to an OTP verification page.

## Step 2: Intercept the OTP Request

The hint said:

> “Look at the requests in Burp and try malformed ones.”

So I:

- Opened Burp Suite
- Turned Intercept ON
- Submitted an OTP value

The intercepted request looked like:

POST /dashboard HTTP/1.1
...
Content-Type: application/x-www-form-urlencoded

otp=100


The server responded with:

Invalid OTP


The request body only contained `otp=100`, and the response contained no useful information.

Nothing obvious appeared vulnerable in this request alone.


## Step 3: Inspect the Registration Request

Since the OTP request showed nothing interesting, I went back and examined the initial registration request in Burp.

While inspecting it, I discovered a parameter:

csrf_token=<REDACTED>


This CSRF token was included during signup.

However, I noticed something important:

- The OTP request did NOT include a CSRF token.
- The server might still expect it.

## Step 4: Modify the OTP Request in Repeater

I:

1. Sent the OTP request to **Burp Repeater**
2. Added the previously copied `csrf_token`
3. Modified the request body to:

csrf_token=<REDACTED>


4. Sent the modified request

Instead of receiving “Invalid OTP,” the server returned:

picoCTF{REDACTED_FLAG}


Flag successfully retrieved.


## Why the Attack Worked

The application likely required a valid **CSRF token** to process authenticated or state-changing requests.

However:

- The OTP form did not automatically include the CSRF token.
- The backend validation expected it.
- The frontend did not enforce it properly.
- By manually adding the token to the OTP request, we satisfied the server’s validation logic.

This indicates improper or inconsistent CSRF validation implementation.

The server trusted the presence of a valid CSRF token without ensuring it was correctly bound to the OTP flow.

## Security Takeaways

1. **CSRF tokens must be enforced consistently**
   - If a route requires a token, the frontend must properly include it.
   - The backend should strictly validate it.

2. **Security should never rely on frontend behavior**
   - Attackers can modify requests using tools like Burp.

3. **Always validate state transitions server-side**
   - If OTP verification depends on session state, enforce it clearly.

4. **Manual request manipulation is powerful**
   - Many vulnerabilities exist because developers assume requests won’t be altered.


## Skills Demonstrated

- Using Burp Suite Intercept
- Sending requests to Burp Repeater
- Inspecting HTTP POST requests
- Identifying hidden parameters (CSRF tokens)
- Modifying request bodies
- Understanding CSRF protection mechanisms
- Basic web application logic analysis

## Disclaimer

This write-up is for educational purposes only and documents a legal Capture-The-Flag (CTF) challenge. No real systems or data were harmed.

## Challenge Link:  
https://play.picoctf.org/practice/challenge/419?page=3
