# 🌐 Amass: Complete Mastery Checklist

> **What is Amass?** Amass is the OWASP-backed open-source subdomain enumeration and external attack surface mapping tool. It combines passive DNS, certificate transparency logs, API sources (Shodan, Censys, VirusTotal, etc.), and active DNS brute-force into a single unified workflow — giving you the most complete external asset inventory available.
>
> **Why does it exist?** Organizations expose dozens or hundreds of subdomains they forget they own. Each forgotten subdomain is a potential attack surface — forgotten dev servers, unpatched legacy apps, exposed admin panels. Amass maps all of them systematically so nothing is missed.
>
> **When to use it:** During Phase 1 external reconnaissance on any bug bounty or external pentest engagement. Before active scanning — you need to know what exists before you can attack it. For continuous external attack surface monitoring.
>
> **When to avoid it:** Internal AD engagements (use BloodHound/Kerbrute instead). When you need speed over depth (use Subfinder for quick passive-only runs — see Section 9 comparison). When you don't have authorization to enumerate the target's DNS infrastructure.
>
> **What mastering Amass unlocks:** Complete external attack surface visibility. Bug bounty asset discovery that competitors miss. Subdomain takeover identification. API-enriched recon combining 30+ data sources. Readiness for OSCP, eCPPT, PNPT, and bug bounty programmes.
>
> **Roadmap Phase:** Phase 1 (Reconnaissance — External Asset Discovery)

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

| Recon & OSINT | Scanning | Web Attacks | Exploitation |
|:-------------|:---------|:-----------|:------------|
| [🌾 theHarvester](theHarvester.md) | [🗺️ Nmap](Nmap.md) | [🕷️ Burp Suite](Burp_Suite.md) | [💀 Metasploit](Metasploit_Framework.md) |
| [🔭 Recon-ng](Recon-ng.md) | [📂 Gobuster](Gobuster.md) | [💉 sqlmap](sqlmap.md) | [🔓 Hydra](Hydra.md) |
| **🌐 Amass** (you are here) | [🔍 Nikto](Nikto.md) | [🌀 ffuf](ffuf.md) | [🐍 Impacket](Impacket.md) |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals & DNS Recon Theory | 5 | 2–3 hours |
| 2 | Core Usage — Passive & Active Enumeration | 6 | 4–6 hours |
| 3 | Intermediate — API Keys & Data Sources | 5 | 4–5 hours |
| 4 | Advanced — Visualization, Intel & Tracking | 4 | 3–5 hours |
| 5 | Tool Integration & Automation | 4 | 2–3 hours |
| 6 | Practical Labs | 4 | 4–7 hours |
| 7 | Methodology & OPSEC | 3 | 2–3 hours |
| 8 | Mastery Challenges | 3 | 3–5 hours |
| | **Total** | **34** | **~24–37 hours** |

**Prerequisites:** DNS fundamentals (A, CNAME, NS, MX records). Understanding of certificate transparency. Basic Linux CLI.

**Alternatives & Comparison:**
- **Subfinder** (ProjectDiscovery) — passive-only, faster, cleaner output, excellent API integration. Use for quick passive runs.
- **theHarvester** — email + subdomain harvesting, simpler, fewer sources.
- **dnsx** — DNS resolution and validation of discovered subdomains.
- **Recon-ng** — broader OSINT framework, less DNS-focused.
- **Amass vs Subfinder:** Amass is deeper and supports active enumeration; Subfinder is faster for passive-only. Use both — pipe Subfinder output into Amass for validation.

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — Why Subdomain Enumeration Matters

- [ ] **Completed** · ⭐ Beginner · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand why subdomains are high-value recon targets and what attackers find there. |
| **Skills Learned** | Attack surface concept, why forgotten subdomains exist (abandoned projects, dev/staging environments, acquired companies), subdomain takeover (dangling DNS pointing to unclaimed cloud resources), what kinds of vulnerabilities are found on subdomains vs main domains. |
| **Practical Exercise** | Research 3 real subdomain takeover cases (GitHub Pages, AWS S3, Heroku). Understand the pattern: DNS CNAME points to a third-party service that no longer exists → anyone can claim it. |
| **Expected Output** | Written list of 5 attack categories enabled by subdomain enumeration: forgotten dev servers, old login portals, exposed APIs, subdomain takeover, out-of-scope-but-accessible admin panels. |

