# 🐺 Wazuh: Complete Mastery Checklist

> **What is Wazuh?** Wazuh is a free and open-source security platform that provides unified SIEM and XDR (Extended Detection and Response) capabilities. It combines endpoint detection (via a lightweight agent), log analysis, vulnerability detection, file integrity monitoring (FIM), configuration auditing, and active response — all integrated with an Elastic Stack backend for storage and Kibana for visualization. Wazuh is effectively a pre-configured, security-focused ELK stack with built-in detection rules and an agent ecosystem.
>
> **Why does it exist?** Splunk and commercial SIEMs are expensive. Pure ELK requires extensive manual configuration to become a security tool. Wazuh bridges the gap: it's open-source, fully featured for security operations, and ships with thousands of built-in detection rules aligned to MITRE ATT&CK.
>
> **When to use it:** Personal lab SIEM (free, unlimited ingest), small-to-medium business security monitoring, SOC practice where Splunk licensing is unavailable, and as the primary security platform in any cost-constrained environment.
>
> **When to avoid it:** When you need enterprise-grade support SLAs, Splunk-specific integrations, or the mature Elastic Security SIEM module with its full rule ecosystem. For pure detection rule writing practice without infrastructure overhead, use a Splunk trial instead.
>
> **What mastering Wazuh unlocks:** Full SOC operations capability without any licensing cost, understanding of agent-based endpoint monitoring, FIM and compliance checking, active response automation, and hands-on experience with the platform used by many real-world MSPs and SMB security teams.
>
> **Roadmap Stage / Module:** Stage 3: Side-Track A (Detection Engineering & SOC Operations)

---

## 🧭 Navigation

> [🏠 Master Roadmap](../README.md) · [🔧 Tools Index](README.md)

| SIEM Platforms | Telemetry | Detection Rules | Forensics |
|:--------------|:----------|:----------------|:----------|
| [📊 Splunk](Splunk.md) | [🔭 Sysmon](Sysmon.md) | [🔎 Sigma](Sigma.md) | [🧠 Volatility](Volatility.md) |
| **🐺 Wazuh** (you are here) | [📦 Plaso](Plaso.md) | [🦠 YARA](YARA.md) | [🔬 Autopsy](Autopsy.md) |
| [📦 ELK](ELK.md) | | | |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Server Installation & Agent Deployment | 6 | 3–4 hours |
| 2 | Log Analysis & Built-in Rules | 7 | 3–4 hours |
| 3 | Custom Rule Writing | 7 | 4–6 hours |
| 4 | File Integrity Monitoring (FIM) | 4 | 2–3 hours |
| 5 | Vulnerability Detection & Compliance | 4 | 2–3 hours |
| 6 | Active Response | 4 | 2–3 hours |
| 7 | Practical Labs | 4 | 5–8 hours |
| | **Total** | **36** | **~21–31 hours** |

**Prerequisites:** Linux fundamentals (Phase 1 complete). Basic understanding of Syslog, JSON, and what a SIEM does.

---

# PHASE 1: SERVER INSTALLATION & AGENT DEPLOYMENT

---

## 1.1 Wazuh Server Installation (All-in-One)

```bash
# Download and run the Wazuh installation assistant
curl -sO https://packages.wazuh.com/4.7/wazuh-install.sh
curl -sO https://packages.wazuh.com/4.7/config.yml

# Edit config.yml to set node names and IPs
# Then run:
sudo bash wazuh-install.sh -a

# This installs: Wazuh Manager, Wazuh Indexer (Elasticsearch), Wazuh Dashboard (Kibana)
# Access the dashboard: https://YOUR_IP
# Default credentials displayed at end of install
```

> [!IMPORTANT]
> Wazuh requires at minimum 4GB RAM and 25GB disk. Use an 8GB RAM VM for comfortable operation. The all-in-one install script handles everything including certificates.

## 1.2 Agent Deployment

