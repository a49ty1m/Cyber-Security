# Phase 1: The Unshakeable Foundation

---

### 🧭 Navigation
🏠 [Master Roadmap](README.md) | [Phase 2](Phase-2.md) ➔

---

> [!NOTE]
> **Phase Overview**
> - **⏱️ Time Commitment (Full-Time):** 3–4 months
> - **⏱️ Time Commitment (Part-Time):** 6–8 months
> - **🎯 Primary Focus:** Master the TCP/IP stack, OSI model, DNS, HTTP/HTTPS, Linux CLI and administration, Windows administration and Event Viewer, Bash/PowerShell, Python/JavaScript, virtualization, cloud basics (AWS/Azure), Docker/Kubernetes, authentication, sessions, cookies, JSON APIs, CORS, and the cryptographic primitives underpinning all of security.

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
  - [Stage 7: Programming & Scripting Fundamentals](#stage-7-programming-scripting-fundamentals)
- [Part 1B: Linux Administration](#part-1b-linux-administration)
  - [Stage 1: User & Access Management](#stage-1-user-access-management)
  - [Stage 2: Service & Process Management](#stage-2-service-process-management)
  - [Stage 3: Networking](#stage-3-networking)
  - [Stage 4: Log Analysis & Monitoring](#stage-4-log-analysis-monitoring)
  - [Stage 5: Storage & Filesystem](#stage-5-storage-filesystem)
  - [Stage 6: Security Hardening](#stage-6-security-hardening)
  - [Lab Progression](#lab-progression)
- [Part 1C: Windows Administration](#part-1c-windows-administration)
  - [Stage 1: User & Access Management](#stage-1-user-access-management)
  - [Stage 2: System Management](#stage-2-system-management)
  - [Stage 3: Event Viewer & Auditing](#stage-3-event-viewer-auditing)
  - [Stage 4: PowerShell Administration](#stage-4-powershell-administration)
  - [Stage 5: Active Directory Concepts (Prerequisite for Part 23)](#stage-5-active-directory-concepts-prerequisite-for-part-23)
  - [Lab Progression](#lab-progression)
  - [macOS Security Awareness (Supplemental)](#macos-security-awareness-supplemental)
- [Part 2: Networking Fundamentals](#part-2-networking-fundamentals)
  - [Layer 1: Physical (The Hardware Surface)](#layer-1-physical-the-hardware-surface)
  - [Layer 2: Data Link (The Local Target)](#layer-2-data-link-the-local-target)
  - [Layer 3: Network (The Routing Logic)](#layer-3-network-the-routing-logic)
  - [Layer 4: Transport (The Reliability Layer)](#layer-4-transport-the-reliability-layer)
  - [Layers 5-7: Application & Session (The Payload)](#layers-5-7-application-session-the-payload)
  - [Lab Progression & Professional Development (2026 Red Team Focus)](#lab-progression-professional-development-2026-red-team-focus)
  - [Automation & Programmability](#automation-programmability)
- [Part 3: Cryptography](#part-3-cryptography)
  - [Stage 1: Core Concepts & Algorithms](#stage-1-core-concepts-algorithms)
  - [Stage 2: Secure Communication (Data in Transit)](#stage-2-secure-communication-data-in-transit)
  - [Stage 3: Identity & Trust (PKI)](#stage-3-identity-trust-pki)
  - [Stage 4: Data at Rest & Password Security](#stage-4-data-at-rest-password-security)
  - [Stage 5: Cryptographic Attacks & Weaknesses](#stage-5-cryptographic-attacks-weaknesses)
  - [Lab Progression](#lab-progression)

---

## Career Foundation & Lab Setup

_Before starting the technical curriculum, establish your academic foundation, lab environment, and practice platforms._

### **Professional Development & Enablers**

- [ ] **Lab Progression Map (Packet Tracer → GNS3/EVE-NG → Wireshark validation)**
  - **Goal:** : Move from simple networking practice to realistic, packet-level practice without guessing.
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
  - **Goal:** : Avoid being locked into one platform. Labs should migrate.
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
  - **Goal:** : Learn cloud networking the way defenders and attackers reason about it.
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
  - **Goal:** : Your time should go to learning—not clicking the same steps.
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
  - **Goal:** : Become fluent in “visibility.” What logging exists, what it misses, and why.
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
  - **Goal:** : Use structured certification objectives to avoid missing basics.
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
  - **Goal:** : Make your practice safe and accountable.
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
  - **Goal:** : Prepare for high-volume tasks you’ll face in real workflows.
  - What to scale:
    - Mass config deployment across many lab nodes
    - Port scan sweeps to baseline services
    - Faster feedback loops
  - Good practice:
    - Use rate limiting.
    - Use concurrency controls.
    - Store scan results as structured output (JSON/CSV) so you can diff runs.

- [ ] **Monitoring Deep Dives (SNMP/NetFlow to visualize exfil patterns)**
  - **Goal:** : Practice detection at the “pattern” level, not just “did the packets work?”
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

### **Home Lab Hardware Requirements**

> [!TIP]
> **Goal:** : Avoid wasting money on inadequate hardware or overspending before you know your specialization.

- [ ] **Minimum Specs:** **32GB RAM** (16GB absolute minimum for running 2–3 VMs simultaneously), **quad-core CPU with VT-x/AMD-V** (Intel VT or AMD-V required for nested virtualization), **500GB+ SSD**. Without hardware virtualization support, nested VMs (VMs inside VMs) will not work.

- [ ] **Recommended Specs:** **64GB RAM, 8-core CPU, 1TB NVMe SSD**. This comfortably runs a Domain Controller + 3 workstations + attacker Kali VM simultaneously for AD labs (Part 23).

- [ ] **Wireless Testing Adapter:** Purchase an **Alfa AWUS036ACH** (or similar Realtek RTL8812AU/RTL8814AU chipset) USB adapter that supports **monitor mode and packet injection**. Built-in WiFi cards rarely support these modes. Required for Part 21 (Wireless Pentesting).

- [ ] **Budget Tiers:** **Tier 1 (~$300):** Used ThinkPad T480/X1 Carbon with 32GB RAM upgrade. **Tier 2 (~$600):** Refurbished Dell Precision/HP Z-series with 64GB. **Tier 3 (~$1,500):** Custom mini-ITX Proxmox server with 128GB RAM for persistent lab infrastructure.

- [ ] **Cloud Supplement:** Use **AWS Free Tier / Azure $200 credit / GCP $300 credit** for cloud security labs (Part 24) without maintaining local infrastructure. Set **billing alerts** to avoid surprise charges.

---

### **Academic & Career Alignment**

> [!TIP]
> **Goal:** : Maximize your formal education and align academic work with offensive security career requirements.

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
  - **Goal:** : differentiate from other graduates.

---

### **Certification Alignment Map**

> [!TIP]
> **Goal:** : Know which certifications to pursue at each phase for industry credibility.

| Phase Completed | Recommended Certifications | Notes |
|---|---|---|
| Phase 1 | **CompTIA A+, Network+, Security+** | Foundation validation; Security+ meets DoD 8570 baseline |
| Phase 2 | **eJPT (INE), CompTIA PenTest+** | Entry offensive validation |
| Phase 3 | **CySA+ (CompTIA), BTL1 (Security Blue Team)** | Blue team validation |
| Phases 1–4 | **eWPT (INE), BSCP (PortSwigger)** | Web security specialization |
| Phases 1–6 | **OSCP (OffSec), PNPT (TCM), CRTP (Altered Security)** | Mid-level offensive; OSCP is the gold standard |
| Phases 1–7 | **GCFE, GCFA (GIAC Forensics), eCRE (INE)** | DFIR / RE specialization |
| Phases 1–8 | **OSEP (OffSec), CRTO (Zero-Point), CISSP** | Senior offensive / architecture validation |
| Full Roadmap | **OSCE3, GXPN, SANS GSE** | Expert-level; pursue only 1–2 |

> ⚠️ **Certifications validate skills; they do not replace them.** Do not pursue certifications until you can pass them based on roadmap skills alone. Never cert-chase before building real capability.

---

### **Training Platforms & Lab Environments**

> [!TIP]
> **Goal:** : Build practical muscle memory through structured, hands-on hacking exercises.

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
  - **Goal:** : develop speed, creativity, and multi-domain problem solving under pressure.

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
  - **Goal:** : Earn the **Burp Suite Certified Practitioner (BSCP)** certification.

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

> [!TIP]
> **Goal:** : Prove readiness before touching serious offensive material.

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

> [!TIP]
> **Goal:** : Master the machine before the Operating System initializes.

- [ ] **CPU Operations:** Master the **Fetch-Decode-Execute** cycle to understand how code actually runs at the hardware level.

- [ ] **Registers:** Command the "steering wheel" of the CPU: **EAX/RAX** (accumulator), **ESP/RSP** (stack pointer), and **EIP/RIP** (instruction pointer).

- [ ] **Architecture Types:** Distinguish between **x86** (32-bit) and **x64** (64-bit) addressing and how they handle memory instructions differently.

- [ ] **Instruction Sets:** Develop a working familiarity with **Assembly** language (**MOV**, **PUSH**, **POP**, **CALL**, **JMP**).

- [ ] **The Boot Chain:** Master the sequence from **UEFI/Secure Boot** $\rightarrow$ **Bootloader** $\rightarrow$ **Kernel Load** $\rightarrow$ **Init/Systemd**.

- [ ] **Hardware I/O & DMA:** Understand how **Direct Memory Access (DMA)** allows peripherals to read/write system RAM by bypassing the CPU.

- [ ] **Storage Forensics:** Understand the physical data storage on **HDDs vs. SSDs** and why "deleting" is not "wiping" in a forensics context.

---

### **Stage 2: Operating System Internals**

> [!TIP]
> **Goal:** : Understand the resource manager and its internal logic.

- [ ] **Privilege Levels:** Master the **"Ring" architecture**; specifically the separation between **Ring 0** (Kernel) and **Ring 3** (User).

- [ ] **System Calls:** Trace syscall execution (e.g., **NtCreateFile** or **execve**) from user-space API calls through the Interrupt to the kernel handler.

- [ ] **Process & Thread Mechanics:** Understand the lifecycle of processes and threads, including scheduling and context switching.

- [ ] **Process Environment Block (PEB):** In Windows, master the **PEB structure** to find loaded DLLs or implement anti-debugging techniques.

- [ ] **Authorization & Tokens:** Master Windows **SIDs**, **Access Tokens**, and **Token Impersonation**; understand Linux **Namespaces** and **Cgroups** (the basis for containers).

- [ ] **File Systems (Linux):** Master the root directory structure, **Inodes**, and the **"Everything is a file"** philosophy.

- [ ] **File Systems (Windows):** Master **NTFS permissions**, **Registry hives**, and the usage of **Alternate Data Streams (ADS)** to hide payloads.

---

### **Stage 3: Memory Management**

> [!TIP]
> **Goal:** : Understand how memory is organized and managed.

- [ ] **Virtual Memory:** Learn how the OS maps physical RAM to virtual addresses to provide process isolation.

- [ ] **The Stack:** Master the **LIFO** (Last-In, First-Out) structure and the **Function Prologue/Epilogue** to understand how return addresses are stored.

- [ ] **The Heap:** Understand **dynamic memory allocation** and how applications request memory at runtime.

- [ ] **Segmentation & Paging:** Understand **segment descriptors** and **page tables** for virtual address translation.

- [ ] **Memory Protection:** Learn about **page permissions (R/W/X)** and **privilege level separation**.

---

### **Stage 4: Data Representation & Logic**

> [!TIP]
> **Goal:** : Master binary representation and Boolean logic fundamentals.

- [ ] **Number Systems:** Be able to convert between **Binary, Decimal, and Hexadecimal** mentally.

- [ ] **Boolean Logic:** Master **AND, OR, NOT, and XOR** (the foundation of encryption and obfuscation).

- [ ] **File Headers:** Identify file types (EXE, ELF, JPG) by their **"Magic Bytes"** instead of extensions.

---

### **Stage 5: Wireless & Physical Connections**

> [!TIP]
> **Goal:** : Understand wireless protocols and physical security infrastructure at a foundational level. Deep offensive techniques for each wireless protocol are covered in Part 21 (Wireless Pentesting, Phase 5).

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

### **Stage 6: Mobile Platform Awareness**

> [!TIP]
> **Goal:** : Know that mobile platforms have distinct architectures and security models. Hands-on mobile hacking is covered in Part 22 (Phase 5).

- [ ] **Android vs iOS Architecture:** Understand at a high level that **Android** (APK format, Linux kernel, sandboxing, SELinux) and **iOS** (IPA format, Mach-O binaries, Secure Enclave, code signing) have fundamentally different security models.

- [ ] **Mobile Security Concepts:** Know that **rooting/jailbreaking**, **certificate pinning**, **biometric authentication**, and **hardware-backed keystores** are key security mechanisms on mobile platforms.

> [!NOTE]
> **Cross-Reference:** Full mobile architecture details (APK/IPA structure, SELinux sandboxing, app permissions, Keychain/Keystore internals) and all exploitation techniques (Frida, SSL pinning bypass, runtime manipulation) are covered in **[Part 22: Mobile Platform Pentesting](file:///home/smilo/Desktop/MY_Folder/Cyber-Security/Roadmap.md#toc-part-22-mobile-platform-pentesting)** (Phase 5). Do not attempt until you have completed Phases 2–4.

---

### **Stage 7: Programming & Scripting Fundamentals**

> [!TIP]
> **Goal:** : Build the coding foundation required for security tooling. Core language skills are taught here; offensive development (shellcode, C2 implants, process injection, AMSI/ETW bypass) is covered in Part 42: Offensive Development & Tooling (Phase 7).

**Python (Automation & Scripting):**

- [ ] **Core Language:** Master **data types, control flow, functions, OOP, file I/O, exception handling**, and **virtual environments (venv/pip)**.

- [ ] **Security Libraries:** Learn **socket, requests, scapy, paramiko, beautifulsoup** for network interaction and scraping.

- [ ] **Automation Use Cases:** Script **port scanners, brute-forcers, web scrapers, log parsers**, and **API interaction tools**.

**JavaScript & Node.js (Web & API Security):**

- [ ] **Core Language:** Master **ES6+ syntax, async/await, Promises, closures, prototypal inheritance, DOM manipulation**, and **event-driven architecture**.

- [ ] **Node.js Runtime:** Understand **npm ecosystem, module system (CommonJS/ESM), Express.js**, and **server-side JavaScript** for building and auditing web applications.

- [ ] **Web Security Context:** Learn **DOM-based XSS, prototype pollution, client-side injection, postMessage abuse**, and **WebSocket security** — JavaScript is the language of the web attack surface.

- [ ] **AI Interface Relevance:** Understand that modern AI model interfaces (**ChatGPT, Gemini, Claude**) are delivered via **JavaScript web applications** — fluency is essential for auditing these frontends.

**C (System-Level Understanding):**

- [ ] **Core Language:** Master **pointers, memory allocation (malloc/free), structs, arrays, strings, bitwise operations**, and **compilation (gcc/clang)**.

- [ ] **System Programming:** Understand **syscalls, file descriptors, process creation (fork/exec), signal handling**, and **shared memory/IPC**.

- [ ] **Memory Understanding:** Understand **stack frame layout, buffer boundaries, heap allocation** at the C level — this forms the foundation for exploit development studied later in Part 29 (Modern Exploitation) and Part 42 (Offensive Development).

**C++ (Awareness Level):**

- [ ] **Core Language:** Understand **classes, templates, STL containers, smart pointers, RAII**, and how C++ extends C.

- [ ] **Reverse Engineering Context:** Learn to read **C++ compiled binaries** (vtables, name mangling, exception handling) during **static analysis with Ghidra/IDA** — studied in depth in Part 28.

**Bash & PowerShell (Operational Scripting):**

- [ ] **Bash Mastery:** Script **recon pipelines, log parsing, cron automation, SSH key management**, and **iptables/nftables rule generation** on Linux.

- [ ] **PowerShell Mastery:** Script **AD enumeration, WMI queries, registry operations, service management**, and **remote execution (Invoke-Command, Enter-PSSession)**.

- [ ] **Cross-Platform Scripting:** Use **Python or Bash** for Linux targets and **PowerShell or C#** for Windows targets; maintain fluency in both ecosystems.

> **📌 Cross-Reference:** Offensive programming is covered in dedicated Parts:
> - **Part 42: Offensive Development & Tooling** (Phase 7) — Exploit prototyping with pwntools, custom C2 implant logic, buffer overflow exploits, shellcode writing, Win32 API process injection, DLL loading, token manipulation, .NET offensive tooling (P/Invoke, D/Invoke, SharpHound, Rubeus), AMSI/ETW bypass, in-memory execution, offensive PowerShell (download cradles, constrained language mode escape).
> - **Part 29: Modern Exploitation** (Phase 7) — Advanced memory exploitation, kernel exploits, browser exploitation.
> - **Part 8: Malware & Weaponization** (Phase 2) — Document weaponization (VBA macros, DDE template abuse, OneNote/PDF weaponization), email client abuse, OAuth consent phishing, cloud persistence, data exfiltration, and covert channels.

---


<a id="toc-part-1b-linux-administration"></a>
## Part 1B: Linux Administration

_Phase 1 — Foundation | Prerequisite: Part 1 Stage 2 (OS Internals) | This module teaches the Linux administration skills required by the Foundation Proof Gate and used throughout every subsequent Phase._

### Stage 1: User & Access Management

- [ ] **User Accounts:** Create, modify, and delete users with **useradd/usermod/userdel**. Understand **/etc/passwd**, **/etc/shadow**, and **/etc/group** file structures.

- [ ] **Group Management:** Create groups, assign users to primary and supplementary groups, understand **newgrp** and group-based access control.

- [ ] **Password Policy:** Configure password aging with **chage**, set complexity requirements via **PAM (pam_pwquality)**, and understand **/etc/login.defs**.

- [ ] **Sudo Configuration:** Understand **/etc/sudoers** syntax, use **visudo**, configure per-user and per-group sudo rules, and understand **NOPASSWD** risks.

- [ ] **File Permissions:** Master **rwx**, **chmod** (symbolic and octal), **chown**, **chgrp**. Understand **SUID, SGID, sticky bit** and their security implications.

- [ ] **ACLs:** Configure **POSIX ACLs** with **getfacl/setfacl** for fine-grained access control beyond standard permissions.

### Stage 2: Service & Process Management

- [ ] **systemd:** Manage services with **systemctl** (start, stop, enable, disable, status, mask). Understand **unit files**, **targets**, and **dependencies**.

- [ ] **Process Management:** Use **ps, top, htop, kill, killall, nice, renice**. Understand **PID, PPID, process states, zombie processes**, and **signal handling**.

- [ ] **Cron & Timers:** Schedule tasks with **crontab** and **systemd timers**. Understand cron syntax, **/etc/cron.d/**, and security implications of cron jobs.

- [ ] **Package Management:** Install, update, and remove software with **apt (Debian/Ubuntu)** and **dnf/yum (RHEL/Fedora)**. Understand **repositories, GPG signing, and dependency resolution**.

- [ ] **Boot Process:** Understand **GRUB2 → systemd → target** boot sequence, **runlevels/targets**, and **single-user mode** for recovery.

### Stage 3: Networking

- [ ] **Network Configuration:** Configure interfaces with **ip addr, ip link, ip route**. Understand **DHCP vs. static**, **/etc/netplan/**, **/etc/network/interfaces**, and **NetworkManager (nmcli)**.

- [ ] **DNS Resolution:** Understand **/etc/resolv.conf**, **/etc/hosts**, **systemd-resolved**, and **dig/nslookup/host** for troubleshooting.

- [ ] **Socket Inspection:** Use **ss** and **netstat** to identify listening services, active connections, and process-socket bindings.

- [ ] **Firewall (iptables/nftables/ufw):** Configure basic packet filtering rules. Understand **chains (INPUT, OUTPUT, FORWARD)**, **default policies**, **stateful tracking**, and **logging**.

- [ ] **SSH Hardening:** Configure **/etc/ssh/sshd_config** — disable root login, enforce key-based auth, change default port, configure **fail2ban**, and understand **SSH tunneling (local, remote, dynamic)**.

### Stage 4: Log Analysis & Monitoring

- [ ] **journalctl:** Query systemd journal logs — filter by **unit, priority, time range, boot**. Understand **persistent vs. volatile** journaling.

- [ ] **Syslog:** Understand **/var/log/syslog**, **/var/log/auth.log**, **/var/log/kern.log**, **/var/log/secure**. Configure **rsyslog** for remote forwarding.

- [ ] **Log Rotation:** Configure **logrotate** to prevent disk exhaustion. Understand **rotation frequency, compression, retention policies**.

- [ ] **dmesg:** Read kernel ring buffer for **hardware errors, driver issues, and boot diagnostics**.

- [ ] **Monitoring Tools:** Use **uptime, free, df, du, iostat, vmstat** for system health monitoring. Understand when to investigate further.

### Stage 5: Storage & Filesystem

- [ ] **Disk Management:** Use **fdisk, parted, lsblk, blkid** to manage partitions. Understand **MBR vs. GPT**.

- [ ] **Filesystem Operations:** Create filesystems with **mkfs**, mount with **mount/fstab**, understand **ext4, XFS, Btrfs** differences.

- [ ] **LVM:** Create and manage **Physical Volumes, Volume Groups, Logical Volumes**. Extend and resize volumes without downtime.

- [ ] **Disk Encryption:** Encrypt partitions with **LUKS (cryptsetup)**. Understand **dm-crypt**, key slots, and unlock-at-boot configuration.

### Stage 6: Security Hardening

- [ ] **SELinux:** Understand **enforcing, permissive, disabled** modes. Use **getenforce, setenforce, sestatus**. Read **audit.log** denials and create custom policies with **audit2allow**.

- [ ] **AppArmor:** Understand **profiles, complain vs. enforce mode**. Use **aa-status, aa-genprof** for profile creation.

- [ ] **System Auditing:** Configure **auditd** rules to monitor file access, user commands, and privilege escalation. Use **ausearch** and **aureport**.

- [ ] **Kernel Hardening:** Understand **sysctl** parameters (**net.ipv4.ip_forward**, **kernel.randomize_va_space**, **fs.protected_hardlinks**) and how to persist them.

### Lab Progression

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Set up a fresh Ubuntu/Debian VM from ISO | Working VM with SSH access |
| 2 | Create 5 users with different group memberships and sudo rules | Screenshot of /etc/sudoers and group files |
| 3 | Configure SSH key-only auth + fail2ban | SSH hardening checklist document |
| 4 | Set up iptables/nftables firewall rules allowing only SSH, HTTP, HTTPS | Firewall ruleset export |
| 5 | Analyze auth.log to identify failed login patterns | 1-page log analysis report |
| 6 | Set up LVM, create/extend logical volumes | Screenshot of lvm commands and df output |
| 7 | Enable SELinux/AppArmor, troubleshoot a denied operation | Audit log analysis + policy fix document |

> [!IMPORTANT]
> **Move-On Gate:** You can create users, manage services, configure networking, read logs, and harden a Linux system from scratch without referring to documentation for basic commands.

---

<a id="toc-part-1c-windows-administration"></a>
## Part 1C: Windows Administration

_Phase 1 — Foundation | Prerequisite: Part 1 Stage 2 (OS Internals) | This module teaches Windows administration skills required by the Foundation Proof Gate and used throughout Active Directory (Part 23), cloud (Part 24), and defensive (Phase 3) modules._

### Stage 1: User & Access Management

- [ ] **Local Users & Groups:** Create and manage local accounts with **lusrmgr.msc** and **net user/net localgroup** commands. Understand **built-in accounts (Administrator, Guest, SYSTEM)**.

- [ ] **NTFS Permissions:** Configure **read, write, modify, full control** on files/folders. Understand **inheritance, explicit vs. inherited permissions**, and **effective permissions**.

- [ ] **Share Permissions:** Distinguish between **NTFS and share permissions**. Configure **SMB shares** and understand **Everyone vs. Authenticated Users** security implications.

- [ ] **User Account Control (UAC):** Understand **UAC prompts, integrity levels (low, medium, high, system)**, and how UAC affects administrative operations.

- [ ] **Local Security Policy:** Configure **password policy, account lockout policy, user rights assignments** via **secpol.msc** and **gpedit.msc**.

### Stage 2: System Management

- [ ] **Windows Services:** Manage services with **services.msc** and **sc.exe/Get-Service**. Understand **service accounts (LocalSystem, LocalService, NetworkService)**, startup types, and recovery options.

- [ ] **Registry:** Navigate **HKLM, HKCU, HKCR, HKU** hives. Understand **Run/RunOnce keys**, **service configurations**, and how malware uses the registry for persistence.

- [ ] **Task Scheduler:** Create and manage scheduled tasks. Understand **triggers, actions, conditions**, and security implications of tasks running as SYSTEM.

- [ ] **Windows Firewall:** Configure **inbound/outbound rules** with **Windows Defender Firewall with Advanced Security (wf.msc)** and **netsh**. Understand **profiles (Domain, Private, Public)**.

- [ ] **Windows Update:** Understand **WSUS, Windows Update for Business**, and **patch management** concepts. Know how to check update history and roll back problematic updates.

### Stage 3: Event Viewer & Auditing

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

### Stage 4: PowerShell Administration

- [ ] **Core Cmdlets:** Master **Get-Process, Get-Service, Get-EventLog, Get-WinEvent, Get-ChildItem, Get-Content, Set-Item, New-Item, Remove-Item, Test-NetConnection**.

- [ ] **Pipeline & Filtering:** Use **Where-Object, Select-Object, Sort-Object, Group-Object, Measure-Object, ForEach-Object, Export-Csv, ConvertTo-Json**.

- [ ] **Remote Management:** Configure and use **PowerShell Remoting (Enable-PSRemoting, Invoke-Command, Enter-PSSession, New-PSSession)**. Understand **WinRM** configuration and **double-hop** authentication issues.

- [ ] **WMI/CIM:** Query system information with **Get-CimInstance** (Win32_Process, Win32_Service, Win32_OperatingSystem). Understand WMI as both an administration and attack tool.

- [ ] **Active Directory Basics:** Use **RSAT tools** and **Active Directory PowerShell module** (Get-ADUser, Get-ADGroup, Get-ADComputer). Understand **OU structure, GPO basics, DNS integration with AD**.

### Stage 5: Active Directory Concepts _(Prerequisite for Part 23)_

- [ ] **AD Architecture:** Understand **domains, forests, trusts, OUs, sites**, and **replication**. Know the difference between a **domain controller** and a **member server**.

- [ ] **Group Policy Basics:** Create and link **GPOs**. Understand **computer vs. user configuration**, **gpupdate /force**, **rsop.msc**, and **GPO inheritance/blocking**.

- [ ] **DNS in AD:** Understand why **AD-integrated DNS** is critical. Know **SRV records (_ldap._tcp)**, **forward/reverse lookup zones**, and **dynamic DNS registration**.

- [ ] **DHCP in AD:** Understand **DHCP server authorization**, **scopes, reservations, options**, and how DHCP integrates with DNS.

### Lab Progression

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Install Windows Server 2022 in VM | Working VM with RDP access |
| 2 | Create local users, configure NTFS permissions on shared folder | Permission matrix document |
| 3 | Promote to Domain Controller, create OU structure with 10+ users | AD topology screenshot |
| 4 | Configure Group Policy (password policy, software restriction) | GPO summary document |
| 5 | Enable Advanced Audit Policy + Sysmon, generate logon events | Event log analysis (identify 4624, 4625, 4688 events) |
| 6 | Configure Windows Firewall rules via PowerShell | Exported firewall ruleset |
| 7 | Write PowerShell script to audit AD: list all admins, find stale accounts, export report | Working .ps1 script + CSV output |

> [!IMPORTANT]
> **Move-On Gate:** You can set up a Windows domain from scratch, create users/groups/GPOs, read Event Viewer logs to identify suspicious activity, and write basic PowerShell automation scripts without referring to documentation for core tasks.

---

### **macOS Security Awareness** _(Supplemental)_

> macOS endpoints are present in most enterprises, especially in development, design, and executive teams. This sidebar provides enough context to avoid a knowledge gap when encountering macOS in the field. Full macOS exploitation is an advanced specialization.

- [ ] **macOS Security Architecture:** Understand **Gatekeeper** (app signing verification), **System Integrity Protection (SIP)** (restricts root from modifying system files), and **Transparency, Consent, and Control (TCC)** (permission prompts for camera, mic, files).

- [ ] **macOS Filesystem & Users:** Know **APFS (encrypted by default), /System, /Library, /Users, /Applications** directory structure. Understand **dscl** for user management and **sudo/admin** vs standard user roles.

- [ ] **macOS Logging:** Understand **Unified Logging (log show/log stream)**, **Console.app**, and how macOS logs differ from Windows Event Viewer and Linux syslog. Know how to query logs for suspicious activity.

- [ ] **macOS Endpoint Security:** Know that **XProtect** (built-in malware detection), **MRT (Malware Removal Tool)**, **Notarization** (Apple's pre-distribution scanning), and **MDM (Mobile Device Management)** profiles are key enterprise controls.

- [ ] **macOS for Pentesters:** Understand that **Objective-See tools (KnockKnock, BlockBlock, LuLu, OverSight)** are the open-source equivalent of EDR for macOS, and that **osascript, Automator, LaunchAgents/LaunchDaemons** are macOS persistence mechanisms.

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

> [!TIP]
> **Goal:** : Move from local simulation to cloud-native networks using a "hack to root" mindset.

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

### Automation & Programmability

> [!TIP]
> **Goal:** : Understand how automation transforms network operations and software-defined architectures.

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

> [!TIP]
> **Goal:** : Understand the mathematical tools available.

- [ ] **CIA Alignment:** Map your crypto goals to the **Understand CIA Triad** (Confidentiality = Encryption, Integrity = Hashing).

- [ ] **Asymmetric Mastery:** Define the roles of **Private vs Public Keys**: Public to Encrypt/Verify, Private to Decrypt/Sign.

- [ ] **Integrity Checks:** Implement **Hashing** (SHA-256) to verify data integrity and detect **False Positives/Negatives** in file transfers.

---

### **Stage 2: Secure Communication (Data in Transit)**

> [!TIP]
> **Goal:** : Secure the pipe between two points.

- [ ] **Protocol Hardening:** Enforce **Secure Protocols** by disabling **SSL** (deprecated) and enforcing **TLS** 1.2/1.3.

- [ ] **Secure Transfer:** Replace cleartext protocols with encrypted alternatives: **FTP vs SFTP** (SSH-based) or **IPSEC** for VPNs.

- [ ] **Handshake Analysis:** Analyze the **Key Exchange** (Diffie-Hellman) within the **Understand Handshakes** process to ensure Forward Secrecy.

---

### **Stage 3: Identity & Trust (PKI)**

> [!TIP]
> **Goal:** : Prove that you are who you say you are.

- [ ] **Infrastructure:** Deploy **PKI** to manage digital certificates, ensuring the validity of public keys.

- [ ] **Email Security:** Implement **S/MIME** to sign and encrypt corporate email, preventing **Phishing** and spoofing.

---

### **Stage 4: Data at Rest & Password Security**

> [!TIP]
> **Goal:** : Secure stored data.

- [ ] **Disk Encryption:** Deploy **BitLocker, LUKS, FileVault** for full-disk encryption.

- [ ] **Password Storage:** Never store plaintext passwords; use **bcrypt, scrypt, Argon2** with **salting** to defeat rainbow tables.

- [ ] **Key Management:** Use **HSM, KMS (AWS KMS, Azure Key Vault)** for secure key storage and rotation.

- [ ] **Modern Hashing Profiles:** Standardize **Argon2id** (memory-hard) with tuned **memory (e.g., 64–256 MB), iterations, parallelism**, or **bcrypt** with current cost; prefer **password peppering** server-side and enforce **per-user salts**. Deprecate **MD5/SHA-1/SHA-256 for password storage** and legacy **PBKDF2-low-iteration** configs.

---

### **Stage 5: Cryptographic Attacks & Weaknesses**

> [!TIP]
> **Goal:** : Understand how crypto fails.

- [ ] **Weak Algorithms:** Identify and avoid **MD5, SHA-1, DES, RC4** in production systems.

- [ ] **Implementation Flaws:** Understand **padding oracle, timing attacks, side-channel attacks** that break otherwise strong algorithms.

- [ ] **Key Management Failures:** Exploit **hardcoded keys, weak KDF, insecure storage** in applications.

- [ ] **Downgrade Attacks:** Force **SSL/TLS downgrade** to weaker ciphers or protocols.

- [ ] **Cryptanalysis:** Understand basics of **frequency analysis, known-plaintext attacks, chosen-plaintext attacks**.

### **Lab Progression**

> [!TIP]
> **Goal:** : Turn crypto from vocabulary into observable behavior.

- [ ] **Hashing Lab:** Generate hashes for files, modify bytes, and prove integrity failure with SHA-256.
- [ ] **Password Storage Lab:** Compare unsalted hash, salted hash, bcrypt, and Argon2id behavior; document cracking cost differences.
- [ ] **TLS Handshake Lab:** Capture TLS 1.3 in Wireshark and identify ClientHello, ServerHello, certificate chain, cipher suite, and key exchange.
- [ ] **Certificate Lab:** Create a local CA, issue a server certificate, trust it in a lab client, then break trust by expiration/name mismatch.
- [ ] **Post-Quantum Awareness:** Document NIST PQC primitives such as ML-KEM and ML-DSA, hybrid deployment, and crypto-agility migration risk.
> [!IMPORTANT]
> **Move-On Gate:** You can explain what was encrypted, what was authenticated, what was signed, and what failed when trust broke.

---

<a id="toc-part-4-footprinting-and-reconnaissance"></a>