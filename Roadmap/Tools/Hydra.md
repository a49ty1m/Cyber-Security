# 🔓 Hydra: Complete Mastery Checklist

> **What is Hydra?** Hydra (THC-Hydra) is the fastest and most flexible online password brute-forcing tool. It attacks live authentication services — SSH, FTP, HTTP, RDP, SMB, MySQL, and 50+ other protocols — by rapidly testing username/password combinations against running services.
>
> **Why does it exist?** Weak passwords remain the #1 way organizations get compromised. Hydra automates the process of testing credentials against network services, proving whether password policies are effective and whether default/weak credentials exist.
>
> **When to use it:** After enumeration reveals authentication services (SSH, FTP, HTTP login, RDP, databases). When you have usernames from enumeration and need to test passwords. When testing default credentials across many hosts. When password policy validation is in scope.
>
> **When to avoid it:** Offline hash cracking (use Hashcat/John). When account lockout policies are active (you'll lock out legitimate users). Without authorization (brute-forcing is noisy and illegal without permission). When rate limiting makes online attacks impractical.
>
> **What mastering Hydra unlocks:** Ability to validate password strength across any protocol. Credential testing automation. Understanding of authentication attack methodology. OSCP/PNPT exam readiness for credential attacks.

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md) · [🐧 Metasploitable 2 Lab](../Lab/Metasploitable_2/TASK_LIST.md) · [🌐 OWASP BWA Lab](../Lab/OWASP_Broken_WebApps/TASK_LIST.md)

| Recon & Scanning | Exploitation | Post-Exploitation | Web & Traffic |
|:-----------------|:-------------|:-------------------|:--------------|
| [🗺️ Nmap](Nmap.md) | [💀 Metasploit](Metasploit_Framework.md) | [🐉 LinPEAS](LinPEAS.md) | [🕷️ Burp Suite](Burp_Suite.md) |
| [🔌 Netcat](Netcat.md) | [🐍 Impacket](Impacket.md) | [🩸 BloodHound](BloodHound.md) | [🦈 Wireshark](Wireshark.md) |
| | **🔓 Hydra** (you are here) | [🔥 Hashcat](Hashcat.md) | |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals & Setup | 5 | 2–3 hours |
| 2 | Core Protocol Attacks | 8 | 5–7 hours |
| 3 | Intermediate Techniques | 5 | 3–5 hours |
| 4 | Advanced Usage | 5 | 4–6 hours |
| 5 | Tool Integration | 4 | 2–3 hours |
| 6 | Practical Labs | 4 | 4–8 hours |
| 7 | Methodology & Limitations | 3 | 2–3 hours |
| 8 | Mastery Challenges | 3 | 4–6 hours |
| | **Total** | **37** | **~26–41 hours** |

**Prerequisites:** Nmap (to discover authentication services). Understanding of authentication protocols. Wordlists (`/usr/share/wordlists/rockyou.txt`). A vulnerable target (Metasploitable 2).

**Alternatives:** Medusa (similar, modular), Ncrack (Nmap project, fewer protocols), Patator (Python-based, highly flexible), Burp Intruder (for HTTP), CrackMapExec (for Windows/SMB/WinRM), Crowbar (for RDP/SSH keys/VNC).

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — Understand Online vs Offline Attacks

- [ ] **Completed** · ⭐ Beginner · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand the fundamental difference: **Online attacks** (Hydra) test credentials against a LIVE service over the network. **Offline attacks** (Hashcat/John) crack password hashes locally without network interaction. Know when each is appropriate. |
| **Skills Learned** | Online brute-force mechanics, why online attacks are slow (network latency, service processing), why offline attacks are fast (GPU computation), when to use each, account lockout implications. |
| **Practical Exercise** | Write a comparison table: Online (Hydra) vs Offline (Hashcat) — speed, network requirement, detection risk, account lockout risk, prerequisites. |
| **Expected Output** | Understanding that Hydra needs a live service; Hashcat needs captured hashes. Online is slower but requires less access. Offline is faster but requires hash extraction. |
| **Common Mistakes** | Using Hydra to "crack hashes" (it can't — it attacks live services). Using Hashcat against a live service (it can't — it cracks hashes). Not considering account lockout (Hydra can lock out every account in an organization). |

