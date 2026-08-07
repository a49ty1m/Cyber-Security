# 🚪 Gobuster: Complete Mastery Checklist

> **What is Gobuster?** Gobuster is a fast directory, file, DNS subdomain, virtual host, and S3 bucket brute-forcer written in Go. It sends parallel requests, replacing a placeholder with each word from a wordlist, and reports hits based on HTTP status codes. It is simpler than ffuf but fast, reliable, and purpose-built for discovery.
>
> **When to use it:** Quick directory and file discovery. DNS subdomain enumeration. Virtual host discovery. When you need a simple, fast, reliable discovery tool. Good first-pass tool before deeper ffuf analysis.
>
> **When to use ffuf instead:** When you need custom filtering (by size, words, regex). When fuzzing headers, POST bodies, or multiple positions. When you need auto-calibration for soft-404 handling.
>
> **What mastering Gobuster unlocks:** Fast web attack surface discovery. DNS subdomain enumeration without Amass/subfinder. Solid first-pass reconnaissance that feeds more targeted manual testing.

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals | 4 | 1–2 hours |
| 2 | Dir Mode | 5 | 2–3 hours |
| 3 | DNS Mode | 4 | 2–3 hours |
| 4 | Other Modes | 3 | 1–2 hours |
| 5 | Advanced Usage | 3 | 1–2 hours |
| 6 | Integration | 3 | 1 hour |
| 7 | Practical Labs | 3 | 2–4 hours |
| 8 | Mastery Challenges | 2 | 2–3 hours |
| | **Total** | **27** | **~12–20 hours** |

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — Modes Overview

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **dir** | Directory and file discovery (HTTP). |
| **dns** | DNS subdomain enumeration. |
| **vhost** | Virtual host discovery (HTTP Host header). |
| **fuzz** | General fuzzing (FUZZ placeholder — similar to ffuf). |
| **s3** | AWS S3 bucket enumeration. |
| **gcs** | Google Cloud Storage bucket enumeration. |

---

### Task 1.2 — Installation

- [ ] **Completed** · ⭐ Beginner · ⏱️ 5 min

| Field | Detail |
|:---|:---|
| **Kali** | `apt install gobuster`. |
| **Go** | `go install github.com/OJ/gobuster/v3@latest`. |
| **Verify** | `gobuster version`. |

---

### Task 1.3 — Global Flags

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Wordlist** | `-w wordlist.txt`. |
| **Threads** | `-t 50` (default 10). |
| **Output** | `-o results.txt`. |
| **Quiet** | `-q` — suppress banner and progress (useful for piping). |
| **No Error** | `--no-error` — suppress connection error output. |
| **Verbose** | `-v` — show all responses (including filtered). |

---

### Task 1.4 — Wordlists

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Dir** | `/usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt`. |
| **DNS** | `/usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt`. |
| **Common** | `/usr/share/wordlists/dirb/common.txt` (fast, ~5k, good first pass). |

---

# PHASE 2: DIR MODE

---

### Task 2.1 — Basic Directory Discovery

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Command** | `gobuster dir -u http://target.com -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -t 50`. |
| **Output** | Shows: `/admin (Status: 301) [Size: 312]`. Each found path with status code and response size. |

---

### Task 2.2 — File Extensions

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Command** | `gobuster dir -u http://target.com -w common.txt -x php,html,bak,txt,zip -t 50`. |
| **High Value** | `.bak`, `.old`, `.bkp` — backup files. `.env` — environment config (credentials). `.git` — source control. `config.php` — database credentials. |

---

### Task 2.3 — Status Code Filtering

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Include Codes** | `-s 200,301,302,403` — only show these codes. Default shows 200,204,301,302,307,401,403,405. |
| **Exclude Codes** | `--exclude-length 1234` — exclude responses of this length (custom 404 bypass). |
| **403 Note** | Always include 403 — it means the directory exists but access is denied. May be bypassable with path tricks. |

