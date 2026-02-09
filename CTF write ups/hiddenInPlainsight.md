# picoCTF — Hidden in Plain Sight (Steganography) Write‑Up

## Challenge Overview
In this challenge, we are given a seemingly normal JPG image and told that something is hidden inside it.  
The goal is to discover the hidden payload and extract the flag.

This challenge focuses on:
- Metadata analysis  
- Base64 decoding  
- Basic steganography using `steghide`  

NOTE: The flag has been intentionally redacted in this write-up.

## Tools Used
- **Kali Linux** — analysis environment  
- **exiftool** — to inspect image metadata  
- **base64** — to decode encoded strings  
- **steghide** — to extract hidden data from the image  


## Step 1 — Inspecting Image Metadata
First, the image metadata was inspected using `exiftool` to look for anything unusual.

```
exiftool img.jpg
```
In the output, a suspicious Comment field stood out:

Comment : REDACTED
This value appeared to be Base64‑encoded.

## Step 2 — Decoding the Comment
The comment was decoded using base64.

echo "REDACTED COMMENT" | base64 -d
Output:

steghide:REDACTED2....=
This suggested:

The tool used to hide the data was steghide

Another Base64‑encoded value was present, likely a password

The second value was decoded:

echo "REDACTED2...." | base64 -d
Output:

REDACTED3
So, the steghide passphrase is REDACTED3.

## Step 3 — Installing Steghide
Attempting to run steghide showed that it was not installed, so it was installed using the package manager.

sudo apt install steghide
Step 4 — Extracting the Hidden Data
With steghide installed, the hidden data was extracted from the image.

steghide extract -sf img.jpg
When prompted for the passphrase, the following was entered:

REDACTED3....
Steghide successfully extracted a file:

wrote extracted data to "flag.txt"
Step 5 — Reading the Flag
Finally, the contents of the extracted file were displayed.

cat flag.txt
Output:

picoCTF{REDACTED4...d79}

## Why This Attack Worked

The image contained sensitive data hidden using steganography, and the password required to extract it was exposed in the image metadata.

## Key issues demonstrated:

Sensitive hints stored in metadata

Use of reversible encoding (Base64)

Weak protection of steganographic content

## Security Takeaways
Metadata should be reviewed and sanitized before sharing files

Secrets should never be stored in plaintext or reversible encodings

Steganography alone is not secure without strong encryption

Files shared publicly should be assumed to be fully inspectable

## Skills Demonstrated
Metadata analysis

Base64 decoding

Steganography detection and extraction

Use of Linux command‑line tools

## Disclaimer
This write‑up is for educational purposes only and documents a legal Capture‑The‑Flag (CTF) challenge. No real systems or data were harmed.

## Challenge Link
https://play.picoctf.org/practice/challenge/524?originalEvent=77&page=1