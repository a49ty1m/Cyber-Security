# Windows Incident Surface — Task 3: System Profile

## Objective

Once investigation tools are trusted, the next step is to **profile the system** — establish a baseline that everything else in the investigation will be compared against.

> **Don't investigate individual artefacts without first understanding the system they came from.**

---

# Mental Model

```text
WHAT SYSTEM AM I INVESTIGATING?
            ↓
WHO / WHERE IS IT?
            ↓
Hostname + IP + MAC
            ↓
WHAT OS IS RUNNING?
            ↓
Version + Build + Architecture
            ↓
WHEN?
            ↓
Install Date + Last Boot + Current Time
            ↓
WHAT CONFIGURATION DOES IT HAVE?
            ↓
System Policies
            ↓
BASELINE FOR FURTHER INVESTIGATION
```

---

# 1. System & Network Information

### Question

> What machine am I investigating, and how is it connected to the network?

```powershell
Get-CimInstance Win32_NetworkAdapterConfiguration -Filter "IPEnabled=TRUE" |
ft DNSHostName, IPAddress, MacAddress |
tee interfaces.txt
```

| Field         | Meaning                             |
| ------------- | ----------------------------------- |
| `DNSHostName` | Hostname of the system              |
| `IPAddress`   | IP addresses assigned to interfaces |
| `MacAddress`  | Hardware address of the interface   |

### Why it matters

```text
Hostname + IP + MAC → Host Identity
```

Particularly useful during live analysis while the system is connected to its regular network.

Correlate later with: network connections, logs, other systems, incident timelines.

### Why Hostname Matters

Knowing you're on `DB-01` vs `WEB-01` changes how you interpret everything else:

```text
Unknown process on WEB-01  ≠  Unknown process on DB-01
```

Finding that your compromised machine is `DB-01` (a database server) changes the priority and nature of every artefact you find after.

---

# 2. OS Version & Installation Details

### Question

> What operating system and build is running on the compromised host?

```powershell
Get-CimInstance -ClassName Win32_OperatingSystem |
fl CSName, Version, BuildNumber, InstallDate, LastBootUpTime, OSArchitecture |
tee sysinfo.txt
```

| Field            | Purpose              |
| ---------------- | -------------------- |
| `CSName`         | Computer name        |
| `Version`        | Windows version      |
| `BuildNumber`    | Specific OS build    |
| `InstallDate`    | OS installation date |
| `LastBootUpTime` | Last system boot     |
| `OSArchitecture` | 32-bit / 64-bit      |

### Why OS Information Matters

```text
Windows Version → Build Number → Patch / Security Baseline → Potential Anomalies
```

If an organization follows an **N-1 patching policy** and this host is significantly older than expected, that is worth investigating.

But:

> **An outdated system isn't automatically evidence of an attacker.**

It could be: misconfiguration, failed update, forgotten machine, or a policy exception. You need correlation with other evidence.

---

# 3. Install Date & Last Boot

Two particularly useful fields:

### Install Date

Helps establish how long the current OS installation has existed.

### Last Boot

Helps establish when the machine was last restarted.

```text
Last Boot → Processes started → Services started → User activity → Network activity
```

The boot time becomes an important reference point for later timeline analysis.

---

# 4. System Architecture

```text
OSArchitecture: 64-bit
```

Architecture provides context for: processes, executables, drivers, malware, and system binaries. It helps establish what kind of Windows environment you're dealing with.

---

# 5. Date & Time

### Question

> What time does the system think it is?

```powershell
Get-Date ; Get-TimeZone | tee systime.txt
```

### Why Time Matters in DFIR

Suppose you discover:

```text
10:15 — Suspicious login
10:17 — PowerShell execution
10:19 — Network connection
10:21 — File created
```

Without knowing the system's time configuration, you can't confidently interpret the timestamps.

```text
Timestamp + Timezone → Correct timeline
```

### TimeZone Command

```powershell
Get-TimeZone
```

Information includes: `Id`, `DisplayName`, `StandardName`, `DaylightName`, `BaseUtcOffset`.

Compare this system against: organization NTP server, other machines, incident timestamps, authentication logs, network logs.

---

# 6. System Policies

### Question

> Have system or Group Policies been modified in a suspicious way?

Attackers may modify policies to achieve their objectives.

