# picoCTF — Drop-In (Git Version Control)

## Challenge Overview

This challenge provided a ZIP file containing a small project directory. Upon extraction, the folder included a `.git` directory and a `message.txt` file.

The objective was to retrieve previously stored information that had been removed from the current version of the file.

The challenge focuses on understanding how Git version control preserves historical data, even after it has been deleted or modified in later commits.

NOTE: The flag has been intentionally redacted in this write-up.


## Tools Used

- Kali Linux  
- `unzip`  
- Git (`git log`, `git show`)  
- Basic Linux command-line navigation  

## Steps to Retrieve Flag

### 1. Extract the ZIP file

```bash
unzip challenge.zip
cd drop-in
```
This revealed:

message.txt

2. Inspect Git Commit History
git log
This showed two commits:

create flag

remove sensitive info

This strongly suggested that the flag existed in an earlier commit and was later removed.

### 3. View the Older Commit
Using the commit hash for "create flag", the previous version was examined:

git show <commit_hash>
This displayed the contents of message.txt when it was first created, revealing the flag.

The flag was successfully recovered from Git history.

### Why This Attack Worked
Git stores every committed version of a file as part of its repository history. Even if a file is modified or sensitive data is removed in a later commit, the previous versions remain accessible unless the history is rewritten.

### Key issues demonstrated:

Sensitive data was committed to version control

The data was removed in a later commit but not permanently deleted

Git preserves full commit history by design

Anyone with repository access can inspect previous snapshots

In a real-world scenario, accidentally committing secrets (API keys, credentials, tokens) and later deleting them does not remove them from Git history. Attackers can retrieve them by reviewing earlier commits.

### Security Takeaways
Never commit sensitive information to version control

Removing secrets in later commits does not erase them from history

Use .gitignore to prevent committing sensitive files

If secrets are exposed, use tools like git filter-repo or BFG Repo-Cleaner to purge history

Rotate any exposed credentials immediately

### Skills Demonstrated
Git repository analysis

Understanding version control internals

Recovering deleted data from commit history

Command-line investigation in Linux

Identifying insecure development practices

### Disclaimer
This write-up is for educational purposes only and documents a legal Capture-The-Flag (CTF) challenge. No real systems or data were harmed.

Challenge Link
https://play.picoctf.org/practice/challenge/411?difficulty=1&page=3
