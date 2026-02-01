# Enumeration — Detailed Notes (Module 7) 🔍

**Definition:** Enumeration is the process where an attacker creates active connections to the system and performs directed queries to gain more information about the target. The attacker establishes an active connection with the victim and tries to discover as much attack vectors as possible.

**Environment:** Enumeration techniques are conducted in an intranet environment.

**Key Distinction:** 
- **Scanning** = Finding an attack surface
- **Enumeration** = Expanding the attack surface

**Importance:** Enumeration is the key to a successful penetration test.

---

## Key Concepts & Information Gathered

### Enumeration vs Scanning
- **Scanning:** Discovers hosts, open ports, and running services
- **Enumeration:** Extracts detailed information from discovered services—users, shares, configurations, routing tables, and service settings

### Information Enumerated by Intruders
- **Network resources:** Hosts, servers, network devices
- **Network shares:** Shared folders, printers, and resources
- **Routing tables:** Network topology and routing information
- **Audit and service settings:** Security configurations and service details
- **SNMP and DNS details:** Device information and domain records
- **Machine names:** Hostnames and computer names
- **Users and groups:** Account names, group memberships, and organizational structure
- **Applications and banners:** Running applications and service version information

### Why Enumeration Matters
Well-executed enumeration reveals accounts, services, and misconfigurations that can be used for:
- Lateral movement within the network
- Privilege escalation attacks
- Targeted exploitation
- Social engineering
- Password attacks

---

## Enumeration Techniques

### Common Enumeration Methods
1. **Extract user names using email IDs**
2. **Extract information using default passwords**
3. **Extract user names using SNMP**
4. **Brute force Active Directory**
5. **Extract user groups from Windows**
6. **Extract information using DNS Zone Transfer**

### Services and Ports to Enumerate

**DNS Services:**
- **TCP/UDP 53:** DNS Zone Transfer

**Microsoft Services:**
- **TCP/UDP 135:** Microsoft RPC Endpoint Mapper
- **UDP 137:** NetBIOS Name Service (NBNS)
- **TCP 139:** NetBIOS Session Service (SMB over NetBIOS)
- **TCP/UDP 445:** SMB over TCP (Direct Host)

**Directory Services:**
- **TCP/UDP 389:** Lightweight Directory Access Protocol (LDAP)
- **TCP/UDP 3268:** Global Catalog Service

**Network Management:**
- **UDP 161:** Simple Network Management Protocol (SNMP)
- **TCP/UDP 162:** SNMP Trap

**Mail Services:**
- **TCP 25:** Simple Mail Transfer Protocol (SMTP)

**Time Services:**
- **UDP 123:** Network Time Protocol (NTP)

---

## RPC Enumeration

### RPC Fundamentals

**Definition:** RPC (Remote Procedure Call) is a protocol that allows a program to execute code on another address space (commonly on another computer on a shared network).

**Port:** TCP/UDP 135 - Microsoft RPC Endpoint Mapper

**Purpose:** The Endpoint Mapper listens on port 135 and tells client applications which dynamically assigned port a particular RPC service is listening on.

### How RPC Works

1. **Client Request:** Client connects to port 135 asking for a specific RPC service
2. **Endpoint Mapper Response:** Returns the dynamic port where the service is running
3. **Service Connection:** Client connects to the returned port to access the service

### RPC Enumeration Techniques

**Information Gathered:**
- Available RPC services
- Dynamic port mappings
- Service UUIDs
- Registered endpoints
- Network service inventory

### RPC Enumeration Tools & Commands

```bash
# Using rpcdump (Windows)
rpcdump /p <target>

# Using rpcinfo (Linux)
rpcinfo -p <target>

# Using Impacket's rpcdump
rpcdump.py <target>

# Using nmap
nmap -sV -p 135 --script=msrpc-enum <target>

# Using rpcclient (can also enumerate via RPC)
rpcclient -U "" -N <target>
> srvinfo  # Server information
> enumdomusers  # Domain users
> querydominfo  # Domain info

# Using Metasploit
use auxiliary/scanner/dcerpc/endpoint_mapper
use auxiliary/scanner/dcerpc/management
```

**Common RPC Services:**
- **LSA (Local Security Authority):** User and group enumeration
- **SAMR (Security Account Manager Remote):** User account information
- **SRVSVC (Server Service):** Share enumeration
- **WINREG (Windows Registry):** Remote registry access

