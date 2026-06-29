# Phase 3: Defense & Detection

---

### 🧭 Navigation
◀ [Phase 2](Phase-2.md) | 🏠 [Master Roadmap](README.md) | [Phase 4](Phase-4.md) ➔

---

> [!NOTE]
> **Phase Overview**
> - **⏱️ Time Commitment (Full-Time):** 2–3 months
> - **⏱️ Time Commitment (Part-Time):** 4–6 months
> - **🎯 Primary Focus:** Detection engineering, SOC & SIEM fundamentals, IDS/IPS/honeypots, threat hunting, incident response basics, forensic fundamentals, and OSINT & threat intelligence. Understand what defenders see before you specialize further.

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
  - [Lab Progression](#lab-progression)
  - [Stage 7: DNS Security Operations](#stage-7-dns-security-operations)
- [Part 15: OSINT & Threat Intelligence](#part-15-osint-threat-intelligence)
  - [Stage 1: Passive Reconnaissance & Data Collection](#stage-1-passive-reconnaissance-data-collection)
  - [Stage 2: Threat Intelligence Analysis](#stage-2-threat-intelligence-analysis)
  - [Stage 3: OSINT Automation & Tooling](#stage-3-osint-automation-tooling)
  - [Stage 4: Threat Intelligence Dissemination](#stage-4-threat-intelligence-dissemination)
  - [Lab Progression](#lab-progression)
  - [GRC Fundamentals Sidebar (Early Supplement for Defensive Careers)](#grc-fundamentals-sidebar-early-supplement-for-defensive-careers)

---

## Part 13A: Detection Engineering & SOC Operations

_Understand defensive detection to know what to evade. This Part covers core detection engineering, SIEM, threat hunting, incident response, and forensic fundamentals (Stages 1–10). Security operations expansion topics (SOAR, DLP, Vulnerability Management, Insider Threat) continue in Part 13B._

### **Stage 1: Defensive Architecture**

- [ ] **Defense-In-Depth:** Layer **EDR, SIEM, CASB, firewall, WAF, IDS/IPS, DNS filtering** with **proper tuning** to reduce false positives and enable hunting.

- [ ] **Threat Hunting:** Proactively search for **suspicious patterns** (parent/child process anomalies, unsigned DLLs, scheduled task abuse, registry modifications) using **Sigma rules, YARA, KQL**.

- [ ] **Incident Response Plan:** Document **detection, containment, eradication, recovery, lessons learned** phases with **clear ownership and escalation paths**.

---

### **Stage 2: Offensive Indicators & TTPs**

- [ ] **IOC Identification:** Recognize **file hashes, domains, IPs, email patterns, behavioral signatures** that map to known attack frameworks (Cobalt Strike, Metasploit, custom).

- [ ] **MITRE ATT&CK Mapping:** Correlate **detected behaviors** to **tactics/techniques** to understand adversary intent and prioritize detection investment.

- [ ] **Artifact Analysis:** Understand forensic artifacts (prefetch, MFT, journal logs, browser history, registry hives, event logs) as **evidence of compromise**.

---

### **Stage 3: Evasion Detection & Hardening**

- [ ] **Living-off-the-Land Detection:** Monitor **native binary execution** (PowerShell, WMI, certutil, mshta, bitsadmin) with **process whitelisting, memory pattern analysis, and behavioral indicators**.

- [ ] **Obfuscation Analysis:** Detect **encoded payloads, packed executables, script obfuscation** via **entropy analysis, dynamic detonation, behavioral sandboxing**.

- [ ] **Anti-Forensics Detection:** Identify **log clearing, file timestomping, registry deletion, bash history removal** via **SIEM correlation and immutable audit logs**.

- [ ] **Command-Line Auditing:** Enable and monitor **PowerShell transcript logging, command-line audit logs (4688), script block logging** for obfuscated execution.

---

### **Stage 4: Detection Engineering & Response**

- [ ] **Detection Rules:** Write **Sigma, Snort/Suricata, Yara, osquery** rules targeting **adversary TTPs** from reconnaissance to exfiltration.

- [ ] **Alert Tuning:** Baseline **normal traffic/processes**, establish **alert thresholds**, reduce **false positives** to improve SOC efficiency.

- [ ] **SOC Playbooks:** Document **runbooks** for each alert type: **triage → validation → containment → remediation → documentation**.

- [ ] **Threat Intelligence Integration:** Consume **OSINT feeds, MISP, AlienVault OTX, commercial threat intel** to enrich **IP/domain/file lookups** in SIEM.

---

### **Stage 5: EDR/XDR/MDR Basics**

> [!TIP]
> **Goal:** : Understand modern endpoint and extended detection capabilities.

- [ ] **EDR Architecture:** Understand **agent-based detection (process, file, registry, network), telemetry collection, cloud backend, response orchestration**.

- [ ] **EDR Capabilities:** Know **behavioral analysis, memory scanning, AMSI integration, ETW collection, indicator of compromise (IOC) matching**.

- [ ] **EDR Evasion vs. Detection:** Understand **living-off-the-land techniques EDR detects**, **code injection detection**, **DLL side-loading detection**.

- [ ] **XDR Approach:** Understand how **XDR correlates endpoint, network, cloud, identity signals** for **detection, hunting, response** across domains.

- [ ] **MDR Services:** Know what **Managed Detection & Response (MDR)** providers offer: **24/7 monitoring, incident response, threat hunting, consulting**.

---

### **Stage 6: SOC & SIEM Fundamentals**

> [!TIP]
> **Goal:** : Understand Security Operations Center workflow and SIEM correlation.

- [ ] **SIEM Basics:** Understand **log aggregation, parsing, normalization, correlation, enrichment** using tools like **Splunk, ELK, ArcSight, QRadar**.

- [ ] **Log Collection:** Know what logs to collect: **Windows Event Logs, Sysmon, firewall logs, proxy logs, DNS logs, authentication logs, application logs**.

- [ ] **Alert Correlation:** Understand **multi-stage detection** (e.g., suspicious logon + process creation + network connection = lateral movement indicator).

- [ ] **SOC Workflow:** Understand **analyst triage → escalation → incident investigation → containment → reporting** process and metrics (MTTD, MTTR).

- [ ] **Dashboard & KPIs:** Know key metrics: **alert volume, MTTD/MTTR, false positive rate, detection coverage %, incident severity distribution**.

- [ ] **SIEM Query Language Fluency:** Compare **SPL (Splunk)**, **KQL (Microsoft Sentinel/Defender)**, and **Lucene/EQL (Elastic/OpenSearch)** syntax for the same detection logic — write the same alert (e.g., "failed logins > 10 in 5 minutes from same source") in all three languages. Maintain a personal cheat sheet mapping equivalent operators across platforms.

---

### **Stage 7: Threat Hunting Methodology**

> [!TIP]
> **Goal:** : Learn proactive threat hunting to find advanced threats.

- [ ] **Hunting Hypotheses:** Formulate hypotheses based on **MITRE ATT&CK, threat reports, prior compromises** (e.g., "Are scheduled tasks being abused?").

- [ ] **Data Source Selection:** Choose **event logs, network traffic, process telemetry, file integrity monitoring** appropriate for hypothesis.

- [ ] **Query Construction:** Build **SQL, KQL, SPL queries** in SIEM to **search for patterns** (unusual process chains, rare executables, domain queries).

- [ ] **Pivot & Correlate:** Use **results to pivot** (e.g., find account → check all logons → find source IP → check all connections).

- [ ] **Validation & Documentation:** Confirm findings are **actual compromise vs. false positive**, document **timeline, IOCs, and response**.

---

### **Stage 8: Incident Response Basics**

> [!TIP]
> **Goal:** : Understand the incident response lifecycle.

- [ ] **Detection & Analysis:** Receive **alert/complaint → triage → determine if real incident → declare incident**.

- [ ] **Containment Strategy:** Short-term: **isolate affected systems**; Long-term: **fix vulnerabilities, update passwords, patch**.

- [ ] **Eradication:** **Remove attacker access** (reset creds, close backdoors, patch exploited systems), verify **persistence mechanisms** removed.

- [ ] **Recovery:** **Restore systems to known good state**, rebuild compromised hosts, verify **no re-infection**.

- [ ] **Lessons Learned:** **Timeline analysis, root cause, detection gaps, improve controls** to prevent recurrence.

- [ ] **Forensic Preservation:** During response, **preserve evidence** (memory dumps, disk images, logs) for **investigation and legal proceedings**.

---

### **Stage 9: Forensic Fundamentals**

> [!TIP]
> **Goal:** : Collect and analyze evidence of compromise.

- [ ] **Live Response:** Collect **running processes, network connections, logged-in users, active services** before shutdown (loses volatile data).

- [ ] **Disk Imaging:** Create **bit-for-bit copy** of drives for **offline analysis**, use tools like **dd, Acquire, FTK Imager**.

- [ ] **Timeline Analysis:** Build **chronological timeline** of **file creation/modification, registry changes, logs** to reconstruct **attack sequence**.

- [ ] **Artifact Examination:** Analyze **Windows Prefetch, Shimcache, MRU, Recycle Bin, browser history, temp files** for **evidence of compromise**.

- [ ] **Memory Analysis:** Use tools like **Volatility, Rekall** to extract **running processes, injected code, encryption keys, command history** from memory dumps.

---

### **Stage 10: Blue Team Evasion Counter-Measures**

> [!TIP]
> **Goal:** : Know how defenders detect and counter red team techniques.

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

---

<a id="toc-part-13b-security-operations-expansion"></a>
## Part 13B: Security Operations Expansion

_Continuation of Part 13A. These stages cover operational security tools and programs that build on the detection engineering foundation. Complete Part 13A before starting this section._

### **Stage 11: Security Orchestration, Automation & Response (SOAR)**

> [!TIP]
> **Goal:** : Automate SOC workflows and incident response actions.

- [ ] **SOAR Architecture:** Understand how **SOAR platforms (Splunk SOAR, Cortex XSOAR, Tines, Shuffle)** integrate with **SIEM, EDR, ticketing, email, firewall APIs** to automate response.

- [ ] **Playbook Design:** Build automated **runbooks** for common scenarios: **phishing triage (extract IOCs → check reputation → quarantine email → block sender → create ticket)**, **malware alert enrichment**, **user account lockout on failed logins**.

- [ ] **API Integration:** Use **REST APIs** to connect SOAR to **VirusTotal, AbuseIPDB, Shodan, Active Directory, Slack/Teams** for automated enrichment and notification.

- [ ] **Case Management:** Understand **incident case lifecycle** within SOAR: **alert → triage → investigation → containment → remediation → closure** with evidence tracking.

- [ ] **Metrics & ROI:** Measure **automation coverage, MTTR reduction, analyst time saved** to demonstrate SOAR value.

---

### **Stage 12: Data Loss Prevention (DLP) Fundamentals**

> [!TIP]
> **Goal:** : Understand DLP as a defensive control, not just something to bypass.

- [ ] **DLP Architecture:** Understand **endpoint DLP** (agent-based monitoring of file operations, clipboard, USB), **network DLP** (inline/tap inspection of traffic), and **cloud DLP** (CASB integration, SaaS monitoring).

- [ ] **Policy Design:** Create DLP policies for **PII detection (SSN, credit cards, IBAN), source code exfiltration prevention, intellectual property protection** using **regex, keywords, fingerprinting, exact data matching**.

- [ ] **Response Actions:** Configure **alert, block, quarantine, encrypt, notify manager** responses based on **policy severity and data classification level**.

- [ ] **CASB Integration:** Understand how **Cloud Access Security Brokers (Netskope, Zscaler, Microsoft Defender for Cloud Apps)** extend DLP to **SaaS platforms (Office 365, Google Workspace, Salesforce)**.

- [ ] **DLP Evasion Awareness:** Know that attackers bypass DLP via **steganography, encryption, encoding, protocol tunneling, and out-of-band channels** — use this knowledge to improve detection, not to circumvent it.

---

### **Stage 13: Vulnerability Management Program**

> [!TIP]
> **Goal:** : Understand the full lifecycle of finding, prioritizing, and remediating vulnerabilities at scale.

- [ ] **Scanner Deployment:** Deploy and configure **Nessus, Qualys, Rapid7 InsightVM, or OpenVAS** for authenticated and unauthenticated scanning across infrastructure.

- [ ] **Scan Scheduling:** Design scan schedules that balance **coverage (weekly/monthly), performance impact (off-peak), and compliance requirements (PCI quarterly ASV scans)**.

- [ ] **Prioritization:** Use **CVSS v4.0, EPSS (Exploit Prediction Scoring System), CISA KEV catalog, asset criticality, and business context** to prioritize remediation over raw severity scores.

- [ ] **Patch Management Lifecycle:** Understand **test → stage → deploy → verify → report** patch workflows, emergency patching for zero-days, and compensating controls when patching is infeasible.

- [ ] **Remediation Tracking:** Use **ticketing systems (Jira, ServiceNow)** to track **remediation SLAs, exception requests, risk acceptance decisions**, and produce **vulnerability trending reports** for leadership.

- [ ] **Continuous Monitoring:** Implement **continuous assessment** via agent-based scanning, cloud posture management (CSPM), and integration with SIEM for vulnerability-correlated alerting.

---

### **Stage 14: Insider Threat Detection**

> [!TIP]
> **Goal:** : Detect and investigate threats originating from within the organization.

- [ ] **Insider Threat Types:** Understand **malicious insiders** (disgruntled employees, espionage), **negligent insiders** (accidental data exposure), and **compromised insiders** (credential theft, social engineering victims).

- [ ] **UEBA (User & Entity Behavior Analytics):** Deploy **behavioral analytics** to baseline normal user behavior (login times, accessed resources, data volumes) and alert on **anomalous patterns** (after-hours access, bulk downloads, unusual destinations).

- [ ] **DLP + SIEM Correlation:** Combine **DLP alerts** (data exfiltration attempts) with **SIEM telemetry** (badge access, VPN connections, email volume) to build **insider risk profiles**.

- [ ] **Insider Threat Program:** Understand program components: **governance (policy, legal, HR), technical controls (monitoring, access reviews), behavioral indicators (resignation, PIP, access hoarding), and investigation workflows**.

- [ ] **Privacy & Legal Constraints:** Balance monitoring with **employee privacy rights, legal requirements (works council, GDPR), union agreements**, and ensure monitoring is **proportionate, documented, and authorized**.

---

### **Lab Progression (Parts 13A + 13B Combined)**

> [!TIP]
> **Goal:** : Build working detection and security operations capabilities, not just vocabulary.

- [ ] **SIEM Build:** Deploy Wazuh, Security Onion, Splunk Free, or ELK in a lab and ingest Windows Event Logs, Sysmon, Linux auth logs, and firewall/DNS logs.
- [ ] **Query Lab:** Write 10 searches across SPL/KQL/Elastic-style syntax for process creation, suspicious PowerShell, failed logons, DNS anomalies, and lateral movement.
- [ ] **Detection Rule Lab:** Write 5 Sigma/YARA/Suricata/Zeek/osquery rules and test them against lab activity.
- [ ] **Incident Timeline Lab:** Reconstruct 2 incidents from logs and produce analyst notes with evidence and containment actions.
- [ ] **SOAR Playbook Lab:** Build one automated phishing triage playbook (extract IOCs → check reputation → quarantine) using Shuffle, Tines, or n8n.

**Move-On Gate (Part 13B):** You can deploy SIEM/SOAR, write detection rules, perform threat hunting, execute incident response workflows, configure DLP policies, and produce a detection coverage matrix mapped to MITRE ATT&CK tactics.

<a id="toc-part-14-ids-firewalls-and-honeypots"></a>
## Part 14: IDS, Firewalls, and Honeypots

### **Stage 1: Foundational Strategy & Networking**

> [!TIP]
> **Goal:** : Establish the theoretical base and network understanding.

- [ ] **Defense in Depth:** Adopt the `Understand Concept of Defense in Depth` philosophy, using multiple layers of security controls.

- [ ] **Network Segmentation:** Design the network with clear boundaries, utilizing `Perimeter vs DMZ vs Segmentation` to limit blast radius.

- [ ] **Protocol Knowledge:** Master networking fundamentals, including `Understand Handshakes` and identifying `Secure vs Unsecure Protocols`.

---

### **Stage 2: Deploying Firewalls (The Shield)**

> [!TIP]
> **Goal:** : Implement access control and segmentation.

- [ ] **Perimeter Defense:** Deploy a `Firewall & Nextgen Firewall` at the network edge, configuring `ACLs` for ingress and egress filtering.

- [ ] **Endpoint Protection:** Enable and configure `Host Based Firewall` on servers and workstations for granular `Port Blocking`.

- [ ] **Log Analysis:** Set up centralized collection for `Firewall Logs` to monitor policy violations and traffic patterns.

---

### **Stage 3: Implementing IDS/IPS (The Watchers)**

> [!TIP]
> **Goal:** : Detect and stop malicious traffic that bypasses firewalls.

- [ ] **Strategic Deployment:** Place `NIDS` sensors at critical network choke points to monitor east-west and north-south traffic.

- [ ] **Host Monitoring:** Install `HIPS` agents on critical servers to detect suspicious process execution and file changes.

- [ ] **Rule Tuning:** Continuously tune signature and anomaly rules to minimize `False Positives` while ensuring no `False Negatives` occur.

- [ ] **SIEM Integration:** Feed IDS/IPS alerts into a `SIEM` for correlation with other security events.

---

### **Stage 4: Utilizing Deception (The Traps)**

> [!TIP]
> **Goal:** : Gather threat intelligence and waste attacker time.

- [ ] **Honeypot Deployment:** Deploy `Honeypots` (both low and high interaction) in the DMZ and internal network to attract attackers.

- [ ] **Traffic Redirection:** Use `Sinkholes` to capture traffic destined for known malicious domains or IPs.

- [ ] **Intelligence Gathering:** Analyze logs and activity from deception tools to inform `Basics and Concepts of Threat Hunting`.

---

### **Stage 5: Operations & Continuous Improvement**

> [!TIP]
> **Goal:** : Integrate into daily security operations.

- [ ] **Incident Response Integration:** Utilize these tools during **Incident Response Process** for rapid **threat identification and containment** of affected systems.

- [ ] **Zero Trust Alignment:** Ensure firewall and IPS policies align with **Zero Trust** principles, verifying every connection attempt.

- [ ] **Performance Tuning:** Regularly review and tune **IDS/IPS rules, firewall ACLs** to balance security and performance.

- [ ] **Threat Intelligence Integration:** Feed **IOCs from threat intelligence** into firewalls and IDS for proactive blocking.

- [ ] **Red/Purple Team Testing:** Conduct regular **red team exercises** to validate detection capabilities and identify blind spots.

---

### **Stage 6: Email Security Architecture**

> [!TIP]
> **Goal:** : Secure the #1 initial access vector — email infrastructure.

- [ ] **Email Authentication (SPF/DKIM/DMARC):** Configure **SPF records** (authorized senders), **DKIM signing** (message integrity), and **DMARC policies** (alignment enforcement with p=reject). Validate with **dmarcian, MXToolbox, Google Postmaster**.

- [ ] **Secure Email Gateway (SEG):** Deploy and tune **Proofpoint, Mimecast, Microsoft Defender for Office 365, or open-source alternatives** — configure **anti-spam, anti-phishing, attachment sandboxing, URL rewriting/detonation**.

- [ ] **Anti-Phishing Defenses:** Implement **display name spoofing detection, lookalike domain alerting, external sender banners, impersonation protection policies** targeting executive and financial staff.

- [ ] **Email DLP:** Configure **Data Loss Prevention rules** to detect and block **outbound PII, credentials, source code, financial data** via email attachments and body content.

- [ ] **Mail Flow Architecture:** Understand **MTA (Mail Transfer Agent) routing, MX records, SMTP relay chains, TLS enforcement (DANE/MTA-STS)**, and how mail traverses from sender to recipient.

- [ ] **Email Forensics Awareness:** Understand **email header analysis (Received headers, X-headers, Message-ID tracking)** to trace phishing campaigns and identify spoofed messages.

---

### **Lab Progression**

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Deploy Snort/Suricata IDS in a lab and write 5 custom rules | IDS ruleset + test results |
| 2 | Configure pfSense/iptables firewall with zone-based policies | Firewall architecture diagram + ruleset |
| 3 | Deploy a honeypot (Cowrie, T-Pot, or HoneyD) and analyze attacker behavior | Honeypot analysis report (24-48 hours of data) |
| 4 | Test IDS evasion techniques and tune rules to detect them | Evasion vs. detection comparison report |
| 5 | Build a complete perimeter defense lab (firewall + IDS + honeypot) | Integrated defense architecture document |

> [!IMPORTANT]
> **Move-On Gate:** You can deploy and configure IDS/IPS, write custom detection rules, deploy honeypots for deception, and tune detection to minimize false positives while catching evasion attempts.

---

### **Stage 7: DNS Security Operations**

> [!TIP]
> **Goal:** : Detect and prevent DNS-based attacks and data exfiltration.

- [ ] **DNSSEC:** Understand **DNSSEC signing, validation chain, DS/DNSKEY records**, and deployment challenges. Know how DNSSEC prevents **cache poisoning** but does not encrypt queries.

- [ ] **Encrypted DNS (DoH/DoT):** Know that **DNS over HTTPS (DoH, port 443)** and **DNS over TLS (DoT, port 853)** encrypt DNS queries, creating **visibility gaps for network defenders**. Understand how to detect and control encrypted DNS via **endpoint policy, proxy-based inspection, and canary domain monitoring**.

- [ ] **DNS Sinkholing:** Deploy **DNS sinkholes** to redirect known malicious domains (C2, phishing, DGA-generated) to controlled IPs for **detection, containment, and IOC enrichment**.

- [ ] **DNS Firewall (RPZ):** Configure **Response Policy Zones (RPZ)** on internal DNS resolvers to block resolution of **malicious, newly-registered, or DGA-generated domains** based on threat intelligence feeds.

- [ ] **DNS Exfiltration Detection:** Monitor for **high-entropy subdomain queries, unusually long DNS names (>50 chars), high query volumes to single domains, TXT record abuse** indicating **DNS tunneling (iodine, dnscat2)**. Correlate with **SIEM alerts and NetFlow** for confirmation.

- [ ] **Passive DNS Monitoring:** Deploy **passive DNS collection (passivedns, Farsight DNSDB)** to maintain historical resolution records for **threat hunting, domain reputation tracking, and incident response**.

---

<a id="toc-part-15-osint--threat-intelligence"></a>
## Part 15: OSINT & Threat Intelligence

### **Stage 1: Passive Reconnaissance & Data Collection**

> [!TIP]
> **Goal:** : Gather intelligence without touching target infrastructure.

- [ ] **Search Engine Intelligence:** Master **Google/Bing/Yandex dorks** for exposed data; use **Shodan/Censys/Zoomeye** for internet-wide scanning.

- [ ] **Social Media Mining:** Scrape **LinkedIn, Twitter, Facebook, Instagram** for employees, org structure, tech stack mentions, and personal details.

- [ ] **Domain & Infrastructure:** Use **WHOIS, DNS records (MX, TXT, SPF, DMARC), Certificate Transparency logs** to map infrastructure.

- [ ] **Breach Data Analysis:** Query **HIBP (Have I Been Pwned), Dehashed, Snusbase** for leaked credentials and PII.

- [ ] **Code Repository Mining:** Search **GitHub, GitLab, Bitbucket** for exposed **API keys, credentials, internal IPs, architecture docs**.

- [ ] **Dark Web Monitoring:** Monitor **paste sites, forums, dark web marketplaces** for leaked data, exploit sales, threat actor chatter.

---

### **Stage 2: Threat Intelligence Analysis**

> [!TIP]
> **Goal:** : Convert raw data into actionable intelligence.

- [ ] **IOC Collection:** Aggregate **file hashes, domains, IPs, email patterns** from **threat feeds, MISP, AlienVault OTX**.

- [ ] **Threat Actor Profiling:** Study **APT groups, TTPs, infrastructure patterns** using **MITRE ATT&CK, threat reports (Mandiant, CrowdStrike)**.

- [ ] **Campaign Tracking:** Monitor **active campaigns, malware families, exploit trends** to understand current threat landscape.

- [ ] **Attribution Analysis:** Correlate **infrastructure, code patterns, language artifacts** to attribute attacks to specific actors.

- [ ] **Victimology Studies:** Understand **target selection, industry focus, geographic distribution** of threat actors.

---

### **Stage 3: OSINT Automation & Tooling**

> [!TIP]
> **Goal:** : Scale reconnaissance with automation.

- [ ] **Reconnaissance Frameworks:** Master **Recon-ng, theHarvester, SpiderFoot, Maltego** for automated data collection.

- [ ] **Subdomain Enumeration:** Use **Amass, Subfinder, Assetfinder, DNSRecon** to discover **subdomains, ASNs, IP ranges**.

- [ ] **API Integration:** Leverage **VirusTotal, Shodan, SecurityTrails, Hunter.io APIs** for programmatic data access.

- [ ] **Custom Scripting:** Build **Python/Bash scripts** to automate **scraping, parsing, correlation** of OSINT data.

- [ ] **Data Pipeline:** Create **ETL pipelines** to aggregate, normalize, and store intelligence in **databases/dashboards**.

---

### **Stage 4: Threat Intelligence Dissemination**

> [!TIP]
> **Goal:** : Communicate intelligence effectively to stakeholders.

- [ ] **Intelligence Reports:** Create **tactical (IOCs), operational (TTPs), strategic (trends)** reports for different audiences.

- [ ] **TLP Classification:** Apply **Traffic Light Protocol (White, Green, Amber, Red)** for information sharing sensitivity.

- [ ] **STIX/TAXII:** Use **Structured Threat Information Expression (STIX)** and **TAXII** for standardized intel sharing.

- [ ] **Threat Briefings:** Deliver **executive briefings** highlighting **risks, trends, recommended actions** in non-technical language.

- [ ] **Community Collaboration:** Participate in **ISACs, threat intel communities, CTI sharing platforms** for collective defense.

---

### **Lab Progression**

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Perform complete OSINT profile of a public figure (using only public data) | OSINT report with sources |
| 2 | Use Shodan/Censys to discover exposed services on a target range | Exposure assessment report |
| 3 | Set up automated threat intelligence feeds (MISP or OpenCTI) | Working TI platform with 3+ feeds |
| 4 | Produce a threat intelligence report on a specific APT group | Structured TI report (TTPs, IOCs, recommendations) |
| 5 | Create STIX-formatted IOCs and share via TAXII server in lab | Working STIX/TAXII demo |

> [!IMPORTANT]
> **Move-On Gate:** You can gather, analyze, and disseminate threat intelligence using industry-standard tools and formats, and produce actionable intelligence reports for both technical and executive audiences.

---

### **GRC Fundamentals Sidebar** _(Early Supplement for Defensive Careers)_

> **Why Here:** SOC analysts, detection engineers, and blue team professionals need basic framework and compliance context much earlier than Phase 8. Complete this sidebar before moving to Phase 4 if you are pursuing a defensive career track. Full GRC depth is covered in Part 35 (Phase 8).

- [ ] **NIST Cybersecurity Framework (CSF):** Understand the **5 core functions** — **Identify, Protect, Detect, Respond, Recover** — and how they map to SOC operations and alert prioritization.

- [ ] **CIS Controls (v8) Awareness:** Know the **18 Critical Security Controls** and **Implementation Groups (IG1–IG3)** as a prioritized, actionable defense checklist.

- [ ] **MITRE ATT&CK as Compliance:** Use **ATT&CK technique coverage mapping** to demonstrate and measure detection maturity — this is how modern SOCs prove value.

- [ ] **Risk Equation Basics:** Understand **Risk = Threat × Vulnerability × Impact** and use it to prioritize alerts and findings over raw CVSS scores.

- [ ] **Incident Response Frameworks:** Know the **NIST SP 800-61** IR lifecycle (Preparation → Detection → Containment → Eradication → Recovery → Lessons Learned) and how it structures SOC playbooks.

- [ ] **Compliance Awareness:** Understand at a high level what **PCI-DSS, HIPAA, GDPR, SOC 2** require — enough to explain why specific controls exist and what auditors look for.

> 📌 _Full GRC depth (audit mechanics, vendor risk, continuous compliance, regulatory testing) is covered in [Part 35: GRC](file:///home/smilo/Desktop/MY_Folder/Cyber-Security/Roadmap.md#toc-part-35-governance-risk--compliance-grc) (Phase 8)._

---

<a id="toc-part-16-adversary-emulation--purple-teaming"></a>