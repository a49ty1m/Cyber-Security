# Phase 1: The Unshakeable Foundation

---

### 🧭 Navigation

🏠 [Master Roadmap](README.md) | [Phase 2](Phase-2.md) ➔

---

> [!NOTE]
> **Phase Overview**
>
> - **⏱️ Time Commitment (Full-Time):** 4–6 months
> - **⏱️ Time Commitment (Part-Time):** 6–10 months
> - **🎯 Primary Focus:** Master the TCP/IP stack, OSI model, DNS, HTTP/HTTPS, Linux CLI and administration, Windows administration and Event Viewer, Bash/PowerShell, Python/JavaScript, virtualization, cloud basics (AWS/Azure), Docker/Kubernetes, authentication, sessions, cookies, JSON APIs, CORS, and the cryptographic primitives underpinning all of security.

> [!IMPORTANT]
> **Current Status: Substantially Complete → Entering Phase 2A**
>
> Phase 1 is largely done. Do NOT restart it. Use **just-in-time prerequisite patches** for specific gaps as they arise in later phases.
>
> **What you can do confidently (do not re-study these):**
> - Linux CLI navigation and common commands
> - Basic Linux system investigation
> - Windows administration and basic PowerShell
> - TCP vs UDP, subnetting, DNS at a practical level
> - HTTP requests, basic traffic capture, general networking
>
> **Known gaps — patch only when a future topic requires them:**
>
> | Gap | When to patch | Patch scope |
> |-----|---------------|-------------|
> | Wireshark / deep packet analysis | When Phase 2 Scanning or Sniffing requires it | 2–4 sessions on Wireshark filters and dissection |
> | TLS internals | When Phase 4 HTTPS interception or Phase 6 requires it | TLS handshake + PKI fundamentals only |
> | Linux service administration | When Phase 2 enumeration labs require it | `systemctl`, user management, `/etc/` configs |
> | Kerberos / Windows identity | Before Phase 6 Part 23 (AD attacks) | Phase 1 Stage 5 & 6 in Part 1C |
> | Advanced PowerShell | During Phase 6 AD work | Targeted PS scripting for AD enumeration |
>
> **Your next action: proceed to [Phase 2](Phase-2.md) → Part 4 (Footprinting & Reconnaissance).**


> [!NOTE]
>
> ### 📝 Phase 1 Documentation Requirements
>
> Every topic you complete in this phase must be documented and committed to your private Git repository. Required artifacts:
>
> - **Markdown lab notes** for every lab completed (structured: objective → steps → output → lessons learned)
> - **Network diagrams** (draw.io/Excalidraw) of your home lab topology
> - **Screenshots** of completed labs, tool output, and configuration changes
> - **Shell command logs** — save terminal history for key sessions
> - **Git commits** — commit after every lab session with descriptive messages
>
> _This documentation becomes the foundation of your Phase 10 portfolio. Start building it now, not later._

---

> [!IMPORTANT]
>
> ### 🧱 Phase 1 Pacing Checkpoints
>
> Phase 1 is intentionally broad. Treat it as six smaller milestones instead of one giant block:
>
> 1. **Lab setup complete:** Hypervisor installed, baseline VMs created, Git documentation repository active.
> 2. **Computer fundamentals complete:** Hardware, OS internals, memory, data representation, and basic scripting understood.
> 3. **Linux administration complete:** Users, permissions, services, networking, logs, storage, and hardening practiced.
> 4. **Windows administration complete:** Users, NTFS permissions, Event Viewer, PowerShell, registry, and AD basics practiced.
> 5. **Networking complete:** OSI/TCP-IP, subnetting, routing, DNS, DHCP, HTTP/S, packet capture, and troubleshooting demonstrated.
> 6. **Cryptography complete:** Hashing, symmetric/asymmetric crypto, TLS, PKI, certificates, password storage, and common failure modes demonstrated.
>
> Do not wait for the final capstone to feel progress. Commit evidence at each checkpoint.

---

### 🗂️ Table of Contents

