<p align="center">
  <h1 align="center">🛡️ Cyber-Security Lab & Learning Portfolio</h1>
  <p align="center">
    <strong>A structured, hands-on cybersecurity training repository</strong><br>
    From absolute beginner to penetration testing practitioner
  </p>
  <p align="center">
    <img src="https://img.shields.io/badge/Files-83-blue" alt="Files">
    <img src="https://img.shields.io/badge/Tasks-509-green" alt="Tasks">
    <img src="https://img.shields.io/badge/Tools-10-orange" alt="Tools">
    <img src="https://img.shields.io/badge/Labs-3-red" alt="Labs">
    <img src="https://img.shields.io/badge/Status-Active-brightgreen" alt="Status">
  </p>


---

**Author:** Aditya Mishra
**Started:** October 2025
**Philosophy:** Learn by doing. Document everything. Master the methodology, not just the commands.

> *"The goal is not to memorize tools — it's to understand systems deeply enough to break them and, more importantly, to fix them."*

---

## 🚀 What Is This Repository?

This is a **complete offensive security training system** built around real vulnerable lab environments. It's not a collection of notes — it's a structured curriculum with **509 hands-on tasks** organized into progressive phases, covering everything from your first `nmap` scan to Active Directory domain compromise.

### What's Inside

| Category | Content | Scale |
|:---------|:--------|:------|
| 🛠️ **Tool Mastery Guides** | 10 tools, each with 8 progressive phases | ~400 tasks |
| 🧪 **Lab Curricula** | Metasploitable 2 + OWASP BWA structured task lists | ~110 tasks |
| 📋 **10-Phase Roadmap** | Beginner → Advanced learning path | 10 phases |
| 📚 **Knowledge Base** | Linux, Networking, Reconnaissance, Scanning, Exploitation | 6 areas |
| 🏰 **CTF Writeups** | OverTheWire Bandit Levels 0–33 | 36 writeups |

---

## 🧭 Quick Navigation

### 📋 Roadmap
| | |
|:---|:---|
| 📋 [**Master Roadmap**](Roadmap/README.md) | 10-phase learning path from fundamentals to advanced pentesting |

### 🧪 Lab Environments
| Lab | Focus | Guide |
|:----|:------|:------|
| 🐧 **Metasploitable 2** | Network exploitation, service attacks, post-exploitation | [Task List](Lab/Metasploitable_2/TASK_LIST.md) |
| 🌐 **OWASP Broken WebApps** | OWASP Top 10, web app security, Burp Suite methodology | [Task List](Lab/OWASP_Broken_WebApps/TASK_LIST.md) |
| 🏰 **OverTheWire Bandit** | Linux CLI, SSH, file permissions, scripting | [Levels 0–33](Lab/OverTheWire/Bandit/README.md) |

### 🛠️ Tool Mastery Guides

Every guide follows the same 8-phase structure: **Fundamentals → Core Features → Intermediate → Advanced → Integration → Labs → Methodology → Mastery Challenges**. Each task includes objectives, skills learned, practical exercises, expected output, and common mistakes.

| | Tool | Category | Tasks | Guide |
|:---:|:-----|:---------|:-----:|:------|
| 🗺️ | **Nmap** | Scanning & Discovery | 47 | [Open](Tools/Nmap.md) |
| 🔌 | **Netcat** | Networking Swiss Army Knife | 38 | [Open](Tools/Netcat.md) |
| 🦈 | **Wireshark** | Traffic Analysis & Forensics | 43 | [Open](Tools/Wireshark.md) |
| 🕷️ | **Burp Suite** | Web Application Testing | 43 | [Open](Tools/Burp_Suite.md) |
| 💀 | **Metasploit** | Exploitation Framework | 44 | [Open](Tools/Metasploit_Framework.md) |
| 🔓 | **Hydra** | Online Brute-Forcing | 37 | [Open](Tools/Hydra.md) |
| 🔥 | **Hashcat** | Offline Password Cracking | 38 | [Open](Tools/Hashcat.md) |
| 🐉 | **LinPEAS** | Linux Privilege Escalation | 39 | [Open](Tools/LinPEAS.md) |
| 🐍 | **Impacket** | Windows/AD Exploitation | 38 | [Open](Tools/Impacket.md) |
| 🩸 | **BloodHound** | AD Attack Path Analysis | 40 | [Open](Tools/BloodHound.md) |

### 📚 Knowledge Base
| Area | Content |
|:-----|:--------|
| 🐧 Linux | [Linux Basics](01.Linux/linux-basics.md) · [Bash Scripting](01.Linux/Bash.md) · [Deep Knowledge](01.Linux/Linux_Knowledge.md) |
| 🌐 Networking | [Networking Fundamentals](02.Networking/README.md) · [Extra Notes](02.Networking/EXTRA.md) |
| 🔍 Reconnaissance | [Footprinting & OSINT](03.Learnings/01.Footprinting-and-Reconnaissance/) |
| 📡 Scanning | [Network Scanning](03.Learnings/02.Scanning/) |
| 📋 Enumeration | [Service Enumeration](03.Learnings/03.Enumeration/) |
| 💣 Exploitation | [System Hacking](04.Exploits/01.System-Hacking/) |

---

## 🎯 Learning Path Overview

The recommended order for working through this repository:

