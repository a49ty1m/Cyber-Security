# 🔭 Recon-ng: Complete Mastery Checklist

> **What is Recon-ng?** Recon-ng is a modular, Python-based OSINT framework with a Metasploit-inspired interface. It provides a structured workspace environment where you load modules — each targeting a specific data source or performing a specific OSINT task — and chain them together to build comprehensive intelligence profiles. It uses a relational database to store all collected intelligence and can export reports in multiple formats.
>
> **Why does it exist?** OSINT collection quickly becomes disorganized — dozens of tools, multiple output formats, no correlation between findings. Recon-ng solves this: it stores everything in a structured database (domains, hosts, contacts, credentials, ports, vulnerabilities), correlates findings across modules, and produces coherent reports. It's the OSINT equivalent of Metasploit for exploitation.
>
> **When to use it:** Comprehensive external OSINT engagements requiring structured data collection. When you need to chain multiple OSINT sources and correlate findings. When you need professional reports from OSINT data. Long-term intelligence gathering requiring persistent workspaces.
>
> **When to use theHarvester instead:** Quick, single-run OSINT for a specific domain. When you don't need a database or complex module chaining.
>
> **What mastering Recon-ng unlocks:** Structured, professional OSINT operations. Module-based intelligence collection from 50+ data sources. Correlated database of all OSINT findings. Professional report generation. The mindset for conducting thorough, systematic reconnaissance.

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals | 5 | 2–3 hours |
| 2 | Module System | 5 | 2–3 hours |
| 3 | Key Modules | 5 | 3–4 hours |
| 4 | API Keys | 3 | 1–2 hours |
| 5 | Reporting | 3 | 1–2 hours |
| 6 | Advanced | 3 | 2–3 hours |
| 7 | Practical Labs | 3 | 3–5 hours |
| 8 | Mastery Challenges | 2 | 2–3 hours |
| | **Total** | **29** | **~16–25 hours** |

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — Architecture

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Workspace** | Isolated working environment. Each engagement gets its own workspace. All data persists in the workspace database. Multiple workspaces for multiple engagements. |
| **Database** | SQLite database per workspace. Tables: `domains`, `hosts`, `contacts`, `credentials`, `ports`, `vulnerabilities`, `locations`, `companies`, `netblocks`. |
| **Modules** | Independent Python modules. Each does one specific OSINT task. Load, configure, and run. Results stored in database automatically. |
| **Marketplace** | Online repository of modules. `marketplace install module_name`. |

---

### Task 1.2 — Installation

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Kali** | `apt install recon-ng`. |
| **PIP** | `pip3 install recon-ng`. |
| **Git** | `git clone https://github.com/lanmaster53/recon-ng`. |
| **Run** | `recon-ng`. |

---

### Task 1.3 — Workspace Management

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Create** | `workspaces create target_company`. |
| **List** | `workspaces list`. |
| **Switch** | `workspaces load target_company`. |
| **Delete** | `workspaces remove target_company`. |

---

### Task 1.4 — Database Operations

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Show** | `show hosts` — all hosts. `show contacts` — all contacts/emails. `show domains` — all domains. `show ports`, `show credentials`, etc. |
| **Add Manually** | `db insert domains` → prompts for domain name. Seed the database before running modules. |
| **Query** | `db query SELECT * FROM hosts WHERE ip_address IS NOT NULL`. Direct SQL. |

---

### Task 1.5 — Seeding the Workspace

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **First Step** | Add the target domain to the database: `db insert domains` → `target.com`. This seeds the starting point for all domain-based modules. |
| **Add Company** | `db insert companies` → `Target Corporation`. For company-based searches. |
| **Add Netblock** | `db insert netblocks` → `192.168.1.0/24`. For IP-based searches. |

---

# PHASE 2: MODULE SYSTEM

---

### Task 2.1 — Module Discovery

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Marketplace** | `marketplace search` — list all available modules. `marketplace search domain` — filter by keyword. |
| **Categories** | `discovery/` — active discovery. `exploitation/` — rare, for specific scenarios. `import/` — import data from files. `recon/` — main OSINT collection (domains, contacts, hosts). `reporting/` — export data. |
| **Installed** | `modules search` — list installed modules. |

---

### Task 2.2 — Installing Modules

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Single** | `marketplace install recon/domains-hosts/hackertarget`. |
| **All** | `marketplace install all` — installs everything. Large download. |
| **Info** | `marketplace info recon/domains-hosts/hackertarget` — see module description, required API keys, and source/output tables. |

---

### Task 2.3 — Using a Module

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Load** | `modules load recon/domains-hosts/hackertarget`. |
| **Info** | `info` — show module description, required options, source, and output tables. |
| **Set Options** | `options set SOURCE target.com`. Or: if `SOURCE` is set to use DB: it auto-uses domains in the database. |
| **Run** | `run`. Results stored in database. |

---

### Task 2.4 — Module Chaining

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Concept** | Module A writes hosts to database → Module B reads hosts from database as its source → Module B writes ports to database → Module C reads ports. Fully automated pipeline. |
| **SOURCE** | Most modules accept `SOURCE` as the database table name: `options set SOURCE hosts`. Runs module against every entry in the hosts table. |
| **Power** | One command runs a module against all 200 hosts in the database — not just one. |

---

### Task 2.5 — Module Source Options

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Default** | Source = the relevant database table (e.g., `domains` for domain-based modules). |
| **Override** | `options set SOURCE specific.domain.com` — single target. |
| **File** | `options set SOURCE file:///path/to/domains.txt` — read from file. |

---

# PHASE 3: KEY MODULES

---

### Task 3.1 — Subdomain Discovery Modules

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **hackertarget** | `recon/domains-hosts/hackertarget` — DNS lookups via hackertarget.com. |
| **crt** | `recon/domains-hosts/certificate_transparency` — CT log lookup. |
| **bing_domain_web** | `recon/domains-hosts/bing_domain_web` — Bing search for subdomains. |
| **shodan_hostname** | `recon/domains-hosts/shodan_hostname` — Shodan API hostname search (requires key). |

---

### Task 3.2 — Email Harvesting Modules

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **hunter_io** | `recon/domains-contacts/hunter_io` — Hunter.io email discovery (requires API key). |
| **pgp_search** | `recon/domains-contacts/pgp_search` — PGP key server emails. |
| **whois_pocs** | `recon/domains-contacts/whois_pocs` — WHOIS point-of-contact emails. |
| **Output** | All emails go into the `contacts` table: name, email, title. |

---

### Task 3.3 — Host Enrichment Modules

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **resolve** | `recon/hosts-hosts/resolve` — resolves all hosts in database to IPs. Essential step before port scanning. |
| **reverse_resolve** | `recon/addresses-hosts/reverse_resolve` — reverse DNS for IP addresses. |
| **ipinfodb** | `recon/hosts-hosts/ipinfodb` — geolocation for discovered IPs. |
| **shodan_net** | `recon/netblocks-hosts/shodan_net` — Shodan scan of a netblock (requires key). |

---

### Task 3.4 — Vulnerability and Exposure Modules

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **github_miner** | `recon/companies-contacts/github_miner` — mine GitHub for employee emails from commits. |
| **xssposed** | `recon/hosts-vulnerabilities/xssposed` — check hosts against XSSposed database. |
| **pwnedlist** | `recon/contacts-credentials/pwnedlist` (requires key) — check emails against breach databases. |
| **hibp** | `recon/contacts-credentials/hibp` — Have I Been Pwned API for breach data. |

---

### Task 3.5 — Social Media Modules

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **twitter_search** | `recon/companies-contacts/twitter_search` — find Twitter accounts for a company. |
| **linkedin_auth** | LinkedIn modules require authentication (Recon-ng used to support this — check current availability). |
| **fullcontact** | `recon/contacts-contacts/fullcontact` — enrich contacts with social profiles (requires key). |

---

# PHASE 4: API KEYS

---

### Task 4.1 — API Key Management

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Store Key** | `keys add shodan_api YOUR_KEY_HERE`. |
| **List Keys** | `keys list` — see all stored keys and which modules require them. |
| **Remove** | `keys remove shodan_api`. |
| **Critical Keys** | Shodan (host intelligence). Hunter.io (email discovery). VirusTotal (threat intel). GitHub (code search). Censys (internet-wide scanning). |

---

### Task 4.2 — Free API Keys

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Shodan** | Free tier: limited searches. shodan.io → account → API key. |
| **Hunter.io** | Free tier: 25 requests/month. hunter.io → account → API key. |
| **VirusTotal** | Free tier: 500 requests/day. virustotal.com → profile → API key. |
| **Censys** | Free tier: limited searches. censys.io → account → API ID + secret. |

---

### Task 4.3 — Maximizing Free Tiers

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Strategy** | Run modules that don't need API keys first (crt.sh, hackertarget, pgp, bing). Then use API-based modules selectively on the most important targets. |
| **Multiple Accounts** | For practice: create multiple free accounts with different email addresses. |

---

# PHASE 5: REPORTING

---

### Task 5.1 — HTML Report

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Module** | `modules load reporting/html`. `options set FILENAME /path/to/report.html`. `options set CREATOR Your Name`. `options set CUSTOMER Target Corp`. `run`. |
| **Contents** | Professional HTML report with all database tables formatted: hosts, contacts, credentials, ports. |

---

### Task 5.2 — CSV Export

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Module** | `modules load reporting/csv`. `options set FILENAME /path/to/report.csv`. `run`. |
| **Use** | Import into Excel for filtering, sorting, deduplication. |

---

### Task 5.3 — JSON Export

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Module** | `modules load reporting/json`. Export for programmatic processing or import into other tools. |
| **Direct SQL** | `db query SELECT email FROM contacts` → pipe to file for direct use. |

---

# PHASE 6: ADVANCED

---

### Task 6.1 — Full Module Pipeline

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Pipeline** | `db insert domains target.com`. Load `certificate_transparency` → run → hosts found. Load `resolve` → run → IPs found. Load `hunter_io` → run → contacts found. Load `shodan_hostname` → run → port/service data. Load `reporting/html` → run → report. |

---

### Task 6.2 — Automating with Scripts

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Resource File** | Create a `.rc` file: one command per line. `recon-ng -r recon_script.rc`. Automates an entire recon workflow. |
| **Content** | `workspaces create target`. `db insert domains target.com`. `modules load recon/domains-hosts/certificate_transparency`. `run`. `modules load recon/hosts-hosts/resolve`. `run`. `modules load reporting/html`. `options set FILENAME /output/report.html`. `run`. |

---

### Task 6.3 — Cross-Module Correlation

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Query** | `db query SELECT contacts.email, hosts.host FROM contacts JOIN hosts ON ...` — join tables to correlate contacts with hosts. |
| **Value** | Find which emails correspond to which systems. Build targeted attack plans. |

---

# PHASE 7: PRACTICAL LABS

---

### Lab 7.1 — Full Recon-ng Workflow

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 45 min

| **Scenario** | Create a new workspace for a lab target. Seed with domain. Run 5 different modules (subdomain, contact, host enrichment). Generate HTML report. |
| **Success Criteria** | Report generated with data from all 5 modules. Database has entries in at least 4 tables. |

---

### Lab 7.2 — Scripted OSINT Pipeline

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| **Scenario** | Write a Recon-ng resource script that fully automates a reconnaissance workflow from domain seed to HTML report. Run it against a lab target. |
| **Success Criteria** | Single command runs entire recon pipeline. Report generated automatically. |

---

### Lab 7.3 — Compare with theHarvester

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| **Scenario** | Run both theHarvester and Recon-ng against the same target. Compare: which found more subdomains? Which found more emails? Which was faster? Which output is more useful? Document the comparison. |
| **Success Criteria** | Quantitative comparison documented. Recommendation on which to use in which scenario. |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — Comprehensive Intel Profile

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 60 min

| **Scenario** | Using Recon-ng (with API keys configured): build the most comprehensive intelligence profile possible for an authorized target. Use 10+ modules. Generate a professional report. Identify the top 3 attack vectors based on findings. |
| **Success Criteria** | 10+ modules used. Professional report generated. Top 3 attack vectors justified. |

---

### Challenge 8.2 — Custom Module

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 90 min

| **Scenario** | Write a custom Recon-ng module that queries a data source not already covered (e.g., a specific threat intelligence API, a regional WHOIS source). The module must read from one database table and write to another. |
| **Success Criteria** | Custom module installed and functional in Recon-ng. Writes data to appropriate database table. |

---

# 📋 FINAL COMPETENCY MATRIX

| Competency | Self-Assessment |
|:---|:---:|
| Can create and manage Recon-ng workspaces | ☐ |
| Can seed the database and install modules from the marketplace | ☐ |
| Can chain modules using database table sources | ☐ |
| Can discover subdomains, contacts, and host intel | ☐ |
| Can configure API keys for enhanced module coverage | ☐ |
| Can generate HTML, CSV, and JSON reports | ☐ |
| Can automate a full recon workflow with a resource script | ☐ |
| Understands when to use Recon-ng vs. theHarvester | ☐ |

---

## 🎯 Interview Questions

1. How does Recon-ng differ from theHarvester in terms of architecture?
2. What is a Recon-ng workspace and why is it important?
3. How does module chaining work in Recon-ng?
4. What is the SOURCE option in a Recon-ng module?
5. How do you configure API keys in Recon-ng?
6. What tables does Recon-ng maintain in its database?
7. How do you automate a full Recon-ng workflow with a resource script?
8. When would you use Recon-ng instead of running individual tools like theHarvester or Amass?
