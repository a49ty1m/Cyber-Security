# Phase 7: Advanced Specializations

---

### 🧭 Navigation
◀ [Phase 6](Phase-6.md) | 🏠 [Master Roadmap](README.md) | [Phase 8](Phase-8.md) ➔

---

> [!NOTE]
> **Phase Overview**
> - **⏱️ Time Commitment (Full-Time):** 4–7 months
> - **⏱️ Time Commitment (Part-Time):** 8–12 months
> - **🎯 Primary Focus:** Digital forensics & incident response, reverse engineering & malware analysis, modern exploitation (heap/kernel/browser), hardware hacking & embedded systems, offensive development (shellcode, C2, process injection, AMSI/ETW bypass), physical pentesting, VoIP/SS7/5G telecom, and blockchain/Web3 smart contract auditing.

---

> [!NOTE]
> ### 📝 Phase 7 Documentation Requirements
> Advanced specialization work must produce portfolio-quality artifacts. Required artifacts:
> - **Forensic reports** — Volatility/Autopsy analysis with timeline reconstruction
> - **IDA/Ghidra annotations** — reverse engineering notes with function labels and comments
> - **Exploit code** — well-commented PoC code with ethical usage disclaimers
> - **Malware IOC lists** — hashes, C2 domains, YARA signatures for analyzed samples
> - **Git commits** — all analysis, code, and reports committed
>
> _By the end of Phase 7, your repository should contain at least 2 deep-dive technical analyses._

---

### 🗂️ Table of Contents