```bash
# Linux agent installation (run on endpoint to monitor)
# Replace WAZUH_MANAGER with your Wazuh server IP
curl -s https://packages.wazuh.com/key/GPG-KEY-WAZUH | gpg --no-default-keyring \
  --keyring gnupg-ring:/usr/share/keyrings/wazuh.gpg --import
echo "deb [signed-by=/usr/share/keyrings/wazuh.gpg] https://packages.wazuh.com/4.x/apt/ stable main" | \
  sudo tee /etc/apt/sources.list.d/wazuh.list
sudo apt update && sudo apt install wazuh-agent

# Configure agent to point to manager
sudo sed -i 's/MANAGER_IP/YOUR_WAZUH_SERVER_IP/' /var/ossec/etc/ossec.conf
sudo systemctl start wazuh-agent
sudo systemctl enable wazuh-agent

# Windows agent (PowerShell — run on Windows VM as Administrator)
# Download the MSI from packages.wazuh.com
# Or deploy with PowerShell:
Invoke-WebRequest -Uri https://packages.wazuh.com/4.x/windows/wazuh-agent-4.7.0-1.msi -OutFile wazuh-agent.msi
msiexec.exe /i wazuh-agent.msi /q WAZUH_MANAGER="YOUR_SERVER_IP" WAZUH_AGENT_NAME="win-vm"
net start wazuhdagent
```

- [ ] **Agent groups:** In the Wazuh dashboard, create agent groups (e.g., "windows-endpoints", "linux-servers"). Groups allow applying different configurations and rules to different endpoint types.
- [ ] **Agent registration:** Wazuh uses a registration service to authenticate new agents. The all-in-one install configures this automatically. In manual deployments, use `sudo /var/ossec/bin/agent-auth -m MANAGER_IP`.

---

# PHASE 2: LOG ANALYSIS & BUILT-IN RULES

---

## 2.1 Wazuh Rule Architecture

```
/var/ossec/rules/              # Built-in rules (DO NOT EDIT)
/var/ossec/etc/rules/          # Custom rules (your additions here)
/var/ossec/etc/ossec.conf      # Main configuration file
/var/ossec/logs/alerts/        # Alert logs
/var/ossec/logs/ossec.log      # Manager logs (debug/errors)
```

- [ ] **Rule severity levels (1–15):**
  - 1–3: Information events (login, config changes)
  - 4–6: Low severity alerts
  - 7–11: Medium severity (attack indicators)
  - 12–15: High severity (active attacks, rootkits, policy violations)
  - Default alert threshold is **level 3** — alerts below 3 are logged but not shown as alerts.

## 2.2 Built-in Rule Categories

| Rule File | Coverage |
|:----------|:---------|
| `0015-ossec_rules.xml` | OSSEC core agent events |
| `0020-syslog_rules.xml` | Linux syslog (auth, sudo, su) |
| `0040-sshd_rules.xml` | SSH brute force, authentication |
| `0580-win-security_rules.xml` | Windows Security Event Log |
| `0575-win-application_rules.xml` | Windows Application log |
| `0915-suricata_rules.xml` | Suricata NIDS integration |

## 2.3 Searching Alerts in the Dashboard

In Wazuh Dashboard → Security Events:
```
# KQL examples (same as Kibana KQL)
rule.level:>=7
agent.name:"win-vm" AND rule.groups:"authentication_failed"
data.win.eventdata.subjectUserName:"administrator"
rule.mitre.id:"T1059.001"
```

---

# PHASE 3: CUSTOM RULE WRITING

---

## 3.1 Wazuh Rule XML Syntax

