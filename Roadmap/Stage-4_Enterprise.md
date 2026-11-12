
# Stage 4 — Enterprise

---

### 🧭 Stage Navigation

| ◀ Previous Stage | 🏠 Master Hub | Next Stage ➔ | 📑 Quick Jump |
| :---: | :---: | :---: | :--- |
| [[Cyber-Security/Roadmap/Stage-3_Web-and-App-Sec\|◀ Stage 3: Web & App Sec]] | [[Cyber-Security/Roadmap/README\|MASTER_README]] | [[Cyber-Security/Roadmap/Stage-5_Specialized\|Stage 5: Specialized ➔]] | [[#🗂️ Table of Contents\|🗂️ Table of Contents]] · [[#🛠️ Mandatory Tool Stack (Must Master in This Stage)\|🛠️ Mandatory Tools]] · [[#🎮 Concurrent CTF Practice — Stage 4\|🎮 CTF Practice]] · [[#🏁 Stage Gate 3 — Enterprise Domain Compromise & Reporting\|🏁 Stage Gate 3]] |

---

> [!NOTE]
> **Stage Overview — Modules 19–26**
> - **⏱️ Estimated Time:** ~10–13 weeks of consistent daily sessions
> - **🎯 Modules:** `19` Active Directory & Entra ID · `20` Cloud Security · `21` Containers & Kubernetes · `22` Adversary Emulation & Purple Teaming · `23` Sniffing & Spoofing · `24` Social Engineering · `25` Malware & Weaponization (conceptual) · `26` Pentest Reporting
> - **🔴 Gate:** AD domain attacked end-to-end · BloodHound exports in Git · 1 professional report — before moving to Stage 5
> - **🎯 Primary Focus:** Active Directory & Entra ID attack paths, cloud security (AWS/Azure/GCP), container & Kubernetes exploitation, adversary emulation & purple teaming, lateral movement, social engineering, and professional pentest reporting.

---

> [!NOTE]
> ### 📝 Stage 4 Documentation Requirements
> Enterprise infrastructure work must be thoroughly documented. Required artifacts:
> - **[[BloodHound]] exports** — attack path graphs with annotated findings
> - **Cloud attack evidence** — CloudTrail logs, IAM policy analysis, exploitation screenshots
> - **Terraform/CloudFormation configs** — infrastructure-as-code for lab environments committed to Git
> - **Purple team ATT&CK heatmap** — technique coverage matrix showing detection gaps
> - **Git commits** — all configs, exports, and reports committed
> _By the end of Stage 4, I should have enterprise attack documentation rivaling junior consultant deliverables._

> [!IMPORTANT]

### 🛠️ Mandatory Tool Stack (Must Master in This Stage)
> | Priority | Tool | Purpose & Core Skills | ✅ Complete By |
> | :--- | :--- | :--- | :--- |
> | **Tier 1 (Mandatory)** | [[BloodHound]] & SharpHound | AD/Azure graph collection, Cypher query analysis, ACL abuse pathing (`ShortestPath to Domain Admins`). | **Module 19 — Topic 1 (Discovery & Enumeration)** |
> | **Tier 1 (Mandatory)** | [[Impacket]] Suite | Protocol-level attacks (`secretsdump.py`, `psexec.py`, `wmiexec.py`, `GetNPUsers.py`, `GetUserSPNs.py`). | **Module 19 — Topic 2 (Credential & Auth Attacks)** |
> | **Tier 1 (Mandatory)** | [[Mimikatz]] & [[Rubeus]] | LSASS credential dumping (`sekurlsa::logonpasswords`), Kerberoasting, AS-REP roasting, Overpass-the-Hash, ticket injection. | **Module 19 — Topic 2 (Credential & Auth Attacks)** |
> | **Tier 1 (Mandatory)** | **Certipy** | Active Directory Certificate Services (ADCS) enumeration, ESC1/ESC4 template exploitation, shadow credentials. | **Module 19 — Topic 3 (Delegation, ACL, and ADCS Abuse)** |
> | **Tier 1 (Mandatory)** | [[NetExec]] (nxc) | Network spray & lateral movement orchestrator across SMB, WinRM, LDAP, MSSQL, and RDP. | **Module 19 — Topic 4 (Lateral Movement & Persistence)** |
> | **Tier 1 (Mandatory)** | **Prowler & Pacu** | AWS/Azure cloud security posture assessment, IAM privilege escalation, misconfiguration exploitation. | **Module 20 — Topic 5 (Cloud-Specific Attack Vectors)** |
> | **Tier 2 (Secondary)** | [[Evil-WinRM]] | WinRM remote shell execution, DLL payload loading, pass-the-hash administrative control. | **Module 19 — Topic 4 (Lateral Movement & Persistence)** |
> | **Tier 2 (Secondary)** | [[Kerbrute]] | Fast Active Directory user enumeration and password brute-forcing via Kerberos pre-auth. | **Module 19 — Topic 1 (Discovery & Enumeration)** |
> | **Tier 2 (Secondary)** | **Trivy & ScoutSuite** | Container/Kubernetes image vulnerability scanning and multi-cloud security auditing. | **Module 21 — Topic 1 & 2 (Container & Kubernetes Security)** |
> **Stage 4 Exit Gate:** I cannot pass Stage 4 until I can enumerate domain accounts with `Kerbrute`, collect AD graph data with `SharpHound`, visualize privilege escalation paths in `BloodHound`, exploit an ADCS misconfiguration with `Certipy`, and dump the NTDS.dit database via `secretsdump.py`.

---

### 🗂️ Table of Contents

- [[#Module 19: Active Directory & Entra ID|Module 19: Active Directory & Entra ID]]
  - [[#Topic 1: Discovery & Enumeration — 🔬 Practical|Topic 1: Discovery & Enumeration]]
  - [[#Topic 2: Credential & Auth Attacks — 🔬 Practical|Topic 2: Credential & Auth Attacks]]
  - [[#Topic 3: Delegation, ACL, and ADCS Abuse — 🔬 Practical|Topic 3: Delegation, ACL, and ADCS Abuse]]
  - [[#Topic 4: Lateral Movement & Persistence — 🔬 Practical|Topic 4: Lateral Movement & Persistence]]
  - [[#Topic 5: Entra ID (Azure AD) & Hybrid Attacks — 🧠🔬 Mixed|Topic 5: Entra ID (Azure AD) & Hybrid Attacks]]
  - [[#Lab Progression (Module 19: Active Directory & Entra ID)|Lab Progression (Module 19: Active Directory & Entra ID)]]
- [[#Module 20: Cloud Computing|Module 20: Cloud Computing]]
  - [[#Topic 1: Architecture & Governance — 🧠 Conceptual|Topic 1: Architecture & Governance]]
  - [[#Topic 2: Storage & Data Security — 🔬 Practical|Topic 2: Storage & Data Security]]
  - [[#Topic 3: Modern Infrastructure & Deployment — 🧠🔬 Mixed|Topic 3: Modern Infrastructure & Deployment]]
  - [[#Topic 4: Automation & Scripting — 🔬 Practical|Topic 4: Automation & Scripting]]
  - [[#Topic 5: Cloud-Specific Attack Vectors — 🔬 Practical|Topic 5: Cloud-Specific Attack Vectors]]
  - [[#Topic 6: IAM & PAM Attack Surface — 🔬 Practical|Topic 6: IAM & PAM Attack Surface]]
- [[#Module 21: Container & Orchestration Security|Module 21: Container & Orchestration Security]]
  - [[#Topic 1: Container Fundamentals & Attacks — 🔬 Practical|Topic 1: Container Fundamentals & Attacks]]
  - [[#Topic 2: Kubernetes Security — 🔬 Practical|Topic 2: Kubernetes Security]]
  - [[#Topic 3: Container Runtime Security — 🧠🔬 Mixed|Topic 3: Container Runtime Security]]
  - [[#Topic 4: Secrets & Configuration Management — 🔬 Practical|Topic 4: Secrets & Configuration Management]]
  - [[#Topic 5: CI/CD & Workflow Automation Attacks — 🔬 Practical|Topic 5: CI/CD & Workflow Automation Attacks]]
  - [[#Lab Progression (Module 21: Container & Orchestration Security)|Lab Progression (Module 21: Container & Orchestration Security)]]
  - [[#Topic 6: Hypervisor Security — 🧠 Conceptual|Topic 6: Hypervisor Security]]
- [[#Module 22: Adversary Emulation & Purple Teaming|Module 22: Adversary Emulation & Purple Teaming]]
  - [[#Topic 1: MITRE ATT&CK Framework Mastery — 🧠 Conceptual|Topic 1: MITRE ATT&CK Framework Mastery]]
  - [[#Topic 2: APT & Threat Actor Emulation — 🔬 Practical|Topic 2: APT & Threat Actor Emulation]]
  - [[#Topic 3: Purple Team Exercises — 🧠🔬 Mixed|Topic 3: Purple Team Exercises]]
  - [[#Topic 4: Metrics & Reporting — 🧠 Conceptual|Topic 4: Metrics & Reporting]]
  - [[#Lab Progression (Module 22: Adversary Emulation & Purple Teaming)|Lab Progression (Module 22: Adversary Emulation & Purple Teaming)]]
- [[#Module 23: Sniffing & Spoofing|Module 23: Sniffing & Spoofing]]
  - [[#Topic 1: The Environment & Fundamentals (The Setup) — 🧠🔬 Mixed|Topic 1: The Environment & Fundamentals (The Setup)]]
  - [[#Topic 2: Sniffing & Passive Reconnaissance (The Ear) — 🔬 Practical|Topic 2: Sniffing & Passive Reconnaissance (The Ear)]]
  - [[#Topic 3: Spoofing & Active Deception (The Lie) — 🔬 Practical|Topic 3: Spoofing & Active Deception (The Lie)]]
  - [[#Topic 4: Man-in-the-Middle & Exploitation (The Kill) — 🔬 Practical|Topic 4: Man-in-the-Middle & Exploitation (The Kill)]]
  - [[#Topic 5: Defenses & Mitigation (The Shield) — 🧠 Conceptual|Topic 5: Defenses & Mitigation (The Shield)]]
  - [[#Lab Progression (Module 23: Sniffing & Spoofing)|Lab Progression (Module 23: Sniffing & Spoofing)]]
- [[#Module 24: Social Engineering|Module 24: Social Engineering]]
  - [[#Topic 0: The Psychology of Social Engineering (The Foundation) — 🧠 Conceptual|Topic 0: The Psychology of Social Engineering (The Foundation)]]
  - [[#Topic 1: Intelligence & Reconnaissance (The Setup) — 🔬 Practical|Topic 1: Intelligence & Reconnaissance (The Setup)]]
  - [[#Topic 2: The Digital Assault (Remote Vectors) — 🧠🔬 Mixed|Topic 2: The Digital Assault (Remote Vectors)]]
  - [[#Topic 3: The Human Element (Direct Interaction) — 🧠 Conceptual|Topic 3: The Human Element (Direct Interaction)]]
  - [[#Topic 4: The Physical Breach (Boots on the Ground) — 🧠🔬 Mixed|Topic 4: The Physical Breach (Boots on the Ground)]]
  - [[#Topic 5: Defense & Awareness (The Shield) — 🧠 Conceptual|Topic 5: Defense & Awareness (The Shield)]]
  - [[#Lab Progression (Module 24: Social Engineering)|Lab Progression (Module 24: Social Engineering)]]
- [[#Module 25: Malware & Weaponization (Conceptual)|Module 25: Malware & Weaponization (Conceptual)]]
  - [[#Topic 1: The Design & Logic (Architecture) — 🧠 Conceptual|Topic 1: The Design & Logic (Architecture)]]
  - [[#Topic 2: The Payload & Mechanism — Exposure Survey — 🧠🔬 Mixed|Topic 2: The Payload & Mechanism — Exposure Survey]]
  - [[#Topic 3: Evasion & Defense Bypassing — Exposure Survey — 🧠 Conceptual|Topic 3: Evasion & Defense Bypassing — Exposure Survey]]
  - [[#Topic 4: Persistence & Escalation — Exposure Survey — 🧠 Conceptual|Topic 4: Persistence & Escalation — Exposure Survey]]
  - [[#Topic 5: Counter-Forensics & Cleanup — Exposure Survey — 🧠 Conceptual|Topic 5: Counter-Forensics & Cleanup — Exposure Survey]]
  - [[#Topic 5b: Windows Persistence Analysis & Memory Forensics — 🧠 Conceptual|Topic 5b: Windows Persistence Analysis & Memory Forensics]]
  - [[#Topic 6: Document & Cloud Weaponization — 🔬 Practical|Topic 6: Document & Cloud Weaponization]]
  - [[#Lab Progression (Module 25: Malware & Weaponization)|Lab Progression (Module 25: Malware & Weaponization)]]
- [[#Module 26: Pentest Methodologies & Report Writing|Module 26: Pentest Methodologies & Report Writing]]
  - [[#Topic 1: Industry-Standard Engagement Frameworks — 🧠 Conceptual|Topic 1: Industry-Standard Engagement Frameworks]]
  - [[#Topic 2: Scoping, Legal Frameworks & Engagement Management — 🧠 Conceptual|Topic 2: Scoping, Legal Frameworks & Engagement Management]]
  - [[#Topic 3: Structured Threat Modeling — 🧠 Conceptual|Topic 3: Structured Threat Modeling]]
  - [[#Topic 4: Vulnerability Scoring & Risk Prioritization — 🧠 Conceptual|Topic 4: Vulnerability Scoring & Risk Prioritization]]
  - [[#Topic 5: Professional Report Writing — 🧠🔬 Mixed|Topic 5: Professional Report Writing]]
  - [[#Lab Progression (Module 26: Penetration Testing Methodologies & Report Writing)|Lab Progression (Module 26: Penetration Testing Methodologies & Report Writing)]]
  - [[#🎮 Concurrent CTF Practice — Stage 4|🎮 Concurrent CTF Practice — Stage 4]]
- [[#🏁 Stage Gate 3 — Enterprise Domain Compromise & Reporting|🏁 Stage Gate 3 — Enterprise Domain Compromise & Reporting]]

---

---

## Module 19A: SOC & Security Operations
[[Module-19A_SOC-Security-Operations|📁]]

> [!NOTE]
> **📚 Recommended Books for This Module**
> - 🔴 `Blue Team Handbook: SOC, SIEM, and Threat Hunting` — Comprehensive SOC operations guide
> - 🔴 `Practical Threat Intelligence and Data-Driven Threat Hunting` — Hands-on threat hunting
> - 🟡 `Security Operations Center: Building, Operating, and Maintaining your SOC` — SOC architecture & operations
> - 🟡 `Applied Network Security Monitoring` — NSM and detection engineering
> - 🟢 `The Practice of Network Security Monitoring` — Foundational NSM concepts

> [!IMPORTANT]
> **Why This Module Exists:** Red teamers who understand blue team operations are MORE EFFECTIVE at bypassing detection. SOC knowledge makes you versatile: offensive skills + defensive awareness = market-ready security professional. This module provides hands-on SIEM engineering and detection writing — NOT just theory.

> [!TIP]
> ⏱️ **Module 19A Total Time Budget: 2–3 weeks**
> T1 (SOC fundamentals): 2 days | T2 (Log management): 2 days | T3 (SIEM engineering): 1 week | T4 (EDR/XDR): 2-3 days | T5 (Detection engineering): 3-4 days | T6 (Threat hunting): 3-4 days.
> SIEM skills are IN DEMAND. Splunk + Microsoft Sentinel + Elastic experience makes you competitive for SOC analyst, detection engineer, and threat hunter roles. As a red teamer, you will use this knowledge to understand what defenders see and how to evade their detections.

### Topic 1: SOC Fundamentals & Architecture — 🧠 Conceptual
[[Topic-1_SOC-Fundamentals|📁]]

> [!TIP]
> **Goal:** Understand how Security Operations Centers function and what they monitor

> [!NOTE]
> ⏱️ **Time Bracket: 2 days** — Master Security Operations Center organizational structure and workflows. Understand the three-tier analyst model (Tier 1 for alert triage, Tier 2 for investigation and analysis, Tier 3 for advanced threat hunting and threat intelligence), specialized roles (Detection Engineers create rules, Incident Responders handle escalations), and complete SOC workflows from alert ingestion through triage, investigation, escalation, remediation, and documentation. Learn critical SOC metrics including MTTD (Mean Time to Detect), MTTR (Mean Time to Respond), false positive rates, and alert fatigue management. Study the SOC technology stack components (SIEM for log correlation, EDR/XDR for endpoint visibility, NDR for network monitoring, SOAR for automation, TIP for threat intelligence, case management systems). Understand 24/7 operational challenges (shift handoffs, playbook adherence, on-call rotation, burnout) and SOC maturity progression from reactive (alert-driven) to proactive (hunting, baselining) to predictive (AI/ML-driven anomaly detection). Deliverable: diagram a complete SOC technology stack and workflow showing how an alert moves from generation to resolution.

- [ ] **SOC Organizational Structure:** Understand the three-tier analyst model: **Tier 1** performs alert triage and initial categorization, **Tier 2** conducts investigation and analysis of escalated incidents, **Tier 3** performs advanced threat hunting and threat intelligence correlation. Specialized roles include **Detection Engineers** who create and tune detection rules, and **Incident Responders** who handle escalations and remediation. *SOC angle: red teamers who understand SOC structure know which tier detects what — evade Tier 1 automated alerts, survive Tier 2 investigation, avoid Tier 3 hunt patterns.*
- [ ] **SOC Workflows:** Master the complete incident lifecycle: **alert ingestion** (SIEM receives events) → **triage** (Tier 1 categorizes severity/validity) → **investigation** (Tier 2 analyzes scope/impact) → **escalation** (promote to Tier 3 or IR) → **remediation** (contain and eradicate threat) → **documentation** (create post-incident report and lessons learned). *SOC angle: each phase has detection opportunities; red team operations must account for handoffs where fresh eyes review earlier activity.*
- [ ] **SOC Metrics — Mean Time to Detect (MTTD):** Time from initial compromise to first detection. Lower is better. *SOC angle: red teamers aim to maximize dwell time before MTTD; blue teamers optimize detection coverage to minimize MTTD.*
- [ ] **SOC Metrics — Mean Time to Respond (MTTR):** Time from detection to containment/remediation. Speed prevents lateral movement. *SOC angle: red team exercises measure MTTR under stress; slow MTTR = more time for objective completion.*
- [ ] **SOC Metrics — False Positive Rate:** Percentage of alerts that are benign. High FPR causes alert fatigue and missed true positives. *SOC angle: red teamers exploit alert fatigue — blend malicious activity into high-noise alerts that analysts dismiss.*
- [ ] **SOC Metrics — Alert Volume & Fatigue:** Daily alert count per analyst. Excessive volume (>100/day/analyst) leads to missed detections. *SOC angle: volume-based DDoS against SOC — flood with false positives to hide real attacks.*
- [ ] **SOC Metrics — Incident Severity Distribution:** Ratio of Critical:High:Medium:Low incidents. Unbalanced distribution indicates tuning issues. *SOC angle: severity inflation (everything Critical) = analyst burnout; severity deflation = real threats categorized Low.*
- [ ] **SOC Technology Stack — SIEM (Security Information & Event Management):** Centralized log aggregation, correlation, and alerting platform. Examples: Splunk, Microsoft Sentinel, Elastic. *SOC angle: SIEM is SOC's eyes — evading SIEM detection rules = evading SOC visibility.*
- [ ] **SOC Technology Stack — EDR/XDR (Endpoint/Extended Detection & Response):** Agent-based endpoint monitoring with behavioral analytics. Examples: CrowdStrike, SentinelOne, Microsoft Defender for Endpoint. *SOC angle: EDR telemetry feeds SIEM; EDR evasion techniques (unhook, direct syscalls) critical for red team.*
- [ ] **SOC Technology Stack — NDR (Network Detection & Response):** Network traffic analysis for lateral movement, C2, exfiltration. Examples: Darktrace, ExtraHop, Vectra. *SOC angle: NDR detects anomalous network behavior; C2 must blend with legitimate traffic patterns.*
- [ ] **SOC Technology Stack — SOAR (Security Orchestration, Automation & Response):** Automates repetitive tasks (enrichment, containment, ticketing). Examples: Palo Alto Cortex XSOAR, Splunk SOAR. *SOC angle: SOAR accelerates response; red team must complete objectives before automated containment triggers.*
- [ ] **SOC Technology Stack — TIP (Threat Intelligence Platform):** Aggregates and correlates threat intelligence feeds (IOCs, TTPs, actor profiles). Examples: ThreatConnect, Anomali, MISP. *SOC angle: TIP matches observed activity to known threats; unique TTPs evade TIP correlation.*
- [ ] **SOC Technology Stack — Case Management Systems:** Track incidents from detection to closure. Examples: TheHive, RTIR, ServiceNow Security Operations. *SOC angle: case management ensures nothing falls through cracks; persistent access requires avoiding case creation entirely.*
- [ ] **24/7 Operations Challenges:** SOC operates continuously with shift handoffs (night shift → day shift knowledge transfer), playbook adherence (consistent response procedures across shifts), on-call rotation (incident escalation paths), and alert fatigue mitigation (tuning rules to reduce noise). *SOC angle: shift changes = opportunity for activity review gaps; exploit handoff periods when fresh analysts haven't internalized context.*
- [ ] **SOC Maturity Model:** SOCs evolve through maturity levels: **Reactive** (purely alert-driven, no hunting), **Proactive** (threat hunting, baseline anomaly detection, threat intelligence integration), **Predictive** (AI/ML anomaly detection, predictive threat modeling, automated response). *SOC angle: reactive SOCs miss novel TTPs; proactive/predictive SOCs require sophisticated evasion and blending with normal behavior.*

---

### Topic 2: Log Management & Analysis — 🔬 Practical
[[Topic-2_Log-Management-Analysis|📁]]

> [!TIP]
> **Goal:** Master log collection, parsing, normalization, and analysis

> [!NOTE]
> ⏱️ **Time Bracket: 2 days** — Master comprehensive log management across all enterprise sources. Study diverse log sources including Windows Event Logs (Security, System, Application, PowerShell, Sysmon), Linux logs (/var/log/auth.log, syslog, auditd, systemd journal), network device logs (firewall, IDS/IPS, proxy, DNS), application logs (web servers, databases, custom applications), and cloud platform logs (AWS CloudTrail, Azure Activity Log, GCP Cloud Logging). Understand log formats (JSON, CEF Common Event Format, LEEF, syslog, XML, key-value pairs) and collection methods (agent-based like Splunk UF/Elastic Beats vs agentless syslog forwarding vs cloud API ingestion). Learn log normalization techniques to map vendor-specific fields to common schemas (CIM, ECS). Define log retention policies balancing compliance requirements, storage costs, and query performance through hot/warm/cold storage tiers. Deep dive into critical Windows Event IDs (4624/4625 logon, 4688 process creation, 4672 privileges, 4768/4769 Kerberos) and Linux authentication/audit logs. Deliverable: manually parse and analyze 5 different log types, then automate extraction using Python or SPL/KQL queries.

- [ ] **Windows Event Logs Collection:** Ingest Security, System, Application, PowerShell, and Sysmon event logs from domain controllers, workstations, and servers. *SOC angle: Windows logs reveal authentication, process execution, and privilege escalation — missing these = blind to core attack chain.*
- [ ] **Linux Logs Collection:** Collect /var/log/auth.log (authentication), syslog (system messages), auditd (system calls/file access), and systemd journal logs. *SOC angle: Linux logs track SSH access, sudo abuse, and persistence mechanisms; missing auditd = no forensic trail.*
- [ ] **Network Device Logs Collection:** Ingest firewall (connection permit/deny), IDS/IPS (threat detections), proxy (web access), and DNS (query/response) logs. *SOC angle: network logs detect lateral movement, C2 beaconing, and data exfiltration; missing DNS logs = no malware domain detection.*
- [ ] **Application Logs Collection:** Collect web server (access/error logs), database (query/authentication), and custom application logs. *SOC angle: application logs reveal exploitation attempts (SQL injection, path traversal), privilege abuse, and data access patterns.*
- [ ] **Cloud Logs Collection:** Ingest AWS CloudTrail (API calls), Azure Activity Log (resource changes), GCP Cloud Logging (service operations). *SOC angle: cloud logs track identity abuse, resource creation (C2 infrastructure), and configuration changes; cloud-blind SOC = missed cloud attacks.*
- [ ] **Log Formats Understanding:** Master JSON, CEF (Common Event Format), LEEF, syslog RFC 5424, XML, and key-value pair formats for cross-platform parsing. *SOC angle: format mismatch breaks parsing; unparsed logs = missed detections; attackers exploit format edge cases.*
- [ ] **Agent-Based Log Collection:** Deploy Splunk Universal Forwarder, Elastic Beats, or Azure Monitor Agent on endpoints for reliable log shipping. *SOC angle: agents provide guaranteed delivery and buffering; red team may kill agents to create visibility gaps.*
- [ ] **Agentless Log Collection:** Configure syslog forwarding, WinRM remote log access, or API ingestion for network devices and appliances without agent support. *SOC angle: agentless = network-dependent; network segmentation or firewall rules can block log flow.*
- [ ] **Cloud-Native Log Connectors:** Use AWS S3 ingestion, Azure Event Hub, or GCP Pub/Sub for native cloud log collection. *SOC angle: cloud connector misconfiguration = delayed log ingestion; real-time detection requires proper streaming setup.*
- [ ] **Log Normalization to Common Schemas:** Map vendor-specific field names (src_ip vs source.ip vs ClientIP) to Common Information Model (CIM) or Elastic Common Schema (ECS). *SOC angle: normalized fields enable cross-platform correlation; unnormalized logs = detection rules fail across vendors.*
- [ ] **Log Retention Policy Design:** Define hot (fast SSD, 7-30 days), warm (slower disk, 30-90 days), cold (archive, 1+ years) storage tiers balancing compliance, costs, and query performance. *SOC angle: short retention = limited historical hunting; attackers exploit retention gaps to hide long-term persistence.*
- [ ] **Event ID 4624/4625 Analysis:** Track successful (4624) and failed (4625) Windows logon events including logon type (2=interactive, 3=network, 10=RDP) and source workstation. *SOC angle: type 3 logons from workstation-to-workstation = lateral movement; failed logons = brute force or password spray.*
- [ ] **Event ID 4688 Process Creation:** Monitor new process creation with full command-line arguments to detect suspicious execution (PowerShell, cmd, regsvr32, rundll32). *SOC angle: command-line logging reveals LOLBins abuse, encoded commands, and script execution; disabled logging = blind to execution.*
- [ ] **Event ID 4672 Special Privileges:** Track when accounts are assigned special privileges (SeDebugPrivilege, SeImpersonatePrivilege) indicating admin-level activity. *SOC angle: unexpected privilege assignment = potential privilege escalation or token manipulation.*
- [ ] **Event ID 4768/4769 Kerberos Analysis:** Monitor TGT requests (4768) and TGS requests (4769) for Kerberoasting (RC4 encryption), Golden Ticket (unusual TGT lifetime), and service access patterns. *SOC angle: TGS requests for high-value SPNs with RC4 = Kerberoasting; anomalous TGT = Golden Ticket abuse.*
- [ ] **Event ID 4776 NTLM Authentication:** Track NTLM authentication events to detect Pass-the-Hash attacks and environments where Kerberos should be used but NTLM falls back. *SOC angle: NTLM from unexpected source = Pass-the-Hash; excessive NTLM = Kerberos misconfiguration or downgrade attack.*
- [ ] **Event ID 4720 User Creation:** Alert on new user account creation, especially in privileged groups or during off-hours. *SOC angle: unauthorized user creation = persistence mechanism; backdoor accounts often created post-compromise.*
- [ ] **Event ID 1102 Audit Log Cleared:** Critical alert for audit log clearing attempts, indicating attacker anti-forensics or insider threat cover-up. *SOC angle: log clearing = adversary knows they're being logged; immediate investigation required.*
- [ ] **PowerShell Operational Log Analysis:** Enable script block logging (EventID 4104) and module logging to capture PowerShell commands and scripts executed. *SOC angle: PowerShell is primary post-exploitation tool; script block logging reveals obfuscated commands, download cradles, and malicious scripts.*
- [ ] **Sysmon Log Analysis:** Parse Sysmon Event IDs for process creation (1), network connections (3), file creation (11), registry modifications (12/13), and image loads (7). *SOC angle: Sysmon provides detailed telemetry missing from default Windows logs; critical for endpoint detection.*
- [ ] **Linux auth.log / secure Analysis:** Parse SSH login attempts, sudo command execution, and authentication failures from /var/log/auth.log (Debian/Ubuntu) or /var/log/secure (RHEL/CentOS). *SOC angle: failed SSH attempts = brute force; sudo commands reveal privilege escalation and lateral movement.*
- [ ] **Linux syslog Analysis:** Monitor /var/log/syslog for system-wide messages including service starts/stops, kernel messages, and daemon activity. *SOC angle: unusual service starts (cron jobs, systemd units) = persistence; kernel messages reveal rootkit activity.*
- [ ] **Linux auditd Analysis:** Configure and parse auditd logs for file access (open/read/write), syscall monitoring (execve for command execution), and user actions. *SOC angle: auditd provides syscall-level visibility; tracks file tampering, privilege escalation, and persistence mechanisms.*
- [ ] **Linux journalctl Analysis:** Query systemd journal logs with journalctl for service failures, boot messages, and application logs. *SOC angle: journal logs capture service abuse and systemd timer-based persistence; centralized logging source for modern Linux systems.*

---

### Topic 3: SIEM Engineering — 🔬 Practical

> [!TIP]
> **Goal:** Deploy, configure, and operate SIEM platforms hands-on

> [!NOTE]
> ⏱️ **Time Bracket: 1 week** — SIEM architecture (data ingestion → parsing → indexing → storage → search → correlation → alerting → visualization), Splunk hands-on (SPL syntax, search modes, field extraction, lookups, macros, dashboards, alerts, correlation searches), Microsoft Sentinel hands-on (KQL syntax, data connectors, workbooks, analytics rules, playbooks, incidents), Elastic Stack (Elasticsearch DSL, Logstash parsing, Kibana visualizations, Beats agents), use case development (write detection rules for common attacks: brute force, privilege escalation, lateral movement, data exfiltration), alert tuning (reduce false positives via whitelisting, baselining, threshold adjustment), log source prioritization (critical vs nice-to-have logs). Deliverable: deploy a SIEM (Splunk or Sentinel or Elastic), ingest logs from 3+ sources, create 10+ detection rules, build incident response dashboard.

- [ ] **SIEM Data Collectors & Forwarders:** Deploy agents or configure syslog forwarding to collect logs from distributed sources and send to SIEM indexers. *SOC angle: forwarder failure = visibility gap; attackers target log forwarding to avoid detection.*
- [ ] **SIEM Parsing & Normalization Layer:** Extract structured fields from raw logs using regex, delimiters, or built-in parsers for consistent querying. *SOC angle: parsing failure = unparsed blobs; detection rules require structured fields to function.*
- [ ] **SIEM Indexing & Storage:** Store parsed logs in searchable indexes with time-series optimization for fast queries and retention management. *SOC angle: index corruption or capacity exhaustion = data loss; retention too short = missed long-term persistence.*
- [ ] **SIEM Search & Query Engine:** Execute ad-hoc searches, threat hunts, and investigation queries across indexed data using platform-specific query language. *SOC angle: slow queries = delayed detection; optimize search performance for real-time hunting.*
- [ ] **SIEM Correlation Engine:** Link related events across time, sources, and fields (e.g., same user, IP, or session) to detect multi-stage attacks. *SOC angle: correlation reveals kill chain progression; isolated event analysis misses attack context.*
- [ ] **SIEM Alerting & Notification:** Trigger alerts on detection rule matches and notify analysts via email, Slack, PagerDuty, or ticketing systems. *SOC angle: alert fatigue from false positives = missed true positives; tuning critical for SOC effectiveness.*
- [ ] **SIEM Visualization & Dashboards:** Build real-time dashboards showing KPIs (alert volume, incident count, MTTD/MTTR) and security posture metrics. *SOC angle: dashboards enable rapid situational awareness; missing metrics = blind management decisions.*
- [ ] **SIEM Case Management Integration:** Link SIEM alerts to incident tracking systems (TheHive, ServiceNow, JIRA) for workflow management and closure tracking. *SOC angle: case management ensures accountability; lost tickets = unresolved incidents.*
- [ ] **Splunk Architecture Components:** Understand indexers (data storage/search), search heads (user interface/dashboards), forwarders (log collection agents), and deployment server (centralized config management). *SOC angle: distributed architecture enables scale; single point of failure in search head = SOC paralysis.*
- [ ] **SPL Search Commands:** Master Splunk Processing Language commands including search (filter events), where (conditions), eval (field calculations), stats (aggregations), transaction (session grouping), and tstats (accelerated datamodel searches). *SOC angle: tstats dramatically speeds up searches on large datasets; critical for real-time detection at scale.*
- [ ] **SPL Field Extraction with Regex:** Extract custom fields from logs using regular expressions when auto-extraction fails. *SOC angle: missed field extraction = detection rule failure; custom C2 protocols require manual regex parsing.*
- [ ] **SPL Time Modifiers:** Use earliest and latest parameters to constrain searches to specific time windows for faster queries. *SOC angle: unbounded time searches slow investigations; precise time ranges accelerate incident response.*
- [ ] **SPL Subsearches and Joins:** Correlate events across multiple indexes or data sources using subsearches (nested queries) and join operations. *SOC angle: join enables cross-datasource correlation like matching firewall denies to endpoint process creation.*
- [ ] **Splunk Data Onboarding:** Configure TCP/UDP inputs, file monitoring (batch upload), Windows Event Log collection, and AWS S3 ingestion. *SOC angle: misconfigured inputs = missing logs; validate data flow after onboarding.*
- [ ] **Splunk Field Extractions:** Configure automatic field extraction, delimiter-based parsing, or regex-based extraction for custom log formats. *SOC angle: field extraction quality directly impacts detection rule accuracy.*
- [ ] **Splunk Lookups for Enrichment:** Create CSV lookups to enrich events with external data (asset inventory, user roles, threat intelligence IOCs). *SOC angle: lookup enrichment enables asset-aware alerting and IOC matching.*
- [ ] **Splunk Macros & Saved Searches:** Define reusable macros for common search patterns and saved searches for scheduled execution. *SOC angle: macros improve consistency; saved searches enable scheduled threat hunts.*
- [ ] **Splunk Dashboards & Visualizations:** Build interactive dashboards with charts, tables, and single-value panels for SOC monitoring. *SOC angle: real-time dashboards enable rapid anomaly detection and management visibility.*
- [ ] **Splunk Alerts & Scheduled Searches:** Create scheduled searches that trigger alerts when conditions are met, with throttling to prevent alert storms. *SOC angle: throttling prevents alert fatigue but may suppress recurring attacks; tune carefully.*
- [ ] **Splunk Correlation Searches:** Configure real-time or scheduled correlation searches to detect multi-event attack patterns. *SOC angle: real-time correlation detects fast-moving threats; scheduled correlation handles complex historical analysis.*
- [ ] **Splunk Apps & Add-Ons:** Install Splunk Enterprise Security (premium SIEM features) and Splunk SOAR (automation/orchestration). *SOC angle: ES provides pre-built correlation rules and dashboards; SOAR automates response workflows.*
- [ ] **Microsoft Sentinel Architecture:** Understand Log Analytics workspace (data storage), data connectors (log ingestion), workbooks (dashboards), analytics rules (detection), and automation playbooks (response). *SOC angle: Sentinel architecture tightly integrates with Azure ecosystem; cloud-native SIEM with scale.*
- [ ] **KQL Operators:** Master Kusto Query Language operators including where (filter), project (select columns), extend (add calculated columns), summarize (aggregate), join (correlate), and mv-expand (array expansion). *SOC angle: KQL syntax differs from SPL; summarize enables grouping by attacker IP, user, or technique.*
- [ ] **KQL Time Functions:** Use ago (relative time), between (time range), and bin (time bucketing) for temporal analysis. *SOC angle: time-based analysis reveals attack timelines and beaconing patterns.*
- [ ] **KQL String Functions:** Apply contains, startswith, endswith, and matches regex for pattern matching in logs. *SOC angle: string matching detects malicious command patterns, suspicious domains, and IOC matches.*
- [ ] **KQL Aggregations:** Use count, dcount (distinct count), sum, avg, and percentile for statistical analysis and anomaly detection. *SOC angle: statistical baselines enable deviation-based threat hunting.*
- [ ] **Sentinel Data Connectors:** Configure connectors for Azure AD, Office 365, AWS, Microsoft Defender products, Syslog, and CEF sources. *SOC angle: connector coverage determines visibility; missing connectors = blind spots.*
- [ ] **Sentinel Workbooks:** Create visualization templates for security monitoring, incident trends, and KPI tracking. *SOC angle: workbooks provide executive dashboards and analyst investigation views.*
- [ ] **Sentinel Analytics Rules:** Build scheduled query rules (run every X minutes), anomaly detection rules (ML-based), and fusion rules (multi-stage correlation). *SOC angle: fusion ML correlates signals across products; anomaly detection adapts to environment baselines.*
- [ ] **Sentinel Automation with Logic Apps:** Create playbooks using Azure Logic Apps for automated response actions (isolate endpoint, block IP, send Slack notification). *SOC angle: automation reduces MTTR; misconfigured playbooks can cause outages (e.g., auto-blocking legitimate IPs).*
- [ ] **Sentinel Incidents & Case Management:** Triage, assign, and track incidents from detection through closure with built-in case management. *SOC angle: incident workflow ensures nothing is missed; severity tuning critical for prioritization.*
- [ ] **Sentinel Threat Intelligence Integration:** Ingest STIX/TAXII threat feeds and match indicators against log data automatically. *SOC angle: TI integration enables IOC matching; stale feeds cause false positives.*
- [ ] **Sentinel Hunting Queries & Bookmarks:** Save custom hunting queries and bookmark interesting events for later investigation. *SOC angle: bookmarks preserve investigation context; hunting queries become future detection rules.*
- [ ] **Elasticsearch Distributed Architecture:** Understand Elasticsearch as distributed search and analytics engine with sharding and replication for scale and resilience. *SOC angle: Elasticsearch powers real-time search; shard failures = partial data loss.*
- [ ] **Logstash Data Processing Pipeline:** Configure Logstash input plugins (file, syslog, beats), filter plugins (grok, mutate, geoip), and output plugins (elasticsearch, file) for log transformation. *SOC angle: Logstash parsing quality determines downstream detection effectiveness.*
- [ ] **Kibana Visualization & Dashboards:** Build visualizations and dashboards in Kibana using Discover (log exploration), Lens (drag-and-drop charts), and Canvas (custom layouts). *SOC angle: Kibana provides SOC monitoring interface; dashboard performance impacts analyst productivity.*
- [ ] **Beats Lightweight Shippers:** Deploy Filebeat (log files), Metricbeat (system metrics), Winlogbeat (Windows events), and Packetbeat (network traffic) agents for data collection. *SOC angle: Beats are lightweight agents; minimal performance impact compared to heavy forwarders.*
- [ ] **Elasticsearch DSL Queries:** Write Elasticsearch Query DSL (JSON-based) for complex searches, aggregations, and filtering. *SOC angle: DSL powers programmatic searches for automation and API-based threat hunting.*
- [ ] **Logstash Grok Patterns:** Use grok filter plugin with pre-built or custom patterns to parse unstructured log data. *SOC angle: grok parsing extracts fields from custom log formats; parsing failures = unparsed blobs.*
- [ ] **Kibana Lens Visualizations:** Create charts, tables, and metrics using Kibana Lens drag-and-drop interface for rapid dashboard creation. *SOC angle: Lens accelerates dashboard creation; analyst self-service reduces backlog.*
- [ ] **Elastic Watcher Alerting:** Configure Watcher to trigger alerts on query matches and send notifications or execute actions. *SOC angle: Watcher enables alerting in open-source Elastic; commercial features include ML anomaly detection.*
- [ ] **Elastic Security SIEM Module:** Deploy Elastic Security module with pre-built detection rules, timelines, case management, and endpoint integration. *SOC angle: Elastic Security provides free SIEM capabilities; scales to enterprise with paid features.*

- [ ] **Use Case Development — Brute Force Detection:** Detect multiple failed logins followed by successful login from same source indicating password guessing. *SOC angle: brute force = common initial access; successful login after failures = potential breakthrough.*
- [ ] **Use Case Development — Privilege Escalation Detection:** Monitor admin rights grants, sudden sudo usage spikes, or unexpected privilege assignments. *SOC angle: privilege escalation = critical attack stage; unexpected elevation requires immediate investigation.*
- [ ] **Use Case Development — Lateral Movement Detection:** Identify unusual RDP/SMB connections, especially workstation-to-workstation traffic patterns. *SOC angle: lateral movement = post-compromise spread; east-west traffic anomalies reveal attacker movement.*
- [ ] **Use Case Development — Data Exfiltration Detection:** Alert on large outbound data transfers, unusual protocols, or off-hours uploads to cloud services. *SOC angle: exfiltration = mission success for attacker; volume/timing anomalies indicate data theft.*
- [ ] **Use Case Development — Malware Execution Detection:** Detect suspicious process chains (Office→PowerShell→cmd), known malware hashes, or LOLBins abuse. *SOC angle: malware execution = initial compromise or post-exploitation; process telemetry reveals execution.*
- [ ] **Use Case Development — Reconnaissance Detection:** Identify port scanning activity, excessive LDAP queries, or DNS tunneling attempts. *SOC angle: reconnaissance = pre-attack phase; early detection prevents further exploitation.*
- [ ] **Use Case Development — Credential Theft Detection:** Alert on Mimikatz indicators, LSASS process access, or credential dumping tools. *SOC angle: credential theft = escalation enabler; detecting Mimikatz prevents domain compromise.*
- [ ] **Alert Tuning — Whitelist Legitimate Activity:** Exclude known-good scheduled tasks, service accounts, and admin IPs from detection rules. *SOC angle: whitelisting reduces false positives; stale whitelists include decommissioned or compromised entities.*
- [ ] **Alert Tuning — Baseline Normal Behavior:** Establish baselines for login times, data transfer volumes, and process execution patterns for deviation detection. *SOC angle: baselines enable anomaly detection; without baselines, everything is noise.*
- [ ] **Alert Tuning — Threshold Adjustment:** Configure rules to trigger after N failed logins (not 1) to balance sensitivity and noise. *SOC angle: thresholds reduce alert volume; too high = missed attacks, too low = alert fatigue.*
- [ ] **Alert Tuning — Time-Based Suppression:** Suppress alerts during scheduled maintenance windows when activity is expected. *SOC angle: maintenance window suppression prevents false positives; attackers may exploit suppression timing.*
- [ ] **Alert Tuning — Contextual Enrichment:** Add user role, device criticality, and asset classification to alerts for prioritization. *SOC angle: context enables triage; CEO laptop alert > guest WiFi alert.*
- [ ] **Log Source Prioritization — Critical Tier 1:** Prioritize Windows Security logs, Sysmon, EDR telemetry, and authentication logs for detection. *SOC angle: Tier 1 logs provide attack visibility; missing these = blind SOC.*
- [ ] **Log Source Prioritization — Important Tier 2:** Collect firewall, proxy, DNS, and cloud control plane logs for network/cloud visibility. *SOC angle: Tier 2 logs complement endpoint telemetry; network logs reveal C2 and lateral movement.*
- [ ] **Log Source Prioritization — Nice-to-Have Tier 3:** Optionally collect application logs, debug logs, and verbose logs for deep investigations. *SOC angle: Tier 3 logs useful for forensics but not real-time detection; balance storage costs vs forensic value.*

---

### Topic 4: EDR, XDR & Endpoint Security — 🔬 Practical

> [!TIP]
> **Goal:** Understand endpoint detection and response platforms

> [!NOTE]
> ⏱️ **Time Bracket: 2-3 days** — EDR architecture (agent-based telemetry collection: process, file, network, registry events), endpoint telemetry sources (Sysmon, ETW, kernel callbacks), EDR detection capabilities (behavioral analysis, IOC matching, YARA rules, ML anomaly detection), Microsoft Defender for Endpoint hands-on (alerts, incidents, advanced hunting with KQL, automated investigation & response, threat analytics), EDR evasion awareness (unhooking, direct syscalls, in-memory evasion — understand what attackers do), XDR concept (correlation across endpoint, network, email, cloud). Deliverable: set up Microsoft Defender for Endpoint trial, generate test alerts, write 5 advanced hunting queries for specific TTPs.

- [ ] **EDR Agent-Based Monitoring:** EDR agents deploy kernel-mode and user-mode components on endpoints to collect comprehensive telemetry. *SOC angle: agent-based = deep visibility; attackers target agents (kill process, tamper drivers) to create blind spots.*
- [ ] **EDR Telemetry — Process Events:** Collect process creation/termination, parent-child relationships, command-line arguments, and user context for execution tracking. *SOC angle: process telemetry reveals LOLBins abuse, suspicious parent-child chains (Excel spawning PowerShell), and injection.*
- [ ] **EDR Telemetry — File Operations:** Monitor file creation, modification, deletion, and access patterns to detect malware droppers and persistence. *SOC angle: file telemetry tracks dropper activity, ransomware encryption, and credential file theft.*
- [ ] **EDR Telemetry — Network Connections:** Capture network connections (IP, port, protocol) initiated by processes for C2 and lateral movement detection. *SOC angle: network telemetry reveals C2 beaconing, unusual outbound connections, and SMB lateral movement.*
- [ ] **EDR Telemetry — Registry Modifications:** Track registry key creation, modification, and deletion for persistence and configuration changes. *SOC angle: registry telemetry detects Run key persistence, service creation, and Windows Defender tampering.*
- [ ] **EDR Telemetry — Loaded DLLs/Modules:** Monitor DLL/module loads into processes to detect DLL injection, reflective loading, and malicious libraries. *SOC angle: module load telemetry reveals injection techniques (CreateRemoteThread, QueueUserAPC) and in-memory malware.*
- [ ] **EDR Telemetry Sources — Sysmon:** Enhanced Windows event logging with detailed process, network, file, and registry events. *SOC angle: Sysmon fills gaps in default Windows logging; widely used for detection; attackers may attempt Sysmon driver tampering.*
- [ ] **EDR Telemetry Sources — ETW:** Event Tracing for Windows provides low-level kernel and application telemetry streams. *SOC angle: ETW captures PowerShell script blocks, .NET runtime events, and kernel callbacks; bypassing ETW = common evasion technique.*
- [ ] **EDR Telemetry Sources — eBPF:** Extended Berkeley Packet Filter enables Linux kernel-level monitoring without kernel modules. *SOC angle: eBPF provides Linux syscall and network visibility; modern alternative to auditd for performance.*
- [ ] **EDR Telemetry Sources — Kernel Callbacks:** Kernel-level hooks intercept system calls, process/thread creation, and image loads. *SOC angle: kernel callbacks provide earliest detection point; direct syscalls bypass user-mode hooks but not kernel callbacks.*
- [ ] **EDR Behavioral Analysis:** Detect malicious behavior based on process relationships, command patterns, and execution anomalies (e.g., Office spawning cmd.exe). *SOC angle: behavioral detection catches novel malware; bypassing requires blending with legitimate behavior.*
- [ ] **EDR IOC Matching:** Match observed indicators (file hashes, IPs, domains, registry keys) against threat intelligence feeds. *SOC angle: IOC matching catches known threats; unique malware avoids IOC detection.*
- [ ] **EDR YARA Rule Matching:** Scan files and memory with YARA signatures to detect malware families and tool artifacts. *SOC angle: YARA detects Cobalt Strike, Mimikatz, and webshells; polymorphic malware evades static signatures.*
- [ ] **EDR ML-Based Anomaly Detection:** Use machine learning to identify deviations from baseline behavior (unusual process, network pattern, file activity). *SOC angle: ML adapts to environment; adversarial ML techniques can poison baselines or evade detection.*
- [ ] **EDR Real-Time Blocking vs Post-Execution Detection:** Real-time blocking prevents execution; post-execution detection analyzes after the fact for alerting/remediation. *SOC angle: real-time blocking = prevention; post-execution = detection after initial compromise.*
- [ ] **MDE Portal Navigation:** Explore alerts (triggered detections), incidents (correlated alerts), devices (endpoint inventory), and threat analytics (emerging threats). *SOC angle: MDE provides unified endpoint visibility; portal organization critical for SOC triage workflow.*
- [ ] **MDE Alert Investigation Workflow:** Triage alerts by reviewing detection details, process tree, file analysis, and automated investigation results. *SOC angle: structured investigation workflow reduces MTTR; skip steps = missed persistence or lateral movement.*
- [ ] **MDE Advanced Hunting Tables:** Query DeviceProcessEvents, DeviceNetworkEvents, DeviceFileEvents, DeviceRegistryEvents, and DeviceLogonEvents with KQL for threat hunting. *SOC angle: advanced hunting enables proactive searches for TTPs not covered by alerts.*
- [ ] **MDE Hunt for MITRE ATT&CK Techniques:** Write KQL queries to hunt for specific techniques like T1003.001 (LSASS dumping), T1078 (valid accounts), or T1055 (process injection). *SOC angle: ATT&CK-based hunting ensures coverage of adversary techniques.*
- [ ] **MDE Automated Investigation & Response (AIR):** Enable automated investigation of alerts with machine-driven evidence collection and remediation recommendations. *SOC angle: AIR accelerates response for common threats; human oversight still required for complex investigations.*
- [ ] **MDE Threat & Vulnerability Management:** Identify endpoint vulnerabilities, misconfigurations, and missing patches for remediation prioritization. *SOC angle: vulnerability management reduces attack surface; unpatched systems = easy initial access.*
- [ ] **MDE Attack Surface Reduction (ASR) Rules:** Configure rules to block common attack techniques (Office macros, script execution, credential theft). *SOC angle: ASR rules provide prevention layer; overly aggressive rules cause operational impact.*
- [ ] **MDE Endpoint Firewall & Network Protection:** Manage Windows Firewall policies and enable network protection (block malicious IPs/domains) centrally. *SOC angle: centralized firewall control prevents C2 and lateral movement at network layer.*
- [ ] **MDE Integration with Microsoft Sentinel:** Forward MDE alerts and telemetry to Sentinel for cross-platform correlation with non-endpoint data. *SOC angle: SIEM integration enables correlation of endpoint activity with network/cloud events.*
- [ ] **CrowdStrike Falcon Awareness:** Understand Falcon's process tree visualization, IOA (Indicator of Attack) detection, and RTR (Real-Time Response) for live investigation. *SOC angle: Falcon's IOA focus detects behaviors over signatures; RTR enables live forensics without RDP.*
- [ ] **SentinelOne Awareness:** Understand autonomous response (automatic threat isolation and rollback) and Storyline visualization for attack reconstruction. *SOC angle: SentinelOne's rollback capability reverses file changes; autonomous response reduces MTTR but requires trust.*
- [ ] **Carbon Black Awareness:** Understand Carbon Black EDR + NGAV (next-gen antivirus) combo for prevention and detection. *SOC angle: Carbon Black records extensive telemetry for forensic analysis.*
- [ ] **Trend Micro Vision One Awareness:** Understand Vision One's XDR correlation across endpoints, email, servers, and cloud workloads. *SOC angle: Vision One provides unified investigation interface across security layers.*
- [ ] **EDR Evasion — Unhooking ntdll.dll:** Attackers restore original ntdll.dll code to bypass user-mode EDR hooks in API functions. *SOC angle: unhooking defeats inline hooking; kernel callbacks still detect; detection requires monitoring unhooking attempts.*
- [ ] **EDR Evasion — Direct Syscalls:** Bypass user-mode hooks by invoking syscalls directly via assembly (SysWhispers, inline syscalls). *SOC angle: direct syscalls evade user-mode hooks but not kernel callbacks; rare for legitimate software.*
- [ ] **EDR Evasion — In-Memory Execution:** Load and execute malware entirely in memory without touching disk to avoid file-based detection. *SOC angle: fileless malware harder to detect; requires memory scanning and behavioral analysis.*
- [ ] **EDR Evasion — Process Injection:** Inject malicious code into legitimate processes to hide execution and blend with normal activity. *SOC angle: process injection techniques (CreateRemoteThread, APC injection, process hollowing) detectable via telemetry anomalies.*
- [ ] **EDR Evasion — Living-Off-the-Land Binaries (LOLBins):** Use legitimate Windows binaries (certutil, bitsadmin, mshta, regsvr32) for malicious purposes to appear benign. *SOC angle: LOLBins abuse requires behavioral detection; process command-line telemetry critical.*
- [ ] **XDR Concept — Cross-Domain Correlation:** XDR correlates telemetry across endpoint, network, email, cloud, and identity to detect multi-stage attacks. *SOC angle: XDR provides unified view; single-domain visibility misses attack chain spanning multiple layers.*
- [ ] **XDR Platforms — Microsoft 365 Defender:** Combines MDE (endpoint), MDO (email), MDI (identity), MDA (cloud apps) for integrated XDR. *SOC angle: M365 Defender provides automated cross-product correlation and unified incident view.*
- [ ] **XDR Platforms — Palo Alto Cortex XDR:** Integrates endpoint, network (firewall), and cloud data for behavioral threat detection. *SOC angle: Cortex XDR stitches together attack chains across network and endpoint telemetry.*
- [ ] **XDR Platforms — Trend Micro Vision One:** Correlates endpoint, email, server, and cloud workload data for unified detection and response. *SOC angle: Vision One provides single pane for multi-layer investigations.*
- [ ] **XDR Benefits — Unified View:** Single console for all security layers reduces context switching and accelerates investigations. *SOC angle: unified view reveals full attack scope; siloed tools miss cross-layer attacks.*
- [ ] **XDR Benefits — Cross-Domain Correlation:** Automatic correlation links related events (email phish → endpoint execution → cloud data access). *SOC angle: correlation reveals kill chain; isolated events hide attack progression.*
- [ ] **XDR Benefits — Automated Response:** Orchestrated response actions across products (isolate endpoint, block sender, revoke cloud session). *SOC angle: automated response reduces MTTR; misconfigured automation can cause outages.*

---

### Topic 5: Detection Engineering — 🔬 Practical

> [!TIP]
> **Goal:** Write high-quality detection rules as code

> [!NOTE]
> ⏱️ **Time Bracket: 3-4 days** — Detection-as-Code methodology (version control, testing, CI/CD for detections), Sigma rules (universal detection language in YAML — write once, convert to Splunk/Elastic/Sentinel), YARA rules for malware/file-based detection, KQL detection queries for Sentinel/MDE, SPL detection queries for Splunk, detection validation & testing (generate attack traffic, verify alert fires, measure false positives), MITRE ATT&CK mapping (tag detections with technique IDs), purple team validation (red team executes technique, blue team confirms detection fires). Deliverable: write 10 Sigma rules for common ATT&CK techniques, convert to target SIEM, test & validate.

- [ ] **Detection-as-Code Version Control:** Store detection rules in Git repositories with commit history, branches, and tags for change tracking. *SOC angle: version control enables rollback of broken rules; lack of versioning = lost detection coverage when rules break.*
- [ ] **Detection-as-Code Peer Review:** Require code reviews for detection rules to catch logic errors, false positive risks, and performance issues. *SOC angle: peer review improves rule quality; unreviewed rules = production blind spots from bugs.*
- [ ] **Detection-as-Code Testing in Dev/Staging:** Test new detections in non-production environment before deploying to avoid alert storms. *SOC angle: testing prevents alert fatigue from untested rules; deploy-to-prod = operational chaos.*
- [ ] **Detection-as-Code CI/CD Pipeline:** Automate detection rule deployment using CI/CD pipelines with validation, testing, and rollback capabilities. *SOC angle: CI/CD ensures consistent deployment; manual deployment = configuration drift and missed updates.*
- [ ] **Detection-as-Code Documentation & Metadata:** Document detection logic, MITRE ATT&CK technique mappings, false positive guidance, and tuning recommendations. *SOC angle: documentation enables analysts to understand alerts; undocumented rules = wasted investigation time.*
- [ ] **Sigma Rule Syntax:** Write detection rules in YAML format with title, id, status, description, references, author, logsource, detection logic, falsepositives, and severity level. *SOC angle: Sigma's universal format enables platform portability; write once, deploy everywhere.*
- [ ] **Sigma Detection Logic Sections:** Define selection blocks (field conditions), keyword lists (string patterns), and conditions (all/any/1 of them logic). *SOC angle: flexible logic enables complex multi-field detections; mismatched conditions = false negatives.*
- [ ] **Sigma Rule Converters:** Convert Sigma rules to platform-specific queries (Splunk SPL, Elastic DSL, Sentinel KQL) using sigmac or uncoder.io. *SOC angle: conversion enables SIEM-agnostic rule development; conversion errors = silent detection gaps.*
- [ ] **Sigma Rule Repositories:** Use SigmaHQ GitHub and SOC Prime Threat Detection Marketplace for community-contributed and commercial detection content. *SOC angle: public rule repos provide baseline coverage; custom rules still needed for environment-specific threats.*
- [ ] **Sigma Rule — Mimikatz Execution:** Detect Mimikatz execution via command-line arguments, process name, or LSASS access patterns. *SOC angle: Mimikatz = credential dumping; detection critical for preventing lateral movement.*
- [ ] **Sigma Rule — PsExec Lateral Movement:** Detect PsExec by service creation with PSEXE* pattern, admin share access, and process execution via services. *SOC angle: PsExec = common lateral movement tool; detection reveals attacker spread.*
- [ ] **Sigma Rule — Credential Dumping (LSASS Access):** Detect suspicious process access to lsass.exe memory (PROCESS_VM_READ permission). *SOC angle: LSASS dumping = credential theft; early detection prevents privilege escalation.*
- [ ] **Sigma Rule — PowerShell Empire/Cobalt Strike Indicators:** Detect known command patterns, staging URLs, named pipes, and C2 beacon artifacts. *SOC angle: framework detection catches widespread tools; custom C2 requires behavioral rules.*
- [ ] **Sigma Rule — Suspicious Scheduled Task Creation:** Detect scheduled tasks with unusual names, high-privilege execution, or suspicious executable paths. *SOC angle: scheduled tasks = persistence; detection prevents long-term access.*
- [ ] **Sigma Rule — Kerberoasting:** Detect Event ID 4769 TGS requests with RC4 encryption for service accounts (Kerberoasting attack). *SOC angle: Kerberoasting = service account password cracking; RC4 usage is primary indicator.*
- [ ] **Sigma Rule — DCSync:** Detect Event ID 4662 with replication rights (DS-Replication-Get-Changes) indicating DCSync credential theft. *SOC angle: DCSync = domain-wide credential compromise; detection prevents mass credential theft.*
- [ ] **Sigma Rule — Pass-the-Hash:** Detect Event ID 4624 logon type 3 (network) with NTLM authentication from unexpected source. *SOC angle: Pass-the-Hash = credential reuse without password; detection reveals stolen hash usage.*
- [ ] **YARA Rule Syntax:** Write rules with strings section (text, hex, regex patterns) and condition section (logic combining strings). *SOC angle: YARA scans files and memory for malware signatures; matches reveal malware presence.*
- [ ] **YARA String Types:** Define text strings (ASCII/Unicode), hex byte patterns, and regex expressions for flexible pattern matching. *SOC angle: multiple string types enable diverse matching; regex provides pattern flexibility.*
- [ ] **YARA Conditions:** Combine string matches with boolean logic (all/any of them), filesize checks, and mathematical operations. *SOC angle: complex conditions reduce false positives; overly specific = miss variants.*
- [ ] **YARA for Malware Family Detection:** Write rules matching unique strings, opcodes, or structures identifying malware families (Emotet, TrickBot, etc.). *SOC angle: family detection enables attribution and response; generic rules miss family-specific TTPs.*
- [ ] **YARA for Webshell Detection:** Detect webshells via common function names (eval, exec, system), file operations, and encoding patterns. *SOC angle: webshell detection prevents persistent web access; automated scanning of web directories critical.*
- [ ] **YARA Rule Repositories:** Use Yara-Rules GitHub and awesome-yara collections for community-contributed malware detection rules. *SOC angle: public YARA rules provide baseline malware coverage; custom rules needed for targeted threats.*
- [ ] **KQL Detection Queries for ATT&CK Techniques:** Write Sentinel/MDE KQL queries targeting specific MITRE ATT&CK techniques with technique ID comments. *SOC angle: ATT&CK mapping ensures technique coverage; gaps in coverage = missed adversary behaviors.*
- [ ] **KQL Let Statements for Reusable Logic:** Define variables with let keyword to reuse logic across query sections for maintainability. *SOC angle: reusable logic simplifies complex queries; hard-coded values = maintenance burden.*
- [ ] **KQL Dynamic Thresholds:** Use percentile and stddev functions to create adaptive thresholds based on statistical baselines. *SOC angle: dynamic thresholds adapt to environment; static thresholds = false positives or false negatives.*
- [ ] **KQL Watchlists for Whitelisting:** Create watchlists of known-good entities (IPs, users, processes) to reduce false positives via exclusions. *SOC angle: watchlists reduce noise; stale watchlists include compromised or decommissioned assets.*
- [ ] **KQL Entity Behavior Analytics Integration:** Integrate user/entity behavior baselines into KQL queries for anomaly detection (unusual access patterns, atypical behavior). *SOC angle: behavior analytics detects compromised accounts; static rules miss subtle behavioral changes.*
- [ ] **SPL Correlation Searches:** Write SPL correlation searches that link multiple events over time windows (e.g., failed login → successful login → privilege escalation). *SOC angle: correlation reveals attack chains; single-event detections miss multi-stage attacks.*
- [ ] **SPL Notable Event Generation:** Create notable events in Splunk Enterprise Security when correlation searches match, triggering analyst investigation. *SOC angle: notables provide structured investigation workflow; missed notables = ignored threats.*
- [ ] **SPL Risk-Based Alerting:** Implement risk scoring framework where individual risky events accumulate scores; alert when threshold exceeded. *SOC angle: risk scoring reduces false positives by requiring multiple suspicious actions; single event may be benign.*
- [ ] **SPL Asset/Identity Correlation:** Enrich alerts with asset criticality and user roles to prioritize high-value targets. *SOC angle: asset context enables prioritization; all alerts equal priority = missed critical compromises.*
- [ ] **Detection Validation — Red Team Attack Simulation:** Execute real attacks (Mimikatz, lateral movement tools) in test environment to generate attacker telemetry. *SOC angle: validation confirms detection works; untested rules may silently fail in production.*
- [ ] **Detection Validation — Verify Alert Fires:** Confirm SIEM generates expected alert from simulated attack with correct severity and fields. *SOC angle: alert verification prevents silent detection failures; broken rules = invisible threats.*
- [ ] **Detection Validation — Measure False Positive Rate:** Track percentage of alerts that are false positives to identify noisy detections requiring tuning. *SOC angle: high FPR causes alert fatigue; tuning critical for SOC effectiveness.*
- [ ] **Detection Validation — Tune Detection Logic:** Adjust detection conditions, thresholds, or whitelists based on validation results. *SOC angle: iterative tuning balances coverage and noise; one-and-done deployment = long-term failure.*
- [ ] **Detection Validation — Document Validation Results:** Record test methodology, results, false positive sources, and tuning changes for audit trail. *SOC angle: documentation ensures repeatability and knowledge transfer; undocumented = lost tribal knowledge.*
- [ ] **MITRE ATT&CK Mapping — Tag Technique IDs:** Tag each detection rule with specific ATT&CK technique ID (T1003.001, T1078, etc.) for coverage tracking. *SOC angle: ATT&CK mapping reveals detection gaps; unmapped rules = unknown coverage.*
- [ ] **MITRE ATT&CK Navigator Coverage:** Visualize detection coverage using ATT&CK Navigator heatmaps showing which techniques are covered. *SOC angle: Navigator reveals blind spots; visual coverage assessment enables targeted detection development.*
- [ ] **MITRE ATT&CK Prioritization:** Prioritize detection development for high-impact techniques like credential access, lateral movement, and persistence. *SOC angle: not all techniques equal; prioritize those most used by adversaries and most damaging.*
- [ ] **Purple Team Exercise — Coordinate Red Team TTPs:** Schedule red team to execute specific TTPs (Kerberoasting, DCSync, lateral movement) at planned time. *SOC angle: purple team validates detection; uncoordinated red team = missed learning opportunities.*
- [ ] **Purple Team Exercise — Blue Team Detection Validation:** Blue team monitors for alerts during red team activity and confirms detection fires. *SOC angle: validation during live attack reveals detection delays, gaps, and false negatives.*
- [ ] **Purple Team Exercise — Document Gaps:** Record which TTPs were detected, which were missed, and root cause of detection failures. *SOC angle: gap analysis drives detection improvements; undocumented gaps repeat in real attacks.*
- [ ] **Purple Team Exercise — Iterative Improvement:** Create new detections for missed TTPs and retest in next purple team cycle. *SOC angle: iterative improvement closes gaps; one-time testing leaves persistent blind spots.*

---

### Topic 6: Threat Hunting — 🔬 Practical

> [!TIP]
> **Goal:** Proactively search for threats that evade automated detections

> [!NOTE]
> ⏱️ **Time Bracket: 3-4 days** — Threat hunting philosophy (hypothesis-driven vs intelligence-driven vs situational awareness hunting), hypothesis generation from threat intelligence, hunting queries (KQL, SPL, Elastic DSL) for specific TTPs, behavioral analytics & UEBA (User and Entity Behavior Analytics), anomaly detection (statistical analysis, outlier identification), hunting for persistence mechanisms (registry Run keys, scheduled tasks, services, WMI subscriptions), hunting for lateral movement (unusual RDP/SMB, credential reuse patterns, admin share access), hunting for command & control (unusual DNS queries, long-duration connections, beaconing), hunt documentation (hypothesis → data sources → queries → findings → next steps), hunt metrics (hypothesis tested, threats found, time to hunt). Deliverable: conduct 3 threat hunts (persistence, lateral movement, C2), document findings, present results.

- [ ] **Proactive vs Reactive Hunting:** Don't wait for alerts; proactively search for threats that evade automated detections. *SOC angle: reactive SOCs miss novel TTPs; proactive hunting finds what alerts miss.*
- [ ] **Hypothesis-Driven Hunting:** Start with theory "adversary likely uses X technique" based on threat landscape, then hunt for evidence. *SOC angle: hypothesis focuses investigation; random hunting wastes time.*
- [ ] **Intelligence-Driven Hunting:** Use threat intel reports (APT campaigns, CVE exploits) to trigger hunts for specific IOCs or TTPs. *SOC angle: intel-driven hunting leverages external knowledge; hunt for what others have seen.*
- [ ] **Situational Awareness Hunting:** Hunt for baseline deviations and statistical anomalies without specific hypothesis. *SOC angle: awareness hunting finds unknown threats; complements hypothesis-driven approach.*
- [ ] **Hypothesis from Threat Intelligence:** Generate hunt hypotheses from APT reports, CVE exploit announcements, and threat actor profiles. *SOC angle: threat intel provides real-world attack patterns; hunt for techniques actively used by adversaries.*
- [ ] **Hypothesis from Red Team Exercises:** After red team engagement, hunt for TTPs that red team used but weren't detected. *SOC angle: red team reveals detection gaps; hunt for what you missed.*
- [ ] **Hypothesis from MITRE ATT&CK:** Pick specific ATT&CK technique (T1003.001, T1055, T1078) and hunt for indicators. *SOC angle: ATT&CK provides structured technique catalog; systematic hunting ensures coverage.*
- [ ] **Hypothesis from Incident Retrospectives:** After incidents, hunt for similar activity that may have been missed in past. *SOC angle: post-incident hunting finds related compromises; one incident often indicates others.*
- [ ] **Hunt for Registry Run Keys:** Search for unusual entries in HKCU/HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run for persistence. *SOC angle: Run keys = common persistence; unusual entries indicate malware or backdoors.*
- [ ] **Hunt for Suspicious Scheduled Tasks:** Identify scheduled tasks with unusual names, high-privilege execution, or suspicious executable paths. *SOC angle: scheduled tasks = reliable persistence; hidden tasks often missed by casual inspection.*
- [ ] **Hunt for New Services:** Detect new Windows services, especially with DLL hijacking indicators or suspicious service binaries. *SOC angle: service creation = admin-level persistence; attacker services often mimic legitimate names.*
- [ ] **Hunt for WMI Event Subscriptions:** Find permanent WMI event consumers used for fileless persistence and execution. *SOC angle: WMI persistence = advanced technique; often overlooked by basic detection.*
- [ ] **Hunt for Startup Folder Files:** Scan user and system startup folders for suspicious executables or scripts. *SOC angle: startup folder = low-sophistication persistence; quick win for detection.*
- [ ] **Hunt for DLL Hijacking Indicators:** Search for DLLs placed in application directories to hijack loading order. *SOC angle: DLL hijacking = stealthy persistence; legitimate-looking DLL paths hide malicious code.*
- [ ] **Hunt for RDP Connections:** Analyze Event ID 4624 logon type 10 (RDP) for unusual source IPs or time patterns indicating lateral movement. *SOC angle: RDP = common lateral movement method; geographic/temporal anomalies reveal attackers.*
- [ ] **Hunt for SMB Admin Share Access:** Search Event ID 5140 for connections to admin shares (\\\\C$, \\\\ADMIN$) from workstation-to-workstation. *SOC angle: admin share access = lateral movement; workstation-to-workstation SMB unusual in normal operations.*
- [ ] **Hunt for PSExec Usage:** Detect service creation with PSEXE* pattern and associated process execution via services. *SOC angle: PsExec = attacker favorite for lateral movement; service pattern distinctive.*
- [ ] **Hunt for Pass-the-Hash:** Find logon type 3 (network) with NTLM authentication from unexpected source without password change. *SOC angle: Pass-the-Hash = credential reuse; NTLM logons from unusual sources indicate stolen hash.*
- [ ] **Hunt for Pass-the-Ticket:** Identify Kerberos logons from unusual machines or impossible travel scenarios. *SOC angle: Pass-the-Ticket = Kerberos credential theft; ticket reuse from wrong machine indicates attack.*
- [ ] **Hunt for WMI/WinRM Lateral Movement:** Search for remote WMI/WinRM connections and associated command execution. *SOC angle: WMI/WinRM = stealthy lateral movement; often missed compared to RDP/PsExec.*
- [ ] **Hunt for Unusual Admin Logons:** Detect admin account logons from unusual geographic locations or time-of-day patterns. *SOC angle: geographic/temporal anomalies reveal compromised admin accounts; legitimate admins follow patterns.*
- [ ] **Hunt for Unusual DNS Queries:** Find DNS queries to unusual domains, DNS tunneling patterns, or DGA (Domain Generation Algorithm) domains. *SOC angle: DNS queries reveal C2 domains; DGA patterns indicate malware beaconing.*
- [ ] **Hunt for Long-Duration Connections:** Identify persistent TCP connections or regular beaconing patterns indicating C2 communication. *SOC angle: C2 beacons maintain connection; long-duration or regular intervals distinctive.*
- [ ] **Hunt for Unusual Ports/Protocols:** Search for non-standard HTTP ports, raw TCP connections, or unusual protocol usage. *SOC angle: C2 often uses non-standard ports; legitimate traffic follows standard port conventions.*
- [ ] **Hunt for TLS Certificate Anomalies:** Detect self-signed certificates, mismatched SNI, or unusual certificate authorities. *SOC angle: C2 TLS certificates differ from legitimate; self-signed certs or CA mismatches indicate malicious traffic.*
- [ ] **Hunt for Unusual User-Agent Strings:** Identify rare or suspicious user-agent strings in HTTP traffic indicating non-browser tools. *SOC angle: C2 user-agents often generic or rare; legitimate browsers have common user-agents.*
- [ ] **Hunt for Beaconing Frequency:** Analyze connection frequency for regular intervals (every 60s, every 5m) indicating automated beaconing. *SOC angle: regular beaconing intervals = C2 heartbeat; legitimate traffic more random.*
- [ ] **Baseline User Login Behavior:** Establish normal login times, geographic locations, and accessed resources per user. *SOC angle: behavior baselines enable deviation detection; compromised accounts deviate from normal patterns.*
- [ ] **Detect Login Deviations:** Alert on logins at 3 AM, from new countries, or accessing unusual applications. *SOC angle: deviations indicate compromised accounts; legitimate users follow routines.*
- [ ] **Account Compromise Indicators:** Find simultaneous logins from different locations (impossible travel) indicating credential theft. *SOC angle: impossible travel = definitive compromise indicator; one account, two locations, short timeframe.*
- [ ] **Privilege Escalation Detection:** Identify users suddenly accessing sensitive resources they never accessed before. *SOC angle: sudden privilege elevation indicates escalation; normal users don't randomly access Domain Admin shares.*
- [ ] **Data Hoarding Detection:** Detect mass file downloads or unusual data access volumes indicating data theft preparation. *SOC angle: data hoarding precedes exfiltration; large volume file access from single user = red flag.*
- [ ] **Statistical Baseline Analysis:** Calculate mean, standard deviation, and percentiles for normal activity metrics. *SOC angle: statistical baselines provide quantitative thresholds; arbitrary thresholds cause false positives or negatives.*
- [ ] **Outlier Identification Methods:** Use Z-score or IQR (Interquartile Range) methods to identify statistical outliers. *SOC angle: outliers indicate anomalies; Z-score >3 or IQR extremes warrant investigation.*
- [ ] **Rare Event Analysis:** Identify long-tail events with very low frequency that may indicate malicious activity. *SOC angle: rare events often malicious; common events blend in, rare events stand out.*
- [ ] **Time-Series Anomaly Detection:** Detect sudden spikes, drops to zero, or pattern changes in time-series data. *SOC angle: time-series anomalies reveal attack start/stop; sudden spike in failed logins = brute force.*
- [ ] **Hunt Documentation — Hypothesis Statement:** Clearly state hunt hypothesis ("adversaries are using Kerberoasting in our environment"). *SOC angle: documented hypothesis enables repeatability; future analysts understand hunt purpose.*
- [ ] **Hunt Documentation — Data Sources Used:** List all log sources queried (Windows Security, Sysmon, EDR, firewall). *SOC angle: data source documentation reveals coverage; future hunts know what was checked.*
- [ ] **Hunt Documentation — Queries Executed:** Record exact KQL, SPL, or other queries used for hunt. *SOC angle: query documentation enables reuse and automation; successful hunts become detection rules.*
- [ ] **Hunt Documentation — Findings:** Document threats found, false positives encountered, and interesting observations. *SOC angle: findings create institutional knowledge; document what worked and what didn't.*
- [ ] **Hunt Documentation — Next Steps:** Record planned actions (new detections, additional hunts, escalations). *SOC angle: next steps ensure follow-through; hunts without action waste effort.*
- [ ] **Hunt Documentation — Metrics:** Track time spent, data volume analyzed, and threats discovered for hunt effectiveness measurement. *SOC angle: metrics justify hunt program; demonstrate value to management.*
- [ ] **Hunt Metric — Hypotheses Tested:** Count number of hunt hypotheses investigated in period. *SOC angle: hypothesis count indicates hunt activity; more hypotheses = broader coverage.*
- [ ] **Hunt Metric — Threats Discovered:** Track actual threats found through hunting (not via alerts). *SOC angle: threat count demonstrates hunt effectiveness; zero threats may indicate need for better hypotheses or lack of threats.*
- [ ] **Hunt Metric — Time to Complete Hunt:** Measure duration from hypothesis to conclusion for efficiency tracking. *SOC angle: hunt duration indicates complexity and efficiency; optimize long hunts.*
- [ ] **Hunt Metric — Data Coverage:** Calculate percentage of environment covered by hunt (% endpoints, % users, % network). *SOC angle: coverage metric reveals hunt thoroughness; partial coverage leaves blind spots.*
- [ ] **Hunt Metric — Hunt Backlog:** Track number of planned hunts not yet executed to manage hunt program workload. *SOC angle: backlog metric indicates capacity constraints; growing backlog = need for more hunters or automation.*

---

### Lab Progression (Module 19A: SOC & Security Operations)

| Level | Task | Deliverable |
| ----- | ---- | ------------ |
| 1 | Deploy Splunk Free or Microsoft Sentinel free tier | Functional SIEM lab environment |
| 2 | Ingest logs from 3+ sources (Windows, Linux, network) | Log ingestion documentation |
| 3 | Write 10 detection rules for MITRE ATT&CK techniques | Detection rule repository |
| 4 | Create Sigma rules and convert to target SIEM | Sigma rule collection |
| 5 | Build SOC dashboard for incident triage | Functional dashboard |
| 6 | Conduct 3 threat hunts (persistence, lateral movement, C2) | Threat hunt reports |
| 7 | Set up Microsoft Defender for Endpoint trial, write advanced hunting queries | MDE hunting query collection |
| 8 | Purple team exercise: execute attack, validate detection | Purple team report |

**Practice Platforms:**
- [Splunk Free](https://www.splunk.com/en_us/download.html) - 500MB/day free tier
- [Microsoft Sentinel](https://azure.microsoft.com/en-us/products/microsoft-sentinel) - Free tier with Azure account
- [Elastic Security](https://www.elastic.co/security) - Free Basic license
- [Boss of the SOC (BOTS)](https://cyberdefenders.org/blueteam-ctf-challenges/) - Blue team CTF challenges
- [Cyber Defenders](https://cyberdefenders.org/) - Blue team labs

> [!IMPORTANT]
> **Move-On Gate:** I can deploy and configure a SIEM. I can write detection rules in Sigma, KQL, and SPL. I can conduct threat hunts for common ATT&CK techniques. I can investigate alerts and produce incident reports. I understand what blue team sees when I attack — making me a better red teamer.

---

## Module 19: Active Directory & Entra ID

> [!NOTE]
> **📚 Recommended Books for This Part**
> - 🔴 `EA - Windows Security Internals with PowerShell` — Primary companion — AD internals, attack paths (Kerberoasting, DCSync, Golden Ticket), PowerShell enumeration
> - 🟡 `Windows PowerShell Cookbook` — Reference — PowerShell command reference for AD enumeration and post-exploitation
> - 🟡 `Windows Server automation with PowerShell cookbook` — Reference — Group Policy, SYSVOL, service configs
> - 🟢 `Cybersecurity Attack-and-Defense Strategies 2nd` — Enterprise attack chain coverage — red vs blue perspective on AD attacks

> [!IMPORTANT]
> **Prerequisite Patch Required Before Module 19:** Before starting AD attacks, complete Stage 1 **Module 03 Topics 5 & 6** (Active Directory Concepts, Windows Identity & Kerberos Foundations). Do not skip these — Kerberoasting and delegation attacks are incomprehensible without understanding the Kerberos ticket lifecycle first. This is a targeted patch, not a full Stage 1 restart.

> [!NOTE]
> **Module 19 Internal Learning Sequence** — on-prem AD first, then Entra ID:
> ```text
> AD architecture: forest / domain / trust relationships
>         ↓
> Objects: users / groups / computers / OUs / service accounts
>         ↓
> LDAP queries & domain enumeration (BloodHound, ldapsearch)
>         ↓
> Kerberos protocol mechanics (TGT, TGS, KRB_AS_REQ/REP, KRB_TGS_REQ/REP)
>         ↓
> SPNs & service accounts (Kerberoasting attack surface)
>         ↓
> Group Policy Objects (GPO) — abuse vectors
>         ↓
> ACLs & delegation — GenericAll, WriteDACL, ForceChangePassword, etc.
>         ↓
> Credential attacks — Pass-the-Hash, Pass-the-Ticket, Overpass-the-Hash
>         ↓
> Kerberoasting & AS-REP Roasting
>         ↓
> Constrained & unconstrained delegation attacks
>         ↓
> AD Certificate Services (AD CS) — ESC1–ESC8 attack paths
>         ↓
> Lateral movement in AD environments
>         ↓
> Persistence mechanisms in AD
>         ↓
> ── THEN: Entra ID ──
>         ↓
> Entra ID (Azure AD) architecture & hybrid identity
>         ↓
> Federation, conditional access, service principals, managed identities
> ```
> **Do not attempt Entra ID / cloud identity before I understand on-prem Kerberos.** Hybrid identity attacks only make sense in context of the on-prem model.

> [!TIP]
> ⏱️ **Module 19 Total Time Budget: 2–3 weeks** — hardest module in Stage 4; core OSCP territory
> T1 (discovery/enum): 2–3 days | T2 (credential/auth attacks): 3–4 days | T3 (delegation/ACL/ADCS): 3–4 days | T4 (lateral movement/persistence): 2–3 days | T5 (Entra ID/hybrid): 2 days.
> Active Directory is the single most tested skill in offensive security interviews. If you can demonstrate BloodHound path execution, Kerberoasting, and DCSync on a real lab, you stand out. Compress nothing here.

### Topic 1: Discovery & Enumeration — 🔬 Practical

> [!TIP]
> **Goal:** Map identity surfaces across on-prem AD and Entra ID (Azure AD).

> [!NOTE]
> ⏱️ **Time Bracket: 2–3 days** — Domain recon (SharpHound/BloodHound-ce: run all collection methods, ingest data, identify shortest path to Domain Admin — this is the deliverable; ldapsearch and PowerView Get-DomainUser/Get-DomainGroup/Get-DomainController for manual enumeration), identity inventory (map all users, computers, service accounts, SPNs, and LAPS posture using Get-ADUser, Get-ADComputer, setspn -Q), policy and exposure audit (GPO enumeration: Get-GPO -All; unconstrained delegation: Get-ADComputer -Filter {TrustedForDelegation -eq $True}; LAPS check: Get-ADComputer -Properties ms-Mcs-AdmPwd), Entra ID recon (az ad user list, az ad sp list, ROADrecon for tenant app and conditional access enumeration). Deliverable: produce a BloodHound attack path graph from a lab domain showing the shortest path from a regular user to Domain Admin.


- [ ] **Domain Recon:** Enumerate **domains/forests, trusts, sites, subnets, FSMO roles**; collect **OU/Group/ACL** data.

- [ ] **Identity Inventory:** List **users, computers, service accounts, Tier0 assets, SPNs**, and **LAPS** posture.

- [ ] **Policy & Exposure:** Audit **GPOs, login scripts, startup tasks**, and **Unconstrained/Constrained/RBCD** exposure.

- [ ] **Entra ID/Cloud Recon:** Enumerate **tenants, apps, service principals, consented permissions, conditional access** and **enterprise apps**.

---

### Topic 2: Credential & Auth Attacks — 🔬 Practical

> [!TIP]
> **Goal:** Steal or replay credentials to gain higher privilege.

> [!NOTE]
> ⏱️ **Time Bracket: 3–4 days** — Kerberoasting (GetUserSPNs.py or Rubeus kerberoast — request TGS for every SPN account; crack with hashcat mode 13100; prioritize high-privilege SPNs like SQLService, MSSQLSvc), AS-REP roasting (GetNPUsers.py against users without pre-auth required; crack with hashcat mode 18200), NTLM relay (Responder captures NTLMv2 hashes from unsolicited NBNS/LLMNR traffic; ntlmrelayx relays to SMB, LDAP, ADCS HTTP enrollment — which of these succeeds depends on SMB signing configuration), token abuse (Mimikatz sekurlsa::logonpasswords, sekurlsa::tickets, lsadump::dcsync; understand why LSASS dump triggers EDR and what alternatives exist), password spray (use safe lockout windows: spray one password per 30 min against all users; target legacy auth endpoints — OWA, SMTP, POP3 — that bypass MFA). Deliverable: Kerberoast at least one SPA and crack the hash; perform NTLM relay via Responder plus ntlmrelayx in a lab environment.


- [ ] **Kerberoast / AS-REP Roast:** Extract **TGS/AS-REP** tickets for offline cracking; prioritize **high-priv SPNs**.

- [ ] **NTLM Relay/SMB/HTTP:** Abuse **NTLM relays** against **SMB/LDAP/HTTP/ADCS HTTP endpoints**; combine with **mTLS gaps**.

- [ ] **Token Abuse:** Steal **TGT/TGS, DPAPI, LSASS, browser tokens**, and **OAuth refresh tokens** across hybrid joins.

- [ ] **Password Hygiene:** Spray with **safe lockout windows**, target **legacy auth (POP/IMAP/SMTP)**, and downgrade to **basic auth** where possible.

---

### Topic 3: Delegation, ACL, and ADCS Abuse — 🔬 Practical

> [!TIP]
> **Goal:** Abuse trust relationships and misconfigurations for escalation.

> [!NOTE]
> ⏱️ **Time Bracket: 3–4 days** — Delegation abuse (Unconstrained: coerce DC authentication via SpoolSample/PetitPotam while monitoring with Rubeus monitor, harvest TGT from memory; Constrained: S4U2self to impersonate any user if SeTcbPrivilege or protocol transition allowed; RBCD: create machine account, set msDS-AllowedToActOnBehalfOfOtherIdentity via GenericWrite, S4U2proxy), ACL/ACE abuse (BloodHound identifies WriteOwner, WriteDACL, GenericAll, GenericWrite, ForceChangePassword paths — execute each step-by-step following BloodHound path, not guessing; shadow credentials via certipy shadow auto against computer accounts with GenericWrite), ADCS abuse (certipy find -vulnerable to enumerate; ESC1 to request admin certificate with attacker-controlled SAN; ESC8 to relay via PetitPotam to HTTP enrollment endpoint; certipy auth to convert PFX to TGT via PKINIT, then UnPAC-the-hash). Deliverable: exploit one ESC1 or ESC8 attack path on a GOAD or custom lab to obtain Domain Admin certificate.


- [ ] **Delegation Abuse:** Exploit **Unconstrained Delegation** (harvesting TGTs from spooler abuse), **Constrained Delegation** (service/alt service S4U2self & S4U2proxy), and **Resource-Based Constrained Delegation (RBCD)** (configuring `msDS-AllowedToActOnBehalfOfOtherIdentity` via machine account creation).

- [ ] **ACL/ACE Abuse:** Graph abuse paths with BloodHound and execute write primitives: **WriteOwner, WriteDACL, GenericAll, GenericWrite, ExtendedRight (ForceChangePassword), AddMember** on critical principals (Domain Admins, Enterprise Admins, Domain Controllers, Tier0 groups).

- [ ] **Shadow Credentials (`msDS-KeyCredentialLink`):** Exploit `GenericWrite`/`WriteProperty` over computer or user accounts using `certipy shadow auto` or `pywhiskey` to inject raw RSA public keys and authenticate via PKINIT without knowing or changing the victim's password.

- [ ] **ADCS (Active Directory Certificate Services) Deep Dive (ESC1–ESC13 via Certipy):**
  - **Reconnaissance & Auditing:** Run `certipy find -vulnerable -stdout` to enumerate Enterprise CAs, Certificate Templates, and vulnerable enrollment permissions.
  - **ESC1 / ESC2:** Templates with Client Authentication EKU and `CT_FLAG_ENROLLEE_SUPPLIES_SUBJECT` enabled — request a certificate with an arbitrary Subject Alternative Name (SAN, e.g., Domain Admin) using `certipy req -ca <CA-Name> -template <Template> -upn administrator@domain.local`.
  - **ESC3:** Enrollment Agent templates (`Certificate Request Agent` EKU) — request an agent certificate to enroll on behalf of another user.
  - **ESC4:** Vulnerable template access control rights (`WriteDacl`, `WriteOwner`, `GenericAll`) — overwrite template properties to enable `ENROLLEE_SUPPLIES_SUBJECT` and Client Authentication, abuse the template, and restore original configuration.
  - **ESC6 & ESC7:** CA configured with `EDITF_ATTRIBUTESUBJECTALTNAME2` (allows SAN specification on any template) or vulnerable CA access rights (`ManageCA`, `ManageCertificates` — issue pending requests or dump CA private keys for Golden Certificates).
  - **ESC8 (NTLM Relay to ADCS Web Enrollment):** Relay coerced authentication (via PetitPotam or PrinterBug without signing) to HTTP enrollment endpoints (`/certsrv/`) to mint machine/user certificates.
  - **ESC9, ESC10, ESC11, ESC13:** Strong certificate binding bypasses, missing RPC packet privacy (`RPC_C_AUTHN_LEVEL_PKT_PRIVACY`), and issuance policy OID group link privilege escalation.
  - **PKINIT Authentication & UnPAC-the-Hash:** Use `certipy auth -pfx cert.pfx -dc-ip <ip>` to authenticate via PKINIT, obtain a Kerberos TGT, and extract the account's plaintext NT hash directly from the Kerberos PAC (`UnPAC-the-hash`).

---

### Topic 4: Lateral Movement & Persistence — 🔬 Practical

> [!TIP]
> **Goal:** Move horizontally and maintain footholds.

> [!NOTE]
> ⏱️ **Time Bracket: 2–3 days** — Lateral movement (WinRM via evil-winrm with hash/ticket; SMB via impacket-smbexec or psexec; RDP with pass-the-hash where restricted admin mode is enabled; WMI via impacket-wmiexec; follow BloodHound CanPSRemote/CanRDP/ExecuteDCOM paths), GPO persistence (New-GPO + Set-GPRegistryValue to add logon script; requires GPO write permissions — BloodHound shows WriteDacl on GPO), DCSync (Mimikatz lsadump::dcsync /domain /user:krbtgt — requires Replicating Directory Changes All; impacket-secretsdump as alternative), Golden Ticket (Mimikatz kerberos::golden with krbtgt hash, domain SID, and target username — forges a TGT accepted by any DC in the domain), SID history injection for cross-forest attacks. Deliverable: perform lateral movement between two machines in a lab using Pass-the-Hash via impacket and establish persistence via a scheduled task GPO.


- [ ] **Lateral Paths:** Use **WinRM/SMB/RDP/WMI/PowerShell Remoting**, **admin shares**, and **task/svc installs** guided by **BloodHound** paths.

- [ ] **GPO Persistence:** Implant via **logon scripts, immediate scheduled tasks, startup items**; abuse **restricted groups** for re-add.

- [ ] **DCSync / DCShadow:** Abuse **Replicating Directory Changes** (`DS-Replication-Get-Changes-All`) using Mimikatz or `impacket-secretsdump` to pull **NTDS.dit** hashes or inject rogue domain objects via DCShadow.

- [ ] **Golden/Silver Tickets:** Forge **krbtgt/service hashes** for long-lived access; manage **ticket lifetime/renewal** OPSEC.

- [ ] **Cross-Forest Trust Exploitation & SID History:**
  - Enumerate domain and forest trusts using PowerView (`Get-DomainTrust`, `Get-ForestDomain`) or `netdom query trust`.
  - Exploit bidirectional / parent-child trusts: forge inter-realm referral tickets (cross-realm TGT) using the domain trust key.
  - Exploit missing SID filtering on external or forest trusts: inject privileged SIDs (e.g., Enterprise Admins `EA -519`) into `sIDHistory` to achieve full compromise across the trust boundary.
  - Abuse Foreign Security Principals (FSPs) and cross-forest delegation.

---

### Topic 5: Entra ID (Azure AD) & Hybrid Attacks — 🧠🔬 Mixed

> [!TIP]
> **Goal:** Exploit cloud identity to pivot and persist.

> [!NOTE]
> ⏱️ **Time Bracket: 2 days** — Consent and OAuth abuse (register a malicious multi-tenant app in a lab Entra tenant; grant it Mail.Read and Files.ReadAll; send a consent phishing link to a test user; examine the refresh token obtained via device code flow), Conditional Access bypass (identify policies that exclude legacy auth — use SMTP/POP3/IMAP to authenticate without MFA), passwordless/passkeys attack surface (SSPR: if backup email/phone is attacker-controlled, account is compromised regardless of strong primary auth; FIDO2 registration: if initial registration is not MFA-gated, attacker can register their own key), cross-cloud pivot (Entra app with AWS OIDC federation trust: enumerate via az ad sp list — if trust exists, use Entra token to AssumeRoleWithWebIdentity in AWS). Deliverable: set up a lab Entra tenant, create a CA policy, and demonstrate one bypass condition with evidence.


- [ ] **Consent & OAuth Abuse:** Steal or register **malicious multi-tenant apps**, abuse **illicit consent grants**, and persist via **refresh tokens**.

- [ ] **Conditional Access Bypass:** Exploit **trusted locations, device compliance gaps, legacy auth exemptions**, and **MFA registration weaknesses**.

- [ ] **Passwordless/Passkeys:** Target **FIDO2/Passkey registration flows**, backup methods, and **SSPR** to hijack accounts.

- [ ] **Cross-Cloud Pivot:** Use **Entra app roles** and **federation trusts** to pivot into **AWS/GCP** integrations; harvest **Graph/SharePoint** data for lateral move.

---

### Lab Progression (Module 19: Active Directory & Entra ID)

> [!TIP]
> **Goal:** Build and attack identity infrastructure with evidence and rollback.

- [ ] **AD Lab Build:** Deploy a domain controller, at least one workstation, DNS, domain users/groups, and basic GPOs.
- [ ] **Vulnerable AD Lab:** Use GOAD, DetectionLab, PurpleCloud, or a self-built intentionally weak domain to practice safely.
- [ ] **BloodHound Lab:** Ingest data, identify attack paths, validate one path in the lab, then write the remediation.
- [ ] **Kerberos Lab:** Perform lab-only AS-REP roasting/Kerberoasting and crack only synthetic passwords created for the exercise.
- [ ] **Entra ID Lab:** Create test users, app registrations, conditional access policies, and sign-in logs; document identity detections.
> [!IMPORTANT]
> **Move-On Gate:** Produce an AD/Entra attack-path report with screenshots, graph evidence, event IDs, and hardening steps.

---

## Module 20: Cloud Computing

> [!NOTE]
> **📚 Recommended Books for This Part**
> - 🔴 `Cloud_Hacking (1)` — Full — cloud attack methodology overview (misconfigs, SSRF to metadata, IAM abuse)
> - 🟢 `Trusted Cloud Computing` — Reference — cloud security architecture and defensive design context

> [!IMPORTANT]
> **Cloud Lab Setup Requirements — Read Before Starting**
> Cloud attack techniques CANNOT be practiced without a real cloud account. Unlike Stage 2 Linux labs (which run locally), cloud labs require live infrastructure. Before starting this part:
> **Account Setup:**
> - [ ] Create a dedicated **AWS Free Tier account** (separate from any personal/work account) at aws.amazon.com/free — Free Tier covers most EC2, S3, IAM labs for 12 months
> - [ ] Create a dedicated **Azure Free Account** (separate from any personal/work account) — $200 credit for 30 days + 12 months of free services
> - [ ] (Optional) Create a **GCP Free Account** — $300 credit for 90 days
> **Cost Controls (Mandatory — Set Before Any Lab Work):**
> - [ ] **AWS Billing Alert:** Go to CloudWatch → Alarms → Billing → create alert at $5/month threshold; also enable Cost Explorer
> - [ ] **Azure Budget Alert:** Go to Cost Management → Budgets → set $5/month alert
> - [ ] Never leave EC2 instances, RDS databases, or NAT Gateways running when not actively using them
> - [ ] Use `aws ec2 stop-instances` or the console to stop (not just terminate) instances to avoid data loss; terminate when done with the lab
> **Intentionally-Vulnerable Cloud Lab Environments:**
> | Platform | Provider | What It Teaches | Setup |
> |---|---|---|---|
> | **CloudGoat** | Rhino Security Labs | AWS IAM privilege escalation, SSRF, Lambda exploitation, S3 misconfigs | `pip install cloudgoat` then `cloudgoat config` |
> | **AzureGoat** | INE Security | Azure IAM, SSRF, storage attacks, Kubernetes in Azure | GitHub: ine-labs/AzureGoat |
> | **GCPGoat** | INE Security | GCP service account abuse, Cloud Run, storage | GitHub: ine-labs/GCPGoat |
> | **flaws.cloud** | Scott Piper (AWS) | S3 misconfiguration CTF walkthrough | flaws.cloud |
> | **flaws2.cloud** | Scott Piper (AWS) | IAM escalation CTF (attacker + defender paths) | flaws2.cloud |
> > [!WARNING]
> > **Never practice cloud attack techniques against accounts I do not own and have not specifically provisioned for testing.** Cloud APIs leave detailed audit trails in CloudTrail/Activity Log. Unauthorized access to cloud accounts is a federal crime under CFAA and equivalent laws. Always use dedicated lab accounts with explicit resource tagging.

> [!TIP]
> ⏱️ **Module 20 Total Time Budget: 2–3 weeks**
> T1 (architecture/governance): 1 day | T2 (storage/data security): 1–2 days | T3 (modern infra/deployment): 1 day | T4 (compute security): 1–2 days | T5 (IAM exploitation): 3–4 days | T6 (SSRF/metadata): 2 days | T7 (Lambda/serverless): 2 days | T8 (network attacks): 1–2 days | T9 (credential harvesting): 2 days | T10 (defense/hardening): 1–2 days | Labs (CloudGoat + flaws.cloud): 3–5 days.
> Cloud is now THE primary attack surface. Every organization uses cloud infrastructure. A pentester who cannot enumerate S3 buckets, exploit SSRF to metadata services, or escalate IAM privileges is missing half the modern engagement scope. Master CloudGoat scenarios before calling this module complete.

---

### Topic 1: Architecture & Governance — 🧠 Conceptual

> [!TIP]
> **Goal:** Define the battlefield and the rules of engagement — understand the cloud responsibility model, IAM structure, and baseline security posture tools before touching any attack techniques.

> [!NOTE]
> ⏱️ **Time Bracket: 1 day** — Cloud model selection (IaaS: EC2/VMs — you own OS up; PaaS: Lambda/App Service — provider owns OS; SaaS: O365 — provider owns everything; the shared responsibility boundary defines what you test), IAM architecture review (AWS: root account → Organizations → accounts → users/roles/policies; Azure: Entra tenant → subscriptions → resource groups → resources; GCP: org → folders → projects → service accounts — know which identity types are exploitable at each level), security posture baseline (run ScoutSuite: scout aws ––report-dir ./report; Prowler: prowler aws; read the full output before starting any attack work), resource tagging (tags like Owner/Environment/CostCenter identify unauthorized resources — resources without standard tags are shadow IT worth targeting). Deliverable: run ScoutSuite or Prowler against a free-tier lab AWS account and document the top 5 findings by severity.


- [ ] **Model Selection:** Select the correct `Cloud Models` (`Public`, `Private`, `Hybrid`) based on data sensitivity.

- [ ] **Responsibility Mapping:** Apply the **Shared Responsibility Model** based on the service type (`IaaS`, `PaaS`, `SaaS`) to identify what I must secure vs. the provider.

- [ ] **Environment Setup:** Initialize the tenant in a `Common Cloud Environment` (`AWS`, `GCP`, or `Azure`) with a secure root account setup.

- [ ] **IAM Architecture Review:** Understand the **IAM hierarchy** for my target cloud — AWS (root → organizations → accounts → users/roles/policies), Azure (Entra tenant → subscriptions → resource groups → resources), GCP (org → folders → projects → service accounts). Know which identity types are exploitable at each level.

- [ ] **Security Posture Baseline:** Run **ScoutSuite** (`scout aws --report-dir ./report`) or **Prowler** (`prowler aws`) to generate a baseline cloud security posture assessment across IAM, S3, networking, logging, and encryption. Read the full output — these tools reveal the attack surface before I start.

- [ ] **Resource Tagging & Environment Hygiene:** Understand how **resource tagging** (Owner, Environment, CostCenter) enables defenders to identify unauthorized resources. From an attacker's perspective: resources without standard tags are likely shadow IT or misconfigurations worth targeting.

---

### Topic 2: Storage & Data Security — 🔬 Practical

> [!TIP]
> **Goal:** Enumerate, audit, and exploit cloud storage misconfigurations — the most common source of cloud data breaches.

> [!NOTE]
> ⏱️ **Time Bracket: 1–2 days** — S3 bucket enumeration (aws s3api list-buckets; for each bucket: get-bucket-acl, get-bucket-policy, get-bucket-cors, get-public-access-block — look for AllUsers ACL grants or Principal:* in bucket policy), unauthenticated discovery (cloudbrute against organization name variants — company-backup, company-logs, company-dev), ACL and policy audit (AllUsers = fully public; AuthenticatedUsers = any AWS account — both are critical findings), CORS misconfiguration (AllowedOrigin:* with AllowCredentials enables cross-origin data theft from authenticated sessions — test with crafted Origin header), secrets scanning (trufflehog s3 ––bucket=name scans all objects for hardcoded credentials, API keys, private certs). Deliverable: complete flaws.cloud levels 1-3 which are all S3-based misconfigurations.


- [ ] **Object Storage Security:** Audit `S3` buckets and `Common Cloud Storage` (Drive, Box) for public access and enforce encryption.

- [ ] **Access Control:** Implement strict IAM policies ensuring only authorized identities can access storage blobs.

- [ ] **S3 Bucket Enumeration:** Use `aws s3api list-buckets` to enumerate all buckets in-scope. For each bucket, run `aws s3api get-bucket-acl`, `get-bucket-policy`, `get-bucket-cors`, and `get-public-access-block` to map the full exposure surface. Use **cloudbrute** for unauthenticated bucket discovery against organization name variants.

- [ ] **ACL & Policy Audit:** Identify buckets with `AllUsers` (public) or `AuthenticatedUsers` (any AWS account) grants in their ACL. Identify bucket policies with `"Principal": "*"` without a restrictive condition. Both patterns create read/write exposure without authentication.

- [ ] **CORS Misconfiguration:** Retrieve CORS config with `aws s3api get-bucket-cors`. Permissive CORS (`AllowedOrigin: *` + `AllowCredentials: true` patterns) enables cross-origin data theft from authenticated browser sessions. Test with a crafted request from an attacker origin.

- [ ] **Secrets in Object Storage:** Use **trufflehog** (`trufflehog s3 --bucket=<name>`) to scan bucket contents for hardcoded credentials, API keys, database connection [[strings]], and private certificates that developers have uploaded and forgotten.

---

### Topic 3: Modern Infrastructure & Deployment — 🧠🔬 Mixed

> [!TIP]
> **Goal:** Audit and attack the compute layer and the deployment pipeline — misconfigurations here grant persistent, privileged access.

> [!NOTE]
> ⏱️ **Time Bracket: 1 day** — IaC security scanning (checkov -d ./terraform/ — identify open security groups, unencrypted S3, wildcard IAM policies; tfsec for Terraform-specific checks; cfn-nag for CloudFormation), Terraform state file exposure (terraform.tfstate contains plaintext resource metadata including IAM ARNs and sometimes credentials — check for state files in public S3 or committed to Git — use trufflehog for detection), CDK and serverless security (serverless.yml Lambda functions with * in IAM policies; API Gateway endpoints without auth; environment variables containing plaintext secrets — find these with grep or semgrep). Deliverable: run checkov against a sample insecure Terraform template and document every HIGH finding with remediation.


- [ ] **Code-Defined Security:** Use `Infrastructure as Code` (IaC) to template firewalls and permissions, preventing human configuration errors.

- [ ] **Serverless Hardening:** Secure `Serverless` functions by minimizing privileges and auditing dependencies for vulnerabilities.

- [ ] **Pipeline Security:** Audit the `general flow of deploying in the cloud` to ensure secrets (API keys) are not hardcoded in the deployment scripts.

- [ ] **IaC Security Scanning:** Run **checkov** (`checkov -d ./terraform/`) against Terraform/CloudFormation/CDK templates to identify misconfigurations before deployment — open security groups, unencrypted storage, overly permissive IAM roles. Also run **tfsec** (Terraform-specific) and **cfn-nag** (CloudFormation-specific) for complementary coverage.

- [ ] **Terraform State File Exposure:** Terraform state files (`terraform.tfstate`) contain plaintext resource metadata including IAM role ARNs, IP addresses, and sometimes credentials. Check for state files stored in public S3 buckets, unencrypted S3 with broad access, or committed to Git repositories. This is one of the highest-value targets in a cloud engagement.

- [ ] **CDK & Serverless Security Patterns:** Audit AWS CDK constructs and serverless framework configurations (`serverless.yml`) for: Lambda functions with `*` in IAM policies, environment variables containing plaintext secrets, API Gateway endpoints without authentication, and functions with `VpcConfig` that bypass security group controls.

---

### Topic 4: Automation & Scripting — 🔬 Practical

> [!TIP]
> **Goal:** Use automation to enumerate, audit, and monitor cloud environments — understand what defenders see so I know what to avoid generating.

> [!NOTE]
> ⏱️ **Time Bracket: 1 day** — AWS CLI enumeration checklist (aws iam list-users; aws iam list-roles; aws iam get-account-authorization-details dumps all policies, users, roles in one call; aws ec2 describe-instances; aws s3api list-buckets; aws lambda list-functions; for Azure: az account list; az role assignment list ––all; az vm list — run these in sequence as first step after any credential compromise), CloudTrail analysis (aws cloudtrail lookup-events ––lookup-attributes AttributeKey=EventName,AttributeValue=AssumeRole to trace lateral movement via role chaining; understand log retention gaps — events older than 90 days require S3 log archive access), Prowler multi-account mode (cross-account enumeration via sts:AssumeRole from auditor role — maps the full IAM attack surface across an AWS Organization). Deliverable: write a Boto3 script that enumerates all IAM users, their attached policies, and flags anyone with AdministratorAccess.


- [ ] **Cloud Automation:** Use **Python (Boto3), Terraform, CloudFormation** to audit security groups and IAM roles automatically.

- [ ] **Admin Scripting:** Master **Bash, PowerShell, AWS CLI, Azure CLI** to manage instances and automate operations.

- [ ] **CI/CD Security:** Integrate **security scanning** (SAST, DAST, dependency checks) into deployment pipelines.

- [ ] **CloudTrail Log Analysis:** Query **CloudTrail** (`aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=ConsoleLogin`) to identify unauthorized API calls, credential use from unusual IPs, role assumption chains, and resource creation events. Understand log retention gaps — events older than 90 days require S3 log archive access.

- [ ] **AWS CLI Enumeration Commands:** Build a systematic enumeration checklist: `aws iam list-users`, `aws iam list-roles`, `aws iam get-account-authorization-details` (dumps all policies, users, roles in one call), `aws ec2 describe-instances`, `aws s3api list-buckets`, `aws lambda list-functions`. For Azure: `az account list`, `az role assignment list --all`, `az vm list`. Run these as the first step after any credential compromise.

- [ ] **Cross-Account Audit Automation:** Use **Prowler's multi-account mode** or write Boto3 scripts using `sts:AssumeRole` to enumerate security posture across all accounts in an AWS Organization from a single auditor role. Understand how cross-account role trust policies create lateral movement paths.

> [!IMPORTANT]
> **⚠️ Stage 4 Intermediate Checkpoint (Module 20: Cloud Computing)**
> I must still complete **Topics 5 and 6** before leaving Module 20. This checkpoint verifies Stage 1–4 readiness only. I am ready to continue to Stage 5 when I can: (1) run ScoutSuite or Prowler against a lab AWS account and interpret the findings report; (2) enumerate all S3 buckets, their ACLs, bucket policies, and CORS configurations using the AWS CLI; (3) use trufflehog to scan an S3 bucket for secrets; (4) run checkov against a Terraform template and explain each HIGH finding; (5) query CloudTrail to identify at least one suspicious API event in a lab environment. If I cannot do all five without looking up the commands, revisit Stages 2–4 before proceeding. **Then continue to Stage 5 (Cloud Attack Vectors) and Stage 6 (IAM & PAM).**

---

### Topic 5: Cloud-Specific Attack Vectors — 🔬 Practical

> [!TIP]
> **Goal:** Understand unique cloud threats.

> [!NOTE]
> ⏱️ **Time Bracket: 2–3 days** — IAM exploitation and role chaining (pacu module iam__privesc_scan to identify privilege escalation paths; iam:PassRole to EC2/Lambda for escalation to higher-tier roles; iam:SetDefaultPolicyVersion to rollback to an overpermissive policy version), storage misconfigurations (already covered in T2 — extend to Azure blob container anonymous access and GCP bucket allUsers IAM binding), IMDS deep dive (IMDSv1: simple GET to 169.254.169.254/latest/meta-data/iam/security-credentials/role-name extracts temp STS keys; IMDSv2: requires PUT to get session token first, then GET with X-aws-ec2-metadata-token header — defeats blind SSRF that cannot set custom headers but not full SSRF or command injection on host), serverless attacks (Lambda environment variable extraction via SSRF to execution context, excessive Lambda execution role permissions, cold-start persistence via Lambda layers). Deliverable: complete CloudGoat iam_privesc_by_rollback or ecs_ecs_task_escape scenario and document the full attack path.


- [ ] **IAM Exploitation & Role Chaining:**
  - Abuse **AssumeRole trust chains** across AWS accounts; enumerate trust policies using `pacu` or `enumerate-iam`.
  - Exploit `iam:PassRole` attached to EC2 or Lambda to elevate privileges to higher-tier service roles.
  - Roll back IAM policies to insecure previous versions using `iam:SetDefaultPolicyVersion`.

- [ ] **Storage Misconfigurations:** Find **public S3 buckets, Azure blob containers, and GCP storage buckets** via unauthenticated enumeration, CORS manipulation, and unencrypted snapshot exports.

- [ ] **Metadata Services (IMDSv1 vs IMDSv2 Deep Dive):**
  - **IMDSv1 Vulnerability:** Query `http://169.254.169.254/latest/meta-data/iam/security-credentials/<role-name>` directly via simple GET in SSRF payloads to extract temporary STS access keys, secret keys, and session tokens.
  - **IMDSv2 Defense & Bypass Surface:** IMDSv2 enforces session-oriented requests requiring a `PUT` request with `X-aws-ec2-metadata-token-ttl-seconds: 21600` to generate a session token, then requires passing the token in `X-aws-ec2-metadata-token: <token>`. Understand how this neutralizes blind SSRF and reverse proxies without header forwarding, but remains vulnerable to full SSRF with custom header injection or command injection on host/container processes.

- [ ] **Serverless Attacks:** Exploit **Lambda/Cloud Functions environment variables, excessive execution permissions, event injection, and cold-start persistence**.

- [ ] **Container Escapes:** Break out of **Docker, Kubernetes pods** via misconfigurations. 📌 _See Module 21 Topic 1 for full container escape techniques and Module 21 Topic 2 for Kubernetes-specific attacks._

- [ ] **Multi-Tenancy & Supply Chain:** Understand **cross-tenant data leakage, shared VPC routing oversights, and CI/CD runner poisoning**.

---

### Topic 6: IAM & PAM Attack Surface — 🔬 Practical

> [!TIP]
> **Goal:** Master identity-based attack techniques in cloud and enterprise environments.

> [!NOTE]
> ⏱️ **Time Bracket: 1–2 days** — IAM policy analysis (enumerate with pacu/enumerate-iam/ScoutSuite; identify wildcard permissions: iam:* or * on * resource — these are immediate findings; privilege escalation paths: lambda:CreateFunction + iam:PassRole = instant admin; iam:CreatePolicyVersion = rollback to permissive version), role chaining and federation abuse (AssumeRole chain across accounts; OIDC federation from Entra to AWS — if an Entra service principal has STS:AssumeRoleWithWebIdentity trust, a compromised Entra account can pivot to AWS; SAML assertion manipulation if IdP signing key is leaked), PAM architecture awareness (CyberArk vault admin compromise: account that manages the vault is the master key to all vaulted credentials; session proxy hijacking for recorded sessions; JIT access abuse: request privileged access, perform actions, expect access revoked automatically — understand how attackers use this window). Deliverable: complete flaws2.cloud attacker path which demonstrates IAM privilege escalation from low-privilege to admin.


- [ ] **IAM Policy Analysis & CIEM:** Enumerate and analyze **IAM policies** using **Pacu, enumerate-iam, ScoutSuite, Prowler** to find **overprivileged roles, wildcard permissions (*)**, and privilege escalation paths across **AWS/Azure/GCP**. Implement **CIEM (Cloud Infrastructure Entitlement Management)** concepts to identify toxic combinations and unused excessive permissions.

- [ ] **Role Chaining & Federation Abuse:** Exploit **AssumeRole chains, cross-account trust relationships, OIDC federation, SAML assertion manipulation** to escalate from low-privilege to administrative access.

- [ ] **Service Account & Managed Identity Abuse:** Target **service accounts, managed identities, workload identity federation** with excessive permissions or leaked credentials. Understand **key rotation failures** and **long-lived access key risks**.

- [ ] **Conditional Access & Policy Bypass:** Test **Azure Conditional Access policies, AWS SCPs (Service Control Policies), GCP Organization Policies** for bypass conditions — **device compliance gaps, location spoofing, legacy auth exemptions, MFA registration weaknesses**.

- [ ] **Privileged Access Management (PAM):** Understand **CyberArk, Delinea (Thycotic), BeyondTrust** vault architecture — **credential vaulting, session recording, just-in-time (JIT) access, credential rotation**. Know the attack surface: **vault admin compromise, session proxy hijacking, checkout abuse, emergency break-glass exploitation**.

- [ ] **Identity Governance:** Understand **access reviews, entitlement management, separation of duties (SoD)**, and how **identity lifecycle gaps** (orphaned accounts, excessive standing privileges, stale service principals) create attack opportunities.

> [!IMPORTANT]
> **Move-On Gate (Module 20: Cloud Computing):** I am ready to proceed to Module 21 when I can: (1) execute an IAM privilege escalation path in a CloudGoat lab from low-privilege user to admin using only misconfigured policies; (2) identify a Conditional Access bypass condition in a lab Azure tenant and explain why it exists; (3) explain the difference between a SAML token, an OAuth access token, and a Kerberos TGT — and what happens when each is stolen.

---

---

## Module 21: Container & Orchestration Security

> [!TIP]
> ⏱️ **Module 21 Total Time Budget: 1 week**
> T1 (container fundamentals/attacks): 2 days | T2 (Kubernetes security): 2 days | T3 (container runtime security): 1 day | T4 (secrets/config management): 1 day | T5 (CI/CD and workflow automation attacks): 1–2 days | T6 (hypervisor security): 1 day.
> Container security is now a standard enterprise engagement scope. Know escape primitives cold: privileged mode, docker.sock mount, hostPID nsenter. Kubernetes RBAC misconfigurations are the cloud equivalent of AD ACL abuse.

### Topic 1: Container Fundamentals & Attacks — 🔬 Practical

> [!TIP]
> **Goal:** Understand containerization and its security implications.

> [!NOTE]
> ⏱️ **Time Bracket: 2 days** — Container anatomy (namespaces and cgroups: understand that a container is just a process group with namespace isolation — not a VM; capabilities: default containers drop most caps but retain NET_BIND_SERVICE, SETUID, SETGID — privileged mode enables all), image vulnerabilities (Trivy: trivy image alpine:latest; focus on CRITICAL and HIGH CVEs in base image layer), Dockerfile security audit (running as root: USER directive; secrets baked into ENV or COPY; FROM with no pinned digest — supply chain risk), container escape primitives (privileged mode: mount /dev/sda1 /mnt inside container; docker.sock mount: docker -H unix:///var/run/docker.sock run -v /:/host -it alpine chroot /host; hostPID nsenter: nsenter -t 1 -m -u -i -n -p –– /bin/bash; cgroup v1 release_agent: write command to notify_on_release). Deliverable: practice privileged container escape and docker.sock escape on a deliberately misconfigured lab container.


- [ ] **Container Anatomy:** Master **namespaces (PID, NET, MNT, IPC, UTS, USER), cgroups (v1/v2 resource limits), capabilities (POSIX capabilities), seccomp profiles, AppArmor/SELinux** as isolation mechanisms.

- [ ] **Image Vulnerabilities:** Scan images with **Trivy, Clair, Grype** for **CVEs, secrets, misconfigs** in layers.

- [ ] **Dockerfile Security:** Audit **Dockerfiles** for **running as root, exposed secrets, vulnerable base images, unnecessary packages**.

- [ ] **Container Escape Primitives & Host Takeover:**
  - **`--privileged` Mode Exploitation:** Containers run without seccomp filtering and with all capabilities enabled; mount the underlying host hard disk (`mount /dev/sda1 /mnt`) and chroot to gain instant host root.
  - **Abuse of Capabilities (`CAP_SYS_ADMIN`):** Exploit cgroup v1 `release_agent` (`notify_on_release`) to execute arbitrary host commands when the cgroup terminates.
  - **Mounted Docker Socket (`/var/run/docker.sock`):** Issue commands to the host Docker daemon from inside the container to spawn a sibling privileged container: `docker -H unix:///var/run/docker.sock run -v /:/host -it alpine chroot /host`.
  - **Namespace Hijacking (`hostPID` + `nsenter`):** If `--pid=host` is enabled, list host processes and use `nsenter -t 1 -m -u -i -n -p -- /bin/bash` to enter the host's root namespace.
  - **Shared Kernel Exploits:** Kernel vulnerabilities (e.g., Dirty COW, Dirty Pipe CVE-2022-0847, CVE-2022-0492) that compromise the host kernel directly through container syscalls.

- [ ] **Docker API Exploitation:** Abuse **exposed Docker API (2375 unauthenticated / 2376 TLS misconfigured)** to remotely spawn privileged containers and compromise host.

---

### Topic 2: Kubernetes Security — 🔬 Practical

> [!TIP]
> **Goal:** Attack and defend container orchestration platforms.

> [!NOTE]
> ⏱️ **Time Bracket: 2 days** — K8s architecture (API server authenticates via certs/tokens; etcd stores all cluster state including secrets in base64 — direct etcd access without auth = full cluster compromise; kubelet listens on 10250 with optional anonymous auth enabled in older configs), RBAC exploitation (kubectl auth can-i ––list ––as system:serviceaccount:default:default to check default SA permissions; look for ClusterRoleBinding to cluster-admin for service accounts; wildcard verbs on core API resources), pod escape (hostPath mount to /: mount host filesystem and chroot; hostNetwork: access services on host network including metadata API; privileged pod = same as container escape T1), secrets extraction (kubectl get secrets ––all-namespaces -o yaml; etcdctl get / ––prefix for etcd direct access; environment variables in pod spec), API server abuse (anonymous auth: curl https://k8s-api:6443/api/v1/pods without token; kubeconfig exposure in git repos or CI environments). Deliverable: complete KubernetesGoat challenge set: RBAC misconfiguration, exposed dashboard, and privileged pod escape.


- [ ] **K8s Architecture:** Understand **control plane (API server, etcd, scheduler)** vs **data plane (kubelet, kube-proxy)** components.

- [ ] **RBAC Exploitation:** Abuse **overprivileged service accounts, role bindings, cluster-admin** for privilege escalation.

- [ ] **Pod Escape:** Break out via **hostPath mounts, hostNetwork, hostPID, privileged pods** to access host filesystem.

- [ ] **Secrets Extraction:** Steal **Kubernetes secrets** from **etcd, mounted volumes, environment variables, service account tokens**.

- [ ] **API Server Abuse:** Exploit **unauthenticated API, certificate theft, kubeconfig exposure** for cluster control.

- [ ] **Network Policy Bypass:** Pivot through **missing network policies** to access isolated pods and services.

---

### Topic 3: Container Runtime Security — 🧠🔬 Mixed

> [!TIP]
> **Goal:** Detect and prevent malicious container activity.

> [!NOTE]
> ⏱️ **Time Bracket: 1 day** — Runtime monitoring (Falco: deploy with Helm, review default rules, understand how Falco detects shell spawning inside containers, unexpected outbound connections, and sensitive file reads — these are the detection signals that catch container escapes), admission control (OPA/Gatekeeper: Rego policy that blocks privileged pods; Kyverno: simpler YAML-based policy for non-root enforcement and required labels), image signing (Cosign: sign images with keyless mode using OIDC identity; verify: cosign verify image ––certificate-identity=email ––certificate-oidc-issuer=issuer), seccomp profiles (syscall restriction: a container with seccomp=unconfined can call any kernel syscall including mount — default profile blocks 60+ dangerous syscalls). Deliverable: install Falco in a lab K8s cluster, trigger a shell-in-container event, and confirm detection in Falco alerts.


- [ ] **Runtime Monitoring:** Deploy **Falco, Sysdig, Aqua** to detect **suspicious syscalls, process execution, network connections**.

- [ ] **Admission Control:** Use **OPA (Open Policy Agent), Kyverno** to enforce **security policies at admission time**.

- [ ] **Image Signing:** Implement **Notary, Cosign** for **image provenance verification** and supply chain security.

- [ ] **Runtime Protection:** Enable **seccomp profiles, AppArmor/SELinux policies** to restrict container capabilities.

- [ ] **Network Segmentation:** Deploy **Calico, Cilium** network policies to **microsegment pod-to-pod communication**.

---

### Topic 4: Secrets & Configuration Management — 🔬 Practical

> [!TIP]
> **Goal:** Secure sensitive data in containerized environments.

> [!NOTE]
> ⏱️ **Time Bracket: 1 day** — Secret stores (HashiCorp Vault Agent Injector: sidecar that injects secrets into pod filesystem at runtime without them appearing in pod spec; AWS Secrets Manager with IRSA: Lambda/pod fetches secret using IAM role assigned via OIDC — no static credentials needed), Sealed Secrets (Bitnami: encrypt secrets in Git with cluster public key; only the cluster controller can decrypt — GitOps-safe), workload identity (AWS IRSA: pod-level IAM role via OIDC federation; GCP Workload Identity: GKE SA bound to GCP SA — no service account key files needed), secret rotation (Vault dynamic secrets: database credentials generated per-request with TTL — credential theft has a short exploitation window). Deliverable: demonstrate the difference between a K8s secret exposed in pod spec env vars vs the same secret fetched at runtime via Vault Agent — document what an attacker sees in each case via kubectl describe pod.


- [ ] **Secret Stores:** Use **HashiCorp Vault, AWS Secrets Manager, Azure Key Vault** instead of K8s native secrets.

- [ ] **Init Containers:** Fetch secrets at **pod startup** via init containers instead of baking into images.

- [ ] **Sealed Secrets:** Encrypt secrets in Git using **Bitnami Sealed Secrets, SOPS** for GitOps workflows.

- [ ] **Workload Identity:** Use **cloud provider workload identity** (AWS IRSA, GCP Workload Identity) for keyless authentication.

- [ ] **Secret Rotation:** Implement **automatic secret rotation** and short-lived credentials.

---

### Topic 5: CI/CD & Workflow Automation Attacks — 🔬 Practical

> [!TIP]
> **Goal:** Compromise the software supply chain and automation tier.

> [!NOTE]
> ⏱️ **Time Bracket: 1–2 days** — Pipeline poisoning (GitHub Actions: pull_request_target trigger runs attacker-supplied code from fork with access to secrets — this is the most common GHA security mistake; inject malicious step by modifying workflow YAML in a PR; Jenkins: Groovy script console with admin access = RCE on Jenkins agent = access to all credentials in Credentials store), dependency confusion (publish a package to PyPI/NPM matching an internal private package name with a higher version — pip/npm resolves public over private; the package executes during install on developer workstations or CI), workflow automation takeover (n8n CVE-2026-21858 and similar SSRF-to-RCE in automation platforms; Zapier and Workato webhook abuse for lateral movement to connected cloud services), credential aggregation (automation platforms store cloud credentials, API keys, and OAuth tokens in integrations — admin access to n8n/Zapier = dump all credentials). Deliverable: set up a local Jenkins instance, demonstrate credential theft from Credentials store via Groovy console, and document the attack path.


- [ ] **Pipeline Poisoning:** Inject malicious steps into **GitHub Actions/Jenkins** to alter builds, steal artifacts, or plant backdoors.

- [ ] **Dependency Confusion:** Publish **public packages** matching internal names to hijack build dependency resolution.

- [ ] **Workflow Takeover:** Exploit **workflow automation (n8n, Zapier, Workato)** misconfigs (e.g., **n8n CVE-2026-21858**) to pivot into **AWS/Azure**.

- [ ] **Credential Aggregation:** Treat automation platforms as **credential vaults**; dump **API keys, OAuth tokens, cloud creds** for lateral movement.

- [ ] **Build Artifact Integrity:** Enforce **signing (Sigstore/Cosign)** and **attestations (SLSA/Provenance)** to detect tampering.

---

### Lab Progression (Module 21: Container & Orchestration Security)

> [!TIP]
> **Goal:** Practice container and Kubernetes security with real clusters, not diagrams.

- [ ] **Container Escape Awareness Lab:** Run a deliberately misconfigured container and document which Linux primitives made it unsafe: capabilities, mounts, namespaces, cgroups, seccomp, AppArmor/SELinux.
- [ ] **KubernetesGoat / k8s-ctf Lab:** Complete at least 5 Kubernetes attack scenarios and map each to a control failure.
- [ ] **Image Security Lab:** Build an image, scan it with Trivy/Grype, fix high-risk findings, and rebuild.
- [ ] **Secrets Lab:** Demonstrate unsafe secret exposure, then fix it using Kubernetes secrets, external secret managers, or workload identity.

---

### Topic 6: Container Supply Chain Security — 🔬 Practical

> [!TIP]
> **Goal:** Secure the container image supply chain from build to deployment

> [!NOTE]
> ⏱️ **Time Bracket: 2–3 days** — Container image signing (Docker Content Trust: uses Notary for signature verification; Cosign from Sigstore: sign images with cosign sign, verify with cosign verify — integrates with keyless signing via OIDC), supply chain attacks via base images (malicious base images from public registries; typosquatting attacks on Docker Hub; backdoored images with cryptocurrency miners), image provenance & attestation (SLSA provenance: verifiable build metadata showing what inputs produced which outputs; in-toto attestation: cryptographic evidence of each supply chain step; provenance verification prevents tampering), registry security (Harbor: open-source registry with RBAC, image scanning, signature enforcement; private registries: authentication via registry secrets; webhook notifications for image push events), admission controller policies (OPA Gatekeeper: enforce policies at Kubernetes admission time — block unsigned images, enforce base image allow lists, require specific labels; Kyverno: Kubernetes-native policy engine with simpler YAML syntax), image scanning in CI/CD pipeline (integrate Trivy/Grype/Snyk into CI: fail build on HIGH/CRITICAL vulnerabilities; shift-left scanning: catch vulnerabilities before deployment), SLSA for containers (SLSA Level 1: provenance exists; Level 2: signed provenance; Level 3: hardened build platform; Level 4: hermetic builds), distroless images & minimal base images (distroless: no package manager, no shell — reduces attack surface by 90%; Alpine vs distroless trade-offs: Alpine has a shell for debugging, distroless does not). Deliverable: implement signed image deployment pipeline with Cosign, create OPA Gatekeeper policy to block unsigned images, integrate Trivy scanning into CI/CD with fail-on-critical threshold.

- [ ] **Docker Content Trust (DCT) Implementation:** Enable DCT with DOCKER_CONTENT_TRUST=1 environment variable to require signed images via Notary v1. *Supply chain angle: DCT verifies image publisher identity; unsigned images rejected at pull time.*
- [ ] **Docker Content Trust Uses Notary:** DCT leverages Notary for signature verification with push keys required for signing images. *Supply chain angle: Notary provides content trust through The Update Framework (TUF) model.*
- [ ] **Docker Content Trust Adoption Challenges:** Limited adoption due to complexity of key management and push key distribution. *Supply chain angle: usability vs security trade-off; complexity prevents widespread adoption.*
- [ ] **Cosign Sign Command:** Use cosign sign command to cryptographically sign container images with private keys or keyless OIDC. *Supply chain angle: cosign simplifies signing compared to DCT; modern supply chain standard.*
- [ ] **Cosign Verify Command:** Use cosign verify to validate image signatures before deployment or runtime. *Supply chain angle: signature verification prevents tampered or unauthorized images from running.*
- [ ] **Cosign Keyless Signing via OIDC:** Sign images without managing keys using OIDC providers (GitHub Actions, Google, Microsoft) for ephemeral certificates. *Supply chain angle: keyless signing removes key management burden; certificates from Fulcio CA.*
- [ ] **Cosign Signature Storage:** Store image signatures in OCI registry alongside images as attached artifacts. *Supply chain angle: co-located signatures simplify distribution; registry serves both image and signature.*
- [ ] **Sigstore Toolchain:** Leverage Sigstore ecosystem including cosign (signing), rekor (transparency log), and fulcio (certificate authority). *Supply chain angle: Sigstore provides complete signing infrastructure; transparency log ensures non-repudiation.*
- [ ] **Supply Chain Attack — Malicious Base Images:** Attackers upload backdoored base images to Docker Hub masquerading as legitimate images. *Supply chain angle: public registries are attacker targets; verify image sources.*
- [ ] **Supply Chain Attack — Typosquatting:** Attackers create images with names similar to popular images (nginx vs nginix, python vs pythom). *Supply chain angle: typos in Dockerfile FROM line pull malicious images; review base image names.*
- [ ] **Supply Chain Attack — Backdoored Cryptocurrency Miners:** Compromised images include hidden cryptocurrency miners consuming CPU/memory resources. *Supply chain angle: miners generate profit for attackers; performance degradation indicator.*
- [ ] **Supply Chain Attack — Compromised Maintainer Accounts:** Attackers compromise Docker Hub maintainer accounts to push malicious updates to legitimate images. *Supply chain angle: trust chain breaks at maintainer; use image digests for immutability.*
- [ ] **Supply Chain Attack — Dependency Confusion:** Dockerfile pip install or npm install may pull attacker-controlled packages with same name as internal packages. *Supply chain angle: public package registries checked before private; namespace confusion enables attack.*
- [ ] **Supply Chain Mitigation — Use Official Images:** Only use Docker Official Images or Verified Publisher images from trusted sources. *Supply chain angle: official images have security reviews and transparency; unverified images = unknown risk.*
- [ ] **Supply Chain Mitigation — Pin by Digest Not Tag:** Pin images by SHA256 digest (image@sha256:abc123) not mutable tags (image:latest). *Supply chain angle: tags can be overwritten; digests are immutable content-addressable references.*
- [ ] **SLSA Provenance Metadata:** Provenance contains verifiable build metadata including source repository, commit SHA, and build command. *Supply chain angle: provenance proves what inputs produced which outputs; tamper detection.*
- [ ] **SLSA Provenance Prevents Tampering:** Verifiable provenance detects source code or build system tampering by cryptographically linking source to artifact. *Supply chain angle: prevents malicious code injection during build; integrity verification.*
- [ ] **in-toto Attestation Evidence:** in-toto provides cryptographic evidence of each supply chain step with signed link metadata. *Supply chain angle: attests who did what, when, with what materials; complete audit trail.*
- [ ] **in-toto Link Metadata:** Link metadata records actors, actions, and materials for each supply chain step (code review, build, test, deploy). *Supply chain angle: metadata proves required steps occurred; missing steps detectable.*
- [ ] **in-toto Layout Policy:** Layout policy defines required supply chain steps and authorized functionaries (roles) per step. *Supply chain angle: policy enforcement ensures multi-person approval and segregation of duties.*
- [ ] **Provenance Verification — Signature Validation:** Verify attestation signatures using public keys or certificate transparency to ensure authenticity. *Supply chain angle: signature validation prevents forged attestations; trust anchor required.*
- [ ] **Provenance Verification — Source Repository Match:** Confirm image was built from expected source repository, not attacker fork. *Supply chain angle: prevents fork confusion; validates source legitimacy.*
- [ ] **Provenance Verification — Build Platform Requirements:** Ensure build platform meets security requirements (SLSA level, hardening, isolation). *Supply chain angle: compromised builder = compromised artifacts; builder trust critical.*
- [ ] **Harbor RBAC:** Harbor provides role-based access control with project-level permissions for push/pull/admin operations. *Supply chain angle: least privilege access; prevents unauthorized image modifications.*
- [ ] **Harbor Integrated Scanning:** Harbor integrates vulnerability scanners (Trivy, Clair) to automatically scan pushed images. *Supply chain angle: scan-on-push catches vulnerabilities before deployment; automated detection.*
- [ ] **Harbor Image Signing Enforcement:** Harbor enforces image signature requirements using Cosign or Notary before allowing pulls. *Supply chain angle: signature enforcement prevents unsigned images from deployment; policy-based control.*
- [ ] **Harbor Cross-Registry Replication:** Harbor replicates images across multiple registries for redundancy and geographic distribution. *Supply chain angle: replication enables disaster recovery and reduces latency.*
- [ ] **Harbor Audit Logging:** Harbor logs all image operations (push, pull, delete) for security monitoring and compliance. *Supply chain angle: audit logs enable forensic investigation of image tampering or unauthorized access.*
- [ ] **Private Registry Authentication:** Use Kubernetes imagePullSecrets to authenticate to private registries for image pulls. *Supply chain angle: authentication prevents unauthorized image access; secrets management critical.*
- [ ] **Private Registry Network Segmentation:** Isolate container registry in private subnet with limited network access. *Supply chain angle: network segmentation reduces attack surface; registry should not be internet-exposed.*
- [ ] **Private Registry Webhook Notifications:** Configure webhooks to trigger on image push events for automated scanning or deployment pipelines. *Supply chain angle: webhooks enable event-driven automation; immediate response to image updates.*
- [ ] **Registry Access Control — Least Privilege:** Grant read-only access for deployments; reserve write access to CI/CD service accounts. *Supply chain angle: least privilege limits blast radius; compromised workload cannot push malicious images.*
- [ ] **Registry Immutable Tags:** Enable immutable tags to prevent tag overwriting, ensuring image integrity. *Supply chain angle: immutability prevents tag substitution attacks; digest-based references remain valid.*
- [ ] **Registry Tag Lifecycle Policies:** Implement policies to automatically delete old or unused images to reduce storage and attack surface. *Supply chain angle: stale images may contain unpatched vulnerabilities; lifecycle management reduces risk.*
- [ ] **OPA Gatekeeper Admission Enforcement:** Deploy OPA Gatekeeper to enforce admission control policies at Kubernetes API level. *Supply chain angle: admission control is fail-closed gate; reject non-compliant workloads before creation.*
- [ ] **OPA Gatekeeper Block Unsigned Images:** Create constraint template to reject pods pulling unsigned images. *Supply chain angle: signature enforcement at admission time; unsigned images never run.*
- [ ] **OPA Gatekeeper Base Image Allow Lists:** Enforce policies allowing only approved base images from trusted registries. *Supply chain angle: allow lists prevent supply chain attacks via malicious base images.*
- [ ] **OPA Gatekeeper Require Specific Labels:** Mandate labels like owner, team, and criticality for pod tracking and accountability. *Supply chain angle: labels enable asset tracking and incident response ownership.*
- [ ] **OPA Gatekeeper Deny Privileged Containers:** Block privileged containers to prevent host namespace access and privilege escalation. *Supply chain angle: privileged containers = container escape risk; deny by default.*
- [ ] **OPA Gatekeeper Registry Restriction Example:** Create policy rejecting images from registries other than harbor.corp.com. *Supply chain angle: registry restriction prevents external untrusted images.*
- [ ] **Kyverno Kubernetes-Native Policy:** Use Kyverno for policy management with simpler YAML syntax compared to OPA Rego. *Supply chain angle: Kyverno's YAML syntax lowers learning curve; faster policy development.*
- [ ] **Kyverno Validate, Mutate, Generate Policies:** Define validation (enforce rules), mutation (modify resources), and generation (create resources) policies. *Supply chain angle: mutation enables automatic security controls (add securityContext); validation blocks violations.*
- [ ] **Kyverno Image Verification via Cosign:** Integrate Kyverno with Cosign for native image signature verification in policies. *Supply chain angle: Kyverno verifies cosign signatures without external tools; streamlined enforcement.*
- [ ] **Kyverno Auto-Add Security Context Example:** Create policy that automatically adds security context to pods missing it. *Supply chain angle: mutation ensures secure defaults; developer doesn't need to specify security controls.*
- [ ] **Policy Enforcement — Fail Closed:** Configure admission controllers to default deny unless policy explicitly allows (fail closed). *Supply chain angle: fail closed = secure by default; policy bugs don't create vulnerabilities.*
- [ ] **Policy Enforcement — Audit Mode First:** Deploy policies in audit mode initially to identify violations without blocking; enforce after tuning. *Supply chain angle: audit mode prevents operational disruption; gradual enforcement reduces risk.*
- [ ] **Policy Enforcement — System Namespace Exemptions:** Exempt system namespaces (kube-system, kube-public) from policies to avoid breaking cluster. *Supply chain angle: system components may require privileges; blanket enforcement breaks cluster operations.*
- [ ] **CI/CD Scanning — Pre-Commit Dockerfile Lint:** Scan Dockerfiles with hadolint for best practices before commit. *Supply chain angle: early detection of insecure patterns (root user, apt-get without cleanup).*
- [ ] **CI/CD Scanning — Build Time Image Scan:** Scan image after build using Trivy, Grype, or Snyk before pushing to registry. *Supply chain angle: shift-left scanning catches vulnerabilities before deployment; fail fast.*
- [ ] **CI/CD Scanning — Registry Scan on Push:** Enable automatic scanning when image pushed to registry (Harbor, AWS ECR). *Supply chain angle: registry scanning provides second validation; catches missed vulnerabilities.*
- [ ] **CI/CD Scanning — Runtime Continuous Scanning:** Continuously scan running images for newly disclosed vulnerabilities. *Supply chain angle: runtime scanning catches zero-days in running workloads; continuous risk assessment.*
- [ ] **Scanning Fail Threshold — Fail on HIGH/CRITICAL:** Configure CI/CD to fail build when HIGH or CRITICAL vulnerabilities detected. *Supply chain angle: fail thresholds enforce minimum security bar; prevents deployment of high-risk images.*
- [ ] **Scanning Fail Threshold — Allow MEDIUM with Approval:** Permit MEDIUM severity vulnerabilities with manual approval workflow. *Supply chain angle: balances security with velocity; manual review for acceptable risks.*
- [ ] **Scanning Patching SLA:** Set service-level agreements for patching (7 days for HIGH, 30 days for MEDIUM vulnerabilities). *Supply chain angle: SLAs ensure timely remediation; expired SLAs trigger escalation.*
- [ ] **Scanning Tool — Trivy:** Use Trivy for fast, comprehensive vulnerability scanning supporting multiple artifact types. *Supply chain angle: Trivy scans containers, filesystems, git repos; broad coverage.*
- [ ] **Scanning Tool — Grype:** Use Anchore's Grype scanner with strong SBOM support for software bill of materials tracking. *Supply chain angle: Grype integrates with Syft for SBOM generation; supply chain transparency.*
- [ ] **Scanning Tool — Snyk:** Use Snyk commercial scanner for good developer UX and IDE integration. *Supply chain angle: Snyk provides fix recommendations and automated PRs; developer-friendly.*
- [ ] **Scanning Tool — Clair:** Use CoreOS Clair scanner with Quay registry integration for container scanning. *Supply chain angle: Clair provides vulnerability database; integrates natively with Quay.*
- [ ] **SLSA Level 1 — Provenance Exists:** Build metadata recorded showing source, builder, and build command. *Supply chain angle: level 1 = basic transparency; no integrity guarantees yet.*
- [ ] **SLSA Level 2 — Signed Provenance:** Provenance cryptographically signed to prevent tampering. *Supply chain angle: level 2 = tamper-proof metadata; detects post-build modifications.*
- [ ] **SLSA Level 3 — Hardened Build Platform:** Build platform hardened with non-falsifiable provenance from isolated builders. *Supply chain angle: level 3 = trustworthy builder; prevents compromised build system from forging provenance.*
- [ ] **SLSA Level 4 — Hermetic Builds:** Reproducible builds with two-person review and hermetic environment. *Supply chain angle: level 4 = highest assurance; reproducible builds enable independent verification.*
- [ ] **SLSA Implementation — Use SLSA L3 Builders:** Deploy GitHub Actions or Google Cloud Build which provide SLSA Level 3 builders. *Supply chain angle: managed builders provide provenance without custom infrastructure.*
- [ ] **SLSA Implementation — Generate Provenance:** Use slsa-github-generator action to automatically generate provenance during CI/CD. *Supply chain angle: automated provenance generation; no manual attestation required.*
- [ ] **SLSA Implementation — Store Provenance in OCI Registry:** Store provenance as OCI artifact attached to image in registry. *Supply chain angle: co-located storage simplifies distribution; provenance travels with image.*
- [ ] **SLSA Implementation — Verify Provenance Before Deployment:** Validate provenance signatures and metadata before deploying to production. *Supply chain angle: deployment-time verification enforces supply chain requirements.*
- [ ] **SLSA Benefits — Prevent Source Tampering:** Provenance links source commit to artifact, detecting unauthorized code changes. *Supply chain angle: prevents attacker code injection; verifiable source lineage.*
- [ ] **SLSA Benefits — Detect Compromised Build Systems:** Build provenance reveals if build occurred on unauthorized or compromised builder. *Supply chain angle: detects supply chain compromise at build layer.*
- [ ] **SLSA Benefits — Enforce Two-Person Review:** Level 4 requires two-person review for production deployments, preventing insider threats. *Supply chain angle: segregation of duties; no single person can deploy malicious code.*
- [ ] **Distroless Images — No Package Manager:** Distroless images exclude package managers (apt, yum) reducing attack surface. *Supply chain angle: no package manager = attackers cannot install tools; minimal post-compromise capability.*
- [ ] **Distroless Images — No Shell:** Distroless images lack shells (/bin/sh, /bin/bash) preventing interactive access. *Supply chain angle: no shell = RCE attackers cannot run shell commands; must use application vulnerabilities directly.*
- [ ] **Distroless Images — Runtime Only:** Include only application runtime (Java, Python, Go, Node) and application code. *Supply chain angle: minimal components = minimal vulnerabilities; 90% smaller attack surface.*
- [ ] **Distroless Images — Ephemeral Container Debugging:** Debug distroless containers using kubectl debug with ephemeral debug container. *Supply chain angle: debugging without permanent shell; temporary debug access.*
- [ ] **Alpine vs Distroless Comparison — Alpine Size:** Alpine base image approximately 5MB with musl libc and shell. *Supply chain angle: Alpine compact but includes shell; trade-off between size and debugging.*
- [ ] **Alpine vs Distroless Comparison — Distroless Size:** Distroless base image approximately 2MB with glibc and no shell. *Supply chain angle: Distroless minimal but harder to debug; security over convenience.*
- [ ] **Alpine vs Distroless Trade-Off:** Alpine easier to debug with shell access; distroless more secure with no shell. *Supply chain angle: choose based on risk tolerance and debugging requirements.*
- [ ] **Multi-Stage Builds — Build Stage:** Use full toolchain image (gcc, npm, pip) for compilation in build stage. *Supply chain angle: build stage includes all tools; not shipped in runtime.*
- [ ] **Multi-Stage Builds — Runtime Stage:** Copy only compiled artifacts to minimal base image for runtime stage. *Supply chain angle: runtime stage excludes build tools; reduces attack surface.*
- [ ] **Multi-Stage Builds Example:** FROM golang AS build for compilation, then FROM gcr.io/distroless/static for runtime. *Supply chain angle: multi-stage separates build from runtime; final image contains only necessary artifacts.*

**Lab Progression:**
- [ ] Sign a container image with Cosign and verify signature
- [ ] Create OPA Gatekeeper policy to block unsigned images
- [ ] Integrate Trivy scanning into CI/CD with fail-on-critical threshold
- [ ] Build a multi-stage Dockerfile with distroless runtime stage
- [ ] Implement SLSA provenance generation in GitHub Actions
- [ ] Configure Harbor registry with signature enforcement

> [!IMPORTANT]
> **Move-On Gate (Topic 6):** I can sign container images with Cosign, write OPA Gatekeeper policies to enforce image signatures, integrate vulnerability scanning into CI/CD pipelines with failure thresholds, and explain the difference between Docker Content Trust and Sigstore/Cosign.

---

### Topic 7: Hypervisor Security — 🧠 Conceptual

> [!TIP]
> **Goal:** Understand the attack surface one layer below containers — the hypervisor. Container escape gets defender attention; hypervisor-level attacks are less understood and harder to detect. Enterprise pentests against virtualised infrastructure encounter these regularly.

> [!NOTE]
> ⏱️ **Time Bracket: 1 day** — VMware ESXi attack surface (SSH with default root credentials; vCenter RCE CVEs like CVE-2021-21985 — a compromised vCenter controls all managed ESXi hosts; VMDK credential extraction: mount VMDK offline with qemu-nbd or 7-zip, access NTDS.dit/SAM+SYSTEM — bypasses all runtime protections; snapshot credential theft: VM snapshot freezes LSASS memory and is accessible offline), Proxmox attack surface (API endpoint at https://host:8006/api2/json; pveum and qm CLI from Proxmox shell), VM escape CVE awareness (VENOM CVE-2015-3456: QEMU floppy controller buffer overflow; VMware Tools escalation history; VirtualBox shared folder and clipboard injection), nested virtualization security implications (hypervisor isolation breaks down in nested VMs; snapshot-based lab environments may expose host credentials through nested VM memory). Deliverable: document two ESXi attack vectors and their specific mitigations, and explain how VMDK credential extraction is detected or prevented.


- [ ] **VMware ESXi Attack Surface:** ESXi is the dominant enterprise bare-metal hypervisor. Key attack vectors:
  - **Unauthenticated ESXi Shell Access:** Legacy ESXi deployments may have SSH enabled with default or weak credentials (`root` / empty). `esxcli` and `vim-cmd` provide full VM management from the shell.
  - **vCenter Server Vulnerabilities:** vCenter (the management plane) has had critical unauthenticated RCE CVEs (CVE-2021-21985, CVE-2021-22005). A compromised vCenter = control over all managed ESXi hosts and all VMs.
  - **VMDK Credential Extraction:** Mount a VMDK file offline to extract credentials from Windows VMs: boot into recovery mode or use `7-zip` / `qemu-nbd` to mount and access the NTDS.dit/SAM + SYSTEM hive. This bypasses runtime protections entirely.
  - **Snapshot Credential Theft:** VM snapshots freeze memory state. A snapshot of a running Windows DC contains LSASS memory — mountable offline for credential extraction without triggering EDR.

- [ ] **Proxmox Attack Surface:** Open-source hypervisor used in SMBs and test environments:
  - Default API endpoint at `https://host:8006/api2/json` — enumerate with unauthenticated calls to identify version and nodes
  - Proxmox VE < 7.x had CSRF and auth bypass vulnerabilities
  - `pveum` and `qm` CLI allow full VM control from the Proxmox shell

- [ ] **VM Escape CVE Awareness:** True VM escapes (guest → hypervisor) are rare but high-value:
  - **VENOM (CVE-2015-3456):** QEMU virtual floppy disk controller buffer overflow — allowed guest-to-host escape on QEMU/KVM and Xen
  - **Escape via VMware Tools:** VMware Tools (running inside guest) has historically had privilege escalation and local escape vulnerabilities
  - **Shared Clipboard / Drag-and-Drop:** VMware and VirtualBox guest isolation can be broken via clipboard injection or shared folder misconfigurations

- [ ] **Nested Virtualisation Security:** Understand security implications of nested VMs (VM inside a VM): hypervisor isolation assumptions break down; snapshot-based lab environments using nested VMs may expose host credentials through nested VM memory.

- [ ] **Defensive Controls — Hypervisor Hardening:**
  - Enable lockdown mode on ESXi (restricts shell and API access to vCenter only)
  - Disable SSH on ESXi hosts in production; use vCenter for management
  - Enforce vCenter RBAC — no shared `administrator@vsphere.local` accounts
  - Network-segregate the management network (VMkernel port) from VM traffic
  - Enable VM encryption (vSphere VM Encryption) for sensitive VMs to prevent offline VMDK extraction

> [!IMPORTANT]
> **Move-On Gate (Module 21):** Produce a Kubernetes hardening report with RBAC, network policy, admission control, image scanning, and runtime detection notes. Demonstrate container image signing with Cosign and OPA Gatekeeper policy enforcement. Additionally, document: (1) two ESXi attack vectors and their mitigations, (2) how VMDK credential extraction works and what prevents it.

---

## Module 22: Adversary Emulation & Purple Teaming

> [!NOTE]
> **Scope & Placement:** Module 22 (Adversary Emulation & Purple Teaming) synthesizes enterprise attack paths from Modules 19–21 (Active Directory, Cloud, Containers) into unified emulation campaigns.

> [!WARNING]
> **Prerequisites:** This module requires offensive maturity (Stage 2) plus enterprise infrastructure knowledge from Modules 19–21. Complete prior Stage 4 content before attempting purple teaming campaigns.

> [!TIP]
> ⏱️ **Module 22 Total Time Budget: 1 week**
> T1 (MITRE ATT&CK mastery): 1–2 days | T2 (APT/threat actor emulation): 2 days | T3 (purple team exercises): 2 days | T4 (metrics/reporting): 1 day.
> Purple teaming is how you demonstrate value beyond breaking things. Defenders who understand offensive tradecraft are rare and expensive. If you can run an emulation plan and produce a detection coverage matrix with MTTD/MTTR numbers, you are hireable in both red and blue team roles.

### Topic 1: MITRE ATT&CK Framework Mastery — 🧠 Conceptual

> [!TIP]
> **Goal:** Understand the universal language of adversary behavior.

> [!NOTE]
> ⏱️ **Time Bracket: 1–2 days** — Tactic familiarity (all 14 tactics in order: Reconnaissance → Resource Development → Initial Access → Execution → Persistence → Privilege Escalation → Defense Evasion → Credential Access → Discovery → Lateral Movement → Collection → Command and Control → Exfiltration → Impact — know what each phase accomplishes and which tool category belongs to it), technique deep-dive (use MITRE ATT&CK Navigator to build a heatmap for one APT group — color the techniques they use; this reveals their operational profile), sub-technique granularity (T1059 is Scripting; T1059.001 is PowerShell; T1059.003 is CMD; defenders create different detection rules for each — operators choose the sub-technique based on detection risk), data source mapping (every technique lists its detection data sources: process creation, network traffic, registry — map these to your SIEM event IDs). Deliverable: build an ATT&CK Navigator heatmap for APT29 and identify the three techniques with the lowest detection data source coverage.


- [ ] **Tactic Familiarity:** Master all **14 tactics** (Initial Access → Impact) and their relationships in the attack lifecycle.

- [ ] **Technique Deep-Dive:** Study **100+ core techniques** with focus on **prevalence, detection difficulty, impact** ratings.

- [ ] **Sub-Technique Granularity:** Understand **sub-technique variations** for precise emulation (e.g., T1059.001 PowerShell vs T1059.003 CMD).

- [ ] **Data Source Mapping:** Link techniques to **detection data sources** (process creation, network traffic, registry modifications).

- [ ] **Mitigation Strategies:** Review **MITRE mitigations** for each technique to understand defensive controls.

---

### Topic 2: APT & Threat Actor Emulation — 🔬 Practical

> [!TIP]
> **Goal:** Replicate real-world adversary campaigns.

> [!NOTE]
> ⏱️ **Time Bracket: 2 days** — APT profiling (APT29 Cozy Bear: spearphishing with NOBELIUM toolset, OAuth consent phishing, Golden SAML; APT28 Fancy Bear: credential harvesting, Mimikatz, NTLMv2 relay; Lazarus Group: supply chain, RATs, cryptocurrency theft; FIN7: sophisticated phishing, custom malware, financial targets — understand each group's preferred initial access and lateral movement TTPs), campaign recreation (MITRE ATT&CK Adversary Emulation Plans: download APT29 or APT3 plan from attack.mitre.org/resources/adversary-emulation-plans; execute step by step in lab — each step maps to a specific ATT&CK technique), tool replication (Atomic Red Team: install, run Invoke-AtomicTest for specific techniques, observe what each generates in logs — this is how you build detection coverage data). Deliverable: execute 5 Atomic Red Team tests for different ATT&CK techniques and document what each generates in Windows Event Logs, Sysmon, and EDR telemetry.


- [ ] **APT Profiling:** Study **APT groups** (APT28, APT29, Lazarus, FIN7) including **TTPs, tools, targeting, infrastructure**.

- [ ] **Campaign Recreation:** Emulate **documented campaigns** step-by-step using **MITRE ATT&CK Navigator** for technique mapping.

- [ ] **Tool Replication:** Use **adversary tools** (Mimikatz, Cobalt Strike, Empire, custom malware) to match TTP fidelity.

- [ ] **Infrastructure Mimicry:** Build **attack infrastructure** (domains, IPs, C2) that mimics **APT patterns and behaviors**.

- [ ] **Operational Tempo:** Match **adversary dwell time, persistence patterns, exfil timing** for realistic simulation.

- [ ] **Adversary Emulation Plans:** Execute **MITRE ATT&CK Adversary Emulation Plans** for groups like **APT29, Scattered Spider** to test realistic kill chains.

---

### Topic 3: Purple Team Exercises — 🧠🔬 Mixed

> [!TIP]
> **Goal:** Collaborative offense-defense improvement.

> [!NOTE]
> ⏱️ **Time Bracket: 2 days** — Joint planning (define exercise scope in writing: specific techniques from ATT&CK, target systems in lab, success criteria — e.g., technique X should generate alert Y within Z minutes; blue team commits to no prior notification of exact timing), live detection tuning (execute attack in lab while blue team watches their SIEM in real-time; when attack runs without triggering an alert, that is a detection gap — immediately document it and tune the rule), gap analysis (for each technique executed: was there an alert? was it high-fidelity or noisy? what would an attacker do to evade the rule? — this is the core deliverable), playbook development (for each detection: write the Sigma rule or SIEM query, the analyst triage steps, and the response procedure). Deliverable: run one purple team exercise covering at minimum 5 ATT&CK techniques; produce a detection coverage matrix with hit/miss results for each.


- [ ] **Joint Planning:** Define **objectives, scope, techniques, success criteria** with both red and blue teams.

- [ ] **Live Detection Tuning:** Execute **attacks in controlled environment** while defenders **tune detection rules in real-time**.

- [ ] **Gap Analysis:** Identify **detection blind spots, control failures, response deficiencies** through collaborative testing.

- [ ] **Playbook Development:** Create **detection playbooks** with **queries, alerts, response procedures** for each emulated technique.

- [ ] **Iterative Improvement:** Run **multiple rounds** of testing with **incremental detection improvements** to measure progress.

---

### Topic 4: Metrics & Reporting — 🧠 Conceptual

> [!TIP]
> **Goal:** Quantify security posture improvement.

> [!NOTE]
> ⏱️ **Time Bracket: 1 day** — Detection coverage percentage (count ATT&CK techniques with at least one detection rule vs total techniques in scope; even 30% coverage is notable in most orgs — document it honestly), MTTD/MTTR calculation (MTTD: time from attack execution to first alert; MTTR: time from first alert to containment action; measure both in each exercise and track over multiple rounds), false positive rate (ratio of total alerts to true positive alerts during exercise; a rule that fires 50 times per technique execution is useless — tune it), control effectiveness rating (for each technique: None = no detection, Partial = detects sometimes or with delay, Full = reliable and timely detection; this matrix becomes the purple team deliverable). Deliverable: produce a one-page purple team metrics summary from your exercise with detection coverage, MTTD, and control effectiveness ratings per technique.


- [ ] **Detection Coverage:** Calculate **% of ATT&CK techniques** with detection coverage across the matrix.

- [ ] **MTTD/MTTR:** Measure **Mean Time to Detect** and **Mean Time to Respond** for each technique tested.

- [ ] **False Positive Rate:** Track **alert accuracy** and **tuning effectiveness** over multiple exercises.

- [ ] **Control Effectiveness:** Rate **preventative, detective, responsive** controls against each technique (None/Partial/Full).

- [ ] **Trend Analysis:** Compare **metrics across time** to demonstrate **security maturity improvement**.

### Lab Progression (Module 22: Adversary Emulation & Purple Teaming)

| Level | Task | Deliverable |
| ------- | ------ | ------------- |
| 1 | Map a single APT group's TTPs to MITRE ATT&CK Navigator | ATT&CK heatmap export |
| 2 | Execute Atomic Red Team tests for 5 techniques in a lab | Detection results per technique |
| 3 | Run a full APT emulation plan (e.g., APT29) in lab | Emulation report with detection gaps |
| 4 | Build detection rules for each gap identified | Updated detection coverage matrix |
| 5 | Conduct a full purple team exercise with metrics | MTTD/MTTR report + improvement recommendations |

> [!IMPORTANT]
> **Move-On Gate:** I can execute adversary emulation plans, measure detection coverage, calculate MTTD/MTTR, and produce actionable purple team reports demonstrating security posture improvement.

---

---

## Module 23: Sniffing & Spoofing

> [!NOTE]
> **📚 Recommended Books for This Part**
> - 🔴 `The Power of Scapy V2` — ARP spoofing, packet injection chapters — tool mastery for MitM and packet manipulation
> - 🟡 `Wireshark Cheat Sheet` — Keep open during all capture and analysis labs
> - 🟢 `Hacking and Network Defense` — Sniffing chapter — defender detection of sniffing activity (informs OPSEC)

> [!TIP]
> ⏱️ **Module 23 Total Time Budget: 1 week**
> T1 (environment/fundamentals): 1 day | T2 (sniffing/passive recon): 1 day | T3 (spoofing/active deception): 1–2 days | T4 (MITM/exploitation): 2 days | T5 (defenses/mitigation): 1 day.
> In modern TLS-everywhere networks, sniffing and spoofing are primarily useful for internal network assessments post-compromise. ARP spoofing plus MITM is a standard internal pentest technique to capture cleartext internal traffic or relay NTLM hashes. SSL stripping is mostly defeated by HSTS preloading but still works against internal HTTP services.

### Topic 1: The Environment & Fundamentals (The Setup) — 🧠🔬 Mixed

> [!TIP]
> **Goal:** Understand the battlefield. I cannot spoof what I cannot map.

> [!NOTE]
> ⏱️ **Time Bracket: 1 day** — Protocol hierarchy and trust model (MAC address is Layer 2 local trust — switches forward by MAC table; IP is Layer 3 routed — ARP bridges the gap between them; ARP has no authentication which is the attack surface), switch vs hub reality (modern networks use switches: you only see your own traffic passively; must ARP spoof or MAC flood to bypass segmentation), NIC configuration (tcpdump -i eth0 in promiscuous mode; airodump-ng in monitor mode for wireless; understand the difference: promiscuous mode sees all frames on the wire, monitor mode captures raw 802.11 frames), TCP/TLS handshake analysis (Wireshark: TCP SYN→SYN-ACK→ACK sequence; TLS ClientHello contains supported cipher suites and SNI; sequence numbers matter for session hijacking timing). Deliverable: set up Wireshark in a home lab and capture and decode a complete HTTP login session from packet to credentials.


- [ ] **Protocol Hierarchy & Trust:** Differentiate between **MAC Addresses** (Layer 2 - Local Trust) and **IP Addresses** (Layer 3 - Routing). Spoofing relies on exploiting the trust mismatch between these layers.

- [ ] **Secure vs. Insecure Protocols:** Identify targets using cleartext protocols like **HTTP, FTP, Telnet, DNS**. These are trivial to sniff. Encrypted protocols like **TLS/HTTPS** and **SSH** require advanced downgrade attacks or decryption to bypass.

- [ ] **The Switch vs. Hub Reality:** Modern networks use switches which segment traffic by MAC. I cannot passively sniff; I must **ARP spoof, MAC flood**, or **VLAN hop** to bypass segmentation.

- [ ] **Interface Configuration:** Configure NIC to **Promiscuous Mode** (tcpdump, Wireshark) to capture all traffic, not just destined to my MAC; practice with **monitor mode** on wireless cards.

- [ ] **Handshake & Session Logic:** Study **TCP/TLS handshakes** (SYN/ACK, ClientHello/ServerHello) to identify session boundaries; understand **sequence numbers, window size, timestamps** for **replay and hijack** timing.

---

### Topic 2: Sniffing & Passive Reconnaissance (The Ear) — 🔬 Practical

> [!TIP]
> **Goal:** Capture data without alerting the target. "Listen before act."

> [!NOTE]
> ⏱️ **Time Bracket: 1 day** — Passive packet capture (tcpdump -i eth0 -w capture.pcap; filter for broadcast/multicast: ARP, DHCP, mDNS identify active hosts and gateways without sending directed traffic; Wireshark follow TCP stream to reassemble HTTP sessions), wireless interception (airodump-ng ––bssid TARGET ––channel 6 ––write capture; wait for client to authenticate or send deauth to force reconnect; aircrack-ng on captured 4-way handshake), protocol analysis (Wireshark filters: http contains password, ftp.request.command == PASS, smtp contains AUTH; extract cleartext credentials, API keys, and session tokens from pcap; tcpflow for stream reassembly). Deliverable: capture a pcap in a lab network, extract at least one cleartext credential using Wireshark filters and follow-stream.


- [ ] **Passive Packet Capture:** Use **tcpdump/Wireshark** to capture broadcast/multicast traffic (ARP, DHCP, mDNS) to identify active hosts, gateways, and services without sending directed traffic.

- [ ] **Wireless Interception:** Set wireless NIC to **monitor mode**; capture **WPA2/WPA3 4-way handshakes, PMKID** for offline cracking; identify **SSID, client MAC, AP MAC** patterns.

- [ ] **Protocol Analysis:** Filter **pcap** by protocol (HTTP, FTP, SMTP, DNS); identify **cleartext credentials, API keys, session tokens**, and software **User-Agent/Server banners**.

- [ ] **Stream Reassembly:** Use **tcpflow, Wireshark Follow TCP Stream** to reassemble files, images, emails, or form submissions from fragmented packets.

---

### Topic 3: Spoofing & Active Deception (The Lie) — 🔬 Practical

> [!TIP]
> **Goal:** Inject false information into the network to redirect or manipulate traffic.

> [!NOTE]
> ⏱️ **Time Bracket: 1–2 days** — ARP spoofing (arpspoof -i eth0 -t victim-ip gateway-ip and simultaneously arpspoof -i eth0 -t gateway-ip victim-ip; enable IP forwarding: echo 1 > /proc/sys/net/ipv4/ip_forward; Bettercap: bettercap -iface eth0, then set arp.spoof.targets, arp.spoof on), DNS spoofing (Bettercap dns.spoof module: set dns.spoof.domains target.com, dns.spoof.address attacker-ip; responds to DNS queries before legitimate resolver), DHCP starvation and rogue DHCP (Bettercap dhcp.server or yersinia -G: exhaust DHCP pool with rapid Discover requests, then serve own gateway/DNS), MAC spoofing (macchanger -r eth0 for random MAC; -m for specific MAC; bypass MAC filtering and DHCP reservations), SSL stripping (Bettercap https.proxy: downgrades HTTPS to HTTP by stripping redirect; defeated by HSTS preloading). Deliverable: perform a complete ARP spoof plus DNS redirect in a lab environment and capture credentials from a redirected HTTP login.


- [ ] **ARP Spoofing:** Flood the network with **gratuitous ARP packets** linking my MAC to the **gateway IP**; forces the switch to route victim traffic through you; use **arpspoof, dsniff, b[[Ettercap]]**.

- [ ] **DNS Spoofing:** Respond to **DNS queries faster than the legitimate server**; redirect victims to malicious login pages for **credential harvesting** or **malware distribution**.

- [ ] **DHCP Starvation & Rogue DHCP:** Exhaust legitimate DHCP pools and serve my own **gateway/DNS** to all clients; enables **MITM and traffic redirection**.

- [ ] **MAC Spoofing:** Change burned-in MAC to bypass **MAC filtering, NAC (Network Access Control), DHCP reservations**; use **macchanger** (Linux) or **SetMACAddress** (Windows).

- [ ] **IP Spoofing:** Forge **source IP** in packet headers to **hide identity, impersonate trusted hosts**, or launch **reflection/amplification attacks** in DDoS.

- [ ] **SSL Stripping & HTTP Downgrade:** Intercept **HTTPS traffic** and downgrade to **HTTP** by breaking the TLS handshake; use **sslstrip, mitmproxy** to expose encrypted traffic in cleartext.

---

### Topic 4: Man-in-the-Middle & Exploitation (The Kill) — 🔬 Practical

> [!TIP]
> **Goal:** Intercept, modify, and relay traffic to extract or manipulate data.

> [!NOTE]
> ⏱️ **Time Bracket: 2 days** — MITM positioning (Bettercap: arp.spoof + net.sniff combination; mitmproxy: set as transparent proxy with iptables redirect; Burp Suite: upstream proxy for HTTPS interception), session hijacking (extract session cookies from HTTP headers in Wireshark or Bettercap net.sniff; inject into browser to impersonate without password), credential sniffing (Bettercap net.sniff filter for POST data containing password/pass/pwd keywords; FTP and Telnet credentials appear in plaintext in pcap), rogue AP evil twin (hostapd-wpe for WPA2-Enterprise identity harvesting; airbase-ng for open AP; route victim traffic through attacker box for full cleartext inspection), traffic injection (Bettercap inject.js module: inject JavaScript into HTTP responses; DNS modification: redirect to phishing page). Deliverable: complete full MITM chain: ARP spoof then credential capture from a lab target browsing HTTP sites.


- [ ] **MITM Positioning:** Establish myself between victim and gateway via **ARP spoofing, DNS redirection, rogue DHCP, or rogue AP**; use **ettercap, mitmproxy, [[Burp_Suite]]** to intercept and modify traffic in real-time.

- [ ] **Session Hijacking:** Extract **session cookies, JWT tokens, CSRF tokens** from sniffed **HTTP headers** and **POST bodies**; inject stolen tokens to impersonate user without password.

- [ ] **Credential Sniffing:** Capture **cleartext logins** (FTP, Telnet, HTTP Basic Auth, SMTP); extract **form credentials** from unencrypted POST requests.

- [ ] **Replay Attacks:** Capture valid **authentication tokens, API requests, or RF signals** and retransmit later to bypass time-based controls; works for **garage door openers, payment terminals, VoIP**.

- [ ] **Rogue Access Point / Evil Twin:** Deploy **fake Wi-Fi AP** with legitimate SSID + stronger signal; force users to connect and route all traffic through my box for **MITM harvesting**.

- [ ] **Traffic Injection & Modification:** Inject malicious **JavaScript, HTML, iframes** into unencrypted HTTP responses; modify **DNS responses** to redirect to attacker servers.

---

### Topic 5: Defenses & Mitigation (The Shield) — 🧠 Conceptual

> [!NOTE]
> ⏱️ **Time Bracket: 1 day** — Encryption and VPN (TLS with HSTS preloading: once a browser sees an HSTS header, it will only connect via HTTPS for the preload period — SSL stripping cannot work against HSTS-preloaded domains; certificate pinning adds another layer by rejecting certs not matching the expected key), switch-level protection (Dynamic ARP Inspection: validates ARP packets against a DHCP snooping binding table — defeats ARP spoofing at the switch level; 802.1X NAC: devices must authenticate before getting network access — prevents rogue device connection), network segmentation (VLAN isolation limits ARP spoof blast radius to the VLAN; east-west TLS encryption between internal services defeats sniffing even inside the VLAN), detection (IDS signatures for high ARP packet volume, ettercap process signatures, SSL downgrade alerts; Netflow analysis detects unusual traffic patterns). Deliverable: for each attack in T2-T4, document the specific defense that would have blocked it.


- [ ] **Encryption & VPN:** Force all traffic through **TLS/HTTPS, IPSec VPN, or VPN tunneling**; renders sniffed payloads unreadable; watch for **HSTS, certificate pinning** as anti-bypass measures.

- [ ] **Switch-Level Protection:** **Dynamic ARP Inspection (DAI)**, **DHCP Snooping**, **port security** reject malformed ARP/DHCP; **802.1X authentication** prevents rogue device connection.

- [ ] **Network Segmentation:** **VLAN isolation, micro-segmentation, zero trust** limits sniffing scope per compromised segment; east-west traffic encryption adds extra layers.

- [ ] **Detection Systems:** **IDS/IPS** flag high ARP packet volume, **MITM tools (ettercap signatures)**, SSL downgrade attempts; **Netflow/sFlow** detects unusual traffic patterns.

- [ ] **User Awareness:** Train users to verify **SSL certificates**, recognize **phishing login pages**, and use **password managers** to avoid clipboard paste attacks.

### Lab Progression (Module 23: Sniffing & Spoofing)

| Level | Task | Deliverable |
| ----- | -------------------------------------------------------------------------- | ----------------------------------------- |
| 1 | Capture traffic with Wireshark in a home lab (HTTP, FTP, DNS) | Annotated pcap with credential extraction |
| 2 | Perform ARP spoofing + MITM with [[Bettercap]] in lab | Screenshot of intercepted traffic |
| 3 | Execute DNS spoofing to redirect lab traffic to phishing page | DNS spoof lab report |
| 4 | Perform SSL stripping against a lab web server without HSTS | Before/after traffic comparison |
| 5 | Full MITM chain: ARP spoof → DNS redirect → credential capture | End-to-end MITM lab report |

> [!IMPORTANT]
> **Move-On Gate:** I can perform a complete MITM attack chain in a lab, capture credentials from unencrypted and downgraded traffic, and explain exactly which defenses (DAI, HSTS, certificate pinning) would have prevented each technique.

------

---

## Module 24: Social Engineering

> [!NOTE]
> **📚 Recommended Books for This Part**
> - 🔴 `Social Engineering The Art of Human Hacking` — The definitive book on SE — read this fully during Module 24
> - 🟡 `The Social Engineers Playbook` — Full (short) — practical tactical scripts and pretexts

> **Safety Gate:** Social engineering practice must use consented simulations only. Do not target real people, employers, classmates, public organizations, or family accounts. Unauthorized phishing and impersonation are not "practice"; they are operational and legal exposure.

> [!TIP]
> ⏱️ **Module 24 Total Time Budget: 1 week**
> T0 (psychology foundation): 1–2 days | T1 (intelligence/recon): 1 day | T2 (digital assault): 1–2 days | T3 (human element): 1 day | T4 (physical breach): 1 day | T5 (defense/awareness): 1 day.
> Social engineering is the most underestimated skill in security. The best technical skills mean nothing if an attacker can call your helpdesk and reset a password. Understanding the psychology is equally important for defenders designing awareness programs as it is for attackers designing campaigns.

### Topic 0: The Psychology of Social Engineering (The Foundation) — 🧠 Conceptual

> [!IMPORTANT]
> **Read this before any other Topic in Module 24.** Social engineering is not a collection of clever tricks — it is applied psychology. Every phishing email, vishing call, and pretexting scenario works because it exploits specific, documented cognitive patterns. Understanding these patterns is what separates an operator who succeeds from one who improvises and fails. Defenders must also understand them to design effective awareness training.

> [!TIP]
> **Goal:** Understand the psychological machinery that makes humans predictable under social engineering pressure.

> [!NOTE]
> ⏱️ **Time Bracket: 1–2 days** — Cialdini's 6 principles (Reciprocity, Commitment, Social Proof, Authority, Liking, Scarcity — for each: understand the cognitive mechanism, identify an example phishing scenario that uses it, and write the defender awareness training point that counters it), cognitive biases (Urgency Bias disables System 2 thinking — organizational policy should require verification delays for unusual requests regardless of stated urgency; In-Group Bias means corporate jargon and name-dropping colleagues builds instant trust — LinkedIn/Glassdoor are the primary intel sources), pretext construction methodology (who am I? why am I contacting? what am I asking? why now? what objections arise? — practice a pretext out loud before deployment; a pretext that collapses under follow-up questions was never ready). Deliverable: write one complete pretext for an IT helpdesk vishing scenario — include the five pretext questions answered, the intelligence sources used, and the defensive awareness guidance that defeats it.


**Cialdini's 6 Principles of Influence (The SE Attacker's Toolkit)**

Robert Cialdini's research on influence identified six universal principles that attackers weaponize. Know each one, recognize it in real-world phishing/pretexting scenarios, and understand both the offensive use and the defensive countermeasure:

- [ ] **1. Reciprocity:** People feel obligated to return favors. Attackers exploit this by sending small gifts, providing helpful information, or doing something "nice" before making a request. Example: Attacker sends a "free" IT tool or helps with a minor problem, then requests access credentials as a natural follow-up.
  - _Defensive awareness:_ Question why an unsolicited party is offering help. Favors from unknown parties are often hooks.

- [ ] **2. Commitment & Consistency:** Once a person commits to something (even trivially), they are psychologically compelled to behave consistently with that commitment. Attackers use small initial requests ("Could I confirm my department?") to build toward larger ones. Example: Foot-in-the-door technique — escalating from harmless questions to credential requests.
  - _Defensive awareness:_ Recognizing that I've agreed to small requests from someone does not obligate you to agree to larger, unusual ones.

- [ ] **3. Social Proof:** People look at what others are doing to determine correct behavior, especially in uncertain situations. Attackers fabricate social proof: "Everyone on my team has already verified their account" or "The CISO approved this procedure." Example: Mass-phishing emails claiming widespread adoption of a fake security update.
  - _Defensive awareness:_ Verify claims of "everyone is doing it" through independent channels — not through links or numbers provided by the requester.

- [ ] **4. Authority:** People comply with perceived authority figures — especially in professional environments. Attackers impersonate executives (CEO fraud/BEC), IT helpdesk, auditors, law enforcement, or regulators. Example: "This is John from IT Security. We detected suspicious activity on my account. I need my current password to verify."
  - _Defensive awareness:_ Real authority figures with legitimate needs never require my password. Verify identity through a known, independent channel before complying.

- [ ] **5. Liking:** People are more likely to comply with requests from people they like or who are similar to them. Attackers build rapport, mirror body language, reference shared interests, claim mutual connections, use flattery. Example: LinkedIn profile mining to find shared connections and mention them in a phishing email to build perceived familiarity.
  - _Defensive awareness:_ Likeability is not trust. A pleasant, familiar-seeming contact can be a well-prepared attacker.

- [ ] **6. Scarcity:** Perceived scarcity creates urgency that bypasses rational decision-making. "This offer expires in 10 minutes," "My account will be suspended in 24 hours," "Only I can fix this." Urgency is the primary switch that disables critical thinking. Example: Phishing emails with countdown timers or imminent threat messaging.
  - _Defensive awareness:_ Real systems with legitimate urgency allow time for verification. Artificial urgency is a psychological weapon — slow down when I feel rushed.

---

**Cognitive Biases Exploited in Social Engineering**

- [ ] **Urgency Bias (System 1 Thinking):** Under time pressure, humans switch from deliberate analytical thinking (System 2) to fast, pattern-matching intuition (System 1). Attackers manufacture urgency to prevent System 2 thinking. Countermeasure: Organizations should establish policies that require verification delays for unusual requests regardless of stated urgency.

- [ ] **Authority Bias:** The tendency to trust and obey authority figures. Manifests as compliance with requests from anyone displaying authority markers (uniform, title, confident tone). Particularly effective via email where visual deception is easy.

- [ ] **Familiarity/Exposure Effect:** Mere repeated exposure to a name, brand, or scenario increases trust in it. Attackers send "drip" campaigns — multiple low-pressure contacts before the actual attack — to build familiarity before the high-pressure request.

- [ ] **In-Group Bias:** People are more cooperative with members of their perceived in-group. Attackers research corporate culture, use internal jargon, name-drop colleagues, and reference recent company events to establish perceived membership. LinkedIn, Glassdoor, job postings, and conference agendas are primary intelligence sources for this.

- [ ] **Fear of Negative Consequence:** The threat of something bad happening (job loss, account suspension, legal action, IT lockout) overrides rational verification behavior. Attackers combine authority + scarcity + threat in "warning emails" from fake IT/HR/legal.

---

**Pretext Construction Methodology**

- [ ] **Pretext Definition:** A pretext is a fabricated scenario, identity, and backstory that the attacker uses to justify the unusual request they are making. A strong pretext is internally consistent, draws on real intelligence about the target, and anticipates objections.

- [ ] **Pretext Construction Framework:** A professional pretext must answer five questions before deployment:
  1. **Who am I?** (role, organization, relationship to target)
  2. **Why am I contacting this person?** (plausible reason grounded in reality)
  3. **What am I asking for?** (specific, reasonable-sounding request)
  4. **Why now?** (urgency rationale that doesn't trigger suspicion)
  5. **What objections might arise, and what is my answer?** (anticipate resistance)

- [ ] **Pretext Intelligence Requirements:** A pretext draws from real OSINT:
  - Employee names, titles, reporting structure (LinkedIn, company website)
  - Recent company events, announcements, projects (press releases, social media)
  - Technology stack used (job postings reveal software in use)
  - Corporate language, acronyms, cultural references (Glassdoor, LinkedIn posts)
  - Physical location details (office address, badge vendor, building layout)

- [ ] **Persona Maintenance:** Once deployed, a pretext must be maintained consistently. Common operator failure: deviating from the stated identity under pressure or failing to answer follow-up questions consistently. A strong pretext is rehearsed, not improvised. Practice the pretext scenario out loud before deployment.

- [ ] **Pretext Failure Modes:** Know what causes pretexts to collapse:
  - Using insider jargon incorrectly (calls out external nature)
  - Unable to answer natural follow-up questions
  - Requesting information that the stated role wouldn't need
  - Inconsistency between email domain, phone number, and stated identity
  - Targets who independently verify through official channels (the defense)

---

### Topic 1: Intelligence & Reconnaissance (The Setup) — 🔬 Practical

> [!TIP]
> **Goal:** Know the target better than they know themselves.

> [!NOTE]
> ⏱️ **Time Bracket: 1 day** — Digital recon (LinkedIn: extract org chart, reporting structure, technology keywords from job postings, employee names and emails with format enumeration; GitHub dorking: site:github.com target.com; Hunter.io for email format discovery; Maltego for relationship mapping), physical recon (dumpster diving requires authorization in engagement scope; observe badge access patterns, delivery procedures, physical security posture — document everything with notes, no photos without authorization), domain and infrastructure prep (register typo-squatting domains: dnstwist target.com to enumerate variations; set up GoPhish server with cloned login page — test before using), social media profiling (LinkedIn for professional details, Twitter/X for personal interests and travel, Glassdoor for internal culture and frustrations, GitHub for technical projects and email addresses). Deliverable: produce a complete OSINT profile for a fictional organization including email format, 5+ employee names/roles, technology stack from job postings, and one social media-derived personal detail about an executive.


- [ ] **Digital Recon:** Execute **OSINT** using **Google Dorks, LinkedIn scraping, GitHub dorking** to extract employee names, emails, roles, tech stacks, and company structure.

- [ ] **Physical Recon:** Perform **dumpster diving** to recover **org charts, vendor invoices, sticky notes** with passwords; observe **badge access patterns, delivery procedures**.

- [ ] **Domain & Infrastructure Prep:** Register **typo-squatting domains** (e.g., `companysupport.com`, `company-login.net`) that mimic target portals; prepare **phishing landing pages**.

- [ ] **Social Media Profiling:** Mine **LinkedIn, Twitter, GitHub, Glassdoor** for **personal details, relationships, job changes** to craft personalized lures.

---

### Topic 2: The Digital Assault (Remote Vectors) — 🧠🔬 Mixed

> [!TIP]
> **Goal:** Compromise the target from a distance via electronic channels.

> [!NOTE]
> ⏱️ **Time Bracket: 1–2 days** — GoPhish campaign setup (configure SMTP relay, import target email list from OSINT, clone login page, set tracking pixel, launch campaign, analyze results: open rate, click rate, credential submission rate — all against test inboxes only), DMARC offensive analysis (dig TXT _dmarc.target.com: if absent or p=none, domain can be spoofed; check SPF softfail ~all; test homoglyph domains with dnstwist ––registered; subdomain takeover for mail spoofing via dangling CNAME), ClickFix simulation (design a fake browser error pop-up that instructs the user to paste a command — understand why this bypasses email gateway scanning: the payload is instruction text, not a file), deepfake vishing awareness (ElevenLabs voice cloning exists at consumer pricing; the defense is callback verification through an independent channel — never trust caller ID). Deliverable: run a GoPhish simulation against test inboxes you control, collect results, and write a 1-page phishing campaign analysis report.


- [ ] **Mass Campaign:** Launch **broad phishing campaigns** with generic lures (password resets, package delivery) for large-scale **credential harvesting**.

- [ ] **Executive Targeting:** Execute **whaling attacks** against **C-suite/CFO** using deep **OSINT context** (recent news, personal interests, vendor relationships) to bypass skepticism.

- [ ] **Mobile Vector:** Deploy **SMS phishing (smishing)** with **MFA reset codes, delivery notifications, bank alerts**; use **VoIP/voice phishing (vishing)** to call employees directly.

- [ ] **Watering Hole:** Compromise **industry-specific forums, GitHub repos, or shared tools** to inject **malware/tracking code** that targets specific teams via **drive-by downloads**.

- [ ] **Deepfake Vishing:** Use **voice cloning/video deepfakes** (e.g., ElevenLabs) for **executive impersonation** in calls/meetings.

- [ ] **ClickFix/ClearFake:** Simulate browser/OS errors that instruct users to **copy-paste provided PowerShell/terminal scripts** ("fix/update now").

- [ ] **Email Authentication Bypass (DMARC/DKIM/SPF Offensive):** Understand how to send convincing email as or near a target domain, bypassing authentication controls:
  - **DMARC alignment bypass:** DMARC passes when the From header domain _aligns_ with either the SPF envelope-from or the DKIM signing domain. A target with `p=quarantine` but no subdomain policy (`sp=none`) allows subdomain spoofing — register `mail.target.com` and send from a subdomain not covered by the DMARC policy.
  - **Missing DMARC / weak p=none:** Check with `dig TXT _dmarc.target.com` — if the record is absent or `p=none`, the domain can be directly spoofed without filtering. Use [dmarc.postmarkapp.com](https://dmarc.postmarkapp.com) or `checkdmarc` to scan targets during recon.
  - **Homoglyph domains:** Register visually identical domains using Unicode lookalike characters (e.g., `Ⅰ` for `l`, `а` for `a`). IDN homoglyph attack: `xn--paypl-h2a.com` renders as `payрal.com` in some email clients. Tools: `dnstwist` with `--registered` flag.
  - **Subdomain takeover for mail spoofing:** If a dangling CNAME on a target subdomain points to an unclaimed third-party service (SendGrid, Mailchimp, GitHub Pages), claim the service and send email from that subdomain. It passes SPF and DKIM because it is a legitimate sending service now controlled by you.
  - **Spoofed display names:** Many mail clients show only the display name, not the From address. `"CEO Name <attacker@random.com>"` passes all authentication controls and appears as CEO to a mobile viewer. Combine with similar-looking reply-to addresses.
  - **SPF softfail exploitation:** A `~all` SPF record (softfail) means DMARC still evaluates — but many recipients accept softfail-flagged mail if DMARC is absent or `p=none`.
  - **Defensive counter-reference:** See Stage 3 Side-Track B for the defender-side SPF/DKIM/DMARC configuration and detection.

---

### Topic 3: The Human Element (Direct Interaction) — 🧠 Conceptual

> [!TIP]
> **Goal:** Use psychology and social manipulation to bypass logic.

> [!NOTE]
> ⏱️ **Time Bracket: 1 day** — Voice pretexting (practice your pretext out loud before calling; IT helpdesk impersonation: "Hi, I'm from IT, we detected suspicious activity on your account and need to verify your credentials" — understand which cognitive triggers this uses: authority + urgency + fear; record yourself and critique the delivery), authority and compliance trigger (people comply faster when the requester has plausible authority markers: title, confident tone, domain-specific jargon — a pretext that uses insider language is 3x more effective than a generic one), reciprocity and obligation (provide small value first: "I helped you reset your last ticket" or "I sent you the documentation you needed" — then request the favor). Deliverable: script a complete vishing pretext for an IT password reset scenario and write the awareness training that would defeat it.


- [ ] **Voice Pretexting:** Call as **IT support, HR, vendor, auditor, law enforcement** using social engineering pretexts; use **authority, urgency, fear** to bypass critical thinking.

- [ ] **Authority & Compliance Trigger:** Leverage **IT/Security/Auditor/Legal persona** to demand compliance; abuse **helpfulness bias** to force password resets or system access.

- [ ] **Reciprocity & Obligation:** Provide small **favors (tech help, free tools)** to create sense of obligation; ask for credentials or access in return.

---

### Topic 4: The Physical Breach (Boots on the Ground) — 🧠🔬 Mixed

> [!TIP]
> **Goal:** Gain physical access to networks and facilities.

> [!NOTE]
> ⏱️ **Time Bracket: 1 day** — Tailgating (authorized employee follow-through using a large box or coffee cup trick; observe office security culture during pre-engagement recon — high-security offices have mantrap airlocks that prevent tailgating regardless of social skills), shoulder surfing (PIN observation at ATMs and key pads; screen reading in open office environments; defense is privacy screen filters and behavioral awareness), badge cloning (Proxmark3 reads HID/EM4100 RFID at close range — requires physical proximity; Flipper Zero for similar at shorter range — note this is hardware-dependent), physical device placement (USB drop: rubber ducky or bash bunny triggers on connection; rogue AP: nano WiFi router hidden under a desk; hardware keylogger: inline USB device between keyboard and computer). Deliverable: for each physical attack vector, document the specific physical security control that prevents it and how you would test for that control in a physical pentest scope.


- [ ] **Tailgating:** Follow **authorized employees** into secure zones using badges/access cards; use **coffee cup hold, uniform/vendor persona** to bypass visual checks.

- [ ] **Shoulder Surfing:** Observe **PIN entry, password typing, screen content** in public spaces (airports, coffee shops, open offices) to capture credentials.

- [ ] **Badge Cloning:** Capture **RFID badge data** using **Proxmark3, ACR122U** and clone to malicious card; bypass **magnetic stripe readers** via cloning.

- [ ] **Physical Device Placement:** Plant **USB drops, rogue access points, hardware keyloggers** in common areas for **auto-execution** when connected by unsuspecting users.

---

### Topic 5: Defense & Awareness (The Shield) — 🧠 Conceptual

> [!TIP]
> **Goal:** Prevent the human hack through training and controls.

> [!NOTE]
> ⏱️ **Time Bracket: 1 day** — Authentication (FIDO2/Passkeys are phishing-resistant because the credential is cryptographically bound to the origin domain — a fake site cannot receive a FIDO2 response; SMS and push OTP MFA are phishable via real-time MITM proxy like Evilginx; MFA fatigue: send 50+ push notifications until user approves from frustration — mitigation is number matching), verification protocols (callback through an independent channel: look up the number yourself, do not call back a number provided by the caller — this single control defeats most vishing), physical security (no-tailgating + mantrap airlocks; visitor escort policy; clean desk policy — sticky notes with passwords are not a joke finding), security awareness training (simulated phishing with GoPhish; immediate feedback loop: if you clicked, you see training content immediately; reward reporting culture: users who report suspicious emails should get recognition, not punishment). Deliverable: design a 1-hour security awareness training module covering Cialdini's 6 principles with one example scenario per principle and one countermeasure.


- [ ] **Authentication:** Enforce **MFA/2FA** (TOTP, hardware keys, push notifications) so password compromise alone doesn't grant access; watch for **MFA fatigue attacks**.

- [ ] **Verification Protocols:** Train staff to **challenge unknown callers** via **secondary channel callback**; never trust caller ID alone; verify requests through official channels.

- [ ] **Physical Security:** Enforce **no-tailgating policies, visitor escorts, badge display requirements, clean desk policies** to prevent **dumpster diving and shoulder surfing**.

- [ ] **Security Awareness:** Regular **phishing simulations, red team testing, security training** to build **skepticism and reporting culture**; reward **security-first behavior**.

- [ ] **MFA Resilience:** Teach differences between **phishing-resistant MFA (FIDO2/Passkeys)** vs **phishable MFA (SMS/Push/OTP)**; test and mitigate **MFA fatigue** scenarios.

### Lab Progression (Module 24: Social Engineering)

> [!TIP]
> **Goal:** Learn social engineering defensively and ethically.

- [ ] **Email Authentication Lab:** Configure and validate SPF, DKIM, and DMARC on a test domain or lab mail stack.
- [ ] **Header Forensics Lab:** Analyze benign/phishing email headers and identify sender path, SPF/DKIM/DMARC result, and suspicious infrastructure.
- [ ] **[[GoPhish]] Simulation Lab:** Run a consented internal lab campaign against test inboxes only; measure open/click/report rates.
- [ ] **Pretext Review:** Write three pretexts and then write the defensive awareness guidance that would defeat them.
  > [!IMPORTANT]
  > **Move-On Gate:** Produce a social-engineering simulation plan with ROE, consent model, metrics, and debrief template.

---

---

## Module 25: Malware & Weaponization (Conceptual)

> **Safety Gate:** Malware work is restricted to isolated local labs with snapshots, host-only networking, no shared clipboard, no mounted host folders, and no third-party targets. Before running any sample or payload, define expected behavior, logging sources, rollback steps, and containment checks.

> [!NOTE]
> **Scope of This Module — Read Carefully:** Module 25 teaches malware as a **survey course**, not an implementation course. At this stage I have not yet studied low-level malware engineering at the binary level — that knowledge is built in Stage 5 (Module 27: Offensive Development) and Shelf 05 (Reverse Engineering). Without that foundation, any implant written would be an unmaintainable artifact.
> **What IS covered here (practitioner-level):**
> - Malware taxonomy and attack lifecycle (categories, architecture decisions, C2 design thinking)
> - Tool-based weaponization: `msfvenom`, Metasploit payload generation, framework-managed C2 (Sliver, Mythic)
> - How AV/EDR detects malware conceptually (signature, heuristic, behavioral scanning)
> - Document and cloud delivery vectors — the initial access tradecraft that red teamers use operationally
> **What Topics 2–5 teach (exposure-level, not implementation-level):**
> Topics 2, 3, 4, and 5 describe techniques — shellcode injection, EDR bypass, anti-forensics — at the conceptual level. They are not implementation labs. When seeing those topics: understand the concept, understand what defenders see, and move on. Do **not** attempt custom binary implant development until completing **Stage 5: Module 27 (Offensive Development & Tooling)**.
> **Why this sequencing matters:** The correct sequence is: _understand the attack here (Module 25) → understand binaries and malware internals (Shelf 05) → build custom tooling (Stage 5 Module 27)._

> [!TIP]
> ⏱️ **Module 25 Total Time Budget: 1 week** — exposure/awareness track; no live malware deliverables at this stage
> T1 (design/architecture): 1 day | T2 (payload/mechanism survey): 1 day | T3 (evasion/defense bypass survey): 1 day | T4 (persistence/escalation survey): 1 day | T5 (counter-forensics survey): 1 day | T5b (Windows persistence/memory forensics): 1 day | T6 (document/cloud weaponization): 1–2 days.
> This module is where you build threat actor empathy — you learn to think like an implant designer without actually building one yet. The operational techniques in T6 (HTML smuggling, weaponized OneNote, Sliver C2) are the exception: these are in-scope for lab practice now.

### Topic 1: The Design & Logic (Architecture) — 🧠 Conceptual

> [!TIP]
> **Goal:** Understand how malware is architected at a design level — the decisions an attacker makes before writing a single line of code.

> [!NOTE]
> ⏱️ **Time Bracket: 1 day** — CIA Triad targeting (Confidentiality: RAT/spyware/credential harvester; Integrity: wiper/data corruptor; Availability: ransomware/DDoS bot — objective drives every architecture decision), malware taxonomy (dropper fetches and executes; loader unpacks and maps; stager fetches full payload at runtime; RAT provides remote access; rootkit hides presence; ransomware encrypts and demands; infostealer harvests credentials/cookies; botnet agent accepts commands from C2 — know which category serves which attack lifecycle phase), C2 protocol selection (HTTP/S beaconing: looks like normal web traffic, most common; DNS tunneling: hard to block without breaking DNS; ICMP covert channel: low-bandwidth, often ignored by firewalls; SaaS API abuse: C2 over Slack/Telegram/GitHub issues — very hard to block without banning legitimate services), Kill Chain mapping (map a hypothetical ransomware campaign from Recon through Impact using MITRE ATT&CK, one technique per phase). Deliverable: map a complete ransomware kill chain to MITRE ATT&CK with one specific technique per tactic phase.


- [ ] **Target the CIA Triad:** Define the malware's objective — does it attack **Confidentiality** (RAT, spyware, credential harvester), **Integrity** (wiper, data corruption), or **Availability** (ransomware, DDoS bot)? The objective drives every architectural decision.

- [ ] **Malware Taxonomy:** Understand the full taxonomy — **dropper, loader, stager, RAT, rootkit, worm, ransomware, wiper, infostealer, spyware, adware, botnet agent** — and how each category relates to the attack lifecycle phase it serves.

- [ ] **C2 Protocol Selection:** Understand the trade-offs between **HTTP/S beaconing, DNS tunneling, ICMP covert channels, and legitimate SaaS API abuse** — not to implement them at this stage, but to understand why attackers choose one over another based on network visibility risk. Implementation comes in Stage 5: Module 27.

- [ ] **Persistence Architecture:** Survey the persistence mechanisms available — **registry run keys, scheduled tasks, WMI subscriptions, DLL hijacking, boot sector** — understand their detection footprint differences conceptually. Implementation and lab practice comes in Module 13 (System Hacking) and Stage 5: Module 27.

- [ ] **Kill Chain Mapping:** Use the **Cyber Kill Chain** or **MITRE ATT&CK** to map a hypothetical malware campaign from **Reconnaissance → Weaponization → Delivery → Exploitation → Installation → C2 → Actions on Objectives**. This mapping exercise trains my mind to think like an attacker planning a campaign, not just using a tool.

- [ ] **Diamond Model:** Apply the **Diamond Model** to a real APT's malware — adversary, capability, infrastructure, victim — to understand why the same malware capability looks different depending on the targeted victim sector.

---

### Topic 2: The Payload & Mechanism — Exposure Survey — 🧠🔬 Mixed

> [!WARNING]
> **Exposure-Only Stage:** This topic describes weaponization techniques at a conceptual level. Do not attempt to implement custom payloads, shellcode injection, or custom C2 until completing **Stage 5: Module 27 (Offensive Development & Tooling)** and **Shelf 05 (Reverse Engineering)**. My goal here is to understand _what_ these techniques do and _why_ defenders flag them — not to build them.

> [!TIP]
> **Goal:** Understand how payloads execute and what defenders detect at each stage.

> [!NOTE]
> ⏱️ **Time Bracket: 1 day** — Memory-based execution concepts (shellcode injection: code written into another process memory and executed; process hollowing: legitimate process created suspended, memory replaced with malicious payload; DLL injection: DLL loaded into target process address space — conceptual understanding only; implementation in Stage 5 Module 27), delivery vectors (phishing: user opens attachment/clicks link; drive-by download: visiting a page triggers exploit of browser/plugin; watering hole: compromise a site the target regularly visits; supply chain: malicious package in a dependency), msfvenom stageless vs staged comparison (msfvenom -p windows/x64/meterpreter_reverse_tcp for stageless; msfvenom -p windows/x64/meterpreter/reverse_tcp for staged — compare file sizes and VirusTotal detection rates; record which engines trigger and whether signature or heuristic), Sliver/Mythic C2 deployment (deploy in lab, generate implant, establish callback, tune sleep/jitter to observe how beacon timing affects traffic analysis). Deliverable: generate stageless and staged msfvenom payloads, compare VirusTotal detection rates, document findings.


- [ ] **Memory-Based Execution:** Understand that attackers inject code into running processes (shellcode injection, process hollowing, DLL injection) to avoid writing to disk and evade file-scanning AV. _Conceptual understanding only — implementation in Stage 5: Module 27._

- [ ] **Delivery Vectors:** Understand **phishing, drive-by download, watering hole, and supply chain injection** as the four primary delivery mechanisms; know what each one requires from the attacker and what it looks like to defenders. _Practical delivery lab in Stage 6 (document weaponization) below._

- [ ] **Staged Payload Architecture:** Understand the difference between **stageless** (one-shot complete payload) and **staged** (stager fetches the full payload at runtime) delivery — know why staged reduces initial payload size but requires an active C2 listener. Use `msfvenom` to generate both and compare their byte sizes and detection rates against VirusTotal (educational only — never upload customer/lab-specific payloads).

- [ ] **Framework-Managed C2:** Deploy **[[Sliver]]** or **Mythic** in my lab, generate an implant, and establish a callback — understand listener configuration, sleep/jitter tuning, and how traffic patterns affect detection. This is the operational-tool-based weaponization that is in scope at this stage.

> **🔬 Observation Lab (Stage 2):** Run EICAR test file (`https://www.eicar.org/download/eicar.com`) through VirusTotal and note detection rate. Then generate an msfvenom stageless payload (`msfvenom -p windows/x64/meterpreter_reverse_tcp LHOST=127.0.0.1 LPORT=4444 -f exe -o stageless.exe`) and a staged payload (`msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=127.0.0.1 LPORT=4444 -f exe -o staged.exe`). Compare: (1) file sizes, (2) VirusTotal detection rates for both. Record which AV engines flag them and whether detections are signature-based or heuristic. Never execute either payload outside a controlled lab VM with no network access.

---

### Topic 3: Evasion & Defense Bypassing — Exposure Survey — 🧠 Conceptual

> [!WARNING]
> **Exposure-Only Stage:** This stage teaches _how_ AMSI bypass, EDR hook removal, and memory-based evasion work at a conceptual level. Do not attempt to implement these at this stage. Custom evasion requires understanding the Windows internals that these techniques exploit — that knowledge is in **Shelf 05 (Reverse Engineering)**. Practical evasion implementation is in **Stage 5: Module 27 (Offensive Development & Tooling)**.

> [!TIP]
> **Goal:** Understand how the defensive stack detects malware and what attackers do to evade each layer.

> [!NOTE]
> ⏱️ **Time Bracket: 1 day** — Static analysis evasion concepts (AV signature: matches byte patterns — changing the binary via packing, encoding, or obfuscation defeats it; implementing a custom packer requires PE format knowledge from Shelf 05), sandbox detection concepts (VM artifact detection: low CPU count, no mouse movement, VMware driver names in registry; sandboxes run samples for a short window — attacker sleeps longer than sandbox timeout), EDR userland hooking bypass concepts (EDR hooks NtWriteVirtualMemory and similar NTAPI functions in ntdll.dll; direct syscall bypasses the hook; unhooking involves restoring the original bytes — implementation in Stage 5 Module 27), memory-based evasion concepts (sleep obfuscation XORs beacon memory during sleep to avoid memory scanner detection; indirect syscalls and call stack spoofing hide the true call origin). Observation lab: run Procmon and compare normal vs encoded PowerShell invocation — document ScriptBlock Logging Event ID 4104 output for each.


> **Prerequisite Context:** This stage references AMSI, EDR, and ETW. Those systems are covered from the defender's perspective in **Stage 3 Side-Track A (Detection Engineering)**. If I have not completed Stage 3 yet, review those topics before studying evasion — evasion without understanding the detection model is guesswork.

- [ ] **Static Analysis Evasion:** Understand that AV signature detection works by matching known byte patterns — attackers evade it by changing the binary (packing, encoding, obfuscation). Know _that_ this works conceptually; implementing a custom packer requires PE format knowledge from Shelf 05 (Reverse Engineering).

- [ ] **Sandbox Detection:** Understand that sandboxes run samples in controlled VMs — attackers detect this by checking for VM artifacts (driver names, low CPU count, no mouse movement), then go dormant. Know the technique; study the implementation in Shelf 05 (Reverse Engineering).

- [ ] **EDR Userland Hooking Bypass:** Understand that EDR products hook Windows API functions at userland to intercept suspicious calls — attackers bypass this by calling syscalls directly or by unhooking. _Conceptual understanding only — syscall implementation in Stage 5: Module 27._

- [ ] **Memory-Based Evasion Concepts:** Understand _what_ sleep obfuscation, call stack spoofing, and indirect syscalls do — each is a technique that makes a beacon harder to detect during memory scanning. Implementation and lab practice in Stage 5: Module 27.

> **🔬 Observation Lab (Stage 3):** In a Windows sandbox VM: (1) Run `Procmon` (Sysinternals), filter on `powershell.exe`. Execute `powershell -Command "Write-Host hello"` and observe the API calls. Now run `powershell -EncodedCommand` with a base64-encoded version of the same command. Compare the Procmon output — same result, different invocation path. This is the "encoded = suspicious" detection signal that AMSI catches. Document what `ScriptBlock Logging` Event ID 4104 shows for each.

---

### Topic 4: Persistence & Escalation — Exposure Survey — 🧠 Conceptual

> [!WARNING]
> **Exposure-Only Stage:** Persistence mechanisms and privilege escalation are taught as canonical practitioner skills in **Stage 2: Module 13 (System Hacking)** already. This stage reviews them in the context of malware architecture — what a long-running implant uses to survive reboots and credential rotations. Rootkit-level persistence (BOOTKIT, UEFI implants, kernel drivers) requires kernel internals knowledge from Stage 5 / Shelf 05. Do not attempt rootkit implementation at this stage.

> [!TIP]
> **Goal:** Understand what persistence mechanisms a malware implant uses and why each has a different detection footprint.

> [!NOTE]
> ⏱️ **Time Bracket: 1 day** — Userland persistence review (registry Run keys: HKCU and HKLM CurrentVersion Run — Event ID 4657 on registry write, Sysmon Event ID 13; scheduled tasks: Event ID 4698 on creation, schtasks /query to enumerate; WMI subscriptions: EventFilter + CommandLineEventConsumer + FilterToConsumerBinding — no file write if fileless WMI, Sysmon Event ID 19/20/21; DLL hijacking: process loads DLL from writable path before legitimate location — Sysmon Event ID 7; Startup folder: Sysmon Event ID 11 on file creation), privileged persistence concepts (kernel drivers require code signing; UEFI implants survive OS reinstall; recognize their artifacts via secure boot attestation and TPM measurement), defense disabling concepts (SYSTEM-level processes can terminate EDR services or disable tamper protection — recognizing this behavior in event logs is the skill to acquire). Observation lab: create scheduled task, find Event ID 106, document detection artifacts.


- [ ] **Userland Persistence Review:** Map the common mechanisms — **registry run keys, scheduled tasks, WMI subscriptions, DLL search order hijacking, Startup folder, COM object hijacking** — to their Windows Event Log artifacts (which Event IDs indicate each mechanism was set). This is the defender-aware review; I practiced them in Module 13.

- [ ] **Privileged Persistence Concepts:** Understand that kernel-level and UEFI-level persistence (bootkits, driver implants) exist and require privileged access plus deep OS internals knowledge — covered in Shelf 05 and Shelf 20/21. Recognizing their artifacts is the skill to acquire here.

- [ ] **Defense Disabling (Conceptual):** Understand that advanced malware terminates AV/EDR processes or disables tamper protection when running as SYSTEM — recognizing this behavior in logs is the defender-relevant skill; the implementation is in Stage 5: Module 27.

> **🔬 Observation Lab (Stage 4):** In a Windows sandbox VM with Sysmon installed: (1) Create a scheduled task with `schtasks /create /sc onlogon /tn "Updater" /tr "calc.exe"`. (2) Open Event Viewer → Applications and Services Logs → Microsoft → Windows → TaskScheduler → Operational. Find the task creation event (Event ID 106). Document: what the event records, what fields an analyst would use to detect malicious scheduled tasks, and what `HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` looks like in Autoruns. Delete the task when done.

---

### Topic 5: Counter-Forensics & Cleanup — Exposure Survey — 🧠 Conceptual

> [!WARNING]
> **Exposure-Only Stage:** Anti-forensics (log manipulation, timestamp modification, artifact scrubbing) are covered conceptually here. Implementing effective anti-forensics requires understanding _what_ forensic artifacts exist — that knowledge is in **Shelf 04 (Digital Forensics)**. The skill to develop here is recognizing what evidence an attacker would try to destroy, so I can look for its _absence_ during an investigation. Operationally, within a legitimate red team engagement, artifact cleanup must stay within Rules of Engagement and must never destroy evidence on production systems.

> [!TIP]
> **Goal:** Understand what artifacts malware and operators leave behind, and what attackers do to reduce their forensic footprint.

> [!NOTE]
> ⏱️ **Time Bracket: 1 day** — Windows artifact landscape (Event Logs, Prefetch files, Shimcache, Amcache, LNK files, MFT records, browser history, registry hives — understand which survive a reboot, a log clear, and a disk wipe), log manipulation awareness (wevtutil cl Security clears the log but generates Event ID 1102 — the clearing event itself is the evidence; SIEMs receive log forwarding before clearing — local log clearing after SIEM ingestion accomplishes nothing), anti-forensics counter-detection (write-protect plus Volatility for memory forensics; SIEM forwarding makes local clearing irrelevant; EDR telemetry bypasses local log clearing; network forensic reconstruction from PCAP survives host-side cleanup), ROE compliance (never destroy production data regardless of privilege; log cleanup is explicitly scoped in the RoE before the engagement starts). Observation lab: run wevtutil cl Security, find Event ID 1102, document what a defender reviewing logs 5 minutes later would still find.


- [ ] **Windows Artifact Landscape:** Know the key artifacts that survive after an attack — **Windows Event Logs, Prefetch files, Shimcache, Amcache, LNK files, MFT records, browser history, $MFT journal, registry hives** — and understand which artifacts survives a reboot, a log clear, or a disk wipe.

- [ ] **Log Manipulation Awareness:** Understand that attackers clear Event Logs using `wevtutil cl System` and that this clearing _itself_ generates Event ID 1102 (Security log cleared) — defenders look for the clearing event, not just empty logs. Also understand that SIEMs receive log forwarding — clearing local logs after a SIEM has already ingested them accomplishes nothing.

- [ ] **Anti-Forensics Counter-Detection:** Know the defender techniques that defeat anti-forensics: **Write-Protect + Memory Forensics (Volatility)**, **SIEM log forwarding**, **EDR telemetry that bypasses local log clearing**, **backup snapshot retention**, and **network forensic reconstruction from PCAP**.

- [ ] **ROE Compliance:** In a red team engagement, anti-forensics and log cleanup are controlled by Rules of Engagement — know exactly what my RoE permits before touching any log or artifact, and never destroy data on production systems regardless of privilege level.

> **🔬 Observation Lab (Stage 5):** In a Windows sandbox VM: (1) Run `wevtutil cl Security` to clear the Security event log. Open Event Viewer and confirm the log is empty. Now check the same Security log — observe Event ID 1102 ("The audit log was cleared"). (2) Open PowerShell history file (`%APPDATA%\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt`) and note what is logged. Delete one entry manually — run `Get-History` in a new session and compare. Document: which artifacts survived the clearance attempt and what a defender reviewing logs 5 minutes after the clear would still find.

---

### Topic 5b: Windows Persistence Analysis & Memory Forensics — 🧠 Conceptual

> [!NOTE]
> **Scope:** This is a conceptual exposure pass — you learn what the techniques are and what artifacts they leave so I can identify them on an engagement or in a blue-team investigation. Deep Volatility memory analysis and advanced rootkit internals are covered post-hire in Shelf S21 (Advanced Windows Internals).

> [!TIP]
> **Goal:** Know every common Windows persistence location an attacker would use, the forensic artifact each produces, and the Volatility plugin or Sysinternals tool that surfaces it.

**Windows Persistence Mechanisms (with detection artifacts):**

- [ ] **Registry Run Keys:** `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`, `HKLM\...\Run`, `RunOnce`, `RunServices`. Detection: Autoruns.exe (Sysinternals), reg query output, Sysmon Event ID 13 (registry value set), Windows Event 4657.

- [ ] **Scheduled Tasks:** `schtasks /create` or via Task Scheduler XML dropped to `C:\Windows\System32\Tasks\`. Detection: `schtasks /query /fo LIST /v`, Sysmon Event ID 1 (process create), Windows Event ID 4698 (scheduled task created), 4702 (modified).

- [ ] **Windows Services:** `sc create EvilSvc binPath= "C:\backdoor.exe" start= auto`. Detection: `sc query`, Windows Event ID 7045 (new service installed), 4688 (process created with SYSTEM token from service).

- [ ] **DLL Search Order Hijacking (Persistence variant):** Place a malicious DLL in a directory searched before the legitimate DLL location for a service/application that auto-starts. Detection: Process Monitor (DLL load events), Sysmon Event ID 7 (image loaded), comparing DLL path against known-good baselines.

- [ ] **WMI Event Subscriptions:** Create `__EventFilter` + `CommandLineEventConsumer` + `__FilterToConsumerBinding` — survives reboots, no registry or file drop required if using "fileless" WMI subscriptions. Detection: `Get-WMIObject -Namespace root\subscription -Class __EventFilter`, Sysmon Event ID 19/20/21 (WMI activity), Windows Event 5861.

- [ ] **Startup Folder Persistence:** Drop a LNK or executable into `C:\Users\<user>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup` or the system-wide equivalent. Detection: Autoruns, directory listing with timestamps, Sysmon Event ID 11 (file created).

- [ ] **Boot/Pre-OS Persistence:** Awareness only — bootkit, MBR/VBR overwrites, UEFI implants. Not lab-practiced at this stage. Detect via: offline bootable scanner, Secure Boot attestation, TPM measurement comparison.

**Windows Memory Forensics (Conceptual — Volatility awareness):**

- [ ] **Why Memory Forensics:** Many advanced threats (fileless malware, in-memory shellcode, process injection) leave minimal or no disk artifacts. Memory forensics captures the running state: process list, network connections, injected code, decrypted credentials, and encryption keys that never touch disk.

- [ ] **Key Volatility 3 Plugins to know:**
  - `windows.pslist` / `windows.pstree` — list running processes and their parent/child relationships; look for orphaned processes or unusual parent-child pairs (e.g., `Word.exe` spawning `cmd.exe`)
  - `windows.cmdline` — show command-line arguments for each process; reveals powershell `-EncodedCommand` or suspicious flags
  - `windows.netscan` — active and recently closed network connections from memory; catches C2 callbacks that are not in `netstat` anymore
  - `windows.dlllist` — DLLs loaded per process; look for DLLs loaded from `%TEMP%`, `%APPDATA%`, or unusual paths
  - `windows.malfind` — scan process memory for regions that are `PAGE_EXECUTE_READWRITE` and contain PE headers or shellcode signatures — primary plugin for detecting injected shellcode
  - `windows.handles` — open handles per process; reveals processes holding handles to suspicious files, registry keys, or mutexes
  - `windows.dumpfiles` / `windows.procdump` — extract files and process executables from memory for static analysis

- [ ] **Memory Acquisition:** Understand the difference between live acquisition (`winpmem`, `DumpIt`, `RAMMap`) vs. crash dump (`%SystemRoot%\MEMORY.DMP`) vs. hibernation file (`hiberfil.sys`). Know that `hiberfil.sys` and `pagefile.sys` contain memory artifacts even without a live acquisition tool.

- [ ] **Lab (Conceptual):** Download a pre-made memory image from [MemLabs](https://github.com/stuxnet999/MemLabs) or [Volatility Foundation samples](https://github.com/volatilityfoundation/volatility/wiki/Memory-Samples). Run `windows.pslist`, `windows.malfind`, and `windows.netscan` on it. Document what looks suspicious and why. This is awareness-level — I am learning to read the output, not yet building full DFIR investigation workflows (that is Shelf S04 / Stage-5 parallel).

---

### Topic 6: Document & Cloud Weaponization — 🔬 Practical

> [!TIP]
> **Goal:** Weaponize documents, email clients, and cloud services for initial access, persistence, and exfiltration. This is the **operational implementation topic** for Module 25 — the techniques here are in-scope for lab practice because they use documented attack patterns that do not require binary internals knowledge.

> [!NOTE]
> ⏱️ **Time Bracket: 1–2 days** — HTML smuggling (build an HTML file using Blob API and createObjectURL to reconstruct a payload inside the browser; test that standard email gateway file-type scanning does not flag it; this is the current primary delivery vector in many red team engagements), OneNote/PDF/ISO weaponization (embed a script in a OneNote page triggered by user click; ISO plus LNK plus script to bypass MOTW on unpatched Windows; understand the October 2022 MOTW patch status), Browser-in-the-Browser BitB attack (build a fake browser pop-up inside a legitimate page mimicking an SSO login dialog — no code execution needed, direct credential harvest), OAuth consent phishing (register a malicious Entra app, send consent link to test user, harvest refresh token with Mail.Read scope), cloud storage exfil (upload dummy data to Dropbox or OneDrive via API with a service account token — understand what CASB/DLP controls detect this vs miss). Deliverable: build an HTML smuggler that delivers an EICAR test file through a simulated email gateway and document the evasion mechanism.


> **Prerequisite:** Complete Module 13 (System Hacking), Module 23 (Sniffing & Spoofing), and Module 24 (Social Engineering) before this topic.

**Office & Document Exploits:**

- [ ] **VBA & XLM 4.0 Macros (Legacy — Declining):** Understand VBA macro payload construction and template injection (`remote DOTM`) — note that **Microsoft's February 2022 change blocks VBA macros from internet-sourced Office files by default** across Office 365 and 2019/2021. Macro-based delivery is now uncommon in phishing campaigns without specific user interaction (Enable Content prompt). Know the technique; prioritize modern alternatives below.

- [ ] **HTML Smuggling (Current Primary Vector):** Build HTML files that use the **`Blob` API and `createObjectURL`** to reconstruct a payload inside the browser, bypassing email gateway and web proxy file-type scanning. HTML smuggling now accounts for a significant proportion of red team initial access because attachments are not downloaded — they are assembled client-side. Practice building a minimal smuggler that delivers an EXE or ZIP without triggering gateway inspection.

- [ ] **OneNote/PDF/Embedded Files (Current Vector):** Weaponize **OneNote pages** (`.one` files with embedded scripts triggered by click), **PDF JavaScript** for opener execution, and **ISO/IMG container files** that bypass MOTW (Mark of the Web) on older Windows builds. Understand the **MOTW bypass path** (ISO → LNK → Script) and why Microsoft's October 2022 patches partially closed it.

- [ ] **DDE & Template Abuse:** Trigger code via **DDEAUTO**, external DOTM template injection, and **Follina-style** (`CVE-2022-30190`) URL template fetch — understand the patch status of each and what still fires in unpatched environments.

- [ ] **Browser-in-the-Browser (BitB) Attacks:** Build a **fake browser pop-up window** inside a legitimate page that mimics an SSO login dialog — bypasses awareness training because the URL displayed looks authentic. No code execution required; credentials are harvested directly.

**Email Client Abuse:**

- [ ] **Outlook Rules & Forms:** Create **client-side rules** for auto-forwarding/persistence and malicious **custom forms/add-ins**.

- [ ] **MAPI/Extended MAPI:** Leverage **Redemption/Outlook interop** for covert access and exfil.

**Cloud & SaaS Persistence:**

- [ ] **OAuth Consent Phishing:** Steal **refresh tokens** via malicious app registration; understand **scopes** and consent screens. _(See also Module 17: API Security and Module 19: Entra ID for deeper OAuth coverage.)_

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

### Lab Progression (Module 25: Malware & Weaponization)

| Level | Task | Deliverable |
| ----- | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| 1 | Generate 5 payload types with `msfvenom` (staged + stageless, EXE/DLL/PS1/ELF) and compare detection rates | VirusTotal screenshots + payload comparison report |
| 2 | Deploy Sliver or Mythic in my lab, generate an implant, establish callback, and configure sleep/jitter | C2 lab setup guide + beacon screenshot |
| 3 | Build an HTML smuggler that delivers a test payload (EICAR) through a simulated email gateway | HTML smuggler code + gateway bypass evidence |
| 4 | Weaponize a OneNote file with an embedded script that calls back to my Sliver listener | Weaponized `.one` file + callback screenshot |
| 5 | Map my lab campaign to MITRE ATT&CK — from delivery through C2 establishment | ATT&CK navigator layer JSON + technique annotations |

> [!IMPORTANT]
> **Move-On Gate (Module 25):** I can explain the malware taxonomy and choose the correct category for a given attack objective; generate payloads using `msfvenom` and a C2 framework; understand conceptually how Stages 2–5 techniques work and what defenders detect; deliver a weaponized document in a lab environment; and map a simulated campaign to MITRE ATT&CK. I am not expected to implement custom implants, PE packers, or EDR bypass code at this stage — that comes in Shelf 05 and Stage 5: Module 27.

---

---

## Module 26: Pentest Methodologies & Report Writing

> [!NOTE]
> **📚 Recommended Books for This Part**
> - 🔴 `The Pentester Blueprint` — 🥇 Full book — pentest career methodology, report writing, and professional conduct; read fully before starting Module 26
> - 🔴 `From Hacking to Report Writing` — Full — report structure, evidence packaging, and finding articulation
> - 🟢 `Web Application Pentest Methodology` — Reference — structured methodology for web pentest engagements

> **Why This Exists:** Knowing how to exploit is useless if I can't structure an engagement professionally or communicate findings in a way that drives remediation. This part covers the "how to operate" layer that transforms technical skills into a professional practice. While its reporting templates (PTES, CVSS v3.1/v4.0, remediation matrices) are introduced in Stage 2 for documenting my first rooted lab machines, here in Stage 4 (Module 26) I master the end-to-end commercial engagement lifecycle: formal legal scoping, threat modeling, executive debriefing, and enterprise deliverable packaging.

> [!TIP]
> ⏱️ **Module 26 Total Time Budget: 1 week**
> T1 (frameworks): 1 day | T2 (scoping/legal/engagement management): 1 day | T3 (threat modeling): 1 day | T4 (vuln scoring/risk): 1 day | T5 (report writing): 2–3 days.
> Reporting is the skill that separates consultants who get hired again from ones who do not. A technically perfect pentest with a vague report drives zero remediation. Master the executive summary — a CFO should understand your top 3 risks after reading 1 page.

### Topic 1: Industry-Standard Engagement Frameworks — 🧠 Conceptual

> [!TIP]
> **Goal:** Understand the structured methodologies that govern professional engagements.

> [!NOTE]
> ⏱️ **Time Bracket: 1 day** — PTES (7 phases: Pre-Engagement Interactions → Intelligence Gathering → Threat Modeling → Vulnerability Research → Exploitation → Post-Exploitation → Reporting; know what deliverables each phase produces and why skipping one breaks engagement quality), OWASP WSTG (test case IDs: WSTG-INFO-001 through WSTG-BUSL-009; map every web finding to a WSTG ID for compliance credibility), NIST SP 800-115 (federal methodology: examination, identification, validation; required for US government and regulated-industry engagements), OWASP MASTG (mobile: MASTG test cases for Android/iOS; MAS Checklist for compliance-grade mobile audits; MASVS security requirements), methodology selection (PTES for comprehensive red team, NIST 800-115 for compliance, OWASP WSTG for web-focused, MASTG for mobile — document selection in every report). Deliverable: create a methodology selection decision tree that maps engagement type to the correct framework with rationale.


- [ ] **PTES (Penetration Testing Execution Standard):** Master all **7 phases** — Pre-Engagement Interactions, Intelligence Gathering, Threat Modeling, Vulnerability Research, Exploitation, Post-Exploitation, Reporting; know what deliverables each phase produces and why skipping a phase breaks engagement quality.

- [ ] **OWASP Web Security Testing Guide (WSTG v4.x):** Use the **WSTG test case IDs** (WSTG-INFO-001 → WSTG-BUSL-009) as a structured web assessment checklist; map every finding to a WSTG ID for client-facing credibility and compliance evidence.

- [ ] **NIST SP 800-115 (Technical Guide to Information Security Testing):** Understand the federal-grade methodology covering **examination, identification, and validation techniques**; required knowledge for US government and regulated-industry engagements.

- [ ] **OWASP MASTG (Mobile Application Security Testing Guide):** Apply dedicated **MASTG test cases** for Android/iOS assessments; use the **MAS Checklist** for compliance-grade mobile audits; map findings to MASVS security requirements.

- [ ] **OSSTMM (Open Source Security Testing Methodology Manual):** Understand the **RAV (Risk Assessment Value)** scoring model and the concept of **attack surface measurement** — useful for mature clients who want quantified security metrics beyond CVSS.

- [ ] **Methodology Selection:** Know when to invoke each — PTES for comprehensive red team ops, NIST 800-115 for compliance-driven audits, OWASP WSTG for web-focused engagements, MASTG for mobile; document my methodology selection in every report.

---

### Topic 2: Scoping, Legal Frameworks & Engagement Management — 🧠 Conceptual

> [!TIP]
> **Goal:** Define engagement boundaries that protect the tester and client legally and operationally.

> [!NOTE]
> ⏱️ **Time Bracket: 1 day** — SoW construction (scope definition: IP ranges, domains, application URLs with version; deliverables with format and page estimate; timeline with milestones; liability cap language; IP ownership of testing artifacts — ambiguous scope equals legal exposure for the tester), RoE document (authorized IP ranges and domains; permitted testing hours; testing exclusions: life-safety systems, production databases; escalation contacts; emergency abort criteria; data handling requirements for captured credentials and PII), Get-Out-of-Jail letter (written authorization signed by someone with authority to authorize testing; verify signatory's authority; carry during physical tests), legal framework awareness (CFAA in US: unauthorized access is a federal crime regardless of intent; Computer Misuse Act 1990 in UK; IT Act 2000/2008 in India; cross-border engagements create dual-jurisdiction liability). Deliverable: draft a complete SoW and RoE document pair for a fictional engagement scenario.


- [ ] **Statement of Work (SoW) Construction:** Draft and review SoW language covering **scope definition (IP ranges, domains, application URLs), deliverables, timelines, payment milestones, liability caps, and IP ownership** of testing artifacts; ambiguous scope = legal exposure.

- [ ] **Rules of Engagement (RoE) Document:** Define in writing: **authorized IP ranges and domains, permitted testing hours (business hours vs. 24/7), testing exclusions (life-safety systems, production DBs), escalation contacts, emergency abort criteria, and data handling requirements**.

- [ ] **Get-Out-of-Jail Letter:** Understand the format and legal requirements of the **written authorization letter** — verify the signatory has authority to authorize testing, check it covers all target systems, and carry it during physical tests; know what makes it legally binding vs. inadequate.

- [ ] **Legal Framework Awareness:** Understand how **CFAA (US), Computer Misuse Act 1990 (UK), IT Act 2000 + Amendment 2008 (India), GDPR, and EU Cybersecurity Act** define criminal vs. authorized access; know how cross-border engagements create dual-jurisdiction liability.

- [ ] **Evidence & Data Handling Policy:** Establish rules for how **captured credentials, PII, financial records, source code, and exfiltrated data are classified, encrypted at rest, access-controlled, and securely destroyed** post-engagement; include this in every SoW.

- [ ] **Engagement Communication Cadence:** Define **weekly status calls, critical finding escalation (phone within 1 hour), interim report delivery, and final debrief meeting** structure; never let a critical finding sit unannounced for 24+ hours.

---

### Topic 3: Structured Threat Modeling — 🧠 Conceptual

> [!TIP]
> **Goal:** Apply structured threat identification before testing begins — not after.

> [!NOTE]
> ⏱️ **Time Bracket: 1 day** — STRIDE (for each DFD element — process, data store, data flow, external entity — apply Spoofing/Tampering/Repudiation/Information Disclosure/Denial of Service/Elevation of Privilege; generate a ranked threat list that scopes the test), PASTA (7-stage business-centric model: define objectives, technical scope, application decomposition, threat analysis, vulnerability analysis, attack enumeration, risk/impact analysis; produces a business-risk-aligned test plan), attack trees (hierarchical diagram rooted at attack goal; AND/OR nodes for alternative paths; prioritize branches by probability times impact), DFD trust boundaries (Level 0-2 DFDs; every trust boundary crossing is an attack surface; DFDs are the most important artifact to produce before testing begins), MITRE ATT&CK as pre-test input (identify likely TTPs based on target industry and known threat actor profiles; build test plan around these TTPs rather than guessing). Deliverable: apply STRIDE to a target application DFD and produce a ranked threat list with at least 10 threats categorized by STRIDE class.


- [ ] **STRIDE Threat Model:** Decompose target system components into **processes, data stores, data flows, and external entities**; apply Spoofing / Tampering / Repudiation / Information Disclosure / Denial of Service / Elevation of Privilege to each element; generate a ranked threat list that scopes the test. _(See also: Shelf 15 Topic 1 — STRIDE applied to architecture design rather than test scoping.)_

- [ ] **PASTA (Process for Attack Simulation and Threat Analysis):** Apply the **7-stage business-centric model** — define objectives → technical scope → application decomposition → threat analysis → vulnerability analysis → attack enumeration → risk/impact analysis; produces a business-risk-aligned test plan. _(See also: Shelf 11 Topic 3 — PASTA applied in GRC risk management context.)_

- [ ] **Attack Trees:** Build **hierarchical attack tree diagrams** rooted at the attack goal with sub-goals as branches; use AND/OR nodes to model alternative paths; identify which branches are highest probability × highest impact for prioritized testing.

- [ ] **Data Flow Diagram (DFD) Trust Boundaries:** Draw Level 0–2 DFDs to identify **trust boundaries, data stores, external entities, and inter-process data flows**; every trust boundary crossing is an attack surface that must be tested.

- [ ] **MITRE ATT&CK as Pre-Test Input:** Use ATT&CK to **pre-identify likely adversary TTPs** based on target industry, known threat actor profiles, and previously disclosed incidents in the sector; build my test plan around these TTPs.

- [ ] **LINDDUN (Privacy Threat Model):** Apply LINDDUN (Linkability, Identifiability, Non-repudiation, Detectability, Disclosure of information, Unawareness, Non-compliance) for privacy-focused assessments — required for GDPR/HIPAA compliance-mapped tests.

---

### Topic 4: Vulnerability Scoring & Risk Prioritization — 🧠 Conceptual

> [!TIP]
> **Goal:** Rate findings objectively and communicate risk in business terms — not just CVSS numbers.

> [!NOTE]
> ⏱️ **Time Bracket: 1 day** — CVSS v3.1 base metrics (all 8: Attack Vector, Attack Complexity, Privileges Required, User Interaction, Scope, C/I/A Impact — calculate scores manually before using calculators; AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H is a 10.0 by definition — know why), CVSS v4.0 changes (Supplemental Metrics group: Automatable, Recovery, Value Density; Threat Metrics replace Temporal; know which version your client's compliance framework requires), EPSS (probability that a CVE will be exploited in the next 30 days; CVSS 9.8 with 0.1% EPSS is operationally different from CVSS 7.5 with 95% EPSS — use both in your report), business risk contextualization (Risk = Likelihood times Business Impact; map to regulatory fine potential, revenue exposure, reputational damage; a CVSS 5.4 on a public OAuth endpoint may carry more business risk than a CVSS 8.1 on an isolated dev server), vulnerability chaining (SSRF Medium + IMDS Low + overprivileged IAM Medium = Full Cloud Compromise Critical — document chains as unified findings). Deliverable: manually calculate CVSS v3.1 scores for 5 findings without using a calculator.


- [ ] **CVSS v3.1 Base Metrics:** Master all **8 base metrics** (Attack Vector, Attack Complexity, Privileges Required, User Interaction, Scope, Confidentiality/Integrity/Availability Impact); calculate scores manually before using calculators to build intuition.

- [ ] **CVSS v4.0 Changes:** Understand the **new Supplemental Metrics group** (Automatable, Recovery, Value Density, Response Effort, Provider Urgency) and the replacement of Temporal Metrics with **Threat Metrics (Exploit Maturity)**; know which scoring version my client's compliance framework requires.

- [ ] **EPSS (Exploit Prediction Scoring System):** Use **EPSS probability scores** alongside CVSS to distinguish actively exploited vulnerabilities from theoretical ones; a CVSS 9.8 with 0.1% EPSS differs operationally from a CVSS 7.5 with 95% EPSS.

- [ ] **Business Risk Contextualization:** Calculate **Risk = Likelihood × Business Impact** — map vulnerabilities to: revenue exposure, regulatory fine potential, reputational damage, operational downtime, and data breach notification costs; a CVSS 5.4 on a public-facing OAuth token endpoint may carry more business risk than a CVSS 8.1 on an isolated dev server.

- [ ] **Vulnerability Chaining Analysis:** Identify when **individually low-severity findings combine** into critical-severity attack chains (e.g., SSRF [Medium] + IMDS credential access [Low] + overprivileged IAM role [Medium] = Full Cloud Compromise [Critical]); document chains as unified findings with individual component breakdowns.

- [ ] **Finding Deduplication:** When a single root cause produces multiple manifestations (e.g., 50 instances of the same SQLi pattern), report as **one finding with representative samples** and a count — not 50 separate findings that inflate severity perception and waste remediation effort.

---

### Topic 5: Professional Report Writing — 🧠🔬 Mixed

> [!TIP]
> **Goal:** Deliver findings in a format that survives executive scrutiny and drives budgeted remediation.

> [!NOTE]
> ⏱️ **Time Bracket: 2–3 days** — Report architecture (Cover Page, Executive Summary, Engagement Overview with scope/methodology/timeline, Attack Narrative as a linear story from foothold to max impact, Findings by Severity with full template for each, Remediation Roadmap tiered by timeline, Appendices with evidence and methodology references), executive summary writing (1-2 pages for C-suite: overall security posture rating, total findings by severity, most critical business risks, top 3 priority actions — written for a CFO at 35,000 feet, not a sysadmin — no CVE numbers, no tool names), technical finding template (Title, Severity, CVSS v3.1 score, EPSS %, Affected Asset, Vulnerability Description, Business Impact, PoC with exact request/response, Remediation Guidance with specific code examples, References with CVE/CWE/OWASP ID), remediation specificity (write executable technical steps: apply parameterized queries using mysqli_prepare with bound parameters — not fix SQL injection; include patch version numbers and configuration file paths), report delivery (password-protected PDF, PGP-encrypted email attachment, define retention and destruction policy in SoW). Deliverable: write a complete pentest report for a fictional enterprise engagement: executive summary, 3 findings with full template, attack narrative, remediation roadmap tiered by timeline.


- [ ] **Report Architecture:** Master the standard structure: **Cover Page → Executive Summary → Engagement Overview (scope, methodology, timeline) → Attack Narrative → Findings by Severity → Remediation Roadmap → Appendices (evidence, tooling, methodology references, CVSS breakdowns)**.

- [ ] **Executive Summary (Non-Technical):** Write a **1–2 page narrative** for the C-suite covering: overall security posture rating, total findings by severity, most critical business risks, and top 3 priority actions — written for a CFO reading at 35,000 feet, not a sysadmin.

- [ ] **Technical Finding Template:** Each finding must include: **Title | Severity | CVSS Score (v3.1/v4.0) | EPSS % | Affected Asset | Vulnerability Description | Business Impact | Proof of Concept (exact request/response/screenshot) | Remediation Guidance (specific, actionable, with code examples where applicable) | References (CVE, CWE, OWASP ID)**.

- [ ] **Attack Narrative / Kill Chain Story:** Write a **linear narrative** tracing the attacker's path from initial foothold through escalation to maximum impact — this is the section that gets security budgets approved; make it read like a post-breach incident report, not a bullet list.

- [ ] **Remediation Specificity:** Write remediation as **executable technical steps** — e.g., "Apply parameterized queries using `mysqli_prepare()` with bound parameters" not "fix SQL injection"; include patch version numbers, configuration file paths, and code snippets; vague remediation = finding stays open.

- [ ] **Proof-of-Concept Discipline:** PoCs must be **reproducible, minimally invasive, and clearly annotated** — include exact HTTP request/response, commands run, and observed vs. expected behavior; redact real credentials and PII captured; test PoC steps against my own notes before submission.

- [ ] **Remediation Roadmap Tiering:** Tier findings into **Immediate (< 7 days — critical/exploited), Short-term (< 30 days — high), Medium-term (< 90 days — medium), Long-term / Strategic (low + systemic architectural issues)**; include effort estimates and responsible team assignments.

- [ ] **Re-test Procedures:** Document **exactly how the client verifies each remediation** — include test steps, expected output, and acceptance criteria; schedule and execute a **formal re-test engagement** where contracted; issue a re-test supplement report with delta findings.

- [ ] **Report Versioning & Delivery:** Maintain **draft → client review → final** versioning; deliver reports in **password-protected PDF** with restricted printing/copying; PGP-encrypt email attachments; define report retention and destruction policy in the SoW.

### Lab Progression (Module 26: Penetration Testing Methodologies & Report Writing)

| Level | Task | Deliverable |
| ----- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| 1 | Draft an SoW and RoE document for a fictional engagement using a provided scenario | Complete SoW + RoE document pair |
| 2 | Apply STRIDE to a target application's DFD and produce a ranked threat list | Threat model document with STRIDE matrix |
| 3 | Write a full pentest report (executive summary + 3 findings with PoC + remediation roadmap) for an enterprise lab engagement | Professional pentest report in PDF format, password-protected |

> [!IMPORTANT]
> **Move-On Gate (Module 26):** I can select and apply the correct engagement methodology (PTES, NIST 800-115, WSTG), produce an SoW and RoE document, perform STRIDE threat modeling, calculate CVSS scores manually, and write a complete pentest report with executive summary, technical findings, and remediation roadmap.

---

---

> [!TIP]

### 🎮 Concurrent CTF Practice — Stage 4
> Enterprise environments require enterprise practice. Standard HTB/THM boxes are no longer enough — you need pro labs.
> | Module | Platform | Lab / Box | Why |
> |---|---|---|---|
> | 19 Active Directory | HackTheBox | **Forest** · **Monteverde** · **Cascade** | Kerberoasting, AS-REP, ACL abuse, Pass-the-Hash |
> | 19 Active Directory | TryHackMe | **Active Directory Basics** · **Attacktive Directory** | Guided AD attack path from scratch |
> | 19 Active Directory | HackTheBox Pro Labs | **Offshore** or **RastaLabs** | Full multi-domain enterprise AD simulation |
> | 20 Cloud | [flaws.cloud](http://flaws.cloud) + [flaws2.cloud](http://flaws2.cloud) | All levels | AWS S3, IAM, metadata exploitation |
> | 20 Cloud | [CloudGoat](https://github.com/RhinoSecurityLabs/cloudgoat) | All scenarios | Rhino Security's vulnerable-by-design AWS env |
> | 21 Containers | HackTheBox | **Unobtainium** · **Registry** | Container escape + Kubernetes privilege escalation |
> | 22–26 Full chain | HackTheBox Pro Labs | **Dante** (OSCP prep) | Full network penetration test simulation |
> **Rule:** For every AD box: export my BloodHound graph, annotate the attack path, commit it to Git. That is a portfolio artifact.

## 🏁 Stage Gate 3 — Enterprise Domain Compromise & Reporting

> [!IMPORTANT]
> **Stage 4 Exit Gate:** Before moving to Advanced Offensive Development (Stage 5), I must prove:
> - Full end-to-end compromise of a multi-forest Active Directory lab (Kerberoasting/AS-REP roasting -> DCSync -> Golden Ticket).
> - BloodHound visualization and execution of shortest attack path committed to Git.
> - One complete, client-ready, professional penetration test report following PTES/CVSS standards.

---

### 🧭 Stage Navigation

| ◀ Previous Stage | 🏠 Master Hub | Next Stage ➔ | ⬆ Top |
| :---: | :---: | :---: | :---: |
| [[Cyber-Security/Roadmap/Stage-3_Web-and-App-Sec\|◀ Stage 3: Web & App Sec]] | [[Cyber-Security/Roadmap/README\|MASTER_README]] | [[Cyber-Security/Roadmap/Stage-5_Specialized\|Stage 5: Specialized ➔]] | [[#Stage 4 — Enterprise\|⬆ Return to Top]] |

> 💡 **Obsidian Tip:** Press `Ctrl + Click` (or `Cmd + Click`) on `[[Cyber-Security/Roadmap/Stage-5_Specialized|Stage 5: Specialized]]` to open the next stage in a split tab, or hover to preview.