- [Career Foundation & Lab Setup](#career-foundation-lab-setup)
  - [Professional Development & Enablers](#professional-development-enablers)
  - [Home Lab Hardware Requirements](#home-lab-hardware-requirements)
  - [Academic & Career Alignment](#academic-career-alignment)
  - [Certification Alignment Map](#certification-alignment-map)
  - [Training Platforms & Lab Environments](#training-platforms-lab-environments)
  - [Foundation Proof Gate](#foundation-proof-gate)
- [Part 1: Fundamentals](#part-1-fundamentals)
  - [Stage 1: Hardware, CPU & Pre-Boot Environment](#stage-1-hardware-cpu-pre-boot-environment)
  - [Stage 2: Operating System Internals](#stage-2-operating-system-internals)
  - [Stage 3: Memory Management](#stage-3-memory-management)
  - [Stage 4: Data Representation & Logic](#stage-4-data-representation-logic)
  - [Stage 5: Wireless & Physical Connections](#stage-5-wireless-physical-connections)
  - [Stage 6: Mobile Platform Awareness](#stage-6-mobile-platform-awareness)
  - [Stage 7A: Programming & Scripting Fundamentals (Python, Bash, PowerShell, JS)](#stage-7a-programming-scripting-fundamentals)
  - [Stage 7B: C & C++ (Phase 7 — deferred)](#stage-7b-c-cpp-programming)
- [Part 1B: Linux Administration](#part-1b-linux-administration)
  - [Stage 1: User & Access Management (Linux)](#stage-1-user-access-management-linux)
  - [Stage 2: Service & Process Management (Linux)](#stage-2-service-process-management-linux)
  - [Stage 3: Networking (Linux)](#stage-3-networking-linux)
  - [Stage 4: Log Analysis & Monitoring (Linux)](#stage-4-log-analysis-monitoring-linux)
  - [Stage 5: Storage & Filesystem (Linux)](#stage-5-storage-filesystem-linux)
  - [Stage 6: Security Hardening (Linux)](#stage-6-security-hardening-linux)
  - [Lab Progression (Linux)](#lab-progression-linux)
- [Part 1C: Windows Administration](#part-1c-windows-administration)
  - [Stage 1: User & Access Management (Windows)](#stage-1-user-access-management-windows)
  - [Stage 2: System Management (Windows)](#stage-2-system-management-windows)
  - [Stage 3: Event Viewer & Auditing (Windows)](#stage-3-event-viewer-auditing-windows)
  - [Stage 4: PowerShell Administration (Windows)](#stage-4-powershell-administration-windows)
  - [Stage 5: Active Directory Concepts (Prerequisite for Part 23)](#stage-5-active-directory-concepts-prerequisite-for-part-23)
  - [Stage 6: Windows Identity & Kerberos Protocol Foundations (Critical Prerequisite for Part 23)](#stage-6-windows-identity-kerberos-foundations)
  - [Lab Progression (Windows)](#lab-progression-windows)
  - [macOS Security Awareness (Supplemental)](#macos-security-awareness-supplemental)
- [Part 2: Networking Fundamentals](#part-2-networking-fundamentals)
  - [Layer 1: Physical (The Hardware Surface)](#layer-1-physical-the-hardware-surface)
  - [Layer 2: Data Link (The Local Target)](#layer-2-data-link-the-local-target)
  - [Layer 3: Network (The Routing Logic)](#layer-3-network-the-routing-logic)
  - [Layer 4: Transport (The Reliability Layer)](#layer-4-transport-the-reliability-layer)
  - [Layers 5-7: Application & Session (The Payload)](#layers-5-7-application-session-the-payload)
  - [Lab Progression & Professional Development (2026 Red Team Focus)](#lab-progression-professional-development-2026-red-team-focus)
  - [Automation & Programmability](#automation-programmability)
  - [PCAP Analysis — Systematic Methodology](#part-2-stage-pcap-analysis)
- [Part 3: Cryptography](#part-3-cryptography)
  - [Stage 1: Core Concepts & Algorithms](#stage-1-core-concepts-algorithms)
  - [Stage 2: Secure Communication (Data in Transit)](#stage-2-secure-communication-data-in-transit)
  - [Stage 3: Identity & Trust (PKI)](#stage-3-identity-trust-pki)
  - [Stage 4: Data at Rest & Password Security](#stage-4-data-at-rest-password-security)
  - [Stage 5: Cryptographic Attacks & Weaknesses](#stage-5-cryptographic-attacks-weaknesses)
  - [Lab Progression (Cryptography)](#lab-progression-cryptography)
- [Part 3B: Authentication Standards Primer](#part-3b-authentication-standards-primer)
  - [Stage 1: Session-Based Authentication](#auth-primer-stage-1-session-based-auth)
  - [Stage 2: Token-Based Authentication & JWT](#auth-primer-stage-2-token-based-auth)
  - [Stage 3: OAuth 2.0 — Delegated Authorization](#auth-primer-stage-3-oauth2)
  - [Stage 4: OpenID Connect (OIDC)](#auth-primer-stage-4-oidc)
  - [Stage 5: API Authentication Patterns](#auth-primer-stage-5-api-auth-patterns)
  - [Stage 6: MFA Types & Weaknesses](#auth-primer-stage-6-mfa-types)
  - [Lab Progression (Authentication Standards)](#auth-primer-lab-progression)
- [Part 3C: Web Technology Fundamentals](#part-3c-web-technology-fundamentals)
  - [Stage 1: HTTP — The Protocol of the Web](#stage-1-http-the-protocol-of-the-web)
  - [Stage 2: Cookies, Sessions & Tokens](#stage-2-cookies-sessions-tokens)
  - [Stage 3: Same-Origin Policy, CORS & Web Security Headers](#stage-3-same-origin-policy-cors-web-security-headers)
  - [Stage 4: Web Authentication Patterns](#stage-4-web-authentication-patterns)
  - [Stage 5: REST APIs, JSON & Modern Web Architecture](#stage-5-rest-apis-json-modern-web-architecture)
  - [Lab Progression (Web Technology Fundamentals)](#lab-progression-web-technology-fundamentals)

---

<a id="career-foundation-lab-setup"></a>

## Career Foundation & Lab Setup

_Before starting the technical curriculum, establish your academic foundation, lab environment, and practice platforms._

<a id="professional-development-enablers"></a>

### **Professional Development & Enablers**

- [ ] **Lab Progression Map (Packet Tracer → GNS3/EVE-NG → Wireshark validation)**
  - **Goal:** Move from simple networking practice to realistic, packet-level practice without guessing.
  - [ ] Stage A — Packet Tracer (learning topology + basic configs)
    - Build networks quickly (routers/switches/firewalls).
    - Learn addressing, routing, VLANs, ACLs, NAT basics.
    - Focus: “Does my design work?”
  - [ ] Stage B — GNS3/EVE-NG (real OS images + realistic behavior)
    - Same idea, but with actual services and Linux-based networking stacks.
    - Use real images (where possible) to practice:
      - routing protocols (OSPF/BGP basics)
      - firewall policies
      - DNS/DHCP
      - VPNs (IPsec/OpenVPN)
      - segmentation, multi-tier routing
  - [ ] Stage C — Validate everything with Wireshark (packet truth)
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
  - **Goal:** Avoid being locked into one platform. Labs should migrate.
  - [ ] Type-1 hypervisors (closer to the hardware)
    - ESXi, Proxmox
    - Usually better performance and easier “lab appliance” patterns.
  - [ ] Type-2 hypervisors (runs on top of an OS)
    - VMware Workstation, VirtualBox
    - Great for quick VMs, testing, and local dev.
  - [ ] Practice habit:
    - Make at least one “template VM” that can be moved (or recreated quickly) between platforms.
    - Use consistent disk images / cloud-init / documented steps.
    - Result: If one platform breaks, your lab doesn’t die with it.

- [ ] **Cloud Assets Core (VPC/VNET + Security controls + IAM + Load Balancing)**
  - **Goal:** Learn cloud networking the way defenders and attackers reason about it.
  - > ⚠️ **Note:** This section introduces cloud concepts early. If VPC/VNET, security groups, and IAM feel abstract, revisit this section after completing Part 2 (Networking Fundamentals). Full cloud security is covered in Part 24 (Phase 6).
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
  - **Goal:** Your time should go to learning—not clicking the same steps.
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
  - **Goal:** Become fluent in “visibility.” What logging exists, what it misses, and why.
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
  - **Goal:** Use structured certification objectives to avoid missing basics.
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
  - **Goal:** Make your practice safe and accountable.
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
  - **Goal:** Prepare for high-volume tasks you’ll face in real workflows.
  - What to scale:
    - Mass config deployment across many lab nodes
    - Port scan sweeps to baseline services
    - Faster feedback loops
  - Good practice:
    - Use rate limiting.
    - Use concurrency controls.
    - Store scan results as structured output (JSON/CSV) so you can diff runs.

- [ ] **Monitoring Deep Dives (SNMP/NetFlow to visualize exfil patterns)**
  - **Goal:** Practice detection at the “pattern” level, not just “did the packets work?”
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

<a id="home-lab-hardware-requirements"></a>

### **Home Lab Hardware Requirements**

> [!TIP]
> **Goal:** Avoid wasting money on inadequate hardware or overspending before you know your specialization.

- [ ] **Minimum Specs:** **32GB RAM** (16GB absolute minimum for running 2–3 VMs simultaneously), **quad-core CPU with VT-x/AMD-V** (Intel VT or AMD-V required for nested virtualization), **500GB+ SSD**. Without hardware virtualization support, nested VMs (VMs inside VMs) will not work.

- [ ] **Recommended Specs:** **64GB RAM, 8-core CPU, 1TB NVMe SSD**. This comfortably runs a Domain Controller + 3 workstations + attacker Kali VM simultaneously for AD labs (Part 23).

- [ ] **Wireless Testing Adapter:** Purchase an **Alfa AWUS036ACH** (or similar Realtek RTL8812AU/RTL8814AU chipset) USB adapter that supports **monitor mode and packet injection**. Built-in WiFi cards rarely support these modes. Required for Part 21 (Wireless Pentesting).

- [ ] **Budget Tiers:** **Tier 1 (~$300):** Used ThinkPad T480/X1 Carbon with 32GB RAM upgrade. **Tier 2 (~$600):** Refurbished Dell Precision/HP Z-series with 64GB. **Tier 3 (~$1,500):** Custom mini-ITX Proxmox server with 128GB RAM for persistent lab infrastructure.

- [ ] **Cloud Supplement:** Use **AWS Free Tier / Azure $200 credit / GCP $300 credit** for cloud security labs (Part 24) without maintaining local infrastructure. Set **billing alerts** to avoid surprise charges.

---

<a id="academic-career-alignment"></a>

### **Academic & Career Alignment**

> [!TIP]
> **Goal:** Maximize your formal education and align academic work with offensive security career requirements.

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
  - **Goal:** differentiate from other graduates.

---

<a id="certification-alignment-map"></a>

### **Certification Alignment Map**

> [!TIP]
> **Goal:** Know which certifications to pursue at each phase for industry credibility.

| Phase Completed | Recommended Certifications                             | Notes                                                    |
| --------------- | ------------------------------------------------------ | -------------------------------------------------------- |
| Phase 1         | **CompTIA A+, Network+, Security+**                    | Foundation validation; Security+ meets DoD 8570 baseline |
| Phase 2         | **eJPT (INE), CompTIA PenTest+**                       | Entry offensive validation                               |
| Phase 3         | **CySA+ (CompTIA), BTL1 (Security Blue Team)**         | Blue team validation                                     |
| Phases 1–4      | **eWPT (INE), BSCP (PortSwigger)**                     | Web security specialization                              |
| Phase 5         | **GMOB (GIAC Mobile Device Security), eWMPT (INE)**    | Mobile security specialization; pursue after Phase 5 completion |
| Phases 1–6      | **OSCP (OffSec), PNPT (TCM), CRTP (Altered Security)** | Mid-level offensive; OSCP is the gold standard           |
| Phases 1–7      | **GCFE, GCFA (GIAC Forensics), eCRE (INE)**            | DFIR / RE specialization                                 |
| Phases 1–8      | **OSEP (OffSec), CRTO (Zero-Point), CISSP**            | Senior offensive / architecture validation               |
| Full Roadmap    | **OSCE3, GXPN, SANS GSE**                              | Expert-level; pursue only 1–2                            |

> ⚠️ **Certifications validate skills; they do not replace them.** Do not pursue certifications until you can pass them based on roadmap skills alone. Never cert-chase before building real capability.

---

<a id="training-platforms-lab-environments"></a>

### **Training Platforms & Lab Environments**

> [!TIP]
> **Goal:** Build practical muscle memory through structured, hands-on hacking exercises.

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
  - **Goal:** develop speed, creativity, and multi-domain problem solving under pressure.

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
  - **Goal:** Earn the **Burp Suite Certified Practitioner (BSCP)** certification.

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

<a id="foundation-proof-gate"></a>

### **Foundation Proof Gate**

> [!TIP]
> **Goal:** Prove readiness before touching serious offensive material.

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
<a id="part-1-fundamentals"></a>

## Part 1: Fundamentals

<a id="stage-1-hardware-cpu-pre-boot-environment"></a>

### **Stage 1: Hardware, CPU & Pre-Boot Environment**

> [!TIP]
> **Goal:** Master the machine before the Operating System initializes.

- [ ] **CPU Operations:** Master the **Fetch-Decode-Execute** cycle to understand how code actually runs at the hardware level.

- [ ] **Registers:** Command the "steering wheel" of the CPU: **EAX/RAX** (accumulator), **ESP/RSP** (stack pointer), and **EIP/RIP** (instruction pointer).

- [ ] **Architecture Types:** Distinguish between **x86** (32-bit) and **x64** (64-bit) addressing and how they handle memory instructions differently.

- [ ] **Instruction Sets:** Develop a working familiarity with **Assembly** language (**MOV**, **PUSH**, **POP**, **CALL**, **JMP**).

- [ ] **The Boot Chain:** Master the sequence from **UEFI/Secure Boot** $\rightarrow$ **Bootloader** $\rightarrow$ **Kernel Load** $\rightarrow$ **Init/Systemd**.

- [ ] **Hardware I/O & DMA:** Understand how **Direct Memory Access (DMA)** allows peripherals to read/write system RAM by bypassing the CPU.

- [ ] **Storage Forensics:** Understand the physical data storage on **HDDs vs. SSDs** and why "deleting" is not "wiping" in a forensics context.

---

<a id="stage-2-operating-system-internals"></a>

### **Stage 2: Operating System Internals**

> [!TIP]
> **Goal:** Understand the resource manager and its internal logic.

- [ ] **Privilege Levels:** Master the **"Ring" architecture**; specifically the separation between **Ring 0** (Kernel) and **Ring 3** (User).

- [ ] **System Calls:** Trace syscall execution (e.g., **NtCreateFile** or **execve**) from user-space API calls through the Interrupt to the kernel handler.

- [ ] **Process & Thread Mechanics:** Understand the lifecycle of processes and threads, including scheduling and context switching.

- [ ] **Process Environment Block (PEB):** In Windows, master the **PEB structure** to find loaded DLLs or implement anti-debugging techniques.

- [ ] **Authorization & Tokens:** Master Windows **SIDs**, **Access Tokens**, and **Token Impersonation**; understand Linux **Namespaces** and **Cgroups** (the basis for containers).

- [ ] **File Systems (Linux):** Master the root directory structure, **Inodes**, and the **"Everything is a file"** philosophy.

- [ ] **File Systems (Windows):** Master **NTFS permissions**, **Registry hives**, and the usage of **Alternate Data Streams (ADS)** to hide payloads.

---

<a id="stage-3-memory-management"></a>

### **Stage 3: Memory Management**

> [!TIP]
> **Goal:** Understand how memory is organized and managed.

- [ ] **Virtual Memory:** Learn how the OS maps physical RAM to virtual addresses to provide process isolation.

- [ ] **The Stack:** Master the **LIFO** (Last-In, First-Out) structure and the **Function Prologue/Epilogue** to understand how return addresses are stored.

- [ ] **The Heap:** Understand **dynamic memory allocation** and how applications request memory at runtime.

- [ ] **Segmentation & Paging:** Understand **segment descriptors** and **page tables** for virtual address translation.

- [ ] **Memory Protection:** Learn about **page permissions (R/W/X)** and **privilege level separation**.

---

<a id="stage-4-data-representation-logic"></a>

### **Stage 4: Data Representation & Logic**

> [!TIP]
> **Goal:** Master binary representation and Boolean logic fundamentals.

- [ ] **Number Systems:** Be able to convert between **Binary, Decimal, and Hexadecimal** mentally.

- [ ] **Boolean Logic:** Master **AND, OR, NOT, and XOR** (the foundation of encryption and obfuscation).

- [ ] **File Headers:** Identify file types (EXE, ELF, JPG) by their **"Magic Bytes"** instead of extensions.

---

<a id="stage-5-wireless-physical-connections"></a>

### **Stage 5: Wireless & Physical Connections**

> [!TIP]
> **Goal:** Understand wireless protocols and physical security infrastructure at a foundational level. Deep offensive techniques for each wireless protocol are covered in Part 21 (Wireless Pentesting, Phase 5).

**WiFi Fundamentals:**

- [ ] **802.11 Standards:** Understand **802.11a/b/g/n/ac/ax**, frequency bands (**2.4GHz, 5GHz, 6GHz**), and channel allocation.

- [ ] **WiFi Authentication:** Learn **Open, WEP, WPA/WPA2/WPA3** handshakes and encryption methods (**TKIP, CCMP, GCMP**).

- [ ] **Enterprise WiFi:** Understand **EAP variants (PEAP, TTLS, TLS)** and **RADIUS** server architecture.

- [ ] **Regulatory:** Know **FCC/ETSI** regulations, **DFS**, and regional channel restrictions.

**RF Survey Fundamentals:**

- [ ] **Antennas & Gain:** Understand antenna types (omni/directional), **dBi gain**, **attenuation**, and **FSPL**.

- [ ] **Channel Planning:** Know **2.4/5/6 GHz** channel spacing, **overlap**, and interference concepts.

- [ ] **Tools Intro:** Basic understanding of **Kismet, iw, iwconfig** for monitoring networks.

**Wireless & IoT Protocol Awareness:**

- [ ] **Bluetooth/BLE Awareness:** Know that **Bluetooth Classic** (profiles, L2CAP, RFCOMM) and **BLE** (GAP, GATT, advertising, pairing) exist as distinct stacks with different security models. 📌 _Full BLE exploitation is covered in Part 21 Stage 4._

- [ ] **NFC/RFID Awareness:** Know that **NFC (ISO14443)** and **RFID (passive/active)** are used for access control, payments, and tracking. 📌 _Full NFC/RFID attacks are covered in Part 21 Stage 6._

- [ ] **IoT Protocol Awareness:** Know that **Zigbee** (mesh, 802.15.4), **Z-Wave**, and **LoRaWAN** (gateway-node, long-range) exist as IoT networking protocols with distinct security models. 📌 _Full IoT protocol exploitation is covered in Part 21 Stage 5._

**Physical Infrastructure:**

- [ ] **Cable Infrastructure:** Know **UTP/STP, fiber optics**, connector types, and physical plant organization.

- [ ] **Environmental & Physical Security Awareness:** Understand **electromagnetic shielding basics** and that **physical access control systems** (smart cards, RFID readers) and **TEMPEST concepts** exist. 📌 _Physical penetration testing is covered in Part 32 (Phase 7). Hardware hacking is covered in Part 30 (Phase 7)._

---

<a id="stage-6-mobile-platform-awareness"></a>

### **Stage 6: Mobile Platform Awareness**

> [!TIP]
> **Goal:** Know that mobile platforms have distinct architectures and security models. Hands-on mobile hacking is covered in Part 22 (Phase 5).

- [ ] **Android vs iOS Architecture:** Understand at a high level that **Android** (APK format, Linux kernel, sandboxing, SELinux) and **iOS** (IPA format, Mach-O binaries, Secure Enclave, code signing) have fundamentally different security models.

- [ ] **Mobile Security Concepts:** Know that **rooting/jailbreaking**, **certificate pinning**, **biometric authentication**, and **hardware-backed keystores** are key security mechanisms on mobile platforms.

> [!NOTE]
> **Cross-Reference:** Full mobile architecture details (APK/IPA structure, SELinux sandboxing, app permissions, Keychain/Keystore internals) and all exploitation techniques (Frida, SSL pinning bypass, runtime manipulation) are covered in **[Part 22: Mobile Platform Pentesting](Phase-5.md#part-22-mobile-platform-pentesting)** (Phase 5). Do not attempt until you have completed Phases 2–4.

---

<a id="stage-7a-programming-scripting-fundamentals"></a>

### **Stage 7A: Programming & Scripting Fundamentals**

> [!TIP]
> **Goal (Stage 7A):** Build a strong programming foundation for cybersecurity by learning to automate tasks, understand software internals, interact with operating systems and networks, and create custom security tooling. This stage covers Python, Bash, PowerShell, and JavaScript — the four languages with immediate utility from Phase 1. **C and C++ are deferred to Stage 7B in Phase 7**, where binary analysis context makes them immediately applicable.
>
> **Stage 7B (C & C++) lives in Phase 7 — before Parts 28 and 42.** Do not attempt C or C++ now. They require debugger experience and binary analysis context to learn meaningfully.

---

#### **Python (Automation, Networking & Security Scripting)**

- [ ] **Core Language Fundamentals:** Master variables, data types, operators, strings, collections (lists, tuples, dictionaries, sets), control flow, loops, functions, modules, packages, decorators, generators, context managers, object-oriented programming, file handling, exception handling, virtual environments (venv), pip, and project structure.

- [ ] **Networking Programming:** Learn socket programming (TCP/UDP), HTTP communication, REST APIs, DNS interaction, SSL/TLS basics, and concurrent networking using threading, multiprocessing, and asyncio.

- [ ] **Security Libraries (Python):** Master the following Python libraries in the given order:

  **🌐 HTTP & Web Automation**
  - [ ] **requests** – HTTP requests, REST APIs, sessions, authentication
  - [ ] **BeautifulSoup (bs4)** – HTML parsing and web scraping
  - [ ] **Selenium** – Browser automation and dynamic web application testing

  **🌍 Networking & Reconnaissance**
  - [ ] **socket** – TCP/UDP networking, client-server communication
  - [ ] **dnspython** – DNS enumeration and record analysis
  - [ ] **scapy** – Packet crafting, sniffing, and network protocol analysis
  - [ ] **pyshark** – Packet capture (PCAP) analysis using Wireshark/TShark

  **🔐 Cryptography & Secure Communications**
  - [ ] **cryptography** – Encryption, hashing, digital signatures, certificates
  - [ ] **paramiko** – SSH automation, remote command execution, SFTP

  **📂 Parsing & Data Processing**
  - [ ] **re** – Regular expressions for pattern matching
  - [ ] **json** – JSON parsing and manipulation
  - [ ] **xml.etree.ElementTree / lxml** – XML parsing
  - [ ] **csv** – CSV file processing
  - [ ] **PyYAML** – YAML parsing and configuration handling
  - [ ] **urllib.parse** – URL parsing and encoding/decoding

  **💥 Exploit Development (Advanced)**
  - [ ] **pwntools** _(learn later)_ – Binary exploitation, CTFs, exploit development, ROP, shellcode

- [ ] **Automation Projects:** Build custom:
  - [ ] Port scanners
  - [ ] Banner grabbers
  - [ ] Directory brute forcers
  - [ ] Web crawlers
  - [ ] Log analyzers
  - [ ] IOC extractors
  - [ ] API automation tools
  - [ ] Report generators
  - [ ] Vulnerability checkers
  - [ ] Packet parsers

- [ ] **Secure Coding Practices:** Learn input validation, error handling, logging, configuration management, secrets handling, dependency management, and code documentation.

- [ ] **Code Quality:** Understand debugging, profiling, testing (pytest), linting, formatting, and version control using Git.

- [ ] **Learning Outcome:** Be capable of writing professional automation scripts and custom security tools without relying entirely on third-party utilities.

---

#### **JavaScript & Node.js (Web, Browser & API Security)**

> [!NOTE]
> **JavaScript Scope in Phase 1:** The functional minimum for Phase 1 is: core language syntax, browser APIs, DOM basics, the fetch/axios communication layer, and the Security Context section (XSS, prototype pollution, CSRF, CORS misconfig). The Node.js/Express, Service Worker, SSE, and modern framework awareness content is intentionally brief and awareness-level — revisit it in Phase 4 with web application testing context where it becomes immediately applicable. Do not stall Phase 1 attempting to master React, Angular, or Express.js depth before moving forward.

- [ ] **Core JavaScript:** Master variables, data types, operators, scope, hoisting, closures, prototypes, prototype chain, objects, arrays, functions, asynchronous programming, callbacks, Promises, async/await, ES6+ features, modules, classes, the event loop, memory model, DOM manipulation, BOM, and browser APIs.

- [ ] **Node.js Fundamentals:** Learn npm, package management, Express.js, middleware, routing, filesystem APIs, child processes, streams, buffers, environment variables, authentication, session management, JWT handling, server-side JavaScript, and REST API development.

- [ ] **Browser Internals:** Understand:
  - [ ] Cookies (attributes: `HttpOnly`, `Secure`, `SameSite`) — _security reasoning for each attribute is covered in full in **Part 3C Stage 2: Cookies, Sessions & Tokens**_
  - [ ] localStorage
  - [ ] sessionStorage
  - [ ] IndexedDB
  - [ ] Cache Storage API
  - [ ] Service Workers
  - [ ] Fetch API
  - [ ] XMLHttpRequest (XHR)
  - [ ] WebSockets
  - [ ] Server-Sent Events (SSE)
  - [ ] Cross-Origin Resource Sharing (CORS) _(canonical full treatment in Part 3C Stage 3: Same-Origin Policy, CORS & Web Security Headers)_
  - [ ] Content Security Policy (CSP)
  - [ ] Same-Origin Policy (SOP)
  - [ ] postMessage API
  - [ ] Browser rendering pipeline
  - [ ] DevTools for debugging and network analysis

- [ ] **JavaScript Security APIs & Libraries:** Gain practical experience with:

  **🌐 HTTP & API Communication**
  - [ ] **fetch** – Modern HTTP requests
  - [ ] **axios** – API requests and interceptors
  - [ ] **WebSocket API** – Real-time communication
  - [ ] **EventSource (SSE)** – Server-Sent Events

  **🧩 DOM Manipulation**
  - [ ] **DOM API** – querySelector, events, element manipulation
  - [ ] **DOMParser** – HTML/XML parsing
  - [ ] **MutationObserver** – Detecting DOM changes

  **🔍 Parsing & Data Handling**
  - [ ] **JSON** – Serialization and parsing
  - [ ] **URL & URLSearchParams** – URL parsing and manipulation
  - [ ] **FormData** – Multipart form handling
  - [ ] **TextEncoder / TextDecoder** – Encoding and decoding

  **🔐 Security & Cryptography**
  - [ ] **Web Crypto API** – Hashing, encryption, key generation
  - [ ] **jsonwebtoken** – JWT creation and verification
  - [ ] **crypto (Node.js)** – Server-side cryptography

  **⚙️ Automation & Testing**
  - [ ] **Puppeteer** – Chrome automation
  - [ ] **Playwright** – Cross-browser automation
  - [ ] **jsdom** – DOM emulation for testing

- [ ] **Security Context:** Study:
  - [ ] DOM XSS
  - [ ] Reflected, Stored & DOM-based XSS
  - [ ] Prototype Pollution
  - [ ] Client-side Injection
  - [ ] Open Redirects
  - [ ] CSRF
  - [ ] CORS Misconfiguration
  - [ ] postMessage abuse
  - [ ] Clickjacking
  - [ ] JWT misuse
  - [ ] WebSocket security
  - [ ] CSP bypasses
  - [ ] Cookie security
  - [ ] LocalStorage & SessionStorage abuse
  - [ ] Service Worker abuse
  - [ ] Client-side request smuggling (awareness)

- [ ] **Automation Projects:** Build custom:
  - [ ] Web crawlers
  - [ ] API fuzzers
  - [ ] Endpoint enumerators
  - [ ] JavaScript endpoint extractors
  - [ ] Secret/API key finders
  - [ ] Link and route discovery tools
  - [ ] JWT analyzers
  - [ ] CORS testing tools
  - [ ] CSP analyzers
  - [ ] Browser automation scripts

- [ ] **Modern Framework Awareness:** Learn how React, Angular, Vue, Svelte, Next.js, Nuxt.js, and Electron influence modern attack surfaces without becoming a frontend developer.

- [ ] **AI Web Applications:** Understand how AI platforms such as ChatGPT, Claude, Gemini, Microsoft Copilot, and similar LLM applications operate as JavaScript frontends communicating with backend APIs, including streaming responses, authentication flows, and browser-based security considerations.

- [ ] **Code Quality:** Learn debugging with Chrome DevTools, Node.js Inspector, ESLint, Prettier, testing (Jest/Vitest), dependency auditing (npm audit), package security, and version control using Git.

- [ ] **Learning Outcome:** Confidently inspect, analyse, automate, and test modern JavaScript applications, SPAs, APIs, browser behaviour, and client-side security during professional web application penetration testing.

---

#### **C (Operating Systems & Memory Fundamentals)**

- [ ] **Language Fundamentals:** Master variables, data types, operators, pointers, pointer arithmetic, arrays, strings, structs, unions, enums, typedefs, functions, recursion, bitwise operations, macros, preprocessing, header files, static vs dynamic variables, dynamic memory allocation, compilation, linking, and debugging.

- [ ] **Memory Management:** Understand:
  - [ ] Stack
  - [ ] Heap
  - [ ] Text Segment (.text)
  - [ ] Data Segment (.data)
  - [ ] BSS (.bss)
  - [ ] Memory Alignment
  - [ ] Padding
  - [ ] Stack Frames
  - [ ] Calling Conventions (cdecl, stdcall, fastcall, System V ABI)
  - [ ] Process Memory Layout
  - [ ] Buffer Boundaries
  - [ ] Memory Allocation (malloc, calloc, realloc, free)

- [ ] **System Programming:** Learn:
  - [ ] File descriptors
  - [ ] Processes
  - [ ] Threads (POSIX Threads)
  - [ ] Signals
  - [ ] Pipes
  - [ ] Named Pipes (FIFO)
  - [ ] TCP/UDP Sockets
  - [ ] Shared Memory
  - [ ] Semaphores
  - [ ] Message Queues
  - [ ] IPC mechanisms
  - [ ] fork()
  - [ ] exec() family
  - [ ] wait()/waitpid()
  - [ ] system() and execve()
  - [ ] Linux system calls
  - [ ] File permissions
  - [ ] Linux APIs (unistd, fcntl, syscalls)

- [ ] **Compiler & Binary Fundamentals:** Understand:
  - [ ] GCC
  - [ ] Clang
  - [ ] Makefiles
  - [ ] Static vs Dynamic Linking
  - [ ] Object Files (.o)
  - [ ] ELF Binary Format
  - [ ] Symbols
  - [ ] Libraries (.a / .so)
  - [ ] Compiler Optimisations
  - [ ] Debugging with GDB
  - [ ] objdump
  - [ ] readelf
  - [ ] nm
  - [ ] strings
  - [ ] ldd

- [ ] **Memory Exploitation Fundamentals:** Learn:
  - [ ] Buffer Overflows (Stack & Heap)
  - [ ] Integer Overflows
  - [ ] Format String Vulnerabilities
  - [ ] Use-After-Free (UAF)
  - [ ] Double Free
  - [ ] Heap Corruption
  - [ ] Null Pointer Dereference
  - [ ] Race Conditions
  - [ ] TOCTOU (Time-of-Check to Time-of-Use)
  - [ ] Off-by-One Errors
  - [ ] Stack Canaries
  - [ ] DEP / NX
  - [ ] ASLR
  - [ ] PIE
  - [ ] RELRO
  - [ ] Safe Memory Management Practices

- [ ] **Essential Tools:** Gain practical experience with:
  - [ ] GDB
  - [ ] GEF or pwndbg
  - [ ] Valgrind
  - [ ] AddressSanitizer (ASan)
  - [ ] objdump
  - [ ] readelf
  - [ ] strings
  - [ ] nm
  - [ ] ltrace
  - [ ] strace
  - [ ] checksec

- [ ] **Automation & Mini Projects:** Build:
  - [ ] TCP client/server
  - [ ] Simple shell
  - [ ] Mini HTTP server
  - [ ] File parser
  - [ ] Process monitor
  - [ ] Memory allocator (mini malloc)
  - [ ] ELF parser
  - [ ] Simple debugger
  - [ ] Binary file analyser

- [ ] **Learning Outcome:** Develop a deep understanding of C programming, Linux internals, process execution, memory management, binary structure, and how memory corruption vulnerabilities occur—forming the foundation for reverse engineering, exploit development, binary exploitation, and operating system security.

---

#### **C++ (Reverse Engineering & Software Analysis)**

- [ ] **Core Language:** Master classes, objects, inheritance, polymorphism, encapsulation, abstraction, constructors, destructors, namespaces, templates, the Standard Template Library (STL), operator overloading, exception handling, smart pointers, RAII, move semantics, object lifecycles, and modern C++ (C++11/14/17) features.

- [ ] **Object-Oriented Internals:** Understand:
  - [ ] Classes & Objects
  - [ ] Constructors
  - [ ] Destructors
  - [ ] Inheritance
  - [ ] Multiple Inheritance
  - [ ] Virtual Functions
  - [ ] Pure Virtual Functions
  - [ ] VTables
  - [ ] VPointers (vptr)
  - [ ] Runtime Type Information (RTTI)
  - [ ] Dynamic Casting
  - [ ] Object Memory Layout
  - [ ] Name Mangling
  - [ ] Template Expansion
  - [ ] Inline Functions

- [ ] **Compiler & Binary Fundamentals:** Learn:
  - [ ] C++ Compilation Process
  - [ ] Name Demangling
  - [ ] Symbol Tables
  - [ ] Static vs Dynamic Linking
  - [ ] ELF (Linux)
  - [ ] PE (Windows)
  - [ ] Shared Libraries (.so / DLL)
  - [ ] Import & Export Tables
  - [ ] Exception Handling Internals
  - [ ] Debug Symbols

- [ ] **Reverse Engineering:** Learn how C++ applications appear inside:
  - [ ] Ghidra
  - [ ] IDA Pro
  - [ ] Binary Ninja
  - [ ] Radare2 / Cutter
  - [ ] x64dbg
  - [ ] WinDbg
  - [ ] GDB

- [ ] **Reverse Engineering Concepts:** Study:
  - [ ] Function Identification
  - [ ] Class Reconstruction
  - [ ] VTable Recovery
  - [ ] RTTI Analysis
  - [ ] Object Reconstruction
  - [ ] Constructor & Destructor Identification
  - [ ] Virtual Function Resolution
  - [ ] Control Flow Graphs (CFG)
  - [ ] Cross References (XREFs)
  - [ ] Strings Analysis
  - [ ] Import/Export Analysis
  - [ ] Symbol Recovery
  - [ ] Manual Decompilation

- [ ] **Malware Analysis Context:** Understand how C++ is commonly used in:
  - [ ] Malware loaders
  - [ ] Packers
  - [ ] Ransomware
  - [ ] Trojans
  - [ ] Remote Access Trojans (RATs)
  - [ ] Command & Control (C2) clients
  - [ ] Windows API-heavy applications

- [ ] **Essential Libraries & APIs:** Gain familiarity with:
  - [ ] Standard Template Library (STL)
  - [ ] Windows API (Win32)
  - [ ] C Runtime Library (CRT)
  - [ ] Boost _(awareness)_
  - [ ] COM Basics _(awareness)_

- [ ] **Practical Projects:**
  - [ ] PE parser
  - [ ] ELF parser
  - [ ] Mini disassembler
  - [ ] Binary string extractor
  - [ ] Symbol demangler
  - [ ] Windows API monitoring tool
  - [ ] Simple DLL loader
  - [ ] Basic binary patcher

- [ ] **Learning Outcome:** Read, analyse, reconstruct, and understand modern C++ binaries by recognising compiler-generated patterns, object-oriented structures, Windows/Linux APIs, and binary internals during malware analysis, reverse engineering, exploit research, and advanced penetration testing.

---

#### **Bash (Linux Automation & Operations)**

- [ ] **Shell Fundamentals:** Master variables, data types, quoting, command substitution, arithmetic operations, loops, conditionals, functions, arrays, pipes, redirection, file descriptors, environment variables, aliases, shell expansion, permissions, process management, exit codes, and shell scripting best practices.

- [ ] **Linux Command-Line Mastery:** Gain proficiency with:

  **📂 File & Text Processing**
  - [ ] grep
  - [ ] awk
  - [ ] sed
  - [ ] cut
  - [ ] tr
  - [ ] sort
  - [ ] uniq
  - [ ] xargs
  - [ ] tee
  - [ ] split
  - [ ] paste
  - [ ] wc
  - [ ] strings
  - [ ] file

  **📁 Filesystem Operations**
  - [ ] find
  - [ ] locate
  - [ ] ls
  - [ ] stat
  - [ ] chmod
  - [ ] chown
  - [ ] ln
  - [ ] tar
  - [ ] gzip
  - [ ] zip
  - [ ] rsync

  **🌐 Networking**
  - [ ] curl
  - [ ] wget
  - [ ] ssh
  - [ ] scp
  - [ ] nc (netcat)
  - [ ] socat
  - [ ] dig
  - [ ] host
  - [ ] nslookup
  - [ ] ping
  - [ ] traceroute
  - [ ] ss
  - [ ] netstat _(legacy awareness)_
  - [ ] tcpdump

  **⚙️ System Administration**
  - [ ] ps
  - [ ] top / htop
  - [ ] kill
  - [ ] systemctl
  - [ ] service
  - [ ] journalctl
  - [ ] crontab
  - [ ] env
  - [ ] export
  - [ ] history
  - [ ] sudo

  **📊 Data Processing**
  - [ ] jq (JSON)
  - [ ] yq (YAML)
  - [ ] base64
  - [ ] md5sum
  - [ ] sha256sum

- [ ] **Linux System Programming Basics:** Understand:
  - [ ] Processes
  - [ ] Background & foreground jobs
  - [ ] Signals
  - [ ] Environment variables
  - [ ] Permissions & ownership
  - [ ] File descriptors
  - [ ] Pipes & named pipes
  - [ ] Cron jobs
  - [ ] System logging
  - [ ] Package management
  - [ ] Bash startup files (.bashrc, .profile)

- [ ] **Automation Projects:** Build scripts for:
  - [ ] Host enumeration
  - [ ] Network reconnaissance
  - [ ] Subdomain enumeration
  - [ ] Log analysis
  - [ ] File processing
  - [ ] Backup automation
  - [ ] System monitoring
  - [ ] Cron job automation
  - [ ] SSH automation
  - [ ] Firewall management
  - [ ] Service monitoring
  - [ ] Package update automation
  - [ ] IOC extraction
  - [ ] Report generation

- [ ] **Security & Pentesting Automation:** Learn to automate:
  - [ ] Nmap scanning
  - [ ] HTTP requests using curl
  - [ ] DNS enumeration
  - [ ] SSL/TLS certificate inspection
  - [ ] Whois lookups
  - [ ] Log parsing
  - [ ] Directory brute-forcing workflows
  - [ ] Batch vulnerability scanning
  - [ ] Parsing reconnaissance results
  - [ ] Linux privilege enumeration

- [ ] **Debugging & Best Practices:** Learn:
  - [ ] ShellCheck
  - [ ] Bash debugging (`set -x`, `set -e`, `set -u`)
  - [ ] Error handling
  - [ ] Logging
  - [ ] Input validation
  - [ ] Portable shell scripting
  - [ ] Modular script design
  - [ ] Git for script version control

- [ ] **Learning Outcome:** Automate Linux administration, reconnaissance, enumeration, log processing, system operations, and penetration testing workflows efficiently using professional, reusable, and maintainable Bash scripts.

---

#### **PowerShell (Windows Automation & Enterprise Administration)**

- [ ] **Language Fundamentals:** Master variables, data types, objects, pipelines, cmdlets, aliases, functions, modules, providers, scripting, execution policies, remoting, error handling, classes, background jobs, and PowerShell best practices.

- [ ] **PowerShell Core Concepts:** Understand:
  - [ ] Objects vs Text
  - [ ] Pipeline Processing
  - [ ] Get-Member
  - [ ] Select-Object
  - [ ] Where-Object
  - [ ] ForEach-Object
  - [ ] Sort-Object
  - [ ] Group-Object
  - [ ] Measure-Object
  - [ ] Out-File
  - [ ] Export-Csv
  - [ ] ConvertTo-Json / ConvertFrom-Json
  - [ ] XML Processing

- [ ] **Windows Administration:** Automate:
  - [ ] Active Directory enumeration
  - [ ] User & Group management
  - [ ] Registry operations
  - [ ] Service management
  - [ ] Process management
  - [ ] Event log collection
  - [ ] WMI queries
  - [ ] CIM
  - [ ] Scheduled Tasks
  - [ ] Windows Services
  - [ ] File & Directory management
  - [ ] SMB share management
  - [ ] Firewall configuration
  - [ ] Windows Defender management
  - [ ] Certificate management

- [ ] **Enterprise Automation:** Learn:
  - [ ] WinRM
  - [ ] PowerShell Remoting
  - [ ] Invoke-Command
  - [ ] Enter-PSSession
  - [ ] New-PSSession
  - [ ] CIM Sessions
  - [ ] Remote Event Log collection
  - [ ] Group Policy automation _(awareness)_
  - [ ] Desired State Configuration (DSC) _(awareness)_

- [ ] **Active Directory Automation:** Learn:
  - [ ] ActiveDirectory PowerShell Module
  - [ ] User enumeration
  - [ ] Group enumeration
  - [ ] Computer enumeration
  - [ ] OU management
  - [ ] GPO enumeration
  - [ ] ACL inspection
  - [ ] Trust enumeration
  - [ ] Domain information gathering

- [ ] **Essential Modules & APIs:** Gain practical experience with:
  - [ ] Microsoft.PowerShell.Management
  - [ ] Microsoft.PowerShell.Utility
  - [ ] ActiveDirectory Module
  - [ ] NetTCPIP
  - [ ] ScheduledTasks
  - [ ] CimCmdlets
  - [ ] PSReadLine
  - [ ] PowerShellGet

- [ ] **Automation Projects:** Build:
  - [ ] Active Directory inventory
  - [ ] User audit reports
  - [ ] Event log collector
  - [ ] Service monitoring scripts
  - [ ] Registry auditing tools
  - [ ] Windows asset inventory
  - [ ] Remote administration toolkit
  - [ ] File integrity checker
  - [ ] Windows health monitoring scripts
  - [ ] Enterprise reporting dashboards

- [ ] **Security & Defensive Automation:** Learn to automate:
  - [ ] Windows system enumeration
  - [ ] Active Directory auditing
  - [ ] Windows Defender status checks
  - [ ] Event log analysis
  - [ ] IOC hunting
  - [ ] Security baseline verification
  - [ ] Windows update auditing
  - [ ] Local administrator auditing
  - [ ] Scheduled Task auditing
  - [ ] Service permission auditing

- [ ] **Debugging & Best Practices:** Learn:
  - [ ] PowerShell ISE / VS Code
  - [ ] PowerShell Debugger
  - [ ] Error handling
  - [ ] Logging
  - [ ] Script signing
  - [ ] Secure credential handling
  - [ ] SecretManagement module _(awareness)_
  - [ ] PSScriptAnalyzer
  - [ ] Git for version control

- [ ] **Learning Outcome:** Confidently automate Windows administration, Active Directory management, enterprise enumeration, system auditing, incident response, and security operations using professional, reusable, and maintainable PowerShell scripts.

---

#### **Cross-Platform Development**

- [ ] Choose the appropriate language for each task:
  - [ ] Python → Automation, APIs, cross-platform tooling
  - [ ] Bash → Linux administration and automation
  - [ ] PowerShell → Windows administration and Active Directory
  - [ ] C → Low-level programming and exploit foundations
  - [ ] C++ → Reverse engineering and malware analysis
  - [ ] JavaScript → Web application and browser security

- [ ] Learn to combine multiple languages into complete security workflows rather than treating each language in isolation.

---

## **Stage Completion Criteria**

Before moving to the next stage, you should be able to:

- [ ] Write custom automation tools from scratch.
- [ ] Read and modify existing security scripts.
- [ ] Debug programs in multiple languages.
- [ ] Interact directly with networks and operating systems using code.
- [ ] Build complete command-line utilities.
- [ ] Parse logs, APIs, packets, and structured data automatically.
- [ ] Select the most appropriate programming language for a given security task.
- [ ] Understand how programming knowledge supports penetration testing, malware analysis, reverse engineering, digital forensics, and detection engineering.

> **📌 Cross-Reference:** Offensive programming is covered in dedicated Parts:
>
> - **Part 42: Offensive Development & Tooling** (Phase 7) — Exploit prototyping with pwntools, custom C2 implant logic, buffer overflow exploits, shellcode writing, Win32 API process injection, DLL loading, token manipulation, .NET offensive tooling (P/Invoke, D/Invoke, SharpHound, Rubeus), AMSI/ETW bypass, in-memory execution, offensive PowerShell (download cradles, constrained language mode escape).
> - **Part 29: Modern Exploitation** (Phase 7) — Advanced memory exploitation, kernel exploits, browser exploitation.
> - **Part 8: Malware & Weaponization** (Phase 2) — Document weaponization (VBA macros, DDE template abuse, OneNote/PDF weaponization), email client abuse, OAuth consent phishing, cloud persistence, data exfiltration, and covert channels.

---

<a id="stage-7b-c-cpp-programming"></a>

### **Stage 7B: C & C++ Programming** ← *Deferred to Phase 7*

> [!IMPORTANT]
> **Do not start Stage 7B now.** This stage is placed here as a structural marker only. C and C++ are the languages of OS internals, exploit primitives, shellcode, and reverse engineering targets — but they require meaningful context to learn effectively:
> - You need to have seen a stack frame in a debugger before C memory layout makes sense.
> - You need to have read disassembly before C++ vtables mean anything.
> - You need to have written at least one exploit before custom shellcode has purpose.
>
> **Return here when you reach Phase 7, before starting Part 28 (Reverse Engineering) and Part 42 (Offensive Development).** At that point, C and C++ become immediately applicable rather than abstract theory.
>
> **Phase 7 location:** Phase-7.md — Stage 7B section before Part 42.

---

<a id="toc-part-1b-linux-administration"></a>
<a id="part-1b-linux-administration"></a>

## Part 1B: Linux Administration

_Phase 1 — Foundation | Prerequisite: Part 1 Stage 2 (OS Internals) | This module teaches the Linux administration skills required by the Foundation Proof Gate and used throughout every subsequent Phase._

<a id="stage-1-user-access-management-linux"></a>

### Stage 1: User & Access Management (Linux)

- [ ] **User Accounts:** Create, modify, and delete users with **useradd/usermod/userdel**. Understand **/etc/passwd**, **/etc/shadow**, and **/etc/group** file structures.

- [ ] **Group Management:** Create groups, assign users to primary and supplementary groups, understand **newgrp** and group-based access control.

- [ ] **Password Policy:** Configure password aging with **chage**, set complexity requirements via **PAM (pam_pwquality)**, and understand **/etc/login.defs**.

- [ ] **Sudo Configuration:** Understand **/etc/sudoers** syntax, use **visudo**, configure per-user and per-group sudo rules, and understand **NOPASSWD** risks.

- [ ] **File Permissions:** Master **rwx**, **chmod** (symbolic and octal), **chown**, **chgrp**. Understand **SUID, SGID, sticky bit** and their security implications.

- [ ] **ACLs:** Configure **POSIX ACLs** with **getfacl/setfacl** for fine-grained access control beyond standard permissions.

<a id="stage-2-service-process-management-linux"></a>

### Stage 2: Service & Process Management (Linux)

- [ ] **systemd:** Manage services with **systemctl** (start, stop, enable, disable, status, mask). Understand **unit files**, **targets**, and **dependencies**.

- [ ] **Process Management:** Use **ps, top, htop, kill, killall, nice, renice**. Understand **PID, PPID, process states, zombie processes**, and **signal handling**.

- [ ] **Cron & Timers:** Schedule tasks with **crontab** and **systemd timers**. Understand cron syntax, **/etc/cron.d/**, and security implications of cron jobs.

- [ ] **Package Management:** Install, update, and remove software with **apt (Debian/Ubuntu)** and **dnf/yum (RHEL/Fedora)**. Understand **repositories, GPG signing, and dependency resolution**.

- [ ] **Boot Process:** Understand **GRUB2 → systemd → target** boot sequence, **runlevels/targets**, and **single-user mode** for recovery.

<a id="stage-3-networking-linux"></a>

### Stage 3: Networking (Linux)

- [ ] **Network Configuration:** Configure interfaces with **ip addr, ip link, ip route**. Understand **DHCP vs. static**, **/etc/netplan/**, **/etc/network/interfaces**, and **NetworkManager (nmcli)**.

- [ ] **DNS Resolution:** Understand **/etc/resolv.conf**, **/etc/hosts**, **systemd-resolved**, and **dig/nslookup/host** for troubleshooting.

- [ ] **Socket Inspection:** Use **ss** and **netstat** to identify listening services, active connections, and process-socket bindings.

- [ ] **Firewall (iptables/nftables/ufw):** Configure basic packet filtering rules. Understand **chains (INPUT, OUTPUT, FORWARD)**, **default policies**, **stateful tracking**, and **logging**.

- [ ] **SSH Hardening:** Configure **/etc/ssh/sshd_config** — disable root login, enforce key-based auth, change default port, configure **fail2ban**, and understand **SSH tunneling (local, remote, dynamic)**.

<a id="stage-4-log-analysis-monitoring-linux"></a>

### Stage 4: Log Analysis & Monitoring (Linux)

- [ ] **journalctl:** Query systemd journal logs — filter by **unit, priority, time range, boot**. Understand **persistent vs. volatile** journaling.

- [ ] **Syslog:** Understand **/var/log/syslog**, **/var/log/auth.log**, **/var/log/kern.log**, **/var/log/secure**. Configure **rsyslog** for remote forwarding.

- [ ] **Log Rotation:** Configure **logrotate** to prevent disk exhaustion. Understand **rotation frequency, compression, retention policies**.

- [ ] **dmesg:** Read kernel ring buffer for **hardware errors, driver issues, and boot diagnostics**.

- [ ] **Monitoring Tools:** Use **uptime, free, df, du, iostat, vmstat** for system health monitoring. Understand when to investigate further.

<a id="stage-5-storage-filesystem-linux"></a>

### Stage 5: Storage & Filesystem (Linux)

- [ ] **Disk Management:** Use **fdisk, parted, lsblk, blkid** to manage partitions. Understand **MBR vs. GPT**.

- [ ] **Filesystem Operations:** Create filesystems with **mkfs**, mount with **mount/fstab**, understand **ext4, XFS, Btrfs** differences.

- [ ] **LVM:** Create and manage **Physical Volumes, Volume Groups, Logical Volumes**. Extend and resize volumes without downtime.

- [ ] **Disk Encryption:** Encrypt partitions with **LUKS (cryptsetup)**. Understand **dm-crypt**, key slots, and unlock-at-boot configuration.

<a id="stage-6-security-hardening-linux"></a>

### Stage 6: Security Hardening (Linux)

- [ ] **SELinux:** Understand **enforcing, permissive, disabled** modes. Use **getenforce, setenforce, sestatus**. Read **audit.log** denials and create custom policies with **audit2allow**.

- [ ] **AppArmor:** Understand **profiles, complain vs. enforce mode**. Use **aa-status, aa-genprof** for profile creation.

- [ ] **System Auditing:** Configure **auditd** rules to monitor file access, user commands, and privilege escalation. Use **ausearch** and **aureport**.

- [ ] **Kernel Hardening:** Understand **sysctl** parameters (**net.ipv4.ip_forward**, **kernel.randomize_va_space**, **fs.protected_hardlinks**) and how to persist them.

<a id="lab-progression-linux"></a>

### Lab Progression (Linux)

| Level | Task                                                                   | Deliverable                                |
| ----- | ---------------------------------------------------------------------- | ------------------------------------------ |
| 1     | Set up a fresh Ubuntu/Debian VM from ISO                               | Working VM with SSH access                 |
| 2     | Create 5 users with different group memberships and sudo rules         | Screenshot of /etc/sudoers and group files |
| 3     | Configure SSH key-only auth + fail2ban                                 | SSH hardening checklist document           |
| 4     | Set up iptables/nftables firewall rules allowing only SSH, HTTP, HTTPS | Firewall ruleset export                    |
| 5     | Analyze auth.log to identify failed login patterns                     | 1-page log analysis report                 |
| 6     | Set up LVM, create/extend logical volumes                              | Screenshot of lvm commands and df output   |
| 7     | Enable SELinux/AppArmor, troubleshoot a denied operation               | Audit log analysis + policy fix document   |

> [!IMPORTANT]
> **Move-On Gate:** You can create users, manage services, configure networking, read logs, and harden a Linux system from scratch without referring to documentation for basic commands.

---

<a id="toc-part-1c-windows-administration"></a>
<a id="part-1c-windows-administration"></a>

## Part 1C: Windows Administration

_Phase 1 — Foundation | Prerequisite: Part 1 Stage 2 (OS Internals) | This module teaches Windows administration skills required by the Foundation Proof Gate and used throughout Active Directory (Part 23), cloud (Part 24), and defensive (Phase 3) modules._

<a id="stage-1-user-access-management-windows"></a>

### Stage 1: User & Access Management (Windows)

- [ ] **Local Users & Groups:** Create and manage local accounts with **lusrmgr.msc** and **net user/net localgroup** commands. Understand **built-in accounts (Administrator, Guest, SYSTEM)**.

- [ ] **NTFS Permissions:** Configure **read, write, modify, full control** on files/folders. Understand **inheritance, explicit vs. inherited permissions**, and **effective permissions**.

- [ ] **Share Permissions:** Distinguish between **NTFS and share permissions**. Configure **SMB shares** and understand **Everyone vs. Authenticated Users** security implications.

- [ ] **User Account Control (UAC):** Understand **UAC prompts, integrity levels (low, medium, high, system)**, and how UAC affects administrative operations.

- [ ] **Local Security Policy:** Configure **password policy, account lockout policy, user rights assignments** via **secpol.msc** and **gpedit.msc**.

<a id="stage-2-system-management-windows"></a>

### Stage 2: System Management (Windows)

- [ ] **Windows Services:** Manage services with **services.msc** and **sc.exe/Get-Service**. Understand **service accounts (LocalSystem, LocalService, NetworkService)**, startup types, and recovery options.

- [ ] **Registry:** Navigate **HKLM, HKCU, HKCR, HKU** hives. Understand **Run/RunOnce keys**, **service configurations**, and how malware uses the registry for persistence.

- [ ] **Task Scheduler:** Create and manage scheduled tasks. Understand **triggers, actions, conditions**, and security implications of tasks running as SYSTEM.

- [ ] **Windows Firewall:** Configure **inbound/outbound rules** with **Windows Defender Firewall with Advanced Security (wf.msc)** and **netsh**. Understand **profiles (Domain, Private, Public)**.

- [ ] **Windows Update:** Understand **WSUS, Windows Update for Business**, and **patch management** concepts. Know how to check update history and roll back problematic updates.

<a id="stage-3-event-viewer-auditing-windows"></a>

### Stage 3: Event Viewer & Auditing (Windows)

- [ ] **Event Log Structure:** Navigate **Application, System, Security, Setup** logs in **Event Viewer (eventvwr.msc)**. Understand **Event IDs, sources, levels (Information, Warning, Error, Critical)**.

- [ ] **Key Security Event IDs:** Know the critical Event IDs:
  - **4624** — Successful logon (with logon types: 2=Interactive, 3=Network, 10=RemoteInteractive)
  - **4625** — Failed logon (track brute force attempts)
  - **4634/4647** — Logoff
  - **4672** — Special privileges assigned (admin logon)
  - **4688** — Process creation (critical for detecting malware execution)
  - **4720** — User account created
  - **4732** — Member added to security-enabled local group
  - **1102** — Audit log cleared (indicator of cover-up)
  - **7045** — Service installed (persistence indicator)

- [ ] **Audit Policy:** Configure **Advanced Audit Policy** via **Group Policy** or **auditpol.exe**. Enable auditing for **logon events, object access, privilege use, process tracking**.

- [ ] **Sysmon:** Install and configure **Sysmon** with a baseline configuration (e.g., SwiftOnSecurity/Olaf Hartong config). Understand **Event IDs 1 (Process Create), 3 (Network Connect), 7 (Image Loaded), 11 (File Created), 13 (Registry Value Set)**.

- [ ] **PowerShell Logging:** Enable **Script Block Logging (Event ID 4104)**, **Module Logging**, and **Transcription Logging**. Understand why these are critical for detecting fileless attacks.

<a id="stage-4-powershell-administration-windows"></a>

### Stage 4: PowerShell Administration (Windows)

- [ ] **Core Cmdlets:** Master **Get-Process, Get-Service, Get-EventLog, Get-WinEvent, Get-ChildItem, Get-Content, Set-Item, New-Item, Remove-Item, Test-NetConnection**.

- [ ] **Pipeline & Filtering:** Use **Where-Object, Select-Object, Sort-Object, Group-Object, Measure-Object, ForEach-Object, Export-Csv, ConvertTo-Json**.

- [ ] **Remote Management:** Configure and use **PowerShell Remoting (Enable-PSRemoting, Invoke-Command, Enter-PSSession, New-PSSession)**. Understand **WinRM** configuration and **double-hop** authentication issues.

- [ ] **WMI/CIM:** Query system information with **Get-CimInstance** (Win32_Process, Win32_Service, Win32_OperatingSystem). Understand WMI as both an administration and attack tool.

- [ ] **Active Directory Basics:** Use **RSAT tools** and **Active Directory PowerShell module** (Get-ADUser, Get-ADGroup, Get-ADComputer). Understand **OU structure, GPO basics, DNS integration with AD**.

<a id="stage-5-active-directory-concepts-prerequisite-for-part-23"></a>

### Stage 5: Active Directory Concepts _(Prerequisite for Part 23)_

- [ ] **AD Architecture:** Understand **domains, forests, trusts, OUs, sites**, and **replication**. Know the difference between a **domain controller** and a **member server**.

- [ ] **Group Policy Basics:** Create and link **GPOs**. Understand **computer vs. user configuration**, **gpupdate /force**, **rsop.msc**, and **GPO inheritance/blocking**.

- [ ] **DNS in AD:** Understand why **AD-integrated DNS** is critical. Know **SRV records (\_ldap.\_tcp)**, **forward/reverse lookup zones**, and **dynamic DNS registration**.

- [ ] **DHCP in AD:** Understand **DHCP server authorization**, **scopes, reservations, options**, and how DHCP integrates with DNS.

> [!NOTE]
> **Stage 5 → Stage 6 Transition:** Stage 5 gives you the conceptual map of Active Directory — the structure, objects, and administrative mechanisms. Stage 6 gives you the protocol mechanics — _why_ these structures exist and _how_ authentication flows through them. The overlap you may notice on account types and trust architecture is intentional: Stage 5 names them, Stage 6 explains how they are exploited. Both stages are required before Phase 6 Part 23 (Active Directory attacks). Do not skip Stage 6 even if Stage 5 felt complete.

<a id="stage-6-windows-identity-kerberos-foundations"></a>

### Stage 6: Windows Identity & Kerberos Protocol Foundations _(Critical Prerequisite for Part 23)_

> [!NOTE]
> **Prerequisite: Stage 5 Required.** This stage explains the authentication protocols and cryptographic mechanisms behind the Active Directory concepts introduced in Stage 5. Where Stage 5 told you that SPNs, service accounts, and delegation exist — Stage 6 explains _how they work at the protocol level_ and _why that makes them exploitable_. Read Stage 5 first, then return here.

> [!IMPORTANT]
> **Why This Exists Here:** Part 23 (Active Directory attacks in Phase 6) immediately begins with Kerberoasting, AS-REP Roasting, ADCS abuse, and ACL exploitation. These techniques are impossible to understand deeply without knowing the underlying Kerberos protocol, LDAP structure, and trust architecture. This stage provides that foundation **before** you reach Phase 6 — not during it. Do not skip this stage even if it feels abstract now; it will crystallize completely when you reach the AD attacks.

- [ ] **Kerberos Authentication Flow:** Trace the full authentication lifecycle step-by-step:
  - **AS-REQ:** Client sends authentication request to the KDC (Key Distribution Center) on the DC, encrypted with user's password hash
  - **AS-REP:** KDC returns a **TGT (Ticket-Granting Ticket)** encrypted with the `krbtgt` account hash — this is what AS-REP Roasting steals
  - **TGS-REQ:** Client presents TGT to request a service ticket for a specific service (identified by its **SPN**)
  - **TGS-REP:** KDC returns a **TGS (Ticket-Granting Service)** ticket encrypted with the **service account's hash** — this is what Kerberoasting steals
  - **AP-REQ:** Client presents TGS to the target service for authentication
  - Understand why the `krbtgt` hash is the most valuable domain credential (Golden Ticket uses it)

- [ ] **Service Principal Names (SPNs):** Understand how SPNs (e.g., `MSSQLSvc/sqlserver.corp.local:1433`) link a service to a user/computer account. Know that **any account with an SPN is Kerberoastable** — this is why monitoring SPNs is a security control.

- [ ] **LDAP Directory Structure:** Understand the **Lightweight Directory Access Protocol** as the query language for Active Directory:
  - **Distinguished Names (DNs):** `CN=John Smith,OU=Finance,DC=corp,DC=local` — how AD objects are addressed
  - **Attributes:** `sAMAccountName`, `userPrincipalName`, `memberOf`, `servicePrincipalName`, `pwdLastSet`, `userAccountControl`
  - **LDAP Filters:** `(&(objectClass=user)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))` — how BloodHound and tools like `ldapsearch` query the directory
  - **Anonymous LDAP Bind:** Understand that misconfigured DCs allow unauthenticated LDAP enumeration — the root cause of many BloodHound discoveries

- [ ] **Forest, Domain, and Trust Architecture:**
  - **Domain:** Single namespace boundary (corp.local); has one or more Domain Controllers
  - **Forest:** Collection of domains sharing a schema, config, and Global Catalog; the security boundary (not the domain)
  - **Trust Types:** Parent-child (automatic, transitive), tree-root (automatic, transitive), external (manual, non-transitive), forest trust (manual, transitive with caveats), shortcut trust (manual optimization)
  - **Trust Direction:** One-way vs bidirectional; understand that trust direction and access direction are opposite — if Domain A trusts Domain B, users **in B** can access resources **in A**
  - **SID History:** How migrated accounts carry old SIDs and why this is an attack vector (SID History injection)

- [ ] **Group Policy Processing Order (LSDOU):**
  - **LSDOU:** Local → Site → Domain → Organizational Unit — later policies override earlier ones by default
  - **Block Inheritance / Enforce:** How to break and restore the processing chain
  - **Group Policy Filtering:** Security filtering (who the GPO applies to) vs WMI filtering (what systems it applies to)
  - **gpresult /R and /H:** How to audit effective policy on a target system — critical for understanding privilege gaps

- [ ] **Account Types and Privilege Tiers:**
  - **Standard User Accounts:** Interactive logon, default domain users
  - **Service Accounts:** Run services; often have excessive privileges; Kerberoastable if SPN is set
  - **Managed Service Accounts (MSA/gMSA):** Auto-rotating passwords; not Kerberoastable (key defensive control)
  - **Computer Accounts:** Machine identity in the domain; end with `$` (e.g., `WORKSTATION01$`); have passwords that auto-rotate every 30 days
  - **Built-in Groups:** Domain Admins, Enterprise Admins, Schema Admins, Account Operators, Backup Operators — understand which grant what level of access
  - **Protected Users Group:** Removes NTLM, DES, RC4 Kerberos, and credential caching — the strongest built-in hardening group

- [ ] **Delegation Types:**
  - **Unconstrained Delegation:** Any service on a machine set with unconstrained delegation receives the user's TGT — extremely dangerous; classic target for the "Printer Bug" attack
  - **Constrained Delegation:** Service can only impersonate to specific target SPNs; still abusable with S4U2Self/S4U2Proxy techniques
  - **Resource-Based Constrained Delegation (RBCD):** Defined on the resource, not the caller; abusable when you have `WriteProperty` on a computer object

- [ ] **Access Control Lists (ACLs) in Active Directory:**
  - **DACLs:** Discretionary Access Control Lists — who can do what to an AD object
  - **Dangerous ACE types:** `GenericAll`, `GenericWrite`, `WriteOwner`, `WriteDACL`, `AllExtendedRights`, `ForceChangePassword`, `Self-Membership`
  - Understand that these ACEs — not just group membership — define the attack paths BloodHound discovers
  - Practice reading an AD object's Security tab and correlating it to BloodHound edges

- [ ] **Active Directory Certificate Services (ADCS) — Awareness:**
  - Understand that ADCS is the PKI infrastructure for issuing certificates to users, machines, and services
  - Know that certificates can be used for authentication (PKINIT) and that misconfigured certificate templates are the root cause of ESC1–ESC8 vulnerabilities
  - You do not need to exploit these now — you need to know they exist so the Part 23 coverage makes sense

> [!TIP]
> **Lab Exercise:** Build a Windows Server 2022 Domain Controller lab (if not already done from Stage 3–5 labs). Run `ldapsearch -x -H ldap://DC_IP -b "DC=corp,DC=local"` from a Linux host. Run `klist` on a domain-joined Windows machine after logon to see your TGT. Run `setspn -T corp.local -Q */*` to list all SPNs. These three commands will make everything above concrete.

<a id="lab-progression-windows"></a>

### Lab Progression (Windows)

| Level | Task                                                                                     | Deliverable                                           |
| ----- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| 1     | Install Windows Server 2022 in VM                                                        | Working VM with RDP access                            |
| 2     | Create local users, configure NTFS permissions on shared folder                          | Permission matrix document                            |
| 3     | Promote to Domain Controller, create OU structure with 10+ users                         | AD topology screenshot                                |
| 4     | Configure Group Policy (password policy, software restriction)                           | GPO summary document                                  |
| 5     | Enable Advanced Audit Policy + Sysmon, generate logon events                             | Event log analysis (identify 4624, 4625, 4688 events) |
| 6     | Configure Windows Firewall rules via PowerShell                                          | Exported firewall ruleset                             |
| 7     | Write PowerShell script to audit AD: list all admins, find stale accounts, export report | Working .ps1 script + CSV output                      |

> [!IMPORTANT]
> **Move-On Gate:** You can set up a Windows domain from scratch, create users/groups/GPOs, read Event Viewer logs to identify suspicious activity, and write basic PowerShell automation scripts without referring to documentation for core tasks.

---

<a id="macos-security-awareness-supplemental"></a>

### **macOS Security Awareness** _(Supplemental)_

> macOS endpoints are present in most enterprises, especially in development, design, and executive teams. This sidebar provides enough context to avoid a knowledge gap when encountering macOS in the field. Full macOS exploitation is an advanced specialization.

- [ ] **macOS Security Architecture:** Understand **Gatekeeper** (app signing verification), **System Integrity Protection (SIP)** (restricts root from modifying system files), and **Transparency, Consent, and Control (TCC)** (permission prompts for camera, mic, files).

- [ ] **macOS Filesystem & Users:** Know **APFS (encrypted by default), /System, /Library, /Users, /Applications** directory structure. Understand **dscl** for user management and **sudo/admin** vs standard user roles.

- [ ] **macOS Logging:** Understand **Unified Logging (log show/log stream)**, **Console.app**, and how macOS logs differ from Windows Event Viewer and Linux syslog. Know how to query logs for suspicious activity.

- [ ] **macOS Endpoint Security:** Know that **XProtect** (built-in malware detection), **MRT (Malware Removal Tool)**, **Notarization** (Apple's pre-distribution scanning), and **MDM (Mobile Device Management)** profiles are key enterprise controls.

- [ ] **macOS for Pentesters:** Understand that **Objective-See tools (KnockKnock, BlockBlock, LuLu, OverSight)** are the open-source equivalent of EDR for macOS, and that **osascript, Automator, LaunchAgents/LaunchDaemons** are macOS persistence mechanisms.

---

<a id="toc-part-2-networking-fundamentals"></a>
<a id="part-2-networking-fundamentals"></a>

## Part 2: Networking Fundamentals

<a id="layer-1-physical-the-hardware-surface"></a>

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

<a id="layer-2-data-link-the-local-target"></a>

### Layer 2: Data Link (The Local Target)

**MAC Addressing & Frame Structure:**

- [ ] **MAC Address Format:** Understand **OUI (Organizationally Unique Identifier)** and manufacturer identification.

- [ ] **Unicast vs. Multicast:** Master **FF:FF:FF:FF:FF:FF** (broadcast) and multicast MAC ranges.

- [ ] **Frame Structure:** Understand **Ethernet frames**, **VLAN tags (802.1Q)**, and **frame size (MTU)** constraints.

- [ ] **MAC Address Spoofing:** Learn tools like **macchanger** and implications for network security.

**ARP Protocol & Attacks:**

- [ ] **ARP Cache Mechanics:** Understand how **ARP tables** map IP addresses to MAC addresses and why ARP is inherently trust-based.

- [ ] **ARP Defense:** Understand **static ARP entries**, **ARP inspection (DAI)**, and detection mechanisms.

> **📌 Cross-Reference:** Hands-on ARP spoofing, poisoning, and MITM via ARP are taught in **Part 9: Sniffing & Spoofing, Phase 3** (the canonical location for all spoofing techniques).

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

**EtherChannel & Link Aggregation:** _(Optional — Network Engineering Depth)_

> ⚠️ _EtherChannel/LACP is a network engineering topic. Security practitioners should know link aggregation exists but detailed configuration of PAgP/LACP modes is not a security prerequisite._

- [ ] **LACP (802.3ad):** Configure **Link Aggregation Control Protocol** with **active/passive** modes for dynamic bundling.

- [ ] **PAgP (Port Aggregation Protocol):** Understand Cisco proprietary **PAgP** with **desirable/auto** modes.

- [ ] **EtherChannel Load Balancing:** Configure **src-mac, dst-mac, src-dst-ip, src-dst-port** load distribution algorithms.

- [ ] **Layer 2 vs Layer 3 EtherChannel:** Understand **L2 EtherChannel (switch ports)** vs **L3 EtherChannel (routed ports)**.

**Cisco Wireless Architecture:** _(Optional — Network Engineering Depth)_

> ⚠️ _Cisco-specific wireless architecture (WLC, CAPWAP, FlexConnect) is relevant for enterprise network roles. Security practitioners should understand that centralized wireless management exists, but Cisco-specific deployment models are not a security prerequisite. Wireless security attacks are covered in Part 21._

- [ ] **Autonomous AP Mode:** Understand **standalone APs** with individual management (legacy).

- [ ] **Lightweight AP (LAP) Mode:** Master **CAPWAP tunneling** to **Wireless LAN Controller (WLC)** for centralized management.

- [ ] **FlexConnect (H-REAP):** Understand **hybrid mode** allowing **local switching** at branch sites with **central authentication**.

- [ ] **WLC Deployment:** Know **centralized, distributed, cloud-based** WLC architectures.

- [ ] **WLAN Physical Infrastructure:** Understand **AP connections (access/trunk ports), WLC uplinks, LAG (Link Aggregation)** for redundancy.

---

<a id="layer-3-network-the-routing-logic"></a>

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

> [!NOTE]
> **BGP Security Sidebar:** BGP is the routing protocol of the internet — every ISP, cloud provider, and large enterprise peers via BGP. Unlike internal routing protocols, BGP has no built-in authentication or route validation. Key security concepts:
> - **BGP Hijacking:** An AS announces prefixes it does not own, attracting traffic that should route elsewhere. Historical examples: Pakistan Telecom (2008, YouTube blackhole), BGP hijacks targeting cryptocurrency exchanges (2018). State-level actors use BGP hijacking for traffic interception.
> - **Route Leaks:** An AS accidentally re-advertises routes it should not, causing traffic rerouting. Leaks differ from hijacks in intent but have the same network impact.
> - **RPKI (Resource Public Key Infrastructure):** The primary mitigation. Certificate authority binds IP prefixes to AS numbers via **Route Origin Authorizations (ROAs)**. BGP routers can validate ROAs and drop **RPKI-invalid** routes. Cloudflare, ARIN, and most large ISPs have adopted RPKI. Cloud providers deploying BGP peering are expected to understand RPKI. Check status: `https://stats.labs.apnic.net/rpki`.
> - **Monitoring:** BGPStream (`bgpstream.caida.org`) and Cloudflare Radar provide real-time BGP anomaly detection. Security engineers at cloud-adjacent companies use these to detect supply-chain routing attacks against their infrastructure.
> - **AS Path Manipulation:** Understanding AS path prepending, MED, and local preference is prerequisite for reasoning about which routes your organisation's traffic will take — relevant when assessing traffic interception risk for specific adversary threat models.

- [ ] **EIGRP (Enhanced Interior Gateway Routing Protocol):** Master Cisco proprietary **DUAL algorithm** and metrics.

- [ ] **RIP (Routing Information Protocol):** Understand legacy distance-vector protocol and 15-hop limit.

- [ ] **Routing Protocol Vulnerabilities:** Learn **route injection, spoofing, and redistribution attacks**.

**First Hop Redundancy Protocols (FHRP):** _(Optional — Network Engineering Depth)_

> ⚠️ _FHRP (HSRP/VRRP/GLBP) is relevant for network infrastructure roles. Security practitioners should know FHRP exists and that it can be attacked (e.g., HSRP/VRRP hijacking), but detailed protocol mechanics are not a security prerequisite._

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

<a id="layer-4-transport-the-reliability-layer"></a>

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

<a id="layers-5-7-application-session-the-payload"></a>

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

**QoS (Quality of Service) Fundamentals:** _(Optional — Network Engineering Depth)_

> ⚠️ _QoS is primarily relevant for network engineering roles. Security practitioners should understand that QoS exists and can be abused (e.g., traffic prioritization manipulation), but detailed configuration is not a prerequisite for security work._

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

- [ ] **Session Cookies:** Understand `HttpOnly`, `Secure`, `SameSite` flags and cookie theft. _(Security attribute security reasoning is in **Part 3C Stage 2: Cookies, Sessions & Tokens** — the canonical treatment with exploitation context.)_

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

<a id="lab-progression-professional-development-2026-red-team-focus"></a>

### Lab Progression & Professional Development (2026 Red Team Focus)

> [!TIP]
> **Goal:** Move from local simulation to cloud-native networks using a "hack to root" mindset.

**Level 1: Foundations (Simulation)** — Tools: **Cisco Packet Tracer, IP Calculator**

- [ ] Simple Connectivity: Two PCs + switch; verify **ping/basic reachability**.

- [ ] The "Phonebook": Stand up **local DNS**; resolve custom hostnames.

- [ ] Automatic Addressing: Configure **DHCP** to hand out IPs to multiple hosts.

- [ ] Subnetting Drills: Design **/24, /25, /26** subnets without online aids.

- [ ] VLAN Creation: Segment by department (e.g., HR, Sales) with **VLANs**.

**Level 2: Tactical (Emulation & Packets)** — Tools: **GNS3, Wireshark, Nmap**

- [ ] Packet Analysis: Capture **TCP 3-way handshake + HTTP** in Wireshark.

- [ ] Routing: Build **static routes**, then **OSPF** for auto path discovery.

- [ ] Filtering: Apply **ACLs** to permit/deny specific traffic.

- [ ] NAT: Enable **source NAT** to exit a lab via one public IP.

- [ ] Inter-VLAN Routing: Use **router-on-a-stick** for isolated VLAN comms.

**Level 3: Linux Muscle Memory**

- [ ] Discovery: Use **ip a, ss -tulpn, arp -a** to map interfaces/listeners/peers.

- [ ] Connectivity & Routing: Troubleshoot with **traceroute, nslookup, dig**.

- [ ] Remote Management: Practice **ssh user@host** and **scp** file moves.

- [ ] Firewall Basics: Block ports with **iptables/ufw**.

**Level 4: Red Team Edge (Kali/Battle Tests)** — Tools: **Kali, Bettercap, Metasploit**

- [ ] Recon: Run **Nmap stealth scans (SYN) + version detection** on lab targets.

- [ ] MITM: Perform **ARP spoof** with **Bettercap/Ettercap** in a controlled lab.

- [ ] Protocol Exploitation: Enumerate/exploit **SMB/FTP/SSH** via **Metasploit** modules.

- [ ] VPN & Tunneling: Stand up **OpenVPN/IPsec**; practice **SSH tunnels** to bypass local firewalls.

**Level 5: Cloud Networking (2026 Standard)** — Tools: **AWS/Azure Free Tier, Terraform**

- [ ] VPC Design: Build **public + private subnets** in **AWS or Azure**.

- [ ] IaC: Use **Terraform** to deploy web server + security group/NACL.

- [ ] Cloud Security: Configure **SGs/NACLs**, then adjust rules to test bypass paths.

- [ ] Scaling: Add a **load balancer** and spread traffic across multiple instances.

---

<a id="automation-programmability"></a>

### Automation & Programmability

> [!TIP]
> **Goal:** Understand how automation transforms network operations and software-defined architectures.

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

---

<a id="part-2-stage-pcap-analysis"></a>

### PCAP Analysis — Systematic Methodology

> [!IMPORTANT]
> **Why This Exists Here:** PCAP analysis is referenced as a prerequisite or required skill in Phase 2 (Part 9 Sniffing/Spoofing), Phase 3 (network forensics), Phase 5 (wireless attacks), and Phase 7 (DFIR network forensics) — but is never taught as a standalone systematic skill anywhere. This stage fills that gap. After completing this stage, you will be able to approach any PCAP file with a structured methodology rather than random scrolling.

_Purpose: Develop a repeatable, professional workflow for capturing, filtering, dissecting, and documenting network evidence from PCAP files. This is one of the most high-leverage skills in both offensive (recon, credential capture, MITM validation) and defensive (incident response, network forensics) security._

**Wireshark Fundamentals:**

- [ ] **Display Filter Syntax (BPF vs Wireshark):** Understand that Wireshark uses its own display filter language separate from BPF (Berkeley Packet Filter) capture filters. Key display filters:
  - `ip.addr == 192.168.1.1` — filter by IP
  - `tcp.port == 443` — filter by port
  - `http.request.method == "POST"` — filter by HTTP method
  - `dns.qry.name contains "evil"` — substring match in DNS query
  - `!(arp or dns or icmp)` — exclude noisy broadcast traffic
  - `tcp.flags.syn == 1 && tcp.flags.ack == 0` — show only SYN packets (new connections)
  - `frame.time_delta > 3` — show frames with >3 second gap (detect timeouts/retransmits)
  - `tls.handshake.type == 1` — show TLS ClientHello
  - `smb2 || ntlmssp` — catch SMB/NTLM traffic
  - `http.authheader || ftp.request.command == "PASS"` — catch cleartext credentials

- [ ] **Capture Filters (tcpdump/tshark):** Use BPF syntax at capture time to reduce file size:
  - `tcpdump -i eth0 -w capture.pcap` — capture all traffic
  - `tcpdump -i eth0 port 80 or port 443 -w web.pcap` — web traffic only
  - `tcpdump -i eth0 host 192.168.1.100 -w target.pcap` — single host
  - `tcpdump -i eth0 not arp -w noarp.pcap` — exclude ARP noise

- [ ] **Tshark (Command-Line Wireshark):** Use `tshark` for scripting and automation:
  - `tshark -r file.pcap -T fields -e ip.src -e ip.dst -e tcp.dstport` — extract fields as CSV
  - `tshark -r file.pcap -Y "http.request.method==POST" -T fields -e http.file_data` — extract POST bodies
  - `tshark -r file.pcap -z conv,tcp` — conversation statistics (who talked to whom)
  - `tshark -r file.pcap -z io,phs` — protocol hierarchy statistics

**Protocol Dissection:**

- [ ] **TCP State Machine Analysis:** Understand every TCP flag combination and what it means in a capture:
  - `SYN` — connection initiation
  - `SYN-ACK` — server accepting connection
  - `ACK` — acknowledgment
  - `FIN` — graceful termination
  - `RST` — abrupt rejection or termination
  - `PSH` — push data immediately to application layer
  - Know that a port is **open** if SYN receives SYN-ACK; **closed** if SYN receives RST; **filtered** if SYN gets no response (dropped by firewall)

- [ ] **HTTP Analysis:** Use `File → Export Objects → HTTP` in Wireshark to extract transferred files. Inspect request/response headers. Look for: cleartext passwords in POST bodies, session cookies in Cookie/Set-Cookie headers, redirect chains, and 401/403 responses indicating authorization gates.

- [ ] **DNS Analysis:** Follow DNS queries end-to-end — request to response. Identify: non-standard DNS servers (potential DNS hijack), high-volume DNS queries (potential data exfiltration via DNS), NX-domain responses (C2 DGA detection), and unusual record types (TXT records used for exfil).

- [ ] **TLS/HTTPS Analysis:** A TLS-encrypted session cannot be decrypted without keys — but the handshake is visible. From the handshake, extract:
  - **SNI (Server Name Indication)** — hostname the client is connecting to (visible in ClientHello even for HTTPS)
  - **Certificate Subject/SAN** — who the server claims to be
  - **Cipher suite negotiated** — check for weak ciphers (RC4, DES, TLS 1.0/1.1)
  - **JA3 fingerprint** — client TLS fingerprint for client identification
  - **JA3S fingerprint** — server TLS fingerprint for server/malware identification
  - Filter: `tls.handshake.type == 1` for all ClientHellos; `ssl.handshake.certificate` for certificate chain

- [ ] **SMB/NTLM Analysis:** `smb2.cmd == 0x0003` (SMB Tree Connect), `ntlmssp` (NTLM auth), `smb2.filename` (files accessed). Capture and extract NetNTLMv2 challenge-response for offline cracking using `smb2` filter and `Responder`.

- [ ] **ARP Analysis:** `arp.opcode == 2` (ARP replies) — look for multiple replies to the same request (ARP spoofing indicator), gratuitous ARP (IP claiming), or ARP requests for gateway from unexpected sources.

**PCAP Workflow for Security Analysis:**

- [ ] **Step 1 — Protocol Hierarchy Statistics:** First view is always `Statistics → Protocol Hierarchy` — understand what protocols are present and in what proportion. Unexpected protocols (IRC, BitTorrent, non-standard ports) are the first anomaly signal.

- [ ] **Step 2 — Conversation Map:** `Statistics → Conversations` (TCP tab) — identify the top talkers and most active connections by byte volume and duration. Beaconing C2 traffic will often appear as many small connections at regular intervals.

- [ ] **Step 3 — Export Credentials:** For cleartext protocols (HTTP POST with `password`, FTP PASS, SMTP AUTH, LDAP bind), use `tshark` field extraction or Wireshark's search to pull credential material.

- [ ] **Step 4 — File Extraction:** `File → Export Objects` — extract HTTP/FTP/SMB objects (executables, scripts, documents) transferred in the capture for further analysis.

- [ ] **Step 5 — Timeline Reconstruction:** Sort by time; identify the first connection, first DNS query, first executable download, first outbound beacon. Build a timeline connecting cause and effect.

- [ ] **Step 6 — IOC Documentation:** For every anomaly found, document: timestamp, source IP:port, destination IP:port, protocol, finding summary, and recommendation. This is your network forensics artifact.

**PCAP Lab Progression:**

> [!NOTE]
> Complete all 10 PCAP exercises below. These become the 10 named `.pcap` deliverables required for the **Networking Packet Proof** gate earlier in this phase.

| #   | Capture Scenario                               | Primary Filter              | Deliverable                                    |
| --- | ---------------------------------------------- | --------------------------- | ---------------------------------------------- |
| 1   | ARP request/reply cycle                        | `arp`                       | Annotated ARP exchange explanation             |
| 2   | DNS query + response (A record and NXDOMAIN)   | `dns`                       | Annotated DNS exchange + negative response     |
| 3   | TCP 3-way handshake + FIN/RST                  | `tcp.flags`                 | TCP state diagram with timestamps              |
| 4   | TLS handshake (ClientHello → Finished)         | `tls.handshake`             | SNI, cipher suite, certificate chain extracted |
| 5   | HTTP GET request + 200 response with body      | `http`                      | HTTP header analysis + object export           |
| 6   | HTTP POST with form data (credentials visible) | `http.request.method==POST` | Credential extraction writeup                  |
| 7   | ICMP ping sweep + traceroute                   | `icmp`                      | Network path reconstruction                    |
| 8   | DHCP DORA (Discover/Offer/Request/Acknowledge) | `bootp`                     | DORA sequence diagram                          |
| 9   | NAT in action (pre/post translation addresses) | `ip.addr`                   | Before/after NAT IP comparison                 |
| 10  | Firewall drop (no response to SYN)             | `tcp.flags.syn==1`          | Open vs filtered vs closed port evidence       |

> [!IMPORTANT]
> **Move-On Gate:** You can open any unknown PCAP file and within 5 minutes identify: the top protocols present, the most active conversations, whether cleartext credentials are visible, and whether any anomalous patterns exist. You can write a 1-page network event summary from a PCAP without assistance.

---

<a id="toc-part-3-cryptography"></a>
<a id="part-3-cryptography"></a>

## Part 3: Cryptography

<a id="stage-1-core-concepts-algorithms"></a>

### **Stage 1: Core Concepts & Algorithms**

> [!TIP]
> **Goal:** Build a working mental model of every cryptographic primitive used in security — symmetric ciphers, asymmetric key operations, hash functions, MACs, and key derivation. Stage 5 teaches how these break. You need this stage first or Stage 5 will be memorisation without understanding.

- [ ] **CIA Alignment:** Map cryptographic tools to security goals: **Confidentiality** = encryption prevents unauthorised reading; **Integrity** = hashing/MAC detects modification; **Authenticity** = digital signatures prove origin; **Non-repudiation** = signed artefacts cannot be disowned. Not every algorithm provides all four — know which provides which.

- [ ] **Symmetric Encryption — How It Works:**
  - A **single shared key** encrypts and decrypts. Sender and receiver must both have the key; key distribution is the hard problem.
  - **AES (Advanced Encryption Standard):** Block cipher operating on 128-bit blocks with 128/192/256-bit keys. The algorithm itself is secure — attacks target the *mode of operation*, not AES directly. Know this distinction.
  - **Block Cipher Modes — This Is Where Security Lives or Dies:**
    - **ECB (Electronic Codebook):** Each block encrypted independently with the same key. **Identical plaintext blocks → identical ciphertext blocks.** Leaks data structure. Never use for anything beyond a single block. The AES-ECB encrypted Tux image is the canonical demonstration.
    - **CBC (Cipher Block Chaining):** Each plaintext block is XORed with the previous ciphertext block before encryption. Requires an **Initialization Vector (IV)** for the first block. IV must be **unpredictable** — a predictable IV enables chosen-plaintext attacks. Requires **padding** to fill the last block — padding validation is the source of padding oracle attacks (Stage 5).
    - **CTR (Counter):** Turns the block cipher into a stream cipher. Encrypts a counter value, XORs the result with plaintext. **No padding needed.** Nonce + counter must never repeat with the same key — nonce reuse reveals XOR of plaintexts.
    - **GCM (Galois/Counter Mode):** CTR mode + authentication tag (GHASH). Provides both confidentiality and integrity in one operation (AEAD — Authenticated Encryption with Associated Data). The authentication key is derived from the encryption key — **nonce reuse in GCM is catastrophic** (exposes authentication key, allows forgery).
  - **ChaCha20-Poly1305:** Stream cipher (ChaCha20) + MAC (Poly1305). AEAD, like GCM. Preferred over AES-GCM on systems without hardware AES acceleration (mobile, IoT). Used in TLS 1.3.

- [ ] **Asymmetric Encryption — Public/Private Key Pairs:**
  - **Key pair properties:** Public key encrypts / verifies signatures; Private key decrypts / creates signatures. Public key can be distributed freely; private key never leaves the owner's control.
  - **RSA:** Security relies on the difficulty of factoring the product of two large primes (n = p × q). Key operations: encryption uses public exponent e, decryption uses private exponent d. **Padding is mandatory** — unpadded RSA is deterministic and malleable:
    - **PKCS#1 v1.5 padding** (legacy, still widespread): vulnerable to Bleichenbacher's attack (padding oracle — see Stage 5).
    - **OAEP (Optimal Asymmetric Encryption Padding):** randomised, secure for encryption.
    - **PSS (Probabilistic Signature Scheme):** randomised, secure for signatures.
  - **ECC (Elliptic Curve Cryptography):** Security relies on the elliptic curve discrete logarithm problem — much harder than integer factorisation for equivalent key sizes. A 256-bit ECC key ≈ 3072-bit RSA in security level.
    - **ECDSA (Elliptic Curve Digital Signature Algorithm):** Signatures. Used in TLS certificates. Requires a unique random nonce per signature — nonce reuse allows private key recovery (the PS3 hack).
    - **ECDH / ECDHE (Elliptic Curve Diffie-Hellman):** Key exchange. Both parties compute the same shared secret without transmitting it. The **E** (Ephemeral) variant generates a new key pair per session — this is what provides **Perfect Forward Secrecy** in TLS 1.3.
    - **Common curves:** P-256 (NIST, widely used), P-384, Curve25519 (modern, high-performance, used in Signal/WireGuard/TLS 1.3).

- [ ] **Hash Functions — One-Way Transformation:**
  - Input of any length → fixed-length digest. **Cannot be reversed.** Identical inputs always produce identical outputs (deterministic). A one-bit change in input produces a completely different output (avalanche effect).
  - **SHA-2 family (SHA-256, SHA-384, SHA-512):** Based on Merkle-Damgård construction — processes input in blocks, chaining intermediate state. Widely used, currently secure for all purposes. SHA-256 produces a 32-byte digest.
  - **SHA-3 / Keccak:** Sponge construction — fundamentally different from SHA-2. Immune to length extension attacks that affect Merkle-Damgård hashes. Not a replacement for SHA-2 in most contexts, but the approved alternative.
  - **BLAKE3:** Modern, parallelisable, faster than SHA-2. Used in some password managers, version control systems, and new protocols.
  - **Common misuses:** Using MD5 or SHA-1 for integrity checks (both are collision-broken). Using an unsalted SHA-256 to store passwords (fast = attackable with GPU rainbow tables).

- [ ] **HMAC — Authenticated Hashing:**
  - HMAC(key, message) = H(key ⊕ opad ∥ H(key ⊕ ipad ∥ message)). Proves the message was produced by someone with the key. Not vulnerable to length extension attacks (unlike raw H(secret ∥ message)). Used in JWT signatures (HS256), API authentication, TLS MAC in older versions.

- [ ] **Key Derivation Functions (KDFs):**
  - **PBKDF2:** Password-based KDF. Applies HMAC iteratively (e.g., 600,000× for SHA-256). Configurable iterations, but parallelisable — GPU cracking is feasible at low iteration counts.
  - **bcrypt:** Memory-expensive by design. Uses the Blowfish key schedule. Work factor is a logarithmic cost parameter. Truncates passwords at 72 bytes — a known limitation.
  - **scrypt:** Memory-hard (requires large RAM, not just CPU cycles). Harder to parallelise on ASICs/GPUs than bcrypt.
  - **Argon2id:** Winner of the Password Hashing Competition (2015). Combines memory-hardness (Argon2i) and GPU resistance (Argon2d). Current OWASP recommendation for new systems. Parameters: memory cost (≥64 MB), time cost (iterations), parallelism.
  - **HKDF (HMAC-based Key Derivation Function):** Not for passwords — for deriving multiple keys from a single shared secret (e.g., deriving TLS session keys from the ECDHE shared secret). RFC 5869.

- [ ] **Cryptographic Randomness — CSPRNG vs PRNG:**
  - A regular PRNG (e.g., `rand()`, `Math.random()`) is deterministic and seeded — an attacker who knows the seed can predict all outputs. **Never use for cryptographic material.**
  - A CSPRNG (Cryptographically Secure PRNG) is seeded from hardware entropy (CPU timing jitter, device interrupts, `/dev/urandom`, `getrandom()` syscall). Outputs are computationally indistinguishable from random.
  - **In practice:** Use `os.urandom()` in Python, `crypto.getRandomValues()` in JS, `SecureRandom` in Java. Avoid seeding with timestamps, process IDs, or predictable values.
  - **IV/nonce generation:** Always generated with a CSPRNG. A predictable IV in CBC or a repeated nonce in GCM/CTR is a critical vulnerability (see Stage 5).

- [ ] **Encoding vs Encryption vs Hashing — The Foundational Confusion:**
  - **Encoding** (Base64, URL encoding, hex): Transforms data format for transmission/storage. **Reversible with no key.** Provides zero security. Seeing Base64 in a field does not mean it is encrypted.
  - **Encryption:** Transforms data using a key. Reversible only with the correct key. Provides confidentiality.
  - **Hashing:** One-way transformation. Not reversible. Provides integrity verification and password storage (with KDFs).
  - Why this matters: developers frequently mistake Base64-encoded data for encrypted data, store Base64-encoded passwords thinking they are "hashed," or confuse a fast hash (SHA-256) with a password KDF (Argon2).

---

<a id="stage-2-secure-communication-data-in-transit"></a>

### **Stage 2: Secure Communication (Data in Transit)**

> [!TIP]
> **Goal:** Understand exactly how TLS secures a connection — every step of the handshake, every field in the cipher suite string, and why forward secrecy matters. This stage directly underpins your ability to analyse TLS captures (Part 2 PCAP lab), exploit TLS misconfigurations (Part 18), and understand downgrade attacks (Stage 5).

- [ ] **TLS 1.3 Handshake — Step by Step:**
  TLS 1.3 reduced the handshake from 2 round-trips (TLS 1.2) to 1 round-trip. Know every message:
  1. **ClientHello:** Client sends supported cipher suites, TLS version, random nonce, and — critically — one or more **KeyShare** entries (client's ECDHE public key for the preferred group, e.g., X25519). The client starts key negotiation immediately rather than waiting for the server to pick parameters.
  2. **ServerHello:** Server selects the cipher suite and returns its own **KeyShare** (ECDHE public key). Both sides can now derive the **shared secret** using ECDH — the connection is encrypted from this point forward.
  3. **{EncryptedExtensions}:** Server sends extensions (ALPN, server name) — now encrypted.
  4. **{Certificate}:** Server's X.509 certificate — encrypted.
  5. **{CertificateVerify}:** Server signs the handshake transcript with its private key — proves it owns the certificate.
  6. **{Finished}:** HMAC over the entire handshake transcript — detects tampering.
  7. **{Finished} (client):** Client verifies and responds. Handshake complete — application data flows.
  - **Key insight:** In TLS 1.3, the server's certificate private key is only used for authentication (CertificateVerify), not for key exchange. The session key comes entirely from ECDHE. This is what provides **Perfect Forward Secrecy** — compromise of the server's private key does not decrypt past sessions.

- [ ] **Cipher Suite Anatomy — Read It Left to Right:**
  A TLS 1.3 cipher suite like `TLS_AES_256_GCM_SHA384` means:
  - `TLS` — protocol
  - `AES_256_GCM` — AEAD algorithm for bulk encryption (AES-256 in GCM mode)
  - `SHA384` — hash algorithm used in HKDF for key derivation
  - TLS 1.3 removed the key exchange and authentication fields from the cipher suite name because ECDHE is mandatory and the cert algorithm is specified separately.
  - A TLS 1.2 suite like `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256` breaks into: key exchange (ECDHE), authentication (RSA certificate), bulk cipher (AES-128-GCM), MAC hash (SHA-256).

- [ ] **Perfect Forward Secrecy (PFS):**
  With static RSA key exchange (pre-TLS 1.3 option): the server's private key encrypts the session key directly. Capture traffic today, obtain the private key later → decrypt all past sessions.
  With ECDHE: each session generates a **fresh ephemeral key pair**. The ECDHE private key is discarded after the handshake. No long-term key can decrypt past sessions. This is PFS. TLS 1.3 makes ECDHE mandatory — PFS is no longer optional.

- [ ] **Protocol Version History & Deprecation:**
  - **SSL 2.0 / SSL 3.0:** Broken (POODLE, DROWN). Must be disabled. Any server still advertising SSLv3 is a critical finding.
  - **TLS 1.0 / TLS 1.1:** Deprecated (RFC 8996, 2021). Vulnerable to BEAST (TLS 1.0), POODLE-over-TLS. PCI-DSS requires disablement. Disable on all servers.
  - **TLS 1.2:** Still acceptable, widely deployed, requires proper cipher suite configuration (disable RC4, export ciphers, NULL ciphers, anonymous DH).
  - **TLS 1.3:** Current standard. Mandatory ECDHE, mandatory AEAD ciphers, removed renegotiation, removed compression (CRIME mitigation).

- [ ] **Certificate Validation During the Handshake:**
  When the client receives the server's certificate, it validates: (1) signature chain to a trusted root CA; (2) certificate not expired; (3) hostname matches Subject Alternative Name (SAN) or Common Name (CN); (4) certificate not revoked (OCSP check or CRL). **Any failure should abort the handshake.** TLS clients that skip validation (e.g., `verify=False` in Python requests) are vulnerable to MITM attacks.

- [ ] **Mutual TLS (mTLS):**
  Standard TLS authenticates only the server. mTLS requires the client to also present a certificate — the server verifies it against a trusted CA. Used in: microservice-to-microservice authentication, zero trust networks, client certificate authentication portals. Attack surface: stolen client certificates enable impersonation; CA compromise enables mTLS bypass.

- [ ] **Secure Protocol Alternatives — Know When to Use Each:**
  - **SFTP / SCP** (SSH-based file transfer) — replaces FTP (cleartext). SSH provides both authentication and encryption.
  - **FTPS** (FTP over TLS) — not the same as SFTP. Uses TLS, but firewall-unfriendly (data channel on dynamic port). Prefer SFTP.
  - **IPsec (IKEv2)** — network-layer encryption for VPNs. Operates below the application layer; encrypts all IP traffic between endpoints. Two modes: **Transport** (encrypts payload only) and **Tunnel** (encrypts entire IP packet — used in site-to-site VPNs).
  - **WireGuard** — modern VPN protocol. Uses ChaCha20-Poly1305 + Curve25519. Simpler than IPsec, faster, and the codebase is orders of magnitude smaller (easier to audit).
  - **SSH** — encrypts terminal sessions, file transfer, and port forwarding. The server's host key should be verified on first connection — a key fingerprint mismatch indicates a MITM or server change.

- [ ] **DTLS (Datagram TLS):**
  TLS runs over TCP. DTLS adapts TLS to run over UDP — used in WebRTC (video/audio), QUIC (underlying HTTP/3), VoIP. Key difference: DTLS must handle out-of-order and dropped datagrams. Attack surface: replay attacks (DTLS has a sliding window replay protection mechanism).

- [ ] **Protocol Hardening Checklist (Practical):**
  On any TLS-enabled service you control or assess:
  - [ ] Disable SSLv2, SSLv3, TLS 1.0, TLS 1.1
  - [ ] Disable weak ciphers: RC4, NULL, EXPORT, anonymous DH (ADH/AECDH), DES/3DES
  - [ ] Enable only AEAD ciphers in TLS 1.2: AES-128-GCM, AES-256-GCM, ChaCha20-Poly1305
  - [ ] Require TLS 1.3 where possible
  - [ ] Set `HSTS` header (HTTP Strict Transport Security) with `max-age` ≥ 1 year
  - [ ] Verify with: `testssl.sh`, `sslyze`, `nmap --script ssl-enum-ciphers`

---

<a id="stage-3-identity-trust-pki"></a>

### **Stage 3: Identity & Trust (PKI)**

> [!TIP]
> **Goal:** Understand how the internet decides to trust a server's public key — and how that trust infrastructure is attacked. PKI underpins HTTPS, code signing, email encryption, VPN authentication, and Active Directory. Certificate-related misconfigurations appear in nearly every enterprise pentest (Part 23 ADCS attacks, Part 24 cloud IAM, Part 18 web server hacking).

- [ ] **X.509 Certificate Anatomy — Read a Certificate Field by Field:**
  A certificate is a signed data structure that binds a public key to an identity. Open any certificate in a browser or with `openssl x509 -text -noout -in cert.pem` and locate:
  - **Subject:** Who the certificate identifies. Modern certs use **Subject Alternative Names (SANs)** for hostnames — the CN field is largely legacy but still parsed by some clients.
  - **Issuer:** The CA that signed this certificate.
  - **Validity (Not Before / Not After):** The certificate's lifetime. After `Not After`, the certificate is expired and must be replaced — expired certs cause outages and are a common pentest finding.
  - **Public Key + Algorithm:** The subject's public key and algorithm (RSA-2048, EC P-256, etc.).
  - **Key Usage / Extended Key Usage:** Constrains what the key can do. `Digital Signature` + `Key Encipherment` for TLS server auth; `Code Signing` for binaries; `Certificate Sign` for CA certs. A cert with `Certificate Sign` but without `CA:true` in Basic Constraints should be rejected as a CA — this is the basis of some ADCS escalation paths.
  - **Subject Key Identifier (SKI) / Authority Key Identifier (AKI):** Used to chain certificates. AKI identifies which CA key signed this cert.
  - **Basic Constraints — CA:true / pathLenConstraint:** Marks whether this cert can sign other certificates and how many intermediate CAs are permitted in the chain.

- [ ] **Certificate Lifecycle — From CSR to Revocation:**
  1. **Key generation:** Subject generates a key pair (private key never leaves the subject).
  2. **CSR (Certificate Signing Request):** Subject creates a CSR containing their public key and requested attributes (CN, SANs, key usage). Signed with the private key to prove possession.
  3. **CA validation:** The CA verifies the requestor controls the domain/identity (DV = domain validation via DNS/HTTP challenge; OV = organisation validation with manual checks; EV = extended validation).
  4. **Issuance:** CA signs the certificate with its private key. The certificate is now trusted by anyone who trusts the CA.
  5. **Deployment:** Certificate installed on the server alongside the private key.
  6. **Renewal:** Before expiry, repeat from step 1 (or reuse the existing key pair with a new CSR). **Let's Encrypt automates this with ACME protocol (Certbot).**
  7. **Revocation:** If the private key is compromised or the cert is mis-issued, the CA revokes it — publishing the serial number in a CRL or making it queryable via OCSP.

- [ ] **CA Hierarchy — Root, Intermediate, and Leaf Certificates:**
  - **Root CA:** Self-signed; embedded in OS/browser trust stores. Root CA private keys are kept **offline in HSMs** — compromise of a root CA is catastrophic (all certs it issued become untrustable). About 150 root CAs are trusted by default in modern browsers.
  - **Intermediate CA:** Signed by the root CA. Issues end-entity (leaf) certificates. Used to isolate the root CA from daily issuance operations. Most TLS certs are issued by intermediates.
  - **Leaf certificate:** The TLS certificate you install on your server. Trusted because: leaf is signed by intermediate → intermediate is signed by root → root is in the trust store.
  - **Chain of trust:** A TLS server must present the full chain (leaf + intermediates) — the client should not need to fetch intermediates. A missing intermediate causes "incomplete chain" errors even if the leaf cert itself is valid.

- [ ] **OCSP (Online Certificate Status Protocol) and CRL (Certificate Revocation List):**
  - **CRL:** A file published by the CA containing a list of revoked serial numbers. Client downloads the CRL and checks the serial. Problems: CRLs can be large, are updated periodically (not real-time), and clients often fail open (accept the cert) if the CRL cannot be fetched.
  - **OCSP:** Client queries the CA's OCSP responder with a specific serial number and receives a signed "good/revoked/unknown" response. Real-time, but leaks to the CA which sites users visit.
  - **OCSP Stapling:** Server pre-fetches its own OCSP response, caches it, and includes ("staples") it in the TLS handshake. Client gets revocation status without contacting the CA directly. No privacy leak, no latency. Enable with `ssl_stapling on` (nginx) or `SSLUseStapling On` (Apache).
  - **Revocation failure modes:** Most browsers **fail open** — if revocation checking fails (CRL unreachable, OCSP timeout), the cert is accepted. Hard-fail revocation (reject if check fails) is rarely deployed because it causes availability issues.

- [ ] **Certificate Transparency (CT):**
  - Every publicly-trusted TLS certificate must be logged to a **CT log** (an append-only, cryptographically verifiable log of all issued certs). Browsers enforce this.
  - **Why it matters offensively:** CT logs are public — [crt.sh](https://crt.sh) and [censys.io](https://search.censys.io) allow you to enumerate all certificates ever issued for a domain, revealing subdomains, internal staging hostnames, and historical infrastructure. This is a primary recon tool in Part 4.
  - **Why it matters defensively:** Your organisation can monitor CT logs for certificates issued for your domain by unauthorised CAs (mis-issuance detection). Tools: `certspotter`, Cloudflare's CT monitor.

- [ ] **Certificate Pinning:**
  - An application hardcodes the expected certificate (or its public key hash) instead of trusting the full CA chain. If the server presents a different certificate — even one signed by a trusted CA — the connection is rejected.
  - **HTTP Public Key Pinning (HPKP):** Browser-level pinning via response header. Deprecated — too easy to permanently brick a site if pins are set incorrectly.
  - **In-app pinning (mobile/desktop):** The app's code contains the expected certificate or SPKI hash. Hardened apps (banking, VPN clients) use this. Bypass techniques are in Part 22 (Frida, Objection, `ssl-kill-switch`).
  - **Security implication:** Corporate SSL inspection proxies (Zscaler, Forcepoint) intercept HTTPS by replacing certificates with corporate CA-signed ones. Apps with cert pinning break under SSL inspection — this is a common enterprise compatibility issue.

- [ ] **S/MIME and Email Encryption:**
  - S/MIME signs and/or encrypts email using the sender's certificate. Signing proves authenticity (recipient validates signature against sender's public key cert); encryption uses the recipient's public key cert.
  - Requires both parties to have certificates issued by mutually trusted CAs — historically a barrier to adoption. Enterprise deployments use an internal CA.
  - **Security relevance:** Understanding S/MIME is prerequisite for understanding email-based attacks (Part 10): why DMARC prevents *domain spoofing* but not *content forgery*, and why digitally signed emails from a phishing actor with their own valid cert still pass S/MIME validation.

- [ ] **PKI Attack Surface (Forward Reference):**
  - **ADCS (Active Directory Certificate Services):** Microsoft's enterprise CA. Misconfigurations (ESC1–ESC8) allow attackers to request certificates for arbitrary users, including domain admins. Covered in depth in Part 23.
  - **CA compromise:** If a CA's private key is stolen, all certs it issued can be forged. Notable historical example: DigiNotar (2011) — CA compromised, fraudulent Google certs issued, CA removed from all trust stores.
  - **Mis-issued certificates:** CAs have issued certs for domains they shouldn't have (e.g., Symantec issuing google.com test certs). CT logs are the primary detection mechanism.
  - **Wildcard certificate abuse:** A `*.domain.com` cert is valid for any single-level subdomain. If stolen or extracted from one server, it can impersonate any subdomain.

---

<a id="stage-4-data-at-rest-password-security"></a>

### **Stage 4: Data at Rest & Password Security**

> [!TIP]
> **Goal:** Secure stored data.

- [ ] **Disk Encryption:** Deploy **BitLocker, LUKS, FileVault** for full-disk encryption.

- [ ] **Password Storage:** Never store plaintext passwords; use **bcrypt, scrypt, Argon2** with **salting** to defeat rainbow tables.

- [ ] **Key Management:** Use **HSM, KMS (AWS KMS, Azure Key Vault)** for secure key storage and rotation.

- [ ] **Modern Hashing Profiles:** Standardize **Argon2id** (memory-hard) with tuned **memory (e.g., 64–256 MB), iterations, parallelism**, or **bcrypt** with current cost; prefer **password peppering** server-side and enforce **per-user salts**. Deprecate **MD5/SHA-1/SHA-256 for password storage** and legacy **PBKDF2-low-iteration** configs.

- [ ] **LUKS (Linux Unified Key Setup) Internals:** LUKS provides full-disk encryption on Linux. Understand the LUKS2 header structure: PBKDF2 or Argon2 key derivation for key slot protection, up to 32 key slots (each can hold a different passphrase or key file), and the master key (volume key) encrypted inside each slot. Key rotation: add a new slot with the new passphrase → verify it unlocks the volume → remove the old slot — the encrypted data itself is never touched, only the key material. Detached LUKS headers increase security: store the header file separately from the encrypted volume; without the header, the ciphertext is indistinguishable from random bytes. `cryptsetup` is the primary tool: `cryptsetup luksOpen`, `luksAddKey`, `luksKillSlot`, `luksDump`.

- [ ] **Envelope Encryption Pattern:** The production standard for cloud and enterprise key management. Architecture: a **Data Encryption Key (DEK)** encrypts the actual data; a **Key Encryption Key (KEK)** encrypts the DEK; the KEK is stored in a Hardware Security Module or KMS. The critical property: rotating the KEK requires re-encrypting only the small DEK, not re-encrypting terabytes of data. AWS S3 SSE-KMS, Azure Storage Service Encryption, and GCP CMEK all implement this pattern. Understand it before designing any data-at-rest system that must support key rotation or compliance requirements.

- [ ] **Key Rotation Lifecycle:** Know what rotation actually means operationally. Automatic rotation (AWS KMS default: annual) creates a new **backing key version** — old versions remain for decryption, new data uses the new version. Full re-encryption rotation: generate new key → decrypt all data with old key → re-encrypt with new key → decommission old key. Know which your system uses and why the distinction matters for breach impact: if a key is compromised, automatic rotation protects future data but not already-encrypted data unless you run a full re-encryption.

---

<a id="stage-5-cryptographic-attacks-weaknesses"></a>

### **Stage 5: Cryptographic Attacks & Weaknesses**

> [!TIP]
> **Goal:** Understand how crypto fails at the mechanism level — not just which algorithms are "weak", but WHY they break and what an attacker can do with the break. These attack classes appear repeatedly across Phases 4–7.

- [ ] **Weak Algorithms — What "Broken" Actually Means:**
  - **MD5:** Collision attacks are practical (two different inputs with identical MD5 hash in seconds). SHA-1 collided in SHAttered (2017). Never use either for integrity or digital signatures.
  - **DES:** 56-bit key — exhaustive search takes hours on modern hardware. Triple-DES (3DES) has meet-in-the-middle and SWEET32 vulnerabilities.
  - **RC4:** Statistical keystream biases allow plaintext recovery after enough ciphertext collection. Broken in WEP, early TLS, TKIP.

- [ ] **Padding Oracle Attacks:** CBC mode requires padding to block boundaries. If a server leaks whether decryption produced valid padding (via error message or timing), an attacker can decrypt arbitrary ciphertext one byte at a time — no key material needed. Practical impact: **POODLE** (SSLv3), **BEAST** (TLS 1.0), ASP.NET `__VIEWSTATE` oracles.

- [ ] **Length Extension Attacks:** Hash functions built on Merkle-Damgård (MD5, SHA-1, SHA-256) are vulnerable to `H(secret || message)` authentication schemes. An attacker knowing the hash and message length can extend the message and forge a valid hash without the secret. Not applicable to HMAC.

- [ ] **Timing Attacks:** Early-exit string comparison leaks secrets via response time differences. Defense: constant-time comparison (`hmac.compare_digest()`). Relevant to: API token validation, cookie comparison.

- [ ] **ECB Mode — Structural Leakage:** Identical plaintext blocks → identical ciphertext blocks. Leaks data structure. Classic: AES-ECB encrypted bitmap still shows the image outline. Enables block rearrangement attacks in cookies/sessions.

- [ ] **IV/Nonce Reuse:** AES-GCM nonce reuse allows recovery of the authentication key and forgery of ciphertext. AES-CTR nonce reuse reveals XOR of plaintexts. CBC predictable IV enables chosen-plaintext attacks.

- [ ] **Key Management Failures:**
  - Hardcoded keys in source code (GitHub dorking for `AES_KEY`, `api_secret` with actual values)
  - Weak KDF: deriving encryption keys from passwords with MD5 instead of PBKDF2/scrypt/Argon2
  - Keys stored alongside encrypted data; no forward secrecy in symmetric key transport

- [ ] **Downgrade Attacks:** TLS negotiation can be forced to weaker options:
  - **POODLE:** Force TLS 1.0 fallback → SSL 3.0 padding oracle
  - **DROWN:** Exploit SSLv2 on a server sharing RSA key with a TLS server → decrypt TLS traffic
  - Defense: reject TLS < 1.2, disable RC4, enforce TLS 1.3 where possible

- [ ] **CRIME / BREACH — Compression + Encryption Side Channel:** TLS that compresses HTTP headers before encrypting allows length-based plaintext extraction. CRIME disabled TLS-level compression. BREACH exploits HTTP gzip compression. Mitigation: disable response compression for pages containing secrets.

- [ ] **Cryptanalysis Basics — Adversary Models:**
  - **Ciphertext-only:** Attacker has only ciphertext. Statistical analysis.
  - **Known-plaintext:** Attacker has plaintext/ciphertext pairs.
  - **Chosen-plaintext (CPA):** Attacker chooses plaintext and observes ciphertext. Breaks ECB, CBC with predictable IV.
  - **Chosen-ciphertext (CCA):** Attacker can decrypt chosen ciphertexts. Breaks unpadded RSA, padding oracles.

---

<a id="stage-6-post-quantum-cryptography"></a>

### **Stage 6: Post-Quantum Cryptography (PQC)**

> [!TIP]
> **Goal:** Understand the quantum threat to current public-key cryptography and the NIST-standardised replacements being deployed in production now.

- [ ] **Why Quantum Breaks Current Public-Key Crypto:** RSA, ECC, DH, and DSA rely on integer factoring and discrete logarithm hardness. **Shor's Algorithm** solves both in polynomial time on a sufficiently large quantum computer (CRQC). A CRQC would break all deployed public-key encryption and signatures. Symmetric algorithms (AES, SHA-256) are weakened but not broken — Grover's Algorithm halves effective key size, so AES-256 retains equivalent 128-bit security. Implication: AES-256 and SHA-384+ remain secure post-quantum; RSA/ECC/DH do not.

- [ ] **"Harvest Now, Decrypt Later" (HNDL) Threat:** Adversaries collect encrypted TLS traffic today to decrypt later with a CRQC. Data with long sensitivity periods (classified communications, medical records, financial contracts) is already at risk. This is why PQC migration is urgent before a CRQC exists.

- [ ] **NIST PQC Standards (August 2024):**
  - **ML-KEM (FIPS 203)** — Replaces RSA/ECDH for key exchange. Also called Kyber. Based on Module LWE (Learning With Errors) lattice problem.
  - **ML-DSA (FIPS 204)** — Replaces RSA/ECDSA for signatures. Also called Dilithium.
  - **SLH-DSA (FIPS 205)** — Hash-based signature algorithm. Algorithm diversity complement to ML-DSA.

- [ ] **Hybrid Deployment (Current Best Practice):** Combine classical (X25519) with PQC (ML-KEM) in a single TLS handshake (`X25519MLKEM768`). If either is broken, the session remains secure. Chrome and Firefox enabled hybrid PQC key exchange by default in 2024.

- [ ] **Crypto-Agility:** Design systems so cryptographic algorithms can be swapped without re-engineering. Use libraries with algorithm abstraction (OpenSSL 3.x, BouncyCastle) rather than hardcoding algorithm identifiers.

- [ ] **SIKE Broken Classically (2022):** SIKE — a NIST PQC finalist — was broken by a classical computer in 62 minutes in 2022. This illustrates that "post-quantum" does not mean "quantum-only threat" — novel constructions can be broken by classical cryptanalysis.

- [ ] **Zero-Knowledge Proofs (ZKP) — Awareness:** A zero-knowledge proof allows one party (the prover) to convince another (the verifier) that a statement is true without revealing any information beyond the truth of the statement. Relevant to:
  - **zk-SNARKs (Succinct Non-Interactive Argument of Knowledge):** Used in Zcash and Ethereum's zkEVM. Prover demonstrates knowledge of a secret satisfying a circuit without revealing the secret.
  - **zk-STARKs:** Transparent (no trusted setup) alternative to SNARKs. Larger proofs but post-quantum secure.
  - **ZKP-based authentication:** Prove knowledge of a password without sending the password — no secret transmitted, no hash to steal.
  - **Security relevance:** ZKP systems introduce new attack surfaces (circuit under-constrained bugs, trusted setup compromise in pairing-based SNARKs). Full ZKP security is covered in Part 34 (Blockchain & Web3 Security). Awareness here is sufficient for Phase 1.

<a id="lab-progression-cryptography"></a>

### **Lab Progression (Cryptography)**

> [!TIP]
> **Goal:** Turn crypto from vocabulary into observable behavior.

- [ ] **Symmetric Modes Lab:** Using Python's `cryptography` library, encrypt the same 48-byte plaintext with AES in ECB mode, then CBC mode (random IV), then GCM mode (random nonce). Compare ciphertext outputs. For ECB: encrypt an image (use a raw pixel bitmap) and observe structural leakage. For CBC: reuse the same IV for two encryptions and document what the first block reveals. For GCM: reuse the nonce twice and observe the authentication tag difference. Document exactly what fails and why.
- [ ] **Hashing Lab:** Generate hashes for files, modify a single byte, and prove integrity failure with SHA-256. Compare hash output lengths for SHA-256, SHA-384, SHA-512, and BLAKE3.
- [ ] **Password Storage Lab:** Compare unsalted SHA-256, salted SHA-256, bcrypt (cost=12), and Argon2id (m=65536, t=3) — measure cracking cost for each using `hashcat` against a known wordlist. Document why speed is the enemy of password security.
- [ ] **TLS Handshake Lab:** Capture TLS 1.3 in Wireshark against a local HTTPS server. Identify: ClientHello (cipher suites offered, KeyShare groups), ServerHello (selected cipher, server KeyShare), Finished messages. Annotate the transition from cleartext to encrypted. Verify PFS by confirming no RSA key exchange occurred.
- [ ] **PKI Chain Lab:** Using `openssl`, create a 3-tier PKI: (1) self-signed root CA, (2) intermediate CA signed by root, (3) leaf certificate signed by intermediate. Install the root CA in a local browser trust store. Serve the leaf cert with `openssl s_server`. Verify the chain validates successfully. Then: revoke the leaf cert (generate a CRL), serve the CRL, and confirm the browser rejects the revoked cert. Deliverable: annotated OpenSSL commands + chain diagram.
- [ ] **Certificate Transparency Lab:** Use `crt.sh` to enumerate all certificates ever issued for a domain you own or a lab domain. Identify: subdomain patterns, issuing CAs, historical certificates that reveal old infrastructure. Document 3 subdomains found exclusively via CT logs that are not discoverable via DNS brute-force.
- [ ] **Post-Quantum Awareness:** Document NIST PQC primitives (ML-KEM, ML-DSA, SLH-DSA), hybrid deployment model, and crypto-agility migration risk. Run `openssl s_client -connect` against a modern server and identify whether `X25519MLKEM768` appears in the KeyShare group list.

> [!IMPORTANT]
> **Move-On Gate:** You can explain what was encrypted, what was authenticated, what was signed, and what failed when trust broke. You can read a TLS cipher suite string and explain each component. You can create a local CA, issue a signed certificate, and verify the chain. You can explain why AES-ECB is insecure without looking it up.

---

<a id="toc-part-3b-authentication-standards-primer"></a>
<a id="part-3b-authentication-standards-primer"></a>

## Part 3B: Authentication Standards Primer

> [!IMPORTANT]
> **Why This Exists Here:** Parts 8, 12, 19, and 23 all reference OAuth, OIDC, JWT, and session tokens as attack surfaces. Students routinely hit JWT attacks and OAuth consent phishing without understanding how token issuance actually works. This primer fills that conceptual gap now — before you hit the attack techniques. Deep exploitation and protocol abuse are covered in Part 19 (API Security, Phase 4) and Part 23 (Entra ID, Phase 6). This Part is concepts only.

_Purpose: Understand how modern applications establish and maintain identity. Understand what tokens ARE, how they are issued, and how they are validated — before you learn to forge or steal them._

<a id="auth-primer-stage-1-session-based-auth"></a>

### **Stage 1: Session-Based Authentication**

> [!TIP]
> **Goal:** Understand the original web identity model — the one most legacy applications still use.

- [ ] **How Sessions Work:** Understand the full lifecycle: user submits credentials → server validates → server creates session record in database or memory → server sets a `Set-Cookie: session_id=...` response header → browser stores and resends cookie on every subsequent request → server looks up session_id to identify user.

- [ ] **Session ID Properties:** Know that secure session IDs must be **cryptographically random (≥128 bits), opaque (no encoded data), short-lived, invalidated on logout and privilege change**, and transmitted only over TLS.

- [ ] **Cookie Security Attributes:** Know the five attributes by name — `HttpOnly`, `Secure`, `SameSite`, `Domain`/`Path`, `Expires`/`Max-Age`. The full security reasoning for each (what its absence allows an attacker to do and why) is in **Part 3C Stage 2: Cookies, Sessions & Tokens** — the canonical treatment. Review it there rather than here.

- [ ] **Session Fixation vs Session Hijacking:** Understand the difference:
  - **Fixation:** Attacker sets the session ID before authentication; victim authenticates and server doesn't rotate the session ID
  - **Hijacking:** Attacker steals an existing valid session ID post-authentication (via XSS, network interception, etc.)

- [ ] **Common Weaknesses:** Sequential/predictable IDs, server-side session stores without TTL, session not invalidated on logout, session not rotated on privilege change, session transmitted over HTTP.

---

<a id="auth-primer-stage-2-token-based-auth"></a>

### **Stage 2: Token-Based Authentication & JWT**

> [!TIP]
> **Goal:** Understand stateless authentication tokens — how they are structured, signed, validated, and abused.

- [ ] **Why Tokens:** Understand the architectural motivation — stateless APIs cannot use server-side session stores; the client must carry all identity information in a signed token.

- [ ] **JWT Structure:** Understand the three parts of a JSON Web Token (`Header.Payload.Signature`):
  - **Header:** `{"alg": "RS256", "typ": "JWT"}` — declares the signing algorithm
  - **Payload:** Claims — `{"sub": "user123", "iss": "https://auth.example.com", "exp": 1729000000, "roles": ["admin"]}` — user identity + permissions
  - **Signature:** Cryptographic proof that the header and payload were not modified after issuance
  - All three parts are **Base64Url-encoded** (not encrypted by default — the payload is readable by anyone)

- [ ] **JWT Validation:** Understand what a correct recipient must verify:
  1. Signature is valid using the expected key
  2. Algorithm matches expected (`alg` header cannot be trusted at face value)
  3. Issuer (`iss`) matches expected
  4. Audience (`aud`) includes the current service
  5. Token is not expired (`exp`)
  6. Token is not used before `nbf` (not-before)

- [ ] **JWT Signing Algorithms:** Know the difference:
  - **HS256/HS512 (HMAC):** Symmetric — same secret used to sign and verify; both parties share the secret
  - **RS256/RS512 (RSA) / ES256 (ECDSA):** Asymmetric — private key signs, public key verifies; parties only share the public key

- [ ] **JWT Common Weaknesses (Awareness):** Know these exist — exploitation is in Part 19:
  - `alg: none` attack — token with no signature accepted if library doesn't enforce algorithm
  - RS256→HS256 confusion — attacker signs with the public key (treated as HMAC secret)
  - Weak secret brute-forcing — HMAC secrets guessable offline
  - Missing audience/issuer validation — token accepted by unintended service

- [ ] **Opaque Tokens vs JWTs:** Understand that many systems use **opaque tokens** (random strings that reference a server-side record) rather than self-contained JWTs. Know that introspection is required to validate opaque tokens. Know the trade-offs: JWTs are stateless and fast but cannot be revoked without a denylist; opaque tokens require a round-trip but can be instantly invalidated.

---

<a id="auth-primer-stage-3-oauth2"></a>

### **Stage 3: OAuth 2.0 — Delegated Authorization**

> [!TIP]
> **Goal:** Understand what OAuth is, what problem it solves, and how the authorization code flow works — before you attack it in Phase 4.

- [ ] **OAuth 2.0 Purpose:** Understand that OAuth 2.0 is an **authorization delegation framework** — it allows a user to grant an application (the client) access to a resource (e.g., their Google Drive) without sharing their password. The user delegates a limited set of permissions (scopes).

- [ ] **Roles:** Know the four OAuth actors:
  - **Resource Owner:** The user who owns the data and can grant permission
  - **Client:** The application requesting access (e.g., a third-party app)
  - **Authorization Server (AS):** Issues tokens after verifying the user's consent (e.g., Google Identity, Azure AD, Okta)
  - **Resource Server:** Holds the protected resource (e.g., Google Drive API); validates access tokens

- [ ] **Authorization Code Flow (Primary Flow):** Trace each step:
  1. Client redirects user to AS with `response_type=code`, `client_id`, `redirect_uri`, `scope`, `state` (CSRF protection)
  2. User authenticates at the AS and grants consent
  3. AS redirects user back to `redirect_uri` with an authorization `code`
  4. Client exchanges code for tokens via a **back-channel server-to-server POST** to the AS `/token` endpoint, including `client_secret`
  5. AS responds with `access_token`, optionally `refresh_token`, and optionally `id_token` (if OIDC)
  6. Client uses `access_token` (Bearer header) to call the Resource Server

- [ ] **PKCE Extension (Proof Key for Code Exchange):** Understand that PKCE replaces `client_secret` for public clients (mobile apps, SPAs) that cannot securely store secrets. A `code_verifier` is generated; its hash (`code_challenge`) is sent with the initial request; the verifier is sent at exchange time. This prevents authorization code interception attacks.

- [ ] **Common OAuth Flows (Awareness):**
  - **Client Credentials:** Machine-to-machine authentication; no user involvement; client authenticates with its own ID and secret
  - **Device Code:** For devices without a browser (Smart TVs, CLI tools); user authorizes on a secondary device — this flow is abused in Device Code phishing
  - **Implicit Flow (Deprecated):** Access token returned directly in URL fragment; do not use; tokens exposed in browser history and referrer headers

- [ ] **OAuth Scopes:** Understand that scopes limit what the access token can do (e.g., `read:email`, `offline_access`, `openid`). Understand that `offline_access` grants a refresh token (persistent access). Know that consent screens show scopes — and that users routinely ignore them.

- [ ] **State Parameter:** Understand that the `state` parameter is an anti-CSRF mechanism — the client generates it, the AS reflects it back, and the client verifies it matches before accepting the code. Missing or predictable `state` is exploitable.

---

<a id="auth-primer-stage-4-oidc"></a>

### **Stage 4: OpenID Connect (OIDC) — Federated Identity**

> [!TIP]
> **Goal:** Understand how OIDC extends OAuth 2.0 to provide authentication (identity), not just authorization.

- [ ] **OIDC vs OAuth 2.0:** Understand the critical distinction:
  - **OAuth 2.0** answers: _"Can this application access this resource on your behalf?"_ — it is about authorization
  - **OIDC** answers: _"Who is this user?"_ — it adds an authentication layer on top of OAuth 2.0
  - OIDC adds the `openid` scope, the **ID Token** (a JWT containing user identity claims), and the `/userinfo` endpoint

- [ ] **ID Token Claims:** Know the standard OIDC claims in the ID token:
  - `sub` — subject identifier (user's unique ID at the IdP)
  - `iss` — issuer (the Identity Provider's URL)
  - `aud` — audience (the client_id of the requesting application)
  - `exp` — expiration time
  - `iat` — issued at time
  - `nonce` — replay attack protection (client-generated, validated by client after receiving token)

- [ ] **Identity Provider (IdP) Discovery:** Understand the `/.well-known/openid-configuration` endpoint — a JSON document advertising all AS endpoints, supported algorithms, and public keys (JWKS URI). This is the first target in an OIDC reconnaissance.

- [ ] **Single Sign-On (SSO) Model:** Understand that OIDC enables SSO — a user authenticates once at the IdP (e.g., Azure AD, Google, Okta) and can access multiple applications (relying parties) without re-entering credentials. Understand how session management at the IdP level works (IdP session vs application session).

- [ ] **SAML vs OIDC:** Know that SAML (Security Assertion Markup Language) is the older XML-based SSO standard used in enterprise environments (Okta, ADFS). OIDC is the modern JSON/REST equivalent. Both are SSO protocols. Both are abused in different ways (SAML Response forgery vs JWT attacks).

---

<a id="auth-primer-stage-5-api-auth-patterns"></a>

### **Stage 5: API Authentication Patterns**

> [!TIP]
> **Goal:** Identify how different API authentication mechanisms work and where each fails.

- [ ] **API Keys:** Random strings passed in headers (`X-API-Key: ...`) or query parameters. Understand that API keys are **not user-authenticated** — they authenticate the application, not the person. Understand risks: keys embedded in client-side JS, mobile app binaries, or public Git repositories.

- [ ] **Basic Authentication:** Base64-encoded `username:password` in the `Authorization: Basic ...` header. Understand that Base64 is not encryption — the credentials are trivially decoded. Only safe over TLS. Legacy — avoid in modern APIs.

- [ ] **Bearer Tokens:** Tokens (JWTs or opaque) passed in `Authorization: Bearer <token>`. The server trusts whoever holds the token — no additional proof of identity required. Understand the implication: a stolen Bearer token is as good as the user's credentials for its lifetime.

- [ ] **mTLS (Mutual TLS):** Client presents a certificate alongside the standard TLS handshake. The server validates the client certificate. Used in service-to-service APIs where both parties must prove identity. High-security, complex to operate.

- [ ] **Service Account Keys vs OIDC Workload Identity:** Understand that cloud service accounts can authenticate via static key files (risky — key can be stolen from disk, memory, or source) or via workload identity federation (ephemeral tokens, no long-lived secrets). Understand why static service account keys are a critical finding in cloud security assessments.

---

<a id="auth-primer-stage-6-mfa-types"></a>

### **Stage 6: Multi-Factor Authentication (MFA) Types & Weaknesses**

> [!TIP]
> **Goal:** Understand MFA mechanisms and their security properties before encountering MFA bypass attacks.

- [ ] **MFA Factors:** Understand the three categories:
  - **Something you know:** Password, PIN, security question
  - **Something you have:** TOTP app (Authenticator), hardware key (YubiKey, FIDO2), SMS OTP, email OTP
  - **Something you are:** Biometrics (fingerprint, FaceID, iris scan)

- [ ] **TOTP (Time-Based One-Time Password):** Understand RFC 6238 — a shared secret + current 30-second time window is hashed (HMAC-SHA1) to generate a 6-digit code. Know that TOTP codes are **phishable** — an attacker can relay them in real time (AiTM attack). Know that TOTP is defeated by phishing proxies like Evilginx2/Modlishka.

- [ ] **FIDO2 / WebAuthn / Passkeys:** Understand that hardware keys and passkeys are **phishing-resistant** — they cryptographically bind the credential to the origin domain. An attacker who proxies the user to a fake domain cannot steal the FIDO2 assertion because the origin check fails. Understand why FIDO2/Passkeys are the only form of MFA that defeats AiTM phishing.

- [ ] **SMS OTP Weaknesses:** Understand that SMS is the weakest MFA:
  - SIM swapping — attacker social-engineers carrier into porting number
  - SS7 interception — telecom-level attack redirecting SMS
  - OTP phishing — user is tricked into reading the code to an attacker
  - Malware — SMS stealer apps on Android

- [ ] **MFA Fatigue (Push Bombing):** Understand that push-based MFA (Authenticator app showing Approve/Deny) is defeated by repeatedly sending push notifications until the user approves to stop the alerts. Mitigated by number matching (app asks user to match number from screen to push notification).

> [!NOTE]
> **Cross-Reference:** MFA bypass attacks (Evilginx2, push bombing, device code phishing) are covered in **Part 7 Stage 1** (System Hacking), **Part 8 Stage 6** (Cloud Weaponization), and **Part 23** (Entra ID MFA conditional access bypass). The mechanism explains above make those attack descriptions immediately actionable.

<a id="auth-primer-lab-progression"></a>

### **Lab Progression (Part 3B: Authentication Standards)**

| Level | Task                                                                                                                                                | Deliverable                                     |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| 1     | Decode a JWT from any login response using jwt.io — identify all claims and algorithm                                                               | Annotated JWT breakdown document                |
| 2     | Set up a local OAuth 2.0 lab using Keycloak — complete the Authorization Code flow and capture every HTTP exchange                                  | HTTP exchange log with step-by-step annotations |
| 3     | Configure a TOTP-enabled account; extract the TOTP secret; simulate OTP theft in a lab MFA relay scenario                                           | Lab notes documenting the attack surface        |
| 4     | Generate and examine an ID token — verify issuer, audience, expiry, and signature using the JWKS URI                                                | Validation script + analysis notes              |
| 5     | Build a local Flask API secured with JWT — intentionally break it three ways (alg:none, expired token accepted, weak HMAC secret) and document each | Broken API code + analysis report               |

> [!IMPORTANT]
> **Move-On Gate:** You can explain the difference between a session cookie, an opaque access token, and a JWT. You can trace the OAuth 2.0 Authorization Code flow step-by-step. You can decode a JWT and identify what is and is not protected. You can explain why FIDO2 defeats phishing but TOTP does not.

> [!TIP]
> **Next Step — Theory to Practice:** Part 3B is the concepts layer. **Part 4 Stage 2** is where you apply these concepts live: intercepting session cookies in Burp Suite, analyzing JWT security attributes, and testing cookie flags against OWASP Juice Shop. Complete Part 3B first, then Part 4 will feel like applying knowledge you already have rather than learning new material.

---

### 🏆 Phase 1 Capstone Project

**Build a Small Enterprise Lab and Document the Full Architecture**

Using your virtualization platform, build a lab environment containing:

- [ ] **1 Windows Server** (Domain Controller with Active Directory)
- [ ] **1 Linux Server** (web server or DNS server)
- [ ] **1 Windows Workstation** (domain-joined)
- [ ] **1 Kali Linux** attack machine
- [ ] **1 pfSense/OPNsense firewall** segmenting the network

**Deliverables:**

- [ ] Network topology diagram (draw.io/Excalidraw) showing all VMs, IPs, subnets, and firewall rules
- [ ] Build guide documenting every installation and configuration step (reproducible by someone else)
- [ ] Security baseline report: what services are running, what ports are open, what logging is enabled
- [ ] All documentation committed to your private Git repository

> [!IMPORTANT]
> **Capstone Gate:** Your lab must be fully operational, documented, and reproducible. A peer should be able to rebuild it from your guide alone.

---

### 🧭 Phase 1 Reflection & Competency Check

- [ ] **Reflection:** What foundational concept felt weakest: OS internals, Linux, Windows, networking, programming, or cryptography?
- [ ] **Reflection:** Which lab failure taught you the most, and how did you debug it?
- [ ] **Competency:** Can you rebuild the lab from documentation without relying on memory?
- [ ] **Competency:** Can you explain the network path, authentication flow, and logging sources in your lab?
- [ ] **Competency:** Can you troubleshoot a broken service using logs, packet captures, and command-line tools?

> [!IMPORTANT]
> **Phase Completion Gate:** Move to Phase 2 only when you can operate your lab independently, explain each major component, and produce professional notes for every configuration decision.

---

<a id="toc-part-4-footprinting-and-reconnaissance"></a>

<a id="part-3c-web-technology-fundamentals"></a>

## Part 3C: Web Technology Fundamentals

> [!IMPORTANT]
> **Why This Exists Here:** Phase 2 teaches session hijacking (Part 12), sniffing HTTP credentials (Part 9), and social engineering via web-based pretexting (Part 10) — all before Phase 4 introduces web applications. You cannot understand session hijacking without first understanding what a session IS. This Part bridges that gap. Complete it before proceeding to Phase 2.

> [!NOTE]
> **Prerequisite: Part 3B Required for Stage 2.** Part 4 Stage 2 (Cookies, Sessions & Tokens) applies the concepts taught in Part 3B (Authentication Standards Primer). If you skipped Part 3B, return to it before starting Stage 2 — the cookie security attributes, session fixation mechanics, and JWT structure will make no sense without that foundation. Part 3B is theory; Part 4 Stage 2 is the hands-on application of that theory in Burp Suite against live targets.

_Understand the web from the ground up — how browsers communicate with servers, how state is maintained, how identity is established, and where attackers look for weaknesses. This is the "what is being attacked" context that makes Phase 2 make sense._

> [!IMPORTANT]
> **⚡ Pre-Flight Checklist — Complete BEFORE Stage 1:**
> - [ ] Install **[Burp Suite Community Edition](https://portswigger.net/burp/communitydownload)** and configure your browser to proxy through `127.0.0.1:8080`. Intercept one HTTP request before reading any further.
> - [ ] Install **Docker** (`sudo apt install docker.io`) and run OWASP Juice Shop: `docker run -d -p 3000:3000 bkimminich/juice-shop`. Verify you can access `http://localhost:3000`.
> - [ ] Install the **Wappalyzer** browser extension (Firefox/Chrome) to fingerprint technology stacks on any site.
>
> These tools are not optional. Every lab in Part 3C requires Burp Suite. You are not learning concepts to describe them — you are learning to observe them in live traffic.

<a id="stage-1-http-the-protocol-of-the-web"></a>

### **Stage 1: HTTP — The Protocol of the Web**

> [!TIP]
> **Goal:** Understand every component of an HTTP request and response before you attempt to intercept or manipulate one.

- [ ] **HTTP Request Anatomy:** Understand the structure of an HTTP request — **request line (method, URI, HTTP version)**, **headers (Host, User-Agent, Content-Type, Authorization, Cookie)**, and **body** (for POST/PUT). Know that HTTP is a **stateless, text-based, application-layer protocol** running over TCP (port 80) or TLS (port 443).

- [ ] **HTTP Methods:** Know the semantic purpose and security implications of each method:
  - **GET** — retrieves data; parameters visible in URL; should have no side effects
  - **POST** — submits data; body-encoded; creates resources or triggers actions
  - **PUT / PATCH / DELETE** — update/modify/remove resources; require proper authorization controls
  - **OPTIONS** — reveals allowed methods (CORS pre-flight); reveals server capabilities
  - **HEAD** — identical to GET but returns only headers (useful for reconnaissance)

- [ ] **HTTP Status Codes:** Learn the security-relevant status codes:
  - `200 OK`, `201 Created`, `204 No Content` — success states
  - `301/302 Redirect` — redirect chains (relevant to open redirect attacks)
  - `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found` — access control indicators
  - `500 Internal Server Error` — error disclosure (stack traces, paths, tech stack)

- [ ] **HTTPS and TLS:** Understand that HTTPS = HTTP over TLS. Know that TLS provides **confidentiality (encryption), integrity (MAC), and authentication (certificates)**. Understand that HTTPS does NOT prevent XSS, SQLi, CSRF, or business logic flaws — it only protects data in transit.

- [ ] **HTTP Headers as Attack Surface:** Understand security-relevant headers:
  - **Host header injection** — attacker-controlled host header can redirect password reset links
  - **X-Forwarded-For** — used for IP tracking; easily spoofed
  - **Referer** — leaks navigation history; can expose sensitive URLs
  - **Content-Type** — server trust in declared MIME type leads to content sniffing attacks

- [ ] **HTTP/2 and HTTP/3 Awareness:** Know that HTTP/2 uses multiplexed binary frames over TCP, and HTTP/3 uses QUIC (UDP-based). Understand that these changes affect how tools intercept traffic and that older exploitation techniques may behave differently.

---

<a id="stage-2-cookies-sessions-tokens"></a>

### **Stage 2: Cookies, Sessions & Tokens**

> [!TIP]
> **Goal:** Understand how web applications maintain state — because this is exactly what session hijacking attacks target.

- [ ] **The Statelessness Problem:** Understand that HTTP is inherently stateless — each request is independent. Web applications use cookies, sessions, or tokens to "remember" authenticated users across requests.

- [ ] **Cookies:**
  - A cookie is a **key-value pair** set by the server via the `Set-Cookie` header, stored in the browser, and automatically sent back in every subsequent request via the `Cookie` header
  - **Cookie Attributes** (critical for security):
    - `Secure` — cookie only transmitted over HTTPS; prevents cleartext interception
    - `HttpOnly` — cookie not accessible from JavaScript; prevents XSS-based theft
    - `SameSite=Strict/Lax/None` — controls cross-site sending; prevents CSRF
    - `Domain` and `Path` — scoping controls for which requests the cookie accompanies
    - `Expires/Max-Age` — persistence duration

- [ ] **Session Management:** Understand the server-side session model:
  1. User authenticates; server creates a **session record** (stored in memory, database, or Redis)
  2. Server sends a **session ID cookie** (random, unpredictable value) to the browser
  3. Browser sends session ID with every request; server looks up the session record
  4. **Attacker goal:** steal or predict the session ID to impersonate the user (session hijacking)

- [ ] **Session ID Security Requirements:** A secure session ID must be:
  - **Cryptographically random** — not predictable from sequence numbers or timestamps
  - **Sufficiently long** — at least 128 bits of entropy
  - **Transmitted only over HTTPS** (Secure flag)
  - **Inaccessible to JavaScript** (HttpOnly flag)
  - **Invalidated on logout** — server must destroy the session record

- [ ] **JSON Web Tokens (JWTs):** Understand the stateless alternative to sessions:
  - JWT = **Header.Payload.Signature** (Base64url-encoded, dot-separated)
  - The **payload** contains **claims** (user ID, roles, expiry time) — readable by anyone
  - The **signature** proves the token was issued by the server (using HMAC-SHA256 or RSA)
  - **Security flaws:** `alg: none` attack (server accepts unsigned tokens), weak secret keys, missing expiry validation, sensitive data in payload (readable in cleartext)

- [ ] **Token Storage Trade-offs:** Understand where tokens/sessions can be stored and the implications:
  - `localStorage` / `sessionStorage` — accessible to JavaScript → vulnerable to XSS
  - `HttpOnly cookies` — not accessible to JavaScript → XSS-safe, but CSRF risk
  - **Best practice:** HttpOnly + SameSite cookies for session storage

---

<a id="stage-3-same-origin-policy-cors-web-security-headers"></a>

### **Stage 3: Same-Origin Policy, CORS & Web Security Headers**

> [!TIP]
> **Goal:** Understand the browser's core security boundary — and why attackers work so hard to bypass it.

- [ ] **Same-Origin Policy (SOP):** The SOP is the browser's foundational security boundary. It prevents JavaScript from one origin reading responses from a different origin. An **origin** is defined as: `scheme + hostname + port` (e.g., `https://example.com:443`). Any difference = different origin.
  - SOP **allows** cross-origin _requests_ to be sent (e.g., forms, image loads)
  - SOP **blocks** JavaScript from _reading_ cross-origin responses
  - **Impact:** Without SOP, a malicious site could read your banking portal's response using your session cookie

- [ ] **Cross-Origin Resource Sharing (CORS):** CORS is a server-side mechanism that **relaxes SOP** for specific trusted origins. Understand:
  - `Access-Control-Allow-Origin: https://trusted.com` — explicitly permits a specific origin
  - `Access-Control-Allow-Origin: *` — permits any origin (dangerous with credentials)
  - `Access-Control-Allow-Credentials: true` — must NOT be combined with wildcard origin
  - **Pre-flight requests** — browser sends `OPTIONS` first for non-simple requests to check CORS policy
  - **Misconfiguration:** Reflecting the `Origin` header without validation, or trusting `null` origin

- [ ] **Security Response Headers:** Know what each header does and how its absence creates vulnerabilities:

  | Header                             | Purpose                             | Missing = Risk               |
  | ---------------------------------- | ----------------------------------- | ---------------------------- |
  | `Content-Security-Policy (CSP)`    | Restricts which scripts can execute | XSS attacks succeed          |
  | `X-Frame-Options: DENY`            | Prevents iframe embedding           | Clickjacking attacks         |
  | `Strict-Transport-Security (HSTS)` | Forces HTTPS                        | SSL stripping MITM           |
  | `X-Content-Type-Options: nosniff`  | Prevents MIME sniffing              | Content injection            |
  | `Referrer-Policy`                  | Controls Referer header leakage     | URL parameter leakage        |
  | `Permissions-Policy`               | Restricts browser API access        | Fingerprinting, camera abuse |

- [ ] **CSP Deep-Dive:** Content Security Policy is the most powerful XSS defense available. Know:
  - `default-src 'self'` — only load resources from same origin
  - `script-src 'nonce-xyz'` — only execute scripts with a specific nonce value
  - `unsafe-inline` and `unsafe-eval` — dangerous directives that weaken CSP significantly
  - CSP bypass techniques: JSONP callbacks, open redirects, trusted CDN abuse

---

<a id="stage-4-web-authentication-patterns"></a>

### **Stage 4: Web Authentication Patterns**

> [!TIP]
> **Goal:** Know how web applications prove identity — attackers break authentication by understanding exactly how these mechanisms work.

- [ ] **HTTP Basic Authentication:** Username:password encoded in Base64, sent in `Authorization: Basic` header. No encryption by default — completely insecure without HTTPS. Server validates against stored credentials.

- [ ] **Form-Based Authentication (Username + Password):** The dominant web pattern:
  1. User submits credentials via HTML form (POST request)
  2. Server validates credentials against database (bcrypt/scrypt/Argon2 hash comparison)
  3. Server creates session, sets session cookie
  4. All subsequent requests authenticated via session cookie
  - Attack vectors: password spraying, credential stuffing, SQL injection in login form, session fixation, timing attacks on hash comparison

- [ ] **Multi-Factor Authentication (MFA):** Know the three factor categories — something you **know** (password), something you **have** (TOTP app, SMS, hardware key), something you **are** (biometrics). Know that SMS-based MFA is vulnerable to SIM swapping. Understand TOTP (Time-based One-Time Password) — HMAC of shared secret + timestamp truncated to 6 digits.

- [ ] **OAuth 2.0 Flow Awareness (Foundational):** OAuth 2.0 Authorization Code Flow is covered in full depth in **Part 3B Stage 3: OAuth 2.0 — Delegated Authorization**. Review it before proceeding to Phase 4 API Security (Part 19) where it is exploited.

- [ ] **API Keys & Bearer Tokens:** Used in API authentication. Sent in `Authorization: Bearer <token>` header or as URL parameters. Key risks: hardcoded in source code, committed to Git repositories, logged in access logs, transmitted in URL (logged by proxies).

- [ ] **Password Storage (Server Side):** bcrypt, scrypt, and Argon2id password hashing — including salt, work factor, and rainbow table resistance — are covered in full in **Part 3 Stage 4: Data at Rest & Password Security**. Review that section for the complete treatment.

---

<a id="stage-5-rest-apis-json-modern-web-architecture"></a>

### **Stage 5: REST APIs, JSON & Modern Web Architecture**

> [!TIP]
> **Goal:** Understand the modern web architecture that most applications are built on — critical for Phase 2 enumeration and Phase 4 API security.

- [ ] **REST API Principles:** Representational State Transfer uses standard HTTP methods to perform CRUD operations on resources. Resources are identified by URLs. REST APIs are stateless — each request must contain full authentication context. Understand:
  - `GET /api/users/42` — retrieve user 42
  - `POST /api/users` — create a new user
  - `PUT /api/users/42` — replace user 42 entirely
  - `PATCH /api/users/42` — update specific fields of user 42
  - `DELETE /api/users/42` — delete user 42

- [ ] **JSON Structure:** JSON (JavaScript Object Notation) is the dominant data format for APIs. Know:
  - Objects: `{"key": "value", "number": 42, "bool": true}`
  - Arrays: `["item1", "item2", {"nested": "object"}]`
  - Null values, nesting, and data types (string, number, boolean, null, array, object)
  - Security relevance: JSON injection, prototype pollution, type confusion attacks

- [ ] **API Versioning & Endpoints:** APIs use versioning (`/api/v1/`, `/api/v2/`) — older versions may have weaker controls. Understand that endpoint enumeration (discovering hidden API paths) is a core Phase 2 recon technique.

- [ ] **Content Negotiation:** APIs declare content types via `Content-Type` and `Accept` headers. A server may respond differently to `application/json` vs `text/html` requests — useful for recon and for bypassing input validation that only applies to web form submissions.

- [ ] **Modern Web Architecture Patterns:**
  - **Single Page Applications (SPAs):** React/Vue/Angular apps that handle routing client-side. Authentication uses tokens (JWTs) stored in localStorage or cookies.
  - **Microservices:** Applications split into small services communicating via internal APIs — internal APIs may have weaker authentication than external-facing ones
  - **API Gateways:** Proxy all external API traffic — rate limiting, authentication, and input validation applied here. Bypass = directly targeting internal service endpoints

- [ ] **Proxy Tools Awareness:** Understand that tools like **Burp Suite** and **OWASP ZAP** act as HTTP proxies sitting between your browser and the web server, capturing and allowing modification of every request and response. This is the primary tool for Phase 4 web security work.

---

<a id="lab-progression-web-technology-fundamentals"></a>

### **Lab Progression (Part 3C: Web Technology Fundamentals)**

> [!TIP]
> **Goal:** Build practical web layer familiarity before any offensive work begins.

| Level | Task                                                                                                                                                                                        | Deliverable                                                |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| 1     | Install Burp Suite Community; configure browser proxy; capture 10 different HTTP requests from real websites and annotate each request/response with method, headers, status code, and body | Annotated HTTP capture log in Markdown                     |
| 2     | Using Burp Repeater, manually modify a cookie value and observe the server response; replay a GET request as a POST and document the difference                                             | Lab notes with screenshots showing request modification    |
| 3     | Set up OWASP Juice Shop (Docker); use browser DevTools to inspect session cookies; identify HttpOnly/Secure/SameSite flags on each cookie; document what each flag's absence allows         | Cookie security analysis report                            |
| 4     | Write a Python script using the `requests` library that: logs into Juice Shop, captures the session cookie, and makes an authenticated API call to retrieve a resource                      | Working Python script committed to Git                     |
| 5     | Using Burp, capture a JWT from Juice Shop; decode the payload (base64); document what claims it contains; attempt the `alg: none` bypass and document whether it succeeds                   | JWT analysis notes with decoded payload and bypass attempt |

> [!IMPORTANT]
> **Move-On Gate (Part 3C):** You can explain the full HTTP request-response cycle, decode and analyze a session cookie, identify its security attributes, decode a JWT payload, and intercept/modify requests in Burp Suite. Only proceed to Phase 2 when you can explain WHY session hijacking works at the protocol level.

---

<a id="phase-1-mini-projects"></a>

## 🛠️ Phase 1 Mini Projects

> [!TIP]
> **Why these projects are here:** Phase 1 covers cryptography, password security, and authentication fundamentals. These 8 projects directly reinforce those concepts by building working tools rather than just reading about them. Each one maps to a specific Part in this phase — build them *after* completing the relevant Part, not before.

> [!NOTE]
> **How to use this section:** Each project lists the Phase 1 Part it belongs to, what prerequisite knowledge is needed, and what you should be able to explain after completing it. All code must be committed to your Git repository with a proper README covering: what the tool does, the vulnerability/concept it demonstrates, and how to run it.

---

### Project 1 — Password Strength Checker

**Maps to:** Part 3 (Cryptography) → Stage 4: Data at Rest & Password Security

**What it is:** A tool that analyzes a given password and scores it based on length, character diversity (uppercase, lowercase, digits, symbols), entropy, and presence in common password blacklists (e.g., `rockyou.txt` top 10,000).

**What you need before building it:**
- Understanding of password entropy (bits of entropy = log₂(character set size) × length)
- Knowledge of dictionary attacks and why common passwords are catastrophically weak
- Basic regex and string manipulation

**Why build it:**
It forces you to internalize the *math* behind password strength — not just "use 12 characters," but *why* that matters. The blacklist check introduces you to real-world breach datasets that attackers use. This is the minimum viable "I understand the human layer of security" project.

**Deliverable:** Python CLI tool — input a password, output a strength score with detailed reasoning. README must explain what entropy is and what `rockyou.txt` is.

---

### Project 2 — Password Generator

**Maps to:** Part 3 (Cryptography) → Stage 4: Data at Rest & Password Security

**What it is:** A configurable password generator that produces cryptographically random passwords based on user-specified length, character set requirements, and optionally checks the output against common-password lists.

**What you need before building it:**
- Know the difference between `random` (pseudorandom, seedable, predictable) and `secrets` (CSPRNG — cryptographically secure pseudorandom number generator)
- Understand character set composition (pool size determines entropy)
- Have completed Project 1 (Password Strength Checker) — use it to validate your generator's output

**Why build it:**
This teaches the single most important distinction a security-aware developer must know: **never use `random` for anything security-sensitive**. `random` in Python is seeded from system time and is trivially predictable. `secrets` uses OS entropy sources. If you can't explain this in an interview, you cannot be trusted to write secure code.

**Deliverable:** Python CLI tool with flags for `--length`, `--symbols`, `--digits`, `--uppercase`. Must use `secrets.choice()` — not `random.choice()`. README must explain why.

---

### Project 3 — Caesar Cipher Encryption Tool

**Maps to:** Part 3 (Cryptography) → Stage 1: Core Concepts & Algorithms

**What it is:** An implementation of the Caesar cipher (a shift substitution cipher) that encrypts and decrypts text, and includes a brute-force cracker that demonstrates why 26 possible keys provides zero real security.

**What you need before building it:**
- Modular arithmetic (`(char + shift) % 26`)
- Understanding of substitution ciphers vs transposition ciphers
- Frequency analysis concept (English letter frequency: E, T, A, O, I, N...)

**Why build it:**
Caesar cipher is *intentionally broken* — that's the point. Building it and then cracking your own output via brute force (only 26 keys exist) makes the concept of *key space* visceral. Your README should explain why 26 possible keys is computationally trivial, what frequency analysis is, and why modern ciphers (AES) have key spaces of 2¹²⁸ or 2²⁵⁶. This project tells a story that leads directly into Project 4.

**Deliverable:** Python CLI that encrypts, decrypts, and brute-forces Caesar-encrypted text. README must document the brute-force output and explain why this cipher fails.

---

### Project 4 — AES File Encryptor

**Maps to:** Part 3 (Cryptography) → Stage 1: Core Concepts & Algorithms + Stage 4: Data at Rest

**What it is:** A tool that encrypts and decrypts files using AES-256 in GCM mode. Takes a user-supplied password, derives an AES key using PBKDF2 (or Argon2), generates a random IV, encrypts the file, and stores the IV + salt + ciphertext together. Decryption reverses the process and validates the GCM authentication tag.

**What you need before building it:**
- Understand symmetric encryption: same key encrypts and decrypts
- Know why you must **never** use raw passwords as keys — always derive via PBKDF2/scrypt/Argon2
- Understand what an IV (Initialization Vector) is and why reusing it is catastrophic
- Know the difference between AES-CBC (no authentication) and AES-GCM (authenticated encryption)
- Library: `cryptography` (Python) — **not** `pycrypto` or `pycryptodome`, which have known issues

**Why build it:**
AES-GCM is the standard for symmetric encryption in TLS 1.3, disk encryption, and secure messaging. Building this yourself forces you to encounter every common implementation mistake — ECB mode, reused IVs, raw passwords as keys, no integrity check — and understand *why* each one is a real CVE. The GCM authentication tag also introduces you to authenticated encryption, which is non-negotiable in production systems.

**Deliverable:** Python CLI — `encrypt <file> --password <pass>` and `decrypt <file.enc> --password <pass>`. The encrypted file must contain: salt (16B) + IV (12B) + ciphertext + GCM tag. README must explain what happens if the IV is reused (hint: complete plaintext recovery is possible).

---

### Project 5 — RSA Key Pair Generator

**Maps to:** Part 3 (Cryptography) → Stage 2: Secure Communication + Stage 3: Identity & Trust (PKI)

**What it is:** A tool that generates RSA-2048 or RSA-4096 public/private key pairs, exports them in PEM format, demonstrates signing a message with the private key and verifying it with the public key, and optionally demonstrates encrypting a small payload with the public key and decrypting with the private key.

**What you need before building it:**
- Conceptual understanding of asymmetric cryptography: public key is shareable, private key is secret
- Why RSA key size matters: RSA-512 was broken in 1999, RSA-1024 is considered deprecated, RSA-2048 is the current minimum
- Understand what PEM format is (base64-encoded DER with `-----BEGIN...-----` headers)
- Library: `cryptography` (Python) — use `rsa.generate_private_key()` with proper padding (OAEP for encryption, PSS for signing)

**Why build it:**
RSA is the foundation of TLS certificates, SSH keys, code signing, and JWT RS256 tokens. Without building this, TLS handshakes and SSH authentication are black boxes. This project also introduces you to *why* RSA is only used for small payloads (key exchange) and not bulk encryption — it's computationally expensive. That asymmetry explains why hybrid encryption (Project 6) is universally used.

**Deliverable:** Python CLI that generates a key pair, saves `private.pem` and `public.pem`, signs a test message, and verifies the signature. README must explain what happens if you lose the private key and why you should never share it.

---

### Project 6 — File Encryption & Decryption Tool (Hybrid)

**Maps to:** Part 3 (Cryptography) → Stage 2: Secure Communication (Capstone of the crypto section)

**What it is:** A hybrid encryption tool — uses RSA (Project 5) to encrypt a randomly generated AES key, and uses AES-GCM (Project 4) to encrypt the actual file. The encrypted output contains: RSA-encrypted AES key + AES IV + AES-GCM ciphertext. Decryption uses the RSA private key to recover the AES key, then decrypts the file.

**What you need before building it:**
- Both Project 4 (AES File Encryptor) and Project 5 (RSA Key Pair Generator) must be complete
- Understand *why* hybrid encryption exists: RSA can only encrypt data up to its key size minus padding (~214 bytes for RSA-2048 with OAEP) — it cannot encrypt large files directly
- Know that this is exactly how TLS works: RSA/ECDH negotiates a session key, AES/ChaCha20 encrypts the actual traffic

**Why build it:**
This is the capstone of all Phase 1 crypto projects. It mirrors the architecture of TLS, PGP, and Signal. If you can implement and explain hybrid encryption from scratch, you can reason about any secure communication protocol. In an interview, being able to say "I built a tool that works like TLS at the crypto layer" and then *explain it correctly* puts you in a different tier from candidates who just read about it.

**Deliverable:** Python CLI with `encrypt <file> --pubkey public.pem` and `decrypt <file.enc> --privkey private.pem`. README must contain a diagram showing the hybrid model: `AES_key → RSA_encrypt(pubkey) → stored; File → AES_GCM(AES_key) → stored`.

---

### Project 7 — Password Manager

**Maps to:** Part 3B (Authentication Standards Primer) → Stage 1: Session-Based Authentication + Part 3 Stage 4: Data at Rest

**What it is:** A local CLI password manager that stores encrypted credentials (service, username, password) using AES-256-GCM, with a master password that is hashed using Argon2 and never stored in plaintext. Supports add, retrieve, list, and delete operations. The vault is a single encrypted file.

**What you need before building it:**
- Project 4 (AES File Encryptor) completed — the vault storage mechanism is the same principle
- Understanding of *slow* hashing algorithms: Argon2 (winner of the Password Hashing Competition), bcrypt — these are intentionally slow to resist brute force. SHA-256 for password hashing is **catastrophically wrong** — document why
- Key stretching: how to derive a strong AES key from a weak master password using Argon2 + salt
- Session locking: clear decrypted passwords from memory after timeout

**Why build it:**
A password manager is one of the highest-impact security tools in daily use, and building one forces you to confront every bad password storage decision that real applications make. The core insight: you must use a *slow* KDF (Argon2/bcrypt) for the master password, not SHA-256. This is the same reason why database breaches of bcrypt-hashed passwords are recoverable only slowly, while SHA-256-hashed breaches are cracked in hours with a GPU. This knowledge transfers directly to secure backend development.

**Deliverable:** Python CLI with commands: `add`, `get`, `list`, `delete`, `lock`. Vault stored as an encrypted JSON file. README must explain *why* Argon2 is used instead of SHA-256 with a concrete timing comparison.

---

### Project 8 — Login System with Multi-Factor Authentication (TOTP)

**Maps to:** Part 3B (Authentication Standards Primer) → Stage 6: MFA Types & Weaknesses

**What it is:** A functional login system (CLI or basic web) that implements: user registration with Argon2-hashed password storage, login with password verification (constant-time comparison), TOTP-based 2FA using RFC 6238 (the same standard as Google Authenticator), session token generation (JWT or UUID token), rate limiting after failed attempts, and account lockout.

**What you need before building it:**
- Part 3B fully completed — you need to understand sessions, tokens, and MFA types before building this
- TOTP standard (RFC 6238): a TOTP code = HOTP(secret, floor(unix_time / 30)) — time-divided into 30-second windows, HMAC-SHA1 truncated to 6 digits
- Libraries: `pyotp` (Python) for TOTP generation/verification
- Constant-time string comparison (`hmac.compare_digest()`) — prevents timing attacks on password verification
- JWT structure (header.payload.signature) if using token-based sessions

**Why build it:**
Authentication is the #1 attack surface in web applications. Building it yourself — rather than using an off-the-shelf library blindly — forces you to understand *why* certain implementation choices exist: why `==` comparison leaks timing information, why TOTP codes expire every 30 seconds, why rate limiting must happen *before* password hashing (not after), and why session tokens must be unpredictable. Every web application developer should be able to implement this, and every security engineer must be able to audit it.

**Deliverable:** Python application with working user registration, login with TOTP, and session management. Include a QR code output (using `qrcode` library) that can be scanned into Google Authenticator. README must explain what a timing attack is and how `hmac.compare_digest()` prevents it.

---

> [!IMPORTANT]
> **Phase 1 Project Completion Gate:** You should be able to explain the cryptographic choices in every project above without looking at the code. If someone asks "why Argon2 and not SHA-256?" or "why AES-GCM and not AES-CBC?" or "why CSPRNG and not random?" — you must answer from understanding, not memory. If you cannot, revisit the relevant Part before moving to Phase 2.
