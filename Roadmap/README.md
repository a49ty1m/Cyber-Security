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
| **01** | [[Stage-1_Foundation#module-01-fundamentals\|Hardware & Architecture]] | **Hardware** | CPU Architecture (`x86/x64`, `ARM/ARM64`), CPU Registers, Instruction Sets, RAM, Cache hierarchies, Storage (`HDD/SSD/NVMe`), BIOS, UEFI, TPM, Secure Boot, DMA, I/O, PCIe, USB, Firmware, Embedded Controllers | `x86_64`, `ARM64`, UEFI, TPM 2.0 |
| | | **Architecture** | Memory Addressing, Virtual & Physical Memory, Stack & Heap internals, Pointers, Processes, Threads, Context Switching, Interrupts, System Calls, Privilege Rings (`User Mode` vs `Kernel Mode`), IPC | POSIX, Win32 API, C |
| **02** | [[Stage-1_Foundation#module-02-linux-administration\|Linux Administration]] | **Internals** | Linux Kernel, Processes, Threads, Syscalls, Signals, File Descriptors, Sockets, Pipes, IPC, Virtual Filesystems (`/proc`, `/sys`, `/dev`), Critical Directories (`/tmp`, `/var`, `/etc`) | `bash`, `strace`, `ltrace`, `gdb` |
| | | **Security Model** | Users, Groups, Permissions, POSIX ACLs, Linux Capabilities, `SUID` / `SGID`, `sudo` policy, Namespaces, `cgroups`, MAC (`SELinux`, `AppArmor`) | `lsof`, `ss`, `ps`, `top`, `tmux` |
| | | **Services** | `systemd` unit lifecycle, Cron jobs, SSH daemon configuration, System Daemons, Startup & Boot mechanisms | `systemctl`, `journalctl`, OpenSSH |
| **03** | [[Stage-1_Foundation#module-03-windows-administration\|Windows Administration]] | **Architecture** | Win32 API, Windows NT Kernel, Processes, Threads, DLLs, Handles, Access Tokens, Services, Registry hives, NTFS & ACLs, Named Pipes, WMI, COM, RPC | Sysinternals (`Procmon`, `Process Explorer`) |
| | | **Authentication** | NTLM, Kerberos, Windows Hello, Credential Providers, LSASS architecture, SAM database, LSA Secrets, DPAPI | Mimikatz, Rubeus, LSASS |
| | | **Security Controls** | UAC, Windows Defender, Windows Firewall, AppLocker, WDAC, AMSI, ETW, Security Event Logs, Local Security Policies | Event Viewer, Group Policy Editor |
| | | **PowerShell & Admin** | PowerShell Core, PowerShell Remoting (`WinRM`), Windows Automation, Security Automation, PowerShell Script Block Logging | PowerShell 7+, WinRM |
| **04** | [[Stage-1_Foundation#module-04-networking-fundamentals\|Networking Fundamentals]] | **Core & Models** | Ethernet, MAC addressing, ARP, IPv4 & IPv6, ICMP, TCP & UDP mechanics, QUIC, Ports & Sockets, Routing, Switching, VLANs, NAT & PAT, Subnetting & CIDR, MTU & Fragmentation | `wireshark`, `tcpdump`, `netcat`, `socat` |
| | | **Protocols** | DNS, DHCP, HTTP, HTTPS, TLS, SSH, FTP, SFTP, SMTP, IMAP, POP3, LDAP, SMB, NFS, SNMP, RDP, WinRM, Kerberos, NTLM, SIP, MQTT, WebSocket, gRPC | OpenSSL, `dig`, `curl` |
| | | **Infrastructure** | Firewalls, WAFs, IDS/IPS, Load Balancers, Proxies (Forward/Reverse), VPN, CDN, DNS Providers, API Gateways, Network Segmentation, Zero Trust Architecture, Service Mesh | Suricata, Snort, Cloudflare |
| | | **Packet Analysis** | Packet Capture, Packet Reconstruction, TCP Stream Analysis, DNS Analysis, TLS Analysis, Protocol Fingerprinting, Traffic Anomaly Detection, Network Forensics | `wireshark`, `tcpdump`, `tshark`, `nmap`, `masscan` |
| **05** | [[Stage-1_Foundation#module-05-cryptography\|Cryptography]] | **Primitives & Core** | Encoding vs Hashing vs Encryption, Symmetric Cryptography (`AES`, `ChaCha20`), Asymmetric Cryptography (`RSA`, `ECC`, `Diffie-Hellman`), Digital Signatures, HMAC, Randomness, Entropy | `openssl`, Python `cryptography` |
| | | **PKI & Key Mgmt** | Public Key Infrastructure (PKI), X.509 Certificates, TLS Handshake mechanics, Key Lifecycle & Management, Password Hashing (`bcrypt`, `scrypt`, `Argon2`), Cryptographic Failures | `hashcat`, `john`, `gpg` |
| **06** | [[Stage-1_Foundation#module-06-authentication-standards\|Authentication & Identity]] | **Authentication** | Password Authentication, MFA / 2FA, Passkeys, Passwordless, Biometrics, Device Authentication, Session Lifecycle Management, Account Recovery, Session Fixation, Session Hijacking | FIDO2 / WebAuthn, OAuth Playground |
| | | **Identity & Federation** | OAuth 2.0, OpenID Connect (OIDC), SAML 2.0, LDAP, Kerberos, Active Directory, Entra ID, Identity Providers (IdP), Federation, RBAC, ABAC, Privileged Access Management (PAM), Identity Governance | Keycloak, Entra ID, Okta |
| | | **Token Security** | JWT Structure (Header, Payload, Signature), JWS, JWE, Signing, Verification, Algorithm Confusion, Key Management, Claims, Expiration, Audience, Issuer, Token Rotation, Refresh Tokens, Token Revocation, Authorization Boundaries | `jwt.io`, Burp Suite |
| **07** | [[Stage-1_Foundation#module-07-web-technology-fundamentals\|Web Technology Fundamentals]] | **Web Fundamentals** | HTTP/HTTPS specs, Requests & Responses, Headers, Cookies, Sessions, Caching, Browser Security Model, Same-Origin Policy (SOP), CORS, CSP, WebSockets, Webhooks | Browser DevTools, Postman, `curl` |
| | | **Modern Architecture** | Service Workers, WebAssembly (Wasm), WebRTC, GraphQL, gRPC, Serverless, Microservices, Reverse Proxies, CDNs, WAFs, API Gateways, Microservice Communication, Internal APIs, Service-to-Service Authentication | Docker, Envoy, Nginx |
| **01–07** | **Programming Track** *(Weekend Track)* | **Scripting & Tooling** | Python, Bash, PowerShell, JavaScript, C / C++, Go, Rust, Java, PHP, SQL, x86/x64 Assembly | Python 3, GCC/Clang, Go, Rust |
| | | **Security Domains** | Automation, Network Programming, HTTP & APIs, Sockets, Async & Multithreading, Parsing & Regex, Exploit Research, Security Tool Development, Data Processing, Browser Internals (DOM, Events, Fetch/XHR), Memory/Pointers/Heap | Scapy, Requests, BeautifulSoup, `pwntools` |

---

### 🟠 STAGE 2 — OFFENSE I
*Modules 08–13 · ~5–6 weeks*

| # | Module | Category / Domain | Core Concepts & Technical Scope | Key Tools & Standards |
|:--:|--------|-------------------|---------------------------------|-----------------------|
| **08–10** | [[Stage-2_Offense-I#module-08-footprinting--reconnaissance\|Recon & Enumeration]] | **Infrastructure** | Domain & Subdomain Enumeration, DNS analysis, ASN mapping, IP Ranges & CIDR blocks, Cloud Asset Discovery, Certificate Transparency logs, Technology Stack Fingerprinting, Exposed Services, Attack Surface Mapping | `amass`, `subfinder`, `assetfinder`, `httpx`, `shodan`, `censys` |
| | | **Application Recon** | Endpoint & Parameter Discovery, API Discovery, JavaScript Source Code Analysis, Hidden Routes, Authentication Flows, Third-Party Integrations, Mobile Backends | `katana`, `gau`, `waybackurls`, `nuclei` |
| | | **Network Recon** | Port Scanning, Service Fingerprinting, Host Footprinting, Sniffing & Traffic Interception, ARP Poisoning, MITM | `nmap`, `masscan`, `naabu`, `maltego`, `spiderfoot` |
| **11** | [[Stage-2_Offense-I#module-11-database-security\|Database Security]] | **SQL Databases** | MySQL, PostgreSQL, Microsoft SQL Server (`MSSQL`), Oracle, SQLite | `sqlmap`, Native DB CLIs |
| | | **NoSQL & Cache** | MongoDB, Redis, Elasticsearch | `nosqlmap`, Redis CLI |
| | | **Attacks & Hardening** | SQL & NoSQL Injection, Auth & Access Controls, Privilege Separation, Secrets Storage in Databases, Encryption at Rest/Transit, Data Exposure, Backup Security, DB Logging & Auditing | Hex dumps, Data exfiltration scripts |
| **12** | [[Stage-2_Offense-I#module-12-password-cracking--hash-analysis\|Credential Attacks]] | **Password Attacks** | Password Security Policies, Online Brute-Force, Password Spraying, Credential Stuffing, Hash Analysis, Dictionary & Rule-Based Cracking | `hashcat`, `john`, `hydra` |
| | | **Secret Stores** | NTLM & Kerberos hashes, Credential Stores, LSASS memory extraction, SAM database, DPAPI blobs, Browser Credentials, SSH Keys, API Keys, Cloud Credentials, Secrets Management Vaults | `rubeus`, `mimikatz`, `secretsdump` |
| **13** | [[Stage-2_Offense-I#module-13-system-hacking--initial-compromise\|System Hacking & PrivEsc]] | **Linux PrivEsc** | `SUID` / `SGID` abuse, `sudo` misconfigurations, Linux Capabilities, Vulnerable Cron Jobs, Systemd Services, `$PATH` Hijacking, Insecure File Permissions, Exposed Credentials, Container Escape Basics, Kernel Exploits | `linpeas`, `GTFOBins`, `pspy` |
| | | **Windows PrivEsc** | Insecure Service Permissions, Unquoted Service Paths, Registry Autoruns, Token Impersonation (`SeImpersonate`), UAC Bypasses, Scheduled Tasks, DLL Search Order Hijacking, WMI abuse, Named Pipe abuse, Kernel Exploits | `winpeas`, `Seatbelt`, `PowerUp`, `SharpUp` |

---

### 🟣 STAGE 3 — WEB & APP SEC
*Modules 14–18 · ~8–10 weeks*

| # | Module | Category / Domain | Core Concepts & Technical Scope | Key Tools & Standards |
|:--:|--------|-------------------|---------------------------------|-----------------------|
| **14–16** | [[Stage-3_Web-and-App-Sec#module-14-web-application-hacking\|Web Security]] | **OWASP Core Vulns** | Broken Access Control, Authentication Failures, SQL Injection, NoSQL Injection, Cross-Site Scripting (`XSS` — Stored/Reflected/DOM), `CSRF`, `SSRF`, `XXE`, Server-Side Template Injection (`SSTI`), `IDOR` / `BOLA`, `BFLA`, Path Traversal, Command Injection, Insecure File Upload, Open Redirect, Prototype Pollution, Insecure Deserialization, Race Conditions, Business Logic Bugs | Burp Suite Pro, OWASP ZAP, `sqlmap`, `ffuf` |
| | | **Modern Web Attacks** | HTTP Request Smuggling (CL.TE, TE.CL, TE.TE), Web Cache Poisoning, Web Cache Deception, Host Header Attacks, HTTP Parser Confusion, Request Splitting, Client-Side Desync | Turbo Intruder, HTTP Request Smuggler |
| | | **Session & Token** | Session Fixation, Session Hijacking, Cookie Tampering, JWT Attacks (Algorithm Confusion, `none` algorithm, weak secret brute-forcing), Token Forgery | `jwt_tool`, Burp Extensions |
| **17** | [[Stage-3_Web-and-App-Sec#module-17-api-security\|API Security]] | **REST APIs** | OWASP API Security Top 10, API Discovery, Authentication & Authorization, Broken Object Level Authorization (`BOLA`), Broken Function Level Authorization (`BFLA`), Rate Limiting Bypasses, Pagination & Filtering flaws, Mass Assignment, API Versioning flaws, Verbose Error Handling | Postman, `kiterunner`, `mitmproxy` |
| | | **GraphQL & Modern** | GraphQL Schema Introspection, Query Depth & Complexity attacks, Batching Attacks, Resolver Security, SOAP, gRPC, WebSockets, Webhooks | InQL, GraphQL Raider, Altair |
| | | **Identity & Tokens** | API Keys, OAuth 2.0 flows & grants, OpenID Connect (OIDC), JWT Access & Refresh Token handling, SAML SSO | Burp Suite, OAuth Playground |
| **18** | [[Stage-3_Web-and-App-Sec#module-18-bug-bounty-methodology\|Bug Bounty Methodology]] | **Core Methodology** | Program Scope Analysis, High-Speed Asset Discovery, Endpoint Discovery, Attack Surface Prioritization, Vulnerability Chaining, Business Logic Flaws, Race Conditions, Impact Analysis, Professional Report Writing, Triage Communication | HackerOne, Bugcrowd, Intigriti |
| | | **Elite Tradecraft** | Unconventional Attack Surfaces, Client-Side JavaScript Analysis & Deobfuscation, API Architecture Mapping, Business Workflow Analysis, Low-Severity to Critical Chaining, Novel Logic Flaws, Research-Driven Hunting | Custom recon pipelines, Burp Suite Pro |

---

### 🏢 STAGE 4 — ENTERPRISE
*Modules 19–26 · ~10–13 weeks*

| # | Module | Category / Domain | Core Concepts & Technical Scope | Key Tools & Standards |
|:--:|--------|-------------------|---------------------------------|-----------------------|
| **19** | [[Stage-4_Enterprise#module-19-active-directory--entra-id\|Active Directory & Entra ID]] | **AD Architecture** | Domains, Forests, Trees, Domain Controllers (DCs), Organizational Units (OUs), Users, Security Groups, Group Policy Objects (GPOs), LDAP, Dynamic DNS, Forest & Domain Trusts | `bloodhound`, `sharphound`, `powerview` |
| | | **Authentication** | Kerberos protocol mechanics (TGT, TGS, AS-REQ/REP), SPNs, Service Accounts, Managed Service Accounts (gMSA), NTLM protocol & relay mechanisms | `impacket`, `netexec`, `rubeus` |
| | | **Offensive Vectors** | AD Enumeration, Credential Exposure, AS-REP Roasting, Kerberoasting, Delegation Abuse (Unconstrained, Constrained, RBCD), ACL/ACE Abuse, AD CS Abuse (ESC1–ESC8), Privilege Escalation, Lateral Movement, DCSync, Golden & Silver Tickets, Domain Persistence | `certipy`, `mimikatz`, `coercer` |
| | | **Defensive & Monitoring**| Identity Detection, Kerberos Monitoring, LDAP Monitoring, Windows Event Log Analysis (Event IDs 4624, 4672, 4768, 4769, 4771), Attack Path Analysis, AD Hardening & Tiered Architecture | Microsoft Sentinel, Sysmon, Event Viewer |
| **20** | [[Stage-4_Enterprise#module-20-cloud-computing\|Cloud Security]] | **Multi-Cloud Tech** | **AWS:** IAM, EC2, S3, VPC, Lambda, ECS, EKS, Cognito, KMS, Secrets Manager, CloudTrail, CloudWatch, API Gateway, Route 53, ECR<br>**Azure:** Entra ID, Azure IAM, VMs, Storage, Functions, Key Vault, AKS, Defender<br>**GCP:** IAM, Compute Engine, Cloud Storage, GKE, Cloud Functions, Secret Manager, Cloud Logging | AWS CLI, Azure CLI, gcloud CLI |
| | | **Cloud Attacks** | IAM Misconfiguration, Identity Attack Paths, Storage Bucket Exposure, Instance Metadata Service (IMDSv1 vs IMDSv2), SSRF to Cloud Metadata, Cloud Credential Extraction, Role & Permission Abuse, Cross-Account Access, Cloud Persistence, Cloud Trail/Logging Evasion | `pacu`, `scoutsuite`, `prowler` |
| **21** | [[Stage-4_Enterprise#module-21-container--orchestration-security\|Containers & Kubernetes]] | **Docker Containers** | Container Images, Runtimes, Dockerfile Security, Private Registries, Container Networking, Volumes, Linux Capabilities, Privileged Containers, Docker Socket Exposure | Docker CLI, `trivy`, `dive` |
| | | **Kubernetes (K8s)** | Pods, Services, Deployments, Ingress Controllers, K8s API Server, RBAC Roles & RoleBindings, ServiceAccounts, Secrets, ConfigMaps, Network Policies, Admission Controllers, Namespaces | `kubectl`, `kube-bench`, `peirates` |
| | | **Security & Attacks** | Container Breakout / Escape to Host, Kubernetes Cluster Privilege Escalation, ServiceAccount Token Abuse, Secret Leakage, Image Supply Chain Attacks, Cluster Security Hardening, Runtime Threat Detection | Falco, `cdk-go` |
| **22** | [[Stage-4_Enterprise#module-22-adversary-emulation--purple-teaming\|Adversary Emulation]] | **Attack Lifecycle** | MITRE ATT&CK Framework: Initial Access → Execution → Persistence → Privilege Escalation → Defense Evasion → Credential Access → Discovery → Lateral Movement → Collection → Command & Control → Exfiltration → Impact | MITRE ATT&CK Navigator |
| | | **Emulation Tradecraft** | Cyber Kill Chain, Diamond Model, Attack Path Development, Adversary Emulation, Identity Attack Paths, Cloud Attack Paths, Hybrid Environment Attacks, Detection Validation, Purple Teaming collaboration, Campaign Planning | `atomic-red-team`, `caldera` |
| **23** | [[Stage-4_Enterprise#module-23-sniffing--spoofing\|Lateral Movement & Sniffing]] | **Lateral Movement** | SMB, RDP, SSH, WinRM, WMI, RPC, Remote Services Execution, Credential Reuse, Pass-the-Hash (`PtH`), Pass-the-Ticket (`PtT`), Overpass-the-Hash, Kerberos Abuse, Remote Administration Protocols | `impacket`, `netexec`, `crackmapexec` |
| | | **Sniffing & Spoofing** | ARP Poisoning, Network MITM, LLMNR & NBT-NS Spoofing, Network Traffic Interception, Credential Capture in Transit | `responder`, `bettercap`, Wireshark |
| **24** | [[Stage-4_Enterprise#module-24-social-engineering\|Social Engineering]] | **Vectors & Delivery** | Phishing, Spear Phishing, Vishing, Smishing, Pretexting, Physical Facility Access, Tailgating, Baiting, Malicious USB Drops, Credential Harvesting Infrastructure | `gophish`, `setoolkit` |
| | | **Methodology** | OSINT-Driven Target Profiling, Psychological Pretext Construction, Defensive Awareness Training, Bypassing Secure Email Gateways (SEG) | OSINT tools, Canva / Email builders |
| **25** | [[Stage-4_Enterprise#module-25-malware--weaponization-conceptual\|Malware & C2 Architectures]] | **Malware Analysis** | Malware Families (Viruses, Worms, Trojans, RATs, Stealers, Loaders, Botnets, Ransomware, Rootkits, Infostealers), Static Analysis, Dynamic Analysis, Behavioral Analysis, Configuration Extraction, Persistence, IOC/IOA Extraction, Sandbox Analysis, Memory Analysis, Network Analysis | `yara`, `sigma`, Any.Run, Hybrid Analysis |
| | | **C2 Infrastructure** | C2 Architecture, HTTP/S, DNS Tunneling, WebSockets, Custom Protocols, Encrypted Channels, Beaconing Intervals & Jitter, Redirectors, Infrastructure Domain Management & Domain Fronting, Traffic Analysis, C2 Detection | `sliver`, `mythic`, `cobalt-strike`, `metasploit`, `havoc`, `empire` |
| **26** | [[Stage-4_Enterprise#module-26-pentest-methodologies--report-writing\|Pentest Reporting]] | **Methodology & RoE** | Pentest Methodologies (PTES, NIST SP 800-115, OWASP), Scoping Questionnaires, Rules of Engagement (RoE), Legal & Compliance Boundaries | PTES Framework |
| | | **Technical Delivery** | Executive Summaries, Technical Writing, Vulnerability Documentation, Reproducible PoC Steps, CVSS v3.1/v4.0 Risk Rating, Remediation Recommendations, Professional Client Debriefing | Markdown / LaTeX templates |

---

### 🔬 STAGE 5 — SPECIALIZED
*Modules 27–30 · ~15–22 weeks*

| # | Module / Sub-Track | Category / Domain | Core Concepts & Technical Scope | Key Tools & Standards |
|:--:|--------------------|-------------------|---------------------------------|-----------------------|
| **27** | [[Stage-5_Specialized#module-27-offensive-development--tooling\|Offensive Development]] | **Exploit Dev** | Memory Corruption, Stack & Heap Exploitation, Pointers, Buffer Overflows, Heap Corruption, Use-After-Free (`UAF`), Double Free, Integer Overflows, Format String Vulnerabilities, Type Confusion, Race Conditions; Mitigations & Bypasses (`ASLR`, `DEP/NX`, `Stack Canaries`, `PIE`, `RELRO`, `CFG/CFI`, Sandboxing); ROP Chains, JOP, Memory Leaks, Exploit Reliability, Browser & Kernel Exploitation | `gdb`, `pwntools`, `mona.py`, Visual Studio, GCC/Clang |
| | | **Tool Development** | Custom Security Tool Authoring in Python, Bash, PowerShell, C/C++, Go, Rust; Recon Tools, Port Scanners, HTTP Clients, API Testing Tools, Fuzzers, Parsers, Enumeration Frameworks, Log Analyzers, Malware Analysis Utilities, Automated Recon Pipelines | Python, Go, Rust, C++ |
| **27** | **Reverse Engineering** *(Parallel Track)* | **Binary Formats** | PE (Portable Executable), ELF, Mach-O, DLLs, Shared Libraries | `PEview`, `readelf`, Hex Editors |
| | | **Analysis & Evasion** | Disassembly, Decompilation, Debugging, Control Flow Analysis, Data Flow Analysis, API Analysis, Strings, Imports/Exports; x86, x64, ARM, ARM64 architectures; Packing, Code Obfuscation, Anti-Debugging, Anti-VM, Control Flow Flattening, Binary Patching, Hooking, Runtime Analysis | `ghidra`, `ida-pro`, `binary-ninja`, `radare2`, `x64dbg`, `windbg` |
| **27** | **Fuzzing & Vuln Research** *(Parallel Track)* | **Fuzzing Mechanics** | Black-Box, White-Box, Grey-Box Fuzzing, Mutation-Based vs Generation-Based Fuzzing, Coverage-Guided Fuzzing, Protocol Fuzzing, File Format Fuzzing, API Fuzzing, Web Fuzzing, Binary Fuzzing, Crash Triage, Corpus Management, Sanitizers (`ASan`, `MSan`, `UBSan`) | `afl++`, `libfuzzer`, `honggfuzz`, `boofuzz` |
| | | **Vuln Research** | Attack Surface Research, Bug Discovery, Root Cause Analysis, Variant Analysis, Patch Diffing, Protocol Research, Parser Analysis, Memory Corruption, Logic Bugs, Supply Chain Vulnerabilities, CVE/CWE/CVSS Analysis, Responsible Disclosure | `semgrep`, `ghidra`, BinDiff |
| | | **Protocols & Source** | SAST, Secure Code Review, Logic Flaw Discovery, Dependency Scanning, Secret Scanning; Industrial Protocols (`Modbus`, `DNP3`, `OPC`), Telecom Signaling (`SS7`, `Diameter`, `IMS`, `VoLTE`) | Wireshark, Protocol Analyzers |
| **28** | [[Stage-5_Specialized#module-28-ai--llm-red-teaming\|AI & LLM Red Teaming]] | **AI Foundations** | Machine Learning, Deep Learning, Neural Networks, Transformers, LLMs, Embeddings, Vector Databases, Retrieval-Augmented Generation (`RAG`), AI Agents, Tool/Function Calling, Model APIs, Agent Memory | LangChain, LlamaIndex, OpenAI / Anthropic APIs |
| | | **LLM Vulnerabilities**| Direct Prompt Injection, Indirect Prompt Injection, Jailbreaks, Sensitive Information Disclosure, System Prompt Leakage, Insecure Output Handling, Excessive Agency, Data & Model Poisoning, Vector / Embedding Weaknesses, Unbounded Consumption | OWASP Top 10 for LLM, `garak`, `pyrit` |
| | | **Agent & RAG Security**| AI Agent Architecture, Agent Identity & Permissions, Tool Abuse & Privilege Escalation, Context Poisoning, Memory Poisoning, Agent-to-Agent Security, Tool Boundary Enforcement, Human-in-the-Loop Bypasses, Agent Sandboxing, Agent Supply Chain, Autonomous Security Testing | Custom AI Red Teaming testbeds |
| **28** | **Modern Attack Surfaces** *(Parallel Track)* | **Cloud-Native & CI/CD**| Containers, Serverless, Service Mesh, Edge Computing, API Ecosystems, Microservices, Immutable Infrastructure, Secret Management, Zero Trust; Secure SDLC, Source Code Security, SAST/DAST/SCA, Secret Scanning, CI/CD Pipeline Security, Git Security, Container & IaC Security, SBOM, Software Signing, Dependency Confusion, Supply Chain Attacks | Semgrep, Trivy, Cosign, Syft |
| | | **Web3 & Blockchain** | Blockchain Architecture, Ethereum & EVM, Solidity, Smart Contracts, Wallets, Tokens, DeFi Protocols, Oracles, Bridges, Signatures; Reentrancy, Access Control Flaws, Integer Issues, Oracle Manipulation, Flash Loans, Signature Abuse, Smart Contract Logic Flaws, Blockchain Forensics | `slither`, `mythril`, Foundry, Remix |
| | | **IoT & Embedded** | Embedded Systems, Firmware Internals, Bootloaders, Hardware Interfaces (`UART`, `SPI`, `I2C`, `JTAG`), Hardware Debugging, Firmware Extraction, Firmware Analysis, Secure Boot Bypasses, OTA Updates, Device Authentication, IoT Network Security | `binwalk`, Saleae Logic, JTAGulator |
| | | **Emerging Attack Vectors**| AI Agents, Autonomous Coding Agents, AI Tool Interfaces, Agent Skills, Model Context Protocol (`MCP`) Security, WebAssembly (`Wasm`), Passkeys, Modern Authentication, Connected Devices | MCP Inspector, Browser DevTools |
| **29** | [[Stage-5_Specialized#module-29-red-team-operations--tradecraft\|Red Team Operations]] | **Red Team Ops** | Attack Path Development, Adversary Emulation, Identity Attack Paths, Cloud Attack Paths, Hybrid Environment Attacks, Detection Validation, Purple Teaming, Full Campaign Planning & Execution | Cobalt Strike, Sliver, Mythic |
| | | **OPSEC** | Personal OPSEC, Infrastructure OPSEC, Identity Separation, Metadata Awareness, Compartmentalization, Secure Communications, Logging Awareness, Infrastructure Hygiene, Operational Security Failures | Tor, Disposable VPS, Redirection infra |
| **29** | **Defensive Awareness** *(Parallel Track)* | **DFIR** | Disk Forensics, Memory Forensics, Network Forensics, Windows / Linux / Browser / Email / Mobile Forensics, Evidence Preservation, Timeline Analysis, Incident Response Triage, Containment, Eradication, Recovery, Root Cause Analysis, IOC Analysis, Malware Investigation | `volatility`, `autopsy`, `ftk`, Wireshark |
| | | **SOC / SIEM / EDR** | Detection Engineering, Alert Triage, Incident Investigation, SOC Workflows, Log Ingestion, Correlation Rules, Event Normalization, Alert Logic, Sigma Rules, Endpoint Detection, Behavioral Detection, XDR, Automated Response Actions | Splunk, Elastic SIEM, Sigma rules |
| | | **Threat Hunting** | Hypothesis-Driven Hunting, IOC Hunting, Behavioral Hunting, MITRE ATT&CK Mapping, YARA, Sigma, Endpoint & Network Telemetry, Detection Coverage Mapping | YARA, Sysmon, Velociraptor |
| **29** | **Intelligence** *(Parallel Track)* | **Threat Intelligence** | Threat Actors, Campaigns, Malware Families, Infrastructure, IOCs, IOAs, TTPs, Domains, IPs, Hashes, Infrastructure Correlation, Threat Attribution, Threat Intelligence Reports, MITRE ATT&CK Mapping | MISP, OpenCTI, MITRE ATT&CK |
| | | **OSINT & Digital Intel**| Search Intelligence, Domain & DNS Intelligence, Username & Email Intel, Public Records, Exif Metadata, Image & Video Geolocation, Social Media Intelligence, Infrastructure Intel, Breach Intelligence, Digital Footprinting | `maltego`, `spiderfoot`, `shodan`, `censys` |
| | | **Dark Web Intel** | Tor, Onion Services, Privacy Networks, Underground Markets, Cybercrime Ecosystems, Threat Actor Communities, Leak Ecosystems, Initial Access Markets, Credential Markets, Ransomware Ecosystems, Cryptocurrency Forensics | Tor Browser, Dark Web scrapers |
| **30** | [[Stage-5_Specialized#module-30-proof-of-work--career-portfolio\|Proof of Work & Career]] | **Hands-on & Labs** | PortSwigger Web Security Academy, DVWA, PentesterLab; Hack The Box (`HTB`), TryHackMe (`THM`), VulnHub, Proving Grounds; Binary Exploitation (Reverse/Pwn); Enterprise Labs (Active Directory & Multi-Cloud) | HTB Pro Labs, PortSwigger Academy |
| | | **Engagements & CVEs** | Penetration Testing Methodologies, Scope Definition, RoE, Exploitation & Post-Exploitation, Client-Ready Reporting, Remediation Guidance; CVE Process, Coordinated Vulnerability Disclosure, Vendor Communication, Advisory Writing | Mitre CVE program, GitHub Advisories |
| | | **Security Research**| Source Code Auditing, Technical Papers, CVE Analysis, Vulnerability Reproduction, PoC Modification, Crash Debugging, Patch Diffing, Variant Finding, Custom Fuzzers, Novel Vulnerability Discovery | GitHub, Exploit-DB, Packet Storm |
| | | **Portfolio & Writing**| Research Papers, Blog Posts, CVE Write-ups, Tool Documentation, Lab Reports, Conference Submissions, Open Source Security Tool Contributions, Public GitHub Portfolio, Industry Certifications | GitHub, Medium / Substack, GitBook |

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
| S18 | [[Shelf_Post-Hire#shelf-18-automotive-security\|Automotive Security]] | CAN Bus, ECU, Telematics, Automotive Forensics |
| S19 | [[Shelf_Post-Hire#shelf-19-telecom-security\|Telecom Security]] | GSM, 4G/5G, SS7, SIM Security, VoLTE |
| S20 | [[Shelf_Post-Hire#shelf-20-advanced-linux-internals\|Advanced Linux Internals]] | Kernel Modules, Container Escape, Linux Persistence |
| S21 | [[Shelf_Post-Hire#shelf-21-advanced-windows-internals\|Advanced Windows Internals]] | Windows Memory Forensics, Token Security, Service Security |

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