### RPC Security Risks

**Vulnerabilities:**
- Information disclosure about services
- Remote code execution vulnerabilities (historical)
- Denial of service attacks
- Relay attacks

**Attack Scenarios:**
- Enumerate users and groups via SAMR
- Discover network shares via SRVSVC
- Access remote registry via WINREG
- Map service infrastructure

---

## NetBIOS / SMB Enumeration

### NetBIOS Fundamentals

**Definition:** NetBIOS (Network Basic Input/Output System) is a program that allows applications on different computers to communicate within a local area network (LAN).

**History:** Created by IBM, adopted by Microsoft

**NetBIOS Name Structure:**
- **16 ASCII character string** used to identify network devices over TCP/IP
- **15 characters** used for the device name
- **16th character** reserved for the service or name record type

### NetBIOS Communication

**Name Resolution:**
- Software applications on NetBIOS network locate and identify each other via their NetBIOS names
- Applications on other computers access NetBIOS names over UDP (NBNS)

**Session Establishment:**
- Two applications start NetBIOS session when client sends "call" command to another client (server) over TCP port 139 (session mode)
- "Hang-up" command terminates a NetBIOS session

**Important Note:** NetBIOS name resolution is NOT supported by Microsoft for Internet Protocol Version 6 (IPv6)

### NetBIOS Enumeration Objectives

**Information Attackers Obtain:**
- List of computers that belong to a domain
- List of shares on individual hosts in the network
- Policies and passwords

**Actions Attackers Perform:**
- Read/Write to shared resources depending on share availability
- Launch DoS attacks on target
- Enumerate password policies

### NetBIOS Enumeration Tools & Commands

**Nbtstat Utility (Windows):**
Displays NetBIOS over TCP/IP (NetBT) protocol statistics, NetBIOS name tables for local and remote computers, and NetBIOS name cache.

**Key Commands:**
```bash
# Get contents of NetBIOS name cache
nbtstat.exe -c

# Get NetBIOS name table of remote computer
nbtstat.exe -a <IP address of remote machine>
```

**Additional Tools:**
- `smbclient -L //<target> -U <user>` — List SMB shares
- `enum4linux -a <target>` — Comprehensive Samba/NetBIOS enumeration
- `smbmap -H <target>` — Share permissions and access checks
- `nbtscan` — NetBIOS name scanner
- `NetBIOS Enumerator` — Windows-based enumeration tool

**What You Can Learn:**
- List of computers in domain
- Available shares and their permissions
- Policy settings
- Possible writable shares for data exfiltration or pivoting

---

## SNMP Enumeration

### SNMP Fundamentals

**Definition:** SNMP (Simple Network Management Protocol) is an application layer protocol which uses UDP protocol to maintain and manage routers, hubs, switches, and other network devices on an IP network.

**Purpose:** SNMP enumeration is used to enumerate user accounts, passwords, groups, system names, and devices on a target system.

**Architecture:** SNMP consists of a manager and an agent:
- **Agents** are embedded on every network device
- **Manager** is installed on a separate computer

### SNMP Components

**1. Managed Device:**
- A device or host (node) which has the SNMP service enabled
- Can be routers, switches, hubs, bridges, computers, etc.

**2. Agent:**
- Software that runs on a managed device
- Primary job: Convert information into SNMP-compatible format for smooth network management

**3. Network Management System (NMS):**
- Software systems used for monitoring network devices
- Centralized management station

### SNMP Community Strings

SNMP uses two passwords to access and configure SNMP agents:

**Read Community String:**
- **Default:** "public"
- **Access:** Allows viewing of device/system configuration
- **Risk:** Read-only but can expose sensitive network information

**Read/Write Community String:**
- **Default:** "private"
- **Access:** Allows remote editing of configuration
- **Risk:** Full control over device if compromised

**Attack Vector:** Attackers use these default community strings to:
- Extract information about devices
- Extract network resources (hosts, routers, devices, shares)
- Retrieve ARP tables, routing tables, traffic statistics

### Management Information Base (MIB)

**Definition:** Virtual database containing formal description of all network objects that can be managed using SNMP.

**Structure:** MIB database is hierarchical, and each managed object is addressed through Object Identifiers (OIDs).

**Types of Managed Objects:**
1. **Scalar objects:** Define a single object instance
2. **Tabular objects:** Define multiple related object instances grouped in MIB tables

