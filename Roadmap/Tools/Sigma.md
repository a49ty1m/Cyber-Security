# 🔎 Sigma: Complete Mastery Checklist

> **What is Sigma?** Sigma is a generic, open-source signature format for SIEM detection rules. It is the **YARA of log detection** — a vendor-neutral rule language that describes attacker behavior in log data, which can then be converted to the query language of any SIEM (Splunk SPL, Elastic KQL, Microsoft Sentinel KQL, QRadar, Wazuh, etc.) using the `sigma-cli` converter. A single Sigma rule can target all SIEMs simultaneously.
>
> **Why does it exist?** Every SIEM has its own query language. A detection rule written in Splunk SPL is useless in Elastic, and vice versa. Sigma solves this by being a common intermediate format. The open-source SigmaHQ repository contains 3,000+ community-written rules aligned to MITRE ATT&CK — the single largest freely available detection rule library.
>
> **When to use it:** Writing detection rules that need to work across multiple SIEMs, contributing to the security community rule library, converting attacker TTPs observed in the wild into detections, and operationalizing threat intelligence as detection logic.
>
> **When to avoid it:** Sigma is a rule *format*, not a detection *engine*. You still need a SIEM to execute the converted rules. For simple one-off searches, write directly in your SIEM's query language. Sigma is for *sharable, reusable* detection content.
>
> **What mastering Sigma unlocks:** Platform-agnostic detection engineering, ability to operationalize threat intelligence, contribution to the SigmaHQ community library, and the skills to rapidly deploy detection coverage across any SIEM environment.
>
> **Roadmap Phase:** Phase 3 — Detection Engineering & SOC Operations (Part 13A Stage 2–3)

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](README.md)

| Detection Rules | SIEM Platforms | Endpoint Telemetry | Malware Analysis |
|:---------------|:--------------|:------------------|:-----------------|
| **🔎 Sigma** (you are here) | [📊 Splunk](Splunk.md) | [🔭 Sysmon](Sysmon.md) | [🦠 YARA](YARA.md) |
| | [🐺 Wazuh](Wazuh.md) | | [🧠 Volatility](Volatility.md) |
| | [📦 ELK](ELK.md) | | |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Sigma Basics & Tool Setup | 5 | 1–2 hours |
| 2 | Rule Anatomy & Syntax | 8 | 3–4 hours |
| 3 | Writing Rules from Scratch | 8 | 4–6 hours |
| 4 | Converting & Deploying Rules | 5 | 2–3 hours |
| 5 | The SigmaHQ Repository | 5 | 2–3 hours |
| 6 | Advanced: Correlation & Conditions | 6 | 3–4 hours |
| 7 | Practical Labs | 4 | 4–6 hours |
| | **Total** | **41** | **~19–28 hours** |

**Prerequisites:** Phase 3 Part 13A Stage 1 complete (Sysmon deployed, SIEM ingesting Windows Event Logs). Familiarity with at least one SIEM query language (Splunk SPL or Kibana KQL).

---

# PHASE 1: SIGMA BASICS & TOOL SETUP

---

## 1.1 Install sigma-cli

```bash
# Install sigma-cli (the official converter tool)
pip3 install sigma-cli

# Install SIEM backend plugins
sigma plugin install splunk
sigma plugin install elasticsearch
sigma plugin install sentinel   # Microsoft Sentinel
sigma plugin install qradar

# List installed backends
sigma plugin list

# Verify
sigma --version
```

## 1.2 Install pySigma (programmatic use)

```bash
# For Python-based automation
pip3 install pySigma
pip3 install pySigma-backend-splunk
pip3 install pySigma-backend-elasticsearch
```

## 1.3 Get the SigmaHQ Rule Repository

```bash
# Clone the community rule library (3000+ rules)
git clone https://github.com/SigmaHQ/sigma.git
cd sigma

# Directory structure:
# rules/windows/         — Windows rules (Sysmon, Security, System, etc.)
# rules/linux/           — Linux rules
# rules/network/         — Network device rules
# rules/cloud/           — AWS/Azure/GCP rules
# rules/web/             — Web server rules
# rules/application/     — Application-specific rules
```

---

# PHASE 2: RULE ANATOMY & SYNTAX

