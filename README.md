<p align="center">
  <h1 align="center">🛡️ Cyber-Security Lab & Learning Portfolio</h1>
  <p align="center">
    <strong>An end-to-end, highly structured offensive & defensive security engineering system</strong><br>
    5 Execution Stages · 30 Core Modules · 17 Post-Hire Specializations · 88 Tool Checklists · 4,800+ Practical Tasks
  </p>
  <p align="center">
    <img src="https://img.shields.io/badge/Files-150%2B-blue" alt="Files">
    <img src="https://img.shields.io/badge/Tasks-4%2C800%2B-green" alt="Tasks">
    <img src="https://img.shields.io/badge/Tools-88-orange" alt="Tools">
    <img src="https://img.shields.io/badge/Stages-5%20%2B%20Shelf-purple" alt="Stages">
    <img src="https://img.shields.io/badge/Status-Active-brightgreen" alt="Status">
  </p>
</p>

---

**Author:** Aditya Mishra  
**Started:** October 2025  
**Core Directive:** Understand systems deeply enough to break them, analyze them, and remediate them at the packet and kernel level. Never run a tool you cannot explain.

> *"The goal is not to memorize tools — it's to understand systems deeply enough to break them and, more importantly, to fix them."*

---

## 🚀 Repository Architecture

This repository is an **active cyber-security engineering system** built around structured vulnerability research, rigorous methodology, and isolated lab environments. Every module pairs deep engineering fundamentals with hands-on lab tasks and verified command proofs.

### System Overview

| Area | Scope & Breakdown | Primary Hub |
|:-----|:------------------|:------------|
| 🗺️ **Master Roadmap** | 5 sequential execution stages covering 30 core modules + proof gates | [Roadmap/README.md](Roadmap/README.md) |
| 🛠️ **Tool Mastery Directory** | 88 comprehensive tool checklists arranged into a 4-tier operational hierarchy | [Roadmap/Tools/README.md](Roadmap/Tools/README.md) |
| 🧪 **Hands-On Labs** | Network exploitation, web security, Linux privilege escalation, and AD testing | [Lab/README.md](Lab/README.md) |
| 📦 **Post-Hire Shelf** | 17 situational specializations (ICS/SCADA, Mobile, Web3, Forensics, Hardware) | [Roadmap/Shelf_Post-Hire.md](Roadmap/Shelf_Post-Hire.md) |
| 📚 **Literature Mapping** | Exhaustive topic-by-topic cross-reference to primary security textbooks | [Roadmap/book_to_phase_map.md](Roadmap/book_to_phase_map.md) |

---

## 🧭 The 5-Stage Execution Framework

The curriculum follows a strict, dependency-driven execution order. Do not skip ahead without passing the designated **Stage Proof Gates**.

| Stage | Focus & Scope | Modules | Key Milestone / Gate |
|:-----:|:--------------|:-------:|:---------------------|
| 🔵 **[Stage 1: Foundation](Roadmap/Stage-1_Foundation.md)** | Hardware architecture, Linux/Windows internals, 7-layer networking, Cryptography, Auth & Web fundamentals | `01–07` | **Foundation Proof Gate** (10 PCAPs, admin baselines, 3 scripts, lab report) |
| 🟠 **[Stage 2: Offense I](Roadmap/Stage-2_Offense-I.md)** | OSINT, Port/Service Scanning, Service Enumeration, Database exploitation, Hash cracking, Initial compromise & PrivEsc | `08–13` | **Stage Gate 1** (Cold root on target, password hash extraction & cracking, PrivEsc) |
| 🟣 **[Stage 3: Web & App Sec](Roadmap/Stage-3_Web-and-App-Sec.md)** | OWASP Top 10, modern web attacks, session hijacking, Web server hacking, API security, Bug bounty methodology, SOC/IDS/CTI | `14–18` | **Stage Gate 2** (3+ HTB/THM writeups, full OWASP coverage, Linux+Windows privesc) |
| 🏢 **[Stage 4: Enterprise](Roadmap/Stage-4_Enterprise.md)** | Active Directory, Kerberos attacks, Cloud IAM, Kubernetes/Containers, Adversary Emulation, MITM, Social Engineering, Reporting | `19–26` | **Stage Gate 3** (End-to-end AD domain compromise, BloodHound graph analysis, 1 full report) |
| 🔬 **[Stage 5: Specialized](Roadmap/Stage-5_Specialized.md)** | Offensive C/C++ Dev, Custom C2 implants, AI/LLM Red Teaming, Red Team operations, Portfolio & CVE discovery | `27–30` | **Final Gate** (Custom C2 in lab, published AI security research, 3+ professional reports) |
| 📦 **[Post-Hire Shelf](Roadmap/Shelf_Post-Hire.md)** | Off-sequence electives (Wireless, Mobile, ICS/SCADA, Digital Forensics, Exploit Dev, GRC, Hardware Hacking) | `S01–S17` | *Unclaimed until operational on the job* |

