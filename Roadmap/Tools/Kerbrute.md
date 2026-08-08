# 🔑 Kerbrute: Complete Mastery Checklist

> **What is Kerbrute?** Kerbrute is a Go-based tool for performing Kerberos-based username enumeration and password spraying against Active Directory. It sends pre-authentication requests directly to the Key Distribution Center (KDC) and interprets the error codes to determine whether usernames are valid — without triggering standard account lockout policies.
>
> **Why does it exist?** Before you have any credentials in an AD engagement, you need a valid username list. Kerbrute exploits the fact that the Kerberos KDC returns different error codes for "valid username, wrong password" (`KRB5KDC_ERR_PREAUTH_FAILED`) vs "username does not exist" (`KRB5KDC_ERR_C_PRINCIPAL_UNKNOWN`) — making it possible to enumerate valid accounts silently.
>
> **When to use it:** At the very start of an AD internal engagement when you have network access to the domain controller but no credentials yet. For username enumeration from OSINT-gathered name lists. For password spraying with a single password across all valid accounts (avoids lockout by staying under the threshold). For AS-REP Roasting target discovery.
>
> **When to avoid it:** When you already have valid credentials (use NetExec, BloodHound, or Impacket instead). When the DC is on a separate network segment not reachable on port 88. When the engagement requires extreme stealth (Kerberos pre-auth failures are logged in Event ID 4768).
>
> **What mastering Kerbrute unlocks:** The ability to start every AD engagement from zero. Username enumeration without LDAP access. Safe password spraying below lockout thresholds. AS-REP Roasting target discovery. OSCP/CRTP/PNPT certification readiness for AD initial access.
>
> **Roadmap Phase:** Phase 2–3 (Scanning & Enumeration, AD Initial Access)

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

| Recon & Scanning | AD Attacks | Post-Exploitation | Credential Access |
|:-----------------|:-----------|:------------------|:-----------------|
| [🗺️ Nmap](Nmap.md) | [🐍 Impacket](Impacket.md) | [🩸 BloodHound](BloodHound.md) | [🔥 Hashcat](Hashcat.md) |
| [🌾 theHarvester](theHarvester.md) | [🌐 NetExec](NetExec.md) | [🪟 WinPEAS](WinPEAS.md) | [📡 Responder](Responder.md) |
| **🔑 Kerbrute** (you are here) | [🩸 BloodHound](BloodHound.md) | [🔥 Hashcat](Hashcat.md) | [🐍 Impacket](Impacket.md) |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals & Kerberos Pre-Auth | 5 | 2–3 hours |
| 2 | Core Usage — Enumeration & Spray | 6 | 4–5 hours |
| 3 | Intermediate (AS-REP, Wordlists, OPSEC) | 5 | 3–5 hours |
| 4 | Advanced (Automation, Integration) | 4 | 3–4 hours |
| 5 | Tool Integration | 4 | 2–3 hours |
| 6 | Practical Labs | 4 | 4–7 hours |
| 7 | Methodology & Detection | 3 | 2–3 hours |
| 8 | Mastery Challenges | 3 | 3–5 hours |
| | **Total** | **34** | **~23–35 hours** |

**Prerequisites:** Network access to domain controller (port 88/TCP Kerberos). A wordlist of potential usernames (OSINT-derived, common first.last format). Basic understanding of Kerberos authentication flow.

**Alternatives:** `nmap --script krb5-enum-users`, `enum4linux-ng` (LDAP-based, noisier), `rpcclient` (requires guest access), `ldapsearch` (requires LDAP access). Kerbrute is preferred because it works with only port 88 access and generates less noise than LDAP-based enumeration.

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — Kerberos Pre-Authentication Explained

- [ ] **Completed** · ⭐ Beginner · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand exactly why Kerberos error codes leak username validity, and why Kerbrute can enumerate without triggering lockout. |
| **Skills Learned** | Kerberos AS-REQ/AS-REP flow, error codes: `KDC_ERR_PREAUTH_FAILED` (valid user, wrong password) vs `KDC_ERR_C_PRINCIPAL_UNKNOWN` (user does not exist), why pre-auth failure ≠ account lockout. |
| **Practical Exercise** | Draw the Kerberos AS-REQ flow: client → KDC (AS-REQ with username) → KDC responds with error if pre-auth fails. Note: account lockout counter only increments on specific authentication events — pre-auth failures via Kerbrute do NOT increment the bad password count on most default AD configurations. |
| **Expected Output** | Written explanation of why Kerbrute can safely enumerate usernames. Understanding that KDC error code differentiation is the core technique. |
| **Common Mistakes** | Assuming Kerbrute is completely invisible (Event ID 4768 is logged for each AS-REQ — just without lockout). Thinking this is a "hack" — it exploits standard Kerberos protocol behavior. |

### Task 1.2 — Installation & Binary Check

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Install Kerbrute and verify it runs correctly. |
| **Practical Exercise** | Download from GitHub releases: `wget https://github.com/ropnop/kerbrute/releases/latest/download/kerbrute_linux_amd64 -O kerbrute` → `chmod +x kerbrute` → `./kerbrute --help`. On Kali: `sudo apt install kerbrute`. |
| **Expected Output** | Kerbrute binary runs, help shows `userenum`, `passwordspray`, `bruteuser`, `bruteforce` subcommands. |
| **Common Mistakes** | Not making the binary executable (`chmod +x`). Running the wrong architecture binary (use `_amd64` for standard 64-bit Kali). |

### Task 1.3 — Domain and DC Discovery

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Identify the domain name and Domain Controller IP before running Kerbrute. |
| **Skills Learned** | Nmap port 88/389 scanning, DNS SRV record lookup for `_kerberos._tcp`, reading domain name from LDAP null base DN query. |
| **Practical Exercise** | `nmap -p 88,389,636,3268 <subnet> --open` → identify DC IPs. `nslookup -type=SRV _kerberos._tcp.<domain>` → confirm domain name and DC. `nmcli` or `/etc/resolv.conf` to see configured DNS (may point to DC already). |
| **Expected Output** | DC IP address and domain name (`CORP.LOCAL` or `corp.local`). Confirmed port 88 open on DC. |
| **Common Mistakes** | Using incorrect domain name (case matters — use FQDN as advertised by DNS). Targeting a machine that is not the DC (port 88 must be on the actual KDC). |

### Task 1.4 — Building a Username Wordlist

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Create a realistic username wordlist for enumeration using common AD naming conventions. |
| **Skills Learned** | AD naming formats (`first.last`, `f.last`, `firstl`, `flast`, `first_last`), generating permutations from OSINT names, using `username-anarchy` tool. |
| **Practical Exercise** | Gather names from LinkedIn, company website, email headers. Use `username-anarchy -i names.txt > usernames.txt` to generate all format permutations. Review the SecLists `/Discovery/OSINT/` username lists as a baseline. |
| **Expected Output** | Username wordlist with 50–500 entries covering multiple naming format variations for each gathered name. |
| **Common Mistakes** | Using a generic username wordlist (rockyou, etc.) — AD usernames follow corporate naming formats, not generic passwords. Not including service accounts and machine accounts (they follow different patterns). |

### Task 1.5 — Understanding Account Lockout Policy

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand the target domain's lockout policy before any spraying activity to avoid locking accounts. |
| **Skills Learned** | Lockout threshold (bad password attempts before lockout), lockout duration, lockout observation window, how to read policy with `net accounts /domain`, `crackmapexec`/`nxc --pass-pol`. |
| **Practical Exercise** | `nxc smb <DC_IP> -u '' -p '' --pass-pol` (null session) OR `nxc smb <DC_IP> -u guest -p '' --pass-pol` → read: lockout threshold, lockout duration. If threshold is 5, spray maximum 3 attempts per account per window period. |
| **Expected Output** | Documented lockout policy. Safe spray limit calculated (threshold - 2 for safety margin). |
| **Common Mistakes** | Spraying without checking lockout policy (can lock out the entire domain — this is a career-ending mistake on real engagements). Assuming default policy is always in place (many orgs have custom policies). |

---

# PHASE 2: CORE USAGE

---

### Task 2.1 — Username Enumeration (userenum)

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Enumerate valid domain usernames from a wordlist using Kerberos pre-authentication error codes. |
| **Skills Learned** | `userenum` subcommand, `-d` domain flag, `--dc` flag, `-o` output flag, reading results (valid users highlighted in green). |
| **Practical Exercise** | `./kerbrute userenum -d corp.local --dc 192.168.1.10 -o valid_users.txt usernames.txt`. Watch output — valid users show `VALID USERNAME`. Invalid users show nothing (or `INVALID`). |
| **Expected Output** | `valid_users.txt` containing confirmed AD usernames. Rate: Kerbrute processes thousands of names per second. |
| **Common Mistakes** | Wrong domain name (use the NetBIOS domain or FQDN as Kerbrute expects). Not saving output with `-o` (results lost if terminal closes). Not threading appropriately (default threads may be slow for large lists — use `-t 20`). |

