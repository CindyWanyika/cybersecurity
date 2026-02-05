Perfect — this is a **great challenge to document**, and it fits your existing write-up style really well. Below is a **clean, simple, beginner-friendly write-up** in the **same markdown format** you use. You can drop this straight into a `.md` file.

I kept the wording clear and not overly fancy, just solid and professional.

---

```markdown
# picoCTF — Heapdump / Memory Disclosure Challenge Write-Up

## Challenge Overview
In this challenge, the goal was to explore a web application and identify an endpoint that exposes a file containing sensitive data. The application is a simple blog website called **picoCTF News**, which includes an article about API Documentation.

The objective was to locate an endpoint that generates files holding the server’s memory and extract a hidden flag from that memory.

The goal of the challenge was to:
- Explore the web application
- Identify exposed API endpoints
- Find a memory dump file
- Extract the hidden flag from the dump

NOTE: The flag has been intentionally redacted in this write-up.


## Tools Used
- Web browser — for navigating the site and reading documentation
- curl — to download files from the command line
- strings — to extract readable text from the memory dump
- grep — to search for the flag


## Step 1 — Exploring the Website
I started by browsing the picoCTF News website and reading through the available blog posts. One article mentioned **API Documentation**, which suggested that the application exposed a public API since CTF mentioned it.

I navigated to the API documentation page to inspect the available endpoints.


## Step 2 — Reviewing the API Documentation
The API documentation listed several endpoints used by the application. While reviewing them, I noticed the following endpoint:

```

GET /heapdump

````

The description of this endpoint indicated that it was used for **diagnosing memory allocation**. This suggested that it generated a memory or heap dump of the server.

Because the challenge description mentioned “files holding the server’s memory,” this endpoint stood out as a likely source of sensitive information.


## Step 3 — Downloading the Heap Dump
I accessed the `/heapdump` endpoint and downloaded the generated file. The file had a `.heapsnapshot` extension, which is commonly used for heap memory snapshots.

To download the file using the command line, I used:

```bash
curl http://verbal-sleep.picoctf.net:<PORT>/heapdump -o heapdump.heapsnapshot
````

The downloaded file was large, which further indicated that it contained memory data.

## Step 4 — Extracting the Flag from Memory

Heap dump files often contain readable strings, including sensitive data stored in memory.

To extract readable text from the file and search for the flag, I ran:

```bash
strings heapdump.heapsnapshot | grep picoCTF
```

This command revealed the flag directly from the memory dump.

## Why This Attack Worked

The `/heapdump` endpoint exposed a live memory snapshot of the server without any authentication or access control.

Key issues demonstrated:

* Publicly accessible debug endpoint
* Exposure of server memory
* Sensitive data stored in plaintext in memory
* No restriction on diagnostic endpoints

In a real-world application, this could lead to leakage of credentials, secrets, or user data.

## Security Takeaways

* Debug and diagnostic endpoints should never be exposed publicly
* Memory dump endpoints must be protected or disabled in production
* Sensitive data should be carefully handled to minimize exposure in memory
* API documentation can unintentionally reveal dangerous functionality

## Skills Demonstrated

* Web application exploration
* API endpoint enumeration
* Identifying information disclosure vulnerabilities
* Using Linux command-line tools for analysis
* Extracting sensitive data from memory dumps

## Disclaimer

This write-up is for educational purposes only and documents a legal Capture-The-Flag (CTF) challenge. No real systems or data were harmed.

## Challenge Link
https://play.picoctf.org/practice/challenge/476?category=1&difficulty=1&page=1