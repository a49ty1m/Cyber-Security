# 🛡️ Cybersecurity Master Roadmap

> **Career Target:** Penetration Testing → Red Team Operations → Advanced Offensive Security → AI Red Teaming

---

## 📑 Table of Contents

| # | Section |
|:-:|---------|
| 1 | [Execution Order](#execution-order) ← **Start here** |
| 2 | [Shelf — Off Sequence Pre-Employment](#shelf) |
| 3 | [Daily Protocol](#daily-protocol) |
| 4 | [Lab Setup](#lab-setup) |

---

<a id="execution-order"></a>

## 🎯 Execution Order — 5 Stages

> Sequential walk order across 5 Stages, top to bottom. 🔴 = master it before moving on. 🟡 = learn it solid, keep moving. 🔵 = conceptual foundation (hands-on build later in specialized stage).

| # | Module | Depth | Stage |
|:-:|--------|:-----:|-------|
| **01** | [Fundamentals](Stage-1_Foundation.md#module-01-fundamentals) — Hardware, OS, Memory, Data Rep, Programming | 🔴 | Foundation |
| **02** | [Linux Administration](Stage-1_Foundation.md#module-02-linux-administration) | 🔴 | Foundation |
| **03** | [Windows Administration](Stage-1_Foundation.md#module-03-windows-administration) | 🟡 | Foundation |
| **04** | [Networking Fundamentals](Stage-1_Foundation.md#module-04-networking-fundamentals) | 🔴 | Foundation |
| **05** | [Cryptography](Stage-1_Foundation.md#module-05-cryptography) — core concepts + attacks | 🔴 | Foundation |
| **06** | [Authentication Standards](Stage-1_Foundation.md#module-06-authentication-standards) — Sessions, JWT, OAuth, MFA | 🔴 | Foundation |
| **07** | [Web Technology Fundamentals](Stage-1_Foundation.md#module-07-web-technology-fundamentals) — HTTP, Cookies, CORS, REST | 🔴 | Foundation |
| | **— [Foundation Proof Gate](Stage-1_Foundation.md#foundation-proof-gate) —** *(10 PCAPs, admin baselines, 3 scripts, lab report)* | | |
| **08** | [Footprinting & Reconnaissance](Stage-2_Offense-I.md#module-08-footprinting--reconnaissance) | 🔴 | Offense I |
| **09** | [Scanning](Stage-2_Offense-I.md#module-09-scanning) | 🔴 | Offense I |
| **10** | [Enumeration](Stage-2_Offense-I.md#module-10-enumeration) | 🔴 | Offense I |
| **11** | [Database Security](Stage-2_Offense-I.md#module-11-database-security) | 🟡 | Offense I |
| **12** | [Password Cracking & Hash Analysis](Stage-2_Offense-I.md#module-12-password-cracking--hash-analysis) | 🔴 | Offense I |
| **13** | [System Hacking & Initial Compromise](Stage-2_Offense-I.md#module-13-system-hacking--initial-compromise) | 🔴 | Offense I |
| | **— [Stage Gate 1](Stage-2_Offense-I.md#stage-gate-1) —** *(root a box, dump & crack a hash, escalate privesc)* | | |
| **14** | [Web Application Hacking](Stage-3_Web-and-App-Sec.md#module-14-web-application-hacking) — SQLi, XSS, SSRF, IDOR, XXE | 🔴 | Web & App Sec |
| **15** | [Session Hijacking & Token Attacks](Stage-3_Web-and-App-Sec.md#module-15-session-hijacking--token-attacks) — Cookies, JWTs, Fixation | 🔴 | Web & App Sec |
| **16** | [Web Server Hacking](Stage-3_Web-and-App-Sec.md#module-16-web-server-hacking) — Misconfig, Directory Traversal | 🔴 | Web & App Sec |
| **17** | [API Security](Stage-3_Web-and-App-Sec.md#module-17-api-security) — OWASP API Top 10, REST/GraphQL/gRPC | 🔴 | Web & App Sec |
| **18** | [Bug Bounty Methodology](Stage-3_Web-and-App-Sec.md#module-18-bug-bounty-methodology) — Scope, Recon, Exploit, Report | 🔴 | Web & App Sec |
| | *(parallel, absorb only — never block)* [Detection Awareness](Stage-3_Web-and-App-Sec.md#side-track-a-detection-engineering--soc-operations), [IDS/Honeypots](Stage-3_Web-and-App-Sec.md#side-track-b-ids-firewalls-and-honeypots), [OSINT](Stage-3_Web-and-App-Sec.md#side-track-c-cyber-threat-intelligence-cti--attack-surface-management) | 🟡 | side-track |
| | **— [Stage Gate 2](Stage-3_Web-and-App-Sec.md#stage-gate-2) —** *(3+ HTB/THM writeups, OWASP Top 10 hands-on, Linux+Windows privesc demonstrated cold)* | | |
| **19** | [Active Directory & Entra ID](Stage-4_Enterprise.md#module-19-active-directory--entra-id) *(+ deferred Kerberos patch from #03)* | 🔴 | Enterprise |
| **20** | [Cloud Computing](Stage-4_Enterprise.md#module-20-cloud-computing) *(+ deferred Cloud Assets patch from #04)* | 🔴 | Enterprise |
| **21** | [Container & Orchestration Security](Stage-4_Enterprise.md#module-21-container--orchestration-security) | 🟡 | Enterprise |
| **22** | [Adversary Emulation & Purple Teaming](Stage-4_Enterprise.md#module-22-adversary-emulation--purple-teaming) | 🔴 | Enterprise |
| **23** | [Sniffing & Spoofing](Stage-4_Enterprise.md#module-23-sniffing--spoofing) — ARP, MITM, Bettercap, Responder | 🟡 | Enterprise |
| **24** | [Social Engineering](Stage-4_Enterprise.md#module-24-social-engineering) — Phishing, Vishing, Physical | 🟡 | Enterprise |
| **25** | [Malware & Weaponization](Stage-4_Enterprise.md#module-25-malware--weaponization-conceptual) *(conceptual — full build is #27)* | 🔵 | Enterprise |
| **26** | [Pentest Methodologies & Report Writing](Stage-4_Enterprise.md#module-26-pentest-methodologies--report-writing) | 🔴 | Enterprise |
| | **— [Stage Gate 3](Stage-4_Enterprise.md#stage-gate-3) —** *(AD domain attacked end-to-end, BloodHound exports in Git, 1 professional report)* | | |
| **27** | [Offensive Development & Tooling](Stage-5_Specialized.md#module-27-offensive-development--tooling) — C2, Shellcode, AMSI/ETW | 🔴 | Specialized |
| **28** | [AI & LLM Red Teaming](Stage-5_Specialized.md#module-28-ai--llm-red-teaming) — Prompt Injection, RAG, Agentic Exploits | 🔴 | Specialized |
| **29** | [Red Team Operations & Tradecraft](Stage-5_Specialized.md#module-29-red-team-operations--tradecraft) — C2, OPSEC, Campaign | 🔴 | Specialized |
| **30** | [Proof of Work & Career Portfolio](Stage-5_Specialized.md#module-30-proof-of-work--career-portfolio) — Certs, GitHub, Bug Bounties | 🔴 | Specialized |
| | **— [Final Gate](Stage-5_Specialized.md#final-gate) —** *(custom C2 in lab, published AI security research, 3+ reports, OSCP)* | | |

---

<a id="shelf"></a>

## 📦 Shelf — Not Numbered, Not Touched Pre-Employment

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

---

<a id="daily-protocol"></a>

## ⏱️ Daily Protocol

> One question answered every morning: **"What is my current module and what am I proving today?"**

### Daily Activities

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
