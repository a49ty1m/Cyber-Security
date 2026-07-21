# 🔥 Hashcat: Complete Mastery Checklist

> **What is Hashcat?** Hashcat is the world's fastest and most advanced offline password recovery (cracking) tool. It uses CPU and GPU hardware acceleration to test billions of password candidates per second against captured password hashes.
>
> **Why does it exist?** When you extract password hashes from a compromised system (from `/etc/shadow`, SAM database, NTDS.dit, web app databases, or network captures), you need to recover the plaintext passwords. Hashcat converts those hashes back to passwords using brute-force, dictionary attacks, and rule-based mutations.
>
> **When to use it:** After extracting password hashes from ANY source — Linux shadows, Windows NTLM, Active Directory, web application databases, Wi-Fi handshakes, encrypted files, application tokens. Offline cracking is faster and stealthier than online brute-forcing (Hydra).
>
> **When to avoid it:** Online authentication attacks (use Hydra). When you don't have hashes (you need the hash first). When the hash type uses extremely slow algorithms with high iterations (bcrypt with cost 14+ takes forever even with GPUs).
>
> **What mastering Hashcat unlocks:** Ability to crack passwords from any hash type. Post-exploitation credential recovery. Wi-Fi security auditing. Password policy validation. Understanding of cryptographic hash functions and their weaknesses.

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md) · [🐧 Metasploitable 2 Lab](../Lab/Metasploitable_2/TASK_LIST.md) · [🌐 OWASP BWA Lab](../Lab/OWASP_Broken_WebApps/TASK_LIST.md)

| Recon & Scanning | Exploitation | Post-Exploitation | Web & Traffic |
|:-----------------|:-------------|:-------------------|:--------------|
| [🗺️ Nmap](Nmap.md) | [💀 Metasploit](Metasploit_Framework.md) | [🐉 LinPEAS](LinPEAS.md) | [🕷️ Burp Suite](Burp_Suite.md) |
| [🔌 Netcat](Netcat.md) | [🐍 Impacket](Impacket.md) | [🩸 BloodHound](BloodHound.md) | [🦈 Wireshark](Wireshark.md) |
| | [🔓 Hydra](Hydra.md) | **🔥 Hashcat** (you are here) | |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals & Hash Theory | 6 | 3–4 hours |
| 2 | Core Attack Modes | 7 | 5–7 hours |
| 3 | Intermediate (Rules, Masks, Combinator) | 6 | 5–7 hours |
| 4 | Advanced (Custom Rules, Performance) | 5 | 5–7 hours |
| 5 | Tool Integration | 4 | 2–4 hours |
| 6 | Practical Labs | 4 | 4–8 hours |
| 7 | Methodology & Limitations | 3 | 2–3 hours |
| 8 | Mastery Challenges | 3 | 4–6 hours |
| | **Total** | **38** | **~30–46 hours** |

**Prerequisites:** Understanding of password hashing concepts. Hash extraction from a compromised target (Metasploitable 2 `/etc/shadow`). GPU recommended but CPU works for learning.

**Alternatives:** John the Ripper (CPU-focused, excellent rule engine, supports more exotic formats), Ophcrack (rainbow tables, Windows-focused), CrackStation (online lookup), Mentalist (wordlist generator GUI).

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — Hashing vs Encryption vs Encoding

- [ ] **Completed** · ⭐ Beginner · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand the fundamental differences: **Encoding** is reversible without a key (Base64, URL). **Encryption** is reversible WITH a key (AES, RSA). **Hashing** is ONE-WAY — you cannot mathematically reverse a hash to get the original password. Cracking = guessing inputs until one produces the same hash. |
| **Skills Learned** | One-way function concept, why hashing is used for password storage, why cracking is "educated guessing" not "decryption," salt and pepper concepts, hash collision concept. |
| **Practical Exercise** | Generate hashes: `echo -n "password123" | md5sum`, `echo -n "password123" | sha256sum`. Observe: the same input always produces the same hash. Different inputs produce completely different hashes. You cannot reverse-engineer the input from the hash. |
| **Expected Output** | Clear understanding: hashing ≠ encryption. Cracking = testing candidates until a match is found. |
| **Common Mistakes** | Saying "decrypt the hash" (hashes cannot be decrypted — they can only be cracked). Confusing encoding with encryption. Not understanding salts (a random value added to the password before hashing — prevents rainbow table attacks and ensures identical passwords produce different hashes). |

---

### Task 1.2 — Hash Type Identification

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Identify hash types by their format, length, and prefix. Hashcat requires you to specify the correct hash mode (`-m`) — wrong mode = zero results. |
| **Skills Learned** | Visual hash identification, common hash formats, using identification tools, Hashcat mode numbers for common types. |
| **Key Hash Types** | **MD5:** 32 hex chars, `-m 0`. **SHA-1:** 40 hex chars, `-m 100`. **SHA-256:** 64 hex chars, `-m 1400`. **NTLM:** 32 hex chars (Windows), `-m 1000`. **NetNTLMv2:** `user::domain:challenge:hash:blob`, `-m 5600`. **bcrypt:** `$2b$10$...`, `-m 3200`. **Linux SHA-512:** `$6$salt$hash`, `-m 1800`. **Linux SHA-256:** `$5$salt$hash`, `-m 7400`. **WPA:** `.hccapx` file, `-m 22000`. |
| **Practical Exercise** | Use `hashid` or `hash-identifier` to identify unknown hashes: `hashid '$6$rounds=5000$salt$longhash'`. Cross-reference with Hashcat's hash modes: `hashcat --help | grep -i "sha-512"` or visit the Hashcat wiki example hashes page. |
| **Expected Output** | Ability to identify the 10 most common hash types by sight. Reference table of hash type → Hashcat mode number. |
| **Common Mistakes** | Confusing MD5 with NTLM (both are 32 hex characters — context matters: from Linux = likely MD5, from Windows SAM = NTLM). Not checking the hash mode wiki page (Hashcat has example hashes for every mode — compare your hash format). Using the wrong `-m` value (Hashcat runs but finds nothing). |

---

### Task 1.3 — Installation & Hardware Detection

- [ ] **Completed** · ⭐ Beginner · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Install Hashcat and verify your hardware (GPU/CPU) is detected. Understand the massive speed difference between CPU and GPU cracking. |
| **Skills Learned** | `hashcat -I` (list detected devices), OpenCL/CUDA driver requirements, GPU vs CPU performance (GPU is 10-100x faster for most hash types), benchmarking with `hashcat -b`. |
| **Practical Exercise** | `hashcat -I` (identify devices). `hashcat -b -m 0` (benchmark MD5 speed). `hashcat -b -m 1000` (benchmark NTLM). `hashcat -b -m 1800` (benchmark SHA-512 crypt — notice how much slower it is). |
| **Expected Output** | Device list showing GPU and/or CPU. Benchmark speeds for common hash types. Understanding that MD5/NTLM crack at billions/sec while bcrypt/SHA-512crypt crack at thousands/sec. |
| **Common Mistakes** | No GPU drivers installed (Hashcat falls back to CPU — dramatically slower). Not benchmarking (you don't know how long a crack will take without knowing your speed). Running in a VM without GPU passthrough (VMs typically can't access the GPU). |

---

### Task 1.4 — Hash File Preparation

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Prepare hash files in the correct format for Hashcat. Each hash type has a specific expected format — wrong format = error or no results. |
| **Skills Learned** | Hash file formatting (one hash per line), extracting hashes from `/etc/shadow`, Windows SAM, NTDS.dit, and database dumps, removing extraneous data, username:hash format handling. |
| **Practical Exercise** | Extract from `/etc/shadow`: `sudo cat /etc/shadow | grep '\$6\$' > linux-hashes.txt`. Format for Hashcat: `awk -F':' '{print $2}' linux-hashes.txt > hashes-only.txt`. Or keep `user:hash` format: `awk -F':' '{print $1":"$2}' /etc/shadow > user-hashes.txt` and use `--username` flag. |
| **Expected Output** | Clean hash file ready for Hashcat. Understanding of format requirements for different hash types. |
| **Common Mistakes** | Including non-hash lines (accounts with `!` or `*` in shadow = no password, skip them). Wrong field extraction (password hash is field 2 in `/etc/shadow`). Windows hashes in wrong format (NTLM is just the hash; NetNTLMv2 includes the full challenge-response). Extra whitespace or newline characters (causes parsing errors). |

---

### Task 1.5 — Understanding Hashcat Output

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Read and interpret Hashcat's runtime output: speed, progress, estimated time, temperature, and cracked hash display. Understand the potfile and `--show` flag. |
| **Skills Learned** | Runtime status (press `s` during cracking), speed interpretation (H/s = hashes per second), ETA reading, temperature monitoring, potfile concept (already-cracked hashes stored in `~/.local/share/hashcat/hashcat.potfile`), `--show` to display cracked hashes. |
| **Practical Exercise** | Run a crack attempt. Press `s` for status. Note: Speed, Progress (X/Y = candidates tested/total), Time.Estimated, Temperature. After cracking: `hashcat -m <mode> hashes.txt --show` (display cracked results). `cat ~/.local/share/hashcat/hashcat.potfile` (view all ever-cracked hashes). |
| **Expected Output** | Ability to read runtime status. Understanding of the potfile system. Ability to retrieve previously cracked hashes. |
| **Common Mistakes** | Not knowing about the potfile (Hashcat skips already-cracked hashes silently — use `--show` to see them). Running the same hashes again and thinking Hashcat failed (it skipped them because they're in the potfile — use `--potfile-disable` to force re-cracking). Not pressing `s` for status (you're cracking blind without it). |

---

### Task 1.6 — Offline vs Online: When to Use Hashcat vs Hydra

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Create a clear decision framework: Have hashes? → Hashcat. Have a live service? → Hydra. Know when each is applicable and their trade-offs. |
| **Comparison** | **Hashcat (Offline):** Needs extracted hashes, billions/sec speed, no network needed, no account lockout, no detection. **Hydra (Online):** Needs live service, ~100 attempts/sec, network dependent, account lockout risk, IDS detection. |
| **Expected Output** | Decision framework documented. Understanding that offline cracking is always preferred when hashes are available. |

---

# PHASE 2: CORE ATTACK MODES

---

