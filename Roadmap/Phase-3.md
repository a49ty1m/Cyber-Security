# Phase 3: Defense & Detection

---

### 🧭 Navigation
◀ [Phase 2](Phase-2.md) | 🏠 [Master Roadmap](README.md) | [Phase 4](Phase-4.md) ➔

---

> [!NOTE]
> **Phase Overview**
> - **⏱️ Time Commitment (Full-Time):** 4–6 months
> - **⏱️ Time Commitment (Part-Time):** 6–10 months
> - **🎯 Primary Focus:** Detection engineering, SOC & SIEM fundamentals, IDS/IPS/honeypots, threat hunting, incident response basics, forensic fundamentals, and OSINT & threat intelligence. Understand what defenders see before you specialize further.

---

> [!NOTE]
> ### 📝 Phase 3 Documentation Requirements
> Every detection and investigation you perform must be documented. Required artifacts:
> - **Detection rule documentation** — Sigma rules, YARA signatures, and Suricata rules with rationale and test evidence
> - **Sigma rule library (APT-derived)** — at least 3 Sigma rules written from a real APT report's TTPs, tested against lab activity, with SIEM alert screenshots proving they fire
> - **PCAP analysis notes** — annotated packet captures explaining what you found and why it matters
> - **SIEM dashboard screenshots** — saved views showing alert correlation and investigation workflows
> - **IR timeline documentation** — structured incident timelines (who, what, when, where, how)
> - **IR Playbook document** — a complete, structured ransomware response playbook covering detection → isolation → evidence preservation → eradication → recovery → post-incident report
> - **Threat intelligence report** — a structured TI report on one APT group: TTPs, IOCs, STIX format, and operational recommendations
> - **Git commits** — all rules, queries, playbooks, and analysis notes committed to your repository
>
> _By the end of Phase 3, you should have a detection rule library, a working IR playbook, an APT-derived Sigma rule set, and an investigation artifact collection in your repository._


---

