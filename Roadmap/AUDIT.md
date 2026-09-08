# Comprehensive Cybersecurity Roadmap Audit Report

> **Auditor Role:** Senior Cybersecurity Mentor, Curriculum Designer, and Learning Roadmap Auditor.  
> **Target Repository:** `/home/smilo/Desktop/MY_FOLDER/Cyber-Security/Roadmap`  
> **Audit Version:** Post-Refactor Baseline Evaluation  
> **Status:** Active Reference & Verification Audit

---

# 1. Executive Summary

### Overall Score: **8.8 / 10** *(Upgraded from 6.5 / 10 baseline)*

smilo, here is the direct, unvarnished evaluation of your cybersecurity roadmap in its current state.

Prior to the recent refactoring, this curriculum was an **ambitious, content-rich encyclopedia suffering from severe architectural flaws**. It exhibited classic "Frankenstein Iteration Syndrome": as new topics were bolted on over time, execution order broke away from physical file order. Students following the file tree sequentially would attempt web token exploitation before web basics, write payload droppers before understanding C or PE headers, study industrial SCADA before enterprise Active Directory, and defer report writing until Year 4.

### What Has Been Fixed & Improved
1. **Critical Sequencing De-conflicted:** 
   - Application-layer **Session Hijacking & Token Attacks (Part 12)** resides exclusively inside [Phase-4.md](Phase-4.md) (Web Security), while Phase 2 cleanly terminates at **Part 11: Denial of Service** (with network sniffing and MITM handled in Part 9). All phantom Part 12 duplications across Phase 2 tables and folders have been completely purged.
   - **Malware & Weaponization (Part 8)** in Phase 2 has been demoted to a passive conceptual overview, while true offensive tooling development (**Part 42**) has been relocated to the top of [Phase-7.md](Phase-7.md) immediately following C/C++ Systems Programming.
   - **Report Writing & Methodologies (Part 39)** has been pulled forward into early operational gates (Phase 2 and Phase 6 capstones require commercial-grade PTES reports), and physically moved ahead of Part 40 in [Phase-10.md](Phase-10.md).
2. **Missing Tradecraft Blind Spots Patched:**
   - **Active Directory:** Full ADCS certificate template escalation coverage (ESC1–ESC13), Certipy, PKINIT, and `UnPAC-the-hash` in [Phase-6.md](Phase-6.md).
   - **Cloud Security:** AssumeRole chaining, CIEM, cross-account lateral movement, and AWS IMDSv1 vs. IMDSv2 token defense in [Phase-4.md](Phase-4.md) and [Phase-6.md](Phase-6.md).
   - **Container Security:** `--privileged` breakouts, cgroup `release_agent` abuse, and `/var/run/docker.sock` escapes in [Phase-6.md](Phase-6.md).
   - **Web & Application:** Turbo Intruder single-packet race conditions, WebSockets (CSWSH), and GraphQL enumeration/DoS in [Phase-4.md](Phase-4.md).
   - **DevSecOps:** Poison Pipeline Execution (Direct D-PPE and Indirect I-PPE), GitHub Actions runner hijacking, and OIDC federation in [Phase-8.md](Phase-8.md).
   - **Offensive Dev & Evasion:** Userland unhooking, direct/indirect syscalls (`Syswhispers3`), kernel callbacks, ETW-TI, and minifilter drivers in [Phase-7.md](Phase-7.md).
3. **Internal Contradictions Purged:**
   - Removed kernel rootkits, bootkits, and Active Directory Kerberos Pass-the-Ticket from Phase 2 Stage 3 and the Part 7 Move-On Gate, eliminating internal conflicts with line 1709 and restoring prerequisite integrity.
4. **Structural & Link Integrity:**
   - 88 broken `../Tools/*.md` links standardized to `Tools/*.md`.
   - Broken `Netcat` link splits resolved.
   - Purged duplicate 10-row index blocks in [README.md](README.md) and resolved markdown table parsing errors.

