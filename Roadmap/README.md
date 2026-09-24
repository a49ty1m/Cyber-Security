
# 🛡️ Cybersecurity Master Roadmap

> **Career Target:** Penetration Testing → Red Team Operations → Advanced Offensive Security → AI Red Teaming

---

> [!TIP]
> ### 💎 Best Navigated in Obsidian
> This Master Roadmap and all Stage modules are deeply interconnected with **bi-directional Obsidian wikilinks** (`[[Stage-X#Heading|Title]]`). Open this repository as a vault in **[Obsidian](https://obsidian.md/)** for interactive link previews, graph analysis, and frictionless navigation.

### 🧭 Stage Fast-Switch & Navigation Hub

| 🏠 Root | 🔵 Stage 1 | 🟠 Stage 2 | 🟣 Stage 3 | 🏢 Stage 4 | 🔬 Stage 5 | 📦 Shelf | 🛠️ Tools |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [🏠 Root README](../README.md) | [[Stage-1_Foundation\|Foundation]] | [[Stage-2_Offense-I\|Offense I]] | [[Stage-3_Web-and-App-Sec\|Web & App Sec]] | [[Stage-4_Enterprise\|Enterprise]] | [[Stage-5_Specialized\|Specialized]] | [[Shelf_Post-Hire\|Post-Hire]] | [[Tools/README\|Tools Hub]] |

---

## 📑 Table of Contents

|  #  | Section                                                                             | Focus & Scope                                                                        |
| :-: | :---------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------- |
|  1  | [[#🎯 Execution Order — 5 Stages\|🎯 Execution Order — 5 Stages]] ← **Start here**  | Sequential 30-module curriculum, depth rankings, stage gates, and time estimates     |
|  2  | [[#🗺️ Topics — Mapped to Execution Order\|🗺️ Topics — Mapped to Execution Order]] | Comprehensive topic breakdowns across all technical security domains                 |
|     | ↳ [[#🔵 STAGE 1 — FOUNDATION\|🔵 Stage 1: Foundation]]                              | Architecture, Linux & Windows Admin, Networking, Cryptography, Auth, Web             |
|     | ↳ [[#🟠 STAGE 2 — OFFENSE I\|🟠 Stage 2: Offense I]]                                | Footprinting, Scanning, Enumeration, DB Exploitation, Cracking, PrivEsc              |
|     | ↳ [[#🟣 STAGE 3 — WEB & APP SEC\|🟣 Stage 3: Web & App Sec]]                        | OWASP Top 10, Modern Web Attacks, API Security, Bug Bounty, SOC/CTI tracks           |
|     | ↳ [[#🏢 STAGE 4 — ENTERPRISE\|🏢 Stage 4: Enterprise]]                              | Active Directory, Kerberos, Cloud IAM, Containers, Adversary Emulation, Reporting    |
|     | ↳ [[#🔬 STAGE 5 — SPECIALIZED\|🔬 Stage 5: Specialized]]                            | Custom C2 Implants, Exploit Dev, AI Red Teaming, Campaign Tradecraft, Portfolio      |
|  3  | [[#📦 Shelf — Post-Hire Electives\|📦 Shelf — Post-Hire Electives]]                 | 21 off-sequence situational tracks (Mobile, ICS/SCADA, Forensics, Hardware, Telecom) |
|  4  | [[#⏱️ Daily Protocol\|⏱️ Daily Protocol & Hard Rules]]                              | 3-step loop (Engineering Foundation ➔ Lab Execution ➔ Proof) & Weekend Scripting     |
|  5  | [[#🛠️ Lab Setup\|🛠️ Lab Setup Baseline]]                                          | Hardware specs, hypervisor baselines, target environments, and practice platforms    |

---

## 🎯 Execution Order — 5 Stages

> Sequential walk order across 5 Stages, top to bottom.
> 🔴 = master it before moving on · 🟡 = learn it solid, keep moving · 🔵 = conceptual foundation (hands-on build later in specialized stage)
> ⏱ Time spans assume consistent daily sessions per the [Daily Protocol](#daily-protocol).

| # | Module | Depth | Stage | Est. Time |
| :---: | --- | :---: | :---: | :---: |
| **01** | [[Stage-1_Foundation#Module 01: Fundamentals\|Fundamentals]] — Hardware, OS, Memory, Data Rep, Programming | 🔴 | Foundation | 2–3 wks |
| **02** | [[Stage-1_Foundation#Module 02: Linux Administration\|Linux Administration]] | 🔴 | Foundation | 2–3 wks |
| **03** | [[Stage-1_Foundation#Module 03: Windows Administration\|Windows Administration]] | 🟡 | Foundation | 1–2 wks |
| **04** | [[Stage-1_Foundation#Module 04: Networking Fundamentals\|Networking Fundamentals]] | 🔴 | Foundation | 2–3 wks |
| **05** | [[Stage-1_Foundation#Module 05: Cryptography\|Cryptography]] — core concepts + attacks | 🔴 | Foundation | 1–2 wks |
| **06** | [[Stage-1_Foundation#Module 06: Authentication Standards\|Authentication Standards]] — Sessions, JWT, OAuth, MFA | 🔴 | Foundation | 1–2 wks |
| **07** | [[Stage-1_Foundation#Module 07: Web Technology Fundamentals\|Web Technology Fundamentals]] — HTTP, Cookies, CORS, REST | 🔴 | Foundation | 1–2 wks |
|  | **— [[Stage-1_Foundation#🏁 Foundation Proof Gate\|Foundation Proof Gate]] —** *(10 PCAPs, admin baselines, 3 scripts, lab report)* |  |  | **~2–3 mos** |
| **08** | [[Stage-2_Offense-I#Module 08: Footprinting & Reconnaissance\|Footprinting & Reconnaissance]] | 🔴 | Offense I | 1–2 wks |
| **09** | [[Stage-2_Offense-I#Module 09: Scanning\|Scanning]] | 🔴 | Offense I | 1 wk |
| **10** | [[Stage-2_Offense-I#Module 10: Enumeration\|Enumeration]] | 🔴 | Offense I | 1–2 wks |
| **11** | [[Stage-2_Offense-I#Module 11: Database Security\|Database Security]] | 🟡 | Offense I | 1 wk |
| **12** | [[Stage-2_Offense-I#Module 12: Password Cracking & Hash Analysis\|Password Cracking & Hash Analysis]] | 🔴 | Offense I | 1 wk |
| **13** | [[Stage-2_Offense-I#Module 13: System Hacking & Initial Compromise\|System Hacking & Initial Compromise]] | 🔴 | Offense I | 2–3 wks |
|  | **— [[Stage-2_Offense-I#🏁 Stage Gate 1 — Host Dominance & Privilege Escalation\|Stage Gate 1]] —** *(root a box, dump & crack a hash, escalate privesc)* |  |  | **~5–6 wks** |
| **14** | [[Stage-3_Web-and-App-Sec#Module 14: Web Application Hacking\|Web Application Hacking]] — SQLi, XSS, SSRF, IDOR, XXE | 🔴 | Web & App Sec | 3–4 wks |
| **15** | [[Stage-3_Web-and-App-Sec#Module 15: Session Hijacking & Token Attacks\|Session Hijacking & Token Attacks]] — Cookies, JWTs, Fixation | 🔴 | Web & App Sec | 1–2 wks |
| **16** | [[Stage-3_Web-and-App-Sec#Module 16: Web Server Hacking\|Web Server Hacking]] — Misconfig, Directory Traversal | 🔴 | Web & App Sec | 1–2 wks |
| **17** | [[Stage-3_Web-and-App-Sec#Module 17: API Security\|API Security]] — OWASP API Top 10, REST/GraphQL/gRPC | 🔴 | Web & App Sec | 2 wks |
| **18** | [[Stage-3_Web-and-App-Sec#Module 18: Bug Bounty Methodology\|Bug Bounty Methodology]] — Scope, Recon, Exploit, Report | 🔴 | Web & App Sec | 2 wks |
|  | *(parallel, absorb only — never block)* [[Stage-3_Web-and-App-Sec#Side-Track A: Detection Engineering & SOC Operations\|Detection Awareness]], [[Stage-3_Web-and-App-Sec#Side-Track B: IDS, Firewalls, and Honeypots\|IDS/Honeypots]], [[Stage-3_Web-and-App-Sec#Side-Track C: Cyber Threat Intelligence (CTI) & Attack Surface Management\|OSINT]] | 🟡 | side-track | ongoing |
|  | **— [[Stage-3_Web-and-App-Sec#🏁 Stage Gate 2 — Web Application Security Gate\|Stage Gate 2]] —** *(3+ HTB/THM writeups, OWASP Top 10 hands-on, Linux+Windows privesc demonstrated cold)* |  |  | **~8–10 wks** |
| **19** | [[Stage-4_Enterprise#Module 19: Active Directory & Entra ID\|Active Directory & Entra ID]] *(+ deferred Kerberos patch from #03)* | 🔴 | Enterprise | 3–4 wks |
| **20** | [[Stage-4_Enterprise#Module 20: Cloud Computing\|Cloud Computing]] *(+ deferred Cloud Assets patch from #04)* | 🔴 | Enterprise | 2–3 wks |
| **21** | [[Stage-4_Enterprise#Module 21: Container & Orchestration Security\|Container & Orchestration Security]] | 🟡 | Enterprise | 1–2 wks |
| **22** | [[Stage-4_Enterprise#Module 22: Adversary Emulation & Purple Teaming\|Adversary Emulation & Purple Teaming]] | 🔴 | Enterprise | 2 wks |
| **23** | [[Stage-4_Enterprise#Module 23: Sniffing & Spoofing\|Sniffing & Spoofing]] — ARP, MITM, Bettercap, Responder | 🟡 | Enterprise | 1 wk |
| **24** | [[Stage-4_Enterprise#Module 24: Social Engineering\|Social Engineering]] — Phishing, Vishing, Physical | 🟡 | Enterprise | 1 wk |
| **25** | [[Stage-4_Enterprise#Module 25: Malware & Weaponization (Conceptual)\|Malware & Weaponization]] *(conceptual — full build is #27)* | 🔵 | Enterprise | 1 wk |
| **26** | [[Stage-4_Enterprise#Module 26: Pentest Methodologies & Report Writing\|Pentest Methodologies & Report Writing]] | 🔴 | Enterprise | 1–2 wks |
|  | **— [[Stage-4_Enterprise#🏁 Stage Gate 3 — Enterprise Domain Compromise & Reporting\|Stage Gate 3]] —** *(AD domain attacked end-to-end, BloodHound exports in Git, 1 professional report)* |  |  | **~10–13 wks** |
| **27** | [[Stage-5_Specialized#Module 27: Offensive Development & Tooling\|Offensive Development & Tooling]] — C2, Shellcode, AMSI/ETW | 🔴 | Specialized | 4–6 wks |
| **28** | [[Stage-5_Specialized#Module 28: AI & LLM Red Teaming\|AI & LLM Red Teaming]] — Prompt Injection, RAG, Agentic Exploits | 🔴 | Specialized | 3–4 wks |
| **29** | [[Stage-5_Specialized#Module 29: Red Team Operations & Tradecraft\|Red Team Operations & Tradecraft]] — C2, OPSEC, Campaign | 🔴 | Specialized | 4–6 wks |
| **30** | [[Stage-5_Specialized#Module 30: Proof of Work & Career Portfolio\|Proof of Work & Career Portfolio]] — Certs, GitHub, Bug Bounties | 🔴 | Specialized | 4–6 wks |
|  | **— [[Stage-5_Specialized#🏁 Final Gate — Mastery & Career Validation\|Final Gate]] —** *(custom C2 in lab, published AI security research, 3+ reports, OSCP)* |  |  | **~15–22 wks** |

> **Total realistic estimate: ~10–14 months** of consistent daily sessions. Drift, passive reading instead of lab time, or skipping stage gates will stretch this significantly.

---

## 🗺️ Topics — Mapped to Execution Order

> Comprehensive topic breakdown mapped directly to the execution order across all 5 stages.

---

### 🔵 STAGE 1 — FOUNDATION
*Modules 01–07 · ~2–3 months*

|     #     | Module                                                                                     | Category / Domain                | Core Concepts & Technical Scope                                                                                                                                                                                     | Key Tools & Standards                                    |
| :-------: | ------------------------------------------------------------------------------------------ | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
|  **01**   | [[Stage-1_Foundation#Module 01: Fundamentals\|Fundamentals]]                               | **Hardware**                     | CPU Architecture (`x86/x64`, `ARM/ARM64`), CPU Registers, Instruction Sets, RAM, Cache hierarchies, Storage (`HDD/SSD/NVMe`), BIOS, UEFI, TPM 2.0, Secure Boot, DMA, I/O, PCIe, USB, Firmware, Embedded Controllers | `x86_64`, `ARM64`, UEFI, TPM 2.0                         |
|           |                                                                                            | **OS Internals & Arch**          | Memory Addressing, Virtual & Physical Memory, Stack & Heap internals, Pointers, Processes, Threads, Context Switching, Interrupts, System Calls, Privilege Rings (`User Mode` vs `Kernel Mode`), IPC                | POSIX, Win32 API, C                                      |
|           |                                                                                            | **Data & Logic**                 | Hexadecimal, Binary, ASCII, Unicode, Endianness (Big vs Little Endian), Bitwise Operations (AND, OR, XOR, NOT, Shifts), Two's Complement, Integer Overflows & Sign Issues                                           | Hex editors, Python 3                                    |
|           |                                                                                            | **Physical & Mobile**            | USB Architecture & HID Attacks, Serial Communication, Bluetooth & NFC fundamentals, Mobile OS Sandbox Models (Android vs iOS), APK / IPA application structures                                                     | ADB, Wireshark, Hardware analyzers                       |
|  **02**   | [[Stage-1_Foundation#Module 02: Linux Administration\|Linux Administration]]               | **Internals & Processes**        | Linux Kernel, Processes, Threads, Syscalls, Signals, File Descriptors, Sockets, Pipes, IPC, Virtual Filesystems (`/proc`, `/sys`, `/dev`), Critical Directories (`/tmp`, `/var`, `/etc`)                            | `bash`, `strace`, `ltrace`, `gdb`                        |
|           |                                                                                            | **Security Model & Access**      | Users, Groups, File Permissions (rwx, octal), POSIX ACLs, Linux Capabilities, `SUID` / `SGID`, Sticky bit, `sudo` policy & sudoers configuration, Namespaces, `cgroups`, MAC (`SELinux`, `AppArmor`)                | `lsof`, `ss`, `ps`, `top`, `getfacl`                     |
|           |                                                                                            | **Networking & Storage**         | Network interfaces, Routing tables, Firewalling (`iptables`, `nftables`, `ufw`), Disk partitioning, Mount points, Inodes, LVM, Swap, Filesystems (ext4, XFS, Btrfs)                                                 | `ip`, `ss`, `iptables`, `fdisk`, `lsblk`                 |
|           |                                                                                            | **Services & Logging**           | `systemd` unit lifecycle, Timers, Cron jobs, SSH daemon configuration & hardening, Syslog, Journald, Log monitoring, Auditd basics                                                                                  | `systemctl`, `journalctl`, OpenSSH, `logrotate`          |
|  **03**   | [[Stage-1_Foundation#Module 03: Windows Administration\|Windows Administration]]           | **Architecture & Subsystems**    | Win32 API, Windows NT Kernel, Processes, Threads, DLLs, Handles, Access Tokens, Services, Registry hives (HKLM, HKCU), NTFS & ACLs/DACLs, Named Pipes, WMI, COM, RPC                                                | Sysinternals (`Procmon`, `Process Explorer`, `Autoruns`) |
|           |                                                                                            | **Authentication & Identity**    | NTLM, Kerberos, Windows Hello, Credential Providers, LSASS architecture, SAM database, LSA Secrets, DPAPI, Local Accounts vs Domain Accounts                                                                        | Mimikatz, Rubeus, LSASS, `klist`                         |
|           |                                                                                            | **Security Controls & Logs**     | UAC, Windows Defender, Windows Firewall, AppLocker, WDAC, AMSI, ETW, Security Event Logs (Event IDs 4624, 4625, 4672, 4688), Local Security Policies, GPO                                                           | Event Viewer, Group Policy Editor, Sysmon                |
|           |                                                                                            | **PowerShell & Admin**           | PowerShell Core (7+), Cmdlets, Pipeline, Remote Management (`WinRM`), PowerShell Script Block Logging, Constrained Language Mode (CLM), Automation scripts                                                          | PowerShell 7+, WinRM, PSReadLine                         |
|  **04**   | [[Stage-1_Foundation#Module 04: Networking Fundamentals\|Networking Fundamentals]]         | **Physical & Data Link (L1–L2)** | Ethernet frames, MAC addressing, CSMA/CD, Switches, VLANs, 802.1Q trunking, STP, ARP protocol, ARP cache poisoning, Collision & Broadcast domains                                                                   | Wireshark, `tcpdump`, `arp`, `macchanger`                |
|           |                                                                                            | **Network & Transport (L3–L4)**  | IPv4 & IPv6 addressing, Subnetting (CIDR, VLSM), Routing protocols (OSPF, BGP, RIP), NAT, ICMP; TCP 3-way handshake, Flags (SYN, ACK, FIN, RST, PSH, URG), Flow control, Windowing, UDP                             | `traceroute`, `ping`, `ipcalc`, Scapy                    |
|           |                                                                                            | **Application Layer (L7)**       | DNS resolution & records (A, AAAA, MX, TXT, PTR, NS, SOA, SRV), DHCP lease process (DORA), HTTP/HTTPS, FTP, SSH, SMTP, POP3, IMAP, SNMP, NTP, RDP, SMB                                                              | `dig`, `nslookup`, `curl`, `nc`, `nmap`                  |
|           |                                                                                            | **Perimeter & Packet Analysis**  | Perimeter Firewalls (Stateful vs Stateless), Proxies, NAT gateways, IDS/IPS concepts, Deep Packet Inspection (DPI), Network baselines, PCAP analysis                                                                | Wireshark, `tshark`, `tcpdump`, NetworkMiner             |
|  **05**   | [[Stage-1_Foundation#Module 05: Cryptography\|Cryptography]]                               | **Core Concepts & Symmetric**    | Symmetric Encryption (AES, ChaCha20, DES/3DES), Block Ciphers, Stream Ciphers, Cipher Modes (ECB, CBC, CTR, GCM), Hashes (MD5, SHA-1, SHA-256, SHA-3), HMAC, Salt, IV, Nonce                                        | `openssl`, Python `cryptography`, CyberChef              |
|           |                                                                                            | **Asymmetric & PKI**             | Asymmetric Encryption (RSA, ECC, Diffie-Hellman, ECDH, DSA, Ed25519), Digital Signatures, PKI, Certificate Authorities (CA), X.509 certificates, CRL, OCSP, TLS 1.2/1.3 Handshake                                   | `openssl`, `certutil`, `gpg`                             |
|           |                                                                                            | **Attacks & Data Protection**    | Known Plaintext, Padding Oracle attacks, Length Extension, Collision attacks, Passwords at rest (`bcrypt`, `scrypt`, `Argon2`, PBKDF2), Post-Quantum Cryptography (PQC: Kyber, Dilithium)                           | `hashcat`, `john`, `padding-oracle-attacker`             |
|  **06**   | [[Stage-1_Foundation#Module 06: Authentication Standards\|Authentication Standards]]       | **Sessions & Passwords**         | Password Authentication policies, Salted hashing, Session lifecycle (creation, timeout, termination), Cookie security flags (HttpOnly, Secure, SameSite), Session fixation, Session hijacking                       | Browser DevTools, Burp Suite, Python                     |
|           |                                                                                            | **Token & Modern Standards**     | JWT Architecture (Header, Payload, Signature), JWS, JWE, Token algorithms, Claims validation, Expiration, Refresh tokens, Token revocation, Passkeys (FIDO2, WebAuthn), Biometrics                                  | `jwt.io`, `jwt_tool`, FIDO2 testbeds                     |
|           |                                                                                            | **Federation & MFA**             | OAuth 2.0 roles & grant types (Auth Code, PKCE, Client Credentials), OpenID Connect (OIDC), SAML 2.0 SSO, MFA types (SMS, TOTP, Push, FIDO hardware keys) & bypasses                                                | OAuth Playground, Keycloak, Burp Suite                   |
|  **07**   | [[Stage-1_Foundation#Module 07: Web Technology Fundamentals\|Web Technology Fundamentals]] | **HTTP & Web Protocols**         | HTTP/1.1, HTTP/2, HTTP/3 (QUIC), Methods (GET, POST, PUT, DELETE, PATCH, OPTIONS, HEAD), Status codes, Request/Response headers, URL structure & encoding, WebSockets, Webhooks                                     | `curl`, Postman, Browser DevTools                        |
|           |                                                                                            | **Browser Security Model**       | Same-Origin Policy (SOP), Cross-Origin Resource Sharing (CORS), Content Security Policy (CSP), Web Security Headers (HSTS, X-Content-Type-Options, X-Frame-Options), DOM internals, Web Storage                     | Chrome DevTools, Burp Suite                              |
|           |                                                                                            | **Modern Web Architecture**      | REST APIs, JSON/XML parsing, Single Page Applications (SPAs), Server-Side Rendering (SSR), Microservices, Reverse Proxies (Nginx), CDNs, WAF fundamentals, Service-to-Service auth                                  | Docker, Nginx, Node.js / Python                          |
| **01–07** | **Programming Track** *(Weekend Track)*                                                    | **Scripting & Tooling**          | Python, Bash, PowerShell, C/C++, Go, Rust; syntax, data structures, regex, OOP, system APIs, CLI authoring                                                                                                          | Python 3, Bash, PowerShell, GCC/Clang, Go, Rust          |
|           |                                                                                            | **Security Domains**             | Socket programming, Network packet manipulation, Custom port scanners, HTTP requests & API clients, Web scrapers, Log parsers, Exploit PoC development, Memory analysis                                             | Scapy, Requests, BeautifulSoup, `pwntools`               |

---

### 🟠 STAGE 2 — OFFENSE I
*Modules 08–13 · ~5–6 weeks*

| # | Module | Category / Domain | Core Concepts & Technical Scope | Key Tools & Standards |
|:--:|--------|-------------------|---------------------------------|-----------------------|
| **08** | [[Stage-2_Offense-I#Module 08: Footprinting & Reconnaissance\|Footprinting & Reconnaissance]] | **OSINT & Passive Recon** | Search engine dorking (Google, Bing), WHOIS databases, DNS records, ASN mapping, IP blocks & CIDR, Certificate Transparency logs, Job postings, Code repos, Tech stack discovery | `subfinder`, `assetfinder`, `amass`, `httpx`, `shodan`, `censys`, `crt.sh` |
| | | **Active Recon & Intelligence** | DNS zone transfers, Subdomain brute-forcing, Web crawler discovery, Metadata harvesting (FOCA, Exif), Web technology fingerprinting, IPv6 discovery, Dark Web breach data reconnaissance | `dig`, `dnsenum`, `wafw00f`, `whatweb`, `theHarvester`, `exiftool` |
| **09** | [[Stage-2_Offense-I#Module 09: Scanning\|Scanning]] | **Host Discovery & Topology** | ARP ping sweeps, ICMP discovery (Echo, Timestamp, Subnet mask), TCP SYN/ACK discovery sweeps, UDP sweeps, Network boundary mapping | `nmap`, `fping`, `masscan`, `netdiscover`, `arp-scan` |
| | | **Port & Service Scanning** | TCP Connect (`-sT`), SYN Stealth (`-sS`), UDP scanning (`-sU`), Null, FIN, Xmas scans, Full port ranges (`-p-`), Service version detection (`-sV`), OS fingerprinting (`-O`) | `nmap`, `masscan`, `naabu`, `rustscan` |
| | | **Defense Assessment & Evasion** | Fragmented packets, Decoy scanning (`-D`), Source port spoofing, Timing templates (`-T0` to `-T5`), Firewall/IDS detection, NSE vulnerability scanning scripts | `nmap` (NSE), Scapy, `hping3` |
| **10** | [[Stage-2_Offense-I#Module 10: Enumeration\|Enumeration]] | **SMB, RPC & NetBIOS** | Null sessions, SMB shares, Permissions, Users, Groups, Password policies, NetBIOS names, RPC endpoints & interfaces | `enum4linux-ng`, `smbclient`, `netexec`, `rpcclient`, `smbmap` |
| | | **Network Services & Directory** | SNMP MIB walking (v1/v2c/v3 communities), SMTP user enumeration (VRFY, EXPN, RCPT TO), LDAP queries, Active Directory base enumeration, DNS enumeration, NFS exports | `snmpwalk`, `onesixtyone`, `smtp-user-enum`, `ldapsearch`, `showmount` |
| | | **Web & App Enumeration** | HTTP banner grabbing, Web server extensions, Virtual host (`vhost`) discovery, Hidden directories & files, API endpoints, Enumeration OPSEC & traffic analysis | `gobuster`, `ffuf`, `feroxbuster`, `nikto`, `curl` |
| **11** | [[Stage-2_Offense-I#Module 11: Database Security\|Database Security]] | **SQL Databases** | MySQL, PostgreSQL, Microsoft SQL Server (`MSSQL`), Oracle, SQLite; In-band, Error-based, Union-based, Blind Boolean/Time-based SQLi, `xp_cmdshell`, `UDF`, `INTO OUTFILE` | `sqlmap`, `dbeaver`, native DB CLIs |
| | | **NoSQL & Cache** | MongoDB injection & operator abuse, Redis unauthenticated command execution (SSH key drop, webshell drop), Elasticsearch API exploitation | `nosqlmap`, `redis-cli`, `curl` |
| | | **PrivEsc & Hardening** | Database privilege escalation, DBA role abuse, Trust links, Data encryption at rest/transit, DB auditing, Hardening baselines | Native DB CLIs, Audit scripts |
| **12** | [[Stage-2_Offense-I#Module 12: Password Cracking & Hash Analysis\|Password Cracking & Hash Analysis]] | **Hash Analysis & Acquisition** | Identifying hash algorithms, Salted hashes, Windows NTLM & LM, Kerberos tickets (krb5tgs, krb5asrep), Linux `/etc/shadow`, Database hashes, Archive hashes (Zip, Rar) | `hash-identifier`, `hashid`, Name-That-Hash |
| | | **Cracking Methodology** | Dictionary attacks, Brute-force, Hybrid attacks, Mask attacks, Rule-based cracking (best64, custom rules), Wordlist curation & mutation, Secrets extraction (SAM, LSASS, NTDS.dit) | `hashcat`, `john`, `cewl`, `cupp`, `secretsdump.py` |
| | | **Protocol & Online Attacks** | Online brute-force attacks, Password spraying (SMB, SSH, RDP, FTP, HTTP), Lockout policy handling; Protocol cracking (NetNTLMv1/v2, WPA2/WPA3 4-way handshake, PMKID) | `hydra`, `medusa`, `crowbar`, `aircrack-ng` |
| **13** | [[Stage-2_Offense-I#Module 13: System Hacking & Initial Compromise\|System Hacking & Initial Compromise]] | **Initial Access & Payloads** | Vulnerability exploitation, Metasploit Framework, Exploit-DB PoCs, Custom exploit modification, Reverse shells, Bind shells, Web shells, Staged vs Stageless payloads, Handlers | `msfconsole`, `msfvenom`, `nc`, `socat`, `revshells.com` |
| | | **Linux PrivEsc** | `SUID` / `SGID` binary abuse, `sudo -l` privileges & CVEs, Linux Capabilities (`cap_setuid`), Vulnerable Cron jobs, Systemd services, `$PATH` hijacking, Kernel exploits | `linpeas.sh`, `GTFOBins`, `pspy`, `unix-privesc-check` |
| | | **Windows PrivEsc** | Service misconfigurations (Unquoted paths, weak permissions), Registry autoruns, AlwaysInstallElevated, Token impersonation (`SeImpersonate`), UAC bypasses, DLL hijacking, Kernel exploits | `winpeas.exe`, `Seatbelt`, `PowerUp`, `SharpUp`, `JuicyPotato` |
| | | **Persistence & Lateral Move** | Persistence mechanisms (SSH keys, cron, registry, services, scheduled tasks), Living off the Land (LOLBAS / GTFOBins), Timestomping, Log clearing, Staging & data exfiltration | LOLBAS, PowerShell, Impacket suite |

---

### 🟣 STAGE 3 — WEB & APP SEC
*Modules 14–18 · ~8–10 weeks*

| # | Module | Category / Domain | Core Concepts & Technical Scope | Key Tools & Standards |
|:--:|--------|-------------------|---------------------------------|-----------------------|
| **14** | [[Stage-3_Web-and-App-Sec#Module 14: Web Application Hacking\|Web Application Hacking]] | **OWASP Top 10 Exploitation** | SQL Injection, Cross-Site Scripting (`XSS` — Stored/Reflected/DOM), `SSRF`, `XXE`, `BOLA` / `IDOR`, Path Traversal / LFI / RFI, Command Injection, Insecure Deserialization, `SSTI`, Access Control | Burp Suite Pro, OWASP ZAP, `sqlmap`, `ffuf`, `commix` |
| | | **Modern Web Attacks** | HTTP Request Smuggling (CL.TE, TE.CL, TE.TE), Web Cache Poisoning & Deception, Host Header attacks, HTTP Desync, Client-side Prototype Pollution, Race Conditions, Logic flaws | Turbo Intruder, HTTP Request Smuggler |
| | | **Post-Exploit & Defense** | Webshell deployment, Database pivoting, Server persistence, Defense mechanisms, WAF bypass techniques, Input validation, Content Security Policy (`CSP`) | Antak, Weevely, WAFW00F, Custom scripts |
| **15** | [[Stage-3_Web-and-App-Sec#Module 15: Session Hijacking & Token Attacks\|Session Hijacking & Token Attacks]] | **Session Architecture** | Session generation entropy, Session fixation, Predictable session IDs, Cookie security attributes (`HttpOnly`, `Secure`, `SameSite=Strict/Lax/None`), Session termination flaws | Burp Sequencer, Cookie Editor, DevTools |
| | | **Token Theft & Forgery** | XSS token theft, MITM session hijacking, Cross-Site WebSocket hijacking; JWT exploitation: `none` algorithm, weak HMAC secrets, Algorithm confusion, `kid` / `jku` header injection, Token replay | `jwt_tool`, Burp Suite, Wireshark |
| **16** | [[Stage-3_Web-and-App-Sec#Module 16: Web Server Hacking\|Web Server Hacking]] | **Server Recon & Misconfig** | Web server footprinting (Apache, Nginx, IIS, Tomcat), HTTP verb tampering, Default credentials, Unprotected admin interfaces, Exposed source control (`.git`), Backup files | `nikto`, `whatweb`, `git-dumper`, `ffuf` |
| | | **Server Exploitation** | Directory traversal, Server-Side Code Execution, Apache path traversal (CVE-2021-41773), Nginx alias traversal, Tomcat Manager WAR deployment, IIS short filename vulnerability | Metasploit, `davtest`, `cadaver`, Exploit-DB PoCs |
| **17** | [[Stage-3_Web-and-App-Sec#Module 17: API Security\|API Security]] | **REST APIs & OWASP API Top 10** | API reconnaissance, Swagger / OpenAPI parsing, `BOLA`, `BOPLA`, `BFLA`, Unrestricted resource consumption, Mass assignment, Security misconfigurations, Verbose error handling | Postman, `kiterunner`, `mitmproxy`, `arjun`, `ffuf` |
| | | **GraphQL & Modern Protocols** | GraphQL introspection, Query depth & complexity exhaustion, Batching attacks, Field suggestions; gRPC endpoint enumeration, WebSockets vulnerabilities, API Gateway bypasses | InQL, GraphQL Raider, Altair, `grpc_cli` |
| | | **API Auth & Hardening** | API Key exposure, OAuth 2.0 grant vulnerabilities, OpenID Connect token verification, JWT authentication bypasses in APIs, Rate limiting & WAF bypasses | Burp Suite, OAuth Playground, `jwt_tool` |
| **18** | [[Stage-3_Web-and-App-Sec#Module 18: Bug Bounty Methodology\|Bug Bounty Methodology]] | **Scoping & Wide Recon** | Bug bounty platform dynamics (HackerOne, Bugcrowd, Intigriti), Rules of Engagement, Wide-scope reconnaissance, ASN & CIDR enumeration, Subdomain takeovers, GitHub dorking | `subfinder`, `amass`, `nuclei`, `subjack`, `trufflehog` |
| | | **Chaining & Professional Triage** | Low-severity to High/Critical chaining, Business logic exploitation, Account takeover chains, Proof of Concept creation, CVSS calculation, Professional triager communication | Markdown report templates, Burp Suite Pro |
| | [[Stage-3_Web-and-App-Sec#Side-Track A: Detection Engineering & SOC Operations\|Side-Track A: Detection Engineering & SOC]] *(Parallel Track)* | **Defensive Architecture & Telemetry** | Enterprise defense models, Network & Host telemetry, Sysmon event logging, Windows Security Events, Linux Auditd, EDR/XDR architecture, SIEM data ingestion & normalization | Sysmon, Velociraptor, Elastic Agent, Wazuh |
| | | **Detection Engineering & Hunting** | Detection rules authoring, Sigma rules, YARA rules, MITRE ATT&CK mapping, Hypothesis-driven threat hunting, Alert triage & SOC workflows, Incident response fundamentals | Sigma, YARA, Splunk, Elastic SIEM |
| | [[Stage-3_Web-and-App-Sec#Side-Track B: IDS, Firewalls, and Honeypots\|Side-Track B: IDS, Firewalls, and Honeypots]] *(Parallel Track)* | **Network Defenses & Deception** | Stateful vs Stateless firewalls, Linux `nftables` / `iptables`, pfSense / OPNsense, Suricata & Snort IDS/IPS rule writing, Evasion detection, Honeypots & deception, Email & DNS security | Suricata, Snort, Cowrie, pfSense, Wireshark |
| | [[Stage-3_Web-and-App-Sec#Side-Track C: Cyber Threat Intelligence (CTI) & Attack Surface Management\|Side-Track C: CTI & Attack Surface Management]] *(Parallel Track)* | **Threat Intel & EASM** | External Attack Surface Management, Threat actor profiling, IOCs & IOAs, Threat intelligence feeds, CTI platforms, MITRE ATT&CK & Diamond Model analysis, Intel operationalization | MISP, OpenCTI, Maltego, SpiderFoot |

---

### 🏢 STAGE 4 — ENTERPRISE
*Modules 19–26 · ~10–13 weeks*

| # | Module | Category / Domain | Core Concepts & Technical Scope | Key Tools & Standards |
|:--:|--------|-------------------|---------------------------------|-----------------------|
| **19** | [[Stage-4_Enterprise#Module 19: Active Directory & Entra ID\|Active Directory & Entra ID]] | **AD Architecture & Enumeration** | Forests, Domains, Trees, Trusts, Domain Controllers, Global Catalogs, Schema, GPOs, OUs; PowerView & BloodHound graph analysis, LDAP enumeration, Domain querying | BloodHound / SharpHound, PowerView, `ldapsearch`, `netexec` |
| | | **Kerberos & Credential Attacks** | Kerberos protocol (AS-REQ/REP, TGS-REQ/REP, AP-REQ), Kerberoasting, AS-REP Roasting, Pass-the-Hash (`PtH`), Pass-the-Ticket (`PtT`), Overpass-the-Hash, Silver & Golden Tickets | Rubeus, Mimikatz, Impacket (`GetUserSPNs.py`, `secretsdump.py`) |
| | | **ACLs, Delegation & ADCS Abuse** | GenericAll, WriteDacl, GenericWrite abuse; Unconstrained, Constrained, and Resource-Based Constrained Delegation (`RBCD`); Active Directory Certificate Services (`ADCS`) ESC1–ESC8 | Certify, PKINITtools, BloodHound, PowerView |
| | | **Lateral Movement & Persistence** | DCSync attack, DCShadow, Skeleton Key, DSRM credential abuse, AdminSDHolder persistence, GPO backdoors, WMI & WinRM execution, DCOM execution, Remote Registry | Mimikatz, Impacket (`wmiexec.py`, `psexec.py`), Evil-WinRM |
| | | **Entra ID (Azure AD) & Hybrid** | Azure AD Connect exploitation, Password Hash Sync, ADFS attacks, Seamless SSO abuse, Primary Refresh Token (`PRT`) abuse, Hybrid identity attacks, Azure RBAC privilege escalation | AADInternals, ROADtools, Azure CLI, MicroBurst |
| **20** | [[Stage-4_Enterprise#Module 20: Cloud Computing\|Cloud Security]] | **Cloud Architecture & IAM** | AWS, Azure, GCP models, Shared responsibility, Cloud root boundaries; IAM Policies, Roles, Groups, Service Accounts, AssumeRole, Cross-account access, STS tokens | AWS CLI, Azure CLI, gcloud, Pacu |
| | | **Storage, Compute & Metadata** | S3 buckets, Azure Blob, GCS permissions, Public exposure analysis; EC2, Azure VMs; Instance Metadata Service (IMDSv1 vs IMDSv2), Metadata theft via SSRF, Cloud IaC | `s3scanner`, Pacu, ScoutSuite, Prowler |
| | | **Exploitation & Persistence** | Privilege escalation vectors in AWS/Azure, Shadow admins, IAM backdoor persistence, Serverless (Lambda/Functions) attacks, CloudTrail evasion, Cloud posture auditing | Pacu, Prowler, ScoutSuite, CloudSploit |
| **21** | [[Stage-4_Enterprise#Module 21: Container & Orchestration Security\|Containers & Kubernetes]] | **Container Internals & Escapes** | Docker engine architecture, Linux namespaces (PID, Mount, Net, IPC, User), `cgroups`, Docker daemon socket exposure, Privileged containers, Capabilities abuse, Container breakout | Docker CLI, `deepce`, `cdk-go`, `amicontained` |
| | | **Kubernetes Security & Attacks** | K8s architecture (API Server, Kubelet, etcd, Controller Manager), Anonymous kubelet access, etcd credential dumping, Pod service account tokens (`JWT`), RBAC misconfigs, PrivEsc | `kubectl`, `kube-hunter`, `kube-bench`, `peirates` |
| | | **Runtime, CI/CD & Hypervisors** | Container runtime security (runc, containerd), AppArmor/Seccomp, Image scanning; CI/CD security (GitHub Actions poisoning, Jenkins RCE, pipeline secrets); Hypervisor escape concepts | Trivy, Grype, Falco, Semgrep |
| **22** | [[Stage-4_Enterprise#Module 22: Adversary Emulation & Purple Teaming\|Adversary Emulation]] | **MITRE ATT&CK & Emulation** | ATT&CK matrix (Tactics, Techniques, Procedures), Navigator heatmaps, Threat actor profiling (APT29, FIN7), Emulation plans, Atomic Red Team execution, Automated emulation platforms | MITRE ATT&CK Navigator, Atomic Red Team, Caldera, Prelude Operator |
| | | **Purple Teaming & Metrics** | Collaborative offensive-defensive exercises, Detection gap analysis, EDR alert validation, Log coverage assessment, Security posture metrics (MTTD, MTTR), Purple team reporting | VECTR, Sigma, Sysmon, Elastic SIEM |
| **23** | [[Stage-4_Enterprise#Module 23: Sniffing & Spoofing\|Lateral Movement & Sniffing]] | **Sniffing & Traffic Interception**| Promiscuous mode, Raw sockets, Passive network sniffing, Cleartext credential extraction (FTP, HTTP, Telnet, SNMP), Network protocol dissection, Wireshark display filters | Wireshark, `tshark`, `tcpdump`, `dsniff` |
| | | **Spoofing, MITM & Poisoning** | ARP cache poisoning, DNS spoofing, DHCP starvation & rogue DHCP, LLMNR & NBT-NS poisoning, WPAD spoofing, NTLM relaying, SSL stripping, Network MITM defenses | `responder`, `bettercap`, `ettercap`, `mitmproxy`, `ntlmrelayx.py` |
| **24** | [[Stage-4_Enterprise#Module 24: Social Engineering\|Social Engineering]] | **Psychology & Target Profiling** | Principles of influence (Authority, Scarcity, Urgency, Reciprocity, Social Proof), OSINT target profiling, Organizational charts, Corporate email naming conventions, Relationship mapping | LinkedIn, Maltego, theHarvester, Hunter.io |
| | | **Delivery Vectors & Physical** | Spear-phishing campaigns, Phishing infrastructure setup (SMTP, Lookalike domains, SPF/DKIM/DMARC, Reverse proxies), Credential harvesting, Vishing, Smishing, USB drops, Physical access | GoPhish, Evilginx2, SET, Modlishka |
| **25** | [[Stage-4_Enterprise#Module 25: Malware & Weaponization (Conceptual)\|Malware & C2 Architectures]] | **Architecture & Staging** | Droppers, Downloaders, Stagers, Full-stage payloads, C2 beacon mechanics, Communication channels (HTTP, HTTPS, DNS, SMB), Heartbeats, Jitter, Malleable C2 profiles | Sliver, Mythic, Cobalt Strike concepts |
| | | **Execution & Evasion Mechanisms**| Process injection (CreateRemoteThread, Process Hollowing, APC Queue), DLL injection, Syscalls vs Win32 APIs, AMSI & ETW bypass concepts, Obfuscation, Persistence, Counter-forensics | Conceptual code, x64dbg, PE-bear, Process Hacker |
| | | **Artifacts & Memory Forensics** | Memory analysis concepts, Volatility framework, Identifying injected code, Malfind, Memory artifacts, Document weaponization (Macros, LNK files, ISO/VHD packaging) | Volatility 3, CyberChef, OLETools |
| **26** | [[Stage-4_Enterprise#Module 26: Pentest Methodologies & Report Writing\|Pentest Reporting]] | **Frameworks, Scoping & Legal** | Penetration testing execution standards (PTES, NIST SP 800-115, OWASP Web Testing Guide, OSSTMM), Rules of Engagement (RoE), NDA, Scoping boundaries, Legal compliance & liability | Engagement checklists, PTES guidelines |
| | | **Threat Modeling & Risk Scoring** | Threat modeling methodologies (STRIDE, PASTA, DREAD), Vulnerability scoring (CVSS v3.1 / v4.0 metrics, Base/Temporal/Environmental scores), EPSS, Business risk contextualization | FIRST CVSS Calculator, Threat Modeling tools |
| | | **Technical Delivery & Reports** | Professional pentest report structure: Executive Summary, Methodology, Scope, Detailed Technical Findings, Reproduction Steps, Risk Matrix, Root Cause Analysis, Remediation Roadmaps | Markdown / LaTeX report templates, Typora, Git |

---

### 🔬 STAGE 5 — SPECIALIZED
*Modules 27–30 · ~15–22 weeks*

| # | Module | Category / Domain | Core Concepts & Technical Scope | Key Tools & Standards |
|:--:|--------|-------------------|---------------------------------|-----------------------|
| **27** | [[Stage-5_Specialized#Module 27: Offensive Development & Tooling\|Offensive Development]] | **Systems Programming Foundations**| C & C++ for security practitioners, Pointers, Memory allocation, Stack/Heap internals, Win32 API, Native APIs (NTDLL), Direct Syscalls, Assembly (x86/x64), Linux POSIX system calls | GCC/Clang, Visual Studio, MSVC, x64dbg, Ghidra |
| | | **Exploit Dev & Windows OffSec** | Stack-based buffer overflows, Shellcode writing & encoding, Bad characters, Bypassing DEP/NX with ROP chains, ASLR bypasses; Process injection, Direct syscalls, PE parsing, EDR unhooking, AMSI/ETW patching | `pwntools`, Mona.py, x64dbg, Visual Studio |
| | | **Linux OffSec Dev & C2 Implants**| Linux ELF binary manipulation, Custom LD_PRELOAD hooks, ptrace injection, Rootkit concepts; Custom C2 implant architecture in Go/Rust/C++, Encrypted communications, Sleep obfuscation, Task execution queue | GCC, Go, Rust, Wireshark |
| **27** | **Reverse Engineering** *(Parallel Track)* | **Binary Formats & Disassembly** | PE (Portable Executable), ELF, Mach-O, DLLs, Shared Libraries, Control Flow Analysis, Data Flow Analysis, API Analysis, Strings, Imports/Exports; x86, x64, ARM, ARM64 architectures | `ghidra`, `ida-pro`, `binary-ninja`, `radare2` |
| | | **Analysis, Debugging & Evasion** | Dynamic debugging, Packing, Code Obfuscation, Anti-Debugging, Anti-VM, Control Flow Flattening, Binary Patching, Hooking, Runtime Analysis | `x64dbg`, `windbg`, PEview, Hex Editors |
| **27** | **Fuzzing & Vuln Research** *(Parallel Track)* | **Fuzzing Mechanics** | Black-Box, White-Box, Grey-Box Fuzzing, Mutation-Based vs Generation-Based Fuzzing, Coverage-Guided Fuzzing, Protocol Fuzzing, File Format Fuzzing, API Fuzzing, Binary Fuzzing, Crash Triage, Sanitizers (`ASan`, `MSan`, `UBSan`) | `afl++`, `libfuzzer`, `honggfuzz`, `boofuzz` |
| | | **Vuln Research & Code Audit** | Attack Surface Research, Bug Discovery, Root Cause Analysis, Variant Analysis, Patch Diffing, Memory Corruption, Logic Bugs, Supply Chain Vulnerabilities, SAST, Secure Code Review | `semgrep`, `ghidra`, BinDiff, Wireshark |
| **28** | [[Stage-5_Specialized#Module 28: AI & LLM Red Teaming\|AI & LLM Red Teaming]] | **AI Foundations & LLM Vulns** | Machine Learning, Transformers, LLM architecture, Tokenization, Embeddings, Vector databases, Retrieval-Augmented Generation (`RAG`); OWASP Top 10 for LLMs, Direct & Indirect Prompt Injection, Jailbreaks, System Prompt extraction | LangChain, LlamaIndex, OpenAI / Anthropic APIs, `garak`, `pyrit` |
| | | **Agent Security & Adversarial ML**| AI Agent architecture, Tool / Function calling vulnerabilities, Excessive agency, Context poisoning, Memory injection, Model inversion, Training data poisoning, Adversarial perturbations, AI red team automation | Custom testbeds, NeMo Guardrails, Mindgard |
| **28** | **Modern Attack Surfaces** *(Parallel Track)* | **Cloud-Native & CI/CD Security**| Containers, Serverless, Service Mesh, API Ecosystems, Microservices, Zero Trust; Secure SDLC, Source Code Security, SAST/DAST/SCA, Secret Scanning, CI/CD Pipeline Security, Git Security, Container & IaC Security, SBOM, Supply Chain Attacks | Semgrep, Trivy, Cosign, Syft |
| | | **Web3 & Blockchain** | Blockchain Architecture, Ethereum & EVM, Solidity, Smart Contracts, Wallets, Tokens, DeFi Protocols, Oracles, Bridges, Signatures; Reentrancy, Access Control Flaws, Integer Issues, Oracle Manipulation, Flash Loans, Blockchain Forensics | `slither`, `mythril`, Foundry, Remix |
| | | **IoT & Embedded Systems** | Embedded Systems, Firmware Internals, Bootloaders, Hardware Interfaces (`UART`, `SPI`, `I2C`, `JTAG`), Hardware Debugging, Firmware Extraction, Firmware Analysis, Secure Boot Bypasses, Device Authentication | `binwalk`, Saleae Logic, JTAGulator |
| **29** | [[Stage-5_Specialized#Module 29: Red Team Operations & Tradecraft\|Red Team Operations]] | **Campaign Planning & Infra** | Threat actor emulation planning, Red team infrastructure setup (Redirectors, Long-haul vs Short-haul C2, Domain fronting/categorization, CDN routing), Malleable C2 profiles, Operational Security (`OPSEC`), Covert communications | Sliver, Mythic, Cobalt Strike, Nginx redirectors |
| | | **Execution & Lateral Movement** | Assumed-breach methodology, Credential access in hardened environments, Cross-forest pivoting, Low-and-slow data exfiltration, Deconfliction procedures with defensive teams, Executive debriefing & timeline reconstruction | Sliver, Impacket, BloodHound, Rubeus |
| **29** | **Defensive Awareness** *(Parallel Track)* | **DFIR & Incident Response** | Disk Forensics, Memory Forensics, Network Forensics, Evidence Preservation, Timeline Analysis, Incident Response Triage, Containment, Eradication, Recovery, Root Cause Analysis, IOC Analysis, Malware Investigation | `volatility`, `autopsy`, `ftk`, Wireshark |
| | | **SOC / SIEM / EDR & Hunting** | Detection Engineering, Alert Triage, Incident Investigation, SOC Workflows, Log Ingestion, Correlation Rules, Event Normalization, Alert Logic, Sigma Rules, Endpoint Detection, Behavioral Detection, Threat Hunting | Splunk, Elastic SIEM, Sigma rules, Sysmon, Velociraptor |
| **29** | **Intelligence** *(Parallel Track)* | **Threat Intelligence** | Threat Actors, Campaigns, Malware Families, Infrastructure, IOCs, IOAs, TTPs, Domains, IPs, Hashes, Infrastructure Correlation, Threat Attribution, Threat Intelligence Reports, MITRE ATT&CK Mapping | MISP, OpenCTI, MITRE ATT&CK |
| | | **OSINT & Dark Web Intel** | Search Intelligence, Domain & DNS Intelligence, Username & Email Intel, Public Records, Exif Metadata, Image & Video Geolocation, Breach Intelligence; Tor, Onion Services, Underground Markets, Cybercrime Ecosystems | `maltego`, `spiderfoot`, `shodan`, `censys`, Tor Browser |
| **30** | [[Stage-5_Specialized#Module 30: Proof of Work & Career Portfolio\|Proof of Work & Career]] | **Hands-on Proof & Labs** | Public portfolio construction, Hack The Box (`HTB`) Pro Labs writeups, TryHackMe (`THM`) milestones, PortSwigger Web Security Academy completions, VulnHub, Enterprise multi-cloud and AD lab demonstrations | HTB Pro Labs, PortSwigger Academy, GitHub |
| | | **Engagements, CVEs & Research** | Penetration Testing Methodologies, Scope Definition, RoE, Exploitation & Reporting; CVE Request & Coordinated Vulnerability Disclosure process, Vulnerability Reproduction, PoC development, Security Advisories | Mitre CVE program, GitHub Advisories, Exploit-DB |
| | | **Portfolio & Career Strategy** | Research Papers, Blog Posts, CVE Write-ups, Open Source Tool authoring & maintenance, Industry Certifications (OSCP, CPTS, CRTO, CISSP), Technical Interview & Whiteboard Defense preparation | GitHub, Medium / Substack, GitBook, LinkedIn |

---

## 📦 Shelf — Post-Hire Electives

> These aren't "later in the sequence" — they're off the sequence entirely until I have a job. No number means no claim on my time right now.

| # | Module | Focus Area |
|:-:|--------|------------|
| S01 | [[Shelf_Post-Hire#Shelf 01: Wireless Network Security\|Wireless Network Security]] | WPA2/WPA3, Evil Twin, PMKID |
| S02 | [[Shelf_Post-Hire#Shelf 02: Mobile Platform Pentesting\|Mobile Security]] | Android/iOS, Frida, MobSF, Pinning |
| S03 | [[Shelf_Post-Hire#Shelf 03: OT/ICS/SCADA Security\|OT / ICS / SCADA Security]] | Modbus, S7comm, Purdue model |
| S04 | [[Shelf_Post-Hire#Shelf 04: Digital Forensics\|Digital Forensics]] | Memory, Disk, Autopsy, Volatility |
| S05 | [[Shelf_Post-Hire#Shelf 05: Reverse Engineering & Malware Analysis\|Reverse Engineering & Malware Analysis]] | Ghidra, x64dbg, unpacking |
| S06 | [[Shelf_Post-Hire#Shelf 06: Modern Exploitation\|Modern Exploitation]] | Binary exploitation, ROP, ASLR/DEP |
| S07 | [[Shelf_Post-Hire#Shelf 07: Hardware Hacking & Embedded Systems\|Hardware Hacking & Embedded Systems]] | UART, JTAG, Firmware extraction |
| S08 | [[Shelf_Post-Hire#Shelf 08: Physical Penetration Testing\|Physical Penetration Testing]] | Lock picking, RFID cloning, bypass |
| S09 | [[Shelf_Post-Hire#Shelf 09: VoIP & Telecommunications Security\|VoIP & Telecommunications Security]] | SIP, RTP, SS7/5G concepts |
| S10 | [[Shelf_Post-Hire#Shelf 10: Blockchain & Web3 Security\|Blockchain & Web3 Security]] | Smart contract audits, reentrancy |
| S11 | [[Shelf_Post-Hire#Shelf 11: Governance, Risk & Compliance (GRC)\|Governance, Risk & Compliance]] | ISO 27001, SOC 2, NIST CSF |
| S12 | [[Shelf_Post-Hire#Shelf 12: Supply Chain Security\|Supply Chain Security]] | SBOM, Dependency confusion, SLSA |
| S13 | [[Shelf_Post-Hire#Shelf 13: DevSecOps & Secure SDLC\|DevSecOps & Secure SDLC]] | CI/CD pipelines, SAST/DAST, Semgrep |
| S14 | [[Shelf_Post-Hire#Shelf 14: Secure Code Review Methodology\|Secure Code Review Methodology]] | Code auditing, source-level vuln analysis |
| S15 | [[Shelf_Post-Hire#Shelf 15: Security Architecture & Engineering\|Security Architecture & Engineering]] | Zero Trust, threat modeling, STRIDE |
| S16 | [[Shelf_Post-Hire#Shelf 16: Security Operations Expansion\|Security Operations Expansion]] | SOAR, DLP, Insider threat |
| S17 | [[Shelf_Post-Hire#Shelf 17: Denial of Service & Availability Resilience\|Denial of Service & Resilience]] | Layer 4/7 mechanisms, Anycast, DDoS mitigation |
| S18 | [[Shelf_Post-Hire#Shelf 18: Automotive Security\|Automotive Security]] | CAN Bus, ECU, UDS, OBD-II, AUTOSAR SecOC |
| S19 | [[Shelf_Post-Hire#Shelf 19: Telecom Security\|Telecom Security]] | GSM/4G/5G, SS7, Diameter, IMSI Catcher, SIM internals |
| S20 | [[Shelf_Post-Hire#Shelf 20: Advanced Linux Internals\|Advanced Linux Internals]] | Kernel modules, eBPF, container escape, LKM rootkits |
| S21 | [[Shelf_Post-Hire#Shelf 21: Advanced Windows Internals\|Advanced Windows Internals]] | Token security, PPL, memory forensics, DKOM |

---

## ⏱️ Daily Protocol

> One question answered every morning: **"What is my current module and what am I proving today?"**

**1. Engineering Foundation**
Read the protocol or mechanism for my current topic. Write structured notes. Understand *why* it works before touching a tool.

**2. Lab Execution**
Terminal open. Wireshark running. Execute commands, capture output, break things. Never run a tool I cannot explain at the packet or system level.

**3. Artifact & Proof**
Save PCAP/log/screenshot. Write the 1-page lab summary. Git commit with a descriptive message. Check the Move-On Gate in the stage file.

### Hard Rules

1. **Never start with passive reading.** Peak energy belongs to the terminal, not a PDF.
2. **Never run a tool blindly.** If I can't explain what a flag does at the packet level — stop, read, then run.
3. **No writeup = learning didn't happen.** Every lab session gets a committed markdown file.
4. **Respect the Stage Gates.** Do not proceed until I can demonstrate the skill without notes.
5. **Git commit after every session.** If I haven't committed in 2 weeks, I'm drifting.

### Programming Track *(Weekends Only)*

| Stage | Language | Focus |
|:-----:|----------|-------|
| Foundation | Python, Bash, PowerShell | Scripting fundamentals, OS automation |
| Offense I | Python, Bash | Tool wrappers, log parsing, scan automation |
| Web & App Sec | Python, JavaScript | Web exploit PoCs, XSS weaponization |
| Enterprise | PowerShell, Python (Scapy) | AD enumeration, Impacket, packet fabrication |
| Specialized | C/C++, Assembly, PowerShell, Python | Shellcode, loaders, AMSI bypass, LLM harnesses |

---

## 🛠️ Lab Setup

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| RAM | 32 GB | 64 GB |
| CPU | Quad-core + VT-x/AMD-V | 8-core with nested virtualization |
| Storage | 500 GB SSD | 1 TB NVMe SSD |
| Wireless Adapter | — | Alfa AWUS036ACH (RTL8812AU, monitor mode + injection) |

**Core Lab Stack:**
- Kali Linux (attack machine)
- Windows Server VM (AD target — module #19)
- Ubuntu/Metasploitable VM (Linux target)
- [TryHackMe](https://tryhackme.com) · [Hack The Box](https://hackthebox.com) · [PortSwigger Web Academy](https://portswigger.net/web-security)

---

### 🧭 Roadmap Navigation

| 🏠 Root Portfolio | 🔵 Start Stage 1 | 🛠️ Tool Mastery Hub | ⬆ Return to Top |
|:---:|:---:|:---:|:---:|
| [🏠 Root README](../README.md) | [[Stage-1_Foundation\|Stage 1: Foundation ➔]] | [[Tools/README\|88 Tool Mastery Guides]] | [[#🛡️ Cybersecurity Master Roadmap\|⬆ Back to Top]] |

