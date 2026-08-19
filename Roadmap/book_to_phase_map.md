# 📚 Book → Roadmap Phase Mapping (smilo's Library)

> **Usage Rule:** Open each book ONLY when you arrive at that Phase/Part. Do NOT read ahead.
> These are **reference and depth books**, not replacements for your roadmap checklists.

---

## Priority Legend

| Symbol | Meaning | What to do |
|---|---|---|
| 🔴 **Must Read** | Non-negotiable primary resource for this Part | Open when you start the Part. Read relevant chapters before touching labs. |
| 🟡 **Should Read** | High-value supplement | Read after your first lab pass when you need more context or depth. |
| 🟢 **Can Read** | Optional depth | Reference only if stuck on a specific topic, or going deeper than the roadmap requires. |

---

## ❌ SKIP ENTIRELY — Zero ROI for Your Track

These exist in your library but have no practical value for Red Team / Offensive Security.
Do not open at any point in your roadmap.

| Category | Examples |
|---|---|
| **Too Old (pre-2010)** | All Hakin9 issues 2005–2009, Python 2.x books, Classic Shell Scripting |
| **Academic/Theoretical CS** | Automata theory, Type Theory, Graph Transformations, Lambda Calculus, Complexity books |
| **Beginner Hacking Fluff** | "Computer Hacking Beginners Guide", "Hacking for Dummies", "Hacking Made Easy", "Getting Started Becoming a Master Hacker" |
| **Completely Off-Track** | React, Kotlin, JavaScript, Java, VBA, Excel Macros, Game Dev, ML/AI (non-security) |
| **Irrelevant Certs** | CISA (audit focus), CCNA Cloud (networking vendor cert, not offensive security) |
| **Hacker Culture** | "Hackers Heroes of the Computer Revolution", "Hacker Culture", "Hacker States" — interesting but zero skill ROI |

---

## ✅ PHASE 1: Foundation
> Phase 1 is 80–90% complete. Use these as **gap-patching references only** — do NOT restart Phase 1.

### Part 1: Fundamentals

| Priority | Book | How to Use |
|---|---|---|
| 🔴 | `Foundations of Information Security - Jason Andress` | CIA triad, auth, access control basics — targeted chapter lookup only |
| 🟡 | `Security in Computing 5th Edition` | Authoritative reference for security concepts |
| 🟢 | `The Linux Command Line - A Complete Introduction` | Quick lookup for specific commands |

### Part 1B: Linux Administration

| Priority | Book | How to Use |
|---|---|---|
| 🔴 | `The Linux Command Line - A Complete Introduction` | Primary CLI and admin reference |
| 🟡 | `Using And Administering Linux Volume 1 Zero To SysAdmin Getting Started` | systemctl, user management, /etc/ configs |
| 🟡 | `Using And Administering Linux Volume 2 Zero To SysAdmin Advanced` | Advanced admin and service configuration |
| 🟢 | `Using And Administering Linux Volume 3 Zero To SysAdmin Network` | Network services on Linux |

### Part 1C: Windows Administration

| Priority | Book | How to Use |
|---|---|---|
| 🔴 | `EA - Windows Security Internals with PowerShell` | Deep Windows internals + PowerShell. Critical again in Phase 6 AD. |
| 🟡 | `Windows PowerShell Cookbook` | PowerShell command reference for admin tasks |

### Part 2: Networking Fundamentals

| Priority | Book | How to Use |
|---|---|---|
| 🔴 | `Data Communications and Networking with TCPIP Protocol Suite - Behrouz A. Forouzan (2022)` | The definitive networking reference — per-chapter as needed (TCP, DNS, subnetting) |
| 🟡 | `Wireshark Cheat Sheet` | ⚡ Keep open during all packet analysis labs |
| 🟢 | `Computer Networking Principles, Protocols, and Practice` | Lighter alternative to Forouzan for readable second opinions |

### Part 3: Cryptography

