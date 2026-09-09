# 📊 Splunk: Complete Mastery Checklist

> **What is Splunk?** Splunk is the industry-leading Security Information and Event Management (SIEM) platform. It ingests, indexes, and makes searchable any machine-generated data — Windows Event Logs, syslog, firewall logs, endpoint telemetry (Sysmon), network flows, application logs, and more. Splunk's proprietary query language (SPL — Search Processing Language) lets you build real-time alerts, dashboards, and detection rules over billions of events.
>
> **Why does it exist?** In any organization with more than a handful of machines, logs become impossible to review manually. Splunk solves the log correlation problem: it aggregates all data in one place, lets analysts query across millions of events in seconds, and fires alerts when attacker behaviors match detection rules.
>
> **When to use it:** SOC analyst work, detection engineering (writing rules to catch attacker TTPs), incident response (searching logs to reconstruct an attack timeline), threat hunting (proactive searches for adversary behavior without a prior alert), and blue team lab exercises.
>
> **When to avoid it:** Splunk Enterprise is expensive. For personal labs, use the free Splunk Enterprise trial (500MB/day ingest) or switch to Wazuh/ELK (fully open-source). Splunk is overkill for single-machine log analysis — use `grep`, `awk`, or `jq` instead.
>
> **What mastering Splunk unlocks:** SOC Analyst roles (Tier 1/2), detection engineering capability, the ability to write correlation rules that catch real attacks, and deep understanding of log-based forensics — all required for Phase 3 Part 13A.
>
> **Roadmap Stage / Module:** Stage 3: Side-Track A (Detection Engineering & SOC Operations)

---

## 🧭 Navigation

> [🏠 Master Roadmap](../README.md) · [🔧 Tools Index](README.md)

| SIEM Platforms | Telemetry | Detection Rules | Forensics |
|:--------------|:----------|:----------------|:----------|
| **📊 Splunk** (you are here) | [🔭 Sysmon](Sysmon.md) | [🔎 Sigma](Sigma.md) | [🧠 Volatility](Volatility.md) |
| [🐺 Wazuh](Wazuh.md) | [📦 Plaso](Plaso.md) | [🦠 YARA](YARA.md) | [🔬 Autopsy](Autopsy.md) |
| [📦 ELK](ELK.md) | | | |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Installation & Data Ingestion | 5 | 2–3 hours |
| 2 | SPL Core — Searching & Filtering | 8 | 4–6 hours |
| 3 | SPL Intermediate — Stats, Lookups, Subsearches | 7 | 4–5 hours |
| 4 | Detection Rule Writing & Alerting | 8 | 5–7 hours |
| 5 | Dashboards & Threat Hunting | 6 | 4–5 hours |
| 6 | Sysmon Integration & Windows Event Logs | 6 | 4–6 hours |
| 7 | Practical Labs | 4 | 6–10 hours |
| | **Total** | **44** | **~29–42 hours** |

**Prerequisites:** Linux fundamentals (Phase 1 complete). Basic understanding of Windows Event Logs and Sysmon (Phase 3 Part 13A Stage 1 recommended). Conceptual understanding of what a SIEM does.

---

# PHASE 1: INSTALLATION & DATA INGESTION

---

## 1.1 Installing Splunk (Free Trial)

```bash
# Download Splunk Enterprise from splunk.com (requires free account)
# Install on Linux (Debian/Ubuntu)
sudo dpkg -i splunk-*.deb

# Start Splunk
sudo /opt/splunk/bin/splunk start --accept-license

# Enable Splunk to start on boot
sudo /opt/splunk/bin/splunk enable boot-start

# Access the web interface
# http://localhost:8000  (default credentials: admin/changeme on first launch)
```

- [ ] **Splunk Free vs Enterprise vs Cloud:** The free license limits ingest to 500MB/day and disables alerting and role-based access control. For lab use, this is sufficient. Know what you lose with the free tier.
- [ ] **Key ports:** Web interface: `8000`, Splunk-to-Splunk (receiver): `9997`, Management API: `8089`, HEC (HTTP Event Collector): `8088`.

## 1.2 Data Ingestion Methods

- [ ] **Monitor a local directory:** Settings → Data Inputs → Files & Directories → Monitor `/var/log`. Splunk watches for new log entries and indexes them automatically.

```bash
# Monitor syslog from CLI (alternative)
/opt/splunk/bin/splunk add monitor /var/log/syslog -index main -sourcetype syslog
```

- [ ] **Upload a log file (one-time):** Settings → Add Data → Upload → Select file. Use this to ingest CTF/lab log files.
- [ ] **HTTP Event Collector (HEC):** A REST API endpoint for applications to push JSON events directly into Splunk. Used for modern app telemetry, Kubernetes logs, and custom tools.

```bash
# Send an event via HEC (after enabling it in Settings → Data Inputs → HTTP Event Collector)
curl -k https://localhost:8088/services/collector \
  -H "Authorization: Splunk YOUR_HEC_TOKEN" \
  -d '{"event": {"message": "test event", "severity": "info"}}'
```

- [ ] **Syslog receiver (UDP/TCP):** Settings → Data Inputs → UDP/TCP → Port 514 → Source type `syslog`. Used to receive logs from network devices and Linux hosts.
- [ ] **Universal Forwarder:** A lightweight Splunk agent installed on endpoints that forwards logs to a central Splunk server. In enterprise environments, this is how Windows Event Logs get to Splunk. Know the difference between forwarder and heavy forwarder.

---

# PHASE 2: SPL CORE — SEARCHING & FILTERING

---

## 2.1 Basic SPL Syntax

```spl
# All events from the last 24 hours (default time picker)
index=* | head 10

# Search for a specific keyword
index=main "failed password"

# Time range: last 7 days
index=main earliest=-7d@d latest=now "authentication failure"

# Filter by sourcetype
index=main sourcetype=WinEventLog "EventCode=4625"

# Filter by field value
index=main sourcetype=WinEventLog EventCode=4625 Account_Name!="-"
```

## 2.2 Field Extraction & Filtering

```spl
# List all fields in results
index=main | fieldsummary

# Display specific fields only
index=main sourcetype=syslog | table _time, host, source, _raw

# Filter with NOT / AND / OR
index=main (EventCode=4625 OR EventCode=4624) AND Account_Name="administrator"

# Wildcard
index=main "powershell*encoded*"

# Case-insensitive (Splunk searches are case-insensitive by default)
index=main "MIMIKATZ" OR "mimikatz"

# Regex search
index=main | regex _raw="cmd\.exe.*(\/c|\/k).*(whoami|net user|ipconfig)"
```

## 2.3 The Search Pipeline

Every SPL query is a pipeline — each `|` passes results to the next command:

```spl
# Pattern: search | transform | display
index=main sourcetype=WinEventLog EventCode=4625
| stats count by Account_Name, host
| sort -count
| head 20
```

- [ ] **Key pipeline commands to master:**
  - `search` — filter events (implicit at start)
  - `stats` — aggregate (count, sum, avg, max, values)
  - `eval` — calculate new fields
  - `where` — filter after stats
  - `table` — select columns to display
  - `sort` — order results
  - `head` / `tail` — limit results
  - `rex` — extract fields using regex
  - `rename` — rename fields
  - `dedup` — remove duplicate events

---

# PHASE 3: SPL INTERMEDIATE

---

## 3.1 `stats` — Aggregation Queries

```spl
# Count failed logins by username (last 24h)
index=main sourcetype=WinEventLog EventCode=4625
| stats count as failures by Account_Name
| sort -failures

# Count by multiple fields (user + source IP)
index=main sourcetype=WinEventLog EventCode=4625
| stats count as failures by Account_Name, IpAddress
| sort -failures

# Calculate average, max, and unique values
index=main sourcetype=WinEventLog
| stats count, max(_time) as last_seen, values(EventCode) as seen_codes by host
```

## 3.2 `eval` — Field Calculations

```spl
# Convert Unix timestamp to human-readable
index=main | eval human_time=strftime(_time, "%Y-%m-%d %H:%M:%S")

# Classify events
index=main EventCode=4625
| eval risk_level=if(count>100, "HIGH", if(count>20, "MEDIUM", "LOW"))

# String concatenation
index=main | eval full_path=CommandLine+" ("+User+")"

# Calculate time difference
index=main | eval minutes_ago=round((now()-_time)/60,0)
```

