# Windows Incident Surface — Task 8: Processes & Directories

## Objective

**Live process analysis and suspicious directory investigation.**

Processes show what is executing right now. By examining owner, PID, parent PID, command line, and executable path, you can uncover suspicious process relationships and execution chains.

> **Don't investigate processes, files, directories, and network connections as separate things. Connect them.**

---

# Mental Model

```text
Process → PID → Parent PID → Parent Process → User
        ↓
Command Line → Executable Path → File on Disk → Network Activity → Attack Chain
```

For directories:

```text
Suspicious Process → Executable Path → Directory
        ↓
Other Files → Scripts / Payloads → Hash + Metadata
```

---

# 1. Enumerate Running Processes

```powershell
Get-CimInstance -ClassName Win32_Process |
ForEach-Object {
    $owner = Invoke-CimMethod -InputObject $_ -MethodName GetOwner
    [PSCustomObject]@{
        User            = $owner.User
        ProcessId       = $_.ProcessId
        ParentProcessId = $_.ParentProcessId
        Name            = $_.Name
        CommandLine     = if ($_.CommandLine.Length -gt 60) {
            $_.CommandLine.Substring(0, 60) + '...'
        } else { $_.CommandLine }
        Path            = $_.Path
    }
} |
ft -AutoSize |
tee process-summary.txt
```

| Field             | Meaning                             |
| ----------------- | ----------------------------------- |
| `User`            | Account running the process         |
| `ProcessId`       | Unique ID of the process            |
| `ParentProcessId` | PID of the process that launched it |
| `Name`            | Process executable name             |
| `CommandLine`     | How the process was launched        |
| `Path`            | Location of the executable          |

This is much better than `Get-Process` alone — you're building relationships between processes.

---

# 2. PIDs and Parent PIDs

**PID** uniquely identifies a process and lets you connect it to other evidence:

```text
PID → Network connection → Remote IP → Remote Port
```

**ParentProcessId** tells you which process launched the current one:

```text
powershell.exe → cmd.exe → malware.exe
```

This lets you reconstruct a **process tree**:

```text
Parent Process
      │
      ├── Child Process
      └── Child Process
```

Suspicious example:

```text
Unexpected Process → cmd.exe → ssh.exe
```

The **relationship itself** becomes evidence.

---

# 3. Process Names Are Not Enough

Don't investigate only:

```text
Name = svchost.exe
```

Investigate:

```text
Name + Path + User + PID + Parent PID + Command Line
```

For example:

```text
svchost.exe from C:\Windows\System32\
    ≠
svchost.exe from C:\Users\Administrator\AppData\Local\Temp\
```

---

# 4. Command Line Analysis

The `CommandLine` field reveals **how the process was launched**:

```text
powershell.exe -enc ...    → Encoded command (suspicious)
cmd.exe /c ...             → Command execution
```

The command is truncated to 60 characters to keep output manageable while preserving the beginning.

---

# 5. Important Findings: SSH & Aurora

The room connects process investigation with network findings from Task 5.

Earlier: multiple `ssh.exe` connections observed.

Now: process analysis shows some SSH instances had the suspicious **aurora-agent** process as their parent.

```text
Task 5: Network connection → ssh.exe
        ↓
Task 8: Process investigation → Parent Process → aurora-agent
```

This is cross-task correlation in action.

---

# 6. User Temp Directories

```powershell
Get-ChildItem -Path "C:\Users\*" -Force |
Where-Object { $_.PSIsContainer } |
ForEach-Object {
    Get-ChildItem -Path "$($_.FullName)\AppData\Local\Temp\*" -Recurse -Force -ErrorAction SilentlyContinue |
    Select-Object @{Name="User"; Expression={$_.FullName.Split('\')[2]}}, FullName, Name, Extension
} |
ft -AutoSize |
tee temp-folders.txt
```

### Why Check Temp Directories?

Attackers may use them because they are writable, less monitored, and convenient for staging.

```text
Temp file ≠ Malware automatically

Temp file → Is it executable? → Is it running? → Who owns it?
        ↓
When was it created? → What is its hash? → Does it communicate?
```

### Focused Investigation

```powershell
Get-ChildItem -Path "C:\Users\Administrator\AppData\Local\Temp\*" -Recurse -Force |
ft FullName, Name, Extension
```

