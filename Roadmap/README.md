# 🛡️ Cybersecurity Master Roadmap

> **Career Target:** Penetration Testing → Red Team Operations → Advanced Offensive Security → AI Red Teaming
>
> **Core Rule:** Phase numbers are organizational labels. Your actual execution order is defined in [Stage Execution Order](#-stage-execution-order) below.

---

## 📑 Table of Contents

| # | Section |
|:-:|---------|
| 1 | [Phase Overview](#-phase-overview) |
| 2 | [Stage Execution Order](#-stage-execution-order) ← **Start here** |
| 3 | [Daily Protocol](#️-daily-protocol) |
| 4 | [Lab Setup](#️-lab-setup) |
| 5 | [Completion Tracker](#-completion-tracker) |

---

## 📊 Phase Overview

| Phase | File | Focus | Time (FT) | Track |
|:-----:|------|-------|:---------:|:-----:|
| 1 | [Phase-1.md](Phase-1.md) | Foundation — OS, Linux/Windows, Networking, Crypto, Web | 4–6 mo | ✅ Critical |
| 2 | [Phase-2.md](Phase-2.md) | Offensive Core — Recon, Scanning, Enumeration, Hacking | 4–5 mo | ✅ Critical |
| 3 | [Phase-3.md](Phase-3.md) | Defense Core — SIEM, Detection, MITRE ATT&CK | Parallel | ✅ Parallel |
| 4 | [Phase-4.md](Phase-4.md) | Web & App Security — OWASP, API, Bug Bounty | 3–4 mo | ✅ Critical |
| 5 | [Phase-5.md](Phase-5.md) | Wireless & Mobile — WiFi, BLE, Android/iOS | 3–5 mo | 🟡 Post-Hire |
| 6 | [Phase-6.md](Phase-6.md) | Infrastructure — Active Directory, Cloud, Kubernetes | 5–7 mo | ✅ Critical |
| 7 | [Phase-7.md](Phase-7.md) | Advanced Security — Offensive Dev, DFIR, Exploit Dev | 2–3 mo* | ✅ Critical* |
| 8 | [Phase-8.md](Phase-8.md) | GRC & DevSecOps — Frameworks, Supply Chain, Architecture | 4–6 mo | 🟡 Post-Hire |
| 9 | [Phase-9.md](Phase-9.md) | AI Security — LLM Red Teaming, Prompt Injection, RAG | 3–5 mo | ✅ Critical |
| 10 | [Phase-10.md](Phase-10.md) | Operations & Career — Red Team Ops, Portfolio, Reports | 2–3 mo | ✅ Critical |

> \* Phase 7: Only **Part 42 (Offensive Development)** is on the critical path. Parts 27/28/29 are post-hire specializations.

> **Critical Path Total:** ~23–33 months full-time to junior/mid penetration tester level.

---

## 🗺️ Stage Execution Order

> [!IMPORTANT]
> Follow this order, not the phase numbers. Prerequisites are encoded here.

```
════════════════════════════════════════════════════════════════
  📍 CURRENT POSITION
════════════════════════════════════════════════════════════════

  Phase 1 — Foundation
  ████████████████████░  ~80–90% complete
  Status: SUBSTANTIALLY COMPLETE
  Action: Patch gaps just-in-time. Do NOT restart.

════════════════════════════════════════════════════════════════
  STAGE 1 — Core Technical Compact             [Months 1–8]
  Milestone: Junior Pentester / OSCP-ready / Bug Bounty capable
════════════════════════════════════════════════════════════════

  Phase 2A — Offensive Fundamentals        ◄── START HERE NOW
  ──────────────────────────────────────────────────────────────
  Part 4  → Footprinting & Reconnaissance
  Part 5  → Scanning
  Part 6  → Enumeration
  Part 6B → Database Security
  Part 31 → Password Cracking & Hash Analysis  (before Part 7)
  Part 7  → System Hacking & Initial Compromise

  Phase 4 — Web & Application Security     ◄── BEFORE Phase 2B
  ──────────────────────────────────────────────────────────────
  Part 17 → Web Application Hacking
  Part 12 → Session Hijacking & Token Attacks
  Part 18 → Web Server Hacking
  Part 19 → API Security
  Part 20 → Bug Bounty Methodology

  EXIT GATE:
  ✓ Root an HTB/THM machine + write a professional report
  ✓ Find OWASP Top 10 vulns in a web app without Metasploit
  ✓ Crack hashes, dump creds, escalate on Linux & Windows
  ✓ 3+ lab writeups committed to Git

════════════════════════════════════════════════════════════════
  STAGE 2 — Enterprise Red Teaming           [Months 9–16]
  Milestone: Enterprise Pentester / Mid-level Red Teamer
════════════════════════════════════════════════════════════════

  Phase 6 — Infrastructure & Identity
  ──────────────────────────────────────────────────────────────
  Part 23 → Active Directory & Entra ID
  Part 24 → Cloud Computing  (AWS / Azure / GCP)
  Part 25 → Container & Kubernetes Security
  Part 16 → Adversary Emulation & Purple Teaming  (capstone)

  Phase 2B — Advanced Offensive Operations
  ──────────────────────────────────────────────────────────────
  Part 9  → Sniffing & Spoofing
  Part 10 → Social Engineering
  Part 8  → Malware & Weaponization  (concepts; full dev in Part 42)
  Part 11 → Denial of Service  (conceptual awareness only)

  Part 39 → Pentest Report Writing  (pulled forward from Phase 10)
  ──────────────────────────────────────────────────────────────
  Every rooted machine = one professional-grade report

  EXIT GATE:
  ✓ Attack an AD domain end-to-end (Kerberoast, ADCS, PTH)
  ✓ Enumerate and exploit AWS/Azure IAM misconfigurations
  ✓ Write a client-facing pentest report with executive summary
  ✓ BloodHound attack path exports committed to Git

════════════════════════════════════════════════════════════════
  STAGE 3 — Specialized Trade               [Months 17–24]
  Milestone: Senior Red Teamer / AI Security Specialist
════════════════════════════════════════════════════════════════

  Phase 7 — Part 42 ONLY
  ──────────────────────────────────────────────────────────────
  Part 42 → Offensive Development & Tooling  (C2, AMSI/ETW bypass)

  Phase 9 — AI Security  (unlocked after Phase 6)
  ──────────────────────────────────────────────────────────────
  Part 38 → AI & LLM Red Teaming

  Phase 10 — Operations & Career
  ──────────────────────────────────────────────────────────────
  Part 40 → Red Team Operations & Tradecraft  (do first)
  Part 41 → Proof of Work & Career Portfolio

  EXIT GATE:
  ✓ Custom C2 implant deployed in lab with evasion
  ✓ Published prompt injection / RAG attack research or tool
  ✓ Portfolio with 3+ professional reports and 5+ writeups
  ✓ OSCP or equivalent certification completed

════════════════════════════════════════════════════════════════
  POST-HIRE — Do NOT block on these pre-employment
════════════════════════════════════════════════════════════════
  Phase 5  → Wireless & Mobile        (if role requires it)
  Phase 8  → GRC & DevSecOps          (if role requires it)
  Phase 7  → Parts 27/28/29           (DFIR, Malware RE, Kernel)
  Phase 6  → Part 26  OT/ICS/SCADA   (industrial roles only)
```

---

## ⏱️ Daily Protocol

> One question answered every morning: **"What is my current Part and what am I proving today?"**

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
4. **Respect the Move-On Gates.** Do not proceed to the next stage until you can demonstrate the skill without notes.
5. **Git commit after every session.** If you haven't committed in 2 weeks, you're drifting.

### Programming Track *(Weekends Only)*

| Phase | Language | Focus |
|:-----:|----------|-------|
| 1 | Python, Bash, PowerShell | Scripting fundamentals, OS automation |
| 2A | Python, Bash | Tool wrappers, log parsing, scan automation |
| 2B | Python (Scapy), Bash | Packet fabrication, network scripting |
| 4 | Python, JavaScript | Web exploit PoCs, XSS weaponization |
| 6 | PowerShell, Python | AD enumeration, cloud IAM, Impacket |
| 7 | C/C++, Assembly, PowerShell | Shellcode, loaders, AMSI bypass |
| 9 | Python | LLM harnesses, prompt injection automation |

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
- Windows Server VM (AD target — Phase 6)
- Ubuntu/Metasploitable VM (Linux target)
- [TryHackMe](https://tryhackme.com) · [Hack The Box](https://hackthebox.com) · [PortSwigger Web Academy](https://portswigger.net/web-security)

---

## ✅ Completion Tracker

> Check boxes in the **phase files** (where Move-On Gates live), not only here.

---

### 🏗️ Phase 1 — Foundation *(~80–90% complete — patch just-in-time)*

- [ ] [Part 1: Fundamentals](Phase-1.md#part-1-fundamentals) — Hardware, OS, Memory
- [ ] [Part 1B: Linux Administration](Phase-1.md#part-1b-linux-administration)
- [ ] [Part 1C: Windows Administration](Phase-1.md#part-1c-windows-administration)
- [ ] [Part 2: Networking](Phase-1.md#part-2-networking-fundamentals)
- [ ] [Part 3: Cryptography](Phase-1.md#part-3-cryptography)
- [ ] [Part 3B: Authentication Standards Primer](Phase-1.md#part-3b-authentication-standards-primer)
- [ ] [Part 3C: Web Technology Fundamentals](Phase-1.md#part-3c-web-technology-fundamentals)
- [ ] Foundation Proof Gate — 10 PCAPs + admin baselines + 3 scripting tools + lab report

---

### ⚔️ Stage 1 — Core Technical Compact *(current)*

**Phase 2A — Offensive Fundamentals**

- [ ] [Part 4: Footprinting & Reconnaissance](Phase-2.md#part-4-footprinting-and-reconnaissance)
- [ ] [Part 5: Scanning](Phase-2.md#part-5-scanning)
- [ ] [Part 6: Enumeration](Phase-2.md#part-6-enumeration)
- [ ] [Part 6B: Database Security](Phase-2.md#part-6b-database-security)
- [ ] [Part 31: Password Cracking & Hash Analysis](Phase-2.md#part-31-password-cracking-hash-analysis)
- [ ] [Part 7: System Hacking & Initial Compromise](Phase-2.md#part-7-system-hacking-initial-compromise)

**Phase 4 — Web & Application Security**

- [ ] [Part 17: Web Application Hacking](Phase-4.md#part-17-web-application-hacking)
- [ ] [Part 12: Session Hijacking & Token Attacks](Phase-4.md#part-12-session-hijacking)
- [ ] [Part 18: Web Server Hacking](Phase-4.md#part-18-web-server-hacking)
- [ ] [Part 19: API Security](Phase-4.md#part-19-api-security)
- [ ] [Part 20: Bug Bounty Methodology](Phase-4.md#part-20-bug-bounty-methodology)

> **Phase 3 — Defensive Awareness** *(absorb in parallel — do NOT block on it)*
> - [Part 13A: Detection Engineering](Phase-3.md#part-13a-detection-engineering-soc-operations) during Phase 2A
> - [Part 14: IDS, Firewalls & Honeypots](Phase-3.md#part-14-ids-firewalls-and-honeypots) during Phase 2A
> - [Part 15: OSINT & Threat Intelligence](Phase-3.md#part-15-osint-threat-intelligence) during Phase 4

*Stage 1 Exit Gate: 3+ HTB/THM writeups, OWASP Top 10 hands-on, Linux & Windows privesc demonstrated*

---

### 🏢 Stage 2 — Enterprise Red Teaming

**Phase 6 — Infrastructure & Identity**

- [ ] [Part 23: Active Directory & Entra ID](Phase-6.md#part-23-active-directory-entra-id)
- [ ] [Part 24: Cloud Computing](Phase-6.md#part-24-cloud-computing)
- [ ] [Part 25: Container & Orchestration Security](Phase-6.md#part-25-container-orchestration-security)
- [ ] [Part 16: Adversary Emulation & Purple Teaming](Phase-6.md#part-16-adversary-emulation-purple-teaming)

**Phase 2B — Advanced Offensive Operations**

- [ ] [Part 9: Sniffing & Spoofing](Phase-2.md#part-9-sniffing-spoofing)
- [ ] [Part 10: Social Engineering](Phase-2.md#part-10-social-engineering)
- [ ] [Part 8: Malware & Weaponization](Phase-2.md#part-8-malware-weaponization)
- [ ] [Part 11: Denial of Service](Phase-2.md#part-11-denial-of-service) *(conceptual)*

**Report Writing (pulled forward)**

- [ ] [Part 39: Pentest Methodologies & Report Writing](Phase-10.md#part-39-penetration-testing-methodologies-report-writing)

> **Phase 3 — Defensive Awareness** *(absorb in parallel)*
> - [Part 13B: Security Operations Expansion](Phase-3.md#part-13b-security-operations-expansion) during Phase 2B
> - [Part 16: Adversary Emulation & Purple Teaming](Phase-6.md#part-16-adversary-emulation-purple-teaming) — Phase 6 capstone

*Stage 2 Exit Gate: AD domain attacked end-to-end, BloodHound exports in Git, 1 professional pentest report*

---

### 🎯 Stage 3 — Specialized Trade

**Phase 7 — Part 42 Only**

- [ ] [Part 42: Offensive Development & Tooling](Phase-7.md#part-42-offensive-development-tooling)

**Phase 9 — AI Security**

- [ ] [Part 38: AI & LLM Red Teaming](Phase-9.md#part-38-ai-llm-red-teaming)

**Phase 10 — Operations & Career**

- [ ] [Part 40: Red Team Operations & Tradecraft](Phase-10.md#part-40-red-team-operations-tradecraft)
- [ ] [Part 41: Proof of Work & Career Portfolio](Phase-10.md#part-41-proof-of-work-career-portfolio)

*Stage 3 Exit Gate: Custom C2 in lab, AI security research published, portfolio with 3+ professional reports, OSCP*

---

### 🟡 Post-Hire — Return After Employment

**Phase 5 — Wireless & Mobile**

- [ ] [Part 21: Wireless Network Security](Phase-5.md#part-21-wireless-network-security)
- [ ] [Part 22: Mobile Security](Phase-5.md#part-22-mobile-security)

**Phase 7 — Deep Specializations**

- [ ] [Part 27: Digital Forensics](Phase-7.md#part-27-digital-forensics)
- [ ] [Part 28: Reverse Engineering & Malware Analysis](Phase-7.md#part-28-reverse-engineering-malware-analysis)
- [ ] [Part 29: Modern Exploitation](Phase-7.md#part-29-modern-exploitation) *(requires Part 42 first)*

**Phase 8 — GRC & DevSecOps**

- [ ] [Part 35: Governance, Risk & Compliance](Phase-8.md#part-35-governance-risk-compliance-grc)
- [ ] [Part 36: Supply Chain Security](Phase-8.md#part-36-supply-chain-security)
- [ ] [Part 37: DevSecOps & Secure SDLC](Phase-8.md#part-37-devsecops-secure-sdlc)
- [ ] [Part 37B: Secure Code Review Methodology](Phase-8.md#part-37b-secure-code-review-methodology)
- [ ] [Part 43: Security Architecture & Engineering](Phase-8.md#part-43-security-architecture-engineering)

**Optional Specializations**

- [ ] [Part 26: OT/ICS/SCADA](Phase-6.md#part-26-oticsscada-security)
- [ ] [Part 30: Hardware Hacking](Phase-7.md#part-30-hardware-hacking-embedded-systems-optional-specialization)
- [ ] [Part 32: Physical Penetration Testing](Phase-7.md#part-32-physical-penetration-testing-optional-specialization)
- [ ] [Part 33: VoIP/SS7/5G](Phase-7.md#part-33-voip-telecommunications-security-optional-specialization)
- [ ] [Part 34: Blockchain/Web3](Phase-7.md#part-34-blockchain-web3-security-optional-specialization)
