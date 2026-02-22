# picoCTF Write-Up: dont-use-client-side  

## Challenge Overview

This challenge presents a “Secure Login Portal” that prompts the user to enter a password. The hint, *Never trust the client,* suggests that the vulnerability likely involves improper reliance on client-side logic for authentication.

The objective was to analyze how the login verification works and determine whether it could be bypassed or reversed.

## Vulnerability Analysis

After inspecting the page, nothing suspicious appeared in cookies or network traffic.  

However, viewing the page source revealed a JavaScript function named `verify()` responsible for password validation.

## Key findings:

- The variable `split` was set to `4`.
- The password was validated using multiple `substring()` checks.
- Each check compared a specific 4-character segment of the input.
- All expected values were hardcoded directly in the JavaScript.

This means the entire password structure was exposed in the frontend code. Since JavaScript executes in the browser, it can be read and analyzed by anyone.


## Exploitation Steps

1. Opened the login page.
2. Inspected the page source.
3. Located the `verify()` JavaScript function.
4. Observed that the password was divided into 4-character chunks.
5. Collected each hardcoded substring comparison.
6. Reordered the chunks based on their substring positions.
7. Reconstructed the full password.
8. Entered the reconstructed password into the form.

Authentication succeeded without any brute force or guessing.

## Why the Attack Worked

The attack worked because the application relied entirely on **client-side validation** for authentication.

Since:
- The password logic was implemented in JavaScript
- The expected values were hardcoded
- There was no server-side verification

An attacker could simply read the source code and reconstruct the correct password.

Client-side code should always be considered fully visible and modifiable.

## Security Takeaways

- Never rely solely on client-side authentication.
- Never store secrets in frontend JavaScript.
- Always perform sensitive validation on the server.
- Treat all client input as untrusted.
- Assume attackers can read and modify client-side code.

This challenge reinforces a fundamental web security principle:  
**The client cannot be trusted.**

## Skills Demonstrated

- Inspecting and analyzing page source
- Reading and understanding JavaScript logic
- Interpreting `substring()` operations
- Reconstructing structured input from conditional checks
- Identifying insecure authentication design
- Applying core web security principles

## Disclaimer

This write-up is for educational purposes only and documents a legal Capture-The-Flag (CTF) challenge. No real systems or data were harmed.

## Challenge Link:
https://play.picoctf.org/practice/challenge/66?category=1&page=2