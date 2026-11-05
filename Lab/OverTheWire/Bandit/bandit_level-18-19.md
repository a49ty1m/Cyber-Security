# [Project] Bandit Level 18 → Level 19 — Notes
**Date:** 2026-10-24  
**Target:** OverTheWire Bandit (Level 18 → Level 19)  
**Author:** Aditya Mishra

## Tools & methodology
Tools:   
Method: 

## What i learn : 
- How user startup scripts like `.bashrc` or `.profile` can be used to log users out upon interactive login.
- How to bypass interactive shell restrictions by passing commands directly to SSH (`ssh bandit18@... -p 2220 cat readme`) or using non-login shell execution.

## Commands used
```bash
ssh bandit18@bandit.labs.overthewire.org -p 2220 cat readme
```

## Findings / Solution
* PASSWORDS for each level are stored in /etc/somegame_pass/.

## Execution
```bash
ssh bandit18@bandit.labs.overthewire.org -p 2220 cat readme
```
* PASSWORDS for each level are stored in /etc/somegame_pass/.