**Core Advanced Modules**
- [Part 27: Digital Forensics](#part-27-digital-forensics)
  - [Stage 1: Preparation & First Response](#stage-1-preparation-first-response)
  - [Stage 2: Evidence Analysis (The Deep Dive)](#stage-2-evidence-analysis-the-deep-dive)
  - [Stage 3: Memory Forensics](#stage-3-memory-forensics)
  - [Stage 4: Network Forensics](#stage-4-network-forensics)
  - [Stage 5: Cloud & Mobile Forensics](#stage-5-cloud-mobile-forensics)
  - [Stage 6: Advanced Analysis & Reporting](#stage-6-advanced-analysis-reporting)
  - [Stage 7: Legal & Reporting](#stage-7-legal-reporting)
  - [Lab Progression](#lab-progression)
- [Part 28: Reverse Engineering & Malware Analysis](#part-28-reverse-engineering-malware-analysis)
  - [Stage 1: Static Analysis Foundations](#stage-1-static-analysis-foundations)
  - [Stage 2: Dynamic Analysis & Debugging](#stage-2-dynamic-analysis-debugging)
  - [Stage 3: Anti-Reverse Engineering & Evasion Techniques](#stage-3-anti-reverse-engineering-evasion-techniques)
  - [Stage 4: Malware Classification & Threat Intelligence](#stage-4-malware-classification-threat-intelligence)
  - [Stage 5: Advanced RE & Automation](#stage-5-advanced-re-automation)
  - [Lab Progression](#lab-progression)
- [Part 29: Modern Exploitation](#part-29-modern-exploitation)
  - [Stage 1: Recon, Triage & Tooling](#stage-1-recon-triage-tooling)
  - [Stage 2: Memory Exploitation (Userland)](#stage-2-memory-exploitation-userland)
  - [Stage 3: Advanced Targets](#stage-3-advanced-targets)
  - [Stage 4: Exploit Delivery & OPSEC](#stage-4-exploit-delivery-opsec)
  - [Stage 5: Post-Exploitation Hardening & Safety](#stage-5-post-exploitation-hardening-safety)
  - [Lab Progression](#lab-progression)
- [Part 42: Offensive Development & Tooling](#part-42-offensive-development-tooling)
  - [Stage 1: Exploit Development Foundation](#stage-1-exploit-development-foundation)
  - [Stage 2: Windows Offensive Development](#stage-2-windows-offensive-development)
  - [Stage 3: Linux Offensive Development](#stage-3-linux-offensive-development)
  - [Stage 4: C2 & Implant Development](#stage-4-c2-implant-development)
  - [Lab Progression](#lab-progression)

**Optional Specialization Modules**
- [Part 30: Hardware Hacking & Embedded Systems [OPTIONAL SPECIALIZATION]](#part-30-hardware-hacking-embedded-systems-optional-specialization)
  - [Stage 1: Hardware Reconnaissance](#stage-1-hardware-reconnaissance)
  - [Stage 2: Firmware Analysis](#stage-2-firmware-analysis)
  - [Stage 3: Runtime Exploitation](#stage-3-runtime-exploitation)
  - [Stage 4: Side-Channel & Physical Attacks](#stage-4-side-channel-physical-attacks)
  - [Stage 5: IoT & Embedded Defense](#stage-5-iot-embedded-defense)
  - [Lab Progression](#lab-progression)
- [Part 32: Physical Penetration Testing [OPTIONAL SPECIALIZATION]](#part-32-physical-penetration-testing-optional-specialization)
  - [Stage 1: Pre-Engagement & Reconnaissance](#stage-1-pre-engagement-reconnaissance)
  - [Stage 2: Entry & Access Control Bypass](#stage-2-entry-access-control-bypass)
  - [Stage 3: HID & USB Payload Attacks](#stage-3-hid-usb-payload-attacks)
  - [Stage 4: On-Site Operations & Data Collection](#stage-4-on-site-operations-data-collection)
  - [Stage 5: Reporting Physical Findings](#stage-5-reporting-physical-findings)
  - [Lab Progression](#lab-progression)
- [Part 33: VoIP & Telecommunications Security [OPTIONAL SPECIALIZATION]](#part-33-voip-telecommunications-security-optional-specialization)
  - [Stage 1: VoIP Protocol Fundamentals](#stage-1-voip-protocol-fundamentals)
  - [Stage 2: VoIP Reconnaissance & Enumeration](#stage-2-voip-reconnaissance-enumeration)
  - [Stage 3: VoIP Attacks](#stage-3-voip-attacks)
  - [Stage 4: SS7 & Telecom Signaling Attacks](#stage-4-ss7-telecom-signaling-attacks)
  - [Stage 5: 5G Security](#stage-5-5g-security)
  - [Stage 6: Defense & Hardening](#stage-6-defense-hardening)
  - [Lab Progression](#lab-progression)
- [Part 34: Blockchain & Web3 Security [OPTIONAL SPECIALIZATION]](#part-34-blockchain-web3-security-optional-specialization)
  - [Stage 1: Blockchain Fundamentals for Security](#stage-1-blockchain-fundamentals-for-security)
  - [Stage 2: Smart Contract Vulnerabilities](#stage-2-smart-contract-vulnerabilities)
  - [Stage 3: Smart Contract Auditing Methodology](#stage-3-smart-contract-auditing-methodology)
  - [Stage 4: Web3 Infrastructure Attacks](#stage-4-web3-infrastructure-attacks)
  - [Stage 5: Defense & Secure Development](#stage-5-defense-secure-development)
  - [Lab Progression](#lab-progression)

---

> [!NOTE]
> **Core vs Optional:** Complete Parts 27, 28, 29, and 42 for the core advanced-security path. Treat Parts 30, 32, 33, and 34 as specialization branches that add depth only when they match your career goal.

---

## Part 27: Digital Forensics

### **Stage 1: Preparation & First Response**

> [!TIP]
> **Goal:** Secure the scene without corrupting evidence.

- [ ] **Incident Identification:** Trigger the `Incident Response Process` upon `Identification` of a breach.

- [ ] **Volatile Collection:** Capture RAM immediately using `memdump` before the system is powered off or rebooted.

- [ ] **Static Acquisition:** Create a forensic image of hard drives using `FTK Imager` or `dd`, ensuring a write-blocker is used.

---

### **Stage 2: Evidence Analysis (The Deep Dive)**

> [!TIP]
> **Goal:** Find the needle in the haystack.

- [ ] **Disk Analysis:** Load the evidence into `autopsy` to recover deleted files, analyze web history, and search for keywords.

- [ ] **Binary Inspection:** Use `winhex` to manually inspect file headers (signatures) to identify files with changed extensions (e.g., an EXE renamed to JPG).

- [ ] **Log Review:** Correlate actions by analyzing `Event Logs` (Login times, Service installs) and `syslogs`.

---

### **Stage 3: Memory Forensics**

> [!TIP]
> **Goal:** Extract evidence from volatile memory — the richest source of attacker artifacts.

- [ ] **Memory Acquisition:** Capture live RAM using **WinPMEM, DumpIt, LiME (Linux Memory Extractor)** before system shutdown. Understand **hibernation files (hiberfil.sys)** and **crash dumps** as alternative memory sources.

- [ ] **Volatility 3 Fundamentals:** Install and configure **Volatility 3**. Understand **symbol tables, ISF (Intermediate Symbol Format)**, and how to select the correct OS profile for analysis.

- [ ] **Process Analysis:** Use **pslist, pstree, malfind, handles, dlllist, cmdline** to identify **suspicious processes, injected code, hidden modules, hollowed processes**, and **unusual parent-child relationships** (e.g., svchost spawning PowerShell).

- [ ] **Network from Memory:** Extract **netscan** results to identify **active network connections, listening ports, and remote C2 addresses** that may not appear in disk-based logs.

- [ ] **Credential Extraction:** Dump **LSASS memory contents, cached domain hashes, Kerberos tickets, DPAPI master keys** from memory images to understand credential exposure scope.

- [ ] **Rootkit Detection:** Use **ssdt, idt, callbacks, driverirp, modscan** plugins to detect **kernel-mode rootkits, SSDT hooks, and hidden drivers** that are invisible to usermode tools.

- [ ] **Memory Timeline:** Extract **process creation times, loaded module timestamps, command history (consoles plugin)**, and **clipboard contents** to reconstruct attacker actions in volatile memory.

---

### **Stage 4: Network Forensics**

> [!TIP]
> **Goal:** Trace the attacker's path through network evidence.

- [ ] **Traffic Reconstruction:** Open **packet captures (PCAP)** in **Wireshark** to find **C2 communication patterns, data exfiltration, lateral movement, cleartext credentials**, and **DNS tunneling indicators**.

- [ ] **Flow Analysis:** When full packets are missing, use **NetFlow/sFlow/IPFIX logs** to identify **connections to malicious IPs, unusual traffic volumes, beaconing patterns (regular interval connections)**, and **data exfiltration spikes**.

- [ ] **Protocol Anomaly Detection:** Identify **protocol abuse** — DNS queries with encoded payloads, ICMP data exfiltration, HTTP/S beaconing with unusual User-Agent strings, encrypted traffic to non-standard ports.

- [ ] **TLS Forensics:** Analyze **JA3/JA4 fingerprints, certificate details, SNI values** to identify **malicious encrypted traffic** without decryption.

---

### **Stage 5: Cloud & Mobile Forensics**

> [!TIP]
> **Goal:** Collect and analyze evidence from cloud and mobile sources.

- [ ] **Cloud Log Forensics:** Analyze **AWS CloudTrail, Azure Activity Log, GCP Audit Logs** for **unauthorized access, privilege escalation, resource creation, data exfiltration, and API abuse**. Understand **log retention policies and gaps**.

- [ ] **Cloud Storage Forensics:** Examine **S3 access logs, Azure Blob storage access patterns, GCS audit logs** for **unauthorized data access, deleted object recovery, and versioning exploitation**.

- [ ] **Container Forensics:** Collect evidence from **Docker containers** (layer analysis, runtime snapshots, container diff) and **Kubernetes audit logs** (API server requests, RBAC violations, pod scheduling anomalies).

- [ ] **Mobile Device Forensics:** Extract evidence from **Android** (adb backup, JTAG, chip-off) and **iOS** (iTunes/Finder backup, Cellebrite, GrayKey) devices. Analyze **app data (SQLite databases, plist files, SharedPreferences)**, **communication logs**, and **location data**.

- [ ] **SaaS Forensics:** Collect evidence from **Microsoft 365 Unified Audit Log, Google Workspace Admin logs, Slack export** for **account compromise, data theft, insider threat investigation**.

---

### **Stage 6: Advanced Analysis & Reporting**

> [!TIP]
> **Goal:** Understand the "How" and tell the story.

- [ ] **Malware Analysis:** Use **static/dynamic analysis, sandbox detonation, reverse engineering** to understand malware behavior and IOCs. 📌 _Full reverse engineering methodology is covered in Part 28._

- [ ] **Timeline Construction:** Build **complete attack timeline** from artifacts (file timestamps, logs, registry, prefetch, memory, network) using **Plaso/log2timeline, Timeline Explorer**.

- [ ] **Anti-Forensics Detection:** Look for signs of **timestomping, log clearing, secure deletion, encryption, steganography** indicating a sophisticated attacker who is actively hiding tracks.

- [ ] **Attribution Analysis:** Correlate **TTPs, IOCs, tools, infrastructure** with known threat actors using **MITRE ATT&CK, threat intelligence platforms (MISP, OpenCTI)**, and **Diamond Model** analysis.

---

### **Stage 7: Legal & Reporting**

> [!TIP]
> **Goal:** Present findings professionally and maintain legal admissibility.

- [ ] **Chain of Custody:** Maintain strict **evidence handling, hash verification (SHA-256), transfer documentation** for legal admissibility. Understand **Daubert/Frye standards** for expert testimony.

- [ ] **Technical Report:** Document **methodology, findings, evidence location, IOCs, MITRE ATT&CK mapping** for technical teams and incident responders.

- [ ] **Executive Summary:** Translate technical findings into **business impact, risk assessment, regulatory implications** for management and board-level communication.

- [ ] **Legal Coordination:** Work with **legal counsel, HR, law enforcement, insurance** on evidence disclosure, prosecution, breach notification, and regulatory reporting.

---

### **Lab Progression**

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Acquire a forensic image using FTK Imager from a lab VM | Forensic image + hash verification document |
| 2 | Analyze a memory dump with Volatility 3 (identify injected process) | Process analysis report with IOCs |
| 3 | Reconstruct attack timeline from Windows Event Logs + Prefetch + Shimcache | Timeline spreadsheet with evidence citations |
| 4 | Analyze a PCAP for C2 beaconing and data exfiltration patterns | Network forensics report |
| 5 | Complete a CyberDefenders DFIR challenge end-to-end | Full forensic report using Part 39 template |

> [!IMPORTANT]
> **Move-On Gate:** You can acquire forensic images without evidence corruption, analyze memory dumps for malware artifacts, reconstruct attack timelines from multiple evidence sources, and produce court-admissible forensic reports.

---

<a id="toc-part-28-reverse-engineering--malware-analysis"></a>
## Part 28: Reverse Engineering & Malware Analysis

### **Stage 1: Static Analysis Foundations**

> [!TIP]
> **Goal:** Analyze binaries without executing them.

- [ ] **File Identification:** Use **file, exiftool, DIE (Detect It Easy)** to identify **file type, architecture, compiler, packer** before loading into a disassembler.

- [ ] **PE/ELF/Mach-O Structure:** Master **executable format headers, sections (.text, .data, .rdata, .bss), import/export tables, relocation entries**, and **entry points**.

- [ ] **Disassembly Tools:** Develop proficiency in **Ghidra** (free) and **IDA Pro** (industry standard) for **disassembly, decompilation, cross-referencing, and function signature recognition**.

- [ ] **String Analysis:** Extract **hardcoded URLs, IPs, registry keys, API calls, encryption keys, error messages** using **strings, FLOSS (FLARE Obfuscated String Solver)**.

- [ ] **Import/Export Analysis:** Identify **suspicious API imports** (VirtualAlloc, CreateRemoteThread, WriteProcessMemory, InternetOpenUrl) that reveal **injection, download, or persistence behavior**.

- [ ] **Control Flow Analysis:** Trace **function call graphs, conditional branches, loops** to understand **program logic, decision points, and hidden functionality**.

- [ ] **.NET/Java Reversing:** Decompile **managed code** using **dnSpy, ILSpy** (.NET) or **JD-GUI, JADX, CFR** (Java/Android) for near-source-level analysis.

---

### **Stage 2: Dynamic Analysis & Debugging**

> [!TIP]
> **Goal:** Observe malware behavior during live execution.

- [ ] **Sandbox Execution:** Detonate samples in **isolated VMs** (FlareVM, REMnux) with **snapshots**; monitor using **Procmon, Process Hacker, Regshot, Wireshark, FakeNet-NG**.

- [ ] **Behavioral Indicators:** Document **file system changes, registry modifications, network connections, process creation, mutex creation, service installs** during execution.

- [ ] **Debugger Proficiency:** Master **x64dbg/x32dbg** (Windows) and **GDB with gef/pwndbg** (Linux) for **breakpoints, stepping, memory inspection, register manipulation**.

- [ ] **API Hooking & Tracing:** Use **API Monitor, Frida, strace/ltrace** to intercept and log **system calls and library calls** at runtime.

- [ ] **Memory Forensics During Execution:** Dump **process memory** with **Volatility, procdump** to find **decrypted payloads, injected code, unpacked stages** that only exist in RAM.

- [ ] **Network Traffic Analysis:** Capture **C2 communications, DNS queries, HTTP beacons, exfiltration attempts** using **Wireshark, mitmproxy, INetSim** during detonation.

---

### **Stage 3: Anti-Reverse Engineering & Evasion Techniques**

> [!TIP]
> **Goal:** Understand and defeat techniques malware uses to resist analysis.

- [ ] **Anti-Debugging:** Detect and bypass **IsDebuggerPresent, NtQueryInformationProcess, timing checks (RDTSC), int 2D/int 3, TLS callbacks** used to detect debuggers.

- [ ] **Anti-VM/Anti-Sandbox:** Identify checks for **VMware/VirtualBox artifacts (registry keys, MAC prefixes, CPUID), mouse movement, screen resolution, uptime, username** and patch them out.

- [ ] **Packing & Crypters:** Unpack **UPX, Themida, VMProtect, custom packers** using **manual unpacking (OEP finding, IAT reconstruction)** and automated tools.

- [ ] **Obfuscation:** Defeat **control flow flattening, dead code insertion, string encryption, opaque predicates** through **symbolic execution, pattern matching, and scripting**.

- [ ] **Code Virtualization:** Understand **VM-based protectors** (Themida, VMProtect) that translate code to **custom bytecode**; use **devirtualization techniques** and trace analysis.

---

### **Stage 4: Malware Classification & Threat Intelligence**

> [!TIP]
> **Goal:** Categorize malware and extract actionable intelligence.

- [ ] **Malware Taxonomy:** Classify samples as **RAT, ransomware, worm, rootkit, bootkit, stealer, loader, dropper, wiper, cryptominer, botnet agent** based on behavior.

- [ ] **IOC Extraction:** Extract **file hashes (MD5/SHA256), domains, IPs, URLs, mutexes, registry keys, YARA signatures** for threat intelligence sharing.

- [ ] **YARA Rule Writing:** Write **custom YARA rules** to detect malware families by **string patterns, byte sequences, file structure, import combinations**.

- [ ] **MITRE ATT&CK Mapping:** Map observed **malware behaviors** to **specific techniques/sub-techniques** for standardized reporting and detection engineering.

- [ ] **Campaign Attribution:** Correlate **code similarities, infrastructure overlaps, TTPs, timestamps, language artifacts** to link samples to **threat actor groups**.

---

### **Stage 5: Advanced RE & Automation**

> [!TIP]
> **Goal:** Scale analysis with scripting and handle complex targets.

- [ ] **Ghidra Scripting:** Write **Ghidra scripts (Java/Python)** to automate **function renaming, string decryption, pattern searching, cross-reference analysis**.

- [ ] **IDAPython:** Use **IDAPython scripts** for **bulk analysis, signature generation, automated deobfuscation, plugin development**.

- [ ] **Binary Diffing:** Use **BinDiff, Diaphora** to compare **patched vs. unpatched binaries** to identify **vulnerability patches and 1-day exploit targets**.

- [ ] **Emulation:** Use **Unicorn Engine, QEMU, Qiling** to **emulate code snippets** (decryption routines, shellcode) without full execution.

- [ ] **Firmware RE:** Apply RE skills to **embedded firmware** (binwalk extraction, architecture identification, cross-compilation debugging).

- [ ] **Kernel-Level RE:** Analyze **drivers, rootkits, bootkits** using **WinDbg kernel debugging, IDA with kernel symbols, Volatility memory analysis**.

---

### **Lab Progression**

> [!TIP]
> **Goal:** Build reverse-engineering muscle memory in a safe malware-analysis environment.

- [ ] **Lab Setup:** Deploy FLARE VM and REMnux in isolated VMs with snapshots and no shared folders.
- [ ] **Static Analysis Lab:** Analyze 5 benign or training binaries with strings, PE/ELF headers, imports, sections, and entropy.
- [ ] **Dynamic Analysis Lab:** Execute controlled samples in a sandbox and capture filesystem, registry, process, and network behavior.
- [ ] **Debugger Lab:** Use x64dbg/GDB to set breakpoints, step through functions, inspect stack/registers, and patch one branch in a toy binary.
- [ ] **YARA Lab:** Write 3 YARA rules for training samples and test false positives against clean files.
> [!IMPORTANT]
> **Move-On Gate:** Produce one malware-analysis-style report with IOCs, behavior summary, ATT&CK mapping, and detection logic.

<a id="toc-part-29-modern-exploitation"></a>
## Part 29: Modern Exploitation

> **Prerequisite Gate:** Complete Part 1 Stages 3–4 (Memory Management, Data Representation), Part 1 Stage 7 (C fundamentals), and Part 42 (Offensive Development — exploit writing, shellcode, assembly) before starting this Part. Modern exploitation builds directly on these foundations.

### **Stage 1: Recon, Triage & Tooling**

> [!TIP]
> **Goal:** Prepare targets and environments for exploit development.

- [ ] **Binary Recon:** Identify **arch, compiler, protections (ASLR, DEP/NX, PIE, RELRO, Stack Canaries, CFG, CET/PAC/BTI)**.

- [ ] **Debug Setup:** Configure **GDB/gef/pwndbg, WinDbg, Frida**; obtain **symbols, PDBs, DWARF** where possible.

- [ ] **Fuzzing:** Use **AFL++, libFuzzer, honggfuzz, Peach**; seed corpora, add **sanitizers (ASan/UBSan/MSan)**; triage crashes.

---

### **Stage 2: Memory Exploitation (Userland)**

> [!TIP]
> **Goal:** Exploit memory-safety bugs under modern mitigations.

- [ ] **Buffer Overflows:** Master how data can overwrite adjacent memory to hijack the **EIP/RIP (Instruction Pointer)**; understand **stack vs heap overflows**.

- [ ] **Stack/Heap Primitives:** Develop **overflow, UAF, double-free, type confusion, OOB read/write** primitives.

- [ ] **Bypass Strategies:** Use **ROP/JOP/SROP, ret2libc, ret2dlresolve, stack pivoting**, and **heap grooming** (tcache/fastbin/largebin, LFH) to gain PC control.

- [ ] **Exploit Mitigations:** Study **ASLR** (Address Space Layout Randomization) and **DEP/NX** (Data Execution Prevention); master **ROP** (Return Oriented Programming) to bypass them. Learn **stack canary** bypass via leaks.

- [ ] **Mitigation Bypass:** Defeat **RELRO/PIE**, **CFG/CET/PAC/BTI** with **COOP, SIGRETURN, pointer authentication bypass**, or **JIT spraying**.

- [ ] **Sandbox Escape:** Target **browser/render sandboxes**, **container seccomp/AppArmor**, and **Win32k lockdown** using **IPC/shmem/race** primitives.

---

### **Stage 3: Advanced Targets**

> [!TIP]
> **Goal:** Move beyond basic binaries to complex environments.

- [ ] **Kernel Exploitation:** Leverage **UAF/race/logic bugs**, bypass **SMEP/SMAP/KASLR/KPTRR**, and use **token stealing/privilege escalation** primitives.

- [ ] **Browser & JS Engines:** Exploit **JIT/IC/GC** bugs; chain **type confusion → infoleak → RCE → sandbox escape**.

- [ ] **Deserialization & Logic:** Exploit **Java/.NET/Python/PHP** gadget chains, **serialization format** confusion, and **race conditions**.

- [ ] **Cloud/Serverless:** Abuse **function sandboxes, cold-start leaks, metadata services (IMDS), and SSRF-to-role** chains.

---

### **Stage 4: Exploit Delivery & OPSEC**

> [!TIP]
> **Goal:** Deliver and operate exploits stealthily.

- [ ] **Stagers & Payloads:** Build **stageless/staged** payloads with **in-memory loaders, reflective DLL/ELF**, and **syscall/indirect syscall** execution.

- [ ] **Evasion:** Apply **sleep obfuscation, call-stack spoofing, DLL hollowing, APC/ETW/AMSI tampering**, and **PPID spoofing**.

- [ ] **Crash Handling:** Implement **auto-retry, watchdogs, safe-fail** to avoid blue screens/service crashes.

- [ ] **Telemetry Shaping:** Throttle **network/beacon timing**, pad **packet sizes**, and mimic **legit protocol usage**.

---

### **Stage 5: Post-Exploitation Hardening & Safety**

> [!TIP]
> **Goal:** Maintain control while minimizing detection and impact.

- [ ] **Cleanup & Rollback:** Remove **artifacts, logs, crash dumps**, restore configs; support **idempotent rollback**.

- [ ] **Persistence Choices:** Select **low-noise persistence** (scheduled tasks, services, WMI events, cron/systemd timers) with **time-bounded lifetimes**.

- [ ] **Safety & Blast Radius:** Gate exploit use with **kill-switches, rate limits, environment checks**, and **canary endpoints** to avoid collateral damage.

---

### **Lab Progression**

> [!TIP]
> **Goal:** Approach exploitation with prerequisites, safety controls, and repeatable labs.

- [ ] **Assembly Gate:** Complete x86/x64 basics: registers, stack frames, calling conventions, `call`, `ret`, jumps, and memory layout.
- [ ] **pwn.college / ROP Emporium Lab:** Complete beginner shellcode, stack overflow, and ROP exercises before touching harder targets.
- [ ] **Fuzzing Lab:** Build a toy parser, fuzz it, crash it, triage the crash, and write a minimal proof of concept.
- [ ] **Mitigation Lab:** Demonstrate how NX, ASLR, stack canaries, PIE, and RELRO change exploitability.
> [!IMPORTANT]
> **Move-On Gate:** Produce one exploit writeup with root cause, crash analysis, exploit reliability notes, and mitigation guidance.

<a id="toc-part-30-hardware-hacking--embedded-systems"></a>
## Part 30: Hardware Hacking & Embedded Systems [OPTIONAL SPECIALIZATION]

### **Stage 1: Hardware Reconnaissance**

> [!TIP]
> **Goal:** Identify attack surface on physical devices.

- [ ] **Chip Identification:** Identify **MCU/SoC models** by reading chip markings; research **datasheets, known vulnerabilities**.

- [ ] **PCB Analysis:** Trace **PCB layouts** to identify **debug ports, test points, memory chips, communication buses**.

- [ ] **Debug Port Discovery:** Locate **JTAG, UART, SPI, I2C** interfaces using **multimeter, logic analyzer, JTAGulator**.

- [ ] **Pinout Mapping:** Use **oscilloscope** to identify **TX/RX pins, clock signals, voltage levels** on unknown headers.

- [ ] **Firmware Extraction:** Dump firmware via **debug interfaces, external flash chip reading, bootloader exploits**.

---

### **Stage 2: Firmware Analysis**

> [!TIP]
> **Goal:** Reverse engineer and find vulnerabilities in firmware.

- [ ] **Binary Extraction:** Use **binwalk** to extract **filesystems, compressed data, encryption keys** from firmware images.

- [ ] **Architecture Identification:** Determine **CPU architecture (ARM, MIPS, x86)** using **file, binwalk, Ghidra**.

- [ ] **Filesystem Analysis:** Mount extracted **SquashFS, JFFS2, UBIFS** to analyze **configs, credentials, certificates**.

- [ ] **Static Analysis:** Reverse engineer binaries with **Ghidra, IDA Pro, radare2** to find **buffer overflows, backdoors, hardcoded keys**.

- [ ] **Crypto Analysis:** Extract **encryption keys, certificates, private keys** from firmware for decryption or impersonation.

---

### **Stage 3: Runtime Exploitation**

> [!TIP]
> **Goal:** Execute code on live embedded systems.

- [ ] **UART Shell Access:** Connect to **UART** to gain **root shell, bootloader access, kernel logs**.

- [ ] **JTAG Debugging:** Use **OpenOCD, Segger J-Link** to **halt CPU, dump memory, modify registers, inject code**.

- [ ] **Bootloader Exploitation:** Exploit **U-Boot, grub** vulnerabilities to gain **pre-OS execution, modify boot parameters**.

- [ ] **Secure Boot Bypass:** Understand the mechanics used to load malicious, persistent bootloaders before OS security kicks in; master techniques like **boot chain manipulation, secure enclave exploitation, TPM/fTPM bypass**.

- [ ] **Memory Corruption:** Exploit **buffer overflows, format string bugs** in embedded applications.

- [ ] **Firmware Modification:** Patch firmware to **disable authentication, add backdoors, modify functionality**; reflash device.

---

### **Stage 4: Side-Channel & Physical Attacks**

> [!TIP]
> **Goal:** Extract secrets through non-traditional attack vectors.

- [ ] **Power Analysis:** Use **ChipWhisperer** for **simple/differential power analysis (SPA/DPA)** to extract encryption keys.

- [ ] **Electromagnetic Analysis:** Capture **EM emissions** during crypto operations to recover secrets.

- [ ] **Fault Injection:** Use **voltage glitching, clock glitching** to skip security checks or expose hidden functionality.

- [ ] **Chip Decapping:** Perform **acid decapping** to expose die for **optical inspection, probing, reverse engineering**.

- [ ] **Bus Snooping:** Intercept **SPI/I2C traffic** between chips to capture **flash contents, key exchange, commands**.

---

### **Stage 5: IoT & Embedded Defense**

> [!TIP]
> **Goal:** Secure embedded systems against attacks.

- [ ] **Secure Boot:** Implement **cryptographic boot chain verification** to prevent unauthorized firmware.

- [ ] **Debug Port Protection:** Disable or lock **JTAG/SWD** in production; use **debug authentication**.

- [ ] **Encrypted Firmware:** Encrypt firmware images; implement **secure firmware updates** with signature verification.

- [ ] **Tamper Detection:** Add **physical tamper switches, mesh overlays, epoxy coating** to detect intrusion.

- [ ] **Hardware Security Modules:** Use **TPM, secure elements (SE), TrustZone** for key storage and secure execution.

- [ ] **Code Signing:** Sign all firmware and application code; verify signatures before execution.

---

### **Lab Progression**

> [!TIP]
> **Goal:** Gain hands-on experience with hardware and embedded system attacks.

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Extract firmware from a consumer IoT device (router, IP camera) using binwalk and analyze the filesystem | Firmware analysis report with extracted credentials/keys |
| 2 | Gain UART shell access on a lab device, dump flash via SPI, and modify firmware | Hardware exploitation walkthrough with photos |
| 3 | Perform side-channel power analysis using ChipWhisperer on a target implementing AES | Side-channel attack report with key recovery evidence |

> [!IMPORTANT]
> **Move-On Gate:** You can extract and analyze firmware, gain debug shell access, and explain side-channel attack fundamentals.

---

<a id="toc-part-31-password-cracking--hash-analysis"></a>


## Part 32: Physical Penetration Testing [OPTIONAL SPECIALIZATION]

> **Safety Gate:** Physical testing requires written authorization, named locations, dates/times, emergency contacts, stop conditions, and a get-out-of-jail letter. Do not practice bypasses on real facilities, campuses, offices, hotels, apartments, or transit systems.

### **Stage 1: Pre-Engagement & Reconnaissance**

> [!TIP]
> **Goal:** Plan the physical assessment within legal scope.

- [ ] **Scope Definition:** Confirm **written authorization, target facilities, allowed hours, assumed identity (e.g., contractor, vendor)**, and **emergency abort contact** before any physical operation.

- [ ] **Facility OSINT:** Use **Google Maps, Satellite imagery, LinkedIn (employee badge photos), job postings (physical security tools mentioned), public filings** to map facility layout, entry points, and security posture.

- [ ] **Physical Observation:** Conduct **covert surveillance** — observe **employee badge behavior, delivery procedures, tailgate vulnerability, smoking areas, loading docks** as low-security entry vectors.

- [ ] **Social Engineering Pretext:** Prepare **believable personas** (IT contractor, fire inspector, HVAC technician, delivery person) with **supporting props, business cards, uniforms, fake work orders**.

---

### **Stage 2: Entry & Access Control Bypass**

> [!TIP]
> **Goal:** Defeat physical barriers to gain facility access.

- [ ] **Tailgating / Piggybacking:** Follow authorized personnel through secured doors using **timing, props (heavy boxes, hands full), social confidence**; test anti-tailgate detection systems.

- [ ] **Lock Picking:** Practice **single-pin picking, raking, bump keys** for standard pin-tumbler locks; understand **high-security locks (Medeco, Abloy)** that resist standard attacks.

- [ ] **Bypass Tools:** Use **under-door tools (UDT), latch slipping tools, door gap attacks** to manipulate door hardware without the key.

- [ ] **RFID/NFC Badge Cloning:** Capture **low-frequency (125kHz HID, EM4100)** badge data with **Proxmark3** from up to 30cm; clone to blank T5577 card; understand **13.56MHz (MIFARE, DESFire)** attack complexity.

- [ ] **Electric Strike / Maglock Bypass:** Use **REX (Request-to-Exit) sensor exploitation, power interruption, crash bar manipulation** to open magnetically locked doors.

- [ ] **Elevator & Stairwell Access:** Identify **fire escape stairwells, service elevators, parking garage access** that bypass reception and security desks.

---

### **Stage 3: HID & USB Payload Attacks**

> [!TIP]
> **Goal:** Deploy physical implants and hardware attack tools.

- [ ] **USB HID Attacks (Rubber Ducky / Bash Bunny):** Craft **DuckyScript payloads** to execute **reverse shells, credential theft, backdoor installation** within seconds when plugged into an unlocked machine.

- [ ] **O.MG Cable:** Deploy **USB cables with embedded implants** that appear legitimate but exfiltrate data or execute commands over WiFi.

- [ ] **LAN Turtle / Shark Jack:** Drop **network implants** that provide **remote SSH access, packet capture, and network scanning** from inside the target network.

- [ ] **USB Drop Attacks:** Leave **weaponized USB drives** in common areas (parking lot, reception, bathroom); craft **autorun payloads, LNK files, fake docs** that execute on Windows/Linux.

- [ ] **Rogue Network Devices:** Plant **WiFi Pineapple, rogue AP, network tap** in server rooms, comms closets, or under desks for persistent network access.

---

### **Stage 4: On-Site Operations & Data Collection**

> [!TIP]
> **Goal:** Achieve objectives once inside.

- [ ] **Workstation Access:** Target **unlocked machines, password-protected screens (bypass with HID)**, install **implants, keyloggers, screen capture tools**.

- [ ] **Shoulder Surfing:** Observe **password entry, sensitive documents, screen content** in open offices, meeting rooms, and public areas.

- [ ] **Dumpster Diving:** Recover **printed credentials, org charts, hardware serial numbers, network diagrams, decommissioned drives** from trash/recycling.

- [ ] **Server Room / Comms Closet:** Attempt access to **network switches, patch panels, servers**; document **unencrypted hardware, unsecured console ports, accessible management interfaces**.

---

### **Stage 5: Reporting Physical Findings**

> [!TIP]
> **Goal:** Document and communicate physical security gaps professionally.

- [ ] **Evidence Collection:** Capture **covert photos/video (within ROE), cloned badge data, dropped USB recovery, access logs** as proof-of-concept evidence.

- [ ] **Risk Mapping:** Map findings to **physical security frameworks (PSIA, ISO 27001 Annex A.11)** and quantify **business impact** (data theft, sabotage, insider threat facilitation).

- [ ] **Remediation Guidance:** Recommend **anti-tailgate turnstiles, RFID upgrade paths, clean desk policy, USB port lockdown, security awareness training, camera placement**.

---

### **Lab Progression**

> [!TIP]
> **Goal:** Gain hands-on experience with physical security assessment techniques.

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Practice lock picking on a training lock set (transparent locks + standard pin tumbler) | Lock bypass skills log with technique notes |
| 2 | Clone a low-frequency RFID badge using Proxmark3 and demonstrate access control bypass in lab | Badge cloning walkthrough with Proxmark3 output |
| 3 | Build and deploy a Rubber Ducky/Bash Bunny payload that establishes a reverse shell within 10 seconds | HID attack payload with demo video and detection guidance |

> [!IMPORTANT]
> **Move-On Gate:** You can pick a standard pin tumbler lock, clone a low-frequency RFID badge, and craft a working HID payload.

---

<a id="toc-part-33-voip--telecommunications-security"></a>
## Part 33: VoIP & Telecommunications Security [OPTIONAL SPECIALIZATION]

### **Stage 1: VoIP Protocol Fundamentals**

> [!TIP]
> **Goal:** Understand how VoIP systems communicate.

- [ ] **SIP (Session Initiation Protocol):** Master **SIP message structure (INVITE, ACK, BYE, REGISTER, OPTIONS)**, **dialog establishment**, **authentication (Digest Auth)**, and **common ports (UDP/TCP 5060, TLS 5061)**.

- [ ] **RTP (Real-time Transport Protocol):** Understand **media stream transport**, **SRTP (Secure RTP)** for encryption, **RTCP** for control, and how **RTP ports are negotiated via SDP**.

- [ ] **VoIP Infrastructure:** Map **components**: **IP-PBX (Asterisk, FreePBX), SBC (Session Border Controller), SIP Trunk, softphones, IP handsets, voicemail servers**.

- [ ] **Codec Identification:** Identify **G.711, G.729, Opus** codecs from SDP negotiation; understand quality vs. bandwidth tradeoffs and how codecs affect capture/decode.

---

### **Stage 2: VoIP Reconnaissance & Enumeration**

> [!TIP]
> **Goal:** Discover and map VoIP infrastructure.

- [ ] **SIP Scanning:** Use **svmap (SIPVicious), nmap SIP NSE scripts** to discover **SIP-enabled devices, extensions, PBX software versions**.

- [ ] **Extension Enumeration:** Use **svwar** to enumerate **valid SIP extensions** via REGISTER/OPTIONS probing; map **active users and voicemail accounts**.

- [ ] **Banner Grabbing:** Identify **PBX vendor and version** from **SIP User-Agent headers**; cross-reference with **CVE databases** for known exploits.

- [ ] **SDP Analysis:** Parse **Session Description Protocol** messages to identify **media types, codec preferences, RTP port ranges, and IP addresses**.

---

### **Stage 3: VoIP Attacks**

> [!TIP]
> **Goal:** Exploit weaknesses in VoIP deployments.

- [ ] **SIP Brute Force:** Use **svcrack (SIPVicious)** to brute-force **SIP extension passwords**; test default credentials (1234, extension number as password).

- [ ] **RTP Interception:** Position in MITM via **ARP spoofing**; capture **RTP streams with Wireshark**; reassemble and decode audio with **VoIPmonitor, sngrep, rtpbreak**.

- [ ] **Call Hijacking:** Send **spoofed BYE messages** to terminate active calls; send **CANCEL or re-INVITE** to redirect calls to attacker-controlled endpoints.

- [ ] **VoIP Fuzzing:** Use **Sip-Proxy, Codenomicon** to fuzz **SIP parsers** for crashes, memory corruption, and denial of service in PBX software.

- [ ] **Vishing Infrastructure:** Understand how **VoIP enables scalable vishing** — spoofed caller ID, auto-dialers, SIP trunk abuse for mass calling campaigns.

- [ ] **VLAN Hopping to Voice VLAN:** Exploit **voice VLAN misconfiguration** (untagged/double-tagged frames) to access VoIP network segment from data VLAN.

---

### **Stage 4: SS7 & Telecom Signaling Attacks**

> [!TIP]
> **Goal:** Understand mobile network signaling vulnerabilities.

- [ ] **SS7 Architecture:** Understand **Signaling System 7 (SS7)** — the global telephone signaling protocol connecting **mobile network operators, MSCs, HLRs, VLRs**.

- [ ] **SS7 Attack Types:** Study **location tracking (SendRoutingInfo), call interception (MAP UpdateLocation), SMS interception (ForwardSM)** — attacks that work against **any mobile network globally**.

- [ ] **Diameter Protocol:** Understand **Diameter** (4G/LTE replacement for SS7) and its own **attack surface** — roaming exploitation, subscriber data disclosure, DoS.

- [ ] **SIM Swapping (Technical):** Understand the **social engineering + SS7/carrier abuse chain** — porting credentials, carrier authentication weaknesses, and MFA bypass consequences.

- [ ] **IMSI Catchers (Stingrays):** Understand how **fake base stations force 2G downgrade**, capture **IMSI identifiers**, and enable **passive interception** of unencrypted traffic.

---

### **Stage 5: 5G Security**

> [!TIP]
> **Goal:** Understand the 5G threat landscape.

- [ ] **5G Architecture:** Understand **5G SA (Standalone) vs NSA (Non-Standalone)**, **gNB (base station), AMF, SMF, UPF** core network functions, and **network slicing**.

- [ ] **5G Attack Surface:** Study **SBA (Service-Based Architecture) HTTP/2 API attacks**, **SUPI/SUCI identifier exposure**, **slice isolation bypass**, **roaming security gaps**.

- [ ] **5G vs 4G Security:** Understand improvements (**SUPI concealment, mandatory mutual auth**) and remaining weaknesses (**legacy 2G/3G fallback, roaming interfaces**).

---

### **Stage 6: Defense & Hardening**

> [!TIP]
> **Goal:** Secure VoIP and telecom infrastructure.

- [ ] **SRTP Enforcement:** Mandate **SRTP** for all media streams and **TLS (SIP over TLS/SIPS)** for signaling; disable unencrypted SIP on all production systems.

- [ ] **SBC Hardening:** Configure **Session Border Controllers** to perform **topology hiding, rate limiting, anomaly detection, and geographic call blocking**.

- [ ] **Authentication Hardening:** Enforce **strong SIP digest passwords**, implement **IP allowlisting** for SIP trunks, disable **anonymous REGISTER**.

---

### **Lab Progression**

> [!TIP]
> **Goal:** Gain hands-on experience with VoIP and telecommunications attacks.

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Set up Asterisk PBX in lab, register SIP clients, and capture SIP/RTP traffic in Wireshark | VoIP protocol analysis report with call flow diagrams |
| 2 | Perform SIP enumeration (svmap, svwar) and eavesdrop on an unencrypted call using Wireshark RTP playback | VoIP exploitation walkthrough with audio extraction evidence |
| 3 | Harden the lab PBX with SRTP, TLS, and SBC rules; verify that previous attacks no longer work | VoIP hardening report with before/after comparison |

> [!IMPORTANT]
> **Move-On Gate:** You can enumerate SIP infrastructure, capture and replay VoIP calls, and harden a PBX with SRTP/TLS.

---

<a id="toc-part-34-blockchain--web3-security"></a>
## Part 34: Blockchain & Web3 Security [OPTIONAL SPECIALIZATION]

### **Stage 1: Blockchain Fundamentals for Security**

> [!TIP]
> **Goal:** Understand how blockchain and smart contracts work before attacking them.

- [ ] **Blockchain Mechanics:** Master **distributed ledger, consensus mechanisms (PoW, PoS, PoA)**, **immutability, transaction finality, mempool**, and **public/private key cryptography** in blockchain context.

- [ ] **Smart Contract Architecture:** Understand **EVM (Ethereum Virtual Machine)**, **Solidity language basics**, **ABI (Application Binary Interface)**, **bytecode vs. source code**, and **contract deployment lifecycle**.

- [ ] **DeFi Ecosystem:** Map **protocols**: **DEXs (Uniswap, Curve), lending (Aave, Compound), oracles (Chainlink), bridges, yield aggregators** — understand how they interact and compose.

- [ ] **Wallet Security:** Understand **EOA (Externally Owned Accounts) vs contract wallets**, **seed phrases (BIP39), HD derivation paths, hardware wallets (Ledger, Trezor)**, and **private key storage risks**.

---

### **Stage 2: Smart Contract Vulnerabilities**

> [!TIP]
> **Goal:** Identify and exploit common Solidity security flaws.

- [ ] **Reentrancy Attacks:** Exploit **recursive external calls before state updates** (The DAO hack pattern); understand `checks-effects-interactions` as the fix; test with **Hardhat/Foundry**.

- [ ] **Integer Overflow/Underflow:** Exploit **arithmetic overflow in Solidity <0.8.0** (e.g., `uint256 balance = 0; balance -= 1;` wraps to MAX); understand SafeMath and Solidity 0.8 built-in checks.

- [ ] **Access Control Flaws:** Find **missing `onlyOwner` modifiers, tx.origin authentication, unprotected `initialize()` functions** in upgradeable contracts.

- [ ] **Logic Flaws & Business Logic Errors:** Exploit **incorrect assumptions** about token prices, balances, or state — often unique to each protocol's design.

- [ ] **Flash Loan Attacks:** Understand **uncollateralized loans within a single transaction**; exploit **oracle price manipulation, liquidity pool imbalances, governance attacks** using flash loans.

- [ ] **Oracle Manipulation:** Exploit **reliance on on-chain DEX spot price as oracle** — manipulate pool price via large swap, exploit contracts that trust it, profit.

- [ ] **Front-Running & MEV:** Understand **Maximal Extractable Value** — sandwich attacks, arbitrage, and liquidation front-running by miners/validators in the mempool.

---

### **Stage 3: Smart Contract Auditing Methodology**

> [!TIP]
> **Goal:** Systematically audit contracts for vulnerabilities.

- [ ] **Static Analysis Tools:** Use **Slither, MythX, Aderyn, Semgrep Solidity rules** to automatically detect common vulnerability patterns.

- [ ] **Symbolic Execution:** Use **Manticore, Echidna (fuzzer), Halmos (formal verification)** to find edge cases not caught by static analysis.

- [ ] **Manual Code Review:** Read contract logic line-by-line; trace **all external calls, state transitions, and access control checks**; verify invariants hold under all conditions.

- [ ] **PoC in Foundry/Hardhat:** Write **test exploits in Foundry (`forge test`)** forking mainnet to demonstrate real attack viability without deploying to live chain.

- [ ] **Audit Report Writing:** Document findings with **severity (Critical/High/Medium/Low/Informational), impact, likelihood, proof-of-concept, and recommended fix**.

---

### **Stage 4: Web3 Infrastructure Attacks**

> [!TIP]
> **Goal:** Attack the broader Web3 ecosystem beyond smart contracts.

- [ ] **Wallet Drainer Attacks:** Understand **malicious `approve()` / `permit()` signatures** that give attackers unlimited token spending rights; study **phishing sites** targeting Web3 users.

- [ ] **Bridge Attacks:** Analyze **cross-chain bridge vulnerabilities** (Ronin $625M, Wormhole $320M) — **validator compromise, signature replay, logic errors in lock/mint mechanisms**.

- [ ] **NFT Security:** Examine **metadata centralization risks, royalty bypass, reentrancy in `onERC721Received`**, and **enumeration attacks** on NFT collections.

- [ ] **Private Key Extraction:** Study attack vectors — **weak entropy in key generation, compromised RNG, phishing for seed phrases, clipboard hijackers, malicious browser extensions**.

- [ ] **RPC Node Attacks:** Understand **exposure of `eth_accounts`, `personal_sign` on misconfigured nodes**; test for **open JSON-RPC endpoints** that can sign transactions.

---

### **Stage 5: Defense & Secure Development**

> [!TIP]
> **Goal:** Build secure smart contracts and Web3 applications.

- [ ] **Security Patterns:** Implement **checks-effects-interactions, pull-over-push payments, rate limiting, circuit breakers (pause mechanisms)** in contract design.

- [ ] **Upgradeable Contract Security:** Use **OpenZeppelin Upgrades Plugins**; understand **storage collision risks, initializer protection, proxy admin key management**.

- [ ] **Formal Verification:** Apply **Certora Prover or K Framework** to mathematically prove critical invariants hold under all possible inputs.

- [ ] **Bug Bounties:** Engage **Immunefi, Code4rena, Sherlock** for smart contract audits and bug bounties; understand **responsible disclosure in Web3 context**.

---

### **Lab Progression**

> [!TIP]
> **Goal:** Gain hands-on experience with smart contract auditing and Web3 attacks.

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Complete Ethernaut and Damn Vulnerable DeFi (first 10 challenges each) | Challenge solutions with exploit code and vulnerability explanations |
| 2 | Audit a sample smart contract using Slither + manual review; write a finding report | Smart contract audit report with severity ratings and PoC |
| 3 | Write a Foundry test that demonstrates a flash loan attack against a vulnerable DeFi protocol on a mainnet fork | Flash loan exploit PoC with Foundry test code and impact analysis |

> [!IMPORTANT]
> **Move-On Gate:** You can identify common Solidity vulnerabilities, write Foundry exploit tests, and produce a professional smart contract audit report.

---

<a id="toc-part-42-offensive-development--tooling"></a>
## Part 42: Offensive Development & Tooling

_Phase 7 — Advanced Specializations | Prerequisites: Part 1 (Programming Fundamentals), Part 7 (System Hacking), Part 8 (Malware & Weaponization) | This module contains the offensive programming content that was previously in Part 1 Stage 7 (Fundamentals). It requires solid system hacking knowledge before attempting._

### **Stage 1: Exploit Development Foundation**

- [ ] **Exploit Prototyping:** Use Python with **pwntools, impacket** for **rapid PoC development**, **fuzzing harnesses**, and **custom C2 implant logic**.

- [ ] **Buffer Overflow Mastery:** Write **stack-based buffer overflow exploits**, understand **stack frame layout, return address overwrite, NOP sleds**, and **bad character identification**.

- [ ] **Shellcode Writing:** Craft **position-independent shellcode** for **reverse shells, bind shells, staged loaders** avoiding null bytes and bad characters.

- [ ] **Egghunters:** Build **egghunter shellcode** to locate payloads in memory when buffer space is limited.

- [ ] **x86/x64 Assembly:** Develop working fluency in **MOV, PUSH, POP, CALL, JMP, INT, SYSCALL** and understand **calling conventions (cdecl, stdcall, fastcall, System V AMD64)**.

- [ ] **Disassembly Reading:** Confidently read **disassembled output** in **Ghidra, IDA Pro, radare2** to identify vulnerabilities and understand compiled logic.

### **Stage 2: Windows Offensive Development**

- [ ] **Win32 API Exploitation:** Use **CreateProcess, VirtualAlloc, WriteProcessMemory, CreateRemoteThread** for **process injection, DLL loading, and token manipulation**.

- [ ] **C# & .NET Offensive Tooling:** Master **P/Invoke and D/Invoke** to call **native Win32 APIs** from managed code. Understand tools like **SharpHound, Rubeus, Seatbelt, SharpUp, Certify** and how to **modify/recompile** them to evade signatures.

- [ ] **In-Memory Execution:** Master **.NET assembly loading (Assembly.Load), reflection, and inline execution** to run offensive tools without dropping files to disk.

- [ ] **AMSI/ETW Bypass:** Understand how **.NET interacts with AMSI** and **ETW** and techniques to patch or disable them at runtime.

- [ ] **Offensive PowerShell:** Master **download cradles, constrained language mode escape, script block logging evasion**, and **AMSI bypass in PowerShell**.

### **Stage 3: Linux Offensive Development**

- [ ] **Linux C Development:** Interact with **POSIX APIs, /proc filesystem, ptrace**, and **LD_PRELOAD hooking** for rootkit/implant development.

- [ ] **ELF Binary Manipulation:** Understand **ELF format, GOT/PLT, dynamic linking** for binary patching and implant injection.

### **Stage 4: C2 & Implant Development**

- [ ] **C2 Architecture:** Design **client-server implant architecture** with **modular payloads, encrypted channels, and sleep obfuscation**.

- [ ] **Protocol Selection:** Choose and implement **HTTP/HTTPS, DNS, named pipes, or cloud API** channels for C2 communication.

- [ ] **C++ Tooling:** Build **custom implants, packers, crypters**, and **network tools** requiring performance and low-level control.

- [ ] **Evasion Integration:** Combine **sleep obfuscation, call stack spoofing, indirect syscalls, and API unhooking** into implant design.

### **Lab Progression**

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Exploit a basic stack buffer overflow (SLMail/Brainpan) | Working exploit script |
| 2 | Write custom shellcode for a reverse shell (x86) | Shellcode + test harness |
| 3 | Build a basic C2 implant (Python client → Python server) | Working C2 demo in lab |
| 4 | Modify a SharpHound/Rubeus tool to evade signatures | Modified tool + AV scan comparison |
| 5 | Implement AMSI bypass + in-memory .NET execution chain | End-to-end evasion demo in lab |

> [!IMPORTANT]
> **Move-On Gate:** You can write working exploits, develop custom shellcode, build basic C2 implants, modify existing offensive tools to evade detection, and bypass AMSI/ETW in a controlled lab environment.

---

### 🏆 Phase 7 Capstone Project

**Perform Malware Analysis on a Real-World Sample OR Write an Exploit for a Known CVE**

Choose one track:

**Track A — Malware Analysis:**
- [ ] Obtain a real-world malware sample from MalwareBazaar or VirusTotal
- [ ] Perform static analysis (PE headers, strings, imports, YARA matching)
- [ ] Perform dynamic analysis (sandbox execution, API monitoring, network traffic)
- [ ] Reverse engineer key functions in IDA/Ghidra
- [ ] Produce a malware analysis report with IOCs (hashes, C2s, YARA rules)

**Track B — Exploit Development:**
- [ ] Select a known CVE with a public advisory (1-day exploit)
- [ ] Analyze the vulnerability root cause (buffer overflow, use-after-free, etc.)
- [ ] Develop a working proof-of-concept exploit in a controlled lab
- [ ] Document the exploitation process and mitigation strategies

**Deliverables:**
- [ ] Professional malware report with IOCs OR exploit writeup with PoC code
- [ ] All analysis artifacts committed to your Git repository

> [!IMPORTANT]
> **Capstone Gate:** Your deliverable must be technical enough to submit to a threat intel team (Track A) or a security research publication (Track B).

---

### 🧭 Phase 7 Reflection & Competency Check

- [ ] **Reflection:** Which advanced domain deserves continued depth, and which optional domains should you intentionally skip for now?
- [ ] **Reflection:** Where did you rely on tooling without fully understanding the underlying artifact, binary, or exploit primitive?
- [ ] **Competency:** Can you produce either a defensible malware analysis report or a working exploit writeup with controlled proof?
- [ ] **Competency:** Can you explain limitations, assumptions, and safety boundaries for your research?
- [ ] **Competency:** Can another technical reviewer reproduce your analysis from your notes and artifacts?

> [!IMPORTANT]
> **Phase Completion Gate:** Move on only when your advanced work is deep, reproducible, ethically scoped, and polished enough for expert review.

---

<a id="toc-part-35-governance-risk--compliance-grc"></a>
