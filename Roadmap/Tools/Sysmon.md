# 🔭 Sysmon (System Monitor): Complete Mastery Checklist

> **What is Sysmon?** Sysmon (System Monitor) is a free Windows system service and device driver from Microsoft Sysinternals that monitors and logs system activity to the Windows Event Log. It provides detailed information on process creation (with full command lines and parent processes), network connections, file creation, registry modifications, driver loads, DLL loads, and more — information that Windows's native audit logging either doesn't capture or captures incompletely. Sysmon is the single most important endpoint telemetry tool for Windows detection engineering.
>
> **Why does it exist?** Windows's built-in audit logging (Event IDs 4688, etc.) is insufficient for security operations. It lacks parent process information, full command lines are truncated, and many critical events simply aren't logged. Sysmon fills these gaps with 30+ event types covering the full spectrum of attacker behavior on Windows endpoints.
>
> **When to use it:** Deploy on every Windows host in your lab before running any attack simulations. Required for meaningful detection engineering in Phase 3. Used in combination with a SIEM (Splunk, Wazuh, ELK) that ingests Sysmon's Event Log.
>
> **When to avoid it:** Sysmon has performance overhead — on low-resource VMs, it can cause noticeable slowdown. Tune the configuration to reduce noise. On production hosts with very high process creation rates (e.g., build servers), excessive logging can fill disks quickly.
>
> **What mastering Sysmon unlocks:** High-fidelity Windows endpoint telemetry, the ability to detect virtually every attacker TTP at the endpoint level, solid foundation for writing Sigma rules, and the practical skills for MITRE ATT&CK coverage assessment.
>
> **Roadmap Stage / Module:** Stage 3: Side-Track A (Detection Engineering & SOC Operations)

---

## 🧭 Navigation

> [🏠 Master Roadmap](../README.md) · [🔧 Tools Index](README.md)

| Endpoint Telemetry | SIEM Platforms | Detection Rules | Forensics |
|:------------------|:--------------|:----------------|:----------|
| **🔭 Sysmon** (you are here) | [📊 Splunk](Splunk.md) | [🔎 Sigma](Sigma.md) | [🧠 Volatility](Volatility.md) |
| | [🐺 Wazuh](Wazuh.md) | [🦠 YARA](YARA.md) | [🔬 Autopsy](Autopsy.md) |
| | [📦 ELK](ELK.md) | | |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Installation & Configuration | 5 | 2–3 hours |
| 2 | Core Event Types (IDs 1–15) | 10 | 4–5 hours |
| 3 | Advanced Event Types (IDs 17–29) | 6 | 3–4 hours |
| 4 | Configuration Tuning & Filtering | 7 | 4–5 hours |
| 5 | SIEM Integration | 4 | 2–3 hours |
| 6 | Attack Simulation & Detection | 8 | 5–7 hours |
| 7 | Practical Labs | 4 | 4–6 hours |
| | **Total** | **44** | **~24–33 hours** |

**Prerequisites:** Windows administration basics. Phase 1 complete. Have a Windows VM (Windows 10/11 or Server 2019/2022) ready.

---

# PHASE 1: INSTALLATION & CONFIGURATION

---

## 1.1 Installation

```powershell
# Download Sysmon from Microsoft Sysinternals
# https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon

# Install with default configuration (minimal logging — not useful for security)
sysmon64.exe -accepteula -i

# Install with the SwiftOnSecurity config (the standard starting point)
# Download config: https://github.com/SwiftOnSecurity/sysmon-config
sysmon64.exe -accepteula -i sysmonconfig-export.xml

# Install with the Olaf Hartong modular config (more comprehensive)
# https://github.com/olafhartong/sysmon-modular
sysmon64.exe -accepteula -i sysmonconfig.xml

# Verify Sysmon is running
sc query sysmon64
Get-Service Sysmon64

# View Sysmon events in Event Viewer
# Applications and Services Logs → Microsoft → Windows → Sysmon → Operational
```

## 1.2 Management Commands

```powershell
# Update configuration (no reinstall needed)
sysmon64.exe -c sysmonconfig.xml

# Uninstall
sysmon64.exe -u

# View current configuration
sysmon64.exe -c

# Check Sysmon schema version
sysmon64.exe -s
```

## 1.3 Configuration File Structure

```xml
<Sysmon schemaversion="4.90">
  <HashAlgorithms>md5,sha256,IMPHASH</HashAlgorithms>
  <CheckRevocation/>  <!-- Check certificate revocation for signed binaries -->

  <EventFiltering>

    <!-- Event type rules go here -->
    <RuleGroup name="" groupRelation="or">
      <ProcessCreate onmatch="exclude">
        <!-- Exclude noisy, known-good processes -->
        <Image condition="is">C:\Windows\System32\svchost.exe</Image>
      </ProcessCreate>
    </RuleGroup>

  </EventFiltering>
</Sysmon>
```