**MITRE ATT&CK:** T1484.001 — Domain or Tenant Policy Modification

```powershell
Get-GPResultantSetOfPolicy `
-ReportType HTML `
-Path (Join-Path -Path (Get-Location).Path -ChildPath "RSOPReport.html")
```

This generates `RSOPReport.html` in the current directory, which can be opened in a browser.

### What Is the RSOP Report?

RSOP — **Resultant Set of Policy** — shows the policies actually being applied to the system/user, including:

- Computer and user policies
- Security configuration
- Administrative settings
- Other applied Group Policy settings

### Why Review Policies?

```text
System Policy → Compare with baseline → Expected?
    YES → Normal     NO → Investigate
```

Ask:
- Is this policy documented?
- Is it expected for this machine?
- Was it recently changed?
- Does it affect security controls?
- Does it correspond with other suspicious activity?

An unusual policy is an **indicator**, not automatically proof of compromise.

---

# 7. The Complete System Profile

After Task 3, you should have:

```text
SYSTEM
├── Hostname
├── Network
│   ├── IP
│   └── MAC
├── Operating System
│   ├── Version
│   ├── Build
│   ├── Architecture
│   ├── Install Date
│   └── Last Boot
├── Time
│   ├── Current Time
│   └── Timezone
└── Policies
    └── RSOP
```

This is your reference point for the rest of the investigation.

---

# 8. Evidence Files

| File                | Contents                                |
| ------------------- | --------------------------------------- |
| `interfaces.txt`    | Hostname, IP addresses, MAC addresses   |
| `sysinfo.txt`       | Computer name, version, build, install date, last boot, architecture |
| `systime.txt`       | Current system time, timezone           |
| `RSOPReport.html`   | Applied system/user policies            |

---

# 9. What Counts as an Anomaly?

Don't use: *"This looks weird, therefore attacker."*

Use: *"This differs from the expected baseline, so I need to investigate why."*

| Type    | Expected                    | Found              | Action                              |
| ------- | --------------------------- | ------------------ | ----------------------------------- |
| OS      | Current supported build     | Much older build   | Investigate patching/misconfiguration |
| Time    | Organization timezone       | Different timezone | Investigate configuration + timeline reliability |
| Policy  | Security policy enabled     | Policy disabled/modified | Investigate who/what changed it |
| Network | Known internal IP           | Unexpected interface/address | Investigate further            |

---

# 10. Investigation Workflow

```text
1. Identify the host and network identity (hostname, IP, MAC)
        ↓
2. Identify OS version, build, and architecture
        ↓
3. Record installation and boot times
        ↓
4. Establish current time and timezone
        ↓
5. Review applied policies
        ↓
6. Compare against organizational baseline
        ↓
7. Mark anomalies for deeper investigation
```

---

# 11. Important DFIR Principle

The most important lesson from Task 3 isn't the `Get-CimInstance` syntax — it's **baseline establishment**:

```text
Baseline → Observation → Comparison → Anomaly → Investigation
```

Without a baseline, you don't know whether something is actually unusual.

---

# Quick Command Reference

| Purpose           | Command                                                                         |
| ----------------- | ------------------------------------------------------------------------------- |
| Hostname, IP, MAC | `Get-CimInstance Win32_NetworkAdapterConfiguration -Filter "IPEnabled=TRUE"`    |
| OS details        | `Get-CimInstance -ClassName Win32_OperatingSystem`                              |
| Current time      | `Get-Date`                                                                      |
| Timezone          | `Get-TimeZone`                                                                  |
| Applied policies  | `Get-GPResultantSetOfPolicy -ReportType HTML -Path "RSOPReport.html"`           |

---

# What I Learned

- Establish the network identity of a Windows host: hostname, IP, MAC
- Determine the OS version, build, and architecture
- Record installation and boot times
- Record the system's current time and timezone
- Generate an RSOP policy report
- Compare system configuration against an organizational baseline
- Treat anomalies as investigation leads rather than immediately calling them malicious

### Most important mindset

```text
Don't ask: "Is this suspicious?"

First ask:  "What should this system look like?"
                    ↓
            Compare actual state
                    ↓
            Find deviations
                    ↓
            Investigate the deviations
```

The real purpose of **System Profile**: establish enough context about the compromised host that the artefacts you investigate later can be interpreted correctly.