```
Phase 1: Linux Fundamentals
    └── OverTheWire Bandit (Levels 0-33)
    └── 01.Linux/ notes

Phase 2: Networking
    └── 02.Networking/ notes
    └── Nmap tool guide
    └── Netcat tool guide
    └── Wireshark tool guide

Phase 3: Reconnaissance & Scanning
    └── 03.Learnings/ (Footprinting, Scanning, Enumeration)
    └── Metasploitable 2 Lab (Levels 0-3)

Phase 4: Web Application Security
    └── Burp Suite tool guide
    └── OWASP BWA Lab (all levels)

Phase 5: Exploitation
    └── Metasploit tool guide
    └── Hydra tool guide
    └── Metasploitable 2 Lab (Levels 4-8)

Phase 6: Post-Exploitation
    └── LinPEAS tool guide
    └── Hashcat tool guide
    └── Metasploitable 2 Lab (Levels 9-13)

Phase 7: Active Directory
    └── Impacket tool guide
    └── BloodHound tool guide
```

---

## 📌 Skills Covered

| Domain | Skills |
|:-------|:-------|
| **Linux** | CLI navigation, file permissions, process management, Bash scripting, SSH, cron, systemd |
| **Networking** | TCP/IP, OSI model, DNS, HTTP, ARP, routing, subnetting, packet analysis |
| **Reconnaissance** | OSINT, footprinting, DNS enumeration, WHOIS, Google dorking, Shodan |
| **Scanning** | Port scanning, service detection, OS fingerprinting, vulnerability scanning |
| **Web Security** | OWASP Top 10 (SQLi, XSS, CSRF, IDOR, SSRF, XXE), authentication bypass, session management |
| **Exploitation** | Metasploit, manual exploitation, payload generation, reverse/bind shells |
| **Post-Exploitation** | Privilege escalation, credential harvesting, lateral movement, persistence, pivoting |
| **Active Directory** | Kerberoasting, AS-REP Roasting, DCSync, pass-the-hash, NTLM relay, BloodHound analysis |
| **Password Attacks** | Online brute-forcing (Hydra), offline cracking (Hashcat), wordlist generation, rule creation |
| **Traffic Analysis** | Packet capture, protocol analysis, credential extraction, TLS inspection, forensics |

---

## 📂 Repository Structure

```
Cyber-Security/
│
├── 01.Linux/                         # Linux fundamentals & Bash scripting
├── 02.Networking/                    # TCP/IP, protocols, networking deep-dives
├── 03.Learnings/                     # CEH-style modules
│   ├── 01.Footprinting-and-Recon/    #   OSINT & information gathering
│   ├── 02.Scanning/                  #   Network & vulnerability scanning
│   └── 03.Enumeration/              #   Service & protocol enumeration
├── 04.Exploits/                      # System hacking & exploitation notes
│   └── 01.System-Hacking/
│
├── Lab/                              # Hands-on lab environments
│   ├── Metasploitable_2/             #   🐧 Network exploitation (109 tasks)
│   ├── OWASP_Broken_WebApps/         #   🌐 Web security (structured curriculum)
│   └── OverTheWire/Bandit/           #   🏰 Linux CLI wargame (36 levels)
│
├── Roadmap/                          # 📋 10-phase master learning roadmap
│   ├── README.md                     #   Roadmap overview
│   └── Phase-1.md ... Phase-10.md    #   Individual phase details
│
├── Tools/                            # 🛠️ 10 tool mastery guides (407 tasks)
│   ├── Nmap.md                       #   Port scanning & discovery
│   ├── Netcat.md                     #   Network utility & shells
│   ├── Wireshark.md                  #   Packet analysis & forensics
│   ├── Burp_Suite.md                 #   Web application testing
│   ├── Metasploit_Framework.md       #   Exploitation framework
│   ├── Hydra.md                      #   Online password attacks
│   ├── Hashcat.md                    #   Offline password cracking
│   ├── LinPEAS.md                    #   Linux privilege escalation
│   ├── Impacket.md                   #   Windows/AD exploitation
│   └── BloodHound.md                 #   AD attack path analysis
│
└── README.md                         # ← You are here
```

---

## 📅 Learning Approach

**Methodology:**
1. 📖 **Study** — Learn concepts through structured materials
2. 🧪 **Practice** — Apply in isolated lab environments (Metasploitable 2, OWASP BWA)
3. 📝 **Document** — Write up every technique, command, and lesson learned
4. 🔁 **Iterate** — Revisit topics with deeper understanding after hands-on experience
5. 🎯 **Master** — Complete mastery challenges and competency self-assessments

**Weekly Schedule:**
- **Mon/Wed (3 hrs):** Labs + Course modules  
- **Tue/Thu/Fri/Sat (5 hrs):** Labs + Course + Book reading + Tool practice  
- **Sun:** Portfolio updates, review, and coding practice  

---

## 📖 Resources

**Course:** [Bitten Tech Solutions](https://www.bittentechsolutions.com/) — Linux, Networking, Ethical Hacking (CEH)  
**Books:** Cybersecurity fundamentals, Networking essentials, Linux administration  
**Platforms:** [OverTheWire](https://overthewire.org/) · [TryHackMe](https://tryhackme.com/) · [HackTheBox](https://hackthebox.com/) · [DVWA](https://github.com/digininja/DVWA) · [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/)  
**References:** [GTFOBins](https://gtfobins.github.io/) · [HackTricks](https://book.hacktricks.xyz/) · [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) · [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)

---

> ⚠️ **Disclaimer:** All tools, techniques, and exercises in this repository are for **authorized educational use only** in isolated lab environments. Never use these skills against systems you do not own or have explicit written permission to test. Unauthorized access to computer systems is illegal.

---

<p align="center">
  <em>Built with curiosity, persistence, and a lot of broken VMs.</em>
</p>
