# Windows Incident Surface — Task 6: Startup & Registry

## Objective

Windows startup locations and Registry keys are common places for attackers to establish **persistence** and execute code automatically.

> **Don't investigate a suspicious registry value in isolation. Follow what it executes and then investigate what that executable loads.**

---

# Mental Model

```text
Startup Entries
      ↓
Registry
      ↓
Suspicious Execution
      ↓
Executable
      ↓
DLL / Helper
      ↓
Attack Chain
```

The investigation should always move **forward** from each finding to the next, building a complete picture.

---

# 1. Startup Execution

### Question

> What programs or commands execute automatically when Windows starts?

```powershell
Get-CimInstance Win32_StartupCommand |
Select-Object Name, command, Location, User |
fl |
tee autorun-cmds.txt
```

| Field      | Meaning                               |
| ---------- | ------------------------------------- |
| `Name`     | Startup entry name                    |
| `Command`  | Command/program executed              |
| `Location` | Where the startup entry is configured |
| `User`     | User associated with the entry        |

### Why Startup Entries Matter

```text
Windows starts → Startup entry executes → Program starts → Attacker maintains execution
```

Attackers can abuse startup mechanisms to launch malware, scripts, backdoors, remote-access tools, or persistence mechanisms.

---

# 2. What to Look For in Startup Entries

Don't assume every startup entry is malicious. Look for:

### Unexpected user

```text
Startup entry → Unknown/unexpected User
```

### Suspicious path

```text
C:\Users\...\AppData\Temp\       (temporary/user-writable location)
C:\Users\...\AppData\...         (unexpected location)
```

rather than an expected Windows or installed-software directory.

### Suspicious command

- `cmd.exe`, PowerShell, scripts
- Unusual arguments or unknown executables

### Unexpected software

Remote-access software may be legitimate or malicious depending on the environment. The room shows **AnyDesk** as a startup entry — context and organizational baseline matter.

---

# 3. Startup vs Logon Persistence

```text
Boot-time startup  → Runs when Windows starts
Logon-time startup → Runs when a user logs in
```

Both can be abused for persistence. The room examines both and eventually identifies a suspicious modification to the Windows **Winlogon `Userinit`** value.

---

# 4. Registry Investigation

### Why the Registry?

The Windows Registry stores a huge amount of system configuration. Attackers can modify it to:
- Establish persistence
- Change system behaviour
- Execute programs
- Load malicious components
- Modify security settings

> **Don't search the entire Registry blindly. Start with keys relevant to the behaviour you're investigating.**

---

# 5. Important Winlogon Keys

```text
HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\Userinit
HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\Shell
```

These are involved in the Windows logon process.

### Userinit

Normally launches:

```text
userinit.exe
```

which is part of the Windows user-session initialization process.

The lab found:

```text
Userinit: C:\Windows\system32\userinit.exe, cmd.exe ...
```

**Additional `cmd.exe` after the legitimate `userinit.exe`** — another command is being launched during the logon process.

> **What does this additional command execute?** — That's where correlation becomes important.

### Shell

```text
Shell: explorer.exe
```

`explorer.exe` is the expected Windows shell — not suspicious. The more interesting finding is the modified `Userinit`.

---

# 6. Follow the Trace

Don't stop at `Userinit → cmd.exe`. Follow the full chain:

```text
Userinit
   ↓
cmd.exe
   ↓
What does cmd.exe launch?
   ↓
netsh.exe
   ↓
What is associated with netsh?
   ↓
Registry / NetSh
   ↓
Suspicious DLL
```

This is the core lesson of Task 6.

---

# 7. NetShell / netsh.exe

`netsh.exe` is a legitimate Windows networking utility. This creates an important DFIR lesson:

> **A legitimate Windows executable can still be part of a malicious execution chain.**

Don't automatically conclude:

```text
netsh.exe = malicious
```

Instead ask:

```text
Why is netsh being executed?
Who is executing it?
Where is it being launched from?
What configuration does it load?
What DLLs are associated with it?
```

**MITRE ATT&CK:** T1546 — Event Triggered Execution (execution through helper DLLs)

---

# 8. NetSh Registry Command

```powershell
Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\NetSh" |
tee netsh-records.txt
```

This is **pivoting based on evidence** — the earlier investigation found `Userinit → cmd.exe → netsh.exe`, so now we investigate the configuration associated with `netsh`.