- [ ] **`onmatch="include"` vs `onmatch="exclude"`:** Sysmon can be configured to log everything and exclude known-good (whitelist approach) or log nothing and include specific items (blacklist approach). The standard approach is **exclude known-good noise**, which is what SwiftOnSecurity's config does.
- [ ] **`groupRelation="or"` vs `"and"`:** Within a RuleGroup, conditions are combined with OR (any match triggers the rule) or AND (all conditions must match). Critical to understand when building compound filters.

---

# PHASE 2: CORE EVENT TYPES

---

## 2.1 Event ID 1 — Process Create

**The most valuable Sysmon event.** Logs every process creation with: full image path, command line, parent process image + command line, user, GUID, file hashes, and whether the process was started in a new session.

```powershell
# Example: Attacker runs encoded PowerShell
# Sysmon Event ID 1 captures:
# Image: C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
# CommandLine: powershell.exe -EncodedCommand JABjAG0AZAA...
# ParentImage: C:\Windows\System32\cmd.exe
# ParentCommandLine: cmd.exe /c powershell.exe -enc JABjAG0AZAA...
# User: DOMAIN\victim
# Hashes: MD5=...,SHA256=...,IMPHASH=...
```

**Critical parent-child relationships to know:**

| Parent | Suspicious Child | TTP |
|:-------|:----------------|:----|
| `winword.exe` / `excel.exe` | `cmd.exe`, `powershell.exe`, `wscript.exe` | Macro execution (T1566) |
| `powershell.exe` | `cmd.exe`, any LOLBin | Staged execution |
| `svchost.exe` | `cmd.exe`, `powershell.exe` | Service exploitation |
| `explorer.exe` | `wscript.exe`, `mshta.exe`, `rundll32.exe` | Fileless execution |
| `msiexec.exe` | any payload | Malicious installer |

- [ ] **IMPHASH:** The Import Hash — a hash of the DLL import table, unique to each compiled binary. Different malware samples of the same family share the same IMPHASH. Useful for threat clustering.

## 2.2 Event ID 3 — Network Connection

Logs every outbound TCP/UDP connection: source/destination IP, port, hostname (DNS lookup at connection time), and the process that made the connection.

```xml
<!-- Exclude common noisy legitimate connections -->
<NetworkConnect onmatch="exclude">
  <Image condition="is">C:\Windows\System32\svchost.exe</Image>
  <DestinationPort condition="is">443</DestinationPort>
  <!-- This excludes ALL svchost HTTPS — too broad. Be more specific: -->
</NetworkConnect>

<!-- Better: only exclude specific known-good destinations -->
<NetworkConnect onmatch="exclude">
  <Image condition="end with">chrome.exe</Image>
</NetworkConnect>
```

**Detection use cases:** C2 beacon detection (process connecting to unusual IPs/ports), lateral movement (psexec.exe/wmic.exe making network connections), data exfiltration (large volume of connections from unusual processes).

## 2.3 Event ID 7 — Image Loaded (DLL Load)

Logs every DLL loaded by a process (signed/unsigned, file path, hash). High-noise event — enable with caution.

- [ ] **DLL hijacking detection:** Legitimate DLL loaded from unusual path (e.g., `C:\Users\Public\version.dll` instead of `C:\Windows\System32\version.dll`).
- [ ] **Reflective DLL injection:** A DLL loaded with no file path (`\Device\HarddiskVolume...` empty or missing) — the DLL was loaded from memory, not disk.

## 2.4 Event ID 8 — CreateRemoteThread

Logs when one process creates a thread in another process — the primary mechanism of **process injection** (T1055).

```
# Suspicious patterns:
# SourceImage: lolbin or attacker tool
# TargetImage: explorer.exe, svchost.exe, or any innocent process
# StartAddress: 0x... (unusual memory region)
```

## 2.5 Event ID 10 — Process Access (LSASS Dump Detection)

Logs when one process opens a handle to another. The most important detection for **credential dumping** (T1003.001).

```
# Critical alert: any process opening LSASS with sensitive GrantedAccess rights
# GrantedAccess values indicating credential dumping:
# 0x1010, 0x1410, 0x143a — PROCESS_VM_READ + PROCESS_QUERY_INFORMATION
# TargetImage: C:\Windows\System32\lsass.exe
```

## 2.6 Event ID 11 — File Create

Logs when a file is created or overwritten. Used to detect dropper activity (malware writing payloads to disk), webshell creation, and staged tools.