### Task 2.2 — Password Spraying (passwordspray)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Spray a single password across all valid usernames — staying under lockout threshold. |
| **Skills Learned** | `passwordspray` subcommand, choosing safe spray passwords (Season+Year, Company+Year, Welcome1), timing sprays to stay under lockout observation window. |
| **Practical Exercise** | `./kerbrute passwordspray -d corp.local --dc 192.168.1.10 valid_users.txt 'Password2024'`. If lockout threshold is 5, do only ONE spray, wait the full observation window, then optionally spray again with a different password. |
| **Expected Output** | Valid credential pairs printed in green: `VALID LOGIN: user@corp.local:Password2024`. |
| **Common Mistakes** | Spraying more times than (threshold - 2) within the observation window. Not waiting between spray rounds. Using complex passwords for spraying (users pick predictable patterns — Season+Year is the most common weak pattern). |

### Task 2.3 — Brute Force Single Account (bruteuser)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Brute-force a single specific account with a password wordlist — only use when you know the account has no lockout (service accounts, local accounts). |
| **Skills Learned** | `bruteuser` subcommand, risk assessment before use, choosing appropriate wordlists (targeted company password lists). |
| **Practical Exercise** | `./kerbrute bruteuser -d corp.local --dc 192.168.1.10 passwords.txt svc_backup` (target: known service account with assumed no lockout). Check lockout policy first — never bruteuser on regular accounts. |
| **Expected Output** | Password found or wordlist exhausted. |
| **Common Mistakes** | Using `bruteuser` on regular domain accounts (will lock them out). Not verifying the account has a lockout exemption before brute-forcing. |

### Task 2.4 — AS-REP Roasting Target Discovery

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Find accounts with Kerberos pre-authentication disabled (AS-REP Roastable) — without needing any credentials. |
| **Skills Learned** | AS-REP Roasting concept (accounts with `DONT_REQUIRE_PREAUTH` flag), using `userenum` output + Impacket GetNPUsers, Kerbrute's `--downgrade` flag for AS-REP harvesting. |
| **Practical Exercise** | After enumerating valid users: `impacket-GetNPUsers corp.local/ -usersfile valid_users.txt -no-pass -outputfile asrep_hashes.txt`. OR use Kerbrute with `userenum` and look for lines that return an AS-REP hash directly (accounts with pre-auth disabled respond with a crackable hash). |
| **Expected Output** | AS-REP hashes for accounts with pre-auth disabled. Feed to Hashcat: `-m 18200 asrep_hashes.txt wordlist.txt`. |
| **Common Mistakes** | Expecting Kerbrute alone to return AS-REP hashes (pair it with Impacket GetNPUsers for reliable extraction). Forgetting to crack the hashes (the hash itself is useless without a cracked password). |

### Task 2.5 — Threading and Speed Tuning

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Tune Kerbrute's thread count and timing for your network conditions. |
| **Practical Exercise** | Default is 10 threads. For a local lab: `-t 50`. For a slow/noisy WAN: `-t 5`. Monitor for dropped requests or timeouts — reduce threads if you see missed responses. Use `--timeout` to adjust per-request timeout. |
| **Expected Output** | Optimized thread count for your lab environment without false negatives. |
| **Common Mistakes** | Using too many threads on a slow network (missed responses look like invalid usernames — false negatives). Not testing thread count on a known-valid account first. |

### Task 2.6 — Output and Reporting

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Save and process Kerbrute output for use in downstream tools. |
| **Practical Exercise** | `-o valid_users.txt` → output contains one valid username per line. `--safe` flag → stop spraying if any lockout is detected. Parse valid_users.txt: `cat valid_users.txt \| awk '{print $NF}' \| cut -d@ -f1 > clean_users.txt` for a clean single-column list. |
| **Expected Output** | Clean username list for use with Impacket, NetExec, Hashcat, BloodHound.py. |

---

# PHASE 3: INTERMEDIATE — OPSEC & WORDLISTS

---