| Priority | Book | How to Use |
|---|---|---|
| 🔴 | `Security in Computing 5th Edition` | Crypto primitives, hashing, PKI — chapter-level reference |
| 🟡 | `Foundations of Information Security - Jason Andress` | Readable crypto foundations without academic abstraction |

### Part 3C: Web Technology Fundamentals

| Priority | Book | How to Use |
|---|---|---|
| 🔴 | `The Tangled Web` | Deep dive on how browsers and HTTP work; directly explains why web vulnerabilities exist |
| 🟡 | `Foundations of Information Security - Jason Andress` | Session, cookie, and auth fundamentals chapter |

---

## ✅ PHASE 2A: Offensive Fundamentals (Parts 4, 5, 6, 6B, 31, 7)

### Part 4: Footprinting & Reconnaissance

| Priority | Book | Specific Chapters | What It Adds |
|---|---|---|---|
| 🔴 | `The Hacker Playbook 2` | Chapter 1: Recon section | Real-world passive + active OSINT methodology |
| 🔴 | `Red Team Field Manual v3` | Reference throughout | ⚡ Fastest command lookup — keep open always |
| 🟡 | `Counter Hack Reloaded - Ed Skoudis & Tom Liston` | Recon chapters | Structured methodology for full recon pipeline |
| 🟡 | `Cybersecurity Attack-and-Defense Strategies 2nd` | Reconnaissance chapter | How defenders see your recon footprint — informs OPSEC |
| 🟢 | `Python for OSINT Tooling` | Full book (short) | Build your own OSINT automation tools in Python |

### Part 5: Scanning

| Priority | Book | Specific Chapters | What It Adds |
|---|---|---|---|
| 🔴 | `Red Team Field Manual v3` | Reference throughout | ⚡ Keep open during all scanning labs |
| 🟡 | `Ethical Hacking A Hands-on Introduction to Breaking In` | Scanning & fingerprinting chapters | Hands-on Nmap and service enumeration |
| 🟡 | `The Power of Scapy V2` | Full (short reference) | Custom packet crafting for advanced scanning |
| 🟡 | `Wireshark Cheat Sheet` | Reference | ⚡ Keep open during packet capture labs |
| 🟢 | `Hacking and Network Defense` | Network scanning chapter | Defender perspective on what scan traffic looks like in logs |

### Part 6: Enumeration

| Priority | Book | Specific Chapters | What It Adds |
|---|---|---|---|
| 🔴 | `Hacking Exposed` | SMB, SNMP, LDAP, RPC chapters | Classic enumeration playbook — still directly applicable |
| 🟡 | `Counter Hack Reloaded - Ed Skoudis & Tom Liston` | Enumeration chapters | Structured per-protocol coverage and what data each leaks |
| 🟢 | `Cyberjutsu Cybersecurity for the Modern Ninja` | Enumeration section | Attacker-focused methodology in clear tactical language |

### Part 6B: Database Security

| Priority | Book | Specific Chapters | What It Adds |
|---|---|---|---|
| 🔴 | `Web Application Hacking Advanced SQL Injection and Data Store Attacks` | DB internals chapters only (save injection for Phase 4) | DB enumeration and extraction fundamentals |
| 🟡 | `Database Security Problems and Solutions` | Full (reference) | DB misconfiguration and exploitation techniques |

### Part 31: Password Cracking & Hash Analysis

| Priority | Book | Specific Chapters | What It Adds |
|---|---|---|---|
| 🔴 | `Hacking_ The Art Of Exploitation 2nd Edition` | Cryptography and hashing chapter | Ground-truth on how hashes work and why cracking is possible |
| 🟡 | `Reverse Engineering and Password Breaking` | Full (short) | Direct coverage of hash formats and cracking methodology |
| 🟢 | `Computer & Internet Security A Hands on Approach 2nd Ed` | Authentication chapters | Explains salting, key derivation, why bcrypt/Argon2 resist cracking |

### Part 7: System Hacking & Initial Compromise