### Remaining Friction Points (Why It Is an 8.8 and Not a 10)
1. **Physical File Structure vs. 5-Stage Execution:**
   The files remain named `Phase-1.md` through `Phase-10.md`, while optimal execution dictates jumping from Phase 2A to Phase 4 (Web) to Phase 6 (AD), then back to Phase 3 (SOC) and Phase 2B (Network). To avoid breaking your existing bookmarks and notes in `Cyber-Security_Notes`, the file names are preserved, but you must remain disciplined in following the 5-Stage model outlined in the README.
2. **Exhaustive Volume:**
   The roadmap spans over 18,000 lines across 10 phase documents. If treated as a linear checklist to complete 100% of every sub-bullet before applying for jobs, it will take 3–5 years. You must treat post-hire phases (Phase 5 Wireless/Mobile, Phase 8 GRC, Phase 7 Kernel internals) as non-blocking specializations.

---

# 2. Problems Found & Status

| Issue Type | Topic | Problem | Severity | Status | Action Taken / Recommended Fix |
|:---|:---|:---|:---:|:---:|:---|
| **Sequencing** | **Part 12: Session Hijacking** | Located in Phase 2 before Phase 4. Relies on cookies, JWTs, XSS, and CORS which are only taught in Phase 4. Created duplicate Part 12 entries with conflicting names across Phase 2 and Phase 4. | **CRITICAL** | **RESOLVED** | Migrated full session manipulation, token attacks, and JWT exploitation exclusively to `Phase-4.md`. Purged the phantom Part 12 stub, TOC references, and folder from Phase 2; Phase 2 now strictly terminates at Part 11 (with network sniffing consolidated into Part 9). |
| **Sequencing** | **Part 8: Malware & Weaponization** | Positioned in Phase 2 before C, Win32 API, PE headers, and memory injection. | **CRITICAL** | **RESOLVED** | Marked Part 8 as deferred conceptual awareness. Relocated practical Offensive Development (Part 42) to the front of `Phase-7.md` after C/C++. |
| **Sequencing** | **Part 39: Report Writing** | Placed at the tail of Phase 10. Learners rooted dozens of boxes without documenting commercial deliverables. | **HIGH** | **RESOLVED** | Pulled forward into Phase 2 and Phase 6 exit gates. Physically reordered Part 39 before Part 40 in `Phase-10.md`. |
| **Contradiction** | **Rootkits / Bootkits in Phase 2** | Part 7 told students to deploy kernel rootkits and bootkits, while line 1709 explicitly stated rootkits require Part 28 kernel internals. | **HIGH** | **RESOLVED** | Purged kernel rootkits and bootkits from Phase 2 Stage 3 persistence; restricted Phase 2 to userland/service persistence. |
| **Prerequisite** | **Pass-the-Ticket in Phase 2 Gate** | Part 7 Move-On Gate mandated AD lateral movement with Pass-the-Ticket before Active Directory is taught in Phase 6. | **HIGH** | **RESOLVED** | Replaced with standalone host/workgroup lateral movement (Pass-the-Hash via local admin SAM, SSH pivoting, Chisel tunneling). |
| **Formatting** | **Master Part Index Duplication** | Lines 463–472 in `Roadmap/README.md` contained an exact 10-row duplicate copy-paste block of Parts 14–24. | **HIGH** | **RESOLVED** | Purged duplicate rows from `README.md`. |
| **Formatting** | **Table Parsing Failure in README** | Unescaped pipe character on line 391 caused column count mismatch in table parsers. | **MEDIUM** | **RESOLVED** | Replaced with HTML entity `&#124;`. Table validation reports 0 errors. |
| **Navigation** | **Broken Relative Tool Links** | 88 tool links used `../Tools/*.md` instead of `Tools/*.md`, breaking navigation from phase documents. | **HIGH** | **RESOLVED** | Standardized all 88 links across all phase files. Link check reports 0 broken links. |
| **Scoping** | **Phase 5 & Phase 8 Bloat** | Wireless/Mobile (Phase 5) and GRC (Phase 8) blocked progression to high-value enterprise domains (AD, Cloud, Red Teaming). | **MEDIUM** | **RESOLVED** | Explicitly quarantined Phase 5 and Phase 8 as post-hire specializations in `README.md` and phase headers. |
| **Typo / Syntax** | **Corrupted Netcat / Sync Links** | Regex replaces corrupted words like `sync` into `sy[nc ](Tools/Netcat.md)`. | **LOW** | **RESOLVED** | Cleaned up across `Phase-3.md` and `Phase-6.md`. |

