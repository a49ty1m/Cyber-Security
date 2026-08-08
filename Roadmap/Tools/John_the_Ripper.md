# 🔑 John the Ripper: Complete Mastery Checklist

> **What is John the Ripper?** John the Ripper (JtR) is a free, open-source password cracking tool. It takes hashed password representations (NTLM, SHA-1, bcrypt, MD5, etc.) and attempts to recover the original plaintext through dictionary attacks, rule-based mangling, brute-force, and combination attacks. It runs on CPU and supports an enormous range of hash formats natively.
>
> **Why does it exist?** Password cracking is essential in penetration testing: captured hashes from SAM databases, /etc/shadow, NTDS.dit, Kerberoasting, and network captures are useless until cracked. JtR converts a hash into a credential you can actually use for lateral movement or escalation.
>
> **When to use it:** Offline cracking of Linux shadow files (`/etc/shadow`). Cracking SAM/NTDS hashes after a Windows compromise. Zip, PDF, SSH key, Office document password cracking. Cracking Kerberoast hashes (though Hashcat is usually faster on GPU). When you want CPU-based cracking or you don't have a GPU available.
>
> **When to avoid it:** When you have a GPU — Hashcat is 10–100x faster on GPU hardware. When you need GPU-specific attack modes or advanced mask syntax — Hashcat is more feature-complete for GPU workflows.
>
> **What mastering JtR unlocks:** Offline credential recovery from any captured hash. Linux password file cracking. Document/archive password cracking. Understanding of the full password cracking methodology (identification → extraction → cracking → credential use).
>
> **Roadmap Phase:** Phase 4–5 (Post-Exploitation — Offline Password Cracking)

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals | 5 | 2–3 hours |
| 2 | Core Attack Modes | 5 | 3–5 hours |
| 3 | Rules and Mangling | 4 | 3–4 hours |
| 4 | Hash Format Support | 4 | 2–3 hours |
| 5 | File Cracking | 4 | 2–3 hours |
| 6 | Integration | 3 | 1–2 hours |
| 7 | Practical Labs | 4 | 4–6 hours |
| 8 | Mastery Challenges | 3 | 3–5 hours |
| | **Total** | **32** | **~20–31 hours** |

**Prerequisites:** Understanding of cryptographic hashing (one-way function — hash cannot be reversed mathematically, only cracked by guessing). Familiarity with how passwords are stored (Linux: `/etc/shadow`, Windows: SAM/NTDS).

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — Password Hashing Basics

- [ ] **Completed** · ⭐ Beginner · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **One-Way Function** | A hash is deterministic (same input → same hash) but not reversible. Cracking = finding input that produces the same hash — by trying candidates. |
| **Salting** | Modern hashes add a unique random salt per user so identical passwords produce different hashes. Defeats precomputed rainbow tables. |
| **Hash Strength** | MD5/NTLM: fast — billions of guesses/sec on modern hardware. bcrypt/scrypt/Argon2: slow by design — thousands of guesses/sec. Always identify the hash type before cracking. |
| **Wordlist Attack** | Try every word in a list. Fast. Works when the password is a common word or found in known breach data. |
| **Brute-Force** | Try every possible character combination. Slow but complete for short passwords. |

---

### Task 1.2 — Installation

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Kali** | Pre-installed. `john --version`. |
| **Jumbo** | `john-jumbo` (community-enhanced) has 100+ more hash formats. `apt install john`. Most Kali installations use Jumbo. |
| **Compile from Source** | `git clone https://github.com/openwall/john; cd john/src; ./configure; make -s clean && make -sj4`. Required for latest formats and performance. |
| **Config File** | `/etc/john/john.conf` or `~/.john/john.conf`. Contains rule sets, format configs. |

---

### Task 1.3 — Identifying Hash Formats

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Auto-detect** | `john hash.txt` — JtR attempts to auto-detect. Works for common formats. |
| **Manual** | `john --list=formats | grep -i ntlm` — find the exact format name. `john --format=NT hash.txt`. |
| **hash-identifier** | `hash-identifier` (Kali tool) — paste a hash → identifies likely format. |
| **hashid** | `hashid <hash>` — more accurate than hash-identifier. |
| **Common Formats** | `NT` = NTLM (Windows). `md5crypt` = Linux MD5 `$1$`. `sha512crypt` = Linux SHA-512 `$6$`. `bcrypt` = `$2a$`. `krb5tgs` = Kerberoast. `office` = Office documents. |

---

### Task 1.4 — Basic Cracking Run

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Command** | `john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt`. |
| **Show Results** | `john --show hash.txt`. |
| **Session** | `john --session=mysession --wordlist=rockyou.txt hash.txt`. Resume: `john --restore=mysession`. |
| **Potfile** | JtR stores cracked passwords in `~/.john/john.pot`. `john --pot=custom.pot ...`. |

---

### Task 1.5 — Format of Input Files

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **/etc/shadow** | `john /etc/shadow` — JtR recognizes shadow format directly. Or: `unshadow /etc/passwd /etc/shadow > combined.txt; john combined.txt`. |
| **Single Hash** | `echo "5f4dcc3b5aa765d61d8327deb882cf99" > hash.txt; john --format=Raw-MD5 hash.txt`. |
| **NTLM Hashes** | From secretsdump: `Administrator:500:aad3b435b51404eeaad3b435b51404ee:8846f7eaee8fb117ad06bdd830b7586c:::`. `john --format=NT hashes.txt`. |
| **Multiple Hashes** | Just put multiple hashes in the file, one per line. JtR cracks all of them. |

---

# PHASE 2: CORE ATTACK MODES

---

### Task 2.1 — Wordlist Mode

- [ ] **Completed** · ⭐ Beginner · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Command** | `john --wordlist=rockyou.txt hash.txt`. |
| **Wordlists** | `rockyou.txt` (14M passwords) — always try first. `SecLists/Passwords/`. `kaonashi.txt` (NTLM-specific). `weakpass_3` (large compilation). |
| **Multiple Wordlists** | JtR takes one wordlist at a time. Run sequentially: first rockyou → then larger lists → then rules. |

---

### Task 2.2 — Incremental (Brute-Force) Mode

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Command** | `john --incremental hash.txt` — full brute-force, all character sets. |
| **Character Set** | `--incremental=Alpha` — letters only. `--incremental=Digits` — numbers only. `--incremental=Alnum` — letters + digits. |
| **Length Limit** | Add to john.conf under `[Incremental:Custom]`: `MinLen=4` `MaxLen=8`. |
| **Reality** | Incremental is slow for long passwords. Best for short passwords (≤6 chars) or when you know the charset. |

---

### Task 2.3 — Single Crack Mode

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Command** | `john --single hash.txt`. |
| **How It Works** | Uses the username (from shadow file or input format) and applies mangling rules to it. `alice` → tries: `alice`, `Alice`, `ALICE`, `alice1`, `alice123`, `alice!`, `3lice` etc. |
| **When Useful** | After extracting a shadow file — run `--single` first (fast). Users often use their own name as the basis. |

---

### Task 2.4 — Wordlist + Rules

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Command** | `john --wordlist=rockyou.txt --rules=best64 hash.txt`. |
| **What Rules Do** | Take each word and apply transformations: capitalize first letter, append numbers, substitute letters with symbols (a→@, e→3), reverse, duplicate. Dramatically expands coverage without a larger wordlist. |
| **Built-in Rulesets** | `best64` (64 common transformations). `Jumbo` (many transformations). `KoreLogic` (comprehensive). `T0XlCv2` (advanced). |

---

### Task 2.5 — Mask Attack

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Concept** | Mask attack = brute-force with a pattern. When you know the password structure: `?u?l?l?l?d?d!` (Upper+3lower+2digits+!). Only tries combinations matching that pattern. |
| **JtR Syntax** | Not natively as flexible as Hashcat's mask attack. Use `--mask` in JtR Jumbo: `john --mask='?a?a?a?a?a?a' hash.txt`. `?a`=all chars, `?u`=uppercase, `?l`=lowercase, `?d`=digit, `?s`=special. |
| **Better Alternative** | Hashcat's mask attack (`-a 3`) is significantly more powerful. Prefer Hashcat for mask attacks when a GPU is available. |

---

# PHASE 3: RULES AND MANGLING

---

### Task 3.1 — How Rules Work

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Rule Syntax** | Rules are defined in `john.conf`. Each rule is a string of transformation codes applied sequentially to a word. |
| **Common Codes** | `l` = lowercase all. `u` = uppercase all. `c` = capitalize first. `r` = reverse. `d` = duplicate. `$X` = append character X. `^X` = prepend X. `sXY` = substitute X with Y. `[` = remove first char. `]` = remove last char. |
| **Example** | `cl$1$!` = capitalize, lowercase rest, append `1`, append `!`. `password` → `Password1!`. |

---

### Task 3.2 — Custom Rule Writing

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Where** | Add to `john.conf` under `[List.Rules:CustomRules]`. |
| **Common Patterns** | Append years: `$2$0$2$4` → append `2024`. Append season+year: create rule set with `spring2024`, `Summer2024` patterns. Common suffix: `$1$2$3`. |
| **Company-Specific** | If company name is known: prepend company name, append year, add special char. `Company2024!`. Write a rule set for these. |