| Priority | Book | Specific Chapters | What It Adds |
|---|---|---|---|
| 🔴 | `The Hacker Playbook 3 (Red Team Edition)` | Initial access, privesc, persistence | Best modern red team field guide — primary companion for Part 7 |
| 🔴 | `Hacking_ The Art Of Exploitation 2nd Edition` | Shellcode, stack/heap overflows | Foundational exploitation textbook — understand WHY exploits work |
| 🔴 | `Red Team Field Manual v3` | Reference throughout | ⚡ Keep open always |
| 🟡 | `The Hacker Playbook 2` | Exploitation and post-exploitation | Practical walk-through of actual techniques |
| 🟡 | `Gray Hat Hacking The Ethical Hacker's Handbook 2022` | System exploitation chapters | Modern, updated privesc techniques |
| 🟢 | `Exploitation Techniques and Tools` | Full (reference doc) | Technique catalog — lookup for specific techniques in labs |
| 🟢 | `Exploit Development on Linux Platform` | Full | Linux-specific exploitation fundamentals |

---

## ✅ PHASE 2B: Advanced Offensive Ops (Parts 9, 10, 12)

### Part 9: Sniffing & Spoofing

| Priority | Book | Specific Chapters | What It Adds |
|---|---|---|---|
| 🔴 | `The Power of Scapy V2` | ARP spoofing, packet injection chapters | Tool mastery for MitM and packet manipulation |
| 🟡 | `Wireshark Cheat Sheet` | Reference | ⚡ Keep open during capture and analysis labs |
| 🟢 | `Hacking and Network Defense` | Sniffing chapter | Defender detection of sniffing activity — informs OPSEC |

### Part 10: Social Engineering

| Priority | Book | Specific Chapters | What It Adds |
|---|---|---|---|
| 🔴 | `Social Engineering The Art of Human Hacking` | Full book | **The** definitive SE book — read fully during Part 10 |
| 🟡 | `The Social Engineers Playbook` | Full (short) | Practical tactical scripts and pretexts |

### Part 12: Session Hijacking

| Priority | Book | Specific Chapters | What It Adds |
|---|---|---|---|
| 🔴 | `The Tangled Web` | Browser/session management chapters | Deep coverage of session flaws — bridges into Phase 4 |

---

## ✅ PHASE 4: Web & Application Security (Parts 17, 18, 19, 20)

> **PortSwigger Academy is your primary platform here.**
> Books are depth companions, not replacements for PortSwigger labs.

### Part 17: Web Application Hacking

| Priority | Book | Specific Chapters | What It Adds |
|---|---|---|---|
| 🔴 | `The Web Application Hacker's Handbook` | Chapter matching current PortSwigger module | **The** foundational web security textbook — maps 1:1 to PortSwigger topics |
| 🔴 | `SQL Injection Attacks and Defense` | Full book | Deepest SQLi reference — read alongside PortSwigger SQLi Modules 6–18 |
| 🔴 | `Burp Suite Compendium` / `The Power of Burp Suite` | Reference throughout Phase 4 | Deep Burp feature coverage |
| 🟡 | `Web Application Security - Andrew Hoffman` | Full book | Developer-code-level explanation of WHY each vulnerability exists |
| 🟡 | `Web penetration testing with kali linux` | Targeted chapters | Covers Burp, sqlmap, Nikto, ZAP in practice |
| 🟡 | `Bypassing Web Application Firewall Workshop` | Full | WAF bypass techniques for filter evasion labs |
| 🟡 | `XSS CheatSheet` | Reference | ⚡ Keep open during PortSwigger XSS modules |
| 🟢 | `White Hat Hacking complete guide to XSS Attacks` | Full (short) | Structured XSS coverage to complement labs |
| 🟢 | `SQL Injection Attacks` / `SQL Injection Strategies` / `SQL injection CyberSecurity` | Reference PDFs | Quick lookup alongside PortSwigger SQLi labs |
| 🟢 | `Web Application Hacking Advanced SQL Injection and Data Store Attacks` | Advanced injection chapters | Advanced DB-level SQLi — read after PortSwigger SQLi track |

### Part 18: Web Server Hacking

