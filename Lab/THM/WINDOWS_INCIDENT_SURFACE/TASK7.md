# Windows Incident Surface — Task 7: Services & Scheduled Items

## Objective

Task 7 focuses on **background execution and persistence**.

Windows services and scheduled tasks can run programs without requiring a user to manually start them. Attackers can abuse these mechanisms to maintain persistence, execute malware, or impair security controls.

> **A service is only the starting point. Follow it to the file, hash the file, inspect its metadata, and correlate it with other evidence.**

---

# Mental Model

```text
Service
   ↓
Service configuration → Executable path → Process ID
   ↓
Executable file → Hash / metadata → Is it legitimate?
```

For scheduled tasks:

```text
Scheduled Task → Trigger → Executable / command → User or SYSTEM → Expected?
```

---

# 1. Running Services

### Question

> Which services are currently running, and what executable does each service use?

```powershell
Get-CimInstance -ClassName Win32_Service |
Where-Object { $_.State -eq 'Running' } |
Select-Object Name, DisplayName, State, StartMode, PathName, ProcessId |
ft -AutoSize |
tee services-active.txt
```

| Field         | Meaning                        |
| ------------- | ------------------------------ |
| `Name`        | Service's internal name        |
| `DisplayName` | Human-readable name            |
| `State`       | Running/stopped/etc.           |
| `StartMode`   | How the service starts         |
| `PathName`    | Executable used by the service |
| `ProcessId`   | PID of the running service     |

### Suspicious Indicators

A service becomes interesting when something doesn't match the expected baseline:

```text
Unknown service → Unexpected executable → Executable in Temp/AppData → Unusual startup mode
```

**Lab finding:** Service named **LMVCSS** whose executable was in a temporary directory, also connected to network activity found earlier.

---

# 2. Non-Running Services

```powershell
Get-CimInstance -ClassName Win32_Service |
Where-Object { $_.State -ne 'Running' } |
Select-Object Name, DisplayName, State, StartMode, PathName, ProcessId |
ft -AutoSize |
tee services-idle.txt
```

### Why Check Non-Running Services?

> **Stopped ≠ harmless**

An attacker may configure a service for persistence while it is currently stopped. A stopped service can still point to:
- Suspicious executable
- Malicious file
- Persistence mechanism
- Disabled security software

### Lab Finding: Aurora-Agent

```text
StartMode: Auto
State:     Stopped
```

At first glance: security agent failed. But it could also mean: **security tool intentionally disabled**.

**MITRE ATT&CK:** T1562 — Impair Defenses

Don't conclude *"Stopped security service = attacker."* Investigate the executable instead.

---

# 3. Service → File Investigation

If you find:

```text
Service: LMVCSS
Path: C:\...\Temp\INITIAL_LANTERN.exe
PID: XXXX
```

Don't stop at the service. Pivot to:

```text
Service → Executable path → File → SHA256 → File metadata
```

This allows you to determine whether the executable itself is suspicious.

---

# 4. Hashing a Suspicious Service Executable

```powershell
Get-FileHash C:\Users\Administrator\AppData\Local\Temp\INITIAL_LANTERN.exe |
tee service-file-1.txt
```

`Get-FileHash` calculates SHA256 by default:

```text
File → SHA256 → Unique fingerprint (64 hexadecimal characters)
```

Compare the hash against: known-good files, known-malicious samples, threat intelligence, trusted baselines.

### Why SHA256?

Attackers can rename `malware.exe` to `svchost.exe` — the filename changes, the hash doesn't.

> A SHA256 hash doesn't tell you "this file is malicious." It tells you "this exact file has this cryptographic fingerprint." You still need context.

---

# 5. File Metadata

```powershell
Get-Item -Path "C:\Users\Administrator\AppData\Local\Temp\INITIAL_LANTERN.exe" |
fl Name, FullName, Length, CreationTime, LastAccessTime, LastWriteTime, VersionInfo |
tee tmp-file-1-details.txt
```

| Field            | Why it matters            |
| ---------------- | ------------------------- |
| `Name`           | Filename                  |
| `FullName`       | Complete path             |
| `Length`         | File size                 |
| `CreationTime`   | When the file was created |
| `LastAccessTime` | Last recorded access      |
| `LastWriteTime`  | Last modification         |
| `VersionInfo`    | Version/product metadata  |

### Why Hash + Metadata Is Better

Instead of saying: *"INITIAL_LANTERN.exe looks suspicious,"* you can create a stronger evidence profile:

```text
File: INITIAL_LANTERN.exe
Path: Temporary directory
SHA256: <hash>
Created: <timestamp>
Modified: <timestamp>
Version information: <metadata>
```

Now the file can be identified and correlated with other evidence.

---

# 6. Comparing Two Files (Hash Matching)