---

### Task 3.3 — KoreLogic Rules

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Download** | KoreLogic published a comprehensive JtR rule set: available on GitHub/Kali. Some are included in john-jumbo. |
| **Use** | `john --wordlist=rockyou.txt --rules=KoreLogic hash.txt`. |
| **Coverage** | ~60 rules covering most common corporate password patterns. Good for AD password audits. |

---

### Task 3.4 — Loopback Mode

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Command** | `john --wordlist=john.pot --rules hash.txt`. |
| **What It Does** | Uses already-cracked passwords from the pot file as the wordlist. Then applies rules. If `password1` was cracked, it tries `password1!`, `Password1`, `PASSWORD1` etc. |
| **Value** | Users in the same organization tend to follow similar password patterns. Cracked passwords reveal the pattern — apply rules to find related uncracked ones. |

---

# PHASE 4: HASH FORMAT SUPPORT

---

### Task 4.1 — Linux Hashes

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Shadow Format** | `username:$type$salt$hash:...`. `$1$` = MD5-crypt. `$5$` = SHA-256-crypt. `$6$` = SHA-512-crypt. `$y$` = yescrypt. |
| **Direct** | `john /etc/shadow --wordlist=rockyou.txt`. |
| **unshadow** | `unshadow /etc/passwd /etc/shadow > combined.txt`. Combines username+hash for single crack mode to use the username. |

---

### Task 4.2 — Windows Hashes

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **NTLM Format** | `user:rid:LM_hash:NT_hash:::`. LM hash is the old, weak one (usually empty: `aad3b435b51404eeaad3b435b51404ee`). NT hash is what you crack. |
| **Crack** | `john --format=NT --wordlist=rockyou.txt ntlm_hashes.txt`. |
| **NTLMv2** | Net-NTLMv2 (from Responder): different format. `john --format=netntlmv2 --wordlist=rockyou.txt netntlmv2.txt`. |

---

### Task 4.3 — Kerberoast Hashes

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Format** | `$krb5tgs$23$*...*` — TGS-REP format from Kerberoasting. |
| **Crack** | `john --format=krb5tgs --wordlist=rockyou.txt kerberoast.txt`. |
| **Better** | Hashcat mode 13100 is significantly faster if a GPU is available. |

---

### Task 4.4 — Application and Database Hashes

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **WordPress** | `$P$` hash. `john --format=phpass --wordlist=rockyou.txt wp_hashes.txt`. |
| **MySQL** | `*hash` format. `john --format=mysql-sha1 ...`. |
| **MSSQL** | `0x0100...`. `john --format=mssql ...`. |
| **List All** | `john --list=formats` — shows all ~400+ supported formats. |

---

# PHASE 5: FILE CRACKING

---

### Task 5.1 — ZIP and RAR Files

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **ZIP** | `zip2john protected.zip > zip.hash; john --wordlist=rockyou.txt zip.hash`. |
| **RAR** | `rar2john protected.rar > rar.hash; john --wordlist=rockyou.txt rar.hash`. |
| **7z** | `7z2john protected.7z > 7z.hash; john --wordlist=rockyou.txt 7z.hash`. |

---

### Task 5.2 — SSH Private Keys

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Extract** | `ssh2john id_rsa > ssh.hash`. |
| **Crack** | `john --wordlist=rockyou.txt ssh.hash`. |
| **Use** | After cracking: `ssh -i id_rsa user@target` → enter cracked passphrase. |

---

### Task 5.3 — Office Documents and PDF

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Office** | `office2john protected.docx > office.hash; john --format=office --wordlist=rockyou.txt office.hash`. |
| **PDF** | `pdf2john protected.pdf > pdf.hash; john --wordlist=rockyou.txt pdf.hash`. |

---

### Task 5.4 — KeePass Databases

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Extract** | `keepass2john database.kdbx > keepass.hash`. |
| **Crack** | `john --format=keepass --wordlist=rockyou.txt keepass.hash`. |
| **Value** | KeePass databases on compromised machines may contain credentials for the entire organization. |

---

# PHASE 6: INTEGRATION

---

### Task 6.1 — JtR + Impacket/secretsdump

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Workflow** | `impacket-secretsdump -just-dc-ntlm domain/admin@DC -outputfile ntds`. → `ntds.ntds` contains all NT hashes. `john --format=NT --wordlist=rockyou.txt ntds.ntds`. |

---