## 2.7 Event IDs 12, 13, 14 — Registry Events

- **12:** Registry key/value created or deleted
- **13:** Registry value set
- **14:** Registry key/value renamed

**Detection use cases:** Persistence via Run keys (`HKCU\Software\Microsoft\Windows\CurrentVersion\Run`), SAM hive modifications, AMSI bypass via registry, COM hijacking.

## 2.8 Event ID 22 — DNS Query

Logs every DNS query made by every process — domain, result, and which process made the query. Critical for **C2 domain detection** and **DNS tunneling** (T1071.004).

```
# Suspicious DNS patterns:
# Long subdomain queries (DNS tunneling): a1b2c3d4.evil.com
# High-entropy subdomains (DGA): xkwqprtz.malware.net
# Unusual process making DNS queries: msiexec.exe, regsvr32.exe
```

---

# PHASE 3: ADVANCED EVENT TYPES

---

| Event ID | Description | Key Use Case |
|:---------|:------------|:-------------|
| 17 | Pipe Created | Named pipe C2 communication (Cobalt Strike, Sliver) |
| 18 | Pipe Connected | Client connecting to C2 named pipe |
| 19 | WMI Event Filter registered | WMI persistence |
| 20 | WMI Event Consumer registered | WMI persistence |
| 21 | WMI Event Consumer bound to filter | WMI persistence |
| 23 | File Delete | Evidence of attacker cleaning up |
| 25 | Process Tampering | Process image replacement (hollowing indicator) |
| 26 | File Delete Logged | File deletion with content logged (requires hash verification) |
| 29 | File Executable Detected | New executable dropped to disk |

- [ ] **Named pipe monitoring (Event 17/18):** Many C2 frameworks (Cobalt Strike, Sliver, Metasploit) communicate between processes via named pipes. Default pipe names are well-known IOCs: `\MSSE-*`, `\postex_*`, `\msagent_*`. Detecting these is high-fidelity C2 indication.
- [ ] **WMI persistence (Event 19/20/21):** WMI subscriptions are one of the stealthiest persistence mechanisms — they survive reboots, leave minimal disk artifacts, and are missed by most AV. Event 19/20/21 are the only reliable detection without specialist tools.

---

# PHASE 4: CONFIGURATION TUNING & FILTERING

---

## 4.1 The SwiftOnSecurity Config (Starting Point)

```bash
# Download
wget https://raw.githubusercontent.com/SwiftOnSecurity/sysmon-config/master/sysmonconfig-export.xml

# This config:
# - Logs process creation (Event 1) with broad include, excludes common LOLBin noise
# - Logs network connections (Event 3) excluding browsers and updaters
# - Logs driver loads (Event 6) with include for unsigned drivers
# - Logs LSASS access (Event 10) - all access
# - Logs file creation (Event 11) in temp/startup paths
# - Logs run key modifications (Event 13)
# - Logs DNS queries (Event 22) excluding noisy domains
```

## 4.2 Writing Custom Exclusions (Noise Reduction)

```xml
<!-- Exclude Windows Defender scanning processes (creates massive Event ID 1 noise) -->
<ProcessCreate onmatch="exclude">
  <Image condition="begin with">C:\ProgramData\Microsoft\Windows Defender\</Image>
</ProcessCreate>

<!-- Exclude backup agents -->
<NetworkConnect onmatch="exclude">
  <Image condition="contains">backup</Image>
  <DestinationPort condition="is">445</DestinationPort>
</NetworkConnect>

<!-- Exclude Teams/Zoom DNS noise -->
<DnsQuery onmatch="exclude">
  <QueryName condition="end with">.teams.microsoft.com</QueryName>
  <QueryName condition="end with">.zoom.us</QueryName>
</DnsQuery>
```

## 4.3 Writing Detection Includes

```xml
<!-- Alert on any process that loads a DLL from a user-writable path -->
<ImageLoad onmatch="include">
  <ImageLoaded condition="begin with">C:\Users\</ImageLoaded>
  <ImageLoaded condition="begin with">C:\ProgramData\</ImageLoaded>
  <ImageLoaded condition="begin with">C:\Windows\Temp\</ImageLoaded>
</ImageLoad>

<!-- Alert on LSASS access (high-fidelity credential dump indicator) -->
<ProcessAccess onmatch="include">
  <TargetImage condition="end with">lsass.exe</TargetImage>
</ProcessAccess>
```

---

# PHASE 5: SIEM INTEGRATION

---