### SNMP Enumeration Tools & Commands

**Basic Commands:**
```bash
# Walk the entire MIB tree
snmpwalk -c public -v2c <target> .1

# Get specific OID
snmpget -c public -v1 <target> <OID>

# Enumerate specific MIB
snmpwalk -c public -v1 <target> 1.3.6.1.4.1

# Check system information
snmpwalk -c public -v2c <target> system
```

**Items of Interest:**
- Routing tables
- ARP tables
- Interface counters
- Device configurations
- Sometimes credentials in misconfigured devices
- Network topology information
- Running processes and services

### SNMP Versions

- **SNMPv1:** Original version, no encryption
- **SNMPv2c:** Improved performance, still uses community strings
- **SNMPv3:** Adds authentication and encryption (most secure)

---

## LDAP Enumeration

### LDAP Fundamentals

**Definition:** LDAP (Lightweight Directory Access Protocol) is an Internet protocol for accessing distributed directory services over a network.

**Port:** Default port 389 (TCP)

**Purpose:** Clients construct an LDAP session by connecting to a Directory System Agent (DSA) on TCP port 389 and sending queries to the DSA.

### LDAP Architecture

**Directory System Agent (DSA):**
- The LDAP server component
- Manages directory information
- Processes client queries and updates

**Data Encoding:**
- Uses Basic Encoding Rules (BER) for transmitting information
- BER is a binary format for encoding data structures

**Directory Structure:**
- Hierarchical tree structure
- Uses Distinguished Names (DN) to identify entries
- Common components: dc (domain), ou (organizational unit), cn (common name)

### LDAP Enumeration Techniques

**Information Gathered:**
- Valid user names and addresses
- Departmental details
- Company structure
- Employee information
- Server names and IP addresses
- Email addresses
- Computer names and attributes

**Common Queries:**
```bash
# Search for all users
ldapsearch -x -h <target> -b "dc=domain,dc=com"

# Enumerate users with specific attributes
ldapsearch -x -h <target> -b "dc=domain,dc=com" "objectClass=user"

# Anonymous bind attempt
ldapsearch -x -h <target> -b "" -s base

# PowerShell Active Directory queries
Get-ADUser -Filter *
Get-ADComputer -Filter *
```

### LDAP Ports

- **Port 389:** Standard LDAP (unencrypted)
- **Port 636:** LDAPS (LDAP over SSL)
- **Port 3268:** LDAP Global Catalog
- **Port 3269:** LDAP Global Catalog over SSL

### Anonymous Access Risk

**Issue:** Many LDAP implementations allow anonymous binding by default.

**Risk:** Attackers can query the directory without authentication:
- Extract organizational structure
- Enumerate user accounts
- Gather email addresses
- Map network resources

**Attack Tools:**
- ldapsearch (Linux)
- LDP.exe (Windows)
- Softerra LDAP Browser
- JXplorer
- Impacket scripts (GetUserSPNs.py for Kerberoasting)

### Active Directory Enumeration

**What it Reveals:**
- User accounts and groups
- Computer objects
- SPNs (Service Principal Names) for Kerberoasting
- Organizational Units (OUs)
- Group Policy Objects (GPOs)

**Important Note:** Even anonymous or low-privileged binds may disclose useful attributes like email addresses and SPNs.

---

## DNS Enumeration & Zone Transfer

### DNS Zone Transfer Fundamentals

**Definition:** DNS zone transfer is the process where a DNS server passes a copy of part of its database to another DNS server.

**Purpose:** Zone transfers help maintain consistency between primary and secondary DNS servers.

**Risk:** Improperly configured DNS servers can allow unauthorized zone transfers, exposing entire network topology to attackers.

### Zone Transfer Types

**AXFR (Full Zone Transfer):**
- Transfers entire zone file
- Uses TCP connection
- Contains all DNS records for the domain
- Most comprehensive information disclosure

**IXFR (Incremental Zone Transfer):**
- Transfers only changes since last update
- Based on zone serial number
- More efficient but still reveals information

### DNS Server Architecture

**Primary DNS Server:**
- Authoritative source for zone data
- Contains the master copy of zone files
- Updates are made directly to this server

**Secondary DNS Server:**
- Gets zone data through zone transfers from primary
- Provides redundancy and load distribution
- Polls primary server to check for updates (serial number)