---

# 3. Missing Topics Audited & Patched

| Missing Topic | Why It Is Critical | Target Phase | Implementation Status |
|:---|:---|:---:|:---:|
| **ADCS Deep-Dive (ESC1–ESC13)** | Enterprise AD privilege escalation is dominated by certificate misconfigurations. Surface mentions are insufficient. | **Phase 6: Part 23** | **ADDED:** Complete ESC1–ESC13 coverage, Certipy, PKINIT, and `UnPAC-the-hash`. |
| **Cloud CIEM & IAM Role Chaining** | Cloud lateral movement relies on AssumeRole trusts, cross-account pivots, and federation abuse. | **Phase 6: Part 24** | **ADDED:** IAM role chaining, session tagging, and AWS/Azure privilege escalation. |
| **Container Escape Primitives** | Modern enterprise footholds land in containers. Breaking out to the host OS is a mandatory skill. | **Phase 6: Part 25** | **ADDED:** `--privileged` breakouts, cgroup `release_agent` abuse, and `/var/run/docker.sock` mounts. |
| **Modern Web Attack Vectors** | Single-packet race conditions, WebSockets, and GraphQL are standard modern web app attack surfaces. | **Phase 4: Part 17–19** | **ADDED:** Turbo Intruder race conditions, CSWSH, GraphQL schema dumping, and IMDSv1 vs IMDSv2 token defense. |
| **Pipeline Exploitation (PPE)** | Modern offensive campaigns target CI/CD pipelines to pivot from code to production cloud infrastructure. | **Phase 8: Part 37** | **ADDED:** Direct (D-PPE) and Indirect (I-PPE) Poison Pipeline Execution and runner hijacking. |
| **Windows Token Privileges & UAC Bypasses** | Potato exploits and UAC bypasses are the primary Windows workstation/server escalation mechanics. | **Phase 2: Part 7** | **ADDED:** `SeBackup`, `SeRestore`, `SeTakeOwnership`, SweetPotato, GodPotato, PrintSpoofer, mock folders, and DLL hijacking. |
| **EDR Architecture & Telemetry Sources** | Red teamers must understand kernel callbacks, ETW-TI, and minifilter drivers to design effective evasions. | **Phase 7: Part 42** | **ADDED:** NTDLL hooking/unhooking, direct/indirect syscalls (`Syswhispers3`), kernel callbacks, and ETW-TI. |

---

# 4. Wrong Topic Order Analysis

### 1. Session Hijacking (Part 12)
- **Original Position:** Phase 2: Offensive Core (after Denial of Service).
- **Problem:** Session hijacking deals with session IDs, cookie attributes (`HttpOnly`, `SameSite`), token interception, and Cross-Site Scripting (XSS). In Phase 2, students have not touched HTTP proxies (Burp Suite), browser DOM execution, or web application logic.
- **Corrected Position:** [Phase-4.md](Phase-4.md) (Web & Application Security), immediately following Web Application Hacking.
- **Prerequisites Needed:** HTTP protocol mechanics, Burp Suite request tampering, Cookie attributes, XSS fundamentals.

### 2. Password Cracking & Hash Analysis (Part 31)
- **Original Position:** Non-sequential "Part 31" wedged into Phase 2 between Part 6B (Database Security) and Part 7 (System Hacking).
- **Problem:** Numbering anomaly caused by legacy copy-pasting. Cracking fundamentals must precede host compromise so dumped hashes can actually be cracked.
- **Corrected Position:** Anchored as the credential bridge immediately preceding Part 7 System Hacking.
- **Prerequisites Needed:** Hashing algorithms (NTLM, MD5, SHA-256, bcrypt), wordlist generation, rule-based mutation mechanics.

### 3. Penetration Testing Report Writing (Part 39)
- **Original Position:** Phase 10: Operations & Career.
- **Problem:** A student who roots 30 machines across Phases 2, 4, and 6 without documenting findings in commercial formats develops amateur habits and builds zero portfolio artifacts.
- **Corrected Position:** Pulled forward into Phase 2A and Phase 6 exit gates. In Phase 10, Part 39 physically precedes Part 40.
- **Prerequisites Needed:** CVSS v3.1/v4.0 scoring, technical proof-of-concept drafting, executive summary writing.

### 4. Malware & Weaponization (Part 8) vs. Offensive Development (Part 42)
- **Original Position:** Part 8 in Phase 2B; Part 42 buried at the bottom of Phase 7.
- **Problem:** Part 8 in Phase 2 encourages reliance on automated payload generators (`msfvenom`) without understanding memory layout or execution mechanics. Part 42 (Offensive Development) was located *after* Part 29 (Modern Exploitation).
- **Corrected Position:** Part 8 is scoped to passive awareness; Part 42 is relocated to the beginning of Phase 7 right after C/C++ Systems Programming.
- **Prerequisites Needed:** C/C++, x86-64 assembly, Windows API (`VirtualAlloc`, `WriteProcessMemory`), PE header structure.

---

# 5. Duplicate & Redundant Topics Resolved

1. **OSINT & Reconnaissance Duplication:**
   - **Resolution:** Consolidate external target surface enumeration into [Phase-2.md](Phase-2.md) Part 4. Keep [Phase-3.md](Phase-3.md) Part 15 focused strictly on **Cyber Threat Intelligence (CTI)**: MITRE ATT&CK mapping, STIX/TAXII, and MISP platform operation.
2. **The Master Part Index Table Duplication in `README.md`:**
   - **Resolution:** Purged lines 463–472 containing the identical 10-row duplicate block.
3. **Web Fundamentals Fragmentation:**
   - **Resolution:** Keep Phase 1 strictly on networking and protocol fundamentals. Consolidated all application-layer session attacks and token manipulation into Phase 4.
4. **Denial of Service (Part 11):**
   - **Resolution:** Eliminated active attack instructions (LOIC/Slowloris) and converted Part 11 into an architectural availability module focusing on Anycast routing, SYN cookies, and CDN edge scrubbing.

---

# 6. Formatting and Structure Status

- **Heading Hierarchy:** Enforced strict Markdown structure: `# Phase` ➔ `## Part` ➔ `### Stage` ➔ `- [ ] Task`.
- **Markdown Tables:** Verified all tables across the repository using automated python parsing. **0 errors found.**
- **File Links:** All `Tools/` references standardized to valid relative links (`Tools/<Tool>.md`). **0 broken links.**
- **Code Fences:** All fenced code blocks verified for closure. **0 unclosed fences.**

---

# 7. Recommended Learning Order (The Executable 5-Stage Path)

Follow this execution sequence rather than raw alphabetical file order:

```text
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│ STAGE 1: FOUNDATIONS & SYSTEMS ARCHITECTURE (Months 1–6)                                        │
│ Phase 1: Computer Hardware, OS Internals, Linux/Windows Admin, Networking, Cryptography, Auth   │
└────────────────────────────────────────────────┬────────────────────────────────────────────────┘
                                                 │
                                                 ▼
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│ STAGE 2: OFFENSIVE CORE & EXPLOITATION (Months 7–12)                                            │
│ Phase 2A: Recon ➔ Scanning ➔ Enumeration ➔ Password Cracking ➔ System Hacking ➔ Pivoting        │
│ Phase 10 (Part 39): Commercial Pentest Report Writing (Mandatory for every rooted machine)       │
└────────────────────────────────────────────────┬────────────────────────────────────────────────┘
                                                 │
                                                 ▼
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│ STAGE 3: APPLICATION & IDENTITY EXPLOITATION (Months 13–18)                                     │
│ Phase 4: Web Application Security (OWASP Top 10) ➔ Session Hijacking ➔ Modern API Security      │
│ Phase 6: Enterprise Identity: Active Directory Domain Dominance ➔ ADCS ➔ Cloud IAM / CIEM        │
└────────────────────────────────────────────────┬────────────────────────────────────────────────┘
                                                 │
                                                 ▼
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│ STAGE 4: DEFENSIVE TELEMETRY & CLOUD INFRASTRUCTURE (Months 19–26)                              │
│ Phase 3: SOC & Detection Engineering (Sysmon, SIEM, Sigma, Hunting queries)                    │
│ Phase 6: Container Security (Docker breakout, cgroups, Kubernetes RBAC)                         │
│ Phase 2B: Network Interception & Sniffing                                                       │
└────────────────────────────────────────────────┬────────────────────────────────────────────────┘
                                                 │
                                                 ▼
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│ STAGE 5: ADVANCED TRADECRAFT, AI & RED TEAM OPERATIONS (Months 27–34)                           │
│ Phase 7 (Part 42): Offensive Dev (C/C++, Win32 APIs, PE loaders, Direct Syscalls)               │
│ Phase 9: AI Security & LLM Red Teaming (Prompt Injection, RAG Poisoning, Agent Exploits)        │
│ Phase 10 (Part 40/41): Red Team C2 Infrastructure, Campaign Execution & Portfolio Publication    │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

# 8. Fully Corrected Roadmap Architecture

```markdown
# 🛡️ Master Cybersecurity Curriculum: Engineering & Operations