### Task 2.1 — Dictionary Attack (Mode 0)

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Run a basic dictionary attack: test every word in a wordlist against the hash(es). This is the starting point for all cracking attempts. |
| **Syntax** | `hashcat -m <mode> -a 0 hashes.txt /usr/share/wordlists/rockyou.txt`. |
| **Real-World Scenario** | You extracted SHA-512 hashes from a Linux server's `/etc/shadow`. Test them against `rockyou.txt` first — it contains the 14 million most common passwords. |
| **Expected Output** | Cracked passwords displayed as `hash:password`. Understanding that dictionary attacks are fast but only find passwords in the wordlist. |
| **Common Mistakes** | Using the wrong hash mode (`-m`). Not trying the smallest effective wordlist first (start with common passwords, escalate to rockyou, then larger lists). Not checking `-a 0` is the attack mode (it's the default but being explicit is good practice). |

---

### Task 2.2 — Dictionary + Rules Attack (Mode 0 + Rules)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Apply mutation rules to dictionary words: capitalize first letter, append numbers, substitute characters (leet speak), reverse, duplicate. Rules multiply the effectiveness of any wordlist by testing variations. |
| **Syntax** | `hashcat -m <mode> -a 0 hashes.txt rockyou.txt -r /usr/share/hashcat/rules/best64.rule`. Multiple rules: `-r rule1.rule -r rule2.rule`. Common rule files: `best64.rule` (essential), `d3ad0ne.rule` (comprehensive), `rockyou-30000.rule` (massive), `dive.rule` (thorough). |
| **Real-World Scenario** | The password is `Summer2024!` — not in any wordlist. But `summer` IS in the wordlist. Rules that capitalize + append `2024!` find it. Rules transform a 14M wordlist into billions of candidates. |
| **Expected Output** | Passwords cracked that weren't in the original wordlist. Understanding that rules are the most efficient way to crack human-generated passwords. |
| **Common Mistakes** | Not using rules at all (dramatically reduces success rate). Using huge rule files on huge wordlists (multiplication: 14M words × 30K rules = 420 billion candidates — may take hours). Not understanding rule syntax (learn to read `best64.rule` entries). |

---

### Task 2.3 — Brute-Force / Mask Attack (Mode 3)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Use mask attacks to test all possible character combinations matching a pattern. This is systematic brute-force with pattern awareness — much smarter than testing every possible combination blindly. |
| **Syntax** | `hashcat -m <mode> -a 3 hashes.txt ?u?l?l?l?l?d?d?d?s`. Charsets: `?l` = lowercase, `?u` = uppercase, `?d` = digit, `?s` = special, `?a` = all printable, `?b` = all bytes. Custom charset: `-1 ?l?d` then use `?1` in the mask. Increment: `--increment --increment-min 4 --increment-max 8` (try lengths 4 through 8). |
| **Real-World Scenario** | You know the password policy requires: 1 uppercase + 5 lowercase + 2 digits + 1 special. Mask: `?u?l?l?l?l?l?d?d?s` tests all combinations matching this exact pattern. |
| **Expected Output** | Passwords cracked matching specific patterns. Understanding of keyspace calculation (how many combinations exist for a given mask). |
| **Common Mistakes** | Using `?a?a?a?a?a?a?a?a` for 8 chars (95^8 = 6.6 quadrillion combinations — takes weeks even on fast GPUs). Not using `--increment` (test shorter lengths first). Not creating pattern-aware masks (humans follow predictable patterns — exploit that). |

---

### Task 2.4 — Combinator Attack (Mode 1)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Combine every word from one wordlist with every word from another. Catches passwords like `solarwinds123`, `football2024`, `admin!password`. |
| **Syntax** | `hashcat -m <mode> -a 1 hashes.txt wordlist1.txt wordlist2.txt`. |
| **Real-World Scenario** | Create list1 with base words (`summer`, `winter`, `spring`, `company`) and list2 with suffixes (`2024`, `2023`, `!`, `123`, `@1`). Combinator produces: `summer2024`, `company!`, `winter123`, etc. |
| **Expected Output** | Passwords cracked from word combinations. Understanding that combinator is efficient for predictable password construction patterns. |
| **Common Mistakes** | Two large wordlists (multiplication creates enormous keyspace). Not thinking about word order (combinator is left+right only — swap the lists or use rules for more flexibility). |

---

### Task 2.5 — Hybrid Attacks (Modes 6 & 7)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Combine dictionary words with brute-force masks. Mode 6: wordlist + mask (append). Mode 7: mask + wordlist (prepend). Catches passwords like `password123`, `2024summer!`. |
| **Syntax** | Append digits: `hashcat -m <mode> -a 6 hashes.txt rockyou.txt ?d?d?d` (word + 3 digits). Prepend: `hashcat -m <mode> -a 7 hashes.txt ?d?d?d?d rockyou.txt` (4 digits + word). |
| **Real-World Scenario** | Common password pattern: dictionary word + 2-4 digits + optional special. `hashcat -a 6 hashes.txt wordlist.txt ?d?d?d?s` catches `summer123!`, `admin456@`. |
| **Expected Output** | Passwords cracked with appended/prepended patterns. Understanding that hybrid attacks are extremely effective against common human password patterns. |
| **Common Mistakes** | Confusing mode 6 and 7 (6 = word+mask, 7 = mask+word). Large masks with large wordlists (exponential keyspace). Not realizing this is one of the most effective attack types for real-world passwords. |

---

### Task 2.6 — Cracking Linux /etc/shadow Hashes

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Crack Linux password hashes extracted from `/etc/shadow`. Identify the hash type by prefix: `$1$` = MD5crypt, `$5$` = SHA-256crypt, `$6$` = SHA-512crypt, `$y$` = yescrypt. |
| **Practical Exercise** | Extract hashes from Metasploitable 2's `/etc/shadow` (obtained via exploitation). Identify type (likely `$1$` MD5crypt on older systems). Crack: `hashcat -m 500 linux-hashes.txt rockyou.txt -r best64.rule`. |
| **Expected Output** | Linux user passwords cracked. Credential inventory expanded. Understanding of Linux hash formats and their relative strength. |
| **Common Mistakes** | Wrong mode number (`$1$` = `-m 500`, `$5$` = `-m 7400`, `$6$` = `-m 1800`). Including non-password lines from shadow (filter out `!`, `*`, empty entries). Not using `--username` when the file contains `user:hash` format. |

---

### Task 2.7 — Cracking Windows NTLM Hashes

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Crack Windows NTLM hashes extracted from SAM, NTDS.dit, or Meterpreter's `hashdump`. NTLM is fast to crack because it's unsalted MD4. |
| **Practical Exercise** | From Meterpreter hashdump output (format: `user:RID:LM:NTLM:::`), extract NTLM portion. Crack: `hashcat -m 1000 ntlm-hashes.txt rockyou.txt -r best64.rule`. Note the cracking speed — NTLM is one of the fastest hash types. |
| **Expected Output** | Windows passwords cracked at extremely high speed. Understanding that NTLM is weak because it's unsalted (identical passwords = identical hashes across all systems). |
| **Common Mistakes** | Extracting the LM hash instead of NTLM (LM is the older, weaker hash — NTLM is the 4th field). Not understanding that NTLM's lack of salting makes it trivially fast to crack. Not using pass-the-hash instead of cracking (if you have the NTLM hash, you may not need the plaintext). |

---

# PHASE 3: INTERMEDIATE TECHNIQUES

---

### Task 3.1 — Writing Custom Rules

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | Write custom Hashcat rules to generate password candidates that match your target's likely password patterns. Rules are the most powerful feature in Hashcat. |
| **Skills Learned** | Rule syntax: `:` (do nothing), `l` (lowercase all), `u` (uppercase all), `c` (capitalize first), `t` (toggle case), `$X` (append X), `^X` (prepend X), `sa@` (substitute a→@), `d` (duplicate), `r` (reverse), `[` (delete first), `]` (delete last), `T0` (toggle position 0). |
| **Practical Exercise** | Create `custom.rule`: `:` (original word), `c` (capitalize), `c$1` (capitalize + append 1), `c$!` (capitalize + append !), `c$2$0$2$4` (capitalize + append 2024), `sa@` (a→@), `se3` (e→3), `c$!$!` (capitalize + append !!). Test: `hashcat -m 0 test-hash.txt wordlist.txt -r custom.rule`. |
| **Expected Output** | Custom rules producing expected mutations. Understanding that good rules model how humans actually create passwords. |
| **Common Mistakes** | Rules too generic (produces too many candidates). Not testing rules with `--stdout` first (`hashcat --stdout wordlist.txt -r custom.rule | head -50` shows what candidates are generated without cracking). Not understanding rule ordering (rules apply left to right). |

---

### Task 3.2 — Mask Files (.hcmask)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Create `.hcmask` files containing multiple masks to run sequentially. This automates testing multiple password patterns in one command. |
| **Syntax** | Create `patterns.hcmask`: `?u?l?l?l?l?l?d?d` (Ullllldd), `?u?l?l?l?l?d?d?d?d` (Ulllldddd), `?d?d?d?d?d?d` (6 digits), `?l?l?l?l?l?l?l?l` (8 lowercase). Run: `hashcat -m <mode> -a 3 hashes.txt patterns.hcmask`. |
| **Expected Output** | Multiple patterns tested sequentially. Understanding that mask files organize brute-force strategy. |

---

### Task 3.3 — Prince Attack (Combination Permutations)

- [ ] **Completed** · ⭐⭐⭐⭐ Intermediate-Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Use the PRINCE (PRobability INfinite Chained Elements) attack to generate password candidates by combining words from a dictionary in order of probability. More intelligent than simple combinator. |
| **Syntax** | `hashcat -m <mode> -a 0 hashes.txt wordlist.txt --prince` (if supported), or use the standalone `princeprocessor` tool: `pp64 wordlist.txt | hashcat -m <mode> hashes.txt`. |
| **Expected Output** | Passwords cracked that are combinations of multiple common words. |

---

### Task 3.4 — Cracking Wi-Fi WPA/WPA2 Handshakes

- [ ] **Completed** · ⭐⭐⭐⭐ Intermediate-Advanced · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Crack captured Wi-Fi WPA/WPA2 handshakes. Understand the capture-to-crack pipeline: capture handshake (aircrack-ng) → convert to Hashcat format → crack. |
| **Syntax** | Convert capture: `hcxpcapngtool -o hash.hc22000 capture.pcapng`. Crack: `hashcat -m 22000 hash.hc22000 rockyou.txt -r best64.rule`. |
| **Expected Output** | Wi-Fi password recovered from handshake capture. Understanding of the WPA cracking pipeline. |
| **Common Mistakes** | Not capturing a complete 4-way handshake (incomplete handshakes can't be cracked). Using the old `.hccapx` format instead of `.hc22000` (newer format). Not understanding that WPA cracking speed is limited by PBKDF2 (slow by design). |

---

### Task 3.5 — Cracking Application-Specific Hashes

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Crack hashes from web applications (WordPress, Joomla, Drupal), databases (MySQL, MSSQL, PostgreSQL), and other applications. Each uses a different hashing scheme. |
| **Key Modes** | WordPress: `-m 400` (phpass). MySQL 4.1+: `-m 300`. MSSQL: `-m 1731`. PostgreSQL MD5: `-m 12`. Drupal 7: `-m 7900`. phpBB3: `-m 400`. Kerberos TGS (Kerberoasting): `-m 13100`. |
| **Expected Output** | Application-specific hashes cracked. Understanding that each application uses different hash schemes with different cracking speeds. |

---

### Task 3.6 — Session Management & Restore

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Save and restore long-running cracking sessions. Name sessions for organization across engagements. |
| **Syntax** | Named session: `hashcat --session engagement1 -m 1800 hashes.txt rockyou.txt`. Pause: press `q` (quit and save). Restore: `hashcat --session engagement1 --restore`. |
| **Expected Output** | Sessions saved and restored without losing progress. Multiple named sessions for different engagements. |

---

# PHASE 4: ADVANCED USAGE

---

### Task 4.1 — Distributed Cracking & Team Workflow

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Split cracking work across multiple machines using `--skip` and `--limit` or Hashtopolis for centralized management. |
| **Skills Learned** | Keyspace splitting, Hashtopolis agent setup, distributed cracking architecture, cloud GPU instances for cracking (AWS p3, Google Cloud GPU). |
| **Expected Output** | Understanding of distributed cracking architecture. Ability to split work across machines. |

---

### Task 4.2 — Hash Extraction Tools & Pipelines

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Master hash extraction from various sources: `secretsdump.py` (AD hashes), `mimikatz` (Windows memory), Meterpreter `hashdump`, database dumps, web app databases, `john2hashcat` format conversion. |
| **Key Tools** | `secretsdump.py -just-dc-ntlm domain/user:pass@DC` (Active Directory). `mimikatz` → `sekurlsa::logonpasswords`. Meterpreter → `hashdump` or `load kiwi` → `creds_all`. `unshadow /etc/passwd /etc/shadow > combined.txt` (for John format). |
| **Expected Output** | Hashes extracted from multiple sources in Hashcat-ready format. |

---

### Task 4.3 — Password Analysis & Statistics

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Analyze cracked passwords for patterns: most common base words, length distribution, character set usage, policy compliance. This data goes into your pentest report. |
| **Practical Exercise** | After cracking a set of hashes: `hashcat -m <mode> hashes.txt --show | awk -F: '{print $NF}'` → save cracked passwords → analyze: `awk '{print length($0)}' cracked.txt | sort | uniq -c | sort -rn` (length distribution). `pipal cracked.txt` (password analysis tool). |
| **Expected Output** | Password analysis report: length distribution, character set usage, top base words, policy compliance percentage. |

---

### Task 4.4 — GPU Tuning & Optimization

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Optimize Hashcat performance: workload profiles (`-w`), temperature limits, device selection, kernel optimization. |
| **Syntax** | Workload profiles: `-w 1` (low), `-w 2` (default), `-w 3` (high), `-w 4` (nightmare — may freeze your GUI). Temperature limit: `--hwmon-temp-abort=90`. Device selection: `-d 1` (use device 1 only). Force CPU: `--force -D 1`. |
| **Expected Output** | Optimized cracking speed without hardware damage. Understanding of workload/temperature trade-offs. |

---

### Task 4.5 — Kerberoasting & AS-REP Roasting Hashes

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Crack Kerberos ticket hashes obtained through Kerberoasting (`-m 13100`) and AS-REP Roasting (`-m 18200`). These are critical Active Directory attack techniques. |
| **Syntax** | Kerberoast: `hashcat -m 13100 kerberoast-hashes.txt rockyou.txt -r best64.rule`. AS-REP Roast: `hashcat -m 18200 asrep-hashes.txt rockyou.txt -r best64.rule`. |
| **Expected Output** | Service account passwords cracked from Kerberos tickets. Understanding of the full Kerberoasting pipeline (request tickets → extract hashes → crack offline). |

---

# PHASE 5: TOOL INTEGRATION

---

### Task 5.1 — Metasploit → Hashcat Pipeline

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| **Workflow** | Meterpreter `hashdump` → save output → format for Hashcat → `hashcat -m 1000 ntlm.txt rockyou.txt` (Windows) or `hashcat -m 1800 shadow.txt rockyou.txt` (Linux). |

---

### Task 5.2 — Impacket → Hashcat Pipeline

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| **Workflow** | `secretsdump.py domain/user:pass@DC -just-dc-ntlm -outputfile hashes` → `hashcat -m 1000 hashes.ntds rockyou.txt -r dive.rule`. |

---

### Task 5.3 — Responder → Hashcat Pipeline

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| **Workflow** | Responder captures NetNTLMv2 hashes → `hashcat -m 5600 responder-hashes.txt rockyou.txt -r best64.rule`. |

---

### Task 5.4 — John the Ripper Comparison & Conversion

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| **Workflow** | John's `*2john` tools extract hashes from files: `ssh2john id_rsa > ssh-hash.txt`, `zip2john file.zip > zip-hash.txt`, `rar2john file.rar > rar-hash.txt`. Convert to Hashcat format. Understanding when John is better (exotic formats, `*2john` extractors) vs Hashcat (speed, GPU). |

---

# PHASE 6–8: LABS, METHODOLOGY & MASTERY

---

### Lab 6.1 — Beginner: Crack Metasploitable 2 Hashes

- [ ] **Completed** · ⭐⭐ Beginner · ⏱️ 45 min

| **Scenario** | Extract `/etc/shadow` from Metasploitable 2 (via exploitation). Crack all passwords using dictionary + rules. |
| **Success Criteria** | All crackable passwords recovered. Hash types identified. Attack modes documented. |

---

### Lab 6.2 — Intermediate: Rule-Based Cracking Challenge

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 60 min

| **Scenario** | Given a set of hashes with passwords following a known policy (8+ chars, uppercase + lowercase + digit), create custom rules optimized for this policy and crack them. |
| **Success Criteria** | Custom rules created. Higher crack rate than default rules. Rule development process documented. |

---

### Lab 6.3 — Advanced: Full Credential Report

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 90 min

| **Scenario** | Given hashes from multiple sources (Linux, Windows, web app), crack them all and produce a password analysis report with statistics, policy recommendations, and risk ratings. |
| **Success Criteria** | Multi-format hashes cracked. Password analysis report produced with pipal or custom analysis. Policy recommendations included. |

---

### Lab 6.4 — Expert: Optimized Cracking Strategy

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 120 min

| **Scenario** | Given a large set of corporate hashes, develop and execute a time-optimized cracking strategy: quick wins first (common passwords, rules), then targeted masks, then exhaustive brute-force. Document each phase's success rate. |

---

### Task 7.1 — Hashcat in the Pentest Lifecycle

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| **Objective** | Map Hashcat to PTES: Post-Exploitation (credential recovery), Reporting (password analysis, policy assessment). Hashcat is exclusively a post-exploitation tool — you need hashes first. |

---

### Task 7.2 — Hashcat Limitations

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 10 min

| **Key Limitations** | Cannot attack live services (use Hydra). Requires extracted hashes. Strong hashing (bcrypt high cost, Argon2) makes cracking impractical. GPU-dependent for speed. Cannot crack if password exceeds wordlist + rules + masks coverage. |

---

### Task 7.3 — Legal Considerations

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 10 min

| **Key Points** | Only crack hashes obtained with authorization. Cracked passwords are sensitive data — secure them. Include password analysis in your report. Recommend stronger hashing algorithms (bcrypt, Argon2) when weak hashing is found. |

---

### Challenge 8.1 — Crack Everything

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 120 min

| **Scenario** | Given 10 different hash types from a simulated engagement, identify each type, select the optimal attack mode, and crack as many as possible in 2 hours. |

---

### Challenge 8.2 — Password Audit Report

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 90 min

| **Scenario** | Produce a professional password audit report from cracked hashes: percentage cracked, time to crack, password patterns, policy violations, and hardening recommendations. |

---

### Challenge 8.3 — Teach Hashcat

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 45 min

| **Scenario** | Prepare a 15-minute demo: hashing theory, hash identification, dictionary attack, rules, mask attack. Live cracking demonstration. |

---

# 📋 FINAL COMPETENCY MATRIX

| Competency | Self-Assessment |
|:---|:---:|
| Can identify common hash types by sight | ☐ |
| Can run dictionary, rule, mask, and hybrid attacks | ☐ |
| Can write custom rules for targeted cracking | ☐ |
| Can crack Linux, Windows, and application hashes | ☐ |
| Can optimize cracking with GPU tuning | ☐ |
| Can produce password analysis reports | ☐ |
| Can integrate with Metasploit, Impacket, Responder | ☐ |
| Can explain offline vs online cracking trade-offs | ☐ |
| Can teach Hashcat to another person | ☐ |

---

## 🎯 Interview Questions

1. What is the difference between hashing, encryption, and encoding?
2. How do you identify a hash type? What tool and visual clues do you use?
3. Explain Hashcat's attack modes (0, 1, 3, 6, 7) and when to use each.
4. What are rules and why are they more effective than pure brute-force?
5. How would you crack a set of Linux SHA-512 hashes from `/etc/shadow`?
6. What is Kerberoasting and how do you crack the resulting hashes?
7. Why is NTLM so fast to crack compared to bcrypt?
8. What is a mask attack and how do you design effective masks?
9. When would you use Hashcat vs John the Ripper?
10. How do you produce a password analysis report from cracking results?
