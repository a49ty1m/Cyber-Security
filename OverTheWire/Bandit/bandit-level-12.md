# [Project] Bandit Level 10 — Short Title
**Date:** 2025-10-04  
**Target:** OverTheWire Bandit (level 10)  
**Time spent:** 5 min  
**Author:** Aditya Mishra

## Executive summary
One-line: use file command then xxd -r to reverse the hexdump then again check file_type by file command then rename in that zip type then decompress repeatedly and for tar use tar xvf to decompress at last get your password


## Tools & methodology
Tools: ssh, ls, cat, file  
Method: connect via SSH → inspect files → read target file

## Findings / Solution
- **Goal:** retrieve password for next level  
 pass = 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4