## 3.3 `timechart` — Time-Based Analysis

```spl
# Failed logins per hour over last 7 days
index=main EventCode=4625
| timechart span=1h count by Account_Name

# Process creation events per minute (spike detection)
index=main sourcetype=WinEventLog EventCode=1
| timechart span=1m count
```

## 3.4 Lookups — Enrichment

```spl
# Use a CSV lookup to enrich IPs with geolocation or threat intel
| iplocation IpAddress
| table Account_Name, IpAddress, Country, City

# Custom lookup (e.g., known bad IPs)
index=main
| lookup threat_intel_ips ip AS IpAddress OUTPUT threat_type
| where isnotnull(threat_type)
```

---

# PHASE 4: DETECTION RULE WRITING & ALERTING

---

## 4.1 Core Attacker TTPs to Detect (MITRE ATT&CK Aligned)

```spl
# T1059.001 — PowerShell execution with encoded commands
index=main sourcetype=WinEventLog EventCode=4104
| search ScriptBlockText="*-EncodedCommand*" OR ScriptBlockText="*-enc *"
| table _time, host, User, ScriptBlockText

# T1003.001 — LSASS access (credential dumping)
index=main sourcetype=WinEventLog EventCode=10
| where TargetImage LIKE "%lsass.exe%"
| table _time, host, SourceImage, TargetImage, GrantedAccess

# T1055 — Process injection (Sysmon Event 8: CreateRemoteThread)
index=main sourcetype=WinEventLog EventCode=8
| where TargetImage NOT IN ("C:\\Windows\\System32\\svchost.exe","C:\\Windows\\System32\\csrss.exe")
| table _time, host, SourceImage, TargetImage, StartAddress

# T1078 — Valid account brute force (>10 failures then success)
index=main EventCode=4625
| stats count as failures by Account_Name, IpAddress
| where failures > 10
| join Account_Name [search index=main EventCode=4624 | stats count as successes by Account_Name]
| where successes > 0

# T1566 — Phishing: Office macro execution spawning cmd/powershell
index=main sourcetype=WinEventLog EventCode=1
| where (ParentImage LIKE "%WINWORD.EXE%" OR ParentImage LIKE "%EXCEL.EXE%")
  AND (Image LIKE "%cmd.exe%" OR Image LIKE "%powershell.exe%")
| table _time, host, ParentImage, Image, CommandLine
```

## 4.2 Creating Alerts

In Splunk Web:
1. Build and run your detection SPL query
2. Click **Save As → Alert**
3. Set: **Trigger Condition** (e.g., "Number of Results > 0"), **Throttle** (prevent alert floods), **Actions** (email, webhook, Slack, PagerDuty)
4. Set **Cron Schedule** for persistent monitoring (e.g., every 5 minutes: `*/5 * * * *`)

- [ ] **Alert throttling:** Set a suppress window (e.g., "suppress alert for 1 hour after triggering") to prevent alert fatigue from repeated triggers on the same event.
- [ ] **CIM (Common Information Model):** Splunk's schema-normalization layer. Alerts written against CIM fields (`src`, `dest`, `user`, `action`) work across any data source without rewriting. Know the CIM fields for Authentication, Network Traffic, and Endpoint.

---

# PHASE 5: DASHBOARDS & THREAT HUNTING

---

## 5.1 Building a SOC Dashboard

Key panels to include in a defensive dashboard:
- Failed login count (last 24h) — timechart
- Top failed usernames — bar chart
- Process creation spikes — timechart by host
- Network connections to external IPs — geolocation map
- PowerShell execution events — table with CommandLine

## 5.2 Threat Hunting SPL Queries

```spl
# Hunt: Lateral movement via PsExec/WMI (Event ID 4648 — explicit credential use)
index=main EventCode=4648
| stats count by TargetServerName, SubjectUserName, LogonType
| sort -count

# Hunt: New local admin accounts created
index=main EventCode=4720 OR EventCode=4732
| table _time, host, Account_Name, Subject_Security_ID

# Hunt: Base64 encoded PowerShell (T1027)
index=main sourcetype=WinEventLog EventCode=4104
| regex ScriptBlockText="(?i)frombase64string|[a-zA-Z0-9+/]{100,}={0,2}"
| table _time, host, User, ScriptBlockText

# Hunt: Unusual parent-child process relationships
index=main sourcetype=WinEventLog EventCode=1
| stats values(Image) as children by ParentImage
| where mvcount(children) > 10
```

