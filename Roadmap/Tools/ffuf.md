# 🌀 ffuf: Complete Mastery Checklist

> **What is ffuf?** ffuf (Fuzz Faster U Fool) is a fast, flexible web fuzzer written in Go. It uses a wordlist to replace the `FUZZ` keyword in any part of an HTTP request — URL path, query string, POST body, headers, or virtual host. It's the primary tool for: directory and file discovery, virtual host enumeration, parameter fuzzing, and API endpoint discovery.
>
> **Why does it exist?** Web application attack surfaces are far larger than what's visible in the browser. Hidden endpoints, backup files, admin panels, old API versions, and misconfigured directories are only discoverable by systematically testing many possible paths. ffuf does this at high speed with flexible filtering options.
>
> **When to use it:** Directory and file bruteforce. Virtual host (vhost) enumeration. API endpoint discovery. Parameter fuzzing. Whenever you need to systematically probe all possible values for any part of an HTTP request.
>
> **When to avoid it:** When you need authenticated fuzzing with complex session management (Burp Intruder handles this better). When you need full crawler-based discovery (a spider explores links; ffuf only tests what's in the wordlist).
>
> **What mastering ffuf unlocks:** Complete web application attack surface discovery. Finding hidden admin panels, backup files, and legacy endpoints. API endpoint enumeration. Virtual host discovery for multi-tenant applications. Core skill for web pentesting and bug bounty.
>
> **ffuf vs feroxbuster:** [feroxbuster](https://github.com/epi052/feroxbuster) is a popular alternative written in Rust — it is faster than ffuf for recursive directory brute-force, handles auto-recursion natively, and has good output filtering. **ffuf** is more flexible for non-directory fuzzing (headers, POST body, query params, vhosts) and has a larger community of wordlist examples. For directory brute-force: either works. For anything beyond directories (parameter fuzzing, vhost, body fuzzing): ffuf is the standard choice. Learn ffuf first — then try feroxbuster for recursive directory work.

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals | 5 | 2–3 hours |
| 2 | Directory Fuzzing | 5 | 3–4 hours |
| 3 | Filtering and Matching | 4 | 2–3 hours |
| 4 | Advanced Fuzzing | 5 | 3–4 hours |
| 5 | Integration | 3 | 1–2 hours |
| 6 | Wordlist Strategy | 3 | 1–2 hours |
| 7 | Practical Labs | 4 | 4–6 hours |
| 8 | Mastery Challenges | 3 | 3–4 hours |
| | **Total** | **32** | **~19–28 hours** |

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — How ffuf Works

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Mechanism** | Replace the `FUZZ` keyword in a request with each line of a wordlist. Send the request. Analyze the response (status code, size, words, lines). Report interesting results. |
| **Placement** | `FUZZ` can go anywhere: URL path, query string, POST body, header values. Multiple `FUZZ` keywords for multi-position fuzzing (use `W1`/`W2`). |
| **Speed** | Written in Go with concurrent goroutines. Default 40 concurrent requests. Much faster than Python/Perl equivalents. |

---

### Task 1.2 — Installation

- [ ] **Completed** · ⭐ Beginner · ⏱️ 5 min

| Field | Detail |
|:---|:---|
| **Kali** | Pre-installed. `ffuf -V`. |
| **Go install** | `go install github.com/ffuf/ffuf/v2@latest`. |
| **Binary** | Download from GitHub releases. |

---

### Task 1.3 — Essential Flags

- [ ] **Completed** · ⭐ Beginner · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Target** | `-u http://target.com/FUZZ` — URL with FUZZ placeholder. |
| **Wordlist** | `-w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt`. |
| **Match** | `-mc 200,301,302` — match these status codes. |
| **Filter** | `-fc 404` — filter out 404 responses. `-fs 1234` — filter responses of this size. `-fw 10` — filter by word count. |
| **Extensions** | `-e .php,.html,.bak,.txt` — append extensions to each wordlist word. |
| **Threads** | `-t 50` — 50 concurrent threads. |
| **Output** | `-o results.json -of json` — save results. |
| **Headers** | `-H "Authorization: Bearer token"` — add header. |
| **Verbose** | `-v` — show full URL in output. |

---

### Task 1.4 — Wordlists for ffuf

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **SecLists** | `apt install seclists` or `git clone https://github.com/danielmiessler/SecLists`. The gold standard. |
| **Directory** | `SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt` (220k words). `raft-large-directories.txt` (comprehensive). |
| **Files** | `raft-large-files.txt`. `common.txt`. |
| **API** | `SecLists/Discovery/Web-Content/api/objects.txt`. |
| **Extensions** | `-e .php,.asp,.aspx,.jsp,.html,.bak,.old,.txt,.zip`. |

---

### Task 1.5 — Baseline Response Analysis

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Before fuzzing, understand what a "normal" non-existent response looks like. |
| **Test** | `curl -v http://target.com/doesnotexist12345` — note: status code (usually 404 or custom), response size, response body. |
| **Custom 404** | If the server returns 200 for all URLs (custom 404 page), filter by response size: `-fs <size_of_custom_404_page>`. |

---

# PHASE 2: DIRECTORY FUZZING

---

### Task 2.1 — Basic Directory Discovery

- [ ] **Completed** · ⭐ Beginner · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Command** | `ffuf -u http://target.com/FUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -mc 200,301,302,403`. |
| **Interesting Codes** | 200: exists and accessible. 301/302: redirects (follow them). 403: exists but forbidden (note it — may be bypassable). |

---

### Task 2.2 — File Discovery with Extensions

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Command** | `ffuf -u http://target.com/FUZZ -w raft-large-files.txt -e .php,.html,.bak,.txt,.zip -mc 200,301`. |
| **High Value** | `.bak` and `.old` files (source code backups). `.git/` (source control). `config.php`, `database.php` (credentials). `backup.zip`. `.env` (environment variables — often contains credentials). |

---

### Task 2.3 — Recursive Discovery

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Command** | `ffuf -u http://target.com/FUZZ -w wordlist.txt -recursion -recursion-depth 3 -mc 200,301`. |
| **What It Does** | When a directory is found, automatically starts a new fuzzing job on `found_dir/FUZZ`. Continues up to `--recursion-depth` levels. |
| **Warning** | Can generate enormous traffic. Use with a rate limit: `-rate 100`. |

---

### Task 2.4 — Custom 404 Handling

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Problem** | Server returns 200 for all requests (custom 404). Simple status code filtering doesn't work. |
| **Solution 1** | Filter by size: get the size of the custom 404 page → `ffuf ... -fs 1234`. |
| **Solution 2** | Filter by word/line count: `-fw 10` or `-fl 50`. |
| **Solution 3** | Filter by regex in response: `-fr "Page Not Found"` — filter out responses containing this string. |

---

### Task 2.5 — Rate Limiting

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Command** | `ffuf ... -rate 50` — maximum 50 requests/second. `-p 0.5` — 500ms delay between requests. |
| **When** | Rate limit when the target is rate-limiting your requests (getting 429s). When you need to be stealthy. When the server is slow and too many concurrent requests cause timeouts. |

---

# PHASE 3: FILTERING AND MATCHING

---

### Task 3.1 — Status Code Filtering

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Match** | `-mc 200` — only show 200s. `-mc all` — show everything. |
| **Filter** | `-fc 404,400` — hide 404 and 400 responses. |
| **Default** | ffuf default shows 200,204,301,302,307,401,403,405,500. Most useful set for discovery. |

---

### Task 3.2 — Size, Words, Lines Filtering

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Filter Size** | `-fs 0` — filter empty responses. `-fs 1234` — filter specific size. |
| **Match Size** | `-ms 500-1000` — only show responses in this size range. |
| **Words** | `-fw 3` — filter responses with exactly 3 words. `-mw 50-200` — match responses with 50–200 words. |
| **Calibrate** | `--calibrate` — ffuf auto-detects baseline and sets filters. Run before fuzzing on sites with unusual 404 behavior. |

---

### Task 3.3 — Regex Filtering

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Filter Response** | `-fr "Error 404|Not Found|doesn't exist"` — filter responses matching this regex. |
| **Match Response** | `-mr "admin|dashboard|login"` — only show responses containing these strings. Useful for finding admin panels: only show pages that mention "admin". |

---

### Task 3.4 — Autocalibration

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Command** | `ffuf -u http://target.com/FUZZ -w wordlist.txt --calibrate`. |
| **What It Does** | Sends a few test requests to non-existent paths → analyzes the response pattern → automatically sets filter thresholds. Reduces false positives on custom-error sites. |

---

# PHASE 4: ADVANCED FUZZING

---

### Task 4.1 — Virtual Host (vhost) Enumeration

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Concept** | Web servers host multiple domains on the same IP via the `Host` header. Different vhosts may have different attack surfaces (admin panel, staging, dev). |
| **Command** | `ffuf -u http://target_ip/ -H "Host: FUZZ.target.com" -w subdomains.txt -fs <normal_response_size>`. |
| **Wordlist** | `SecLists/Discovery/DNS/subdomains-top1million-5000.txt`. |
| **Filter** | The default response for an unknown vhost → note its size → `-fs <size>`. Responses with different sizes = valid vhosts. |

---

### Task 4.2 — GET Parameter Fuzzing

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Discover Parameters** | `ffuf -u "http://target.com/page?FUZZ=value" -w parameters.txt -mc 200`. |
| **Fuzz Values** | `ffuf -u "http://target.com/page?id=FUZZ" -w numbers.txt -mc 200 -fs <normal_size>`. |
| **Wordlists** | `SecLists/Discovery/Web-Content/burp-parameter-names.txt`. |

---

### Task 4.3 — POST Body Fuzzing

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Command** | `ffuf -u http://target.com/login -X POST -d "username=admin&password=FUZZ" -w rockyou.txt -mc 200,302 -H "Content-Type: application/x-www-form-urlencoded"`. |
| **JSON** | `ffuf -u http://target.com/api -X POST -d '{"key":"FUZZ"}' -H "Content-Type: application/json" -w wordlist.txt`. |

---

### Task 4.4 — Multiple Fuzzing Positions

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Two Positions** | `ffuf -u "http://target.com/W1/W2" -w usernames.txt:W1 -w paths.txt:W2`. Uses `W1` and `W2` as placeholder names with separate wordlists. |
| **Mode** | `-mode clusterbomb` — all combinations of W1 × W2. `-mode pitchfork` — W1[i] paired with W2[i] (parallel, same index). |
| **Use Case** | Test user/directory combinations: `http://target.com/users/W1/files/W2`. |

---

### Task 4.5 — Header Fuzzing

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Authorization Bypass** | `ffuf -u http://target.com/admin -H "X-Forwarded-For: FUZZ" -w ips.txt` — test if X-Forwarded-For bypass allows access. |
| **Custom Headers** | `ffuf -u http://target.com/ -H "FUZZ: admin" -w headers.txt` — fuzz header names. |

---

# PHASE 5: INTEGRATION

---

### Task 5.1 — ffuf + Burp Suite

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Proxy** | `ffuf ... -x http://127.0.0.1:8080` — route through Burp. See all requests in Burp history. Replay interesting responses in Burp Repeater. |
| **Output to Burp** | Identify interesting paths in ffuf → manually test in Burp Repeater for deeper analysis. |

---

### Task 5.2 — ffuf + Gobuster Comparison

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **ffuf** | More flexible (any position). Better filtering. Vhost fuzzing. Parameter fuzzing. Recommended for most web fuzzing tasks. |
| **Gobuster** | Simpler, slightly faster on basic directory busting. DNS subdomain mode. Good for quick directory discovery. |
| **Use Both** | Quick initial scan: Gobuster. Detailed, filtered, multi-position: ffuf. |

---

### Task 5.3 — Output Parsing

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **JSON Output** | `ffuf -o results.json -of json`. Parse: `cat results.json | python3 -c "import json,sys; [print(r['url']) for r in json.load(sys.stdin)['results']]"`. |
| **CSV** | `-of csv` — simpler format for spreadsheet analysis. |
| **HTML** | `-of html` — interactive report (open in browser). |

---

# PHASE 6: WORDLIST STRATEGY

---

### Task 6.1 — Wordlist Prioritization

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Order** | 1. `common.txt` (fast, ~5k) — quick check. 2. `directory-list-2.3-medium.txt` (220k) — standard. 3. `raft-large-directories.txt` (comprehensive). 4. Technology-specific wordlists (WordPress, Laravel, etc.). |
| **Tech-Specific** | `SecLists/Discovery/Web-Content/CMS/` — CMS-specific. Identify the tech stack first → use the right wordlist. |

---

### Task 6.2 — Custom Wordlist Generation

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **CeWL** | `cewl http://target.com -d 3 -m 5 -w custom.txt` — spiders the site and generates a wordlist from page content. Finds organization-specific words. |
| **Combine** | `cat common.txt custom.txt | sort -u > combined.txt`. |

---

### Task 6.3 — Reducing Wordlist Size

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Filter Existing** | If you already know the tech stack: `grep -i "wordpress\|wp-" directory-list-2.3-medium.txt > wp_paths.txt`. |
| **Remove Duplicates** | `sort -u wordlist.txt > deduped.txt`. |

---

# PHASE 7: PRACTICAL LABS

---

### Lab 7.1 — Directory Discovery on DVWA

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| **Scenario** | Run ffuf against DVWA. Find the admin panel, config files, and backup directories. Use medium wordlist + `.php,.bak` extensions. Filter 404s. Document all interesting finds. |
| **Success Criteria** | Admin panel found. At least one backup/config file found. All results documented. |

---

### Lab 7.2 — Vhost Discovery

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| **Scenario** | HTB machine or lab with multiple virtual hosts on one IP. Use ffuf vhost mode to discover all virtual hostnames. Add discovered vhosts to `/etc/hosts`. Access each discovered vhost. |
| **Success Criteria** | At least 2 vhosts discovered. Both accessible after adding to hosts file. |

---

### Lab 7.3 — Parameter Discovery

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| **Scenario** | Web application with hidden GET parameter that enables admin functionality. Use ffuf parameter fuzzing to discover the parameter. Exploit the discovered parameter. |
| **Success Criteria** | Hidden parameter discovered via ffuf. Functionality exploited. |

---

### Lab 7.4 — Full Attack Surface Mapping

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 60 min

| **Scenario** | HackTheBox or TryHackMe web machine. Use ffuf for: (1) directory discovery, (2) file discovery with extensions, (3) vhost enumeration if applicable. Document complete attack surface map. Identify the most interesting endpoint for further exploitation. |
| **Success Criteria** | Complete attack surface documented. Hidden endpoint that leads to further exploitation identified. |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — Bug Bounty Discovery

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 60 min

| **Scenario** | Run ffuf against a bug bounty target (within scope). Use multiple wordlists and extension sets. Filter intelligently. Document every interesting find. Identify at least one endpoint worthy of further investigation. |
| **Success Criteria** | Systematic discovery completed. At least one interesting endpoint identified. Methodology documented. |

---

### Challenge 8.2 — WAF-Evasive Fuzzing

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| **Scenario** | Target with WAF rate limiting. Configure ffuf rate limit, random delays, and rotating User-Agents to stay under WAF threshold. Complete directory discovery without triggering a block. |
| **Success Criteria** | Discovery completed. No WAF block triggered. Rate-limiting strategy documented. |

---

### Challenge 8.3 — API Endpoint Discovery

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| **Scenario** | REST API target. Use ffuf to discover: API endpoints (paths), API versions (`/api/v1/`, `/api/v2/`), hidden methods for discovered endpoints (HTTP method fuzzing). Combine with Postman for endpoint testing. |
| **Success Criteria** | API version map built. Hidden endpoints discovered. At least one undocumented endpoint found. |

---

# 📋 FINAL COMPETENCY MATRIX

| Competency | Self-Assessment |
|:---|:---:|
| Can run basic directory and file discovery with ffuf | ☐ |
| Can filter results effectively (size, code, regex) | ☐ |
| Can fuzz GET parameters, POST bodies, and headers | ☐ |
| Can enumerate virtual hosts with ffuf | ☐ |
| Can use multiple `FUZZ` positions with separate wordlists | ☐ |
| Can handle custom 404 pages and soft-404 responses | ☐ |
| Can use recursion and rate limiting appropriately | ☐ |
| Can select and prioritize wordlists for specific tech stacks | ☐ |
| Can proxy ffuf through Burp Suite | ☐ |
| Can parse and use ffuf JSON output programmatically | ☐ |

---

## 🎯 Interview Questions

1. What does the `FUZZ` keyword do in ffuf?
2. How do you handle a website that returns 200 for all non-existent paths?
3. How do you discover virtual hosts using ffuf?
4. What is the difference between `-mc` and `-fc` flags?
5. How do you fuzz multiple positions simultaneously with different wordlists?
6. How do you use `--calibrate` and when is it useful?
7. What wordlists would you use for WordPress-specific directory discovery?
8. How do you rate-limit ffuf to avoid triggering WAF blocks?
9. How do you discover hidden GET or POST parameters with ffuf?
10. What is the difference between ffuf's `clusterbomb` and `pitchfork` modes?
