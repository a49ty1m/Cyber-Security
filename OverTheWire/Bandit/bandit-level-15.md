# [Project] Bandit Level 15 — Short Title
**Target:** OverTheWire Bandit (level 13)  
**Author:** Aditya Mishra

## Executive summary
One-line: use nc or netcat command it is use to connect between servers if you login as localhost at 30000 it will ask or password and will give the password for next level

## Tools & methodology
Tools: ssh, ls, cat, file  
Method: connect via SSH → inspect files → read target file

## Findings / Solution
- **Goal:** retrieve password for next level  
 pass = 8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo

walkthrough

bandit15@bandit:~$  ncat --ssl localhost 30001
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo
Correct!
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx

