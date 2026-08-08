# 🎫 Rubeus: Complete Mastery Checklist

> **What is Rubeus?** Rubeus is a C# .NET tool for raw Kerberos interaction and abuses. Unlike Impacket (Python, runs from Linux) or Mimikatz (C, direct memory access), Rubeus operates entirely within the Windows Kerberos API — making it stealthier, more flexible, and directly usable from Windows sessions, Sliver C2 armory, or in-memory via Evil-WinRM's `Invoke-Binary`.
>
> **Why does it exist?** Impacket is excellent for Kerberos attacks from Linux, but once you are operating inside a Windows environment (post-exploitation), you need native Windows-side Kerberos tooling. Rubeus fills that gap — it can request, manipulate, import, and abuse Kerberos tickets entirely through standard Windows Kerberos APIs without touching LSASS.
>
> **When to use it:** During Windows post-exploitation when you need Kerberoasting, AS-REP Roasting, Pass-the-Ticket, or S4U delegation abuse from within a Windows session. When Impacket is not viable (Windows-only environment). When stealth is important — Rubeus generates standard Kerberos traffic rather than LSASS memory reads.
>
> **When to avoid it:** From a Linux attack machine (use Impacket instead). When you only need basic hash extraction (use Mimikatz). When the target has AppLocker/WDAC blocking .NET assemblies (use Impacket from Linux).
>
> **What mastering Rubeus unlocks:** Windows-native Kerberos attack execution. AS-REP Roasting and Kerberoasting without Impacket. Pass-the-Ticket, S4U2Self/S4U2Proxy delegation abuse, ticket harvesting, and constrained delegation exploitation. CRTP, CRTE, OSEP certification readiness.
>
> **Roadmap Phase:** Phase 4–5 (Post-Exploitation, Kerberos Attacks, Lateral Movement)

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

| Kerberos Attacks | AD Attacks | Credential Access | C2 |
|:----------------|:-----------|:-----------------|:---|
| [🐍 Impacket](Impacket.md) | [🩸 BloodHound](BloodHound.md) | [🐱 Mimikatz](Mimikatz.md) | [🐍 Sliver](Sliver.md) |
| **🎫 Rubeus** (you are here) | [🌐 NetExec](NetExec.md) | [🔥 Hashcat](Hashcat.md) | [🪟 Evil-WinRM](Evil-WinRM.md) |
| [🔑 Kerbrute](Kerbrute.md) | [🩸 BloodHound](BloodHound.md) | [📡 Responder](Responder.md) | [💀 Metasploit](Metasploit_Framework.md) |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals & Kerberos Protocol Deep Dive | 5 | 3–4 hours |
| 2 | Core Attacks — Roasting & Ticket Requests | 6 | 5–7 hours |
| 3 | Intermediate — Pass-the-Ticket & Harvesting | 5 | 4–6 hours |
| 4 | Advanced — Delegation Abuse & S4U | 5 | 5–8 hours |
| 5 | Tool Integration | 4 | 2–3 hours |
| 6 | Practical Labs | 4 | 5–8 hours |
| 7 | Methodology & Detection | 3 | 2–3 hours |
| 8 | Mastery Challenges | 3 | 4–6 hours |
| | **Total** | **35** | **~30–45 hours** |

**Prerequisites:** Solid understanding of Kerberos (TGT, TGS, AS-REQ, AS-REP, TGS-REQ, TGS-REP). Windows post-exploitation access (local user minimum; some modules require DA). Understanding of AD delegation types.

**Alternatives:** Impacket suite (from Linux — `GetNPUsers`, `GetUserSPNs`, `getST`), Mimikatz `kerberos::` module (overlapping Kerberos functionality), PowerSploit `Invoke-Kerberoast` (older PowerShell approach, more detected).

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — Kerberos Protocol Deep Dive

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 45 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand the full Kerberos ticket-granting process that Rubeus operates within. |
| **Skills Learned** | AS-REQ → AS-REP (TGT issuance), TGS-REQ → TGS-REP (service ticket issuance), ticket structure (PAC, encryption keys, lifetime), RC4 vs AES encryption, why RC4-encrypted service tickets are crackable (Kerberoasting). |
| **Practical Exercise** | Draw the full Kerberos flow: Client → KDC AS-REQ (with pre-auth) → KDC returns TGT → Client sends TGT to KDC TGS-REQ (for specific SPN) → KDC returns TGS encrypted with service account's hash → Client presents TGS to service. Identify exactly where Kerberoasting intercepts (the TGS is encrypted with the service hash — if RC4, it is crackable offline). |
| **Expected Output** | Full Kerberos flow diagram annotated with where each Rubeus attack intercepts the protocol. |