```xml
<!-- /var/ossec/etc/rules/local_rules.xml -->

<!-- Rule structure -->
<group name="custom_rules,">

  <!-- Detect PowerShell with encoded commands -->
  <rule id="100001" level="12">
    <if_group>windows</if_group>
    <field name="win.eventdata.commandLine" type="pcre2">(?i)-(?:EncodedCommand|enc|e)\s+[A-Za-z0-9+/]{20,}</field>
    <description>PowerShell encoded command execution detected</description>
    <mitre>
      <id>T1059.001</id>
    </mitre>
    <group>attack,execution</group>
  </rule>

  <!-- Brute force detection: 5 failures in 2 minutes -->
  <rule id="100002" level="10" frequency="5" timeframe="120">
    <if_matched_group>authentication_failed</if_matched_group>
    <same_source_ip />
    <description>Brute force attack: multiple authentication failures from same IP</description>
    <mitre>
      <id>T1110</id>
    </mitre>
  </rule>

  <!-- LSASS access detection (Sysmon Event ID 10) -->
  <rule id="100003" level="14">
    <if_group>sysmon</if_group>
    <field name="win.system.eventID">^10$</field>
    <field name="win.eventdata.targetImage" type="pcre2">(?i)lsass\.exe</field>
    <description>Potential credential dumping: LSASS process accessed</description>
    <mitre>
      <id>T1003.001</id>
    </mitre>
  </rule>

</group>
```

## 3.2 Key Rule Attributes

| Attribute | Description |
|:----------|:------------|
| `id` | Unique rule ID (custom rules: 100000–109999) |
| `level` | Severity 1–15 |
| `frequency` | Number of times to match within `timeframe` seconds |
| `timeframe` | Time window for frequency rules (seconds) |
| `if_matched_sid` | Trigger if a specific rule ID fired previously |
| `same_source_ip` | Group events by source IP |
| `field` | Match a specific decoded field by name |
| `match` | Simple string match in `full_log` |
| `regex` | POSIX regex match |
| `pcre2` | Perl-compatible regex (preferred) |

## 3.3 Testing Custom Rules

```bash
# Test a rule against a log sample without restarting the manager
sudo /var/ossec/bin/wazuh-logtest

# Type or paste a log line and press Enter
# Wazuh will decode it and show which rules match

# Example: test SSH failed login detection
Dec 10 12:00:00 myhost sshd[1234]: Failed password for invalid user admin from 1.2.3.4 port 54321 ssh2
```

```bash
# Restart rules after changes (no full restart needed for rules)
sudo systemctl restart wazuh-manager

# Validate config before restart
sudo /var/ossec/bin/wazuh-analysisd -t
```

---

# PHASE 4: FILE INTEGRITY MONITORING (FIM)

---

## 4.1 Configuring FIM

```xml
<!-- In /var/ossec/etc/ossec.conf -->
<syscheck>
  <!-- Enable FIM -->
  <disabled>no</disabled>

  <!-- Scan interval (seconds) -->
  <frequency>300</frequency>

  <!-- Directories to monitor -->
  <directories check_all="yes" report_changes="yes" realtime="yes">/etc</directories>
  <directories check_all="yes" report_changes="yes">/usr/bin,/usr/sbin</directories>
  <directories check_all="yes">/var/www/html</directories>

  <!-- Ignore transient files -->
  <ignore>/etc/mtab</ignore>
  <ignore>/etc/hosts.deny</ignore>
  <ignore type="sregex">^/proc</ignore>
</syscheck>
```

- [ ] **What FIM monitors:** File hash (MD5, SHA-1, SHA-256), permissions, ownership, file size, inode, last modification time. On Linux, it uses `inotify` for real-time detection.
- [ ] **Use cases:** Detect webshell drops in `/var/www/html`, unauthorized binary modifications in `/usr/bin`, configuration tampering in `/etc/passwd` or `/etc/shadow`, and SUID binary additions.
- [ ] **FIM + rootkit detection:** Wazuh combines FIM with rootkit checks (`rootcheck`) that look for hidden processes, hidden ports, suspicious file attributes, and kernel module anomalies.

---

# PHASE 5: VULNERABILITY DETECTION & COMPLIANCE

---

## 5.1 Vulnerability Detector

```xml
<!-- Enable vulnerability detector in ossec.conf -->
<vulnerability-detector>
  <enabled>yes</enabled>
  <interval>12h</interval>
  <min_full_scan_interval>6h</min_full_scan_interval>
  <run_on_start>yes</run_on_start>

  <provider name="canonical">
    <enabled>yes</enabled>
    <os>bionic</os>
    <os>focal</os>
    <os>jammy</os>
    <update_interval>1h</update_interval>
  </provider>

  <provider name="nvd">
    <enabled>yes</enabled>
    <update_interval>1h</update_interval>
  </provider>
</vulnerability-detector>
```