### 🗂️ Table of Contents
- [Part 13A: Detection Engineering & SOC Operations](#part-13a-detection-engineering-soc-operations)
  - [Stage 1: Defensive Architecture](#stage-1-defensive-architecture)
  - [Stage 2: Offensive Indicators & TTPs](#stage-2-offensive-indicators-ttps)
  - [Stage 3: Evasion Detection & Hardening](#stage-3-evasion-detection-hardening)
  - [Stage 4: Detection Engineering & Response](#stage-4-detection-engineering-response)
  - [Stage 5: EDR/XDR/MDR Basics](#stage-5-edrxdrmdr-basics)
  - [Stage 6: SOC & SIEM Fundamentals](#stage-6-soc-siem-fundamentals)
  - [Stage 7: Threat Hunting Methodology](#stage-7-threat-hunting-methodology)
  - [Stage 8: Incident Response Basics](#stage-8-incident-response-basics)
  - [Stage 9: Forensic Fundamentals](#stage-9-forensic-fundamentals)
  - [Stage 10: Blue Team Evasion Counter-Measures](#stage-10-blue-team-evasion-counter-measures)
- [Part 13B: Security Operations Expansion](#part-13b-security-operations-expansion)
  - [Stage 11: Security Orchestration, Automation & Response (SOAR)](#stage-11-security-orchestration-automation-response-soar)
  - [Stage 12: Data Loss Prevention (DLP) Fundamentals](#stage-12-data-loss-prevention-dlp-fundamentals)
  - [Stage 13: Vulnerability Management Program](#stage-13-vulnerability-management-program)
  - [Stage 14: Insider Threat Detection](#stage-14-insider-threat-detection)
  - [Lab Progression (Parts 13A + 13B Combined)](#lab-progression-parts-13a-13b-combined)
- [Part 14: IDS, Firewalls, and Honeypots](#part-14-ids-firewalls-and-honeypots)
  - [Stage 1: Foundational Strategy & Networking](#stage-1-foundational-strategy-networking)
  - [Stage 2: Deploying Firewalls (The Shield)](#stage-2-deploying-firewalls-the-shield)
  - [Stage 3: Implementing IDS/IPS (The Watchers)](#stage-3-implementing-idsips-the-watchers)
  - [Stage 4: Utilizing Deception (The Traps)](#stage-4-utilizing-deception-the-traps)
  - [Stage 5: Operations & Continuous Improvement](#stage-5-operations-continuous-improvement)
  - [Stage 6: Email Security Architecture](#stage-6-email-security-architecture)
  - [Stage 7: DNS Security Operations](#stage-7-dns-security-operations)
  - [Lab Progression (Part 14: IDS, Firewalls, and Honeypots)](#lab-progression-part-14-ids-firewalls-and-honeypots)
- [Part 15: OSINT & Threat Intelligence](#part-15-osint-threat-intelligence)
  - [Stage 1: Passive Reconnaissance & Data Collection](#stage-1-passive-reconnaissance-data-collection)
  - [Stage 2: Threat Intelligence Analysis](#stage-2-threat-intelligence-analysis)
  - [Stage 3: OSINT Automation & Tooling](#stage-3-osint-automation-tooling)
  - [Stage 4: Threat Intelligence Dissemination](#stage-4-threat-intelligence-dissemination)
  - [Stage 5: Threat Intel Operationalization](#stage-5-threat-intel-operationalization)
  - [Lab Progression (Part 15: OSINT & Threat Intelligence)](#lab-progression-part-15-osint-threat-intelligence)
  - [GRC Fundamentals Sidebar (Early Supplement for Defensive Careers)](#grc-fundamentals-sidebar-early-supplement-for-defensive-careers)

---

<a id="part-13a-detection-engineering-soc-operations"></a>
## Part 13A: Detection Engineering & SOC Operations

_Understand defensive detection to know what to evade. This Part covers core detection engineering, SIEM, threat hunting, incident response, and forensic fundamentals (Stages 1–10). Security operations expansion topics (SOAR, DLP, Vulnerability Management, Insider Threat) continue in Part 13B._

<a id="stage-1-defensive-architecture"></a>
### **Stage 1: Defensive Architecture**

- [ ] **Defense-In-Depth:** Layer **EDR, SIEM, CASB, firewall, WAF, IDS/IPS, DNS filtering** with **proper tuning** to reduce false positives and enable hunting.

- [ ] **Threat Hunting:** Proactively search for **suspicious patterns** (parent/child process anomalies, unsigned DLLs, scheduled task abuse, registry modifications) using **Sigma rules, YARA, KQL**.

- [ ] **Incident Response Plan:** Document **detection, containment, eradication, recovery, lessons learned** phases with **clear ownership and escalation paths**.

---

<a id="stage-2-offensive-indicators-ttps"></a>
### **Stage 2: Offensive Indicators & TTPs**

- [ ] **IOC Identification:** Recognize **file hashes, domains, IPs, email patterns, behavioral signatures** that map to known attack frameworks (Cobalt Strike, [Metasploit](../Tools/Metasploit_Framework.md), custom).

- [ ] **MITRE ATT&CK Mapping:** Correlate **detected behaviors** to **tactics/techniques** to understand adversary intent and prioritize detection investment.

- [ ] **Artifact Analysis:** Understand forensic artifacts (prefetch, MFT, journal logs, browser history, registry hives, event logs) as **evidence of compromise**.

---

<a id="stage-3-evasion-detection-hardening"></a>
### **Stage 3: Evasion Detection & Hardening**

- [ ] **Living-off-the-Land Detection:** Monitor **native binary execution** (PowerShell, WMI, certutil, mshta, bitsadmin) with **process whitelisting, memory pattern analysis, and behavioral indicators**.

- [ ] **Obfuscation Analysis:** Detect **encoded payloads, packed executables, script obfuscation** via **entropy analysis, dynamic detonation, behavioral sandboxing**.

- [ ] **Anti-Forensics Detection:** Identify **log clearing, file timestomping, registry deletion, bash history removal** via **SIEM correlation and immutable audit logs**.

- [ ] **Command-Line Auditing:** Enable and monitor **PowerShell transcript logging, command-line audit logs (4688), script block logging** for obfuscated execution.

---

<a id="stage-4-detection-engineering-response"></a>
### **Stage 4: Detection Engineering & Response**

- [ ] **Detection Rules:** Write **Sigma, Snort/Suricata, Yara, osquery** rules targeting **adversary TTPs** from reconnaissance to exfiltration.

- [ ] **Alert Tuning:** Baseline **normal traffic/processes**, establish **alert thresholds**, reduce **false positives** to improve SOC efficiency.

- [ ] **SOC Playbooks:** Document **runbooks** for each alert type: **triage → validation → containment → remediation → documentation**.

- [ ] **Threat Intelligence Integration:** Consume **OSINT feeds, MISP, AlienVault OTX, commercial threat intel** to enrich **IP/domain/file lookups** in SIEM.

> [!IMPORTANT]
> **Stage Gate — Stages 1–4 (Detection Engineering):** Before proceeding to Stage 5, you must demonstrate:
> - [ ] Written at least 1 working Sigma rule that fires on a specific MITRE ATT&CK technique in a live SIEM
> - [ ] Identified 3 LOLBin execution patterns (e.g., certutil download, mshta execution, bitsadmin transfer) and named the event log source for each
> - [ ] Documented what anti-forensics evidence looks like in a Windows Event Log (e.g., event 1102 log cleared, event 4719 audit policy changed)
> - [ ] Explained the difference between signature-based detection and behavioral detection with a concrete example of a technique each approach would and would not catch

---

<a id="stage-5-edrxdrmdr-basics"></a>
### **Stage 5: EDR/XDR/MDR Basics**

> [!TIP]
> **Goal:** Understand modern endpoint and extended detection capabilities.

- [ ] **EDR Architecture:** Understand **agent-based detection (process, file, registry, network), telemetry collection, cloud backend, response orchestration**.

- [ ] **EDR Capabilities:** Know **behavioral analysis, memory scanning, AMSI integration, ETW collection, indicator of compromise (IOC) matching**.

- [ ] **EDR Evasion vs. Detection:** Understand **living-off-the-land techniques EDR detects**, **code injection detection**, **DLL side-loading detection**.

- [ ] **XDR Approach:** Understand how **XDR correlates endpoint, network, cloud, identity signals** for **detection, hunting, response** across domains.

- [ ] **MDR Services:** Know what **Managed Detection & Response (MDR)** providers offer: **24/7 monitoring, incident response, threat hunting, consulting**.

---

<a id="stage-6-soc-siem-fundamentals"></a>
### **Stage 6: SOC & SIEM Fundamentals**

> [!TIP]
> **Goal:** Understand Security Operations Center workflow and SIEM correlation.

- [ ] **SIEM Basics:** Understand **log aggregation, parsing, normalization, correlation, enrichment** using tools like **Splunk, ELK, ArcSight, QRadar**.

- [ ] **Log Collection:** Know what logs to collect: **Windows Event Logs, Sysmon, firewall logs, proxy logs, DNS logs, authentication logs, application logs**.

- [ ] **Alert Correlation:** Understand **multi-stage detection** (e.g., suspicious logon + process creation + network connection = lateral movement indicator).

- [ ] **SOC Workflow:** Understand **analyst triage → escalation → incident investigation → containment → reporting** process and metrics (MTTD, MTTR).

- [ ] **Dashboard & KPIs:** Know key metrics: **alert volume, MTTD/MTTR, false positive rate, detection coverage %, incident severity distribution**.

- [ ] **SIEM Query Language Fluency:** Compare **SPL (Splunk)**, **KQL (Microsoft Sentinel/Defender)**, and **Lucene/EQL (Elastic/OpenSearch)** syntax for the same detection logic — write the same alert (e.g., "failed logins > 10 in 5 minutes from same source") in all three languages. Maintain a personal cheat sheet mapping equivalent operators across platforms.

> [!IMPORTANT]
> **Stage Gate — Stage 6 (SOC/SIEM):** Before proceeding to Stage 7 (Threat Hunting), you must demonstrate:
> - [ ] Deployed a working SIEM (Splunk Free, Wazuh, ELK, or Security Onion) ingesting logs from at least 3 sources (e.g., Windows Event, Sysmon, Linux auth, DNS)
> - [ ] Written the same alert rule in at least 2 SIEM query languages (SPL, KQL, or Lucene)
> - [ ] Investigated a real alert end-to-end: triage → validate → document → close — without walkthrough assistance
> - [ ] Can name the 5 most important Windows Event IDs for detecting initial access and lateral movement and explain what each one captures

---

<a id="stage-7-threat-hunting-methodology"></a>
### **Stage 7: Threat Hunting Methodology**

> [!TIP]
> **Goal:** Learn proactive threat hunting to find advanced threats.

- [ ] **Hunting Hypotheses:** Formulate hypotheses based on **MITRE ATT&CK, threat reports, prior compromises** (e.g., "Are scheduled tasks being abused?").

- [ ] **Data Source Selection:** Choose **event logs, network traffic, process telemetry, file integrity monitoring** appropriate for hypothesis.

- [ ] **Query Construction:** Build **SQL, KQL, SPL queries** in SIEM to **search for patterns** (unusual process chains, rare executables, domain queries).

- [ ] **Pivot & Correlate:** Use **results to pivot** (e.g., find account → check all logons → find source IP → check all connections).

- [ ] **Validation & Documentation:** Confirm findings are **actual compromise vs. false positive**, document **timeline, IOCs, and response**.

- [ ] **Jupyter Notebook Threat Hunting:** Mature threat hunting programmes use Jupyter notebooks (JupyterHub or VS Code Jupyter extension) as the primary analysis environment: SIEM or Elasticsearch data pulled via API into pandas DataFrames, statistical anomaly detection with scipy/scikit-learn, and visualisation with matplotlib/seaborn. Reproducible **"hunt books"** — notebooks committed to Git and peer-reviewed — are the production standard at Microsoft MSTIC, Elastic Security Labs, and SANS Hunt teams. Study the [MSTICPy library](https://github.com/microsoft/msticpy) (Microsoft Threat Intelligence Center's open-source hunting library): it provides pre-built connectors for Microsoft Sentinel, Splunk, and QRadar, plus entity enrichment, IOC lookup, and timeline visualisation. Hunt books treat detection logic as code: version-controlled, diff-able, and testable — the same shift-left discipline that CI/CD brought to application code.

---

<a id="stage-8-incident-response-basics"></a>
### **Stage 8: Incident Response Basics**

> [!TIP]
> **Goal:** Understand the incident response lifecycle.

- [ ] **Detection & Analysis:** Receive **alert/complaint → triage → determine if real incident → declare incident**.

- [ ] **Containment Strategy:** Short-term: **isolate affected systems**; Long-term: **fix vulnerabilities, update passwords, patch**.

- [ ] **Eradication:** **Remove attacker access** (reset creds, close backdoors, patch exploited systems), verify **persistence mechanisms** removed.

- [ ] **Recovery:** **Restore systems to known good state**, rebuild compromised hosts, verify **no re-infection**.

- [ ] **Lessons Learned:** **Timeline analysis, root cause, detection gaps, improve controls** to prevent recurrence.

- [ ] **Forensic Preservation:** During response, **preserve evidence** (memory dumps, disk images, logs) for **investigation and legal proceedings**.

> [!IMPORTANT]
> **Stage Gate — Stage 8 (Incident Response):** Before proceeding to Stage 9 (Forensics), you must demonstrate:
> - [ ] Produced a structured incident timeline for a simulated incident containing: first indicator, initial compromise, lateral movement, data access/impact, and containment actions — with timestamps and evidence sources for each entry
> - [ ] Written a containment playbook for at least 1 attack scenario (ransomware or credential theft) covering: isolation steps, evidence preservation order, communication contacts, and rollback criteria
> - [ ] Explained the distinction between containment and eradication — and why premature eradication destroys forensic evidence

---

<a id="stage-9-forensic-fundamentals"></a>
### **Stage 9: Forensic Fundamentals**

> [!TIP]
> **Goal:** Collect and analyze evidence of compromise.

- [ ] **Live Response:** Collect **running processes, network connections, logged-in users, active services** before shutdown (loses volatile data).

- [ ] **Disk Imaging:** Create **bit-for-bit copy** of drives for **offline analysis**, use tools like **dd, Acquire, [FTK Imager](../Tools/FTK_Imager.md)**.

- [ ] **Timeline Analysis:** Build **chronological timeline** of **file creation/modification, registry changes, logs** to reconstruct **attack sequence**.

- [ ] **Artifact Examination:** Analyze **Windows Prefetch, Shimcache, MRU, Recycle Bin, browser history, temp files** for **evidence of compromise**.

- [ ] **Memory Analysis:** Use tools like **[Volatility](../Tools/Volatility.md), Rekall** to extract **running processes, injected code, encryption keys, command history** from memory dumps.

---

<a id="stage-10-blue-team-evasion-counter-measures"></a>
### **Stage 10: Blue Team Evasion Counter-Measures**

> [!TIP]
> **Goal:** Know how defenders detect and counter red team techniques.

- [ ] **Process Whitelisting:** Defenders use **AppLocker, Device Guard** to allow only **approved executables**; evade via **living-off-the-land** or **trusted paths**.

- [ ] **Memory Protection:** Defenders enable **DEP/NX, ASLR, CET**; understand these reduce **code injection effectiveness**.

- [ ] **Signing Checks:** Defenders verify **code signatures**; exploit **weak validation** or **stolen certificates**.

- [ ] **Logging & Audit:** Defenders enable **command-line logging, PowerShell block logging, Sysmon, ETW**; evade via **log tampering or memory-only payloads**.

- [ ] **Behavioral Blocking:** EDRs use **behavior analysis** to block **suspicious chains** (e.g., Office → PowerShell → network); develop awareness of **detectable patterns**.

- [ ] **Alert Tuning:** Build **low false-positive alerts** for high-confidence indicators (e.g., AMSI evasion, direct syscalls, token theft patterns).

- [ ] **Playbook Development:** Create **runbooks** for common attack patterns (ransomware deployment, credential theft, lateral movement) with **clear triage and containment steps**.

- [ ] **Purple Teaming:** Partner with red teams to **validate detections, test response procedures, and measure MTTD (Mean Time to Detect) and MTTR (Mean Time to Respond)**.

---

**Move-On Gate (Part 13A):** Produce a detection coverage matrix mapped to MITRE ATT&CK tactics covering Stages 1–10.

> [!IMPORTANT]
> **Stage Gate — Stage 10 (Blue Team Counter-Measures):** Before proceeding to Part 13B, you must demonstrate all of:
> - [ ] Identified 3 MITRE ATT&CK techniques that your current lab SIEM would NOT detect and explained why (telemetry gap, logic gap, or tuning issue)
> - [ ] Written 1 detection rule that specifically targets a living-off-the-land technique (PowerShell, certutil, wmic, mshta, or bitsadmin)
> - [ ] Explained how an attacker using only signed Windows binaries would evade your current detection setup — and proposed a countermeasure
> - [ ] Produced a MITRE ATT&CK Navigator layer showing which techniques your lab rules cover (green) and which are uncovered (red)

---

<a id="toc-part-13b-security-operations-expansion"></a>
<a id="part-13b-security-operations-expansion"></a>
## Part 13B: Security Operations Expansion

_Continuation of Part 13A. These stages cover operational security tools and programs that build on the detection engineering foundation. Complete Part 13A before starting this section._

<a id="stage-11-security-orchestration-automation-response-soar"></a>
### **Stage 11: Security Orchestration, Automation & Response (SOAR)**

> [!TIP]
> **Goal:** Automate SOC workflows and incident response actions.

- [ ] **SOAR Architecture:** Understand how **SOAR platforms (Splunk SOAR, Cortex XSOAR, Tines, Shuffle)** integrate with **SIEM, EDR, ticketing, email, firewall APIs** to automate response.

- [ ] **Playbook Design:** Build automated **runbooks** for common scenarios: **phishing triage (extract IOCs → check reputation → quarantine email → block sender → create ticket)**, **malware alert enrichment**, **user account lockout on failed logins**.

- [ ] **API Integration:** Use **REST APIs** to connect SOAR to **VirusTotal, AbuseIPDB, Shodan, Active Directory, Slack/Teams** for automated enrichment and notification.

- [ ] **Case Management:** Understand **incident case lifecycle** within SOAR: **alert → triage → investigation → containment → remediation → closure** with evidence tracking.

- [ ] **Metrics & ROI:** Measure **automation coverage, MTTR reduction, analyst time saved** to demonstrate SOAR value.

---

<a id="stage-12-data-loss-prevention-dlp-fundamentals"></a>
### **Stage 12: Data Loss Prevention (DLP) Fundamentals**

> [!TIP]
> **Goal:** Understand DLP as a defensive control, not just something to bypass.

- [ ] **DLP Architecture:** Understand **endpoint DLP** (agent-based monitoring of file operations, clipboard, USB), **network DLP** (inline/tap inspection of traffic), and **cloud DLP** (CASB integration, SaaS monitoring).

- [ ] **Policy Design:** Create DLP policies for **PII detection (SSN, credit cards, IBAN), source code exfiltration prevention, intellectual property protection** using **regex, keywords, fingerprinting, exact data matching**.

- [ ] **Response Actions:** Configure **alert, block, quarantine, encrypt, notify manager** responses based on **policy severity and data classification level**.

- [ ] **CASB Integration:** Understand how **Cloud Access Security Brokers (Netskope, Zscaler, Microsoft Defender for Cloud Apps)** extend DLP to **SaaS platforms (Office 365, Google Workspace, Salesforce)**.

- [ ] **DLP Evasion Awareness:** Know that attackers bypass DLP via **steganography, encryption, encoding, protocol tunneling, and out-of-band channels** — use this knowledge to improve detection, not to circumvent it.

---

<a id="stage-13-vulnerability-management-program"></a>
### **Stage 13: Vulnerability Management Program**

> [!TIP]
> **Goal:** Understand the full lifecycle of finding, prioritizing, and remediating vulnerabilities at scale.

- [ ] **Scanner Deployment:** Deploy and configure **Nessus, Qualys, Rapid7 InsightVM, or OpenVAS** for authenticated and unauthenticated scanning across infrastructure.

- [ ] **Scan Scheduling:** Design scan schedules that balance **coverage (weekly/monthly), performance impact (off-peak), and compliance requirements (PCI quarterly ASV scans)**.

- [ ] **Prioritization:** Use **CVSS v4.0, EPSS (Exploit Prediction Scoring System), CISA KEV catalog, asset criticality, and business context** to prioritize remediation over raw severity scores.

- [ ] **Patch Management Lifecycle:** Understand **test → stage → deploy → verify → report** patch workflows, emergency patching for zero-days, and compensating controls when patching is infeasible.

- [ ] **Remediation Tracking:** Use **ticketing systems (Jira, ServiceNow)** to track **remediation SLAs, exception requests, risk acceptance decisions**, and produce **vulnerability trending reports** for leadership.

- [ ] **Continuous Monitoring:** Implement **continuous assessment** via agent-based scanning, cloud posture management (CSPM), and integration with SIEM for vulnerability-correlated alerting.

---

<a id="stage-14-insider-threat-detection"></a>
### **Stage 14: Insider Threat Detection**

> [!TIP]
> **Goal:** Detect and investigate threats originating from within the organization.

- [ ] **Insider Threat Types:** Understand **malicious insiders** (disgruntled employees, espionage), **negligent insiders** (accidental data exposure), and **compromised insiders** (credential theft, social engineering victims).

- [ ] **UEBA (User & Entity Behavior Analytics):** Deploy **behavioral analytics** to baseline normal user behavior (login times, accessed resources, data volumes) and alert on **anomalous patterns** (after-hours access, bulk downloads, unusual destinations).

- [ ] **DLP + SIEM Correlation:** Combine **DLP alerts** (data exfiltration attempts) with **SIEM telemetry** (badge access, VPN connections, email volume) to build **insider risk profiles**.

- [ ] **Insider Threat Program:** Understand program components: **governance (policy, legal, HR), technical controls (monitoring, access reviews), behavioral indicators (resignation, PIP, access hoarding), and investigation workflows**.

- [ ] **Privacy & Legal Constraints:** Balance monitoring with **employee privacy rights, legal requirements (works council, GDPR), union agreements**, and ensure monitoring is **proportionate, documented, and authorized**.

---

<a id="lab-progression-parts-13a-13b-combined"></a>
### **Lab Progression (Parts 13A + 13B Combined)**

> [!TIP]
> **Goal:** Build working detection and security operations capabilities, not just vocabulary.

- [ ] **SIEM Build:** Deploy Wazuh, Security Onion, Splunk Free, or ELK in a lab and ingest Windows Event Logs, Sysmon, Linux auth logs, and firewall/DNS logs.
- [ ] **Query Lab:** Write 10 searches across SPL/KQL/Elastic-style syntax for process creation, suspicious PowerShell, failed logons, DNS anomalies, and lateral movement.
- [ ] **Detection Rule Lab:** Write 5 Sigma/YARA/Suricata/Zeek/osquery rules and test them against lab activity.
- [ ] **Incident Timeline Lab:** Reconstruct 2 incidents from logs and produce analyst notes with evidence and containment actions.
- [ ] **SOAR Playbook Lab:** Build one automated phishing triage playbook (extract IOCs → check reputation → quarantine) using Shuffle, Tines, or n8n.
- [ ] **IR Playbook Execution Lab:** Build and run a complete Incident Response playbook for a **ransomware scenario** in your home lab: (1) detect the ransomware beacon via SIEM alert; (2) isolate the infected VM from the network segment; (3) preserve a forensic memory dump and disk image before remediation; (4) identify the initial access vector from logs; (5) eradicate the payload and restore from a clean snapshot; (6) write a post-incident report with a timeline, root cause, and control improvement recommendations. Use a scenario from **[Blue Team Labs Online](https://blueteamlabs.online)**, **[LetsDefend](https://letsdefend.io)**, or **[CyberDefenders](https://cyberdefenders.org)** as your scenario source if you don't want to stage your own.

**Platform Guide for Phase 3:**

| Platform | Best For | Cost |
|----------|----------|------|
| [Blue Team Labs Online](https://blueteamlabs.online) | DFIR investigations, SOC analyst challenges, log analysis, malware triage | Free + Pro |
| [LetsDefend](https://letsdefend.io) | SOC analyst workflows, alert triage, phishing analysis, incident handling | Free + Pro |
| [CyberDefenders](https://cyberdefenders.org) | Blue team CTF challenges, PCAP analysis, forensics, threat hunting | Free + Pro |
| [Hack The Box Sherlocks](https://hackthebox.com) | DFIR forensics investigations in realistic enterprise scenarios | Free + VIP |
| [Splunk Free / Security Onion / Wazuh](https://wazuh.com) | Self-hosted SIEM/EDR lab environments for detection engineering practice | Free (self-hosted) |



> [!IMPORTANT]
> **Stage Gate — Part 13B Completion (Stages 11–14):** Before proceeding to Part 14 (IDS, Firewalls, Honeypots), you must demonstrate all of:
> - [ ] **SOAR:** Built at least 1 automated playbook in Shuffle, Tines, or n8n that executes a real response action (IP reputation check, email quarantine, or ticket creation) when triggered by a SIEM alert
> - [ ] **DLP:** Created a DLP policy in a lab environment (or documented one for a simulated scenario) with at least 3 detection rules targeting different data types (PII, source code, credentials) with appropriate response actions
> - [ ] **Vulnerability Management:** Run an authenticated Nessus/OpenVAS scan against a lab VM and produced a prioritized remediation report using EPSS or CISA KEV to justify priority order — not just raw CVSS scores
> - [ ] **Insider Threat:** Written a UEBA detection hypothesis for at least 1 insider threat scenario (bulk download before resignation, after-hours access to sensitive files) and named the data sources required to execute it

<a id="toc-part-14-ids-firewalls-and-honeypots"></a>
<a id="part-14-ids-firewalls-and-honeypots"></a>
## Part 14: IDS, Firewalls, and Honeypots

<a id="stage-1-foundational-strategy-networking"></a>
### **Stage 1: Foundational Strategy & Networking**

> [!TIP]
> **Goal:** Establish the theoretical base and network understanding.

- [ ] **Defense in Depth:** Adopt the `Understand Concept of Defense in Depth` philosophy, using multiple layers of security controls.

- [ ] **Network Segmentation:** Design the network with clear boundaries, utilizing `Perimeter vs DMZ vs Segmentation` to limit blast radius.

- [ ] **Protocol Knowledge:** Master networking fundamentals, including `Understand Handshakes` and identifying `Secure vs Unsecure Protocols`.

---

<a id="stage-2-deploying-firewalls-the-shield"></a>
### **Stage 2: Deploying Firewalls (The Shield)**

> [!TIP]
> **Goal:** Implement access control and segmentation.

- [ ] **Perimeter Defense:** Deploy a `Firewall & Nextgen Firewall` at the network edge, configuring `ACLs` for ingress and egress filtering.

- [ ] **Endpoint Protection:** Enable and configure `Host Based Firewall` on servers and workstations for granular `Port Blocking`.

- [ ] **Log Analysis:** Set up centralized collection for `Firewall Logs` to monitor policy violations and traffic patterns.

---

<a id="stage-3-implementing-idsips-the-watchers"></a>
### **Stage 3: Implementing IDS/IPS (The Watchers)**

> [!TIP]
> **Goal:** Detect and stop malicious traffic that bypasses firewalls.

- [ ] **Strategic Deployment:** Place `NIDS` sensors at critical network choke points to monitor east-west and north-south traffic.

- [ ] **Host Monitoring:** Install `HIPS` agents on critical servers to detect suspicious process execution and file changes.

- [ ] **Rule Tuning:** Continuously tune signature and anomaly rules to minimize `False Positives` while ensuring no `False Negatives` occur.

- [ ] **SIEM Integration:** Feed IDS/IPS alerts into a `SIEM` for correlation with other security events.

---

<a id="stage-4-utilizing-deception-the-traps"></a>
### **Stage 4: Utilizing Deception (The Traps)**

> [!TIP]
> **Goal:** Deploy detection-layer deception that catches attackers operating quietly below IDS thresholds, while understanding how attackers evade it.

- [ ] **Honeypot Deployment:** Deploy `Honeypots` (both low and high interaction) in the DMZ and internal network to attract attackers. Use **Cowrie** (SSH/Telnet), **HoneyD**, or **T-Pot** (multi-protocol stack). Log every interaction and correlate to SIEM.

- [ ] **Traffic Redirection:** Use `Sinkholes` to capture traffic destined for known malicious domains or IPs.

- [ ] **Intelligence Gathering:** Analyze logs and activity from deception tools to inform `Basics and Concepts of Threat Hunting`.

- [ ] **Canary Tokens:** Deploy [canarytokens.org](https://canarytokens.org) tokens across your environment. Understand the three primary token types:
  - **DNS canary tokens** — embed in files/configs; fire on DNS lookup when a file is opened on an internet-connected host
  - **HTTP/URL canary tokens** — embed in documents, email signatures, API docs; fire on HTTP GET when accessed
  - **File-open canary tokens** (Word, PDF, folder) — fire when a document is opened, leaking attacker IP and user-agent
  - Deploy tokens in: fake credentials files, decoy API key configs, unused service accounts, document shares, internal wikis

- [ ] **Canary Token Lab (Hands-On — 10 minutes):** Complete this exercise before reading further:
  1. Go to [canarytokens.org/generate](https://canarytokens.org/generate) and generate a **DNS token**. Enter your email for alerts.
  2. Copy the generated DNS hostname into a file on your lab machine named `aws_credentials.txt` as a fake value: `aws_secret_access_key = AKIA[paste-token-hostname-here]`
  3. Open the file from a terminal (`cat aws_credentials.txt`) — observe whether the DNS token fires. (It will not fire from `cat` alone since no DNS resolution occurs. This is intentional — understand why.)
  4. Now generate an **HTTP token** and embed the URL in a fake config file. Use `curl` to trigger it manually.
  5. Check the canarytokens.org dashboard — observe the activation log showing your IP, user-agent, and timestamp.
  6. **Offensive takeaway:** Knowing token trigger mechanics tells you which file access patterns to avoid on an engagement. A file opened with `cat` does not beacon; a Word document opened in Microsoft Office on an internet-connected host does.
  - Deliverable: screenshot of canary token activation log with attacker IP, user-agent, and timestamp annotated.

- [ ] **Honeyfiles and Honeycredentials:** Plant decoy files that look genuinely valuable to a lateral-moving attacker:
  - `credentials.txt`, `passwords.xlsx`, `backup_keys.txt`, `db_passwords.conf` containing fake but plausible credentials
  - Apply canary tokens inside these files so access is logged
  - Monitor for any use of honeycredentials in authentication logs — use is near-certain evidence of active compromise
  - Place on common share locations (\\\\FILESERVER\\Finance$, \\\\FILESERVER\\IT_Admin$) where attackers enumerate after foothold

- [ ] **Modern Deception Platform Awareness:** Understand enterprise deception platforms beyond basic honeypots:
  - **Attivo Networks / SentinelOne Singularity Identity** — identity-layer deception, fake AD accounts with monitored credentials
  - **Illusive Networks** — network-wide deception fabric with fake endpoints, credentials, and connections seeded across endpoints
  - **Thinkst Canary** — commercial canary token infrastructure with management dashboard and alerting
  - Understand how these platforms differ from honeypots: they blend into the live environment rather than sitting isolated in DMZ

- [ ] **Attacker Evasion of Deception Infrastructure:** Understand what attackers look for to avoid triggering deception:
  - Honeypot fingerprinting: blank/minimal service banners, near-perfect uptime, unusual file timestamps, missing Windows event logs
  - Canary detection: files with atypically recent modification times, identical file sizes, names that are too generic ("passwords.txt")
  - Defenders counter this by making deception assets realistic: age files, add plausible modification history, use actual service banners
  - Understand that even sophisticated attackers who detect some canaries will often trigger others due to deception density

---

<a id="stage-5-operations-continuous-improvement"></a>
### **Stage 5: Operations & Continuous Improvement**

> [!TIP]
> **Goal:** Integrate into daily security operations.

- [ ] **Incident Response Integration:** Utilize these tools during **Incident Response Process** for rapid **threat identification and containment** of affected systems.

- [ ] **Zero Trust Alignment:** Ensure firewall and IPS policies align with **Zero Trust** principles, verifying every connection attempt.

- [ ] **Performance Tuning:** Regularly review and tune **IDS/IPS rules, firewall ACLs** to balance security and performance.

- [ ] **Threat Intelligence Integration:** Feed **IOCs from threat intelligence** into firewalls and IDS for proactive blocking.

- [ ] **Red/Purple Team Testing:** Conduct regular **red team exercises** to validate detection capabilities and identify blind spots.

---

<a id="stage-6-email-security-architecture"></a>
### **Stage 6: Email Security Architecture**

> [!TIP]
> **Goal:** Secure the #1 initial access vector — email infrastructure.

- [ ] **Email Authentication (SPF/DKIM/DMARC):** Configure **SPF records** (authorized senders), **DKIM signing** (message integrity), and **DMARC policies** (alignment enforcement with p=reject). Validate with **dmarcian, MXToolbox, Google Postmaster**.

- [ ] **Secure Email Gateway (SEG):** Deploy and tune **Proofpoint, Mimecast, Microsoft Defender for Office 365, or open-source alternatives** — configure **anti-spam, anti-phishing, attachment sandboxing, URL rewriting/detonation**.

- [ ] **Anti-Phishing Defenses:** Implement **display name spoofing detection, lookalike domain alerting, external sender banners, impersonation protection policies** targeting executive and financial staff.

- [ ] **Email DLP:** Configure **Data Loss Prevention rules** to detect and block **outbound PII, credentials, source code, financial data** via email attachments and body content.

- [ ] **Mail Flow Architecture:** Understand **MTA (Mail Transfer Agent) routing, MX records, SMTP relay chains, TLS enforcement (DANE/MTA-STS)**, and how mail traverses from sender to recipient.

- [ ] **Email Forensics Awareness:** Understand **email header analysis (Received headers, X-headers, Message-ID tracking)** to trace phishing campaigns and identify spoofed messages.

---

<a id="stage-7-dns-security-operations"></a>
### **Stage 7: DNS Security Operations**

> [!TIP]
> **Goal:** Detect and prevent DNS-based attacks and data exfiltration.

- [ ] **DNSSEC:** Understand **DNSSEC signing, validation chain, DS/DNSKEY records**, and deployment challenges. Know how DNSSEC prevents **cache poisoning** but does not encrypt queries.

- [ ] **Encrypted DNS (DoH/DoT):** Know that **DNS over HTTPS (DoH, port 443)** and **DNS over TLS (DoT, port 853)** encrypt DNS queries, creating **visibility gaps for network defenders**. Understand how to detect and control encrypted DNS via **endpoint policy, proxy-based inspection, and canary domain monitoring**.

- [ ] **DNS Sinkholing:** Deploy **DNS sinkholes** to redirect known malicious domains (C2, phishing, DGA-generated) to controlled IPs for **detection, containment, and IOC enrichment**.

- [ ] **DNS Firewall (RPZ):** Configure **Response Policy Zones (RPZ)** on internal DNS resolvers to block resolution of **malicious, newly-registered, or DGA-generated domains** based on threat intelligence feeds.

- [ ] **DNS Exfiltration Detection:** Monitor for **high-entropy subdomain queries, unusually long DNS names (>50 chars), high query volumes to single domains, TXT record abuse** indicating **DNS tunneling (iodine, dnscat2)**. Correlate with **SIEM alerts and NetFlow** for confirmation.

- [ ] **Passive DNS Monitoring:** Deploy **passive DNS collection (passivedns, Farsight DNSDB)** to maintain historical resolution records for **threat hunting, domain reputation tracking, and incident response**.

---

<a id="lab-progression-part-14-ids-firewalls-and-honeypots"></a>
### **Lab Progression (Part 14: IDS, Firewalls, and Honeypots)**

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Deploy Snort/Suricata IDS in a lab and write 5 custom rules | IDS ruleset + test results |
| 2 | Configure pfSense/iptables firewall with zone-based policies | Firewall architecture diagram + ruleset |
| 3 | Deploy a honeypot (Cowrie, T-Pot, or HoneyD) and analyze attacker behavior | Honeypot analysis report (24-48 hours of data) |
| 4 | Test IDS evasion techniques and tune rules to detect them | Evasion vs. detection comparison report |
| 5 | Build a complete perimeter defense lab (firewall + IDS + honeypot) | Integrated defense architecture document |

> [!IMPORTANT]
> **Move-On Gate:** You can deploy and configure IDS/IPS, write custom detection rules, deploy honeypots for deception, and tune detection to minimize false positives while catching evasion attempts.

<a id="toc-part-15-osint--threat-intelligence"></a>
<a id="part-15-osint-threat-intelligence"></a>
## Part 15: OSINT & Threat Intelligence

<a id="stage-1-passive-reconnaissance-data-collection"></a>
### **Stage 1: Passive Reconnaissance & Data Collection**

> [!TIP]
> **Goal:** Gather intelligence without touching target infrastructure.

- [ ] **Search Engine Intelligence:** Master **Google/Bing/Yandex dorks** for exposed data; use **Shodan/Censys/Zoomeye** for internet-wide scanning.

- [ ] **Social Media Mining:** Scrape **LinkedIn, Twitter, Facebook, Instagram** for employees, org structure, tech stack mentions, and personal details.

- [ ] **Domain & Infrastructure:** Use **WHOIS, DNS records (MX, TXT, SPF, DMARC), Certificate Transparency logs** to map infrastructure.

- [ ] **Breach Data Analysis:** Query **HIBP (Have I Been Pwned), Dehashed, Snusbase** for leaked credentials and PII.

- [ ] **Code Repository Mining:** Search **GitHub, GitLab, Bitbucket** for exposed **API keys, credentials, internal IPs, architecture docs**.

- [ ] **Dark Web Monitoring:** Monitor **paste sites, forums, dark web marketplaces** for leaked data, exploit sales, threat actor chatter.

---

<a id="stage-2-threat-intelligence-analysis"></a>
### **Stage 2: Threat Intelligence Analysis**

> [!TIP]
> **Goal:** Convert raw data into actionable intelligence.

- [ ] **IOC Collection:** Aggregate **file hashes, domains, IPs, email patterns** from **threat feeds, MISP, AlienVault OTX**.

- [ ] **Threat Actor Profiling:** Study **APT groups, TTPs, infrastructure patterns** using **MITRE ATT&CK, threat reports (Mandiant, CrowdStrike)**.

- [ ] **Campaign Tracking:** Monitor **active campaigns, malware families, exploit trends** to understand current threat landscape.

- [ ] **Attribution Analysis:** Correlate **infrastructure, code patterns, language artifacts** to attribute attacks to specific actors.

- [ ] **Victimology Studies:** Understand **target selection, industry focus, geographic distribution** of threat actors.

---

<a id="stage-3-osint-automation-tooling"></a>
### **Stage 3: OSINT Automation & Tooling**

> [!TIP]
> **Goal:** Scale reconnaissance with automation and operationalise threat intelligence platforms.

- [ ] **Reconnaissance Frameworks:** Master **[Recon-ng](../Tools/Recon-ng.md), [theHarvester](../Tools/theHarvester.md), [SpiderFoot](../Tools/SpiderFoot.md), [Maltego](../Tools/Maltego.md)** for automated data collection.

- [ ] **Subdomain Enumeration:** Use **Amass, Subfinder, Assetfinder, DNSRecon** to discover **subdomains, ASNs, IP ranges**.

- [ ] **API Integration:** Leverage **VirusTotal, Shodan, SecurityTrails, Hunter.io APIs** for programmatic data access.

- [ ] **Custom Scripting:** Build **Python/Bash scripts** to automate **scraping, parsing, correlation** of OSINT data.

- [ ] **Data Pipeline:** Create **ETL pipelines** to aggregate, normalize, and store intelligence in **databases/dashboards**.

- [ ] **MISP Platform Operation:** Deploy and operate a [MISP (Malware Information Sharing Platform)](https://www.misp-project.org/) instance. Master the operational mechanics, not just awareness:
  - **Feed management:** Subscribe to and synchronise public MISP feeds (CIRCL default feeds, abuse.ch URLhaus, Botvrij). Understand pull vs. push sy[nc ](../Tools/Netcat.md)models and feed caching behaviour.
  - **Event creation and sharing:** Create a MISP event from a threat report, populate attributes (IP, domain, hash, YARA rule), set distribution level (Organisation only / Community / All communities), and share via a MISP sync connection or TAXII server.
  - **Indicator enrichment:** Use MISP modules (VirusTotal, Shodan, PassiveTotal, CIRCL HASHLOOKUP) to automatically enrich submitted indicators. Understand enrichment confidence and staleness.
  - **Threat actor tagging:** Apply MITRE ATT&CK Galaxy cluster tags to events and attributes. Tag threat actors (e.g., `misp-galaxy:threat-actor="Lazarus Group"`), malware families (`misp-galaxy:malware="Emotet"`), and attack patterns. Understand how tagging enables correlation across events and feeds.
  - **Warninglists and Correlation:** Enable MISP warninglists to suppress false positives (CDN IPs, public resolvers). Understand how MISP's correlation engine links related indicators across events automatically.
  - **MISP → SIEM pipeline:** Export indicators in MISP native format or via its API to your SIEM lookup tables. See Stage 5 for the full pipeline exercise.

---

<a id="stage-4-threat-intelligence-dissemination"></a>
### **Stage 4: Threat Intelligence Dissemination**

> [!TIP]
> **Goal:** Communicate intelligence effectively to stakeholders.

- [ ] **Intelligence Reports:** Create **tactical (IOCs), operational (TTPs), strategic (trends)** reports for different audiences.

- [ ] **TLP Classification:** Apply **Traffic Light Protocol (White, Green, Amber, Red)** for information sharing sensitivity.

- [ ] **STIX/TAXII:** Use **Structured Threat Information Expression (STIX)** and **TAXII** for standardized intel sharing.

- [ ] **Threat Briefings:** Deliver **executive briefings** highlighting **risks, trends, recommended actions** in non-technical language.

- [ ] **Community Collaboration:** Participate in **ISACs, threat intel communities, CTI sharing platforms** for collective defense.

---

<a id="stage-5-threat-intel-operationalization"></a>
### **Stage 5: Threat Intel Operationalization**

> [!TIP]
> **Goal:** Close the gap between *collecting* threat intelligence and *acting on it*. A threat report with IOCs and TTPs has zero value if it sits in a PDF. This stage converts intel into SIEM rules, hunting queries, and detection coverage.

- [ ] **IOC → SIEM Pipeline:** Take a published threat report (e.g., [CISA advisories](https://www.cisa.gov/alerts-advisories), [Mandiant APT reports](https://www.mandiant.com/resources/reports), [Sekoia.io blog](https://blog.sekoia.io)) and extract IOCs (IPs, domains, hashes, registry keys, mutexes). Import them into your SIEM/MISP as custom indicators. Write SIEM queries that alert on these IOCs in real-time. Verify the alert fires against test traffic before marking the IOC as operational.

- [ ] **TTP → Detection Rules:** Take a published APT campaign report (e.g., Lazarus Group, Sandworm, APT41). Map 5 TTPs from the report to MITRE ATT&CK technique IDs. For each TTP, write a Sigma rule targeting the log source that would catch the behavior (e.g., T1059.001 PowerShell → process creation log with `powershell.exe -EncodedCommand`). Test each rule in your SIEM by executing the matching behavior in a controlled lab VM. Commit all rules to your Git repository.

- [ ] **Threat Hunting from Intel:** Select one APT report and build a hunting hypothesis: "If this threat actor operated in our environment, what evidence would exist in which log sources?" Build a hunting query for each hypothesis in your SIEM query language (SPL/KQL/EQL). Run the query against your lab data and document: query logic, expected output, actual output, and whether the hunt was productive.

- [ ] **MISP → SIEM Integration:** Configure MISP to automatically push new indicators to your SIEM (via MISP feeds or MISP Warninglists export → SIEM lookup table). Validate that a new IOC added to MISP generates an alert in your SIEM within 15 minutes. This is the core of an automated threat intel pipeline.

- [ ] **Intel-Driven Rule Review:** After writing 10 detection rules over the course of Phase 3, re-review each rule against a new threat report. Ask: "Would this rule catch the TTP described in this report?" If not — update the rule. Detection rule maintenance is as important as rule creation.

> [!IMPORTANT]
> **Operationalization Gate:** You are ready to proceed when you can take a raw APT report, extract structured IOCs, write Sigma rules for 3+ TTPs, import IOCs into your SIEM, verify alerts fire, and run a threat hunt query with documented results. If you can only collect intel but not act on it, you are not yet a threat intelligence practitioner.

---

<a id="lab-progression-part-15-osint-threat-intelligence"></a>
### **Lab Progression (Part 15: OSINT & Threat Intelligence)**

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Perform complete OSINT profile of a public figure (using only public data) | OSINT report with sources |
| 2 | Use Shodan/Censys to discover exposed services on a target range | Exposure assessment report |
| 3 | Set up automated threat intelligence feeds (MISP or OpenCTI) | Working TI platform with 3+ feeds |
| 4 | Produce a threat intelligence report on a specific APT group | Structured TI report (TTPs, IOCs, recommendations) |
| 5 | Create STIX-formatted IOCs and share via TAXII server in lab | Working STIX/TAXII demo |
| 6 | Take one APT report → extract IOCs → write 3 Sigma rules → verify they fire in SIEM | Sigma rule set + SIEM alert screenshots |

> [!IMPORTANT]
> **Move-On Gate (Part 15):** You can gather, analyze, and disseminate threat intelligence using industry-standard tools and formats, and produce actionable intelligence reports for both technical and executive audiences. **You must also complete Stage 5 operationalization:** take a raw APT report, extract structured IOCs, import them into your SIEM, write Sigma rules for at least 3 TTPs, verify the alerts fire in your lab, and execute a documented threat hunt query with recorded results. A practitioner who can collect intel but not act on it has not completed this part.


---

<a id="grc-fundamentals-sidebar-early-supplement-for-defensive-careers"></a>
### **GRC Fundamentals Sidebar** _(Early Supplement for Defensive Careers)_

> **Why Here:** SOC analysts, detection engineers, and blue team professionals encounter governance and compliance obligations on Day 1 of employment — not after years of technical specialization. You need to understand what constitutes a reportable incident, what frameworks drive your employer's security program, and how risk language works before you respond to your first real alert. Full GRC depth (audit mechanics, risk quantification, regulatory testing, vendor risk) is in Part 35 (Phase 8). This sidebar gives you the operational minimum.

---

**Stage G1: NIST Cybersecurity Framework (CSF) — Operational Context**

- [ ] **The 5 CSF Functions:** Memorize and internalize the **Identify → Protect → Detect → Respond → Recover** cycle. Understand that every SOC alert and every defensive tool maps to one or more of these functions:
  - **Identify (ID):** Asset inventory, risk assessment, supply chain risk — know what you have before you can protect it
  - **Protect (PR):** Access control, awareness training, data security, maintenance, protective technology
  - **Detect (DE):** Continuous monitoring, anomaly detection, detection processes — this is where SIEM and EDR live
  - **Respond (RS):** Response planning, communications, analysis, mitigation, improvements — your IR playbooks
  - **Recover (RC):** Recovery planning, improvements, communications — restoring operations after an incident

- [ ] **CSF as a Communication Tool:** When your CISO says "we need to improve our Detect posture," they mean improving SIEM coverage, detection rules, and threat hunting. CSF is the language your leadership uses to talk about security investment. Understand it so you can contribute meaningfully to those conversations.

- [ ] **NIST CSF 2.0 (Govern Function):** NIST CSF 2.0 added a 6th function — **Govern (GV)** — covering organizational context, risk strategy, roles, policies, and supply chain risk. This function sits above all others and drives how the other 5 are implemented.

---

**Stage G2: Regulatory Obligations — What Defenders Must Know**

> [!WARNING]
> Failing to meet mandatory breach notification timelines can result in regulatory fines, personal liability for CISOs, and public disclosure. Know these timelines before you respond to your first incident.

- [ ] **GDPR (General Data Protection Regulation — EU):**
  - Applies to any organization processing data of EU residents, regardless of where the org is based
  - **72-hour notification requirement:** Personal data breaches must be reported to the relevant Data Protection Authority within 72 hours of becoming aware — not 72 hours after investigation completion
  - Individual notification required if the breach is "likely to result in a high risk to the rights and freedoms" of affected individuals
  - Maximum fine: €20M or 4% of global annual turnover (whichever is higher)

- [ ] **HIPAA (Health Insurance Portability and Accountability Act — US Healthcare):**
  - Applies to **Covered Entities** (healthcare providers, health plans, clearinghouses) and **Business Associates** (vendors handling PHI)
  - **Protected Health Information (PHI):** Any individually identifiable health information — 18 categories of identifiers
  - **Breach Notification Rule:** Affected individuals must be notified within 60 days of discovery; HHS notification required within 60 days; if >500 individuals affected, media notification required in the affected state; if 500+ individuals, HHS must be notified immediately
  - Minimum Necessary Standard: Access to PHI must be limited to what is necessary for the job function

- [ ] **PCI-DSS (Payment Card Industry Data Security Standard):**
  - Applies to any entity that stores, processes, or transmits cardholder data
  - 12 requirements organized around: network security, access control, vulnerability management, monitoring, information security policy
  - **Penetration testing requirement:** PCI-DSS mandates annual penetration testing (network and application) and testing after significant infrastructure changes — this is why pentesting exists as a compliance service
  - Incident response: Must have a tested IR plan; must notify card brands and acquiring bank immediately upon breach suspicion

- [ ] **Incident Notification Decision Tree:** When responding to a potential breach, apply this sequence:
  1. Is personal data (PII, PHI, payment card data) involved? → Yes → determine scope
  2. What jurisdiction applies? → EU residents = GDPR, US healthcare = HIPAA, payment cards = PCI-DSS
  3. What is the notification timeline for this jurisdiction?
  4. Has the timeline started? (Clock usually starts at "awareness" or "discovery" — not at confirmed impact)
  5. Who is the notification contact? (DPA, HHS, card brands, legal counsel, PR team)

---

**Stage G3: Risk Terminology — The Language of Security Decisions**

- [ ] **Core Risk Equation:** `Risk = Threat × Vulnerability × Impact`
  - **Threat:** A potential cause of harm (e.g., ransomware operators, insider threat, nation-state actors)
  - **Vulnerability:** A weakness that can be exploited (e.g., unpatched CVE, misconfigured S3 bucket, weak password policy)
  - **Impact:** The consequence if exploitation succeeds (e.g., data breach, system unavailability, financial loss, reputational damage)
  - **Likelihood:** How probable is the threat-vulnerability combination being realized? (1–5 scale or qualitative: Low/Medium/High/Critical)

- [ ] **Risk vs. Vulnerability:** A vulnerability without a plausible threat or material impact is **low risk**. A critical vulnerability on an internet-exposed system with known active exploitation is **critical risk**. CVSS scores measure vulnerability severity — not organizational risk. Always translate CVSS to risk by considering your environment.

- [ ] **Risk Acceptance vs. Risk Treatment:** Four options for handling identified risk:
  - **Mitigate:** Implement a control to reduce the likelihood or impact
  - **Transfer:** Shift the risk to a third party (cyber insurance, SLA contractual clauses)
  - **Accept:** Formally acknowledge the risk and decide not to act (requires executive sign-off and documentation)
  - **Avoid:** Eliminate the risk by stopping the activity that creates it

- [ ] **Risk Register Basics:** Organizations maintain a risk register — a documented list of identified risks with owner, likelihood, impact, treatment decision, and review date. As a SOC analyst, you may be asked to add or update risk register entries based on threat intelligence or incident findings.

---

**Stage G4: Incident Classification Framework**

- [ ] **Severity Classification:** Most organizations use a tiered severity system for incidents. Know a typical framework:

  | Severity | Definition | Examples | Response Time |
  |----------|-----------|---------|---------------|
  | **Critical (P1)** | Active breach, ransomware, data exfiltration in progress | Confirmed ransomware, APT intrusion, insider data theft | Immediate (< 1 hour) |
  | **High (P2)** | Likely breach or imminent risk | Malware confirmed on critical system, privileged account compromise | < 4 hours |
  | **Medium (P3)** | Potential incident requiring investigation | Suspicious login patterns, anomalous data movement, policy violation | < 24 hours |
  | **Low (P4)** | Security event unlikely to cause significant harm | Failed login attempts, policy violation without data risk | < 72 hours |

- [ ] **Incident Categories (CISA Model):** Know the standard incident categories used in government and enterprise:
  - **Category 1 — Unauthorized Access:** User accessing systems/data they shouldn't
  - **Category 2 — Denial of Service:** Deliberate disruption of availability
  - **Category 3 — Malicious Code:** Virus, worm, ransomware, rootkit
  - **Category 4 — Improper Usage:** Violation of acceptable use policy
  - **Category 5 — Scans/Probes/Attempted Access:** Reconnaissance, port scanning, brute force

- [ ] **False Positive vs. True Positive:** A **true positive** is a real attack correctly flagged by a detection rule. A **false positive** is a legitimate activity incorrectly flagged as malicious. A **false negative** is a real attack that was not detected. Tuning the ratio of true positives to false positives is the core daily work of a detection engineer.

---

**Stage G5: Compliance Framework Awareness (By Industry)**

- [ ] **Framework by Industry Quick Reference:**

  | Industry | Primary Framework | Regulator |
  |----------|------------------|-----------|
  | US Healthcare | HIPAA | HHS Office for Civil Rights |
  | Payment Processing | PCI-DSS | PCI Security Standards Council |
  | EU Data Processing | GDPR | National Data Protection Authorities |
  | US Federal Agencies | NIST SP 800-53, FedRAMP | NIST, OMB, CISA |
  | Financial Services (US) | SOX (IT controls), GLBA, FFIEC | SEC, FDIC, OCC |
  | US Defense Supply Chain | CMMC (Cybersecurity Maturity Model Certification) | DoD |
  | Indian Data Processing | DPDP Act 2023 | Data Protection Board of India |

- [ ] **What Auditors Look For (Basics):** Compliance audits typically check for: documented policies, evidence that controls are operating, access control logs, vulnerability scan results, patch management records, incident response plan existence (and evidence of testing), and security awareness training completion records. Your SIEM and incident documentation are primary audit evidence sources.

- [ ] **SOC 2 Type I vs. Type II:** SOC 2 is an auditing standard for service organizations. **Type I** evaluates whether controls are designed correctly at a point in time. **Type II** evaluates whether controls operated effectively over a period (usually 6–12 months). Customers ask for SOC 2 Type II reports to verify vendor security posture.

---

> 📌 _Full GRC depth (audit mechanics, vendor risk assessment, continuous compliance automation, FAIR risk quantification, regulatory testing procedures, ISO 27001 control implementation) is covered in [Part 35: GRC](Phase-8.md#part-35-governance-risk-compliance-grc) (Phase 8). This sidebar gives you the minimum needed to function effectively in a defensive role from Day 1._



---

### 🏆 Phase 3 Capstone Project

**Deploy a SIEM, Investigate Simulated Attacks, and Build a Detection Library**

- [ ] **Deploy a SIEM** (Splunk Free, ELK, or Wazuh) in your lab and ingest logs from your Phase 1 lab environment
- [ ] **Write 5 custom detection rules** (Sigma format) covering different MITRE ATT&CK tactics
- [ ] **Simulate 3 attacks** using Atomic Red Team and investigate each using only your SIEM
- [ ] **Build an investigation timeline** for each simulated incident

**Deliverables:**
- [ ] Detection coverage matrix mapping your 5 rules to MITRE ATT&CK techniques
- [ ] 3 investigation reports (timeline, evidence, root cause, recommendations)
- [ ] SIEM configuration guide (reproducible deployment steps)
- [ ] All Sigma rules and queries committed to your Git repository

> [!IMPORTANT]
> **Capstone Gate:** Your SIEM must be operational, your detection rules must fire on the simulated attacks, and your investigation reports must follow a structured IR format.

---

### 🧭 Phase 3 Reflection & Competency Check

- [ ] **Reflection:** Which detections were noisy, missing, or too fragile?
- [ ] **Reflection:** What evidence changed your initial incident hypothesis?
- [ ] **Competency:** Can you ingest logs, write rules, test them, and tune false positives?
- [ ] **Competency:** Can you build an incident timeline from multiple data sources?
- [ ] **Competency:** Can you explain detection gaps in terms of telemetry, logic, and attacker behavior?

> [!IMPORTANT]
> **Phase Completion Gate:** Move on only when you can investigate simulated attacks from evidence, improve detections, and write analyst notes that another defender can act on.

---

> [!NOTE]
> **✅ Phase 3 ends here.**
> Part 16 (Adversary Emulation & Purple Teaming) is the **Phase 6 capstone** — it is intentionally numbered out of sequence and lives in [Phase-6.md](Phase-6.md). You will encounter it after completing Phase 6 Parts 23–25. Do not attempt Part 16 now. Proceed to Phase 4: Web & Application Security.
>
> ◀ [Phase 2](Phase-2.md) | 🏠 [Master Roadmap](README.md) | [Phase 4](Phase-4.md) ➔
