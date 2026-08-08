# 🕷️ SpiderFoot: Complete Mastery Checklist

> **What is SpiderFoot?** SpiderFoot is an automated OSINT collection platform with 200+ modules that query hundreds of data sources simultaneously — search engines, DNS records, WHOIS, threat intelligence feeds, dark web mentions, Shodan, HaveIBeenPwned, LinkedIn, GitHub, and more. It builds a graph of relationships between discovered entities (domains, IPs, emails, persons, phone numbers, certificates). It has a web UI for interactive use and CLI for automation.
>
> **Why does it exist?** Running 200+ individual OSINT queries manually is impractical. SpiderFoot automates this collection, correlates findings, and presents them as an interconnected graph — revealing relationships that individual tool runs miss. It is particularly powerful for building comprehensive external intelligence profiles.
>
> **When to use it:** Comprehensive external OSINT for an engagement. Threat intelligence and attack surface management. When you need breadth over depth — SpiderFoot is wide but individual modules go less deep than dedicated tools. Brand and exposure monitoring.
>
> **When to use theHarvester or Recon-ng:** For specific, targeted queries. When you need module-level control and structured database output. SpiderFoot for comprehensive automated coverage; Recon-ng for controlled, structured pipelines.
>
> **Roadmap Phase:** Phase 1 (Reconnaissance — Automated OSINT Collection)

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals | 4 | 1–2 hours |
| 2 | Web UI | 4 | 2–3 hours |
| 3 | Core Modules | 4 | 2–3 hours |
| 4 | API Keys | 3 | 1–2 hours |
| 5 | Analysis | 3 | 2–3 hours |
| 6 | CLI and Automation | 3 | 1–2 hours |
| 7 | Practical Labs | 3 | 3–5 hours |
| 8 | Mastery Challenges | 2 | 2–3 hours |
| | **Total** | **26** | **~14–23 hours** |

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — SpiderFoot Architecture

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Scan** | Each investigation is a "scan" with a target (domain, IP, email, person, etc.) and a set of modules to run. |
| **Modules** | 200+ modules, each querying a specific data source or performing analysis. Modules generate "events" (findings). |
| **Events** | Typed findings: DOMAIN_NAME, IP_ADDRESS, EMAILADDR, USERNAME, PHONE_NUMBER, VULNERABILITY_CVE, DARKNET_MENTION, etc. |
| **Graph** | SpiderFoot links events — a domain → IP → ASN → other domains on same ASN. Relationship graph. |

---

### Task 1.2 — Installation

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **GitHub** | `git clone https://github.com/smicallef/spiderfoot`. `pip3 install -r requirements.txt`. `python3 sf.py -l 127.0.0.1:5001`. |
| **Docker** | `docker pull smicallef/spiderfoot`. `docker run -p 5001:5001 smicallef/spiderfoot`. |
| **Kali** | `apt install spiderfoot` or manual install. |
| **Web UI** | Navigate to `http://127.0.0.1:5001`. |

---

### Task 1.3 — Scan Types

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Domain** | Start with a domain → discovers subdomains, emails, IPs, certificates, mentions. |
| **IP Address** | Start with IP → discovers hostnames, ASN, geolocation, open ports, CVEs. |
| **Email** | Start with email → breaches, social profiles, associated domains. |
| **Person** | Start with a name → social profiles, LinkedIn, mentions. |
| **Phone** | Start with phone number → carrier, geolocation, mentions. |

---

### Task 1.4 — SpiderFoot HX (Cloud)

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **HX** | `spiderfoot.net` — hosted version. More modules, dark web access, better performance. Freemium. |
| **Self-hosted** | Full control. No data sent to third party. Limited by your API keys and bandwidth. |

---

# PHASE 2: WEB UI

---

### Task 2.1 — Creating a Scan

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **New Scan** | Web UI → New Scan → Enter target name → Select scan type. |
| **Module Selection** | Choose: "All" (comprehensive), "Footprint" (domain/IP surface), "Investigate" (deep dig), "Passive" (no active queries), "OSINT" (open source only). Or custom: manually select modules. |
| **Start** | Click Run. Modules execute in parallel. Results stream in real time. |

