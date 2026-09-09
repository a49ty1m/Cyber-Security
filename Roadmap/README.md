# 🛡️ Cybersecurity Master Roadmap

> **Career Target:** Penetration Testing → Red Team Operations → Advanced Offensive Security → AI Red Teaming

---

## 📑 Table of Contents

| # | Section |
|:-:|---------|
| 1 | [Execution Order](#-execution-order--renumbered) ← **Start here** |
| 2 | [Shelf — Off Sequence Pre-Employment](#-shelf--not-numbered-not-touched-pre-employment) |
| 3 | [Daily Protocol](#️-daily-protocol) |
| 4 | [Lab Setup](#️-lab-setup) |

---

## 🎯 Execution Order — Renumbered

> Old numbering (Part 4, Part 31, Part 6B, Part 16 living in Phase 6...) was never sequential — it was archival metadata. This is your actual walk order, top to bottom, nothing else. 🔴 = master it before moving on. 🟡 = learn it solid, keep moving. Cut items from the shelf table are simply gone — not listed, not owed to anyone.

| # | Module | Depth | Stage |
|:-:|--------|:-----:|-------|
| **01** | [Fundamentals](Phase-1.md#part-1-fundamentals) — Hardware, OS, Memory, Data Rep, Programming | 🔴 | Foundation |
| **02** | [Linux Administration](Phase-1.md#part-1b-linux-administration) | 🔴 | Foundation |
| **03** | [Windows Administration](Phase-1.md#part-1c-windows-administration) *(core — Stages 1–4)* | 🟡 | Foundation |
| **04** | [Networking Fundamentals](Phase-1.md#part-2-networking-fundamentals) | 🔴 | Foundation |
| **05** | [Cryptography](Phase-1.md#part-3-cryptography) — core concepts + attacks | 🔴 | Foundation |
| **06** | [Authentication Standards](Phase-1.md#part-3b-authentication-standards-primer) — Sessions, JWT, OAuth, MFA | 🔴 | Foundation |
| **07** | [Web Technology Fundamentals](Phase-1.md#part-3c-web-technology-fundamentals) — HTTP, Cookies, CORS, REST | 🔴 | Foundation |
| | **— Foundation Proof Gate —** *(10 PCAPs, admin baselines, 3 scripts, lab report)* | | |
| **08** | [Footprinting & Reconnaissance](Phase-2.md#part-4-footprinting-and-reconnaissance) | 🔴 | Offense I |
| **09** | [Scanning](Phase-2.md#part-5-scanning) | 🔴 | Offense I |
| **10** | [Enumeration](Phase-2.md#part-6-enumeration) | 🔴 | Offense I |
| **11** | [Database Security](Phase-2.md#part-6b-database-security) | 🟡 | Offense I |
| **12** | [Password Cracking & Hash Analysis](Phase-2.md#part-31-password-cracking-hash-analysis) | 🔴 | Offense I |
| **13** | [System Hacking & Initial Compromise](Phase-2.md#part-7-system-hacking-initial-compromise) | 🔴 | Offense I |
| | **— Stage Gate 1 —** *(root a box, dump & crack a hash, escalate privesc)* | | |
| **14** | [Web Application Hacking](Phase-4.md#part-17-web-application-hacking) — SQLi, XSS, SSRF, IDOR, XXE | 🔴 | Web & App Sec |
| **15** | [Session Hijacking & Token Attacks](Phase-4.md#part-12-session-hijacking) — Cookies, JWTs, Fixation | 🔴 | Web & App Sec |
| **16** | [Web Server Hacking](Phase-4.md#part-18-web-server-hacking) — Misconfig, Directory Traversal | 🔴 | Web & App Sec |
| **17** | [API Security](Phase-4.md#part-19-api-security) — OWASP API Top 10, REST/GraphQL/gRPC | 🔴 | Web & App Sec |
| **18** | [Bug Bounty Methodology](Phase-4.md#part-20-bug-bounty-methodology) — Scope, Recon, Exploit, Report | 🔴 | Web & App Sec |
| | *(parallel, absorb only — never block)* [Detection Awareness](Phase-3.md#part-13a-detection-engineering-soc-operations), [IDS/Honeypots](Phase-3.md#part-14-ids-firewalls-and-honeypots), [OSINT](Phase-3.md#part-15-osint-threat-intelligence) | 🟡 | side-track |
| | **— Stage Gate 2 —** *(3+ HTB/THM writeups, OWASP Top 10 hands-on, Linux+Windows privesc demonstrated cold)* | | |
| **19** | [Active Directory & Entra ID](Phase-6.md#part-23-active-directory-entra-id) *(+ deferred Kerberos patch from #03)* | 🔴 | Enterprise |
| **20** | [Cloud Computing](Phase-6.md#part-24-cloud-computing) *(+ deferred Cloud Assets patch from #04)* | 🔴 | Enterprise |
| **21** | [Container & Orchestration Security](Phase-6.md#part-25-container-orchestration-security) | 🟡 | Enterprise |
| **22** | [Adversary Emulation & Purple Teaming](Phase-6.md#part-16-adversary-emulation-purple-teaming) | 🔴 | Enterprise |
| **23** | [Sniffing & Spoofing](Phase-2.md#part-9-sniffing-spoofing) — ARP, MITM, Bettercap, Responder | 🟡 | Enterprise |
| **24** | [Social Engineering](Phase-2.md#part-10-social-engineering) — Phishing, Vishing, Physical | 🟡 | Enterprise |
| **25** | [Malware & Weaponization](Phase-2.md#part-8-malware-weaponization) *(conceptual — full build is #27)* | 🔵 | Enterprise |
| **26** | [Pentest Methodologies & Report Writing](Phase-10.md#part-39-penetration-testing-methodologies-report-writing) | 🔴 | Enterprise |
| | **— Stage Gate 3 —** *(AD domain attacked end-to-end, BloodHound exports in Git, 1 professional report)* | | |
| **27** | [Offensive Development & Tooling](Phase-7.md#part-42-offensive-development-tooling) — C2, Shellcode, AMSI/ETW | 🔴 | Specialized |
| **28** | [AI & LLM Red Teaming](Phase-9.md#part-38-ai-llm-red-teaming) — Prompt Injection, RAG, Agentic Exploits | 🔴 | Specialized |
| **29** | [Red Team Operations & Tradecraft](Phase-10.md#part-40-red-team-operations-tradecraft) — C2, OPSEC, Campaign | 🔴 | Specialized |
| **30** | [Proof of Work & Career Portfolio](Phase-10.md#part-41-proof-of-work-career-portfolio) — Certs, GitHub, Bug Bounties | 🔴 | Specialized |
| | **— Final Gate —** *(custom C2 in lab, published AI security research, 3+ reports, OSCP)* | | |

---

## 📦 Shelf — Not Numbered, Not Touched Pre-Employment

> These aren't "later in the sequence" — they're off the sequence entirely until you have a job. No number means no claim on your time right now.

| Module | Phase File | Old Ref |
|--------|-----------|---------|
| Wireless Network Security | [Phase-5.md](Phase-5.md) | Part 21 |
| Mobile Security | [Phase-5.md](Phase-5.md) | Part 22 |
| Digital Forensics | [Phase-7.md](Phase-7.md) | Part 27 |
| Reverse Engineering & Malware Analysis | [Phase-7.md](Phase-7.md) | Part 28 |
| Modern Exploitation | [Phase-7.md](Phase-7.md) | Part 29 |
| Governance, Risk & Compliance | [Phase-8.md](Phase-8.md) | Part 35 |
| Supply Chain Security | [Phase-8.md](Phase-8.md) | Part 36 |
| DevSecOps & Secure SDLC | [Phase-8.md](Phase-8.md) | Part 37 / 37B |
| Security Architecture & Engineering | [Phase-8.md](Phase-8.md) | Part 43 |
| OT/ICS/SCADA | [Phase-6.md](Phase-6.md) | Part 26 |
| Hardware Hacking | [Phase-7.md](Phase-7.md) | Part 30 |
| Physical Penetration Testing | [Phase-7.md](Phase-7.md) | Part 32 |
| VoIP/SS7/5G | [Phase-7.md](Phase-7.md) | Part 33 |
| Blockchain/Web3 | [Phase-7.md](Phase-7.md) | Part 34 |

---

## ⏱️ Daily Protocol

> One question answered every morning: **"What is my current module and what am I proving today?"**

### Daily Activities

**1. Engineering Foundation**
Read the protocol or mechanism for your current topic. Write structured notes. Understand *why* it works before touching a tool.

**2. Lab Execution**
Terminal open. Wireshark running. Execute commands, capture output, break things. Never run a tool you cannot explain at the packet or system level.

**3. Artifact & Proof**
Save PCAP/log/screenshot. Write the 1-page lab summary. Git commit with a descriptive message. Check the Move-On Gate in the phase file.

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
