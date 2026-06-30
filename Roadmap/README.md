# 🛡️ Cybersecurity & AI Security: Master Roadmap

> **Core Philosophy:** AI security is not a separate field — it is an expansion of traditional security domains. Master the systems, networks, and traditional security models first, then layer AI red teaming on top.

---

> [!IMPORTANT]
> **Modular Roadmap Structure:** The comprehensive content of this learning path has been divided into **10 dedicated phase modules** for ease of tracking and reading. You can access the detailed objectives by clicking the phase titles in the dashboard or learning path below.

---

## 🧭 Modular Roadmap Dashboard

| Phase | Module / Link                              | Core Topics & Focus                                                | Est. Pacing (FT / PT) |
| :---: | :----------------------------------------- | :----------------------------------------------------------------- | :-------------------: |
|  🏗️  | **[Phase 1: Foundation](Phase-1.md)**      | Hardware, OS, Linux & Windows Admin, Networking, Cryptography      |     4–6m / 6–10m      |
|  ⚔️   | **[Phase 2: Offense Core](Phase-2.md)**    | Recon, Scanning, Initial Access, Malware, Social Eng., Cracking    |     5–7m / 8–12m      |
|  🛡️  | **[Phase 3: Defense Core](Phase-3.md)**    | Detection Eng., SIEM, SOC, Threat Hunting, IR, OSINT               |      3–4m / 4–7m      |
|  🌐   | **[Phase 4: Web & App Sec](Phase-4.md)**   | Web Hacking, API Security, Bug Bounty Methodology                  |      3–4m / 4–7m      |
|  📡   | **[Phase 5: Wireless/Mobile](Phase-5.md)** | RF, WiFi, Bluetooth/BLE, NFC/RFID, Android/iOS pentesting          |      2–3m / 3–5m      |
|  ☁️   | **[Phase 6: Infrastructure](Phase-6.md)**  | AD & Entra ID, Cloud Sec (AWS/Azure), Kubernetes, ICS/SCADA        |     4–6m / 6–10m      |
|  🔬   | **[Phase 7: Advanced Sec](Phase-7.md)**    | DFIR, Malware RE, Exploit Dev (Heap/Kernel), Offensive Dev         |     4–7m / 8–12m      |
|  📋   | **[Phase 8: DevSecOps & GRC](Phase-8.md)** | SAST/DAST, Software Supply Chain, Threat Modeling, Architecture    |      2–3m / 3–5m      |
|  🧠   | **[Phase 9: AI Security](Phase-9.md)**     | LLM Red Teaming, Prompt Injection, RAG Poisoning, Agentic Exploits |      3–4m / 4–7m      |
|  🎯   | **[Phase 10: Career Ops](Phase-10.md)**    | Pentest Methodologies, Red Team Operations, Portfolios             |      2–3m / 3–5m      |
|  📊   | **Total Roadmap**                          | **30–48 Months (Full-Time) / 36–60 Months (Part-Time)**            |    **~2.5–5 Years**   |

> [!NOTE]
> **Timeline Reality Check:** The pacing assumes consistent lab work, documentation, and capstone completion. Optional specializations can add months beyond the core estimate.

---

## ⚡ Specialized Learning Paths (Tracks)

You do not need to follow the roadmap in a strict linear fashion if you have a specific career specialization in mind. Here are the recommended path configurations:

### 🔴 Red Team & Penetration Testing Track
*For aspiring pentesting, red teaming, and offensive security research roles.*
1. **[Phase 1](Phase-1.md)** (Foundations) ➔ **[Phase 2](Phase-2.md)** (Offense Core) ➔ **[Phase 4](Phase-4.md)** (Web & API) ➔ **[Phase 5](Phase-5.md)** (Wireless & Mobile) ➔ **[Phase 6](Phase-6.md)** (Infrastructure) ➔ **[Phase 7](Phase-7.md)** (Advanced & Exploit Dev) ➔ **[Phase 10](Phase-10.md)** (Red Team Ops)