Move from: **Broad enumeration → Interesting location → Focused investigation**

---

# 7. Suspicious Temp Files Found

```text
INITIAL_LANTERN.exe         → Connected to suspicious service
Invoke-SocksProxy.psm1      → PowerShell proxy module (very suspicious)
```

The directory `C:\Users\Administrator\AppData\SpcTmp\` contains both files — making the directory itself an investigation lead.

```text
Suspicious Process → INITIAL_LANTERN.exe → Suspicious Temp Directory → Invoke-SocksProxy.psm1
```

---

# 8. Hash a Suspicious File

```powershell
Get-FileHash C:\Users\Administrator\AppData\Local\Temp\Invoke-SocksProxy.psm1
```

SHA256 by default — the fingerprint survives renaming:

```text
malicious.psm1 → renamed → update.psm1
Filename changes. SHA256 does NOT.
```

Use the hash to: compare copies, match known malware, verify identity, preserve evidence identifier.

---

# 9. Disk Volumes

```powershell
Get-CimInstance -ClassName Win32_Volume |
ft -AutoSize DriveLetter, Label, FileSystem, Capacity, FreeSpace |
tee disc-volumes.txt
```

| Field         | Meaning               |
| ------------- | --------------------- |
| `DriveLetter` | Assigned drive letter |
| `Label`       | Volume label          |
| `FileSystem`  | Filesystem type       |
| `Capacity`    | Total capacity        |
| `FreeSpace`   | Available space       |

**Lab finding:** A volume with **no drive letter** — suspicious in context. A volume without a drive letter can have legitimate reasons, but unexplained storage should be documented and investigated.

---

# 10. Full Correlation Across the Room

```text
NETWORK → ssh.exe → PROCESS → aurora-agent → SERVICE
        ↓
Suspicious executable → TEMP DIRECTORY → INITIAL_LANTERN.exe + Invoke-SocksProxy.psm1
```

This is what **mind mapping findings during an investigation** looks like.

---

# Investigation Workflows

### Process Investigation

```text
Process Name → PID → Parent PID → Parent Process → User → Command Line
        ↓
Executable Path → File Hash → Network Connections → Related Services/Tasks → Conclusion
```

### Directory Investigation

```text
Directory → Files → Extensions → Executable/Script?
        ↓
Hash → Timestamps → Associated Process → Network Activity → Related Persistence
```

> Don't recursively inspect every directory without a reason. Directory investigation can become overwhelming.

---

# Quick Revision

| Question                         | Command / Field                           |
| -------------------------------- | ----------------------------------------- |
| What is running?                 | `Get-CimInstance Win32_Process`           |
| Uniquely identify process?       | `ProcessId`                               |
| What process launched it?        | `ParentProcessId`                         |
| Which account owns the process?  | `GetOwner()` method                       |
| How was the process executed?    | `CommandLine`                             |
| Where is the executable?         | `Path`                                    |
| SHA256 fingerprint?              | `Get-FileHash <file>`                     |
| Artefacts in Temp directories?   | `Get-ChildItem <TempPath> -Recurse -Force` |
| What storage volumes exist?      | `Get-CimInstance Win32_Volume`            |

---

# What I Learned

- Enumerate running Windows processes with ownership and parent-child relationships
- Understand **PID** and **Parent PID** and build process trees
- Identify which user owns a process
- Examine process command lines
- Locate actual executables on disk
- Investigate user Temp directories for suspicious executables and PowerShell modules
- Calculate SHA256 hashes of suspicious files
- Enumerate disk volumes, including those without drive letters

### Most important lesson

```text
USER → PROCESS → PID / PARENT PID → EXECUTABLE PATH → FILE → SHA256
        ↓
DIRECTORY → NETWORK CONNECTION → SERVICE / SCHEDULED TASK → ATTACK CHAIN
```

For this room, the key correlation:

```text
ssh.exe → Parent: aurora-agent → Suspicious service
        ↓
Suspicious executable → Temp directory → INITIAL_LANTERN.exe + Invoke-SocksProxy.psm1
```

**Process analysis isn't about memorizing process names — it's about reconstructing relationships and following artefacts until the story makes sense.**
