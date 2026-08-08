# 🌾 theHarvester: Complete Mastery Checklist

> **What is theHarvester?** theHarvester is an OSINT tool that aggregates information about a target organization from multiple public sources — search engines, DNS servers, certificate transparency logs, PGP key servers, LinkedIn, Shodan, and more. It collects: email addresses, subdomains, IP addresses, employee names, and virtual hosts associated with a given domain.
>
> **Why does it exist?** The pre-attack reconnaissance phase requires gathering intelligence without directly touching the target. theHarvester automates passive data collection from dozens of sources simultaneously — giving you a structured list of emails (for phishing), subdomains (for additional attack surface), and IPs (for scanning) — all from public data with no direct target interaction.
>
> **When to use it:** At the start of every external engagement. Email address collection for social engineering or credential stuffing. Subdomain discovery before active scanning. Employee name discovery for targeted phishing or LinkedIn-based attacks.
>
> **When to use other tools additionally:** Amass and Subfinder for more comprehensive subdomain enumeration. Hunter.io and LinkedIn for deeper email/employee research. Shodan for detailed IP/service intelligence.
>
> **What mastering theHarvester unlocks:** Systematic passive OSINT collection. Email address discovery for phishing campaigns. Subdomain enumeration without touching the target. Full pre-attack intelligence profile construction.
>
> **Roadmap Phase:** Phase 1 (Reconnaissance — Passive OSINT)

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals | 4 | 1–2 hours |
| 2 | Data Sources | 5 | 2–3 hours |
| 3 | Emails | 3 | 1–2 hours |
| 4 | Subdomains | 3 | 1–2 hours |
| 5 | Integration | 3 | 1–2 hours |
| 6 | Reporting | 2 | 1 hour |
| 7 | Practical Labs | 3 | 2–4 hours |
| 8 | Mastery Challenges | 2 | 2–3 hours |
| | **Total** | **25** | **~11–19 hours** |

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — OSINT Philosophy

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Passive vs. Active** | Passive: collect from public data sources only — no direct contact with the target. Active: send queries to the target (DNS lookup, web crawling). theHarvester does both — but passive sources are preferred first. |
| **Why OSINT First** | Zero detection risk (you're just reading public data). Builds target profile before any scanning. Identifies attack vectors (phishing emails, subdomains, exposed services). |
| **Legal** | OSINT on public data is generally legal. Email addresses from corporate sites are public. Respect ToS of data sources. |

---

### Task 1.2 — Installation

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Kali** | Pre-installed. `theHarvester -h`. |
| **GitHub** | `git clone https://github.com/laramies/theHarvester; pip3 install -r requirements.txt`. |
| **API Keys** | `~/.theHarvester/api-keys.yaml` — add API keys for Shodan, Hunter.io, VirusTotal, GitHub, etc. More sources = more results. |

---

### Task 1.3 — Basic Syntax

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Command** | `theHarvester -d target.com -b all`. |
| **Flags** | `-d domain` — target domain. `-b source` — data source(s). `-l 500` — limit results per source (default 500). `-n` — DNS brute force. `-f report` — save HTML/XML report to file. |
| **Sources** | `-b all` — all available sources. `-b google,bing,crtsh` — specific sources. |

---

### Task 1.4 — Output Understanding

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Sections** | Emails found. Hosts found (subdomains and IPs). Virtual hosts. Shodan results (if key set). |
| **Format** | Text output to terminal. `-f filename` for HTML/XML. |
| **Deduplication** | Results from all sources merged and deduplicated. |

---

# PHASE 2: DATA SOURCES

---

### Task 2.1 — Search Engine Sources

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Google** | `-b google` — uses Google dorks. Limited by rate limiting. |
| **Bing** | `-b bing` — often finds different results than Google. Less rate limiting. |
| **Yahoo** | `-b yahoo`. |
| **DuckDuckGo** | `-b duckduckgo`. |
| **Baidu** | `-b baidu` — useful for targets with Chinese presence. |

---

### Task 2.2 — Certificate Transparency

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **crtsh** | `-b crtsh` — Certificate Transparency logs. Every SSL/TLS cert issued is logged publicly. Reveals subdomains that have had certs issued. Very reliable. |
| **certspotter** | `-b certspotter` — another CT log source. |
| **Value** | Finds subdomains that search engines haven't indexed — internal tools, staging servers, admin panels. Completely passive. |

---

### Task 2.3 — DNS Sources

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **DNS Brute Force** | `-n` flag — theHarvester actively bruteforces DNS subdomains. Not passive. |
| **hackertarget** | `-b hackertarget` — DNS lookup via hackertarget.com API. |
| **DNS Dumpster** | `-b dnsdumpster` — DNS records from dnsdumpster.com. |
| **Netcraft** | `-b netcraft` — Netcraft's web server survey. Subdomains and hosting info. |

---

### Task 2.4 — Intelligence Sources

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Shodan** | `-b shodan` (requires API key). Find open ports, banners, technologies on the target's IPs. |
| **VirusTotal** | `-b virustotal` (requires API key). Subdomains seen by VirusTotal. |
| **GitHub** | `-b github-code` (requires API key). Email addresses found in GitHub code. Useful for finding developer emails and leaked credentials. |
| **Hunter.io** | `-b hunter` (requires API key). Email addresses for the domain. |
| **LinkedIn** | `-b linkedin` — employee names from LinkedIn. |

---

### Task 2.5 — PGP and Email Sources

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **PGP** | `-b pgp` — PGP key server search. Users who have uploaded PGP keys often use their corporate email. |
| **EmailHarvester Format** | Emails found: `user@target.com`, `firstname.lastname@target.com`. Reveals naming convention (critical for targeted phishing). |

---

# PHASE 3: EMAILS

---

### Task 3.1 — Email Naming Convention Analysis

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Extract Convention** | Analyze discovered emails: `jsmith@target.com` → `firstname_lastname`. `john.smith@target.com` → `firstname.lastname`. `j.smith@target.com` → `f.lastname`. |
| **Generate More** | Once convention known: apply to known employee names (from LinkedIn, company site) to generate candidate email addresses for phishing or password spraying. |
| **Verify** | Use Hunter.io, Clearbit, or SMTP VRFY (if enabled) to verify generated addresses. |

---

### Task 3.2 — Email to Password Spraying

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Workflow** | Collect emails → extract usernames (part before @) → use as usernames for password spraying against OWA/O365/VPN. |
| **Tools** | `nxc smb target -u usernames.txt -p "Winter2024!"`. `spray` tool for O365. `MSOLSpray` for Microsoft 365. |

---

### Task 3.3 — Email to Phishing

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Target Selection** | IT staff emails (admin access). Finance staff (business email compromise). Executives (CEO fraud). |
| **Integration** | Email list → GoPhish campaign. Harvest → profile → craft believable lure → deploy. |

---

# PHASE 4: SUBDOMAINS

---

### Task 4.1 — Subdomain Collection

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Command** | `theHarvester -d target.com -b crtsh,google,bing,hackertarget,dnsdumpster -f subdomains`. |
| **Add to Hosts** | For HTB/lab: extract subdomains → add to `/etc/hosts` → visit each. |

---

### Task 4.2 — Subdomain to IP Mapping

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Resolve** | `for sub in subdomains.txt; do host $sub; done` — resolve each subdomain to IP. |
| **Find Interesting** | Subdomains resolving to internal IPs exposed externally. Subdomains resolving to non-production ranges (staging, dev). Subdomains with different hosting than main site. |

---

### Task 4.3 — Subdomain Takeover Check

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Concept** | Subdomain points to a third-party service (GitHub Pages, Heroku, etc.) that no longer exists → attacker claims the service → controls the subdomain. |
| **Check** | `subjack -w subdomains.txt -t 100 -o output.txt` — automated subdomain takeover check. |
| **Manual** | For each subdomain: does it resolve? What does it point to? Is the pointed-to resource claimable? |

---

# PHASE 5: INTEGRATION

---

### Task 5.1 — theHarvester + Amass

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Workflow** | theHarvester first (fast, multiple sources) → Amass for deeper passive enumeration → combine subdomain lists → deduplicate → resolve all → scan open ones. |
| **Combine** | `cat theharvester_subdomains.txt amass_subdomains.txt | sort -u > all_subdomains.txt`. |

---

### Task 5.2 — theHarvester + Shodan

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Workflow** | theHarvester finds IPs → feed to Shodan API → get open ports, banners, CVEs for each IP. `shodan host <ip>` for each discovered IP. |

---

### Task 5.3 — theHarvester + Nmap

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Workflow** | Collect subdomains/IPs → resolve → Nmap scan discovered IPs. `nmap -sV -iL resolved_ips.txt -oN nmap_results.txt`. |

---

# PHASE 6: REPORTING

---

### Task 6.1 — Generating Reports

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **HTML** | `theHarvester -d target.com -b all -f report` → creates `report.html` and `report.xml`. |
| **Review** | Open HTML in browser: formatted sections for emails, hosts, IPs, Shodan results. |

---

### Task 6.2 — Intelligence Profile Construction

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Build Profile** | Combine theHarvester results with LinkedIn (employee list), Shodan (exposed services), job postings (reveals tech stack), news articles (acquisitions, partnerships). |
| **Output** | Target profile document: org overview, key personnel, email convention, exposed subdomains, IP ranges, technologies, likely attack vectors. |

---

# PHASE 7: PRACTICAL LABS

---

### Lab 7.1 — Full OSINT Run on a Domain

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| **Scenario** | Run theHarvester against a practice target (a company with a public OSINT footprint — many CTF/OSINT challenges use real companies with consent). Use all available sources. Document: emails found, subdomains found, naming convention identified, IPs discovered. |
| **Success Criteria** | At least 5 emails discovered. Naming convention identified. At least 10 subdomains discovered. |

---

### Lab 7.2 — HTB/THM OSINT Machine

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 45 min

| **Scenario** | HTB/THM OSINT challenge: use theHarvester to collect intelligence about the target domain. Use discovered information (emails, subdomains) to gain access. |
| **Success Criteria** | Intelligence directly leads to access. Methodology documented. |

---

### Lab 7.3 — Build an Intelligence Profile

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| **Scenario** | Using an authorized target (lab environment or OSINT CTF): build a complete intelligence profile using theHarvester + Shodan + LinkedIn + crt.sh + Google dorks. Present as a professional red team pre-engagement report. |
| **Success Criteria** | Professional pre-engagement report. All categories populated. Attack vector recommendations included. |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — Maximum Email Discovery

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| **Scenario** | Given an authorized domain: maximize email discovery using theHarvester + Hunter.io + GitHub search + LinkedIn. Identify the complete naming convention. Generate 50+ candidate email addresses. Verify them. |
| **Success Criteria** | 50+ verified email addresses. Naming convention documented. |

---

### Challenge 8.2 — Full Pre-Attack Recon

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 60 min

| **Scenario** | External pentest lab: perform complete pre-attack passive reconnaissance. Build the intelligence profile. Identify the top 3 likely attack vectors. Justify each. Plan the next active phase (port scanning strategy, phishing targets, subdomain to attack first). |
| **Success Criteria** | Complete intel profile. Top 3 attack vectors with justification. Active phase plan ready. |

---

# 📋 FINAL COMPETENCY MATRIX

| Competency | Self-Assessment |
|:---|:---:|
| Can run theHarvester against all available sources | ☐ |
| Can analyze email results and identify naming conventions | ☐ |
| Can collect subdomains from CT logs and search engines | ☐ |
| Can integrate Shodan results for IP intelligence | ☐ |
| Can combine theHarvester with Amass and Nmap | ☐ |
| Can generate HTML/XML reports | ☐ |
| Can build a complete intelligence profile from theHarvester output | ☐ |
| Understands how discovered emails feed phishing and spraying | ☐ |

---

## 🎯 Interview Questions

1. What information does theHarvester collect and from where?
2. What is the difference between passive and active sources in theHarvester?
3. How does Certificate Transparency help subdomain discovery?
4. How do you determine an organization's email naming convention?
5. What do you do with discovered employee email addresses in a pentest?
6. How do you combine theHarvester with Shodan for deeper intelligence?
7. What is subdomain takeover and how do you identify candidates?
8. How do you build an intelligence profile from OSINT tools?