| Priority | Book | Specific Chapters | What It Adds |
|---|---|---|---|
| 🟡 | `Web Application Attacks` | Reference | Broad server-side attack catalog beyond SQLi and XSS |
| 🟢 | `Web security exposed` | Reference | Supplementary attack coverage |
| 🟢 | `WordPress Hacking and Security` | Reference | CMS-specific methodology for real-world scope targets |

### Part 19: API Security

| Priority | Book | Specific Chapters | What It Adds |
|---|---|---|---|
| 🔴 | `Hacking APIs Breaking Web Application Programming Interfaces - Corey` | Full book | **The** dedicated API security book — maps directly to Part 19 |
| 🟡 | `Web security testing guide` | Reference | OWASP WSTG API test cases — use IDs when writing reports |

### Part 20: Bug Bounty & Penetration Testing

| Priority | Book | Specific Chapters | What It Adds |
|---|---|---|---|
| 🔴 | `zseano's methodology` | Full (short) | Practical bug bounty workflow from an experienced hunter |
| 🔴 | `From Hacking to Report Writing` | Full | Bridges exploitation to professional report writing |
| 🟡 | `Bug Bounty Hunting For Web Security` | Full | Platform-specific methodology for HackerOne, Bugcrowd etc. |
| 🟡 | `Web security testing guide` | Reference | OWASP WSTG test case IDs for reporting (e.g. WSTG-INPV-05) |
| 🟢 | `Web Application Pentest Methodology` | Reference | Structured methodology doc for writing assessments |

---

## ✅ PHASE 5: Wireless & Mobile (Parts 21, 22)

### Part 21: Wireless Pentesting

| Priority | Book | Specific Chapters | What It Adds |
|---|---|---|---|
| 🔴 | `Wireless Hacking` | Full | Core wireless attack methodology (WPA2 cracking, PMKID, Evil AP) |
| 🔴 | `Wireless Hacking Cheat Sheet v1.1` | Reference | ⚡ Keep open during all Part 21 labs |
| 🟡 | `Wireless Network Security` | Reference | Defensive perspective — informs OPSEC and detection awareness |
| 🟢 | `Wifi & Security` / `WiFi hacking article` | Reference | Supplementary reading |

### Part 22: Mobile Platform Pentesting

| Priority | Book | Specific Chapters | What It Adds |
|---|---|---|---|
| 🔴 | `Hacking android` | Full | Android attack surface, APK analysis, and exploitation |
| 🔴 | `Hacking and securing ios applications` | Full | iOS binary analysis, Jailbreak exploitation, runtime hooking |
| 🟡 | `Cybersecurity for Mobile Devices` | Reference | Broad mobile security coverage |
| 🟢 | `Best of Mobile Hacking` | Reference | Supplementary attack techniques |
| 🟢 | `Hacking Android Smartphones with NFC Tags` / `Bluetooth Low Energy Hacking` | Reference | Use only if labs include BLE/NFC vectors |

---

## ✅ PHASE 6: Infrastructure & Identity (Parts 23, 24, 25, 16)

### Part 23: Active Directory & Entra ID

| Priority | Book | Specific Chapters | What It Adds |
|---|---|---|---|
| 🔴 | `EA - Windows Security Internals with PowerShell` | AD internals, attack paths chapters | Best single resource for Kerberoasting, DCSync, Golden Ticket, PowerShell enumeration |
| 🟡 | `Windows PowerShell Cookbook` | Reference | PowerShell scripting for AD enumeration and post-exploitation |
| 🟡 | `Windows Server automation with PowerShell cookbook` | Reference | Group Policy, SYSVOL, service configs |
| 🟢 | `Cybersecurity Attack-and-Defense Strategies 2nd` | Enterprise attack chain chapters | Red vs blue perspective on AD attack chains |

### Part 24: Cloud Computing

| Priority | Book | Specific Chapters | What It Adds |
|---|---|---|---|
| 🔴 | `Cloud_Hacking (1)` | Full | Cloud attack methodology (misconfigs, SSRF to metadata, IAM abuse) |
| 🟢 | `Trusted Cloud Computing` | Reference | Cloud security architecture — defensive context |