---

### Task 1.2 — Installation & Supported Protocols

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Verify Hydra installation and review supported protocols. Hydra supports 50+ protocols — know the most important ones for pentesting. |
| **Skills Learned** | `hydra -h` for help, listing supported protocols, understanding that each protocol module has its own syntax requirements, identifying which protocols Hydra handles best. |
| **Practical Exercise** | `hydra -h | head -30` (version and usage). `hydra -U http-post-form` (show module-specific help). Key protocols to know: `ssh`, `ftp`, `http-get`, `http-post-form`, `rdp`, `smb`, `mysql`, `vnc`, `telnet`, `smtp`, `pop3`, `imap`. |
| **Expected Output** | Protocol list documented. Module-specific help accessed for HTTP form attacks. |
| **Common Mistakes** | Not checking protocol-specific help (`hydra -U <protocol>` shows detailed syntax). Assuming all protocols work identically (HTTP form attacks require completely different syntax than SSH). |

---

### Task 1.3 — Wordlist Selection & Preparation

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand wordlist strategy: start small and targeted before going to large lists. Know key wordlists, how to create custom lists, and how to optimize lists for the target. |
| **Skills Learned** | Wordlist sources (`/usr/share/wordlists/`, SecLists, CeWL for custom), `rockyou.txt` (14M passwords), targeted wordlist creation, wordlist mutation with `john --rules`, deduplication, sorting by probability. |
| **Practical Exercise** | Check available wordlists: `ls /usr/share/wordlists/`. Create a targeted list: `cewl http://<target> -d 2 -m 5 -w custom-wordlist.txt` (scrape target website for passwords). Combine and deduplicate: `cat list1.txt list2.txt | sort -u > combined.txt`. Check size: `wc -l combined.txt`. |
| **Expected Output** | Understanding of wordlist strategy (small targeted → medium → large). Custom wordlist generated from the target. Combined and deduplicated master wordlist. |
| **Common Mistakes** | Starting with `rockyou.txt` (14 million entries × network latency = days). Not using CeWL for target-specific words. Not deduplicating (wasted attempts on duplicate passwords). Not considering the target's password policy (if 8+ chars required, remove shorter words). |

---

### Task 1.4 — Username Enumeration First

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Always enumerate valid usernames BEFORE brute-forcing passwords. A targeted attack against known usernames is orders of magnitude more efficient than testing random usernames. |
| **Skills Learned** | Username enumeration techniques (SMTP VRFY, login error differences, LDAP queries, web application user listing, social engineering/OSINT), building targeted username lists. |
| **Practical Exercise** | Enumerate users on Metasploitable 2: `smtp-user-enum -M VRFY -U /usr/share/wordlists/metasploit/unix_users.txt -t <target>`. From Nmap scripts: `nmap --script smb-enum-users <target>`. Build username list from results. |
| **Expected Output** | List of confirmed valid usernames. Understanding that username enumeration dramatically reduces brute-force time. |
| **Common Mistakes** | Brute-forcing with a huge username list when you could enumerate first. Not trying common system accounts (root, admin, administrator, user, guest, test). Not collecting usernames from all sources (web application, SMTP, SMB, LDAP). |

---

### Task 1.5 — Basic Hydra Syntax & Options

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Master Hydra's core syntax and essential options. |
| **Skills Learned** | `-l` (single username), `-L` (username file), `-p` (single password), `-P` (password file), `-t` (threads, default 16), `-f` (stop after first match), `-V` (verbose, show each attempt), `-o` (output file), `-M` (target list file), `-s` (custom port), `-e nsr` (try null, same-as-username, reversed username). |
| **Syntax** | Single user: `hydra -l admin -P passwords.txt <target> ssh`. User list: `hydra -L users.txt -P passwords.txt <target> ssh`. Quick checks: `hydra -l admin -p admin <target> ssh` (single credential). Common extras: `hydra -L users.txt -P passwords.txt -e nsr -f -V <target> ssh`. |
| **Expected Output** | Understanding of all core flags. Quick reference created. |
| **Common Mistakes** | Confusing `-l` (lowercase, single user) with `-L` (uppercase, file). Confusing `-p` with `-P`. Not using `-e nsr` (catches null password, username-as-password, and reversed-username without adding them to the wordlist). Not using `-f` (continues testing after finding valid credentials — wasting time). |

