# 🔍 Nikto: Complete Mastery Checklist

> **What is Nikto?** Nikto is an open-source web server vulnerability scanner. It sends a large number of HTTP requests to a web server, checking for: known CVEs in web server software, dangerous default files, misconfigured headers, information disclosure, outdated server versions, and thousands of known vulnerable paths. It gives you a rapid first-pass vulnerability picture of any web server in minutes.
>
> **Why does it exist?** Manually checking a web server against thousands of known issues is impractical. Nikto automates this — running a comprehensive, signature-based scan that surfaces common, well-known issues immediately. It's not a deep application scanner (that's Burp Suite's job), but it catches the low-hanging fruit very fast.
>
> **When to use it:** After identifying an HTTP/HTTPS service with Nmap. First-pass web server assessment before manual testing. CTF machines — Nikto often surfaces the entry point quickly. Checking for default files, outdated software, and security headers in one command.
>
> **When to avoid it:** Nikto is very noisy — it generates thousands of requests in a short time. Don't use it on production systems without authorization. When stealth is required, Nikto is not the right tool. It doesn't replace Burp Suite for application-level testing.
>
> **What mastering Nikto unlocks:** Fast web server vulnerability fingerprinting. Security header analysis. Default file and credential discovery. The starting point before deeper manual web application testing.

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals | 4 | 1–2 hours |
| 2 | Core Scanning | 5 | 2–3 hours |
| 3 | Output and Reporting | 3 | 1–2 hours |
| 4 | Advanced Options | 4 | 2–3 hours |
| 5 | Interpreting Results | 4 | 2–3 hours |
| 6 | Integration | 3 | 1–2 hours |
| 7 | Practical Labs | 3 | 2–4 hours |
| 8 | Mastery Challenges | 2 | 2–3 hours |
| | **Total** | **28** | **~13–22 hours** |

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — What Nikto Checks

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Server Software** | Outdated Apache, Nginx, IIS, Tomcat versions with known CVEs. |
| **Default Files** | Default installation pages, test scripts, sample apps left on the server. |
| **Security Headers** | Missing or misconfigured: `X-Frame-Options`, `X-XSS-Protection`, `Content-Security-Policy`, `Strict-Transport-Security`, `X-Content-Type-Options`. |
| **Dangerous Files** | `/admin/`, `/backup/`, `/.git/`, `phpinfo.php`, `/server-status`, `/server-info`. |
| **Outdated Libraries** | jQuery versions, PHP versions, CMS versions compared against known CVE databases. |
| **HTTP Methods** | Dangerous enabled methods: TRACE, PUT, DELETE. |
| **SSL/TLS** | Weak ciphers, expired certs, insecure protocol versions (SSLv3, TLS 1.0). |

---

### Task 1.2 — Installation

- [ ] **Completed** · ⭐ Beginner · ⏱️ 5 min

| Field | Detail |
|:---|:---|
| **Kali** | Pre-installed. `nikto -Version`. |
| **Manual** | `git clone https://github.com/sullo/nikto`. `perl nikto.pl`. |
| **Perl** | Nikto requires Perl. |

---

### Task 1.3 — Basic Syntax

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Target** | `nikto -h http://target.com` or `nikto -h target_ip`. |
| **Port** | `-p 8080` — non-standard port. |
| **SSL** | `-ssl` — force HTTPS. Or just use `https://` in the URL. |
| **Output** | `-o output.html -Format htm` — HTML report. `-o output.txt -Format txt`. `-o output.csv -Format csv`. |

---

### Task 1.4 — Nikto vs. Other Web Scanners

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Nikto** | Server-level. Fast. Signature-based. Not application-aware. Best for: server software issues, headers, default files. |
| **Burp Suite** | Application-level. Interactive proxy + active scanner. Best for: XSS, SQLi, IDOR, logic flaws. |
| **OWASP ZAP** | Application-level. Open source Burp alternative. |
| **Workflow** | Nikto first (server-level picture in minutes) → Burp/ZAP for application-level deep dive. |

---

# PHASE 2: CORE SCANNING

---

### Task 2.1 — Basic Scan

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Command** | `nikto -h http://target.com`. |
| **Duration** | A standard scan takes 2–10 minutes depending on the server and network speed. |
| **Output** | Shows findings as they're discovered. Each line: `+ OSVDB-XXXX: /path: Finding description`. |

---