---

# PHASE 6: SYSMON INTEGRATION & WINDOWS EVENT LOGS

---

## 6.1 Key Windows Event IDs

| Event ID | Description | Detection Value |
|:---------|:------------|:----------------|
| 4624 | Successful logon | Lateral movement, unusual logon types |
| 4625 | Failed logon | Brute force, spray attacks |
| 4648 | Logon with explicit credentials | Pass-the-Hash, PsExec |
| 4688 | New process created | Command execution (enable auditing) |
| 4698 | Scheduled task created | Persistence |
| 4720 | User account created | Backdoor accounts |
| 4732 | Member added to privileged group | Privilege escalation |
| 7045 | New service installed | Persistence |

## 6.2 Key Sysmon Event IDs (after deploying Sysmon)

| Event ID | Description | Detection Value |
|:---------|:------------|:----------------|
| 1 | Process Create (full command line + parent) | Execution, LOLBins |
| 3 | Network Connection | C2 beaconing, lateral movement |
| 7 | Image Loaded (DLL load) | DLL hijacking, injection |
| 8 | CreateRemoteThread | Process injection |
| 10 | ProcessAccess (LSASS access) | Credential dumping |
| 11 | File Create | Dropper activity, staging |
| 12/13/14 | Registry Events | Persistence via Run keys |
| 22 | DNS Query | C2 domain resolution |

```spl
# Correlate Sysmon Event 3 (network) with Event 1 (process creation)
index=main sourcetype=WinEventLog EventCode=3
| where Image NOT IN (known_browsers_and_updaters)
| table _time, host, Image, DestinationIp, DestinationPort, DestinationHostname
```

---

# PHASE 7: PRACTICAL LABS

---

- [ ] **Lab 1 — BOTS Dataset:** Download the Splunk Boss of the SOC (BOTS) v2 or v3 dataset. This is a realistic SOC dataset with embedded attack scenarios. Complete at least 5 investigation questions using SPL. Document your queries and findings.

- [ ] **Lab 2 — Detection Engineering:** Deploy a Windows VM with Sysmon, forward logs to Splunk. Execute: (a) encoded PowerShell, (b) LSASS dump with Mimikatz (lab environment only), (c) a scheduled task for persistence. Write a custom SPL alert for each. Confirm alerts fire.

- [ ] **Lab 3 — Threat Hunting Exercise:** Using the BOTS dataset or your own lab data, conduct a structured threat hunt for lateral movement. Hypothesis: "An attacker moved laterally using valid credentials." Search Event IDs 4648, 4624 (Logon Type 3), and correlate with Sysmon Event 3. Document your hypothesis, search queries, findings, and conclusion.

- [ ] **Lab 4 — Dashboard Build:** Create a SOC monitoring dashboard in Splunk covering: failed logins, process creation spikes, PowerShell execution count, and network connections to non-RFC1918 IPs. Present it as if explaining to a junior analyst.

---

## 📝 Operational Notes

- **SPL is not SQL:** `stats ... by` ≠ `GROUP BY`. SPL operates on a streaming pipeline — each command transforms the event stream. Think of it as a series of filters and transforms, not a database query.
- **Time is everything:** Always set your time range explicitly. Default "All time" searches are slow and expensive. Use `earliest=-24h@h latest=now` in your searches.
- **Index discipline:** In real environments, segregate data by `index` (e.g., `index=windows`, `index=network`, `index=endpoint`). Searching `index=*` is slow and noisy.
- **Splunk ES (Enterprise Security):** The premium SIEM layer on top of Splunk. It adds pre-built correlation rules, Risk Based Alerting (RBA), and a Notable Event workflow. You won't have this in the free tier — but know it exists and what it does.
- **Free alternatives:** If you don't want to pay for Splunk, ELK (Elastic Stack + Kibana) and Wazuh are functionally equivalent for lab work. See `ELK.md` and `Wazuh.md`.