---

## 2.1 Sigma Rule Structure

```yaml
title: PowerShell Encoded Command Execution
id: 5b3f3f63-9a4b-4cb8-8c3b-0b86ac5f68a9   # UUID — generate with uuidgen
status: test            # test | experimental | stable | deprecated | unsupported
description: Detects execution of PowerShell with an encoded command argument, commonly used to obfuscate malicious scripts
references:
  - https://attack.mitre.org/techniques/T1059/001/
author: Your Name
date: 2024/01/01
modified: 2024/01/15
tags:
  - attack.execution
  - attack.t1059.001
  - attack.defense_evasion
  - attack.t1027

logsource:
  category: process_creation    # Sigma category — maps to Sysmon Event 1, Security 4688, etc.
  product: windows

detection:
  selection:
    Image|endswith:
      - '\powershell.exe'
      - '\pwsh.exe'
    CommandLine|contains|all:
      - '-'
      - 'enc'
  filter_main_legitimate:
    CommandLine|contains:
      - '-EncodedCommand ""'    # Empty encoded command (some scripts do this legitimately)
  condition: selection and not filter_main_legitimate

falsepositives:
  - Legitimate administrative scripts using encoded commands
  - Software deployment tools (SCCM, PDQ)

level: high    # informational | low | medium | high | critical
```

## 2.2 Log Source Categories

| Category | Maps To | Event IDs |
|:---------|:--------|:---------|
| `process_creation` | Sysmon Event 1, Windows 4688 | Process creation |
| `network_connection` | Sysmon Event 3 | Network connections |
| `image_load` | Sysmon Event 7 | DLL loads |
| `create_remote_thread` | Sysmon Event 8 | Remote thread injection |
| `raw_access_thread` | Sysmon Event 9 | Raw disk access |
| `process_access` | Sysmon Event 10 | Process handle open |
| `file_event` | Sysmon Event 11 | File create |
| `registry_add` / `registry_set` | Sysmon 12/13 | Registry modification |
| `dns_query` | Sysmon Event 22 | DNS lookups |
| `firewall` | Firewall logs | Network allow/deny |

## 2.3 Detection Field Modifiers

```yaml
# Field modifiers control how values are matched:

Image|endswith: '\cmd.exe'          # String ends with
Image|startswith: 'C:\Windows\'    # String starts with
CommandLine|contains: 'mimikatz'    # String contains (case-insensitive by default)
CommandLine|contains|all:           # ALL of these must be present
  - '-enc'
  - 'powershell'
CommandLine|contains|windash:       # Match both - and / variants (for cmdline switches)
  - '/enc'
EventID|re: '^(4624|4625|4648)$'   # Regex match
count: '>= 5'                       # Numeric comparison
```

## 2.4 Condition Logic

```yaml
# Basic: match if selection hits
condition: selection

# NOT: exclude matches
condition: selection and not filter

# Multiple selections with OR
detection:
  selection_cmd:
    Image|endswith: '\cmd.exe'
  selection_ps:
    Image|endswith: '\powershell.exe'
  condition: selection_cmd or selection_ps

# ALL conditions must match (AND)
condition: selection_parent and selection_child

# Aggregation: count-based detection
detection:
  failed_login:
    EventID: 4625
  condition: failed_login | count() > 10    # More than 10 failed logins
  timeframe: 5m                              # Within 5 minutes
```

---

# PHASE 3: WRITING RULES FROM SCRATCH

---

## 3.1 Rule Writing Process

1. **Identify the TTP:** What attacker behavior are you trying to detect? Map to MITRE ATT&CK.
2. **Find the log source:** Which log (Sysmon Event 1? Windows Security 4625? DNS?) captures this behavior?
3. **Identify key fields:** What fields distinguish malicious from benign? (Image, CommandLine, ParentImage, TargetImage, etc.)
4. **Write the detection:** Use field modifiers to match the malicious pattern.
5. **Add filters:** Remove known-false-positive cases.
6. **Test:** Convert to your SIEM's language and validate against real log data.

## 3.2 Example: LSASS Credential Dumping (T1003.001)