```powershell
Get-FileHash "C:\Program Files\Aurora-Agent\aurora-agent-64.exe" | tee service-file-2.txt
Get-Item "C:\Program Files\Aurora-Agent\aurora-agent-64.exe" |
fl Name, FullName, Length, CreationTime, LastAccessTime, LastWriteTime, VersionInfo |
tee service-file-2-details.txt
```

If two files share the same SHA256:

```text
File A → SHA256 X
File B → SHA256 X
→ Identical file contents with extremely high confidence
```

This can reveal that a suspicious temporary file is actually a renamed copy of another executable.

---

# 7. Scheduled Items

### Question

> What programs are configured to execute automatically on a schedule?

```powershell
Get-ScheduledJob | tee scheduled-jobs.txt
```

Attackers can abuse scheduled tasks to execute malicious code automatically. Scheduled tasks can execute: programs, scripts, maintenance actions, security tools, persistence mechanisms.

### What a Task Contains

```text
Task → Trigger → Action → Executable → User/SYSTEM
```

When investigating one, ask:
- Who created it?
- When does it run?
- What does it execute?
- Which user runs it?
- Where is the executable? Is it legitimate?

---

# 8. Lab Finding: Aurora-Agent Scheduled Tasks

The room's task enumeration found:

```text
aurora-agent-program-update
aurora-agent-signature-update
```

These pointed to:

```text
C:\Program Files\Aurora-Agent\aurora-agent-util.exe
```

The room connects this back to the suspicious Aurora-Agent service. This is exactly the type of correlation you should practice.

---

# 9. Building the Attack Chain

```text
Suspicious Service (LMVCSS)
       ↓
Executable in temporary directory
       ↓
INITIAL_LANTERN.exe
       ↓
SHA256 + metadata
       ↓
Network activity from earlier tasks
```

And separately:

```text
Stopped Aurora-Agent Service
       ↓
Executable inspected (aurora-agent-64.exe)
       ↓
Scheduled Tasks found
       ↓
Aurora-Agent update tasks
       ↓
Same suspicious ecosystem
```

---

# 10. Running vs Non-Running: Key Difference

### Running service

```text
State = Running → Active process → Process ID available → Investigate live activity
```

### Non-running service

```text
State = Stopped → No active process currently → Configuration still exists → Executable can still be investigated
```

> **Don't investigate only what is currently running. A stopped service can still be an important persistence or defence-evasion artefact.**

---

# 11. Complete Suspicious Service Investigation Workflow

```text
Service → Name → DisplayName → State → StartMode → PathName → ProcessId
        ↓
Executable → SHA256 → File metadata
        ↓
Network activity → Scheduled tasks → Conclusion
```

Ask for each service:

```text
Why does it exist? → What's its startup mode? → What executable does it run?
        ↓
Where is that executable? → SHA256? → When was it created/modified?
        ↓
Legitimate version info? → Network communication? → Related scheduled tasks?
        ↓
Another artefact corroborates the finding?
```

---

# Quick Revision

| Question                      | Command                                                     |
| ----------------------------- | ----------------------------------------------------------- |
| What services are active?     | `Get-CimInstance Win32_Service \| Where-Object {$_.State -eq 'Running'}` |
| What services exist but idle? | `Get-CimInstance Win32_Service \| Where-Object {$_.State -ne 'Running'}` |
| File SHA256 fingerprint?      | `Get-FileHash <file>`                                       |
| File identity and timestamps? | `Get-Item <file> \| fl Name, FullName, Length, CreationTime, ...` |
| Scheduled jobs configured?    | `Get-ScheduledJob`                                          |

---

# Evidence Files

| File                      | Contains                                          |
| ------------------------- | ------------------------------------------------- |
| `services-active.txt`     | Running service inventory                         |
| `services-idle.txt`       | Non-running service inventory                     |
| `service-file-1.txt`      | SHA256 of INITIAL_LANTERN.exe                     |
| `tmp-file-1-details.txt`  | Metadata for INITIAL_LANTERN.exe                  |
| `service-file-2.txt`      | SHA256 of aurora-agent-64.exe                     |
| `service-file-2-details.txt` | Metadata for aurora-agent-64.exe               |
| `scheduled-jobs.txt`      | Scheduled job information                         |

---

# What I Learned

- Enumerate **running services** and **non-running services**
- Understand why stopped services can still matter
- Identify a service's executable path and Process ID
- Investigate the executable associated with a service
- Calculate **SHA256 hashes** with `Get-FileHash`
- Collect file timestamps and metadata with `Get-Item`
- Investigate scheduled jobs/tasks
- Correlate services with files, processes, scheduled tasks, and network activity

### Most important lesson

> **Don't only hunt what is running. Hunt what is configured to run.**

```text
SERVICE → Executable → SHA256 → File metadata → Process → Network → Scheduled Task → Attack Chain
```

A **running service** reveals active malicious behaviour. A **non-running service** reveals persistence or an intentionally disabled security component.