```powershell
# Forward Sysmon logs via Winlogbeat (for ELK)
# winlogbeat.yml:
winlogbeat.event_logs:
  - name: Microsoft-Windows-Sysmon/Operational
    event_id: 1,3,7,8,10,11,12,13,14,17,18,19,20,21,22,23,25,26,29

# Forward via Splunk Universal Forwarder
# inputs.conf:
[WinEventLog://Microsoft-Windows-Sysmon/Operational]
disabled = false
renderXml = true
index = sysmon
```

- [ ] **Sysmon in Wazuh:** Wazuh has built-in Sysmon decoders. After deploying the agent on a Windows host with Sysmon, Wazuh automatically parses Sysmon XML events and maps fields. No extra configuration needed.

---

# PHASE 6: ATTACK SIMULATION & DETECTION

---

Run these in your lab Windows VM and verify Sysmon captures each:

- [ ] **T1059.001 — PowerShell encoded command:** `powershell.exe -enc JABjAG0AZAA=` → Should trigger Event ID 1 with encoded command in CommandLine.
- [ ] **T1003.001 — LSASS dump:** Run `procdump.exe -ma lsass.exe lsass.dmp` or open Task Manager → lsass.exe → Create Dump File → Should trigger Event ID 10 with `GrantedAccess: 0x1fffff`.
- [ ] **T1053.005 — Scheduled Task:** `schtasks /create /tn "Update" /tr "cmd.exe /c whoami" /sc onstart` → Should trigger Event ID 12/13 (registry) and a service Event ID 1.
- [ ] **T1071.004 — DNS tunneling:** Use `dnscat2` or `iodine` in lab → Should trigger Event ID 22 with high-entropy subdomain queries.
- [ ] **T1055 — Process injection:** Use a benign injection PoC (e.g., inject calculator shellcode into notepad) → Should trigger Event ID 8 (CreateRemoteThread).
- [ ] **T1027 — Obfuscation:** `certutil.exe -encode payload.exe payload.b64` → Event ID 1 captures certutil with encode flag — classic LOLBin indicator.
- [ ] **T1218.011 — Rundll32:** `rundll32.exe javascript:"\..\mshtml,RunHTMLApplication ";alert('test')` → Event ID 1 captures unusual rundll32 CommandLine.
- [ ] **Named pipe C2 simulation:** Use Metasploit Meterpreter named pipe transport → Event ID 17/18 captures named pipe creation.

---

# PHASE 7: PRACTICAL LABS

---

- [ ] **Lab 1 — Telemetry Baseline:** Install Sysmon with SwiftOnSecurity config on a clean Windows VM. Run normal user activity (open browser, Word, notepad) for 30 minutes. Review Event Viewer to understand what "normal" Sysmon output looks like before any attacks.

- [ ] **Lab 2 — Attack Coverage Mapping:** Execute one technique from each MITRE ATT&CK tactic (Initial Access, Execution, Persistence, Privilege Escalation, Defense Evasion, Credential Access, Discovery, Lateral Movement). For each, identify which Sysmon Event ID captures it.

- [ ] **Lab 3 — Config Hardening:** Start with a verbose config generating 10,000+ events/hour. Progressively add exclusions to reduce volume by 80% without losing detection coverage for the attacks in Lab 2. Document every exclusion added and its justification.

- [ ] **Lab 4 — Sigma Rule Writing from Sysmon Events:** Pick one attack from Lab 2. Look at the raw Sysmon Event fields in Event Viewer. Write a Sigma rule that would detect it. Test the rule using `sigma-cli` to convert it to Splunk SPL and verify it fires against log data.

---

## 📝 Operational Notes

- **Schema versioning:** Sysmon configuration files have a `schemaversion` attribute. Always match the schema version to your installed Sysmon version. Use `sysmon64.exe -s` to see the current schema. Mismatched schemas cause configuration parsing failures.
- **Event ID 255 — Sysmon error:** If you see Event ID 255 in the Sysmon log, the configuration has an error. Check `wevtutil qe Microsoft-Windows-Sysmon/Operational /q:"*[System[EventID=255]]"` for details.
- **Sysmon vs EDR:** Commercial EDR products (CrowdStrike, SentinelOne, Microsoft Defender for Endpoint) provide richer telemetry than Sysmon. But Sysmon is free and gives you 80% of the visibility at 0% of the cost — invaluable for labs and small teams.
- **Log retention:** Sysmon events go to the Windows Event Log. By default, Windows Event Logs have small size limits (20MB). Increase the Sysmon Operational log size: `wevtutil sl Microsoft-Windows-Sysmon/Operational /ms:2147483648` (2GB).
- **GUID tracking:** Every process gets a unique GUID (`ProcessGuid` field). You can correlate all Sysmon events for the same process instance across Event IDs using this GUID — critical for building attack chains.
