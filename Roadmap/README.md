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
| **01** | [Fundamentals](Stage-1_Foundation.md#module-01-fundamentals) — Hardware, OS, Memory, Data Rep, Programming | 🔴 | Foundation | 2–3 wks |
| **02** | [Linux Administration](Stage-1_Foundation.md#module-02-linux-administration) | 🔴 | Foundation | 2–3 wks |
| **03** | [Windows Administration](Stage-1_Foundation.md#module-03-windows-administration) | 🟡 | Foundation | 1–2 wks |
| **04** | [Networking Fundamentals](Stage-1_Foundation.md#module-04-networking-fundamentals) | 🔴 | Foundation | 2–3 wks |
| **05** | [Cryptography](Stage-1_Foundation.md#module-05-cryptography) — core concepts + attacks | 🔴 | Foundation | 1–2 wks |
| **06** | [Authentication Standards](Stage-1_Foundation.md#module-06-authentication-standards) — Sessions, JWT, OAuth, MFA | 🔴 | Foundation | 1–2 wks |
| **07** | [Web Technology Fundamentals](Stage-1_Foundation.md#module-07-web-technology-fundamentals) — HTTP, Cookies, CORS, REST | 🔴 | Foundation | 1–2 wks |
| | **— [Foundation Proof Gate](Stage-1_Foundation.md#foundation-proof-gate) —** *(10 PCAPs, admin baselines, 3 scripts, lab report)* | | | **~2–3 mos** |
| **08** | [Footprinting & Reconnaissance](Stage-2_Offense-I.md#module-08-footprinting--reconnaissance) | 🔴 | Offense I | 1–2 wks |
| **09** | [Scanning](Stage-2_Offense-I.md#module-09-scanning) | 🔴 | Offense I | 1 wk |
| **10** | [Enumeration](Stage-2_Offense-I.md#module-10-enumeration) | 🔴 | Offense I | 1–2 wks |
| **11** | [Database Security](Stage-2_Offense-I.md#module-11-database-security) | 🟡 | Offense I | 1 wk |
| **12** | [Password Cracking & Hash Analysis](Stage-2_Offense-I.md#module-12-password-cracking--hash-analysis) | 🔴 | Offense I | 1 wk |
| **13** | [System Hacking & Initial Compromise](Stage-2_Offense-I.md#module-13-system-hacking--initial-compromise) | 🔴 | Offense I | 2–3 wks |
| | **— [Stage Gate 1](Stage-2_Offense-I.md#stage-gate-1) —** *(root a box, dump & crack a hash, escalate privesc)* | | | **~5–6 wks** |
| **14** | [Web Application Hacking](Stage-3_Web-and-App-Sec.md#module-14-web-application-hacking) — SQLi, XSS, SSRF, IDOR, XXE | 🔴 | Web & App Sec | 3–4 wks |
| **15** | [Session Hijacking & Token Attacks](Stage-3_Web-and-App-Sec.md#module-15-session-hijacking--token-attacks) — Cookies, JWTs, Fixation | 🔴 | Web & App Sec | 1–2 wks |
| **16** | [Web Server Hacking](Stage-3_Web-and-App-Sec.md#module-16-web-server-hacking) — Misconfig, Directory Traversal | 🔴 | Web & App Sec | 1–2 wks |
| **17** | [API Security](Stage-3_Web-and-App-Sec.md#module-17-api-security) — OWASP API Top 10, REST/GraphQL/gRPC | 🔴 | Web & App Sec | 2 wks |
| **18** | [Bug Bounty Methodology](Stage-3_Web-and-App-Sec.md#module-18-bug-bounty-methodology) — Scope, Recon, Exploit, Report | 🔴 | Web & App Sec | 2 wks |
| | *(parallel, absorb only — never block)* [Detection Awareness](Stage-3_Web-and-App-Sec.md#side-track-a-detection-engineering--soc-operations), [IDS/Honeypots](Stage-3_Web-and-App-Sec.md#side-track-b-ids-firewalls-and-honeypots), [OSINT](Stage-3_Web-and-App-Sec.md#side-track-c-cyber-threat-intelligence-cti--attack-surface-management) | 🟡 | side-track | ongoing |
| | **— [Stage Gate 2](Stage-3_Web-and-App-Sec.md#stage-gate-2) —** *(3+ HTB/THM writeups, OWASP Top 10 hands-on, Linux+Windows privesc demonstrated cold)* | | | **~8–10 wks** |
| **19** | [Active Directory & Entra ID](Stage-4_Enterprise.md#module-19-active-directory--entra-id) *(+ deferred Kerberos patch from #03)* | 🔴 | Enterprise | 3–4 wks |
| **20** | [Cloud Computing](Stage-4_Enterprise.md#module-20-cloud-computing) *(+ deferred Cloud Assets patch from #04)* | 🔴 | Enterprise | 2–3 wks |
| **21** | [Container & Orchestration Security](Stage-4_Enterprise.md#module-21-container--orchestration-security) | 🟡 | Enterprise | 1–2 wks |
| **22** | [Adversary Emulation & Purple Teaming](Stage-4_Enterprise.md#module-22-adversary-emulation--purple-teaming) | 🔴 | Enterprise | 2 wks |
| **23** | [Sniffing & Spoofing](Stage-4_Enterprise.md#module-23-sniffing--spoofing) — ARP, MITM, Bettercap, Responder | 🟡 | Enterprise | 1 wk |
| **24** | [Social Engineering](Stage-4_Enterprise.md#module-24-social-engineering) — Phishing, Vishing, Physical | 🟡 | Enterprise | 1 wk |
| **25** | [Malware & Weaponization](Stage-4_Enterprise.md#module-25-malware--weaponization-conceptual) *(conceptual — full build is #27)* | 🔵 | Enterprise | 1 wk |
| **26** | [Pentest Methodologies & Report Writing](Stage-4_Enterprise.md#module-26-pentest-methodologies--report-writing) | 🔴 | Enterprise | 1–2 wks |
| | **— [Stage Gate 3](Stage-4_Enterprise.md#stage-gate-3) —** *(AD domain attacked end-to-end, BloodHound exports in Git, 1 professional report)* | | | **~10–13 wks** |
| **27** | [Offensive Development & Tooling](Stage-5_Specialized.md#module-27-offensive-development--tooling) — C2, Shellcode, AMSI/ETW | 🔴 | Specialized | 4–6 wks |
| **28** | [AI & LLM Red Teaming](Stage-5_Specialized.md#module-28-ai--llm-red-teaming) — Prompt Injection, RAG, Agentic Exploits | 🔴 | Specialized | 3–4 wks |
| **29** | [Red Team Operations & Tradecraft](Stage-5_Specialized.md#module-29-red-team-operations--tradecraft) — C2, OPSEC, Campaign | 🔴 | Specialized | 4–6 wks |
| **30** | [Proof of Work & Career Portfolio](Stage-5_Specialized.md#module-30-proof-of-work--career-portfolio) — Certs, GitHub, Bug Bounties | 🔴 | Specialized | 4–6 wks |
| | **— [Final Gate](Stage-5_Specialized.md#final-gate) —** *(custom C2 in lab, published AI security research, 3+ reports, OSCP)* | | | **~15–22 wks** |

> **Total realistic estimate: ~10–14 months** of consistent daily sessions. Drift, passive reading instead of lab time, or skipping stage gates will stretch this significantly.

---

## 🗺️ Topics — Mapped to Execution Order

> Topics listed per module, in the exact sequence you walk them.

---

### 🔵 S T A G E   1   —   F O U N D A T I O N
*Modules 01–07 · ~2–3 months*

---

#### `01` H A R D W A R E   &   C O M P U T E R   A R C H I T E C T U R E

**Hardware**
`CPU Architecture` `x86 / x64` `ARM / ARM64` `CPU Registers` `Instruction Sets` `RAM` `Cache` `Storage` `HDD / SSD / NVMe` `BIOS` `UEFI` `TPM` `Secure Boot` `DMA` `I/O` `PCIe` `USB` `Firmware` `Embedded Controllers`

**Computer Architecture**
`Memory Addressing` `Virtual Memory` `Physical Memory` `Stack` `Heap` `Pointers` `Processes` `Threads` `Context Switching` `Interrupts` `System Calls` `Privilege Rings` `User Mode` `Kernel Mode` `IPC`

---

#### `02` L I N U X

**Internals**
`Kernel` `Processes` `Threads` `Syscalls` `Signals` `File Descriptors` `Sockets` `Pipes` `IPC` `/proc` `/sys` `/dev` `/tmp` `/var` `/etc`

**Security Model**
`Users` `Groups` `Permissions` `ACL` `Capabilities` `SUID` `SGID` `sudo` `Namespaces` `cgroups` `SELinux` `AppArmor`

**Services**
`systemd` `Cron` `SSH` `Services` `Daemons` `Startup Mechanisms`

— **Tools:** `Bash` `strace` `ltrace` `gdb` `lsof` `ss` `ps` `top` `tmux`

---

#### `03` W I N D O W S

**Architecture**
`Win32` `Windows NT` `Processes` `Threads` `DLLs` `Handles` `Tokens` `Services` `Registry` `NTFS` `ACLs` `Named Pipes` `WMI` `COM` `RPC`

**Authentication**
`NTLM` `Kerberos` `Windows Hello` `Credential Providers` `LSASS` `SAM` `LSA` `DPAPI`

**Security**
`UAC` `Windows Defender` `Windows Firewall` `AppLocker` `WDAC` `AMSI` `ETW` `Event Logging` `Security Policies`

**PowerShell**
`PowerShell` `PowerShell Remoting` `Windows Automation` `Security Automation` `PowerShell Logging`

---

#### `04` N E T W O R K I N G

**Core**
`Ethernet` `MAC` `ARP` `IPv4` `IPv6` `ICMP` `TCP` `UDP` `QUIC` `Ports` `Sockets` `Routing` `Switching` `VLAN` `NAT` `PAT` `Subnetting` `CIDR` `MTU` `Fragmentation`

**Protocols**
`DNS` `DHCP` `HTTP` `HTTPS` `TLS` `SSH` `FTP` `SFTP` `SMTP` `IMAP` `POP3` `LDAP` `SMB` `NFS` `SNMP` `RDP` `WinRM` `Kerberos` `NTLM` `SIP` `MQTT` `WebSocket` `gRPC`

**Infrastructure**
`Firewalls` `WAF` `IDS` `IPS` `Load Balancers` `Reverse Proxies` `Forward Proxies` `VPN` `CDN` `DNS Providers` `API Gateways` `Network Segmentation` `Zero Trust` `Service Mesh`

**Packet-Level Skills**
`Packet Capture` `Packet Reconstruction` `TCP Stream Analysis` `DNS Analysis` `TLS Analysis` `Protocol Fingerprinting` `Traffic Anomaly Detection` `Network Forensics`

— **Tools:** `Wireshark` `tcpdump` `Nmap` `Masscan` `Netcat` `Socat` `NSE`

---

#### `05` C R Y P T O G R A P H Y

`Encoding` `Hashing` `Encryption` `Symmetric Cryptography` `AES` `ChaCha20` `RSA` `ECC` `Diffie-Hellman` `Digital Signatures` `HMAC` `PKI` `Certificates` `TLS` `Randomness` `Entropy` `Key Management` `Password Hashing` `bcrypt` `scrypt` `Argon2` `Cryptographic Failures`

---

#### `06` A U T H E N T I C A T I O N   &   I D E N T I T Y

**Authentication**
`Password Authentication` `MFA` `2FA` `Passkeys` `Passwordless` `Biometrics` `Device Authentication` `Session Management`

**Identity**
`OAuth` `OIDC` `SAML` `LDAP` `Kerberos` `Active Directory` `Entra ID` `Identity Providers` `Federation`

**JWT & Token Security**
`JWT Structure` `JWS` `JWE` `Signing` `Verification` `Algorithm Selection` `Key Management` `Claims` `Expiration` `Audience` `Issuer` `Token Rotation` `Refresh Tokens` `Token Revocation` `Authorization Boundaries`

**Authorization**
`Account Recovery` `Session Fixation` `Session Hijacking` `Token Security` `RBAC` `ABAC` `Privileged Access` `Identity Governance`

---

#### `07` W E B   T E C H N O L O G Y   F U N D A M E N T A L S

**Web Fundamentals**
`HTTP` `HTTPS` `Requests` `Responses` `Headers` `Cookies` `Sessions` `Caching` `Browser Security` `Same-Origin Policy` `CORS` `CSP` `WebSockets` `Webhooks`

**Modern Web**
`Service Workers` `WebAssembly` `WebRTC` `GraphQL` `gRPC` `Serverless` `Microservices`
`Reverse Proxy` `CDN` `WAF` `API Gateway` `Load Balancer` `Microservice Communication` `Internal APIs` `Service-to-Service Authentication`

#### `01–07` P R O G R A M M I N G   *(Weekend Track)*
`Python` `Bash` `PowerShell` `JavaScript` `C / C++` `Go` `Rust` `Java` `PHP` `SQL` `Assembly`
`Automation` `Networking` `HTTP` `APIs` `Sockets` `Async` `Multithreading` `Parsing` `Regex` `Exploit Research` `Security Tool Development` `Data Processing`
`Browser Internals` `DOM` `Events` `Fetch` `XHR` `WebSockets` `Node.js` `Client-Side Security`
`Memory` `Pointers` `Structures` `Heap` `Stack` `Memory Management` `Native APIs`

---

### 🟠 S T A G E   2   —   O F F E N S E   I
*Modules 08–13 · ~5–6 weeks*

---

#### `08–10` R E C O N   &   E N U M E R A T I O N

**Infrastructure Recon**
`Domains` `Subdomains` `DNS` `ASN` `IP Ranges` `Cloud Assets` `Certificates` `Technology Stack` `Exposed Services` `Internet-Facing Infrastructure`

**Application Recon**
`Endpoints` `Parameters` `APIs` `JavaScript Files` `Hidden Routes` `Authentication Flows` `Third-Party Integrations` `Mobile Backends`

**Network Recon**
`Reconnaissance` `Scanning` `Enumeration` `Footprinting` `Sniffing` `Spoofing` `ARP Poisoning` `MITM`

— **Tools:** `Amass` `Subfinder` `Assetfinder` `httpx` `Naabu` `Nmap` `Nuclei` `Shodan` `Censys` `Maltego` `SpiderFoot`

---

#### `11` D A T A B A S E   S E C U R I T Y

**SQL:** `MySQL` `PostgreSQL` `MSSQL` `Oracle` `SQLite`
**NoSQL:** `MongoDB` `Redis` `Elasticsearch`
**Security:** `Injection` `Authentication` `Authorization` `Privilege Separation` `Secrets` `Encryption` `Data Exposure` `Backup Security` `Logging` `Database Auditing`

---

#### `12` C R E D E N T I A L   A T T A C K S

`Password Security` `Password Policies` `Brute Force` `Password Spraying` `Credential Stuffing` `Hash Analysis` `NTLM` `Kerberos` `Credential Stores` `Browser Credentials` `SSH Keys` `API Keys` `Cloud Credentials` `Secrets Management`

— **Tools:** `Hashcat` `John the Ripper` `Rubeus` `Mimikatz` `Secretsdump`

---

#### `13` S Y S T E M   H A C K I N G   &   P R I V I L E G E   E S C A L A T I O N

**Linux PrivEsc:** `SUID` `SGID` `sudo` `Capabilities` `Cron` `Services` `PATH` `Permissions` `Credentials` `Containers` `Kernel`
**Windows PrivEsc:** `Services` `Registry` `Tokens` `UAC` `Scheduled Tasks` `DLL Search Order` `WMI` `Named Pipes` `Permissions` `Credentials` `Kernel`

---

### 🟣 S T A G E   3   —   W E B   &   A P P   S E C
*Modules 14–18 · ~8–10 weeks*

---

#### `14–16` W E B   S E C U R I T Y

**Core Vulnerabilities**
`Broken Access Control` `Authentication Failures` `SQL Injection` `NoSQL Injection` `XSS` `CSRF` `SSRF` `XXE` `SSTI` `IDOR / BOLA` `BFLA` `Path Traversal` `Command Injection` `File Upload` `Open Redirect` `Prototype Pollution` `Deserialization` `Race Conditions` `Business Logic Bugs`

**Modern Web Attacks**
`HTTP Request Smuggling` `Web Cache Poisoning` `Web Cache Deception` `Host Header Attacks` `Parser Confusion` `Request Splitting` `Client-Side Desync`

**Session & Token Attacks**
`Session Fixation` `Session Hijacking` `Cookie Tampering` `JWT Attacks` `Token Forgery`

---

#### `17` A P I   S E C U R I T Y

**REST:** `API Discovery` `Authentication` `Authorization` `Object-Level Authorization` `Function-Level Authorization` `Rate Limits` `Pagination` `Filtering` `Mass Assignment` `Versioning` `Error Handling`
**GraphQL:** `Schema` `Queries` `Mutations` `Introspection` `Resolver Security` `Complexity` `Batching`
**Other:** `SOAP` `gRPC` `WebSockets` `Webhooks`
**Identity:** `API Keys` `OAuth 2.0` `OpenID Connect` `JWT` `Access Tokens` `Refresh Tokens` `SAML` `SSO`

---

#### `18` B U G   B O U N T Y   M E T H O D O L O G Y

`Scope Analysis` `Asset Discovery` `Endpoint Discovery` `API Analysis` `Authentication Testing` `Authorization Testing` `Business Logic` `Race Conditions` `Chaining` `Impact Analysis` `Report Writing` `Triage Communication`
Elite: `Unusual Attack Surfaces` `JavaScript Analysis` `API Architecture Understanding` `Business Workflow Analysis` `Low-Severity Chaining` `Novel Logic Flaws` `Research-Driven Hunting`

---

### 🏢 S T A G E   4   —   E N T E R P R I S E
*Modules 19–26 · ~10–13 weeks*

---

#### `19` A C T I V E   D I R E C T O R Y   &   E N T R A   I D

**Architecture:** `Domain` `Forest` `Tree` `Domain Controller` `OU` `Users` `Groups` `GPO` `LDAP` `DNS` `Trusts`
**Authentication:** `Kerberos` `NTLM` `Tickets` `SPNs` `Service Accounts` `Managed Service Accounts`
**Attack Surface:** `Identity ACLs` `Delegation` `Group Membership` `AD CS` `Certificate Templates` `Trust Relationships`
**Offensive:** `Enumeration` `Credential Exposure` `Kerberos Abuse` `NTLM Abuse` `Delegation Abuse` `ACL Abuse` `AD CS Abuse` `Privilege Escalation` `Lateral Movement` `Persistence` `Domain-Level Attack Paths`
**Defensive:** `Identity Detection` `Kerberos Monitoring` `LDAP Monitoring` `Windows Event Analysis` `Attack Path Analysis` `AD Hardening`

— **Tools:** `BloodHound` `Impacket` `NetExec` `Rubeus` `Mimikatz` `Certipy` `PowerView`

---

#### `20` C L O U D   S E C U R I T Y

**AWS:** `IAM` `EC2` `S3` `VPC` `Lambda` `ECS` `EKS` `Cognito` `KMS` `Secrets Manager` `CloudTrail` `CloudWatch` `API Gateway` `Route 53` `ECR`
**Azure:** `Entra ID` `Azure IAM` `Virtual Machines` `Storage` `Functions` `Key Vault` `AKS` `Defender`
**GCP:** `IAM` `Compute` `Cloud Storage` `GKE` `Cloud Functions` `Secret Manager` `Cloud Logging`
**Cloud Attacks:** `IAM Misconfiguration` `Identity Attack Paths` `Storage Exposure` `Metadata Services` `SSRF` `Cloud Credentials` `Role Abuse` `Cross-Account Access` `Cloud Persistence` `Cloud Detection`

---

#### `21` C O N T A I N E R S   &   K U B E R N E T E S

**Docker:** `Images` `Containers` `Dockerfile` `Registry` `Networking` `Volumes` `Capabilities` `Privileges` `Docker Socket`
**Kubernetes:** `Pods` `Services` `Deployments` `Ingress` `API Server` `RBAC` `Service Accounts` `Secrets` `ConfigMaps` `Network Policies` `Admission Controllers` `Namespaces`
**Security:** `Container Escape` `Kubernetes Privilege Escalation` `Identity Abuse` `Secret Exposure` `Image Security` `Cluster Security` `Runtime Detection`

---

#### `22` A D V E R S A R Y   E M U L A T I O N   &   R E D   T E A M I N G

**Attack Lifecycle:** `Reconnaissance` `Initial Access` `Execution` `Persistence` `Defense Evasion` `Credential Access` `Discovery` `Collection` `Command & Control` `Exfiltration` `Impact`
**Advanced:** `Attack Path Development` `Adversary Emulation` `Identity Attack Paths` `Cloud Attack Paths` `Hybrid Environment Attacks` `Detection Validation` `Purple Teaming` `OPSEC` `Campaign Planning`
**Frameworks:** `MITRE ATT&CK` `Cyber Kill Chain` `Diamond Model` `Atomic Red Team` `Caldera`

---

#### `23` L A T E R A L   M O V E M E N T   &   S N I F F I N G

**Lateral Movement:** `SMB` `RDP` `SSH` `WinRM` `WMI` `RPC` `Remote Services` `Credential Reuse` `Pass-the-Hash` `Pass-the-Ticket` `Overpass-the-Hash` `Kerberos Abuse` `Remote Administration`
**Sniffing / Spoofing:** `ARP Poisoning` `MITM` `Responder` `Bettercap` `Network Interception`

---

#### `24` S O C I A L   E N G I N E E R I N G

`Phishing` `Spear Phishing` `Vishing` `Smishing` `Pretexting` `Physical Access` `Tailgating` `Baiting` `OSINT-Driven SE` `Pretext Construction`

---

#### `25` M A L W A R E   &   C 2

**Malware Families:** `Virus` `Worm` `Trojan` `RAT` `Stealer` `Loader` `Botnet` `Ransomware` `Rootkit` `Spyware` `Infostealer`
**Analysis:** `Static Analysis` `Dynamic Analysis` `Behavioral Analysis` `Configuration Extraction` `Persistence` `IOC Extraction` `Sandbox Analysis` `Memory Analysis` `Network Analysis`
**Detection:** `YARA` `Sigma` `Behavioral Detection` `IOC` `IOA` `TTP Mapping`
**C2:** `C2 Architecture` `HTTP/S` `DNS` `WebSocket` `Custom Protocols` `Encrypted Channels` `Beaconing` `Redirectors` `Infrastructure Domain Management` `Traffic Analysis` `C2 Detection`

— **C2 Frameworks:** `Sliver` `Mythic` `Cobalt Strike` `Metasploit` `Havoc` `Empire`

---

#### `26` P E N T E S T   R E P O R T I N G

`Pentest Methodologies` `Scope Definition` `Rules of Engagement` `Technical Writing` `Executive Summaries` `Vulnerability Documentation` `Reproduction Steps` `Risk Rating` `Remediation Recommendations` `Professional Communication`

---

### 🔬 S T A G E   5   —   S P E C I A L I Z E D
*Modules 27–30 · ~15–22 weeks*

---

#### `27` O F F E N S I V E   D E V E L O P M E N T   &   T O O L I N G

**Exploit Development**
`Stack` `Heap` `Pointers` `Memory Corruption` `Information Disclosure`
`Buffer Overflow` `Heap Corruption` `Use-After-Free` `Double Free` `Integer Overflow` `Format String` `Type Confusion` `Race Conditions`
`ASLR` `DEP / NX` `Stack Canaries` `PIE` `RELRO` `CFG` `CFI` `Sandboxing`
`ROP` `JOP` `Memory Leaks` `Exploit Reliability` `Browser Exploitation` `Kernel Exploitation`

**Security Tool Development & Automation**
`Python` `Bash` `PowerShell` `C / C++` `Go` `Rust`
`Recon Tools` `Port Scanners` `HTTP Clients` `API Testing Tools` `Fuzzers` `Parsers` `Enumeration Frameworks` `Log Analyzers` `Malware Analysis Utilities` `Custom Research Tools`
`Recon Automation` `Enumeration` `Asset Discovery` `API Testing` `Vulnerability Scanning` `Log Processing` `Report Generation`

---

#### `27` R E V E R S E   E N G I N E E R I N G   *(parallel to #27)*

**Binary Formats:** `PE` `ELF` `Mach-O` `DLL` `Shared Libraries`
**Analysis:** `Static Analysis` `Dynamic Analysis` `Disassembly` `Decompilation` `Debugging` `Control Flow` `Data Flow` `API Analysis` `Strings` `Imports` `Exports`
**Architecture:** `x86` `x64` `ARM` `ARM64`
**Advanced:** `Packing` `Obfuscation` `Anti-Debugging` `Anti-VM` `Control Flow Obfuscation` `Binary Patching` `Hooking` `Runtime Analysis`

— **Tools:** `Ghidra` `IDA` `Binary Ninja` `radare2` `x64dbg` `WinDbg` `GDB`

---

#### `27` F U Z Z I N G   &   V U L N E R A B I L I T Y   R E S E A R C H   *(parallel to #27)*

**Fuzzing:** `Black-Box` `White-Box` `Grey-Box` `Mutation-Based` `Generation-Based` `Coverage-Guided` `Protocol Fuzzing` `File Format Fuzzing` `API Fuzzing` `Web Fuzzing` `Binary Fuzzing` `Crash Triage` `Corpus Management` `Sanitizers`
**Vulnerability Research:** `Attack Surface Research` `Bug Discovery` `Root Cause Analysis` `Variant Analysis` `Patch Diffing` `Protocol Research` `Parser Analysis` `Memory Corruption` `Logic Bugs` `Race Conditions` `Authentication Research` `Authorization Research` `Supply-Chain Research` `CVE Analysis` `CWE` `CVSS` `Exploitability Analysis` `Responsible Disclosure`
**Source Code Auditing:** `SAST` `Secure Code Review` `Logic Flaw Discovery` `Patch Diffing` `Variant Analysis` `Dependency Analysis` `Secret Scanning` `API Surface Analysis` `Authentication Review` `Authorization Review`
**Protocol Research:** `Protocol Fuzzing` `Protocol Fingerprinting` `Custom Protocol Analysis` `Packet-Level Reconstruction` `Parser Analysis` `Modbus` `DNP3` `OPC` `Industrial Protocols` `Telecom Signaling` `SS7` `Diameter` `IMS` `VoLTE`

---

#### `28` A I   &   L L M   R E D   T E A M I N G

**AI Foundations:** `Machine Learning` `Deep Learning` `Neural Networks` `Transformers` `LLMs` `Embeddings` `Vector Databases` `RAG` `AI Agents` `Tool Calling` `Function Calling` `Model APIs` `Agent Memory`
**LLM Security:** `Prompt Injection` `Indirect Prompt Injection` `Jailbreaks` `Sensitive Information Disclosure` `System Prompt Leakage` `Insecure Output Handling` `Excessive Agency` `Data / Model Poisoning` `Vector / Embedding Weaknesses` `Unbounded Consumption`
**Agent Security:** `AI Agent Architecture` `Agent Identity` `Agent Permissions` `Tool Abuse` `Context Poisoning` `Memory Poisoning` `Agent-to-Agent Security` `Tool Boundary Security` `Human-in-the-Loop` `Agent Sandboxing` `Agent Supply Chain` `Autonomous Security Testing` `AI Red Teaming`
**RAG Security:** `RAG Architecture` `Vector Database Security` `Embedding Weaknesses` `Context Poisoning` `Retrieval Manipulation` `Data Poisoning` `Indirect Prompt Injection via RAG`

---

#### `28` M O D E R N   A T T A C K   S U R F A C E S   *(parallel to #28)*

**Cloud-Native:** `Containers` `Serverless` `Service Mesh` `Edge Computing` `API Ecosystems` `Microservices` `Immutable Infrastructure` `Secret Management` `Cloud Identity` `Zero Trust`
**Supply Chain:** `Secure SDLC` `Source Code Security` `SAST` `DAST` `SCA` `Secret Scanning` `Dependency Security` `Package Security` `CI/CD Security` `Git Security` `Container Security` `IaC Security` `SBOM` `Artifact Security` `Software Signing` `Build Pipeline Security` `Dependency Confusion` `Supply Chain Attacks`
**Web3:** `Blockchain Architecture` `Ethereum` `EVM` `Solidity` `Smart Contracts` `Wallets` `Tokens` `DeFi` `Oracles` `Bridges` `Signatures` `Reentrancy` `Access Control` `Integer Issues` `Oracle Manipulation` `Flash Loan` `Signature Abuse` `Smart Contract Logic` `Wallet Security` `Bridge Security` `Blockchain Forensics`
**IoT & Embedded:** `Embedded Systems` `Firmware` `Bootloaders` `UART` `SPI` `I2C` `JTAG` `Hardware Debugging` `Firmware Extraction` `Firmware Analysis` `Secure Boot` `OTA Updates` `Device Authentication` `IoT Network Security`
**Emerging:** `AI Agents` `Autonomous Coding Agents` `AI Tool Interfaces` `Agent Skills` `MCP Security` `WebAssembly` `Passkeys` `Modern Authentication` `Connected Devices` `Autonomous Systems`

---

#### `29` R E D   T E A M   O P E R A T I O N S   &   O P S E C

**Red Team Operations:** `Attack Path Development` `Adversary Emulation` `Identity Attack Paths` `Cloud Attack Paths` `Hybrid Environment Attacks` `Detection Validation` `Purple Teaming` `Campaign Planning`
**OPSEC:** `Personal OPSEC` `Infrastructure OPSEC` `Identity Separation` `Metadata Awareness` `Compartmentalization` `Secure Communications` `Logging Awareness` `Infrastructure Hygiene` `Operational Security Failures`

---

#### `29` D E F E N S I V E   A W A R E N E S S   *(parallel to #29)*

**DFIR:** `Disk Forensics` `Memory Forensics` `Network Forensics` `Windows Forensics` `Linux Forensics` `Browser Forensics` `Email Forensics` `Mobile Forensics` `Timeline Analysis` `Artifact Analysis` `Evidence Preservation`
`Detection` `Triage` `Investigation` `Containment` `Eradication` `Recovery` `Root Cause Analysis` `IOC Analysis` `Timeline Construction` `Malware Investigation` `Post-Incident Review`
**SOC / SIEM / EDR:** `Detection Engineering` `Alert Triage` `Incident Investigation` `SOC Workflow` `Log Ingestion` `Correlation Rules` `Event Normalization` `Alert Logic` `Sigma Rules` `Endpoint Detection` `Behavioral Detection` `XDR` `Response Actions`
**Threat Hunting:** `Hypothesis-Driven Hunting` `IOC Hunting` `Behavioral Hunting` `MITRE ATT&CK Mapping` `YARA` `Sigma` `Endpoint Telemetry` `Network Telemetry`
**Detection Engineering:** `Detection Logic` `Behavioral Rules` `IOA` `TTP-Based Detection` `Alert Quality` `False Positive Reduction` `Detection Coverage Mapping`

— **Tools:** `Volatility` `Autopsy` `FTK` `Wireshark`

---

#### `29` I N T E L L I G E N C E   *(parallel to #29)*

**Threat Intelligence:** `Threat Actors` `Campaigns` `Malware Families` `Infrastructure` `IOCs` `IOAs` `TTPs` `Domains` `IPs` `Hashes` `Infrastructure Correlation` `Attribution` `Threat Reports` `MITRE ATT&CK Mapping`
**OSINT & Digital Investigation:** `Search Intelligence` `Domain Intelligence` `Username Intelligence` `Email Intelligence` `Public Records` `Metadata` `Image Intelligence` `Video Intelligence` `Social Media Intelligence` `Infrastructure Intelligence` `Breach Intelligence` `Digital Footprinting`
**Dark Web Intelligence:** `Tor` `Onion Services` `Privacy Networks` `Underground Markets` `Cybercrime Ecosystems` `Threat Actor Communities` `Leak Ecosystems` `Malware Ecosystems` `Initial Access Markets` `Credential Markets` `Ransomware Ecosystems` `Cryptocurrency Intelligence` `Dark Web OSINT`
**Threat Actor Research:** `Attribution` `Campaign Analysis` `TTPs` `Infrastructure Correlation` `Malware Families` `Threat Reports` `Actor Profiling` `MITRE ATT&CK Groups`
**Malware Intelligence:** `IOC Extraction` `TTP Mapping` `Configuration Extraction` `C2 Infrastructure` `Malware Families` `Attribution` `Sandbox Reports` `Memory Analysis`

— **Tools:** `Maltego` `SpiderFoot` `Shodan` `Censys`

---

#### `30` P R O O F   O F   W O R K   &   C A R E E R

**CTF:** `Web (PortSwigger, DVWA, PentesterLab)` `Network/System (HTB, THM, VulnHub, Proving Grounds)` `Reverse/Pwn (Binary Exploitation)` `Crypto Challenges` `Forensics (Memory, Disk, Network, Malware)` `OSINT Challenges` `Enterprise (AD Labs, Cloud Labs)`
**Penetration Testing:** `Pentest Methodologies` `Scope Definition` `Rules of Engagement` `Reconnaissance` `Exploitation` `Post-Exploitation` `Reporting` `Remediation Guidance`
**Responsible Disclosure:** `CVE Process` `Coordinated Disclosure` `Vendor Communication` `Advisory Writing` `Timeline Management` `PoC Handling`
**Security Research:** `Read Source Code` `Read Technical Papers` `Read CVEs` `Read Advisories` `Reproduce Vulnerabilities` `Modify PoCs` `Debug Crashes` `Patch Diffing` `Find Variants` `Build Fuzzers` `Analyze Protocols` `Reverse Binaries` `Develop Hypotheses` `Discover Novel Vulnerabilities` `Publish Responsible Research`
**Technical Writing:** `Research Papers` `Blog Posts` `CVE Write-ups` `Tool Documentation` `Lab Reports` `Conference Submissions`
**Open Source Contribution:** `Security Tool Contributions` `Research Publications` `Public PoC Development` `Community Engagement` `GitHub Portfolio`

---



## 📦 Shelf — Self Post-Hire

> These aren't "later in the sequence" — they're off the sequence entirely until you have a job. No number means no claim on your time right now.

| # | Module | Focus Area |
|:-:|--------|------------|
| S01 | [Wireless Network Security](Shelf_Post-Hire.md#shelf-01-wireless-network-security) | WPA2/WPA3, Evil Twin, PMKID |
| S02 | [Mobile Security](Shelf_Post-Hire.md#shelf-02-mobile-platform-pentesting) | Android/iOS, Frida, MobSF, Pinning |
| S03 | [OT / ICS / SCADA Security](Shelf_Post-Hire.md#shelf-03-otics-scada-security) | Modbus, S7comm, Purdue model |
| S04 | [Digital Forensics](Shelf_Post-Hire.md#shelf-04-digital-forensics) | Memory, Disk, Autopsy, Volatility |
| S05 | [Reverse Engineering & Malware Analysis](Shelf_Post-Hire.md#shelf-05-reverse-engineering--malware-analysis) | Ghidra, x64dbg, unpacking |
| S06 | [Modern Exploitation](Shelf_Post-Hire.md#shelf-06-modern-exploitation) | Binary exploitation, ROP, ASLR/DEP |
| S07 | [Hardware Hacking & Embedded Systems](Shelf_Post-Hire.md#shelf-07-hardware-hacking--embedded-systems) | UART, JTAG, Firmware extraction |
| S08 | [Physical Penetration Testing](Shelf_Post-Hire.md#shelf-08-physical-penetration-testing) | Lock picking, RFID cloning, bypass |
| S09 | [VoIP & Telecommunications Security](Shelf_Post-Hire.md#shelf-09-voip--telecommunications-security) | SIP, RTP, SS7/5G concepts |
| S10 | [Blockchain & Web3 Security](Shelf_Post-Hire.md#shelf-10-blockchain--web3-security) | Smart contract audits, reentrancy |
| S11 | [Governance, Risk & Compliance](Shelf_Post-Hire.md#shelf-11-governance-risk--compliance-grc) | ISO 27001, SOC 2, NIST CSF |
| S12 | [Supply Chain Security](Shelf_Post-Hire.md#shelf-12-supply-chain-security) | SBOM, Dependency confusion, SLSA |
| S13 | [DevSecOps & Secure SDLC](Shelf_Post-Hire.md#shelf-13-devsecops--secure-sdlc) | CI/CD pipelines, SAST/DAST, Semgrep |
| S14 | [Secure Code Review Methodology](Shelf_Post-Hire.md#shelf-14-secure-code-review-methodology) | Code auditing, source-level vuln analysis |
| S15 | [Security Architecture & Engineering](Shelf_Post-Hire.md#shelf-15-security-architecture--engineering) | Zero Trust, threat modeling, STRIDE |
| S16 | [Security Operations Expansion](Shelf_Post-Hire.md#shelf-16-security-operations-expansion) | SOAR, DLP, Insider threat |
| S17 | [Denial of Service & Resilience](Shelf_Post-Hire.md#shelf-17-denial-of-service--availability-resilience) | Layer 4/7 mechanisms, Anycast, DDoS mitigation |
| S18 | [Automotive Security](Shelf_Post-Hire.md#shelf-18-automotive-security) | CAN Bus, ECU, Telematics, Automotive Forensics |
| S19 | [Telecom Security](Shelf_Post-Hire.md#shelf-19-telecom-security) | GSM, 4G/5G, SS7, SIM Security, VoLTE |
| S20 | [Advanced Linux Internals](Shelf_Post-Hire.md#shelf-20-advanced-linux-internals) | Kernel Modules, Container Escape, Linux Persistence |
| S21 | [Advanced Windows Internals](Shelf_Post-Hire.md#shelf-21-advanced-windows-internals) | Windows Memory Forensics, Token Security, Service Security |

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

