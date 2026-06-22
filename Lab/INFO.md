# About Windows

This file contains useful Windows shortcuts, Run commands, system tools, and
basic troubleshooting commands.

## Run Dialog Shortcuts

Open the Run dialog with:

```text
Win + R
```

| Command | Opens / Purpose |
|---------|-----------------|
| `msconfig` | System Configuration |
| `taskmgr` | Task Manager |
| `cmd` | Command Prompt |
| `powershell` | Windows PowerShell |
| `control` | Control Panel |
| `settings:` | Windows Settings |
| `appwiz.cpl` | Programs and Features |
| `ncpa.cpl` | Network Connections |
| `firewall.cpl` | Windows Defender Firewall |
| `sysdm.cpl` | System Properties |
| `desk.cpl` | Display Settings |
| `main.cpl` | Mouse Properties |
| `mmsys.cpl` | Sound Settings |
| `timedate.cpl` | Date and Time Settings |
| `intl.cpl` | Region Settings |
| `powercfg.cpl` | Power Options |
| `devmgmt.msc` | Device Manager |
| `diskmgmt.msc` | Disk Management |
| `compmgmt.msc` | Computer Management |
| `services.msc` | Services Manager |
| `eventvwr.msc` | Event Viewer |
| `gpedit.msc` | Local Group Policy Editor |
| `lusrmgr.msc` | Local Users and Groups |
| `secpol.msc` | Local Security Policy |
| `regedit` | Registry Editor |
| `cleanmgr` | Disk Cleanup |
| `resmon` | Resource Monitor |
| `perfmon` | Performance Monitor |
| `dxdiag` | DirectX Diagnostic Tool |
| `winver` | Windows Version Information |
| `mstsc` | Remote Desktop Connection |
| `shell:startup` | Startup Folder |
| `%temp%` | Temporary Files Folder |
| `temp` | Windows Temp Folder |
| `recent` | Recent Files |
| `osk` | On-Screen Keyboard |
| `magnify` | Magnifier |
| `snippingtool` | Snipping Tool |
| `notepad` | Notepad |
| `calc` | Calculator |

## Windows `.exe` Commands

These commands can be opened from `Win + R`, Command Prompt, PowerShell, or
File Explorer address bar. Some tools may need administrator permission.

### Common Apps

| `.exe` Command | Opens / Purpose |
|----------------|-----------------|
| `explorer.exe` | File Explorer |
| `notepad.exe` | Notepad |
| `write.exe` | WordPad, if installed |
| `mspaint.exe` | Microsoft Paint |
| `calc.exe` | Calculator |
| `cmd.exe` | Command Prompt |
| `powershell.exe` | Windows PowerShell |
| `pwsh.exe` | PowerShell 7, if installed |
| `wt.exe` | Windows Terminal, if installed |
| `taskmgr.exe` | Task Manager |
| `control.exe` | Control Panel |
| `msedge.exe` | Microsoft Edge |
| `iexplore.exe` | Internet Explorer, older Windows only |
| `charmap.exe` | Character Map |
| `osk.exe` | On-Screen Keyboard |
| `magnify.exe` | Magnifier |
| `narrator.exe` | Narrator |
| `snippingtool.exe` | Snipping Tool |
| `sndvol.exe` | Volume Mixer |
| `mblctr.exe` | Windows Mobility Center |
| `wab.exe` | Windows Contacts, if available |
| `dvdplay.exe` | DVD Player, older Windows only |

### System Information And Diagnostics

| `.exe` Command | Opens / Purpose |
|----------------|-----------------|
| `msinfo32.exe` | System Information |
| `dxdiag.exe` | DirectX Diagnostic Tool |
| `winver.exe` | Windows version information |
| `perfmon.exe` | Performance Monitor |
| `resmon.exe` | Resource Monitor |
| `eventvwr.exe` | Event Viewer |
| `werfault.exe` | Windows Error Reporting |
| `mdsched.exe` | Windows Memory Diagnostic |
| `dfrgui.exe` | Defragment and Optimize Drives |
| `cleanmgr.exe` | Disk Cleanup |
| `chkdsk.exe` | Check disk from terminal |
| `sfc.exe` | System File Checker |
| `dism.exe` | Windows image servicing and repair |
| `sigverif.exe` | File Signature Verification |
| `verifier.exe` | Driver Verifier Manager |
| `msdt.exe` | Microsoft Support Diagnostic Tool |

### Settings And Control Tools

| `.exe` Command | Opens / Purpose |
|----------------|-----------------|
| `SystemSettings.exe` | Windows Settings app |
| `msconfig.exe` | System Configuration |
| `regedit.exe` | Registry Editor |
| `gpedit.msc` | Local Group Policy Editor |
| `secpol.msc` | Local Security Policy |
| `services.msc` | Services Manager |
| `devmgmt.msc` | Device Manager |
| `diskmgmt.msc` | Disk Management |
| `compmgmt.msc` | Computer Management |
| `lusrmgr.msc` | Local Users and Groups |
| `certmgr.msc` | Current user certificates |
| `certlm.msc` | Local machine certificates |
| `printmanagement.msc` | Print Management |
| `wf.msc` | Windows Defender Firewall with Advanced Security |

