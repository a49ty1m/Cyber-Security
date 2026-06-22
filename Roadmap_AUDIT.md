# Cybersecurity & AI Security Roadmap — Full Audit

**Auditor Role:** Senior Cybersecurity Mentor, Curriculum Designer, Learning Roadmap Auditor
**Document Audited:** [Roadmap.md](file:///home/smilo/Desktop/MY_FOLDER/Cyber-Security/Roadmap.md) (5,299 lines, 286 KB)
**Audit Date:** 2026-06-22

---

## 1. Executive Summary

### Overall Score: 7.4 / 10

This is one of the most comprehensive self-authored cybersecurity roadmaps I've seen. It covers 41 parts across 9 phases, includes lab progressions, safety gates, proof gates, and extends into AI security — a domain most roadmaps ignore entirely. The author clearly has real intent and has done significant research.

That said, the roadmap has structural problems that will hurt the learner in practice:

### Major Strengths

1. **Breadth is exceptional.** 41 parts covering hardware to AI red teaming is genuinely rare. Most roadmaps stop at Phase 4.
2. **Safety gates are present.** DoS, malware, social engineering, wireless, and physical sections all have explicit safety warnings. This is not common and shows operational maturity in design.
3. **Lab progressions exist.** Multiple parts have "Lab Progression" sections with move-on gates. This is structurally superior to "learn X" bullet lists.
4. **Proof gates force accountability.** The Foundation Proof Gate (lines 394–424) demands deliverables (`.md` files, `.pcap` files, Git repos). This is the right approach.
5. **AI Security is integrated correctly.** Phase 9 (Part 38) with 18 stages is one of the most thorough AI security curricula publicly available.
6. **OWASP API Top 10 coverage** (Part 19) is methodical and current.
7. **Career portfolio section** (Part 41) directly ties skills to employability — certifications, GitHub, bug bounties, writing, presentations.

### Major Weaknesses

1. **Premature offensive content in Phase 1.** Part 1 contains weaponized mobile attacks (MDM bypass, malware delivery, Frida hooking) and advanced document exploits (VBA macros, DDE, OneNote weaponization) before the student has learned networking or cryptography. This is structurally broken.
2. **Massive content duplication.** Topics like ARP spoofing, MITM, DNS spoofing, credential theft, LOLBAS, and session hijacking are repeated across 4–6 different parts with near-identical depth.
3. **No Linux or Windows administration section.** The roadmap jumps from CPU registers to OS internals to memory management without teaching the student how to actually *use* Linux or Windows as an administrator. The proof gate demands Linux/Windows admin skills but Part 1 never teaches them.
4. **Phase 3 (Defense) is too thin at 1–2 months.** 10 phases of blue team content crammed into 1–2 months alongside OSINT, purple teaming, and adversary emulation is unrealistic.
5. **Time estimates are aggressive.** 18–30 months full-time for this volume of material is closer to 30–48 months in reality for a learner starting from scratch.
6. **Part 2 (Networking) is bloated with Cisco-specific configuration.** Multiple pages of Cisco IOS CLI commands (DHCP config, NAT config, WLAN GUI, QoS) are vendor-specific knowledge that doesn't belong in a security fundamentals curriculum.
7. **Missing explicit Linux administration and Windows administration curriculum.** Referenced by proof gates but never taught.

### Estimated Skill Level If Followed Exactly

If completed honestly with all labs and proof gates: **Strong mid-level security professional** capable of SOC Analyst, Junior Penetration Tester, or Application Security Engineer roles. Advanced specialization phases (7–9) would push into senior/specialist territory, but only if the foundation phases are corrected.

---

## 2. Problems Found

| # | Issue Type | Location | Problem | Severity | Recommended Fix |
|---|-----------|----------|---------|----------|-----------------|
| 1 | Sequencing | Part 1, Stage 5b (Lines 554–601) | Mobile platform architecture includes **offensive techniques** (jailbreak detection bypass, SSL pinning bypass, keychain extraction, Frida/Cycript runtime manipulation, MDM bypass, enterprise app abuse, mobile malware delivery) in what is labeled a "Fundamentals" section. Student hasn't learned networking, crypto, or web security yet. | **Critical** | Split: Move fundamentals (APK/IPA structure, security models) to Part 1. Move all offensive techniques to Part 22 (Mobile Pentesting). |
| 2 | Sequencing | Part 1, Stage 6 (Lines 604–650) | "Application Suites & Cloud Vectors" teaches **VBA macro weaponization, DDE abuse, OneNote/PDF weaponization, OAuth consent phishing, device code flow abuse, covert channel exfiltration, and CASB/SWG evasion** — all advanced offensive techniques — in Part 1 Fundamentals. | **Critical** | Move entirely to Phase 2 (Offensive Core) or Phase 7 (Advanced). Students need networking, web, and cryptography before weaponization. |
| 3 | Sequencing | Part 1, Stage 5 (Lines 500–551) | Wireless & Physical Connections includes enterprise WiFi (EAP/RADIUS), BLE stack, Zigbee/Z-Wave, LoRaWAN, TEMPEST concepts, and IoT protocols in the fundamentals. This is intermediate-to-advanced content placed before TCP/IP. | **High** | Move BLE/Zigbee/Z-Wave/LoRaWAN/IoT/TEMPEST to Phase 5 (Wireless & Mobile). Keep only WiFi fundamentals (802.11 standards, frequency bands, WPA basics) in Part 1. |
| 4 | Duplication | Parts 4, 5, 6 | Reconnaissance, scanning, and enumeration overlap heavily. Part 4 Phase 3 teaches Nmap scanning. Part 5 teaches Nmap scanning. Part 4 Phase 5 teaches SNMP/LDAP/NFS/RPC enumeration. Part 6 teaches the same SNMP/LDAP/NFS/RPC enumeration. | **High** | Consolidate: Part 4 = passive-only OSINT. Part 5 = all active scanning (host discovery + port scanning + version detection). Part 6 = all service enumeration (protocol-specific extraction). Remove duplicate Nmap/enumeration from Part 4. |
| 5 | Duplication | ARP Spoofing | Taught in Part 2 (Layer 2), Part 7 (System Hacking), Part 9 (Sniffing & Spoofing), Part 12 (Session Hijacking), and Part 21 (Wireless). Five separate treatments. | **High** | Teach ARP mechanics and spoofing once in Part 2. Reference it in later parts without re-teaching the technique. |
| 6 | Duplication | MITM Attacks | Covered in Part 7 (Phase 1), Part 9 (Phase 4), Part 12 (Stage 2–3), and Part 21 (Stage 3). Four separate near-identical treatments. | **High** | Consolidate MITM into Part 9 (Sniffing & Spoofing) as the authoritative section. Other parts reference it. |
| 7 | Duplication | LOLBAS/GTFOBins | Mentioned in Part 4 (Phase 4), Part 5 (Stage 4), Part 7 (Phase 2), Part 8 (Phase 2), Part 18 (Stage 4), and Part 40 (Red Team). Six separate mentions with varying depth. | **Medium** | Teach once in Part 7 (System Hacking). Cross-reference elsewhere. |
| 8 | Duplication | DNS Spoofing/Exfiltration | Covered in Part 2 (DNS section), Part 4, Part 7, Part 9, and Part 11. Five treatments. | **Medium** | Teach DNS mechanics in Part 2. Teach DNS attack techniques once in Part 9. |
| 9 | Duplication | Credential Theft (LSASS, Pass-the-Hash, Kerberoasting) | Covered in Part 7 (Phase 2–3), Part 23 (Stages 2–4), and Part 40 (Red Team). Triple coverage. | **Medium** | Part 23 is the authoritative AD credential section. Part 7 covers generic credential theft. Part 40 references both. |
| 10 | Missing Topic | Linux Administration | The Foundation Proof Gate (line 398) requires Linux admin skills, but no part teaches them. Part 1 covers OS internals (ring architecture, syscalls, PEB) but not practical Linux admin: package management, systemd, journalctl, firewall rules, networking config, disk management, cron, user management. | **Critical** | Add a dedicated "Linux System Administration" stage to Part 1, before the programming section. |
| 11 | Missing Topic | Windows Administration | Same as above. The proof gate demands Windows admin proof, but Part 1 covers OS internals (tokens, SIDs, NTFS), not practical admin: Event Viewer, services, Group Policy basics, PowerShell administration, networking, disk management. | **Critical** | Add a dedicated "Windows System Administration" stage to Part 1, before the programming section. |
| 12 | Bloat | Part 2 Networking (Lines 730–1527) | ~800 lines of networking content including deep Cisco-specific IOS configuration (DHCP server commands, NAT CLI, QoS profiles, WLAN GUI config, NTP master, SNMP community strings, EtherChannel configuration, Rapid PVST+ details). This is CCNA exam prep, not security fundamentals. | **High** | Trim Cisco-specific CLI commands to a brief reference. Focus on protocol concepts, security implications, and packet analysis. Move deep Cisco config to an optional "Network Engineering Reference" appendix. |
| 13 | Sequencing | Part 1 Stage 7 (Programming) after Stage 5b (Mobile Exploits) | Programming fundamentals are placed after mobile exploitation. The student is expected to bypass SSL pinning with Frida scripts before learning Python. | **Critical** | Move Programming (Stage 7) to be Stage 3 or 4 in Part 1, immediately after OS Internals and Memory Management. |
| 14 | Scope | Part 4 Phase 7 (Satellite & Geospatial Intelligence) | Satellite imagery, SIGINT, and geospatial triangulation are nation-state/military OSINT capabilities. Niche enough that it shouldn't be in the main progression. | **Low** | Mark as `[OPTIONAL SPECIALIZATION]` like Parts 30, 32, 33. |
| 15 | Quality | Part 1 Stage 4 (Data Representation) | Stage 4 repeats "Instruction Sets: Basic familiarity with Assembly (MOV, PUSH, POP, CALL, JMP)" — this is identical to the Stage 1 item on line 440. | **Medium** | Remove the duplicate from Stage 4. Keep it in Stage 1 where it belongs (CPU context). |
| 16 | Sequencing | Part 8 (Malware & Weaponization) in Phase 2 | Malware design, C2 protocol design, in-memory evasion, sleep obfuscation, call stack spoofing are placed in Phase 2 (Offensive Core). These require reverse engineering skills taught in Phase 7, Part 28. | **High** | Move Part 8 to Phase 7 (Advanced Specializations) after Part 28 (Reverse Engineering). You can't write evasive malware if you can't reverse engineer existing samples. |
| 17 | Time Estimate | Phase 3 (Defense & Detection) | 1–2 months full-time for Parts 13–16 covering SOC, SIEM, EDR/XDR/MDR, incident response, forensic fundamentals, threat hunting methodology, detection engineering, blue team evasion counter-measures, adversary emulation, and purple teaming. This is 6+ months of material compressed into 1–2. | **High** | Revise to 3–5 months full-time / 6–10 months part-time. This is as deep as the offensive core. |
| 18 | Time Estimate | Phase 7 (Advanced Specializations) | 3–5 months for Parts 27–34: Digital Forensics, Reverse Engineering, Modern Exploitation, Hardware Hacking, Password Cracking, Physical Pentesting, VoIP/Telecom, and Blockchain. Four of these are full specializations that take months each. | **High** | Revise to 6–12 months full-time. Alternatively, mark 4+ parts as optional specializations and keep 3–5 months for core parts only. |
| 19 | Missing Topic | Email Security (Standalone) | Email security is scattered across social engineering (phishing), OSINT (SPF/DKIM/DMARC), and cloud persistence. No consolidated treatment of email header analysis, mail flow, relay attacks, mail server hardening. | **Medium** | Add email security as a subsection of Part 2 (Application Layer) or Part 13 (Detection). |
| 20 | Missing Topic | Security Architecture & Zero Trust (Deep) | "Zero Trust" is mentioned in passing (Parts 14, 22) but never properly taught. No coverage of zero trust architecture, micro-segmentation strategy, identity-centric security, BeyondCorp model, or NIST SP 800-207. | **Medium** | Add a Zero Trust Architecture section to Part 14 or Part 35 (GRC). |
| 21 | Missing Topic | Incident Response (Standalone) | IR is a subsection of Part 13 (6 bullet points, lines 2704–2718). For a career-track roadmap targeting IR roles, this is severely underdeveloped. No coverage of IR team structure, communication protocols, legal holds, evidence preservation chain, third-party coordination, or tabletop exercises. | **High** | Expand IR into a standalone part or significantly expand the Part 13 section with IR team structure, communication, legal, and tabletop exercises. |
| 22 | Quality | Part 14 (IDS, Firewalls, Honeypots) | Uses backtick-quoted concept names like `Understand Concept of Defense in Depth`, `Perimeter vs DMZ vs Segmentation`, `Honeypots`. This reads like auto-generated cross-references to a glossary that doesn't exist. | **Low** | Replace backtick references with standard bold formatting and actual descriptions. |
| 23 | Missing Topic | Threat Modeling (Consolidated) | STRIDE is mentioned in Parts 35, 37, and 39, but there's no consolidated, hands-on threat modeling curriculum. Students need to practice DFDs, trust boundaries, and abuse cases as a standalone skill before it appears in three different contexts. | **Medium** | Add a focused threat modeling exercise to Part 1 or the Career Foundation section. |
| 24 | Quality | Part 11 (DoS) Stage 3 | Teaches "Botnet Assembly: Recruit thousands of infected IoT/servers" and "use existing botnet services (DDoS-as-a-Service)." Even with the safety gate, teaching botnet rental is operationally irresponsible for a learning roadmap. | **Medium** | Reframe as "Understand botnet economics and infrastructure" — study it, don't operate it. Focus on defense and detection, which is the employable skill. |
| 25 | Missing Topic | Log Analysis (Dedicated) | No standalone log analysis section. Log analysis appears scattered across forensics, SIEM, and IR. For SOC roles, dedicated log analysis skills (Windows Event IDs, Sysmon, Linux auth logs, web server logs, firewall logs, proxy logs) need focused training. | **Medium** | Add a dedicated log analysis subsection to Part 13 or create a standalone lab-focused module. |
| 26 | Sequencing | Part 31 (Password Cracking) in Phase 7 | Password cracking is placed after reverse engineering and modern exploitation. In practice, cracking captured hashes is needed immediately after enumeration (Phase 2). Students will be cracking NTLMv2 hashes from Responder in Part 7 labs. | **High** | Move Part 31 to Phase 2 (after Part 7) or consolidate into Part 7 as a subsection. |
| 27 | Missing Topic | Network Security Monitoring (NSM) | No coverage of Zeek/Bro, Security Onion as an NSM platform, network evidence collection, or NSM data types (full packet capture, session data, statistical data, alert data). Zeek is mentioned once (line 2766) in a lab bullet. | **Medium** | Add NSM fundamentals to Part 13 or Part 14. |
| 28 | Quality | Part 29 (Modern Exploitation) | Stage 2 references "SROP" without expansion. Stage 4 references "PPID spoofing" without explaining it. Multiple technique names are dropped without sufficient context for a learner to know what to study. | **Low** | Expand abbreviations and add one-sentence context for each advanced technique name. |
| 29 | Missing Topic | Windows Event Log Analysis (Specific IDs) | The roadmap mentions "Windows Event Logs" generically but never teaches specific critical Event IDs: 4624/4625 (logon), 4688 (process creation), 4672 (special privileges), 7045 (service install), 1102 (log cleared), Sysmon Event IDs 1, 3, 7, 8, 10, 11, 13, 22, 23. | **Medium** | Add a Windows Event Log deep-dive to Part 13 with specific Event IDs and detection use cases. |
| 30 | Duplication | Session Hijacking | Part 12 is entirely about session hijacking, but session hijacking techniques (cookie theft, token injection, replay attacks) are also covered in Part 7 (Phase 3), Part 9 (Phase 4), and Part 17 (Stage 3). | **Medium** | Consolidate: Part 12 is the authoritative section. Other parts cross-reference. |
| 31 | Missing Topic | Secure Coding Practices (Standalone) | Part 37 (DevSecOps) mentions SAST/DAST but secure coding practices are limited to 2 bullets in Part 17 (Stage 5). No OWASP Secure Coding Practices Quick Reference, no language-specific secure coding guidelines, no secure code review methodology. | **Medium** | Add secure coding fundamentals to Part 37 Stage 1 or create a pre-Part 17 secure coding module. |

---

## 3. Missing Topics

| Missing Topic | Why It Is Important | Where It Should Be Added |
|--------------|---------------------|--------------------------|
| **Linux System Administration** | Proof gate requires it. Every security role uses Linux daily. Can't do pentesting, forensics, or SOC work without it. | Part 1, new Stage between OS Internals and Programming |
| **Windows System Administration** | Same as above. AD attacks, malware analysis, forensics, EDR — all require Windows admin fluency. | Part 1, new Stage between OS Internals and Programming |
| **Zero Trust Architecture (NIST 800-207)** | Modern enterprise security architecture. Referenced but never taught. | Part 35 (GRC) or new section in Part 14 |
| **Incident Response (Expanded)** | 6 bullets is inadequate for a career-track skill. IR team structure, legal holds, tabletop exercises, communication protocols missing. | Expand Part 13 Phase 8 or create standalone Part |
| **Windows Event Log Analysis (Specific IDs)** | SOC analysts live in Event Viewer. Must know 4624, 4625, 4688, 4672, 7045, 1102, Sysmon IDs by heart. | Part 13, new subsection |
| **Network Security Monitoring (NSM)** | Zeek, Security Onion, full-packet capture analysis, network evidence. Core blue team skill. | Part 13 or Part 14 |
| **Secure Coding Practices** | Knowing how to find vulnerabilities without knowing how to fix them is half the skill. | Part 37 expansion |
| **Security Architecture Patterns** | Defense-in-depth is mentioned but DMZ design, network segmentation patterns, microsegmentation, SASE/SSE are not taught as design skills. | Part 14 expansion or new section |
| **Cloud-Native Logging & Monitoring** | CloudTrail, CloudWatch, Azure Monitor, GCP Cloud Logging, GuardDuty, Sentinel — none are covered in depth. | Part 24 expansion |
| **Email Security (Consolidated)** | Mail headers, relay chains, SPF/DKIM/DMARC deep-dive, O365 mail flow rules, mail server hardening. | Part 2 or Part 13 |
| **Tabletop Exercises** | IR tabletop exercises are the most common activity in enterprise security teams. Never mentioned. | Part 13 or Part 35 |
| **Security Metrics & Reporting (Operational)** | Beyond MTTD/MTTR. Coverage %, alert fidelity, detection lag, analyst utilization. | Part 13 or Part 35 |
| **Data Classification & Handling** | Roadmap mentions PII/PHI but never teaches formal data classification schemes (Public, Internal, Confidential, Restricted). | Part 35 (GRC) |

---

## 4. Wrong Topic Order Analysis

### Issue 1: Mobile Exploitation in Fundamentals

**Current Position:** Part 1, Stage 5b (Lines 586–601)
**Problem:** Jailbreak detection bypass, SSL pinning bypass, keychain extraction, Frida runtime manipulation, MDM bypass, enterprise app abuse, and mobile malware delivery are placed in "Fundamentals." The student hasn't learned TCP/IP, cryptography, or web security. You cannot bypass SSL pinning if you don't understand TLS. You cannot write Frida scripts if you don't know Python/JavaScript.
**Correct Position:** Part 22 (Mobile Platform Pentesting), Phase 5.
**Prerequisites Needed:** Part 2 (Networking), Part 3 (Cryptography), Part 7 (System Hacking), Part 17 (Web Application Hacking), Part 1 Stage 7 (Programming — Python/JavaScript).

---

### Issue 2: Document Weaponization in Fundamentals

**Current Position:** Part 1, Stage 6 (Lines 604–650)
**Problem:** VBA macro building, DDE abuse, OneNote/PDF weaponization, OAuth consent phishing, device code flow abuse, covert channel exfiltration, CASB/SWG evasion are placed before the student knows how a network packet works. These are Phase 2–7 level techniques.
**Correct Position:** Split across Part 8 (Malware & Weaponization) for document exploits and Part 23 (AD & Entra ID) for OAuth/device code attacks. Covert channels → Part 7 Phase 5.
**Prerequisites Needed:** Part 2 (Networking), Part 3 (Cryptography), Part 7 (System Hacking), Part 10 (Social Engineering).

---

### Issue 3: Programming After Mobile Exploitation

**Current Position:** Part 1, Stage 7 (Lines 652–727) — after Stage 5b (Mobile Exploits)
**Problem:** The student is expected to do Frida hooking, Cycript manipulation, and Burp proxy interception in Stage 5b before learning Python, JavaScript, C, or Assembly in Stage 7.
**Correct Position:** Programming should be Stage 3 (after Memory Management), before anything that requires writing or reading code.
**Prerequisites Needed:** Part 1 Stages 1–3 (Hardware, OS, Memory).

---

### Issue 4: Password Cracking in Phase 7

**Current Position:** Part 31 (Phase 7 — Advanced Specializations)
**Problem:** Password cracking is needed immediately in Phase 2. Kerberoasting (Part 7/23) produces hashes. Wireless handshake capture (Part 21) produces hashes. NTLM relay (Part 7) captures hashes. The student needs cracking skills by Phase 2, not Phase 7.
**Correct Position:** Move to Phase 2, immediately after Part 7 (System Hacking), or integrate as a subsection of Part 7.
**Prerequisites Needed:** Part 1 Stage 4 (Data Representation — hex, binary), Part 3 (Cryptography — hashing).

---

### Issue 5: Malware & Weaponization in Phase 2

**Current Position:** Part 8 (Phase 2 — Offensive Core)
**Problem:** In-memory evasion, sleep obfuscation, call stack spoofing, indirect syscalls, and C2 protocol design require reverse engineering skills (Part 28), which aren't taught until Phase 7. You can't evade EDR if you don't understand how EDR hooks work. You can't write shellcode if you haven't done Assembly (taught in Part 1 Stage 7 but not practiced until Part 29).
**Correct Position:** Move to Phase 7, after Part 28 (Reverse Engineering & Malware Analysis).
**Prerequisites Needed:** Part 28 (RE), Part 29 (Modern Exploitation), Part 1 Stage 7 (Assembly, C, C++).

---

## 5. Duplicate or Redundant Topics

| Topic | Found In | Recommended Action |
|-------|----------|-------------------|
| **ARP Spoofing** | Part 2, Part 7, Part 9, Part 12, Part 21 | Teach mechanics in Part 2. Teach attack technique once in Part 9. Cross-reference everywhere else. |
| **MITM Attacks** | Part 7, Part 9, Part 12, Part 21 | Part 9 is the authoritative MITM section. Remove full re-teachings from Parts 7, 12, 21. |
| **DNS Spoofing/Exfiltration** | Part 2, Part 4, Part 7, Part 9, Part 11 | Teach DNS mechanics in Part 2. DNS attacks in Part 9. DNS exfiltration in Part 7 (Phase 5). |
| **LOLBAS/GTFOBins** | Part 4, Part 5, Part 7, Part 8, Part 18, Part 40 | Teach once in Part 7 (System Hacking). Reference by name elsewhere. |
| **Kerberoasting/AS-REP Roasting** | Part 7, Part 23, Part 31, Part 40 | Part 23 is the authoritative Kerberos attack section. Part 31 covers the cracking angle. Parts 7 and 40 should cross-reference. |
| **Session Hijacking** | Part 7, Part 9, Part 12, Part 17 | Part 12 is the authoritative session hijacking section. Remove from Parts 7, 9, 17. |
| **Pass-the-Hash / Pass-the-Ticket** | Part 7, Part 8, Part 23, Part 40 | Part 23 (AD) and Part 7 (System Hacking) share this logically. Part 8 and 40 should cross-reference. |
| **SSL Stripping** | Part 2, Part 7, Part 9, Part 12 | Teach once in Part 9 (Sniffing & Spoofing). |
| **WAF/CDN Bypass** | Part 4 (Phase 2), Part 5 (Stage 6), Part 17 (Stage 5), Part 19 (Stage 5) | Consolidate into Part 17 (Web App) with a cross-reference from Part 5. |
| **Container Escape** | Part 7 (Phase 2), Part 24 (Stage 5), Part 25 (Stage 1) | Part 25 is the authoritative container security section. Remove from Part 7 and Part 24. |
| **Cloud IMDS/Metadata** | Part 7 (Phase 2), Part 17 (Stage 4), Part 24 (Stage 5), Part 29 (Stage 3) | Teach once in Part 24 (Cloud). Cross-reference from exploitation parts. |
| **Instruction Sets (Assembly)** | Part 1 Stage 1 (line 440), Part 1 Stage 4 (line 496) | Exact duplicate. Remove from Stage 4. |
| **Web Shell Deployment** | Part 7 (Phase 3), Part 17 (Stage 4), Part 18 (Stage 4) | Teach once in Part 17. Cross-reference from Parts 7 and 18. |
| **Evil Twin / Rogue AP** | Part 7 (Phase 1), Part 9 (Phase 4), Part 21 (Stage 3) | Part 21 (Wireless) is the authoritative section. Remove from Parts 7 and 9. |

**Impact of Duplication:** Conservatively, ~400–600 lines could be eliminated through proper cross-referencing. This would reduce the roadmap from 5,299 to ~4,700–4,900 lines without losing any coverage.

---

## 6. Formatting and Structure Issues

| Issue | Location | Detail |
|-------|----------|--------|
| **Stage numbering collision** | Part 1 | Stage 5 (Wireless) and Stage 5b (Mobile) — "5b" is not a proper numbering scheme. Should be Stage 5 and Stage 6. But the current Stage 6 is "Application Suites" and Stage 7 is "Programming." These need sequential renumbering. |
| **Inconsistent phase/stage naming** | Parts 4–12 vs Parts 13–16 | Parts 4–12 use "Phase 1, Phase 2..." within each part. Parts 13–16 also use "Phase 1, Phase 2..." This creates ambiguity. Part 13 Phase 8 vs top-level Phase 8 (GRC). |
| **Backtick-style cross-references** | Part 14 (Lines 2777–2831) | Uses `Understand Concept of Defense in Depth`, `Perimeter vs DMZ vs Segmentation`, `Honeypots` — looks like auto-generated glossary links that go nowhere. |
| **Backtick-style cross-references** | Parts 20, 22, 27 | Same issue. `Penetration Testing Rules of Engagement`, `OWASP10`, `Incident Response Process` — these inline backtick references don't link to anything. |
| **Inconsistent Stage vs Phase naming** | Across all parts | Some parts use "Stage 1, Stage 2" (Parts 1, 5, 6, 19, 21, 22, 23, 24, 25, 26). Other parts use "Phase 1, Phase 2" (Parts 4, 7, 8, 9, 13, 16). This is inconsistent. |
| **LaTeX syntax in markdown** | Line 442 | `$\rightarrow$` — LaTeX arrow that won't render in standard Markdown. Use `→` (Unicode arrow). |
| **Missing anchor** | Part 2 section headers | Lab Progression, Automation & Programmability sections within Part 2 lack anchor IDs, making them unreachable from the TOC. |
| **Optional marking inconsistency** | Parts 30, 32, 33, 34 | Parts 30, 32, 33 are marked `[OPTIONAL SPECIALIZATION]`. Part 34 (Blockchain) is also optional but not marked. |

---

## 7. Recommended Learning Order

This is the corrected, ideal sequence from absolute beginner to advanced. Changes from original are marked with `[MOVED]` or `[NEW]`.

### Phase 1 — Foundation (4–6 months full-time)

1. **Hardware, CPU & Pre-Boot** — Part 1 Stage 1
2. **Operating System Internals** — Part 1 Stage 2
3. **Memory Management** — Part 1 Stage 3
4. **Data Representation & Logic** — Part 1 Stage 4 (deduplicated)
5. **[NEW] Linux System Administration** — practical admin, not theory
6. **[NEW] Windows System Administration** — practical admin, not theory
7. **Programming & Scripting** — Part 1 Stage 7 `[MOVED UP]`
8. **WiFi Fundamentals Only** — Part 1 Stage 5 (stripped of BLE/Zigbee/IoT/TEMPEST)
9. **Mobile Platform Architecture Fundamentals Only** — Part 1 Stage 5b (stripped of offensive techniques)
10. **Networking Fundamentals** — Part 2 (trimmed of Cisco CLI bloat)
11. **Cryptography** — Part 3
12. **Foundation Proof Gate** — existing deliverables

### Phase 2 — Offensive Core (4–6 months full-time)

13. **Footprinting & Reconnaissance** — Part 4 (passive only, remove duplicate scanning/enumeration)
14. **Scanning** — Part 5
15. **Enumeration** — Part 6
16. **System Hacking & Initial Compromise** — Part 7
17. **Password Cracking & Hash Analysis** — Part 31 `[MOVED FROM PHASE 7]`
18. **Sniffing & Spoofing** — Part 9
19. **Session Hijacking** — Part 12
20. **Social Engineering** — Part 10
21. **Denial of Service** — Part 11

### Phase 3 — Defense & Detection (3–5 months full-time) `[EXPANDED]`

22. **Detection & Mitigation (Blue Team)** — Part 13 (expanded with Windows Event IDs, log analysis, NSM, expanded IR)
23. **IDS, Firewalls, and Honeypots** — Part 14
24. **OSINT & Threat Intelligence** — Part 15
25. **Adversary Emulation & Purple Teaming** — Part 16

### Phase 4 — Web & Application Security (2–3 months full-time)

26. **Web Application Hacking** — Part 17
27. **Web Server Hacking** — Part 18
28. **API Security** — Part 19
29. **Bug Bounty and Penetration Testing** — Part 20

### Phase 5 — Wireless & Mobile (1–2 months full-time)

30. **Wireless Pentesting** — Part 21 (now includes BLE/Zigbee/NFC/IoT content moved from Part 1)
31. **Mobile Platform Pentesting** — Part 22 (now includes offensive techniques moved from Part 1)

### Phase 6 — Infrastructure & Identity (2–3 months full-time)

32. **Active Directory & Entra ID** — Part 23
33. **Cloud Computing** — Part 24
34. **Container & Orchestration Security** — Part 25
35. **OT/ICS/SCADA Security** — Part 26

### Phase 7 — Advanced Specializations (6–12 months full-time) `[EXPANDED TIME]`

36. **Digital Forensics** — Part 27
37. **Reverse Engineering & Malware Analysis** — Part 28
38. **Malware & Weaponization** — Part 8 `[MOVED FROM PHASE 2]`
39. **Modern Exploitation** — Part 29
40. **Hardware Hacking** — Part 30 [OPTIONAL]
41. **Physical Penetration Testing** — Part 32 [OPTIONAL]
42. **VoIP & Telecommunications** — Part 33 [OPTIONAL]
43. **Blockchain & Web3 Security** — Part 34 [OPTIONAL]

### Phase 8 — GRC, Supply Chain & DevSecOps (1–2 months full-time)

44. **Governance, Risk & Compliance** — Part 35
45. **Supply Chain Security** — Part 36
46. **DevSecOps & Secure SDLC** — Part 37

### Phase 9 — AI Security (2–3 months full-time)

47. **AI & LLM Red Teaming** — Part 38

### Operations & Career (ongoing)

48. **Penetration Testing Methodologies & Report Writing** — Part 39
49. **Red Team Operations & Tradecraft** — Part 40
50. **Proof of Work & Career Portfolio** — Part 41

---

## 8. Fully Corrected Roadmap (Outline)

> [!NOTE]
> Providing a corrected structural outline. The original 5,299-line content is retained — this reorganizes and patches the structure. Implementing this as a full rewrite would produce a separate document.

```
Phase 1: Foundation (4-6 months FT / 8-12 months PT)
├── Career Foundation & Lab Setup (existing, keep as-is)
├── Part 1: Fundamentals
│   ├── Stage 1: Hardware, CPU & Pre-Boot (keep)
│   ├── Stage 2: Operating System Internals (keep)
│   ├── Stage 3: Memory Management (keep)
│   ├── Stage 4: Data Representation & Logic (remove duplicate Assembly item)
│   ├── Stage 5: Linux System Administration [NEW]
│   │   ├── Package management (apt/dnf/pacman)
│   │   ├── User/group/permissions/ACLs
│   │   ├── systemd/journalctl/cron
│   │   ├── Networking (ip, ss, nmcli, netplan)
│   │   ├── Firewall (iptables/nftables/ufw)
│   │   ├── Disk management (fdisk, lvm, mount)
│   │   ├── SSH administration
│   │   └── Log analysis (auth.log, syslog, journalctl)
│   ├── Stage 6: Windows System Administration [NEW]
│   │   ├── User/group management (GUI + PowerShell)
│   │   ├── Event Viewer (critical Event IDs)
│   │   ├── Services, Registry, Group Policy basics
│   │   ├── PowerShell administration
│   │   ├── Windows networking (ipconfig, netstat, route)
│   │   ├── Windows Firewall
│   │   ├── Disk management
│   │   └── Windows Defender / security settings
│   ├── Stage 7: Programming & Exploit Languages (MOVED UP from Stage 7)
│   ├── Stage 8: WiFi & Physical Layer Fundamentals (trimmed Stage 5)
│   └── Stage 9: Mobile Platform Architecture Fundamentals (trimmed Stage 5b)
│   [REMOVED from Part 1: Document weaponization → Part 8]
│   [REMOVED from Part 1: Mobile offensive techniques → Part 22]
│   [REMOVED from Part 1: BLE/Zigbee/IoT/TEMPEST → Part 21]
│   [REMOVED from Part 1: Cloud persistence/exfil → Part 24]
├── Part 2: Networking Fundamentals (trimmed of Cisco CLI bloat)
├── Part 3: Cryptography (keep)
└── Foundation Proof Gate (keep)

Phase 2: Offensive Core (4-6 months FT / 8-12 months PT)
├── Part 4: Footprinting & Reconnaissance (passive only, remove active scanning duplication)
├── Part 5: Scanning (all active scanning consolidated here)
├── Part 6: Enumeration (all service enumeration consolidated here)
├── Part 7: System Hacking & Initial Compromise (keep, deduplicate cross-referenced techniques)
├── Part 31: Password Cracking & Hash Analysis [MOVED HERE]
├── Part 9: Sniffing & Spoofing (authoritative MITM/ARP/DNS spoofing section)
├── Part 12: Session Hijacking (keep, deduplicate)
├── Part 10: Social Engineering (keep)
└── Part 11: Denial of Service (keep, reframe botnet section)

Phase 3: Defense & Detection (3-5 months FT / 6-10 months PT) [EXPANDED]
├── Part 13: Detection & Mitigation (expanded)
│   ├── [EXPANDED] Windows Event Log Analysis (specific IDs)
│   ├── [EXPANDED] Incident Response (standalone depth)
│   ├── [NEW] Network Security Monitoring (Zeek, Security Onion)
│   ├── [NEW] Log Analysis (dedicated)
│   └── [NEW] Tabletop Exercises
├── Part 14: IDS, Firewalls, and Honeypots (fix backtick references)
│   └── [NEW] Zero Trust Architecture section
├── Part 15: OSINT & Threat Intelligence (keep)
└── Part 16: Adversary Emulation & Purple Teaming (keep)

Phase 4: Web & App Security (2-3 months FT / 4-6 months PT)
├── Part 17: Web Application Hacking (keep)
├── Part 18: Web Server Hacking (keep, deduplicate)
├── Part 19: API Security (keep)
└── Part 20: Bug Bounty & Penetration Testing (keep)

Phase 5: Wireless & Mobile (1-2 months FT / 2-4 months PT)
├── Part 21: Wireless Pentesting (absorb BLE/Zigbee/IoT from Part 1)
└── Part 22: Mobile Platform Pentesting (absorb offensive techniques from Part 1)

Phase 6: Infrastructure & Identity (2-3 months FT / 4-6 months PT)
├── Part 23: Active Directory & Entra ID (keep, deduplicate credential attacks)
├── Part 24: Cloud Computing (keep, add cloud-native logging)
├── Part 25: Container & Orchestration Security (keep)
└── Part 26: OT/ICS/SCADA Security (keep)

Phase 7: Advanced Specializations (6-12 months FT / 12-24 months PT) [EXPANDED TIME]
├── Part 27: Digital Forensics (keep)
├── Part 28: Reverse Engineering & Malware Analysis (keep)
├── Part 8: Malware & Weaponization [MOVED HERE — requires RE skills]
├── Part 29: Modern Exploitation (keep)
├── Part 30: Hardware Hacking [OPTIONAL] (keep)
├── Part 32: Physical Penetration Testing [OPTIONAL] (keep)
├── Part 33: VoIP & Telecommunications [OPTIONAL] (keep)
└── Part 34: Blockchain & Web3 Security [OPTIONAL, add label] (keep)

Phase 8: GRC, Supply Chain & DevSecOps (1-2 months FT / 2-4 months PT)
├── Part 35: GRC (keep, add data classification + zero trust if not in Part 14)
├── Part 36: Supply Chain Security (keep)
└── Part 37: DevSecOps & Secure SDLC (keep, add secure coding practices)

Phase 9: AI Security (2-3 months FT / 4-6 months PT)
└── Part 38: AI & LLM Red Teaming (keep — this is well done)

Operations & Career (ongoing)
├── Part 39: Penetration Testing Methodologies & Report Writing (keep)
├── Part 40: Red Team Operations & Tradecraft (keep)
└── Part 41: Proof of Work & Career Portfolio (keep)
```

### Corrected Time Estimates

| Phase | Full-Time | Part-Time |
|-------|-----------|-----------|
| Phase 1: Foundation | 4–6 months | 8–12 months |
| Phase 2: Offensive Core | 4–6 months | 8–12 months |
| Phase 3: Defense & Detection | 3–5 months | 6–10 months |
| Phase 4: Web & App Security | 2–3 months | 4–6 months |
| Phase 5: Wireless & Mobile | 1–2 months | 2–4 months |
| Phase 6: Infrastructure & Identity | 2–3 months | 4–6 months |
| Phase 7: Advanced Specializations | 6–12 months | 12–24 months |
| Phase 8: GRC, Supply Chain & DevSecOps | 1–2 months | 2–4 months |
| Phase 9: AI Security | 2–3 months | 4–6 months |
| **Total (core only, no optionals)** | **~28–46 months** | **~54–90 months** |

---

## 9. Practical Learning Layer

### Phase 1: Foundation

| Skill Area | Labs / Projects | Platforms |
|-----------|----------------|-----------|
| Linux Admin | OverTheWire Bandit (all 34 levels), build a LAMP stack, configure SSH/firewall/cron from scratch | OverTheWire, TryHackMe (Linux Fundamentals path) |
| Windows Admin | Build AD lab (DC + workstation), manage users/GPO/services via PowerShell | TryHackMe (Windows Fundamentals), home lab |
| Networking | Packet Tracer topology labs → GNS3 with Wireshark validation, capture 10 protocol PCAPs | Cisco Packet Tracer, GNS3, Wireshark |
| Programming | Build 3 tools: port scanner (Python), log parser (Bash), HTTP requester (Python) | Home lab, GitHub |
| Cryptography | Hash lab, TLS handshake capture, local CA build, post-quantum awareness doc | Home lab, Wireshark |

### Phase 2: Offensive Core

| Skill Area | Labs / Projects | Platforms |
|-----------|----------------|-----------|
| Recon/Scanning/Enum | Complete TryHackMe Offensive Pentesting path, 10 HTB easy machines | TryHackMe, HackTheBox, VulnHub |
| System Hacking | 5 intentionally vulnerable VMs with full writeups (initial access → privesc → evidence) | HackTheBox, VulnHub, TryHackMe |
| Password Cracking | Crack lab-generated NTLM, NTLMv2, WPA2, Kerberos hashes with Hashcat/JtR | Home lab |
| Sniffing/Spoofing | ARP spoof + MITM in isolated lab, capture and analyze 5 attack PCAPs | Home lab (Bettercap, Wireshark) |
| Social Engineering | GoPhish simulation against test inboxes, SPF/DKIM/DMARC lab setup | GoPhish, home lab mail server |

### Phase 3: Defense & Detection

| Skill Area | Labs / Projects | Platforms |
|-----------|----------------|-----------|
| SIEM/Detection | Deploy Wazuh or ELK, ingest logs, write 10 detection queries | Wazuh, ELK, Security Onion |
| Detection Rules | Write 5 Sigma rules, 3 YARA rules, test against lab activity | Home lab |
| Incident Response | Reconstruct 2 incidents from logs, produce analyst reports | CyberDefenders, Blue Team Labs Online, LetsDefend |
| Forensics | Memory analysis (Volatility), disk imaging (FTK Imager), timeline construction | CyberDefenders, TryHackMe |
| Threat Hunting | Formulate 3 hypotheses, hunt in SIEM, document findings | Home lab, CyberDefenders |

### Phase 4: Web & App Security

| Skill Area | Labs / Projects | Platforms |
|-----------|----------------|-----------|
| Web Hacking | Complete PortSwigger Web Security Academy (all labs), target BSCP certification | PortSwigger Academy |
| API Security | Test OWASP API Top 10 against crAPI, DVGA (GraphQL) | crAPI, DVGA, PentesterLab |
| Bug Bounty | Start on HackerOne/Bugcrowd, find first 10 valid findings | HackerOne, Bugcrowd, Intigriti |

### Phase 5: Wireless & Mobile

| Skill Area | Labs / Projects | Platforms |
|-----------|----------------|-----------|
| Wireless | Capture WPA2 handshake in own lab, evil twin setup (isolated), WPS Pixie Dust | Home lab (Alfa adapter) |
| Mobile | OWASP MASTG exercises, Frida labs on intentionally vulnerable apps | MOBISEC, DIVA, InsecureBankv2, MSTG labs |

### Phase 6: Infrastructure & Identity

| Skill Area | Labs / Projects | Platforms |
|-----------|----------------|-----------|
| Active Directory | GOAD lab, BloodHound ingest + path validation, Kerberoast/AS-REP roast lab | GOAD, DetectionLab, PurpleCloud |
| Cloud | AWS/Azure free tier VPC build, Terraform IaC, IAM exploitation with Pacu/ScoutSuite | CloudGoat, flAWS, SadCloud |
| Containers | Kubernetes Goat, container escape lab, Trivy image scanning | Kubernetes Goat, home lab |

### Phase 7: Advanced Specializations

| Skill Area | Labs / Projects | Platforms |
|-----------|----------------|-----------|
| Forensics | 5 CyberDefenders challenges, Autopsy/Volatility workflow | CyberDefenders |
| Reverse Engineering | FLARE VM setup, 5 crackmes, 3 malware samples (training only), 1 full analysis report | FLARE VM, REMnux, crackmes.one, MalwareBazaar |
| Modern Exploitation | pwn.college, ROP Emporium, 1 fuzzing lab with AFL++ | pwn.college, ROP Emporium, Exploit Education |

### Phase 8: GRC & DevSecOps

| Skill Area | Labs / Projects | Platforms |
|-----------|----------------|-----------|
| GRC | Build risk register, write 2 policies, control mapping exercise | Home lab / document-based |
| DevSecOps | GitHub Actions pipeline with Semgrep + gitleaks + Trivy, break-the-build gate | GitHub, home projects |
| Supply Chain | SBOM generation with CycloneDX, dependency confusion awareness lab | Home projects |

### Phase 9: AI Security

| Skill Area | Labs / Projects | Platforms |
|-----------|----------------|-----------|
| LLM Red Teaming | Gandalf AI CTF, HackAPrompt, OWASP AI Goat, local Ollama + Open WebUI lab | Gandalf, HackAPrompt, home lab (Ollama) |
| AI Tools | Build LangChain security agent, PyRIT/Garak testing against local models | Home lab, GitHub |
| AI Projects | 2-3 AI security tools on GitHub, technical writeups on Medium/blog | GitHub, Medium |

---

## 10. Final Verdict

### Is this roadmap realistic?

**Partially.** The breadth is real and the topics are legitimate. But the time estimates are delusional for a true beginner. The original 18–30 months full-time claim for 41 parts would require someone who already has strong IT fundamentals to sprint through. For someone starting from scratch, 30–48 months full-time is realistic for core phases. With optional specializations, 4–5 years part-time.

### What are its biggest weaknesses?

1. **Premature offensive content in fundamentals.** This is the single biggest structural flaw. Mobile exploitation, document weaponization, and OAuth abuse in Part 1 before the student knows TCP/IP is pedagogically dangerous — it teaches pattern-matching ("type this command") instead of understanding.
2. **No explicit Linux/Windows admin curriculum.** The roadmap demands admin skills in its proof gate but never teaches them. This is a foundational gap that will create fragile offensive skills built on shaky operational knowledge.
3. **Massive duplication inflates the document.** The same techniques are taught 4–6 times across different parts. This creates the illusion of depth while actually being repetition.
4. **Defense phase is severely underweighted.** 1–2 months for blue team vs. 3–4 months for offensive core reveals a bias. In reality, most entry-level security jobs are defensive (SOC, IR, detection engineering).

### What will it fail to teach?

- **Practical system administration** — the student will know how a syscall works but not how to configure a firewall or manage users
- **Security architecture design** — how to design a secure network from scratch, not just attack one
- **Operational SOC workflow** — the daily grind of alert triage, escalation, reporting, and tool operation
- **Communication skills** — how to write for executives, present to boards, or explain risk to non-technical stakeholders (touched briefly in Part 39 but not practiced)
- **Team operations** — how to work in a SOC, red team, or IR team with other humans

### How long would completion realistically take?

| Scenario | Time |
|----------|------|
| Full-time, strong IT background | 24–36 months |
| Full-time, complete beginner | 36–48 months |
| Part-time, strong IT background | 48–72 months |
| Part-time, complete beginner | 60–90 months (5–7.5 years) |

### Would you personally recommend this roadmap?

**Yes, with corrections.** After fixing the sequencing issues (move offensive content out of fundamentals, add Linux/Windows admin, reorder programming), deduplicating content, expanding the defense phase, and adjusting time estimates — this roadmap is better than 95% of what's available publicly. The AI security section alone is worth the price of admission.

The author's instinct to build from hardware up, demand proof artifacts, include safety gates, and extend into AI security is strategically sound. The execution just needs the structural corrections documented above.

### What would you change to become an elite cybersecurity professional?

1. **Fix the sequencing.** Apply the corrected order from Section 7 of this audit. No offensive techniques before networking and crypto.
2. **Add 2 months of pure Linux/Windows admin.** You cannot hack what you cannot operate. Period.
3. **Double the defense time.** Most of your career will be spent detecting, not exploiting. Even red teamers need to understand what defenders see.
4. **Build in public from Day 1.** Don't wait for Phase 9 to start your GitHub/blog. Document every lab from Phase 1. Your lab notes *are* your portfolio.
5. **Specialize after Phase 4.** You don't need all 8 optional specializations. Pick 1–2 that align with your target role and go deep instead of wide.
6. **Get real-world experience by Phase 3.** Internship, SOC role, IT helpdesk — anything. The roadmap can't teach you how to operate under pressure, communicate with non-technical people, or navigate organizational politics.
7. **Stop treating certifications as the goal.** OSCP is proof you can pass a 24-hour exam. It's not proof you can run a real engagement. Build tools, find bugs, write reports. Those are unfakeable.

---

> **Final Note:** This roadmap is a weapon if sharpened correctly. The raw material is excellent. The structural issues are fixable. Apply the corrections, respect the time estimates, and build proof at every stage. The roadmap doesn't need more content — it needs better architecture.