---

## ✅ PHASE 7: Advanced Specializations (Parts 27, 28, 29, 42)

### Part 27: Digital Forensics (DFIR)

| Priority | Book | Specific Chapters | What It Adds |
|---|---|---|---|
| 🔴 | `The Art of Memory Forensics` | Full book | **The** definitive memory forensics reference — mandatory reading |
| 🔴 | `SANS DFIR Cheatsheets and Notebooks` | Reference | ⚡ Keep open during all Part 27 labs |
| 🟡 | `Hacking Exposed Computer Forensics Secrets & Solutions 2nd` | Full | Disk and network forensics methodology |
| 🟡 | `Effective Threat Investigation` | Full | Structured threat investigation methodology and evidence chaining |
| 🟢 | `Smartphone Forensics Cheatsheet by SANS` | Reference | Mobile evidence acquisition quick ref |

### Part 28: Reverse Engineering & Malware Analysis

| Priority | Book | Specific Chapters | What It Adds |
|---|---|---|---|
| 🔴 | `Reversing Secrets of Reverse Engineering - Eldad Eilam` | Full book | **The** foundational RE textbook — read early in Part 28 |
| 🟡 | `The Android Malware Handbook (2023)` | Full | Mobile malware RE — use if labs cover mobile malware |
| 🟡 | `Designing BSD rootkit` | Full | Rootkit internals, evasion, and persistence mechanisms |
| 🟢 | `Best of Reverse Engineering` / `Reverse Engineering Hacking and Cracking` | Reference | Supplementary RE techniques |
| 🟢 | `The Rootkit Arsenal Escape and Evasion in the Dark Corners` | Reference | Deepest rootkit reference — read after basic RE is solid |

### Part 29: Modern Exploitation

| Priority | Book | Specific Chapters | What It Adds |
|---|---|---|---|
| 🔴 | `Hacking_ The Art Of Exploitation 2nd Edition` | Full book | Shellcode, stack overflows, heap exploitation — read fully in Part 29 |
| 🟡 | `Exploit Development on Linux Platform` | Full | Linux-specific exploit writing and shellcode injection |
| 🟡 | `Exploit Development Wintel Platform` | Full | Windows-specific exploit development (SEH, ROP chains) |
| 🟢 | `Build Your Own EXPLOITS` | Full | Practical exploit building projects from concept to working PoC |

### Part 42: Offensive Development & Tooling

| Priority | Book | Specific Chapters | What It Adds |
|---|---|---|---|
| 🔴 | `Black Hat Python 2nd Edition` | Full book | C2 building, RAT development, evasion, custom offensive tooling |
| 🟡 | `Black Hat Go Go Programming For Hackers and Pentesters` | Full | Modern Go-based offensive tooling and implant development |
| 🟡 | `Gray Hat Python - Seitz, Justin` | Full | Debugging, fuzzing, shellcode injection, process manipulation via Python |
| 🟢 | `REALWORLDPYTHON Hackers Guide 2020` | Full | Real-world offensive Python automation projects |

---

## ✅ PHASE 8: DevSecOps & GRC (Parts 35, 37, 37B, 43)

### Part 35: Governance, Risk & Compliance (GRC)

| Priority | Book | Use |
|---|---|---|
| 🔴 | `Foundations of Information Security - Jason Andress` | Security policy and risk management fundamentals |
| 🟡 | `CISSP Study Guide 4th Edition` | Broad governance, risk, and compliance framework reference |
| 🟢 | `The Practical Guide to HIPAA Privacy and Security Compliance 2nd` | Compliance framework depth for healthcare/regulated environments |

### Part 37: DevSecOps & Secure SDLC

| Priority | Book | Use |
|---|---|---|
| 🔴 | `Security for Software Engineers` | Secure SDLC, threat modeling, SAST/DAST — maps directly to Part 37 |
| 🟡 | `Web Application Security - Andrew Hoffman` | Secure code patterns from an AppSec engineer perspective |