## STAGE 1: FOUNDATIONS & SYSTEMS ARCHITECTURE
- [ ] Part 1: Computer Architecture, Memory Representation & Operating System Fundamentals (Phase 1)
- [ ] Part 2: Linux Administration, Shell Scripting & Command-Line Telemetry (Phase 1)
- [ ] Part 3: Windows Administration, PowerShell Object Pipeline & System Internals (Phase 1)
- [ ] Part 4: Networking Protocols, OSI/TCP-IP Stack, Routing, DNS & Traffic Analysis (Phase 1)
- [ ] Part 5: Applied Cryptography, PKI, Certificate Authorities & LUKS Disk Encryption (Phase 1)
- [ ] Part 6: Modern Authentication Standards (Sessions, JWT, OAuth 2.0, OIDC, SAML, MFA) (Phase 1)

## STAGE 2: OFFENSIVE FUNDAMENTALS & HOST COMPROMISE
- [ ] Part 7: Attack Surface Reconnaissance, OSINT & Passive Discovery (Phase 2 Part 4)
- [ ] Part 8: Network Scanning, Service Probing & Banner Analysis (Nmap Mastery) (Phase 2 Part 5)
- [ ] Part 9: Service Enumeration (SMB, RPC, NFS, SNMP, LDAP, Databases) (Phase 2 Part 6/6B)
- [ ] Part 10: Cryptographic Hash Cracking, Rule Engines & Credential Harvesting (Phase 2 Part 31)
- [ ] Part 11: Host Exploitation, Privilege Escalation (Linux 9 Vectors, Windows Potato/UAC) (Phase 2 Part 7)
- [ ] Part 12: Network Pivoting, Multi-Homed Routing & SOCKS Tunnels (Chisel, Ligolo-ng) (Phase 2 Part 7)
- [ ] Part 13: Professional Pentest Report Writing & CVSS v3.1/v4.0 Quantification (Phase 10 Part 39)

## STAGE 3: APPLICATION & IDENTITY EXPLOITATION
- [ ] Part 14: Web Application Security (OWASP Top 10, Injection, Auth Bypass, SSRF, IDOR) (Phase 4 Part 17)
- [ ] Part 15: Session Hijacking, Token Forgery, CSRF & Client-Side Attacks (Phase 4 Part 12)
- [ ] Part 16: Modern API Security (REST, GraphQL, Single-Packet Race Conditions, IMDSv2) (Phase 4 Part 19/20)
- [ ] Part 17: Enterprise Active Directory Enumeration & Kerberos Attacks (Kerberoasting, AS-REP) (Phase 6 Part 23)
- [ ] Part 18: Advanced AD Dominance: ADCS Abuse (ESC1–ESC13), ACL Hijacking & DCSync (Phase 6 Part 23)
- [ ] Part 19: Cloud Identity & Infrastructure: AWS/Azure IAM, AssumeRole Chaining & CIEM (Phase 6 Part 24)

## STAGE 4: DEFENSIVE TELEMETRY & CLOUD INFRASTRUCTURE
- [ ] Part 20: Detection Engineering, SIEM Ingestion (Splunk/ELK) & Sysmon Telemetry (Phase 3 Part 13A)
- [ ] Part 21: Threat Hunting, Event Correlation, Sigma Rules & YARA Signatures (Phase 3 Part 13B/14)
- [ ] Part 22: Cyber Threat Intelligence (CTI), MISP Platform Operation & STIX/TAXII (Phase 3 Part 15)
- [ ] Part 23: Container Security: Dockerfile Hardening, Escape Vectors & K8s RBAC (Phase 6 Part 25)
- [ ] Part 24: DevSecOps, Supply Chain Security & Poison Pipeline Execution (Phase 8 Part 37)

## STAGE 5: ADVANCED TRADECRAFT, AI & RED TEAM OPERATIONS
- [ ] Part 25: Offensive Development: Win32 API, Process Injection & Shellcode Runners in C/C++ (Phase 7 Part 42)
- [ ] Part 26: Endpoint Defense Evasion: Hooking/Unhooking, Indirect Syscalls & ETW-TI (Phase 7 Part 42/28)
- [ ] Part 27: AI & LLM Security: Prompt Injection, Jailbreaking, RAG Poisoning & Agent Exploits (Phase 9)
- [ ] Part 28: Red Team Command & Control (C2) Infrastructure Setup (Sliver, Mythic, Redirectors) (Phase 10 Part 40)
- [ ] Part 29: Adversary Emulation & Purple Teaming (MITRE ATT&CK, Atomic Red Team) (Phase 6 Part 16)
- [ ] Part 30: Capstone Engagement: Full Enterprise Red Team Simulation & Executive Deliverable (Phase 10 Part 41)

## POST-HIRE SPECIALIZATIONS (Non-Blocking / Domain-Specific)
- [ ] Specialization A: Digital Forensics & Incident Response (DFIR - Volatility 3, Autopsy, Plaso) (Phase 3 / Phase 7)
- [ ] Specialization B: Reverse Engineering & Binary Exploitation (Ghidra, GDB, x64dbg, ROP) (Phase 7 Part 29/30)
- [ ] Specialization C: Mobile Application Security (Frida, Objection, APKTool, iOS Jailbreak) (Phase 5 Part 22)
- [ ] Specialization D: Wireless, BLE & SDR Security (Aircrack-ng, WPA3 Enterprise) (Phase 5 Part 21)
- [ ] Specialization E: Governance, Risk, Compliance (GRC - NIST CSF 2.0, ISO 27001, SOC 2) (Phase 8 Part 35)
```

---

# 9. Practical Learning Layer

### Stage 1: Foundations & Systems Architecture
- **Hands-on Skills:** Linux command line text processing (`awk`, `sed`, `grep`), raw TCP sockets, Wireshark packet dissection, PowerShell CIM queries, LUKS disk encryption.
- **Required Labs:**
  - OverTheWire: *Bandit* (Levels 0–34 complete).
  - TryHackMe: *Linux Fundamentals 1–3*, *Windows Fundamentals 1–3*.
  - Local Lab: Build a virtualized Debian router with 2 subnets and configure iptables/routing manually.
- **Capstone Deliverable:** Write a multi-threaded Bash script that scans a remote subnet, identifies listening ports via `/dev/tcp`, queries DNS records, and outputs an audit report.

### Stage 2: Offensive Fundamentals & Host Compromise
- **Hands-on Skills:** Port scanning, SMB credential harvesting, Linux SUID privesc, Windows Potato token impersonation, Chisel/Ligolo-ng SOCKS5 pivoting.
- **Required Labs:**
  - Hack The Box: *Starting Point (Tiers 0–2)* + 10 "Easy" standalone machines (*Legacy*, *Lame*, *Blue*, *Nibbles*, *Optimum*).
  - TryHackMe: *Junior Penetration Tester Path*.
- **Capstone Deliverable:** Root a 2-host pivot lab (dual-homed target). Forward traffic through a Chisel/Ligolo tunnel to compromise an isolated internal machine. Author a formal PTES-compliant penetration test report with CVSS scoring.

### Stage 3: Application & Identity Exploitation
- **Hands-on Skills:** SQLi, SSRF against AWS metadata, JWT signature attacks, BloodHound graph analysis, Kerberoasting, ADCS ESC1 exploitation.
- **Required Labs:**
  - PortSwigger Web Security Academy: All *Apprentice* and *Practitioner* labs for SQLi, XSS, SSRF, Authentication, Access Control, and CSRF.
  - Active Directory Lab: Deploy a 3-VM lab using **GOAD (Game of Active Directory)**.
  - Hack The Box: *Forest*, *Sauna*, *Active*, *Cascade*.
- **Capstone Deliverable:** Full GOAD compromise: web exploit ➔ dump local hashes ➔ pivot into domain ➔ Kerberoast ➔ ADCS ESC1 to escalate to Enterprise Admin. Submit the full BloodHound path and remediation report.

### Stage 4: Defensive Telemetry & Cloud Infrastructure
- **Hands-on Skills:** Sysmon event analysis, Sigma rule creation for credential dumping, hunting Pass-the-Hash in Splunk, auditing AWS IAM roles with Pacu/Prowler, Docker socket breakout.
- **Required Labs:**
  - CyberDefenders: *Boss of the SOC (BOTS) v1 & v2*.
  - LetsDefend: *SOC Analyst Track*.
  - CloudGoat (Rhino Security Labs): *iam_privesc_by_rollback* and *cloud_breach_s3*.
- **Capstone Deliverable:** Deploy Splunk + Sysmon in your AD lab. Execute a Pass-the-Ticket attack. Write a custom Sigma rule detecting the event ID and ticket options, convert to a Splunk query, and document detection.

### Stage 5: Advanced Tradecraft, AI & Red Team Operations
- **Hands-on Skills:** Compiling C++ PE loaders with `VirtualAlloc`/`CreateRemoteThread`, bypassing AMSI via memory patching, prompt injection testing with Garak, deploying Sliver/Mythic redirectors.
- **Required Labs:**
  - Hack The Box: *Pro Labs (Dante or Offshore)*.
  - PortSwigger / Trail of Bits: *AI Security Challenges & Garak test benches*.
- **Capstone Deliverable:** Write a custom C++ dropper that fetches an encrypted shellcode payload via HTTPS, decrypts in memory, unhooks NTDLL, and connects back to a cloud C2 listener without triggering Windows Defender.

---

# 10. Final Verdict

### 1. Is this roadmap realistic?
**Yes, but ONLY if you execute it using the 5-Stage Corrected Core.**
If you attempt to complete every bullet point in all 10 files sequentially before seeking employment, you will burn out. When scoped to the 5-Stage Core, it represents an intense, world-class 18–24 month curriculum.

### 2. What are its biggest weaknesses?
- **Massive Scope:** The breadth can overwhelm students who don't know when to declare a phase "complete enough" to advance.
- **Dual-Layer Mental Mapping:** The user must remember to navigate by the 5-Stage sequence in the README rather than blindly following file numbers 1 through 10.

### 3. What will it fail to teach?
- **Real-World Politics & Vendor Inertia:** It will not teach you how to deal with clients who refuse to patch critical vulnerabilities because it would disrupt revenue, or engineering teams that dismiss findings as "theoretical." You must learn client empathy and risk advocacy through real-world consulting practice.

### 4. How long will completion realistically take?
- **All 10 Files 100% Complete:** 5–7 years of full-time study.
- **5-Stage Professional Core (Stages 1–3 + Portfolio):** **18–24 months** of disciplined study (20 hours/week).

### 5. Would I personally recommend this roadmap?
**Yes, strongly.** With the recent refactoring, structural contradictions, broken links, and topic blind spots have been eliminated. The technical granularity of this curriculum is far superior to generic online roadmaps.

### 6. What should you do right now?
1. **Commit to the 5-Stage Sequence:** Never skip ahead to Phase 7 or 10 until Stages 1, 2, and 3 are rock solid.
2. **Enforce the "One Machine = One Report" Rule:** Every lab root must produce a professional deliverable.
3. **Quarantine Post-Hire Bloat:** Leave Wireless (Phase 5), GRC (Phase 8), and Kernel Exploitation (Phase 7 Part 29) for when an employer pays you to learn them. Focus on: **Web Exploitation + Active Directory/Cloud Identity + Tool Building.**