### Task 1.2 — DNS Enumeration Techniques Overview

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand the difference between passive DNS enumeration (no direct contact with target) and active DNS brute-force (sends queries that target can see). |
| **Skills Learned** | Passive sources: certificate transparency (crt.sh, Censys), DNS aggregators (VirusTotal, PassiveTotal), Shodan, Google/Bing dorks. Active methods: DNS brute-force (sending `mail.target.com?`, `dev.target.com?` etc), DNS zone transfer (`AXFR`). |
| **Practical Exercise** | Manual passive test: go to `crt.sh/?q=%.target.com` → look at all certificates issued for the target domain. Count how many subdomains are visible. This is one of Amass's passive sources. |
| **Expected Output** | Clear distinction between passive (no target contact, uses public data) and active (sends DNS queries toward target infrastructure). Understanding of when each is appropriate. |

### Task 1.3 — Certificate Transparency Logs

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand how TLS certificate issuance logs expose subdomains passively. |
| **Skills Learned** | Certificate Transparency (CT) log concept, `crt.sh` as a public CT log search engine, why every HTTPS subdomain appears in CT logs (browsers require logged certificates since 2018), using CT logs for recon before active scanning. |
| **Practical Exercise** | `curl -s "https://crt.sh/?q=%.hackerone.com&output=json" \| jq '.[].name_value' \| sort -u` — pipe crt.sh results for a bug bounty target. Count unique subdomains found passively with zero DNS queries to the target. |
| **Expected Output** | List of subdomains discovered via CT logs alone. Understanding that this produces zero target-side logs. |

### Task 1.4 — Installation & Configuration

- [ ] **Completed** · ⭐ Beginner · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Install Amass and set up the configuration file for API keys. |
| **Practical Exercise** | `sudo apt install amass` OR `go install -v github.com/owasp-amass/amass/v4/...@master`. Verify: `amass -version`. Create config dir: `mkdir -p ~/.config/amass/`. Copy example config: `amass enum --help` (find config path). `amass intel --help` and `amass enum --help` to understand subcommands. |
| **Expected Output** | Amass installed, version confirmed, config directory created. |

### Task 1.5 — Amass Subcommands Overview

- [ ] **Completed** · ⭐ Beginner · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand Amass's subcommand structure: `intel`, `enum`, `viz`, `track`, `db`. |
| **Skills Learned** | `intel` — discover root domains from ASN/CIDR/org. `enum` — enumerate subdomains of a known root domain. `viz` — visualize collected data. `track` — compare enumerations over time. `db` — manage the Amass graph database. |
| **Expected Output** | Table mapping each subcommand to its use case. Understanding that `enum` is the primary subcommand used 90% of the time. |

---

# PHASE 2: CORE USAGE

---

### Task 2.1 — Passive Subdomain Enumeration

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Run a passive-only enumeration that makes zero direct contact with the target's DNS infrastructure. |
| **Skills Learned** | `-passive` flag, understanding passive sources (CT logs, VirusTotal, Shodan, etc.), output flags (`-o`), JSON output (`-json`). |
| **Practical Exercise** | `amass enum -passive -d hackerone.com -o passive_subs.txt` (use a bug bounty target you have permission to enumerate). Review output. Count unique subdomains. Time the scan — passive runs finish in 2–10 minutes depending on API keys configured. |
| **Expected Output** | Text file of discovered subdomains from passive sources only. Zero DNS queries sent to target. |
| **Common Mistakes** | Running without `-passive` flag by default (Amass does active DNS resolution unless told not to). Not saving output with `-o` (results lost). Expecting instant results (passive sources have rate limits). |

### Task 2.2 — Active DNS Enumeration

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 45 min