---

### Task 2.4 — Authentication

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Cookie** | `-c "session=abc123"` — add cookie. |
| **Header** | `-H "Authorization: Bearer token"`. |
| **HTTP Basic** | `-U username -P password`. |

---

### Task 2.5 — HTTPS and Follow Redirects

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **HTTPS** | `gobuster dir -u https://target.com -k ...`. `-k` skips TLS verification (for self-signed certs). |
| **Redirects** | `-r` — follow redirects. Without `-r`, 301/302 shows the destination in brackets. |

---

# PHASE 3: DNS MODE

---

### Task 3.1 — Basic DNS Subdomain Enumeration

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Command** | `gobuster dns -d target.com -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -t 50`. |
| **Output** | Shows resolved subdomains: `Found: mail.target.com [192.168.1.10]`. |
| **Resolver** | `-r 8.8.8.8` — use a specific DNS resolver. Useful when default resolver is slow or blocks queries. |

---

### Task 3.2 — Wildcard DNS Handling

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Problem** | Some domains have wildcard DNS: `*.target.com` → all subdomains resolve. Every word appears as a valid subdomain. |
| **Detection** | Gobuster detects wildcards automatically and warns you. |
| **Handling** | `--wildcard` flag — forces gobuster to continue even if wildcard is detected, but results will be unreliable. |
| **Alternative** | Use passive DNS tools (SecurityTrails, Shodan, crt.sh) or certificate transparency instead. |

---

### Task 3.3 — Show IP Addresses

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Flag** | `-i` — show IP addresses for found subdomains. |
| **Use** | Map subdomain → IP → feed IPs to Nmap. Find subdomains resolving to internal IPs (internal service exposed externally). |

---

### Task 3.4 — DNS Enumeration vs. Certificate Transparency

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Gobuster DNS** | Active — sends DNS queries. Limited to wordlist coverage. Detectable. |
| **crt.sh** | Passive — reads public SSL certificate logs. Finds subdomains that a wordlist would miss. No target interaction. |
| **Workflow** | crt.sh first (passive) → Gobuster DNS to fill gaps and verify. |

---

# PHASE 4: OTHER MODES

---

### Task 4.1 — Vhost Mode

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Command** | `gobuster vhost -u http://target_ip -w subdomains.txt --append-domain -t 30`. |
| **How** | Changes the `Host` header to `word.target.com` for each word. Different response = valid vhost. |
| **Filter** | `--exclude-length` to filter out the default "unknown vhost" response size. |
| **vs. ffuf** | Both work. ffuf gives more filtering options. Gobuster vhost is simpler to set up. |

---

### Task 4.2 — Fuzz Mode

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Command** | `gobuster fuzz -u "http://target.com/FUZZ" -w wordlist.txt`. |
| **vs. ffuf** | Less features than ffuf for fuzzing. Use ffuf for advanced fuzzing. Gobuster fuzz is a basic alternative. |

---

### Task 4.3 — S3 Bucket Discovery

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Command** | `gobuster s3 -w company-wordlist.txt`. |
| **What It Finds** | Publicly accessible S3 buckets. Try company name, product name, internal project names. |
| **Value** | Misconfigured public S3 buckets often contain sensitive files (database backups, code, credentials). |

---

# PHASE 5: ADVANCED USAGE

---

### Task 5.1 — Proxy and Delay

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Proxy** | `--proxy http://127.0.0.1:8080` — route through Burp. |
| **Delay** | `--delay 200ms` — wait 200ms between requests per thread. Useful for rate limit evasion. |

---

### Task 5.2 — Timeout and Retry

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Timeout** | `--timeout 5s` — request timeout. Reduce for fast networks. Increase for slow/distant targets. |
| **Retries** | Gobuster doesn't retry by default. Use `-t` (more threads) but be aware of overloading slow servers. |

---

### Task 5.3 — User-Agent

