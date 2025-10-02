# [Project] Bandit Level 00 — Short Title
**Date:** 2025-10-02  
**Target:** OverTheWire Bandit (level 00)  
**Time spent:** 2min  
**Author:** Aditya Mishra

## Executive summary
One-line: just read readne file, soo basic.

## Scope & rules
Lab-only: OverTheWire Bandit. No external tests.

## Tools & methodology
Tools: ssh, ls, cat, file  
Method: connect via SSH → inspect files → read target file

## Findings / Solution
- **Goal:** retrieve password for next level  
- **Commands (copy-paste):**
```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220
ls -la
cat readme