- [ ] **Vulnerability scan flow:** Wazuh agent inventories all installed packages → sends to manager → manager correlates against CVE databases (NVD, Ubuntu USN, Red Hat Errata, Windows patches) → flags unpatched CVEs with severity scores.

## 5.2 CIS Benchmark Compliance (SCA)

```bash
# Security Configuration Assessment runs automatically
# View results: Wazuh Dashboard → Agents → [Agent] → Security Configuration Assessment

# The SCA policy files live here (check which apply to your OS)
ls /var/ossec/ruleset/sca/
# cis_debian10.yml, cis_ubuntu20-04.yml, cis_rhel8.yml, etc.
```

---

# PHASE 6: ACTIVE RESPONSE

---

```xml
<!-- Define a command in ossec.conf -->
<command>
  <name>firewall-drop</name>
  <executable>firewall-drop</executable>
  <timeout_allowed>yes</timeout_allowed>
</command>

<!-- Apply command as active response -->
<active-response>
  <command>firewall-drop</command>
  <location>local</location>
  <rules_group>authentication_failures</rules_group>
  <timeout>600</timeout>  <!-- Block for 10 minutes -->
</active-response>
```

- [ ] **Active response scripts:** Wazuh ships default scripts: `firewall-drop` (adds iptables rule), `host-deny` (adds to `/etc/hosts.deny`), `disable-account` (locks Linux user). Know where they live: `/var/ossec/active-response/bin/`.
- [ ] **Active response risk:** Auto-blocking based on IDS alerts can cause self-inflicted outages (blocking legitimate traffic, admins locked out). Always test in lab, never blindly deploy to production.

---

# PHASE 7: PRACTICAL LABS

---

- [ ] **Lab 1 — Full Deployment:** Install Wazuh server + deploy agents on (a) a Kali/Ubuntu VM and (b) a Windows VM with Sysmon. Verify both agents appear as Active in the dashboard with events flowing.

- [ ] **Lab 2 — Attack & Detect:** From Kali, run `hydra` against the SSH on the Ubuntu VM. Watch the Wazuh dashboard — confirm brute force alerts fire. Then SSH in successfully and confirm the success event appears too.

- [ ] **Lab 3 — Custom Rule:** Write a custom Wazuh rule (rule ID 100001+) that fires at level 12 when PowerShell is run with an encoded command argument. Test it using `wazuh-logtest`. Execute the trigger on the Windows VM and confirm the alert appears in the dashboard.

- [ ] **Lab 4 — FIM in Action:** Add `/var/www/html` to FIM monitoring with `realtime=yes`. Start an Apache server and deploy a file (simulating a webshell drop). Confirm Wazuh generates an FIM alert within 60 seconds. Check what fields are populated in the alert (file hash, path, permissions).

---

## 📝 Operational Notes

- **Wazuh vs Splunk:** Wazuh has weaker SPL/KQL query capabilities than Splunk. Complex correlation queries are harder. For detection engineering with heavy SPL usage, Splunk's query language is richer. For out-of-box detection coverage and zero licensing cost, Wazuh wins.
- **Rule ID namespace:** Custom rules must be in the range 100000–109999 to avoid conflicts with built-in rules. Check `/var/ossec/rules/` to see which IDs are taken.
- **Wazuh 4.x vs 3.x:** Major architectural changes in 4.x — the indexer (Elasticsearch) and dashboard (Kibana fork) are now officially part of Wazuh. Older 3.x docs that reference separate ELK installation are outdated.
- **Memory tuning:** The Wazuh Indexer (Elasticsearch) JVM heap should be 50% of available RAM. Edit `/etc/wazuh-indexer/jvm.options` to set `-Xms2g -Xmx2g` for a 4GB RAM system.
- **Integration with Shuffle:** Wazuh integrates with Shuffle SOAR (open-source SOAR platform) for automated incident response workflows — useful for Phase 3 SOC automation coverage.