```yaml
title: LSASS Memory Access by Non-System Process
id: a2b05a65-5b39-4e42-8da8-a6fcbda2c8db
status: test
description: Detects non-system processes accessing LSASS memory, indicating potential credential dumping
references:
  - https://attack.mitre.org/techniques/T1003/001/
tags:
  - attack.credential_access
  - attack.t1003.001
logsource:
  category: process_access
  product: windows
detection:
  selection:
    TargetImage|endswith: '\lsass.exe'
    GrantedAccess|contains:
      - '0x1010'
      - '0x1410'
      - '0x1418'
      - '0x143a'
      - '0x1fffff'   # PROCESS_ALL_ACCESS
  filter_legitimate:
    SourceImage|startswith:
      - 'C:\Windows\System32\'
      - 'C:\Windows\SysWOW64\'
      - 'C:\ProgramData\Microsoft\Windows Defender\'
  condition: selection and not filter_legitimate
falsepositives:
  - Security tools (CrowdStrike, SentinelOne, Cylance) accessing LSASS for protection
  - Backup agents
level: high
```

## 3.3 Example: WMI Persistence (T1546.003)

```yaml
title: WMI Event Subscription for Persistence
id: c3c491c5-0fcc-4671-a0c3-5d2b1f59ae8f
status: stable
description: Detects creation of WMI event subscriptions, a common persistence mechanism
tags:
  - attack.persistence
  - attack.t1546.003
logsource:
  category: wmi_event
  product: windows
detection:
  selection:
    EventID:
      - 19   # WMI Filter registered (Sysmon)
      - 20   # WMI Consumer registered (Sysmon)
      - 21   # WMI Consumer to Filter binding (Sysmon)
  condition: selection
falsepositives:
  - Legitimate security software using WMI subscriptions
  - Administrative automation scripts
level: medium
```

## 3.4 Example: DNS C2 Beaconing (T1071.004)

```yaml
title: Suspicious DNS Query with Long Encoded Subdomain
id: 1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d
status: experimental
description: Detects DNS queries with unusually long subdomains, characteristic of DNS tunneling or DGA domains
tags:
  - attack.command_and_control
  - attack.t1071.004
logsource:
  category: dns_query
  product: windows
detection:
  selection:
    QueryName|re: '^[a-z0-9]{30,}\.'   # Subdomain with 30+ alphanumeric chars
  filter_cdn:
    QueryName|contains:
      - '.cloudfront.net'
      - '.fastly.net'
      - '.akamai.net'
  condition: selection and not filter_cdn
falsepositives:
  - Legitimate CDN domains with long hostnames
  - Some analytics services
level: medium
```

---

# PHASE 4: CONVERTING & DEPLOYING RULES

---

## 4.1 Converting Rules with sigma-cli

```bash
# Convert a single rule to Splunk SPL
sigma convert -t splunk rules/windows/process_creation/proc_creation_win_powershell_encoded_cmd.yml

# Convert with pipeline (for field mapping)
sigma convert -t splunk -p sysmon rules/windows/process_creation/proc_creation_win_mimikatz_command_line.yml

# Convert to Elastic (EQL)
sigma convert -t elasticsearch -p ecs_windows rules/windows/process_creation/proc_creation_win_powershell_encoded_cmd.yml

# Convert to Microsoft Sentinel KQL
sigma convert -t sentinel rules/windows/process_creation/proc_creation_win_powershell_encoded_cmd.yml

# Convert an entire rules directory (bulk)
sigma convert -t splunk -p sysmon rules/windows/process_creation/ -o splunk_rules.txt

# Convert with output format options
sigma convert -t splunk --format savedsearches rules/windows/ -o splunk_savedsearches.conf
```

## 4.2 Pipelines — Field Mapping

Sigma uses abstract field names. Pipelines map them to your actual SIEM's field names:

```yaml
# Example: without pipeline
# Image → abstract
# With sysmon pipeline:
# Image → process.executable (ECS) OR Image (Splunk Sysmon TA)

# List available pipelines
sigma plugin list
# sysmon, ecs_windows, carbon_black, crowdstrike, etc.

# Use the right pipeline for your log source
sigma convert -t splunk -p sysmon myrule.yml    # For Splunk with Sysmon TA
sigma convert -t elasticsearch -p ecs_windows myrule.yml  # For ELK with ECS field mapping
```