### Task 6.2 — JtR + Responder

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Workflow** | Responder captures Net-NTLMv2 hashes from LLMNR/NBT-NS poisoning. `Responder.db` or per-user files in `/usr/share/responder/logs/`. `john --format=netntlmv2 --wordlist=rockyou.txt NTLMv2_hash.txt`. |

---

### Task 6.3 — JtR vs. Hashcat Decision

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Use JtR** | No GPU available. Linux shadow files (convenient format handling). File cracking (zip2john etc.). Rule writing convenience. Quick single-mode run. |
| **Use Hashcat** | GPU available (10–100x faster). Mask attacks. Large NTLM hash dumps. Kerberoast hashes. Long cracking sessions. |

---

# PHASE 7: PRACTICAL LABS

---

### Lab 7.1 — Shadow File Crack

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| **Scenario** | Create a test shadow file with known passwords (`openssl passwd -6 password123`). Crack it with JtR wordlist + rules. Verify the cracked result with `--show`. |
| **Success Criteria** | Hash cracked. Verified with `--show`. Time documented. |

---

### Lab 7.2 — NTLM Hash Crack

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| **Scenario** | Extract NT hashes from a Windows VM (with admin access — lab only: `reg save HKLM\SAM sam.bak`). Transfer to Kali. Crack with JtR + wordlist + best64 rules. |
| **Success Criteria** | NT hashes cracked. Credentials verified by re-authentication. |

---

### Lab 7.3 — File Password Recovery

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| **Scenario** | Password-protect a ZIP file with a known simple password. Use zip2john → JtR to recover it. Repeat with an SSH key. |
| **Success Criteria** | ZIP and SSH key passwords recovered. |

---

### Lab 7.4 — Kerberoast + Crack

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| **Scenario** | In an AD lab: perform Kerberoasting (`GetUserSPNs.py`). Save TGS hashes. Crack with JtR `krb5tgs` format. Use cracked credentials to authenticate as the service account. |
| **Success Criteria** | TGS hash cracked. Service account authenticated with cracked password. |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — Corporate Password Audit

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 90 min

| **Scenario** | Given an NTDS dump from an AD lab (500+ hashes): crack as many as possible using wordlist + multiple rule sets. Document: crack rate, time taken, password pattern analysis (most common structures). Write recommendations. |
| **Success Criteria** | >50% crack rate. Password pattern report written. Specific weak-password policy recommendations made. |

---

### Challenge 8.2 — Custom Rule Set

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 60 min

| **Scenario** | Analyze 20 cracked passwords from a previous crack session. Identify common patterns (season+year, company+number, etc.). Write a custom JtR rule set targeting these patterns. Test against remaining uncracked hashes — verify the custom rules crack additional hashes. |
| **Success Criteria** | Custom rule set created. At least 5 additional hashes cracked by the custom rules. |

---

### Challenge 8.3 — CTF Hash Challenge

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 60 min

| **Scenario** | Find a CTF challenge involving password cracking (HackTheBox, TryHackMe). Identify the hash format. Choose the appropriate attack mode and wordlist. Crack the hash to get the flag. Document the methodology. |
| **Success Criteria** | Flag captured. Full cracking methodology documented (format → tool → wordlist → rules → result). |

---

# 📋 FINAL COMPETENCY MATRIX

| Competency | Self-Assessment |
|:---|:---:|
| Can identify hash formats from format strings and visual patterns | ☐ |
| Can crack Linux shadow files with wordlist + rules | ☐ |
| Can crack NTLM and Net-NTLMv2 hashes | ☐ |
| Can crack Kerberoast TGS hashes | ☐ |
| Can crack ZIP, RAR, SSH, Office, and KeePass files | ☐ |
| Can write custom JtR rule sets targeting specific password patterns | ☐ |
| Can use loopback mode to crack related passwords | ☐ |
| Knows when to use JtR vs. Hashcat | ☐ |
| Can integrate JtR into a post-exploitation workflow | ☐ |
| Can analyze cracked passwords and write policy recommendations | ☐ |

---

## 🎯 Interview Questions

1. What is the difference between a wordlist attack and a brute-force attack?
2. What does salting do to a hash and how does it affect cracking?
3. How do you extract hashes from a Linux shadow file for JtR?
4. What is the `--single` mode in JtR and when is it effective?
5. What are JtR rules and how do they expand wordlist coverage?
6. How do you crack Net-NTLMv2 hashes captured by Responder?
7. What is loopback mode and why is it useful in an AD environment?
8. When would you use JtR instead of Hashcat for password cracking?
9. How do you crack a password-protected SSH private key?
10. What does a 40% NTLM crack rate tell you about an organization's password policy?
