# 🌐 Maltego: Complete Mastery Checklist

> **What is Maltego?** Maltego is a link analysis and data mining tool for OSINT and investigative work. It visually maps relationships between entities — people, organizations, domains, IPs, phone numbers, email addresses, social accounts — on an interactive graph canvas. It queries hundreds of data sources ("Transforms") to enrich entities and discover connections automatically. It is the industry standard for visual intelligence analysis.
>
> **Why does it exist?** OSINT data becomes complex quickly. Hundreds of entities with thousands of relationships can't be understood in a spreadsheet. Maltego's visual graph makes it immediately clear how entities connect — who is associated with what infrastructure, what accounts connect to what people, how organizations relate. It's the difference between data and intelligence.
>
> **When to use it:** Threat intelligence investigations. Understanding organized criminal infrastructure. Social engineering target profiling. Attribution research. Complex OSINT with many interconnected entities. Red team pre-engagement profiling.
>
> **When to use theHarvester/SpiderFoot:** For automated bulk collection. Maltego is better for interactive, analyst-driven investigation where visual relationships matter.
>
> **Roadmap Phase:** Phase 1 (Reconnaissance — Visual Link Analysis and OSINT Investigation)

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals | 4 | 1–2 hours |
| 2 | Interface | 4 | 2–3 hours |
| 3 | Transforms | 5 | 3–4 hours |
| 4 | Investigation | 4 | 3–5 hours |
| 5 | Advanced | 3 | 2–3 hours |
| 6 | Reporting | 2 | 1–2 hours |
| 7 | Practical Labs | 3 | 3–5 hours |
| 8 | Mastery Challenges | 2 | 2–3 hours |
| | **Total** | **27** | **~17–27 hours** |

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — Core Concepts

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Entity** | An object on the graph: Domain, Person, EmailAddress, IPAddress, Website, PhoneNumber, Organization, etc. |
| **Transform** | A query that takes one entity as input and produces related entities as output. `Domain → DNS MX Records` = run a Transform on a Domain entity → produces MailServerName entities. |
| **Graph** | Visual canvas showing entities (nodes) and their relationships (edges). Click entity → run transforms → graph expands. |
| **Machine** | Automated sequence of transforms. Run against an entity → multiple transforms run automatically. |

---

### Task 1.2 — Editions

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Community** | Free. Limited transforms per day. No commercial use. Sufficient for learning and lab work. |
| **Professional** | Paid (~$1500/year). Unlimited transforms. Commercial use. Premium data sources. |
| **Enterprise** | Team features. Shared graphs. Collaboration. |
| **Download** | `maltego.com` → Download → Register (email required). |

---

### Task 1.3 — Entity Types

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Infrastructure** | Domain, DNS Name, URL, IP Address, AS Number, Netblock, MX Record, NS Record. |
| **Personal** | Person, Email Address, Phone Number, Alias, Social Account, Photo. |
| **Organizations** | Organization, Company. |
| **Documents** | Document, Image, File. |
| **Locations** | Location, GPSCoordinate. |

---

### Task 1.4 — The Transform Hub

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Hub** | `maltego.com/transform-hub` — marketplace for Transform providers. |
| **Free** | Built-in Maltego transforms (DNS, WHOIS, etc.). Shodan Community. VirusTotal Community. |
| **Paid** | RiskIQ, Recorded Future, PassiveTotal, Full Contact, SpiderFoot HX. |
| **Install** | Transform Hub → install → transforms available in the app. |

---

# PHASE 2: INTERFACE

---

### Task 2.1 — Canvas and Navigation

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Canvas** | Central workspace. Drag entities. Scroll to zoom. |
| **Entity Palette** | Left sidebar: entity types. Drag onto canvas to create. |
| **Output Window** | Bottom: transform output log. |
| **Detail View** | Right panel: entity properties when selected. |
| **Layouts** | View → Layouts: Block, Bubble, Circular, Entity Weight layout. Use to organize complex graphs. |

---

### Task 2.2 — Adding Entities

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Drag** | Drag entity type from palette onto canvas. |
| **Properties** | Double-click → enter the entity value (e.g., `target.com` for a Domain entity). |
| **Paste** | Copy a list of entities → Paste in canvas → Maltego creates multiple entities. |

---

### Task 2.3 — Running Transforms

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Single Transform** | Right-click entity → Run Transform → select specific transform. |
| **All Transforms** | Right-click → Run All Transforms (runs every applicable transform). Generates many entities. |
| **Transform Set** | Predefined set of related transforms. Right-click → Run Transform → Transform Set. |

---

### Task 2.4 — Graph Management

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Delete** | Select entities → Delete. Remove low-value noise. |
| **Color** | Right-click → Color → categorize entities by type or risk level. |
| **Bookmark** | Right-click → Bookmark → mark important entities. |
| **Notes** | Right-click → Note → add analyst notes to entities. |
| **Focus** | Double-click a connection line → see the transform that created this relationship. |

---

# PHASE 3: TRANSFORMS

---

### Task 3.1 — Domain Transforms

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **DNS Lookup** | Domain → `To DNS Name [using resolving]` → discovers A, CNAME, MX, NS records. |
| **MX Records** | Domain → `To MX records` → mail servers. |
| **NS Records** | Domain → `To NS records` → name servers. |
| **WHOIS** | Domain → `To WHOIS [registrant email]` → registrant contact. |
| **CT Logs** | Domain → `To SSL Certificates [crt.sh]` → certificate transparency subdomains. |
| **Shodan** | Domain → `To Shodan Hostname` → open ports and banners (requires Shodan key). |

---

### Task 3.2 — IP Address Transforms

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Reverse DNS** | IP → `To DNS Name [Reverse lookup]` → hostname. |
| **ASN** | IP → `To AS Numbers [using common crawl]` → ASN. ASN → all IPs in that AS. |
| **Geolocation** | IP → `To Location [city]` → geolocation. |
| **Shodan** | IP → `To Shodan - IP Address` → open ports, banners, CVEs. |
| **Other Domains** | IP → `To Domains [sharing this IP]` → virtual hosting → reveals all domains on the same server. |

---

### Task 3.3 — Email Transforms

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Person** | Email → `To Person [Full Contact]` → real name, social profiles. |
| **Breach** | Email → `To Breaches [HIBP]` → which breaches this email appeared in. |
| **Social** | Email → `To Social Accounts` → Twitter, LinkedIn, GitHub linked accounts. |
| **Domain** | Email → `To Domain` → extract domain from email address. |

---

### Task 3.4 — Person Transforms

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Social** | Person → `To Social Networks [Twitter, LinkedIn]` → social profiles. |
| **Email** | Person → `To Email Addresses [Hunter.io]` → email addresses (requires key). |
| **Photo** | Person → `To Photo [LinkedIn]` → profile photo. |
| **Organization** | Person → `To Organization [LinkedIn]` → employer. |

---

### Task 3.5 — Machines

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Run Machine** | Select entity → Machines → select machine → run. |
| **Built-in** | `Company Stalker` — input person/company → discovers email, social, domain, infrastructure. `Twitter Digger` — input Twitter account → maps connections. `Find Wikipedia edits for emails` — unusual research. |
| **Custom** | Write custom machines in Maltego's machine editor (Maltego TRX framework). |

---

# PHASE 4: INVESTIGATION

---

### Task 4.1 — Domain Investigation Workflow

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Start** | Add Domain entity: `target.com`. |
| **Expand** | DNS, MX, NS, WHOIS, CT logs, Shodan → all in one run. |
| **IPs found** | Run IP transforms: reverse DNS, shared domains, ASN, geolocation, Shodan banners. |
| **Emails found** | Run email transforms: person lookup, breach check, social accounts. |
| **Graph** | Growing attack surface map — all relationships visible. |

---

### Task 4.2 — Person Profiling

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Target** | Start with name or email. |
| **Social** | Run all social account transforms → Twitter, LinkedIn, GitHub. |
| **Connections** | From Twitter: followers, following, mentions → map social network. |
| **Email** | From LinkedIn → email addresses. |
| **Breaches** | Check all found emails against HIBP. |

---

### Task 4.3 — Infrastructure Mapping

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Start** | Domain → IPs → ASN → netblock → other IPs in netblock → all domains on those IPs. |
| **Result** | Complete infrastructure map. All servers, shared hosting, related domains. |
| **Pivot** | Find domain registered by same email → pivot to new domain → find more infrastructure. |

---

### Task 4.4 — Threat Actor Attribution

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Concept** | Given C2 IP → find related domains → WHOIS registrant email → person entity → social profiles → real identity? |
| **Pivot Chain** | IP → domain → registrant → email → breach data → password reuse → other accounts → attribution. |
| **Careful** | Attribution is hard. Threat actors use bulletproof hosting, false WHOIS. Never make definitive attribution claims without high-confidence evidence. |

---

# PHASE 5: ADVANCED

---

### Task 5.1 — Custom Transforms

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **TRX Framework** | Write transforms in Python using Maltego TRX: `pip install maltego-trx`. |
| **Structure** | Input: entity type and value. Output: list of new entities with relationships. |
| **Deploy** | Run as local server → add to Maltego as custom transform. |

---

### Task 5.2 — Shodan Integration

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Shodan Hub** | Install Shodan transforms from Transform Hub. |
| **Enrich IPs** | IP → Shodan transforms → ports, services, banners, CVEs as entities on graph. |
| **Pivot** | CVE entity → show all other IPs with same CVE → attack surface visibility. |

---

### Task 5.3 — Graph Export for Report

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Export** | File → Export Graph → CSV/PDF/XMIND/GEXF. |
| **Screenshot** | Screenshot the graph for inclusion in reports. |
| **Report** | Maltego → Reports — built-in report generator (Professional edition). |

---

# PHASE 6: REPORTING

---

### Task 6.1 — Graph as Evidence

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Visual** | The graph IS the finding — export it as a visual. Shows the attack surface breadth and entity relationships at a glance. |
| **Annotate** | Color code: red = critical findings. Green = low risk. Add notes to key entities. |

---

### Task 6.2 — Entity List Export

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **CSV** | Export entity list → emails, IPs, domains in CSV. Use in other tools or reports. |
| **Filter** | Select entities by type → export filtered list. `All Email entities → export → email list for phishing targets`. |

---

# PHASE 7: PRACTICAL LABS

---

### Lab 7.1 — Domain Investigation

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| **Scenario** | Create Domain entity for an authorized target. Run all DNS, Shodan, CT log, and email transforms. Document the complete infrastructure discovered. |
| **Success Criteria** | Graph has 20+ entities. All entity types represented. Infrastructure map documented. |

---

### Lab 7.2 — Person Profiling (OSINT CTF)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 45 min

| **Scenario** | OSINT CTF challenge (TraceLabs, CTF events). Use Maltego to map a person's digital footprint. Find: email, social accounts, employer, location. |
| **Success Criteria** | Person profile complete. At least 3 social accounts found. Graph exported. |

---

### Lab 7.3 — Infrastructure Attribution

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| **Scenario** | Given a malicious IP (from a public threat intelligence feed): use Maltego to map its infrastructure. Find related domains, other IPs, hosting provider, WHOIS details. Build an attribution report. |
| **Success Criteria** | Full infrastructure mapped. Attribution report written with confidence assessment. |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — Full Red Team Intel Profile

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 90 min

| **Scenario** | Pre-engagement intelligence for an authorized red team target. Use Maltego to build a complete attack surface and personnel profile. Identify top phishing targets and exposed infrastructure. Export graph and findings. |
| **Success Criteria** | Professional pre-engagement report. Visual graph exported. Top 5 attack vectors identified. |

---

### Challenge 8.2 — Custom Transform

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 60 min

| **Scenario** | Write a custom Maltego transform using Python TRX that queries a data source not already in the Transform Hub. Deploy locally and use in an investigation. |
| **Success Criteria** | Custom transform functional. Successfully queries target data source. Creates correct output entities. |

---

# 📋 FINAL COMPETENCY MATRIX

| Competency | Self-Assessment |
|:---|:---:|
| Can add entities and run transforms in Maltego | ☐ |
| Can conduct a full domain investigation | ☐ |
| Can build a person's digital footprint profile | ☐ |
| Can use Shodan and HIBP transforms | ☐ |
| Can use the graph layout and annotation features | ☐ |
| Can export graphs and entity lists for reports | ☐ |
| Understands when to use Maltego vs. automated OSINT tools | ☐ |

---

## 🎯 Interview Questions

1. What is an entity and what is a Transform in Maltego?
2. How do you start a domain investigation in Maltego?
3. What transforms would you run on an email address?
4. How do you pivot from an IP address to other infrastructure?
5. What is a Maltego Machine and when do you use one?
6. How do you write a custom Transform?
7. When would you choose Maltego over SpiderFoot for OSINT?