### Task 3.1 — OPSEC: What Gets Logged

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand the Windows event log footprint of Kerbrute activity. |
| **Skills Learned** | Event ID 4768 (AS-REQ — Kerberos auth ticket requested), Event ID 4771 (pre-auth failed), how SOC analysts detect username enumeration from high-rate 4768 events, slow enumeration techniques. |
| **Practical Exercise** | Run Kerbrute against a test DC. Check Security event log: `Get-WinEvent -LogName Security | Where-Object {$_.Id -eq 4771} | Select -First 20`. Note the source IP, username, and frequency. |
| **Expected Output** | Understanding that Kerbrute generates Event 4768/4771 entries. High-rate enumeration is detectable by any competent SOC. Low-and-slow (5–10 usernames/minute) is much harder to detect. |
| **Common Mistakes** | Thinking Kerbrute is invisible. Running full wordlists at default speed against a monitored production DC. |

### Task 3.2 — Custom Wordlists from OSINT

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Build a targeted username wordlist from real OSINT data rather than generic lists. |
| **Skills Learned** | LinkedIn scraping with theHarvester, generating name permutations with `username-anarchy`, combining multiple OSINT sources, deduplication. |
| **Practical Exercise** | `theHarvester -d corp.com -b linkedin` → extract names → `echo "John Smith" >> names.txt` for each result → `username-anarchy -i names.txt -f first.last,f.last,firstl,first > usernames.txt` → `sort -u usernames.txt > deduped.txt`. |
| **Expected Output** | Targeted wordlist of 200–2000 entries based on actual employee names. Much higher hit rate than generic wordlists. |

### Task 3.3 — Password Policy Research for Smart Spraying

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Choose spray passwords intelligently based on the target's likely password policy. |
| **Skills Learned** | Common weak passwords meeting complexity requirements, seasonal patterns, company-name passwords, default passwords for new accounts. |
| **Practical Exercise** | Research the company's public password policy (sometimes on their careers page or IT docs). Build a spray list of 3–5 candidates: `Company2024!`, `Winter2024!`, `Welcome1`, `Password1`, `<Company>1234`. Never use all at once — spray one per lockout window. |
| **Expected Output** | Prioritized spray password list ranked by probability. |

### Task 3.4 — Using SecLists Username Wordlists

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Leverage SecLists pre-built username lists when OSINT is limited. |
| **Practical Exercise** | `ls /usr/share/seclists/Usernames/` → explore `Names/names.txt`, `xato-net-10-million-usernames-dup.txt`. For AD: combine with name-format permutations. `kerbrute userenum -d corp.local --dc <DC> /usr/share/seclists/Usernames/Names/names.txt`. |
| **Expected Output** | Baseline valid username list from generic wordlist. OSINT-derived lists still preferred — this is a fallback. |

### Task 3.5 — Fine-Grained Password Policy Awareness

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand that AD supports per-user and per-group Password Settings Objects (PSO/Fine-Grained Password Policy) — some accounts have different lockout thresholds. |
| **Skills Learned** | PSO concept, how to identify PSO-protected accounts (requires LDAP read access), safe assumption when you cannot read PSOs. |
| **Practical Exercise** | If you have credentials: `Get-ADFineGrainedPasswordPolicy -Filter *` (PowerShell) or `ldapsearch -x -b "CN=Password Settings Container,CN=System,DC=corp,DC=local"`. Without creds: assume the most restrictive policy. |
| **Expected Output** | Understanding that some accounts (especially service/admin accounts) may have stricter lockout policies than the domain default. |

---

# PHASE 4: ADVANCED INTEGRATION

---

### Task 4.1 — Kerbrute + Impacket AS-REP Roasting Chain

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Kerbrute-enumerated users as input to Impacket's GetNPUsers for AS-REP Roasting. |
| **Practical Exercise** | `./kerbrute userenum -d corp.local --dc <DC> -o users.txt wordlist.txt` → `impacket-GetNPUsers corp.local/ -usersfile users.txt -no-pass -outputfile hashes.txt` → `hashcat -m 18200 hashes.txt /usr/share/wordlists/rockyou.txt` → use cracked creds with Evil-WinRM or NetExec. |
| **Expected Output** | Cracked plaintext credentials from AS-REP hash. Shell access with no prior credentials. |

