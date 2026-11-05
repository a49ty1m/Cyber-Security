# [Project] Bandit Level 19 → Level 20 — Notes
**Date:** 2026-10-24  
**Target:** OverTheWire Bandit (Level 19 → Level 20)  
**Author:** Aditya Mishra

## Tools & methodology
Tools:   
Method: 

## What i learn : 
- Understanding the SUID (Set Owner User ID) bit on executables (`-rwsr-x---`).
- An SUID executable runs with the permissions of the file owner (bandit20) rather than the executing user (bandit19), allowing access to privileged files like `/etc/bandit_pass/bandit20`.

## Commands used
```bash
ssh bandit19@bandit.labs.overthewire.org -p 2220
ls -la
file bandit20-do
./bandit20-do cat /etc/bandit_pass/bandit20
```

## Findings / Solution
- Password for next level:

## Execution
```bash
ssh bandit19@bandit.labs.overthewire.org -p 2220
ls -la
file bandit20-do
./bandit20-do cat /etc/bandit_pass/bandit20
```