### Network Tools

| `.exe` Command | Use |
|----------------|-----|
| `mstsc.exe` | Remote Desktop Connection |
| `rasphone.exe` | Dial-up / VPN connection manager |
| `ncpa.cpl` | Network Connections |
| `ipconfig.exe` | Show or manage IP configuration |
| `ping.exe` | Test network connectivity |
| `tracert.exe` | Trace route to a host |
| `pathping.exe` | Advanced route and packet loss test |
| `nslookup.exe` | DNS lookup tool |
| `netstat.exe` | Show network connections |
| `arp.exe` | Show or modify ARP cache |
| `route.exe` | View or edit routing table |
| `netsh.exe` | Network shell configuration tool |
| `ftp.exe` | FTP client |
| `telnet.exe` | Telnet client, if enabled |
| `ssh.exe` | OpenSSH client, if installed/enabled |
| `scp.exe` | Secure copy client, if installed/enabled |
| `sftp.exe` | Secure FTP client, if installed/enabled |
| `curl.exe` | Transfer data from URLs |

### Process And Service Tools

| `.exe` Command | Use |
|----------------|-----|
| `tasklist.exe` | List running processes |
| `taskkill.exe` | Stop a process |
| `sc.exe` | Manage Windows services |
| `net.exe` | Manage users, shares, services, and network options |
| `net1.exe` | Alternate `net` command binary |
| `runas.exe` | Run a program as another user |
| `shutdown.exe` | Shut down, restart, or log off |
| `logoff.exe` | Log off current user |
| `timeout.exe` | Wait for a specific number of seconds |
| `where.exe` | Find executable path |
| `whoami.exe` | Show current user identity |
| `hostname.exe` | Show computer name |
| `quser.exe` | Show logged-in users |
| `query.exe` | Query sessions, users, or processes |

### File And Disk Commands

| `.exe` Command | Use |
|----------------|-----|
| `robocopy.exe` | Advanced file and folder copy |
| `xcopy.exe` | Copy files and folders |
| `copy.exe` | Copy files from Command Prompt |
| `move.exe` | Move files from Command Prompt |
| `del.exe` | Delete files from Command Prompt |
| `tree.com` | Show folder tree |
| `compact.exe` | Show or change NTFS compression |
| `cipher.exe` | Manage encryption or wipe free space |
| `fsutil.exe` | Advanced file system utility |
| `diskpart.exe` | Disk partition tool |
| `format.com` | Format a disk |
| `label.exe` | Change disk volume label |
| `mountvol.exe` | Manage volume mount points |
| `subst.exe` | Map a path to a drive letter |
| `attrib.exe` | Show or change file attributes |
| `icacls.exe` | View or edit file permissions |
| `takeown.exe` | Take ownership of files |

### Security And Account Commands

| `.exe` Command | Use |
|----------------|-----|
| `WindowsSecurityHealthService.exe` | Windows Security health service |
| `MpCmdRun.exe` | Microsoft Defender command-line tool |
| `netplwiz.exe` | User Accounts settings |
| `credwiz.exe` | Stored usernames and password backup/restore |
| `certutil.exe` | Certificate and encoding utility |
| `auditpol.exe` | Audit policy tool |
| `gpupdate.exe` | Refresh Group Policy |
| `gpresult.exe` | Show applied Group Policy |
| `secedit.exe` | Security configuration tool |
| `bcdedit.exe` | Boot configuration editor |
| `reagentc.exe` | Windows Recovery Environment configuration |

### Useful `.exe` Examples

```cmd
taskmgr.exe
msconfig.exe
devmgmt.msc
services.msc
ipconfig.exe /all
ping.exe google.com
netstat.exe -ano
tasklist.exe
taskkill.exe /PID 1234 /F
sfc.exe /scannow
dism.exe /Online /Cleanup-Image /RestoreHealth
shutdown.exe /r /t 0
```

## Keyboard Shortcuts

