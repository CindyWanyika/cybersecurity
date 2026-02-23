# 🕵️ picoCTF Insp3ct0r Challenge Write-Up 
 
## Challenge Overview

This challenge involved analyzing a web application instance launched on demand. The prompt suggested that the provided code “may need inspection,” and the hint specifically pointed toward inspecting web code in the browser.

The goal was to find a hidden flag within the web application.

## Vulnerability Analysis

The key clue was the hint:

> **How do you inspect web code on a browser?**

This immediately suggests using browser developer tools to inspect the client-side source code.

Web applications send HTML, CSS, and JavaScript to the client (browser). Anything embedded in these files including comments is visible to users through:

- **Right-click → Inspect**
- **View Page Source**
- **Sources tab in Developer Tools**

If developers accidentally leave sensitive information (like flags, API keys, or credentials) inside comments in frontend files, it becomes publicly accessible.

In this case, the flag was hidden inside comments across multiple frontend files.

## Exploitation Steps

1. **Launched the challenge instance.**

2. **Opened Developer Tools**
   - Right-clicked on the webpage.
   - Selected **Inspect**.
   - Navigated to the **Sources** tab.

3. **Inspected HTML File**
   - Opened the main HTML file.
   - Found a portion of the flag hidden inside an HTML comment:
     ```html
     <!-- flag_part_1 -->
     ```

4. **Inspected CSS File**
   - Navigated to the linked CSS file.
   - Found another portion of the flag inside a CSS comment:
     ```css
     /* flag_part_2 */
     ```

5. **Inspected JavaScript File**
   - Opened the JavaScript file.
   - Located the final portion of the flag inside a JS comment:
     ```javascript
     // flag_part_3
     ```

6. **Reconstructed the Flag**
   - Combined all three parts in the correct order.
   - Successfully reconstructed the complete flag.


## Why the Attack Worked

This attack worked because:

- The flag was stored in **client-side files**.
- Client-side code is fully accessible to anyone using a browser.
- Comments in HTML, CSS, and JavaScript are **not secure storage locations**.
- No obfuscation or server-side validation was used to protect the flag.

The developers relied on users not inspecting the source code which is never a safe assumption.

## Security Takeaways

- **Never store secrets in client-side code.**
- Sensitive data must remain on the server.
- Remove unnecessary comments before deploying production code.
- Assume users can view everything sent to their browser.
- Security through obscurity is not security.



## Skills Demonstrated

- Using browser Developer Tools effectively
- Inspecting HTML, CSS, and JavaScript source files
- Identifying sensitive information in comments
- Understanding client-side vs. server-side security boundaries
- Reconstructing fragmented data into a usable format


## Key Concept Reinforced

Anything sent to the client can be read by the client.
If a browser can see it, a user can see it.

## Disclaimer
This write-up is for educational purposes only and documents a legal Capture-The-Flag (CTF) challenge. No real systems or data were harmed.

## Challenge Link:
https://play.picoctf.org/practice/challenge/18?category=1&page=2