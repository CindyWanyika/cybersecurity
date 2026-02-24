# PicoCTF Web Exploitation – Scavenger Hunt Write-Up

>The full flag has been intentionally redacted from this write up

# Challenge Overview

This challenge required locating hidden pieces of a flag scattered across different parts of a website. The task focused on manual web enumeration and understanding how web servers expose files.

The flag was divided into multiple parts and hidden in:
- HTML source code
- CSS file
- robots.txt
- Apache configuration file
- macOS metadata file


# Vulnerability Analysis

The challenge relied on **improper exposure of sensitive files**. Specifically:

1. Developers left comments inside production files.
2. The `robots.txt` file exposed hidden paths.
3. The Apache `.htaccess` file was publicly accessible.
4. A macOS `.DS_Store` file was uploaded to the server.

These are common real-world mistakes during web deployment.

# Steps

## Step 1 - Inspecting the HTML Source

- Opened the webpage.
- Used View Page Source.
- Found Part 1 of the flag inside an HTML comment.


## Step 2 - Checking the CSS File

- Opened the linked stylesheet.
- Found Part 2 of the flag inside a CSS comment.

## Step 3 - Inspecting the JavaScript File

The JavaScript file contained this comment:

```js
/* How can I keep Google from indexing my website? */
```

This is a reference to the `robots.txt` file.


## Step 1 - Accessing robots.txt

Visited:

http://wily-courier.picoctf.net:PORT/.robots.txt

Found:

```
# Part 3: [REDACTED]
# I think this is an apache server... can you Access the next flag?
```

The Apache hint suggested checking `.htaccess`.

---

## STEP 5 - Accessing .htaccess

Visited:

http://wily-courier.picoctf.net:PORT/.htaccess

Found:

```
# Part 4: [REDACTED]
# I love making websites on my Mac, I can Store a lot of information there.
```

The Mac hint suggested checking `.DS_Store`.

---

## Step 6 - Accessing .DS_Store

Visited:

http://wily-courier.picoctf.net:PORT/.DS_Store

Found:

```
Congrats! You've completed the scavenger hunt!
Part 5: [REDACTED]
```


# 🏁 Final Flag Structure

The full flag followed this format:

```
picoCTF{[REDACTED_PART_1][REDACTED_PART_2][REDACTED_PART_3][REDACTED_PART_4][REDACTED_PART_5]}
```

# Why the Attack Worked

This challenge worked because:

- Sensitive comments were left in production files.
- Hidden system files were publicly accessible.
- Server configuration files were not restricted.
- The deployment process failed to remove development artifacts.

No advanced exploitation was required — only careful enumeration.


# Security Takeaways

1. Never leave sensitive comments in production code.
2. Restrict access to:
   - `.htaccess`
   - `.DS_Store`
   - Other configuration files
3. Use proper deployment pipelines.
4. Disable directory indexing.
5. Regularly audit exposed files on production servers.

# Skills Demonstrated

- Manual web enumeration
- Source code inspection
- Understanding of `robots.txt`
- Knowledge of Apache server files
- Awareness of macOS metadata files
- Logical chaining of hints

## Disclaimer
This write-up is for educational purposes only and documents a legal Capture-The-Flag (CTF) challenge. No real systems or data were harmed.

## Challenge Link:
https://play.picoctf.org/practice/challenge/161?category=1&page=2
