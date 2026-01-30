# [Project] Bandit Level 17 — Short Title
**Date:** 2025-10-06  
**Target:** OverTheWire Bandit (level 17)  
**Author:** Aditya Mishra

## Executive summary
One-line: use the diff command to check between two files passwords.new and passwords.old

## Tools & methodology
Tools: ssh, ls, cat, file  
Method: connect via SSH → inspect files → read target file

## Findings / Solution
- **Goal:** retrieve password for next level  
 pass = EReVavePLFHtFlFsjn3hyzMlvSuSAcRD

walkthrough

bandit17@bandit:~$ diff passwords.old passwords.new
42c42
< pGozC8kOHLkBMOaL0ICPvLV1IjQ5F1VA
---
> x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO
