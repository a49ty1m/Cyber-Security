# 🛡️ Cybersecurity Master Roadmap

> **Career Target:** Penetration Testing → Red Team Operations → Advanced Offensive Security → AI Red Teaming

---

## 📑 Table of Contents

| # | Section |
|:-:|---------|
| 1 | [Execution Order + Topics](#execution-order) ← **Start here** |
| 2 | [Shelf — Self Post-Hire](#shelf) |
| 3 | [Daily Protocol](#daily-protocol) |
| 4 | [Lab Setup](#lab-setup) |

---

<a id="execution-order"></a>

## 🎯 Execution Order — 5 Stages

> Sequential walk order across 5 Stages, top to bottom.
> 🔴 = master it before moving on · 🟡 = learn it solid, keep moving · 🔵 = conceptual foundation (hands-on build later in specialized stage)
> ⏱ Time spans assume consistent daily sessions per the [Daily Protocol](#daily-protocol).

| # | Module | Depth | Stage | Est. Time |
|:--:|--------|:-----:|-------|:---------:|
| **01** | [[Stage-1_Foundation#module-01-fundamentals\|Fundamentals]] — Hardware, OS, Memory, Data Rep, Programming | 🔴 | Foundation | 2–3 wks |
| **02** | [[Stage-1_Foundation#module-02-linux-administration\|Linux Administration]] | 🔴 | Foundation | 2–3 wks |
| **03** | [[Stage-1_Foundation#module-03-windows-administration\|Windows Administration]] | 🟡 | Foundation | 1–2 wks |
| **04** | [[Stage-1_Foundation#module-04-networking-fundamentals\|Networking Fundamentals]] | 🔴 | Foundation | 2–3 wks |
| **05** | [[Stage-1_Foundation#module-05-cryptography\|Cryptography]] — core concepts + attacks | 🔴 | Foundation | 1–2 wks |
| **06** | [[Stage-1_Foundation#module-06-authentication-standards\|Authentication Standards]] — Sessions, JWT, OAuth, MFA | 🔴 | Foundation | 1–2 wks |
| **07** | [[Stage-1_Foundation#module-07-web-technology-fundamentals\|Web Technology Fundamentals]] — HTTP, Cookies, CORS, REST | 🔴 | Foundation | 1–2 wks |
| | **— [[Stage-1_Foundation#foundation-proof-gate\|Foundation Proof Gate]] —** *(10 PCAPs, admin baselines, 3 scripts, lab report)* | | | **~2–3 mos** |
| **08** | [[Stage-2_Offense-I#module-08-footprinting--reconnaissance\|Footprinting & Reconnaissance]] | 🔴 | Offense I | 1–2 wks |
| **09** | [[Stage-2_Offense-I#module-09-scanning\|Scanning]] | 🔴 | Offense I | 1 wk |
| **10** | [[Stage-2_Offense-I#module-10-enumeration\|Enumeration]] | 🔴 | Offense I | 1–2 wks |
| **11** | [[Stage-2_Offense-I#module-11-database-security\|Database Security]] | 🟡 | Offense I | 1 wk |
| **12** | [[Stage-2_Offense-I#module-12-password-cracking--hash-analysis\|Password Cracking & Hash Analysis]] | 🔴 | Offense I | 1 wk |
| **13** | [[Stage-2_Offense-I#module-13-system-hacking--initial-compromise\|System Hacking & Initial Compromise]] | 🔴 | Offense I | 2–3 wks |
| | **— [[Stage-2_Offense-I#stage-gate-1\|Stage Gate 1]] —** *(root a box, dump & crack a hash, escalate privesc)* | | | **~5–6 wks** |
| **14** | [[Stage-3_Web-and-App-Sec#module-14-web-application-hacking\|Web Application Hacking]] — SQLi, XSS, SSRF, IDOR, XXE | 🔴 | Web & App Sec | 3–4 wks |
| **15** | [[Stage-3_Web-and-App-Sec#module-15-session-hijacking--token-attacks\|Session Hijacking & Token Attacks]] — Cookies, JWTs, Fixation | 🔴 | Web & App Sec | 1–2 wks |
| **16** | [[Stage-3_Web-and-App-Sec#module-16-web-server-hacking\|Web Server Hacking]] — Misconfig, Directory Traversal | 🔴 | Web & App Sec | 1–2 wks |
| **17** | [[Stage-3_Web-and-App-Sec#module-17-api-security\|API Security]] — OWASP API Top 10, REST/GraphQL/gRPC | 🔴 | Web & App Sec | 2 wks |
| **18** | [[Stage-3_Web-and-App-Sec#module-18-bug-bounty-methodology\|Bug Bounty Methodology]] — Scope, Recon, Exploit, Report | 🔴 | Web & App Sec | 2 wks |
| | *(parallel, absorb only — never block)* [[Stage-3_Web-and-App-Sec#side-track-a-detection-engineering--soc-operations\|Detection Awareness]], [[Stage-3_Web-and-App-Sec#side-track-b-ids-firewalls-and-honeypots\|IDS/Honeypots]], [[Stage-3_Web-and-App-Sec#side-track-c-cyber-threat-intelligence-cti--attack-surface-management\|OSINT]] | 🟡 | side-track | ongoing |
| | **— [[Stage-3_Web-and-App-Sec#stage-gate-2\|Stage Gate 2]] —** *(3+ HTB/THM writeups, OWASP Top 10 hands-on, Linux+Windows privesc demonstrated cold)* | | | **~8–10 wks** |
| **19** | [[Stage-4_Enterprise#module-19-active-directory--entra-id\|Active Directory & Entra ID]] *(+ deferred Kerberos patch from #03)* | 🔴 | Enterprise | 3–4 wks |
| **20** | [[Stage-4_Enterprise#module-20-cloud-computing\|Cloud Computing]] *(+ deferred Cloud Assets patch from #04)* | 🔴 | Enterprise | 2–3 wks |
| **21** | [[Stage-4_Enterprise#module-21-container--orchestration-security\|Container & Orchestration Security]] | 🟡 | Enterprise | 1–2 wks |
| **22** | [[Stage-4_Enterprise#module-22-adversary-emulation--purple-teaming\|Adversary Emulation & Purple Teaming]] | 🔴 | Enterprise | 2 wks |
| **23** | [[Stage-4_Enterprise#module-23-sniffing--spoofing\|Sniffing & Spoofing]] — ARP, MITM, Bettercap, Responder | 🟡 | Enterprise | 1 wk |
| **24** | [[Stage-4_Enterprise#module-24-social-engineering\|Social Engineering]] — Phishing, Vishing, Physical | 🟡 | Enterprise | 1 wk |
| **25** | [[Stage-4_Enterprise#module-25-malware--weaponization-conceptual\|Malware & Weaponization]] *(conceptual — full build is #27)* | 🔵 | Enterprise | 1 wk |
| **26** | [[Stage-4_Enterprise#module-26-pentest-methodologies--report-writing\|Pentest Methodologies & Report Writing]] | 🔴 | Enterprise | 1–2 wks |
| | **— [[Stage-4_Enterprise#stage-gate-3\|Stage Gate 3]] —** *(AD domain attacked end-to-end, BloodHound exports in Git, 1 professional report)* | | | **~10–13 wks** |
| **27** | [[Stage-5_Specialized#module-27-offensive-development--tooling\|Offensive Development & Tooling]] — C2, Shellcode, AMSI/ETW | 🔴 | Specialized | 4–6 wks |
| **28** | [[Stage-5_Specialized#module-28-ai--llm-red-teaming\|AI & LLM Red Teaming]] — Prompt Injection, RAG, Agentic Exploits | 🔴 | Specialized | 3–4 wks |
| **29** | [[Stage-5_Specialized#module-29-red-team-operations--tradecraft\|Red Team Operations & Tradecraft]] — C2, OPSEC, Campaign | 🔴 | Specialized | 4–6 wks |
| **30** | [[Stage-5_Specialized#module-30-proof-of-work--career-portfolio\|Proof of Work & Career Portfolio]] — Certs, GitHub, Bug Bounties | 🔴 | Specialized | 4–6 wks |
| | **— [[Stage-5_Specialized#final-gate\|Final Gate]] —** *(custom C2 in lab, published AI security research, 3+ reports, OSCP)* | | | **~15–22 wks** |

> **Total realistic estimate: ~10–14 months** of consistent daily sessions. Drift, passive reading instead of lab time, or skipping stage gates will stretch this significantly.

---

## 🗺️ Topics — Mapped to Execution Order

> Comprehensive topic breakdown mapped directly to the execution order across all 5 stages.

---

### 🔵 STAGE 1 — FOUNDATION
*Modules 01–07 · ~2–3 months*

| # | Module | Category / Domain | Core Concepts & Technical Scope | Key Tools & Standards |
|:--:|--------|-------------------|---------------------------------|-----------------------|
| **01** | [[Stage-1_Foundation#module-01-fundamentals\|Fundamentals]] | **Hardware** | CPU Architecture (`x86/x64`, `ARM/ARM64`), CPU Registers, Instruction Sets, RAM, Cache hierarchies, Storage (`HDD/SSD/NVMe`), BIOS, UEFI, TPM 2.0, Secure Boot, DMA, I/O, PCIe, USB, Firmware, Embedded Controllers | `x86_64`, `ARM64`, UEFI, TPM 2.0 |
| | | **OS Internals & Arch** | Memory Addressing, Virtual & Physical Memory, Stack & Heap internals, Pointers, Processes, Threads, Context Switching, Interrupts, System Calls, Privilege Rings (`User Mode` vs `Kernel Mode`), IPC | POSIX, Win32 API, C |
| | | **Data & Logic** | Hexadecimal, Binary, ASCII, Unicode, Endianness (Big vs Little Endian), Bitwise Operations (AND, OR, XOR, NOT, Shifts), Two's Complement, Integer Overflows & Sign Issues | Hex editors, Python 3 |
| | | **Physical & Mobile** | USB Architecture & HID Attacks, Serial Communication, Bluetooth & NFC fundamentals, Mobile OS Sandbox Models (Android vs iOS), APK / IPA application structures | ADB, Wireshark, Hardware analyzers |
| **02** | [[Stage-1_Foundation#module-02-linux-administration\|Linux Administration]] | **Internals & Processes** | Linux Kernel, Processes, Threads, Syscalls, Signals, File Descriptors, Sockets, Pipes, IPC, Virtual Filesystems (`/proc`, `/sys`, `/dev`), Critical Directories (`/tmp`, `/var`, `/etc`) | `bash`, `strace`, `ltrace`, `gdb` |
| | | **Security Model & Access** | Users, Groups, File Permissions (rwx, octal), POSIX ACLs, Linux Capabilities, `SUID` / `SGID`, Sticky bit, `sudo` policy & sudoers configuration, Namespaces, `cgroups`, MAC (`SELinux`, `AppArmor`) | `lsof`, `ss`, `ps`, `top`, `getfacl` |
| | | **Networking & Storage** | Network interfaces, Routing tables, Firewalling (`iptables`, `nftables`, `ufw`), Disk partitioning, Mount points, Inodes, LVM, Swap, Filesystems (ext4, XFS, Btrfs) | `ip`, `ss`, `iptables`, `fdisk`, `lsblk` |
| | | **Services & Logging** | `systemd` unit lifecycle, Timers, Cron jobs, SSH daemon configuration & hardening, Syslog, Journald, Log monitoring, Auditd basics | `systemctl`, `journalctl`, OpenSSH, `logrotate` |
| **03** | [[Stage-1_Foundation#module-03-windows-administration\|Windows Administration]] | **Architecture & Subsystems** | Win32 API, Windows NT Kernel, Processes, Threads, DLLs, Handles, Access Tokens, Services, Registry hives (HKLM, HKCU), NTFS & ACLs/DACLs, Named Pipes, WMI, COM, RPC | Sysinternals (`Procmon`, `Process Explorer`, `Autoruns`) |
| | | **Authentication & Identity** | NTLM, Kerberos, Windows Hello, Credential Providers, LSASS architecture, SAM database, LSA Secrets, DPAPI, Local Accounts vs Domain Accounts | Mimikatz, Rubeus, LSASS, `klist` |
| | | **Security Controls & Logs** | UAC, Windows Defender, Windows Firewall, AppLocker, WDAC, AMSI, ETW, Security Event Logs (Event IDs 4624, 4625, 4672, 4688), Local Security Policies, GPO | Event Viewer, Group Policy Editor, Sysmon |
| | | **PowerShell & Admin** | PowerShell Core (7+), Cmdlets, Pipeline, Remote Management (`WinRM`), PowerShell Script Block Logging, Constrained Language Mode (CLM), Automation scripts | PowerShell 7+, WinRM, PSReadLine |
| **04** | [[Stage-1_Foundation#module-04-networking-fundamentals\|Networking Fundamentals]] | **Physical & Data Link (L1–L2)** | Ethernet frames, MAC addressing, CSMA/CD, Switches, VLANs, 802.1Q trunking, STP, ARP protocol, ARP cache poisoning, Collision & Broadcast domains | Wireshark, `tcpdump`, `arp`, `macchanger` |
| | | **Network & Transport (L3–L4)** | IPv4 & IPv6 addressing, Subnetting (CIDR, VLSM), Routing protocols (OSPF, BGP, RIP), NAT, ICMP; TCP 3-way handshake, Flags (SYN, ACK, FIN, RST, PSH, URG), Flow control, Windowing, UDP | `traceroute`, `ping`, `ipcalc`, Scapy |
| | | **Application Layer (L7)** | DNS resolution & records (A, AAAA, MX, TXT, PTR, NS, SOA, SRV), DHCP lease process (DORA), HTTP/HTTPS, FTP, SSH, SMTP, POP3, IMAP, SNMP, NTP, RDP, SMB | `dig`, `nslookup`, `curl`, `nc`, `nmap` |
| | | **Perimeter & Packet Analysis** | Perimeter Firewalls (Stateful vs Stateless), Proxies, NAT gateways, IDS/IPS concepts, Deep Packet Inspection (DPI), Network baselines, PCAP analysis | Wireshark, `tshark`, `tcpdump`, NetworkMiner |
| **05** | [[Stage-1_Foundation#module-05-cryptography\|Cryptography]] | **Core Concepts & Symmetric** | Symmetric Encryption (AES, ChaCha20, DES/3DES), Block Ciphers, Stream Ciphers, Cipher Modes (ECB, CBC, CTR, GCM), Hashes (MD5, SHA-1, SHA-256, SHA-3), HMAC, Salt, IV, Nonce | `openssl`, Python `cryptography`, CyberChef |
| | | **Asymmetric & PKI** | Asymmetric Encryption (RSA, ECC, Diffie-Hellman, ECDH, DSA, Ed25519), Digital Signatures, PKI, Certificate Authorities (CA), X.509 certificates, CRL, OCSP, TLS 1.2/1.3 Handshake | `openssl`, `certutil`, `gpg` |
| | | **Attacks & Data Protection** | Known Plaintext, Padding Oracle attacks, Length Extension, Collision attacks, Passwords at rest (`bcrypt`, `scrypt`, `Argon2`, PBKDF2), Post-Quantum Cryptography (PQC: Kyber, Dilithium) | `hashcat`, `john`, `padding-oracle-attacker` |
| **06** | [[Stage-1_Foundation#module-06-authentication-standards\|Authentication Standards]] | **Sessions & Passwords** | Password Authentication policies, Salted hashing, Session lifecycle (creation, timeout, termination), Cookie security flags (HttpOnly, Secure, SameSite), Session fixation, Session hijacking | Browser DevTools, Burp Suite, Python |
| | | **Token & Modern Standards** | JWT Architecture (Header, Payload, Signature), JWS, JWE, Token algorithms, Claims validation, Expiration, Refresh tokens, Token revocation, Passkeys (FIDO2, WebAuthn), Biometrics | `jwt.io`, `jwt_tool`, FIDO2 testbeds |
| | | **Federation & MFA** | OAuth 2.0 roles & grant types (Auth Code, PKCE, Client Credentials), OpenID Connect (OIDC), SAML 2.0 SSO, MFA types (SMS, TOTP, Push, FIDO hardware keys) & bypasses | OAuth Playground, Keycloak, Burp Suite |
| **07** | [[Stage-1_Foundation#module-07-web-technology-fundamentals\|Web Technology Fundamentals]] | **HTTP & Web Protocols** | HTTP/1.1, HTTP/2, HTTP/3 (QUIC), Methods (GET, POST, PUT, DELETE, PATCH, OPTIONS, HEAD), Status codes, Request/Response headers, URL structure & encoding, WebSockets, Webhooks | `curl`, Postman, Browser DevTools |
| | | **Browser Security Model** | Same-Origin Policy (SOP), Cross-Origin Resource Sharing (CORS), Content Security Policy (CSP), Web Security Headers (HSTS, X-Content-Type-Options, X-Frame-Options), DOM internals, Web Storage | Chrome DevTools, Burp Suite |
| | | **Modern Web Architecture** | REST APIs, JSON/XML parsing, Single Page Applications (SPAs), Server-Side Rendering (SSR), Microservices, Reverse Proxies (Nginx), CDNs, WAF fundamentals, Service-to-Service auth | Docker, Nginx, Node.js / Python |
| **01–07** | **Programming Track** *(Weekend Track)* | **Scripting & Tooling** | Python, Bash, PowerShell, C/C++, Go, Rust; syntax, data structures, regex, OOP, system APIs, CLI authoring | Python 3, Bash, PowerShell, GCC/Clang, Go, Rust |
| | | **Security Domains** | Socket programming, Network packet manipulation, Custom port scanners, HTTP requests & API clients, Web scrapers, Log parsers, Exploit PoC development, Memory analysis | Scapy, Requests, BeautifulSoup, `pwntools` |

---

### 🟠 STAGE 2 — OFFENSE I
*Modules 08–13 · ~5–6 weeks*

| # | Module | Category / Domain | Core Concepts & Technical Scope | Key Tools & Standards |
|:--:|--------|-------------------|---------------------------------|-----------------------|
| **08** | [[Stage-2_Offense-I#module-08-footprinting--reconnaissance\|Footprinting & Reconnaissance]] | **OSINT & Passive Recon** | Search engine dorking (Google, Bing), WHOIS databases, DNS records, ASN mapping, IP blocks & CIDR, Certificate Transparency logs, Job postings, Code repos, Tech stack discovery | `subfinder`, `assetfinder`, `amass`, `httpx`, `shodan`, `censys`, `crt.sh` |
| | | **Active Recon & Intelligence** | DNS zone transfers, Subdomain brute-forcing, Web crawler discovery, Metadata harvesting (FOCA, Exif), Web technology fingerprinting, IPv6 discovery, Dark Web breach data reconnaissance | `dig`, `dnsenum`, `wafw00f`, `whatweb`, `theHarvester`, `exiftool` |
| **09** | [[Stage-2_Offense-I#module-09-scanning\|Scanning]] | **Host Discovery & Topology** | ARP ping sweeps, ICMP discovery (Echo, Timestamp, Subnet mask), TCP SYN/ACK discovery sweeps, UDP sweeps, Network boundary mapping | `nmap`, `fping`, `masscan`, `netdiscover`, `arp-scan` |
| | | **Port & Service Scanning** | TCP Connect (`-sT`), SYN Stealth (`-sS`), UDP scanning (`-sU`), Null, FIN, Xmas scans, Full port ranges (`-p-`), Service version detection (`-sV`), OS fingerprinting (`-O`) | `nmap`, `masscan`, `naabu`, `rustscan` |
| | | **Defense Assessment & Evasion** | Fragmented packets, Decoy scanning (`-D`), Source port spoofing, Timing templates (`-T0` to `-T5`), Firewall/IDS detection, NSE vulnerability scanning scripts | `nmap` (NSE), Scapy, `hping3` |
| **10** | [[Stage-2_Offense-I#module-10-enumeration\|Enumeration]] | **SMB, RPC & NetBIOS** | Null sessions, SMB shares, Permissions, Users, Groups, Password policies, NetBIOS names, RPC endpoints & interfaces | `enum4linux-ng`, `smbclient`, `netexec`, `rpcclient`, `smbmap` |
| | | **Network Services & Directory** | SNMP MIB walking (v1/v2c/v3 communities), SMTP user enumeration (VRFY, EXPN, RCPT TO), LDAP queries, Active Directory base enumeration, DNS enumeration, NFS exports | `snmpwalk`, `onesixtyone`, `smtp-user-enum`, `ldapsearch`, `showmount` |
| | | **Web & App Enumeration** | HTTP banner grabbing, Web server extensions, Virtual host (`vhost`) discovery, Hidden directories & files, API endpoints, Enumeration OPSEC & traffic analysis | `gobuster`, `ffuf`, `feroxbuster`, `nikto`, `curl` |
| **11** | [[Stage-2_Offense-I#module-11-database-security\|Database Security]] | **SQL Databases** | MySQL, PostgreSQL, Microsoft SQL Server (`MSSQL`), Oracle, SQLite; In-band, Error-based, Union-based, Blind Boolean/Time-based SQLi, `xp_cmdshell`, `UDF`, `INTO OUTFILE` | `sqlmap`, `dbeaver`, native DB CLIs |
| | | **NoSQL & Cache** | MongoDB injection & operator abuse, Redis unauthenticated command execution (SSH key drop, webshell drop), Elasticsearch API exploitation | `nosqlmap`, `redis-cli`, `curl` |
| | | **PrivEsc & Hardening** | Database privilege escalation, DBA role abuse, Trust links, Data encryption at rest/transit, DB auditing, Hardening baselines | Native DB CLIs, Audit scripts |
| **12** | [[Stage-2_Offense-I#module-12-password-cracking--hash-analysis\|Password Cracking & Hash Analysis]] | **Hash Analysis & Acquisition** | Identifying hash algorithms, Salted hashes, Windows NTLM & LM, Kerberos tickets (krb5tgs, krb5asrep), Linux `/etc/shadow`, Database hashes, Archive hashes (Zip, Rar) | `hash-identifier`, `hashid`, Name-That-Hash |
| | | **Cracking Methodology** | Dictionary attacks, Brute-force, Hybrid attacks, Mask attacks, Rule-based cracking (best64, custom rules), Wordlist curation & mutation, Secrets extraction (SAM, LSASS, NTDS.dit) | `hashcat`, `john`, `cewl`, `cupp`, `secretsdump.py` |
| | | **Protocol & Online Attacks** | Online brute-force attacks, Password spraying (SMB, SSH, RDP, FTP, HTTP), Lockout policy handling; Protocol cracking (NetNTLMv1/v2, WPA2/WPA3 4-way handshake, PMKID) | `hydra`, `medusa`, `crowbar`, `aircrack-ng` |
| **13** | [[Stage-2_Offense-I#module-13-system-hacking--initial-compromise\|System Hacking & Initial Compromise]] | **Initial Access & Payloads** | Vulnerability exploitation, Metasploit Framework, Exploit-DB PoCs, Custom exploit modification, Reverse shells, Bind shells, Web shells, Staged vs Stageless payloads, Handlers | `msfconsole`, `msfvenom`, `nc`, `socat`, `revshells.com` |
| | | **Linux PrivEsc** | `SUID` / `SGID` binary abuse, `sudo -l` privileges & CVEs, Linux Capabilities (`cap_setuid`), Vulnerable Cron jobs, Systemd services, `$PATH` hijacking, Kernel exploits | `linpeas.sh`, `GTFOBins`, `pspy`, `unix-privesc-check` |
| | | **Windows PrivEsc** | Service misconfigurations (Unquoted paths, weak permissions), Registry autoruns, AlwaysInstallElevated, Token impersonation (`SeImpersonate`), UAC bypasses, DLL hijacking, Kernel exploits | `winpeas.exe`, `Seatbelt`, `PowerUp`, `SharpUp`, `JuicyPotato` |
| | | **Persistence & Lateral Move** | Persistence mechanisms (SSH keys, cron, registry, services, scheduled tasks), Living off the Land (LOLBAS / GTFOBins), Timestomping, Log clearing, Staging & data exfiltration | LOLBAS, PowerShell, Impacket suite |

---

### 🟣 STAGE 3 — WEB & APP SEC
*Modules 14–18 · ~8–10 weeks*

| # | Module | Category / Domain | Core Concepts & Technical Scope | Key Tools & Standards |
|:--:|--------|-------------------|---------------------------------|-----------------------|
| **14** | [[Stage-3_Web-and-App-Sec#module-14-web-application-hacking\|Web Application Hacking]] | **OWASP Top 10 Exploitation** | SQL Injection, Cross-Site Scripting (`XSS` — Stored/Reflected/DOM), `SSRF`, `XXE`, `BOLA` / `IDOR`, Path Traversal / LFI / RFI, Command Injection, Insecure Deserialization, `SSTI`, Access Control | Burp Suite Pro, OWASP ZAP, `sqlmap`, `ffuf`, `commix` |
| | | **Modern Web Attacks** | HTTP Request Smuggling (CL.TE, TE.CL, TE.TE), Web Cache Poisoning & Deception, Host Header attacks, HTTP Desync, Client-side Prototype Pollution, Race Conditions, Logic flaws | Turbo Intruder, HTTP Request Smuggler |
| | | **Post-Exploit & Defense** | Webshell deployment, Database pivoting, Server persistence, Defense mechanisms, WAF bypass techniques, Input validation, Content Security Policy (`CSP`) | Antak, Weevely, WAFW00F, Custom scripts |
| **15** | [[Stage-3_Web-and-App-Sec#module-15-session-hijacking--token-attacks\|Session Hijacking & Token Attacks]] | **Session Architecture** | Session generation entropy, Session fixation, Predictable session IDs, Cookie security attributes (`HttpOnly`, `Secure`, `SameSite=Strict/Lax/None`), Session termination flaws | Burp Sequencer, Cookie Editor, DevTools |
| | | **Token Theft & Forgery** | XSS token theft, MITM session hijacking, Cross-Site WebSocket hijacking; JWT exploitation: `none` algorithm, weak HMAC secrets, Algorithm confusion, `kid` / `jku` header injection, Token replay | `jwt_tool`, Burp Suite, Wireshark |
| **16** | [[Stage-3_Web-and-App-Sec#module-16-web-server-hacking\|Web Server Hacking]] | **Server Recon & Misconfig** | Web server footprinting (Apache, Nginx, IIS, Tomcat), HTTP verb tampering, Default credentials, Unprotected admin interfaces, Exposed source control (`.git`), Backup files | `nikto`, `whatweb`, `git-dumper`, `ffuf` |
| | | **Server Exploitation** | Directory traversal, Server-Side Code Execution, Apache path traversal (CVE-2021-41773), Nginx alias traversal, Tomcat Manager WAR deployment, IIS short filename vulnerability | Metasploit, `davtest`, `cadaver`, Exploit-DB PoCs |
| **17** | [[Stage-3_Web-and-App-Sec#module-17-api-security\|API Security]] | **REST APIs & OWASP API Top 10** | API reconnaissance, Swagger / OpenAPI parsing, `BOLA`, `BOPLA`, `BFLA`, Unrestricted resource consumption, Mass assignment, Security misconfigurations, Verbose error handling | Postman, `kiterunner`, `mitmproxy`, `arjun`, `ffuf` |
| | | **GraphQL & Modern Protocols** | GraphQL introspection, Query depth & complexity exhaustion, Batching attacks, Field suggestions; gRPC endpoint enumeration, WebSockets vulnerabilities, API Gateway bypasses | InQL, GraphQL Raider, Altair, `grpc_cli` |
| | | **API Auth & Hardening** | API Key exposure, OAuth 2.0 grant vulnerabilities, OpenID Connect token verification, JWT authentication bypasses in APIs, Rate limiting & WAF bypasses | Burp Suite, OAuth Playground, `jwt_tool` |
| **18** | [[Stage-3_Web-and-App-Sec#module-18-bug-bounty-methodology\|Bug Bounty Methodology]] | **Scoping & Wide Recon** | Bug bounty platform dynamics (HackerOne, Bugcrowd, Intigriti), Rules of Engagement, Wide-scope reconnaissance, ASN & CIDR enumeration, Subdomain takeovers, GitHub dorking | `subfinder`, `amass`, `nuclei`, `subjack`, `trufflehog` |
| | | **Chaining & Professional Triage** | Low-severity to High/Critical chaining, Business logic exploitation, Account takeover chains, Proof of Concept creation, CVSS calculation, Professional triager communication | Markdown report templates, Burp Suite Pro |
| | [[Stage-3_Web-and-App-Sec#side-track-a-detection-engineering--soc-operations\|Side-Track A: Detection Engineering & SOC]] *(Parallel Track)* | **Defensive Architecture & Telemetry** | Enterprise defense models, Network & Host telemetry, Sysmon event logging, Windows Security Events, Linux Auditd, EDR/XDR architecture, SIEM data ingestion & normalization | Sysmon, Velociraptor, Elastic Agent, Wazuh |
| | | **Detection Engineering & Hunting** | Detection rules authoring, Sigma rules, YARA rules, MITRE ATT&CK mapping, Hypothesis-driven threat hunting, Alert triage & SOC workflows, Incident response fundamentals | Sigma, YARA, Splunk, Elastic SIEM |
| | [[Stage-3_Web-and-App-Sec#side-track-b-ids-firewalls-and-honeypots\|Side-Track B: IDS, Firewalls, and Honeypots]] *(Parallel Track)* | **Network Defenses & Deception** | Stateful vs Stateless firewalls, Linux `nftables` / `iptables`, pfSense / OPNsense, Suricata & Snort IDS/IPS rule writing, Evasion detection, Honeypots & deception, Email & DNS security | Suricata, Snort, Cowrie, pfSense, Wireshark |
| | [[Stage-3_Web-and-App-Sec#side-track-c-cyber-threat-intelligence-cti--attack-surface-management\|Side-Track C: CTI & Attack Surface Management]] *(Parallel Track)* | **Threat Intel & EASM** | External Attack Surface Management, Threat actor profiling, IOCs & IOAs, Threat intelligence feeds, CTI platforms, MITRE ATT&CK & Diamond Model analysis, Intel operationalization | MISP, OpenCTI, Maltego, SpiderFoot |

---

### 🏢 STAGE 4 — ENTERPRISE
*Modules 19–26 · ~10–13 weeks*

| # | Module | Category / Domain | Core Concepts & Technical Scope | Key Tools & Standards |
|:--:|--------|-------------------|---------------------------------|-----------------------|
| **19** | [[Stage-4_Enterprise#module-19-active-directory--entra-id\|Active Directory & Entra ID]] | **AD Architecture & Enumeration** | Forests, Domains, Trees, Trusts, Domain Controllers, Global Catalogs, Schema, GPOs, OUs; PowerView & BloodHound graph analysis, LDAP enumeration, Domain querying | BloodHound / SharpHound, PowerView, `ldapsearch`, `netexec` |
| | | **Kerberos & Credential Attacks** | Kerberos protocol (AS-REQ/REP, TGS-REQ/REP, AP-REQ), Kerberoasting, AS-REP Roasting, Pass-the-Hash (`PtH`), Pass-the-Ticket (`PtT`), Overpass-the-Hash, Silver & Golden Tickets | Rubeus, Mimikatz, Impacket (`GetUserSPNs.py`, `secretsdump.py`) |
| | | **ACLs, Delegation & ADCS Abuse** | GenericAll, WriteDacl, GenericWrite abuse; Unconstrained, Constrained, and Resource-Based Constrained Delegation (`RBCD`); Active Directory Certificate Services (`ADCS`) ESC1–ESC8 | Certify, PKINITtools, BloodHound, PowerView |
| | | **Lateral Movement & Persistence** | DCSync attack, DCShadow, Skeleton Key, DSRM credential abuse, AdminSDHolder persistence, GPO backdoors, WMI & WinRM execution, DCOM execution, Remote Registry | Mimikatz, Impacket (`wmiexec.py`, `psexec.py`), Evil-WinRM |
| | | **Entra ID (Azure AD) & Hybrid** | Azure AD Connect exploitation, Password Hash Sync, ADFS attacks, Seamless SSO abuse, Primary Refresh Token (`PRT`) abuse, Hybrid identity attacks, Azure RBAC privilege escalation | AADInternals, ROADtools, Azure CLI, MicroBurst |
| **20** | [[Stage-4_Enterprise#module-20-cloud-computing\|Cloud Security]] | **Cloud Architecture & IAM** | AWS, Azure, GCP models, Shared responsibility, Cloud root boundaries; IAM Policies, Roles, Groups, Service Accounts, AssumeRole, Cross-account access, STS tokens | AWS CLI, Azure CLI, gcloud, Pacu |
| | | **Storage, Compute & Metadata** | S3 buckets, Azure Blob, GCS permissions, Public exposure analysis; EC2, Azure VMs; Instance Metadata Service (IMDSv1 vs IMDSv2), Metadata theft via SSRF, Cloud IaC | `s3scanner`, Pacu, ScoutSuite, Prowler |
| | | **Exploitation & Persistence** | Privilege escalation vectors in AWS/Azure, Shadow admins, IAM backdoor persistence, Serverless (Lambda/Functions) attacks, CloudTrail evasion, Cloud posture auditing | Pacu, Prowler, ScoutSuite, CloudSploit |
| **21** | [[Stage-4_Enterprise#module-21-container--orchestration-security\|Containers & Kubernetes]] | **Container Internals & Escapes** | Docker engine architecture, Linux namespaces (PID, Mount, Net, IPC, User), `cgroups`, Docker daemon socket exposure, Privileged containers, Capabilities abuse, Container breakout | Docker CLI, `deepce`, `cdk-go`, `amicontained` |
| | | **Kubernetes Security & Attacks** | K8s architecture (API Server, Kubelet, etcd, Controller Manager), Anonymous kubelet access, etcd credential dumping, Pod service account tokens (`JWT`), RBAC misconfigs, PrivEsc | `kubectl`, `kube-hunter`, `kube-bench`, `peirates` |
| | | **Runtime, CI/CD & Hypervisors** | Container runtime security (runc, containerd), AppArmor/Seccomp, Image scanning; CI/CD security (GitHub Actions poisoning, Jenkins RCE, pipeline secrets); Hypervisor escape concepts | Trivy, Grype, Falco, Semgrep |
| **22** | [[Stage-4_Enterprise#module-22-adversary-emulation--purple-teaming\|Adversary Emulation]] | **MITRE ATT&CK & Emulation** | ATT&CK matrix (Tactics, Techniques, Procedures), Navigator heatmaps, Threat actor profiling (APT29, FIN7), Emulation plans, Atomic Red Team execution, Automated emulation platforms | MITRE ATT&CK Navigator, Atomic Red Team, Caldera, Prelude Operator |
| | | **Purple Teaming & Metrics** | Collaborative offensive-defensive exercises, Detection gap analysis, EDR alert validation, Log coverage assessment, Security posture metrics (MTTD, MTTR), Purple team reporting | VECTR, Sigma, Sysmon, Elastic SIEM |
| **23** | [[Stage-4_Enterprise#module-23-sniffing--spoofing\|Lateral Movement & Sniffing]] | **Sniffing & Traffic Interception**| Promiscuous mode, Raw sockets, Passive network sniffing, Cleartext credential extraction (FTP, HTTP, Telnet, SNMP), Network protocol dissection, Wireshark display filters | Wireshark, `tshark`, `tcpdump`, `dsniff` |
| | | **Spoofing, MITM & Poisoning** | ARP cache poisoning, DNS spoofing, DHCP starvation & rogue DHCP, LLMNR & NBT-NS poisoning, WPAD spoofing, NTLM relaying, SSL stripping, Network MITM defenses | `responder`, `bettercap`, `ettercap`, `mitmproxy`, `ntlmrelayx.py` |
| **24** | [[Stage-4_Enterprise#module-24-social-engineering\|Social Engineering]] | **Psychology & Target Profiling** | Principles of influence (Authority, Scarcity, Urgency, Reciprocity, Social Proof), OSINT target profiling, Organizational charts, Corporate email naming conventions, Relationship mapping | LinkedIn, Maltego, theHarvester, Hunter.io |
| | | **Delivery Vectors & Physical** | Spear-phishing campaigns, Phishing infrastructure setup (SMTP, Lookalike domains, SPF/DKIM/DMARC, Reverse proxies), Credential harvesting, Vishing, Smishing, USB drops, Physical access | GoPhish, Evilginx2, SET, Modlishka |
| **25** | [[Stage-4_Enterprise#module-25-malware--weaponization-conceptual\|Malware & C2 Architectures]] | **Architecture & Staging** | Droppers, Downloaders, Stagers, Full-stage payloads, C2 beacon mechanics, Communication channels (HTTP, HTTPS, DNS, SMB), Heartbeats, Jitter, Malleable C2 profiles | Sliver, Mythic, Cobalt Strike concepts |
| | | **Execution & Evasion Mechanisms**| Process injection (CreateRemoteThread, Process Hollowing, APC Queue), DLL injection, Syscalls vs Win32 APIs, AMSI & ETW bypass concepts, Obfuscation, Persistence, Counter-forensics | Conceptual code, x64dbg, PE-bear, Process Hacker |
| | | **Artifacts & Memory Forensics** | Memory analysis concepts, Volatility framework, Identifying injected code, Malfind, Memory artifacts, Document weaponization (Macros, LNK files, ISO/VHD packaging) | Volatility 3, CyberChef, OLETools |
| **26** | [[Stage-4_Enterprise#module-26-pentest-methodologies--report-writing\|Pentest Reporting]] | **Frameworks, Scoping & Legal** | Penetration testing execution standards (PTES, NIST SP 800-115, OWASP Web Testing Guide, OSSTMM), Rules of Engagement (RoE), NDA, Scoping boundaries, Legal compliance & liability | Engagement checklists, PTES guidelines |
| | | **Threat Modeling & Risk Scoring** | Threat modeling methodologies (STRIDE, PASTA, DREAD), Vulnerability scoring (CVSS v3.1 / v4.0 metrics, Base/Temporal/Environmental scores), EPSS, Business risk contextualization | FIRST CVSS Calculator, Threat Modeling tools |
| | | **Technical Delivery & Reports** | Professional pentest report structure: Executive Summary, Methodology, Scope, Detailed Technical Findings, Reproduction Steps, Risk Matrix, Root Cause Analysis, Remediation Roadmaps | Markdown / LaTeX report templates, Typora, Git |

---

### 🔬 STAGE 5 — SPECIALIZED
*Modules 27–30 · ~15–22 weeks*

| # | Module | Category / Domain | Core Concepts & Technical Scope | Key Tools & Standards |
|:--:|--------|-------------------|---------------------------------|-----------------------|
| **27** | [[Stage-5_Specialized#module-27-offensive-development--tooling\|Offensive Development]] | **Systems Programming Foundations**| C & C++ for security practitioners, Pointers, Memory allocation, Stack/Heap internals, Win32 API, Native APIs (NTDLL), Direct Syscalls, Assembly (x86/x64), Linux POSIX system calls | GCC/Clang, Visual Studio, MSVC, x64dbg, Ghidra |
| | | **Exploit Dev & Windows OffSec** | Stack-based buffer overflows, Shellcode writing & encoding, Bad characters, Bypassing DEP/NX with ROP chains, ASLR bypasses; Process injection, Direct syscalls, PE parsing, EDR unhooking, AMSI/ETW patching | `pwntools`, Mona.py, x64dbg, Visual Studio |
| | | **Linux OffSec Dev & C2 Implants**| Linux ELF binary manipulation, Custom LD_PRELOAD hooks, ptrace injection, Rootkit concepts; Custom C2 implant architecture in Go/Rust/C++, Encrypted communications, Sleep obfuscation, Task execution queue | GCC, Go, Rust, Wireshark |
| **27** | **Reverse Engineering** *(Parallel Track)* | **Binary Formats & Disassembly** | PE (Portable Executable), ELF, Mach-O, DLLs, Shared Libraries, Control Flow Analysis, Data Flow Analysis, API Analysis, Strings, Imports/Exports; x86, x64, ARM, ARM64 architectures | `ghidra`, `ida-pro`, `binary-ninja`, `radare2` |
| | | **Analysis, Debugging & Evasion** | Dynamic debugging, Packing, Code Obfuscation, Anti-Debugging, Anti-VM, Control Flow Flattening, Binary Patching, Hooking, Runtime Analysis | `x64dbg`, `windbg`, PEview, Hex Editors |
| **27** | **Fuzzing & Vuln Research** *(Parallel Track)* | **Fuzzing Mechanics** | Black-Box, White-Box, Grey-Box Fuzzing, Mutation-Based vs Generation-Based Fuzzing, Coverage-Guided Fuzzing, Protocol Fuzzing, File Format Fuzzing, API Fuzzing, Binary Fuzzing, Crash Triage, Sanitizers (`ASan`, `MSan`, `UBSan`) | `afl++`, `libfuzzer`, `honggfuzz`, `boofuzz` |
| | | **Vuln Research & Code Audit** | Attack Surface Research, Bug Discovery, Root Cause Analysis, Variant Analysis, Patch Diffing, Memory Corruption, Logic Bugs, Supply Chain Vulnerabilities, SAST, Secure Code Review | `semgrep`, `ghidra`, BinDiff, Wireshark |
| **28** | [[Stage-5_Specialized#module-28-ai--llm-red-teaming\|AI & LLM Red Teaming]] | **AI Foundations & LLM Vulns** | Machine Learning, Transformers, LLM architecture, Tokenization, Embeddings, Vector databases, Retrieval-Augmented Generation (`RAG`); OWASP Top 10 for LLMs, Direct & Indirect Prompt Injection, Jailbreaks, System Prompt extraction | LangChain, LlamaIndex, OpenAI / Anthropic APIs, `garak`, `pyrit` |
| | | **Agent Security & Adversarial ML**| AI Agent architecture, Tool / Function calling vulnerabilities, Excessive agency, Context poisoning, Memory injection, Model inversion, Training data poisoning, Adversarial perturbations, AI red team automation | Custom testbeds, NeMo Guardrails, Mindgard |
| **28** | **Modern Attack Surfaces** *(Parallel Track)* | **Cloud-Native & CI/CD Security**| Containers, Serverless, Service Mesh, API Ecosystems, Microservices, Zero Trust; Secure SDLC, Source Code Security, SAST/DAST/SCA, Secret Scanning, CI/CD Pipeline Security, Git Security, Container & IaC Security, SBOM, Supply Chain Attacks | Semgrep, Trivy, Cosign, Syft |
| | | **Web3 & Blockchain** | Blockchain Architecture, Ethereum & EVM, Solidity, Smart Contracts, Wallets, Tokens, DeFi Protocols, Oracles, Bridges, Signatures; Reentrancy, Access Control Flaws, Integer Issues, Oracle Manipulation, Flash Loans, Blockchain Forensics | `slither`, `mythril`, Foundry, Remix |
| | | **IoT & Embedded Systems** | Embedded Systems, Firmware Internals, Bootloaders, Hardware Interfaces (`UART`, `SPI`, `I2C`, `JTAG`), Hardware Debugging, Firmware Extraction, Firmware Analysis, Secure Boot Bypasses, Device Authentication | `binwalk`, Saleae Logic, JTAGulator |
| **29** | [[Stage-5_Specialized#module-29-red-team-operations--tradecraft\|Red Team Operations]] | **Campaign Planning & Infra** | Threat actor emulation planning, Red team infrastructure setup (Redirectors, Long-haul vs Short-haul C2, Domain fronting/categorization, CDN routing), Malleable C2 profiles, Operational Security (`OPSEC`), Covert communications | Sliver, Mythic, Cobalt Strike, Nginx redirectors |
| | | **Execution & Lateral Movement** | Assumed-breach methodology, Credential access in hardened environments, Cross-forest pivoting, Low-and-slow data exfiltration, Deconfliction procedures with defensive teams, Executive debriefing & timeline reconstruction | Sliver, Impacket, BloodHound, Rubeus |
| **29** | **Defensive Awareness** *(Parallel Track)* | **DFIR & Incident Response** | Disk Forensics, Memory Forensics, Network Forensics, Evidence Preservation, Timeline Analysis, Incident Response Triage, Containment, Eradication, Recovery, Root Cause Analysis, IOC Analysis, Malware Investigation | `volatility`, `autopsy`, `ftk`, Wireshark |
| | | **SOC / SIEM / EDR & Hunting** | Detection Engineering, Alert Triage, Incident Investigation, SOC Workflows, Log Ingestion, Correlation Rules, Event Normalization, Alert Logic, Sigma Rules, Endpoint Detection, Behavioral Detection, Threat Hunting | Splunk, Elastic SIEM, Sigma rules, Sysmon, Velociraptor |
| **29** | **Intelligence** *(Parallel Track)* | **Threat Intelligence** | Threat Actors, Campaigns, Malware Families, Infrastructure, IOCs, IOAs, TTPs, Domains, IPs, Hashes, Infrastructure Correlation, Threat Attribution, Threat Intelligence Reports, MITRE ATT&CK Mapping | MISP, OpenCTI, MITRE ATT&CK |
| | | **OSINT & Dark Web Intel** | Search Intelligence, Domain & DNS Intelligence, Username & Email Intel, Public Records, Exif Metadata, Image & Video Geolocation, Breach Intelligence; Tor, Onion Services, Underground Markets, Cybercrime Ecosystems | `maltego`, `spiderfoot`, `shodan`, `censys`, Tor Browser |
| **30** | [[Stage-5_Specialized#module-30-proof-of-work--career-portfolio\|Proof of Work & Career]] | **Hands-on Proof & Labs** | Public portfolio construction, Hack The Box (`HTB`) Pro Labs writeups, TryHackMe (`THM`) milestones, PortSwigger Web Security Academy completions, VulnHub, Enterprise multi-cloud and AD lab demonstrations | HTB Pro Labs, PortSwigger Academy, GitHub |
| | | **Engagements, CVEs & Research** | Penetration Testing Methodologies, Scope Definition, RoE, Exploitation & Reporting; CVE Request & Coordinated Vulnerability Disclosure process, Vulnerability Reproduction, PoC development, Security Advisories | Mitre CVE program, GitHub Advisories, Exploit-DB |
| | | **Portfolio & Career Strategy** | Research Papers, Blog Posts, CVE Write-ups, Open Source Tool authoring & maintenance, Industry Certifications (OSCP, CPTS, CRTO, CISSP), Technical Interview & Whiteboard Defense preparation | GitHub, Medium / Substack, GitBook, LinkedIn |

---

## 📦 Shelf — Self Post-Hire

> These aren't "later in the sequence" — they're off the sequence entirely until you have a job. No number means no claim on your time right now.

| # | Module | Focus Area |
|:-:|--------|------------|
| S01 | [[Shelf_Post-Hire#shelf-01-wireless-network-security\|Wireless Network Security]] | WPA2/WPA3, Evil Twin, PMKID |
| S02 | [[Shelf_Post-Hire#shelf-02-mobile-platform-pentesting\|Mobile Security]] | Android/iOS, Frida, MobSF, Pinning |
| S03 | [[Shelf_Post-Hire#shelf-03-otics-scada-security\|OT / ICS / SCADA Security]] | Modbus, S7comm, Purdue model |
| S04 | [[Shelf_Post-Hire#shelf-04-digital-forensics\|Digital Forensics]] | Memory, Disk, Autopsy, Volatility |
| S05 | [[Shelf_Post-Hire#shelf-05-reverse-engineering--malware-analysis\|Reverse Engineering & Malware Analysis]] | Ghidra, x64dbg, unpacking |
| S06 | [[Shelf_Post-Hire#shelf-06-modern-exploitation\|Modern Exploitation]] | Binary exploitation, ROP, ASLR/DEP |
| S07 | [[Shelf_Post-Hire#shelf-07-hardware-hacking--embedded-systems\|Hardware Hacking & Embedded Systems]] | UART, JTAG, Firmware extraction |
| S08 | [[Shelf_Post-Hire#shelf-08-physical-penetration-testing\|Physical Penetration Testing]] | Lock picking, RFID cloning, bypass |
| S09 | [[Shelf_Post-Hire#shelf-09-voip--telecommunications-security\|VoIP & Telecommunications Security]] | SIP, RTP, SS7/5G concepts |
| S10 | [[Shelf_Post-Hire#shelf-10-blockchain--web3-security\|Blockchain & Web3 Security]] | Smart contract audits, reentrancy |
| S11 | [[Shelf_Post-Hire#shelf-11-governance-risk--compliance-grc\|Governance, Risk & Compliance]] | ISO 27001, SOC 2, NIST CSF |
| S12 | [[Shelf_Post-Hire#shelf-12-supply-chain-security\|Supply Chain Security]] | SBOM, Dependency confusion, SLSA |
| S13 | [[Shelf_Post-Hire#shelf-13-devsecops--secure-sdlc\|DevSecOps & Secure SDLC]] | CI/CD pipelines, SAST/DAST, Semgrep |
| S14 | [[Shelf_Post-Hire#shelf-14-secure-code-review-methodology\|Secure Code Review Methodology]] | Code auditing, source-level vuln analysis |
| S15 | [[Shelf_Post-Hire#shelf-15-security-architecture--engineering\|Security Architecture & Engineering]] | Zero Trust, threat modeling, STRIDE |
| S16 | [[Shelf_Post-Hire#shelf-16-security-operations-expansion\|Security Operations Expansion]] | SOAR, DLP, Insider threat |
| S17 | [[Shelf_Post-Hire#shelf-17-denial-of-service--availability-resilience\|Denial of Service & Resilience]] | Layer 4/7 mechanisms, Anycast, DDoS mitigation |

---

<a id="daily-protocol"></a>

## ⏱️ Daily Protocol

> One question answered every morning: **"What is my current module and what am I proving today?"**

**1. Engineering Foundation**
Read the protocol or mechanism for your current topic. Write structured notes. Understand *why* it works before touching a tool.

**2. Lab Execution**
Terminal open. Wireshark running. Execute commands, capture output, break things. Never run a tool you cannot explain at the packet or system level.

**3. Artifact & Proof**
Save PCAP/log/screenshot. Write the 1-page lab summary. Git commit with a descriptive message. Check the Move-On Gate in the stage file.

### Hard Rules

1. **Never start with passive reading.** Peak energy belongs to the terminal, not a PDF.
2. **Never run a tool blindly.** If you can't explain what a flag does at the packet level — stop, read, then run.
3. **No writeup = learning didn't happen.** Every lab session gets a committed markdown file.
4. **Respect the Stage Gates.** Do not proceed until you can demonstrate the skill without notes.
5. **Git commit after every session.** If you haven't committed in 2 weeks, you're drifting.

### Programming Track *(Weekends Only)*

| Stage | Language | Focus |
|:-----:|----------|-------|
| Foundation | Python, Bash, PowerShell | Scripting fundamentals, OS automation |
| Offense I | Python, Bash | Tool wrappers, log parsing, scan automation |
| Web & App Sec | Python, JavaScript | Web exploit PoCs, XSS weaponization |
| Enterprise | PowerShell, Python (Scapy) | AD enumeration, Impacket, packet fabrication |
| Specialized | C/C++, Assembly, PowerShell, Python | Shellcode, loaders, AMSI bypass, LLM harnesses |

---

<a id="lab-setup"></a>

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