---

## 🛠️ Tool Mastery Guides (88 Tools)

The repository features **88 structured tool guides** organized by tier in [Roadmap/Tools/README.md](Roadmap/Tools/README.md). Each guide includes core concepts, syntax, progressive lab exercises, expected outputs, common failure modes, and interview questions.

### Tier 1 — Core Engagement Essentials (10 Tools)
*Must be mastered before entering client or enterprise engagements.*

| Tool | Focus & Purpose | Guide |
|:-----|:----------------|:-----:|
| 🔌 **Netcat** | TCP/UDP swiss-army knife, port scanning, raw connections, reverse/bind shells | [Open Guide](Roadmap/Tools/Netcat.md) |
| 🦈 **Wireshark** | Deep packet inspection, protocol analysis, credential extraction, PCAP forensics | [Open Guide](Roadmap/Tools/Wireshark.md) |
| 🗺️ **Nmap** | Host discovery, port scanning, service versioning, OS detection, NSE scripts | [Open Guide](Roadmap/Tools/Nmap.md) |
| 🔥 **Hashcat** | GPU-accelerated hash cracking, wordlist mutations, rule-based attacks, masks | [Open Guide](Roadmap/Tools/Hashcat.md) |
| 🔓 **Hydra** | High-speed network logon cracking (SSH, FTP, SMB, RDP, HTTP, Form-based) | [Open Guide](Roadmap/Tools/Hydra.md) |
| 🐉 **LinPEAS** | Automated Linux privilege escalation enumeration and configuration audit | [Open Guide](Roadmap/Tools/LinPEAS.md) |
| 💀 **Metasploit** | Full-scale penetration testing framework, exploit execution, Meterpreter handlers | [Open Guide](Roadmap/Tools/Metasploit_Framework.md) |
| 🕷️ **Burp Suite** | Web application proxy, Repeater, Intruder, vulnerability scanner, custom extensions | [Open Guide](Roadmap/Tools/Burp_Suite.md) |
| 🩸 **BloodHound** | Active Directory attack path discovery, Six Degrees of Domain Admin, cypher queries | [Open Guide](Roadmap/Tools/BloodHound.md) |
| 🐍 **Impacket** | Python AD offensive tooling (`secretsdump`, `GetUserSPNs`, `wmiexec`, `ntlmrelayx`) | [Open Guide](Roadmap/Tools/Impacket.md) |

> **Explore all 88 tools:** See [Roadmap/Tools/README.md](Roadmap/Tools/README.md) for **Tier 2 (Frequent — 22 tools)**, **Tier 3 (Situational — 27 tools)**, and **Tier 4 (Niche / Reference — 29 tools)**.

---

## 🧪 Hands-On Lab Environments

Theory without execution is dead weight. All knowledge is validated against isolated virtual machine environments and targets.