### 🔵 SOC, DFIR & Defensive Engineering Track
*For security analysts, detection engineers, incident responders, and forensic examiners.*
1. **[Phase 1](Phase-1.md)** (Foundations) ➔ **[Phase 3](Phase-3.md)** (Defense Core) ➔ **[Phase 6](Phase-6.md)** (Infrastructure Security) ➔ **[Phase 7](Phase-7.md)** (Digital Forensics & Malware RE) ➔ **[Phase 8](Phase-8.md)** (Security Architecture & GRC)

### 🤖 AI Red Teaming & Security Specialist Track
*For engineers securing LLM applications, agentic systems, and cloud-native AI setups.*
1. **[Phase 1](Phase-1.md)** (Fundamentals) ➔ **[Phase 2](Phase-2.md)** (Offensive Basics) ➔ **[Phase 4](Phase-4.md)** (API Security) ➔ **[Phase 8](Phase-8.md)** (Supply Chain & DevSecOps) ➔ **[Phase 9](Phase-9.md)** (AI & LLM Red Teaming)

### 🧩 Optional Specializations
These tracks are powerful, but they are not required for the core roadmap. Add them after the relevant prerequisites are complete and only if they support your career direction.

- **Hardware & Embedded Security:** [Part 30](Phase-7.md#part-30-hardware-hacking-embedded-systems-optional-specialization)
- **Physical Penetration Testing:** [Part 32](Phase-7.md#part-32-physical-penetration-testing-optional-specialization)
- **Telecom Security:** [Part 33](Phase-7.md#part-33-voip-telecommunications-security-optional-specialization)
- **Blockchain & Web3 Security:** [Part 34](Phase-7.md#part-34-blockchain-web3-security-optional-specialization)

---

## 📖 How to Use This Roadmap

1. **Clone and Track:** Keep this repository open in a Markdown-compatible workspace (such as [Obsidian](https://obsidian.md/)).
2. **Interactive Checklists:** Every phase file has interactive checkbox inputs (`- [ ]`). Check them off as you read, practice, and master each topic.
3. **Do Not Bypass Gates:** Each section has a **Move-On Gate** (highlighted in `[!IMPORTANT]` blocks). Do not proceed to subsequent parts until you can perform the gate tasks confidently without documentation.
4. **Use Reflection Checkpoints:** At the end of each phase, answer the reflection prompts and complete the competency checklist before moving on.
5. **Build a Proof of Work:** As you pass the gates, document your work in a private Git repository to build your portfolio (as outlined in Phase 10).

---

## 📝 Continuous Documentation Protocol

> [!IMPORTANT]
> **Portfolio building starts in Phase 1, not Phase 10.**

Every phase in this roadmap includes a **Documentation Requirements** block listing the specific artifacts you must produce and commit. This is not optional — it is what transforms self-study into a professional portfolio.

**Set up from Day 1:**
1. **Create a private Git repository** (e.g., `cybersecurity-journey`) and commit after every lab session
2. **Use structured markdown** for all notes (objective → steps → output → lessons learned)
3. **Save tool output** — Nmap scans, Burp captures, PCAP files, SIEM queries, detection rules
4. **Create diagrams** for every architecture and attack chain (draw.io, Excalidraw, or Mermaid)
5. **Screenshot everything** — lab setups, tool output, successful exploitation, before/after hardening

**By Phase 10, your repository should contain:**
- 50+ structured lab notes across all phases
- 10+ network/architecture diagrams
- 5+ detection rules (Sigma/YARA/Suricata)
- 3+ professional reports (pentest, wireless, mobile, AI)
- 9 capstone project deliverables
- A curated selection ready for public portfolio publication

---

## 🛠️ Home Lab Hardware Specs

To successfully complete the hands-on labs across all modules:

* **Minimum Specifications:**
  - 32GB RAM (to run 2-3 VMs concurrently)
  - Quad-core CPU with VT-x/AMD-V nested virtualization support
  - 500GB Solid State Drive (SSD)
* **Recommended Specifications:**
  - 64GB RAM (needed for active Directory domain and container security labs)
  - 8-core CPU
  - 1TB NVMe SSD
* **RF & Wireless Testing:**
  - External USB WiFi adapter supporting monitor mode and packet injection (e.g. Alfa AWUS036ACH or chipsets like RTL8812AU).

---

## 🗺️ Detailed Phase Descriptions

### [Phase 1: The Unshakeable Foundation](Phase-1.md)
Master the TCP/IP stack, OSI model, DNS, HTTP/HTTPS, Linux CLI and administration, Windows administration and Event Viewer, Bash/PowerShell, Python/JavaScript, virtualization, cloud basics (AWS/Azure), Docker/Kubernetes, authentication, sessions, cookies, JSON APIs, CORS, and the cryptographic primitives underpinning all of security.

### [Phase 2: Offensive Core](Phase-2.md)
Footprinting, scanning, enumeration, system hacking, malware design, sniffing/spoofing, social engineering, denial-of-service, session hijacking, and password cracking. The complete offensive lifecycle from recon to impact.

### [Phase 3: Defense & Detection](Phase-3.md)
Detection engineering, SOC & SIEM fundamentals, IDS/IPS/honeypots, threat hunting, incident response basics, forensic fundamentals, and OSINT & threat intelligence. Understand what defenders see before you specialize further.

### [Phase 4: Web & Application Security](Phase-4.md)
Web application hacking, web server exploitation, API security (OWASP API Top 10), and professional bug bounty methodology.

### [Phase 5: Wireless & Mobile](Phase-5.md)
WiFi pentesting (WPA3, evil twin, PMKID), Bluetooth/BLE/Zigbee/NFC/RFID/GPS attacks, SDR spectrum analysis, and Android/iOS dynamic+static analysis.

### [Phase 6: Infrastructure & Identity](Phase-6.md)
Active Directory & Entra ID (on-prem + hybrid cloud identity), cloud computing attacks (AWS/Azure/GCP), container & Kubernetes security, OT/ICS/SCADA industrial systems, and adversary emulation & purple teaming.

### [Phase 7: Advanced Specializations](Phase-7.md)
Digital forensics & incident response, reverse engineering & malware analysis, modern exploitation (heap/kernel/browser), hardware hacking & embedded systems, offensive development (shellcode, C2, process injection, AMSI/ETW bypass), physical pentesting, VoIP/SS7/5G telecom, and blockchain/Web3 smart contract auditing.

### [Phase 8: Governance, Supply Chain, DevSecOps & Architecture](Phase-8.md)
GRC frameworks (NIST, ISO 27001, PCI-DSS, DPDP Act), supply chain security (SBOM, SLSA, dependency confusion), DevSecOps integration (SAST/DAST/SCA, secrets scanning, IaC security), and security architecture & engineering (Zero Trust, defense-in-depth design, segmentation, reference architectures).

### [Phase 9: AI Security](Phase-9.md)
Layer AI system knowledge on top of your mastered traditional track. Understand tokens, context windows, MCP, embeddings, temperature, fine-tuning, OWASP LLM Top 10, RAG poisoning, supply chain attacks, shadow AI prevention, and defensive AI operations.

### [Phase 10: Operations & Career](Phase-10.md)
Penetration testing methodologies (PTES, OWASP WSTG, NIST 800-115, professional report writing), red team operations & tradecraft, and building an unfakeable proof-of-work portfolio.

---

## ✅📋 Completion Tracker & Quick Navigation

**🧭 Control Layer:**
- [ ] [Execution Control Layer](#toc-execution-control-layer) — Proof standards, phase gates, role tracks, safety boundaries

**🏗️ Phase 1 — Foundation:**
- [ ] [Career Foundation & Lab Setup](Phase-1.md#career-foundation-lab-setup) — Lab Setup, Platforms, Academic Alignment
- [ ] [Part 1: Fundamentals](Phase-1.md#part-1-fundamentals) — Hardware, OS, Memory, Data, Programming
- [ ] [Part 1B: Linux Administration](Phase-1.md#part-1b-linux-administration) — Users, Permissions, Services, Networking, Logs, SELinux/AppArmor
- [ ] [Part 1C: Windows Administration](Phase-1.md#part-1c-windows-administration) — Users, NTFS, Registry, Event Viewer, PowerShell, AD Basics
- [ ] [Part 2: Networking Fundamentals](Phase-1.md#part-2-networking-fundamentals) — Layers 1–7, Protocols, Tools
- [ ] [Part 3: Cryptography](Phase-1.md#part-3-cryptography) — Concepts → Transit → Trust → Rest → Attacks

**⚔️ Phase 2 — Offensive Core:**
- [ ] [Part 4: Footprinting and Reconnaissance](Phase-2.md#part-4-footprinting-and-reconnaissance) — Passive → Active → Strategy
- [ ] [Part 5: Scanning](Phase-2.md#part-5-scanning) — Host Discovery → Port Enumeration → Defense Assessment
- [ ] [Part 6: Enumeration](Phase-2.md#part-6-enumeration) — Network Discovery → Service Profiling → Attack Mapping
- [ ] [Part 7: System Hacking & Initial Compromise](Phase-2.md#part-7-system-hacking-initial-compromise) — Breach → Escalation → Persistence → Evasion → Exfil → Reporting
- [ ] [Part 8: Malware & Weaponization](Phase-2.md#part-8-malware-weaponization) — Design → Weaponization → Evasion → Persistence → Anti-Forensics
- [ ] [Part 9: Sniffing & Spoofing](Phase-2.md#part-9-sniffing-spoofing) — Protocols → Sniffing → Spoofing → MITM → Defenses
- [ ] [Part 10: Social Engineering](Phase-2.md#part-10-social-engineering) — Recon → Digital → Human → Physical → Defense
- [ ] [Part 11: Denial of Service](Phase-2.md#part-11-denial-of-service) — Planning → Methods → Execution → Mitigation
- [ ] [Part 12: Session Hijacking](Phase-2.md#part-12-session-hijacking) — Steal → Hijack → Secure
- [ ] [Part 31: Password Cracking & Hash Analysis](Phase-2.md#part-31-password-cracking-hash-analysis) — Methodology, Tools, Rules, Wordlists, Offline Cracking

**🛡️ Phase 3 — Defense & Detection:**
- [ ] [Part 13A: Detection Engineering & SOC Operations](Phase-3.md#part-13a-detection-engineering-soc-operations) — SIEM, Detection Rules, Threat Hunting, IR, Forensic Fundamentals
- [ ] [Part 13B: Security Operations Expansion](Phase-3.md#part-13b-security-operations-expansion) — SOAR, DLP, Vulnerability Management, Insider Threat Detection
- [ ] [Part 14: IDS, Firewalls, and Honeypots](Phase-3.md#part-14-ids-firewalls-and-honeypots) — Strategy → Deployment → Deception → Operations
- [ ] [Part 15: OSINT & Threat Intelligence](Phase-3.md#part-15-osint-threat-intelligence) — Collection → Analysis → Automation → Dissemination

**🌐 Phase 4 — Web & Application Security:**
- [ ] [Part 17: Web Application Hacking](Phase-4.md#part-17-web-application-hacking) — Recon → Analysis → Exploit → Persist → Defend
- [ ] [Part 18: Web Server Hacking](Phase-4.md#part-18-web-server-hacking) — Recon → Hardening → Exploit → Persist
- [ ] [Part 19: API Security](Phase-4.md#part-19-api-security) — OWASP API Top 10, REST/GraphQL/gRPC, Auth Attacks, Testing Methodology
- [ ] [Part 20: Bug Bounty and Penetration Testing](Phase-4.md#part-20-bug-bounty-and-penetration-testing) — Scope → Recon → Exploit → Report

**📡 Phase 5 — Wireless & Mobile:**
- [ ] [Part 21: Wireless Pentesting](Phase-5.md#part-21-wireless-pentesting) — Recon → Breach → MITM → BLE/Zigbee/NFC/GPS/SDR → Defense
- [ ] [Part 22: Mobile Platform Pentesting](Phase-5.md#part-22-mobile-platform-pentesting) — Static → Dynamic → Network → Defense

**☁️ Phase 6 — Infrastructure, Identity & Purple Teaming:**
- [ ] [Part 23: Active Directory & Entra ID](Phase-6.md#part-23-active-directory-entra-id) — On-Prem AD → ADCS → Entra ID/OAuth
- [ ] [Part 24: Cloud Computing](Phase-6.md#part-24-cloud-computing) — Architecture → Storage → Deployment → Automation → Attacks
- [ ] [Part 25: Container & Orchestration Security](Phase-6.md#part-25-container-orchestration-security) — Docker, Kubernetes, Secrets Management
- [ ] [Part 26: OT/ICS/SCADA Security](Phase-6.md#part-26-oticsscada-security) — Industrial Protocols, PLC, HMI, Safety Systems
- [ ] [Part 16: Adversary Emulation & Purple Teaming](Phase-6.md#part-16-adversary-emulation-purple-teaming) — MITRE ATT&CK, APT Simulation, Metrics

**🔬 Phase 7 — Advanced Specializations:**
- [ ] [Part 27: Digital Forensics](Phase-7.md#part-27-digital-forensics) — Prep → Analysis → Network → Reporting
- [ ] [Part 28: Reverse Engineering & Malware Analysis](Phase-7.md#part-28-reverse-engineering-malware-analysis) — Static → Dynamic → Debugging → Anti-RE → Automation
- [ ] [Part 29: Modern Exploitation](Phase-7.md#part-29-modern-exploitation) — Memory Safety → Sandbox Escape → Mitigation Bypass
- [ ] [Part 42: Offensive Development & Tooling](Phase-7.md#part-42-offensive-development-tooling) — Shellcode, C2 Implants, Process Injection, AMSI/ETW Bypass

**🧩 Optional Specializations:**
- [ ] [Part 30: Hardware Hacking & Embedded Systems](Phase-7.md#part-30-hardware-hacking-embedded-systems-optional-specialization) — Optional specialization: Firmware, JTAG, UART, Side-Channel, IoT
- [ ] [Part 32: Physical Penetration Testing](Phase-7.md#part-32-physical-penetration-testing-optional-specialization) — Optional specialization: Lock Bypass, HID Attacks, Facility Assessment, Reporting
- [ ] [Part 33: VoIP & Telecommunications Security](Phase-7.md#part-33-voip-telecommunications-security-optional-specialization) — Optional specialization: SS7, SIP/RTP, VoIP Exploitation, 5G
- [ ] [Part 34: Blockchain & Web3 Security](Phase-7.md#part-34-blockchain-web3-security-optional-specialization) — Optional specialization: Smart Contracts, DeFi Attacks, Wallet Security

**📋 Phase 8 — Governance, Supply Chain, DevSecOps & Architecture:**
- [ ] [Part 35: Governance, Risk & Compliance](Phase-8.md#part-35-governance-risk-compliance-grc) — Frameworks, Regulations, Audit, Scope
- [ ] [Part 36: Supply Chain Security](Phase-8.md#part-36-supply-chain-security) — Dependency Attacks, SBOM, Build Integrity, OSS Risk
- [ ] [Part 37: DevSecOps & Secure SDLC](Phase-8.md#part-37-devsecops-secure-sdlc) — SAST/DAST/SCA, Secrets Scanning, Pipeline Security
- [ ] [Part 43: Security Architecture & Engineering](Phase-8.md#part-43-security-architecture-engineering) — Zero Trust, Defense-in-Depth Design, Segmentation, Reference Architectures

**🧠 Phase 9 — AI Security:**
- [ ] [Part 38: AI & LLM Red Teaming](Phase-9.md#part-38-ai-llm-red-teaming) — AI Fundamentals → Adversarial Attacks → Agentic AI → Defensive AI → Workflow Integration → Projects → Career

**🎯 Phase 10 — Operations & Career:**
- [ ] [Part 39: Penetration Testing Methodologies & Report Writing](Phase-10.md#part-39-penetration-testing-methodologies-report-writing) — PTES, OWASP WSTG, NIST 800-115, Threat Modeling, CVSS, Report Writing
- [ ] [Part 40: Red Team Operations & Tradecraft](Phase-10.md#part-40-red-team-operations-tradecraft) — Infrastructure, Discipline, Operations
- [ ] [Part 41: Proof of Work & Career Portfolio](Phase-10.md#part-41-proof-of-work-career-portfolio) — Tools, GitHub, Writing, Bug Bounties, Certifications

---