### Task 1.2 — Rubeus vs Impacket: When to Use Which

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Make the right tool choice for each scenario. |
| **Skills Learned** | Rubeus strengths: Windows-native, .NET, in-memory via Invoke-Binary, no Python dependency, uses standard Windows Kerberos API (stealthier). Impacket strengths: runs from Linux attacker machine, no access to target needed (some modules), broader protocol support, output format more parser-friendly. |
| **Practical Exercise** | For each scenario, decide Rubeus or Impacket: (1) Kerberoast from Kali with domain creds (Impacket). (2) Kerberoast from within a Windows Evil-WinRM session (Rubeus). (3) AS-REP Roast with no creds from Kali (Impacket GetNPUsers). (4) Pass-the-Ticket within Windows session (Rubeus). |
| **Expected Output** | Decision table: scenario → tool choice → reason. |

### Task 1.3 — Getting Rubeus on Target

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Get Rubeus running on target using multiple delivery methods. |
| **Skills Learned** | Compiled binary upload (Evil-WinRM `upload`), in-memory via `Invoke-Binary` (Evil-WinRM `-e`), Sliver armory (`armory install rubeus`), from Metasploit Meterpreter session (execute-assembly). |
| **Practical Exercise** | Method 1: `evil-winrm -i <target> -u user -p pass -e /path/to/exe/` → `Invoke-Binary Rubeus.exe klist`. Method 2: In Sliver: `armory install rubeus` → `execute-assembly Rubeus.exe klist`. |
| **Expected Output** | Rubeus executing successfully via at least two delivery methods. |
| **Common Mistakes** | Defender catching Rubeus binary on disk (use in-memory delivery). Rubeus compiled with default strings gets detected — use a custom-compiled version in real engagements. |

### Task 1.4 — Rubeus Command Structure

- [ ] **Completed** · ⭐ Beginner · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand Rubeus's action-based command structure. |
| **Practical Exercise** | `Rubeus.exe help` → list all actions. Key actions: `asreproast`, `kerberoast`, `asktgt`, `asktgs`, `ptt`, `dump`, `harvest`, `tgtdeleg`, `s4u`, `monitor`, `roast`, `describe`, `klist`. For each: one-line description of what it does. |
| **Expected Output** | Reference table of all Rubeus actions. Understanding of the `Rubeus.exe <action> [/flags]` syntax pattern. |

### Task 1.5 — Viewing and Describing Tickets (klist / describe)

- [ ] **Completed** · ⭐ Beginner · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | List and inspect Kerberos tickets currently in the Windows session. |
| **Practical Exercise** | `Rubeus.exe klist` → lists all tickets in current session. `Rubeus.exe describe /ticket:<base64_blob>` → decodes and displays ticket details (username, SPN, encryption type, expiry, flags). Compare with `klist` (built-in Windows command). |
| **Expected Output** | All current session tickets listed. Ticket details decoded and understood. |

---

# PHASE 2: CORE ATTACKS — ROASTING

---