| Environment | Focus Area | Entry Point |
|:------------|:-----------|:-----------:|
| 🐧 **Metasploitable 2** | Service enumeration, network-level exploitation, Linux post-exploitation | [109-Task Lab Guide](Lab/Metasploitable_2/TASK_LIST.md) |
| 🌐 **OWASP Broken WebApps** | OWASP Top 10 hands-on practice, Burp Suite testing, web vulnerability analysis | [Web Security Lab](Lab/OWASP_Broken_WebApps/TASK_LIST.md) |
| 🏰 **OverTheWire Bandit** | Command line fluency, SSH configuration, Linux permissions, pipeline mastery | [Bandit 0–33 Writeups](Lab/OverTheWire/Bandit/README.md) |
| 🎯 **TryHackMe / Enterprise** | Network architectures, Windows incident investigation, target challenge rooms | [THM Notes & Scenarios](Lab/THM/) |
| 📖 **Lab Methodology Guide** | Standardized lab workflow, capture requirements, and documentation rules | [Lab Guide](Lab/LAB_GUIDE.md) |

---

## 📂 Repository Directory Layout

```
Cyber-Security/
├── Lab/                                      # Isolated practice environments & challenge writeups
│   ├── LAB_GUIDE.md                          # Standardized lab execution & writeup methodology
│   ├── Metasploitable_2/                     # Network exploitation lab (109 verified tasks)
│   ├── OWASP_Broken_WebApps/                 # Web application vulnerability curriculum
│   ├── OverTheWire/Bandit/                   # Linux CLI wargame (Levels 0–33 complete)
│   └── THM/                                  # TryHackMe machines & Windows incident rooms
│
├── Roadmap/                                  # Master Roadmap & Curriculum Engine
│   ├── README.md                             # Execution order, stage timelines & topic mapping
│   ├── Stage-1_Foundation.md                 # Modules 01–07: Architecture, OS, Network, Crypto
│   ├── Stage-2_Offense-I.md                  # Modules 08–13: Recon, Scanning, Enum, Exploitation
│   ├── Stage-3_Web-and-App-Sec.md            # Modules 14–18: Web/API Security & Defensive Tracks
│   ├── Stage-4_Enterprise.md                 # Modules 19–26: Active Directory, Cloud, Containers
│   ├── Stage-5_Specialized.md                # Modules 27–30: Exploit Dev, AI Red Team, Tradecraft
│   ├── Shelf_Post-Hire.md                    # Modules S01–S17: Post-hire specialization library
│   ├── book_to_phase_map.md                  # Comprehensive textbook-to-stage study crosswalk
│   ├── Prompt_to_Learn.md                    # Self-prompting and active recall framework
│   └── Tools/                                # 88 Tool Mastery Guides (Tiers 1–4)
│       ├── README.md                         # Tool directory index & tier matrix
│       ├── Nmap.md, Wireshark.md, ...        # Tier 1: Core tools
│       ├── Amass.md, Gobuster.md, ...        # Tier 2: Frequent tools
│       ├── Pacu.md, Sysmon.md, ...           # Tier 3: Situational tools
│       └── APKTool.md, Aircrack-ng.md, ...   # Tier 4: Niche & reference tools
│
└── README.md                                 # ← Main portfolio hub
```

---

## ⏱️ Daily Engineering Protocol

Every single study and lab session adheres to a strict 3-step loop:

1. **Mechanism Before Tool:** Never launch a tool without understanding the RFC, protocol, or operating system mechanic it targets. Write technical notes first.
2. **Terminal Execution:** Wireshark running, tcpdump capturing, commands executed methodically with flags understood at the byte level.
3. **Proof Artifact:** Save the PCAP, log, or exploit output. Commit the lab writeup to Git. If it isn't documented with proof, the skill was not learned.

---

> ⚠️ **Disclaimer:** All tooling, methodologies, and technical documentation in this repository are maintained exclusively for **authorized educational research, defensive hardening, and authorized penetration testing** within isolated, owned lab environments. Unauthorized testing against systems without explicit, written permission is illegal.