---

### Task 2.2 — Reviewing Results

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Browse** | Scan → Browse → Event type filter. Filter by: IP_ADDRESS, EMAILADDR, VULNERABILITY, DARKNET_MENTION, etc. |
| **Graph** | Scan → Graph → visual relationship map. Entities as nodes, relationships as edges. |
| **Status** | High interest: VULNERABILITY_CVE, DARKNET_MENTION, CREDENTIAL_BREACH, PHONE_NUMBER, EMAILADDR. |

---

### Task 2.3 — Filtering by Event Type

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Key Events** | `VULNERABILITY_CVE` — CVEs found for discovered services. `CREDENTIAL_BREACH` — emails found in breach databases. `DARKNET_MENTION` — target mentioned on dark web. `LINKED_URL_INTERNAL` — internal URL exposure. `INTERNET_NAME` — discovered hostnames. `EMAILADDR` — email addresses. |
| **Filter** | Event Type dropdown in Browse view. Focus on high-value event types first. |

---

### Task 2.4 — Exporting Results

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Export** | Scan → Download → CSV or JSON. Filter by event type before downloading for focused exports. |
| **GEXF** | Graph format for Gephi visualization. Large relationship maps. |

---

# PHASE 3: CORE MODULES

---

### Task 3.1 — DNS and Certificate Modules

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **sfp_dnsresolve** | Resolves discovered hostnames to IPs. |
| **sfp_crt** | Certificate transparency log queries. Subdomain discovery. |
| **sfp_dnsdumpster** | DNSDumpster API for DNS records. |
| **sfp_hackertarget** | Hackertarget API for subdomains. |

---

### Task 3.2 — Threat Intel Modules

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **sfp_shodan** | Shodan host lookup for discovered IPs (requires API key). |
| **sfp_virustotal** | VirusTotal for domain/IP reputation (requires API key). |
| **sfp_alienvault** | AlienVault OTX threat intelligence. |
| **sfp_threatcrowd** | ThreatCrowd data for IPs and domains. |

---

### Task 3.3 — Breach and Credential Modules

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **sfp_haveibeenpwned** | HIBP API — check emails against breach databases (requires API key). |
| **sfp_leakix** | LeakIX for exposed/vulnerable services. |
| **sfp_dehashed** | DeHashed breach database (requires paid key for full access). |

---

### Task 3.4 — Social and Code Modules

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **sfp_github** | GitHub code search — find mentions of the target in code (requires API key). |
| **sfp_linkedin** | LinkedIn discovery (limited without official API). |
| **sfp_hunter** | Hunter.io email discovery (requires API key). |

---

# PHASE 4: API KEYS

---

### Task 4.1 — Setting API Keys

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Web UI** | Settings → Global Options → enter API keys for each service. |
| **Key Services** | Shodan, VirusTotal, Hunter.io, HIBP, GitHub, Censys, PassiveTotal, SecurityTrails. |

---

### Task 4.2 — Priority API Keys

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Free Keys** | Shodan (limited free). VirusTotal (500/day free). GitHub (5000/hour with account). HIBP (free for email check). |
| **High-value** | Shodan + VirusTotal + HIBP cover the most important threat intel categories. Prioritize these. |

---

### Task 4.3 — Passive-Only Scan

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Passive** | Select "Passive" scan type → only queries third-party databases, no direct target contact. Zero detection risk. |
| **Use Case** | Pre-engagement intelligence when you cannot afford any target interaction. |

---

# PHASE 5: ANALYSIS

---

### Task 5.1 — Graph Analysis

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Graph View** | Visualize entity relationships. Clusters of related infrastructure. Shared hosting relationships. |
| **Pivot** | Domain → IP → other domains on same IP → expand attack surface. |
| **Connected Targets** | Domains sharing ASN, certificates, or IP ranges = likely same organization → broader scope. |

---

### Task 5.2 — Vulnerability Analysis

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **CVE Events** | SpiderFoot correlates service banners (from Shodan) with known CVEs → surfaces vulnerable exposed services. |
| **Action** | Validate each CVE finding manually. Shodan banners can be outdated. Verify the actual version before attempting exploitation. |