- [ ] **Completed** · ⭐ Beginner · ⏱️ 5 min

| Field | Detail |
|:---|:---|
| **Custom UA** | `-a "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"` — set a browser-like User-Agent. Some sites block non-browser UAs. |

---

# PHASE 6: INTEGRATION

---

### Task 6.1 — Gobuster + Nmap

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Workflow** | Nmap: find open ports. Port 80/443/8080 → run Gobuster dir on each HTTP service. Port 53 → run Gobuster dns. |

---

### Task 6.2 — Gobuster + ffuf

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Workflow** | Gobuster: quick first pass with medium wordlist → identifies high-level structure. ffuf: deeper analysis on found directories with larger wordlists, extension sets, and custom filtering. |

---

### Task 6.3 — Output Processing

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Save** | `-o results.txt`. |
| **Extract URLs** | `grep -oP '(?<=/).*?(?= )' results.txt` — extract paths. |
| **Filter 200s** | `grep "(Status: 200)" results.txt`. |

---

# PHASE 7: PRACTICAL LABS

---

### Lab 7.1 — Directory Discovery (DVWA)

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| **Scenario** | Run Gobuster dir against DVWA with medium wordlist + `.php,.bak` extensions. Document all found paths and their status codes. |
| **Success Criteria** | Admin path and config files identified. |

---

### Lab 7.2 — DNS Subdomain Discovery

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| **Scenario** | In a lab DNS environment (or HTB machine): run Gobuster DNS to discover subdomains. Add discovered subdomains to `/etc/hosts`. Visit each to identify additional attack surface. |
| **Success Criteria** | At least 2 subdomains discovered. Each visited. Attack surface expanded. |

---

### Lab 7.3 — HTB/THM Full Discovery

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| **Scenario** | HackTheBox/TryHackMe web machine. Run Gobuster dir first → identify interesting directories. Run vhost mode → find additional virtual hosts. Feed all findings to ffuf for deeper analysis. Document complete attack surface. |
| **Success Criteria** | Directory discovery complete. Vhosts discovered. Full attack surface documented. Path to exploitation identified. |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — Find Hidden Admin via Gobuster

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| **Scenario** | Use Gobuster to find a hidden admin panel on a CTF/HTB target. The panel must not be linked from the main site. Access the admin panel and exploit it to gain further access. |
| **Success Criteria** | Admin panel found via directory brute-force. Admin functionality accessed. |

---

### Challenge 8.2 — Wordlist Tuning

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| **Scenario** | Given a target running a specific PHP framework, generate a custom wordlist using CeWL + framework-specific SecLists. Compare results vs. generic medium wordlist. Document which approach found more unique paths. |
| **Success Criteria** | Custom wordlist created. Comparison performed. At least 3 unique paths found by custom wordlist not in generic. |

---

# 📋 FINAL COMPETENCY MATRIX

| Competency | Self-Assessment |
|:---|:---:|
| Can run directory discovery with extensions | ☐ |
| Can enumerate DNS subdomains and handle wildcard DNS | ☐ |
| Can discover virtual hosts with the vhost mode | ☐ |
| Can filter results by status code and response length | ☐ |
| Can perform authenticated discovery (cookies/headers) | ☐ |
| Can select appropriate wordlists for different tech stacks | ☐ |
| Can proxy Gobuster through Burp Suite | ☐ |
| Knows when to use Gobuster vs. ffuf | ☐ |

---

## 🎯 Interview Questions

1. What is the difference between Gobuster's `dir`, `dns`, and `vhost` modes?
2. How do you handle a target that returns 200 for all paths (custom 404)?
3. What file extensions are highest priority when fuzzing for backup files?
4. How do you use Gobuster DNS mode and what does it find?
5. What is wildcard DNS and how does Gobuster handle it?
6. When would you use Gobuster over ffuf and vice versa?
7. How do you perform authenticated directory discovery in Gobuster?
