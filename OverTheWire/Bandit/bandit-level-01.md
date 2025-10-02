# [Project] Bandit Level XX — Short Title
**Date:** 2025-10-02  
**Target:** OverTheWire Bandit (level XX)  
**Time spent:** 20 min  
**Author:** Your Name

## Executive summary
One-line: what you did and the result (e.g., "Logged into Bandit level 0, read 'readme' to obtain password for next level").

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
