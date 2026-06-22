# Cybersecurity & AI Security: Master Roadmap

> **Core Philosophy:** AI security is built ON TOP of traditional security mastery — not in place of it.

> **Companion Audit:** [Roadmap_AUDIT.md](Roadmap_AUDIT.md)

---

## Table of Contents

**🏗️ Phase 1 — Foundation**
- [Career Foundation & Lab Setup](#toc-career-foundation--lab-setup)
- [Part 1: Fundamentals](#toc-part-1-fundamentals) — Hardware, OS, Memory, Data, Wireless, Programming, Applications
- [Part 2: Networking Fundamentals](#toc-part-2-networking-fundamentals) — Layers 1–7, Protocols, Tools
- [Part 3: Cryptography](#toc-part-3-cryptography) — Concepts → Transit → Trust → Rest → Attacks

**⚔️ Phase 2 — Offensive Core**
- [Part 4: Footprinting and Reconnaissance](#toc-part-4-footprinting-and-reconnaissance) — Passive → Active → Strategy
- [Part 5: Scanning](#toc-part-5-scanning) — Host Discovery → Port Enumeration → Defense Assessment
- [Part 6: Enumeration](#toc-part-6-enumeration) — Network Discovery → Service Profiling → Attack Mapping
- [Part 7: System Hacking & Initial Compromise](#toc-part-7-system-hacking--initial-compromise) — Breach → Escalation → Persistence → Evasion → Exfil
- [Part 8: Malware & Weaponization](#toc-part-8-malware--weaponization) — Design → Weaponization → Evasion → Persistence
- [Part 9: Sniffing & Spoofing](#toc-part-9-sniffing--spoofing) — Protocols → Sniffing → Spoofing → MITM → Defenses
- [Part 10: Social Engineering](#toc-part-10-social-engineering) — Recon → Digital → Human → Physical → Defense
- [Part 11: Denial of Service](#toc-part-11-denial-of-service) — Planning → Methods → Execution → Mitigation
- [Part 12: Session Hijacking](#toc-part-12-session-hijacking) — Steal → Hijack → Secure

**🛡️ Phase 3 — Defense & Detection**
- [Part 13: Detection & Mitigation](#toc-part-13-detection--mitigation-blue-team-perspective) — Blue Team defensive detection
- [Part 14: IDS, Firewalls, and Honeypots](#toc-part-14-ids-firewalls-and-honeypots) — Strategy → Deployment → Deception → Operations
- [Part 15: OSINT & Threat Intelligence](#toc-part-15-osint--threat-intelligence) — Collection → Analysis → Automation → Dissemination
- [Part 16: Adversary Emulation & Purple Teaming](#toc-part-16-adversary-emulation--purple-teaming) — MITRE ATT&CK, APT Simulation, Metrics

**🌐 Phase 4 — Web & Application Security**
- [Part 17: Web Application Hacking](#toc-part-17-web-application-hacking) — Recon → Analysis → Exploit → Persist → Defend
- [Part 18: Web Server Hacking](#toc-part-18-web-server-hacking) — Recon → Hardening → Exploit → Persist
- [Part 19: API Security](#toc-part-19-api-security) — OWASP API Top 10, REST/GraphQL/gRPC, Auth Attacks
- [Part 20: Bug Bounty and Penetration Testing](#toc-part-20-bug-bounty-and-penetration-testing) — Scope → Recon → Exploit → Report

**📡 Phase 5 — Wireless & Mobile**
- [Part 21: Wireless Pentesting](#toc-part-21-wireless-pentesting) — Recon → Breach → MITM → BLE/Zigbee/NFC/GPS/SDR → Defense
- [Part 22: Mobile Platform Pentesting](#toc-part-22-mobile-platform-pentesting) — Static → Dynamic → Network → Defense

**☁️ Phase 6 — Infrastructure & Identity**
- [Part 23: Active Directory & Entra ID](#toc-part-23-active-directory--entra-id) — On-Prem AD → ADCS → Entra ID/OAuth
- [Part 24: Cloud Computing](#toc-part-24-cloud-computing) — Architecture → Storage → Deployment → Automation → Attacks
- [Part 25: Container & Orchestration Security](#toc-part-25-container--orchestration-security) — Docker, Kubernetes, Secrets Management
- [Part 26: OT/ICS/SCADA Security](#toc-part-26-oticsscada-security) — Industrial Protocols, PLC, HMI, Safety Systems

**🔬 Phase 7 — Advanced Specializations**
- [Part 27: Digital Forensics](#toc-part-27-digital-forensics) — Prep → Analysis → Network → Reporting
- [Part 28: Reverse Engineering & Malware Analysis](#toc-part-28-reverse-engineering--malware-analysis) — Static → Dynamic → Debugging → Anti-RE → Automation
- [Part 29: Modern Exploitation](#toc-part-29-modern-exploitation) — Memory Safety → Sandbox Escape → Mitigation Bypass
- [Part 30: Hardware Hacking & Embedded Systems](#toc-part-30-hardware-hacking--embedded-systems) — Firmware, JTAG, UART, Side-Channel, IoT
- [Part 31: Password Cracking & Hash Analysis](#toc-part-31-password-cracking--hash-analysis) — Methodology, Tools, Rules, Wordlists
- [Part 32: Physical Penetration Testing](#toc-part-32-physical-penetration-testing) — Lock Bypass, HID Attacks, Facility Assessment
- [Part 33: VoIP & Telecommunications Security](#toc-part-33-voip--telecommunications-security) — SS7, SIP/RTP, VoIP Exploitation, 5G
- [Part 34: Blockchain & Web3 Security](#toc-part-34-blockchain--web3-security) — Smart Contracts, DeFi Attacks, Wallet Security

**📋 Phase 8 — Governance, Supply Chain & DevSecOps**
- [Part 35: Governance, Risk & Compliance](#toc-part-35-governance-risk--compliance-grc) — Frameworks, Regulations, Audit, Scope
- [Part 36: Supply Chain Security](#toc-part-36-supply-chain-security) — Dependency Attacks, SBOM, Build Integrity, OSS Risk
- [Part 37: DevSecOps & Secure SDLC](#toc-part-37-devsecops--secure-sdlc) — SAST/DAST/SCA, Secrets Scanning, Pipeline Security

**🧠 Phase 9 — AI Security**
- [Part 38: AI & LLM Red Teaming](#toc-part-38-ai--llm-red-teaming) — Adversarial Attacks → Agentic AI → Defensive AI → Projects

**🎯 Operations & Career**
- [Part 39: Penetration Testing Methodologies & Report Writing](#toc-part-39-penetration-testing-methodologies--report-writing) — PTES, OWASP WSTG, NIST 800-115, CVSS
- [Part 40: Red Team Operations & Tradecraft](#toc-part-40-red-team-operations--tradecraft) — Infrastructure, Discipline, Operations
- [Part 41: Proof of Work & Career Portfolio](#toc-part-41-proof-of-work--career-portfolio) — Tools, GitHub, Writing, Bug Bounties, Certifications

---

## ⏱️ Pacing Estimates

_Multi-year curriculum. Not a weekend plan._

| Phase | Full-Time | Part-Time |
|---|---|---|
| Phase 1: Foundation | 2–3 months | 4–6 months |
| Phase 2: Offensive Core | 3–4 months | 6–8 months |
| Phase 3: Defense & Detection | 1–2 months | 2–4 months |
| Phase 4: Web & App Security | 2–3 months | 4–6 months |
| Phase 5: Wireless & Mobile | 1–2 months | 2–4 months |
| Phase 6: Infrastructure & Identity | 2–3 months | 4–6 months |
| Phase 7: Advanced Specializations | 3–5 months | 6–10 months |
| Phase 8: GRC, Supply Chain & DevSecOps | 1–2 months | 2–4 months |
| Phase 9: AI Security | 2–3 months | 4–6 months |
| **Total** | **~18–30 months** | **~36–58 months** |

---

<a id="toc-career-foundation--lab-setup"></a>
## Career Foundation & Lab Setup

_Before starting the technical curriculum, establish your academic foundation, lab environment, and practice platforms._

### **Professional Development & Enablers**

- [ ] **Lab Progression Map (Packet Tracer → GNS3/EVE-NG → Wireshark validation)**
  - Goal: Move from simple networking practice to realistic, packet-level practice without guessing.
  - Stage A — Packet Tracer (learning topology + basic configs)
    - Build networks quickly (routers/switches/firewalls).
    - Learn addressing, routing, VLANs, ACLs, NAT basics.
    - Focus: “Does my design work?”
  - Stage B — GNS3/EVE-NG (real OS images + realistic behavior)
    - Same idea, but with actual services and Linux-based networking stacks.
    - Use real images (where possible) to practice:
      - routing protocols (OSPF/BGP basics)
      - firewall policies
      - DNS/DHCP
      - VPNs (IPsec/OpenVPN)
      - segmentation, multi-tier routing
  - Stage C — Validate everything with Wireshark (packet truth)
    - After each change/config push:
      - Capture traffic (pcap) at the interface where you expect behavior to occur.
      - Confirm:
        - correct IPs, ports, protocols
        - correct routes (SYN/SYN-ACK/ACK flows)
        - DNS queries/responses
        - firewall drops/rejects
      - Save captures (naming convention like `LAB01_vlan_trunk_acl_v1.pcap`) to compare later.
    - Result: You stop relying on “it seems to work” and start learning from evidence.

- [ ] **Virtualization Breadth (Type-1 + Type-2)**
  - Goal: Avoid being locked into one platform. Labs should migrate.
  - Type-1 hypervisors (closer to the hardware)
    - ESXi, Proxmox
    - Usually better performance and easier “lab appliance” patterns.
  - Type-2 hypervisors (runs on top of an OS)
    - VMware Workstation, VirtualBox
    - Great for quick VMs, testing, and local dev.
  - Practice habit:
    - Make at least one “template VM” that can be moved (or recreated quickly) between platforms.
    - Use consistent disk images / cloud-init / documented steps.
    - Result: If one platform breaks, your lab doesn’t die with it.

- [ ] **Cloud Assets Core (VPC/VNET + Security controls + IAM + Load Balancing)**
  - Goal: Learn cloud networking the way defenders and attackers reason about it.
  - Core components to practice
    - VPC/VNET
      - subnets
      - route tables
      - gateways
    - Security Groups / NACLs
      - stateful vs stateless thinking
      - least privilege rules
    - Load Balancers
      - front-end distribution
      - listener rules
      - health checks
    - IAM
      - who can create/modify networking resources
      - role-based access
      - permissions boundaries
  - Why it matters: Cloud security incidents often happen because of misconfigured networking and overly permissive IAM.

- [ ] **Automation Muscle (idempotent scripts for repeated lab tasks)**
  - Goal: Your time should go to learning—not clicking the same steps.
  - Automate things like:
    - Subnet discovery
      - detect existing CIDRs
      - propose non-overlapping subnets
    - Config pushes
      - push configs to routers/firewalls via SSH/Ansible
    - Log cleanup
      - rotate logs
      - clear test artifacts before retesting
  - “Idempotent” means:
    - If you run the script 10 times, the environment ends in the same correct state each time.
    - No duplicates, no random drift, no “works only the first time”.
  - Example outcomes:
    - Rebuild the same lab topology in minutes.
    - Retest after Wireshark capture without manual cleanup.

- [ ] **Monitoring & Evasion (baseline: NetFlow/SNMP/pcap; label what defenders see)**
  - Goal: Become fluent in “visibility.” What logging exists, what it misses, and why.
  - Baseline data sources
    - NetFlow
      - high-level “who talked to whom”
      - bytes/flows
    - SNMP
      - device metrics
      - traffic counters (less granular than pcap)
    - pcap
      - full packet headers
      - payload (most detailed)
  - Key mindset
    - For each technique or network change, determine what’s observable in each tool:
      - Does NetFlow show the connection attempt?
      - Does SNMP increase counters?
      - Is the packet content visible in pcap?
    - Record gaps:
      - Some changes appear only at L7.
      - Some are blocked before NetFlow can classify them.
      - Some are “silent” depending on where capture happens.
  - Defender-oriented framing
    - Even if you’re doing offensive-style practice, the lab should answer: “If I were the defender, what would I detect?”
    - This builds real-world operational awareness.

- [ ] **Certifications (CompTIA Network+ / Cisco / AWS Advanced Networking)**
  - Goal: Use structured certification objectives to avoid missing basics.
  - Network+ (entry)
    - fundamentals: routing concepts
    - subnetting
    - troubleshooting
  - Cisco core certs
    - deeper routing/switching knowledge
    - firewall-adjacent networking knowledge
  - AWS Advanced Networking
    - cloud-native routing
    - segmentation
    - scaling patterns
  - This isn’t “to collect badges”—it’s to ensure you learn networking in a complete sequence.

- [ ] **Ethics & ROE (Rules of Engagement + audit trails)**
  - Goal: Make your practice safe and accountable.
  - Explicit ROE:
    - what systems are allowed
    - what test types are allowed
    - data-handling rules
  - Audit trails:
    - record what you ran and when
      - script logs
      - command history exports
      - change notes
  - Always use labs/consented environments for hands-on activities.
  - Why it belongs in lab setup: Without ROE, even “harmless” testing habits can become unsafe.

- [ ] **Automation Scaling (mass config / port scans with Python)**
  - Goal: Prepare for high-volume tasks you’ll face in real workflows.
  - What to scale:
    - Mass config deployment across many lab nodes
    - Port scan sweeps to baseline services
    - Faster feedback loops
  - Good practice:
    - Use rate limiting.
    - Use concurrency controls.
    - Store scan results as structured output (JSON/CSV) so you can diff runs.

- [ ] **Monitoring Deep Dives (SNMP/NetFlow to visualize exfil patterns)**
  - Goal: Practice detection at the “pattern” level, not just “did the packets work?”
  - Advanced lab idea:
    - Create a scenario resembling data movement.
    - Simulate “exfil-like” flows:
      - large transfers
      - repeated small transfers
      - odd destinations
    - Then observe:
      - NetFlow charts
        - spikes in egress bytes
        - unusual destination patterns
      - SNMP counters
        - traffic anomalies at the interface level
        - traffic anomalies at the device level
      - Correlate with pcap
        - confirm what created the pattern
    - Result: You learn to connect “what happened” (pcap) to “what detection sees” (NetFlow/SNMP).

---

### **Academic & Career Alignment**

_Goal: Maximize your formal education and align academic work with offensive security career requirements._

- [ ] **Degree Baseline**
  - A formal undergraduate degree (**B-Tech in CS, IT, or related field**) fulfills baseline **HR screening requirements** for entry-level security roles and many certifications.

- [ ] **Leverage Academic Projects**
  - Treat university **database, networking, and software engineering projects** as structural training for:
    - **backend exploit development**
    - **API security**
    - **system architecture** understanding

- [ ] **Coding Curriculum Alignment**
  - The **C, C++, and Python** coding taught in engineering semesters provides the **architectural foundation** needed to eventually write:
    - custom, undetected payloads
    - exploit primitives

- [ ] **Capstone/Final Year Projects**
  - Target a security-related capstone to build a **portfolio piece** (examples):
    - vulnerability scanner
    - SIEM dashboard
    - malware analysis sandbox
    - network IDS

- [ ] **Internship Targeting**
  - Pursue internships at **SOCs, MSSPs, consulting firms, or product security teams** during academic years to build **real-world defensive/offensive experience** before graduation.

- [ ] **Research & Publications**
  - If possible, contribute to:
    - academic security research
    - CVE disclosures
    - conference talks (BSides, DefCon villages)
  - Goal: differentiate from other graduates.

---

### **Training Platforms & Lab Environments**

_Goal: Build practical muscle memory through structured, hands-on hacking exercises._

- [ ] **TryHackMe (Beginner → Intermediate)**
  - Complete **learning paths** for guided, progressive skill building:
    - Pre-Security
    - Jr Penetration Tester
    - Offensive Pentesting

- [ ] **Hack The Box (Intermediate → Advanced)**
  - Progress through active and retired machines covering:
    - Linux/Windows privesc
    - AD exploitation
    - web attacks
  - Target: **Hacker rank** or above.

- [ ] **OverTheWire Bandit (Linux Fundamentals)**
  - Complete all **34 levels** to build Linux CLI muscle memory:
    - file manipulation
    - SSH
    - permissions
    - scripting
    - process management

- [ ] **OverTheWire Natas (Web Security)**
  - Complete levels to practice server-side web exploitation:
    - command injection
    - SQLi
    - file inclusion
    - session attacks

- [ ] **PentesterLab (Web Exploitation)**
  - Work through exercises and badges focusing on:
    - OWASP Top 10
    - JWT attacks
    - OAuth flaws
    - deserialization

- [ ] **VulnHub (Offline Labs)**
  - Download and attack purposely vulnerable VMs in your local **VMware/VirtualBox** lab for offline practice (no internet dependency).

- [ ] **CyberDefenders (Blue Team)**
  - Practice DFIR challenges to understand the defender’s perspective:
    - memory forensics
    - malware analysis
    - log analysis
  - Use this to sharpen evasion awareness.

- [ ] **Capture The Flag (CTFs)**
  - Participate in:
    - picoCTF
    - NahamCon CTF
    - HTB CTF
    - Google CTF
  - Goal: develop speed, creativity, and multi-domain problem solving under pressure.

- [ ] **Active Directory Labs**
  - Build dedicated AD lab environments (DC + workstations) in **VirtualBox/VMware**, or use **GOAD (Game of Active Directory)** to practice:
    - Kerberoasting
    - BloodHound
    - lateral movement
    - domain persistence

- [ ] **TryHackMe AI Security Path**
  - Complete the dedicated AI security learning path covering:
    - AI Threat Modeling
    - Data Poisoning
    - Prompt Security
    - AI Forensics
  - Isolated lab environments keep hands-on AI attack/defense exercises safe.

- [ ] **PortSwigger Web Security Academy (Free)**
  - Complete labs covering the **full OWASP Top 10** plus advanced topics:
    - SQL injection, XSS, CSRF, SSRF, XXE
    - JWT attacks, OAuth flaws, WebSocket attacks
    - **Web LLM Attacks** — dedicated labs for attacking LLM-integrated web applications
  - Goal: Earn the **Burp Suite Certified Practitioner (BSCP)** certification.

- [ ] **OWASP AI Security Resources**
  - Study the **OWASP LLM Top 10 (2025)** and the **OWASP AI Security Project**
  - Use the **AI Red Team Lab** for structured prompt injection and jailbreaking exercises
  - Contribute to the **OWASP AI Exchange** for community-driven threat intelligence

- [ ] **Local AI Security Lab Setup (Recommended)**
  - Build a **self-hosted AI testing playground** for safe exploit practice:
    - **Ollama** — run open-source LLMs (Llama, Mistral, Gemma) locally without cloud dependency
    - **Open WebUI** — deploy a ChatGPT-like interface connected to your local Ollama instance
    - **Custom MCP Configurations** — configure Model Context Protocol servers to test tool-use exploits, permission escalation, and agentic attack scenarios
    - **Vulnerable AI Apps** — deploy intentionally vulnerable LLM applications (OWASP AI Goat, Damn Vulnerable LLM Agent) for structured exploitation practice
  - This is the **most recommended method** for testing prompt injection, jailbreaking, and agentic exploits safely without risking production API bans.

---

### **Foundation Proof Gate**

_Goal: Prove readiness before touching serious offensive material._

- [ ] **Linux Administration Proof**
  - Create users/groups, set file permissions/ACLs, configure `sudo`, manage services with `systemctl`, inspect logs with `journalctl`, configure networking, and document all commands.
  - Deliverable: `linux_admin_baseline.md` with commands, outputs, mistakes, and fixes.

- [ ] **Windows Administration Proof**
  - Create local users/groups, inspect Event Viewer, manage services, use PowerShell remoting in a lab, read registry locations safely, and enable basic audit logging.
  - Deliverable: `windows_admin_baseline.md` with screenshots, commands, and event IDs observed.

- [ ] **Networking Packet Proof**
  - Capture and explain ARP, DNS, TCP handshake, TLS handshake, HTTP request/response, ICMP, DHCP, NAT behavior, firewall deny, and one failed connection.
  - Deliverable: 10 named `.pcap` files plus a short explanation for each.

- [ ] **Scripting Proof**
  - Build three small tools:
    - log parser
    - subnet/IP helper
    - HTTP/API requester
  - Deliverable: scripts in a Git repository with README, usage examples, and test input/output.

- [ ] **Documentation Proof**
  - Write one complete lab report using the Part 39 reporting style: scope, environment, steps, evidence, findings, remediation, and lessons learned.
  - Deliverable: `foundation_lab_report.md`.

- [ ] **Safety Proof**
  - Write a personal lab ROE covering allowed targets, forbidden targets, network isolation, malware handling, cloud budget limits, credential storage, and data cleanup.
  - Deliverable: `lab_rules_of_engagement.md`.

---

<a id="toc-part-1-fundamentals"></a>
## Part 1: Fundamentals

### **Stage 1: Hardware, CPU & Pre-Boot Environment**

_Goal: Master the machine before the Operating System initializes._

- [ ] **CPU Operations:** Master the **Fetch-Decode-Execute** cycle to understand how code actually runs at the hardware level.

- [ ] **Registers:** Command the "steering wheel" of the CPU: **EAX/RAX** (accumulator), **ESP/RSP** (stack pointer), and **EIP/RIP** (instruction pointer).

- [ ] **Architecture Types:** Distinguish between **x86** (32-bit) and **x64** (64-bit) addressing and how they handle memory instructions differently.

- [ ] **Instruction Sets:** Develop a working familiarity with **Assembly** language (**MOV**, **PUSH**, **POP**, **CALL**, **JMP**).

- [ ] **The Boot Chain:** Master the sequence from **UEFI/Secure Boot** $\rightarrow$ **Bootloader** $\rightarrow$ **Kernel Load** $\rightarrow$ **Init/Systemd**.

- [ ] **Hardware I/O & DMA:** Understand how **Direct Memory Access (DMA)** allows peripherals to read/write system RAM by bypassing the CPU.

- [ ] **Storage Forensics:** Understand the physical data storage on **HDDs vs. SSDs** and why "deleting" is not "wiping" in a forensics context.

---

### **Stage 2: Operating System Internals**

_Goal: Understand the resource manager and its internal logic._

- [ ] **Privilege Levels:** Master the **"Ring" architecture**; specifically the separation between **Ring 0** (Kernel) and **Ring 3** (User).

- [ ] **System Calls:** Trace syscall execution (e.g., **NtCreateFile** or **execve**) from user-space API calls through the Interrupt to the kernel handler.

- [ ] **Process & Thread Mechanics:** Understand the lifecycle of processes and threads, including scheduling and context switching.

- [ ] **Process Environment Block (PEB):** In Windows, master the **PEB structure** to find loaded DLLs or implement anti-debugging techniques.

- [ ] **Authorization & Tokens:** Master Windows **SIDs**, **Access Tokens**, and **Token Impersonation**; understand Linux **Namespaces** and **Cgroups** (the basis for containers).

- [ ] **File Systems (Linux):** Master the root directory structure, **Inodes**, and the **"Everything is a file"** philosophy.

- [ ] **File Systems (Windows):** Master **NTFS permissions**, **Registry hives**, and the usage of **Alternate Data Streams (ADS)** to hide payloads.

---

### **Stage 3: Memory Management**

_Goal: Understand how memory is organized and managed._

- [ ] **Virtual Memory:** Learn how the OS maps physical RAM to virtual addresses to provide process isolation.

- [ ] **The Stack:** Master the **LIFO** (Last-In, First-Out) structure and the **Function Prologue/Epilogue** to understand how return addresses are stored.

- [ ] **The Heap:** Understand **dynamic memory allocation** and how applications request memory at runtime.

- [ ] **Segmentation & Paging:** Understand **segment descriptors** and **page tables** for virtual address translation.

- [ ] **Memory Protection:** Learn about **page permissions (R/W/X)** and **privilege level separation**.

---

### **Stage 4: Data Representation & Logic**

_Goal: Master binary representation and Boolean logic fundamentals._

- [ ] **Number Systems:** Be able to convert between **Binary, Decimal, and Hexadecimal** mentally.

- [ ] **Boolean Logic:** Master **AND, OR, NOT, and XOR** (the foundation of encryption and obfuscation).

- [ ] **File Headers:** Identify file types (EXE, ELF, JPG) by their **"Magic Bytes"** instead of extensions.

- [ ] **Instruction Sets:** Basic familiarity with **Assembly** (MOV, PUSH, POP, CALL, JMP).

---

### **Stage 5: Wireless & Physical Connections**

_Goal: Understand wireless protocols and physical security infrastructure._

**WiFi Fundamentals:**

- [ ] **802.11 Standards:** Understand **802.11a/b/g/n/ac/ax**, frequency bands (**2.4GHz, 5GHz, 6GHz**), and channel allocation.

- [ ] **WiFi Authentication:** Learn **Open, WEP, WPA/WPA2/WPA3** handshakes and encryption methods (**TKIP, CCMP, GCMP**).

- [ ] **Enterprise WiFi:** Understand **EAP variants (PEAP, TTLS, TLS)** and **RADIUS** server architecture.

- [ ] **Regulatory:** Know **FCC/ETSI** regulations, **DFS**, and regional channel restrictions.

**RF Survey Fundamentals:**

- [ ] **Antennas & Gain:** Understand antenna types (omni/directional), **dBi gain**, **attenuation**, and **FSPL**.

- [ ] **Channel Planning:** Know **2.4/5/6 GHz** channel spacing, **overlap**, and interference concepts.

- [ ] **Tools Intro:** Basic understanding of **Kismet, iw, iwconfig** for monitoring networks.

**Bluetooth & BLE Fundamentals:**

- [ ] **BLE Stack:** Understand **GAP, GATT**, **advertising**, **pairing/bonding**, and **security modes**.

- [ ] **BLE Protocols:** Know **UUID, services, characteristics**, and connection establishment.

- [ ] **Bluetooth Classic:** Understand **profiles, L2CAP, RFCOMM**, and basic architecture.

**NFC/RFID Fundamentals:**

- [ ] **NFC Standards:** Know **ISO14443, ISO15693**, and **Type 1-4** tag families.

- [ ] **MIFARE Overview:** Understand **Classic vs. DESFire/Ultralight** architecture and basic operation.

- [ ] **RFID Basics:** Know **passive vs. active**, range, frequency bands, and use cases.

**IoT Protocols:**

- [ ] **Zigbee/Z-Wave:** Understand mesh networking, **joining mechanisms**, and basic security architecture.

- [ ] **LoRaWAN:** Know **gateway-node architecture**, **join requests**, and regional parameters.

**Physical Security:**

- [ ] **Access Control Systems:** Understand **magstripe, smart card, RFID readers** and tamper detection basics.

- [ ] **Cable Infrastructure:** Know **UTP/STP, fiber optics**, connector types, and physical plant organization.

- [ ] **Environmental Threats:** Understand **electromagnetic shielding**, **TEMPEST concepts**, and basic mitigation.

---

### **Stage 5b: Mobile Platform Architecture**

_Goal: Understand Android and iOS architecture and security models._

**Android Fundamentals:**

- [ ] **APK Structure:** Understand **APK format, manifest, resources, assets**, and signed vs. unsigned APKs.

- [ ] **Android Security Model:** Learn **sandboxing, SELinux, permissions model (M+)**, and **app verification**.

- [ ] **Rooting & SuperUser:** Understand what **rooting** means, implications for security, and difference from jailbreaking.

- [ ] **Storage:** Know internal vs. **external storage**, **app-specific storage**, and permission implications.

**iOS Fundamentals:**

- [ ] **IPA Structure:** Understand **IPA format, Mach-O binaries, Info.plist**, and provisioning profiles.

- [ ] **iOS Security Model:** Learn **code signing**, **Secure Enclave**, **Data Protection**, and **sandbox restrictions**.

- [ ] **Jailbreaking:** Understand what **jailbreaking** means and implications for device security.

- [ ] **iOS Permissions:** Know **privacy labels**, **tracking prevention**, and **privacy controls**.

**Cross-Platform Basics:**

- [ ] **Certificate Pinning:** Understand why apps implement **SSL/TLS certificate pinning** and its purpose.

- [ ] **Biometric Auth:** Know **fingerprint/face recognition** APIs and their security model.

- [ ] **Keystore:** Understand **secure key storage**, **hardware-backed keystores**, and credential management.

- [ ] **Jailbreak Detection Bypass:** Patch **integrity checks**, hide **Cydia/Sileo**, use **A-Bypass/Shadow** hooks.

- [ ] **SSL Pinning Bypass:** Use **SSL Kill Switch, Burp CA**, or **Frida scripts** to intercept encrypted traffic.

- [ ] **Keychain Extraction:** Dump **keychain items** on jailbroken devices using **keychain_dumper/Clutch**.

- [ ] **Runtime Manipulation:** Hook **Objective-C methods** with **Frida/Cycript** for dynamic analysis.

**Mobile Device Management (MDM) & Enterprise:**

- [ ] **MDM Bypass:** Exploit **enrollment gaps**, remove **configuration profiles**, escape **DEP/supervised mode**.

- [ ] **Enterprise App Abuse:** Sideload **unsigned apps** via **enterprise certificates**, exploit **provisioning misconfigs**.

- [ ] **Mobile Malware Delivery:** Craft **phishing campaigns** targeting **mobile users**, abuse **SMS/MMS** for payload delivery.

---

### **Stage 6: Application Suites & Cloud Vectors**

_Goal: Understand software stacks and cloud computing basics._

**Office & Document Exploits:**

- [ ] **VBA & XLM 4.0 Macros:** Build payloads, sign macros, and abuse **template injection (remote DOTM)**.

- [ ] **DDE & Template Abuse:** Trigger code via **DDEAUTO**, external templates, and **Follina-style** URL template fetches.

- [ ] **OneNote/PDF/Embedded Files:** Weaponize **OneNote pages, PDF JS**, and embedded **LNK/ISO/IMG** loaders; understand **MOTW** bypasses.

- [ ] **Protected View/ATP Evasion:** Study **mark-of-the-web**, **protected view**, and common sandbox evasion tricks.

**Email Client Abuse:**

- [ ] **Outlook Rules & Forms:** Create **client-side rules** for auto-forwarding/persistence and malicious **custom forms/add-ins**.

- [ ] **MAPI/Extended MAPI:** Leverage **Redemption/Outlook interop** for covert access and exfil.

**Cloud & SaaS Persistence:**

- [ ] **OAuth Consent Phishing:** Steal **refresh tokens** via malicious app registration; understand **scopes** and consent screens.

- [ ] **Device Code & App Passwords:** Abuse **device code flow**, **legacy auth**, and **app passwords** for bypassing MFA.

- [ ] **Conditional Access Gaps:** Identify mis-scoped policies, **trusted locations**, and bypass paths.

- [ ] **Shared Mailboxes & Delegation:** Maintain access via **delegate rights** and mailbox rules.

**Data Exfiltration & Covert Channels:**

- [ ] **Cloud Storage APIs:** Use **Drive/OneDrive/Dropbox** APIs with **service accounts/tokens**; rotate tokens for persistence.

- [ ] **Covert Channels:** Exfil via **DNS-over-HTTPS**, **S3 pre-signed URLs**, **steganography in images/docs**, and throttled uploads.

- [ ] **Egress Controls:** Understand common **CASB/SWG** controls and how to mimic normal user traffic patterns.

**Logging, Forensics, and Cleanup:**

- [ ] **O365/Azure Audit:** Know where **Sign-In, Audit, Unified Audit** logs land; plan for artifacts.

- [ ] **Google Workspace Logs:** Review **Admin/Drive/Access Transparency** for trace evidence.

- [ ] **Artifact Hygiene:** Track **recent documents, registry keys, LNK files**, and clear only when within ROE.

---

### **Stage 7: Programming & Exploit Development Languages**

_Goal: Build the coding foundation required to write custom tools, exploits, and undetected payloads._

**Python (Automation & Scripting):**

- [ ] **Core Language:** Master **data types, control flow, functions, OOP, file I/O, exception handling**, and **virtual environments (venv/pip)**.

- [ ] **Security Libraries:** Learn **socket, requests, scapy, pwntools, paramiko, impacket, beautifulsoup** for network interaction, exploit development, and scraping.

- [ ] **Automation Use Cases:** Script **port scanners, brute-forcers, web scrapers, log parsers, payload generators**, and **API interaction tools**.

- [ ] **Exploit Prototyping:** Use Python for **rapid PoC development**, **fuzzing harnesses**, and **custom C2 implant logic**.

**JavaScript & Node.js (Web & API Security):**

- [ ] **Core Language:** Master **ES6+ syntax, async/await, Promises, closures, prototypal inheritance, DOM manipulation**, and **event-driven architecture**.

- [ ] **Node.js Runtime:** Understand **npm ecosystem, module system (CommonJS/ESM), Express.js**, and **server-side JavaScript** for building and auditing web applications.

- [ ] **Web Security Context:** Learn **DOM-based XSS, prototype pollution, client-side injection, postMessage abuse**, and **WebSocket security** — JavaScript is the language of the web attack surface.

- [ ] **API Interaction:** Use **fetch API, Axios, Puppeteer/Playwright** for **automated web scraping, API fuzzing, headless browser automation**, and **browser-based exploit delivery**.

- [ ] **AI Interface Relevance:** Understand that modern AI model interfaces (**ChatGPT, Gemini, Claude**) are delivered via **JavaScript web applications** — fluency is essential for auditing these frontends.

**C (System-Level & Exploit Development):**

- [ ] **Core Language:** Master **pointers, memory allocation (malloc/free), structs, arrays, strings, bitwise operations**, and **compilation (gcc/clang)**.

- [ ] **System Programming:** Understand **syscalls, file descriptors, process creation (fork/exec), signal handling**, and **shared memory/IPC**.

- [ ] **Exploit Development Foundation:** Write **buffer overflow exploits, shellcode, egghunters**, and understand **stack frame layout at the C level**.

- [ ] **Windows C Development:** Use **Win32 API (CreateProcess, VirtualAlloc, WriteProcessMemory)** for **process injection, DLL loading, and token manipulation**.

- [ ] **Linux C Development:** Interact with **POSIX APIs, /proc filesystem, ptrace**, and **LD_PRELOAD hooking** for rootkit/implant development.

**C++ (Performance-Critical Tooling):**

- [ ] **Core Language:** Understand **classes, templates, STL containers, smart pointers, RAII**, and how C++ extends C for structured exploit frameworks.

- [ ] **Tool Development:** Build **custom implants, packers, crypters**, and **network tools** requiring performance and low-level control.

- [ ] **Reverse Engineering Context:** Read and understand **C++ compiled binaries** (vtables, name mangling, exception handling) during **static analysis with Ghidra/IDA**.

**C# & .NET (Windows API & Offensive Tooling):**

- [ ] **Core Language:** Master **C# syntax, .NET runtime (CLR), namespaces, assemblies, NuGet packages**, and **Visual Studio workflow**.

- [ ] **Windows API Interaction:** Use **P/Invoke and D/Invoke** to call **native Win32 APIs** from managed code for **process injection, token theft, registry manipulation**.

- [ ] **Offensive .NET Tooling:** Understand tools built in C# like **SharpHound, Rubeus, Seatbelt, SharpUp, Certify** — and how to **modify/recompile** them to evade signatures.

- [ ] **In-Memory Execution:** Master **.NET assembly loading (Assembly.Load), reflection, and inline execution** to run offensive tools without dropping files to disk.

- [ ] **AMSI/ETW Bypass:** Understand how **.NET interacts with AMSI (Antimalware Scan Interface)** and **ETW (Event Tracing for Windows)** and techniques to patch or disable them.

**Assembly (Shellcode & Low-Level Exploitation):**

- [ ] **x86/x64 Assembly:** Develop working fluency in **MOV, PUSH, POP, CALL, JMP, INT, SYSCALL** and understand **calling conventions (cdecl, stdcall, fastcall, System V AMD64)**.

- [ ] **Shellcode Writing:** Craft **position-independent shellcode** for **reverse shells, bind shells, staged loaders** avoiding null bytes and bad characters.

- [ ] **Disassembly Reading:** Confidently read **disassembled output** in **Ghidra, IDA Pro, radare2** to identify vulnerabilities and understand compiled logic.

**Bash & PowerShell (Operational Scripting):**

- [ ] **Bash Mastery:** Script **recon pipelines, log parsing, cron automation, SSH key management**, and **iptables/nftables rule generation** on Linux.

- [ ] **PowerShell Mastery:** Script **AD enumeration, WMI queries, registry operations, service management**, and **remote execution (Invoke-Command, Enter-PSSession)**.

- [ ] **Offensive PowerShell:** Understand **PowerShell download cradles, AMSI bypass, constrained language mode escape**, and **script block logging evasion**.

- [ ] **Cross-Platform Scripting:** Use **Python or Bash** for Linux targets and **PowerShell or C#** for Windows targets; maintain fluency in both ecosystems.

---

<a id="toc-part-2-networking-fundamentals"></a>
## Part 2: Networking Fundamentals

### Layer 1: Physical (The Hardware Surface)

**Transmission Media & Cabling:**

- [ ] **Copper Cables:** Master **UTP, STP, and Coaxial** cables; understand **crosstalk**, **attenuation**, and **impedance**.

- [ ] **Fiber Optics:** Learn **Single-Mode (SMF)** vs. **Multi-Mode (MMF)**; understand **signal decay** and **dispersion**.

- [ ] **Wireless Transmission:** Master **RF propagation**, **antenna types**, **dBm measurements**, and **signal strength (RSSI)**.

- [ ] **Cable Standards:** Know **Cat5e, Cat6, Cat6A, Cat7** specifications and maximum distances.

**Network Topologies & Layout:**

- [ ] **Star Topology:** Central switch/hub; understand single point of failure and ease of management.

- [ ] **Ring Topology:** Sequential device connections; understand token-passing mechanisms (Token Ring).

- [ ] **Mesh Topology:** Full or partial redundancy; understand high availability and bandwidth costs.

- [ ] **Bus Topology:** Shared medium (legacy); understand collision domains and termination requirements.

- [ ] **Hybrid Topologies:** Understand modern mixed approaches combining multiple topology types.

**Wireless Standards & Frequencies:**

- [ ] **NFC (Near Field Communication):** 13.56 MHz, short range; understand **Type 1, 2, 3, 4 tags**.

- [ ] **Bluetooth:** 2.4 GHz ISM band; master **BLE (1 Mbps), Classic (3 Mbps), and Bluetooth 5.x speeds**.

- [ ] **WiFi (802.11):** Master **802.11a/b/g/n/ac/ax/be**; understand channel widths (20/40/80/160 MHz).

- [ ] **Cellular (4G/5G):** Understand **frequency bands**, **spectrum allocation**, and **base station architecture**.

- [ ] **Infrared (IR):** Understand line-of-sight requirements and usage in IoT/remote controls.

**Hardware Components & Connectors:**

- [ ] **RJ45 Connectors:** Understand **T568A/T568B wiring standards** and pin assignments.

- [ ] **Network Interface Cards (NICs):** Master **MAC addresses**, **promiscuous mode**, and **driver attacks**.

- [ ] **Repeaters & Hubs:** Understand Layer 1 devices and collision domain expansion.

- [ ] **Transceivers & Converters:** Master **SFP, QSFP, and media converters** for heterogeneous networks.

- [ ] **Power over Ethernet (PoE):** Understand **PoE (802.3af - 15.4W), PoE+ (802.3at - 25.5W), PoE++ (802.3bt - 51-71W)** standards for powering **IP phones, APs, cameras** over Ethernet.

**Network Architecture & Topology Designs:**

- [ ] **Two-Tier (Collapsed Core):** Understand **Access + Distribution/Core** combined design for small-to-medium networks.

- [ ] **Three-Tier (Hierarchical):** Master **Access, Distribution, Core** layers for scalable enterprise networks.

- [ ] **Spine-Leaf Architecture:** Understand modern **data center topology** with **equal-cost paths, low latency, east-west traffic optimization**.

- [ ] **SOHO (Small Office/Home Office):** Know typical **single router/switch** setups with integrated wireless.

- [ ] **On-Premises vs Cloud:** Understand **physical datacenter vs cloud-hosted** infrastructure trade-offs.

- [ ] **WAN Architecture:** Master **hub-and-spoke, partial mesh, full mesh** WAN designs.

**Physical Layer Security & Attacks:**

- [ ] **Cable Interception:** Understand **fiber tapping**, **copper snooping**, and physical plant security.

- [ ] **Signal Jamming:** Learn frequency jamming techniques for wireless networks.

- [ ] **Rogue Access Points:** Understand **evil twin attacks** and hardware spoofing.

- [ ] **Physical Tampering:** Master detection of splitters, taps, and modifications.

---

### Layer 2: Data Link (The Local Target)

**MAC Addressing & Frame Structure:**

- [ ] **MAC Address Format:** Understand **OUI (Organizationally Unique Identifier)** and manufacturer identification.

- [ ] **Unicast vs. Multicast:** Master **FF:FF:FF:FF:FF:FF** (broadcast) and multicast MAC ranges.

- [ ] **Frame Structure:** Understand **Ethernet frames**, **VLAN tags (802.1Q)**, and **frame size (MTU)** constraints.

- [ ] **MAC Address Spoofing:** Learn tools like **macchanger** and implications for network security.

**ARP Protocol & Attacks:**

- [ ] **ARP Cache Mechanics:** Understand how **ARP tables** map IP addresses to MAC addresses.

- [ ] **ARP Spoofing:** Master **ARP Cache Poisoning** to position yourself for MITM attacks.

- [ ] **Gratuitous ARP:** Understand unsolicited ARP replies and their use in attacks.

- [ ] **ARP Scanning:** Learn to enumerate active hosts without traditional ICMP pings.

- [ ] **ARP Defense:** Understand **static ARP entries**, **ARP inspection (DAI)**, and detection mechanisms.

**VLAN & Virtual Networks:**

- [ ] **VLAN Tagging (802.1Q):** Master the 12-bit VLAN ID and priority bits.

- [ ] **VLAN Hopping:** Execute **double-tagging attacks** via trunk misconfigurations.

- [ ] **VLAN Segmentation:** Design and bypass network segmentation strategies.

- [ ] **Management VLANs:** Understand dangers of misconfigured management interfaces.

- [ ] **Private VLANs:** Learn secondary VLAN restrictions and bypass techniques.

**Switch Architecture & Attacks:**

- [ ] **CAM Tables:** Understand **Content Addressable Memory** and port learning mechanisms.

- [ ] **CAM Table Flooding:** Learn to force a switch into "hub mode" and flood traffic.

- [ ] **MAC Flooding Tools:** Master **macof** and similar attack tools.

- [ ] **Port Security:** Understand **sticky MAC**, **MAC aging**, and bypass vectors.

- [ ] **Spanning Tree Protocol (STP):** Understand BPDU manipulation and loop prevention bypass.

**Layer 2 Security Features:**

- [ ] **Port Security:** Configure **maximum MAC addresses, violation modes (protect/restrict/shutdown)**, and **sticky MAC learning**.

- [ ] **DHCP Snooping:** Enable **DHCP snooping** to build a trusted **IP-MAC binding table** and block rogue DHCP servers.

- [ ] **Dynamic ARP Inspection (DAI):** Configure **DAI** to validate **ARP packets** against the DHCP snooping database; prevent ARP spoofing.

- [ ] **IP Source Guard:** Understand **IPSG** to prevent **IP spoofing** by filtering traffic based on DHCP snooping bindings.

**Rapid PVST+ Spanning Tree Protocol:**

- [ ] **Root Bridge Election:** Understand **primary/secondary root bridge** configuration using **priority values (0-61440 in 4096 increments)**.

- [ ] **Port States:** Master **Discarding, Learning, Forwarding** states in Rapid PVST+.

- [ ] **Port Roles:** Understand **Root Port, Designated Port, Alternate Port, Backup Port**.

- [ ] **PortFast:** Configure **PortFast** on access ports to bypass **listening/learning** states; skip on trunk ports.

- [ ] **BPDU Guard:** Enable **BPDU Guard** to shutdown ports receiving **BPDUs** (protects against rogue switches).

- [ ] **BPDU Filter:** Understand **BPDU Filter** to suppress **BPDU transmission/reception** on ports.

- [ ] **Root Guard:** Configure **Root Guard** to prevent **unauthorized root bridge** takeover.

- [ ] **Loop Guard:** Enable **Loop Guard** to prevent **alternate/root ports** from becoming designated due to **unidirectional link failure**.

**Network Scope & Physical Reach:**

- [ ] **PAN (Personal Area Network):** Bluetooth/NFC range (meters); personal device networks.

- [ ] **LAN (Local Area Network):** Ethernet/WiFi; typically single building or campus.

- [ ] **WLAN (Wireless LAN):** 802.11 networks; understand coverage, roaming, and handoff.

- [ ] **MAN (Metropolitan Area Network):** City-level coverage; typically WiMAX or leased lines.

- [ ] **WAN (Wide Area Network):** Global reach via ISP connections, VPNs, and dedicated circuits.

**Layer 2 Protocols & Analysis:**

- [ ] **Spanning Tree Protocol (STP):** Understand topology changes and BPDU manipulation.

- [ ] **Link Aggregation (802.3ad):** Master **EtherChannel** and multi-link trunking.

- [ ] **LLDP (Link Layer Discovery Protocol):** Learn device discovery and topology mapping.

- [ ] **Packet Capture & Analysis:** Master **Wireshark** for Layer 2 frame analysis.

**Cisco Discovery Protocols:**

- [ ] **CDP (Cisco Discovery Protocol):** Configure and verify **CDP** for discovering **directly connected Cisco devices**; understand security risks.

- [ ] **LLDP (Link Layer Discovery Protocol):** Configure **LLDP** as vendor-neutral alternative to CDP; understand **LLDP-MED** for VoIP.

- [ ] **CDP/LLDP Security:** Understand **information disclosure** risks and when to **disable on edge ports**.

**EtherChannel & Link Aggregation:**

- [ ] **LACP (802.3ad):** Configure **Link Aggregation Control Protocol** with **active/passive** modes for dynamic bundling.

- [ ] **PAgP (Port Aggregation Protocol):** Understand Cisco proprietary **PAgP** with **desirable/auto** modes.

- [ ] **EtherChannel Load Balancing:** Configure **src-mac, dst-mac, src-dst-ip, src-dst-port** load distribution algorithms.

- [ ] **Layer 2 vs Layer 3 EtherChannel:** Understand **L2 EtherChannel (switch ports)** vs **L3 EtherChannel (routed ports)**.

**Cisco Wireless Architecture:**

- [ ] **Autonomous AP Mode:** Understand **standalone APs** with individual management (legacy).

- [ ] **Lightweight AP (LAP) Mode:** Master **CAPWAP tunneling** to **Wireless LAN Controller (WLC)** for centralized management.

- [ ] **FlexConnect (H-REAP):** Understand **hybrid mode** allowing **local switching** at branch sites with **central authentication**.

- [ ] **WLC Deployment:** Know **centralized, distributed, cloud-based** WLC architectures.

- [ ] **WLAN Physical Infrastructure:** Understand **AP connections (access/trunk ports), WLC uplinks, LAG (Link Aggregation)** for redundancy.

---

### Layer 3: Network (The Routing Logic)

**IP Addressing & Subnetting:**

- [ ] **IPv4 Addressing:** Master **dotted-decimal notation** and **binary conversion** for IP blocks.

- [ ] **Public vs. Private Space:** Know **10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16** and reserved ranges.

- [ ] **Subnet Masks:** Calculate **CIDR notation** (/8, /16, /24, /25, /26, /30, /31, /32).

- [ ] **Wildcard Masks:** Understand inverse notation for **ACL and routing** configurations.

- [ ] **Host Boundaries:** Calculate first host, last host, and broadcast address in any subnet.

- [ ] **IPv6 Addressing:** Master **IPv6 compression**, **link-local**, **ULA**, and **multicast** addressing.

- [ ] **IPv6 Shorthand:** Understand **::1, ::/128, fe80::/10** and common IPv6 patterns.

**Routing & Path Selection:**

- [ ] **Routing Tables:** Understand **route entries**, **metric**, and **next-hop** selection.

- [ ] **Static Routing:** Configure and exploit hardcoded route entries.

- [ ] **Default Route (0.0.0.0/0):** Understand the catch-all and its role in exfiltration.

- [ ] **Route Summarization:** Aggregate multiple subnets into single routing entries.

- [ ] **Longest Prefix Match:** Understand how routers select the most specific route.

**Dynamic Routing Protocols:**

- [ ] **OSPF (Open Shortest Path First):** Master **Areas, LSA, SPF algorithm**, and DR/BDR election.

- [ ] **OSPFv2 Configuration:** Configure **single-area OSPF**, understand **neighbor adjacencies, point-to-point vs broadcast networks**.

- [ ] **OSPF DR/BDR Election:** Understand **Designated Router/Backup DR** election on **broadcast/NBMA networks** based on **priority and Router ID**.

- [ ] **OSPF Router ID:** Configure and verify **Router ID** selection (manual > loopback > highest IP).

- [ ] **BGP (Border Gateway Protocol):** Understand **AS numbers, path vectors, and route redistribution**.

- [ ] **EIGRP (Enhanced Interior Gateway Routing Protocol):** Master Cisco proprietary **DUAL algorithm** and metrics.

- [ ] **RIP (Routing Information Protocol):** Understand legacy distance-vector protocol and 15-hop limit.

- [ ] **Routing Protocol Vulnerabilities:** Learn **route injection, spoofing, and redistribution attacks**.

**First Hop Redundancy Protocols (FHRP):**

- [ ] **HSRP (Hot Standby Router Protocol):** Understand Cisco proprietary **virtual IP/MAC**, **active/standby routers**, and **priority/preemption**.

- [ ] **VRRP (Virtual Router Redundancy Protocol):** Learn industry-standard **VRRP** with **master/backup** election.

- [ ] **GLBP (Gateway Load Balancing Protocol):** Understand Cisco **GLBP** for **load sharing** across multiple gateways.

- [ ] **FHRP Purpose:** Know FHRP provides **default gateway redundancy** to prevent **single point of failure** for end hosts.

**NAT & PAT Mechanics:**

- [ ] **Static NAT:** Understand 1:1 IP mapping for incoming connections.

- [ ] **Dynamic NAT:** Learn pool-based translation with overloading.

- [ ] **PAT (Port Address Translation):** Master how thousands of internal hosts share one public IP.

- [ ] **NAT Bypass:** Use **port forwarding, UPnP, and SSDP** to bypass internal restrictions.

- [ ] **NAT Traversal:** Understand **STUN, TURN**, and techniques for P2P across NAT boundaries.

- [ ] **NAT Vulnerabilities:** Learn **ARP spoofing behind NAT** and dual-stack exploitation.

**Gateway & Border Security:**

- [ ] **Default Gateway:** Master the primary exit point for all non-local traffic.

- [ ] **Gateway Discovery:** Use **DHCP analysis** and **traceroute** to identify gateways.

- [ ] **Gateway Vulnerabilities:** Exploit **ICMP redirects** and **gateway impersonation**.

- [ ] **Firewall Positioning:** Understand **edge protection** and **DMZ** designs.

- [ ] **Exit Points:** Identify alternative exfiltration paths (secondary gateways, VPNs, proxies).

**ICMP & Diagnostics:**

- [ ] **Ping (Echo Request/Reply):** Understand ICMP type 8/0 and reachability testing.

- [ ] **Traceroute (TTL Exceeded):** Master hop-by-hop path discovery and **UDP/TCP variants**.

- [ ] **ICMP Redirects:** Learn type 5 redirects used in **MITM attacks**.

- [ ] **ICMP Tunneling:** Master data exfiltration via ICMP payloads.

- [ ] **ICMP Filtering:** Understand **ping blocking** and defensive implications.

---

### Layer 4: Transport (The Reliability Layer)

**TCP Protocol Mechanics:**

- [ ] **TCP Header Structure:** Master **source/destination ports, sequence numbers, acknowledgments**.

- [ ] **TCP Flags:** Understand **SYN, ACK, FIN, RST, PSH, URG** and their roles in connection states.

- [ ] **Three-Way Handshake:** Master **SYN, SYN-ACK, ACK** sequence for connection establishment.

- [ ] **TCP State Machine:** Understand **LISTEN, SYN_SENT, SYN_RECEIVED, ESTABLISHED, FIN_WAIT, CLOSE_WAIT, CLOSED**.

- [ ] **Window Scaling:** Master **TCP window size** and **flow control** mechanisms.

- [ ] **TCP Options:** Understand **MSS, SACK, Timestamps, and Window Scaling** negotiation.

**UDP Protocol & Characteristics:**

- [ ] **UDP Header:** Understand lightweight **source port, destination port, length, checksum**.

- [ ] **Connectionless Nature:** Learn stateless operation and lack of delivery guarantees.

- [ ] **UDP Use Cases:** Master applications for **DNS, DHCP, NTP, SNMP, RTP** (real-time media).

- [ ] **UDP Flooding:** Understand **bandwidth attacks** and amplification vectors.

**Port & Service Enumeration:**

- [ ] **Common Ports:** Memorize **SSH (22), RDP (3389), DNS (53), HTTP (80), HTTPS (443)**.

- [ ] **Mail Services:** Master **SMTP (25), POP3 (110), IMAP (143)** and secure variants.

- [ ] **Directory Services:** Understand **LDAP (389), Kerberos (88)** and **Active Directory** implications.

- [ ] **Database Ports:** Know **MySQL (3306), MSSQL (1433), PostgreSQL (5432), Oracle (1521)**.

- [ ] **Application Ports:** Understand **RPC (135), NetBIOS (139,445), VNC (5900)** and exploitation risks.

**Network Scanning & Reconnaissance:**

- [ ] **Nmap TCP Scan:** Master **-sS (SYN), -sT (connect), -sA (ACK)** scan types.

- [ ] **Nmap UDP Scan:** Understand **-sU** and **ICMP unreachable** responses.

- [ ] **FIN, NULL, Xmas Scans:** Learn **stealth techniques** and firewall evasion via flag combinations.

- [ ] **ACK Scan:** Understand mapping of **filtered vs. unfiltered** ports (firewall rules).

- [ ] **Idle/Zombie Scan:** Master source IP spoofing using **idle hosts** as proxy.

- [ ] **Timing Templates:** Understand **-T0 (paranoid) through -T5 (insane)** for evasion vs. speed.

**TCP/UDP Vulnerabilities & Attacks:**

- [ ] **SYN Flood:** Understand **half-open connections** and resource exhaustion.

- [ ] **TCP Sequence Prediction:** Learn **session hijacking** via predicted sequence numbers.

- [ ] **RST Injection:** Master connection termination attacks.

- [ ] **ACK Flooding:** Understand **bandwidth amplification** and detection evasion.

- [ ] **Port Knocking:** Learn **knock-based firewall bypass** sequences.

- [ ] **Source Port Spoofing:** Understand **DNS amplification** and **NTP reflection** attacks.

**Transport Layer Filtering:**

- [ ] **Stateless Firewalls:** Understand **ACL-based blocking** and bypass via fragmentation.

- [ ] **Stateful Firewalls:** Learn **connection state tracking** and evasion techniques.

- [ ] **IDS/IPS Evasion:** Master **packet fragmentation, timing delays, and payload obfuscation**.

---

### Layers 5-7: Application & Session (The Payload)

**DNS Protocol & Exploitation:**

- [ ] **DNS Record Types:** Master **A, AAAA, MX, CNAME, NS, SOA, TXT, SPF, DKIM**.

- [ ] **DNS Query Process:** Understand **recursive vs. iterative** queries and resolver chain.

- [ ] **DNS Caching:** Learn **TTL (Time-To-Live)** and cache timing implications.

- [ ] **DNS Poisoning:** Master **cache poisoning** to redirect traffic to attacker IPs.

- [ ] **DNS Amplification:** Understand **reflection attacks** using open resolvers.

- [ ] **DNS Exfiltration:** Learn data extraction via **DNS queries** (stealth covert channel).

- [ ] **DNSSEC:** Understand digital signing and validation of DNS responses.

- [ ] **DNS Tools:** Master **nslookup, dig, host** for reconnaissance and manipulation.

**DHCP Protocol & Attacks:**

- [ ] **DHCP Lease Cycle:** Understand **DISCOVER, OFFER, REQUEST, ACK** sequence.

- [ ] **DHCP Options:** Master **Option 3 (gateway), Option 6 (DNS), Option 15 (domain)**.

- [ ] **DHCP Starvation:** Learn **DHCP exhaustion** attacks to kill availability.

- [ ] **Rogue DHCP Server:** Understand **DHCP spoofing** to distribute attacker IPs as gateway.

- [ ] **DHCP Snooping:** Learn **DHCP filtering** and detection of rogue servers.

- [ ] **DHCP Relay:** Understand across-subnet DHCP and manipulation vectors.

**IP Services Configuration:**

- [ ] **DHCP Server Configuration:** Configure **Cisco IOS DHCP server** with **pools, exclusions, default-router, dns-server, lease time**.

- [ ] **DHCP Client Configuration:** Configure interfaces as **DHCP clients** using **ip address dhcp**.

- [ ] **DHCP Relay Agent:** Configure **ip helper-address** to relay **DHCP requests** across subnets to remote DHCP server.

- [ ] **DNS Role in Networks:** Understand **DNS resolution process**, **forward/reverse lookups**, and **recursive vs iterative queries**.

- [ ] **DNS Configuration:** Configure **ip name-server** and **ip domain-lookup** for hostname resolution on network devices.

**NTP (Network Time Protocol):**

- [ ] **NTP Purpose:** Understand **time synchronization** importance for **logging, authentication, certificates, troubleshooting**.

- [ ] **NTP Hierarchy:** Master **Stratum levels** (0-15), where **Stratum 0 = atomic clock**, **Stratum 1 = primary**, etc.

- [ ] **NTP Client Configuration:** Configure devices as **NTP clients** using to sync time.

- [ ] **NTP Server Configuration:** Configure router as **NTP server** using **ntp master** for internal time distribution.

- [ ] **NTP Authentication:** Implement **NTP authentication** using **keys** to prevent time manipulation attacks.

**SNMP (Simple Network Management Protocol):**

- [ ] **SNMP Architecture:** Understand **Manager-Agent** model, **MIB (Management Information Base)**, and **OID** hierarchy.

- [ ] **SNMP Versions:** Know **SNMPv1 (insecure), SNMPv2c (community strings), SNMPv3 (authentication & encryption)**.

- [ ] **SNMP Operations:** Master **GET, GET-NEXT, GET-BULK, SET, TRAP, INFORM** message types.

- [ ] **SNMP Community Strings:** Understand **read-only (RO)** and **read-write (RW)** community strings as passwords.

- [ ] **SNMP in Network Operations:** Use SNMP for **monitoring interface status, bandwidth utilization, CPU/memory, configuration backup**.

- [ ] **SNMP Security Risks:** Understand **community string exposure, SNMP enumeration, unauthorized config changes**.

**Syslog (System Logging):**

- [ ] **Syslog Facilities:** Understand **facility codes** (local0-7, kern, user, mail, daemon, auth, etc.) for message categorization.

- [ ] **Syslog Severity Levels:** Master **0-7 severity** (0=Emergency, 1=Alert, 2=Critical, 3=Error, 4=Warning, 5=Notice, 6=Informational, 7=Debug).

- [ ] **Syslog Configuration:** Configure `logging host <ip>`, `logging trap <level>`, and `logging source-interface`.

- [ ] **Syslog vs Local Logging:** Understand **logging buffer, console, monitor** vs **centralized syslog server**.

- [ ] **Syslog for Security:** Use syslog for **incident response, forensics, compliance, anomaly detection**.

**TFTP/FTP File Transfer:**

- [ ] **TFTP (Trivial File Transfer Protocol):** Understand **UDP port 69**, **no authentication**, simple operation.

- [ ] **TFTP Use Cases:** Use for **IOS upgrades, config backup/restore, boot image loading** on Cisco devices.

- [ ] **TFTP Commands:** Master **copy running-config tftp:**, **copy tftp: flash:**, **boot system tftp:**.

- [ ] **FTP (File Transfer Protocol):** Understand **TCP ports 20/21**, **authentication**, **active vs passive mode**.

- [ ] **FTP vs TFTP:** Know **TFTP = simple, no auth, UDP** vs **FTP = complex, authenticated, TCP**.

- [ ] **Secure Alternatives:** Prefer **SCP, SFTP** over **TFTP/FTP** for secure file transfers.

**NAT Configuration:**

- [ ] **Static NAT Configuration:** Configure `ip nat inside source static <local-ip> <global-ip>` for 1:1 mapping.

- [ ] **Dynamic NAT with Pools:** Configure `ip nat pool` and `ip nat inside source list <acl> pool <name>`.

- [ ] **PAT (NAT Overload):** Configure `ip nat inside source list <acl> interface <outside-int> overload`.

- [ ] **NAT Inside/Outside:** Apply **ip nat inside** and **ip nat outside** to appropriate interfaces.

- [ ] **NAT Verification:** Use **show ip nat translations**, **show ip nat statistics** for troubleshooting.

**QoS (Quality of Service) Fundamentals:**

- [ ] **QoS Purpose:** Understand managing **bandwidth, latency, jitter, packet loss** for critical applications (VoIP, video).

- [ ] **Classification:** Identify and **mark traffic** based on **Layer 2 (CoS), Layer 3 (DSCP/ToS), Layer 4 (ports), Layer 7 (application)**.

- [ ] **Marking:** Apply **DSCP values (0-63)**, **IP Precedence (0-7)**, or **802.1p CoS (0-7)** to packets for priority signaling.

- [ ] **Queuing:** Understand **FIFO, Priority Queuing (PQ), Weighted Fair Queuing (WFQ), Class-Based WFQ (CBWFQ), Low Latency Queuing (LLQ)**.

- [ ] **Congestion Management:** Use queuing to **schedule packet transmission** during congestion based on priority.

- [ ] **Congestion Avoidance:** Implement **Random Early Detection (RED/WRED)** to **drop lower-priority packets** before buffers fill.

- [ ] **Policing:** Enforce **rate limits** by **dropping or remarking** excess traffic immediately.

- [ ] **Shaping:** **Buffer excess traffic** and send later to smooth bursty traffic patterns.

- [ ] **Per-Hop Behavior (PHB):** Understand QoS actions applied at **each network device** along the path.

- [ ] **Trust Boundaries:** Know where to **trust/classify** markings (access layer) vs where to **enforce** (distribution/core).

**Authentication Protocols:**

- [ ] **Kerberos (Port 88):** Master **TGT, TGS, and mutual authentication** with Windows AD.

- [ ] **LDAP (Port 389):** Understand **directory queries** and **credential validation** against AD.

- [ ] **RADIUS (Port 1812):** Learn **shared secret** based remote authentication for dial-up/wireless.

- [ ] **TACACS+ (Port 49):** Understand **Cisco AAA** protocol with better encryption than RADIUS.

- [ ] **NTLM:** Master **challenge-response** authentication and hash passing attacks.

- [ ] **OAuth 2.0:** Understand **authorization code flow, tokens**, and **token theft** risks.

- [ ] **SAML:** Learn **XML-based** federated authentication and **assertion forgery**.

- [ ] **Identity Protection (NHI):** Hunt **service principals, app registrations, API keys, OAuth tokens**; classify **non-human identities** and guard **least privilege/rotation**.

**SSL/TLS & Encryption:**

- [ ] **TLS Handshake:** Master **ClientHello, ServerHello, key exchange, finished messages**.

- [ ] **Certificate Chain:** Understand **root, intermediate, end-entity** certificates and validation.

- [ ] **Cipher Suites:** Master **key exchange (RSA, DH, ECDH), encryption (AES, 3DES), hash (SHA)**.

- [ ] **SSL Stripping:** Learn **downgrade attacks** to force HTTP over HTTPS.

- [ ] **HSTS (HTTP Strict-Transport-Security):** Understand pinning to prevent SSL stripping.

- [ ] **Certificate Pinning:** Learn **public key / certificate pinning** in applications.

- [ ] **TLS Vulnerabilities:** Understand **Heartbleed, POODLE, BEAST, CRIME** and mitigation.

- [ ] **Perfect Forward Secrecy (PFS):** Master **ephemeral key exchange** to limit past compromise.

**HTTP Protocol & Web Attacks:**

- [ ] **HTTP Methods:** Understand **GET, POST, PUT, DELETE, PATCH, OPTIONS, HEAD**.

- [ ] **HTTP Headers:** Master **Host, User-Agent, Authorization, Cookie, X-Forwarded-For**.

- [ ] **Status Codes:** Know **2xx (success), 3xx (redirect), 4xx (client), 5xx (server)**.

- [ ] **Session Cookies:** Understand **HttpOnly, Secure, SameSite** flags and cookie theft.

- [ ] **HTTP/2 & HTTP/3:** Master **multiplexing, server push**, and new vulnerability surfaces.

- [ ] **REST APIs:** Understand **resource endpoints, authentication, rate limiting** bypass.

- [ ] **CORS (Cross-Origin Resource Sharing):** Master **preflight requests (OPTIONS), Access-Control-Allow-Origin headers, credentialed requests**, and how **CORS misconfigurations** enable **cross-origin data theft** from APIs and AI model endpoints.

- [ ] **WebSockets:** Understand **WebSocket handshake (HTTP Upgrade), persistent bidirectional channels**, and security implications — **cross-site WebSocket hijacking, origin validation bypass**, and use in **real-time AI streaming interfaces**.

**Session & Application Layer Attacks:**

- [ ] **Session Hijacking:** Steal cookies via **network sniffing, XSS, malware**.

- [ ] **Session Fixation:** Force victim into attacker-known session ID.

- [ ] **CSRF (Cross-Site Request Forgery):** Exploit **state-changing actions** without user knowledge.

- [ ] **SSRF (Server-Side Request Forgery):** Abuse **server trust** to access internal resources.

- [ ] **XXE (XML External Entity):** Parse **malicious XML** to read files or launch DOS.

- [ ] **Injection Attacks:** Understand **SQL, command, LDAP** injection for backend compromise.

- [ ] **Deserialization:** Learn **unsafe object unmarshaling** leading to RCE.

**VPN & Tunneling Protocols:**

- [ ] **IPSec (Layer 3):** Master **AH, ESP**, tunnel vs. transport modes, and key exchange.

- [ ] **GRE (Generic Routing Encapsulation):** Understand **stateless tunneling** and encapsulation.

- [ ] **OpenVPN (Layer 3/4):** Learn **SSL/TLS-based** VPN with UDP/TCP.

- [ ] **WireGuard:** Understand **lightweight, kernel-space** modern VPN protocol.

- [ ] **VPN Bypass:** Learn **DNS leaks, IPv6 leaks**, and split-tunneling exploitation.

**Network Device Management Access:**

- [ ] **Console Access:** Connect via **console cable (RJ45/USB)** using **9600 baud, 8N1** for out-of-band management.

- [ ] **Telnet (Port 23):** Understand **unencrypted** remote CLI access; avoid in production.

- [ ] **SSH (Port 22):** Configure **SSH version 2** for **encrypted** remote management; generate **RSA keys**, set **domain name**.

- [ ] **HTTP/HTTPS Management:** Access **web GUI** via **HTTP (80)** or **HTTPS (443)**; understand certificate warnings.

- [ ] **TACACS+ (Port 49):** Implement **centralized AAA** for **granular command authorization** and **full packet encryption**.

- [ ] **RADIUS (Port 1812/1813):** Use for **network access authentication** (802.1X, VPN, wireless); encrypts only password.

- [ ] **Cloud-Managed Networking:** Understand **Cisco Meraki, Cisco DNA Center** for **centralized cloud management** of distributed devices.

- [ ] **Local Password Security:** Configure **enable secret** (MD5), **username/password** (encrypted with **service password-encryption**).

- [ ] **Privilege Levels:** Understand **privilege levels 0-15** and **exec-timeout** for security.

**Wireless LAN GUI Configuration:**

- [ ] **WLAN Creation:** Create **SSID/WLAN** profiles via **WLC GUI** or standalone AP interface.

- [ ] **WLAN Security Settings:** Configure **WPA2-Personal (PSK)**, **WPA2-Enterprise (802.1X/RADIUS)**, **WPA3** authentication.

- [ ] **Pre-Shared Key (PSK):** Set **WPA2-PSK passphrase** (8-63 characters) for personal/small office WLANs.

- [ ] **QoS Profiles for WLAN:** Apply **QoS profiles** (Platinum, Gold, Silver, Bronze) to prioritize **voice, video, best-effort, background**.

- [ ] **Advanced WLAN Settings:** Configure **broadcast SSID, radio policies (802.11a/b/g/n/ac), client limits, session timeout**.

- [ ] **VLAN Assignment:** Map **WLAN to VLAN** for segmentation; configure **interface groups**.

- [ ] **FlexConnect Local Switching:** Enable for **local data switching** at branch APs with **central authentication**.

**Network Monitoring & Analysis:**

- [ ] **Packet Capture (tcpdump/Wireshark):** Master **filter syntax** and protocol dissection.

- [ ] **NetFlow/sFlow:** Understand **flow-based monitoring** for traffic patterns without full capture.

- [ ] **Proxy Servers:** Master **transparent, forward** proxies and **man-in-the-middle** positioning.

- [ ] **IDS/IPS Systems:** Understand **signature-based detection** and evasion techniques.

- [ ] **SIEM Concepts:** Learn **log aggregation, correlation**, and **alert tuning**.

---

### Lab Progression & Professional Development (2026 Red Team Focus)

_Goal: Move from local simulation to cloud-native networks using a "hack to root" mindset._

**Phase 1: Foundations (Simulation)** — Tools: **Cisco Packet Tracer, IP Calculator**

- [ ] Simple Connectivity: Two PCs + switch; verify **ping/basic reachability**.

- [ ] The "Phonebook": Stand up **local DNS**; resolve custom hostnames.

- [ ] Automatic Addressing: Configure **DHCP** to hand out IPs to multiple hosts.

- [ ] Subnetting Drills: Design **/24, /25, /26** subnets without online aids.

- [ ] VLAN Creation: Segment by department (e.g., HR, Sales) with **VLANs**.

**Phase 2: Tactical (Emulation & Packets)** — Tools: **GNS3, Wireshark, Nmap**

- [ ] Packet Analysis: Capture **TCP 3-way handshake + HTTP** in Wireshark.

- [ ] Routing: Build **static routes**, then **OSPF** for auto path discovery.

- [ ] Filtering: Apply **ACLs** to permit/deny specific traffic.

- [ ] NAT: Enable **source NAT** to exit a lab via one public IP.

- [ ] Inter-VLAN Routing: Use **router-on-a-stick** for isolated VLAN comms.

**Phase 3: Linux Muscle Memory**

- [ ] Discovery: Use **ip a, ss -tulpn, arp -a** to map interfaces/listeners/peers.

- [ ] Connectivity & Routing: Troubleshoot with **traceroute, nslookup, dig**.

- [ ] Remote Management: Practice **ssh user@host** and **scp** file moves.

- [ ] Firewall Basics: Block ports with **iptables/ufw**.

**Phase 4: Red Team Edge (Kali/Battle Tests)** — Tools: **Kali, Bettercap, Metasploit**

- [ ] Recon: Run **Nmap stealth scans (SYN) + version detection** on lab targets.

- [ ] MITM: Perform **ARP spoof** with **Bettercap/Ettercap** in a controlled lab.

- [ ] Protocol Exploitation: Enumerate/exploit **SMB/FTP/SSH** via **Metasploit** modules.

- [ ] VPN & Tunneling: Stand up **OpenVPN/IPsec**; practice **SSH tunnels** to bypass local firewalls.

**Phase 5: Cloud Networking (2026 Standard)** — Tools: **AWS/Azure Free Tier, Terraform**

- [ ] VPC Design: Build **public + private subnets** in **AWS or Azure**.

- [ ] IaC: Use **Terraform** to deploy web server + security group/NACL.

- [ ] Cloud Security: Configure **SGs/NACLs**, then adjust rules to test bypass paths.

- [ ] Scaling: Add a **load balancer** and spread traffic across multiple instances.

---

### Automation & Programmability

_Goal: Understand how automation transforms network operations and software-defined architectures._

**Automation Impact on Network Management:**

- [ ] **Why Automation:** Understand benefits of **consistency, speed, scale, reduced human error, version control** in network operations.

- [ ] **Traditional vs Modern:** Compare **manual CLI configuration** vs **API-driven automation, Infrastructure as Code (IaC)**.

- [ ] **Use Cases:** Master **bulk configuration, compliance auditing, automated backup/restore, zero-touch provisioning (ZTP)**.

- [ ] **DevOps for NetOps:** Understand **CI/CD pipelines, Git version control, testing** applied to network configs.

**Controller-Based & Software-Defined Networking:**

- [ ] **Traditional Networks:** Understand **distributed control plane** where each device makes forwarding decisions independently.

- [ ] **Controller-Based Networks:** Master **centralized control plane** with **Cisco DNA Center, SD-WAN, Meraki Dashboard**.

- [ ] **Software-Defined Architecture Components:**
  - [ ] **Control Plane:** Centralized **routing decisions, policy management** (moved to controller).
  - [ ] **Data Plane:** Distributed **packet forwarding** (remains on network devices).
  - [ ] **Separation Benefits:** Understand **policy abstraction, simplified management, rapid deployment**.

- [ ] **Underlay Network:** Physical infrastructure providing **IP connectivity** between devices.

- [ ] **Overlay Network:** Logical **tunnels (VXLAN, GRE, IPsec)** built over underlay for **segmentation and abstraction**.

- [ ] **Fabric Architecture:** Understand **SD-Access fabric** with **control, data, policy** planes unified.

**Northbound vs Southbound APIs:**

- [ ] **Southbound APIs:** Controller-to-device communication using **OpenFlow, NETCONF, RESTCONF, SNMP** to **program forwarding behavior**.

- [ ] **Northbound APIs:** Application-to-controller communication using **REST APIs** for **orchestration, management apps, custom automation**.

- [ ] **API Direction:** Remember **Southbound = down to devices**, **Northbound = up to applications**.

**AI & Machine Learning in Network Operations:**

- [ ] **Predictive AI:** Understand ML for **capacity planning, failure prediction, anomaly detection, traffic forecasting**.

- [ ] **Generative AI:** Use AI for **network design suggestions, configuration generation, natural language troubleshooting**.

- [ ] **AI-Driven Insights:** Leverage **Cisco DNA Assurance, ThousandEyes** for **proactive issue detection, root cause analysis**.

- [ ] **ML Use Cases:** Master **security threat detection, user experience monitoring, wireless optimization**.

**REST APIs & Data Encoding:**

- [ ] **REST (Representational State Transfer):** Understand stateless **client-server** architecture over **HTTP/HTTPS**.

- [ ] **HTTP Verbs/CRUD:** Master mapping:
  - [ ] **GET = Read** (retrieve resource)
  - [ ] **POST = Create** (add new resource)
  - [ ] **PUT/PATCH = Update** (modify existing resource)
  - [ ] **DELETE = Delete** (remove resource)

- [ ] **RESTful API Authentication:** Understand **Basic Auth, Token-based (Bearer), OAuth 2.0, API Keys**.

- [ ] **Response Codes:** Know **200 OK, 201 Created, 204 No Content, 400 Bad Request, 401 Unauthorized, 404 Not Found, 500 Server Error**.

- [ ] **JSON Data Encoding:** Understand **JSON structure** (objects, arrays, key-value pairs) as primary REST API data format.

- [ ] **JSON Components:** Recognize **{} = object, [] = array, "key": "value"** pairs, data types (string, number, boolean, null).

- [ ] **JSON vs XML:** Understand **JSON** is more lightweight and preferred for modern APIs.

**Configuration Management Tools:**

- [ ] **Ansible Capabilities:** Understand **agentless, YAML playbooks, SSH-based** automation for **network device configuration**.

- [ ] **Ansible Modules:** Recognize `ios_command`, `ios_config`, `nxos_*`, `eos_*` modules for vendor-specific automation.

- [ ] **Terraform Capabilities:** Understand **Infrastructure as Code (IaC)** with **declarative HCL syntax, state management**.

- [ ] **Terraform Providers:** Recognize **Cisco ACI, NSX, AWS VPC, Azure VNET** providers for network infrastructure.

- [ ] **Idempotency:** Understand both tools ensure **desired state** without duplicate changes on re-run.

- [ ] **Version Control Integration:** Know both integrate with **Git** for **configuration versioning and rollback**.

**Python for Network Automation (Foundation):**

- [ ] **Python Libraries:** Recognize **Netmiko, NAPALM, Paramiko** for SSH-based device management.

- [ ] **API Libraries:** Understand **requests library** for REST API interactions.

- [ ] **Data Parsing:** Use **json module** to parse API responses and **jinja2** for config templating.

- [ ] **Scripting Use Cases:** Automate **config backups, bulk changes, compliance checks, inventory collection**.

<a id="toc-part-3-cryptography"></a>
## Part 3: Cryptography

### **Stage 1: Core Concepts & Algorithms**

_Goal: Understand the mathematical tools available._

- [ ] **CIA Alignment:** Map your crypto goals to the **Understand CIA Triad** (Confidentiality = Encryption, Integrity = Hashing).

- [ ] **Asymmetric Mastery:** Define the roles of **Private vs Public Keys**: Public to Encrypt/Verify, Private to Decrypt/Sign.

- [ ] **Integrity Checks:** Implement **Hashing** (SHA-256) to verify data integrity and detect **False Positives/Negatives** in file transfers.

---

### **Stage 2: Secure Communication (Data in Transit)**

_Goal: Secure the pipe between two points._

- [ ] **Protocol Hardening:** Enforce **Secure Protocols** by disabling **SSL** (deprecated) and enforcing **TLS** 1.2/1.3.

- [ ] **Secure Transfer:** Replace cleartext protocols with encrypted alternatives: **FTP vs SFTP** (SSH-based) or **IPSEC** for VPNs.

- [ ] **Handshake Analysis:** Analyze the **Key Exchange** (Diffie-Hellman) within the **Understand Handshakes** process to ensure Forward Secrecy.

---

### **Stage 3: Identity & Trust (PKI)**

_Goal: Prove that you are who you say you are._

- [ ] **Infrastructure:** Deploy **PKI** to manage digital certificates, ensuring the validity of public keys.

- [ ] **Email Security:** Implement **S/MIME** to sign and encrypt corporate email, preventing **Phishing** and spoofing.

---

### **Stage 4: Data at Rest & Password Security**

_Goal: Secure stored data._

- [ ] **Disk Encryption:** Deploy **BitLocker, LUKS, FileVault** for full-disk encryption.

- [ ] **Password Storage:** Never store plaintext passwords; use **bcrypt, scrypt, Argon2** with **salting** to defeat rainbow tables.

- [ ] **Key Management:** Use **HSM, KMS (AWS KMS, Azure Key Vault)** for secure key storage and rotation.

- [ ] **Modern Hashing Profiles:** Standardize **Argon2id** (memory-hard) with tuned **memory (e.g., 64–256 MB), iterations, parallelism**, or **bcrypt** with current cost; prefer **password peppering** server-side and enforce **per-user salts**. Deprecate **MD5/SHA-1/SHA-256 for password storage** and legacy **PBKDF2-low-iteration** configs.

---

### **Stage 5: Cryptographic Attacks & Weaknesses**

_Goal: Understand how crypto fails._

- [ ] **Weak Algorithms:** Identify and avoid **MD5, SHA-1, DES, RC4** in production systems.

- [ ] **Implementation Flaws:** Understand **padding oracle, timing attacks, side-channel attacks** that break otherwise strong algorithms.

- [ ] **Key Management Failures:** Exploit **hardcoded keys, weak KDF, insecure storage** in applications.

- [ ] **Downgrade Attacks:** Force **SSL/TLS downgrade** to weaker ciphers or protocols.

- [ ] **Cryptanalysis:** Understand basics of **frequency analysis, known-plaintext attacks, chosen-plaintext attacks**.

### **Lab Progression**

_Goal: Turn crypto from vocabulary into observable behavior._

- [ ] **Hashing Lab:** Generate hashes for files, modify bytes, and prove integrity failure with SHA-256.
- [ ] **Password Storage Lab:** Compare unsalted hash, salted hash, bcrypt, and Argon2id behavior; document cracking cost differences.
- [ ] **TLS Handshake Lab:** Capture TLS 1.3 in Wireshark and identify ClientHello, ServerHello, certificate chain, cipher suite, and key exchange.
- [ ] **Certificate Lab:** Create a local CA, issue a server certificate, trust it in a lab client, then break trust by expiration/name mismatch.
- [ ] **Post-Quantum Awareness:** Document NIST PQC primitives such as ML-KEM and ML-DSA, hybrid deployment, and crypto-agility migration risk.
- [ ] **Move-On Gate:** You can explain what was encrypted, what was authenticated, what was signed, and what failed when trust broke.

---

<a id="toc-part-4-footprinting-and-reconnaissance"></a>
## Part 4: Footprinting and Reconnaissance

### **Phase 1: The "Ghost" Phase (Passive OSINT & Human Profiling)**

_Goal: Maximum data acquisition with zero target interaction._

- [ ] **Organizational Hierarchy:** Profile the **Audience** (Stakeholders, HR, Legal, Management) to understand who holds the keys and who is the weakest link.

- [ ] **Search Engine Hacking:** Use **Google Dorks** (`site:`, `filetype:`, `intitle:`) to find exposed documents and login portals.

- [ ] **Social Vector Mapping:** Scrape LinkedIn and professional sites to identify targets for **Phishing, Whishing, Whaling, or Smishing** based on reported tech stacks.

- [ ] **Physical Perimeter Assessment:** Evaluate the likelihood of **Shoulder Surfing, Tailgating, or Dumpster Diving** vulnerabilities.

- [ ] **Metadata & Leak Analysis:** Use **Wayback Machine** for historical paths and **GitHub/GitLab Dorking** for hardcoded API keys or internal naming conventions.

- [ ] **Domain & Ownership:** Perform **WHOIS Lookups** to identify registration dates, contact info, and associated subdomains.

- [ ] **Passive DNS & CT:** Pull **passive DNS** and **Certificate Transparency (crt.sh)** to surface shadow subdomains and SANs; cluster hosting/ASN/country.

- [ ] **Breach & Paste Monitoring:** Check **breach corpuses** (HIBP/Dehashed) and pastes/code search for leaked creds, API keys, or internal hostnames.

- [ ] **Mail Posture Recon:** Review **SPF/DMARC/DKIM** to assess spoofing risk and likely mail providers.

---

### **Phase 2: Semi-Passive Infrastructure Mapping**

_Goal: Querying third-party aggregators to see what the world already knows about them._

- [ ] **External Intel Scouring:** Query **VirusTotal, urlscan, any.run, Joe Sandbox, and urlvoid** for existing malware samples or documented domain behavior.

- [ ] **Third-Party Scans:** Use **Shodan & Censys** to find open ports, outdated services, and geographical distribution without scanning the target yourself.

- [ ] **Subdomain & DNS Enumeration:** Use **Sublist3r/Amass** for subdomains and check **DNS records** (MX, TXT, NS) to map mail providers and third-party integrations.

- [ ] **Protocol Audit:** Identify if the target is clinging to **Insecure Protocols** (FTP vs. SFTP, SSL vs. TLS).

- [ ] **WAF/CDN/TLS Fingerprinting:** Detect **WAF/CDN** fronting via **JA3/JA4, HTTP header quirks, TLS ALPN/HTTP2**, and favicon hashes.

- [ ] **VHost & Favicon Hunts:** Bruteforce **vhosts/domains** and use **favicon hash**/HTTP header diffs to find hidden apps.

---

### **Phase 3: Active Footprinting & Network Interrogation**

_Goal: Direct contact to map the live network fabric. Risk of detection is now ACTIVE._

- [ ] **Live Host Discovery:** Use **ping, arp, and hping** to identify which internal or external assets are actually breathing.

- [ ] **Network Path Analysis:** Use **tracert** to map the hops and identify **Perimeter vs. DMZ vs. Segmentation** boundaries.

- [ ] **Surgical Port Scanning:** Execute **Nmap Essentials** (starting with `-sS` stealth scans) to identify listening services and **OS Fingerprinting**.

- [ ] **Aggressive DNS Interrogation:** Use **nslookup and dig** to force the disclosure of hidden internal records or mail servers.

- [ ] **Web Content Discovery:** Run **ffuf or Gobuster** for directory brute-forcing and use **Wappalyzer** for technology profiling (CMS, frameworks, databases).

- [ ] **TLS Surface:** Harvest **cert SANs**, check **cipher/curve** support, **HTTP/2/ALPN** negotiation, and redirect/downgrade behavior.

- [ ] **Web Route Mapping:** Parse **robots.txt/sitemap.xml** and fuzz **parameters/paths** with status/length filters to uncover hidden routes.

---

### **Phase 4: Advanced Fingerprinting & Logic Analysis**

_Goal: Understand the defensive "brain" of the target._

- [ ] **Traffic Analysis:** If vantage is gained, use **Wireshark** to analyze **Packet Captures** and examine **Handshakes** for encryption/auth weaknesses.

- [ ] **Defensive Profiling:** Identify the presence of **IDS/IPS, SIEM, SOAR, and EDR/DLP**. If found, slow down your operation immediately.

- [ ] **Unintended Binary Research:** Map the target's OS to potential **LOLBAS, GTFOBINS, or WADCOMS** vectors for later movement.

- [ ] **Version-to-CVE Correlation:** Cluster hosts by **banners/JA3/favicons** and map exposed versions to **CVE** candidates before exploitation.

---

### **Phase 5: IPv6 & Protocol Enumeration**

_Goal: Discover targets using newer protocols and dual-stack networks._

- [ ] **IPv6 Reconnaissance:** Identify **IPv6 addresses** via **Shodan, Censys, IPv6 address enumeration tools** even when IPv4 is locked down.

- [ ] **Link-Local Discovery:** Scan for **link-local addresses** to discover local IPv6 devices and address schemes.

- [ ] **DHCPv6 Enumeration:** Use **DHCPv6 client** to extract **prefix, DNS servers, domain names** from DHCP responses.

- [ ] **SNMP Enumeration:** Query **SNMP community strings** (public/private) on discovered hosts to extract **routing tables, interface info, system description**.

- [ ] **LDAP Probing:** Query **LDAP** on **port 389** to enumerate **users, groups, organizational structure, computer objects**.

- [ ] **NFS Shares:** Probe for **NFS exports** on **port 2049** and attempt to mount for **file enumeration and exfiltration**.

- [ ] **RPC Enumeration:** Use **rpcclient, nmap NSE** to interrogate **RPC services** on **port 135/445** for **users, groups, shares**.

---

### **Phase 6: Dark Web & Breach Intelligence**

_Goal: Uncover intelligence from dark web and historical breaches._

- [ ] **Dark Web Searches:** Use **Tor, I2P**, or dedicated **dark web search engines** to find **leaked corporate data, stolen creds, threat reports**.

- [ ] **Breach Corpus Searching:** Query **Dehashed, Have I Been Pwned, Shodan**, and **breach databases** for **employee emails, leaked credentials, domain info**.

- [ ] **Threat Actor Profiling:** Identify relevant **APT groups, cybercrime forums, adversary tradecraft** that target your industry.

- [ ] **Ransomware Gang Sites:** Monitor **ransomware operator sites** for **leaked data, victim announcements, negotiation demands**.

- [ ] **Credential Stuffing Data:** Leverage **leaked cred combos** for **password spray, targeted phishing, VPN/email access**.

---

### **Phase 7: Satellite & Geospatial Intelligence**

_Goal: Use geospatial data to understand physical assets and infrastructure._

- [ ] **Satellite Imagery:** Use **Google Earth Pro, Sentinel Hub, USGS** to visualize **data center locations, server rooms, facility security**.

- [ ] **Geolocation Triangulation:** Combine **IP geolocation, BGP origin, ASN info** to identify **likely hosting providers and data center countries**.

- [ ] **Signal Intelligence (SIGINT):** Use **RF mapping tools (Shodan, GreyNoise)** to identify **telecommunications infrastructure, cell towers, transmission sites**.

- [ ] **Infrastructure Clustering:** Map **AS numbers, IP blocks, DNS servers** to identify **shared hosting clusters, CDN nodes, provider boundaries**.

---

### **Phase 8: Strategy & Attack Mapping**

_Goal: Convert raw data into an execution plan._

- [ ] **Security Architecture Classification:** Determine if they are utilizing **Zero Trust** or standard **MFA & 2FA**.

- [ ] **Framework Alignment:** Map your findings against the **Cyber Kill Chain, Diamond Model, or MITRE ATT&CK**.

- [ ] **Vulnerability Finalization:** Decide the entry vector based on recon: **SQL Injection, MITM, or Brute Force**.

---

<a id="toc-part-5-scanning"></a>
## Part 5: Scanning

### **Stage 1: Host Discovery & Network Topology (The "Roll Call")**

_Goal: Identify live assets without wasting time on dead IPs or triggering ICMP alarms._

- [ ] **ARP Discovery:** Use `arp-scan` or `nmap -PR` for local segment discovery to bypass host firewalls that drop ICMP.

- [ ] **ICMP & TCP/UDP Sweeps:** Perform standard `ping` sweeps or use `nmap -PS/-PU` (ports 80, 443, 53) to find external hosts that block standard pings.

- [ ] **Passive Traffic Capture:** Utilize **Wireshark** to capture broadcast traffic, revealing active hosts without sending a single packet.

- [ ] **Network Pathing & Perimeter Analysis:** Deploy `tracert` or `hping3 --traceroute` to map hops and define **Perimeter vs DMZ vs Segmentation** boundaries.

- [ ] **IPv6 Discovery:** Include **NDP/`nmap -6`** sweeps for dual-stack assets and SLAAC-derived hosts.

---

### **Stage 2: Port, Service & Protocol Enumeration (The "Door Check")**

_Goal: Determine exactly what applications are running and how they communicate._

- [ ] **Stealth SYN Scanning:** Use `nmap -sS` to identify open ports without completing the three-way **Handshake**, minimizing your footprint in application logs.

- [ ] **Version & OS Fingerprinting:** Deploy `nmap -sV` for service banners and `nmap -O` to analyze TCP/IP stack responses for **Operating System Hardening** clues.

- [ ] **Protocol Audit:** Analyze discovered services to determine if they use **Secure vs Insecure Protocols** (e.g., FTP vs SFTP, SSL vs TLS).

- [ ] **Connection Handshake Analysis:** Examine **Handshakes** to understand the specific authentication and encryption methods protecting the service.

- [ ] **UDP Surface Check:** Do not ignore `nmap -sU` for often-overlooked services like DNS (53), SNMP (161), and DHCP (67).

- [ ] **Timing & Hygiene:** Apply sane **-T profiles**, exclusion lists, and prefer **safe NSE** scripts before vuln categories to avoid tripping controls.

- [ ] **IPv6 Stack:** Mirror key scans with **`nmap -6`** for IPv6 services.

---

### **Stage 3: Defense & Configuration Assessment (The "Armor Check")**

_Goal: Identify security controls that will attempt to block or alert on your presence._

- [ ] **Firewall & ACL Enumeration:** Detect the presence of a **Firewall & Nextgen Firewall** or **Host Based Firewalls** by analyzing filtered ports and **ACL** (Access Control List) behavior.

- [ ] **IDS/IPS Probing:** Use fragmentation (`-f`) or timing decoys (`-D`) to identify active **NIDS, NIPS, or HIPS** systems that may block aggressive patterns.

- [ ] **Web Surface Discovery:** Use `ffuf` or `Gobuster` for **Directory Brute-forcing** to find hidden `/admin` or `/config` panels that are not linked publicly.

- [ ] **Service-Specific Enum:** Targeted checks for **SMB/RPC/WinRM**, **LDAP/Kerberos (AS-REP preauth, SPNs)**, **SNMP v1/v2c/v3**, **SMTP VRFY/EXPN**, **SSH KEX/ciphers**, **RDP/NLA**, **DBs (MySQL/MSSQL/Postgres)**, **Redis/Mongo/Elastic**.

---

### **Stage 4: Vulnerability Association & Attack Mapping**

_Goal: Convert raw scan data into actionable exploitation vectors._

- [ ] **Scripted Vulnerability Probing:** Use the **Nmap Scripting Engine (NSE)** (`--script vuln`) to check for known **Zero Day** or common exploits in identified versions.

- [ ] **Attack Surface Selection:** Match findings to your known **Common Attacks**—e.g., **SQL Injection** for web servers or **Buffer Overflows** for legacy binaries.

- [ ] **Unintended Tool Research:** For discovered OS versions, research **LOLBAS, GTFOBINS, or WADCOMS** to leverage existing system binaries for lateral movement.

- [ ] **Traffic Intelligence:** Finalize your plan by inspecting **Packet Captures** for cleartext protocols or weak encryption that allows for **MITM** or **Replay Attacks**.

- [ ] **Cluster & Correlate:** Group hosts by **banners/JA3/favicons** and map versions to likely **CVEs** before exploitation.

---

### **Stage 5: Stealth & Evasion Techniques**

_Goal: Scan without detection by firewalls, IDS, and EDR._

- [ ] **Fragmentation & Decoys:** Use `nmap -f` (fragment packets) or `-D` (decoy IPs) to evade **NIDS/NIPS signature detection**.

- [ ] **Timing Profiles:** Apply appropriate `-T` profile (T0-T5) to avoid triggering **rate-based IDS rules** or **adaptive firewalls**.

- [ ] **Null/FIN/Xmas Scans:** Use alternative scan types (`nmap -sN/-sF/-sX`) that bypass **stateless firewalls** but may not work through **stateful firewalls**.

- [ ] **ACK Scanning:** Use `-sA` to map **firewall rule sets** without attempting to establish connections.

- [ ] **Idle/Zombie Scanning:** Use `-sI` with a **zombie host** to perform **blind port scans** that don't directly originate from your IP.

- [ ] **Source Port Spoofing:** Use `--source-port 53/80` to impersonate **DNS/HTTP traffic** and bypass port-based **ACL rules**.

- [ ] **Packet Manipulation:** Craft **custom packets** with **Scapy** to evade **DPI (Deep Packet Inspection)** and **pattern-matching filters**.

---

### **Stage 6: Advanced Scanning Techniques**

_Goal: Optimize scanning efficiency and discover hidden services._

- [ ] **Parallel & Distributed Scanning:** Use **masscan** for rapid scanning of large ranges; distribute scans across **multiple IPs/proxies** to avoid threshold detection.

- [ ] **Custom Probes & NSE Scripting:** Write **NSE scripts** for **service-specific probing** (e.g., extracting **SANs from TLS**, **banner grabbing**, **service enumeration**).

- [ ] **WAF/CDN Bypass:** Identify backend IPs via **DNS history, SSL cert mismatches, HTTP header fingerprints**, and scan directly if possible.

- [ ] **Certificate Transparency (CT) Recon:** Parse **CT logs** to discover **hidden subdomains, domain variants, and organization structure**.

- [ ] **Reverse DNS Lookup:** Use **reverse DNS** to discover **vhosts, services, and hostnames** associated with IP ranges.

- [ ] **Proxychains & Proxy Pivoting:** Route scans through **VPNs, proxies, compromised hosts** to obscure source IP and bypass **geographic restrictions**.

<a id="toc-part-6-enumeration"></a>
## Part 6: Enumeration

> **Note:** Part 5 (Scanning) covers host discovery, port scanning, and defense identification. Part 6 focuses specifically on **extracting detailed information from discovered services** to build an attack profile. If you haven't completed Part 5, do so first.

### **Stage 1: Service Enumeration & Banner Grabbing**

_Goal: Extract version, configuration, and identity information from each discovered service._

- [ ] **Banner Grabbing:** Use **Netcat, Telnet, Nmap -sV** to capture **service banners** revealing **software name, version, OS hints, and build information**.

- [ ] **SMB Enumeration:** Use **enum4linux-ng, smbclient, CrackMapExec** to list **shares, users, groups, permissions, null sessions, and password policies** on Windows/Samba hosts.

- [ ] **SNMP Enumeration:** Query **SNMP (UDP 161)** with **snmpwalk, onesixtyone** using **community strings (public/private)** to extract **system info, interfaces, running processes, installed software**.

- [ ] **NFS Enumeration:** Use **showmount -e** to discover **exported shares**; check for **world-readable exports** and **root squash misconfigurations**.

- [ ] **SSH Enumeration:** Fingerprint **SSH versions, supported algorithms, key exchange methods** using **ssh-audit**; identify **weak ciphers, deprecated protocols**.

- [ ] **RDP Enumeration:** Use **nmap --script rdp-enum-encryption, rdp-ntlm-info** to extract **OS version, domain info, NLA requirements** from RDP endpoints.

---

### **Stage 2: Directory & Identity Enumeration**

_Goal: Map users, groups, and organizational structure from directory services._

- [ ] **LDAP Enumeration:** Query **LDAP** (port 389) to extract **users, groups, computers, password policies** without authentication.

- [ ] **Active Directory Recon:** Use **ldapsearch, enum4linux-ng, BloodHound** to map **domain trusts, group membership, SPNs, delegation**.

- [ ] **Kerberos Enumeration:** Use **kerbrute** for **username enumeration** via **AS-REQ responses**; identify **accounts without pre-authentication (AS-REP Roastable)**.

- [ ] **SMTP Enumeration:** Use **VRFY, EXPN, RCPT TO** commands to **verify valid email addresses and usernames** on mail servers.

- [ ] **RPC Enumeration:** Use **rpcclient, rpcinfo** to enumerate **RPC endpoints, user SIDs, domain information, printer shares**.

---

### **Stage 3: DNS & Infrastructure Enumeration**

_Goal: Extract naming, network, and infrastructure intelligence from DNS._

- [ ] **DNS Zone Transfer:** Attempt **AXFR/IXFR** transfers to extract **full DNS records** and internal hostnames.

- [ ] **DNS Record Enumeration:** Query **A, AAAA, MX, TXT, SRV, CNAME, NS, PTR** records to map **mail servers, services, subdomains, SPF/DMARC/DKIM** policies.

- [ ] **DNS Spoofing Prep:** Identify **DNS split-view** configurations and **internal domain naming** for **DNS rebinding attacks**.

- [ ] **Reverse DNS Sweeps:** Perform **PTR record lookups** across discovered IP ranges to reveal **hostnames, naming conventions, and hidden services**.

---

### **Stage 4: Database & Application Enumeration**

_Goal: Extract schemas, credentials, and data from discovered database and application services._

- [ ] **Database Discovery:** Identify **MySQL, MSSQL, PostgreSQL, Oracle, MongoDB, Redis, Elasticsearch** on standard/non-standard ports.

- [ ] **Database Default Creds:** Test **default credentials** (root/password, sa/sa, admin/admin) against discovered databases.

- [ ] **Database Information Schema:** Query **INFORMATION_SCHEMA** tables to enumerate **user accounts, object permissions, stored procedures**.

- [ ] **Backup & Recovery:** Identify **backup locations, recovery mode**, and **log files** that may contain **plaintext passwords or recovery keys**.

- [ ] **Web Application Enumeration:** Use **Gobuster, feroxbuster, ffuf** to discover **hidden directories, API endpoints, admin panels, configuration files, and backup archives** (.bak, .old, .swp).

---

### **Stage 5: Attack Surface Consolidation & Enumeration OpSec**

_Goal: Consolidate findings into an attack plan while maintaining stealth._

- [ ] **Attack Surface Map:** Combine all enumeration results into a **structured target profile** — users, credentials, shares, services, misconfigurations, and potential exploitation vectors.

- [ ] **Prioritized Attack Paths:** Rank targets by **exploitability and impact** — prioritize **null sessions, default credentials, writable shares, exposed admin panels, and AS-REP Roastable accounts**.

- [ ] **Tool Fingerprinting Awareness:** Understand that enumeration tools leave signatures — **vary User-Agents, throttle requests, rotate source IPs** where possible.

- [ ] **Timing Discipline:** Spread enumeration queries over time; avoid **rapid-fire LDAP/SMB/SNMP queries** that trigger **anomaly-based detection**.

- [ ] **Documentation:** Record all findings with **timestamps, source IPs, and tool commands** used — this feeds directly into **reporting and evidence collection**.

<a id="toc-part-7-system-hacking--initial-compromise"></a>
## Part 7: System Hacking & Initial Compromise

### **Phase 1: The Breach (Initial Access & Exploitation)**

_Goal: Weaponize theoretical vulnerabilities to bypass the perimeter and establish foothold._

**Application & Web Exploitation:**

- [ ] **SQL Injection:** Craft payloads for **error-based, blind, union-based, and time-based** exfiltration.

- [ ] **Buffer Overflow:** Target legacy binaries; craft **ROP chains** to bypass **ASLR/DEP**.

- [ ] **Directory/Path Traversal:** Abuse improper input validation to read **system files, configs, or keys**.

- [ ] **SSTI/Template Injection:** Exploit **Jinja2, Twig, ERB** misconfigs for **RCE**.

- [ ] **Deserialization:** Attack unsafe **Java/Python/PHP** unmarshaling for code execution.

- [ ] **SSRF:** Abuse server trust to pivot to **internal APIs, cloud metadata (IMDS), or localhost services**.

- [ ] **XXE/XML External Entity:** Parse malicious XML for **file read, XXE blind**, and **DOS**.

- [ ] **API Endpoint Abuse:** Exploit **BOLA/BFLA** (Broken Object/Function Level Auth) and **rate-limit bypass**.

- [ ] **Authentication Bypass:** Exploit **logic flaws** in login flows, abuse **password reset tokens**, manipulate **OAuth state parameters**.

- [ ] **Business Logic Flaws:** Identify **race conditions, insufficient workflow validation, price manipulation** in checkout/transaction flows.

- [ ] **File Upload Vulnerabilities:** Bypass **extension filters**, use **null bytes, double extensions, MIME type confusion** to upload **web shells**.

- [ ] **CAPTCHA Bypass:** Exploit **client-side validation**, reuse **tokens**, automate with **OCR/ML models**, abuse **audio alternatives**.

- [ ] **GraphQL Exploitation:** Perform **introspection queries**, abuse **batching/aliasing** for **DoS**, exploit **nested queries** and **IDOR**.

**Credential Assault:**

- [ ] **Brute Force:** Methodical password guessing with **wordlists, rule-based mangling**.

- [ ] **Password Spray:** Low-and-slow attacks across many accounts to avoid lockout.

- [ ] **Default Creds:** Enumerate and test **factory defaults** (admin/admin, root/root).

- [ ] **MFA Bypass:** Exploit **MFA fatigue, SIM-swap, push notification spoofing**.

- [ ] **Credential Stuffing:** Reuse leaked passwords from **breach corpuses** (HIBP/Dehashed).

**Human Vector & Social Engineering:**

- [ ] **Phishing:** Craft **HTML-smuggled payloads, ISO/LNK loaders, OneNote macros** with pretexting.

- [ ] **Whaling/Spear Phishing:** Target **executives** with personalized, researched lures.

- [ ] **Smishing/Vishing:** Use **SMS/voice** to deliver **URL shorteners, MFA prompts, or fake updates**.

- [ ] **Pretext:** Build **fake contractor, vendor, or IT support** persona to extract credentials verbally.

- [ ] **Watering Hole:** Compromise **public websites** frequented by targets to deliver **malware/tracker**.

**Network Interception & MITM:**

- [ ] **ARP Spoofing:** Poison **ARP tables** to intercept **unencrypted traffic**.

- [ ] **DNS Spoofing:** Redirect traffic via **cache poisoning or rogue DNS servers**.

- [ ] **SSL Stripping:** Downgrade **HTTPS to HTTP** when **HSTS** is weak or absent.

- [ ] **WiFi Evil Twin:** Build **rogue AP** with **karma/auto-join** to harvest credentials and inject payloads.

- [ ] **NGO Interception:** Capture traffic at **network gateways/bridges** with **tcpdump/Wireshark**.

---

### **Phase 2: The Ascension (Privilege Escalation)**

_Goal: Move from low-level foothold to administrative control by exploiting system logic._

**Windows Privilege Escalation:**

- [ ] **UAC Bypass:** Exploit **COM elevation, DLL hijack, token impersonation** to bypass **User Account Control**.

- [ ] **Service Misconfigs:** Abuse **weak service permissions, unquoted paths, service binaries** for **privilege hijack**.

- [ ] **Token Impersonation:** Steal **delegation tokens** from services to impersonate **SYSTEM/Domain Admin**.

- [ ] **DLL/DLL-Proxying:** Hijack **DLL search order** or use **sideloading** to execute arbitrary code at higher privilege.

- [ ] **Kernel Exploitation:** Target **unpatched zero-days** (MS21-1234) for **kernel-level code execution**.

- [ ] **Group Policy Exploitation:** Abuse **GPP passwords, startup scripts, scheduled tasks** for **privilege gain**.

**Active Directory Attacks:**

- [ ] **Kerberoasting:** Extract **TGS tickets** for **service accounts (SPNs)**, crack offline with **hashcat/JtR** to recover **plaintext passwords**.

- [ ] **AS-REP Roasting:** Target accounts with **pre-authentication disabled**, extract **AS-REP hashes** for offline cracking.

- [ ] **Golden/Silver Tickets:** Forge **TGT (Golden)** or **TGS (Silver)** tickets using **krbtgt hash** or **service account hash** for **persistent domain access**.

- [ ] **DCSync Attack:** Abuse **replication rights** to extract **password hashes** from **Domain Controller** without direct access.

- [ ] **BloodHound/SharpHound:** Map **AD trust relationships, ACLs, group memberships** to find **shortest path to Domain Admin**.

- [ ] **NTLM Relay:** Capture **NTLM authentication** and relay to **SMB/LDAP/HTTP** services for **lateral movement**.

- [ ] **Constrained/Unconstrained Delegation:** Abuse **delegation rights** to impersonate **privileged users** across domain services.

**Linux Privilege Escalation:**

- [ ] **setuid/setgid Abuse:** Exploit **vulnerable SUID binaries** (vim, cp, find) with **PATH manipulation**.

- [ ] **Capabilities Abuse:** Abuse **CAP_SETUID/CAP_SYS_ADMIN** for **shell execution as root**.

- [ ] **sudo Misconfigs:** Leverage **sudoers entries** (NOPASSWD, wildcard paths) for **privilege escalation**.

- [ ] **Kernel LPE:** Exploit **unpatched kernel vulnerabilities** (dirty cow, CVE-2016-5195) for **root shell**.

- [ ] **Cron/Systemd Abuse:** Hijack **cron jobs, systemd timers, .timer files** for **privilege execution**.

**Container & K8s Breakout:**

- [ ] **Mounted docker.sock:** Escape **container to host** via **Docker socket abuse**.

- [ ] **Privileged Containers:** Escape from **--privileged, CAP_SYS_ADMIN** containers.

- [ ] **hostPath Mounts:** Write to **host filesystem** via mounted volumes for **persistence**.

- [ ] **RBAC/CNI Misconfigs:** Abuse **Kubernetes role bindings** and **network policy gaps**.

**Cloud Platform Attacks:**

- [ ] **AWS IAM Exploitation:** Enumerate **overprivileged roles**, abuse **AssumeRole**, exploit **resource-based policies** for **privilege escalation**.

- [ ] **S3 Bucket Abuse:** Find **public buckets** via **bucket enumeration**, exploit **ACL misconfigs**, steal data from **pre-signed URLs**.

- [ ] **Cloud Metadata Services (IMDS):** Query **169.254.169.254** for **IAM credentials, instance metadata**, use **IMDSv2 bypass** techniques.

- [ ] **Azure AD Exploitation:** Abuse **service principals**, steal **access tokens**, exploit **OAuth consent grants** for lateral movement.

- [ ] **GCP Service Accounts:** Steal **service account keys**, abuse **IAM bindings**, exploit **Compute Engine metadata**.

- [ ] **Lambda/Function Abuse:** Inject code into **serverless functions**, abuse **environment variables**, exfil via **function logs**.

**LOLBAS & Living off the Land:**

- [ ] **Windows:** Abuse **PowerShell, WMI, certutil, bitsadmin, mshta** for **execution and evasion**.

- [ ] **Linux:** Leverage **bash, find, awk, sed, curl, wget** for **lateral movement and persistence**.

---

### **Phase 3: The Stronghold (Persistence & Lateral Movement)**

_Goal: Establish permanent presence and move horizontally across network._

**Credential Harvesting & Token Abuse:**

- [ ] **Pass-the-Hash:** Capture **NTLM hashes** and re-authenticate without cracking passwords.

- [ ] **Pass-the-Ticket:** Steal **Kerberos TGS tickets** to access **network services as compromised user**.

- [ ] **LSASS Dumping:** Extract **plaintext creds, hashes** via **mimikatz, procdump, comsvcs.dll**.

- [ ] **Browser/SSO Token Theft:** Harvest **OAuth/SAML tokens, session cookies** from **memory or storage**.

- [ ] **SSH Key Harvesting:** Steal **private keys** from **~/.ssh/id_rsa, agent sockets**.

**Malware & Backdoors:**

- [ ] **Rootkit Deployment:** Hide **files, processes, ports** via **kernel-mode rootkit** for **deep persistence**.

- [ ] **Trojan Backdoors:** Deploy **reverse shells, C2 beacons** disguised as **legitimate services**.

- [ ] **Bootkit/UEFI Implants:** Achieve **pre-OS persistence** via **bootloader compromise**.

- [ ] **Web Shell Placement:** Upload **ASP.NET, PHP, JSP** shells to **web-root** for **persistent access**.

- [ ] **Cron/Registry Backdoors:** Install **cron jobs, registry RunOnce** for **automatic re-execution**.

**Lateral Movement & Pivoting:**

- [ ] **SMB/WinRM:** Use **PsExec, Invoke-Command** to execute **commands on adjacent machines**.

- [ ] **SSH Agent Hijack:** Compromise **SSH forwarding** to move to **key-trusted hosts**.

- [ ] **RDP Relay/NTLM Relay:** Exploit **weak signing** to relay **RDP/HTTP credentials** to **other systems**.

- [ ] **DNS Exfiltration:** Tunnel **data over DNS queries** to exfiltrate **files incrementally**.

- [ ] **Printer/SNMP Abuse:** Exploit **print servers, SNMP v1/v2c** for **lateral access**.

- [ ] **SaaS-to-SaaS Pivoting:** Leverage **OAuth tokens/app integrations** to pivot from **Slack/Teams** into **Salesforce/GitHub/Google Workspace**.

---

### **Phase 4: The Shadow (Defense Evasion & Anti-Forensics)**

_Goal: Blind the Blue Team and minimize evidence of compromise._

**Log Manipulation & Cleanup:**

- [ ] **Windows Event Log:** Delete or clear **Security, System, Application** logs; disable **audit logging**.

- [ ] **Linux Auditd:** Disable **auditd**, flush **auth.log, syslog** via **log rotation abuse**.

- [ ] **Firewall/SIEM:** Identify **log shipping** and poison **central logs** or syslog streams.

- [ ] **Application Logs:** Scrub **web server logs, database audit trails, application-specific logs**.

**Defense Evasion:**

- [ ] **EDR Evasion:** Disable **Windows Defender, real-time protection**; abuse **exploit guard gaps**.

- [ ] **DLP Bypass:** Exfil via **covert channels, low-bandwidth tunnels, encryption obfuscation**.

- [ ] **IDS/NIDS Evasion:** Use **packet fragmentation, timing jitter, polymorphic payloads**.

- [ ] **AppArmor/SELinux Bypass:** Disable or escape **mandatory access controls**.

**Anti-Forensics:**

- [ ] **File Deletion:** Use **shred, srm, cipher /w** for **secure wiping** of tools and artifacts.

- [ ] **Timestomping:** Modify **file timestamps** (touch -t, $MFT, xattr) to **hide activity**.

- [ ] **Memory Wiping:** Clear **bash history, .zsh_history, PowerShell history** and environment variables.

- [ ] **Registry Cleanup:** Delete **run keys, browser history, recent documents, prefetch files**.

- [ ] **Obfuscation:** Use **base64, hex, ROT13** to hide **scripts, commands, strings** from pattern matching.

---

### **Phase 5: Data Exfiltration & Impact**

_Goal: Extract sensitive data and demonstrate business impact._

**Data Exfiltration Channels:**

- [ ] **DNS Tunneling:** Encode **data in DNS queries** and exfil via **recursive lookups**.

- [ ] **HTTPS Covert Channels:** Blend **exfil into normal HTTPS** streams with **size/timing variance**.

- [ ] **Cloud APIs:** Use **pre-signed S3/Blob URLs, Drive APIs** for **high-bandwidth exfil**.

- [ ] **ICMP/Ping Tunneling:** Tunnel **data over ping requests** when **TCP/UDP egress blocked**.

- [ ] **Dead-Drop Upload:** Stage **files to attacker-controlled sites** (GitHub gists, pastebin, etc.).

**Impact & Damage:**

- [ ] **Ransomware Deployment:** Encrypt **critical files** with **RSA/AES hybrid** and demand **ransom**.

- [ ] **Data Destruction:** Wipe **backups, system restore points** to prevent **recovery**.

- [ ] **Service Disruption:** Corrupt **databases, config files** to trigger **outages and chaos**.

---

### **Phase 6: The Professional (Governance & Reporting)**

_Goal: Execute within legal/ethical boundaries and deliver findings professionally._

**Rules of Engagement & Compliance:**

- [ ] **Scope Adherence:** Operate only within **authorized IP ranges, domains, systems** per engagement letter.

- [ ] **ROE Documentation:** Track **timeline, actions, access paths, artifacts discovered** for audit trail.

- [ ] **Escalation & Abort:** Know **when to stop, how to notify blue team, emergency procedures**.

- [ ] **Data Handling:** Secure **screenshots, credentials, exfiltrated files** with **encryption, access control**.

**Framework Alignment & Documentation:**

- [ ] **MITRE ATT&CK Mapping:** Correlate **every technique used** (T1234.567) to **documented tactics**.

- [ ] **Kill Chain Analysis:** Track the **Reconnaissance → Weaponization → Delivery → Exploitation → Installation → C2 → Actions** flow.

- [ ] **Vulnerability Timeline:** Document **discovery date, exploitation date, remediation deadline**.

**Audience-Centric Reporting:**

- [ ] **Executive Summary:** Non-technical **risk/impact narrative** for **board/C-suite**.

- [ ] **Technical Deep-Dive:** Detailed **attack chain, proof-of-concept, IOCs** for **security/engineering teams**.

- [ ] **Remediation Roadmap:** Prioritized **fixes by risk level** with **effort estimates and timelines**.

- [ ] **Metrics & KPIs:** Highlight **MTTD (Mean Time to Detect), MTTC (Mean Time to Contain), detection gaps**.

### **Lab Progression**

_Goal: Practice compromise only in controlled environments and produce professional evidence._

- [ ] **Beginner Host Labs:** Complete at least 5 intentionally vulnerable Linux/Windows machines; document initial access, privilege escalation, evidence, and remediation.
- [ ] **Credential Handling Lab:** Capture and crack lab-only hashes, then document storage, chain of custody, and cleanup. Use the Password Cracking Gate before attempting this.
- [ ] **Post-Exploitation Timeline:** Build an operator timeline and defender timeline for one lab compromise.
- [ ] **Detection Pairing:** For every exploit path, identify Windows Event Logs, Sysmon, auditd, network, or SIEM artifacts.
- [ ] **Move-On Gate:** Submit 3 full lab attack reports using the Part 39 structure.

<a id="toc-part-8-malware--weaponization"></a>
## Part 8: Malware & Weaponization

> **Safety Gate:** Malware work is restricted to isolated local labs with snapshots, host-only networking, no shared clipboard, no mounted host folders, and no third-party targets. Before running any sample or payload, define expected behavior, logging sources, rollback steps, and containment checks.

### **Phase 1: The Design & Logic (Architecture)**

_Goal: Design the malware's purpose using core security principles._

- [ ] **Target the CIA Triad:** Define if your payload destroys **Integrity** (Wipers/Data modification) or denies **Availability** (Ransomware/DDoS).

- [ ] **Weaponize Cryptography:** Implement **Public vs Private Keys** (Asymmetric Encryption) to lock files securely, ensuring only the attacker holds the decryption key.

- [ ] **Cryptographic Attacks:** Understand **padding oracle attacks, timing attacks, weak random number generation** to break encryption implementations.

- [ ] **Key Management Flaws:** Exploit **hardcoded keys, weak key derivation (KDF), insecure key storage** in applications.

- [ ] **C2 Protocol Design:** Choose **Secure vs Insecure Protocols** for Command & Control. Will you hide inside **HTTPS** traffic or use **DNS** tunneling to evade **Firewall & Next-Gen Firewall** inspection?

- [ ] **Risk Assessment:** Use the **Diamond Model** or **Cyber Kill Chain** to map out how your malware will move from **Reconnaissance** to **Actions on Objectives**.

---

### **Phase 2: The Payload & Mechanism (Weaponization)**

_Goal: Execute code on the target system._

- [ ] **Memory Exploitation:** Leverage **Buffer Overflow** or **Memory Leak** vulnerabilities to inject shellcode into legitimate processes, bypassing file scanning.

- [ ] **Delivery Vectors:** Utilize **Social Engineering** (Phishing/Whaling) or **Drive-by Attacks** to get the initial execution on the endpoint.

- [ ] **Payload Staging:** Use **modern modular frameworks** (Sliver, Havoc, Mythic, Brute Ratel C4) and **Metasploit/Cobalt Strike** with signature-hardened profiles.

- [ ] **Cloud-Native C2:** Hide beacons inside **trusted APIs** (e.g., **Microsoft Graph/SharePoint, Slack/Teams webhooks**) to blend with enterprise traffic beyond HTTP/DNS.

- [ ] **Living off the Land:** Instead of dropping new binaries, use **LOLBAS**, **GTFOBINS**, or **WADCOMS** to execute malicious logic using trusted system tools (e.g., PowerShell, Bash).

---

### **Phase 3: Evasion & Defense Bypassing (Invisibility)**

_Goal: Blind the defensive stack._

- [ ] **Defeat Static Analysis:** Apply **Obfuscation** (packing, encoding) to change the file hash and bypass traditional **Antivirus** signatures.

- [ ] **Sandbox Detection:** Code the malware to detect **Sandboxing** environments (e.g., checking for specific drivers, lack of mouse movement) and go dormant to generate a **False Negative**.

- [ ] **EDR/DLP Bypass:** Unhook API calls to hide from **EDR** (Endpoint Detection Response) and **DLP** monitors. Operate in memory (Fileless) to avoid leaving disk artifacts.

- [ ] **Traffic Masking:** Encrypt C2 traffic to look like normal web browsing, defeating **NIDS/NIPS** (Network Intrusion Prevention Systems).

- [ ] **In-Memory Evasion:** Apply **sleep obfuscation, call stack spoofing, indirect syscalls** to evade **memory scanning and EDR heuristics** during beacon idle time.

---

### **Phase 4: Persistence & Escalation (Entrenchment)**

_Goal: Survive reboots and gain total control._

- [ ] **Privilege Escalation:** Exploit **Operating System Hardening** gaps or **Kernel** vulnerabilities (Zero Day) to escalate from User to **SYSTEM/Root**.

- [ ] **Persistence Mechanisms:** Hide payload execution in **Scheduled Tasks**, **Registry Keys**, or **WMI** subscriptions to survive **Patching** and reboots.

- [ ] **Lateral Movement:** Use **Pass the Hash** or compromised **MFA & 2FA** tokens to pivot to other systems within the **Perimeter**.

- [ ] **Defense Disabling:** Actively terminate **Antimalware** or **Host Based Firewall** processes if privileges allow.

---

### **Phase 5: Counter-Forensics & Professionalism (The Cleanup)**

_Goal: Hide the tracks and adhere to engagement rules._

- [ ] **Anti-Forensics:** Use secure deletion to scrub **RAM artifacts** and **Packet Captures** to frustrate the **Basics of Forensics** investigation.

- [ ] **Log Manipulation:** Alter or clear **Event Logs** and **Syslogs** to blind **SIEM** and **SOAR** systems from correlating the attack.

- [ ] **Reverse Engineering Resistance:** Strip binary symbols and use anti-debugging techniques to make **Basics of Reverse Engineering** difficult for the Blue Team.

- [ ] **Rules of Engagement:** (For Red Teams) Ensure the malware's scope aligns with the **Penetration Testing Rules of Engagement**—do not destroy production data unless authorized.

---

<a id="toc-part-9-sniffing--spoofing"></a>
## Part 9: Sniffing & Spoofing

### **Phase 1: The Environment & Fundamentals (The Setup)**

_Goal: Understand the battlefield. You cannot spoof what you cannot map._

- [ ] **Protocol Hierarchy & Trust:** Differentiate between **MAC Addresses** (Layer 2 - Local Trust) and **IP Addresses** (Layer 3 - Routing). Spoofing relies on exploiting the trust mismatch between these layers.

- [ ] **Secure vs. Insecure Protocols:** Identify targets using cleartext protocols like **HTTP, FTP, Telnet, DNS**. These are trivial to sniff. Encrypted protocols like **TLS/HTTPS** and **SSH** require advanced downgrade attacks or decryption to bypass.

- [ ] **The Switch vs. Hub Reality:** Modern networks use switches which segment traffic by MAC. You cannot passively sniff; you must **ARP spoof, MAC flood**, or **VLAN hop** to bypass segmentation.

- [ ] **Interface Configuration:** Configure NIC to **Promiscuous Mode** (tcpdump, Wireshark) to capture all traffic, not just destined to your MAC; practice with **monitor mode** on wireless cards.

- [ ] **Handshake & Session Logic:** Study **TCP/TLS handshakes** (SYN/ACK, ClientHello/ServerHello) to identify session boundaries; understand **sequence numbers, window size, timestamps** for **replay and hijack** timing.

---

### **Phase 2: Sniffing & Passive Reconnaissance (The Ear)**

_Goal: Capture data without alerting the target. "Listen before act."_

- [ ] **Passive Packet Capture:** Use **tcpdump/Wireshark** to capture broadcast/multicast traffic (ARP, DHCP, mDNS) to identify active hosts, gateways, and services without sending directed traffic.

- [ ] **Wireless Interception:** Set wireless NIC to **monitor mode**; capture **WPA2/WPA3 4-way handshakes, PMKID** for offline cracking; identify **SSID, client MAC, AP MAC** patterns.

- [ ] **Protocol Analysis:** Filter **pcap** by protocol (HTTP, FTP, SMTP, DNS); identify **cleartext credentials, API keys, session tokens**, and software **User-Agent/Server banners**.

- [ ] **Stream Reassembly:** Use **tcpflow, Wireshark Follow TCP Stream** to reassemble files, images, emails, or form submissions from fragmented packets.

---

### **Phase 3: Spoofing & Active Deception (The Lie)**

_Goal: Inject false information into the network to redirect or manipulate traffic._

- [ ] **ARP Spoofing:** Flood the network with **gratuitous ARP packets** linking your MAC to the **gateway IP**; forces the switch to route victim traffic through you; use **arpspoof, dsniff, bettercap**.

- [ ] **DNS Spoofing:** Respond to **DNS queries faster than the legitimate server**; redirect victims to malicious login pages for **credential harvesting** or **malware distribution**.

- [ ] **DHCP Starvation & Rogue DHCP:** Exhaust legitimate DHCP pools and serve your own **gateway/DNS** to all clients; enables **MITM and traffic redirection**.

- [ ] **MAC Spoofing:** Change burned-in MAC to bypass **MAC filtering, NAC (Network Access Control), DHCP reservations**; use **macchanger** (Linux) or **SetMACAddress** (Windows).

- [ ] **IP Spoofing:** Forge **source IP** in packet headers to **hide identity, impersonate trusted hosts**, or launch **reflection/amplification attacks** in DDoS.

- [ ] **SSL Stripping & HTTP Downgrade:** Intercept **HTTPS traffic** and downgrade to **HTTP** by breaking the TLS handshake; use **sslstrip, mitmproxy** to expose encrypted traffic in cleartext.

---

### **Phase 4: Man-in-the-Middle & Exploitation (The Kill)**

_Goal: Intercept, modify, and relay traffic to extract or manipulate data._

- [ ] **MITM Positioning:** Establish yourself between victim and gateway via **ARP spoofing, DNS redirection, rogue DHCP, or rogue AP**; use **ettercap, mitmproxy, Burp Suite** to intercept and modify traffic in real-time.

- [ ] **Session Hijacking:** Extract **session cookies, JWT tokens, CSRF tokens** from sniffed **HTTP headers** and **POST bodies**; inject stolen tokens to impersonate user without password.

- [ ] **Credential Sniffing:** Capture **cleartext logins** (FTP, Telnet, HTTP Basic Auth, SMTP); extract **form credentials** from unencrypted POST requests.

- [ ] **Replay Attacks:** Capture valid **authentication tokens, API requests, or RF signals** and retransmit later to bypass time-based controls; works for **garage door openers, payment terminals, VoIP**.

- [ ] **Rogue Access Point / Evil Twin:** Deploy **fake Wi-Fi AP** with legitimate SSID + stronger signal; force users to connect and route all traffic through your box for **MITM harvesting**.

- [ ] **Traffic Injection & Modification:** Inject malicious **JavaScript, HTML, iframes** into unencrypted HTTP responses; modify **DNS responses** to redirect to attacker servers.

---

### **Phase 5: Defenses & Mitigation (The Shield)**

_Goal: Understand defensive controls to anticipate and evade them._

- [ ] **Encryption & VPN:** Force all traffic through **TLS/HTTPS, IPSec VPN, or VPN tunneling**; renders sniffed payloads unreadable; watch for **HSTS, certificate pinning** as anti-bypass measures.

- [ ] **Switch-Level Protection:** **Dynamic ARP Inspection (DAI)**, **DHCP Snooping**, **port security** reject malformed ARP/DHCP; **802.1X authentication** prevents rogue device connection.

- [ ] **Network Segmentation:** **VLAN isolation, micro-segmentation, zero trust** limits sniffing scope per compromised segment; east-west traffic encryption adds extra layers.

- [ ] **Detection Systems:** **IDS/IPS** flag high ARP packet volume, **MITM tools (ettercap signatures)**, SSL downgrade attempts; **Netflow/sFlow** detects unusual traffic patterns.

- [ ] **User Awareness:** Train users to verify **SSL certificates**, recognize **phishing login pages**, and use **password managers** to avoid clipboard paste attacks.

<a id="toc-part-10-social-engineering"></a>
## Part 10: Social Engineering

> **Safety Gate:** Social engineering practice must use consented simulations only. Do not target real people, employers, classmates, public organizations, or family accounts. Unauthorized phishing and impersonation are not "practice"; they are operational and legal exposure.

### **Stage 1: Intelligence & Reconnaissance (The Setup)**

_Goal: Know the target better than they know themselves._

- [ ] **Digital Recon:** Execute **OSINT** using **Google Dorks, LinkedIn scraping, GitHub dorking** to extract employee names, emails, roles, tech stacks, and company structure.

- [ ] **Physical Recon:** Perform **dumpster diving** to recover **org charts, vendor invoices, sticky notes** with passwords; observe **badge access patterns, delivery procedures**.

- [ ] **Domain & Infrastructure Prep:** Register **typo-squatting domains** (e.g., `companysupport.com`, `company-login.net`) that mimic target portals; prepare **phishing landing pages**.

- [ ] **Social Media Profiling:** Mine **LinkedIn, Twitter, GitHub, Glassdoor** for **personal details, relationships, job changes** to craft personalized lures.

---

### **Stage 2: The Digital Assault (Remote Vectors)**

_Goal: Compromise the target from a distance via electronic channels._

- [ ] **Mass Campaign:** Launch **broad phishing campaigns** with generic lures (password resets, package delivery) for large-scale **credential harvesting**.

- [ ] **Executive Targeting:** Execute **whaling attacks** against **C-suite/CFO** using deep **OSINT context** (recent news, personal interests, vendor relationships) to bypass skepticism.

- [ ] **Mobile Vector:** Deploy **SMS phishing (smishing)** with **MFA reset codes, delivery notifications, bank alerts**; use **VoIP/voice phishing (vishing)** to call employees directly.

- [ ] **Watering Hole:** Compromise **industry-specific forums, GitHub repos, or shared tools** to inject **malware/tracking code** that targets specific teams via **drive-by downloads**.

- [ ] **Deepfake Vishing:** Use **voice cloning/video deepfakes** (e.g., ElevenLabs) for **executive impersonation** in calls/meetings.

- [ ] **ClickFix/ClearFake:** Simulate browser/OS errors that instruct users to **copy-paste provided PowerShell/terminal scripts** (“fix/update now”).

---

### **Stage 3: The Human Element (Direct Interaction)**

_Goal: Use psychology and social manipulation to bypass logic._

- [ ] **Voice Pretexting:** Call as **IT support, HR, vendor, auditor, law enforcement** using social engineering pretexts; use **authority, urgency, fear** to bypass critical thinking.

- [ ] **Authority & Compliance Trigger:** Leverage **IT/Security/Auditor/Legal persona** to demand compliance; abuse **helpfulness bias** to force password resets or system access.

- [ ] **Reciprocity & Obligation:** Provide small **favors (tech help, free tools)** to create sense of obligation; ask for credentials or access in return.

---

### **Stage 4: The Physical Breach (Boots on the Ground)**

_Goal: Gain physical access to networks and facilities._

- [ ] **Tailgating:** Follow **authorized employees** into secure zones using badges/access cards; use **coffee cup hold, uniform/vendor persona** to bypass visual checks.

- [ ] **Shoulder Surfing:** Observe **PIN entry, password typing, screen content** in public spaces (airports, coffee shops, open offices) to capture credentials.

- [ ] **Badge Cloning:** Capture **RFID badge data** using **Proxmark3, ACR122U** and clone to malicious card; bypass **magnetic stripe readers** via cloning.

- [ ] **Physical Device Placement:** Plant **USB drops, rogue access points, hardware keyloggers** in common areas for **auto-execution** when connected by unsuspecting users.

---

### **Stage 5: Defense & Awareness (The Shield)**

_Goal: Prevent the human hack through training and controls._

- [ ] **Authentication:** Enforce **MFA/2FA** (TOTP, hardware keys, push notifications) so password compromise alone doesn't grant access; watch for **MFA fatigue attacks**.

- [ ] **Verification Protocols:** Train staff to **challenge unknown callers** via **secondary channel callback**; never trust caller ID alone; verify requests through official channels.

- [ ] **Physical Security:** Enforce **no-tailgating policies, visitor escorts, badge display requirements, clean desk policies** to prevent **dumpster diving and shoulder surfing**.

- [ ] **Security Awareness:** Regular **phishing simulations, red team testing, security training** to build **skepticism and reporting culture**; reward **security-first behavior**.

- [ ] **MFA Resilience:** Teach differences between **phishing-resistant MFA (FIDO2/Passkeys)** vs **phishable MFA (SMS/Push/OTP)**; test and mitigate **MFA fatigue** scenarios.

### **Lab Progression**

_Goal: Learn social engineering defensively and ethically._

- [ ] **Email Authentication Lab:** Configure and validate SPF, DKIM, and DMARC on a test domain or lab mail stack.
- [ ] **Header Forensics Lab:** Analyze benign/phishing email headers and identify sender path, SPF/DKIM/DMARC result, and suspicious infrastructure.
- [ ] **GoPhish Simulation Lab:** Run a consented internal lab campaign against test inboxes only; measure open/click/report rates.
- [ ] **Pretext Review:** Write three pretexts and then write the defensive awareness guidance that would defeat them.
- [ ] **Move-On Gate:** Produce a social-engineering simulation plan with ROE, consent model, metrics, and debrief template.

<a id="toc-part-11-denial-of-service"></a>
## Part 11: Denial of Service

> **Safety Gate:** DoS testing is local-lab-only unless a written contract explicitly authorizes it. Never run DoS tools against public IPs, SaaS platforms, school networks, ISP infrastructure, or bug bounty targets unless the scope explicitly permits availability testing.

### **Stage 1: Objective & Strategy (The Planning)**

_Goal: Understand DoS/DDoS scope and firepower requirements._

- [ ] **Denial of Service (DoS):** Single attacker sends **crafted traffic** to overwhelm a target's **CPU, bandwidth, or connections**; from one IP; **relatively easy detection**.

- [ ] **Distributed Denial of Service (DDoS):** **Multiple sources** (botnet, amplification servers) send traffic **simultaneously**; harder to trace and block; **stronger firepower**.

- [ ] **Target Assessment:** Identify **critical services** (web, DNS, mail, VPN) and **upstream bottlenecks** (ISP bandwidth, DDoS mitigation capacity) to determine **attack viability**.

---

### **Stage 2: The Arsenal (Attack Methods)**

_Goal: Select the right DoS technique for target vulnerabilities._

- [ ] **Volumetric Attacks:** Consume **bandwidth** using **SYN floods, UDP floods, ICMP floods** to saturate network pipes; use **DNS amplification, NTP reflection** to multiply traffic (1 request → 1000× response).

- [ ] **Protocol Attacks:** Exploit **TCP/IP stack weaknesses** (malformed packets, fragment handling, connection states) using **Ping of Death, Teardrop, SYN floods** to crash systems or exhaust connection limits.

- [ ] **Application-Layer Attacks:** Target **specific services** with **HTTP floods (Slowloris), database queries (CPU spike), cached assets** to overwhelm **web servers, APIs, load balancers** at Layer 7.

- [ ] **IoT/Botnets:** Compromise **webcams, routers, smart devices** via **default creds, unpatched firmware** to join **Mirai, Dridex-style botnets** for DDoS-as-a-Service.

---

### **Stage 3: Infrastructure & Execution (The Assault)**

_Goal: Deploy and sustain the attack at scale._

- [ ] **Botnet Assembly:** Recruit **thousands of infected IoT/servers** or use **existing botnet services** (DDoS-as-a-Service, rent botnet time); establish **C&C control** via IRC/DNS/Peer-to-Peer.

- [ ] **Traffic Generation:** Use **tools like hping3, slowhttptest, LOIC, Colasoft PacketBuilder** to craft and blast custom packets; coordinate **multi-vector attacks** (volumetric + protocol + app-layer simultaneously).

- [ ] **Proxy/Spoofing:** Use **open reflectors/amplifiers** (DNS servers, NTP, SNMP) to amplify traffic; spoof **source IP addresses** to obscure attacker origin.

- [ ] **Duration & Monitoring:** Sustain attack for **hours/days** while monitoring **target availability, ISP response, filtering changes**; adjust payload/vector on-the-fly.

---

### **Stage 4: Defense & Mitigation (The Shield)**

_Goal: Detect, absorb, and neutralize DoS attacks._

- [ ] **Edge Defense:** Deploy **Cloudflare, Akamai, AWS Shield Standard** to absorb DDoS at **ISP/CDN level** before traffic reaches origin; filter **malformed packets, spoofed IPs** at network edge.

- [ ] **Rate Limiting & Throttling:** Implement **connection limits, request rate caps, CAPTCHAs, geo-blocking** to let legitimate users through while rejecting flood traffic.

- [ ] **Monitoring & Detection:** Deploy **NetFlow/sFlow analysis, IDS/IPS (Suricata, Zeek)** to detect **unusual traffic patterns, connection spikes, protocol anomalies**; alert on **RTO timeouts, CPU/bandwidth saturation**.

- [ ] **Architectural Resilience:** Use **anycast DNS, geographically distributed servers, auto-scaling, load balancing** to spread load; oversizing infrastructure to **absorb baseline attacks**; prepare **incident response playbooks**.

- [ ] **ISP/Carrier Coordination:** Work with **ISP's DDoS mitigation services** to scrub traffic upstream; establish **BGP blackholing** to discard attack traffic at border; maintain **redundant ISPs/circuits**.

<a id="toc-part-12-session-hijacking"></a>
## Part 12: Session Hijacking

### **Stage 1: Reconnaissance & Vulnerability Analysis**

_Goal: Find a target and identify its weaknesses._

- [ ] **Target Identification:** Use **Reconnaissance** and **OSINT** to identify target web applications.

- [ ] **Protocol Analysis:** Check if the application uses **Unsecure Protocols** (HTTP) for any part of the session, making it vulnerable to sniffing.

- [ ] **Session Mechanism Analysis:** Study **session ID generation, cookie attributes, token entropy** for weak patterns.

- [ ] **Vulnerability Scanning:** Test for **XSS, CSRF, MITM susceptibility, weak session timeouts**.

---

### **Stage 2: Stealing the Session ID (The Attack Vectors)**

_Goal: Execute the attack to acquire the victim's session token._

- [ ] **Network Sniffing:** If HTTP is in use, launch **packet capture** with **Wireshark** on the local network or from a **Rogue Access Point** to intercept session cookies.

- [ ] **Client-Side Injection:** Craft and deliver an **XSS** payload (via **Phishing** or a stored vulnerability) to steal `document.cookie` from the user's browser.

- [ ] **Man-in-the-Middle:** Execute a **MITM** attack using **ARP spoofing, DNS spoofing**, or **SSL stripping** to intercept encrypted sessions.

- [ ] **Session Fixation:** Force victim to use **attacker-controlled session ID** by injecting it via URL or cookies before authentication.

- [ ] **Browser Extension Abuse:** Exploit **malicious browser extensions** to exfiltrate cookies from victim's browser storage.

---

### **Stage 3: Execution & Impersonation**

_Goal: Use the stolen token to access the user's account._

- [ ] **Token Injection & Hijack:** Inject the stolen session ID into your browser cookies to achieve **impersonation** of the victim, bypassing **authentication** completely.

- [ ] **Session Replay:** Reuse captured **authentication tokens, API keys, JWT** to access protected resources.

- [ ] **Privilege Escalation:** If session belongs to **privileged user**, exploit to gain **administrative access**.

---

### **Stage 4: Defense & Mitigation (The Shield)**

_Goal: Prevent the attack from succeeding._

- [ ] **Enforce Encryption:** Mandate **TLS 1.2+** for all web traffic; implement **HSTS** to prevent SSL stripping.

- [ ] **Secure Cookie Attributes:** Implement `HttpOnly`, `Secure`, `SameSite=Strict` flags on cookies to mitigate **XSS** theft and CSRF.

- [ ] **Session Management:** Implement **session regeneration after login**, **absolute/idle timeouts**, **IP/User-Agent binding**.

- [ ] **Multi-Factor Authentication:** Deploy **MFA/2FA** to ensure stolen session token alone is insufficient for sensitive actions.

- [ ] **Network Monitoring:** Use **IDS/IPS** to detect **MITM patterns, ARP spoofing, SSL stripping attempts**.

<a id="toc-part-13-detection--mitigation-blue-team-perspective"></a>
## Part 13: Detection & Mitigation (Blue Team Perspective)

_Understand defensive detection to know what to evade._

### **Phase 1: Defensive Architecture**

- [ ] **Defense-In-Depth:** Layer **EDR, SIEM, CASB, firewall, WAF, IDS/IPS, DNS filtering** with **proper tuning** to reduce false positives and enable hunting.

- [ ] **Threat Hunting:** Proactively search for **suspicious patterns** (parent/child process anomalies, unsigned DLLs, scheduled task abuse, registry modifications) using **Sigma rules, YARA, KQL**.

- [ ] **Incident Response Plan:** Document **detection, containment, eradication, recovery, lessons learned** phases with **clear ownership and escalation paths**.

---

### **Phase 2: Offensive Indicators & TTPs**

- [ ] **IOC Identification:** Recognize **file hashes, domains, IPs, email patterns, behavioral signatures** that map to known attack frameworks (Cobalt Strike, Metasploit, custom).

- [ ] **MITRE ATT&CK Mapping:** Correlate **detected behaviors** to **tactics/techniques** to understand adversary intent and prioritize detection investment.

- [ ] **Artifact Analysis:** Understand forensic artifacts (prefetch, MFT, journal logs, browser history, registry hives, event logs) as **evidence of compromise**.

---

### **Phase 3: Evasion Detection & Hardening**

- [ ] **Living-off-the-Land Detection:** Monitor **native binary execution** (PowerShell, WMI, certutil, mshta, bitsadmin) with **process whitelisting, memory pattern analysis, and behavioral indicators**.

- [ ] **Obfuscation Analysis:** Detect **encoded payloads, packed executables, script obfuscation** via **entropy analysis, dynamic detonation, behavioral sandboxing**.

- [ ] **Anti-Forensics Detection:** Identify **log clearing, file timestomping, registry deletion, bash history removal** via **SIEM correlation and immutable audit logs**.

- [ ] **Command-Line Auditing:** Enable and monitor **PowerShell transcript logging, command-line audit logs (4688), script block logging** for obfuscated execution.

---

### **Phase 4: Detection Engineering & Response**

- [ ] **Detection Rules:** Write **Sigma, Snort/Suricata, Yara, osquery** rules targeting **adversary TTPs** from reconnaissance to exfiltration.

- [ ] **Alert Tuning:** Baseline **normal traffic/processes**, establish **alert thresholds**, reduce **false positives** to improve SOC efficiency.

- [ ] **SOC Playbooks:** Document **runbooks** for each alert type: **triage → validation → containment → remediation → documentation**.

- [ ] **Threat Intelligence Integration:** Consume **OSINT feeds, MISP, AlienVault OTX, commercial threat intel** to enrich **IP/domain/file lookups** in SIEM.

---

### **Phase 5: EDR/XDR/MDR Basics**

_Goal: Understand modern endpoint and extended detection capabilities._

- [ ] **EDR Architecture:** Understand **agent-based detection (process, file, registry, network), telemetry collection, cloud backend, response orchestration**.

- [ ] **EDR Capabilities:** Know **behavioral analysis, memory scanning, AMSI integration, ETW collection, indicator of compromise (IOC) matching**.

- [ ] **EDR Evasion vs. Detection:** Understand **living-off-the-land techniques EDR detects**, **code injection detection**, **DLL side-loading detection**.

- [ ] **XDR Approach:** Understand how **XDR correlates endpoint, network, cloud, identity signals** for **detection, hunting, response** across domains.

- [ ] **MDR Services:** Know what **Managed Detection & Response (MDR)** providers offer: **24/7 monitoring, incident response, threat hunting, consulting**.

---

### **Phase 6: SOC & SIEM Fundamentals**

_Goal: Understand Security Operations Center workflow and SIEM correlation._

- [ ] **SIEM Basics:** Understand **log aggregation, parsing, normalization, correlation, enrichment** using tools like **Splunk, ELK, ArcSight, QRadar**.

- [ ] **Log Collection:** Know what logs to collect: **Windows Event Logs, Sysmon, firewall logs, proxy logs, DNS logs, authentication logs, application logs**.

- [ ] **Alert Correlation:** Understand **multi-stage detection** (e.g., suspicious logon + process creation + network connection = lateral movement indicator).

- [ ] **SOC Workflow:** Understand **analyst triage → escalation → incident investigation → containment → reporting** process and metrics (MTTD, MTTR).

- [ ] **Dashboard & KPIs:** Know key metrics: **alert volume, MTTD/MTTR, false positive rate, detection coverage %, incident severity distribution**.

---

### **Phase 7: Threat Hunting Methodology**

_Goal: Learn proactive threat hunting to find advanced threats._

- [ ] **Hunting Hypotheses:** Formulate hypotheses based on **MITRE ATT&CK, threat reports, prior compromises** (e.g., "Are scheduled tasks being abused?").

- [ ] **Data Source Selection:** Choose **event logs, network traffic, process telemetry, file integrity monitoring** appropriate for hypothesis.

- [ ] **Query Construction:** Build **SQL, KQL, SPL queries** in SIEM to **search for patterns** (unusual process chains, rare executables, domain queries).

- [ ] **Pivot & Correlate:** Use **results to pivot** (e.g., find account → check all logons → find source IP → check all connections).

- [ ] **Validation & Documentation:** Confirm findings are **actual compromise vs. false positive**, document **timeline, IOCs, and response**.

---

### **Phase 8: Incident Response Basics**

_Goal: Understand the incident response lifecycle._

- [ ] **Detection & Analysis:** Receive **alert/complaint → triage → determine if real incident → declare incident**.

- [ ] **Containment Strategy:** Short-term: **isolate affected systems**; Long-term: **fix vulnerabilities, update passwords, patch**.

- [ ] **Eradication:** **Remove attacker access** (reset creds, close backdoors, patch exploited systems), verify **persistence mechanisms** removed.

- [ ] **Recovery:** **Restore systems to known good state**, rebuild compromised hosts, verify **no re-infection**.

- [ ] **Lessons Learned:** **Timeline analysis, root cause, detection gaps, improve controls** to prevent recurrence.

- [ ] **Forensic Preservation:** During response, **preserve evidence** (memory dumps, disk images, logs) for **investigation and legal proceedings**.

---

### **Phase 9: Forensic Fundamentals**

_Goal: Collect and analyze evidence of compromise._

- [ ] **Live Response:** Collect **running processes, network connections, logged-in users, active services** before shutdown (loses volatile data).

- [ ] **Disk Imaging:** Create **bit-for-bit copy** of drives for **offline analysis**, use tools like **dd, Acquire, FTK Imager**.

- [ ] **Timeline Analysis:** Build **chronological timeline** of **file creation/modification, registry changes, logs** to reconstruct **attack sequence**.

- [ ] **Artifact Examination:** Analyze **Windows Prefetch, Shimcache, MRU, Recycle Bin, browser history, temp files** for **evidence of compromise**.

- [ ] **Memory Analysis:** Use tools like **Volatility, Rekall** to extract **running processes, injected code, encryption keys, command history** from memory dumps.

---

### **Phase 10: Blue Team Evasion Counter-Measures**

_Goal: Know how defenders detect and counter red team techniques._

- [ ] **Process Whitelisting:** Defenders use **AppLocker, Device Guard** to allow only **approved executables**; evade via **living-off-the-land** or **trusted paths**.

- [ ] **Memory Protection:** Defenders enable **DEP/NX, ASLR, CET**; understand these reduce **code injection effectiveness**.

- [ ] **Signing Checks:** Defenders verify **code signatures**; exploit **weak validation** or **stolen certificates**.

- [ ] **Logging & Audit:** Defenders enable **command-line logging, PowerShell block logging, Sysmon, ETW**; evade via **log tampering or memory-only payloads**.

- [ ] **Behavioral Blocking:** EDRs use **behavior analysis** to block **suspicious chains** (e.g., Office → PowerShell → network); develop awareness of **detectable patterns**.

- [ ] **Alert Tuning:** Build **low false-positive alerts** for high-confidence indicators (e.g., AMSI evasion, direct syscalls, token theft patterns).

- [ ] **Playbook Development:** Create **runbooks** for common attack patterns (ransomware deployment, credential theft, lateral movement) with **clear triage and containment steps**.

- [ ] **Purple Teaming:** Partner with red teams to **validate detections, test response procedures, and measure MTTD (Mean Time to Detect) and MTTR (Mean Time to Respond)**.

---

### **Lab Progression**

_Goal: Build a working detection environment, not just blue-team vocabulary._

- [ ] **SIEM Build:** Deploy Wazuh, Security Onion, Splunk Free, or ELK in a lab and ingest Windows Event Logs, Sysmon, Linux auth logs, and firewall/DNS logs.
- [ ] **Query Lab:** Write 10 searches across SPL/KQL/Elastic-style syntax for process creation, suspicious PowerShell, failed logons, DNS anomalies, and lateral movement.
- [ ] **Detection Rule Lab:** Write 5 Sigma/YARA/Suricata/Zeek/osquery rules and test them against lab activity.
- [ ] **Incident Timeline Lab:** Reconstruct 2 incidents from logs and produce analyst notes with evidence and containment actions.
- [ ] **Move-On Gate:** Produce a detection coverage matrix mapped to MITRE ATT&CK tactics.

<a id="toc-part-14-ids-firewalls-and-honeypots"></a>
## Part 14: IDS, Firewalls, and Honeypots

### **Stage 1: Foundational Strategy & Networking**

_Goal: Establish the theoretical base and network understanding._

- [ ] **Defense in Depth:** Adopt the `Understand Concept of Defense in Depth` philosophy, using multiple layers of security controls.

- [ ] **Network Segmentation:** Design the network with clear boundaries, utilizing `Perimeter vs DMZ vs Segmentation` to limit blast radius.

- [ ] **Protocol Knowledge:** Master networking fundamentals, including `Understand Handshakes` and identifying `Secure vs Unsecure Protocols`.

---

### **Stage 2: Deploying Firewalls (The Shield)**

_Goal: Implement access control and segmentation._

- [ ] **Perimeter Defense:** Deploy a `Firewall & Nextgen Firewall` at the network edge, configuring `ACLs` for ingress and egress filtering.

- [ ] **Endpoint Protection:** Enable and configure `Host Based Firewall` on servers and workstations for granular `Port Blocking`.

- [ ] **Log Analysis:** Set up centralized collection for `Firewall Logs` to monitor policy violations and traffic patterns.

---

### **Stage 3: Implementing IDS/IPS (The Watchers)**

_Goal: Detect and stop malicious traffic that bypasses firewalls._

- [ ] **Strategic Deployment:** Place `NIDS` sensors at critical network choke points to monitor east-west and north-south traffic.

- [ ] **Host Monitoring:** Install `HIPS` agents on critical servers to detect suspicious process execution and file changes.

- [ ] **Rule Tuning:** Continuously tune signature and anomaly rules to minimize `False Positives` while ensuring no `False Negatives` occur.

- [ ] **SIEM Integration:** Feed IDS/IPS alerts into a `SIEM` for correlation with other security events.

---

### **Stage 4: Utilizing Deception (The Traps)**

_Goal: Gather threat intelligence and waste attacker time._

- [ ] **Honeypot Deployment:** Deploy `Honeypots` (both low and high interaction) in the DMZ and internal network to attract attackers.

- [ ] **Traffic Redirection:** Use `Sinkholes` to capture traffic destined for known malicious domains or IPs.

- [ ] **Intelligence Gathering:** Analyze logs and activity from deception tools to inform `Basics and Concepts of Threat Hunting`.

---

### **Stage 5: Operations & Continuous Improvement**

_Goal: Integrate into daily security operations._

- [ ] **Incident Response Integration:** Utilize these tools during **Incident Response Process** for rapid **threat identification and containment** of affected systems.

- [ ] **Zero Trust Alignment:** Ensure firewall and IPS policies align with **Zero Trust** principles, verifying every connection attempt.

- [ ] **Performance Tuning:** Regularly review and tune **IDS/IPS rules, firewall ACLs** to balance security and performance.

- [ ] **Threat Intelligence Integration:** Feed **IOCs from threat intelligence** into firewalls and IDS for proactive blocking.

- [ ] **Red/Purple Team Testing:** Conduct regular **red team exercises** to validate detection capabilities and identify blind spots.

---

<a id="toc-part-15-osint--threat-intelligence"></a>
## Part 15: OSINT & Threat Intelligence

### **Stage 1: Passive Reconnaissance & Data Collection**

_Goal: Gather intelligence without touching target infrastructure._

- [ ] **Search Engine Intelligence:** Master **Google/Bing/Yandex dorks** for exposed data; use **Shodan/Censys/Zoomeye** for internet-wide scanning.

- [ ] **Social Media Mining:** Scrape **LinkedIn, Twitter, Facebook, Instagram** for employees, org structure, tech stack mentions, and personal details.

- [ ] **Domain & Infrastructure:** Use **WHOIS, DNS records (MX, TXT, SPF, DMARC), Certificate Transparency logs** to map infrastructure.

- [ ] **Breach Data Analysis:** Query **HIBP (Have I Been Pwned), Dehashed, Snusbase** for leaked credentials and PII.

- [ ] **Code Repository Mining:** Search **GitHub, GitLab, Bitbucket** for exposed **API keys, credentials, internal IPs, architecture docs**.

- [ ] **Dark Web Monitoring:** Monitor **paste sites, forums, dark web marketplaces** for leaked data, exploit sales, threat actor chatter.

---

### **Stage 2: Threat Intelligence Analysis**

_Goal: Convert raw data into actionable intelligence._

- [ ] **IOC Collection:** Aggregate **file hashes, domains, IPs, email patterns** from **threat feeds, MISP, AlienVault OTX**.

- [ ] **Threat Actor Profiling:** Study **APT groups, TTPs, infrastructure patterns** using **MITRE ATT&CK, threat reports (Mandiant, CrowdStrike)**.

- [ ] **Campaign Tracking:** Monitor **active campaigns, malware families, exploit trends** to understand current threat landscape.

- [ ] **Attribution Analysis:** Correlate **infrastructure, code patterns, language artifacts** to attribute attacks to specific actors.

- [ ] **Victimology Studies:** Understand **target selection, industry focus, geographic distribution** of threat actors.

---

### **Stage 3: OSINT Automation & Tooling**

_Goal: Scale reconnaissance with automation._

- [ ] **Reconnaissance Frameworks:** Master **Recon-ng, theHarvester, SpiderFoot, Maltego** for automated data collection.

- [ ] **Subdomain Enumeration:** Use **Amass, Subfinder, Assetfinder, DNSRecon** to discover **subdomains, ASNs, IP ranges**.

- [ ] **API Integration:** Leverage **VirusTotal, Shodan, SecurityTrails, Hunter.io APIs** for programmatic data access.

- [ ] **Custom Scripting:** Build **Python/Bash scripts** to automate **scraping, parsing, correlation** of OSINT data.

- [ ] **Data Pipeline:** Create **ETL pipelines** to aggregate, normalize, and store intelligence in **databases/dashboards**.

---

### **Stage 4: Threat Intelligence Dissemination**

_Goal: Communicate intelligence effectively to stakeholders._

- [ ] **Intelligence Reports:** Create **tactical (IOCs), operational (TTPs), strategic (trends)** reports for different audiences.

- [ ] **TLP Classification:** Apply **Traffic Light Protocol (White, Green, Amber, Red)** for information sharing sensitivity.

- [ ] **STIX/TAXII:** Use **Structured Threat Information Expression (STIX)** and **TAXII** for standardized intel sharing.

- [ ] **Threat Briefings:** Deliver **executive briefings** highlighting **risks, trends, recommended actions** in non-technical language.

- [ ] **Community Collaboration:** Participate in **ISACs, threat intel communities, CTI sharing platforms** for collective defense.

---

<a id="toc-part-16-adversary-emulation--purple-teaming"></a>
## Part 16: Adversary Emulation & Purple Teaming

### **Stage 1: MITRE ATT&CK Framework Mastery**

_Goal: Understand the universal language of adversary behavior._

- [ ] **Tactic Familiarity:** Master all **14 tactics** (Initial Access → Impact) and their relationships in the attack lifecycle.

- [ ] **Technique Deep-Dive:** Study **100+ core techniques** with focus on **prevalence, detection difficulty, impact** ratings.

- [ ] **Sub-Technique Granularity:** Understand **sub-technique variations** for precise emulation (e.g., T1059.001 PowerShell vs T1059.003 CMD).

- [ ] **Data Source Mapping:** Link techniques to **detection data sources** (process creation, network traffic, registry modifications).

- [ ] **Mitigation Strategies:** Review **MITRE mitigations** for each technique to understand defensive controls.

---

### **Stage 2: APT & Threat Actor Emulation**

_Goal: Replicate real-world adversary campaigns._

- [ ] **APT Profiling:** Study **APT groups** (APT28, APT29, Lazarus, FIN7) including **TTPs, tools, targeting, infrastructure**.

- [ ] **Campaign Recreation:** Emulate **documented campaigns** step-by-step using **MITRE ATT&CK Navigator** for technique mapping.

- [ ] **Tool Replication:** Use **adversary tools** (Mimikatz, Cobalt Strike, Empire, custom malware) to match TTP fidelity.

- [ ] **Infrastructure Mimicry:** Build **attack infrastructure** (domains, IPs, C2) that mimics **APT patterns and behaviors**.

- [ ] **Operational Tempo:** Match **adversary dwell time, persistence patterns, exfil timing** for realistic simulation.

- [ ] **Adversary Emulation Plans:** Execute **MITRE ATT&CK Adversary Emulation Plans** for groups like **APT29, Scattered Spider** to test realistic kill chains.

---

### **Stage 3: Purple Team Exercises**

_Goal: Collaborative offense-defense improvement._

- [ ] **Joint Planning:** Define **objectives, scope, techniques, success criteria** with both red and blue teams.

- [ ] **Live Detection Tuning:** Execute **attacks in controlled environment** while defenders **tune detection rules in real-time**.

- [ ] **Gap Analysis:** Identify **detection blind spots, control failures, response deficiencies** through collaborative testing.

- [ ] **Playbook Development:** Create **detection playbooks** with **queries, alerts, response procedures** for each emulated technique.

- [ ] **Iterative Improvement:** Run **multiple rounds** of testing with **incremental detection improvements** to measure progress.

---

### **Stage 4: Metrics & Reporting**

_Goal: Quantify security posture improvement._

- [ ] **Detection Coverage:** Calculate **% of ATT&CK techniques** with detection coverage across the matrix.

- [ ] **MTTD/MTTR:** Measure **Mean Time to Detect** and **Mean Time to Respond** for each technique tested.

- [ ] **False Positive Rate:** Track **alert accuracy** and **tuning effectiveness** over multiple exercises.

- [ ] **Control Effectiveness:** Rate **preventative, detective, responsive** controls against each technique (None/Partial/Full).

- [ ] **Trend Analysis:** Compare **metrics across time** to demonstrate **security maturity improvement**.

---

<a id="toc-part-17-web-application-hacking"></a>
## Part 17: Web Application Hacking

### **Stage 1: Reconnaissance & Mapping**

_Goal: Understand the target application's structure and technologies._

- [ ] **OSINT & Discovery:** Perform **Reconnaissance** using **Google Dorks, Shodan, Certificate Transparency** to find subdomains, exposed admin panels, and developer info.

- [ ] **Service Enumeration:** Use `nmap -sV -sC` to identify web servers, versions, and common vulnerabilities.

- [ ] **Technology Fingerprinting:** Use **Wappalyzer, BuiltWith, WhatWeb** to identify frameworks, CMS, WAF, CDN, and backend technologies.

- [ ] **Content Discovery:** Run **Gobuster, ffuf, dirsearch** to find hidden directories, backup files, API endpoints, and admin panels.

- [ ] **Sitemap & Robots Analysis:** Parse **robots.txt, sitemap.xml, security.txt** for disallowed paths and contact info.

---

### **Stage 2: Vulnerability Analysis & Probing**

_Goal: Find potential entry points and weaknesses._

- [ ] **Input Validation Testing:** Test every input field for **SQL Injection, NoSQL Injection, Command Injection, LDAP Injection**.

- [ ] **Path Manipulation:** Probe for **Directory/Path Traversal** using `../../../etc/passwd` and **LFI/RFI** vulnerabilities.

- [ ] **Logic Testing:** Analyze **authentication/authorization** mechanisms; test for **IDOR, broken access controls, privilege escalation**.

- [ ] **Protocol & Crypto Analysis:** Check **TLS configuration** with **sslyze/testssl.sh**; test for **weak ciphers, certificate issues, HTTPS downgrade**.

- [ ] **API Testing:** Enumerate **REST/GraphQL/SOAP** endpoints; test for **lack of rate limiting, exposed documentation, mass assignment**.

---

### **Stage 3: Exploitation (The OWASP Top 10)**

_Goal: Prove the vulnerability and gain access._

- [ ] **Injection Attacks:** Execute **SQL injection** for data extraction; **command injection** for RCE; **LDAP/XPath** injection.

- [ ] **Cross-Site Scripting (XSS):** Deliver **reflected, stored, DOM-based** XSS to steal cookies, hijack sessions, or deface pages.

- [ ] **CSRF & Request Forgery:** Construct **CSRF attacks** to perform state-changing actions; test **SSRF** for internal network access.

- [ ] **Authentication Bypass:** Exploit **logic flaws, password reset**, **JWT manipulation, OAuth misconfigs** to gain unauthorized access.

- [ ] **File Upload Exploitation:** Bypass **filters** to upload **web shells** via **null bytes, double extensions, MIME confusion**.

- [ ] **Deserialization Attacks:** Exploit **unsafe deserialization** in Java/Python/PHP for RCE.

- [ ] **XXE & SSTI:** Parse **malicious XML** for file read; exploit **template engines** (Jinja2, Twig) for code execution.

---

### **Stage 4: Post-Exploitation & Persistence**

_Goal: Maintain access and pivot deeper._

- [ ] **Web Shell Management:** Deploy **persistent web shells** (PHP, ASPX, JSP) in writable directories.

- [ ] **Database Enumeration:** Extract **credentials, PII, business data** via SQL injection or direct access.

- [ ] **Lateral Movement:** Use compromised web app to **pivot to internal network, access cloud metadata (IMDS), enumerate AWS/Azure resources**.

- [ ] **Data Exfiltration:** Exfil via **DNS, HTTPS covert channels, cloud storage APIs**.

---

### **Stage 5: Defense & Mitigation (The Shield)**

_Goal: Prevent and detect these attacks._

- [ ] **WAF Deployment:** Implement **Web Application Firewall** (ModSecurity, CloudFlare WAF, AWS WAF) with custom rules.

- [ ] **Secure Coding:** Use **parameterized queries, input validation, output encoding, CSP headers** to prevent injections.

- [ ] **Strong Authentication:** Require **MFA/2FA, strong password policies, account lockout, CAPTCHA** after failed attempts.

- [ ] **Security Headers:** Implement **CSP, X-Frame-Options, HSTS, X-Content-Type-Options** to mitigate client-side attacks.

- [ ] **Continuous Monitoring:** Deploy **SIEM, web server logging, intrusion detection** to identify attack patterns.

<a id="toc-part-18-web-server-hacking"></a>
## Part 18: Web Server Hacking

### **Stage 1: Target Acquisition & Reconnaissance**

_Goal: Identify the target server and gather intelligence._

- [ ] **OSINT Gathering:** Conduct **Reconnaissance** using **WHOIS, DNS enumeration, Certificate Transparency** to identify IP ranges and domain information.

- [ ] **Network Mapping:** Determine the server's network position via **traceroute, OSINT**; identify if it's in **Perimeter, DMZ, or internal** segments.

- [ ] **Historical Analysis:** Use **Wayback Machine, Shodan history** to identify previous exposures and configuration changes.

---

### **Stage 2: Scanning & Service Enumeration**

_Goal: Map out the server's attack surface._

- [ ] **Port Scanning:** Use `nmap -sS -sV -sC -p-` to discover **all open ports** and identify services (Apache, Nginx, IIS, Tomcat, SSH, FTP, DB).

- [ ] **Banner Grabbing:** Use **curl, nc, telnet** to grab service banners and identify **software versions, OS fingerprints**.

- [ ] **HTTP Method Enumeration:** Test for **PUT, DELETE, TRACE, OPTIONS** enabled; check **WebDAV** misconfiguration.

- [ ] **Protocol Audit:** Check for **insecure protocols (HTTP, FTP, Telnet)**; analyze **TLS** config with **testssl.sh** for weak ciphers.

- [ ] **Virtual Host Discovery:** Enumerate **vhosts** via **Host header manipulation, DNS brute-forcing** to find hidden services.

---

### **Stage 3: Vulnerability Assessment & Exploitation**

_Goal: Find and exploit flaws to gain initial access._

- [ ] **Patch Audit:** Check for **outdated software versions** against CVE databases; test for **known exploits** (Apache Struts, IIS 6.0, etc.).

- [ ] **Web Application Attacks:** Attempt **SQL injection, XSS, file upload** against hosted applications to compromise the web server.

- [ ] **File System Attacks:** Test for **directory traversal** (`../../../etc/passwd`), **LFI/RFI**, **arbitrary file read**.

- [ ] **Service Exploitation:** Look for **buffer overflow, format string, RCE** exploits for specific service versions (Apache mod_ssl, ProFTPd, vsftpd).

- [ ] **Credential Attacks:** Launch **brute force, password spray, dictionary attacks** against **SSH, FTP, admin panels** with Hydra/Medusa.

- [ ] **Default Credentials:** Test **default admin passwords** for web servers (tomcat/tomcat, admin/admin) and management interfaces.

---

### **Stage 4: Post-Exploitation & Persistence**

_Goal: Escalate privileges and maintain control._

- [ ] **Privilege Escalation:** After gaining low-privilege shell, use **kernel exploits, SUID binaries, sudo misconfigs, service misconfigurations** for root/SYSTEM.

- [ ] **Web Shell Deployment:** Upload **persistent web shells** (b374k, c99, webacoo) to writable web directories for backdoor access.

- [ ] **Living off the Land:** Utilize **LOLBAS (Windows)** or **GTFOBins (Linux)** to execute commands and maintain persistence via **cron jobs, scheduled tasks, startup scripts**.

- [ ] **Credential Harvesting:** Dump **database credentials, config files** (`web.config`, `wp-config.php`), **SSH keys** for lateral movement.

- [ ] **Covering Tracks:** Clear **access logs, error logs, auth logs**; use **timestomping** to hide file modifications.

<a id="toc-part-19-api-security"></a>
## Part 19: API Security

### **Stage 1: API Reconnaissance & Mapping**

_Goal: Discover and map API attack surface._

- [ ] **API Discovery:** Find undocumented endpoints via **JS file analysis, Wayback Machine, Google Dorks (`site:target.com api`), Shodan**, and **Burp Suite passive crawling**.

- [ ] **Spec File Harvesting:** Locate exposed **OpenAPI/Swagger (`/swagger.json`, `/api-docs`), WSDL, GraphQL introspection** schemas that reveal all routes, parameters, and data models.

- [ ] **Endpoint Enumeration:** Fuzz **API paths and versions** (`/api/v1/`, `/api/v2/`, `/v3/`) using **ffuf, kiterunner, Arjun** with API-specific wordlists.

- [ ] **Technology Fingerprinting:** Identify **framework, auth scheme, rate limiting, versioning strategy** from headers, response patterns, and error messages.

---

### **Stage 2: OWASP API Security Top 10**

_Goal: Methodically test each API-specific vulnerability class._

- [ ] **API1 — Broken Object Level Authorization (BOLA/IDOR):** Substitute **object IDs** (user, order, account) in requests to access **other users' resources** without authorization check.

- [ ] **API2 — Broken Authentication:** Test **weak tokens, missing expiry, no rate limiting on login, JWT algorithm confusion (`alg:none`), token reuse after logout**.

- [ ] **API3 — Broken Object Property Level Authorization (BOPLA):** Send **extra fields** in PUT/PATCH requests to modify properties the user shouldn't control (e.g., `"role":"admin"`, `"is_verified":true`).

- [ ] **API4 — Unrestricted Resource Consumption:** Test **missing rate limits, no pagination caps, large payload DoS, CPU-exhausting regex/query parameters**.

- [ ] **API5 — Broken Function Level Authorization (BFLA):** Access **admin-only endpoints** (`/api/admin/users`, `/api/internal/`) using **regular user tokens**; test HTTP method switching (GET → DELETE).

- [ ] **API6 — Unrestricted Access to Sensitive Business Flows:** Abuse **checkout flows, invite systems, voting, coupon redemption** without rate limiting or workflow enforcement.

- [ ] **API7 — Server-Side Request Forgery (SSRF):** Supply **internal URLs, cloud metadata endpoints** (`169.254.169.254`) as API parameters for internal network pivoting.

- [ ] **API8 — Security Misconfiguration:** Find **exposed debug endpoints, verbose errors, missing CORS restrictions, HTTP instead of HTTPS, default API keys**.

- [ ] **API9 — Improper Inventory Management:** Target **deprecated API versions, shadow APIs, staging/dev endpoints** still accessible in production.

- [ ] **API10 — Unsafe Consumption of APIs:** Exploit **third-party API data** that is trusted and processed without validation, causing **injection or SSRF** on the consuming server.

---

### **Stage 3: Protocol-Specific API Attacks**

_Goal: Attack REST, GraphQL, gRPC, and SOAP distinctly._

- [ ] **REST API Testing:** Chain **BOLA + privilege escalation**, test **HTTP verb tampering**, exploit **mass assignment** via undocumented writable fields.

- [ ] **GraphQL Attacks:** Run **introspection queries** to dump full schema; exploit **batching/aliasing for DoS**, **nested query depth abuse**, **IDOR via node IDs**, and **mutations without auth checks**.

- [ ] **gRPC Security:** Use **grpcurl, Evans** to enumerate services; test for **missing auth interceptors, reflection enabled in prod, proto injection**.

- [ ] **SOAP/XML APIs:** Exploit **XXE via SOAP body**, test **WS-Security header bypass**, abuse **type confusion in XML parsing**.

---

### **Stage 4: API Authentication & Token Attacks**

_Goal: Break API authentication mechanisms._

- [ ] **JWT Attacks:** Test **`alg:none` bypass, RS256→HS256 confusion, weak secret brute-force (hashcat mode 16500), kid injection, jku/x5u header injection** to forge arbitrary tokens.

- [ ] **OAuth 2.0 Attacks:** Exploit **CSRF on authorization endpoint, open redirect in redirect_uri, state parameter bypass, token leakage via Referer header**.

- [ ] **API Key Attacks:** Find **keys in JS bundles, git history, response headers, error messages**; test **key rotation absence, missing key scoping**.

- [ ] **mTLS Bypass:** Identify **endpoints that skip client certificate validation**, abuse **certificate pinning gaps**, exploit **proxy stripping of client certs**.

---

### **Stage 5: Defense & Hardening**

_Goal: Know what defenders implement so you can test it properly._

- [ ] **API Gateway Controls:** Understand **rate limiting, quota enforcement, request validation, JWT verification, IP allowlisting** at the gateway layer.

- [ ] **Input Validation:** Test that **schema validation, type enforcement, max length, allowed values** are enforced server-side not just client-side.

- [ ] **Logging & Monitoring:** Verify **all API calls are logged** with enough context (user, IP, endpoint, response code) for anomaly detection.

---

<a id="toc-part-20-bug-bounty-and-penetration-testing"></a>
## Part 20: Bug Bounty and Penetration Testing

### **Stage 1: Preparation & Scoping**

_Goal: Stay legal and define the target._

- [ ] **Legal Check:** Read and sign the `Penetration Testing Rules of Engagement` or the Bug Bounty Policy (Safe Harbor).

- [ ] **Scope Validation:** Confirm IP ranges and domains. Ensure you are not attacking "Out of Scope" assets.

- [ ] **Framework Selection:** Decide if you are testing against `NIST`, `ISO`, or `OWASP10` standards.

---

### **Stage 2: Reconnaissance (The Wide Net)**

_Goal: Find what others missed._

- [ ] **Subdomain Enumeration:** Use **OSINT** tools to find `dev`, `stage`, or `test` subdomains.

- [ ] **Port Scanning:** Run `nmap` to identify non-standard ports (e.g., 8080, 8443) and running services.

- [ ] **Tech Stack Analysis:** Use `curl` or browser extensions to identify the server, framework (React, Angular), and backend (PHP, Python).

---

### **Stage 3: Vulnerability Assessment (The Deep Dive)**

_Goal: Find the flaw._

- [ ] **Input Fuzzing:** Test all input fields for `SQL Injection`, `XSS`, and `Buffer Overflow`.

- [ ] **Access Control:** Test for `IDOR` (Insecure Direct Object Reference) and verify `Authentication vs Authorization` logic.

- [ ] **Configuration Check:** Look for `Directory Traversal`, exposed `.git` folders, or default credentials (`admin/admin`).

---

### **Stage 4: Exploitation & Validation**

_Goal: Prove the risk without breaking the system._

- [ ] **PoC Development:** Create a non-destructive Proof of Concept. (e.g., `alert(1)` for XSS, `whoami` for RCE).

- [ ] **False Positive Check:** Verify the finding is a `True Positive` before reporting.

- [ ] **Lateral Movement:** (Pentest only) Attempt `Privilege Escalation` or `Pass the Hash` if internal access is achieved.

---

### **Stage 5: Reporting & Triage**

_Goal: Get paid and drive remediation._

- [ ] **Impact Assessment:** Clearly explain **business risk** (data breach, financial loss, compliance violation) to management.

- [ ] **Proof of Concept:** Provide **detailed steps, screenshots, videos, request/response** to reproduce the vulnerability.

- [ ] **Remediation Guidance:** Offer **specific technical fixes** (parameterized queries, input validation, patching) with code examples.

- [ ] **CVSS Scoring:** Calculate **CVSS score** to quantify severity and prioritize remediation.

---

### **Stage 6: Professional Development**

_Goal: Build skills and reputation._

- [ ] **Platform Selection:** Focus on **HackerOne, Bugcrowd, Synack, Intigriti** platforms with active programs.

- [ ] **Specialization:** Develop expertise in **specific areas** (API security, mobile, cloud, blockchain).

- [ ] **Documentation:** Maintain **personal writeups, CVEs, Hall of Fame entries** for portfolio building.

- [ ] **Community Engagement:** Participate in **CTFs, conferences, Twitter/Discord security communities** for networking.

- [ ] **Continuous Learning:** Stay updated on **latest vulnerabilities, techniques, tools** through blogs, research papers, trainings.

---

<a id="toc-part-21-wireless-pentesting"></a>
## Part 21: Wireless Pentesting

> **Safety Gate:** RF testing must stay inside legal spectrum rules and authorized lab targets. Use your own access points, Faraday isolation where appropriate, low power settings, and written permission. GPS jamming/spoofing and unauthorized wireless interference can create real-world safety issues.

### **Stage 1: RF Reconnaissance & Setup**

_Goal: Map the airspace and identify targets._

- [ ] **Monitor Mode:** Configure hardware to capture raw 802.11 frames.

- [ ] **Protocol Audit:** Identify the target's encryption: **WPA vs WPA2 vs WPA3 vs WEP**. Note that WEP is obsolete but trivial to crack; WPA3 is resistant to dictionary attacks.

- [ ] **WPS Check:** Scan for **WPS** enabled APs. If active, this is the primary high-value target for PIN brute-forcing (Pixie Dust).

---

### **Stage 2: Access Point Assault (The Breaching of Keys)**

_Goal: Obtain the credentials to join the network._

- [ ] **Handshake Capture:** Execute a **Deauth Attack** against a connected client to force a reconnection and capture the 4-way handshake.

- [ ] **Replay Attacks:** (For legacy/WEP) Use **Replay Attack** techniques to generate traffic and accelerate IV collection for cracking.

- [ ] **Offline Cracking:** Run the captured handshake against wordlists using Hashcat/Aircrack-ng.

---

### **Stage 3: Enterprise & Client Attacks (The Man-in-the-Middle)**

_Goal: Steal individual user identities or hijack connections._

- [ ] **Evil Twin Deployment:** Launch an **Evil Twin** attack to impersonate the target SSID. Use a captive portal to harvest credentials.

- [ ] **Enterprise Stripping:** Target **EAP vs PEAP** configurations. Downgrade encryption or crack the challenge-response hashes (MSCHAPv2) captured from the Evil Twin.

- [ ] **Rogue AP:** Plant a **Rogue Access Point** physically in the facility to create an unauthorized backdoor into the LAN.

- [ ] **KRACK Attack:** Exploit **Key Reinstallation Attack** against WPA2 to decrypt traffic (requires client participation, patches available).

- [ ] **PMKID Attack:** Extract **PMKID** from unassociated clients for offline cracking (faster than 4-way handshake, works against WPA2/WPA3).

---

### **Stage 4: Bluetooth & BLE Attacks**

_Goal: Compromise Bluetooth connections and devices._

- [ ] **BLE Fundamentals:** Understand **Bluetooth Low Energy** (BLE) **GATT/GAP, advertising, pairing mechanisms, security modes**.

- [ ] **Bluejacking:** Send **unsolicited messages** to BLE devices (informational, not harmful, for PoC).

- [ ] **Bluesnarfing:** Gain **unauthorized access** to BLE device data (contacts, calendar, files).

- [ ] **KNOB Attack:** Exploit **Key Negotiation of Bluetooth** to negotiate weak encryption keys.

- [ ] **BLE Pairing Bypass:** Exploit **weak pin/oob verification** or perform **man-in-the-middle attacks** on pairing to intercept keys.

- [ ] **Bluetooth Eavesdropping:** Use tools like **ubertooth, Proxmark** to capture Bluetooth packets and attempt decryption.

---

### **Stage 5: Zigbee, Z-Wave & IoT Attacks**

_Goal: Compromise smart home and industrial IoT networks._

- [ ] **Zigbee Basics:** Understand **Zigbee mesh networking, 802.15.4 radio, AES-128 encryption, default keys**.

- [ ] **Zigbee Sniffing:** Use **USRP, cc2531 dongles** to capture **Zigbee traffic** and extract **network keys** from initial joins.

- [ ] **Zigbee Replay:** Capture and replay **legitimate frames** to trigger device actions (turn lights on/off, unlock).

- [ ] **Z-Wave Attacks:** Exploit **Z-Wave security flaws** (obsolete S0, weak S2 implementations) to hijack devices.

- [ ] **Default Credentials:** Test **Zigbee/Z-Wave hubs** for **default passwords, backdoor accounts**.

- [ ] **Firmware Extraction:** Dump **device firmware** via **UART, JTAG** to find **hardcoded keys or vulnerabilities**.

---

### **Stage 6: NFC & RFID Attacks**

_Goal: Compromise Near-Field Communication and passive identification systems._

- [ ] **NFC Basics:** Understand **ISO14443-A/B, Mifare protocols, Type 1-4 tags, Android NFC API**.

- [ ] **NFC Cloning:** Extract **NFC card data** using **Proxmark, ACR122U** and write to **blank cards/tags**.

- [ ] **NFC Relay Attack:** Set up **two NFC readers** at distance to **relay communication** between reader and card (e.g., contactless payment fraud).

- [ ] **RFID Spoofing:** Craft **malicious RFID tags** to bypass access control readers (badges, building entry).

- [ ] **RFID Skimming:** Read **unencrypted RFID tags** from distance using **passive readers** (passport, credit card cloning).

- [ ] **ISO7816 Smartcard Attacks:** Understand **smartcard protocols** and exploit **weak implementations, timing attacks, power analysis**.

---

### **Stage 7: GPS & Satellite Spoofing**

_Goal: Manipulate location services and navigation._

- [ ] **GPS Basics:** Understand **GPS signal structure, GNSS systems (GPS/GLONASS/Galileo), pseudoranges, civilian vs military**.

- [ ] **GPS Spoofing:** Use **USRP or GPS simulators** to transmit **fake GPS signals** and cause devices to report false locations.

- [ ] **GPS Jamming:** Transmit **noise** on **L1 frequency (1575.42 MHz)** to deny GPS service (illegal but demonstrable in lab).

- [ ] **Satellite Communication Hacking:** Understand **Inmarsat, Iridium, Globalstar satellites**; identify **ground stations** for signal theft.

- [ ] **Drone GPS Hijacking:** Spoof **drone GPS** to cause drift, return-to-home corruption, or loss of control.

---

### **Stage 8: SDR & Spectrum Analysis**

_Goal: Understand software-defined radio and RF reconnaissance._

- [ ] **SDR Fundamentals:** Know tools like **USRP, HackRF, BladeRF** and frameworks like **GNU Radio, CubicSDR**.

- [ ] **Spectrum Scanning:** Use **spectrum analyzers** to identify **active RF signals, frequency bands, modulation types**.

- [ ] **Signal Demodulation:** Demodulate **AM, FM, FSK, PSK, QPSK** signals and extract **data streams**.

- [ ] **Cellular Eavesdropping:** Understand **2G/3G/4G/5G protocols** and attempt to capture **downlink signals** (law enforcement only in licensed contexts).

- [ ] **Protocol Fuzzing:** Use **GrFuzz, AFLplusplus** to fuzz **RF protocols** and find **unexpected states or crashes**.

---

### **Stage 9: Defense & Hardening (The Shield)**

_Goal: Secure the airwaves._

- [ ] **Protocol Hardening:** Migrate all APs to **WPA3 (SAE)** to mitigate handshake cracking; disable **WPS** immediately.

- [ ] **Certificate Enforcement:** For **EAP/PEAP** networks, enforce **server certificate validation** on all client devices to neutralize **Evil Twin** attacks.

- [ ] **Wireless IPS:** Deploy **WIDS/WIPS** sensors to detect **deauth attacks, rogue APs, evil twins, unusual RF patterns**.

- [ ] **Network Segmentation:** Isolate wireless networks via **VLANs, guest networks**; implement **802.1X authentication** for enterprise.

- [ ] **Physical Security:** Secure AP placement to prevent **physical tampering, rogue AP installation**; use **tamper-evident seals**.

---

<a id="toc-part-22-mobile-platform-pentesting"></a>
## Part 22: Mobile Platform Pentesting

### **Stage 1: Lab Setup & Reconnaissance**

_Goal: Prepare the environment and understand the target._

- [ ] **Environment Prep:** Configure a Rooted (Android) or Jailbroken (iOS) device to bypass **Operating System Hardening**.

- [ ] **Binary Acquisition:** Extract the APK or IPA and perform **Basics of Reverse Engineering** using tools like `jadx` or `Ghidra`.

- [ ] **Reconnaissance:** Map the app's attack surface (activities, services, URL schemes) and identify backend endpoints.

---

### **Stage 2: Static Analysis (Code Review)**

_Goal: Find hardcoded secrets and configuration flaws._

- [ ] **Manifest/Plist Audit:** Check for exported components or insecure permissions that violate **Zero Trust** principles.

- [ ] **Secret Hunting:** Search decompiled code for **Key Exchange** material, API tokens, or hardcoded credentials.

- [ ] **Crypto Audit:** Verify if the app uses weak **Hashing** or **Salting** algorithms for local storage.

---

### **Stage 3: Dynamic Analysis (Runtime Manipulation)**

_Goal: Bypass client-side controls._

- [ ] **Security Control Bypass:** Use Frida to bypass Root Detection and SSL Pinning (breaking the **SSL vs TLS** trust chain).

- [ ] **Logic Manipulation:** Hook functions to bypass **Authentication vs Authorization** checks (e.g., bypassing a PIN screen).

- [ ] **Memory Dumping:** Analyze device memory for sensitive data that should have been cleared (violating **Confidentiality** in the **CIA Triad**).

---

### **Stage 4: Network & API Attacks**

_Goal: Compromise the backend server._

- [ ] **Traffic Interception:** Proxy traffic to analyze **Secure vs Unsecure Protocols** and payload structures.

- [ ] **API Vulnerability Testing:** Test backend endpoints for **OWASP10** vulnerabilities like **SQL Injection**, **IDOR**, and **Broken Access Control**.

- [ ] **Session Management:** Test for weak **Session ID** generation or lack of **MFA & 2FA** on the mobile endpoints.

---

### **Stage 5: Local Data Storage & Defense**

_Goal: Assess data at rest security._

- [ ] **Insecure Storage Check:** Inspect local files (**SQLite, SharedPreferences, Plist, Keychain**) for unencrypted **PII, credentials, API keys**.

- [ ] **Log Analysis:** Check system **logs (Logcat/Syslog)** for sensitive data leakage during app usage.

- [ ] **Backup Analysis:** Extract and analyze **iOS/Android backups** for sensitive data exposure.

---

### **Stage 6: Defense & Secure Development**

_Goal: Build security into mobile apps._

- [ ] **Secure Storage:** Use **Android Keystore, iOS Keychain** for sensitive data; encrypt local databases.

- [ ] **Certificate Pinning:** Implement **SSL/certificate pinning** to prevent MITM attacks.

- [ ] **Code Obfuscation:** Use **ProGuard (Android), Swift obfuscation** to hinder reverse engineering.

- [ ] **Runtime Protection:** Implement **root/jailbreak detection, debugger detection, integrity checks**.

- [ ] **Secure Communication:** Enforce **TLS 1.2+**, validate **certificates**, use **certificate pinning** for API calls.

---

<a id="toc-part-23-active-directory--entra-id"></a>
## Part 23: Active Directory & Entra ID

### **Stage 1: Discovery & Enumeration**

_Goal: Map identity surfaces across on-prem AD and Entra ID (Azure AD)._

- [ ] **Domain Recon:** Enumerate **domains/forests, trusts, sites, subnets, FSMO roles**; collect **OU/Group/ACL** data.

- [ ] **Identity Inventory:** List **users, computers, service accounts, Tier0 assets, SPNs**, and **LAPS** posture.

- [ ] **Policy & Exposure:** Audit **GPOs, login scripts, startup tasks**, and **Unconstrained/Constrained/RBCD** exposure.

- [ ] **Entra ID/Cloud Recon:** Enumerate **tenants, apps, service principals, consented permissions, conditional access** and **enterprise apps**.

---

### **Stage 2: Credential & Auth Attacks**

_Goal: Steal or replay credentials to gain higher privilege._

- [ ] **Kerberoast / AS-REP Roast:** Extract **TGS/AS-REP** tickets for offline cracking; prioritize **high-priv SPNs**.

- [ ] **NTLM Relay/SMB/HTTP:** Abuse **NTLM relays** against **SMB/LDAP/HTTP/ADCS HTTP endpoints**; combine with **mTLS gaps**.

- [ ] **Token Abuse:** Steal **TGT/TGS, DPAPI, LSASS, browser tokens**, and **OAuth refresh tokens** across hybrid joins.

- [ ] **Password Hygiene:** Spray with **safe lockout windows**, target **legacy auth (POP/IMAP/SMTP)**, and downgrade to **basic auth** where possible.

---

### **Stage 3: Delegation, ACL, and ADCS Abuse**

_Goal: Abuse trust relationships and misconfigurations for escalation._

- [ ] **Delegation Abuse:** Exploit **Unconstrained, Constrained (service/alt service), and Resource-Based Constrained Delegation (RBCD)** for impersonation.

- [ ] **ACL/ACE Abuse:** Exploit **WriteOwner, WriteDACL, GenericAll/GenericWrite, AddMember** on critical principals (DA, EA, DCs, Tier0 groups).

- [ ] **Shadow Credentials:** Abuse **msDS-KeyCredentialLink** to add rogue keys for persistence.

- [ ] **ADCS (PKI) Abuse:** Exploit **ESC1-ESC8** templates (ENROLLEE_SUPPLIES_SUBJECT, weak EKUs, SAN impersonation) to mint **golden certs**; target **HTTP enrollment endpoints** for relays.

---

### **Stage 4: Lateral Movement & Persistence**

_Goal: Move horizontally and maintain footholds._

- [ ] **Lateral Paths:** Use **WinRM/SMB/RDP/WMI/PowerShell Remoting**, **admin shares**, and **task/svc installs** guided by **BloodHound** paths.

- [ ] **GPO Persistence:** Implant via **logon scripts, immediate scheduled tasks, startup items**; abuse **restricted groups** for re-add.

- [ ] **DC Sync / DC Shadow:** Abuse **Replicating Directory Changes** to pull **NTDS.dit** or inject rogue DC changes.

- [ ] **Golden/Silver Tickets:** Forge **krbtgt/service hashes** for long-lived access; manage **ticket lifetime/renewal** OPSEC.

---

### **Stage 5: Entra ID (Azure AD) & Hybrid Attacks**

_Goal: Exploit cloud identity to pivot and persist._

- [ ] **Consent & OAuth Abuse:** Steal or register **malicious multi-tenant apps**, abuse **illicit consent grants**, and persist via **refresh tokens**.

- [ ] **Conditional Access Bypass:** Exploit **trusted locations, device compliance gaps, legacy auth exemptions**, and **MFA registration weaknesses**.

- [ ] **Passwordless/Passkeys:** Target **FIDO2/Passkey registration flows**, backup methods, and **SSPR** to hijack accounts.

- [ ] **Cross-Cloud Pivot:** Use **Entra app roles** and **federation trusts** to pivot into **AWS/GCP** integrations; harvest **Graph/SharePoint** data for lateral move.

---

### **Lab Progression**

_Goal: Build and attack identity infrastructure with evidence and rollback._

- [ ] **AD Lab Build:** Deploy a domain controller, at least one workstation, DNS, domain users/groups, and basic GPOs.
- [ ] **Vulnerable AD Lab:** Use GOAD, DetectionLab, PurpleCloud, or a self-built intentionally weak domain to practice safely.
- [ ] **BloodHound Lab:** Ingest data, identify attack paths, validate one path in the lab, then write the remediation.
- [ ] **Kerberos Lab:** Perform lab-only AS-REP roasting/Kerberoasting and crack only synthetic passwords created for the exercise.
- [ ] **Entra ID Lab:** Create test users, app registrations, conditional access policies, and sign-in logs; document identity detections.
- [ ] **Move-On Gate:** Produce an AD/Entra attack-path report with screenshots, graph evidence, event IDs, and hardening steps.

<a id="toc-part-24-cloud-computing"></a>
## Part 24: Cloud Computing

### **Stage 1: Architecture & Governance**

_Goal: Define the battlefield and the rules of engagement._

- [ ] **Model Selection:** Select the correct `Cloud Models` (`Public`, `Private`, `Hybrid`) based on data sensitivity.

- [ ] **Responsibility Mapping:** Apply the **Shared Responsibility Model** based on the service type (`IaaS`, `PaaS`, `SaaS`) to identify what you must secure vs. the provider.

- [ ] **Environment Setup:** Initialize the tenant in a `Common Cloud Environment` (`AWS`, `GCP`, or `Azure`) with a secure root account setup.

---

### **Stage 2: Storage & Data Security**

_Goal: Lock down the data assets._

- [ ] **Object Storage Security:** Audit `S3` buckets and `Common Cloud Storage` (Drive, Box) for public access and enforce encryption.

- [ ] **Access Control:** Implement strict IAM policies ensuring only authorized identities can access storage blobs.

---

### **Stage 3: Modern Infrastructure & Deployment**

_Goal: Secure the compute and the pipeline._

- [ ] **Code-Defined Security:** Use `Infrastructure as Code` (IaC) to template firewalls and permissions, preventing human configuration errors.

- [ ] **Serverless Hardening:** Secure `Serverless` functions by minimizing privileges and auditing dependencies for vulnerabilities.

- [ ] **Pipeline Security:** Audit the `general flow of deploying in the cloud` to ensure secrets (API keys) are not hardcoded in the deployment scripts.

---

### **Stage 4: Automation & Scripting**

_Goal: Automate defense and auditing._

- [ ] **Cloud Automation:** Use **Python (Boto3), Terraform, CloudFormation** to audit security groups and IAM roles automatically.

- [ ] **Admin Scripting:** Master **Bash, PowerShell, AWS CLI, Azure CLI** to manage instances and automate operations.

- [ ] **CI/CD Security:** Integrate **security scanning** (SAST, DAST, dependency checks) into deployment pipelines.

---

### **Stage 5: Cloud-Specific Attack Vectors**

_Goal: Understand unique cloud threats._

- [ ] **IAM Exploitation:** Abuse **overprivileged roles, AssumeRole chains, resource-based policies** for privilege escalation.

- [ ] **Storage Misconfigurations:** Find **public S3 buckets, blob containers** via enumeration and exploitation.

- [ ] **Metadata Services:** Query **IMDS (169.254.169.254)** for IAM credentials, instance metadata.

- [ ] **Serverless Attacks:** Exploit **Lambda environment variables, excessive permissions, function injection**.

- [ ] **Container Escapes:** Break out of **Docker, Kubernetes pods** via misconfigurations.

- [ ] **Multi-Tenancy Issues:** Understand **side-channel attacks, resource exhaustion** in shared cloud environments.

---

<a id="toc-part-25-container--orchestration-security"></a>
## Part 25: Container & Orchestration Security

### **Stage 1: Container Fundamentals & Attacks**

_Goal: Understand containerization and its security implications._

- [ ] **Container Anatomy:** Master **namespaces, cgroups, capabilities, seccomp, AppArmor/SELinux** as isolation mechanisms.

- [ ] **Image Vulnerabilities:** Scan images with **Trivy, Clair, Grype** for **CVEs, secrets, misconfigs** in layers.

- [ ] **Dockerfile Security:** Audit **Dockerfiles** for **running as root, exposed secrets, vulnerable base images, unnecessary packages**.

- [ ] **Container Escape:** Exploit **--privileged flag, CAP_SYS_ADMIN, mounted docker.sock, kernel exploits** to break out to host.

- [ ] **Docker API Exploitation:** Abuse **exposed Docker API (2375/2376)** to spawn privileged containers and compromise host.

---

### **Stage 2: Kubernetes Security**

_Goal: Attack and defend container orchestration platforms._

- [ ] **K8s Architecture:** Understand **control plane (API server, etcd, scheduler)** vs **data plane (kubelet, kube-proxy)** components.

- [ ] **RBAC Exploitation:** Abuse **overprivileged service accounts, role bindings, cluster-admin** for privilege escalation.

- [ ] **Pod Escape:** Break out via **hostPath mounts, hostNetwork, hostPID, privileged pods** to access host filesystem.

- [ ] **Secrets Extraction:** Steal **Kubernetes secrets** from **etcd, mounted volumes, environment variables, service account tokens**.

- [ ] **API Server Abuse:** Exploit **unauthenticated API, certificate theft, kubeconfig exposure** for cluster control.

- [ ] **Network Policy Bypass:** Pivot through **missing network policies** to access isolated pods and services.

---

### **Stage 3: Container Runtime Security**

_Goal: Detect and prevent malicious container activity._

- [ ] **Runtime Monitoring:** Deploy **Falco, Sysdig, Aqua** to detect **suspicious syscalls, process execution, network connections**.

- [ ] **Admission Control:** Use **OPA (Open Policy Agent), Kyverno** to enforce **security policies at admission time**.

- [ ] **Image Signing:** Implement **Notary, Cosign** for **image provenance verification** and supply chain security.

- [ ] **Runtime Protection:** Enable **seccomp profiles, AppArmor/SELinux policies** to restrict container capabilities.

- [ ] **Network Segmentation:** Deploy **Calico, Cilium** network policies to **microsegment pod-to-pod communication**.

---

### **Stage 4: Secrets & Configuration Management**

_Goal: Secure sensitive data in containerized environments._

- [ ] **Secret Stores:** Use **HashiCorp Vault, AWS Secrets Manager, Azure Key Vault** instead of K8s native secrets.

- [ ] **Init Containers:** Fetch secrets at **pod startup** via init containers instead of baking into images.

- [ ] **Sealed Secrets:** Encrypt secrets in Git using **Bitnami Sealed Secrets, SOPS** for GitOps workflows.

- [ ] **Workload Identity:** Use **cloud provider workload identity** (AWS IRSA, GCP Workload Identity) for keyless authentication.

- [ ] **Secret Rotation:** Implement **automatic secret rotation** and short-lived credentials.

---

### **Stage 5: CI/CD & Workflow Automation Attacks**

_Goal: Compromise the software supply chain and automation tier._

- [ ] **Pipeline Poisoning:** Inject malicious steps into **GitHub Actions/Jenkins** to alter builds, steal artifacts, or plant backdoors.

- [ ] **Dependency Confusion:** Publish **public packages** matching internal names to hijack build dependency resolution.

- [ ] **Workflow Takeover:** Exploit **workflow automation (n8n, Zapier, Workato)** misconfigs (e.g., **n8n CVE-2026-21858**) to pivot into **AWS/Azure**.

- [ ] **Credential Aggregation:** Treat automation platforms as **credential vaults**; dump **API keys, OAuth tokens, cloud creds** for lateral movement.

- [ ] **Build Artifact Integrity:** Enforce **signing (Sigstore/Cosign)** and **attestations (SLSA/Provenance)** to detect tampering.

---

### **Lab Progression**

_Goal: Practice container and Kubernetes security with real clusters, not diagrams._

- [ ] **Container Escape Awareness Lab:** Run a deliberately misconfigured container and document which Linux primitives made it unsafe: capabilities, mounts, namespaces, cgroups, seccomp, AppArmor/SELinux.
- [ ] **KubernetesGoat / k8s-ctf Lab:** Complete at least 5 Kubernetes attack scenarios and map each to a control failure.
- [ ] **Image Security Lab:** Build an image, scan it with Trivy/Grype, fix high-risk findings, and rebuild.
- [ ] **Secrets Lab:** Demonstrate unsafe secret exposure, then fix it using Kubernetes secrets, external secret managers, or workload identity.
- [ ] **Move-On Gate:** Produce a Kubernetes hardening report with RBAC, network policy, admission control, image scanning, and runtime detection notes.

<a id="toc-part-26-oticsscada-security"></a>
## Part 26: OT/ICS/SCADA Security

### **Stage 1: Industrial Protocol Fundamentals**

_Goal: Understand operational technology communication._

- [ ] **Modbus TCP/RTU:** Master **function codes (read coils, write registers)**, perform **unauthenticated reads/writes** to PLCs.

- [ ] **DNP3:** Understand **SCADA protocol** used in utilities; exploit **lack of authentication, replay attacks**.

- [ ] **IEC 61850:** Learn **power substation protocol**; understand **GOOSE messages, MMS** for substation automation.

- [ ] **BACnet:** Audit **building automation systems**; enumerate **devices, read/write points** without authentication.

- [ ] **OPC UA:** Exploit **OPC servers** for **data exfiltration, authentication bypass, denial of service**.

---

### **Stage 2: PLC & HMI Exploitation**

_Goal: Compromise industrial controllers and interfaces._

- [ ] **PLC Enumeration:** Use **Nmap NSE scripts, plcscan** to identify **Siemens S7, Allen-Bradley, Schneider** devices.

- [ ] **Ladder Logic Analysis:** Reverse engineer **PLC programs** to understand **control logic, safety interlocks**.

- [ ] **Firmware Manipulation:** Extract and modify **PLC firmware** to inject malicious logic or backdoors.

- [ ] **HMI Exploitation:** Exploit **HMI software vulnerabilities, default credentials, SQL injection** in SCADA interfaces.

- [ ] **Engineering Workstation:** Target **engineering stations** with **phishing, malware** as gateway to OT network.

---

### **Stage 3: Safety System Attacks**

_Goal: Understand attacks on critical safety instrumented systems._

- [ ] **Safety PLC:** Identify **safety-rated PLCs** and understand **fail-safe vs fail-operational** modes.

- [ ] **Interlock Bypass:** Manipulate **logic to disable safety interlocks** causing unsafe operational states.

- [ ] **Sensor Manipulation:** Spoof **sensor values** (temperature, pressure, level) to trigger incorrect responses.

- [ ] **Emergency Shutdown (ESD):** Understand **ESD systems** and potential for **malicious activation/deactivation**.

- [ ] **Physical Impact:** Assess **real-world consequences** of cyber attacks (equipment damage, safety incidents, environmental harm).

---

### **Stage 4: OT Network Segmentation & Defense**

_Goal: Implement defense-in-depth for industrial environments._

- [ ] **Purdue Model:** Apply **ISA-95/Purdue Enterprise Reference Architecture** for **zone-based segmentation**.

- [ ] **DMZ Architecture:** Deploy **data diodes, unidirectional gateways** to isolate OT from IT networks.

- [ ] **Protocol Whitelisting:** Use **industrial firewalls** to whitelist **allowed protocols, function codes, device communications**.

- [ ] **Anomaly Detection:** Deploy **OT-aware IDS (Claroty, Nozomi, Dragos)** to detect **protocol deviations, unauthorized commands**.

- [ ] **Asset Inventory:** Maintain **passive discovery** of all OT assets using **network taps, SPAN ports**.

- [ ] **Patch Management:** Implement **risk-based patching** with **change control, redundancy, rollback procedures**.

---

<a id="toc-part-27-digital-forensics"></a>
## Part 27: Digital Forensics

### **Stage 1: Preparation & First Response**

_Goal: Secure the scene without corrupting evidence._

- [ ] **Incident Identification:** Trigger the `Incident Response Process` upon `Identification` of a breach.

- [ ] **Volatile Collection:** Capture RAM immediately using `memdump` before the system is powered off or rebooted.

- [ ] **Static Acquisition:** Create a forensic image of hard drives using `FTK Imager` or `dd`, ensuring a write-blocker is used.

---

### **Stage 2: Evidence Analysis (The Deep Dive)**

_Goal: Find the needle in the haystack._

- [ ] **Disk Analysis:** Load the evidence into `autopsy` to recover deleted files, analyze web history, and search for keywords.

- [ ] **Binary Inspection:** Use `winhex` to manually inspect file headers (signatures) to identify files with changed extensions (e.g., an EXE renamed to JPG).

- [ ] **Log Review:** Correlate actions by analyzing `Event Logs` (Login times, Service installs) and `syslogs`.

---

### **Stage 3: Network Forensics**

_Goal: Trace the attacker's path._

- [ ] **Traffic Reconstruction:** Open `Packet Captures` in `wireshark` to find C2 communication, data exfiltration, or cleartext passwords.

- [ ] **Flow Analysis:** If full packets are missing, use `netflow` logs to identify connections to malicious IPs.

---

### **Stage 4: Advanced Analysis & Reporting**

_Goal: Understand the "How" and tell the story._

- [ ] **Malware Analysis:** Use **static/dynamic analysis, sandbox detonation, reverse engineering** to understand malware behavior and IOCs.

- [ ] **Timeline Construction:** Build **complete attack timeline** from artifacts (file timestamps, logs, registry, prefetch).

- [ ] **Anti-Forensics Detection:** Look for signs of **timestomping, log clearing, secure deletion, encryption** indicating sophisticated attacker.

- [ ] **Attribution Analysis:** Correlate **TTPs, IOCs, tools** with known threat actors using **MITRE ATT&CK, threat intelligence**.

---

### **Stage 5: Legal & Reporting**

_Goal: Present findings professionally._

- [ ] **Chain of Custody:** Maintain strict **evidence handling, documentation** for legal admissibility.

- [ ] **Technical Report:** Document **methodology, findings, evidence location, IOCs** for technical teams.

- [ ] **Executive Summary:** Translate technical findings into **business impact, risk assessment** for management.

- [ ] **Legal Coordination:** Work with **legal counsel, HR, law enforcement** on evidence disclosure and prosecution.

---

<a id="toc-part-28-reverse-engineering--malware-analysis"></a>
## Part 28: Reverse Engineering & Malware Analysis

### **Stage 1: Static Analysis Foundations**

_Goal: Analyze binaries without executing them._

- [ ] **File Identification:** Use **file, exiftool, DIE (Detect It Easy)** to identify **file type, architecture, compiler, packer** before loading into a disassembler.

- [ ] **PE/ELF/Mach-O Structure:** Master **executable format headers, sections (.text, .data, .rdata, .bss), import/export tables, relocation entries**, and **entry points**.

- [ ] **Disassembly Tools:** Develop proficiency in **Ghidra** (free) and **IDA Pro** (industry standard) for **disassembly, decompilation, cross-referencing, and function signature recognition**.

- [ ] **String Analysis:** Extract **hardcoded URLs, IPs, registry keys, API calls, encryption keys, error messages** using **strings, FLOSS (FLARE Obfuscated String Solver)**.

- [ ] **Import/Export Analysis:** Identify **suspicious API imports** (VirtualAlloc, CreateRemoteThread, WriteProcessMemory, InternetOpenUrl) that reveal **injection, download, or persistence behavior**.

- [ ] **Control Flow Analysis:** Trace **function call graphs, conditional branches, loops** to understand **program logic, decision points, and hidden functionality**.

- [ ] **.NET/Java Reversing:** Decompile **managed code** using **dnSpy, ILSpy** (.NET) or **JD-GUI, JADX, CFR** (Java/Android) for near-source-level analysis.

---

### **Stage 2: Dynamic Analysis & Debugging**

_Goal: Observe malware behavior during live execution._

- [ ] **Sandbox Execution:** Detonate samples in **isolated VMs** (FlareVM, REMnux) with **snapshots**; monitor using **Procmon, Process Hacker, Regshot, Wireshark, FakeNet-NG**.

- [ ] **Behavioral Indicators:** Document **file system changes, registry modifications, network connections, process creation, mutex creation, service installs** during execution.

- [ ] **Debugger Proficiency:** Master **x64dbg/x32dbg** (Windows) and **GDB with gef/pwndbg** (Linux) for **breakpoints, stepping, memory inspection, register manipulation**.

- [ ] **API Hooking & Tracing:** Use **API Monitor, Frida, strace/ltrace** to intercept and log **system calls and library calls** at runtime.

- [ ] **Memory Forensics During Execution:** Dump **process memory** with **Volatility, procdump** to find **decrypted payloads, injected code, unpacked stages** that only exist in RAM.

- [ ] **Network Traffic Analysis:** Capture **C2 communications, DNS queries, HTTP beacons, exfiltration attempts** using **Wireshark, mitmproxy, INetSim** during detonation.

---

### **Stage 3: Anti-Reverse Engineering & Evasion Techniques**

_Goal: Understand and defeat techniques malware uses to resist analysis._

- [ ] **Anti-Debugging:** Detect and bypass **IsDebuggerPresent, NtQueryInformationProcess, timing checks (RDTSC), int 2D/int 3, TLS callbacks** used to detect debuggers.

- [ ] **Anti-VM/Anti-Sandbox:** Identify checks for **VMware/VirtualBox artifacts (registry keys, MAC prefixes, CPUID), mouse movement, screen resolution, uptime, username** and patch them out.

- [ ] **Packing & Crypters:** Unpack **UPX, Themida, VMProtect, custom packers** using **manual unpacking (OEP finding, IAT reconstruction)** and automated tools.

- [ ] **Obfuscation:** Defeat **control flow flattening, dead code insertion, string encryption, opaque predicates** through **symbolic execution, pattern matching, and scripting**.

- [ ] **Code Virtualization:** Understand **VM-based protectors** (Themida, VMProtect) that translate code to **custom bytecode**; use **devirtualization techniques** and trace analysis.

---

### **Stage 4: Malware Classification & Threat Intelligence**

_Goal: Categorize malware and extract actionable intelligence._

- [ ] **Malware Taxonomy:** Classify samples as **RAT, ransomware, worm, rootkit, bootkit, stealer, loader, dropper, wiper, cryptominer, botnet agent** based on behavior.

- [ ] **IOC Extraction:** Extract **file hashes (MD5/SHA256), domains, IPs, URLs, mutexes, registry keys, YARA signatures** for threat intelligence sharing.

- [ ] **YARA Rule Writing:** Write **custom YARA rules** to detect malware families by **string patterns, byte sequences, file structure, import combinations**.

- [ ] **MITRE ATT&CK Mapping:** Map observed **malware behaviors** to **specific techniques/sub-techniques** for standardized reporting and detection engineering.

- [ ] **Campaign Attribution:** Correlate **code similarities, infrastructure overlaps, TTPs, timestamps, language artifacts** to link samples to **threat actor groups**.

---

### **Stage 5: Advanced RE & Automation**

_Goal: Scale analysis with scripting and handle complex targets._

- [ ] **Ghidra Scripting:** Write **Ghidra scripts (Java/Python)** to automate **function renaming, string decryption, pattern searching, cross-reference analysis**.

- [ ] **IDAPython:** Use **IDAPython scripts** for **bulk analysis, signature generation, automated deobfuscation, plugin development**.

- [ ] **Binary Diffing:** Use **BinDiff, Diaphora** to compare **patched vs. unpatched binaries** to identify **vulnerability patches and 1-day exploit targets**.

- [ ] **Emulation:** Use **Unicorn Engine, QEMU, Qiling** to **emulate code snippets** (decryption routines, shellcode) without full execution.

- [ ] **Firmware RE:** Apply RE skills to **embedded firmware** (binwalk extraction, architecture identification, cross-compilation debugging).

- [ ] **Kernel-Level RE:** Analyze **drivers, rootkits, bootkits** using **WinDbg kernel debugging, IDA with kernel symbols, Volatility memory analysis**.

---

### **Lab Progression**

_Goal: Build reverse-engineering muscle memory in a safe malware-analysis environment._

- [ ] **Lab Setup:** Deploy FLARE VM and REMnux in isolated VMs with snapshots and no shared folders.
- [ ] **Static Analysis Lab:** Analyze 5 benign or training binaries with strings, PE/ELF headers, imports, sections, and entropy.
- [ ] **Dynamic Analysis Lab:** Execute controlled samples in a sandbox and capture filesystem, registry, process, and network behavior.
- [ ] **Debugger Lab:** Use x64dbg/GDB to set breakpoints, step through functions, inspect stack/registers, and patch one branch in a toy binary.
- [ ] **YARA Lab:** Write 3 YARA rules for training samples and test false positives against clean files.
- [ ] **Move-On Gate:** Produce one malware-analysis-style report with IOCs, behavior summary, ATT&CK mapping, and detection logic.

<a id="toc-part-29-modern-exploitation"></a>
## Part 29: Modern Exploitation

### **Stage 1: Recon, Triage & Tooling**

_Goal: Prepare targets and environments for exploit development._

- [ ] **Binary Recon:** Identify **arch, compiler, protections (ASLR, DEP/NX, PIE, RELRO, Stack Canaries, CFG, CET/PAC/BTI)**.

- [ ] **Debug Setup:** Configure **GDB/gef/pwndbg, WinDbg, Frida**; obtain **symbols, PDBs, DWARF** where possible.

- [ ] **Fuzzing:** Use **AFL++, libFuzzer, honggfuzz, Peach**; seed corpora, add **sanitizers (ASan/UBSan/MSan)**; triage crashes.

---

### **Stage 2: Memory Exploitation (Userland)**

_Goal: Exploit memory-safety bugs under modern mitigations._

- [ ] **Buffer Overflows:** Master how data can overwrite adjacent memory to hijack the **EIP/RIP (Instruction Pointer)**; understand **stack vs heap overflows**.

- [ ] **Stack/Heap Primitives:** Develop **overflow, UAF, double-free, type confusion, OOB read/write** primitives.

- [ ] **Bypass Strategies:** Use **ROP/JOP/SROP, ret2libc, ret2dlresolve, stack pivoting**, and **heap grooming** (tcache/fastbin/largebin, LFH) to gain PC control.

- [ ] **Exploit Mitigations:** Study **ASLR** (Address Space Layout Randomization) and **DEP/NX** (Data Execution Prevention); master **ROP** (Return Oriented Programming) to bypass them. Learn **stack canary** bypass via leaks.

- [ ] **Mitigation Bypass:** Defeat **RELRO/PIE**, **CFG/CET/PAC/BTI** with **COOP, SIGRETURN, pointer authentication bypass**, or **JIT spraying**.

- [ ] **Sandbox Escape:** Target **browser/render sandboxes**, **container seccomp/AppArmor**, and **Win32k lockdown** using **IPC/shmem/race** primitives.

---

### **Stage 3: Advanced Targets**

_Goal: Move beyond basic binaries to complex environments._

- [ ] **Kernel Exploitation:** Leverage **UAF/race/logic bugs**, bypass **SMEP/SMAP/KASLR/KPTRR**, and use **token stealing/privilege escalation** primitives.

- [ ] **Browser & JS Engines:** Exploit **JIT/IC/GC** bugs; chain **type confusion → infoleak → RCE → sandbox escape**.

- [ ] **Deserialization & Logic:** Exploit **Java/.NET/Python/PHP** gadget chains, **serialization format** confusion, and **race conditions**.

- [ ] **Cloud/Serverless:** Abuse **function sandboxes, cold-start leaks, metadata services (IMDS), and SSRF-to-role** chains.

---

### **Stage 4: Exploit Delivery & OPSEC**

_Goal: Deliver and operate exploits stealthily._

- [ ] **Stagers & Payloads:** Build **stageless/staged** payloads with **in-memory loaders, reflective DLL/ELF**, and **syscall/indirect syscall** execution.

- [ ] **Evasion:** Apply **sleep obfuscation, call-stack spoofing, DLL hollowing, APC/ETW/AMSI tampering**, and **PPID spoofing**.

- [ ] **Crash Handling:** Implement **auto-retry, watchdogs, safe-fail** to avoid blue screens/service crashes.

- [ ] **Telemetry Shaping:** Throttle **network/beacon timing**, pad **packet sizes**, and mimic **legit protocol usage**.

---

### **Stage 5: Post-Exploitation Hardening & Safety**

_Goal: Maintain control while minimizing detection and impact._

- [ ] **Cleanup & Rollback:** Remove **artifacts, logs, crash dumps**, restore configs; support **idempotent rollback**.

- [ ] **Persistence Choices:** Select **low-noise persistence** (scheduled tasks, services, WMI events, cron/systemd timers) with **time-bounded lifetimes**.

- [ ] **Safety & Blast Radius:** Gate exploit use with **kill-switches, rate limits, environment checks**, and **canary endpoints** to avoid collateral damage.

---

### **Lab Progression**

_Goal: Approach exploitation with prerequisites, safety controls, and repeatable labs._

- [ ] **Assembly Gate:** Complete x86/x64 basics: registers, stack frames, calling conventions, `call`, `ret`, jumps, and memory layout.
- [ ] **pwn.college / ROP Emporium Lab:** Complete beginner shellcode, stack overflow, and ROP exercises before touching harder targets.
- [ ] **Fuzzing Lab:** Build a toy parser, fuzz it, crash it, triage the crash, and write a minimal proof of concept.
- [ ] **Mitigation Lab:** Demonstrate how NX, ASLR, stack canaries, PIE, and RELRO change exploitability.
- [ ] **Move-On Gate:** Produce one exploit writeup with root cause, crash analysis, exploit reliability notes, and mitigation guidance.

<a id="toc-part-30-hardware-hacking--embedded-systems"></a>
## Part 30: Hardware Hacking & Embedded Systems [OPTIONAL SPECIALIZATION]

### **Stage 1: Hardware Reconnaissance**

_Goal: Identify attack surface on physical devices._

- [ ] **Chip Identification:** Identify **MCU/SoC models** by reading chip markings; research **datasheets, known vulnerabilities**.

- [ ] **PCB Analysis:** Trace **PCB layouts** to identify **debug ports, test points, memory chips, communication buses**.

- [ ] **Debug Port Discovery:** Locate **JTAG, UART, SPI, I2C** interfaces using **multimeter, logic analyzer, JTAGulator**.

- [ ] **Pinout Mapping:** Use **oscilloscope** to identify **TX/RX pins, clock signals, voltage levels** on unknown headers.

- [ ] **Firmware Extraction:** Dump firmware via **debug interfaces, external flash chip reading, bootloader exploits**.

---

### **Stage 2: Firmware Analysis**

_Goal: Reverse engineer and find vulnerabilities in firmware._

- [ ] **Binary Extraction:** Use **binwalk** to extract **filesystems, compressed data, encryption keys** from firmware images.

- [ ] **Architecture Identification:** Determine **CPU architecture (ARM, MIPS, x86)** using **file, binwalk, Ghidra**.

- [ ] **Filesystem Analysis:** Mount extracted **SquashFS, JFFS2, UBIFS** to analyze **configs, credentials, certificates**.

- [ ] **Static Analysis:** Reverse engineer binaries with **Ghidra, IDA Pro, radare2** to find **buffer overflows, backdoors, hardcoded keys**.

- [ ] **Crypto Analysis:** Extract **encryption keys, certificates, private keys** from firmware for decryption or impersonation.

---

### **Stage 3: Runtime Exploitation**

_Goal: Execute code on live embedded systems._

- [ ] **UART Shell Access:** Connect to **UART** to gain **root shell, bootloader access, kernel logs**.

- [ ] **JTAG Debugging:** Use **OpenOCD, Segger J-Link** to **halt CPU, dump memory, modify registers, inject code**.

- [ ] **Bootloader Exploitation:** Exploit **U-Boot, grub** vulnerabilities to gain **pre-OS execution, modify boot parameters**.

- [ ] **Secure Boot Bypass:** Understand the mechanics used to load malicious, persistent bootloaders before OS security kicks in; master techniques like **boot chain manipulation, secure enclave exploitation, TPM/fTPM bypass**.

- [ ] **Memory Corruption:** Exploit **buffer overflows, format string bugs** in embedded applications.

- [ ] **Firmware Modification:** Patch firmware to **disable authentication, add backdoors, modify functionality**; reflash device.

---

### **Stage 4: Side-Channel & Physical Attacks**

_Goal: Extract secrets through non-traditional attack vectors._

- [ ] **Power Analysis:** Use **ChipWhisperer** for **simple/differential power analysis (SPA/DPA)** to extract encryption keys.

- [ ] **Electromagnetic Analysis:** Capture **EM emissions** during crypto operations to recover secrets.

- [ ] **Fault Injection:** Use **voltage glitching, clock glitching** to skip security checks or expose hidden functionality.

- [ ] **Chip Decapping:** Perform **acid decapping** to expose die for **optical inspection, probing, reverse engineering**.

- [ ] **Bus Snooping:** Intercept **SPI/I2C traffic** between chips to capture **flash contents, key exchange, commands**.

---

### **Stage 5: IoT & Embedded Defense**

_Goal: Secure embedded systems against attacks._

- [ ] **Secure Boot:** Implement **cryptographic boot chain verification** to prevent unauthorized firmware.

- [ ] **Debug Port Protection:** Disable or lock **JTAG/SWD** in production; use **debug authentication**.

- [ ] **Encrypted Firmware:** Encrypt firmware images; implement **secure firmware updates** with signature verification.

- [ ] **Tamper Detection:** Add **physical tamper switches, mesh overlays, epoxy coating** to detect intrusion.

- [ ] **Hardware Security Modules:** Use **TPM, secure elements (SE), TrustZone** for key storage and secure execution.

- [ ] **Code Signing:** Sign all firmware and application code; verify signatures before execution.

---

<a id="toc-part-31-password-cracking--hash-analysis"></a>
## Part 31: Password Cracking & Hash Analysis

### **Stage 1: Hash Identification & Acquisition**

_Goal: Identify what you have before cracking._

- [ ] **Hash Identification:** Use **hashid, hash-identifier, Name-That-Hash** to identify algorithm from hash format (length, prefix like `$2y$`, `$6$`, `$NT$`).

- [ ] **Hash Acquisition:** Obtain hashes from **SAM/NTDS.dit (Windows), /etc/shadow (Linux), database dumps, LSASS memory, pcap files, web app source**.

- [ ] **Common Hash Types:** Master identifying and handling **NTLM, NTLMv1/v2, NetNTLM, MD5, SHA-1, SHA-256, bcrypt, Argon2, PBKDF2, WPA2-PMKID, Kerberos (5/17/18/23)**.

---

### **Stage 2: Cracking Methodology & Tools**

_Goal: Apply the right technique to each hash type._

- [ ] **Hashcat Fundamentals:** Master **attack modes (-a 0 dictionary, -a 1 combination, -a 3 brute/mask, -a 6/7 hybrid)**, GPU acceleration, session management, and potfile usage.

- [ ] **John the Ripper:** Use **JtR** for format auto-detection, **incremental mode, wordlist mode, rules**, and cracking **non-GPU-friendly formats** (bcrypt, Argon2).

- [ ] **Dictionary Attacks:** Use curated wordlists — **rockyou.txt, SecLists, weakpass, kaonashi** — as the first pass against any hash.

- [ ] **Rule-Based Attacks:** Apply **Hashcat rules (best64.rule, OneRuleToRuleThemAll, d3ad0ne)** to mangle wordlists — capitalize, add numbers, leet-speak substitutions — to crack complex passwords efficiently.

- [ ] **Mask Attacks:** Use **Hashcat mask syntax** (`?u?l?l?l?l?d?d?s`) to brute-force **known password patterns** (e.g., company naming conventions, seasonal passwords like `Summer2024!`).

- [ ] **Hybrid Attacks:** Combine **wordlist + mask** (`-a 6` / `-a 7`) to crack passwords like `rockyou_words + 2024!` or `!2024 + rockyou_words`.

- [ ] **Rainbow Tables:** Understand **precomputed hash-to-plaintext lookup tables** and why **salting defeats them**; use **RainbowCrack** for legacy unsalted MD5/SHA1.

---

### **Stage 3: Protocol-Specific Cracking**

_Goal: Crack hashes captured from real network protocols._

- [ ] **NTLM / NetNTLMv2:** Capture with **Responder, ntlmrelayx**; crack with **hashcat -m 5600**; understand why NTLMv2 is harder than NTLMv1.

- [ ] **Kerberos Tickets:** Crack **Kerberoasted TGS (-m 13100)** and **AS-REP hashes (-m 18200)** offline with hashcat using targeted service-account wordlists.

- [ ] **WPA2 Handshakes:** Crack **4-way handshake (-m 22000)** and **PMKID (-m 22001)** from wireless captures with GPU-accelerated hashcat.

- [ ] **SSH Private Keys:** Use **ssh2john** to extract crackable hash from passphrase-protected keys; crack with JtR.

- [ ] **Office / PDF / ZIP:** Extract hashes with **office2john, pdf2john, zip2john**; crack with JtR or hashcat for document password recovery.

---

### **Stage 4: Wordlist & Intelligence Curation**

_Goal: Build targeted wordlists that outperform generic lists._

- [ ] **OSINT-Driven Wordlists:** Use **CeWL** to spider target websites and extract **company-specific vocabulary** for highly targeted password lists.

- [ ] **Custom Rule Writing:** Write **Hashcat/JtR rules** encoding target's known password policy — minimum length, required chars, common suffix patterns.

- [ ] **Credential Stuffing Lists:** Use **breach corpora (Collection #1, Dehashed)** to build target-specific lists from previously leaked passwords for the same user base.

- [ ] **Mentalist / PACK:** Use **Mentalist (GUI) or PACK (Policy Analysis)** to analyze cracked passwords and generate statistically optimized masks and rules.

---

<a id="toc-part-32-physical-penetration-testing"></a>
## Part 32: Physical Penetration Testing [OPTIONAL SPECIALIZATION]

> **Safety Gate:** Physical testing requires written authorization, named locations, dates/times, emergency contacts, stop conditions, and a get-out-of-jail letter. Do not practice bypasses on real facilities, campuses, offices, hotels, apartments, or transit systems.

### **Stage 1: Pre-Engagement & Reconnaissance**

_Goal: Plan the physical assessment within legal scope._

- [ ] **Scope Definition:** Confirm **written authorization, target facilities, allowed hours, assumed identity (e.g., contractor, vendor)**, and **emergency abort contact** before any physical operation.

- [ ] **Facility OSINT:** Use **Google Maps, Satellite imagery, LinkedIn (employee badge photos), job postings (physical security tools mentioned), public filings** to map facility layout, entry points, and security posture.

- [ ] **Physical Observation:** Conduct **covert surveillance** — observe **employee badge behavior, delivery procedures, tailgate vulnerability, smoking areas, loading docks** as low-security entry vectors.

- [ ] **Social Engineering Pretext:** Prepare **believable personas** (IT contractor, fire inspector, HVAC technician, delivery person) with **supporting props, business cards, uniforms, fake work orders**.

---

### **Stage 2: Entry & Access Control Bypass**

_Goal: Defeat physical barriers to gain facility access._

- [ ] **Tailgating / Piggybacking:** Follow authorized personnel through secured doors using **timing, props (heavy boxes, hands full), social confidence**; test anti-tailgate detection systems.

- [ ] **Lock Picking:** Practice **single-pin picking, raking, bump keys** for standard pin-tumbler locks; understand **high-security locks (Medeco, Abloy)** that resist standard attacks.

- [ ] **Bypass Tools:** Use **under-door tools (UDT), latch slipping tools, door gap attacks** to manipulate door hardware without the key.

- [ ] **RFID/NFC Badge Cloning:** Capture **low-frequency (125kHz HID, EM4100)** badge data with **Proxmark3** from up to 30cm; clone to blank T5577 card; understand **13.56MHz (MIFARE, DESFire)** attack complexity.

- [ ] **Electric Strike / Maglock Bypass:** Use **REX (Request-to-Exit) sensor exploitation, power interruption, crash bar manipulation** to open magnetically locked doors.

- [ ] **Elevator & Stairwell Access:** Identify **fire escape stairwells, service elevators, parking garage access** that bypass reception and security desks.

---

### **Stage 3: HID & USB Payload Attacks**

_Goal: Deploy physical implants and hardware attack tools._

- [ ] **USB HID Attacks (Rubber Ducky / Bash Bunny):** Craft **DuckyScript payloads** to execute **reverse shells, credential theft, backdoor installation** within seconds when plugged into an unlocked machine.

- [ ] **O.MG Cable:** Deploy **USB cables with embedded implants** that appear legitimate but exfiltrate data or execute commands over WiFi.

- [ ] **LAN Turtle / Shark Jack:** Drop **network implants** that provide **remote SSH access, packet capture, and network scanning** from inside the target network.

- [ ] **USB Drop Attacks:** Leave **weaponized USB drives** in common areas (parking lot, reception, bathroom); craft **autorun payloads, LNK files, fake docs** that execute on Windows/Linux.

- [ ] **Rogue Network Devices:** Plant **WiFi Pineapple, rogue AP, network tap** in server rooms, comms closets, or under desks for persistent network access.

---

### **Stage 4: On-Site Operations & Data Collection**

_Goal: Achieve objectives once inside._

- [ ] **Workstation Access:** Target **unlocked machines, password-protected screens (bypass with HID)**, install **implants, keyloggers, screen capture tools**.

- [ ] **Shoulder Surfing:** Observe **password entry, sensitive documents, screen content** in open offices, meeting rooms, and public areas.

- [ ] **Dumpster Diving:** Recover **printed credentials, org charts, hardware serial numbers, network diagrams, decommissioned drives** from trash/recycling.

- [ ] **Server Room / Comms Closet:** Attempt access to **network switches, patch panels, servers**; document **unencrypted hardware, unsecured console ports, accessible management interfaces**.

---

### **Stage 5: Reporting Physical Findings**

_Goal: Document and communicate physical security gaps professionally._

- [ ] **Evidence Collection:** Capture **covert photos/video (within ROE), cloned badge data, dropped USB recovery, access logs** as proof-of-concept evidence.

- [ ] **Risk Mapping:** Map findings to **physical security frameworks (PSIA, ISO 27001 Annex A.11)** and quantify **business impact** (data theft, sabotage, insider threat facilitation).

- [ ] **Remediation Guidance:** Recommend **anti-tailgate turnstiles, RFID upgrade paths, clean desk policy, USB port lockdown, security awareness training, camera placement**.

---

<a id="toc-part-33-voip--telecommunications-security"></a>
## Part 33: VoIP & Telecommunications Security [OPTIONAL SPECIALIZATION]

### **Stage 1: VoIP Protocol Fundamentals**

_Goal: Understand how VoIP systems communicate._

- [ ] **SIP (Session Initiation Protocol):** Master **SIP message structure (INVITE, ACK, BYE, REGISTER, OPTIONS)**, **dialog establishment**, **authentication (Digest Auth)**, and **common ports (UDP/TCP 5060, TLS 5061)**.

- [ ] **RTP (Real-time Transport Protocol):** Understand **media stream transport**, **SRTP (Secure RTP)** for encryption, **RTCP** for control, and how **RTP ports are negotiated via SDP**.

- [ ] **VoIP Infrastructure:** Map **components**: **IP-PBX (Asterisk, FreePBX), SBC (Session Border Controller), SIP Trunk, softphones, IP handsets, voicemail servers**.

- [ ] **Codec Identification:** Identify **G.711, G.729, Opus** codecs from SDP negotiation; understand quality vs. bandwidth tradeoffs and how codecs affect capture/decode.

---

### **Stage 2: VoIP Reconnaissance & Enumeration**

_Goal: Discover and map VoIP infrastructure._

- [ ] **SIP Scanning:** Use **svmap (SIPVicious), nmap SIP NSE scripts** to discover **SIP-enabled devices, extensions, PBX software versions**.

- [ ] **Extension Enumeration:** Use **svwar** to enumerate **valid SIP extensions** via REGISTER/OPTIONS probing; map **active users and voicemail accounts**.

- [ ] **Banner Grabbing:** Identify **PBX vendor and version** from **SIP User-Agent headers**; cross-reference with **CVE databases** for known exploits.

- [ ] **SDP Analysis:** Parse **Session Description Protocol** messages to identify **media types, codec preferences, RTP port ranges, and IP addresses**.

---

### **Stage 3: VoIP Attacks**

_Goal: Exploit weaknesses in VoIP deployments._

- [ ] **SIP Brute Force:** Use **svcrack (SIPVicious)** to brute-force **SIP extension passwords**; test default credentials (1234, extension number as password).

- [ ] **RTP Interception:** Position in MITM via **ARP spoofing**; capture **RTP streams with Wireshark**; reassemble and decode audio with **VoIPmonitor, sngrep, rtpbreak**.

- [ ] **Call Hijacking:** Send **spoofed BYE messages** to terminate active calls; send **CANCEL or re-INVITE** to redirect calls to attacker-controlled endpoints.

- [ ] **VoIP Fuzzing:** Use **Sip-Proxy, Codenomicon** to fuzz **SIP parsers** for crashes, memory corruption, and denial of service in PBX software.

- [ ] **Vishing Infrastructure:** Understand how **VoIP enables scalable vishing** — spoofed caller ID, auto-dialers, SIP trunk abuse for mass calling campaigns.

- [ ] **VLAN Hopping to Voice VLAN:** Exploit **voice VLAN misconfiguration** (untagged/double-tagged frames) to access VoIP network segment from data VLAN.

---

### **Stage 4: SS7 & Telecom Signaling Attacks**

_Goal: Understand mobile network signaling vulnerabilities._

- [ ] **SS7 Architecture:** Understand **Signaling System 7 (SS7)** — the global telephone signaling protocol connecting **mobile network operators, MSCs, HLRs, VLRs**.

- [ ] **SS7 Attack Types:** Study **location tracking (SendRoutingInfo), call interception (MAP UpdateLocation), SMS interception (ForwardSM)** — attacks that work against **any mobile network globally**.

- [ ] **Diameter Protocol:** Understand **Diameter** (4G/LTE replacement for SS7) and its own **attack surface** — roaming exploitation, subscriber data disclosure, DoS.

- [ ] **SIM Swapping (Technical):** Understand the **social engineering + SS7/carrier abuse chain** — porting credentials, carrier authentication weaknesses, and MFA bypass consequences.

- [ ] **IMSI Catchers (Stingrays):** Understand how **fake base stations force 2G downgrade**, capture **IMSI identifiers**, and enable **passive interception** of unencrypted traffic.

---

### **Stage 5: 5G Security**

_Goal: Understand the 5G threat landscape._

- [ ] **5G Architecture:** Understand **5G SA (Standalone) vs NSA (Non-Standalone)**, **gNB (base station), AMF, SMF, UPF** core network functions, and **network slicing**.

- [ ] **5G Attack Surface:** Study **SBA (Service-Based Architecture) HTTP/2 API attacks**, **SUPI/SUCI identifier exposure**, **slice isolation bypass**, **roaming security gaps**.

- [ ] **5G vs 4G Security:** Understand improvements (**SUPI concealment, mandatory mutual auth**) and remaining weaknesses (**legacy 2G/3G fallback, roaming interfaces**).

---

### **Stage 6: Defense & Hardening**

_Goal: Secure VoIP and telecom infrastructure._

- [ ] **SRTP Enforcement:** Mandate **SRTP** for all media streams and **TLS (SIP over TLS/SIPS)** for signaling; disable unencrypted SIP on all production systems.

- [ ] **SBC Hardening:** Configure **Session Border Controllers** to perform **topology hiding, rate limiting, anomaly detection, and geographic call blocking**.

- [ ] **Authentication Hardening:** Enforce **strong SIP digest passwords**, implement **IP allowlisting** for SIP trunks, disable **anonymous REGISTER**.

---

<a id="toc-part-34-blockchain--web3-security"></a>
## Part 34: Blockchain & Web3 Security [OPTIONAL SPECIALIZATION]

### **Stage 1: Blockchain Fundamentals for Security**

_Goal: Understand how blockchain and smart contracts work before attacking them._

- [ ] **Blockchain Mechanics:** Master **distributed ledger, consensus mechanisms (PoW, PoS, PoA)**, **immutability, transaction finality, mempool**, and **public/private key cryptography** in blockchain context.

- [ ] **Smart Contract Architecture:** Understand **EVM (Ethereum Virtual Machine)**, **Solidity language basics**, **ABI (Application Binary Interface)**, **bytecode vs. source code**, and **contract deployment lifecycle**.

- [ ] **DeFi Ecosystem:** Map **protocols**: **DEXs (Uniswap, Curve), lending (Aave, Compound), oracles (Chainlink), bridges, yield aggregators** — understand how they interact and compose.

- [ ] **Wallet Security:** Understand **EOA (Externally Owned Accounts) vs contract wallets**, **seed phrases (BIP39), HD derivation paths, hardware wallets (Ledger, Trezor)**, and **private key storage risks**.

---

### **Stage 2: Smart Contract Vulnerabilities**

_Goal: Identify and exploit common Solidity security flaws._

- [ ] **Reentrancy Attacks:** Exploit **recursive external calls before state updates** (The DAO hack pattern); understand `checks-effects-interactions` as the fix; test with **Hardhat/Foundry**.

- [ ] **Integer Overflow/Underflow:** Exploit **arithmetic overflow in Solidity <0.8.0** (e.g., `uint256 balance = 0; balance -= 1;` wraps to MAX); understand SafeMath and Solidity 0.8 built-in checks.

- [ ] **Access Control Flaws:** Find **missing `onlyOwner` modifiers, tx.origin authentication, unprotected `initialize()` functions** in upgradeable contracts.

- [ ] **Logic Flaws & Business Logic Errors:** Exploit **incorrect assumptions** about token prices, balances, or state — often unique to each protocol's design.

- [ ] **Flash Loan Attacks:** Understand **uncollateralized loans within a single transaction**; exploit **oracle price manipulation, liquidity pool imbalances, governance attacks** using flash loans.

- [ ] **Oracle Manipulation:** Exploit **reliance on on-chain DEX spot price as oracle** — manipulate pool price via large swap, exploit contracts that trust it, profit.

- [ ] **Front-Running & MEV:** Understand **Maximal Extractable Value** — sandwich attacks, arbitrage, and liquidation front-running by miners/validators in the mempool.

---

### **Stage 3: Smart Contract Auditing Methodology**

_Goal: Systematically audit contracts for vulnerabilities._

- [ ] **Static Analysis Tools:** Use **Slither, MythX, Aderyn, Semgrep Solidity rules** to automatically detect common vulnerability patterns.

- [ ] **Symbolic Execution:** Use **Manticore, Echidna (fuzzer), Halmos (formal verification)** to find edge cases not caught by static analysis.

- [ ] **Manual Code Review:** Read contract logic line-by-line; trace **all external calls, state transitions, and access control checks**; verify invariants hold under all conditions.

- [ ] **PoC in Foundry/Hardhat:** Write **test exploits in Foundry (`forge test`)** forking mainnet to demonstrate real attack viability without deploying to live chain.

- [ ] **Audit Report Writing:** Document findings with **severity (Critical/High/Medium/Low/Informational), impact, likelihood, proof-of-concept, and recommended fix**.

---

### **Stage 4: Web3 Infrastructure Attacks**

_Goal: Attack the broader Web3 ecosystem beyond smart contracts._

- [ ] **Wallet Drainer Attacks:** Understand **malicious `approve()` / `permit()` signatures** that give attackers unlimited token spending rights; study **phishing sites** targeting Web3 users.

- [ ] **Bridge Attacks:** Analyze **cross-chain bridge vulnerabilities** (Ronin $625M, Wormhole $320M) — **validator compromise, signature replay, logic errors in lock/mint mechanisms**.

- [ ] **NFT Security:** Examine **metadata centralization risks, royalty bypass, reentrancy in `onERC721Received`**, and **enumeration attacks** on NFT collections.

- [ ] **Private Key Extraction:** Study attack vectors — **weak entropy in key generation, compromised RNG, phishing for seed phrases, clipboard hijackers, malicious browser extensions**.

- [ ] **RPC Node Attacks:** Understand **exposure of `eth_accounts`, `personal_sign` on misconfigured nodes**; test for **open JSON-RPC endpoints** that can sign transactions.

---

### **Stage 5: Defense & Secure Development**

_Goal: Build secure smart contracts and Web3 applications._

- [ ] **Security Patterns:** Implement **checks-effects-interactions, pull-over-push payments, rate limiting, circuit breakers (pause mechanisms)** in contract design.

- [ ] **Upgradeable Contract Security:** Use **OpenZeppelin Upgrades Plugins**; understand **storage collision risks, initializer protection, proxy admin key management**.

- [ ] **Formal Verification:** Apply **Certora Prover or K Framework** to mathematically prove critical invariants hold under all possible inputs.

- [ ] **Bug Bounties:** Engage **Immunefi, Code4rena, Sherlock** for smart contract audits and bug bounties; understand **responsible disclosure in Web3 context**.

---

<a id="toc-part-35-governance-risk--compliance-grc"></a>
## Part 35: Governance, Risk & Compliance (GRC)

### **Stage 1: Security Frameworks & Standards**

_Goal: Understand the regulatory and standards landscape that defines what pentesters test against._

- [ ] **NIST Cybersecurity Framework (CSF):** Master the **5 functions (Identify, Protect, Detect, Respond, Recover)** and how they map to security controls.

- [ ] **NIST 800-53 / 800-171:** Understand **security control families** (Access Control, Audit, Incident Response) used in **federal and defense** compliance.

- [ ] **ISO 27001/27002:** Know the **ISMS (Information Security Management System)** framework, **Annex A controls**, and **certification audit process**.

- [ ] **CIS Controls (v8):** Master the **18 Critical Security Controls** as a prioritized, actionable defense checklist; understand **Implementation Groups (IG1-IG3)**.

- [ ] **MITRE ATT&CK as Compliance:** Use **ATT&CK coverage mapping** to demonstrate detection maturity against specific adversary techniques.

---

### **Stage 2: Industry Regulations & Legal Requirements**

_Goal: Know the laws and regulations that dictate security requirements across industries._

- [ ] **PCI-DSS (Payment Card Industry):** Understand the **12 requirements** for protecting cardholder data; know **scope reduction (network segmentation), SAQ types**, and how pentesters validate Requirement 11.3.

- [ ] **HIPAA (Healthcare):** Understand **PHI (Protected Health Information)** safeguards, **technical/administrative/physical** controls, and **breach notification requirements**.

- [ ] **GDPR (EU Data Protection):** Know **data subject rights, lawful basis for processing, Data Protection Impact Assessments (DPIA), breach notification (72-hour rule)**, and **extraterritorial scope**.

- [ ] **SOC 2 (Service Organizations):** Understand **Trust Services Criteria (Security, Availability, Processing Integrity, Confidentiality, Privacy)** and how pentest findings map to SOC 2 reports.

- [ ] **SOX (Sarbanes-Oxley):** Know **IT General Controls (ITGCs)** for financial system integrity — **access control, change management, backup/recovery**.

- [ ] **DPDP Act (India):** Understand **India's Digital Personal Data Protection Act** — consent-based processing, Data Fiduciary obligations, cross-border transfer rules, and **Board penalties**.

- [ ] **Computer Fraud & Abuse Act (CFAA):** Understand US federal law on **unauthorized access**; know how **scope of engagement** and **written authorization** protect pentesters legally.

---

### **Stage 3: Risk Management & Assessment**

_Goal: Quantify and communicate risk so findings drive action._

- [ ] **Risk Equation:** Master **Risk = Threat × Vulnerability × Impact** and use it to **prioritize findings** over raw CVSS scores.

- [ ] **Risk Assessment Methodologies:** Understand **NIST 800-30 (qualitative), FAIR (quantitative), OCTAVE, CRAMM** for structured risk evaluation.

- [ ] **Threat Modeling:** Apply **STRIDE, PASTA, Attack Trees** to proactively identify **threats to systems before testing** and guide scope selection.

- [ ] **Business Impact Analysis (BIA):** Map **technical vulnerabilities to business consequences** — revenue loss, reputational damage, regulatory fines, operational downtime.

- [ ] **Risk Appetite & Tolerance:** Understand how organizations define **acceptable risk levels** and how pentest recommendations must align with business context.

---

### **Stage 4: Audit, Scope & Compliance Testing**

_Goal: Execute engagements that satisfy compliance requirements._

- [ ] **Scoping for Compliance:** Define pentest scope to cover **specific compliance requirements** (e.g., PCI-DSS Req 11.3 requires internal/external pentest + segmentation testing).

- [ ] **Control Validation:** Test whether **implemented controls** (MFA, encryption, logging, access controls) actually function as documented in policies.

- [ ] **Evidence Collection:** Gather **screenshots, logs, packet captures, configuration exports** formatted for **auditor review** and compliance documentation.

- [ ] **Gap Analysis Reporting:** Identify **missing controls, partial implementations, policy violations** and map them to **specific framework requirements** with remediation guidance.

- [ ] **Third-Party Risk:** Assess **vendor/supplier security posture** via **questionnaires, pentest scoping, SLA review**, and **supply chain risk evaluation**.

- [ ] **Continuous Compliance:** Understand shift from **point-in-time audits** to **continuous monitoring, automated compliance checks, and DevSecOps integration**.

---

### **Lab Progression**

_Goal: Make GRC practical by producing audit-ready artifacts._

- [ ] **Risk Register Lab:** Build a risk register for your home lab or a sample SaaS system with likelihood, impact, owner, treatment, and due date.
- [ ] **Policy Lab:** Write one access-control policy and one incident-response policy with scope, roles, exceptions, and review cadence.
- [ ] **Control Mapping Lab:** Map 10 technical controls to NIST CSF, CIS Controls, or ISO 27001 Annex A.
- [ ] **Vendor Risk Lab:** Create a lightweight vendor security questionnaire and score a fictional third-party service.
- [ ] **Business Continuity Lab:** Write a basic BIA and recovery priority list for a sample business process.
- [ ] **Move-On Gate:** Produce an audit evidence pack with policy, risk register, control mapping, and remediation plan.

<a id="toc-part-36-supply-chain-security"></a>
## Part 36: Supply Chain Security

### **Stage 1: Understanding the Attack Surface**

_Goal: Map how software and hardware dependencies become attack vectors._

- [ ] **Supply Chain Threat Model:** Understand the **three attack vectors**: compromised **source code** (SolarWinds), compromised **build/distribution** (XZ Utils backdoor), and compromised **dependencies** (event-stream npm).

- [ ] **SBOM (Software Bill of Materials):** Generate and analyze **SBOM (CycloneDX, SPDX format)** to inventory all third-party components, transitive dependencies, and their known CVEs.

- [ ] **Dependency Inventory:** Map **direct + transitive dependencies** across package ecosystems (**npm, PyPI, Maven, NuGet, RubyGems**) to understand total exposed surface.

---

### **Stage 2: Dependency & Package Attacks**

_Goal: Exploit weaknesses in open-source package ecosystems._

- [ ] **Dependency Confusion:** Register **public packages with the same name** as internal private packages; force targets to download your malicious version when their registry falls back to public PyPI/npm.

- [ ] **Typosquatting:** Publish packages with **names one keystroke away** from popular packages (`reqeusts`, `colourama`, `crypt0`) to catch developer typos during `pip install`.

- [ ] **Malicious Package Injection:** Study real cases (**event-stream, PyTorch-nightly, ctx**) where **legitimate packages were backdoored** post-compromise of the maintainer account.

- [ ] **Version Pinning Attacks:** Target packages using **unpinned `latest`** or **broad version ranges** (`>=1.0`); understand how **lock files (package-lock.json, Pipfile.lock)** mitigate this.

- [ ] **Protestware & Intentional Sabotage:** Understand cases where **maintainers intentionally introduced bugs/wipes** (colors.js, node-ipc) and the supply chain trust model risks this exposes.

---

### **Stage 3: Build System & CI/CD Attacks**

_Goal: Compromise the pipeline that produces software._

- [ ] **Pipeline Poisoning:** Inject **malicious steps into CI/CD workflows** (GitHub Actions, Jenkins, GitLab CI) to **steal secrets, alter artifacts, plant backdoors** in compiled output.

- [ ] **Workflow Injection:** Exploit **untrusted input in GitHub Actions expressions** (`${{ github.event.pull_request.title }}`) to achieve **command injection in CI runners**.

- [ ] **Secrets Exfiltration:** Steal **CI/CD secrets (API keys, deploy tokens, signing certs)** from **environment variables, GitHub Secrets, HashiCorp Vault** during pipeline execution.

- [ ] **Artifact Tampering:** Replace **legitimate build artifacts** post-build but pre-deployment; understand **artifact signing (Sigstore/Cosign)** as a defense.

- [ ] **SLSA Framework:** Understand **Supply-chain Levels for Software Artifacts (SLSA)** maturity model (L1-L4) and what each level proves about build provenance.

---

### **Stage 4: Open-Source & Third-Party Risk**

_Goal: Assess and test third-party component security._

- [ ] **OSS Vulnerability Scanning:** Use **Trivy, Grype, Snyk, OWASP Dependency-Check** to scan project dependencies for **known CVEs** and **license violations**.

- [ ] **Maintainer Account Takeover:** Understand how **compromised npm/PyPI maintainer accounts** (via credential stuffing or social engineering) enable **silent package backdooring**.

- [ ] **Repo Jacking:** Exploit **GitHub repository namespace reuse** — when a user changes their username, old repo URLs can be claimed by attackers to serve malicious packages.

- [ ] **Trojanized Tooling:** Test environments for **compromised developer tools** (malicious VS Code extensions, backdoored CLI tools, modified build systems).

---

### **Stage 5: Defense & Verification**

_Goal: Know how to validate supply chain integrity._

- [ ] **Sigstore / Cosign:** Verify **container image and artifact signatures** to ensure provenance; understand **keyless signing with OIDC identity**.

- [ ] **Dependency Pinning:** Enforce **exact version pinning + hash verification** in lock files; use **Renovate/Dependabot** for automated safe updates.

- [ ] **Private Registries:** Maintain **internal package mirrors (Artifactory, Nexus)** with **allowlisting** to prevent dependency confusion attacks.

- [ ] **Code Signing:** Implement **code signing for all releases**; verify signatures in deployment pipelines before execution.

---

<a id="toc-part-37-devsecops--secure-sdlc"></a>
## Part 37: DevSecOps & Secure SDLC

### **Stage 1: Security in the Development Lifecycle**

_Goal: Understand where security integrates across the SDLC._

- [ ] **SDLC Security Gates:** Map **security activities to SDLC phases** — threat modeling (design), SAST (code), SCA (build), DAST (test), pentest (pre-release), monitoring (production).

- [ ] **Shift-Left Security:** Understand the **cost and benefit model** — finding a bug in design costs 10x less than finding it in production; align testing earlier in the cycle.

- [ ] **Threat Modeling:** Apply **STRIDE to application architecture** — identify **Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege** risks before coding.

- [ ] **Secure Design Principles:** Master **least privilege, defense-in-depth, fail securely, complete mediation, open design, separation of privilege** as architectural requirements.

---

### **Stage 2: Static Analysis (SAST)**

_Goal: Find vulnerabilities in source code without executing it._

- [ ] **SAST Tools:** Use **Semgrep, SonarQube, Checkmarx, Bandit (Python), Brakeman (Rails), SpotBugs (Java)** to scan source code for **injection flaws, insecure crypto, hardcoded secrets**.

- [ ] **Custom SAST Rules:** Write **Semgrep rules** to detect **organization-specific insecure patterns** (custom crypto usage, missing input validation in internal frameworks).

- [ ] **False Positive Management:** Triage SAST output — distinguish **true positives, false positives, and low-risk findings**; suppress noise without hiding real issues.

- [ ] **IDE Integration:** Understand how **security plugins (Snyk IDE, SonarLint, Semgrep VS Code)** give developers **real-time feedback** during coding.

---

### **Stage 3: Dynamic Analysis (DAST & IAST)**

_Goal: Test running applications for security flaws._

- [ ] **DAST Tools:** Use **OWASP ZAP, Burp Suite Pro (automated scan), Nikto** to **black-box test** running applications for **OWASP Top 10 vulnerabilities** in CI pipelines.

- [ ] **IAST (Interactive Application Security Testing):** Understand how **IAST agents (Contrast Security, Seeker)** instrument running code to detect vulnerabilities from the inside during functional tests.

- [ ] **API DAST:** Configure **ZAP or Burp** with **OpenAPI specs** to automatically fuzz all API endpoints for **injection, auth bypass, and BOLA**.

- [ ] **Authenticated Scanning:** Configure DAST tools with **session cookies or API keys** to test **post-login functionality** inaccessible to anonymous scans.

---

### **Stage 4: Software Composition Analysis (SCA)**

_Goal: Find vulnerabilities in third-party dependencies._

- [ ] **SCA Tools:** Use **Snyk, Dependabot, OWASP Dependency-Check, Black Duck** to continuously scan **package manifests** for **CVEs, outdated versions, license violations**.

- [ ] **Vulnerability Prioritization:** Understand **reachability analysis** — not every CVE in a dependency is exploitable; prioritize based on **actual code paths** that use the vulnerable function.

- [ ] **License Compliance:** Identify **copyleft licenses (GPL, AGPL)** that may require open-sourcing proprietary code; flag **license conflicts** in dependency trees.

---

### **Stage 5: Secrets Detection & Pipeline Security**

_Goal: Prevent credential leakage through code and pipelines._

- [ ] **Secrets Scanning:** Use **truffleHog, gitleaks, git-secrets** to scan **git history** (not just current HEAD) for **API keys, passwords, private keys, connection strings**.

- [ ] **Pre-commit Hooks:** Install **pre-commit framework with detect-secrets or gitleaks** to block secret commits before they reach the remote repository.

- [ ] **Pipeline Hardening:** Apply **least-privilege to CI service accounts**, use **short-lived OIDC tokens** instead of long-lived secrets, scope permissions to **minimum required for each job**.

- [ ] **Container Image Security:** Scan **base images and Dockerfiles** with **Trivy, Dockle** for CVEs, misconfigurations, and secrets baked into image layers.

- [ ] **IaC Security:** Scan **Terraform, CloudFormation, Helm charts** with **Checkov, tfsec, kics** for **open security groups, public storage, missing encryption, IAM over-permission**.

### **Secure Coding & Pipeline Lab Progression**

_Goal: Prove you can prevent vulnerabilities, not only scan for them._

- [ ] **Secure Coding Fix Lab:** Take a small vulnerable app and fix SQL injection, XSS, command injection, path traversal, insecure deserialization, weak auth, and insecure direct object reference patterns.
- [ ] **Code Review Lab:** Review one intentionally vulnerable repository and produce findings with file/line references, exploitability notes, and safe remediation.
- [ ] **GitHub Actions Security Lab:** Build a CI pipeline with Semgrep, gitleaks, Trivy, dependency scanning, and artifact upload.
- [ ] **Break-the-Build Gate:** Configure the pipeline to fail on critical secrets, critical dependency CVEs, and high-confidence SAST findings.
- [ ] **Threat Model Lab:** Draw a DFD for a sample app and map trust boundaries, abuse cases, and required controls.
- [ ] **Move-On Gate:** Produce a before/after report showing vulnerable code, fixed code, tests, and CI evidence.

---

<a id="toc-part-38-ai--llm-red-teaming"></a>
## Part 38: AI & LLM Red Teaming

### **Stage 1: AI Fundamentals for Security Practitioners**

_Goal: Understand the raw mechanics of AI/ML models to attack and defend them effectively._

- [ ] **Transformer Architecture:** Study the **Transformer model** (attention heads, tokenization, embeddings, positional encoding) — understand how LLMs generate text at a mechanistic level to identify exploitable behavior.

- [ ] **Context Windows & Token Limits:** Understand how **context window size** (4K, 8K, 32K, 128K+ tokens) affects model behavior — know how **context overflow, truncation, and sliding window strategies** create exploitable edge cases (instruction amnesia, guardrail escape via long contexts).

- [ ] **Temperature & Sampling Parameters:** Learn how **temperature, top-p (nucleus sampling), top-k, and frequency/presence penalties** control output randomness — understand that **higher temperature increases exploitability** by making the model more likely to produce unfiltered or unexpected outputs.

- [ ] **Retrieval-Augmented Generation (RAG):** Understand the full **RAG pipeline** (chunking → embedding → vector DB → retrieval → generation); know how each stage can be poisoned or manipulated.

- [ ] **Fine-Tuning Concepts:** Learn how **supervised fine-tuning (SFT), RLHF, and LoRA** work; understand how fine-tuning changes model behavior and creates new attack surfaces (backdoors, alignment drift).

- [ ] **AI Math Foundations:** Study the underlying math — **gradient descent, loss functions, attention weights, softmax probabilities** — to understand why adversarial inputs work and how to craft more effective attacks.

- [ ] **API Integration (Python & Bash):** Integrate **OpenAI, Claude (Anthropic), and Gemini (Google)** APIs into Python and Bash scripts; build wrappers for security automation tasks (recon summarization, vuln explanation, report drafting).

- [ ] **Prompt Engineering for Security:** Master structured prompting techniques — **system/user role separation, chain-of-thought, few-shot examples** — applied strictly to security contexts (threat modeling, CVE analysis, payload generation assistance).

- [ ] **AI/ML Course Grounding:** Complete foundational AI courses (e.g., **DeepLearning.AI Specialization** or **Google AI Essentials**) to understand the math behind models before testing them offensively.

---

### **Stage 2: Attack Surface & Frameworks**

_Goal: Map the AI/LLM attack surface using structured threat models._

- [ ] **OWASP LLM Top 10 (2025):** Prioritize **LLM01 Prompt Injection**, **LLM02 Sensitive Information Disclosure**, and **LLM10 Unbounded Consumption (denial-of-wallet)**; build test cases for each.

- [ ] **Model Scoping:** Identify **system prompts, guardrails, plugins/tools, retrieval sources, rate limits** and what data the model can reach.

- [ ] **Safety Policy Mapping:** Map controls to **content filters, tool permission boundaries, data classification**, and measure gaps.

---

### **Stage 3: Adversarial Techniques (LLM01/LLM06)**

_Goal: Break safety controls and force unintended actions._

- [ ] **Jailbreaking:** Use **role-play prompts (e.g., DAN), multi-turn "crescendo" manipulation**, and **character/encoding obfuscation** to bypass safety layers.

- [ ] **Agentic Exploitation (LLM06 Excessive Agency):** Trick autonomous agents into **calling disallowed tools, escalating permissions, or executing dangerous actions**.

- [ ] **Prompt Injection:** Deliver **in-band and out-of-band injections** via user input, files, and linked resources to override system prompts.

---

### **Stage 4: RAG & Data Supply Chain Attacks**

_Goal: Poison or subvert the knowledge base feeding the model._

- [ ] **RAG Poisoning:** Inject **malicious documents or vectors** into **vector DBs/indices** to induce **hallucinations or payload delivery**.

- [ ] **Retrieval Abuse:** Manipulate **chunking, scoring, metadata filters** to force **malicious context** into responses.

- [ ] **Data Exfil via RAG:** Weaponize **document recall** to leak **sensitive embeddings or proprietary content**.

---

### **Stage 5: Language Model Specific Attacks**

_Goal: Exploit LLM architecture and fine-tuning vulnerabilities._

- [ ] **Prompt Injection (LLM01):** Master **direct, indirect, multi-turn, and encoding-based injections** to override safety guardrails.

- [ ] **Excessive Agency (LLM06):** Force LLM-powered agents to **call unintended tools, escalate permissions, bypass access controls**.

- [ ] **Training Data Leakage:** Extract **memorized training data** via **completion, prefix completion, membership inference**.

- [ ] **Instruction Hierarchy Bypass:** Exploit **conflicting instructions** (system prompt vs. user input) to cause **unsafe behavior**.

- [ ] **Sycophancy & Alignment Hacking:** Manipulate models to prioritize **user approval over accuracy, safety**, causing deceptive outputs.

---

### **Stage 6: Multi-Model & Agent Attacks**

_Goal: Exploit weaknesses in agentic and multi-model systems._

- [ ] **Agent Jailbreaking:** Trick **agents with tool access** to call **disallowed APIs or perform escalated actions**.

- [ ] **Tool Confusion:** Supply **conflicting or misleading tools** to cause **agent to misuse capabilities**.

- [ ] **Multi-Model Poisoning:** Compromise **upstream models** in a pipeline to degrade **downstream results**.

- [ ] **Agent Exfiltration:** Use **agent tool calls** to exfiltrate **data, model outputs, system information**.

- [ ] **Prompt Leakage via Agents:** Trigger **verbose logging or error messages** to leak **system prompts, API keys, context**.

---

### **Stage 7: Adversarial Examples & ML Robustness**

_Goal: Craft inputs that cause model misclassification or unexpected behavior._

- [ ] **Adversarial Patch Generation:** Create **minimal perturbations** (pixel-level or token-level) to flip model predictions (e.g., misclassify objects, bypass spam filters).

- [ ] **Universal Adversarial Perturbations (UAP):** Develop **single perturbation sequences** that fool the model across many inputs.

- [ ] **Text-Based Adversarial Examples:** Generate **typos, special chars, unicode tricks** to bypass **content filters, keyword detection**.

- [ ] **Robustness Testing Frameworks:** Use tools like **CleverHans, Foolbox, Adversarial-Robustness-Toolbox** to systematically find weaknesses.

- [ ] **Defense Evasion via Adversarial Samples:** Understand how **adversarial training, input sanitization, ensemble defenses** are applied.

---

### **Stage 8: Model Extraction & Inversion**

_Goal: Steal or reverse-engineer the model's behavior and weights._

- [ ] **Model Extraction via API:** Use **probing queries, decision boundary mapping** to reverse-engineer **model architecture, layer sizes**.

- [ ] **Training Data Extraction:** Use **membership inference attacks** to determine if **specific data was in training set**.

- [ ] **Prompt Leakage:** Extract **system prompts, fine-tuning instructions, API keys** via **prompt injection, log manipulation**.

- [ ] **Functionality Cloning:** Build **surrogate model** that mimics extracted behavior, cheaper than using the original API.

---

### **Stage 9: Dataset Poisoning & Backdoors**

_Goal: Corrupt training pipelines to install persistent behavior changes._

- [ ] **Label Flipping:** Inject **mislabeled examples** during training to degrade model accuracy on target classes.

- [ ] **Trojan/Backdoor Attacks:** Insert **trigger patterns** that cause specific misbehavior only when triggered (e.g., misclassify specific images when watermark present).

- [ ] **Gradual Poisoning:** Inject **subtle, distributed poisoning** to avoid detection while degrading performance.

- [ ] **Federated Learning Poisoning:** Attack **distributed training** by sending malicious gradients from compromised workers.

- [ ] **Supply Chain Poisoning:** Compromise **training data sources, pre-trained models, dependencies** to plant backdoors.

---

### **Stage 10: Privacy Attacks & PII Leakage**

_Goal: Extract private information embedded in models._

- [ ] **Membership Inference:** Determine if **specific records were used in training** via prediction confidence analysis.

- [ ] **Attribute Inference:** Deduce **sensitive attributes** of training individuals from model behavior.

- [ ] **Model Inversion:** Reconstruct **training data samples** (e.g., faces from facial recognition model).

- [ ] **Reconstruction Attacks:** Use **gradient descent** to reconstruct **sensitive inputs** from model outputs.

- [ ] **De-anonymization:** Link **anonymized training data** to real identities via **model predictions and external data**.

---

### **Stage 11: AI-Augmented Red Team Workflow**

_Goal: Force-multiply your existing red team toolkit with AI-native tooling._

- [ ] **Burp Suite AI Plugins:** Install and operate AI-powered Burp extensions — use **AI-assisted scanning, request analysis, and vulnerability explanation** plugins to accelerate web app assessments.

- [ ] **AutoRecon + LLM Analysis:** Run **AutoRecon** for automated multi-tool recon; pipe structured output into an **LLM (GPT/Claude/Gemini)** for intelligent prioritization, service context, and attack path recommendations.

- [ ] **PentestGPT:** Use **PentestGPT** (LLM-guided pentest assistant) to navigate complex engagement steps — test its guidance quality, understand its failure modes, and learn to correct its reasoning.

- [ ] **AI-Assisted Report Writing:** Use LLMs to draft **findings, risk ratings, and executive summaries** from structured notes; review and correct output for accuracy, then refine prompts for consistency.

- [ ] **AI Threat Modeling:** Apply LLM-assisted **STRIDE/PASTA threat modeling** — feed system architecture descriptions into an AI to enumerate threats; validate against manual analysis.

- [ ] **AI Forensics Concepts:** Understand how **AI systems leave forensic artifacts** (inference logs, model versioning, embedding stores) and how to investigate AI-assisted attacks post-incident.

---

### **Stage 12: Agentic AI & Autonomous Attack Infrastructure**

_Goal: Build autonomous agents that execute security tasks end-to-end._

- [ ] **LangChain for Security Automation:** Build **LangChain-based agents** in Python that chain tools (Nmap, Shodan API, CVE search, Burp) with LLM reasoning to automate multi-step recon and enumeration workflows.

- [ ] **CrewAI Multi-Agent Systems:** Design **CrewAI role-based agent crews** (e.g., Recon Agent + Exploit Agent + Report Agent) that collaborate autonomously on a penetration testing engagement.

- [ ] **Model Context Protocol (MCP):** Learn the **MCP standard** — how AI agents communicate with external tools and data sources; understand MCP server architecture and security implications of poorly scoped MCP permissions.

- [ ] **Adversarial Testing Against Live LLMs:** Practice offensive testing against **production LLMs** (within authorized scope/bug bounty programs) — attempt prompt injection, context manipulation, and tool abuse against real deployed systems.

- [ ] **AI-Specific CTFs:** Participate in **AI/LLM-focused Capture The Flag competitions** (e.g., Gandalf AI CTF, HackAPrompt, CTFd-based AI challenges) to build speed and creativity against novel AI attack scenarios.

- [ ] **Custom GPT for Recon Automation:** Build a **custom GPT or assistant** (via OpenAI API or open-source models) designed solely for reconnaissance automation — feeds it OSINT data, outputs structured attack surface maps and prioritized targets.

---

### **Stage 13: Tooling & Evaluation**

_Goal: Automate and measure AI red team coverage._

- [ ] **Red Team Tooling:** Use **PyRIT (Microsoft)**, **Garak**, **DeepTeam**, alongside traditional frameworks (**Metasploit**) for orchestration.

- [ ] **Benchmarking:** Track **success rates** across **OWASP LLM Top 10** and **agent/tool abuse cases**; log **prompt, response, decision traces**.

- [ ] **Safety Regression:** Build **automated test suites** to prevent **prompt regressions** after model or policy updates.

---

### **Stage 14: Defense & Responsible AI**

_Goal: Harden AI systems against attacks and ensure ethical deployment._

- [ ] **Input Validation & Sanitization:** Filter **prompt injections, adversarial patterns, malicious encodings**.

- [ ] **Output Guardrails:** Implement **content filtering, toxicity detection, sensitive info masking** on responses.

- [ ] **Model Hardening:** Use **adversarial training, regularization, ensemble methods** to improve robustness.

- [ ] **Monitoring & Detection:** Track **unusual queries, repeated failures, extraction signals** to detect attacks.

- [ ] **Audit Logging:** Log **all prompts, model outputs, decisions** for **post-incident forensics and compliance**.

- [ ] **Responsible Disclosure:** Establish **vulnerability bounty programs, responsible disclosure timelines** for AI security researchers.

- [ ] **Threat Model Documentation:** Maintain **risk register** of **known weaknesses, mitigations, residual risk** in AI systems.

---

### **Stage 15: Shadow AI & Organizational AI Risk**

_Goal: Understand and prevent unauthorized AI usage that creates organizational exposure._

- [ ] **Shadow AI Identification:** Detect **unauthorized use of public LLMs (ChatGPT, Gemini, Claude)** by employees pasting **source code, customer data, internal documents, API keys** into external AI services — creating **data leakage vectors** invisible to traditional DLP.

- [ ] **AI Data Loss Prevention (DLP):** Implement **DLP policies specific to AI services** — block/monitor traffic to **api.openai.com, generativelanguage.googleapis.com, api.anthropic.com** at the proxy/firewall level; deploy **endpoint DLP agents** that detect copy-paste of classified content into AI web interfaces.

- [ ] **AI Acceptable Use Policy:** Draft and enforce organizational **AI usage policies** defining **approved tools, data classification restrictions, prohibited use cases**, and **consequences for violations** — align with **NIST AI RMF** and **EU AI Act** requirements.

- [ ] **Approved AI Tooling:** Deploy **sanctioned, self-hosted AI solutions** (enterprise ChatGPT, Azure OpenAI, AWS Bedrock, local Ollama instances) with **audit logging, data retention controls, and access management** to replace shadow AI usage.

- [ ] **AI Supply Chain Risk:** Assess **third-party AI integrations** (Copilot, Grammarly, Jasper, AI coding assistants) for **data handling, model training opt-out, and contractual data protection** — treat each as a potential exfiltration channel.

---

### **Stage 16: Defensive AI Operations**

_Goal: Deploy AI-powered defensive capabilities and detect AI-generated threats._

- [ ] **Deepfake Detection:** Understand and deploy tools for detecting **AI-generated images, video, and audio** — study **artifact analysis (compression patterns, frequency domain), temporal inconsistency detection, and provenance verification (C2PA/Content Credentials)**.

- [ ] **AI Voice Cloning Defense:** Implement **voice authentication hardening** against **ElevenLabs/RVC-style cloning attacks** — deploy **anti-spoofing liveness detection, challenge-response voice verification**, and **ban voice-only authorization** for sensitive operations.

- [ ] **AI-Enhanced Phishing Detection:** Deploy **ML/NLP-based email analysis** to detect **AI-generated phishing** that bypasses traditional signature-based filters — train classifiers on **stylometric analysis, sender behavior anomalies, and LLM-characteristic writing patterns**.

- [ ] **AI-Powered SOC Integration:** Leverage **AI/ML for security operations** — use **anomaly detection models** for network traffic, **NLP-based log analysis** for threat hunting, and **automated alert triage** to handle volume at scale without analyst burnout.

- [ ] **AI Incident Response:** Develop **playbooks for AI-specific incidents** — compromised model endpoints, data poisoning detection, prompt injection campaigns, unauthorized model access, and **AI-generated social engineering at scale**.

- [ ] **AI Forensics:** Understand how **AI systems leave forensic artifacts** — **inference logs, model versioning, embedding stores, fine-tuning datasets, API call histories** — and how to investigate AI-assisted attacks post-incident.

---

### **Stage 17: AI Security Projects & Portfolio**

_Goal: Prove production capability through real, complex, integrated AI-security projects._

- [ ] **AI-Driven Fuzzer (C/C++):** Build a **machine learning-guided fuzzer** in C/C++ that uses coverage feedback and learned mutation strategies to discover vulnerabilities faster than traditional dumb fuzzing.

- [ ] **Automated Payload Obfuscator:** Develop an AI-assisted tool that **automatically transforms payloads** (shellcode, scripts) to evade AV/EDR signatures using LLM-guided encoding, variable substitution, and structure mutation.

- [ ] **Integrated AI-Security Project (GitHub):** Push **2–3 highly complex, integrated AI-security tools** to a public GitHub repository — include README, architecture diagrams, usage examples, and documented attack scenarios.

- [ ] **Technical Writeups (Medium/LinkedIn):** Write **substantive, technical breakdowns** of your AI security research — document methodology, failures, and findings in long-form posts targeting both practitioners and hiring managers.

- [ ] **Community Presentation:** Present findings at **local hacker meetups, BSides, or DEF CON AI Village** — build credibility through live demonstrations and Q&A with the community.

---

### **Stage 18: AI Security Career Targeting**

_Goal: Position yourself specifically for AI-native security roles._

- [ ] **AI Security Role Identification:** Target roles explicitly requiring **AI security skills** — LLM Red Teamer, AI Safety Engineer, ML Security Researcher, Prompt Security Engineer — at AI labs, security consultancies, and enterprise AI teams.

- [ ] **Resume Differentiation:** Highlight **autonomous systems engineered, agents built, AI tools integrated** — frame contributions in terms of capability delivered, not just technologies used.

- [ ] **AI Security Community Engagement:** Contribute to **OWASP LLM Top 10 working group**, open-source AI security tools (**Garak, PyRIT**), or AI safety research to build verifiable community presence.

- [ ] **Portfolio Alignment:** Ensure your **GitHub, Medium, and LinkedIn** tell a coherent story — each project links to a writeup, each writeup links to working code.

---

<a id="toc-part-39-penetration-testing-methodologies--report-writing"></a>
## Part 39: Penetration Testing Methodologies & Report Writing

> **Why This Exists:** Knowing how to exploit is useless if you can't structure an engagement professionally or communicate findings in a way that drives remediation. This part covers the "how to operate" layer that transforms technical skills into a professional practice.

### **Stage 1: Industry-Standard Engagement Frameworks**

_Goal: Understand the structured methodologies that govern professional engagements._

- [ ] **PTES (Penetration Testing Execution Standard):** Master all **7 phases** — Pre-Engagement Interactions, Intelligence Gathering, Threat Modeling, Vulnerability Research, Exploitation, Post-Exploitation, Reporting; know what deliverables each phase produces and why skipping a phase breaks engagement quality.

- [ ] **OWASP Web Security Testing Guide (WSTG v4.x):** Use the **WSTG test case IDs** (WSTG-INFO-001 → WSTG-BUSL-009) as a structured web assessment checklist; map every finding to a WSTG ID for client-facing credibility and compliance evidence.

- [ ] **NIST SP 800-115 (Technical Guide to Information Security Testing):** Understand the federal-grade methodology covering **examination, identification, and validation techniques**; required knowledge for US government and regulated-industry engagements.

- [ ] **OWASP MASTG (Mobile Application Security Testing Guide):** Apply dedicated **MASTG test cases** for Android/iOS assessments; use the **MAS Checklist** for compliance-grade mobile audits; map findings to MASVS security requirements.

- [ ] **OSSTMM (Open Source Security Testing Methodology Manual):** Understand the **RAV (Risk Assessment Value)** scoring model and the concept of **attack surface measurement** — useful for mature clients who want quantified security metrics beyond CVSS.

- [ ] **Methodology Selection:** Know when to invoke each — PTES for comprehensive red team ops, NIST 800-115 for compliance-driven audits, OWASP WSTG for web-focused engagements, MASTG for mobile; document your methodology selection in every report.

---

### **Stage 2: Scoping, Legal Frameworks & Engagement Management**

_Goal: Define engagement boundaries that protect the tester and client legally and operationally._

- [ ] **Statement of Work (SoW) Construction:** Draft and review SoW language covering **scope definition (IP ranges, domains, application URLs), deliverables, timelines, payment milestones, liability caps, and IP ownership** of testing artifacts; ambiguous scope = legal exposure.

- [ ] **Rules of Engagement (RoE) Document:** Define in writing: **authorized IP ranges and domains, permitted testing hours (business hours vs. 24/7), testing exclusions (life-safety systems, production DBs), escalation contacts, emergency abort criteria, and data handling requirements**.

- [ ] **Get-Out-of-Jail Letter:** Understand the format and legal requirements of the **written authorization letter** — verify the signatory has authority to authorize testing, check it covers all target systems, and carry it during physical tests; know what makes it legally binding vs. inadequate.

- [ ] **Legal Framework Awareness:** Understand how **CFAA (US), Computer Misuse Act 1990 (UK), IT Act 2000 + Amendment 2008 (India), GDPR, and EU Cybersecurity Act** define criminal vs. authorized access; know how cross-border engagements create dual-jurisdiction liability.

- [ ] **Evidence & Data Handling Policy:** Establish rules for how **captured credentials, PII, financial records, source code, and exfiltrated data are classified, encrypted at rest, access-controlled, and securely destroyed** post-engagement; include this in every SoW.

- [ ] **Engagement Communication Cadence:** Define **weekly status calls, critical finding escalation (phone within 1 hour), interim report delivery, and final debrief meeting** structure; never let a critical finding sit unannounced for 24+ hours.

---

### **Stage 3: Structured Threat Modeling**

_Goal: Apply structured threat identification before testing begins — not after._

- [ ] **STRIDE Threat Model:** Decompose target system components into **processes, data stores, data flows, and external entities**; apply Spoofing / Tampering / Repudiation / Information Disclosure / Denial of Service / Elevation of Privilege to each element; generate a ranked threat list that scopes the test.

- [ ] **PASTA (Process for Attack Simulation and Threat Analysis):** Apply the **7-stage business-centric model** — define objectives → technical scope → application decomposition → threat analysis → vulnerability analysis → attack enumeration → risk/impact analysis; produces a business-risk-aligned test plan.

- [ ] **Attack Trees:** Build **hierarchical attack tree diagrams** rooted at the attack goal with sub-goals as branches; use AND/OR nodes to model alternative paths; identify which branches are highest probability × highest impact for prioritized testing.

- [ ] **Data Flow Diagram (DFD) Trust Boundaries:** Draw Level 0–2 DFDs to identify **trust boundaries, data stores, external entities, and inter-process data flows**; every trust boundary crossing is an attack surface that must be tested.

- [ ] **MITRE ATT&CK as Pre-Test Input:** Use ATT&CK to **pre-identify likely adversary TTPs** based on target industry, known threat actor profiles, and previously disclosed incidents in the sector; build your test plan around these TTPs.

- [ ] **LINDDUN (Privacy Threat Model):** Apply LINDDUN (Linkability, Identifiability, Non-repudiation, Detectability, Disclosure of information, Unawareness, Non-compliance) for privacy-focused assessments — required for GDPR/HIPAA compliance-mapped tests.

---

### **Stage 4: Vulnerability Scoring & Risk Prioritization**

_Goal: Rate findings objectively and communicate risk in business terms — not just CVSS numbers._

- [ ] **CVSS v3.1 Base Metrics:** Master all **8 base metrics** (Attack Vector, Attack Complexity, Privileges Required, User Interaction, Scope, Confidentiality/Integrity/Availability Impact); calculate scores manually before using calculators to build intuition.

- [ ] **CVSS v4.0 Changes:** Understand the **new Supplemental Metrics group** (Automatable, Recovery, Value Density, Response Effort, Provider Urgency) and the replacement of Temporal Metrics with **Threat Metrics (Exploit Maturity)**; know which scoring version your client's compliance framework requires.

- [ ] **EPSS (Exploit Prediction Scoring System):** Use **EPSS probability scores** alongside CVSS to distinguish actively exploited vulnerabilities from theoretical ones; a CVSS 9.8 with 0.1% EPSS differs operationally from a CVSS 7.5 with 95% EPSS.

- [ ] **Business Risk Contextualization:** Calculate **Risk = Likelihood × Business Impact** — map vulnerabilities to: revenue exposure, regulatory fine potential, reputational damage, operational downtime, and data breach notification costs; a CVSS 5.4 on a public-facing OAuth token endpoint may carry more business risk than a CVSS 8.1 on an isolated dev server.

- [ ] **Vulnerability Chaining Analysis:** Identify when **individually low-severity findings combine** into critical-severity attack chains (e.g., SSRF [Medium] + IMDS credential access [Low] + overprivileged IAM role [Medium] = Full Cloud Compromise [Critical]); document chains as unified findings with individual component breakdowns.

- [ ] **Finding Deduplication:** When a single root cause produces multiple manifestations (e.g., 50 instances of the same SQLi pattern), report as **one finding with representative samples** and a count — not 50 separate findings that inflate severity perception and waste remediation effort.

---

### **Stage 5: Professional Report Writing**

_Goal: Deliver findings in a format that survives executive scrutiny and drives budgeted remediation._

- [ ] **Report Architecture:** Master the standard structure: **Cover Page → Executive Summary → Engagement Overview (scope, methodology, timeline) → Attack Narrative → Findings by Severity → Remediation Roadmap → Appendices (evidence, tooling, methodology references, CVSS breakdowns)**.

- [ ] **Executive Summary (Non-Technical):** Write a **1–2 page narrative** for the C-suite covering: overall security posture rating, total findings by severity, most critical business risks, and top 3 priority actions — written for a CFO reading at 35,000 feet, not a sysadmin.

- [ ] **Technical Finding Template:** Each finding must include: **Title | Severity | CVSS Score (v3.1/v4.0) | EPSS % | Affected Asset | Vulnerability Description | Business Impact | Proof of Concept (exact request/response/screenshot) | Remediation Guidance (specific, actionable, with code examples where applicable) | References (CVE, CWE, OWASP ID)**.

- [ ] **Attack Narrative / Kill Chain Story:** Write a **linear narrative** tracing the attacker's path from initial foothold through escalation to maximum impact — this is the section that gets security budgets approved; make it read like a post-breach incident report, not a bullet list.

- [ ] **Remediation Specificity:** Write remediation as **executable technical steps** — e.g., "Apply parameterized queries using `mysqli_prepare()` with bound parameters" not "fix SQL injection"; include patch version numbers, configuration file paths, and code snippets; vague remediation = finding stays open.

- [ ] **Proof-of-Concept Discipline:** PoCs must be **reproducible, minimally invasive, and clearly annotated** — include exact HTTP request/response, commands run, and observed vs. expected behavior; redact real credentials and PII captured; test PoC steps against your own notes before submission.

- [ ] **Remediation Roadmap Tiering:** Tier findings into **Immediate (< 7 days — critical/exploited), Short-term (< 30 days — high), Medium-term (< 90 days — medium), Long-term / Strategic (low + systemic architectural issues)**; include effort estimates and responsible team assignments.

- [ ] **Re-test Procedures:** Document **exactly how the client verifies each remediation** — include test steps, expected output, and acceptance criteria; schedule and execute a **formal re-test engagement** where contracted; issue a re-test supplement report with delta findings.

- [ ] **Report Versioning & Delivery:** Maintain **draft → client review → final** versioning; deliver reports in **password-protected PDF** with restricted printing/copying; PGP-encrypt email attachments; define report retention and destruction policy in the SoW.

---


<a id="toc-part-40-red-team-operations--tradecraft"></a>
## Part 40: Red Team Operations & Tradecraft

> **Safety Gate:** Red team infrastructure, phishing, payload delivery, credential access, lateral movement, and evasion require explicit written authorization and a defined ROE. In production, undocumented operator action becomes incident noise, client risk, and legal evidence against you.

### Strategy & Core Operations

**Planning, ROE, and Safety:**

- [ ] Define **objectives, success criteria, scope, and exclusions**; align with **Rules of Engagement** and legal guardrails.

- [ ] Establish **comms plan, abort criteria, and blowout procedures**; document all operator actions for auditability.

**Infrastructure & C2:**

- [ ] Build **redirectors/frontends** (Nginx/Apache/Cloud/CDN) to shield C2 and rotate domains/certs.

- [ ] Operate multiple **C2 profiles** (HTTP(S)/DNS/SMB/MTLS) with **jitter, sleep, and OPSEC** tuning.

- [ ] Harden **VPS/cloud instances** with minimal services, **egress controls**, and per-op segregation.

- [ ] Use modern **modular C2** (Sliver, Havoc, Mythic, Brute Ratel C4) with **sleep obfuscation/call-stack spoofing** where supported.

- [ ] **Cloud-Native C2:** Tunnel through **Microsoft Graph/SharePoint, Slack/Teams webhooks, other trusted APIs** to blend with business traffic.

- [ ] **IaC for Red Teams:** Provision disposable infra via **Terraform/Ansible** (C2, redirectors, TLS, DNS, storage) for rapid tear-down/rotation.

**Initial Access & Payload Delivery:**

- [ ] Craft **phishing/pretexting** with **HTML smuggling, ISO/LNK/Shortcut** loaders, and **macro/OneNote** lures.

- [ ] Harden payloads with **AMSI evasion, ETW patching, obfuscation**, and staged vs. stageless choices.

**Privilege Escalation & Credential Access:**

- [ ] **Windows:** Exploit **UAC bypass, service misconfigs, token impersonation, vulnerable drivers**, and **LSASS/DPAPI/SAM** extraction.

- [ ] **Linux:** Abuse **sudo/suid/cap_setuid files, misconfigured services, kernel LPE**, and harvest **ssh keys/agent sockets**.

- [ ] Practice **pass-the-hash, pass-the-ticket, Kerberoasting/AS-REP roast**, and **vault/credential manager** theft.

**Lateral Movement & Persistence:**

- [ ] Move via **SMB/WinRM/WMI/RDP**, **SSH agent hijack**, and **PsExec/Impacket** equivalents.

- [ ] Persist with **services, scheduled tasks, WMI event consumers, startup scripts, cron/systemd timers, SSH authorized_keys**.

**Living Off the Land & Evasion:**

- [ ] Use **LOLBAS/GTFOBins** to blend in; prefer **native binaries** over custom tools.

- [ ] Evade **EDR/IDS** with **sideloading, DLL hijack, LOL drivers, memory-only beacons, timestomping, and log tampering**.

- [ ] Tune noise: minimize **parent/child process anomalies**, limit **PowerShell logs (ScriptBlock/Module)**, and watch **Sysmon** events.

**Logging, Monitoring, and Cleanup:**

- [ ] Track footprints in **Windows Event Logs, Sysmon, ETW, Prefetch, AmCache, SRUM**; on Linux in **auth.log, auditd, bash history, journalctl**.

- [ ] Plan **cleanup and restoration** per ROE; document **IOCs, timelines, and access paths** for reporting.

**Automation & Scripting Discipline:**

- [ ] Maintain fluency in **Bash, PowerShell, Python**; script **collection, parsing, and lateral movement** tasks.

- [ ] Template **checklists/playbooks** for repeatable ops; version control tooling and payloads.

<a id="toc-part-41-proof-of-work--career-portfolio"></a>
## Part 41: Proof of Work & Career Portfolio

> **Core Principle:** Theory without evidence is worthless. Every technical skill in this roadmap must be validated through _unfakeable_ proof of work — tools you've built, reports you've written, certifications you've earned, and bugs you've found. This section ties it all together.

### **Stage 1: Certification Roadmap**

_Goal: Validate skills through industry-recognized, hands-on certifications._

**Offensive Security Certifications (Hands-On Priority):**

- [ ] **OSCP (Offensive Security Certified Professional):** The **gold standard** for penetration testing. Complete the **PEN-200 course** and pass the **24-hour practical exam** — demonstrates you can hack real machines, not just answer multiple-choice questions.

- [ ] **OSWE (Offensive Security Web Expert):** Earn the **WEB-300 certification** for advanced **white-box web application exploitation** — source code review, custom exploit development, authentication bypass.

- [ ] **OSED (Offensive Security Exploit Developer):** Earn the **EXP-301 certification** for **Windows userland exploitation** — buffer overflows, DEP/ASLR bypass, shellcode development, ROP chains.

- [ ] **OSEP (Offensive Security Experienced Penetration Tester):** Earn the **PEN-300 certification** for **advanced evasion techniques** — AMSI bypass, process injection, lateral movement in hardened environments.

**Application Security Certifications:**

- [ ] **BSCP (Burp Suite Certified Practitioner):** Complete **PortSwigger Web Security Academy** labs and pass the **practical exam** — validates OWASP Top 10 exploitation, JWT attacks, SSRF, deserialization, and advanced web hacking skills.

- [ ] **CWEE (Certified Web Exploitation Expert):** HTB's certification focused on **advanced web exploitation** — SQL injection, template injection, file upload attacks, deserialization chains.

**AI Security Certifications (Emerging):**

- [ ] **COAE (Certified Offensive AI Expert):** Earn Hack The Box's **AI security certification** covering **LLM exploitation, prompt injection, RAG poisoning, AI red teaming methodology**.

- [ ] **OSAI (OffSec AI-300):** Complete OffSec's **AI security certification** for **offensive AI testing** — validate ability to test and attack AI/ML systems in enterprise environments.

- [ ] **Google AI Essentials / DeepLearning.AI Specialization:** Complete foundational AI courses to validate **understanding of model architecture, training pipelines, and ML math** before specializing in AI security.

**Blue Team & Cloud Certifications:**

- [ ] **BTL1 (Blue Team Level 1):** Validate **SOC analyst skills** — log analysis, SIEM usage, incident response, threat detection.

- [ ] **CCD (Certified CyberDefender):** CyberDefenders certification for **DFIR and threat hunting** — memory forensics, malware analysis, log analysis.

- [ ] **AWS SAA / Azure AZ-500 / GCP Security:** Earn **cloud security certifications** to validate **IAM, networking, compliance, and cloud-native security** skills.

---

### **Stage 2: Technical Portfolio & GitHub Presence**

_Goal: Build a public portfolio that proves you can build, not just study._

- [ ] **GitHub Repository Strategy:** Maintain a **clean, professional GitHub profile** with **2–5 significant security projects** — each with **README, architecture diagrams, usage examples, and documented attack scenarios**.

- [ ] **Clean Commit History:** Practice **atomic commits with descriptive messages** — hiring managers and security teams review your commit history to assess engineering discipline.

- [ ] **Project Categories:** Build projects across multiple domains to demonstrate breadth:
  - **Offensive tool** (custom scanner, exploit framework, payload generator)
  - **Defensive tool** (log analyzer, detection rule generator, YARA rule suite)
  - **AI security tool** (prompt injection tester, LLM red team framework, RAG poisoning PoC)
  - **Automation** (recon pipeline, report generator, CI/CD security scanner)

- [ ] **Documentation Quality:** Every project must include: **installation instructions, usage examples, architecture overview, limitations, and license**. Poor documentation kills credibility.

- [ ] **Contribution to Open Source:** Contribute to **established security tools** (Impacket, BloodHound, Garak, PyRIT, Nuclei, OWASP projects) — demonstrates ability to work with existing codebases, not just greenfield projects.

---

### **Stage 3: Technical Writing & Content**

_Goal: Demonstrate depth of understanding through published analysis._

- [ ] **Technical Blog Posts (Medium / Personal Site):** Write **5–10 substantive, technical breakdowns** of your security research — document **methodology, failures, findings, and remediation guidance** in long-form posts targeting both practitioners and hiring managers.

- [ ] **CTF Writeups:** Publish **detailed writeups for solved CTF challenges** — explain the thought process, dead ends, and eventual solution with code snippets and screenshots.

- [ ] **Vulnerability Disclosures:** Document any **responsibly disclosed vulnerabilities** with **CVE identifiers, impact analysis, and timeline** — these are the most credible proof of offensive capability.

- [ ] **Cheat Sheets & Reference Guides:** Create **condensed reference materials** (OSCP cheat sheet, AD attack playbook, API pentesting checklist) — demonstrates synthesis of complex knowledge and helps the community.

- [ ] **LinkedIn Technical Content:** Post **regular technical insights, tool reviews, and industry commentary** — LinkedIn is the primary hiring platform for security roles; build a professional narrative.

---

### **Stage 4: Bug Bounties & Community Engagement**

_Goal: Validate offensive skills against real-world targets and build reputation._

- [ ] **Bug Bounty Platforms:** Maintain active profiles on **HackerOne, Bugcrowd, Synack, Intigriti, Immunefi (Web3)** — prioritize programs in your specialization (web, API, cloud, AI).

- [ ] **First 10 Valid Findings:** Target **low-hanging fruit first** (open redirects, IDOR, info disclosure) to build platform reputation, then escalate to **critical-severity findings**.

- [ ] **Hall of Fame & Acknowledgments:** Collect **public acknowledgments** from bug bounty programs — these serve as third-party validation of your skills on your resume.

- [ ] **CTF Competitions:** Compete regularly in **picoCTF, NahamCon, HTB CTF, Google CTF, DEFCON CTF qualifiers, AI-specific CTFs (Gandalf, HackAPrompt)** — track your ranking progression.

- [ ] **Community Presentations:** Present findings at **local hacker meetups, BSides, DEFCON villages, OWASP chapter meetings** — build credibility through live demonstrations and Q&A.

- [ ] **Mentorship & Teaching:** Contribute to the community by **mentoring junior practitioners, answering StackOverflow/Reddit questions, creating educational content** — teaching deepens understanding and builds network.

---

### **Stage 5: Career Positioning & Job Search Strategy**

_Goal: Convert skills and proof into career opportunities._

- [ ] **Role Targeting:** Identify specific roles matching your skill profile:
  - **Offensive:** Penetration Tester, Red Team Operator, Exploit Developer, Bug Bounty Hunter
  - **Defensive:** SOC Analyst, Detection Engineer, Incident Responder, Threat Hunter
  - **AppSec:** Application Security Engineer, Security Code Reviewer, DevSecOps Engineer
  - **AI Security:** LLM Red Teamer, AI Safety Engineer, ML Security Researcher, Prompt Security Engineer
  - **Cloud:** Cloud Security Architect, Cloud Pentester, IAM Security Engineer

- [ ] **Resume Engineering:** Structure your resume around **impact and capability delivered** — not just technologies listed. Quantify results: _"Discovered 47 vulnerabilities across 12 bug bounty programs; built automated recon pipeline reducing initial assessment time by 60%."_

- [ ] **Portfolio Coherence:** Ensure your **GitHub, blog, LinkedIn, bug bounty profiles, and certifications** tell a **coherent, unified story** — each project links to a writeup, each writeup links to working code, each certification validates the skills demonstrated in projects.

- [ ] **Interview Preparation:** Practice **technical interviews** covering **live hacking demonstrations, CTF-style challenges, architecture review, threat modeling exercises**, and **behavioral questions** about incident handling and team collaboration.

- [ ] **Continuous Skill Maintenance:** Security is a **continuous learning field** — maintain certifications (OSCP requires CPEs), continue bug bounty hunting, publish new research, attend conferences, and stay current with emerging threats and tools.

---