---

### Task 5.3 — Dark Web Monitoring

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Modules** | Dark web modules require Tor connectivity or dedicated dark web data services. |
| **Value** | Find mentions of the target organization on dark web forums, paste sites, data leak sites. Credential databases. |
| **HX** | SpiderFoot HX has better dark web coverage than self-hosted. |

---

# PHASE 6: CLI AND AUTOMATION

---

### Task 6.1 — CLI Mode

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Command** | `python3 sf.py -s target.com -t DOMAIN_NAME -m sfp_crt,sfp_hackertarget,sfp_dnsresolve -o csv -q`. |
| **Flags** | `-s target` — scan target. `-t type` — target type. `-m modules` — comma-separated modules. `-o format` — output format (csv, json, tab). `-q` — quiet (no progress). |

---

### Task 6.2 — Scan Templates

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Save** | Save a module selection as a template. Reuse for similar engagements. |
| **Quick** | "Footprint" preset = standard module set for domain attack surface. |

---

### Task 6.3 — Correlation with Other Tools

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Export → Nmap** | Export all discovered IPs → feed to Nmap for port scanning. |
| **Export → ffuf** | Export all discovered subdomains → feed to ffuf or Gobuster for web fuzzing. |
| **Export → nxc** | Discovered network ranges → nxc smb for authentication testing. |

---

# PHASE 7: PRACTICAL LABS

---

### Lab 7.1 — Full Domain OSINT

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| **Scenario** | Run a "Footprint" scan against a lab domain (or an authorized target). Review all event types. Export emails (EMAILADDR), subdomains (INTERNET_NAME), and IPs (IP_ADDRESS). |
| **Success Criteria** | All three data types exported. Graph reviewed. Top 3 findings identified. |

---

### Lab 7.2 — Threat Intel Analysis

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| **Scenario** | With Shodan and VirusTotal API keys configured: run a scan against an authorized domain. Review VULNERABILITY_CVE and CREDENTIAL_BREACH events. Verify findings manually. |
| **Success Criteria** | CVE events reviewed. At least 1 verified against actual service version. Breach data found for at least 1 email. |

---

### Lab 7.3 — Passive External Recon

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| **Scenario** | Passive-only SpiderFoot scan against a target before active engagement. No direct target contact. Build initial intelligence profile. Document findings in a structured report. |
| **Success Criteria** | Complete passive scan. Intelligence profile written. Attack surface map built. |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — Compare All OSINT Tools

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 60 min

| **Scenario** | Run SpiderFoot, theHarvester, and Recon-ng against the same target. Compare: unique findings per tool, time taken, depth vs. breadth. Write a recommendation on when to use each. |
| **Success Criteria** | Quantitative comparison. Clear recommendation document. |

---

### Challenge 8.2 — Full Pre-Engagement Report

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 60 min

| **Scenario** | Using SpiderFoot as the primary tool: build a complete pre-engagement intelligence report for an authorized target. Include: subdomains, IPs, emails, vulnerabilities, breach exposure, social mentions. |
| **Success Criteria** | Professional report. All major categories covered. |

---

# 📋 FINAL COMPETENCY MATRIX

| Competency | Self-Assessment |
|:---|:---:|
| Can run a SpiderFoot scan and review results by event type | ☐ |
| Can select appropriate modules for a scan | ☐ |
| Can configure API keys for enhanced coverage | ☐ |
| Can use the graph view to analyze relationships | ☐ |
| Can export findings and feed them to other tools | ☐ |
| Can run SpiderFoot via CLI | ☐ |
| Understands SpiderFoot vs. theHarvester vs. Recon-ng | ☐ |

---

## 🎯 Interview Questions

1. What makes SpiderFoot different from theHarvester or Recon-ng?
2. What is the difference between a passive and active SpiderFoot scan?
3. What event types are highest priority in a SpiderFoot scan?
4. How does SpiderFoot correlate findings across modules?
5. What API keys provide the most value in SpiderFoot?
6. How do you use SpiderFoot output in a downstream tool like Nmap?