### Expected Entries

```text
ifmon.dll, rasmontr.dll, authfwcfg.dll, dhcpcmonitor.dll,
dot3cfg.dll, fwcfg.dll, hnetmon.dll, netiohlp.dll, nshhttp.dll
```

These are associated with legitimate NetShell functionality.

> **Don't flag a DLL just because it appears in a Registry key. Compare it with expected/default system behaviour.**

---

# 9. Suspicious DLL Finding

The investigation found an unusual DLL entry (`****shield`) that:
- Doesn't match the normal pattern
- Isn't part of expected default configuration
- Appears associated with a temporary location
- Can potentially be loaded through `netsh.exe`

This moves the investigation from **registry anomaly** to **potential malicious DLL execution**.

---

# 10. The Complete Attack Chain

```text
Windows Logon
      ↓
Winlogon\Userinit
      ↓
cmd.exe
      ↓
netsh.exe
      ↓
NetSh Registry Configuration
      ↓
Suspicious DLL
      ↓
Potential Code Execution
```

Much stronger than simply saying: *"I found a weird registry value."*

---

# 11. Legitimate Tool ≠ Legitimate Activity

```text
netsh.exe = legitimate executable

BUT:
Winlogon → cmd.exe → netsh.exe → suspicious DLL = malicious chain
```

Don't classify an executable based only on its filename. Investigate:

```text
Name + Path + Parent/launcher + Arguments + Registry configuration
      ↓
Loaded components + User + Timeline
```

---

# 12. Suspicious Indicators Checklist

### Startup entry suspicious when:

```text
Unexpected name? → Unexpected user? → Unexpected location? → Unexpected command?
      ↓
Runs from Temp/AppData? → Unknown executable? → Unknown DLL? → Modified Registry key?
```

One indicator may be innocent. Several correlated indicators are much more significant.

### Registry entry suspicious when:

- Unexpected executables: `cmd.exe`, `powershell.exe`, `unknown.exe` where they don't belong
- Unexpected DLL not in Windows default configuration
- Unusual path (temporary or user-writable directories)
- Abnormal value structure compared to other entries

The room uses pattern-based comparison to identify the suspicious NetSh entry.

---

# 13. Correlation Is the Main Skill

```text
Finding
  ↓
Ask "What does this execute?"
  ↓
Follow the execution
  ↓
Find next artefact
  ↓
Investigate that artefact
  ↓
Build attack chain
```

Every step gives you another piece of evidence.

---

# Investigation Flow

```text
STARTUP
   ↓
Find automatic execution
   ↓
Identify suspicious user/command/path
   ↓
Check Registry persistence (Winlogon Userinit / Shell)
   ↓
Follow executed program
   ↓
Investigate its configuration (NetSh)
   ↓
Find associated DLL
   ↓
Check path + legitimacy
   ↓
Correlate evidence
   ↓
Build attack chain
```

---

# Quick Revision

| Question                      | Command / Location                                           |
| ----------------------------- | ------------------------------------------------------------ |
| What executes automatically?  | `Get-CimInstance Win32_StartupCommand`                       |
| What executes at logon?       | `HKLM\...\Winlogon` → `Userinit` and `Shell` values         |
| NetSh DLL configuration?      | `Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\NetSh"`   |

---

# Evidence Files

| File               | Contains                                          |
| ------------------ | ------------------------------------------------- |
| `autorun-cmds.txt` | Startup entry name, command, location, user       |
| `netsh-records.txt`| NetSh Registry values, DLL entries, anomalous config |

---

# What I Learned

- Windows startup entries can provide persistence clues
- `Win32_StartupCommand` enumerates startup commands
- Winlogon `Userinit` and `Shell` are critical Registry locations during logon
- A legitimate executable can be abused as part of a malicious execution chain
- `netsh.exe` can load helper DLLs through its registry configuration
- Registry anomalies should be investigated based on **expected patterns and system baselines**
- Suspicious DLLs should be traced back to their execution mechanism
- Startup persistence and Registry evidence can be correlated to reconstruct an attack

### Most important lesson

> **Don't stop when you find the first suspicious artefact. Follow the trail.**

```text
Suspicious Startup → Registry → Executable → Configuration → DLL → Execution
```

That is the real skill Task 6 teaches: **turn individual artefacts into an attack chain.**