### Task 4.2 — Kerbrute + NetExec Validation Chain

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Validate Kerbrute spray results with NetExec for SMB/WinRM access confirmation. |
| **Practical Exercise** | Kerbrute finds `jsmith:Password2024` → `nxc smb <subnet> -u jsmith -p 'Password2024'` → `nxc winrm <subnet> -u jsmith -p 'Password2024'` → `(Pwn3d!)` hosts → `evil-winrm -i <host> -u jsmith -p 'Password2024'`. |
| **Expected Output** | Valid credentials confirmed on multiple protocols. Shell access achieved. |

### Task 4.3 — Kerbrute + BloodHound.py Chain

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Use spray-found credentials to run BloodHound.py and map the AD environment. |
| **Practical Exercise** | After finding valid creds with Kerbrute spray: `bloodhound-python -d corp.local -u jsmith -p 'Password2024' -dc dc01.corp.local -c All` → import ZIP to BloodHound CE → identify attack paths. |
| **Expected Output** | BloodHound data collected with low-priv credentials. Attack paths to Domain Admin visible. |

### Task 4.4 — Automation: Loop Spray with Lockout Safety

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Write a simple bash script that sprays one password, waits the full lockout observation window, then sprays the next — safely automating multi-round spraying. |
| **Practical Exercise** | `for pass in 'Winter2024!' 'Spring2024!' 'Password1'; do ./kerbrute passwordspray -d corp.local --dc <DC> users.txt "$pass" -o spray_$(date +%s).txt; echo "Waiting 31 minutes..."; sleep 1860; done`. Adjust sleep to lockout observation window + 1 minute. |
| **Expected Output** | Automated safe spray that respects lockout windows. Results saved per-round with timestamps. |

---

# PHASE 5: TOOL INTEGRATION

---

### Task 5.1 — theHarvester → Kerbrute Pipeline

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min
| Field | Detail |
|:---|:---|
| **Objective** | Build a full OSINT → enumeration pipeline: email harvest → username generation → Kerberos validation. |
| **Practical Exercise** | `theHarvester -d corp.com -b all -f harvest.xml` → extract names/emails → `username-anarchy` → `kerbrute userenum`. |

### Task 5.2 — Kerbrute → Impacket Full Chain

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 35 min
| Field | Detail |
|:---|:---|
| **Objective** | Enum → spray → AS-REP roast → Kerberoast → DCSync using Kerbrute as the first step. |
| **Practical Exercise** | Full chain: `kerbrute userenum` → `kerbrute passwordspray` → `impacket-GetNPUsers` → `impacket-GetUserSPNs` → Hashcat → `impacket-secretsdump`. |

### Task 5.3 — Kerbrute → NetExec → Evil-WinRM

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min
| Field | Detail |
|:---|:---|
| **Objective** | Full no-prior-creds AD initial access chain using Kerbrute as the starting point. |
| **Practical Exercise** | `kerbrute passwordspray` → found creds → `nxc winrm` to find WinRM access → `evil-winrm` interactive shell. |

### Task 5.4 — Kerbrute in a Red Team Report

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 25 min
| Field | Detail |
|:---|:---|
| **Objective** | Document Kerbrute findings professionally for a penetration test report. |
| **Practical Exercise** | Write a finding: "Domain username enumeration via Kerberos pre-authentication error codes. X valid accounts identified. Password spray resulted in Y valid credential pairs." Include risk rating, evidence screenshot, and remediation (Fine-Grained Password Policy, monitoring Event ID 4768 rate anomalies). |

---

# PHASE 6: PRACTICAL LABS

---

### Lab 6.1 — TryHackMe: Attacktive Directory

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 2 hours
| Field | Detail |
|:---|:---|
| **Scenario** | THM guided AD room. Kerbrute is explicitly used for username enumeration and AS-REP Roasting discovery. |
| **Success Criteria** | Valid users enumerated with Kerbrute. AS-REP hash obtained and cracked. Domain compromised. |

### Lab 6.2 — HTB Machine: Forest

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 2–3 hours
| Field | Detail |
|:---|:---|
| **Scenario** | HTB Forest — AD domain with AS-REP Roastable account. Kerbrute used to enumerate svc-alfresco before AS-REP Roasting. |
| **Success Criteria** | Username found via Kerbrute → hash cracked → Evil-WinRM shell → Domain Admin via BloodHound. |

### Lab 6.3 — Home Lab: Zero-Credential AD Start

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 3–4 hours
| Field | Detail |
|:---|:---|
| **Scenario** | Home AD lab. Starting with only DC IP. Enumerate all users via Kerbrute, spray default password, obtain shell, document findings. |
| **Success Criteria** | Valid credentials obtained via enumeration+spray alone. Full attack chain documented. |