### Task 2.1 — Kerberoasting

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | Request service tickets for accounts with SPNs and extract the RC4-encrypted ticket for offline cracking. |
| **Skills Learned** | Kerberoasting concept (any domain user can request a TGS for any SPN — the TGS is encrypted with the service account's hash), `/rc4opsec` vs default, output formats for Hashcat. |
| **Practical Exercise** | `Rubeus.exe kerberoast /outfile:kerb_hashes.txt` (roast all SPNs). Transfer to Kali → `hashcat -m 13100 kerb_hashes.txt rockyou.txt`. High-value targets: service accounts that are likely domain admins (`svc_sql`, `svc_backup`, `svc_admin`). |
| **Expected Output** | Kerberoast hashes in Hashcat-compatible format. At least one cracked service account password. |
| **Common Mistakes** | Not filtering for RC4 tickets (AES-only accounts cannot be cracked). Not targeting high-privilege SPNs (cracking `svc_print` is useless; `svc_sql` running as DA is gold). |

### Task 2.2 — AS-REP Roasting

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Request AS-REP for accounts with pre-authentication disabled and crack the returned encrypted blob. |
| **Skills Learned** | `asreproast` action, `/user` (specific user) vs scanning all accounts, output for Hashcat mode 18200, difference from Kerberoasting (no credentials needed for AS-REP Roast). |
| **Practical Exercise** | `Rubeus.exe asreproast /outfile:asrep_hashes.txt /format:hashcat`. Transfer to Kali → `hashcat -m 18200 asrep_hashes.txt rockyou.txt`. |
| **Expected Output** | AS-REP hashes for accounts with pre-auth disabled. Cracked passwords. |

### Task 2.3 — Kerberoast with /tgtdeleg (No Elevated Privileges)

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Kerberoast without elevated privileges by delegating a TGT via the Unconstrained Delegation trick. |
| **Skills Learned** | `/tgtdeleg` flag — extracts a usable TGT without requiring SYSTEM or admin via the Unconstrained Delegation `KRB_CRED` trick, useful when you only have a low-privilege domain account. |
| **Practical Exercise** | `Rubeus.exe kerberoast /tgtdeleg /outfile:hashes.txt` — runs Kerberoast using a delegated TGT instead of a direct ticket request. Compare output with standard kerberoast. |
| **Expected Output** | Kerberoast hashes obtained without elevated privileges. Understanding of when `/tgtdeleg` provides advantage. |

### Task 2.4 — Targeted Kerberoast (Single Account)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Kerberoast a specific high-value account rather than all SPNs — quieter and more targeted. |
| **Practical Exercise** | `Rubeus.exe kerberoast /user:svc_mssql /domain:corp.local /dc:dc01.corp.local /outfile:targeted.txt`. BloodHound identifies which SPN accounts are interesting → target only those. |
| **Expected Output** | Single account Kerberoast hash. Stealthier than roasting all SPNs. |

### Task 2.5 — roast: Combined Roasting

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Use the `roast` action to perform both Kerberoasting and AS-REP Roasting in a single run. |
| **Practical Exercise** | `Rubeus.exe roast /outfile:all_roast.txt /format:hashcat` → single command produces both AS-REP and TGS hashes ready for Hashcat. |
| **Expected Output** | Combined hash file with both attack types. Efficient one-step roasting operation. |

### Task 2.6 — Feeding Hashes to Hashcat

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Correctly crack Rubeus-produced hashes with Hashcat. |
| **Practical Exercise** | Kerberoast: `hashcat -m 13100 kerb_hashes.txt rockyou.txt -r best64.rule`. AS-REP: `hashcat -m 18200 asrep_hashes.txt rockyou.txt -r best64.rule`. Verify format matches — Rubeus `/format:hashcat` produces the correct `$krb5tgs$23$...` and `$krb5asrep$23$...` prefixes. |
| **Expected Output** | Cracked service account passwords. |

---

# PHASE 3: PASS-THE-TICKET & HARVESTING

---

### Task 3.1 — Ticket Harvesting (harvest)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Continuously monitor and extract new Kerberos tickets as users log in. |
| **Skills Learned** | `harvest /interval:30` — checks for new tickets every 30 seconds, exports them as base64 `.kirbi` files. Useful on shared servers (RDS, jump boxes) where multiple users authenticate. |
| **Practical Exercise** | `Rubeus.exe harvest /interval:30` → let it run while another user authenticates → note new TGT captured → use for PTT. |
| **Expected Output** | Captured TGT from another user's session. Understanding that jump boxes and shared servers are high-value harvest targets. |

### Task 3.2 — monitor: Real-Time Ticket Monitoring

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Monitor for new logon sessions and capture TGTs in real time. |
| **Practical Exercise** | `Rubeus.exe monitor /interval:5 /nowrap` — monitors every 5 seconds, exports tickets without base64 wrapping. Useful during DC compromise to capture privileged admin TGTs as they authenticate. |
| **Expected Output** | Real-time ticket capture. Admin TGT available for PTT if an admin logs in while monitor is running. |

### Task 3.3 — dump: Extract All Current Tickets

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Dump all Kerberos tickets from all current sessions on the machine (requires SYSTEM). |
| **Practical Exercise** | `Rubeus.exe dump /nowrap` → all tickets across all sessions. `Rubeus.exe dump /user:Administrator /nowrap` → Administrator's tickets only. Transfer tickets to attack machine for PTT. |
| **Expected Output** | All session tickets extracted. High-privilege tickets identified. |

### Task 3.4 — ptt: Pass-the-Ticket

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Inject a Kerberos ticket into the current session for lateral movement or privilege escalation. |
| **Skills Learned** | `ptt` action with `/ticket:<base64>` or `/ticket:<file.kirbi>`, creating new logon sessions for ticket injection (`/createnetonly:cmd.exe`), verifying injection with `klist`. |
| **Practical Exercise** | `Rubeus.exe ptt /ticket:<base64_TGT>` → `klist` (confirm ticket injected) → `dir \\dc01\C$` (verify access). For cleaner isolation: `Rubeus.exe createnetonly /program:cmd.exe` → inject ticket into new logon session. |
| **Expected Output** | Ticket injected and access confirmed to target resources. |

### Task 3.5 — asktgt: Request a TGT

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Request a TGT directly using a password, hash, or AES key — without relying on Windows cached credentials. |
| **Practical Exercise** | `Rubeus.exe asktgt /user:jsmith /password:Password1 /domain:corp.local /ptt` (with plaintext). `Rubeus.exe asktgt /user:jsmith /rc4:<ntlm_hash> /domain:corp.local /ptt` (with hash — Overpass-the-Hash). `Rubeus.exe asktgt /user:jsmith /aes256:<key> /domain:corp.local /opsec /ptt` (AES — stealthier). |
| **Expected Output** | TGT obtained and injected. Domain resources accessible as specified user. |

---

# PHASE 4: ADVANCED — DELEGATION ABUSE

---

### Task 4.1 — Unconstrained Delegation Abuse

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 50 min

| Field | Detail |
|:---|:---|
| **Objective** | Abuse Unconstrained Delegation to capture TGTs from privileged users who authenticate to a compromised server. |
| **Skills Learned** | Unconstrained Delegation concept (server caches TGTs of authenticating users in LSASS — any service they connect to gets their TGT), finding UD machines via BloodHound (`Unconstrained` node property), using Rubeus `monitor` + Printer Bug/PetitPotam to coerce DC authentication. |
| **Practical Exercise** | BloodHound → find computer with Unconstrained Delegation → compromise it → `Rubeus.exe monitor /interval:5 /nowrap` → trigger DC-to-server auth (SpoolSample/PetitPotam) → capture DC machine TGT → `Rubeus.exe ptt /ticket:<DC_TGT>` → DCSync as DC machine account. |
| **Expected Output** | DC machine account TGT captured. DCSync performed to dump all domain hashes. |
| **Common Mistakes** | Not having SYSTEM on the Unconstrained Delegation server (Rubeus monitor requires elevated privileges). Not using a coercion technique — waiting for organic traffic takes too long. |

### Task 4.2 — Constrained Delegation Abuse (S4U2Proxy)

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| Field | Detail |
|:---|:---|
| **Objective** | Abuse Constrained Delegation to access services as any user, including Domain Admin. |
| **Skills Learned** | Constrained Delegation concept (service account allowed to delegate to specific SPNs), S4U2Self (get TGS for any user to yourself), S4U2Proxy (forward that TGS to the delegated service), `s4u` action. |
| **Practical Exercise** | BloodHound → find account with Constrained Delegation (`AllowedToDelegate` edge) → `Rubeus.exe s4u /user:svc_web /rc4:<hash> /impersonateuser:Administrator /msdsspn:cifs/dc01.corp.local /ptt`. |
| **Expected Output** | TGS for CIFS/dc01 as Administrator. `dir \\dc01\C$` succeeds. |

### Task 4.3 — Resource-Based Constrained Delegation (RBCD)

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 60 min

| Field | Detail |
|:---|:---|
| **Objective** | Abuse write permissions on a computer object to configure RBCD and escalate privileges. |
| **Skills Learned** | RBCD concept (target computer trusts specified principals to delegate to it), `msDS-AllowedToActOnBehalfOfOtherIdentity` attribute, creating a machine account with PowerMad, S4U abuse chain. |
| **Practical Exercise** | BloodHound shows GenericWrite on a computer object → create new machine account (PowerMad `New-MachineAccount`) → set `msDS-AllowedToActOnBehalfOfOtherIdentity` to the new machine account → `Rubeus.exe s4u /user:NEWMACHINE$ /rc4:<hash> /impersonateuser:Administrator /msdsspn:cifs/target.corp.local /ptt`. |
| **Expected Output** | Administrator-level access to target machine via RBCD abuse. Full domain compromise if target is DC. |

### Task 4.4 — tgtdeleg: Extracting a Usable TGT Without Elevation

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Extract a TGT for the current user without requiring elevation — uses the Windows Negotiate/Kerberos delegation trick. |
| **Practical Exercise** | `Rubeus.exe tgtdeleg /target:krbtgt/CORP.LOCAL` → produces a forwardable TGT for the current user → use for Kerberoasting (`/tgtdeleg`) or PTT in another session. |
| **Expected Output** | Current user's TGT extracted without admin/SYSTEM privileges. |

### Task 4.5 — asktgs: Manual Service Ticket Requests

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Request service tickets for specific SPNs manually — useful for targeted access without running a full Kerberoast. |
| **Practical Exercise** | `Rubeus.exe asktgs /ticket:<TGT_b64> /service:cifs/fileserver.corp.local /ptt` → access `\\fileserver\share`. `Rubeus.exe asktgs /ticket:<TGT_b64> /service:http/intranet.corp.local /ptt` → access internal web service. |
| **Expected Output** | Service ticket obtained and injected. Access to specific services confirmed. |

---

# PHASE 5: TOOL INTEGRATION

---

### Task 5.1 — BloodHound → Rubeus Attack Chain

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 40 min
| Field | Detail |
|:---|:---|
| **Objective** | Use BloodHound to identify Kerberos attack vectors then execute them with Rubeus. |
| **Practical Exercise** | BloodHound: find Kerberoastable users → Rubeus `kerberoast`. BloodHound: find Unconstrained Delegation computers → Rubeus `monitor` + coerce. BloodHound: find `AllowedToDelegate` → Rubeus `s4u`. |

### Task 5.2 — Rubeus + Hashcat (Roast → Crack Pipeline)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min
| Field | Detail |
|:---|:---|
| **Objective** | Build the roast → crack → reuse pipeline. |
| **Practical Exercise** | `Rubeus.exe roast /format:hashcat /outfile:hashes.txt` → transfer → `hashcat -m 13100`/`-m 18200` → cracked creds → `evil-winrm` or `nxc` with new creds. |

### Task 5.3 — Rubeus via Sliver C2

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min
| Field | Detail |
|:---|:---|
| **Objective** | Execute Rubeus via Sliver's execute-assembly without touching disk. |
| **Practical Exercise** | In Sliver: `armory install rubeus` → `use <session>` → `execute-assembly Rubeus.exe kerberoast /outfile:hashes.txt`. Transfer output to Kali. |

### Task 5.4 — Rubeus via Evil-WinRM Invoke-Binary

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min
| Field | Detail |
|:---|:---|
| **Objective** | Run Rubeus in-memory via Evil-WinRM without writing the binary to disk. |
| **Practical Exercise** | `evil-winrm -i <target> -u user -p pass -e /path/to/exe/` → `Invoke-Binary Rubeus.exe kerberoast /format:hashcat`. |

---

# PHASE 6: PRACTICAL LABS

---

### Lab 6.1 — HTB: Sauna (AS-REP Roasting)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 2–3 hours
| Field | Detail |
|:---|:---|
| **Scenario** | HTB Sauna — web page reveals employee names → username enumeration → AS-REP Roasting with Kerbrute/Rubeus → crack hash → Evil-WinRM. |
| **Success Criteria** | AS-REP hash obtained via Rubeus `asreproast`, cracked, WinRM shell established. |

### Lab 6.2 — HTB: Spookysec (Kerberoasting)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 2 hours
| Field | Detail |
|:---|:---|
| **Scenario** | THM/HTB AD machine with Kerberoastable service accounts. Use Rubeus to extract and crack TGS hashes. |
| **Success Criteria** | Kerberoast hash cracked via Rubeus + Hashcat. Admin access achieved. |

### Lab 6.3 — Home AD Lab: Delegation Abuse Chain

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 4–5 hours
| Field | Detail |
|:---|:---|
| **Scenario** | Home AD lab. Configure Unconstrained Delegation on a server. Compromise that server → use Rubeus monitor + PetitPotam to coerce DC auth → capture DC TGT → DCSync. |
| **Success Criteria** | DC TGT captured via Rubeus. DCSync completed. All domain hashes obtained. |

### Lab 6.4 — CRTP Lab: S4U Abuse

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 3–4 hours
| Field | Detail |
|:---|:---|
| **Scenario** | Certified Red Team Professional (CRTP) lab environment. Abuse Constrained Delegation via Rubeus S4U2Proxy to move from a service account to Domain Admin. |
| **Success Criteria** | S4U chain completed. DA-level access achieved. Full attack path documented. |

---

# PHASE 7: METHODOLOGY & DETECTION

---

### Task 7.1 — Rubeus in the AD Attack Kill Chain

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min
| Field | Detail |
|:---|:---|
| **Objective** | Place Rubeus correctly in the AD attack chain alongside Kerbrute, BloodHound, Mimikatz, and Impacket. |
| **Expected Output** | Kill chain diagram: Kerbrute (enum) → Rubeus asreproast/kerberoast (no creds needed for AS-REP) → Hashcat (crack) → Rubeus asktgt/ptt (use creds) → BloodHound (map) → Rubeus delegation abuse (escalate) → Mimikatz/Impacket DCSync (domain dominance). |

### Task 7.2 — Blue Team Detection

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min
| Field | Detail |
|:---|:---|
| **Objective** | Understand how defenders detect Rubeus activity. |
| **Skills Learned** | Event 4769 (TGS request — Kerberoasting generates many in short time), Event 4768 (AS-REQ — AS-REP Roast), Kerberoasting detection: RC4 TGS requests for service accounts (most legitimate requests use AES), Unconstrained Delegation detection: Event 4624 + non-standard ticket flags, Honey SPN accounts (fake Kerberoastable accounts that alert on any TGS request). |

### Task 7.3 — Hardening Against Rubeus Attacks

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min
| Field | Detail |
|:---|:---|
| **Objective** | Know the defensive controls that reduce Rubeus attack effectiveness. |
| **Skills Learned** | Service account hardening (MSA/gMSA — auto-rotating 120-char passwords, not Kerberoastable), require AES-only for service tickets (disables RC4 cracking), remove unnecessary Unconstrained Delegation, Protected Users group (disables delegation), audit SPNs regularly. |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — No-Creds to Domain Admin via Rubeus

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 4–5 hours
Home AD lab. Starting from a domain-joined machine with a regular user account: Rubeus asreproast → crack → asktgt → BloodHound → kerberoast → crack → ptt → escalation → DA. No Mimikatz, no Impacket. Rubeus + Hashcat only.

### Challenge 8.2 — Delegation Chain to DC

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 5–6 hours
Configure and exploit a full Unconstrained Delegation chain: service account → UD computer → coerced DC auth → captured TGT → DCSync. Document every event log generated throughout. Write a detection + remediation report.

### Challenge 8.3 — Rubeus Detection Lab

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 3 hours
Run Rubeus kerberoast against a home lab DC. Simultaneously monitor Splunk with Sysmon. Build a detection rule that fires on RC4 TGS requests for service accounts. Demonstrate the rule catching the attack in real time.

---

## 🎓 Competency Matrix

| Skill | Beginner | Intermediate | Advanced |
|:------|:--------:|:------------:|:--------:|
| Kerberoasting with Rubeus | | [ ] | |
| AS-REP Roasting with Rubeus | | [ ] | |
| Ticket listing and description | [ ] | | |
| Pass-the-Ticket (ptt) | | [ ] | |
| TGT request via asktgt (hash) | | [ ] | |
| Ticket harvesting (harvest/monitor) | | [ ] | |
| Unconstrained Delegation abuse | | | [ ] |
| Constrained Delegation S4U abuse | | | [ ] |
| RBCD abuse via Rubeus | | | [ ] |
| Full no-creds → DA chain via Rubeus | | | [ ] |
| Kerberoasting detection rule | | [ ] | |

---

## 💬 Interview Questions

1. What is the difference between AS-REP Roasting and Kerberoasting?
2. Why is RC4 encryption in Kerberos tickets exploitable, and what replaced it?
3. What privileges does Rubeus require to run `dump`? Why?
4. What is the difference between `harvest` and `monitor` in Rubeus?
5. How does `tgtdeleg` allow a low-privilege user to extract a TGT?
6. Explain the S4U2Self and S4U2Proxy protocol extensions and how Rubeus abuses them.
7. What is Unconstrained Delegation and why is it dangerous?
8. How would a defender detect Kerberoasting using Windows event logs?
9. What is a Group Managed Service Account (gMSA) and why does it prevent Kerberoasting?
10. Walk through an RBCD attack chain from GenericWrite on a computer object to Domain Admin.