| Shortcut | Use |
|----------|-----|
| `Win` | Open Start menu |
| `Win + R` | Open Run dialog |
| `Win + E` | Open File Explorer |
| `Win + I` | Open Settings |
| `Win + D` | Show desktop |
| `Win + L` | Lock the computer |
| `Win + A` | Open Quick Settings / Action Center |
| `Win + S` | Open Search |
| `Win + X` | Open Power User menu |
| `Win + Tab` | Open Task View |
| `Alt + Tab` | Switch between open apps |
| `Alt + F4` | Close current app |
| `Ctrl + Shift + Esc` | Open Task Manager directly |
| `Ctrl + Alt + Delete` | Security options screen |
| `Ctrl + C` | Copy |
| `Ctrl + X` | Cut |
| `Ctrl + V` | Paste |
| `Ctrl + Z` | Undo |
| `Ctrl + Y` | Redo |
| `Ctrl + A` | Select all |
| `Ctrl + F` | Find |
| `F2` | Rename selected file |
| `F5` | Refresh |
| `PrtSc` | Capture screenshot |
| `Win + PrtSc` | Save screenshot automatically |
| `Win + Shift + S` | Screenshot selection tool |
| `Win + V` | Clipboard history |
| `Win + .` | Emoji and symbols panel |
| `Win + P` | Project display options |
| `Win + K` | Connect to wireless display/audio |
| `Win + H` | Voice typing |
| `Win + Ctrl + D` | Create virtual desktop |
| `Win + Ctrl + Left/Right` | Switch virtual desktops |
| `Win + Ctrl + F4` | Close virtual desktop |

## File Explorer Shortcuts

| Shortcut | Use |
|----------|-----|
| `Ctrl + N` | Open new File Explorer window |
| `Ctrl + Shift + N` | Create new folder |
| `Alt + Enter` | Open file/folder properties |
| `Alt + Left` | Go back |
| `Alt + Right` | Go forward |
| `Alt + Up` | Go to parent folder |
| `Ctrl + L` | Select address bar |
| `Ctrl + Shift + E` | Show all folders in navigation pane |
| `Shift + Delete` | Permanently delete selected item |

## Useful Command Prompt Commands

| Command | Use |
|---------|-----|
| `ipconfig` | Show IP configuration |
| `ipconfig /all` | Show full network details |
| `ipconfig /release` | Release current IP address |
| `ipconfig /renew` | Request a new IP address |
| `ipconfig /flushdns` | Clear DNS cache |
| `ping <host>` | Test network connectivity |
| `tracert <host>` | Trace route to a host |
| `nslookup <domain>` | Query DNS records |
| `netstat -ano` | Show network connections with process IDs |
| `systeminfo` | Show system details |
| `hostname` | Show computer name |
| `whoami` | Show current user |
| `dir` | List files and folders |
| `cd <folder>` | Change directory |
| `cls` | Clear terminal screen |
| `tree` | Show folder tree |
| `copy` | Copy files |
| `xcopy` | Copy files and folders |
| `robocopy` | Advanced file copy tool |
| `tasklist` | List running processes |
| `taskkill /PID <pid> /F` | Force kill a process |
| `sfc /scannow` | Scan and repair system files |
| `chkdsk` | Check disk for errors |
| `shutdown /s /t 0` | Shut down immediately |
| `shutdown /r /t 0` | Restart immediately |

## PowerShell Commands

| Command | Use |
|---------|-----|
| `Get-Process` | List running processes |
| `Stop-Process -Id <pid>` | Stop a process by ID |
| `Get-Service` | List services |
| `Start-Service <name>` | Start a service |
| `Stop-Service <name>` | Stop a service |
| `Get-ChildItem` | List files and folders |
| `Set-Location <path>` | Change directory |
| `Get-Content <file>` | Read file content |
| `Test-Connection <host>` | Ping a host |
| `Get-NetIPAddress` | Show IP addresses |
| `Get-NetTCPConnection` | Show TCP connections |
| `Get-ExecutionPolicy` | Show script execution policy |

## Security And Admin Tools

| Tool / Command | Use |
|----------------|-----|
| `Windows Security` | Antivirus, firewall, device security |
| `wf.msc` | Advanced Windows Firewall |
| `secpol.msc` | Local security policies |
| `gpedit.msc` | Group policy settings |
| `eventvwr.msc` | View system and security logs |
| `lusrmgr.msc` | Manage local users and groups |
| `net user` | List local users |
| `net user <name>` | Show details for a user |
| `net localgroup` | List local groups |
| `net localgroup administrators` | Show local admins |
| `whoami /priv` | Show current user privileges |
| `whoami /groups` | Show current user groups |
| `cipher /w:<drive>` | Wipe free space on a drive |

## Troubleshooting Checklist

1. Restart the application.
2. Check Task Manager for high CPU, RAM, or disk usage.
3. Check network using `ipconfig`, `ping`, and `nslookup`.
4. Check Windows Update.
5. Check Device Manager for driver issues.
6. Check Event Viewer for errors.
7. Run `sfc /scannow` if Windows files may be corrupted.
8. Restart the system if services or drivers are stuck.

## Quick Notes

- `msconfig` opens System Configuration, useful for boot settings and startup troubleshooting.
- `taskmgr` opens Task Manager.
- `Ctrl + Shift + Esc` is the fastest keyboard shortcut for Task Manager.
- Use Run commands when you want to open Windows tools quickly.
- Be careful with `regedit`, `diskmgmt.msc`, and admin commands because wrong changes can break the system.
