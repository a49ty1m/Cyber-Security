# [Project] Bandit Level 19 — setuid Helper Binary
**Date:** 2026-04-02  
**Target:** OverTheWire Bandit (level 19)  
**Author:** Aditya Mishra

## Executive summary
This level introduces a helper binary that runs commands as the next level user.

## Goal
- Retrieve the password for level 20.

## Tools & methodology
Tools: `ls`, `file`, `./bandit20-do`, `cat`  
Method: inspect the helper binary and use it to read the next password file.

## Commands used
```bash
ssh bandit19@bandit.labs.overthewire.org -p 2220
ls -la
file bandit20-do
./bandit20-do cat /etc/bandit_pass/bandit20
```

## Findings / Solution
- **Goal:** retrieve password for next level  
 pass = EReVavePLFHtFlFsjn3hyzMlvSuSAcRD

walkthrough

bandit17@bandit:~$ diff passwords.old passwords.new
42c42
< pGozC8kOHLkBMOaL0ICPvLV1IjQ5F1VA
---
> x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO
