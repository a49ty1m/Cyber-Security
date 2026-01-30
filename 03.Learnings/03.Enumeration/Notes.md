# Enumeration — Detailed Notes (Module 7) 🔍

**Overview:** Enumeration is the active phase where an attacker creates directed queries and establishes connections to extract detailed information about network resources, users, services, and configurations. It complements scanning by converting discovered surface (hosts/ports) into actionable items for exploitation.

---

## Key Concepts
- **Enumeration vs Scanning:** Scanning finds the surface (hosts, ports). Enumeration expands on that surface—e.g., listing users, shares, routing tables, and service configurations.
- **Why it matters:** Well-executed enumeration reveals accounts, services, and misconfigurations that can be used for lateral movement and privilege escalation.

---

## Common Targets & Services to Enumerate
- DNS (TCP/UDP 53) — zone transfers, hostnames
- NetBIOS / SMB (UDP 137, TCP 139/445) — machine names, shares, policies
- SNMP (UDP 161/162) — device configs, ARP/routing tables
- LDAP (TCP/UDP 389) and Global Catalog (3268) — AD objects, users, groups
- SMTP (TCP 25) — VRFY/EXPN to enumerate valid mailboxes
- NTP (UDP 123) — client lists and internal host exposure
- Other services: RDP, RPC endpoint mapper (135)

---

## NetBIOS / SMB Enumeration
- **NetBIOS:** NetBIOS names (16 bytes) are used for Windows LAN identification and can reveal hostnames and service types.
- **Tools & commands:**
  - `nbtstat -c` (local cache), `nbtstat -A <ip>` (remote name table)
  - `smbclient -L //<target> -U <user>` (list SMB shares)
  - `enum4linux -a <target>` (comprehensive Samba/NetBIOS enumeration)
  - `smbmap -H <target>` (share permissions and access checks)
- **What you can learn:** List of computers in domain, shares, policy settings, and possible writable shares for data exfiltration or pivoting.

---

## SNMP Enumeration
- **Basics:** SNMP exposes device management information via MIBs (hierarchical OIDs). Default community strings (`public`, `private`) are common and widely exploited.
- **Tools & commands:**
  - `snmpwalk -c public -v2c <target> .1` (walk the MIB tree)
  - `snmpget -c public -v1 <target> <OID>` (retrieve specific OID)
- **Items of interest:** Routing tables, ARP tables, interface counters, device configs, and sometimes credentials in misconfigured devices.
- **Mitigation:** Remove/disable SNMP if unused, change community strings, upgrade to SNMPv3 (encrypted), restrict management access to trusted hosts.

---

## LDAP / Active Directory Enumeration
- **What it reveals:** User accounts, groups, computer objects, SPNs, and organizational units that support targeted credential attacks and Kerberoasting.
- **Tools & commands:**
  - `ldapsearch -x -h <ldap-server> -b "dc=example,dc=com" '(objectClass=person)' cn` (enumerate users)
  - `Get-ADUser`, `Get-ADComputer` (PowerShell/AD module) in authenticated scenarios
  - `Impacket` scripts for AD enumeration (e.g., `GetUserSPNs.py`)
- **Important note:** Even anonymous or low-privileged binds may disclose useful attributes (email addresses, SPNs).
- **Mitigation:** Enforce least-privilege LDAP binds, limit anonymous queries, and monitor for unusual LDAP queries.

---

## DNS Enumeration & Zone Transfer (AXFR)
- **Why:** A successful zone transfer exposes hostnames, IPs, and records (MX, TXT, SRV) giving a full map of targets.
- **Commands:**
  - `dig axfr @ns1.example.com example.com` (attempt full zone transfer)
  - `host -l example.com ns1.example.com` (alternate zone transfer check)
- **Defenses:** Disable AXFR to untrusted clients, ensure private/internal records aren't publicly served, use split-horizon DNS where appropriate.

---

## SMTP Enumeration
- **Commands & flow:** Use `telnet` to connect to SMTP and issue `VRFY <user>`, `EXPN <alias>`, or `RCPT TO:<user@domain>` to validate mailboxes; differences in server responses can indicate valid recipients.
- **Mitigations:** Configure SMTP to suppress detailed responses for unknown recipients and disable `VRFY`/`EXPN` where possible.

---

## NTP Enumeration
- **What to look for:** Misconfigured NTP servers can reveal client lists or internal hostnames (via `monlist` on older NTP implementations) and be abused in amplification attacks.
- **Commands (lab):** `ntpq -p <target>` or `ntpdc -c monlist <target>` (note: modern servers mitigate monlist exposure).
- **Mitigation:** Update NTP to modern versions, restrict access, and disable legacy commands that leak client info.

---

## SMB-specific enumeration & exploitation surface
- **SMB behaviors:** SMB exposes shares, printers, and may accept anonymous logins depending on configuration.
- **Useful tools:** `smbclient`, `smbmap`, `enum4linux`, `crackmapexec` for authenticated checks and lateral movement testing.
- **Checkpoints:** Look for writable shares, legacy protocols (SMBv1), and misconfigurations that allow anonymous access.

---

## Countermeasures & Detection
- **Network controls:** Block unnecessary ports at the perimeter, segment networks, and isolate management interfaces.
- **Service hardening:** Disable unused services (SMB, SNMP, zone transfers), change defaults, and use encryption (SNMPv3, LDAP over TLS).
- **Monitoring:** Alert on unusual LDAP queries, repeated SMTP VRFY/EXPN attempts, high SNMP walk activity, and large AXFR attempts.
- **Administrative checks:** Regularly audit shares, access controls, service configurations, and apply least-privilege for service accounts.

---

## Lab-friendly commands & quick reference (Authorized use only)
- NetBIOS/SMB: `enum4linux -a <target>`, `smbclient -L //<target> -U ''`, `smbmap -H <target>`
- SNMP: `snmpwalk -c public -v2c <target> .1` (read-only community)
- LDAP: `ldapsearch -x -h <ldap> -b 'dc=example,dc=com' '(objectClass=person)' cn`
- DNS: `dig axfr @ns1.example.com example.com` (zone transfer)
- SMTP: `telnet <mailserver> 25` → `VRFY bob` / `EXPN list`
- NTP: `ntpq -p <target>`, `ntpdc -c monlist <target>` (legacy)

---

## Embedded slides & diagrams 🖼️
- **Overview / Enumeration concepts:**
  ![Module 7 - Overview](images/module7-01.png)
  *Caption: Definitions and high-level enumeration goals.*

- **Services to enumerate (slide):**
  ![Services & ports](images/module7-07.png)
  *Caption: Ports and services (DNS, SNMP, LDAP, SMB) an attacker targets.*

- **NetBIOS / SMB (slide):**
  ![NetBIOS & SMB](images/module7-10.png)
  *Caption: NetBIOS name structure and SMB core concepts.*

- **SNMP (slide):**
  ![SNMP basics](images/module7-17.png)
  *Caption: SNMP architecture, communities, and MIBs.*

- **LDAP & AD (slide):**
  ![LDAP / AD](images/module7-23.png)
  *Caption: LDAP queries reveal users, groups, and SPNs useful for Kerberoasting.*

- **DNS zone transfer (slide):**
  ![DNS zone transfer](images/module7-32.png)
  *Caption: AXFR/IXFR mechanics and why zone transfers are sensitive.*

- **SMB enumeration (slide):**
  ![SMB enumeration](images/module7-40.png)
  *Caption: SMB ports, dialects, and enumeration possibilities.*

- **Countermeasures (slide):**
  ![Enumeration countermeasures](images/module7-44.png)
  *Caption: Practical defenses for each enumeration vector.*

---

> **Note:** All commands and tools listed are for **authorized**, controlled lab environments only. Do not run offensive scans or queries against systems you do not own or have explicit permission to test.

---

*Notes expanded from Module 7 (Enumeration) on 2026-01-30.*