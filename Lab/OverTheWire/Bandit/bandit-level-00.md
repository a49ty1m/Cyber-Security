# [Project] Bandit Level 00 — Short Title
**Target:** OverTheWire Bandit (level 00)  
**Author:** Aditya Mishra

## Executive summary
One-line: just read readne file, soo basic.

## Tools & methodology
Tools: ssh, ls, cat, file  
Method: connect via SSH → inspect files → read target file

## Findings / Solution
- **Goal:** retrieve password for next level
pass = bandit0  
- **Commands (copy-paste):**
```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220
ls -la
cat readme

