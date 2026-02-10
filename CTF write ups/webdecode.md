# picoCTF — WebDecode Write-Up

## Challenge Overview
This challenge focuses on using the **browser web inspector** to locate hidden data inside a website.
The flag is not visible on the page itself but is embedded within the **HTML source code** in an encoded format.

Skills used:
- Web Inspector / Developer Tools
- HTML source analysis
- Base64 decoding


## Step 1: Explore the Website
Opening the website displays the message:

> *"Try inspecting the page!! You might find it there"*

This suggests that the flag is hidden in the page source rather than the visible content.


## Step 2: Inspect the HTML Source
Using the browser’s Developer Tools:
- Right-click on the page
- Select **Inspect**
- Navigate to the **Elements** tab

While examining the HTML, a suspicious attribute is found inside a `<section>` tag:

```html
notify_true="c...REDACTED....1bH0="
```
The string:
Contains only letters and numbers
Ends with =
Does not resemble readable text

These characteristics indicate Base64 encoding.

## Step 3: Decode the Encoded String
The encoded value is decoded using Base64.

Example using the terminal:

echo c..REDACTED...H0 | base64 -d
Decoding the string reveals the flag.

## Step 4: Retrieve the Flag
After decoding, the following flag is obtained:

picoCTF{REDACTED}

## Disclaimer
This write‑up is for educational purposes only and documents a legal Capture‑The‑Flag (CTF) challenge. No real systems or credentials were harmed.


## Challenge Link
https://play.picoctf.org/practice/challenge/427?category=1&difficulty=1&page=1

