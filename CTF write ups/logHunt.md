# picoCTF — Log Hunt Challenge Write-Up

## Challenge Overview
In this challenge, a server was leaking pieces of a secret flag through its log files. The flag was not stored in one place; instead, it was fragmented across multiple log entries and some fragments were repeated.

The objective was to analyze the server logs, extract all leaked fragments, remove duplicates, and reconstruct the original flag.

The goal of the challenge was to:
- Download and inspect the server logs
- Identify leaked flag fragments
- Handle repeated log entries
- Reconstruct the full flag from scattered parts

**NOTE:** The complete flag and flag fragments have been intentionally redacted in this write-up.

---

## Tools Used
- Kali Linux — analysis environment
- strings — to extract readable strings from the log file
- grep — to filter relevant log entries
- cut, sort, uniq, tr — for processing and reconstructing the flag

---

## Step 1 — Inspecting the Log File
After downloading the provided `server.log` file, I began by extracting readable strings to understand its contents.

```bash
strings -n 20 server.log
```
This revealed structured log entries containing timestamps, log levels, and messages.

## Step 2 — Identifying Flag Fragments

To locate possible flag data, I searched the logs for the picoCTF flag format:

strings -n 20 server.log | grep picoCTF
This revealed repeated entries containing only partial flag data, indicating that the flag was split across multiple log messages.

To see all fragments, I searched for entries labeled FLAGPART:

strings -n 20 server.log | grep FLAGPART

This command revealed multiple fragments of the flag scattered throughout the logs, with some fragments repeated several times.

## Step 3 — Extracting and Deduplicating Fragments

Next, I extracted only the flag fragment portion from each log entry:

strings -n 20 server.log | grep FLAGPART | cut -d':' -f3
Since the challenge description mentioned that fragments were sometimes repeated, I removed duplicates:

This resulted in the following unique fragments:

picoCTF{us3_

REDACTED

sk1lls_

REDACTED}

## Step 4 — Reconstructing the Flag
The fragments appeared in logical order, so I combined them to reconstruct the full flag.

To automate this, I used:

strings -n 20 server.log | grep FLAGPART | cut -d':' -f3 | sort | uniq | tr -d '\n'
This command concatenated all unique fragments into a single line, revealing the full flag.

## Why This Attack Worked
The application leaked sensitive information by logging fragments of a secret value.

Key issues demonstrated:

Sensitive data written directly to logs

Flag split across multiple log entries

Repeated fragments enabling reconstruction

Logs accessible without proper restrictions

Even though each log entry contained only a fragment, the complete secret could be recovered by analyzing the logs.

## Security Takeaways
Sensitive data should never be written to application logs

Logs must be treated as sensitive assets

Secrets should be masked or omitted from logs

Proper logging practices are critical for secure systems

Log access should be restricted and monitored

## Skills Demonstrated
Log file analysis

Identifying information disclosure vulnerabilities

Using Linux command-line tools for data extraction

Handling duplicated and fragmented data

Reconstructing leaked secrets from logs

## Disclaimer
This write-up is for educational purposes only and documents a legal Capture-The-Flag (CTF) challenge. No real systems or data were harmed.

## Challenge Link
https://play.picoctf.org/practice/challenge/527?difficulty=1&page=1