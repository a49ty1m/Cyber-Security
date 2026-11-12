# 🛡️ Cybersecurity Master Roadmap

> **Career Target:** Penetration Testing → Red Team Operations → Advanced Offensive Security → AI Red Teaming

---

### 🧭 Roadmap Navigation

| 🏠 Root | 🔵 Stage 1 | 🟠 Stage 2 | 🟣 Stage 3 | 🏢 Stage 4 | 🔬 Stage 5 | 📦 Shelf | 🛠️ Tools |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **YOU ARE HERE** | [[Cyber-Security/Roadmap/Stage-1_Foundation\|Foundation]] | [[Cyber-Security/Roadmap/Stage-2_Offense-I\|Offense I]] | [[Cyber-Security/Roadmap/Stage-3_Web-and-App-Sec\|Web & App Sec]] | [[Cyber-Security/Roadmap/Stage-4_Enterprise\|Enterprise]] | [[Cyber-Security/Roadmap/Stage-5_Specialized\|Specialized]] | [[Cyber-Security/Roadmap/Shelf_Post-Hire\|Post-Hire]] | [[Cyber-Security/Roadmap/Tools/README\|Tools Hub]] |

---

> [!TIP]
> ### 💎 Best Navigated in Obsidian
> This Master Roadmap and all Stage modules are deeply interconnected with **bi-directional Obsidian wikilinks** (`[[Stage-X#Heading|Title]]`). Open this repository as a vault in **[Obsidian](https://obsidian.md/)** for interactive link previews, graph analysis, and frictionless navigation.

> [!IMPORTANT]
> ### 🆕 **ROADMAP EXPANSION COMPLETE (January 2026)**
> This roadmap has been **expanded and updated** to align with the AI ERA 2026 cybersecurity standard. **10 new modules and topics** have been added across all 5 stages, increasing coverage from ~55-60% to **~90%** while maintaining the offensive security focus.
> 
> **Key Additions:**
> - 🔥 **Mobile Application Security** (Android & iOS pentesting)
> - 🔥 **SOC & SIEM Engineering** (Splunk, Sentinel, Elastic)
> - 🔥 **Hands-on Malware Analysis** (Static, Dynamic, Memory Forensics)
> - 🔥 **Vulnerability Research & Fuzzing** (AFL++, LibFuzzer)
> - **Post-Quantum Cryptography** & **Zero Trust Architecture**
> - **Advanced OSINT** & **Wireless/IoT Scanning**
> - **Container Supply Chain Security** (Cosign, SLSA, OPA Gatekeeper)
> 
> **Time Impact:** +11-14 weeks (~2.5-3 months) added to total roadmap  
> **See:** `COMPLETE_IMPLEMENTATION_LOG.md` for full details

---

## 🚀 START HERE — Quick Orientation

### **Three Ways to Use This Roadmap:**

1. **📖 Complete Linear Path** (Recommended)  
   Start at Stage 1, Module 1 and progress sequentially through all 5 stages. This is the most thorough approach and takes ~12-17 months with consistent daily practice.

2. **🎯 Targeted Learning**  
   Jump to specific modules based on current goals (e.g., start with Web Security if preparing for OSCP, or Active Directory if targeting enterprise roles). Use the module dependencies chart to ensure prerequisites are met.

3. **📚 Reference Guide**  
   Use as a comprehensive security knowledge base and tool reference. Each module includes detailed topic breakdowns, tool lists, and book recommendations.

**Recommended Daily Flow:**
- **Phase 1:** Read/Watch (30-45 min) — Theory and concepts
- **Phase 2:** Hands-on Lab (2-3 hours) — Practical exercises
- **Phase 3:** Documentation (30 min) — Write notes, update tracking
- **Phase 4:** CTF Challenge (1 hour) — Apply skills in challenges

---

### Time Investment Reality Check

| Stage | Modules | Estimated Time | Cumulative |
|-------|---------|----------------|------------|
| Stage 1 | 01-07 | 3-4 months | 3-4 months |
| Stage 2 | 08-13 | 2.5-3.5 months | 5.5-7.5 months |
| Stage 3 | 14-18 (+17B) 🆕 | 3-3.5 months | 8.5-11 months |
| Stage 4 | 19-26 (+19A) 🆕 | 3-4 months | 11.5-15 months |
| Stage 5 | 27-30 (+27B, 27C) 🆕 | 4.5-6 months | 16-21 months |
| **Total** | **33 modules** 🆕 | **~16-21 months** | **with 2026 expansions** |

**Note:** Timeline assumes **4-6 hours daily** of **active hands-on practice**. Passive reading or video watching does not count toward this estimate.

---



## �️ Table of Contents

| # | Section | Description |
| :-: | :--- | :--- |
| 1 | [[#🎯 Execution Order — 5 Stages\|🎯 Execution Order]] | Sequential 33-module curriculum with depth rankings and time estimates |
| 2 | [[#� Module Learning Matrix\|� Module Learning Matrix]] | Tools, books, and CTF checkpoints mapped to each module |
| 3 | [[#�️ Stage Topic Breakdown\|�️ Stage Topic Breakdown]] | Comprehensive technical scope across all domains |
| 4 | [[#📦 Shelf — Post-Hire Electives\|📦 Shelf]] | 21 off-sequence tracks (Mobile, ICS/SCADA, Forensics, Hardware) |
| 5 | [[#⏱️ Daily Protocol\|⏱️ Daily Protocol]] | 4-phase loop, session tiers, and weekly rhythm |
| 6 | [[#🛠️ Lab Setup\|🛠️ Lab Setup]] | Hardware specs, hypervisor, and practice platforms |

---

## 🎯 Execution Order — 5 Stages

> [!NOTE]
> **How to Read This Table:**
> - 🔴 = Master before moving on · 🟡 = Learn solid, keep moving · 🔵 = Conceptual (hands-on later)
> - ⏱ Time estimates assume **4-6 hours daily** active practice per [[#⏱️ Daily Protocol\|Daily Protocol]]
> - Stage gates validate readiness before advancing to next stage

| # | Module | Depth | Stage | Est. Time |
| :---: | --- | :---: | :---: | :---: |
| 01 | [[Cyber-Security/Roadmap/Stage-1_Foundation#Module 01: Fundamentals\|Fundamentals]] — Hardware, OS, Memory, Data Rep, Programming + **PQC, Zero Trust** 🆕 | 🔴 | Foundation | 5–8 wks |
| 02 | [[Cyber-Security/Roadmap/Stage-1_Foundation#Module 02: Linux Administration\|Linux Administration]] | 🔴 | Foundation | 1.5–2 wks |
| 03 | [[Cyber-Security/Roadmap/Stage-1_Foundation#Module 03: Windows Administration\|Windows Administration]] | 🟡 | Foundation | 2–2.5 wks |
| 04 | [[Cyber-Security/Roadmap/Stage-1_Foundation#Module 04: Networking Fundamentals\|Networking Fundamentals]] | 🔴 | Foundation | 2.5–4 wks |
| 05 | [[Cyber-Security/Roadmap/Stage-1_Foundation#Module 05: Cryptography\|Cryptography]] — core concepts + attacks | 🔴 | Foundation | 1.5–2 wks |
| 06 | [[Cyber-Security/Roadmap/Stage-1_Foundation#Module 06: Authentication Standards\|Authentication Standards]] — Sessions, JWT, OAuth, MFA | 🔴 | Foundation | 1.5–2 wks |
| 07 | [[Cyber-Security/Roadmap/Stage-1_Foundation#Module 07: Web Technology Fundamentals\|Web Technology Fundamentals]] — HTTP, Cookies, CORS, REST | 🔴 | Foundation | 1–1.5 wks |
|| **[[Cyber-Security/Roadmap/Stage-1_Foundation#🏁 Foundation Proof Gate\|🏁 Foundation Proof Gate]]** *(10 PCAPs, admin baselines, 3 scripts, lab report)* ||| **~3–4 mos** |
| 08 | [[Cyber-Security/Roadmap/Stage-2_Offense-I#Module 08: Footprinting & Reconnaissance\|Footprinting & Reconnaissance]] + **Advanced OSINT (200+ techniques)** 🆕 | 🔴 | Offense I | 1.5–2 wks |
| 09 | [[Cyber-Security/Roadmap/Stage-2_Offense-I#Module 09: Scanning\|Scanning]] + **Wireless & IoT Scanning (80+ techniques)** 🆕 | 🔴 | Offense I | 1.5 wks |
| 10 | [[Cyber-Security/Roadmap/Stage-2_Offense-I#Module 10: Enumeration\|Enumeration]] | 🔴 | Offense I | 1.5 wks |
| 11 | [[Cyber-Security/Roadmap/Stage-2_Offense-I#Module 11: Database Security\|Database Security]] | 🟡 | Offense I | 1.5–2 wks |
| 12 | [[Cyber-Security/Roadmap/Stage-2_Offense-I#Module 12: Password Cracking & Hash Analysis\|Password Cracking & Hash Analysis]] | 🔴 | Offense I | 1 wk |
| 13 | [[Cyber-Security/Roadmap/Stage-2_Offense-I#Module 13: System Hacking & Initial Compromise\|System Hacking & Initial Compromise]] | 🔴 | Offense I | 4–5 wks |
|| **[[Cyber-Security/Roadmap/Stage-2_Offense-I#🏁 Stage Gate 1 — Host Dominance & Privilege Escalation\|🏁 Stage Gate 1]]** *(root a box, dump & crack a hash, escalate privesc)* ||| **~7–9 wks** |
| 14 | [[Cyber-Security/Roadmap/Stage-3_Web-and-App-Sec#Module 14: Web Application Hacking\|Web Application Hacking]] — SQLi, XSS, SSRF, IDOR, XXE | 🔴 | Web & App Sec | 2–3 wks |
| 15 | [[Cyber-Security/Roadmap/Stage-3_Web-and-App-Sec#Module 15: Session Hijacking & Token Attacks\|Session Hijacking & Token Attacks]] — Cookies, JWTs, Fixation | 🔴 | Web & App Sec | 1 wk |
| 16 | [[Cyber-Security/Roadmap/Stage-3_Web-and-App-Sec#Module 16: Web Server Hacking\|Web Server Hacking]] — Misconfig, Directory Traversal | 🔴 | Web & App Sec | 1 wk |
| 17 | [[Cyber-Security/Roadmap/Stage-3_Web-and-App-Sec#Module 17: API Security\|API Security]] — OWASP API Top 10, REST/GraphQL/gRPC | 🔴 | Web & App Sec | 1 wk |
| 17B 🆕 | [[Cyber-Security/Roadmap/Stage-3_Web-and-App-Sec#Module 17B: Mobile Application Security\|Mobile Application Security]] — Android & iOS Pentesting | 🔴 | Web & App Sec | 1–1.5 wks |
| 18 | [[Cyber-Security/Roadmap/Stage-3_Web-and-App-Sec#Module 18: Bug Bounty Methodology\|Bug Bounty Methodology]] — Scope, Recon, Exploit, Report | 🔴 | Web & App Sec | 1–2 wks |
|| *(parallel tracks — absorb, never block)* [[Cyber-Security/Roadmap/Stage-3_Web-and-App-Sec#Side-Track A: Detection Engineering & SOC Operations\|Detection]], [[Cyber-Security/Roadmap/Stage-3_Web-and-App-Sec#Side-Track B: IDS, Firewalls, and Honeypots\|IDS/Honeypots]], [[Cyber-Security/Roadmap/Stage-3_Web-and-App-Sec#Side-Track C: Cyber Threat Intelligence (CTI) & Attack Surface Management\|CTI/OSINT]] | 🟡 | side-track | ongoing |
|| **[[Cyber-Security/Roadmap/Stage-3_Web-and-App-Sec#🏁 Stage Gate 2 — Web Application Security Gate\|🏁 Stage Gate 2]]** *(3+ writeups, OWASP Top 10, privesc demonstrated)* ||| **~10–13 wks** |
| 19 | [[Cyber-Security/Roadmap/Stage-4_Enterprise#Module 19: Active Directory & Entra ID\|Active Directory & Entra ID]] *(+ deferred Kerberos patch from #03)* | 🔴 | Enterprise | 2–3 wks |
| 19A 🆕 | [[Cyber-Security/Roadmap/Stage-4_Enterprise#Module 19A: SOC & Security Operations\|SOC & Security Operations]] — SIEM, EDR, Detection Engineering, Threat Hunting | 🔴 | Enterprise | 2–3 wks |
| 20 | [[Cyber-Security/Roadmap/Stage-4_Enterprise#Module 20: Cloud Computing\|Cloud Computing]] *(+ deferred Cloud Assets patch from #04)* | 🔴 | Enterprise | 2–3 wks |
| 21 | [[Cyber-Security/Roadmap/Stage-4_Enterprise#Module 21: Container & Orchestration Security\|Container & Orchestration Security]] + **Supply Chain (Cosign, SLSA)** 🆕 | 🔴 | Enterprise | 1 wk |
| 22 | [[Cyber-Security/Roadmap/Stage-4_Enterprise#Module 22: Adversary Emulation & Purple Teaming\|Adversary Emulation & Purple Teaming]] | 🔴 | Enterprise | 1 wk |
| 23 | [[Cyber-Security/Roadmap/Stage-4_Enterprise#Module 23: Sniffing & Spoofing\|Sniffing & Spoofing]] — ARP, MITM, Bettercap, Responder | 🟡 | Enterprise | 1 wk |
| 24 | [[Cyber-Security/Roadmap/Stage-4_Enterprise#Module 24: Social Engineering\|Social Engineering]] — Phishing, Vishing, Physical | 🟡 | Enterprise | 1 wk |
| 25 | [[Cyber-Security/Roadmap/Stage-4_Enterprise#Module 25: Malware & Weaponization (Conceptual)\|Malware & Weaponization]] *(conceptual — full build is #27B)* | 🔵 | Enterprise | 1 wk |
| 26 | [[Cyber-Security/Roadmap/Stage-4_Enterprise#Module 26: Pentest Methodologies & Report Writing\|Pentest Methodologies & Report Writing]] | 🔴 | Enterprise | 1 wk |
|| **[[Cyber-Security/Roadmap/Stage-4_Enterprise#🏁 Stage Gate 3 — Enterprise Domain Compromise & Reporting\|🏁 Stage Gate 3]]** *(AD domain attack, BloodHound exports, professional report)* ||| **~12–16 wks** |
| 27 | [[Cyber-Security/Roadmap/Stage-5_Specialized#Module 27: Offensive Development & Tooling\|Offensive Development & Tooling]] — C2, Shellcode, AMSI/ETW, Exploit Dev | 🔴 | Specialized | 4–6 wks |
| 27B 🆕 | [[Cyber-Security/Roadmap/Stage-5_Specialized#Module 27B: Malware Analysis\|Malware Analysis]] — Static, Dynamic, Memory Forensics, Reverse Engineering | 🔴 | Specialized | 3–4 wks |
| 27C 🆕 | [[Cyber-Security/Roadmap/Stage-5_Specialized#Module 27C: Vulnerability Research & Fuzzing\|Vulnerability Research & Fuzzing]] — AFL++, LibFuzzer, CVE Process | 🔴 | Specialized | 2–3 wks |
| 28 | [[Cyber-Security/Roadmap/Stage-5_Specialized#Module 28: AI & LLM Red Teaming\|AI & LLM Red Teaming]] — Prompt Injection, RAG, Agentic Exploits, MCP Security | 🔴 | Specialized | 4–6 wks |
| 29 | [[Cyber-Security/Roadmap/Stage-5_Specialized#Module 29: Red Team Operations & Tradecraft\|Red Team Operations & Tradecraft]] — C2, OPSEC, Campaign | 🔴 | Specialized | 2–3 wks |
| 30 | [[Cyber-Security/Roadmap/Stage-5_Specialized#Module 30: Proof of Work & Career Portfolio\|Proof of Work & Career Portfolio]] — Certs, GitHub, Bug Bounties | 🔴 | Specialized | Ongoing |
|| **[[Cyber-Security/Roadmap/Stage-5_Specialized#🏁 Final Gate — Mastery & Career Validation\|🏁 Final Gate]]** *(custom C2, published research, reports, OSCP)* ||| **~17–24 wks** |

> [!IMPORTANT]
> **Total Roadmap Duration: ~16-21 months**
> Assumes **4-6 hours daily** of active hands-on practice. The 2026 expansion added **~11-14 weeks**. Passive reading, skipping labs, or ignoring stage gates will extend this significantly.

---

##  Module Learning Matrix

> **Purpose:** This table maps each module to the specific tools, books, and CTF challenges you must complete during that module. Use this as your daily reference checklist.
>
> **How to use:**
> - **Core Tools** — Master these tools during the module (hands-on practice daily)
> - **Required Reading** — Read these specific book sections while learning
> - **CTF/Lab Checkpoints** — Complete these challenges to validate mastery before moving to next module

| Module | Core Tools | Required Reading | CTF/Lab Checkpoints |
| :------: | ----------- | ------------------ | --------------------- |
| [[Cyber-Security/Roadmap/Stage-1_Foundation#Module 01: Fundamentals\|01 - Fundamentals]] | Python, GCC/Clang, `gdb`, Hex editors, `strace` | *Hacking: The Art of Exploitation* Ch.1-3; *Computer Systems: A Programmer's Perspective* Ch.2-3 | [OverTheWire: Bandit](https://overthewire.org/wargames/bandit/) 0–10 |
| [[Cyber-Security/Roadmap/Stage-1_Foundation#Module 02: Linux Administration\|02 - Linux Admin]] | `bash`, `systemctl`, `iptables`, `ssh`, `ps/top`, `journalctl` | *The Linux Command Line* (full); RTFM §Linux Admin; *Linux Basics for Hackers* Ch.1-8 | [OverTheWire: Bandit](https://overthewire.org/wargames/bandit/) 11–25; [THM: Linux Fundamentals](https://tryhackme.com/module/linux-fundamentals) 1–3 |
| [[Cyber-Security/Roadmap/Stage-1_Foundation#Module 03: Windows Administration\|03 - Windows Admin]] | PowerShell, Sysinternals Suite, Event Viewer, `whoami /all`, Registry Editor | *Windows Internals Part 1* Ch.1-5; *PowerShell for Sysadmins* Ch.1-6; Operator Handbook §Windows | [THM: Windows Fundamentals](https://tryhackme.com/module/windows-fundamentals) 1–3; [HTB Academy: Windows Fundamentals](https://academy.hackthebox.com/module/details/49) |
| [[Cyber-Security/Roadmap/Stage-1_Foundation#Module 04: Networking Fundamentals\|04 - Networking]] | Wireshark, `tcpdump`, `nmap`, `ping`, `traceroute`, `dig`, `netcat` | *TCP/IP Illustrated Vol.1* Ch.1-4, 17-18; *The Tangled Web* Ch.1-2; BTFM §Networking | [Wireshark Sample Captures](https://wiki.wireshark.org/SampleCaptures) (10 PCAPs); [THM: Network Services](https://tryhackme.com/room/networkservices) 1–2; [PortSwigger: HTTP basics](https://portswigger.net/web-security/learning-path) |
| [[Cyber-Security/Roadmap/Stage-1_Foundation#Module 05: Cryptography\|05 - Cryptography]] | `openssl`, `hashcat`, `john`, Python `cryptography`, CyberChef | *Serious Cryptography* Ch.1-9; *Cryptography Engineering* Ch.1-5; RTFM §Crypto | [CryptoHack](https://cryptohack.org/challenges/): General (20+); [THM: Encryption - Crypto 101](https://tryhackme.com/room/encryptioncrypto101) |
| [[Cyber-Security/Roadmap/Stage-1_Foundation#Module 06: Authentication Standards\|06 - Auth Standards]] | Burp Suite, `jwt_tool`, Browser DevTools, Postman, `jwt.io` | *OAuth 2.0 Simplified*; *Web Application Hacker's Handbook* Ch.6-7; PortSwigger Auth guide | [PortSwigger Academy: Authentication](https://portswigger.net/web-security/authentication); [THM: Authenticate](https://tryhackme.com/room/authenticatethm), [THM: OWASP Top 10](https://tryhackme.com/room/owasptop10) |
| [[Cyber-Security/Roadmap/Stage-1_Foundation#Module 07: Web Technology Fundamentals\|07 - Web Tech]] | `curl`, Postman, Burp Suite, Browser DevTools (Network/Console) | *HTTP: The Definitive Guide* Ch.1-6; *The Tangled Web* Ch.3-9; PortSwigger HTTP guide | [PortSwigger Academy: HTTP Request Smuggling](https://portswigger.net/web-security/request-smuggling); [THM: Web Fundamentals](https://tryhackme.com/module/web-fundamentals) |
| [[Cyber-Security/Roadmap/Stage-2_Offense-I#Module 08: Footprinting & Reconnaissance\|08 - Footprinting]] | `subfinder`, `amass`, `assetfinder`, `httpx`, `theHarvester`, `shodan-cli` | *Open Source Intelligence Techniques* (Bazzell) Ch.1-5; RTFM §Recon; Operator Handbook §OSINT | [THM: Red Team Recon](https://tryhackme.com/room/redteamrecon); [HTB: Challenges](https://app.hackthebox.com/challenges); OSINT CTF exercises |
| [[Cyber-Security/Roadmap/Stage-2_Offense-I#Module 09: Scanning\|09 - Scanning]] | `nmap`, `masscan`, `rustscan`, `nmap NSE scripts`, `nuclei` | *Nmap Network Scanning* (official) Ch.1-8; RTFM §Scanning; Operator Handbook Ch.2 | [HTB Machines](https://app.hackthebox.com/machines) (Lame, Legacy, Blue); [THM: Nmap](https://tryhackme.com/room/furthernmap), [THM: Network Services](https://tryhackme.com/room/networkservices); [PentesterLab](https://pentesterlab.com) |
| [[Cyber-Security/Roadmap/Stage-2_Offense-I#Module 10: Enumeration\|10 - Enumeration]] | `enum4linux-ng`, `smbclient`, `netexec`, `ldapsearch`, `snmpwalk`, `gobuster` | *The Hacker Playbook 3* Ch.3; RTFM §Enumeration; *Penetration Testing* (Weidman) Ch.5 | [HTB Machines](https://app.hackthebox.com/machines) (Jerry, Nibbles, Networked); [THM: SMB](https://tryhackme.com/room/smb), [THM: Active Directory](https://tryhackme.com/room/winadbasics) |
| [[Cyber-Security/Roadmap/Stage-2_Offense-I#Module 11: Database Security\|11 - Database Security]] | `sqlmap`, MySQL/PostgreSQL/MSSQL clients, `nosqlmap`, `redis-cli` | *The Web Application Hacker's Handbook* Ch.9; *SQL Injection Attacks and Defense* Ch.1-6 | [PortSwigger Academy: SQL Injection](https://portswigger.net/web-security/sql-injection); [HTB: Popcorn](https://app.hackthebox.com/machines/Popcorn); [THM: SQL Injection](https://tryhackme.com/room/sqlinjectionlm) |
| [[Cyber-Security/Roadmap/Stage-2_Offense-I#Module 12: Password Cracking & Hash Analysis\|12 - Password Cracking]] | `hashcat`, `john`, `hydra`, `cewl`, `crunch`, `secretsdump.py` | *Hash Crack* (Joshua Picolet); RTFM §Passwords; Operator Handbook §Cracking | [THM: Password Attacks](https://tryhackme.com/room/passwordattacks), [THM: Crack the Hash](https://tryhackme.com/room/crackthehash); [HTB: Challenges](https://app.hackthebox.com/challenges) |
| [[Cyber-Security/Roadmap/Stage-2_Offense-I#Module 13: System Hacking & Initial Compromise\|13 - System Hacking]] | Metasploit, `msfvenom`, `nc`/`socat`, LinPEAS/WinPEAS, GTFOBins, PowerUp | *Metasploit: The Penetration Tester's Guide* Ch.1-9; *The Hacker Playbook 3* Ch.4-5; RTFM §PrivEsc | [HTB Machines](https://app.hackthebox.com/machines) (Shocker, Beep, Devel, Optimum, Grandpa, Granny); [THM: Linux PrivEsc](https://tryhackme.com/room/linuxprivesc), [THM: Windows PrivEsc](https://tryhackme.com/room/windows10privesc) |
| [[Cyber-Security/Roadmap/Stage-3_Web-and-App-Sec#Module 14: Web Application Hacking\|14 - Web App Hacking]] | Burp Suite Pro, `sqlmap`, `ffuf`, `commix`, `xsstrike`, `dalfox` | *The Web Application Hacker's Handbook* Ch.8-13; *Real-World Bug Hunting* Ch.1-8 | [PortSwigger Academy](https://portswigger.net/web-security) (SQLi, XSS, SSRF, XXE, Path traversal); [HTB Machines](https://app.hackthebox.com/machines) (Markup, Driver) |
| [[Cyber-Security/Roadmap/Stage-3_Web-and-App-Sec#Module 15: Session Hijacking & Token Attacks\|15 - Session & Tokens]] | Burp Suite (Sequencer/Repeater), `jwt_tool`, Cookie Editor, DevTools | *The Web Application Hacker's Handbook* Ch.7; PortSwigger JWT guide | [PortSwigger Academy: JWT Attacks](https://portswigger.net/web-security/jwt); [THM: Post Request Box](https://tryhackme.com/room/postrequestbox); [HTB: Pikaboo](https://app.hackthebox.com/machines/Pikaboo) |
| [[Cyber-Security/Roadmap/Stage-3_Web-and-App-Sec#Module 16: Web Server Hacking\|16 - Web Server Hacking]] | `nikto`, `whatweb`, `ffuf`, `git-dumper`, `davtest`, Apache/Nginx exploits | *The Hacker Playbook 3* Ch.6; RTFM §Web Servers | [HTB Machines](https://app.hackthebox.com/machines) (Mirai, Shocker); [THM: Attacktive Directory](https://tryhackme.com/room/attacktivedirectory); [PortSwigger: Directory Traversal](https://portswigger.net/web-security/file-path-traversal) |
| [[Cyber-Security/Roadmap/Stage-3_Web-and-App-Sec#Module 17: API Security\|17 - API Security]] | Postman, `kiterunner`, `arjun`, `ffuf`, Altair (GraphQL), `grpc_cli` | *Hacking APIs* (Corey Ball); OWASP API Security Top 10 guide; PortSwigger API guide | [PortSwigger Academy: API Testing](https://portswigger.net/web-security/api-testing); [HTB Machines](https://app.hackthebox.com/machines) (JSON, DevOops); [THM: API Hacking](https://tryhackme.com/room/apihacking) |
| [[Cyber-Security/Roadmap/Stage-3_Web-and-App-Sec#Module 17B: Mobile Application Security\|17B - Mobile Security]] 🆕 | Android Studio, ADB, Frida, Objection, MobSF, JADX, APKTool, drozer | *Mobile Application Hacker's Handbook*; OWASP Mobile Security Testing Guide (MSTG); *Android Hacker's Handbook* | [OWASP UnCrackable Apps](https://github.com/OWASP/owasp-mstg); [InsecureBankv2](https://github.com/dineshshetty/Android-InsecureBankv2); [DVIA-v2](https://github.com/prateek147/DVIA-v2) (iOS) |
| [[Cyber-Security/Roadmap/Stage-3_Web-and-App-Sec#Module 18: Bug Bounty Methodology\|18 - Bug Bounty]] | `subfinder`, `nuclei`, `subjack`, `trufflehog`, GitHub dorking tools | *Real-World Bug Hunting* (Peter Yaworski); *Bug Bounty Bootcamp* (Vickie Li) Ch.1-15 | Finish 3+ public bug bounty reports; [HTB Academy: Bug Bounty Hunter](https://academy.hackthebox.com/path/preview/bug-bounty-hunter); [HackerOne Hacktivity](https://hackerone.com/hacktivity) |
| [[Cyber-Security/Roadmap/Stage-4_Enterprise#Module 19: Active Directory & Entra ID\|19 - Active Directory]] | BloodHound/SharpHound, Rubeus, Mimikatz, Impacket suite, PowerView, Certify | *Active Directory Security* (Will Schroeder); *Attacking Active Directory* (Mayfly); RTFM §AD | [HTB Machines](https://app.hackthebox.com/machines) (Forest, Sauna, Cascade, Resolute, Blackfield); [THM: Attacking Kerberos](https://tryhackme.com/room/attackingkerberos), [THM: Breaching AD](https://tryhackme.com/room/breachingad) |
| [[Cyber-Security/Roadmap/Stage-4_Enterprise#Module 19A: SOC & Security Operations\|19A - SOC Operations]] 🆕 | Splunk, Elastic Stack, Microsoft Sentinel, Sysmon, Sigma, YARA, Velociraptor | *Applied Incident Response* (Steve Anson); *Blue Team Handbook* series; Splunk/Elastic/Sentinel documentation | [Boss of the SOC (BOTS)](https://cyberdefenders.org/blueteam-ctf-challenges/); [Splunk Attack Range](https://github.com/splunk/attack_range); Build detection lab with Sysmon + SIEM |
| [[Cyber-Security/Roadmap/Stage-4_Enterprise#Module 20: Cloud Computing\|20 - Cloud Security]] | AWS CLI, Azure CLI, `gcloud`, Pacu, ScoutSuite, Prowler, `s3scanner` | *Hands-On AWS Penetration Testing* (Karl Gilbert); *Cloud Security Handbook* (Eyal Estrin) Ch.1-8 | [THM: Cloud Security](https://tryhackme.com/module/cloud-security); [HTB: Cloud Labs](https://app.hackthebox.com/machines); [flAWS.cloud](http://flaws.cloud) |
| [[Cyber-Security/Roadmap/Stage-4_Enterprise#Module 21: Container & Orchestration Security\|21 - Containers & K8s]] | Docker CLI, `kubectl`, `kube-hunter`, `kube-bench`, `deepce`, `cdk-go` | *Container Security* (Liz Rice); *Kubernetes Security* (Kaizhe Huang) Ch.1-6; RTFM §Containers | [THM: Intro to Docker](https://tryhackme.com/room/introtodocker); [HTB Machines](https://app.hackthebox.com/machines) (Pit, Epsilon); [Kubernetes Goat](https://madhuakula.com/kubernetes-goat/) |
| [[Cyber-Security/Roadmap/Stage-4_Enterprise#Module 22: Adversary Emulation & Purple Teaming\|22 - Adversary Emulation]] | MITRE ATT&CK Navigator, Atomic Red Team, Caldera, Sigma rules | *Adversarial Tradecraft in Cybersecurity* (Dan Borges); MITRE ATT&CK documentation; Purple Team guides | [MITRE ATT&CK](https://attack.mitre.org): Run 10+ techniques; [Atomic Red Team](https://atomicredteam.io); Build detection in lab SIEM |
| [[Cyber-Security/Roadmap/Stage-4_Enterprise#Module 23: Sniffing & Spoofing\|23 - Sniffing & Spoofing]] | Wireshark, `responder`, `bettercap`, `ntlmrelayx.py`, `ettercap`, `mitmproxy` | *The Hacker Playbook 3* Ch.3; RTFM §MITM; Operator Handbook §Lateral Movement | [THM: Wireshark 101](https://tryhackme.com/room/wireshark101), [THM: Responder](https://tryhackme.com/room/responder); [HTB Machines](https://app.hackthebox.com/machines) (Access, Active); Lab: MITM attack on local network |
| [[Cyber-Security/Roadmap/Stage-4_Enterprise#Module 24: Social Engineering\|24 - Social Engineering]] | GoPhish, Evilginx2, SET, Hunter.io, Maltego, LinkedIn scraping tools | *Social Engineering: The Science of Human Hacking* (Hadnagy); *The Art of Deception* (Mitnick) | Build phishing campaign in lab; [THM: Phishing Analysis](https://tryhackme.com/room/phishingemails1); Practice pretexting scenarios |
| [[Cyber-Security/Roadmap/Stage-4_Enterprise#Module 25: Malware & Weaponization (Conceptual)\|25 - Malware (Conceptual)]] | x64dbg, Ghidra, Process Hacker, Volatility 3, OLETools, CyberChef | *Practical Malware Analysis* Ch.1-12; *Malware Analyst's Cookbook* Ch.1-8 | Analyze 5 malware samples ([FLARE VM](https://github.com/mandiant/flare-vm)); [THM: Malware Analysis](https://tryhackme.com/room/malmalintrooverview); [HTB: Reverse Engineering](https://app.hackthebox.com/challenges) |
| [[Cyber-Security/Roadmap/Stage-4_Enterprise#Module 26: Pentest Methodologies & Report Writing\|26 - Pentest Reporting]] | Markdown/LaTeX, Typora, Obsidian, Git, CVSS calculator, report templates | *The Art of Network Penetration Testing* (Royce Davis) Ch.10; Sample pentest reports (public) | Write 3 full pentest reports ([PTES standard](http://www.pentest-standard.org)); Peer review; Portfolio-ready format |
| [[Cyber-Security/Roadmap/Stage-5_Specialized#Module 27: Offensive Development & Tooling\|27 - Offensive Dev]] | Visual Studio, C/C++, Go, Rust, x64dbg, `msfvenom`, BOF compilers | *Red Team Development and Operations* Ch.1-12; *Black Hat Go* Ch.1-9; *Offensive Rust* | Build custom shellcode loader; Write AMSI/ETW bypass PoC; [HTB: Offensive Development](https://app.hackthebox.com/challenges) |
| [[Cyber-Security/Roadmap/Stage-5_Specialized#Module 27B: Malware Analysis\|27B - Malware Analysis]] 🆕 | Ghidra, IDA Pro, x64dbg, Volatility 3, Cuckoo Sandbox, YARA, ProcMon | *Practical Malware Analysis* (Sikorski/Honig); *Malware Analyst's Cookbook*; *The Art of Memory Forensics* | Analyze 10+ malware samples; [FLARE VM](https://github.com/mandiant/flare-vm); [Malware Traffic Analysis](https://www.malware-traffic-analysis.net); Write YARA rules |
| [[Cyber-Security/Roadmap/Stage-5_Specialized#Module 27C: Vulnerability Research & Fuzzing\|27C - Vuln Research]] 🆕 | AFL++, LibFuzzer, honggfuzz, Ghidra, BinDiff, pwntools, CodeQL | *The Fuzzing Book*; *A Bug Hunter's Diary*; *The Art of Software Security Assessment* | Fuzz 5+ targets; Find 1+ CVE-worthy bug; Write exploit PoC; [Fuzzing101](https://github.com/antonio-morales/Fuzzing101) |
| [[Cyber-Security/Roadmap/Stage-5_Specialized#Module 28: AI & LLM Red Teaming\|28 - AI Red Teaming]] | Python, OpenAI/Anthropic APIs, LangChain, HuggingFace, prompt injection frameworks | *AI Security* (Emily Fox); LLM security papers (arXiv); OWASP LLM Top 10 guide | [Gandalf AI](https://gandalf.lakera.ai) (all levels); Prompt injection CTF; Build RAG poisoning PoC; Document 3 novel attacks |
| [[Cyber-Security/Roadmap/Stage-5_Specialized#Module 29: Red Team Operations & Tradecraft\|29 - Red Team Ops]] | Sliver/Mythic C2, Cobalt Strike (conceptual), OPSEC tools, campaign frameworks | *Red Team Development and Operations* Ch.13-20; *Operator Handbook* (full); MITRE ATT&CK | Design full campaign plan; Execute multi-stage attack in lab ([Sliver C2](https://github.com/BishopFox/sliver)); Document OPSEC considerations |
| [[Cyber-Security/Roadmap/Stage-5_Specialized#Module 30: Proof of Work & Career Portfolio\|30 - Portfolio & Career]] | GitHub, LinkedIn, blog platform, OSCP/CRTO study, bug bounty platforms | *The Hacker Playbook 3* Ch.9; Career guides; OSCP syllabus; Bug bounty methodology guides | [OffSec: OSCP](https://www.offsec.com/courses/pen-200/); Publish 5+ GitHub repos; Write 3 technical blog posts; Submit 1 CVE/bug bounty |

---

## �️ Stage Topic Breakdown

> [!NOTE]
> **Purpose:** Comprehensive technical scope across all domains, mapped to execution order.
> For daily checklists, see [[#📚 Module Learning Matrix|Module Learning Matrix]].
> For module navigation, see [[#🎯 Execution Order — 5 Stages|Execution Order]].

---

### 🔵 STAGE 1 — FOUNDATION
*Modules 01–07 · ~3–4 months*

| # | Module | Category / Domain | Core Concepts & Technical Scope | Key Tools & Standards |
| :-------: | ------------------------------------------------------------------------------------------ | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| 01 | [[Cyber-Security/Roadmap/Stage-1_Foundation#Module 01: Fundamentals\|Fundamentals]] | **Hardware** | CPU Architecture (`x86/x64`, `ARM/ARM64`), CPU Registers, Instruction Sets, RAM, Cache hierarchies, Storage (`HDD/SSD/NVMe`), BIOS, UEFI, TPM 2.0, Secure Boot, DMA, I/O, PCIe, USB, Firmware, Embedded Controllers | `x86_64`, `ARM64`, UEFI, TPM 2.0 |
||| **OS Internals & Arch** | Memory Addressing, Virtual & Physical Memory, Stack & Heap internals, Pointers, Processes, Threads, Context Switching, Interrupts, System Calls, Privilege Rings (`User Mode` vs `Kernel Mode`), IPC | POSIX, Win32 API, C |
||| **Data & Logic** | Hexadecimal, Binary, ASCII, Unicode, Endianness (Big vs Little Endian), Bitwise Operations (AND, OR, XOR, NOT, Shifts), Two's Complement, Integer Overflows & Sign Issues | Hex editors, Python 3 |
||| **Physical & Mobile** | USB Architecture & HID Attacks, Serial Communication, Bluetooth & NFC fundamentals, Mobile OS Sandbox Models (Android vs iOS), APK / IPA application structures | ADB, Wireshark, Hardware analyzers |
| 02 | [[Cyber-Security/Roadmap/Stage-1_Foundation#Module 02: Linux Administration\|Linux Administration]] | **Internals & Processes** | Linux Kernel, Processes, Threads, Syscalls, Signals, File Descriptors, Sockets, Pipes, IPC, Virtual Filesystems (`/proc`, `/sys`, `/dev`), Critical Directories (`/tmp`, `/var`, `/etc`) | `bash`, `strace`, `ltrace`, `gdb` |
||| **Security Model & Access** | Users, Groups, File Permissions (rwx, octal), POSIX ACLs, Linux Capabilities, `SUID` / `SGID`, Sticky bit, `sudo` policy & sudoers configuration, Namespaces, `cgroups`, MAC (`SELinux`, `AppArmor`) | `lsof`, `ss`, `ps`, `top`, `getfacl` |
||| **Networking & Storage** | Network interfaces, Routing tables, Firewalling (`iptables`, `nftables`, `ufw`), Disk partitioning, Mount points, Inodes, LVM, Swap, Filesystems (ext4, XFS, Btrfs) | `ip`, `ss`, `iptables`, `fdisk`, `lsblk` |
||| **Services & Logging** | `systemd` unit lifecycle, Timers, Cron jobs, SSH daemon configuration & hardening, Syslog, Journald, Log monitoring, Auditd basics | `systemctl`, `journalctl`, OpenSSH, `logrotate` |
| 03 | [[Cyber-Security/Roadmap/Stage-1_Foundation#Module 03: Windows Administration\|Windows Administration]] | **Architecture & Subsystems** | Win32 API, Windows NT Kernel, Processes, Threads, DLLs, Handles, Access Tokens, Services, Registry hives (HKLM, HKCU), NTFS & ACLs/DACLs, Named Pipes, WMI, COM, RPC | Sysinternals (`Procmon`, `Process Explorer`, `Autoruns`) |
||| **Authentication & Identity** | NTLM, Kerberos, Windows Hello, Credential Providers, LSASS architecture, SAM database, LSA Secrets, DPAPI, Local Accounts vs Domain Accounts | Mimikatz, Rubeus, LSASS, `klist` |
||| **Security Controls & Logs** | UAC, Windows Defender, Windows Firewall, AppLocker, WDAC, AMSI, ETW, Security Event Logs (Event IDs 4624, 4625, 4672, 4688), Local Security Policies, GPO | Event Viewer, Group Policy Editor, Sysmon |
||| **PowerShell & Admin** | PowerShell Core (7+), Cmdlets, Pipeline, Remote Management (`WinRM`), PowerShell Script Block Logging, Constrained Language Mode (CLM), Automation scripts | PowerShell 7+, WinRM, PSReadLine |
| 04 | [[Cyber-Security/Roadmap/Stage-1_Foundation#Module 04: Networking Fundamentals\|Networking Fundamentals]] | **Physical & Data Link (L1–L2)** | Ethernet frames, MAC addressing, CSMA/CD, Switches, VLANs, 802.1Q trunking, STP, ARP protocol, ARP cache poisoning, Collision & Broadcast domains | Wireshark, `tcpdump`, `arp`, `macchanger` |
||| **Network & Transport (L3–L4)** | IPv4 & IPv6 addressing, Subnetting (CIDR, VLSM), Routing protocols (OSPF, BGP, RIP), NAT, ICMP; TCP 3-way handshake, Flags (SYN, ACK, FIN, RST, PSH, URG), Flow control, Windowing, UDP | `traceroute`, `ping`, `ipcalc`, Scapy |
||| **Application Layer (L7)** | DNS resolution & records (A, AAAA, MX, TXT, PTR, NS, SOA, SRV), DHCP lease process (DORA), HTTP/HTTPS, FTP, SSH, SMTP, POP3, IMAP, SNMP, NTP, RDP, SMB | `dig`, `nslookup`, `curl`, `nc`, `nmap` |
||| **Perimeter & Packet Analysis** | Perimeter Firewalls (Stateful vs Stateless), Proxies, NAT gateways, IDS/IPS concepts, Deep Packet Inspection (DPI), Network baselines, PCAP analysis | Wireshark, `tshark`, `tcpdump`, NetworkMiner |
| 05 | [[Cyber-Security/Roadmap/Stage-1_Foundation#Module 05: Cryptography\|Cryptography]] | **Core Concepts & Symmetric** | Symmetric Encryption (AES, ChaCha20, DES/3DES), Block Ciphers, Stream Ciphers, Cipher Modes (ECB, CBC, CTR, GCM), Hashes (MD5, SHA-1, SHA-256, SHA-3), HMAC, Salt, IV, Nonce | `openssl`, Python `cryptography`, CyberChef |
||| **Asymmetric & PKI** | Asymmetric Encryption (RSA, ECC, Diffie-Hellman, ECDH, DSA, Ed25519), Digital Signatures, PKI, Certificate Authorities (CA), X.509 certificates, CRL, OCSP, TLS 1.2/1.3 Handshake | `openssl`, `certutil`, `gpg` |
||| **Attacks & Data Protection** | Known Plaintext, Padding Oracle attacks, Length Extension, Collision attacks, Passwords at rest (`bcrypt`, `scrypt`, `Argon2`, PBKDF2) | `hashcat`, `john`, `padding-oracle-attacker` |
||| **🆕 Post-Quantum Cryptography (PQC)** | Quantum threat to RSA/ECC/DH (Shor's Algorithm), AES-256 remains quantum-resistant (Grover halves strength), "Harvest Now Decrypt Later" threat, NIST PQC standards (ML-KEM/Kyber for key exchange, ML-DSA/Dilithium for signatures, SLH-DSA hash-based), Hybrid deployment (X25519MLKEM768), Crypto-agility principles, Zero-Knowledge Proofs awareness (zk-SNARKs/STARKs) | OpenSSL 3.x, Chrome/Firefox hybrid PQC |
| 06 | [[Cyber-Security/Roadmap/Stage-1_Foundation#Module 06: Authentication Standards\|Authentication Standards]] | **Sessions & Passwords** | Password Authentication policies, Salted hashing, Session lifecycle (creation, timeout, termination), Cookie security flags (HttpOnly, Secure, SameSite), Session fixation, Session hijacking | Browser DevTools, Burp Suite, Python |
||| **Token & Modern Standards** | JWT Architecture (Header, Payload, Signature), JWS, JWE, Token algorithms, Claims validation, Expiration, Refresh tokens, Token revocation, Passkeys (FIDO2, WebAuthn), Biometrics | `jwt.io`, `jwt_tool`, FIDO2 testbeds |
||| **Federation & MFA** | OAuth 2.0 roles & grant types (Auth Code, PKCE, Client Credentials), OpenID Connect (OIDC), SAML 2.0 SSO, MFA types (SMS, TOTP, Push, FIDO hardware keys) & bypasses | OAuth Playground, Keycloak, Burp Suite |
||| **🆕 Zero Trust Architecture (ZTA)** | Zero Trust principles (never trust, always verify), Network micro-segmentation, Identity-based perimeters, Continuous verification, Least privilege access, BeyondCorp model, NIST SP 800-207, Conditional access policies, Device posture checking, Software-Defined Perimeter (SDP) | Azure AD Conditional Access, Google BeyondCorp, Zscaler |
| 07 | [[Cyber-Security/Roadmap/Stage-1_Foundation#Module 07: Web Technology Fundamentals\|Web Technology Fundamentals]] | **HTTP & Web Protocols** | HTTP/1.1, HTTP/2, HTTP/3 (QUIC), Methods (GET, POST, PUT, DELETE, PATCH, OPTIONS, HEAD), Status codes, Request/Response headers, URL structure & encoding, WebSockets, Webhooks | `curl`, Postman, Browser DevTools |
||| **Browser Security Model** | Same-Origin Policy (SOP), Cross-Origin Resource Sharing (CORS), Content Security Policy (CSP), Web Security Headers (HSTS, X-Content-Type-Options, X-Frame-Options), DOM internals, Web Storage | Chrome DevTools, Burp Suite |
||| **Modern Web Architecture** | REST APIs, JSON/XML parsing, Single Page Applications (SPAs), Server-Side Rendering (SSR), Microservices, Reverse Proxies (Nginx), CDNs, WAF fundamentals, Service-to-Service auth | Docker, Nginx, Node.js / Python |
| **01–07** | **Programming Track** *(Weekend Track)* | **Scripting & Tooling** | Python, Bash, PowerShell, C/C++, Go, Rust; syntax, data structures, regex, OOP, system APIs, CLI authoring | Python 3, Bash, PowerShell, GCC/Clang, Go, Rust |
||| **Security Domains** | Socket programming, Network packet manipulation, Custom port scanners, HTTP requests & API clients, Web scrapers, Log parsers, Exploit PoC development, Memory analysis | Scapy, Requests, BeautifulSoup, `pwntools` |

---

### 🟠 STAGE 2 — OFFENSE I
*Modules 08–13 · ~11–13.5 weeks*

| # | Module | Category / Domain | Core Concepts & Technical Scope | Key Tools & Standards |
| :--: | -------- | ------------------- | --------------------------------- | ----------------------- |
| 08 | [[Cyber-Security/Roadmap/Stage-2_Offense-I#Module 08: Footprinting & Reconnaissance\|Footprinting & Reconnaissance]] | **OSINT & Passive Recon** | Search engine dorking (Google, Bing), WHOIS databases, DNS records, ASN mapping, IP blocks & CIDR, Certificate Transparency logs, Job postings, Code repos, Tech stack discovery | `subfinder`, `assetfinder`, `amass`, `httpx`, `shodan`, `censys`, `crt.sh` |
||| **Active Recon & Intelligence** | DNS zone transfers, Subdomain brute-forcing, Web crawler discovery, Metadata harvesting (FOCA, Exif), Web technology fingerprinting, IPv6 discovery, Dark Web breach data reconnaissance | `dig`, `dnsenum`, `wafw00f`, `whatweb`, `theHarvester`, `exiftool` |
||| **🆕 Advanced OSINT** | Social media intelligence (LinkedIn, Twitter/X, Facebook), People search engines (Pipl, Spokeo), Business intelligence (Crunchbase, Owler), Breach databases (HIBP, Dehashed), Company infrastructure mapping, Email pattern analysis, Employee profiling, Document metadata, Public code repositories (GitHub, GitLab), Conference talks & presentations, Patent databases, Domain history & archived sites | Maltego, SpiderFoot, Recon-ng, OSINT Framework, Archive.org |
| 09 | [[Cyber-Security/Roadmap/Stage-2_Offense-I#Module 09: Scanning\|Scanning]] | **Host Discovery & Topology** | ARP ping sweeps, ICMP discovery (Echo, Timestamp, Subnet mask), TCP SYN/ACK discovery sweeps, UDP sweeps, Network boundary mapping | `nmap`, `fping`, `masscan`, `netdiscover`, `arp-scan` |
||| **Port & Service Scanning** | TCP Connect (`-sT`), SYN Stealth (`-sS`), UDP scanning (`-sU`), Null, FIN, Xmas scans, Full port ranges (`-p-`), Service version detection (`-sV`), OS fingerprinting (`-O`) | `nmap`, `masscan`, `naabu`, `rustscan` |
||| **Defense Assessment & Evasion** | Fragmented packets, Decoy scanning (`-D`), Source port spoofing, Timing templates (`-T0` to `-T5`), Firewall/IDS detection, NSE vulnerability scanning scripts | `nmap` (NSE), Scapy, `hping3` |
||| **🆕 Wireless & IoT Scanning** | WiFi enumeration (2.4GHz/5GHz/6GHz bands, WEP/WPA/WPA2/WPA3), Bluetooth scanning (BLE, Classic), Zigbee/Z-Wave discovery, LoRa/LoRaWAN, RFID/NFC scanning, IoT protocol discovery (MQTT, CoAP, AMQP), Router/AP fingerprinting, WiFi handshake capture, Evil twin AP setup, Bluetooth pairing attacks, IoT firmware extraction | Aircrack-ng suite, `hcxdumptool`, `hcxtools`, Kismet, Bluez utils, `ubertooth`, SDR tools (HackRF, RTL-SDR), Wireshark (Zigbee), `nmap` IoT scripts |
| 10 | [[Cyber-Security/Roadmap/Stage-2_Offense-I#Module 10: Enumeration\|Enumeration]] | **SMB, RPC & NetBIOS** | Null sessions, SMB shares, Permissions, Users, Groups, Password policies, NetBIOS names, RPC endpoints & interfaces | `enum4linux-ng`, `smbclient`, `netexec`, `rpcclient`, `smbmap` |
||| **Network Services & Directory** | SNMP MIB walking (v1/v2c/v3 communities), SMTP user enumeration (VRFY, EXPN, RCPT TO), LDAP queries, Active Directory base enumeration, DNS enumeration, NFS exports | `snmpwalk`, `onesixtyone`, `smtp-user-enum`, `ldapsearch`, `showmount` |
||| **Web & App Enumeration** | HTTP banner grabbing, Web server extensions, Virtual host (`vhost`) discovery, Hidden directories & files, API endpoints, Enumeration OPSEC & traffic analysis | `gobuster`, `ffuf`, `feroxbuster`, `nikto`, `curl` |
| 11 | [[Cyber-Security/Roadmap/Stage-2_Offense-I#Module 11: Database Security\|Database Security]] | **SQL Databases** | MySQL, PostgreSQL, Microsoft SQL Server (`MSSQL`), Oracle, SQLite; In-band, Error-based, Union-based, Blind Boolean/Time-based SQLi, `xp_cmdshell`, `UDF`, `INTO OUTFILE` | `sqlmap`, `dbeaver`, native DB CLIs |
||| **NoSQL & Cache** | MongoDB injection & operator abuse, Redis unauthenticated command execution (SSH key drop, webshell drop), Elasticsearch API exploitation | `nosqlmap`, `redis-cli`, `curl` |
||| **PrivEsc & Hardening** | Database privilege escalation, DBA role abuse, Trust links, Data encryption at rest/transit, DB auditing, Hardening baselines | Native DB CLIs, Audit scripts |
| 12 | [[Cyber-Security/Roadmap/Stage-2_Offense-I#Module 12: Password Cracking & Hash Analysis\|Password Cracking & Hash Analysis]] | **Hash Analysis & Acquisition** | Identifying hash algorithms, Salted hashes, Windows NTLM & LM, Kerberos tickets (krb5tgs, krb5asrep), Linux `/etc/shadow`, Database hashes, Archive hashes (Zip, Rar) | `hash-identifier`, `hashid`, Name-That-Hash |
||| **Cracking Methodology** | Dictionary attacks, Brute-force, Hybrid attacks, Mask attacks, Rule-based cracking (best64, custom rules), Wordlist curation & mutation, Secrets extraction (SAM, LSASS, NTDS.dit) | `hashcat`, `john`, `cewl`, `cupp`, `secretsdump.py` |
||| **Protocol & Online Attacks** | Online brute-force attacks, Password spraying (SMB, SSH, RDP, FTP, HTTP), Lockout policy handling; Protocol cracking (NetNTLMv1/v2, WPA2/WPA3 4-way handshake, PMKID) | `hydra`, `medusa`, `crowbar`, `aircrack-ng` |
| 13 | [[Cyber-Security/Roadmap/Stage-2_Offense-I#Module 13: System Hacking & Initial Compromise\|System Hacking & Initial Compromise]] | **Initial Access & Payloads** | Vulnerability exploitation, Metasploit Framework, Exploit-DB PoCs, Custom exploit modification, Reverse shells, Bind shells, Web shells, Staged vs Stageless payloads, Handlers | `msfconsole`, `msfvenom`, `nc`, `socat`, `revshells.com` |
||| **Linux PrivEsc** | `SUID` / `SGID` binary abuse, `sudo -l` privileges & CVEs, Linux Capabilities (`cap_setuid`), Vulnerable Cron jobs, Systemd services, `$PATH` hijacking, Kernel exploits | `linpeas.sh`, `GTFOBins`, `pspy`, `unix-privesc-check` |
||| **Windows PrivEsc** | Service misconfigurations (Unquoted paths, weak permissions), Registry autoruns, AlwaysInstallElevated, Token impersonation (`SeImpersonate`), UAC bypasses, DLL hijacking, Kernel exploits | `winpeas.exe`, `Seatbelt`, `PowerUp`, `SharpUp`, `JuicyPotato` |
||| **Persistence & Lateral Move** | Persistence mechanisms (SSH keys, cron, registry, services, scheduled tasks), Living off the Land (LOLBAS / GTFOBins), Timestomping, Log clearing, Staging & data exfiltration | LOLBAS, PowerShell, Impacket suite |

---

### 🟣 STAGE 3 — WEB & APP SEC
*Modules 14–18 · ~7–10.5 weeks*

| # | Module | Category / Domain | Core Concepts & Technical Scope | Key Tools & Standards |
| :--: | -------- | ------------------- | --------------------------------- | ----------------------- |
| 14 | [[Cyber-Security/Roadmap/Stage-3_Web-and-App-Sec#Module 14: Web Application Hacking\|Web Application Hacking]] | **OWASP Top 10 Exploitation** | SQL Injection, Cross-Site Scripting (`XSS` — Stored/Reflected/DOM), `SSRF`, `XXE`, `BOLA` / `IDOR`, Path Traversal / LFI / RFI, Command Injection, Insecure Deserialization, `SSTI`, Access Control | Burp Suite Pro, OWASP ZAP, `sqlmap`, `ffuf`, `commix` |
||| **Modern Web Attacks** | HTTP Request Smuggling (CL.TE, TE.CL, TE.TE), Web Cache Poisoning & Deception, Host Header attacks, HTTP Desync, Client-side Prototype Pollution, Race Conditions, Logic flaws | Turbo Intruder, HTTP Request Smuggler |
||| **Post-Exploit & Defense** | Webshell deployment, Database pivoting, Server persistence, Defense mechanisms, WAF bypass techniques, Input validation, Content Security Policy (`CSP`) | Antak, Weevely, WAFW00F, Custom scripts |
| 15 | [[Cyber-Security/Roadmap/Stage-3_Web-and-App-Sec#Module 15: Session Hijacking & Token Attacks\|Session Hijacking & Token Attacks]] | **Session Architecture** | Session generation entropy, Session fixation, Predictable session IDs, Cookie security attributes (`HttpOnly`, `Secure`, `SameSite=Strict/Lax/None`), Session termination flaws | Burp Sequencer, Cookie Editor, DevTools |
||| **Token Theft & Forgery** | XSS token theft, MITM session hijacking, Cross-Site WebSocket hijacking; JWT exploitation: `none` algorithm, weak HMAC secrets, Algorithm confusion, `kid` / `jku` header injection, Token replay | `jwt_tool`, Burp Suite, Wireshark |
| 16 | [[Cyber-Security/Roadmap/Stage-3_Web-and-App-Sec#Module 16: Web Server Hacking\|Web Server Hacking]] | **Server Recon & Misconfig** | Web server footprinting (Apache, Nginx, IIS, Tomcat), HTTP verb tampering, Default credentials, Unprotected admin interfaces, Exposed source control (`.git`), Backup files | `nikto`, `whatweb`, `git-dumper`, `ffuf` |
||| **Server Exploitation** | Directory traversal, Server-Side Code Execution, Apache path traversal (CVE-2021-41773), Nginx alias traversal, Tomcat Manager WAR deployment, IIS short filename vulnerability | Metasploit, `davtest`, `cadaver`, Exploit-DB PoCs |
| 17 | [[Cyber-Security/Roadmap/Stage-3_Web-and-App-Sec#Module 17: API Security\|API Security]] | **REST APIs & OWASP API Top 10** | API reconnaissance, Swagger / OpenAPI parsing, `BOLA`, `BOPLA`, `BFLA`, Unrestricted resource consumption, Mass assignment, Security misconfigurations, Verbose error handling | Postman, `kiterunner`, `mitmproxy`, `arjun`, `ffuf` |
||| **GraphQL & Modern Protocols** | GraphQL introspection, Query depth & complexity exhaustion, Batching attacks, Field suggestions; gRPC endpoint enumeration, WebSockets vulnerabilities, API Gateway bypasses | InQL, GraphQL Raider, Altair, `grpc_cli` |
||| **API Auth & Hardening** | API Key exposure, OAuth 2.0 grant vulnerabilities, OpenID Connect token verification, JWT authentication bypasses in APIs, Rate limiting & WAF bypasses | Burp Suite, OAuth Playground, `jwt_tool` |
| 17B 🆕 | [[Cyber-Security/Roadmap/Stage-3_Web-and-App-Sec#Module 17B: Mobile Application Security\|Mobile Application Security]] | **Mobile Recon & Setup** | Android vs iOS security models, APK/IPA structure, Rooting/Jailbreaking, ADB, Frida instrumentation, SSL pinning bypass, Certificate trust store manipulation | Android Studio, Xcode, Frida, Objection, MobSF |
||| **OWASP Mobile Top 10** | Insecure Data Storage, Weak Cryptography, Insecure Authentication, Insecure Communication, Code Tampering, Reverse Engineering, Insecure Authorization, Client-side Injection | JADX, APKTool, Ghidra, Hopper, IDA Pro |
||| **Mobile API Security** | Mobile-specific API vulnerabilities, Certificate pinning bypass, Token storage analysis, Mobile OAuth flows, Deep link exploitation, Push notification security, Mobile backend communication analysis | Burp Suite Mobile Assistant, Charles Proxy, mitmproxy, Frida scripts |
||| **Platform-Specific Attacks** | Android: Intent spoofing, Exported components, Broadcast receivers, Content providers; iOS: IPC exploitation, Keychain analysis, URL scheme hijacking, Biometric bypass | drozer, Cycript, class-dump, SSL Kill Switch |
||| **Mobile Defense & Hardening** | Code obfuscation, Runtime Application Self-Protection (RASP), Root/Jailbreak detection, Anti-debugging, Certificate pinning implementation, Secure storage practices, Mobile DevSecOps | ProGuard, R8, DexGuard, AppShield
| 18 | [[Cyber-Security/Roadmap/Stage-3_Web-and-App-Sec#Module 18: Bug Bounty Methodology\|Bug Bounty Methodology]] | **Scoping & Wide Recon** | Bug bounty platform dynamics (HackerOne, Bugcrowd, Intigriti), Rules of Engagement, Wide-scope reconnaissance, ASN & CIDR enumeration, Subdomain takeovers, GitHub dorking | `subfinder`, `amass`, `nuclei`, `subjack`, `trufflehog` |
||| **Chaining & Professional Triage** | Low-severity to High/Critical chaining, Business logic exploitation, Account takeover chains, Proof of Concept creation, CVSS calculation, Professional triager communication | Markdown report templates, Burp Suite Pro |
|| [[Cyber-Security/Roadmap/Stage-3_Web-and-App-Sec#Side-Track A: Detection Engineering & SOC Operations\|Side-Track A: Detection Engineering & SOC]] *(Parallel Track)* | **Defensive Architecture & Telemetry** | Enterprise defense models, Network & Host telemetry, Sysmon event logging, Windows Security Events, Linux Auditd, EDR/XDR architecture, SIEM data ingestion & normalization | Sysmon, Velociraptor, Elastic Agent, Wazuh |
||| **Detection Engineering & Hunting** | Detection rules authoring, Sigma rules, YARA rules, MITRE ATT&CK mapping, Hypothesis-driven threat hunting, Alert triage & SOC workflows, Incident response fundamentals | Sigma, YARA, Splunk, Elastic SIEM |
|| [[Cyber-Security/Roadmap/Stage-3_Web-and-App-Sec#Side-Track B: IDS, Firewalls, and Honeypots\|Side-Track B: IDS, Firewalls, and Honeypots]] *(Parallel Track)* | **Network Defenses & Deception** | Stateful vs Stateless firewalls, Linux `nftables` / `iptables`, pfSense / OPNsense, Suricata & Snort IDS/IPS rule writing, Evasion detection, Honeypots & deception, Email & DNS security | Suricata, Snort, Cowrie, pfSense, Wireshark |
|| [[Cyber-Security/Roadmap/Stage-3_Web-and-App-Sec#Side-Track C: Cyber Threat Intelligence (CTI) & Attack Surface Management\|Side-Track C: CTI & Attack Surface Management]] *(Parallel Track)* | **Threat Intel & EASM** | External Attack Surface Management, Threat actor profiling, IOCs & IOAs, Threat intelligence feeds, CTI platforms, MITRE ATT&CK & Diamond Model analysis, Intel operationalization | MISP, OpenCTI, Maltego, SpiderFoot |

---

### 🏢 STAGE 4 — ENTERPRISE
*Modules 19–26 · ~12–16 weeks*

| # | Module | Category / Domain | Core Concepts & Technical Scope | Key Tools & Standards |
| :--: | -------- | ------------------- | --------------------------------- | ----------------------- |
| 19 | [[Cyber-Security/Roadmap/Stage-4_Enterprise#Module 19: Active Directory & Entra ID\|Active Directory & Entra ID]] | **AD Architecture & Enumeration** | Forests, Domains, Trees, Trusts, Domain Controllers, Global Catalogs, Schema, GPOs, OUs; PowerView & BloodHound graph analysis, LDAP enumeration, Domain querying | BloodHound / SharpHound, PowerView, `ldapsearch`, `netexec` |
||| **Kerberos & Credential Attacks** | Kerberos protocol (AS-REQ/REP, TGS-REQ/REP, AP-REQ), Kerberoasting, AS-REP Roasting, Pass-the-Hash (`PtH`), Pass-the-Ticket (`PtT`), Overpass-the-Hash, Silver & Golden Tickets | Rubeus, Mimikatz, Impacket (`GetUserSPNs.py`, `secretsdump.py`) |
||| **ACLs, Delegation & ADCS Abuse** | GenericAll, WriteDacl, GenericWrite abuse; Unconstrained, Constrained, and Resource-Based Constrained Delegation (`RBCD`); Active Directory Certificate Services (`ADCS`) ESC1–ESC8 | Certify, PKINITtools, BloodHound, PowerView |
||| **Lateral Movement & Persistence** | DCSync attack, DCShadow, Skeleton Key, DSRM credential abuse, AdminSDHolder persistence, GPO backdoors, WMI & WinRM execution, DCOM execution, Remote Registry | Mimikatz, Impacket (`wmiexec.py`, `psexec.py`), Evil-WinRM |
||| **Entra ID (Azure AD) & Hybrid** | Azure AD Connect exploitation, Password Hash Sync, ADFS attacks, Seamless SSO abuse, Primary Refresh Token (`PRT`) abuse, Hybrid identity attacks, Azure RBAC privilege escalation | AADInternals, ROADtools, Azure CLI, MicroBurst |
| 19A 🆕 | [[Cyber-Security/Roadmap/Stage-4_Enterprise#Module 19A: SOC & Security Operations\|SOC & Security Operations]] | **SOC Fundamentals & Architecture** | SOC models (in-house, co-managed, MSSP), SOC tiers (L1/L2/L3), Roles & responsibilities, Shift operations, Escalation procedures, SOC metrics (MTTD, MTTR, MTTA), Incident classification, NIST Cybersecurity Framework, Kill Chain & MITRE ATT&CK | SOC workflow tools, NIST CSF, MITRE ATT&CK |
||| **Log Management & Analysis** | Log sources (Windows Events, Syslog, Application logs), Log collection architecture, Log parsing & normalization, Retention policies, Log storage optimization, Common log analysis patterns, Baseline establishment | Syslog-ng, rsyslog, Logstash, Fluentd |
||| **SIEM Architecture & Engineering** | Log aggregation, Parsing & normalization, Data enrichment, Retention policies, SIEM platforms (Splunk, Elastic, Sentinel, QRadar), SPL, KQL, Lucene, Field extraction, Dashboards | Splunk, Elastic Stack, Microsoft Sentinel, Wazuh |
||| **EDR & Telemetry** | Endpoint Detection & Response architecture, Sysmon configuration, Windows Security Events, Linux Auditd, Process telemetry, Network telemetry, File system monitoring, Registry monitoring | Sysmon, Velociraptor, OSQuery, Wazuh agents |
||| **Detection Engineering** | Detection rule logic, Sigma rules, YARA, Custom detection pipelines, Alert tuning (False positives/negatives), Detection-as-Code, Alert prioritization, Detection validation | Sigma, YARA, Atomic Red Team, Detection Lab |
||| **Threat Hunting** | Hypothesis-driven hunting, Hunt playbooks, IOC/IOA identification, Anomaly detection, Threat intelligence integration, Hunt metrics, Crown Jewel analysis, Adversary emulation for hunt validation | Jupyter notebooks, Velociraptor, OSQuery, Hunt platform |
||| **Incident Response & SOAR** | Incident triage, Escalation procedures, Playbooks, Mean Time to Detect (MTTD), Mean Time to Respond (MTTR), SOAR automation, Case management, Chain of custody | TheHive, Cortex, Shuffle, MISP |
| 20 | [[Cyber-Security/Roadmap/Stage-4_Enterprise#Module 20: Cloud Computing\|Cloud Security]] | **Cloud Architecture & IAM** | AWS, Azure, GCP models, Shared responsibility, Cloud root boundaries; IAM Policies, Roles, Groups, Service Accounts, AssumeRole, Cross-account access, STS tokens | AWS CLI, Azure CLI, gcloud, Pacu |
||| **Storage, Compute & Metadata** | S3 buckets, Azure Blob, GCS permissions, Public exposure analysis; EC2, Azure VMs; Instance Metadata Service (IMDSv1 vs IMDSv2), Metadata theft via SSRF, Cloud IaC | `s3scanner`, Pacu, ScoutSuite, Prowler |
||| **Exploitation & Persistence** | Privilege escalation vectors in AWS/Azure, Shadow admins, IAM backdoor persistence, Serverless (Lambda/Functions) attacks, CloudTrail evasion, Cloud posture auditing | Pacu, Prowler, ScoutSuite, CloudSploit |
| 21 | [[Cyber-Security/Roadmap/Stage-4_Enterprise#Module 21: Container & Orchestration Security\|Containers & Kubernetes]] | **Container Internals & Escapes** | Docker engine architecture, Linux namespaces (PID, Mount, Net, IPC, User), `cgroups`, Docker daemon socket exposure, Privileged containers, Capabilities abuse, Container breakout | Docker CLI, `deepce`, `cdk-go`, `amicontained` |
||| **Kubernetes Security & Attacks** | K8s architecture (API Server, Kubelet, etcd, Controller Manager), Anonymous kubelet access, etcd credential dumping, Pod service account tokens (`JWT`), RBAC misconfigs, PrivEsc | `kubectl`, `kube-hunter`, `kube-bench`, `peirates` |
||| **Secrets & Configuration Management** | Kubernetes Secrets, ConfigMaps, etcd encryption at rest, Sealed Secrets, External Secrets Operator, HashiCorp Vault integration, SOPS, Secret sprawl, Environment variable leakage, Init container secrets | Sealed Secrets, External Secrets, Vault, SOPS |
||| **Supply Chain Security 🆕** | Software Bill of Materials (SBOM), Image signing (Cosign, Notary), SLSA framework, Supply chain levels, Provenance attestation, OPA Gatekeeper admission control, Policy as Code, Dependency confusion | Cosign, Syft, SLSA, OPA Gatekeeper, in-toto |
||| **Runtime, CI/CD & Hypervisors** | Container runtime security (runc, containerd), AppArmor/Seccomp, Image scanning; CI/CD security (GitHub Actions poisoning, Jenkins RCE, pipeline secrets); Hypervisor escape concepts | Trivy, Grype, Falco, Semgrep |
| 22 | [[Cyber-Security/Roadmap/Stage-4_Enterprise#Module 22: Adversary Emulation & Purple Teaming\|Adversary Emulation]] | **MITRE ATT&CK & Emulation** | ATT&CK matrix (Tactics, Techniques, Procedures), Navigator heatmaps, Threat actor profiling (APT29, FIN7), Emulation plans, Atomic Red Team execution, Automated emulation platforms | MITRE ATT&CK Navigator, Atomic Red Team, Caldera, Prelude Operator |
||| **Purple Teaming & Metrics** | Collaborative offensive-defensive exercises, Detection gap analysis, EDR alert validation, Log coverage assessment, Security posture metrics (MTTD, MTTR), Purple team reporting | VECTR, Sigma, Sysmon, Elastic SIEM |
| 23 | [[Cyber-Security/Roadmap/Stage-4_Enterprise#Module 23: Sniffing & Spoofing\|Lateral Movement & Sniffing]] | **Sniffing & Traffic Interception** | Promiscuous mode, Raw sockets, Passive network sniffing, Cleartext credential extraction (FTP, HTTP, Telnet, SNMP), Network protocol dissection, Wireshark display filters | Wireshark, `tshark`, `tcpdump`, `dsniff` |
||| **Spoofing, MITM & Poisoning** | ARP cache poisoning, DNS spoofing, DHCP starvation & rogue DHCP, LLMNR & NBT-NS poisoning, WPAD spoofing, NTLM relaying, SSL stripping, Network MITM defenses | `responder`, `bettercap`, `ettercap`, `mitmproxy`, `ntlmrelayx.py` |
| 24 | [[Cyber-Security/Roadmap/Stage-4_Enterprise#Module 24: Social Engineering\|Social Engineering]] | **Psychology & Target Profiling** | Principles of influence (Authority, Scarcity, Urgency, Reciprocity, Social Proof), OSINT target profiling, Organizational charts, Corporate email naming conventions, Relationship mapping | LinkedIn, Maltego, theHarvester, Hunter.io |
||| **Delivery Vectors & Physical** | Spear-phishing campaigns, Phishing infrastructure setup (SMTP, Lookalike domains, SPF/DKIM/DMARC, Reverse proxies), Credential harvesting, Vishing, Smishing, USB drops, Physical access | GoPhish, Evilginx2, SET, Modlishka |
| 25 | [[Cyber-Security/Roadmap/Stage-4_Enterprise#Module 25: Malware & Weaponization (Conceptual)\|Malware & C2 Architectures]] | **Architecture & Staging** | Droppers, Downloaders, Stagers, Full-stage payloads, C2 beacon mechanics, Communication channels (HTTP, HTTPS, DNS, SMB), Heartbeats, Jitter, Malleable C2 profiles | Sliver, Mythic, Cobalt Strike concepts |
||| **Execution & Evasion Mechanisms** | Process injection (CreateRemoteThread, Process Hollowing, APC Queue), DLL injection, Syscalls vs Win32 APIs, AMSI & ETW bypass concepts, Obfuscation, Persistence, Counter-forensics | Conceptual code, x64dbg, PE-bear, Process Hacker |
||| **Artifacts & Memory Forensics** | Memory analysis concepts, Volatility framework, Identifying injected code, Malfind, Memory artifacts, Document weaponization (Macros, LNK files, ISO/VHD packaging) | Volatility 3, CyberChef, OLETools |
| 26 | [[Cyber-Security/Roadmap/Stage-4_Enterprise#Module 26: Pentest Methodologies & Report Writing\|Pentest Reporting]] | **Frameworks, Scoping & Legal** | Penetration testing execution standards (PTES, NIST SP 800-115, OWASP Web Testing Guide, OSSTMM), Rules of Engagement (RoE), NDA, Scoping boundaries, Legal compliance & liability | Engagement checklists, PTES guidelines |
||| **Threat Modeling & Risk Scoring** | Threat modeling methodologies (STRIDE, PASTA, DREAD), Vulnerability scoring (CVSS v3.1 / v4.0 metrics, Base/Temporal/Environmental scores), EPSS, Business risk contextualization | FIRST CVSS Calculator, Threat Modeling tools |
||| **Technical Delivery & Reports** | Professional pentest report structure: Executive Summary, Methodology, Scope, Detailed Technical Findings, Reproduction Steps, Risk Matrix, Root Cause Analysis, Remediation Roadmaps | Markdown / LaTeX report templates, Typora, Git |

---

### 🔬 STAGE 5 — SPECIALIZED
*Modules 27–30 · ~15–22 weeks*

| # | Module | Category / Domain | Core Concepts & Technical Scope | Key Tools & Standards |
| :--: | -------- | ------------------- | --------------------------------- | ----------------------- |
| 27 | [[Cyber-Security/Roadmap/Stage-5_Specialized#Module 27: Offensive Development & Tooling\|Offensive Development]] | **Systems Programming Foundations** | C & C++ for security practitioners, Pointers, Memory allocation, Stack/Heap internals, Win32 API, Native APIs (NTDLL), Direct Syscalls, Assembly (x86/x64), Linux POSIX system calls | GCC/Clang, Visual Studio, MSVC, x64dbg, Ghidra |
||| **Exploit Dev & Windows OffSec** | Stack-based buffer overflows, Shellcode writing & encoding, Bad characters, Bypassing DEP/NX with ROP chains, ASLR bypasses; Process injection, Direct syscalls, PE parsing, EDR unhooking, AMSI/ETW patching | `pwntools`, Mona.py, x64dbg, Visual Studio |
||| **Linux OffSec Dev & C2 Implants** | Linux ELF binary manipulation, Custom LD_PRELOAD hooks, ptrace injection, Rootkit concepts; Custom C2 implant architecture in Go/Rust/C++, Encrypted communications, Sleep obfuscation, Task execution queue | GCC, Go, Rust, Wireshark |
| 27B 🆕 | [[Cyber-Security/Roadmap/Stage-5_Specialized#Module 27B: Malware Analysis\|Malware Analysis]] | **Static Analysis & Reverse Engineering** | PE (Portable Executable), ELF, Mach-O structure, Static triage, Strings analysis, Imports/Exports, Packing detection, Unpacking, Disassembly (IDA, Ghidra, Binary Ninja), Control Flow & Data Flow Analysis | Ghidra, IDA Pro, Binary Ninja, radare2, PE-bear |
||| **Dynamic & Behavioral Analysis** | Sandbox environments (Cuckoo, ANY.RUN), Process monitoring (ProcMon, Process Hacker), API call tracing, Registry changes, File system activity, Network traffic analysis, Anti-analysis evasion | Cuckoo Sandbox, Process Monitor, Wireshark, Regshot |
||| **Advanced Dynamic Analysis & Debugging** | Debugger fundamentals (x64dbg, WinDbg, GDB), Breakpoint strategies, Single-stepping, Memory inspection, API hooking detection, Anti-debugging techniques bypass, Malware unpacking in debugger, Shellcode extraction | x64dbg, WinDbg, GDB, OllyDbg, API Monitor |
||| **Memory Forensics** | Memory dumps acquisition, Volatility framework, Process injection detection, Malfind plugin, Rootkit detection, Hidden process enumeration, Network connection analysis, Code cave analysis, Memory-only malware | Volatility 3, Rekall, YARA rules, WinDbg |
||| **Reverse Engineering Techniques** | IDA Pro/Ghidra workflows, Function identification, Cross-references analysis, Decompilation, Binary patching, Obfuscation analysis (control flow flattening, string encryption), Code emulation, Symbolic execution | IDA Pro, Ghidra, Binary Ninja, angr, Unicorn Engine |
| 27C 🆕 | [[Cyber-Security/Roadmap/Stage-5_Specialized#Module 27C: Vulnerability Research & Fuzzing\|Vulnerability Research & Fuzzing]] | **Vulnerability Research Methodology** | Target selection (high-value targets, complex parsers), Attack surface mapping (input vectors, file formats, protocols, APIs), Vulnerability classes (memory corruption, logic bugs, injection flaws, integer overflows), Crash triage (debugger, stack traces, exploitability assessment, test case minimization), Exploit development (PoC, reliability, weaponization, responsible disclosure) | Debuggers, EXPLOITABLE plugin, Delta debugging |
||| **Fuzzing Fundamentals** | Mutation-based fuzzing (bit flips, byte insertions, Radamsa, zzuf), Generation-based fuzzing (grammar-based inputs, Peach, Boofuzz), Crash detection (sanitizers: ASan/MSan/UBSan, debugger automation, deduplication), Corpus management (seed corpus, minimization, coverage-driven selection) | Radamsa, zzuf, Peach Fuzzer, Boofuzz |
||| **Coverage-Guided Fuzzing** | AFL++ (compile-time instrumentation, edge coverage, queue management, persistent mode, custom mutators, QEMU mode, MOpt, CmpLog, RedQueen), LibFuzzer (in-process fuzzing, LLVMFuzzerTestOneInput, corpus sync), Harness development (input parsing, memory management, initialization overhead), Coverage analysis (lcov, gcov, unreached code identification) | AFL++, LibFuzzer, honggfuzz, QEMU |
||| **Network & Protocol Fuzzing** | Stateful protocol fuzzing (session management, state machines, Boofuzz, Sulley), Boofuzz framework (protocol structure definition with primitives, session callbacks, target monitoring), API fuzzing (REST APIs, GraphQL, SOAP/XML-RPC), Custom network fuzzers (Scapy packet crafting, raw sockets, multi-layer fuzzing, Wireshark analysis) | Boofuzz, Scapy, Burp Intruder, ffuf, wfuzz, Wireshark |
||| **CVE Assignment & Responsible Disclosure** | CVE request process (MITRE workflow, CNA process, technical description, CVE ID assignment), Coordinated disclosure (90-day timeline, vendor notification, patch verification, public disclosure timing), Bug bounty platforms (HackerOne, Bugcrowd, scope definition, severity classification, report writing), Responsible disclosure ethics (avoid weaponization, legal considerations, researcher reputation) | MITRE CVE form, HackerOne, Bugcrowd, CVSS scoring |
| 28 | [[Cyber-Security/Roadmap/Stage-5_Specialized#Module 28: AI & LLM Red Teaming\|AI & LLM Red Teaming]] | **AI Foundations & LLM Vulns** | Machine Learning, Transformers, LLM architecture, Tokenization, Embeddings, Vector databases, Retrieval-Augmented Generation (`RAG`); OWASP Top 10 for LLMs, Direct & Indirect Prompt Injection, Jailbreaks, System Prompt extraction | LangChain, LlamaIndex, OpenAI / Anthropic APIs, `garak`, `pyrit` |
||| **Agent Security & Adversarial ML** | AI Agent architecture, Tool / Function calling vulnerabilities, Excessive agency, Context poisoning, Memory injection, Model inversion, Training data poisoning, Adversarial perturbations, AI red team automation | Custom testbeds, NeMo Guardrails, Mindgard |
| 28 | **Modern Attack Surfaces** *(Parallel Track)* | **Cloud-Native & CI/CD Security** | Containers, Serverless, Service Mesh, API Ecosystems, Microservices, Zero Trust; Secure SDLC, Source Code Security, SAST/DAST/SCA, Secret Scanning, CI/CD Pipeline Security, Git Security, Container & IaC Security, SBOM, Supply Chain Attacks | Semgrep, Trivy, Cosign, Syft |
||| **Web3 & Blockchain** | Blockchain Architecture, Ethereum & EVM, Solidity, Smart Contracts, Wallets, Tokens, DeFi Protocols, Oracles, Bridges, Signatures; Reentrancy, Access Control Flaws, Integer Issues, Oracle Manipulation, Flash Loans, Blockchain Forensics | `slither`, `mythril`, Foundry, Remix |
||| **IoT & Embedded Systems** | Embedded Systems, Firmware Internals, Bootloaders, Hardware Interfaces (`UART`, `SPI`, `I2C`, `JTAG`), Hardware Debugging, Firmware Extraction, Firmware Analysis, Secure Boot Bypasses, Device Authentication | `binwalk`, Saleae Logic, JTAGulator |
| 29 | [[Cyber-Security/Roadmap/Stage-5_Specialized#Module 29: Red Team Operations & Tradecraft\|Red Team Operations]] | **Campaign Planning & Infra** | Threat actor emulation planning, Red team infrastructure setup (Redirectors, Long-haul vs Short-haul C2, Domain fronting/categorization, CDN routing), Malleable C2 profiles, Operational Security (`OPSEC`), Covert communications | Sliver, Mythic, Cobalt Strike, Nginx redirectors |
||| **Execution & Lateral Movement** | Assumed-breach methodology, Credential access in hardened environments, Cross-forest pivoting, Low-and-slow data exfiltration, Deconfliction procedures with defensive teams, Executive debriefing & timeline reconstruction | Sliver, Impacket, BloodHound, Rubeus |
| 29 | **Defensive Awareness** *(Parallel Track)* | **DFIR & Incident Response** | Disk Forensics, Memory Forensics, Network Forensics, Evidence Preservation, Timeline Analysis, Incident Response Triage, Containment, Eradication, Recovery, Root Cause Analysis, IOC Analysis, Malware Investigation | `volatility`, `autopsy`, `ftk`, Wireshark |
||| **SOC / SIEM / EDR & Hunting** | Detection Engineering, Alert Triage, Incident Investigation, SOC Workflows, Log Ingestion, Correlation Rules, Event Normalization, Alert Logic, Sigma Rules, Endpoint Detection, Behavioral Detection, Threat Hunting | Splunk, Elastic SIEM, Sigma rules, Sysmon, Velociraptor |
| 29 | **Intelligence** *(Parallel Track)* | **Threat Intelligence** | Threat Actors, Campaigns, Malware Families, Infrastructure, IOCs, IOAs, TTPs, Domains, IPs, Hashes, Infrastructure Correlation, Threat Attribution, Threat Intelligence Reports, MITRE ATT&CK Mapping | MISP, OpenCTI, MITRE ATT&CK |
||| **OSINT & Dark Web Intel** | Search Intelligence, Domain & DNS Intelligence, Username & Email Intel, Public Records, Exif Metadata, Image & Video Geolocation, Breach Intelligence; Tor, Onion Services, Underground Markets, Cybercrime Ecosystems | `maltego`, `spiderfoot`, `shodan`, `censys`, Tor Browser |
| 30 | [[Cyber-Security/Roadmap/Stage-5_Specialized#Module 30: Proof of Work & Career Portfolio\|Proof of Work & Career]] | **Hands-on Proof & Labs** | Public portfolio construction, Hack The Box (`HTB`) Pro Labs writeups, TryHackMe (`THM`) milestones, PortSwigger Web Security Academy completions, VulnHub, Enterprise multi-cloud and AD lab demonstrations | HTB Pro Labs, PortSwigger Academy, GitHub |
||| **Engagements, CVEs & Research** | Penetration Testing Methodologies, Scope Definition, RoE, Exploitation & Reporting; CVE Request & Coordinated Vulnerability Disclosure process, Vulnerability Reproduction, PoC development, Security Advisories | Mitre CVE program, GitHub Advisories, Exploit-DB |
||| **Portfolio & Career Strategy** | Research Papers, Blog Posts, CVE Write-ups, Open Source Tool authoring & maintenance, Industry Certifications (OSCP, CPTS, CRTO, CISSP), Technical Interview & Whiteboard Defense preparation | GitHub, Medium / Substack, GitBook, LinkedIn |

---

## 📦 Shelf — Post-Hire Electives

> These aren't "later in the sequence" — they're off the sequence entirely until I have a job. No number means no claim on my time right now.

| # | Module | Focus Area |
| :-: | -------- | ------------ |
| S01 | [[Cyber-Security/Roadmap/Shelf_Post-Hire#Shelf 01: Wireless Network Security\|Wireless Network Security]] | WPA2/WPA3, Evil Twin, PMKID |
| S02 | [[Cyber-Security/Roadmap/Shelf_Post-Hire#Shelf 02: Mobile Platform Pentesting\|Mobile Security]] | Android/iOS, Frida, MobSF, Pinning |
| S03 | [[Cyber-Security/Roadmap/Shelf_Post-Hire#Shelf 03: OT/ICS/SCADA Security\|OT / ICS / SCADA Security]] | Modbus, S7comm, Purdue model |
| S04 | [[Cyber-Security/Roadmap/Shelf_Post-Hire#Shelf 04: Digital Forensics\|Digital Forensics]] | Memory, Disk, Autopsy, Volatility |
| S05 | [[Cyber-Security/Roadmap/Shelf_Post-Hire#Shelf 05: Reverse Engineering & Malware Analysis\|Reverse Engineering & Malware Analysis]] | Ghidra, x64dbg, unpacking |
| S06 | [[Cyber-Security/Roadmap/Shelf_Post-Hire#Shelf 06: Modern Exploitation\|Modern Exploitation]] | Binary exploitation, ROP, ASLR/DEP |
| S07 | [[Cyber-Security/Roadmap/Shelf_Post-Hire#Shelf 07: Hardware Hacking & Embedded Systems\|Hardware Hacking & Embedded Systems]] | UART, JTAG, Firmware extraction |
| S08 | [[Cyber-Security/Roadmap/Shelf_Post-Hire#Shelf 08: Physical Penetration Testing\|Physical Penetration Testing]] | Lock picking, RFID cloning, bypass |
| S09 | [[Cyber-Security/Roadmap/Shelf_Post-Hire#Shelf 09: VoIP & Telecommunications Security\|VoIP & Telecommunications Security]] | SIP, RTP, SS7/5G concepts |
| S10 | [[Cyber-Security/Roadmap/Shelf_Post-Hire#Shelf 10: Blockchain & Web3 Security\|Blockchain & Web3 Security]] | Smart contract audits, reentrancy |
| S11 | [[Cyber-Security/Roadmap/Shelf_Post-Hire#Shelf 11: Governance, Risk & Compliance (GRC)\|Governance, Risk & Compliance]] | ISO 27001, SOC 2, NIST CSF |
| S12 | [[Cyber-Security/Roadmap/Shelf_Post-Hire#Shelf 12: Supply Chain Security\|Supply Chain Security]] | SBOM, Dependency confusion, SLSA |
| S13 | [[Cyber-Security/Roadmap/Shelf_Post-Hire#Shelf 13: DevSecOps & Secure SDLC\|DevSecOps & Secure SDLC]] | CI/CD pipelines, SAST/DAST, Semgrep |
| S14 | [[Cyber-Security/Roadmap/Shelf_Post-Hire#Shelf 14: Secure Code Review Methodology\|Secure Code Review Methodology]] | Code auditing, source-level vuln analysis |
| S15 | [[Cyber-Security/Roadmap/Shelf_Post-Hire#Shelf 15: Security Architecture & Engineering\|Security Architecture & Engineering]] | Zero Trust, threat modeling, STRIDE |
| S16 | [[Cyber-Security/Roadmap/Shelf_Post-Hire#Shelf 16: Security Operations Expansion\|Security Operations Expansion]] | SOAR, DLP, Insider threat |
| S17 | [[Cyber-Security/Roadmap/Shelf_Post-Hire#Shelf 17: Denial of Service & Availability Resilience\|Denial of Service & Resilience]] | Layer 4/7 mechanisms, Anycast, DDoS mitigation |
| S18 | [[Cyber-Security/Roadmap/Shelf_Post-Hire#Shelf 18: Automotive Security\|Automotive Security]] | CAN Bus, ECU, UDS, OBD-II, AUTOSAR SecOC |
| S19 | [[Cyber-Security/Roadmap/Shelf_Post-Hire#Shelf 19: Telecom Security\|Telecom Security]] | GSM/4G/5G, SS7, Diameter, IMSI Catcher, SIM internals |
| S20 | [[Cyber-Security/Roadmap/Shelf_Post-Hire#Shelf 20: Advanced Linux Internals\|Advanced Linux Internals]] | Kernel modules, eBPF, container escape, LKM rootkits |
| S21 | [[Cyber-Security/Roadmap/Shelf_Post-Hire#Shelf 21: Advanced Windows Internals\|Advanced Windows Internals]] | Token security, PPL, memory forensics, DKOM |

---

## ⏱️ Daily Protocol

> One question every morning: **"Which 3 points am I doing today, how big is each, and what will prove I did them?"**

### 🧠 Built Around My Real Constraints

- **Real weekday budget: 3–4 hrs after college.** Plan with 3, treat the 4th hour as a bonus.
- **Known failure: focus and energy drop midway.** The loop is ordered by brain cost: new and hard work first, guided and passive work last.
- **No continuous screen block over 50 min.** Then a real break.
- **Daily target (Full Session): 3 points done, or the scheduled points if they're bigger.** One finished L point counts the same as 3 S points. Short Session target: 1 point. Recovery: none.

### 🔒 Session Types

Pick the type honestly *before* starting. The order never changes, only the size of each block.

| Session Type | Duration | Use When | Scope |
| :--- | :---: | --- | --- |
| **Full Session** | 3–4 hrs | Normal weekday, normal energy | Every block below |
| **Short Session** | 60–90 min | Deadline within 48 h, or a heavy college day | Block 0 + 1 point (with writeup) + THM capped at 30 min |
| **Recovery Session** | 20–30 min | Sick, travel, burned out | Reread yesterday's notes. No new material. |

A Short or Recovery day still counts. A skipped day doesn't. Tag the git commit `[short]` / `[recovery]`. The 3-point target applies to **Full Sessions only**, otherwise it would be broken by day 3 and the whole protocol would lose credibility.

### 🔁 The Daily Loop

Run it in this order. Nothing gets reordered mid-day.

**Block 0 — Lock the Points** *(5 min)*
Pick points from the current module's Stage file (a point = one Topic or sub-topic). Give each a **size** and a **done-line** before opening a tab.

| Size | Time (writeup included) | What it looks like | Example |
| :-: | :-: | --- | --- |
| **S** | 30 min | One concept, one short lab | Fetch-Decode-Execute, watched in gdb |
| **M** | 60 min | A tool or technique lab | Nmap scan types against a target |
| **L** | 90 min | A full lab that needs a THM room | The Nmap room, end to end |

The point pool is ~90 min, so a day is **3 × S, or 1 M + 1 S, or 1 L**. One L per day, and it is the whole pool. When the schedule hands you an M or L, that point *is* the day's target. Don't add filler to reach 3.

A **done-line** is a checkable sentence: *"I can predict what RIP, RSP and RAX do on push/call/ret and show it in gdb."* Never "master registers". If you can't write the done-line, the point is too vague: split or reword it.

Size is locked at Block 0. A point that blows its box is **not done**. Carry it to tomorrow, don't extend it.

**Block 1 — Points** *(3 × 30 min, 5-min break between points)*
Hardest thinking of the day, so it gets your freshest hour and a half. Each point has the same shape:
1. **Lab first (~22 min).** Terminal open. Before running anything, write one line: *what do I expect to see at the packet/system level?* Run it, compare. If I can't explain a flag, stop.
2. **Books only if stuck.** Trigger: I can't explain what a command did, or the lab failed for a conceptual reason. Only the section for *this* point, **max 10 min**, then back to the lab.
3. **Writeup (~8 min), immediately after the lab, in the running note.** Keep the entry to four lines:
   - What I did (commands/steps)
   - What I expected vs. what happened
   - The one thing that surprised me or broke
   - **The done-line, answered from memory with notes closed.** If I can't, the point is carried, not done.
4. **`git commit`** (30 seconds).

**Break** *(10 min, off-screen)*
Water, food, walk. Not my phone. This protects the second half of the session.

**Block 2 — TryHackMe** *(1 room a day, hard cap 60 min, 30 on Short)*
Guided = lowest cognitive cost, so it takes the tired part of the session. Pick the room the night before, tied to the current module where possible. When the cap hits, stop even mid-room and let the rest roll into tomorrow's room. **If today's room was already a point's lab (an L day), it counts as today's THM. Skip this block.**

**Block 3 — OverTheWire** *(only if time is left, 30–45 min: 1 Bandit + 1 Natas)*
Unguided practice, where skill actually gets built. Do it **before lectures** if the lectures are passive (watching/reading), because this is the hardest thinking of the late session. If time is short, one Bandit level is the floor.
- **No hints until 60 minutes total on a level.** The clock is cumulative across days (log minutes spent). Then write up what I learned either way.
- **Zero new platforms** until something is finished on the ones already in use.

**Block 4 — Lectures** *(whatever time remains)*
Passive, lowest effort, last slot. If a college deadline is within 48 hours, today is a Short Session and the freed time goes to coursework.

**Log** *(1 min)*: points done out of 3, energy rating, tomorrow's carry-over.

### ⏳ Example Budgets

| Block                                |         Full          |    Short     |
| :----------------------------------- | :-------------------: | :----------: |
| 0 · Lock points                      |           5           |      5       |
| 1 · Points (3 × 30, breaks included) |          100          | 30 (1 point) |
| Break (off-screen)                   |          10           |      0       |
| 2 · TryHackMe                        |          ≤60          |     ≤30      |
| 3 · OverTheWire                      |    30–45 (if time)    |      0       |
| **Subtotal**                         | **~2h 55m to 3h 40m** | **~65 min**  |
| 4 · Lectures                         | remainder of the day  |  remainder   |

### ⚡ Energy Rules

1. **Hardest and newest work happens in the first 100 minutes.** Never start a new concept after the break.
2. **50 minutes on-screen max, then a real break.**
3. **Stuck 20 min with zero progress?** Write down exactly what's blocking me, use the book cap, or park the point. Don't grind.
4. **Energy 2/5 or lower for two blocks in a row?** Downgrade to a Short Session for the rest of the day. Downgrade, never skip. Writeups always happen.
5. **Rate energy 1–5 after every block.** After two weeks, move blocks based on the data.

### Hard Rules

1. **Lab before books, always.**
2. **Never run a tool blindly.** If I can't explain what a flag does at the packet level, stop and read (inside the book cap), then run.
3. **No writeup = the point isn't done.**
4. **A point only counts when its done-line passes.** Skimmed or unfinished means carried.
5. **Respect the Stage Gates.** No advancing until I can demonstrate the skill without notes.
6. **Git commit after every point.** No commit in 2 weeks means I'm drifting.
7. **Sizes are set in Block 0 and are hard stops.** A point never grows mid-session.

### 📅 Weekly Rhythm

| Day | Focus |
| :--- | --- |
| **Mon–Fri** | Current module, full Daily Loop, Session Type per the rules above |
| **Sat** | Programming Track + coursework + longer unguided block |
| **Sun** | Programming Track + **Weekly Review**: reread the week's notes and energy ratings, tally points done vs. carried (carrying more than ~30% means my sizes are wrong), then re-derive one concept from memory with zero notes open |
| **Last day of month** | **Buffer Day**: no new material. Close every open writeup, confirm no 2-week git gap, redo one Stage Gate check cold. Also play one live CTF from CTFtime. |

### 📋 Daily Log Template

```
### [Date] — Module ## · [Session Type]
- Point 1 [S/M/L]: ___
  Done-line: I can ___ / I produced ___
  [ ] done / carried      Energy (1–5): __
- Point 2 [S/M/L]: ___
  Done-line: I can ___ / I produced ___
  [ ] done / carried      Energy (1–5): __
- Point 3 [S]: ___
  Done-line: I can ___ / I produced ___
  [ ] done / carried      Energy (1–5): __
- Points done today: __ / __  (target: 3, or the scheduled points)
- [ ] THM room: ___ (stopped at cap?)
- [ ] OverTheWire: ___ (level, minutes spent __ / 60 before hints)
- Lectures: ___
- Carry to tomorrow: ___
```

### Programming Track *(Weekends Only)*

| Stage | Language | Focus |
| :-----: | ---------- | ------- |
| Foundation | Python, Bash, PowerShell | Scripting fundamentals, OS automation |
| Offense I | Python, Bash | Tool wrappers, log parsing, scan automation |
| Web & App Sec | Python, JavaScript | Web exploit PoCs, XSS weaponization |
| Enterprise | PowerShell, Python (Scapy) | AD enumeration, Impacket, packet fabrication |
| Specialized | C/C++, Assembly, PowerShell, Python | Shellcode, loaders, AMSI bypass, LLM harnesses |

---

## 🛠️ Lab Setup

| Component | Minimum | Recommended |
| ----------- | --------- | ------------- |
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

### 🎯 Practice Platforms — Tiered List

#### Beginner

| Platform | Notes |
| ---------- | ------- |
| [TryHackMe](https://tryhackme.com) ✓ | Daily anchor — guided rooms, good for concept introduction |
| [OverTheWire: Bandit → Natas](https://overthewire.org/wargames/) ✓ | Linux fundamentals and web basics via wargames |
| [picoCTF / picoGym](https://picoctf.org) ✓ | Small, accessible CTF challenges across categories |
| [Hacker101 CTF](https://ctf.hacker101.com) ✓ | Good first web-hacking flags, HackerOne-linked |
| [CTFlearn](https://ctflearn.com) | Small easy challenges across categories — low friction entry |

#### Intermediate

| Platform | Notes |
| ---------- | ------- |
| [HTB Starting Point → easy/medium retired boxes](https://hackthebox.com) ✓ | Unguided boxes, closer to real work |
| [PortSwigger Web Security Academy](https://portswigger.net/web-security) ✓ | Best web training that exists — free, lab-driven, no hand-holding |
| [Root-Me](https://root-me.org) ✓ | Broad category coverage, good for gaps |
| [CryptoHack](https://cryptohack.org) ✓ | Crypto fundamentals via practical challenges |
| [pwn.college](https://pwn.college) ✓ | Binary exploitation — structured belt progression |
| [PentesterLab](https://pentesterlab.com) ✓ | Web + code review focus |
| [Proving Grounds Play (OffSec)](https://www.offsec.com/labs/) | OSCP-style boxes, a few free per day |
| [HackMyVM / Vulnyx](https://hackmyvm.eu) | VulnHub-style downloadable VMs, newer stock |
| [CyberDefenders](https://cyberdefenders.org) ✓ | Blue team and forensics labs |

#### Advanced

| Platform | Notes |
| ---------- | ------- |
| [HTB hard/insane boxes + Pro Labs](https://hackthebox.com) ✓ | Pro Labs for full AD attack chains |
| [ROP Emporium](https://ropemporium.com) / [Exploit Education](https://exploit.education) / [pwnable.kr](https://pwnable.kr) ✓ | Binary exploitation depth |
| [pwnable.tw](https://pwnable.tw) | Hard pwn — no hints, no scaffolding |
| [Crackmes.one](https://crackmes.one) | Reverse engineering challenges |
| [Live CTFs via CTFtime](https://ctftime.org) ✓ | The real test — no hints, real competition |
| [Google CTF and Hackropole archives](https://goo.gle/ctf) | Past hard CTF challenges with writeups |

---