### Task 2.2 — Scanning Through a Proxy

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Burp Proxy** | `nikto -h http://target.com -useproxy http://127.0.0.1:8080`. All Nikto requests visible in Burp history. Manually review interesting requests/responses. |

---

### Task 2.3 — Authentication

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **HTTP Basic** | `nikto -h http://target.com -id user:password`. |
| **Cookie** | `nikto -h http://target.com -C "session=abc123"`. |

---

### Task 2.4 — Scan Multiple Targets

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **File** | `nikto -h targets.txt` — one host:port per line. |
| **Nmap Integration** | `nmap -p80,443,8080 192.168.1.0/24 -oG - | nikto -h -` — pipe Nmap results directly to Nikto. |

---

### Task 2.5 — Scan Tuning

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Tuning** | `-T` flag selects test categories. `-T 1` — interesting files. `-T 2` — misconfiguration. `-T 4` — injection (XSS, SQLi). `-T 9` — SQL injection. Multiple: `-T 124` — tests 1, 2, and 4. |
| **No SSL** | `-nossl` — skip SSL checks. |
| **404 detection** | `-404code 403` — tell Nikto that 403 means file exists. |

---

# PHASE 3: OUTPUT AND REPORTING

---

### Task 3.1 — Output Formats

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **HTML** | `nikto -h target -o report.html -Format htm` — best for sharing with clients. |
| **CSV** | `-o findings.csv -Format csv` — import into Excel/spreadsheet. |
| **XML** | `-o findings.xml -Format xml` — import into Metasploit or other tools. |
| **Text** | `-o findings.txt -Format txt` — grep-able plain text. |

---

### Task 3.2 — Reading Nikto Output

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **OSVDB** | Each finding cites an OSVDB-ID (Open Source Vulnerability Database reference). Look up for more detail. |
| **+** | Each line starting with `+` is a finding. |
| **Priority** | Prioritize: CVE references > default credentials > dangerous files > missing headers > informational. |

---

### Task 3.3 — False Positive Awareness

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Rule** | Nikto reports findings based on signatures. Always verify manually — visit the path in a browser or curl it. Many findings are false positives (server responds 200 to everything, or path exists but is harmless). |
| **Verify** | `curl -v http://target.com/path/from/nikto` — verify the finding is real and accessible. |

---

# PHASE 4: ADVANCED OPTIONS

---

### Task 4.1 — Evasion Techniques

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Evasion Mode** | `-evasion 1` — random URL encoding. `-evasion 2` — directory self-reference. `-evasion 3` — premature URL ending. Multiple: `-evasion 12` (both 1 and 2). |
| **Purpose** | Try to bypass IDS/WAF signatures. Not always effective against modern WAFs. |

---

### Task 4.2 — Timing

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Delay** | `-D 1` — 1-second delay between requests. Slows scan but reduces chance of rate limiting. |
| **Timeout** | `-timeout 10` — 10-second request timeout. |

---

### Task 4.3 — Plugin Selection

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **List Plugins** | `nikto -list-plugins`. |
| **Run Specific** | `nikto -h target -Plugins "headers;ssl"` — run only headers and SSL plugins. |

---

### Task 4.4 — Virtual Host Scanning

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **vhost** | `nikto -h 192.168.1.10 -vhost admin.target.com` — sends Host header as the virtual hostname while connecting to the IP. |

---

# PHASE 5: INTERPRETING RESULTS

---

### Task 5.1 — Security Header Findings

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **X-Frame-Options** | Missing → clickjacking possible. Add: `X-Frame-Options: DENY`. |
| **Content-Security-Policy** | Missing → XSS easier. Add CSP that restricts script sources. |
| **Strict-Transport-Security** | Missing on HTTPS → HSTS not enforced. Add: `Strict-Transport-Security: max-age=31536000`. |
| **X-Content-Type-Options** | Missing → MIME sniffing possible. Add: `X-Content-Type-Options: nosniff`. |
| **Referrer-Policy** | Missing → information leakage via Referer header. |

---

### Task 5.2 — Default Files and Credentials

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **phpinfo.php** | Exposes full PHP configuration, server paths, environment variables. Remove from production. |
| **Default Pages** | `/apache2-default/`, `/xampp/`, `/iisstart.htm` — server was never properly configured. |
| **Default Creds** | Nikto may flag default credential paths. Test: admin/admin, admin/password on any admin panel found. |

---