**Zone File Contents:**
- SOA (Start of Authority) record
- NS (Name Server) records
- A (Address) records
- MX (Mail Exchange) records
- CNAME (Canonical Name) records
- TXT records

### Information Disclosed Through Zone Transfer

**Critical Information Exposed:**
- DNS server names and locations
- Hostnames of key systems (web servers, mail servers, FTP servers)
- Machine names and their IP addresses
- User names (from email addresses)
- Internal network structure
- Subdomains and their purposes
- Service locations (databases, intranet sites)

### DNS Enumeration Commands

```bash
# Attempt full zone transfer using dig
dig axfr @ns1.example.com example.com

# Alternate zone transfer using host
host -l example.com ns1.example.com

# Find DNS servers for a domain
dig ns example.com

# Query specific DNS records
dig example.com ANY
dig example.com MX
dig example.com TXT

# Reverse DNS lookup
dig -x <IP_ADDRESS>

# Using nslookup
nslookup
> server ns1.example.com
> ls -d example.com
```

### DNS Enumeration Tools

- **dig** - Domain Information Groper
- **nslookup** - Name Server Lookup
- **host** - DNS lookup utility
- **dnsenum** - Automated DNS enumeration
- **fierce** - DNS reconnaissance
- **dnsrecon** - DNS enumeration script

---

## SMTP Enumeration

### SMTP Fundamentals

**Definition:** SMTP (Simple Mail Transfer Protocol) is used to handle sending of emails over TCP port 25.

**Purpose:** Mail servers use SMTP to send, receive, and relay outgoing mail between senders and receivers.

**Enumeration Goal:** Verify valid email addresses and user accounts on the target mail server.

### SMTP Commands for Enumeration

**VRFY (Verify):**
- **Purpose:** Validates whether a specific user exists on the system
- **Syntax:** `VRFY username`
- **Response:** Different responses for valid vs invalid users
- **Example:**
  ```
  VRFY admin
  250 admin <admin@domain.com>  (User exists)
  
  VRFY invalid
  550 User unknown  (User doesn't exist)
  ```

**EXPN (Expand):**
- **Purpose:** Reveals the actual delivery addresses of aliases and mailing lists
- **Syntax:** `EXPN mailing-list`
- **Risk:** Exposes multiple email addresses from a single query

**RCPT TO (Recipient To):**
- **Purpose:** Defines the recipients of the message
- **Syntax:** `RCPT TO:<user@domain.com>`
- **Response Difference:**
  - Valid user: `250 OK`
  - Invalid user: `550 User unknown`

### SMTP Enumeration Process

**Using Telnet:**
```bash
# Connect to SMTP server
telnet mail.target.com 25

# Server banner
220 mail.target.com ESMTP

# Identify yourself
HELO attacker.com
250 mail.target.com

# Verify users
VRFY admin
250 admin <admin@target.com>

VRFY root
250 root <root@target.com>

VRFY invaliduser
550 User unknown

# Expand mailing lists
EXPN staff
250 user1@target.com
250 user2@target.com
250 user3@target.com

# Test recipient validation
MAIL FROM:<test@attacker.com>
250 OK

RCPT TO:<admin@target.com>
250 OK  (Valid user)

RCPT TO:<fake@target.com>
550 User unknown  (Invalid user)
```

### SMTP Response Analysis

**Success Responses (2xx):**
- 250: User exists / Command successful
- 251: User not local, will forward

**Error Responses (5xx):**
- 550: User unknown / Mailbox unavailable
- 551: User not local
- 553: Mailbox name not allowed

**Attack Strategy:** Analyze response differences to identify valid accounts for targeted attacks.

### SMTP Enumeration Tools

- **Telnet** - Manual enumeration
- **smtp-user-enum** - Automated SMTP user enumeration
- **Metasploit** - smtp_enum module
- **NetScanTools** - SMTP testing utilities

---

## NTP Enumeration

### NTP Fundamentals

**Definition:** NTP (Network Time Protocol) is designed to synchronize clocks of networked computers.

**Port:** UDP 123

**Purpose:** Maintains time synchronization across network devices to ensure coordinated operations and accurate logging.

**Accuracy:**
- 10ms accuracy over the Internet
- 200 microseconds accuracy in Local Area Networks (LAN)

### NTP Architecture - Stratum Levels

**Stratum 0:**
- High-precision timekeeping devices
- Examples: Atomic clocks, GPS clocks
- Not directly connected to network

**Stratum 1:**
- Computers directly connected to Stratum 0 devices
- Primary time servers
- Highest accuracy network-accessible time source

**Stratum 2:**
- Computers that synchronize with Stratum 1 servers
- Most common corporate time servers
- Provide time to end devices

**Stratum 3:**
- Computers that synchronize with Stratum 2 servers
- Each level adds slight delay and accuracy loss

### NTP Enumeration Techniques

**Information Leaked:**
- List of connected hosts
- Client IP addresses
- System names and hostnames
- Internal IP addresses
- Organization's internal network topology
- Even IPs of hosts in the DMZ (Demilitarized Zone)

**monlist Command (Deprecated):**
- Older NTP versions (before 4.2.7) supported "monlist" command
- Returns list of last 600 hosts that connected to the NTP server
- Massive information disclosure vulnerability
- Used in amplification DDoS attacks

### NTP Enumeration Commands

```bash
# Query NTP server
ntpq -c readlist <target>

# Get peer information
ntpq -c peers <target>

# Try monlist (on vulnerable servers)
ntpdc -c monlist <target>

# Get NTP variables
ntpq -c rv <target>

# Using nmap
nmap -sU -p123 --script ntp-info <target>
nmap -sU -p123 --script ntp-monlist <target>
```

### NTP Security Risks

**Information Disclosure:**
- Network topology mapping
- Internal host discovery
- Time-based attack synchronization

**DDoS Amplification:**
- monlist responses are much larger than queries
- Spoofed requests can amplify attacks 200x
- Abused in reflection attacks

### NTP Enumeration Tools

- **ntpq** - Standard NTP query program
- **ntpdc** - NTP daemon control program
- **nmap** - Network scanner with NTP scripts
- **ntpdate** - Set date and time via NTP
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

## SMB Enumeration (Detailed)

### SMB Fundamentals

**Definition:** SMB (Server Message Block) is a network file sharing protocol that allows applications on a computer to read and write to files and to request services from server programs in a computer network.

**OSI Layer:** Application Layer (Layer 7)

**Ports:**
- **Port 139:** SMB over NetBIOS (legacy)
- **Port 445:** SMB over TCP/IP (direct hosting)

**Purpose:** Share access to files, printers, serial ports, and miscellaneous communications between nodes on a network.

### SMB Implementations

**CIFS (Common Internet File System):**
- Microsoft's implementation of SMB
- Used in Windows environments
- Supports file and printer sharing

**Samba:**
- Open-source implementation of SMB/CIFS
- Allows Linux/Unix servers to provide file and print services to Windows clients
- Cross-platform compatibility

### SMB Versions

**SMB 1.0:**
- Original version, multiple security vulnerabilities
- Should be disabled (EternalBlue exploited SMB v1)

**SMB 2.0:**
- Reduced chattiness, improved performance
- Introduced in Windows Vista/Server 2008

**SMB 3.0:**
- End-to-end encryption
- SMB Direct (RDMA)
- Introduced in Windows 8/Server 2012

### SMB Enumeration Techniques

**Information Gathered:**
- Shared resources (folders, printers)
- User accounts and groups
- Domain/workgroup information
- Operating system version
- Security policies
- Network topology

**Enumeration Methods:**
1. **Null Session Attacks** (older systems)
2. **Guest account access**
3. **Authenticated enumeration** (with credentials)
4. **SMB signing disabled** exploitation

### SMB Enumeration Tools & Commands

```bash
# Using enum4linux (comprehensive SMB enumeration)
enum4linux -a <target>

# Using smbclient
smbclient -L //<target> -N  # List shares (null session)
smbclient //<target>/share -U username  # Access specific share

# Using smbmap
smbmap -H <target>
smbmap -H <target> -u username -p password

# Using rpcclient
rpcclient -U "" -N <target>
> enumdomusers  # List users
> enumdomgroups  # List groups
> querydominfo  # Domain information

# Using nmap
nmap -p 445 --script smb-enum-shares <target>
nmap -p 445 --script smb-enum-users <target>
nmap -p 445 --script smb-os-discovery <target>

# Using Metasploit
use auxiliary/scanner/smb/smb_enumshares
use auxiliary/scanner/smb/smb_enumusers
use auxiliary/scanner/smb/smb_version

# Using crackmapexec
crackmapexec smb <target> -u '' -p ''
crackmapexec smb <target> -u username -p password --shares
```

### Null Session Attacks

**Definition:** Establishing a connection to a Windows system without authentication.

**How it Works:**
```bash
# Windows command line
net use \\<target>\IPC$ "" /user:""

# Linux
smbclient -L //<target> -N
rpcclient -U "" <target>
```

**Information from Null Sessions:**
- User account names
- Share names and permissions
- System policies
- Registry keys (on older systems)

**Mitigation:** Disable anonymous access, restrict IPC$ share access.

### SMB Security Considerations

**Risks:**
- Credential harvesting
- Lateral movement
- Data exfiltration via shares
- Ransomware propagation (WannaCry, NotPetya)

**Common Misconfigurations:**
- Default credentials
- World-readable shares
- SMB v1 enabled
- Anonymous access allowed
- Weak passwords

---

## Enumeration Countermeasures

### General Security Principles

**1. Principle of Least Privilege:**
- Grant minimum necessary permissions
- Regularly review and audit access rights
- Disable unnecessary services

**2. Network Segmentation:**
- Separate critical systems from general network
- Use VLANs and firewalls
- Implement DMZ for public-facing services

**3. Strong Authentication:**
- Enforce complex passwords
- Implement multi-factor authentication
- Use account lockout policies

**4. Monitoring and Logging:**
- Enable detailed logging for all services
- Monitor for enumeration attempts
- Implement SIEM solutions

### Service-Specific Countermeasures

#### NetBIOS & SMB Protection

**1. Disable NetBIOS over TCP/IP:**
- Turn off NetBIOS if not required
- Block ports 137, 138, 139 at firewall

**2. Configure SMB Security:**
- Disable SMB v1 protocol
- Enable SMB signing (prevents relay attacks)
- Restrict anonymous access
- Configure proper share permissions

**3. IPC$ Share Hardening:**
```
# Registry setting to restrict null sessions
HKLM\SYSTEM\CurrentControlSet\Control\LSA\RestrictAnonymous = 1 or 2
```

**4. Firewall Rules:**
- Block SMB (445) from Internet
- Restrict SMB to trusted networks only

#### SNMP Protection

**1. Remove SNMP Agent:**
- Uninstall if not needed
- Disable SNMP service

**2. Change Default Community Strings:**
- Never use "public" or "private"
- Use complex, unique strings
- Different strings for different devices

**3. Upgrade to SNMPv3:**
- Uses encryption and authentication
- Requires user credentials
- Provides message integrity

**4. Access Control:**
- Restrict SNMP access to management stations only
- Use ACLs to limit source IPs
- Configure read-only access where possible

**5. Additional Hardening:**
```bash
# Example SNMPv3 configuration
snmp-server group ADMIN v3 priv
snmp-server user admin ADMIN v3 auth sha AuthPass priv aes 128 PrivPass
snmp-server host <management-ip> version 3 priv admin
```

#### LDAP Protection

**1. Disable Anonymous Binds:**
- Require authentication for all queries
- Configure LDAP server to reject anonymous connections

**2. Use SSL/TLS (LDAPS):**
- Encrypt LDAP traffic
- Use port 636 instead of 389
- Implement certificate-based authentication

**3. Access Control Lists:**
- Limit query results based on user permissions
- Restrict attributes that can be queried
- Implement query result size limits

**4. Configure Policies:**
- Set maximum query complexity
- Limit number of results returned
- Implement rate limiting

**5. Monitor LDAP Queries:**
- Log all directory access attempts
- Alert on unusual query patterns
- Track failed authentication attempts

#### DNS Protection

**1. Disable Zone Transfers:**
```bash
# BIND configuration example
zone "example.com" {
    type master;
    file "/etc/bind/db.example.com";
    allow-transfer { <secondary-server-ip>; };  # Only allow trusted servers
};
```

**2. Split-Horizon DNS:**
- Internal DNS for internal resources
- External DNS with limited information
- Never expose internal hostnames externally

**3. Use Premium DNS Registration:**
- Protects WHOIS information
- Reduces information leakage
- Prevents social engineering

**4. DNSSEC:**
- Authenticates DNS responses
- Prevents DNS spoofing
- Ensures data integrity

**5. Hide Internal Resources:**
- Don't create public DNS records for internal servers
- Use private DNS zones
- Implement DNS filtering

#### SMTP Protection

**1. Disable VRFY and EXPN:**
```bash
# Postfix configuration
disable_vrfy_command = yes

# Sendmail configuration
O PrivacyOptions=goaway  # Disables VRFY and EXPN
```

**2. Configure Proper Responses:**
- Return same response for valid and invalid users
- "User unknown" should be generic

**3. Implement Rate Limiting:**
- Limit connection attempts
- Implement greylisting
- Use tarpitting for suspected enumeration

**4. Disable Open Relay:**
- Only allow authenticated sending
- Restrict relay to local domains
- Use SPF, DKIM, DMARC

**5. Use TLS/SSL:**
- Encrypt SMTP connections
- Use STARTTLS
- Enforce encryption for sensitive domains

#### NTP Protection

**1. Configure Access Control:**
```bash
# ntp.conf restrictions
restrict default kod nomodify notrap nopeer noquery
restrict -6 default kod nomodify notrap nopeer noquery
restrict 127.0.0.1
restrict -6 ::1
```

**2. Disable monlist:**
- Ensure NTP version 4.2.7 or later
- Command removed by default in newer versions

**3. Use Authentication:**
```bash
# NTP authentication
keys /etc/ntp/keys
trustedkey 1
requestkey 1
controlkey 1
```

**4. Firewall Rules:**
- Restrict NTP access to trusted sources
- Block NTP from Internet if only internal sync needed
- Rate limit NTP queries

**5. Monitor NTP Servers:**
- Log query attempts
- Alert on excessive queries
- Track unusual synchronization patterns

### Additional Best Practices

**1. Regular Security Audits:**
- Perform internal enumeration tests
- Validate countermeasures effectiveness
- Review and update configurations

**2. Patch Management:**
- Keep all systems updated
- Apply security patches promptly
- Test patches in lab before production

**3. Intrusion Detection:**
- Deploy IDS/IPS systems
- Configure alerts for enumeration patterns
- Correlate events across systems

**4. Security Training:**
- Educate administrators on enumeration risks
- Train users on social engineering
- Regular security awareness programs

**5. Incident Response:**
- Maintain incident response plan
- Define procedures for detected enumeration
- Practice response scenarios regularly

---

## Windows Native Enumeration Tools

### Built-in Windows Commands

Windows provides several native command-line tools for enumeration that don't require additional software:

#### Network Information Commands

```cmd
# Display NetBIOS over TCP/IP statistics
nbtstat -a <IP_address>    # Remote machine name table
nbtstat -c                  # Contents of NetBIOS name cache
nbtstat -n                  # Local NetBIOS names
nbtstat -r                  # Names resolved by broadcast and WINS
nbtstat -s                  # NetBIOS sessions table

# Display network connections and listening ports
netstat -an                 # All connections and ports
netstat -r                  # Routing table
netstat -e                  # Ethernet statistics
```

#### User and Group Enumeration

```cmd
# Local system enumeration
net user                    # List all users on local system
net user <username>         # Detailed info about specific user
net localgroup              # List all local groups
net localgroup <groupname>  # List members of specific group

# Domain enumeration (requires domain context)
net user /domain            # List all domain users
net group /domain           # List all domain groups
net group "Domain Admins" /domain  # List domain admins
net accounts /domain        # Password and lockout policy
```

#### Share Enumeration

```cmd
# Local shares
net share                   # Display shared resources

# Remote shares
net view \\<target>         # List shares on remote computer
net view /domain            # List computers in domain
net view /domain:<domain>   # List computers in specific domain
```

#### Session Information

```cmd
net session                 # Display active sessions on server
net use                     # Display active connections
net use \\<target>\IPC$ "" /user:""  # Establish null session
```

#### System Information

```cmd
systeminfo                  # Comprehensive system information
systeminfo /s <target>      # Remote system information
whoami                      # Current user context
whoami /all                 # Detailed user privileges and groups
set                         # Display environment variables
```

### PowerShell Enumeration Cmdlets