| Field | Detail |
|:---|:---|
| **Objective** | Run a full active enumeration combining passive sources with DNS brute-force. |
| **Skills Learned** | Active mode (default), DNS brute-force with wordlists, resolver configuration (`-rf` for resolver file), rate limiting (`-max-dns-queries`). |
| **Practical Exercise** | `amass enum -d target.com -brute -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -o active_subs.txt`. Monitor output in real time. Compare results with passive run — active should find significantly more. |
| **Expected Output** | Larger subdomain list than passive run. New subdomains found via brute-force that CT logs didn't reveal. |
| **Common Mistakes** | Using a huge wordlist on a slow network (millions-entry wordlists take hours). Not specifying resolvers (Amass uses public resolvers by default — add a custom resolver file for speed). Running active without authorization (generates DNS query logs on target's DNS servers). |

### Task 2.3 — ASN & IP Range Discovery (amass intel)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Use `amass intel` to discover root domains belonging to a company from their ASN or IP ranges. |
| **Skills Learned** | ASN lookup, `-org` flag (search by company name), `-asn` flag (enumerate from ASN), `-cidr` flag (enumerate from IP range), why discovering root domains before subdomains is important for large organizations. |
| **Practical Exercise** | `amass intel -org "HackerOne"` → find their ASN → `amass intel -asn <ASN_number> -o root_domains.txt` → now enumerate each root domain: `amass enum -df root_domains.txt -passive`. |
| **Expected Output** | List of root domains owned by the target organization. Foundation for subdomain enumeration across all assets, not just the main domain. |

### Task 2.4 — Output Formats & Parsing

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Work with Amass output in different formats for downstream tool consumption. |
| **Skills Learned** | `-o` (plain text), `-json` (JSON with source metadata), `-oA` (all formats), parsing with `jq`, deduplication with `sort -u`, piping to `httpx` for HTTP probing. |
| **Practical Exercise** | `amass enum -passive -d target.com -json amass_out.json` → `jq '.name' amass_out.json \| sort -u > subs.txt` → `cat subs.txt \| httpx -silent -o live_subs.txt` → live subdomains ready for Nmap/Nuclei/Burp. |
| **Expected Output** | Pipeline: Amass → parsed subdomains → httpx-validated live hosts → ready for next tool. |

### Task 2.5 — DNS Zone Transfer Attempt

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Attempt DNS AXFR (zone transfer) against target nameservers — rare but reveals the entire zone when misconfigured. |
| **Practical Exercise** | `dig axfr @ns1.target.com target.com` — most production nameservers refuse this. Try against lab: set up BIND with zone transfers allowed → verify `dig axfr` returns all records. Amass automatically attempts zone transfers during active enumeration. |
| **Expected Output** | Understanding of zone transfer concept. Confirmation that modern nameservers reject AXFR by default. Note when it succeeds — it is a Critical finding. |

### Task 2.6 — Custom Resolvers for Speed & Reliability

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Provide Amass with a list of fast, reliable DNS resolvers to dramatically speed up active enumeration. |
| **Practical Exercise** | Download public resolver list: `wget https://raw.githubusercontent.com/trickest/resolvers/main/resolvers.txt`. `amass enum -d target.com -rf resolvers.txt -brute -w wordlist.txt`. Compare scan time with and without custom resolvers. |
| **Expected Output** | Significantly faster active enumeration. Understanding that default public resolvers (8.8.8.8, 1.1.1.1) rate-limit heavy DNS queries. |

---

# PHASE 3: API KEYS & DATA SOURCES

---

### Task 3.1 — Configuring API Keys

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | Configure API keys for Amass's data sources to unlock the full passive enumeration capability. |
| **Skills Learned** | Amass config file (`~/.config/amass/config.ini`), free API keys available from: Shodan (free tier), VirusTotal (free), SecurityTrails (free tier), Censys (free), URLScan.io (free), GitHub (free token), AlienVault OTX (free). |
| **Practical Exercise** | Create `~/.config/amass/config.ini` → add API keys for VirusTotal, SecurityTrails, URLScan, GitHub. Re-run passive enum and compare subdomain count before vs after API keys. The difference is dramatic — often 3–5x more subdomains. |
| **Expected Output** | Config file with at least 5 API sources configured. Documented increase in subdomain count after key configuration. |

### Task 3.2 — Understanding Amass Data Sources

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Know which data sources Amass queries and what each contributes. |
| **Practical Exercise** | `amass enum -list` → view all configured data sources. Categorize them: CT logs (Certspotter, crt.sh), passive DNS (SecurityTrails, CIRCL), search engines (Google, Bing, Yahoo), threat intel (VirusTotal, OTX), internet scanning (Shodan, Censys), code search (GitHub). |
| **Expected Output** | Source-category mapping table. Understanding that each source type finds different subdomains — all are needed for complete coverage. |

### Task 3.3 — Subfinder Integration and Comparison

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand when to use Subfinder vs Amass and how to combine them for maximum coverage. |
| **Skills Learned** | Subfinder installation (`go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest`), Subfinder passive-only workflow, combining results with `sort -u`, Subfinder speed advantage for quick passive runs. |
| **Practical Exercise** | Run both against the same target: `subfinder -d target.com -o sf_subs.txt` AND `amass enum -passive -d target.com -o amass_subs.txt`. Merge: `cat sf_subs.txt amass_subs.txt \| sort -u > all_subs.txt`. Compare unique counts — each finds subdomains the other misses. |
| **Expected Output** | Combined subdomain list from both tools. Typically 10–20% more unique subdomains from combining both vs either alone. |
| **Common Mistakes** | Thinking one tool is "better" — they query different sources. Always run both for maximum coverage on real engagements. |

### Task 3.4 — Shodan Integration

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Amass's Shodan integration to find subdomains from internet scan data. |
| **Practical Exercise** | Add Shodan API key to config. Run `amass enum -passive -d target.com`. Shodan-discovered hosts often include non-standard ports and IP-only services invisible to pure DNS enumeration. Cross-reference Amass results with direct `shodan search hostname:target.com`. |
| **Expected Output** | Subdomains discovered via Shodan's scan database. Understanding that Shodan finds hosts that don't advertise themselves via DNS. |

### Task 3.5 — GitHub Subdomain Enumeration

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Amass's GitHub source to find subdomains mentioned in public code repositories. |
| **Practical Exercise** | Add GitHub token to Amass config. Run passive enum and watch for GitHub-sourced subdomains in `-json` output (`"source":"GitHub"`). Separately search GitHub manually: `site:github.com "target.com" subdomain`. |
| **Expected Output** | Subdomains found in public GitHub repos — often internal/dev subdomains developers accidentally committed. |

---

# PHASE 4: ADVANCED — VISUALIZATION & TRACKING

---

### Task 4.1 — amass viz: Attack Surface Graph

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Generate a visual network graph of the discovered attack surface. |
| **Practical Exercise** | After enumeration, export to dot format: `amass viz -dot -d target.com -o graph.dot`. Render with Graphviz: `dot -Tpng graph.dot -o graph.png`. Alternatively use D3.js output: `amass viz -d3 -d target.com -o graph.html` — open in browser for interactive exploration. |
| **Expected Output** | Visual graph showing domain → subdomain → IP relationships. Useful for reports and for spotting anomalous connections. |

### Task 4.2 — amass track: Change Detection

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Run Amass periodically against a target and detect new subdomains that appear between scans. |
| **Practical Exercise** | Run first enum: `amass enum -d target.com`. Wait 24 hours. Run again. `amass track -d target.com` → shows new, removed, and changed subdomains between runs. New subdomains = newly deployed assets that may be less hardened. |
| **Expected Output** | Delta report showing new and removed subdomains. Understanding that continuous tracking is valuable for bug bounty and long-term red team engagements. |

### Task 4.3 — amass db: Database Queries

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Query the Amass local graph database to extract data from previous enumeration runs. |
| **Practical Exercise** | `amass db -names -d target.com` (list all subdomains). `amass db -show -d target.com` (show full asset details). `amass db -summary -d target.com` (stats on the collected dataset). Useful for re-querying without re-running scans. |
| **Expected Output** | Ability to query historical Amass data without re-running enumeration. |

### Task 4.4 — Subdomain Takeover Identification

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| Field | Detail |
|:---|:---|
| **Objective** | Identify dangling CNAME records pointing to unclaimed third-party services — subdomain takeover candidates. |
| **Skills Learned** | Subdomain takeover concept, `can-i-take-over-xyz` GitHub reference list, using `subjack` or `nuclei -t subdomain-takeover/` against Amass results. |
| **Practical Exercise** | `amass enum -passive -d target.com -o subs.txt` → `cat subs.txt \| httpx -silent -o live.txt` → `nuclei -l live.txt -t nuclei-templates/takeovers/ -o takeovers.txt`. Review results for CNAME targets like `amazonaws.com`, `github.io`, `heroku.com`, `azurewebsites.net`. |
| **Expected Output** | List of potential subdomain takeover candidates. For any confirmed: document the dangling CNAME, the unclaimed service, and the steps to verify. |

---

# PHASE 5: TOOL INTEGRATION

---

### Task 5.1 — Amass → Nmap Pipeline

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 25 min
| Field | Detail |
|:---|:---|
| **Objective** | Feed Amass-discovered subdomains into Nmap for port scanning. |
| **Practical Exercise** | `amass enum -passive -d target.com -o subs.txt` → `nmap -iL subs.txt -p 80,443,8080,8443 --open -oN web_ports.txt`. Pipe resolved IPs: `amass enum -passive -d target.com -ip -o subs_ips.txt \| awk '{print $2}' > ips.txt \| nmap -iL ips.txt`. |

### Task 5.2 — Amass → Nuclei Pipeline

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min
| Field | Detail |
|:---|:---|
| **Objective** | Chain Amass subdomain discovery into Nuclei for automated vulnerability scanning across the full attack surface. |
| **Practical Exercise** | `amass enum -passive -d target.com -o subs.txt` → `cat subs.txt \| httpx -silent \| nuclei -t ~/nuclei-templates/ -severity critical,high -o vulns.txt`. |

### Task 5.3 — Amass + Subfinder Deduplication

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min
| Field | Detail |
|:---|:---|
| **Objective** | Combine Amass and Subfinder outputs into a single deduplicated master list. |
| **Practical Exercise** | `cat amass_out.txt subfinder_out.txt \| sort -u \| anew master_subs.txt` (using `anew` for append-new-only deduplication). |

### Task 5.4 — theHarvester → Amass → Recon-ng Full OSINT Chain

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 35 min
| Field | Detail |
|:---|:---|
| **Objective** | Build a full Phase 1 recon chain using all three OSINT tools together. |
| **Practical Exercise** | `theHarvester` → emails/names/domains → `amass enum` → all subdomains → `recon-ng` → enrich with WHOIS/contacts/breaches → comprehensive target profile. |

---

# PHASE 6: PRACTICAL LABS

---

### Lab 6.1 — HackerOne Bug Bounty: Full Subdomain Recon

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 3–4 hours
| Field | Detail |
|:---|:---|
| **Scenario** | Pick a HackerOne program with a broad scope (`*.target.com`). Run full Amass passive + active enumeration. Combine with Subfinder. Validate live hosts with httpx. |
| **Success Criteria** | 50+ unique live subdomains discovered. At least one subdomain not on the main site. Full asset inventory documented. |

### Lab 6.2 — OSCP External Recon Simulation

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 2–3 hours
| Field | Detail |
|:---|:---|
| **Scenario** | Simulate OSCP-style external recon: given a company domain, enumerate all subdomains, map IPs, identify interesting services. |
| **Success Criteria** | Complete subdomain list with IP mappings. HTTP/HTTPS services identified. Interesting targets (login portals, API endpoints, dev servers) highlighted. |

### Lab 6.3 — Subdomain Takeover Hunt

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 2–3 hours
| Field | Detail |
|:---|:---|
| **Scenario** | Run Amass against a bug bounty target. Check all CNAME records. Identify dangling CNAMEs pointing to unclaimed services. Verify with Nuclei takeover templates. |
| **Success Criteria** | At least one potential takeover candidate identified. Verified by checking if the third-party service can be claimed. |

### Lab 6.4 — Continuous Monitoring Setup

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 2 hours
| Field | Detail |
|:---|:---|
| **Scenario** | Set up a cron job that runs Amass daily against a target domain and alerts on new subdomains. |
| **Success Criteria** | Cron job running. `amass track` detects new subdomains between runs. Alert (email or Slack webhook) fires on new subdomain discovery. |

---

# PHASE 7: METHODOLOGY & OPSEC

---

### Task 7.1 — External Recon Methodology

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min
| Field | Detail |
|:---|:---|
| **Objective** | Position Amass in the full external recon methodology. |
| **Expected Output** | Methodology flowchart: `amass intel` (root domains) → `amass enum -passive` (subdomains, no noise) → `amass enum -active` (full brute-force, authorized) → `httpx` (live hosts) → `Nmap`/`Nuclei` (services/vulns). |

### Task 7.2 — OPSEC: Passive vs Active Trade-offs

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min
| Field | Detail |
|:---|:---|
| **Objective** | Understand the detection and legal trade-offs of passive vs active enumeration. |
| **Skills Learned** | Passive = zero target-side logs (reads from public data sources only). Active = DNS queries appear in target's DNS server logs and can trigger IDS. For black-box external pentests: always start passive. For authorized tests: active is fine. For bug bounty: passive unless scope explicitly allows active. |

### Task 7.3 — Scope Management

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min
| Field | Detail |
|:---|:---|
| **Objective** | Stay within authorized scope when enumerating multi-domain organizations. |
| **Practical Exercise** | Use `-df domains.txt` to enumerate multiple root domains at once while staying in scope. Use `-exclude` to skip out-of-scope subdomains. Always verify with the scope document before active enumeration. |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — 500+ Subdomain Recon

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 3–4 hours
Pick a large company's bug bounty program. Configure all available free API keys. Run full passive + active Amass enumeration. Combine with Subfinder. Target: 500+ unique live subdomains documented with services identified.

### Challenge 8.2 — Full Recon-to-Vuln Pipeline

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 4–6 hours
Amass → Subfinder → httpx → Nuclei. Automate the entire pipeline in a bash script. Output: live subdomain list, HTTP response codes, technology fingerprints, vulnerability scan results. All in one automated run.

### Challenge 8.3 — Takeover Submission

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ Variable
Find and responsibly disclose a real subdomain takeover vulnerability via a bug bounty program using Amass. Document the full methodology for your portfolio.

---

## 🎓 Competency Matrix

| Skill | Beginner | Intermediate | Advanced |
|:------|:--------:|:------------:|:--------:|
| Passive subdomain enumeration | [ ] | | |
| Active DNS brute-force | | [ ] | |
| ASN/CIDR root domain discovery | | [ ] | |
| API key configuration (5+ sources) | | [ ] | |
| Subfinder + Amass combined pipeline | | [ ] | |
| httpx validation of discovered subdomains | [ ] | | |
| Subdomain takeover identification | | | [ ] |
| Amass track for change detection | | [ ] | |
| Full automated recon pipeline | | | [ ] |
| Bug bounty recon methodology | | | [ ] |

---

## 💬 Interview Questions

1. What is the difference between passive and active subdomain enumeration?
2. How do certificate transparency logs reveal subdomains without querying the target?
3. Why should you run both Amass and Subfinder rather than just one?
4. What is a subdomain takeover and what DNS record configuration enables it?
5. What is `amass intel` used for and how does it differ from `amass enum`?
6. Why does adding API keys dramatically increase Amass's subdomain discovery count?
7. What is a DNS zone transfer (AXFR) and why is it a critical finding when it succeeds?
8. How would you set up continuous subdomain monitoring for a bug bounty target?
9. Describe a full Phase 1 recon pipeline from domain name to live subdomain list.
10. What OPSEC considerations apply when running active Amass enumeration on a bug bounty target?