### Task 5.3 — Dangerous HTTP Methods

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **TRACE** | `nikto: TRACE method is active` → Cross-Site Tracing (XST). Can expose cookies in some scenarios. |
| **PUT** | PUT enabled → can upload files to the server directly. Test: `curl -X PUT http://target/shell.php -d "@shell.php"`. |
| **DELETE** | DELETE enabled on writable resources → can delete files. |

---

### Task 5.4 — CVE Findings

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Priority** | Any finding with a CVE reference deserves immediate attention. Nikto may flag: `Apache 2.4.49 - CVE-2021-41773 Path Traversal/RCE`. |
| **Verify** | Look up the CVE. Check the exact version. If version matches: test the exploit. |
| **Searchsploit** | `searchsploit apache 2.4.49` — find available exploits. |

---

# PHASE 6: INTEGRATION

---

### Task 6.1 — Nikto + Nmap Pipeline

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Command** | `nmap -p 80,443,8080,8443 192.168.1.0/24 --open -oG - | grep "/open" | awk '{print $2}' | xargs -I{} nikto -h http://{} -o nikto_{}.txt`. |
| **Result** | Automated Nikto scan of all discovered web servers in the network range. |

---

### Task 6.2 — Nikto + ffuf Workflow

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Order** | Nikto first → identifies known dangerous paths and server version. ffuf → deeper directory enumeration using appropriate wordlists based on tech stack identified by Nikto. |

---

### Task 6.3 — Nikto + Burp Suite

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Workflow** | Nikto finds interesting paths → copy to Burp Repeater → manually explore. Nikto through Burp proxy → all requests logged for later replay. |

---

# PHASE 7: PRACTICAL LABS

---

### Lab 7.1 — Nikto on DVWA

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| **Scenario** | Run Nikto against DVWA (Damn Vulnerable Web App). Review output. Identify: missing security headers, dangerous files, server version. Verify each finding manually with curl. |
| **Success Criteria** | All findings verified. Security headers status documented. |

---

### Lab 7.2 — HTB/THM Web Machine

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| **Scenario** | Run Nikto against an HTB/THM web machine as part of initial enumeration. Identify findings that point toward the entry point. Use Nikto output to guide ffuf and Burp testing. |
| **Success Criteria** | Nikto finding leads to a foothold or useful intelligence. Nikto integrated into the full workflow. |

---

### Lab 7.3 — CVE Verification

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| **Scenario** | Set up a deliberately outdated Apache or Nginx version in a VM. Run Nikto. Find the CVE finding. Look up the exploit. Verify it against the lab server. |
| **Success Criteria** | CVE found by Nikto. Exploit verified successfully on the lab server. |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — Full Web Recon Report

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| **Scenario** | Run Nikto against a lab web application. Write a professional recon report from the output: server version, security headers status, dangerous files found, CVEs identified. Include remediation recommendations for each finding. |
| **Success Criteria** | Professional report written. Every finding includes: evidence, risk level, remediation recommendation. |

---

### Challenge 8.2 — Nikto in an Automated Pipeline

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| **Scenario** | Write a bash script that: takes a subnet range, runs Nmap to find web servers, runs Nikto against each web server found, consolidates all findings into a single report. |
| **Success Criteria** | Script functional. Multi-target Nikto scan automated. Findings consolidated. |

---

# 📋 FINAL COMPETENCY MATRIX

| Competency | Self-Assessment |
|:---|:---:|
| Can run a basic Nikto scan against HTTP and HTTPS targets | ☐ |
| Can use tuning flags to target specific test categories | ☐ |
| Can route Nikto through Burp Suite for request inspection | ☐ |
| Can interpret missing security header findings | ☐ |
| Can identify and verify CVE findings from Nikto output | ☐ |
| Can scan multiple targets using file input and Nmap integration | ☐ |
| Can generate HTML/CSV reports from Nikto | ☐ |
| Understands Nikto's limitations vs. application-level scanners | ☐ |

---

## 🎯 Interview Questions

1. What categories does Nikto check during a web server scan?
2. How do you route Nikto traffic through Burp Suite?
3. What is the difference between Nikto and Burp Suite's active scanner?
4. How do you interpret a missing `X-Frame-Options` header finding?
5. What does an enabled HTTP TRACE method allow an attacker to do?
6. How do you integrate Nikto with Nmap to scan all web servers in a network?
7. How do you reduce false positives in Nikto results?
8. What scan tuning flag would you use to focus only on SQL injection tests?