```powershell
# Active Directory Module
Get-ADUser -Filter *
Get-ADGroup -Filter *
Get-ADComputer -Filter *
Get-ADDomain
Get-ADForest
Get-ADDomainController

# Network information
Get-NetTCPConnection
Get-NetRoute
Get-NetAdapter
Get-DnsClientCache

# Local system
Get-LocalUser
Get-LocalGroup
Get-LocalGroupMember -Group "Administrators"
Get-SmbShare
Get-SmbConnection

# Remote enumeration
Get-WmiObject -Class Win32_ComputerSystem -ComputerName <target>
Get-WmiObject -Class Win32_OperatingSystem -ComputerName <target>
Get-WmiObject -Class Win32_Process -ComputerName <target>
```

### Windows Management Instrumentation (WMI)

```cmd
# System information
wmic computersystem list brief
wmic os list brief
wmic process list brief
wmic service list brief
wmic share list brief

# User information
wmic useraccount list brief
wmic group list brief
wmic netlogin list brief

# Remote queries
wmic /node:<target> computersystem list brief
wmic /node:<target> useraccount list brief
```

### Windows Registry Enumeration

```cmd
# Query registry keys
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion
reg query "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters"

# Remote registry query
reg query \\<target>\HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion
```

### Third-Party Windows Tools

**Sysinternals Suite:**
- **PsExec:** Execute processes remotely
- **PsList:** List processes on local or remote systems
- **PsLoggedOn:** Show locally and remotely logged on users
- **PsGetSid:** Display SID of users or groups
- **AccessChk:** Check access permissions

**Other Tools:**
- **BloodHound:** Active Directory relationship mapper
- **PowerView:** PowerShell AD enumeration
- **SharpView:** C# implementation of PowerView
- **ADExplorer:** Active Directory explorer GUI

---

## Enumeration Summary & Best Practices

### Key Takeaways

**1. Enumeration is Critical:**
- Bridges the gap between scanning and exploitation
- Provides actionable intelligence for attacks
- Reveals misconfigurations and weak spots

**2. Multiple Vectors Exist:**
- Each protocol/service has unique enumeration methods
- Comprehensive enumeration requires testing all services
- Information from multiple sources can be correlated

**3. Defense Requires Layers:**
- No single countermeasure protects against all enumeration
- Must secure each service individually
- Regular auditing and monitoring essential

### Enumeration Methodology

**Step 1: Identify Services**
- Port scanning to discover open services
- Banner grabbing for version information
- Service fingerprinting

**Step 2: Targeted Enumeration**
- Use appropriate tools for each service
- Start with anonymous/unauthenticated access
- Escalate to authenticated enumeration if credentials available

**Step 3: Information Correlation**
- Combine data from multiple sources
- Build comprehensive network map
- Identify high-value targets

**Step 4: Documentation**
- Record all findings systematically
- Note misconfigurations and vulnerabilities
- Prepare for exploitation phase

### Red Team Perspective

**Enumeration Goals:**
- User account discovery
- Network topology mapping
- Service identification and versioning
- Misconfiguration detection
- Credential harvesting opportunities
- Lateral movement paths

**Stealth Considerations:**
- Excessive enumeration creates logs
- Rate limiting and timing important
- Use encrypted channels when possible
- Blend with normal network traffic

### Blue Team Perspective

**Detection Strategies:**
- Monitor for enumeration patterns
- Track failed authentication attempts
- Alert on unusual LDAP/SNMP queries
- Log DNS zone transfer attempts
- Detect null session establishment

**Hardening Priorities:**
1. Disable unnecessary services
2. Enforce strong authentication
3. Restrict anonymous access
4. Implement network segmentation
5. Keep systems patched and updated
6. Deploy IDS/IPS solutions
7. Regular security audits

### Compliance and Legal Considerations

**Important Reminders:**
- Enumeration must be authorized
- Document scope and permissions
- Respect privacy and data protection laws
- Report findings responsibly
- Follow ethical hacking principles

**Authorization Types:**
- Written permission from asset owner
- Documented scope of work
- Clear rules of engagement
- Incident response contacts
- Legal protection agreements

### Next Steps After Enumeration

**Vulnerability Assessment:**
- Match enumerated services to known vulnerabilities
- Check version numbers against CVE databases
- Identify missing patches

**Exploitation Planning:**
- Prioritize high-value targets
- Select appropriate exploits
- Plan attack paths and pivoting
- Prepare tools and payloads

**Reporting:**
- Document all enumerated information
- Highlight critical findings
- Provide remediation recommendations
- Risk assessment and prioritization

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