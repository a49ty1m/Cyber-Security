# 🛡️ Cybersecurity & AI Security: Master Roadmap

> **Core Philosophy:** AI security is not a separate field — it is an expansion of traditional security domains. Master the systems, networks, and traditional security models first, then layer AI red teaming on top.

> **Career Target:** Penetration Testing → Red Teaming → Advanced Offensive Security → AI Red Teaming

> [!IMPORTANT]
> **Phase 1 is substantially complete. Your next action is [Phase 2 → Part 4: Footprinting & Reconnaissance](Phase-2.md#part-4-footprinting-and-reconnaissance).**

---

## 📑 Table of Contents

| # | Section | What it does |
|:-:|---------|-------------|
| 1 | [📊 Phase Dashboard](#-phase-dashboard) | 10-phase overview with timelines |
| 2 | [🗺️ Personal Execution Order](#-personal-execution-order) | **Your actual study sequence — start here** |
| 3 | [⚡ Career Tracks](#-career-tracks) | Red Team / Defensive / AI specialization paths |
| 4 | [📖 How to Use This Roadmap](#-how-to-use-this-roadmap) | Practical usage rules |
| 5 | [🛡️ Phase 3 Treatment](#-phase-3-treatment) | Why Phase 3 is a parallel track, not a blocker |
| 6 | [📚 Resource Usage Policy](#-resource-usage-policy) | Roadmap vs courses vs labs |
| 7 | [🩹 Just-in-Time Prerequisites](#-just-in-time-prerequisite-system) | Fix gaps without restarting phases |
| 8 | [🎯 Daily Focus Rule](#-daily-focus-rule) | What to study today |
| 9 | [📝 Documentation Protocol](#-documentation-protocol) | Portfolio from Day 1 |
| 10 | [💻 Programming Track](#-programming-parallel-track) | Python / Bash / PowerShell milestones |
| 11 | [🛠️ Home Lab Specs](#-home-lab-hardware-specs) | Hardware requirements |
| 12 | [🗂️ Master Part Index](#-master-part-index) | Jump to any Part by number |
| 13 | [🛠️ AI Study Assistant](#-ai-study-assistant) | Expand any topic into a full module |
| 14 | [✅ Completion Tracker](#-completion-tracker) | Interactive progress checklist |

---

## 📊 Phase Dashboard

> The phase number is **organizational metadata**, not execution order. See [Personal Execution Order](#-personal-execution-order) for your actual sequence.

| Phase | Module | Core Topics & Focus | Est. Time (FT / PT) |
| :---: | :----- | :------------------ | :-----------------: |
| 🏗️ | **[Phase 1: Foundation](Phase-1.md)** | Hardware, OS, Linux & Windows Admin, Networking, Crypto, Auth Primer | 4–6m / 6–10m |
| ⚔️ | **[Phase 2: Offense Core](Phase-2.md)** | Recon, Scanning, Enumeration, Initial Access, Privesc, Cracking | 5–7m / 8–12m |
| 🛡️ | **[Phase 3: Defense Core](Phase-3.md)** _(parallel track)_ | Detection Eng., SIEM, SOC, Threat Hunting, IR, OSINT | 4–6m / 6–10m |
| 🌐 | **[Phase 4: Web & App Sec](Phase-4.md)** | Web Hacking, API Security, Bug Bounty Methodology | 3–4m / 4–7m |
| 📡 | **[Phase 5: Wireless & Mobile](Phase-5.md)** _(after Phase 6)_ | WiFi, BLE/NFC/RFID, Android/iOS (+optional GPS/SDR) | 3–5m / 5–8m |
| ☁️ | **[Phase 6: Infrastructure](Phase-6.md)** | AD & Entra ID, Cloud (AWS/Azure/GCP), Kubernetes, ICS/SCADA (opt.) | 6–9m / 10–14m |
| 🔬 | **[Phase 7: Advanced Sec](Phase-7.md)** | Offensive Dev (Part 42 first), DFIR, Malware RE, Exploit Dev | 8–14m / 12–18m |
| 📋 | **[Phase 8: DevSecOps & GRC](Phase-8.md)** | SAST/DAST, Supply Chain, Threat Modeling, Architecture | 4–6m / 6–9m |
| 🧠 | **[Phase 9: AI Security](Phase-9.md)** | LLM Red Teaming, Prompt Injection, RAG Poisoning, Agentic Exploits | 3–5m / 5–8m |
| 🎯 | **[Phase 10: Operations & Career](Phase-10.md)** | Red Team Ops, Pentest Methodologies, Report Writing, Portfolio | 3–5m / 5–8m |
| 📊 | **Total Roadmap** | **41–65 Months Full-Time / 64–100 Months Part-Time** | **~3.5–8 Years** |

> [!WARNING]
> **Realistic Timeline:** The original 30–48 month estimate was aspirational. With real lab work, documentation, and capstone completion, expect **41–65 months full-time** (3.5–5.5 years). Part-time learners should plan **5–8 years**. Optional specializations (GPS/SDR, OT/ICS, VoIP, Web3) are not included in the totals above.

> [!TIP]
> **Practice Cadence — long roadmaps fail without rhythm:**
> - **Daily (30 min):** One platform challenge — [TryHackMe](https://tryhackme.com), [PicoCTF](https://picoctf.org), or [OverTheWire](https://overthewire.org) in early phases
> - **Weekly:** Complete 1 HTB/THM machine and write it up — no writeup means the learning didn't happen
> - **Monthly:** Review Git commits, identify what you still can't do without notes — those are your gaps
> - **If you haven't committed to Git in 2 weeks:** you're drifting — restart with a small lab, not a big concept

---

## 🗺️ Personal Execution Order

> [!IMPORTANT]
> **This is your dependency-aware study sequence.** Phase numbers are organizational labels — this section defines the actual order based on technical prerequisites, career value, and skill dependencies. It supersedes any other ordering suggestion in this file.

```text
╔══════════════════════════════════════════════════════════════╗
║  📍 CURRENT POSITION                                         ║
╚══════════════════════════════════════════════════════════════╝

Phase 1 — Foundation
████████████████████░  ~80–90% complete
Status: SUBSTANTIALLY COMPLETE
Action: Patch gaps just-in-time as they arise. Do NOT restart.
    │
    ▼
Phase 2A — Offensive Fundamentals          ◄── START HERE NOW
────────────────────────────────────────────────────────────────
  Part 4  → Footprinting & Reconnaissance
  Part 5  → Scanning
  Part 6  → Enumeration
  Part 6B → Database Security
  Part 31 → Password Cracking & Hash Analysis  (required before Part 7)
  Part 7  → System Hacking & Initial Compromise
    │
    ▼
Phase 2B — Advanced Offensive Operations
────────────────────────────────────────────────────────────────
  Core Parts 9, 10, 12: do now
  Parts 8, 11 (Malware, DoS): defer until after Phase 4
    │
    ▼
Phase 4 — Web & Application Security
────────────────────────────────────────────────────────────────
  Part 17 → Web Application Hacking
  Part 18 → Web Server Hacking
  Part 19 → API Security
  Part 20 → Bug Bounty Methodology
    │
    ▼
Phase 6 — Infrastructure & Identity
────────────────────────────────────────────────────────────────
  Part 23 → Active Directory & Entra ID  (on-prem first, then cloud)
  Part 24 → Cloud Computing  (AWS/Azure/GCP)
  Part 25 → Container & Kubernetes Security
  Part 16 → Adversary Emulation & Purple Teaming  (Phase 6 capstone)
    │
    ▼
Phase 5 — Wireless & Mobile  [intentionally AFTER Phase 6]
────────────────────────────────────────────────────────────────
  Part 21 → Wireless Network Security
  Part 22 → Mobile Security
  GPS/SDR/NFC deep dives = OPTIONAL — skip unless role demands it
    │
    ▼
Phase 7 — Advanced Specializations
────────────────────────────────────────────────────────────────
  ⚠️ HARD SEQUENCE — do not reorder:
  Part 42 → Offensive Development & Tooling  (required first)
  Part 27 → Digital Forensics
  Part 28 → Reverse Engineering & Malware Analysis
  Part 29 → Modern Exploitation  (requires Part 42)
  Optional: Parts 30, 32, 33, 34 — defer unless role-specific
    │
    ▼
Phase 8 — Governance, DevSecOps & Architecture
────────────────────────────────────────────────────────────────
  Part 35 → GRC
  Part 36 → Supply Chain Security
  Part 37 → DevSecOps & Secure SDLC
  Part 37B → Secure Code Review
  Part 43 → Security Architecture
    │
    ▼
Phase 9 — AI Security
────────────────────────────────────────────────────────────────
  ⚠️ Requires Phases 1–8 complete — do NOT skip ahead
    │
    ▼
Phase 10 — Operations & Career
────────────────────────────────────────────────────────────────
  ⚠️ Requires Phase 9 complete
  Part 40 → Red Team Operations & Tradecraft  (do first)
  Part 39 → Pentest Methodologies & Report Writing
  Part 41 → Proof of Work & Career Portfolio
```

### Why This Order Differs from Phase Numbers

| Decision | Rationale |
|----------|-----------|
| **Phase 6 before Phase 5** | AD, cloud identity, and containers are central to enterprise red teaming. Wireless/mobile is a specialization, not a prerequisite for internal compromise. Do higher-value material first. |
| **Phase 9 required before Phase 10** | Phase 10 files explicitly require Phase 9. The older shortcut (Phase 7 → Phase 10) contradicted the actual file dependencies. |
| **Phase 2B core only before Phase 4** | Malware development and DoS are far more valuable after web/infrastructure context. Without that foundation they become rabbit holes. |
| **Part 31 before Part 7** | Password cracking is a prerequisite for most initial access and post-exploitation work in Part 7. |
| **Part 42 before Part 29** | Part 29 (Modern Exploitation) explicitly requires shellcode writing and assembly fundamentals built in Part 42. |

---

## ⚡ Career Tracks

### 🔴 Red Team & Penetration Testing _(your track)_

> Follow the [Personal Execution Order](#-personal-execution-order) above. The sequence below is a summary.

**1→2A→2B(core)→4→6→5→7→8→9→10**
Phase 3 runs as a **parallel defensive awareness layer**, not a sequential blocker — see [Phase 3 Treatment](#-phase-3-treatment).

### 🔵 SOC, DFIR & Defensive Engineering

_For analysts, detection engineers, incident responders, and forensic examiners._

**[Phase 1](Phase-1.md) → [Phase 3](Phase-3.md) → [Phase 6](Phase-6.md) → [Phase 7](Phase-7.md) → [Phase 8](Phase-8.md)**

### 🤖 AI Red Teaming & Security Specialist

_For engineers securing LLM applications, agentic systems, and cloud-native AI._

**[Phase 1](Phase-1.md) → [Phase 2](Phase-2.md) → [Phase 4](Phase-4.md) → [Phase 8](Phase-8.md) → [Phase 9](Phase-9.md)**

### 🧩 Optional Specializations

Add only after the relevant prerequisites are complete and only if they align with your career direction.

| Specialization | Entry Point |
|----------------|-------------|
| Hardware & Embedded Security | [Part 30](Phase-7.md#part-30-hardware-hacking-embedded-systems-optional-specialization) |
| Physical Penetration Testing | [Part 32](Phase-7.md#part-32-physical-penetration-testing-optional-specialization) |
| Telecom Security (VoIP/SS7/5G) | [Part 33](Phase-7.md#part-33-voip-telecommunications-security-optional-specialization) |
| Blockchain & Web3 Security | [Part 34](Phase-7.md#part-34-blockchain-web3-security-optional-specialization) |
| OT/ICS/SCADA | [Part 26](Phase-6.md#part-26-oticsscada-security) |

---

## 📖 How to Use This Roadmap

1. **Single Source of Truth:** The roadmap decides what you study. Not a course. Not a THM path. Not whatever topic seems interesting today. The roadmap.
2. **Interactive Checklists:** Every phase file has `- [ ]` checkboxes. Check them off only when you can perform the skill — not when you've read about it.
3. **Respect the Gates:** Each Part has a **Move-On Gate** (in `[!IMPORTANT]` callouts). Do not proceed until you pass it without looking at notes.
4. **Document Everything:** Every lab session produces a Git-committed writeup. No writeup = the learning didn't happen.
5. **Use Phase Files Directly:** This README is an index. The actual curriculum is in the phase files. Click through.
6. **AI Expansion:** See [AI Study Assistant](#-ai-study-assistant) to expand any checklist item into a full structured module.

---

## 🛡️ Phase 3 Treatment

Phase 3 is **not a sequential prerequisite** for the Red Team track. It runs as a **parallel defensive awareness layer** alongside your offensive studies.

**Absorb these alongside Phase 2/4/6 — they make you a better attacker:**

| Concept | Why it matters offensively | When |
|---------|---------------------------|------|
| MITRE ATT&CK framework | Maps your TTPs to what defenders detect | During Phase 2B |
| Windows/Linux event IDs | Know what your attacks log | During Phase 2A |
| SIEM basics (Splunk/ELK) | Query logs to improve OPSEC | During Phase 2B |
| EDR/XDR behavior detection | Know why payloads get caught | During Phase 6/7 |
| Detection engineering concepts | Write attacks that evade rules | During Phase 6 |
| Threat hunting methodology | Purple team exercises | During Phase 6 Part 16 |

**Available but not blocking your path:**
- Deep SOC Tier 1/2/3 workflows
- Full IR specialization (forensics from an offensive angle is in Phase 7 Part 27)
- Advanced DLP policy design

> **Phase 3 becomes fully active at Phase 6 Part 16 (Purple Teaming)** — that's when defensive knowledge and offensive skill combine for the first time in a structured way. Until then, absorb Phase 3 concepts opportunistically as they appear in your current phase.

> **Do not spend 4–6 months becoming a SOC analyst before continuing your offensive progression.** Detection awareness makes you a better attacker. Full defensive specialization is a career pivot, not a step on the red team path.

---

## 📚 Resource Usage Policy

> [!IMPORTANT]
> **The roadmap is the curriculum. Courses, books, and platforms are supporting tools — not competing curricula.**

| Resource | Role | Rule |
|----------|------|------|
| **This Roadmap** | Curriculum — what to learn and in what order | Always primary |
| **Courses & Books** | Explanation and reference | Use for the current Part only. Do not start a course that covers a future phase. |
| **TryHackMe / HTB / PortSwigger** | Practice environments | Use for the current Part only. Do not follow a THM path that pulls you off-track. |
| **Python / Bash / PowerShell** | Parallel weekend programming track | Weekends only. Does not compete with the main track. |

**Decision tree — "Can I study X right now?"**

```
Is X required by my current Part?      → Yes: study it
Is X a prerequisite patch?             → Yes: patch it, then return
Is X programming?                      → Save for the weekend track
Is X from a future phase?              → Mark it, do NOT start it now
Is X optional?                         → Defer unless role-specific
```

---

## 🩹 Just-in-Time Prerequisite System

Do NOT restart an entire phase because of a single knowledge gap. Use **targeted prerequisite patches**.

**How it works:** When a topic requires something you haven't built yet — stop, do a focused 2–4 session patch on that specific gap, then return immediately.

**Examples:**

| Blocked topic | Missing prerequisite | Patch scope | Return |
|---------------|----------------------|-------------|--------|
| Network traffic analysis | Wireshark fundamentals | 2–4 sessions: capture → filter → dissect | Current Part |
| HTTPS interception | TLS handshake mechanics | TLS/PKI/certificate chain | Current Part |
| Phase 6 Part 23 (AD attacks) | Kerberos / Windows identity | Phase 1 Part 1C Stage 5 & 6 only | Part 23 |
| Phase 4 web interception | HTTP/browser internals | Phase 1 Part 3C review | Current Part |

> **This is the opposite of "go back to Phase 1 and redo everything."** Fix the specific gap — not the whole phase.

---

## 🎯 Daily Focus Rule

> **The roadmap answers one question every day: "What should I study today?"**

Your unit of progress is: **Concept → Tool → Lab → Attack methodology → Evidence → Gate → Next**

Not: **read checklist → check box → move on.**

| Question | Answer |
|----------|--------|
| What am I learning? | The current Part in the Personal Execution Order |
| What do I practice? | The lab specified in that Part |
| What do I produce? | The artifact in the Documentation Requirements block |
| How do I know I'm done? | I pass the Move-On Gate without looking at notes |
| Can I study X instead? | Only if X is: current Part / prerequisite patch / weekend programming |

---

## 📝 Documentation Protocol

> [!IMPORTANT]
> **Portfolio building starts in Phase 1, not Phase 10.**

Every phase file contains a **Documentation Requirements** block. These artifacts are not optional — they are what turns self-study into a professional portfolio.

**Set up on Day 1:**

1. Create a private Git repository (e.g., `cybersecurity-journey`) and commit after every session
2. Use structured markdown for all notes — format: `Objective → Steps → Output → Lessons Learned`
3. Save all tool output — Nmap scans, Burp captures, PCAPs, SIEM queries, detection rules
4. Create diagrams for every architecture and attack chain (draw.io, Excalidraw, or Mermaid)
5. Screenshot everything — lab setup, tool output, successful exploitation, before/after states

**By Phase 10, your repository should contain:**

| Artifact | Minimum count |
|----------|:---:|
| Structured lab notes | 50+ |
| Network / architecture diagrams | 10+ |
| Detection rules (Sigma / YARA / Suricata) | 5+ |
| Professional reports (pentest, wireless, mobile, AI) | 3+ |
| Capstone project deliverables | 9 |

---

## 💻 Programming Parallel Track

> [!NOTE]
> **Weekend track only — not a competing curriculum.** Python, Bash, and PowerShell are practiced on Saturdays/Sundays. The milestones below are phase-specific — study them when the roadmap reaches that phase, not before.

| Language | Milestone | Phase it's needed |
|----------|-----------|-------------------|
| **Python** | File I/O, loops, functions, `subprocess` | Phase 2A |
| **Python** | `socket`, `requests`, `scapy` basics | Phase 2 |
| **Python** | HTTP client, form parsing, cookies | Phase 4 |
| **Python** | `ldap3`, `impacket` usage | Phase 6 |
| **Python** | `numpy`, model inference basics | Phase 9 (prerequisite) |
| **Bash** | Variables, loops, conditionals, pipes | Phase 2A |
| **Bash** | `curl`, `grep`/`awk`/`sed`, process management | Phase 2 |
| **Bash** | Cron, log parsing, tool chaining | Phase 3 |
| **PowerShell** | Cmdlets, pipelines, object output | Phase 2A |
| **PowerShell** | AD module, `Invoke-`, WMI/CIM | Phase 6 |
| **PowerShell** | AMSI bypass, constrained language mode | Phase 7 |
| **C / Assembly** | Shellcode writing, x86-64 calling conventions | Phase 7 Part 42 — **do not start early** |

> **Rule:** If a milestone belongs to a future phase, mark it and move on. Start it when the roadmap arrives there.

---

## 🛠️ Home Lab Hardware Specs

| Category | Minimum | Recommended |
|----------|---------|-------------|
| **RAM** | 32 GB (2–3 VMs concurrently) | 64 GB (AD domain + container labs) |
| **CPU** | Quad-core with VT-x/AMD-V | 8-core with nested virtualization |
| **Storage** | 500 GB SSD | 1 TB NVMe SSD |
| **Wireless** | — | External USB WiFi adapter with monitor mode & packet injection (e.g. Alfa AWUS036ACH, RTL8812AU chipset) |

---

## 🗂️ Master Part Index

> **Navigation aid:** Parts are numbered non-sequentially by design (Parts 31 and 42 live in Phase 2 and Phase 7 respectively; Part 16 lives in Phase 6). Use this table to jump directly to any Part without guessing which phase file it's in.

|  Part  | Name                                                                                                           | Phase  | Notes                                         |
| :----: | :------------------------------------------------------------------------------------------------------------- | :----: | :-------------------------------------------- |
|   1    | [Fundamentals](Phase-1.md#part-1-fundamentals)                                                                 |   1    | Hardware, OS, Memory, Programming             |
|   1B   | [Linux Administration](Phase-1.md#part-1b-linux-administration)                                                |   1    |                                               |
|   1C   | [Windows Administration](Phase-1.md#part-1c-windows-administration)                                            |   1    |                                               |
|   2    | [Networking](Phase-1.md#part-2-networking)                                                                     |   1    | TCP/IP, Protocols, Routing, VPNs              |
|   3    | [Cryptography](Phase-1.md#part-3-cryptography)                                                                 |   1    |                                               |
|   3B   | [Authentication Standards Primer](Phase-1.md#part-3b-authentication-standards-primer)                          |   1    | Sessions, JWT, OAuth 2.0, OIDC, MFA           |
|   3C   | [Web Technology Fundamentals](Phase-1.md#part-3c-web-technology-fundamentals)                                  |   1    | HTTP, Cookies, SOP/CORS, REST APIs            |
|   4    | [Footprinting & Reconnaissance](Phase-2.md#part-4-footprinting-and-reconnaissance)                             |   2    | **← Current**                                 |
|   5    | [Scanning](Phase-2.md#part-5-scanning)                                                                         |   2    |                                               |
|   6    | [Enumeration](Phase-2.md#part-6-enumeration)                                                                   |   2    |                                               |
|   6B   | [Database Security](Phase-2.md#part-6b-database-security)                                                      |   2    | MySQL, MSSQL, MongoDB, Redis                  |
| **31** | [**Password Cracking & Hash Analysis**](Phase-2.md#part-31-password-cracking-hash-analysis)                    | **2**  | **⚠️ Lives between Parts 6 and 7**            |
|   7    | [System Hacking & Initial Compromise](Phase-2.md#part-7-system-hacking-initial-compromise)                     |   2    |                                               |
|   8    | [Malware & Weaponization](Phase-2.md#part-8-malware-weaponization)                                             |   2    | Full malware engineering → Part 42            |
|   9    | [Sniffing & Spoofing](Phase-2.md#part-9-sniffing-spoofing)                                                     |   2    |                                               |
|   10   | [Social Engineering](Phase-2.md#part-10-social-engineering)                                                    |   2    |                                               |
|   11   | [Denial of Service](Phase-2.md#part-11-denial-of-service)                                                      |   2    |                                               |
|   12   | [Session Hijacking](Phase-2.md#part-12-session-hijacking)                                                      |   2    |                                               |
|  13A   | [Detection Engineering & SOC Operations](Phase-3.md#part-13a-detection-engineering-soc-operations)             |   3    | SIEM, Detection Rules, Threat Hunting         |
|  13B   | [Security Operations Expansion](Phase-3.md#part-13b-security-operations-expansion)                             |   3    | SOAR, DLP, Vuln Management                    |
|   14   | [IDS, Firewalls & Honeypots](Phase-3.md#part-14-ids-firewalls-and-honeypots)                                   |   3    |                                               |
|   15   | [OSINT & Threat Intelligence](Phase-3.md#part-15-osint-threat-intelligence)                                    |   3    |                                               |
|   17   | [Web Application Hacking](Phase-4.md#part-17-web-application-hacking)                                          |   4    |                                               |
|   18   | [Web Server Hacking](Phase-4.md#part-18-web-server-hacking)                                                    |   4    |                                               |
|   19   | [API Security](Phase-4.md#part-19-api-security)                                                                |   4    |                                               |
|   20   | [Bug Bounty Methodology](Phase-4.md#part-20-bug-bounty-methodology)                                            |   4    |                                               |
|   21   | [Wireless Network Security](Phase-5.md#part-21-wireless-network-security)                                      |   5    |                                               |
|   22   | [Mobile Security](Phase-5.md#part-22-mobile-security)                                                          |   5    |                                               |
|   23   | [Active Directory & Entra ID](Phase-6.md#part-23-active-directory-entra-id)                                    |   6    |                                               |
|   24   | [Cloud Computing Security](Phase-6.md#part-24-cloud-computing)                                                 |   6    |                                               |
|   25   | [Container & Orchestration Security](Phase-6.md#part-25-container-orchestration-security)                      |   6    | Docker, Kubernetes, Secrets Mgmt              |
|   26   | [OT/ICS/SCADA Security _(OPTIONAL)_](Phase-6.md#part-26-oticsscada-security)                                   |   6    | Industrial Protocols, PLC, HMI                |
| **16** | [**Adversary Emulation & Purple Teaming**](Phase-6.md#part-16-adversary-emulation-purple-teaming)              | **6**  | **⚠️ Phase 6 capstone — NOT Phase 3**         |
| **42** | [**Offensive Development & Tooling**](Phase-7.md#part-42-offensive-development-tooling)                        | **7**  | **⚠️ Complete BEFORE Part 29**                |
|   27   | [Digital Forensics](Phase-7.md#part-27-digital-forensics)                                                      |   7    |                                               |
|   28   | [Reverse Engineering & Malware Analysis](Phase-7.md#part-28-reverse-engineering-malware-analysis)              |   7    |                                               |
|   29   | [Modern Exploitation](Phase-7.md#part-29-modern-exploitation)                                                  |   7    | ⚠️ Requires Part 42 first                     |
|   30   | [Hardware Hacking _(OPTIONAL)_](Phase-7.md#part-30-hardware-hacking-embedded-systems-optional-specialization)  |   7    |                                               |
|   32   | [Physical Pentesting _(OPTIONAL)_](Phase-7.md#part-32-physical-penetration-testing-optional-specialization)    |   7    |                                               |
|   33   | [VoIP/SS7/5G _(OPTIONAL)_](Phase-7.md#part-33-voip-telecommunications-security-optional-specialization)        |   7    |                                               |
|   34   | [Blockchain/Web3 _(OPTIONAL)_](Phase-7.md#part-34-blockchain-web3-security-optional-specialization)            |   7    |                                               |
|   35   | [Governance, Risk & Compliance](Phase-8.md#part-35-governance-risk-compliance-grc)                             |   8    | NIST, ISO 27001, PCI-DSS, DPDP                |
|   36   | [Supply Chain Security](Phase-8.md#part-36-supply-chain-security)                                              |   8    | SBOM, SLSA, Dependency Confusion              |
|   37   | [DevSecOps & Secure SDLC](Phase-8.md#part-37-devsecops-secure-sdlc)                                            |   8    | SAST/DAST/SCA, Pipeline Security              |
|  37B   | [Secure Code Review Methodology](Phase-8.md#part-37b-secure-code-review-methodology)                           |   8    | Semgrep, taint analysis                       |
|   43   | [Security Architecture & Engineering](Phase-8.md#part-43-security-architecture-engineering)                    |   8    | Zero Trust, Defense-in-Depth                  |
|   38   | [AI & LLM Red Teaming](Phase-9.md#part-38-ai-llm-red-teaming)                                                  |   9    | Prompt injection, RAG attacks, adversarial ML |
| **40** | [**Red Team Operations & Tradecraft **](Phase-10.md#part-40-red-team-operations-tradecraft)                    | **10** | **⚠️ Complete BEFORE Part 39**                |
|   39   | [Pentest Methodologies & Report Writing](Phase-10.md#part-39-penetration-testing-methodologies-report-writing) |   10   | PTES, OWASP WSTG, NIST 800-115, CVSS          |
|   41   | [Proof of Work & Career Portfolio](Phase-10.md#part-41-proof-of-work-career-portfolio)                         |   10   | Certifications, GitHub, Bug Bounties          |


---

## 🛠️ AI Study Assistant

> **Expand any checklist item into a full learning module.** See [PROMPT_TEMPLATE.md](PROMPT_TEMPLATE.md) — paste it into ChatGPT, Claude, or Gemini with any roadmap bullet point to receive a structured 11-section breakdown: purpose → offensive perspective → defensive perspective → tools → lab → key takeaways.

---

## ✅ Completion Tracker

> Mark items complete in the **phase files** (where the detailed content and gates live), not just here. This tracker is for quick cross-phase navigation.

---

**🏗️ Phase 1 — Foundation** _(substantially complete)_

- [ ] [Career Foundation & Lab Setup](Phase-1.md#career-foundation-lab-setup)
- [ ] [Part 1: Fundamentals](Phase-1.md#part-1-fundamentals) — Hardware, OS, Memory, Programming
- [ ] [Part 1B: Linux Administration](Phase-1.md#part-1b-linux-administration) — Users, Permissions, Services, Logs, SELinux/AppArmor
- [ ] [Part 1C: Windows Administration](Phase-1.md#part-1c-windows-administration) — Users, NTFS, Registry, Event Viewer, PowerShell, AD Basics
- [ ] [Part 2: Networking](Phase-1.md#part-2-networking-fundamentals) — OSI/TCP-IP, Protocols, Tools
- [ ] [Part 3: Cryptography](Phase-1.md#part-3-cryptography) — Concepts → Transit → Trust → Rest → Attacks
- [ ] [Part 3B: Authentication Standards Primer](Phase-1.md#part-3b-authentication-standards-primer) — Sessions, JWT, OAuth 2.0, OIDC, MFA
- [ ] [Part 3C: Web Technology Fundamentals](Phase-1.md#part-3c-web-technology-fundamentals) — HTTP, Cookies, SOP/CORS, REST APIs

---

**⚔️ Phase 2 — Offensive Core** _(current phase)_

_Phase 2A — do in this order:_

- [ ] [Part 4: Footprinting & Reconnaissance](Phase-2.md#part-4-footprinting-and-reconnaissance) — Passive → Active → Strategy 
- [ ] [Part 5: Scanning](Phase-2.md#part-5-scanning) — Host Discovery → Port Enumeration → Defense Assessment
- [ ] [Part 6: Enumeration](Phase-2.md#part-6-enumeration) — Service Profiling → Attack Mapping
- [ ] [Part 6B: Database Security](Phase-2.md#part-6b-database-security) — MySQL, MSSQL, MongoDB, Redis
- [ ] [Part 31: Password Cracking & Hash Analysis](Phase-2.md#part-31-password-cracking-hash-analysis) — Methodology, Tools, Wordlists _(prerequisite for Part 7)_
- [ ] [Part 7: System Hacking & Initial Compromise](Phase-2.md#part-7-system-hacking-initial-compromise) — Breach → Escalation → Persistence → Evasion → Exfil

_Phase 2B — core now, deferred items later:_

- [ ] [Part 9: Sniffing & Spoofing](Phase-2.md#part-9-sniffing-spoofing) — Protocols → Sniffing → MITM → Defenses _(do now)_
- [ ] [Part 10: Social Engineering](Phase-2.md#part-10-social-engineering) — Recon → Digital → Human → Physical _(do now)_
- [ ] [Part 12: Session Hijacking](Phase-2.md#part-12-session-hijacking) — Steal → Hijack → Secure _(do now)_
- [ ] [Part 8: Malware & Weaponization](Phase-2.md#part-8-malware-weaponization) — Taxonomy → msfvenom → Evasion _(defer until after Phase 4)_
- [ ] [Part 11: Denial of Service](Phase-2.md#part-11-denial-of-service) — Methods → Execution → Mitigation _(defer until after Phase 4)_

---

**🛡️ Phase 3 — Defense & Detection** _(parallel track — absorb alongside offensive phases)_

- [ ] [Part 13A: Detection Engineering & SOC Operations](Phase-3.md#part-13a-detection-engineering-soc-operations)
- [ ] [Part 13B: Security Operations Expansion](Phase-3.md#part-13b-security-operations-expansion)
- [ ] [Part 14: IDS, Firewalls & Honeypots](Phase-3.md#part-14-ids-firewalls-and-honeypots)
- [ ] [Part 15: OSINT & Threat Intelligence](Phase-3.md#part-15-osint-threat-intelligence)

---

**🌐 Phase 4 — Web & Application Security**

- [ ] [Part 17: Web Application Hacking](Phase-4.md#part-17-web-application-hacking) — Recon → Exploit → Persist
- [ ] [Part 18: Web Server Hacking](Phase-4.md#part-18-web-server-hacking) — Recon → Exploit → Persist
- [ ] [Part 19: API Security](Phase-4.md#part-19-api-security) — OWASP API Top 10, REST/GraphQL/gRPC, Auth Attacks
- [ ] [Part 20: Bug Bounty & Penetration Testing](Phase-4.md#part-20-bug-bounty-and-penetration-testing) — Scope → Recon → Exploit → Report

---

**☁️ Phase 6 — Infrastructure, Identity & Purple Teaming** _(before Phase 5)_

- [ ] [Part 23: Active Directory & Entra ID](Phase-6.md#part-23-active-directory-entra-id) — On-Prem AD → ADCS → Entra ID/OAuth
- [ ] [Part 24: Cloud Computing](Phase-6.md#part-24-cloud-computing) — Architecture → Storage → Attacks
- [ ] [Part 25: Container & Orchestration Security](Phase-6.md#part-25-container-orchestration-security) — Docker, Kubernetes, Secrets Mgmt
- [ ] [Part 26: OT/ICS/SCADA Security](Phase-6.md#part-26-oticsscada-security) — _(OPTIONAL)_
- [ ] [Part 16: Adversary Emulation & Purple Teaming](Phase-6.md#part-16-adversary-emulation-purple-teaming) — MITRE ATT&CK, APT Simulation _(capstone)_

---

**📡 Phase 5 — Wireless & Mobile** _(after Phase 6)_

- [ ] [Part 21: Wireless Pentesting](Phase-5.md#part-21-wireless-pentesting) — Recon → Breach → MITM → BLE/Zigbee/NFC
- [ ] [Part 22: Mobile Platform Pentesting](Phase-5.md#part-22-mobile-platform-pentesting) — Static → Dynamic → Network

---

**🔬 Phase 7 — Advanced Specializations** _(hard sequence: 42 → 27 → 28 → 29)_

- [ ] [Part 42: Offensive Development & Tooling](Phase-7.md#part-42-offensive-development-tooling) — Shellcode, C2, AMSI/ETW Bypass ← **do first**
- [ ] [Part 27: Digital Forensics](Phase-7.md#part-27-digital-forensics) — Evidence → Analysis → Network → Reporting
- [ ] [Part 28: Reverse Engineering & Malware Analysis](Phase-7.md#part-28-reverse-engineering-malware-analysis) — Static → Dynamic → Anti-RE
- [ ] [Part 29: Modern Exploitation](Phase-7.md#part-29-modern-exploitation) — Memory Safety → Sandbox Escape → Mitigation Bypass

**🧩 Optional Specializations** _(defer unless role-specific)_

- [ ] [Part 30: Hardware Hacking](Phase-7.md#part-30-hardware-hacking-embedded-systems-optional-specialization) — Firmware, JTAG, UART, Side-Channel, IoT
- [ ] [Part 32: Physical Penetration Testing](Phase-7.md#part-32-physical-penetration-testing-optional-specialization) — Lock Bypass, HID, Facility Assessment
- [ ] [Part 33: VoIP & Telecommunications Security](Phase-7.md#part-33-voip-telecommunications-security-optional-specialization) — SS7, SIP/RTP, 5G
- [ ] [Part 34: Blockchain & Web3 Security](Phase-7.md#part-34-blockchain-web3-security-optional-specialization) — Smart Contracts, DeFi, Wallet Security

---

**📋 Phase 8 — Governance, Supply Chain, DevSecOps & Architecture**

- [ ] [Part 35: Governance, Risk & Compliance](Phase-8.md#part-35-governance-risk-compliance-grc) — Frameworks, Regulations, Audit
- [ ] [Part 36: Supply Chain Security](Phase-8.md#part-36-supply-chain-security) — SBOM, SLSA, Dependency Confusion, Build Integrity
- [ ] [Part 37: DevSecOps & Secure SDLC](Phase-8.md#part-37-devsecops-secure-sdlc) — SAST/DAST/SCA, Secrets Scanning, Pipeline Security
- [ ] [Part 37B: Secure Code Review Methodology](Phase-8.md#part-37b-secure-code-review-methodology) — Code Review, Semgrep Rule Writing
- [ ] [Part 43: Security Architecture & Engineering](Phase-8.md#part-43-security-architecture-engineering) — Zero Trust, Defense-in-Depth, Reference Architectures

---

**🧠 Phase 9 — AI Security**

- [ ] [Part 38: AI & LLM Red Teaming](Phase-9.md#part-38-ai-llm-red-teaming) — AI Fundamentals → Adversarial Attacks → Agentic AI → Defensive AI → Career

---

**🎯 Phase 10 — Operations & Career**

- [ ] [Part 40: Red Team Operations & Tradecraft](Phase-10.md#part-40-red-team-operations-tradecraft) — C2, OPSEC, Campaign Planning, Deconfliction ← **do first**
- [ ] [Part 39: Pentest Methodologies & Report Writing](Phase-10.md#part-39-penetration-testing-methodologies-report-writing) — PTES, OWASP WSTG, NIST 800-115, CVSS
- [ ] [Part 41: Proof of Work & Career Portfolio](Phase-10.md#part-41-proof-of-work-career-portfolio) — Certifications, GitHub, Bug Bounties, Interview Prep

---