---

# PHASE 5: THE SIGMAHQ REPOSITORY

---

## 5.1 Rule Categories to Know

```bash
# High-value rule directories
ls sigma/rules/windows/
# builtin/         — Windows built-in event logs
# create_remote_thread/  — Process injection
# create_stream_hash/    — ADS usage
# dns_query/        — DNS-based detections
# file_access/      — Sensitive file access
# image_load/       — DLL hijacking, LOLBin abuse
# network_connection/ — C2, lateral movement
# pipe_created/     — Named pipe C2
# process_access/   — LSASS dumping
# process_creation/ — The largest category (execution TTPs)
# registry_add/event/set/ — Persistence via registry
```

## 5.2 Finding Rules for Specific TTPs

```bash
# Find all rules for a specific MITRE technique
grep -r "t1059.001" sigma/rules/ --include="*.yml" -l

# Find all high/critical severity rules
grep -r "level: high" sigma/rules/windows/ --include="*.yml" -l | wc -l

# Find rules for a specific tool (e.g., Mimikatz)
grep -r "mimikatz" sigma/rules/ --include="*.yml" -l
```

---

# PHASE 6: ADVANCED — CORRELATION & CONDITIONS

---

## 6.1 Near-Real-Time Correlation Rules

```yaml
# Detect: Many failed logins then a successful login (brute force + success)
title: Brute Force Success After Multiple Failures
logsource:
  category: authentication
  product: windows
detection:
  failures:
    EventID: 4625
  success:
    EventID: 4624
  condition: failures | count() > 5 | timeframe 5m | near success
```

## 6.2 Multi-Event Sequences

```yaml
# Detect: Encoded PowerShell followed by network connection within 30 seconds
title: PowerShell Encoded Command then Network Connection
# Note: full sequence correlation requires SIEM-native EQL/SPL correlation
# Sigma 2.0 introduces sequence detection for this use case
```

---

# PHASE 7: PRACTICAL LABS

---

- [ ] **Lab 1 — Rule Conversion Sprint:** Take 10 rules from the SigmaHQ repository targeting Windows process creation. Convert all 10 to Splunk SPL and 10 to Elasticsearch EQL. Deploy all 20 in your respective lab SIEMs. Confirm they parse without errors.

- [ ] **Lab 2 — Write and Validate:** Execute an LSASS dump in a lab VM using `procdump` or Task Manager. View the resulting Sysmon Event 10 in Event Viewer. Write a Sigma rule from scratch targeting this event. Convert it and verify it fires in your SIEM.

- [ ] **Lab 3 — False Positive Tuning:** Take the SwiftOnSecurity Sigma ruleset and apply it to a week of lab log data. Identify the top 5 false-positive-generating rules. Add appropriate filter conditions to each. Document every filter added and the legitimate behavior it excludes.

- [ ] **Lab 4 — TTP Coverage Map:** Using the SigmaHQ rules, map your SIEM's current detection coverage against the MITRE ATT&CK matrix. Which tactics have >5 rules? Which have 0? Create a gap analysis document with 3 new rules you would write to fill the most critical gaps.

---

## 📝 Operational Notes

- **Sigma 2.0 vs Sigma 1.x:** Sigma 2.0 (pySigma) introduced breaking changes in the conversion pipeline. Old `sigmac` is deprecated — use `sigma-cli` / pySigma. Many online tutorials still reference `sigmac`; these are outdated.
- **Rule `status` field:** Only use `status: stable` for rules that have been validated against real data with known-low false positive rates. Use `status: test` during development. Using SigmaHQ community rules directly in production without testing is a recipe for alert fatigue.
- **UUID generation:** Every Sigma rule needs a unique UUID in the `id` field. Generate with `uuidgen` (Linux) or `python3 -c "import uuid; print(uuid.uuid4())"`.
- **`windash` modifier:** Windows command-line arguments can use `/` or `-` interchangeably (e.g., `cmd /c` and `cmd -c`). The `|windash` modifier matches both variants automatically.
- **Sigma vs YARA:** Sigma detects attackers in *logs* (at the network/SIEM layer). YARA detects attackers in *files and memory* (at the endpoint layer). They are complementary, not competing.