### Lab 6.4 — HTB Machine: Active

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 2 hours
| Field | Detail |
|:---|:---|
| **Scenario** | HTB Active — user found via SMB share GPP creds, then Kerberoasting. Use Kerbrute to verify account names before Kerberoasting. |
| **Success Criteria** | Kerbrute confirms valid accounts. Kerberoast hash cracked. Administrator shell. |

---

# PHASE 7: METHODOLOGY & DETECTION

---

### Task 7.1 — Kerbrute in the AD Engagement Methodology

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min
| Field | Detail |
|:---|:---|
| **Objective** | Position Kerbrute in the AD engagement kill chain: always first when you have DC access but no credentials. |
| **Expected Output** | Attack chain diagram: Nmap → **Kerbrute userenum** → **Kerbrute passwordspray** → Impacket/NetExec → BloodHound → Escalation. |

### Task 7.2 — Blue Team Detection

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min
| Field | Detail |
|:---|:---|
| **Objective** | Understand how defenders detect Kerberos enumeration and spraying. |
| **Skills Learned** | Event 4768 (AS-REQ rate anomaly), Event 4771 (pre-auth failure spike), network IDS rules for high-rate Kerberos to DC port 88, SIEM correlation rules. |
| **Expected Output** | Detection rule: "Alert on >100 Event 4771 from single source IP within 60 seconds." |

### Task 7.3 — Mitigation and Hardening

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min
| Field | Detail |
|:---|:---|
| **Objective** | Know how to reduce Kerbrute effectiveness from the defender side. |
| **Skills Learned** | Fine-Grained Password Policy with low lockout threshold, monitoring Event 4768/4771 rates, firewall rules restricting port 88 access to known management hosts, honey accounts (fake users that alert on any auth attempt). |
| **Expected Output** | Defensive checklist against Kerberos enumeration and spraying. |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — OSINT to Shell in Under 2 Hours

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 2 hours

Start with only a company domain name. Use LinkedIn/Google for employee names, generate usernames with username-anarchy, run Kerbrute enumeration, spray one password, obtain a shell via Evil-WinRM. Full chain in 2 hours.

### Challenge 8.2 — Zero-Credential Domain Admin

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 4 hours

Home AD lab. Starting with only DC IP and no credentials: Kerbrute enum → spray → AS-REP roast or Kerberoast → crack → BloodHound → path to DA. Document every step with timestamps and tool output.

### Challenge 8.3 — Build a Kerbrute Detection Dashboard

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 3 hours

Set up Splunk Free or ELK on a home lab. Configure Windows DC to forward security events. Run Kerbrute against the DC. Build a Splunk/Kibana dashboard that detects the enumeration in real time. Demonstrate both the attack and the detection.

---

## 🎓 Competency Matrix

| Skill | Beginner | Intermediate | Advanced |
|:------|:--------:|:------------:|:--------:|
| Explain Kerberos pre-auth error code leak | [ ] | | |
| Username enumeration with userenum | [ ] | | |
| Password spray with lockout-safe timing | | [ ] | |
| AS-REP Roasting target discovery | | [ ] | |
| OSINT-driven custom wordlist creation | | [ ] | |
| Fine-grained password policy awareness | | [ ] | |
| Full Kerbrute → Impacket → Hashcat chain | | | [ ] |
| Full zero-cred → DA chain using Kerbrute | | | [ ] |
| Blue team detection and SIEM rule writing | | | [ ] |

---

## 💬 Interview Questions

1. What Kerberos error codes does Kerbrute exploit to enumerate valid usernames?
2. Why does Kerbrute not trigger account lockout during username enumeration?
3. What event IDs would a defender see in Windows Security logs when Kerbrute runs?
4. What is a safe number of spray attempts per account given a lockout threshold of 5?
5. What is AS-REP Roasting and how does Kerbrute assist in finding targets?
6. How would you build a targeted username wordlist from OSINT before running Kerbrute?
7. What is Fine-Grained Password Policy and why does it matter for spraying operations?
8. How does `kerbrute passwordspray` differ from Hydra's SMB brute force?
9. What defensive controls would you recommend to prevent Kerbrute from being effective?
10. Walk through the full chain from Kerbrute username enumeration to a Domain Admin shell.