### Part 37B: Secure Code Review

| Priority | Book | Use |
|---|---|---|
| 🔴 | `Web Application Security - Andrew Hoffman` | Identifies vulnerable patterns (SQL sinks, XSS outputs, insecure deserialization) in code |
| 🟡 | `Security for Software Engineers` | Secure coding patterns across languages |

### Part 43: Security Architecture & Engineering

| Priority | Book | Use |
|---|---|---|
| 🟡 | `CISSP Study Guide 4th Edition` | Security architecture domains (network, identity, cryptography, physical) |
| 🟡 | `Foundations of Information Security - Jason Andress` | Architecture and design security principles |
| 🟢 | `Cybersecurity First Principles A Reboot of Strategy and Tactics` | Strategic architecture thinking |

---

## ✅ PHASE 9: AI Security

| Priority | Book | Use |
|---|---|---|
| 🟡 | `Hacking AI` | LLM attack surface, prompt injection concepts |
| 🟢 | `Data Mining and Machine Learning in Cybersecurity` | ML model vulnerabilities — adversarial ML and poisoning attacks context |

---

## ✅ PHASE 10: Operations & Career (Parts 39, 40, 41)

### Part 40: Red Team Operations

| Priority | Book | Use |
|---|---|---|
| 🔴 | `Red Team Field Manual v3` | ⚡ Keep open at all times — fastest command reference |
| 🟡 | `The Red Report 2023` | Current attacker TTP trends and real-incident data |
| 🟡 | `Threat Intelligence Handbook` | CTI methodology for adversary profiling and red team planning |
| 🟢 | `Cybersecurity Attack-and-Defense Strategies 2nd` | Structured red team operation planning |

### Part 39: Penetration Testing & Report Writing

| Priority | Book | Use |
|---|---|---|
| 🔴 | `The Pentester Blueprint` | Pentest career methodology, report writing, professional conduct — read before Part 39 |
| 🔴 | `From Hacking to Report Writing` | Report structure, evidence packaging, finding articulation |
| 🟢 | `Web Application Pentest Methodology` | Structured methodology doc for web pentest engagements |

### Part 41: Proof of Work & Career Portfolio

| Priority | Book | Use |
|---|---|---|
| 🟡 | `cyber security interview questions` | Technical interview preparation |
| 🟡 | `Cybersecurity First Principles A Reboot of Strategy and Tactics` | Strategic framing for senior-level interviews and portfolio positioning |
| 🟢 | `Threat Detection Report 2023` | Current threat landscape context for interview discussions |

---

## 📅 Hakin9 Magazines (2010–2014) — Targeted Use Only

Do not read cover-to-cover. Glance only if a specific topic has no better modern source:

| Series | When to Glance | Why |
|---|---|---|
| `Hakin9 Regular 2013–2014` | Phase 2B or Phase 4 if stuck on a specific technique | Some solid intermediate-level articles on specific tools |
| `Hakin9 Mobile Security 2012` | Phase 5 Part 22 | Mobile security concepts — historical context only |
| `Hakin9 EXTRA Forensic 2011` | Phase 7 Part 27 | Early forensic methodology |
| All others | **Skip** | Core coverage handled better by modern books above |

---

## ⚡ Always-Open Quick Reference Cards

Pin these to your taskbar and keep them open:

| Priority | Cheat Sheet | When to Use |
|---|---|---|
| 🔴 | `Red Team Field Manual v3` | Every phase — fastest command reference |
| 🟡 | `Wireshark Cheat Sheet` | Phase 2 Part 5 (Scanning) + Part 9 (Sniffing) |
| 🟡 | `Wireless Hacking Cheat Sheet v1.1` | Phase 5 Part 21 |
| 🟡 | `XSS CheatSheet` | Phase 4 alongside PortSwigger |
| 🟡 | `SANS DFIR Cheatsheets` | Phase 7 Part 27 |
| 🟢 | `Ctf CheatSheet` | Ongoing TryHackMe and HTB challenges |
