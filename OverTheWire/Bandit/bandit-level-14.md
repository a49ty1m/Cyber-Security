# [Project] Bandit Level 13 — Short Title
**Date:** 2025-10-06  
**Target:** OverTheWire Bandit (level 13)  
**Time spent:** 20 min  
**Author:** Aditya Mishra

## Executive summary
One-line: use nc or netcat command it is use to connect between servers if you login as localhost at 30000 it will ask or password and will give the password for next level

## Tools & methodology
Tools: ssh, ls, cat, file  
Method: connect via SSH → inspect files → read target file

## Findings / Solution
- **Goal:** retrieve password for next level  
 pass = MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS

walkthrough

bandit14@bandit:~$ nc -l 30000
nc: Address already in use
bandit14@bandit:~$ ls
bandit14@bandit:~$ nc localhost 30000
MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS
Correct!
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo

bandit14@bandit:~$ 
