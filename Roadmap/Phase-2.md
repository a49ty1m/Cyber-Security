# Phase 2: Offensive Core

---

### 🧭 Navigation
◀ [Phase 1](Phase-1.md) | 🏠 [Master Roadmap](README.md) | [Phase 3](Phase-3.md) ➔

---

> [!NOTE]
> **Phase Overview**
> - **⏱️ Time Commitment (Full-Time):** 4–6 months
> - **⏱️ Time Commitment (Part-Time):** 8–12 months
> - **🎯 Primary Focus:** Footprinting, scanning, enumeration, system hacking, malware design, sniffing/spoofing, social engineering, denial-of-service, session hijacking, and password cracking. The complete offensive lifecycle from recon to impact.

---

### 🗂️ Table of Contents
- [Part 4: Footprinting and Reconnaissance](#part-4-footprinting-and-reconnaissance)
  - [Stage 1: The "Ghost" Phase (Passive OSINT & Human Profiling)](#stage-1-the-ghost-phase-passive-osint-human-profiling)
  - [Stage 2: Semi-Passive Infrastructure Mapping](#stage-2-semi-passive-infrastructure-mapping)
  - [Stage 3: Active Footprinting & Network Interrogation](#stage-3-active-footprinting-network-interrogation)
  - [Stage 4: Advanced Fingerprinting & Logic Analysis](#stage-4-advanced-fingerprinting-logic-analysis)
  - [Stage 5: IPv6 & Protocol Enumeration](#stage-5-ipv6-protocol-enumeration)
  - [Stage 6: Dark Web & Breach Intelligence](#stage-6-dark-web-breach-intelligence)
  - [Stage 7: Satellite & Geospatial Intelligence](#stage-7-satellite-geospatial-intelligence)
  - [Stage 8: Strategy & Attack Mapping](#stage-8-strategy-attack-mapping)
  - [Lab Progression](#lab-progression)
- [Part 5: Scanning](#part-5-scanning)
  - [Stage 1: Host Discovery & Network Topology (The "Roll Call")](#stage-1-host-discovery-network-topology-the-roll-call)
  - [Stage 2: Port, Service & Protocol Enumeration (The "Door Check")](#stage-2-port-service-protocol-enumeration-the-door-check)
  - [Stage 3: Defense & Configuration Assessment (The "Armor Check")](#stage-3-defense-configuration-assessment-the-armor-check)
  - [Stage 4: Vulnerability Association & Attack Mapping](#stage-4-vulnerability-association-attack-mapping)
  - [Stage 5: Stealth & Evasion Techniques](#stage-5-stealth-evasion-techniques)
  - [Stage 6: Advanced Scanning Techniques](#stage-6-advanced-scanning-techniques)
  - [Lab Progression](#lab-progression)
- [Part 6: Enumeration](#part-6-enumeration)
  - [Stage 1: Service Enumeration & Banner Grabbing](#stage-1-service-enumeration-banner-grabbing)
  - [Stage 2: Directory & Identity Enumeration](#stage-2-directory-identity-enumeration)
  - [Stage 3: DNS & Infrastructure Enumeration](#stage-3-dns-infrastructure-enumeration)
  - [Stage 4: Database & Application Enumeration](#stage-4-database-application-enumeration)
  - [Stage 5: Attack Surface Consolidation & Enumeration OpSec](#stage-5-attack-surface-consolidation-enumeration-opsec)
  - [Lab Progression](#lab-progression)
- [Part 7: System Hacking & Initial Compromise](#part-7-system-hacking-initial-compromise)
  - [Stage 1: The Breach (Initial Access & Exploitation)](#stage-1-the-breach-initial-access-exploitation)
  - [Stage 2: The Ascension (Privilege Escalation)](#stage-2-the-ascension-privilege-escalation)
  - [Stage 3: The Stronghold (Persistence & Lateral Movement)](#stage-3-the-stronghold-persistence-lateral-movement)
  - [Stage 4: The Shadow (Defense Evasion & Anti-Forensics)](#stage-4-the-shadow-defense-evasion-anti-forensics)
  - [Stage 5: Data Exfiltration & Impact](#stage-5-data-exfiltration-impact)
  - [Stage 6: The Professional (Governance & Reporting)](#stage-6-the-professional-governance-reporting)
  - [Lab Progression](#lab-progression)
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
  - [Lab Progression](#lab-progression)
- [Part 10: Social Engineering](#part-10-social-engineering)
  - [Stage 1: Intelligence & Reconnaissance (The Setup)](#stage-1-intelligence-reconnaissance-the-setup)
  - [Stage 2: The Digital Assault (Remote Vectors)](#stage-2-the-digital-assault-remote-vectors)
  - [Stage 3: The Human Element (Direct Interaction)](#stage-3-the-human-element-direct-interaction)
  - [Stage 4: The Physical Breach (Boots on the Ground)](#stage-4-the-physical-breach-boots-on-the-ground)
  - [Stage 5: Defense & Awareness (The Shield)](#stage-5-defense-awareness-the-shield)
  - [Lab Progression](#lab-progression)
- [Part 11: Denial of Service](#part-11-denial-of-service)
  - [Stage 1: Objective & Strategy (The Planning)](#stage-1-objective-strategy-the-planning)
  - [Stage 2: The Arsenal (Attack Methods)](#stage-2-the-arsenal-attack-methods)
  - [Stage 3: Infrastructure & Execution (The Assault)](#stage-3-infrastructure-execution-the-assault)
  - [Stage 4: Defense & Mitigation (The Shield)](#stage-4-defense-mitigation-the-shield)
  - [Lab Progression](#lab-progression)
- [Part 12: Session Hijacking](#part-12-session-hijacking)
  - [Stage 1: Reconnaissance & Vulnerability Analysis](#stage-1-reconnaissance-vulnerability-analysis)
  - [Stage 2: Stealing the Session ID (The Attack Vectors)](#stage-2-stealing-the-session-id-the-attack-vectors)
  - [Stage 3: Execution & Impersonation](#stage-3-execution-impersonation)
  - [Stage 4: Defense & Mitigation (The Shield)](#stage-4-defense-mitigation-the-shield)
  - [Lab Progression](#lab-progression)
- [Part 31: Password Cracking & Hash Analysis](#part-31-password-cracking-hash-analysis)
  - [Stage 1: Hash Identification & Acquisition](#stage-1-hash-identification-acquisition)
  - [Stage 2: Cracking Methodology & Tools](#stage-2-cracking-methodology-tools)
  - [Stage 3: Protocol-Specific Cracking](#stage-3-protocol-specific-cracking)
  - [Stage 4: Wordlist & Intelligence Curation](#stage-4-wordlist-intelligence-curation)

---

## Part 4: Footprinting and Reconnaissance

### **Stage 1: The "Ghost" Phase (Passive OSINT & Human Profiling)**

> [!TIP]
> **Goal:** Maximum data acquisition with zero target interaction.

- [ ] **Organizational Hierarchy:** Profile the **Audience** (Stakeholders, HR, Legal, Management) to understand who holds the keys and who is the weakest link.

- [ ] **Search Engine Hacking:** Use **Google Dorks** (`site:`, `filetype:`, `intitle:`) to find exposed documents and login portals.

- [ ] **Social Vector Mapping:** Scrape LinkedIn and professional sites to identify targets for **Phishing, Whishing, Whaling, or Smishing** based on reported tech stacks.

- [ ] **Physical Perimeter Assessment:** Evaluate the likelihood of **Shoulder Surfing, Tailgating, or Dumpster Diving** vulnerabilities.

- [ ] **Metadata & Leak Analysis:** Use **Wayback Machine** for historical paths and **GitHub/GitLab Dorking** for hardcoded API keys or internal naming conventions.

- [ ] **Domain & Ownership:** Perform **WHOIS Lookups** to identify registration dates, contact info, and associated subdomains.

- [ ] **Passive DNS & CT:** Pull **passive DNS** and **Certificate Transparency (crt.sh)** to surface shadow subdomains and SANs; cluster hosting/ASN/country.

- [ ] **Breach & Paste Monitoring:** Check **breach corpuses** (HIBP/Dehashed) and pastes/code search for leaked creds, API keys, or internal hostnames.

- [ ] **Mail Posture Recon:** Review **SPF/DMARC/DKIM** to assess spoofing risk and likely mail providers.

---

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

### **Stage 4: Advanced Fingerprinting & Logic Analysis**

> [!TIP]
> **Goal:** Understand the defensive "brain" of the target.

- [ ] **Traffic Analysis:** If vantage is gained, use **Wireshark** to analyze **Packet Captures** and examine **Handshakes** for encryption/auth weaknesses.

- [ ] **Defensive Profiling:** Identify the presence of **IDS/IPS, SIEM, SOAR, and EDR/DLP**. If found, slow down your operation immediately.

- [ ] **Unintended Binary Research:** Map the target's OS to potential **LOLBAS, GTFOBins, or WADCOMS** vectors for later movement. _(See Part 7, Phase 2 for canonical LOLBAS/GTFOBins coverage.)_

- [ ] **Version-to-CVE Correlation:** Cluster hosts by **banners/JA3/favicons** and map exposed versions to **CVE** candidates before exploitation.

---

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

### **Stage 6: Dark Web & Breach Intelligence**

> [!TIP]
> **Goal:** Uncover intelligence from dark web and historical breaches.

- [ ] **Dark Web Searches:** Use **Tor, I2P**, or dedicated **dark web search engines** to find **leaked corporate data, stolen creds, threat reports**.

- [ ] **Breach Corpus Searching:** Query **Dehashed, Have I Been Pwned, Shodan**, and **breach databases** for **employee emails, leaked credentials, domain info**.

- [ ] **Threat Actor Profiling:** Identify relevant **APT groups, cybercrime forums, adversary tradecraft** that target your industry.

- [ ] **Ransomware Gang Sites:** Monitor **ransomware operator sites** for **leaked data, victim announcements, negotiation demands**.

- [ ] **Credential Stuffing Data:** Leverage **leaked cred combos** for **password spray, targeted phishing, VPN/email access**.

---

### **Stage 7: Satellite & Geospatial Intelligence**

> [!TIP]
> **Goal:** Use geospatial data to understand physical assets and infrastructure.

- [ ] **Satellite Imagery:** Use **Google Earth Pro, Sentinel Hub, USGS** to visualize **data center locations, server rooms, facility security**.

- [ ] **Geolocation Triangulation:** Combine **IP geolocation, BGP origin, ASN info** to identify **likely hosting providers and data center countries**.

- [ ] **Signal Intelligence (SIGINT):** Use **RF mapping tools (Shodan, GreyNoise)** to identify **telecommunications infrastructure, cell towers, transmission sites**.

- [ ] **Infrastructure Clustering:** Map **AS numbers, IP blocks, DNS servers** to identify **shared hosting clusters, CDN nodes, provider boundaries**.

---

### **Stage 8: Strategy & Attack Mapping**

> [!TIP]
> **Goal:** Convert raw data into an execution plan.

- [ ] **Security Architecture Classification:** Determine if they are utilizing **Zero Trust** or standard **MFA & 2FA**.

- [ ] **Framework Alignment:** Map your findings against the **Cyber Kill Chain, Diamond Model, or MITRE ATT&CK**.

- [ ] **Vulnerability Finalization:** Decide the entry vector based on recon: **SQL Injection, MITM, or Brute Force**.

---

### **Lab Progression**

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Perform passive recon on a bug bounty target using only OSINT tools | Reconnaissance report (domains, subdomains, emails, tech stack) |
| 2 | Use Google Dorks to find exposed files on a permitted target | Dork queries + findings document |
| 3 | Enumerate subdomains using 3+ tools (Sublist3r, Amass, crt.sh) | Combined subdomain list with deduplication |
| 4 | Map a target's full DNS infrastructure (MX, NS, TXT, CNAME) | DNS map diagram |
| 5 | Perform active recon on a home lab target (traceroute, banner grabbing) | Active recon report |

> [!IMPORTANT]
> **Move-On Gate:** You can produce a complete reconnaissance report on an unfamiliar target using both passive and active techniques, identify the technology stack, and prioritize attack surface areas.

---

<a id="toc-part-5-scanning"></a>
## Part 5: Scanning

### **Stage 1: Host Discovery & Network Topology (The "Roll Call")**

> [!TIP]
> **Goal:** Identify live assets without wasting time on dead IPs or triggering ICMP alarms.

- [ ] **ARP Discovery:** Use `arp-scan` or `nmap -PR` for local segment discovery to bypass host firewalls that drop ICMP.

- [ ] **ICMP & TCP/UDP Sweeps:** Perform standard `ping` sweeps or use `nmap -PS/-PU` (ports 80, 443, 53) to find external hosts that block standard pings.

- [ ] **Passive Traffic Capture:** Utilize **Wireshark** to capture broadcast traffic, revealing active hosts without sending a single packet.

- [ ] **Network Pathing & Perimeter Analysis:** Deploy `tracert` or `hping3 --traceroute` to map hops and define **Perimeter vs DMZ vs Segmentation** boundaries.

- [ ] **IPv6 Discovery:** Include **NDP/`nmap -6`** sweeps for dual-stack assets and SLAAC-derived hosts.

---

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

### **Stage 3: Defense & Configuration Assessment (The "Armor Check")**

> [!TIP]
> **Goal:** Identify security controls that will attempt to block or alert on your presence.

- [ ] **Firewall & ACL Enumeration:** Detect the presence of a **Firewall & Nextgen Firewall** or **Host Based Firewalls** by analyzing filtered ports and **ACL** (Access Control List) behavior.

- [ ] **IDS/IPS Probing:** Use fragmentation (`-f`) or timing decoys (`-D`) to identify active **NIDS, NIPS, or HIPS** systems that may block aggressive patterns.

- [ ] **Web Surface Discovery:** Use `ffuf` or `Gobuster` for **Directory Brute-forcing** to find hidden `/admin` or `/config` panels that are not linked publicly.

- [ ] **Service-Specific Enum:** Targeted checks for **SMB/RPC/WinRM**, **LDAP/Kerberos (AS-REP preauth, SPNs)**, **SNMP v1/v2c/v3**, **SMTP VRFY/EXPN**, **SSH KEX/ciphers**, **RDP/NLA**, **DBs (MySQL/MSSQL/Postgres)**, **Redis/Mongo/Elastic**.

---

### **Stage 4: Vulnerability Association & Attack Mapping**

> [!TIP]
> **Goal:** Convert raw scan data into actionable exploitation vectors.

- [ ] **Scripted Vulnerability Probing:** Use the **Nmap Scripting Engine (NSE)** (`--script vuln`) to check for known **Zero Day** or common exploits in identified versions.

- [ ] **Attack Surface Selection:** Match findings to your known **Common Attacks**—e.g., **SQL Injection** for web servers or **Buffer Overflows** for legacy binaries.

- [ ] **Unintended Tool Research:** For discovered OS versions, research **LOLBAS, GTFOBins, or WADCOMS** to leverage existing system binaries for lateral movement. _(See Part 7, Phase 2 for canonical LOLBAS/GTFOBins coverage.)_

- [ ] **Traffic Intelligence:** Finalize your plan by inspecting **Packet Captures** for cleartext protocols or weak encryption that allows for **MITM** or **Replay Attacks**.

- [ ] **Cluster & Correlate:** Group hosts by **banners/JA3/favicons** and map versions to likely **CVEs** before exploitation.

---

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

### **Stage 6: Advanced Scanning Techniques**

> [!TIP]
> **Goal:** Optimize scanning efficiency and discover hidden services.

- [ ] **Parallel & Distributed Scanning:** Use **masscan** for rapid scanning of large ranges; distribute scans across **multiple IPs/proxies** to avoid threshold detection.

- [ ] **Custom Probes & NSE Scripting:** Write **NSE scripts** for **service-specific probing** (e.g., extracting **SANs from TLS**, **banner grabbing**, **service enumeration**).

- [ ] **WAF/CDN Bypass:** Identify backend IPs via **DNS history, SSL cert mismatches, HTTP header fingerprints**, and scan directly if possible.

- [ ] **Certificate Transparency (CT) Recon:** Parse **CT logs** to discover **hidden subdomains, domain variants, and organization structure**.

- [ ] **Reverse DNS Lookup:** Use **reverse DNS** to discover **vhosts, services, and hostnames** associated with IP ranges.

- [ ] **Proxychains & Proxy Pivoting:** Route scans through **VPNs, proxies, compromised hosts** to obscure source IP and bypass **geographic restrictions**.

### **Lab Progression**

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Scan a home lab subnet with Nmap (host discovery + port scan) | Nmap output report |
| 2 | Perform service version detection and OS fingerprinting | Annotated scan results |
| 3 | Write a custom NSE script to detect a specific vulnerability | Working .nse script |
| 4 | Scan a target through a proxy chain / VPN tunnel | Scan results + stealth analysis |
| 5 | Compare scan results with and without IDS evasion techniques | Evasion effectiveness report |

> [!IMPORTANT]
> **Move-On Gate:** You can discover all live hosts and open ports on a /24 subnet, identify service versions and OS types, and adapt scan techniques to evade basic IDS detection.

---

<a id="toc-part-6-enumeration"></a>
## Part 6: Enumeration

> [!NOTE]
> **Note:** Part 5 (Scanning) covers host discovery, port scanning, and defense identification. Part 6 focuses specifically on **extracting detailed information from discovered services** to build an attack profile. If you haven't completed Part 5, do so first.

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

### **Stage 2: Directory & Identity Enumeration**

> [!TIP]
> **Goal:** Map users, groups, and organizational structure from directory services.

- [ ] **LDAP Enumeration:** Query **LDAP** (port 389) to extract **users, groups, computers, password policies** without authentication.

- [ ] **Active Directory Recon:** Use **ldapsearch, enum4linux-ng, BloodHound** to map **domain trusts, group membership, SPNs, delegation**.

- [ ] **Kerberos Enumeration:** Use **kerbrute** for **username enumeration** via **AS-REQ responses**; identify **accounts without pre-authentication (AS-REP Roastable)**.

- [ ] **SMTP Enumeration:** Use **VRFY, EXPN, RCPT TO** commands to **verify valid email addresses and usernames** on mail servers.

- [ ] **RPC Enumeration:** Use **rpcclient, rpcinfo** to enumerate **RPC endpoints, user SIDs, domain information, printer shares**.

---

### **Stage 3: DNS & Infrastructure Enumeration**

> [!TIP]
> **Goal:** Extract naming, network, and infrastructure intelligence from DNS.

- [ ] **DNS Zone Transfer:** Attempt **AXFR/IXFR** transfers to extract **full DNS records** and internal hostnames.

- [ ] **DNS Record Enumeration:** Query **A, AAAA, MX, TXT, SRV, CNAME, NS, PTR** records to map **mail servers, services, subdomains, SPF/DMARC/DKIM** policies.

- [ ] **DNS Spoofing Prep:** Identify **DNS split-view** configurations and **internal domain naming** for **DNS rebinding attacks**.

- [ ] **Reverse DNS Sweeps:** Perform **PTR record lookups** across discovered IP ranges to reveal **hostnames, naming conventions, and hidden services**.

---

### **Stage 4: Database & Application Enumeration**

> [!TIP]
> **Goal:** Extract schemas, credentials, and data from discovered database and application services.

- [ ] **Database Discovery:** Identify **MySQL, MSSQL, PostgreSQL, Oracle, MongoDB, Redis, Elasticsearch** on standard/non-standard ports.

- [ ] **Database Default Creds:** Test **default credentials** (root/password, sa/sa, admin/admin) against discovered databases.

- [ ] **Database Information Schema:** Query **INFORMATION_SCHEMA** tables to enumerate **user accounts, object permissions, stored procedures**.

- [ ] **Backup & Recovery:** Identify **backup locations, recovery mode**, and **log files** that may contain **plaintext passwords or recovery keys**.

- [ ] **Web Application Enumeration:** Use **Gobuster, feroxbuster, ffuf** to discover **hidden directories, API endpoints, admin panels, configuration files, and backup archives** (.bak, .old, .swp).

---

### **Stage 5: Attack Surface Consolidation & Enumeration OpSec**

> [!TIP]
> **Goal:** Consolidate findings into an attack plan while maintaining stealth.

- [ ] **Attack Surface Map:** Combine all enumeration results into a **structured target profile** — users, credentials, shares, services, misconfigurations, and potential exploitation vectors.

- [ ] **Prioritized Attack Paths:** Rank targets by **exploitability and impact** — prioritize **null sessions, default credentials, writable shares, exposed admin panels, and AS-REP Roastable accounts**.

- [ ] **Tool Fingerprinting Awareness:** Understand that enumeration tools leave signatures — **vary User-Agents, throttle requests, rotate source IPs** where possible.

- [ ] **Timing Discipline:** Spread enumeration queries over time; avoid **rapid-fire LDAP/SMB/SNMP queries** that trigger **anomaly-based detection**.

- [ ] **Documentation:** Record all findings with **timestamps, source IPs, and tool commands** used — this feeds directly into **reporting and evidence collection**.

### **Lab Progression**

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Enumerate SMB shares and users on a Windows lab target | Enumeration findings document |
| 2 | Enumerate SNMP on a network device (community strings, MIBs) | SNMP data export |
| 3 | Perform full LDAP enumeration against a lab AD domain | User/group/OU listing |
| 4 | Enumerate DNS zone transfers and subdomain brute-forcing | DNS enumeration report |
| 5 | Build a complete attack surface map from enumeration data | Attack profile document with prioritized paths |

> [!IMPORTANT]
> **Move-On Gate:** You can enumerate services, users, shares, and misconfigurations across SMB, LDAP, SNMP, DNS, and web services, and produce a prioritized attack surface map.

---

<a id="toc-part-7-system-hacking--initial-compromise"></a>
## Part 7: System Hacking & Initial Compromise

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

### **Stage 2: The Ascension (Privilege Escalation)**

> [!TIP]
> **Goal:** Move from low-level foothold to administrative control by exploiting system logic.

**Windows Privilege Escalation:**

- [ ] **UAC Bypass:** Exploit **COM elevation, DLL hijack, token impersonation** to bypass **User Account Control**.

- [ ] **Service Misconfigs:** Abuse **weak service permissions, unquoted paths, service binaries** for **privilege hijack**.

- [ ] **Token Impersonation:** Steal **delegation tokens** from services to impersonate **SYSTEM/Domain Admin**.

- [ ] **DLL/DLL-Proxying:** Hijack **DLL search order** or use **sideloading** to execute arbitrary code at higher privilege.

- [ ] **Kernel Exploitation:** Target **unpatched zero-days** (MS21-1234) for **kernel-level code execution**.

- [ ] **Group Policy Exploitation:** Abuse **GPP passwords, startup scripts, scheduled tasks** for **privilege gain**.

**Active Directory Attacks:**

- [ ] **Kerberoasting:** Extract **TGS tickets** for **service accounts (SPNs)**, crack offline with **hashcat/JtR** to recover **plaintext passwords**.

- [ ] **AS-REP Roasting:** Target accounts with **pre-authentication disabled**, extract **AS-REP hashes** for offline cracking.

- [ ] **Golden/Silver Tickets:** Forge **TGT (Golden)** or **TGS (Silver)** tickets using **krbtgt hash** or **service account hash** for **persistent domain access**.

- [ ] **DCSync Attack:** Abuse **replication rights** to extract **password hashes** from **Domain Controller** without direct access.

- [ ] **BloodHound/SharpHound:** Map **AD trust relationships, ACLs, group memberships** to find **shortest path to Domain Admin**.

- [ ] **NTLM Relay:** Capture **NTLM authentication** and relay to **SMB/LDAP/HTTP** services for **lateral movement**.

- [ ] **Constrained/Unconstrained Delegation:** Abuse **delegation rights** to impersonate **privileged users** across domain services.

**Linux Privilege Escalation:**

- [ ] **setuid/setgid Abuse:** Exploit **vulnerable SUID binaries** (vim, cp, find) with **PATH manipulation**.

- [ ] **Capabilities Abuse:** Abuse **CAP_SETUID/CAP_SYS_ADMIN** for **shell execution as root**.

- [ ] **sudo Misconfigs:** Leverage **sudoers entries** (NOPASSWD, wildcard paths) for **privilege escalation**.

- [ ] **Kernel LPE:** Exploit **unpatched kernel vulnerabilities** (dirty cow, CVE-2016-5195) for **root shell**.

- [ ] **Cron/Systemd Abuse:** Hijack **cron jobs, systemd timers, .timer files** for **privilege execution**.

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

### **Lab Progression**

> [!TIP]
> **Goal:** Practice compromise only in controlled environments and produce professional evidence.

- [ ] **Beginner Host Labs:** Complete at least 5 intentionally vulnerable Linux/Windows machines; document initial access, privilege escalation, evidence, and remediation.
- [ ] **Credential Handling Lab:** Capture and crack lab-only hashes, then document storage, chain of custody, and cleanup. Use the Password Cracking Gate before attempting this.
- [ ] **Post-Exploitation Timeline:** Build an operator timeline and defender timeline for one lab compromise.
- [ ] **Detection Pairing:** For every exploit path, identify Windows Event Logs, Sysmon, auditd, network, or SIEM artifacts.
> [!IMPORTANT]
> **Move-On Gate:** Submit 3 full lab attack reports using the Part 39 structure.

<a id="toc-part-8-malware--weaponization"></a>
## Part 8: Malware & Weaponization

> **Safety Gate:** Malware work is restricted to isolated local labs with snapshots, host-only networking, no shared clipboard, no mounted host folders, and no third-party targets. Before running any sample or payload, define expected behavior, logging sources, rollback steps, and containment checks.

### **Stage 1: The Design & Logic (Architecture)**

> [!TIP]
> **Goal:** Design the malware's purpose using core security principles.

- [ ] **Target the CIA Triad:** Define if your payload destroys **Integrity** (Wipers/Data modification) or denies **Availability** (Ransomware/DDoS).

- [ ] **Weaponize Cryptography:** Implement **Public vs Private Keys** (Asymmetric Encryption) to lock files securely, ensuring only the attacker holds the decryption key.

- [ ] **Cryptographic Attacks:** Understand **padding oracle attacks, timing attacks, weak random number generation** to break encryption implementations.

- [ ] **Key Management Flaws:** Exploit **hardcoded keys, weak key derivation (KDF), insecure key storage** in applications.

- [ ] **C2 Protocol Design:** Choose **Secure vs Insecure Protocols** for Command & Control. Will you hide inside **HTTPS** traffic or use **DNS** tunneling to evade **Firewall & Next-Gen Firewall** inspection?

- [ ] **Risk Assessment:** Use the **Diamond Model** or **Cyber Kill Chain** to map out how your malware will move from **Reconnaissance** to **Actions on Objectives**.

---

### **Stage 2: The Payload & Mechanism (Weaponization)**

> [!TIP]
> **Goal:** Execute code on the target system.

- [ ] **Memory Exploitation:** Leverage **Buffer Overflow** or **Memory Leak** vulnerabilities to inject shellcode into legitimate processes, bypassing file scanning.

- [ ] **Delivery Vectors:** Utilize **Social Engineering** (Phishing/Whaling) or **Drive-by Attacks** to get the initial execution on the endpoint.

- [ ] **Payload Staging:** Use **modern modular frameworks** (Sliver, Havoc, Mythic, Brute Ratel C4) and **Metasploit/Cobalt Strike** with signature-hardened profiles.

- [ ] **Cloud-Native C2:** Hide beacons inside **trusted APIs** (e.g., **Microsoft Graph/SharePoint, Slack/Teams webhooks**) to blend with enterprise traffic beyond HTTP/DNS.

- [ ] **Living off the Land:** Use **LOLBAS**, **GTFOBins**, or **WADCOMS** to execute malicious logic using trusted system tools. _(See Part 7, Phase 2 for canonical LOLBAS/GTFOBins coverage.)_

---

### **Stage 3: Evasion & Defense Bypassing (Invisibility)**

> [!TIP]
> **Goal:** Blind the defensive stack.

- [ ] **Defeat Static Analysis:** Apply **Obfuscation** (packing, encoding) to change the file hash and bypass traditional **Antivirus** signatures.

- [ ] **Sandbox Detection:** Code the malware to detect **Sandboxing** environments (e.g., checking for specific drivers, lack of mouse movement) and go dormant to generate a **False Negative**.

- [ ] **EDR/DLP Bypass:** Unhook API calls to hide from **EDR** (Endpoint Detection Response) and **DLP** monitors. Operate in memory (Fileless) to avoid leaving disk artifacts.

- [ ] **Traffic Masking:** Encrypt C2 traffic to look like normal web browsing, defeating **NIDS/NIPS** (Network Intrusion Prevention Systems).

- [ ] **In-Memory Evasion:** Apply **sleep obfuscation, call stack spoofing, indirect syscalls** to evade **memory scanning and EDR heuristics** during beacon idle time.

---

### **Stage 4: Persistence & Escalation (Entrenchment)**

> [!TIP]
> **Goal:** Survive reboots and gain total control.

- [ ] **Privilege Escalation:** Exploit **Operating System Hardening** gaps or **Kernel** vulnerabilities (Zero Day) to escalate from User to **SYSTEM/Root**. _(See Part 7, Phase 2 for canonical privilege escalation methodology.)_

- [ ] **Persistence Mechanisms:** Hide payload execution in **Scheduled Tasks**, **Registry Keys**, or **WMI** subscriptions to survive **Patching** and reboots.

- [ ] **Lateral Movement:** Use **Pass the Hash** or compromised **MFA & 2FA** tokens to pivot to other systems within the **Perimeter**. _(See Part 7, Phase 3 for canonical credential harvesting and lateral movement techniques.)_

- [ ] **Defense Disabling:** Actively terminate **Antimalware** or **Host Based Firewall** processes if privileges allow.

---

### **Stage 5: Counter-Forensics & Professionalism (The Cleanup)**

> [!TIP]
> **Goal:** Hide the tracks and adhere to engagement rules.

- [ ] **Anti-Forensics:** Use secure deletion to scrub **RAM artifacts** and **Packet Captures** to frustrate the **Basics of Forensics** investigation.

- [ ] **Log Manipulation:** Alter or clear **Event Logs** and **Syslogs** to blind **SIEM** and **SOAR** systems from correlating the attack.

- [ ] **Reverse Engineering Resistance:** Strip binary symbols and use anti-debugging techniques to make **Basics of Reverse Engineering** difficult for the Blue Team.

- [ ] **Rules of Engagement:** (For Red Teams) Ensure the malware's scope aligns with the **Penetration Testing Rules of Engagement**—do not destroy production data unless authorized.

---

### **Stage 6: Document & Cloud Weaponization**

> [!TIP]
> **Goal:** Weaponize documents, email clients, and cloud services for initial access, persistence, and exfiltration. This content was previously misplaced in Part 1 (Fundamentals) — it requires knowledge from Parts 4–7 and Part 10 (Social Engineering) first.

> **Prerequisite:** Complete Part 7 (System Hacking), Part 9 (Sniffing & Spoofing), and Part 10 (Social Engineering) before this phase.

**Office & Document Exploits:**

- [ ] **VBA & XLM 4.0 Macros:** Build payloads, sign macros, and abuse **template injection (remote DOTM)**.

- [ ] **DDE & Template Abuse:** Trigger code via **DDEAUTO**, external templates, and **Follina-style** URL template fetches.

- [ ] **OneNote/PDF/Embedded Files:** Weaponize **OneNote pages, PDF JS**, and embedded **LNK/ISO/IMG** loaders; understand **MOTW** bypasses.

- [ ] **Protected View/ATP Evasion:** Study **mark-of-the-web**, **protected view**, and common sandbox evasion tricks.

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

---

<a id="toc-part-9-sniffing--spoofing"></a>
## Part 9: Sniffing & Spoofing

### **Stage 1: The Environment & Fundamentals (The Setup)**

> [!TIP]
> **Goal:** Understand the battlefield. You cannot spoof what you cannot map.

- [ ] **Protocol Hierarchy & Trust:** Differentiate between **MAC Addresses** (Layer 2 - Local Trust) and **IP Addresses** (Layer 3 - Routing). Spoofing relies on exploiting the trust mismatch between these layers.

- [ ] **Secure vs. Insecure Protocols:** Identify targets using cleartext protocols like **HTTP, FTP, Telnet, DNS**. These are trivial to sniff. Encrypted protocols like **TLS/HTTPS** and **SSH** require advanced downgrade attacks or decryption to bypass.

- [ ] **The Switch vs. Hub Reality:** Modern networks use switches which segment traffic by MAC. You cannot passively sniff; you must **ARP spoof, MAC flood**, or **VLAN hop** to bypass segmentation.

- [ ] **Interface Configuration:** Configure NIC to **Promiscuous Mode** (tcpdump, Wireshark) to capture all traffic, not just destined to your MAC; practice with **monitor mode** on wireless cards.

- [ ] **Handshake & Session Logic:** Study **TCP/TLS handshakes** (SYN/ACK, ClientHello/ServerHello) to identify session boundaries; understand **sequence numbers, window size, timestamps** for **replay and hijack** timing.

---

### **Stage 2: Sniffing & Passive Reconnaissance (The Ear)**

> [!TIP]
> **Goal:** Capture data without alerting the target. "Listen before act."

- [ ] **Passive Packet Capture:** Use **tcpdump/Wireshark** to capture broadcast/multicast traffic (ARP, DHCP, mDNS) to identify active hosts, gateways, and services without sending directed traffic.

- [ ] **Wireless Interception:** Set wireless NIC to **monitor mode**; capture **WPA2/WPA3 4-way handshakes, PMKID** for offline cracking; identify **SSID, client MAC, AP MAC** patterns.

- [ ] **Protocol Analysis:** Filter **pcap** by protocol (HTTP, FTP, SMTP, DNS); identify **cleartext credentials, API keys, session tokens**, and software **User-Agent/Server banners**.

- [ ] **Stream Reassembly:** Use **tcpflow, Wireshark Follow TCP Stream** to reassemble files, images, emails, or form submissions from fragmented packets.

---

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

### **Stage 5: Defenses & Mitigation (The Shield)**
- [ ] **Encryption & VPN:** Force all traffic through **TLS/HTTPS, IPSec VPN, or VPN tunneling**; renders sniffed payloads unreadable; watch for **HSTS, certificate pinning** as anti-bypass measures.

- [ ] **Switch-Level Protection:** **Dynamic ARP Inspection (DAI)**, **DHCP Snooping**, **port security** reject malformed ARP/DHCP; **802.1X authentication** prevents rogue device connection.

- [ ] **Network Segmentation:** **VLAN isolation, micro-segmentation, zero trust** limits sniffing scope per compromised segment; east-west traffic encryption adds extra layers.

- [ ] **Detection Systems:** **IDS/IPS** flag high ARP packet volume, **MITM tools (ettercap signatures)**, SSL downgrade attempts; **Netflow/sFlow** detects unusual traffic patterns.

- [ ] **User Awareness:** Train users to verify **SSL certificates**, recognize **phishing login pages**, and use **password managers** to avoid clipboard paste attacks.

### **Lab Progression**

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Capture traffic with Wireshark in a home lab (HTTP, FTP, DNS) | Annotated pcap with credential extraction |
| 2 | Perform ARP spoofing + MITM with Bettercap in lab | Screenshot of intercepted traffic |
| 3 | Execute DNS spoofing to redirect lab traffic to phishing page | DNS spoof lab report |
| 4 | Perform SSL stripping against a lab web server without HSTS | Before/after traffic comparison |
| 5 | Full MITM chain: ARP spoof → DNS redirect → credential capture | End-to-end MITM lab report |

> [!IMPORTANT]
> **Move-On Gate:** You can perform a complete MITM attack chain in a lab, capture credentials from unencrypted and downgraded traffic, and explain exactly which defenses (DAI, HSTS, certificate pinning) would have prevented each technique.

---

<a id="toc-part-10-social-engineering"></a>
## Part 10: Social Engineering

> **Safety Gate:** Social engineering practice must use consented simulations only. Do not target real people, employers, classmates, public organizations, or family accounts. Unauthorized phishing and impersonation are not "practice"; they are operational and legal exposure.

### **Stage 1: Intelligence & Reconnaissance (The Setup)**

> [!TIP]
> **Goal:** Know the target better than they know themselves.

- [ ] **Digital Recon:** Execute **OSINT** using **Google Dorks, LinkedIn scraping, GitHub dorking** to extract employee names, emails, roles, tech stacks, and company structure.

- [ ] **Physical Recon:** Perform **dumpster diving** to recover **org charts, vendor invoices, sticky notes** with passwords; observe **badge access patterns, delivery procedures**.

- [ ] **Domain & Infrastructure Prep:** Register **typo-squatting domains** (e.g., `companysupport.com`, `company-login.net`) that mimic target portals; prepare **phishing landing pages**.

- [ ] **Social Media Profiling:** Mine **LinkedIn, Twitter, GitHub, Glassdoor** for **personal details, relationships, job changes** to craft personalized lures.

---

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

### **Stage 3: The Human Element (Direct Interaction)**

> [!TIP]
> **Goal:** Use psychology and social manipulation to bypass logic.

- [ ] **Voice Pretexting:** Call as **IT support, HR, vendor, auditor, law enforcement** using social engineering pretexts; use **authority, urgency, fear** to bypass critical thinking.

- [ ] **Authority & Compliance Trigger:** Leverage **IT/Security/Auditor/Legal persona** to demand compliance; abuse **helpfulness bias** to force password resets or system access.

- [ ] **Reciprocity & Obligation:** Provide small **favors (tech help, free tools)** to create sense of obligation; ask for credentials or access in return.

---

### **Stage 4: The Physical Breach (Boots on the Ground)**

> [!TIP]
> **Goal:** Gain physical access to networks and facilities.

- [ ] **Tailgating:** Follow **authorized employees** into secure zones using badges/access cards; use **coffee cup hold, uniform/vendor persona** to bypass visual checks.

- [ ] **Shoulder Surfing:** Observe **PIN entry, password typing, screen content** in public spaces (airports, coffee shops, open offices) to capture credentials.

- [ ] **Badge Cloning:** Capture **RFID badge data** using **Proxmark3, ACR122U** and clone to malicious card; bypass **magnetic stripe readers** via cloning.

- [ ] **Physical Device Placement:** Plant **USB drops, rogue access points, hardware keyloggers** in common areas for **auto-execution** when connected by unsuspecting users.

---

### **Stage 5: Defense & Awareness (The Shield)**

> [!TIP]
> **Goal:** Prevent the human hack through training and controls.

- [ ] **Authentication:** Enforce **MFA/2FA** (TOTP, hardware keys, push notifications) so password compromise alone doesn't grant access; watch for **MFA fatigue attacks**.

- [ ] **Verification Protocols:** Train staff to **challenge unknown callers** via **secondary channel callback**; never trust caller ID alone; verify requests through official channels.

- [ ] **Physical Security:** Enforce **no-tailgating policies, visitor escorts, badge display requirements, clean desk policies** to prevent **dumpster diving and shoulder surfing**.

- [ ] **Security Awareness:** Regular **phishing simulations, red team testing, security training** to build **skepticism and reporting culture**; reward **security-first behavior**.

- [ ] **MFA Resilience:** Teach differences between **phishing-resistant MFA (FIDO2/Passkeys)** vs **phishable MFA (SMS/Push/OTP)**; test and mitigate **MFA fatigue** scenarios.

### **Lab Progression**

> [!TIP]
> **Goal:** Learn social engineering defensively and ethically.

- [ ] **Email Authentication Lab:** Configure and validate SPF, DKIM, and DMARC on a test domain or lab mail stack.
- [ ] **Header Forensics Lab:** Analyze benign/phishing email headers and identify sender path, SPF/DKIM/DMARC result, and suspicious infrastructure.
- [ ] **GoPhish Simulation Lab:** Run a consented internal lab campaign against test inboxes only; measure open/click/report rates.
- [ ] **Pretext Review:** Write three pretexts and then write the defensive awareness guidance that would defeat them.
> [!IMPORTANT]
> **Move-On Gate:** Produce a social-engineering simulation plan with ROE, consent model, metrics, and debrief template.

<a id="toc-part-11-denial-of-service"></a>
## Part 11: Denial of Service

> **Safety Gate:** DoS testing is local-lab-only unless a written contract explicitly authorizes it. Never run DoS tools against public IPs, SaaS platforms, school networks, ISP infrastructure, or bug bounty targets unless the scope explicitly permits availability testing.

### **Stage 1: Objective & Strategy (The Planning)**

> [!TIP]
> **Goal:** Understand DoS/DDoS scope and firepower requirements.

- [ ] **Denial of Service (DoS):** Single attacker sends **crafted traffic** to overwhelm a target's **CPU, bandwidth, or connections**; from one IP; **relatively easy detection**.

- [ ] **Distributed Denial of Service (DDoS):** **Multiple sources** (botnet, amplification servers) send traffic **simultaneously**; harder to trace and block; **stronger firepower**.

- [ ] **Target Assessment:** Identify **critical services** (web, DNS, mail, VPN) and **upstream bottlenecks** (ISP bandwidth, DDoS mitigation capacity) to determine **attack viability**.

---

### **Stage 2: The Arsenal (Attack Methods)**

> [!TIP]
> **Goal:** Select the right DoS technique for target vulnerabilities.

- [ ] **Volumetric Attacks:** Consume **bandwidth** using **SYN floods, UDP floods, ICMP floods** to saturate network pipes; use **DNS amplification, NTP reflection** to multiply traffic (1 request → 1000× response).

- [ ] **Protocol Attacks:** Exploit **TCP/IP stack weaknesses** (malformed packets, fragment handling, connection states) using **Ping of Death, Teardrop, SYN floods** to crash systems or exhaust connection limits.

- [ ] **Application-Layer Attacks:** Target **specific services** with **HTTP floods (Slowloris), database queries (CPU spike), cached assets** to overwhelm **web servers, APIs, load balancers** at Layer 7.

- [ ] **IoT/Botnets:** Compromise **webcams, routers, smart devices** via **default creds, unpatched firmware** to join **Mirai, Dridex-style botnets** for DDoS-as-a-Service.

---

### **Stage 3: Infrastructure & Execution (The Assault)**

> [!TIP]
> **Goal:** Deploy and sustain the attack at scale.

- [ ] **Botnet Assembly:** Recruit **thousands of infected IoT/servers** or use **existing botnet services** (DDoS-as-a-Service, rent botnet time); establish **C&C control** via IRC/DNS/Peer-to-Peer.

- [ ] **Traffic Generation:** Use **tools like hping3, slowhttptest, LOIC, Colasoft PacketBuilder** to craft and blast custom packets; coordinate **multi-vector attacks** (volumetric + protocol + app-layer simultaneously).

- [ ] **Proxy/Spoofing:** Use **open reflectors/amplifiers** (DNS servers, NTP, SNMP) to amplify traffic; spoof **source IP addresses** to obscure attacker origin.

- [ ] **Duration & Monitoring:** Sustain attack for **hours/days** while monitoring **target availability, ISP response, filtering changes**; adjust payload/vector on-the-fly.

---

### **Stage 4: Defense & Mitigation (The Shield)**

> [!TIP]
> **Goal:** Detect, absorb, and neutralize DoS attacks.

- [ ] **Edge Defense:** Deploy **Cloudflare, Akamai, AWS Shield Standard** to absorb DDoS at **ISP/CDN level** before traffic reaches origin; filter **malformed packets, spoofed IPs** at network edge.

- [ ] **Rate Limiting & Throttling:** Implement **connection limits, request rate caps, CAPTCHAs, geo-blocking** to let legitimate users through while rejecting flood traffic.

- [ ] **Monitoring & Detection:** Deploy **NetFlow/sFlow analysis, IDS/IPS (Suricata, Zeek)** to detect **unusual traffic patterns, connection spikes, protocol anomalies**; alert on **RTO timeouts, CPU/bandwidth saturation**.

- [ ] **Architectural Resilience:** Use **anycast DNS, geographically distributed servers, auto-scaling, load balancing** to spread load; oversizing infrastructure to **absorb baseline attacks**; prepare **incident response playbooks**.

- [ ] **ISP/Carrier Coordination:** Work with **ISP's DDoS mitigation services** to scrub traffic upstream; establish **BGP blackholing** to discard attack traffic at border; maintain **redundant ISPs/circuits**.

### **Lab Progression**

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Study DoS attack types and classify by OSI layer | Classification document with examples |
| 2 | Simulate SYN flood against lab web server with hping3 | Traffic capture + server impact analysis |
| 3 | Test Slowloris against Apache in lab, then apply mitigation | Before/after performance comparison |
| 4 | Configure rate limiting and SYN cookies on lab firewall | Firewall configuration + test results |
| 5 | Design a DDoS defense architecture for a hypothetical company | Architecture diagram + defense plan |

> [!IMPORTANT]
> **Move-On Gate:** You can explain and classify DoS/DDoS attack types, demonstrate basic DoS in a lab, and design defensive countermeasures at the network, host, and application layers.

---

<a id="toc-part-12-session-hijacking"></a>
## Part 12: Session Hijacking

### **Stage 1: Reconnaissance & Vulnerability Analysis**

> [!TIP]
> **Goal:** Find a target and identify its weaknesses.

- [ ] **Target Identification:** Use **Reconnaissance** and **OSINT** to identify target web applications.

- [ ] **Protocol Analysis:** Check if the application uses **Unsecure Protocols** (HTTP) for any part of the session, making it vulnerable to sniffing.

- [ ] **Session Mechanism Analysis:** Study **session ID generation, cookie attributes, token entropy** for weak patterns.

- [ ] **Vulnerability Scanning:** Test for **XSS, CSRF, MITM susceptibility, weak session timeouts**.

---

### **Stage 2: Stealing the Session ID (The Attack Vectors)**

> [!TIP]
> **Goal:** Execute the attack to acquire the victim's session token.

- [ ] **Network Sniffing:** If HTTP is in use, launch **packet capture** with **Wireshark** on the local network or from a **Rogue Access Point** to intercept session cookies.

- [ ] **Client-Side Injection:** Craft and deliver an **XSS** payload (via **Phishing** or a stored vulnerability) to steal `document.cookie` from the user's browser.

- [ ] **Man-in-the-Middle:** Execute a **MITM** attack using **ARP spoofing, DNS spoofing**, or **SSL stripping** to intercept encrypted sessions.

- [ ] **Session Fixation:** Force victim to use **attacker-controlled session ID** by injecting it via URL or cookies before authentication.

- [ ] **Browser Extension Abuse:** Exploit **malicious browser extensions** to exfiltrate cookies from victim's browser storage.

---

### **Stage 3: Execution & Impersonation**

> [!TIP]
> **Goal:** Use the stolen token to access the user's account.

- [ ] **Token Injection & Hijack:** Inject the stolen session ID into your browser cookies to achieve **impersonation** of the victim, bypassing **authentication** completely.

- [ ] **Session Replay:** Reuse captured **authentication tokens, API keys, JWT** to access protected resources.

- [ ] **Privilege Escalation:** If session belongs to **privileged user**, exploit to gain **administrative access**.

---

### **Stage 4: Defense & Mitigation (The Shield)**

> [!TIP]
> **Goal:** Prevent the attack from succeeding.

- [ ] **Enforce Encryption:** Mandate **TLS 1.2+** for all web traffic; implement **HSTS** to prevent SSL stripping.

- [ ] **Secure Cookie Attributes:** Implement `HttpOnly`, `Secure`, `SameSite=Strict` flags on cookies to mitigate **XSS** theft and CSRF.

- [ ] **Session Management:** Implement **session regeneration after login**, **absolute/idle timeouts**, **IP/User-Agent binding**.

- [ ] **Multi-Factor Authentication:** Deploy **MFA/2FA** to ensure stolen session token alone is insufficient for sensitive actions.

- [ ] **Network Monitoring:** Use **IDS/IPS** to detect **MITM patterns, ARP spoofing, SSL stripping attempts**. _(See Part 9 for canonical spoofing coverage.)_

### **Lab Progression**

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Analyze session cookies in a lab web app (entropy, attributes) | Cookie analysis report |
| 2 | Perform session fixation attack on a vulnerable lab app | Attack steps + session token evidence |
| 3 | Steal session cookies via XSS in DVWA/WebGoat | Session hijack lab report |
| 4 | Implement secure session management on a lab app | Hardened configuration document |
| 5 | Test session hijacking defenses (regeneration, binding, timeouts) | Defense effectiveness report |

> [!IMPORTANT]
> **Move-On Gate:** You can identify weak session management, perform session hijacking via multiple vectors (fixation, XSS, sniffing), and implement secure session handling with proper cookie attributes, regeneration, and MFA.

> 📌 **Cross-Reference:** Web application session attacks (JWT hijacking, OAuth token theft, API session management, cookie-based CSRF) are covered in depth in **[Part 17: Web Application Hacking](Phase-4.md#part-17-web-application-hacking)** and **[Part 19: API Security](Phase-4.md#part-19-api-security)** (Phase 4). The techniques in this Part focus on network-layer session attacks; web-layer attacks require Phase 4 knowledge.

---




## Part 31: Password Cracking & Hash Analysis

### **Stage 1: Hash Identification & Acquisition**

> [!TIP]
> **Goal:** Identify what you have before cracking.

- [ ] **Hash Identification:** Use **hashid, hash-identifier, Name-That-Hash** to identify algorithm from hash format (length, prefix like `$2y$`, `$6$`, `$NT$`).

- [ ] **Hash Acquisition:** Obtain hashes from **SAM/NTDS.dit (Windows), /etc/shadow (Linux), database dumps, LSASS memory, pcap files, web app source**.

- [ ] **Common Hash Types:** Master identifying and handling **NTLM, NTLMv1/v2, NetNTLM, MD5, SHA-1, SHA-256, bcrypt, Argon2, PBKDF2, WPA2-PMKID, Kerberos (5/17/18/23)**.

---

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

### **Stage 3: Protocol-Specific Cracking**

> [!TIP]
> **Goal:** Crack hashes captured from real network protocols.

- [ ] **NTLM / NetNTLMv2:** Capture with **Responder, ntlmrelayx**; crack with **hashcat -m 5600**; understand why NTLMv2 is harder than NTLMv1.

- [ ] **Kerberos Tickets:** Crack **Kerberoasted TGS (-m 13100)** and **AS-REP hashes (-m 18200)** offline with hashcat using targeted service-account wordlists.

- [ ] **WPA2 Handshakes:** Crack **4-way handshake (-m 22000)** and **PMKID (-m 22001)** from wireless captures with GPU-accelerated hashcat.

- [ ] **SSH Private Keys:** Use **ssh2john** to extract crackable hash from passphrase-protected keys; crack with JtR.

- [ ] **Office / PDF / ZIP:** Extract hashes with **office2john, pdf2john, zip2john**; crack with JtR or hashcat for document password recovery.

---

### **Stage 4: Wordlist & Intelligence Curation**

> [!TIP]
> **Goal:** Build targeted wordlists that outperform generic lists.

- [ ] **OSINT-Driven Wordlists:** Use **CeWL** to spider target websites and extract **company-specific vocabulary** for highly targeted password lists.

- [ ] **Custom Rule Writing:** Write **Hashcat/JtR rules** encoding target's known password policy — minimum length, required chars, common suffix patterns.

- [ ] **Credential Stuffing Lists:** Use **breach corpora (Collection #1, Dehashed)** to build target-specific lists from previously leaked passwords for the same user base.

- [ ] **Mentalist / PACK:** Use **Mentalist (GUI) or PACK (Policy Analysis)** to analyze cracked passwords and generate statistically optimized masks and rules.

> 📌 **Cross-Reference:** Password cracking skills are directly applied in **[Part 23: Active Directory & Entra ID](Phase-6.md#part-23-active-directory-entra-id)** (Kerberoasting, AS-REP Roasting), **[Part 21: Wireless Pentesting](Phase-5.md#part-21-wireless-pentesting)** (WPA handshake cracking), and **Part 7: System Hacking** (credential-based lateral movement). Complete this Part before Phase 5–6.

---

<a id="toc-part-32-physical-penetration-testing"></a>