---

# PHASE 2: CORE PROTOCOL ATTACKS

---

### Task 2.1 — SSH Brute-Force

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Brute-force SSH credentials on Metasploitable 2. SSH is the most commonly brute-forced service in pentests. |
| **Syntax** | `hydra -l msfadmin -P /usr/share/wordlists/rockyou.txt -t 4 -f <target> ssh`. Reduced threads (`-t 4`) because SSH rate-limits aggressive connections. |
| **Real-World Scenario** | Found SSH on port 22 during Nmap scan. Enumerated username "admin" via SMTP. Testing common passwords against it. |
| **Expected Output** | Valid SSH credentials discovered. Understanding of SSH's rate-limiting behavior and why low thread counts are necessary. |
| **Common Mistakes** | Using too many threads (`-t 16` default is too aggressive for SSH — causes "connection refused" errors). Not trying `-e nsr` first (catches the easiest wins). Using `rockyou.txt` when a smaller targeted list would work in seconds. |

---

### Task 2.2 — FTP Brute-Force

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Brute-force FTP credentials. FTP is less rate-limited than SSH, allowing faster attacks. Also check for anonymous access. |
| **Syntax** | `hydra -L users.txt -P passwords.txt -f <target> ftp`. Anonymous check: `hydra -l anonymous -p anonymous -f <target> ftp`. |
| **Expected Output** | Valid FTP credentials or anonymous access confirmed. |
| **Common Mistakes** | Not checking anonymous access first (it's the quickest win). Not understanding that FTP credentials may differ from SSH credentials. |

---

### Task 2.3 — HTTP GET Basic Authentication

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Brute-force HTTP Basic Authentication (the popup login dialog in browsers). Understand how Basic Auth transmits credentials (Base64-encoded in the Authorization header). |
| **Syntax** | `hydra -l admin -P passwords.txt <target> http-get /protected-directory/`. |
| **Expected Output** | Valid HTTP Basic Auth credentials. Understanding that Basic Auth sends credentials Base64-encoded (NOT encrypted) with every request. |
| **Common Mistakes** | Confusing HTTP Basic Auth (browser popup) with HTTP form login (HTML form). Using the wrong path (Hydra needs the protected URL path). Not understanding that Basic Auth over HTTP is essentially cleartext. |

---

### Task 2.4 — HTTP POST Form Brute-Force

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | Brute-force an HTML login form (like DVWA). This is the most complex Hydra module because you must specify the POST path, parameters, and the failure/success indicator string. |
| **Syntax** | `hydra -l admin -P passwords.txt <target> http-post-form "/dvwa/login.php:username=^USER^&password=^PASS^&Login=Login:Login failed:H=Cookie: PHPSESSID=abc123; security=low"`. Format: `"path:POST-parameters:failure-string[:optional-headers]"`. `^USER^` and `^PASS^` are replaced by Hydra with each attempt. `F=` prefix = failure string (show in response when login fails). `S=` prefix = success string (show in response when login succeeds). |
| **Real-World Scenario** | Most web applications use HTML form logins, not Basic Auth. You need to capture the exact POST request in Burp first, then translate it to Hydra syntax. |
| **Expected Output** | Valid web application credentials discovered. Understanding of the `http-post-form` module syntax. |
| **Common Mistakes** | Getting the failure string wrong (Hydra reports every attempt as "successful" if the failure string isn't found). Not including required cookies (DVWA needs PHPSESSID). Not handling CSRF tokens (Hydra can't refresh CSRF tokens — use Burp Intruder or custom scripts). Not URL-encoding special characters in the POST body. Wrong POST parameter names (capture the exact request in Burp first). |

---

### Task 2.5 — SMB Brute-Force

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Brute-force SMB (Windows file sharing) credentials. SMB is a high-value target because valid credentials give file share access and potentially remote command execution. |
| **Syntax** | `hydra -L users.txt -P passwords.txt <target> smb`. |
| **Expected Output** | Valid SMB credentials. Understanding that SMB credentials can be used for share access, psexec, WMI, and pass-the-hash. |
| **Common Mistakes** | Account lockout (Windows often locks accounts after 3-5 failed attempts). Not checking the lockout policy before brute-forcing. Not trying CrackMapExec instead (better for SMB-specific attacks). |

---

### Task 2.6 — RDP Brute-Force

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Brute-force Remote Desktop Protocol credentials. RDP is a high-value target — valid credentials give full GUI access to Windows systems. |
| **Syntax** | `hydra -l administrator -P passwords.txt -t 1 -f <target> rdp`. Use `-t 1` (one thread) — RDP is extremely slow and disconnects aggressively. |
| **Expected Output** | Valid RDP credentials. Understanding that RDP brute-forcing is very slow and risky (account lockout, NLA complications). |
| **Common Mistakes** | Using high thread counts (RDP crashes with multiple connections). Not accounting for Network Level Authentication (NLA). Account lockout (often 3-5 attempts). RDP brute-forcing is better done with Crowbar or custom tools. |

---

### Task 2.7 — Database Brute-Force (MySQL, PostgreSQL)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Brute-force database credentials for directly exposed database services. |
| **Syntax** | MySQL: `hydra -l root -P passwords.txt <target> mysql`. PostgreSQL: `hydra -l postgres -P passwords.txt <target> postgres`. |
| **Expected Output** | Valid database credentials. Understanding that database access = full data access = critical finding. |
| **Common Mistakes** | Not trying default credentials first (`root:root`, `root:` (blank), `postgres:postgres`). Not checking if the database allows remote connections (MySQL defaults to localhost-only). |

---

### Task 2.8 — Multi-Target Brute-Force

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Test credentials across multiple hosts simultaneously using Hydra's `-M` flag. Useful when the same credentials may work on multiple servers. |
| **Syntax** | `hydra -l admin -P passwords.txt -M targets.txt ssh`. Where `targets.txt` contains one IP per line. |
| **Expected Output** | Credentials tested against all hosts. Valid logins identified across the network. |
| **Common Mistakes** | Not creating proper target files (one IP per line, no trailing whitespace). Not limiting threads when scanning many hosts (network saturation). |

---

# PHASE 3: INTERMEDIATE TECHNIQUES

---

### Task 3.1 — Credential Stuffing with Pitchfork-Style Attacks

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Hydra's `-C` flag for credential stuffing: testing pre-paired username:password combinations from a colon-separated file. This is different from brute-forcing (which tests all combinations). |
| **Syntax** | Create `creds.txt`: `admin:admin\nadmin:password\nroot:root\nuser:user123`. Run: `hydra -C creds.txt <target> ssh`. |
| **Expected Output** | Only paired credentials tested (not all combinations). Faster and more targeted than full brute-force. |
| **Common Mistakes** | Confusing `-C` (colon-separated pairs) with `-L`/`-P` (all combinations). Wrong file format (must be `username:password`, one per line). |

---

### Task 3.2 — Password Spray Attacks

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Perform a password spray: test ONE password against MANY usernames before moving to the next password. This avoids account lockout (each account sees only 1-2 failed attempts). |
| **Syntax** | `hydra -L users.txt -p "Summer2024!" -f <target> smb`. Then manually change the password and run again. For automated spraying with delay: use CrackMapExec or a custom script with sleep intervals. |
| **Expected Output** | Valid credentials found without triggering account lockout. Understanding of spray vs brute-force trade-offs. |
| **Common Mistakes** | Hydra doesn't natively support spray timing (it tests all users with one password, but then immediately moves to the next password — you need manual delays or a different tool). Not knowing the lockout threshold (spray strategy depends on it). Using generic passwords instead of seasonal/contextual ones (e.g., `CompanyName2024!`, `Season+Year+!`). |

---

### Task 3.3 — Custom Port & SSL Configuration

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Attack services running on non-standard ports and services requiring SSL/TLS connections. |
| **Syntax** | Custom port: `hydra -l admin -P passwords.txt -s 2222 <target> ssh` (SSH on port 2222). SSL: `hydra -l admin -P passwords.txt -S <target> https-post-form "..."` (HTTPS). Or: `hydra -l admin -P passwords.txt -s 8443 -S <target> https-get /admin/`. |
| **Expected Output** | Successful attacks against non-standard ports and SSL-protected services. |
| **Common Mistakes** | Forgetting `-s` for non-standard ports. Forgetting `-S` for SSL. Using `http-post-form` when the target uses HTTPS (`https-post-form` or `-S` flag). |

---

### Task 3.4 — Output Management & Restoring Sessions

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Save Hydra results to files, use verbose output for debugging, and restore interrupted sessions. |
| **Syntax** | Save results: `hydra -o results.txt -L users.txt -P passwords.txt <target> ssh`. JSON output: `hydra -b json -o results.json ...`. Restore: `hydra -R` (resumes the last interrupted session from `hydra.restore`). Verbose: `-V` (show every attempt), `-d` (debug mode). |
| **Expected Output** | Results saved to file. Interrupted session restored. Understanding of when verbose/debug modes are needed. |
| **Common Mistakes** | Not saving output (results are lost when terminal closes). Not knowing about `-R` restore (restarting from scratch wastes time). Using `-V` on large wordlists (floods the terminal — use `-o` to save instead). |

---

### Task 3.5 — Dealing with Rate Limiting & Timeouts

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Handle services that rate-limit or timeout connections. Tune Hydra's connection parameters for reliability. |
| **Syntax** | Reduce threads: `-t 4` or `-t 1`. Connection timeout: `-w 10` (wait 10 seconds). Response timeout: `-W 5`. Wait between attempts: use with `-c <seconds>` per connection attempt. |
| **Expected Output** | Stable brute-force against rate-limited services. No "connection refused" errors. |
| **Common Mistakes** | Ignoring "too many connections" errors (reduce threads). Not adjusting timeouts for slow targets. Not understanding that some services ban IPs after too many failures (need to IP-rotate or slow down). |

---

# PHASE 4: ADVANCED USAGE

---

### Task 4.1 — HTTPS Form Attacks with Session Cookies & CSRF

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | Attack complex web login forms that require: SSL, session cookies, CSRF tokens, and specific headers. This is where most beginners fail with Hydra. |
| **Skills Learned** | Capturing exact POST requests from Burp, translating Burp requests to Hydra syntax, handling cookies with `H=Cookie:`, understanding Hydra's HTTP form module limitations, when to switch to Burp Intruder or custom scripts. |
| **Practical Exercise** | Capture a DVWA login request in Burp. Note: POST path, all parameters (including CSRF token), failure string, required cookies. Translate to Hydra syntax. If CSRF changes per request → Hydra can't handle it → use Burp Intruder. |
| **Expected Output** | Successful attack against a cookie-required web form. Understanding of when Hydra's HTTP module fails (dynamic CSRF tokens). |
| **Common Mistakes** | Not capturing the exact request from Burp first (guessing parameters fails). CSRF token rotation breaking every attempt (use Burp Intruder instead). Wrong failure string (Hydra reports false positives). Not URL-encoding special characters. |

---

### Task 4.2 — Attacking Services with Key-Based Auth (SSH Keys)

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Test SSH services for key-based authentication. If you have a stolen SSH private key, test it against discovered hosts. Use Crowbar for SSH key spraying. |
| **Skills Learned** | SSH key-based authentication testing, Hydra limitations with SSH keys (limited support), Crowbar as a better tool for SSH key attacks, key passphrase brute-forcing with John. |
| **Practical Exercise** | If you have a stolen key: `ssh -i stolen_key user@<target>`. Key passphrase cracking: `ssh2john stolen_key > hash.txt && john hash.txt --wordlist=rockyou.txt`. Multiple targets: `crowbar -b sshkey -s <targets>/32 -u root -k /path/to/keys/`. |
| **Expected Output** | Understanding of key-based authentication attacks. SSH key passphrase cracking workflow. |

---

### Task 4.3 — Parallel Service Attacks

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Attack multiple protocols on the same target simultaneously by running multiple Hydra instances. Understand resource management and interference risks. |
| **Practical Exercise** | Terminal 1: `hydra -l admin -P pass.txt <target> ssh -o ssh-results.txt &`. Terminal 2: `hydra -l admin -P pass.txt <target> ftp -o ftp-results.txt &`. Terminal 3: `hydra -l root -P pass.txt <target> mysql -o mysql-results.txt &`. |
| **Expected Output** | Parallel attacks against multiple services. Results from each saved to separate files. |
| **Common Mistakes** | Overloading the target with too many parallel attacks. Not saving to separate output files. Not monitoring all instances for errors. |

---

### Task 4.4 — Hydra for Bug Bounty & CTF

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand when Hydra is appropriate in bug bounty (rarely — most programs prohibit brute-forcing) and CTFs (commonly — weak credentials are intentional). |
| **Key Considerations** | Bug bounty: check program rules first — most prohibit brute-force attacks. CTFs: weak credentials are common puzzles — use small targeted wordlists. Always check for default credentials manually before automating. Rate limiting and lockout may be part of the challenge. |

---

### Task 4.5 — Alternative Tools Comparison

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Compare Hydra with alternatives and know when each is the better choice. |
| **Comparison** | **Medusa:** Similar to Hydra, modular, slightly different syntax. **CrackMapExec:** Better for SMB/WinRM/LDAP, supports pass-the-hash. **Burp Intruder:** Better for HTTP with CSRF tokens and complex sessions. **Patator:** Python-based, most flexible for edge cases. **Crowbar:** Better for RDP and SSH key attacks. **Spray:** Better for password spraying with lockout awareness. |

---

# PHASE 5: TOOL INTEGRATION

---

### Task 5.1 — Nmap → Hydra Pipeline

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| **Workflow** | `grep "22/open" scan.gnmap | awk '{print $2}' > ssh-targets.txt` → `hydra -L users.txt -P passwords.txt -M ssh-targets.txt ssh -o ssh-results.txt`. |

---

### Task 5.2 — Hydra → Metasploit Pipeline

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| **Workflow** | Hydra discovers `admin:password123` for SSH → Metasploit: `use auxiliary/scanner/ssh/ssh_login` → `set USERNAME admin` → `set PASSWORD password123` → `run` → session obtained. |

---

### Task 5.3 — OSINT → CeWL → Hydra Pipeline

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| **Workflow** | Scrape target website for words: `cewl http://<target> -d 3 -m 5 -w cewl-words.txt` → Mutate with rules: `john --rules --wordlist=cewl-words.txt --stdout > mutated.txt` → Attack: `hydra -l admin -P mutated.txt <target> ssh`. |

---

### Task 5.4 — Hydra + Metasploitable 2: Full Credential Audit

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| **Workflow** | Nmap identifies all auth services → test default credentials manually → Hydra automated attack against SSH, FTP, Telnet, MySQL, PostgreSQL → compile credential inventory → use credentials for further exploitation. |

---

# PHASE 6: PRACTICAL LABS

---

### Lab 6.1 — Beginner: Brute-Force SSH on Metasploitable 2

- [ ] **Completed** · ⭐⭐ Beginner · ⏱️ 30 min

| **Scenario** | Discover the SSH service on Metasploitable 2 with Nmap. Create a small targeted wordlist. Brute-force SSH with Hydra. |
| **Success Criteria** | Valid SSH credentials found. Login verified with `ssh`. Process documented. |

---

### Lab 6.2 — Intermediate: HTTP Form Brute-Force on DVWA

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 60 min

| **Scenario** | Capture the DVWA login request in Burp. Translate it to Hydra syntax. Brute-force the login. |
| **Success Criteria** | Correct Hydra syntax for DVWA's POST form. Valid credentials discovered. Understanding of failure string identification. |

---

### Lab 6.3 — Advanced: Multi-Protocol Credential Audit

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 90 min

| **Scenario** | Perform a complete credential audit of Metasploitable 2: SSH, FTP, Telnet, MySQL, PostgreSQL, VNC, HTTP. Compile a credential matrix. |
| **Success Criteria** | All discoverable credentials found. Professional credential audit report produced. |

---

### Lab 6.4 — Expert: Password Spray Simulation

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 60 min

| **Scenario** | Set up a password spray scenario: 20 enumerated usernames, test the top 5 most common passwords against all accounts without triggering a lockout threshold of 3 failures. |
| **Success Criteria** | Spray completed without any account lockout. Valid credentials discovered. Timing and methodology documented. |

---

# PHASE 7: METHODOLOGY

---

### Task 7.1 — Hydra in the Pentest Lifecycle

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| **Objective** | Map Hydra to PTES: Vulnerability Analysis (testing default credentials), Exploitation (credential-based access). Hydra is NOT a reconnaissance tool — it requires prior enumeration results. |

---

### Task 7.2 — Hydra Limitations

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| **Key Limitations** | Cannot crack offline hashes (use Hashcat/John). Cannot handle dynamic CSRF tokens in web forms. Account lockout risk. Slow compared to offline cracking. Noisy — easily detected by IDS/SIEM. Poor rate control compared to custom scripts. Some protocols poorly supported. |

---

### Task 7.3 — Legal & Ethical Considerations

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 10 min

| **Key Points** | ALWAYS have written authorization. Document the lockout policy before testing. Start with small targeted lists. Know when to stop (after finding one valid credential, you've proven the point). Report account lockout risks in your findings. Clean up any locked accounts after testing. |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — Complete Credential Audit Report

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 90 min

| **Scenario** | Perform a full credential audit of your lab network and produce a professional report: services tested, credentials found, risk rating, and remediation (password policy, MFA, account lockout). |

---

### Challenge 8.2 — Custom Hydra Automation Script

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 120 min

| **Scenario** | Write a Bash script that: reads Nmap results → extracts all authentication services → runs targeted Hydra attacks against each → compiles results into a report. |

---

### Challenge 8.3 — Teach Hydra

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 45 min

| **Scenario** | Prepare a 15-minute demo: online vs offline attacks, SSH brute-force, HTTP form attacks, wordlist strategy. Live demo against Metasploitable 2. |

---

# 📋 FINAL COMPETENCY MATRIX

| Competency | Self-Assessment |
|:---|:---:|
| Can brute-force SSH, FTP, Telnet credentials | ☐ |
| Can attack HTTP Basic Auth and POST form logins | ☐ |
| Can perform password spray attacks safely | ☐ |
| Can select and create appropriate wordlists | ☐ |
| Can handle rate limiting and account lockout risks | ☐ |
| Can integrate Hydra with Nmap and Metasploit | ☐ |
| Can explain when to use Hydra vs alternatives | ☐ |
| Can produce a professional credential audit report | ☐ |
| Can teach Hydra to another person | ☐ |

---

## 🎯 Interview Questions

1. What is the difference between online and offline password attacks?
2. Explain the Hydra syntax for attacking an HTTP POST login form.
3. What is a password spray and how does it differ from brute-force?
4. How do you handle CSRF tokens in Hydra attacks?
5. What wordlist strategy do you use and why?
6. When would you use CrackMapExec instead of Hydra?
7. How do you avoid account lockout during credential testing?
8. What is `-e nsr` and why should you always use it?
