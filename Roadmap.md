# Red Team Fundamentals: Master Checklist

## PART I: FUNDAMENTALS

### 1. Hardware, CPU & Pre-Boot Environment

_Mastering the machine before the Operating System initializes._

- [ ] **CPU Operations:** Master the **Fetch-Decode-Execute** cycle to understand how code actually runs at the hardware level.
    
- [ ] **Registers:** Command the "steering wheel" of the CPU: **EAX/RAX** (accumulator), **ESP/RSP** (stack pointer), and **EIP/RIP** (instruction pointer).
    
- [ ] **Architecture Types:** Distinguish between **x86** (32-bit) and **x64** (64-bit) addressing and how they handle memory instructions differently.
    
- [ ] **Instruction Sets:** Develop a working familiarity with **Assembly** language (**MOV**, **PUSH**, **POP**, **CALL**, **JMP**).
    
- [ ] **The Boot Chain:** Master the sequence from **UEFI/Secure Boot** $\rightarrow$ **Bootloader** $\rightarrow$ **Kernel Load** $\rightarrow$ **Init/Systemd**.
    
- [ ] **Secure Boot Bypass:** Understand the mechanics used to load malicious, persistent bootloaders before OS security kicks in.
    
- [ ] **Hardware I/O & DMA:** Understand how **Direct Memory Access (DMA)** allows peripherals to read/write system RAM by bypassing the CPU.
    
- [ ] **Storage Forensics:** Understand the physical data storage on **HDDs vs. SSDs** and why "deleting" is not "wiping" in a forensics context.
    



---

### 2. Operating System Internals

_Understanding the resource manager to manipulate its logic._

- [ ] **Privilege Levels:** Master the **"Ring" architecture**; specifically the separation between **Ring 0** (Kernel) and **Ring 3** (User).
    
- [ ] **System Calls:** Trace syscall execution (e.g., **NtCreateFile** or **execve**) from user-space API calls through the Interrupt to the kernel handler.
    
- [ ] **Process & Thread Mechanics:** Understand the lifecycle of processes and threads, including scheduling and context switching.
    
- [ ] **Process Environment Block (PEB):** In Windows, master the **PEB structure** to find loaded DLLs or implement anti-debugging techniques.
    
- [ ] **Authorization & Tokens:** Master Windows **SIDs**, **Access Tokens**, and **Token Impersonation**; understand Linux **Namespaces** and **Cgroups** (the basis for containers).
    
- [ ] **File Systems (Linux):** Master the root directory structure, **Inodes**, and the **"Everything is a file"** philosophy.
    
- [ ] **File Systems (Windows):** Master **NTFS permissions**, **Registry hives**, and the usage of **Alternate Data Streams (ADS)** to hide payloads.
    



---

### 3. Memory Management & Exploitation

_The primary surface for local code execution and privilege escalation._

- [ ] **Virtual Memory:** Learn how the OS maps physical RAM to virtual addresses to provide process isolation.
    
- [ ] **The Stack:** Master the **LIFO** (Last-In, First-Out) structure and the **Function Prologue/Epilogue** to understand how return addresses are stored.
    
- [ ] **The Heap:** Understand **dynamic memory allocation** and how applications request memory at runtime.
    
- [ ] **Buffer Overflows:** Master how data can overwrite adjacent memory to hijack the **EIP/Instruction Pointer**.
    
- [ ] **Exploit Mitigations:** Study **ASLR** (Address Space Layout Randomization) and **DEP/NX** (Data Execution Prevention); master **ROP** (Return Oriented Programming) to bypass them.
    



---

### 4. Data Representation & Logic

- [ ] **Number Systems:** Be able to convert between **Binary, Decimal, and Hexadecimal** mentally.
    
- [ ] **Boolean Logic:** Master **AND, OR, NOT, and XOR** (the foundation of encryption and obfuscation).
    
- [ ] **File Headers:** Identify file types (EXE, ELF, JPG) by their **"Magic Bytes"** instead of extensions.
    
- [ ] **Instruction Sets:** Basic familiarity with **Assembly** (MOV, PUSH, POP, CALL, JMP).

---

### 5. Wireless & Physical Connections

**WiFi Operations & Security:**
- [ ] **NIC Capabilities:** Ensure adapters support **monitor mode** and **packet injection**; practice with **airmon-ng/iw**.
- [ ] **WPA2/WPA3 Attacks:** Capture **4-way handshakes/PMKID**, perform **offline cracking**, and understand **SAE/dragonfly**.
- [ ] **Enterprise WiFi:** Exploit **EAP-TTLS/PEAP** misconfigurations and weak **RADIUS** setups.
- [ ] **Evil Twin/Captive Portals:** Build **rogue APs**, use **karma** attacks, and harvest credentials via portals.
- [ ] **WPS Weaknesses:** Execute **Pixie Dust** and **Reaver** style PIN attacks; detect locked-out APs.
- [ ] **Deauth/Disassoc:** Use targeted **deauthentication** for handshakes and understand **WIDS/WIPS** detection and evasion.

**RF Survey & Tooling:**
- [ ] **Antennas & Gain:** Choose antennas (omni/dir) and read **dBi**, **attenuation**, and **line-of-sight** requirements.
- [ ] **Channel Planning:** Understand **2.4/5/6 GHz** channels, **DFS** constraints, and interference sources.
- [ ] **Wardriving:** Use **Kismet**, **WiGLE**, and GPS logging to map APs and signal strength.
- [ ] **Spectrum Analysis:** Identify **jamming**, **bleed-over**, and non-802.11 interference.

**Bluetooth, BLE, and HID:**
- [ ] **BLE Primer:** Understand **advertising channels**, **pairing/bonding**, and **GATT** services.
- [ ] **Bluetooth Attacks:** Practice **Bluesnarfing, Bluebugging, Bluejacking**, and **KNOB/BLUR** style downgrades.
- [ ] **HID Impersonation:** Use devices like **Rubber Ducky/USB HID** to emulate keyboards and inject keystrokes.

**NFC/RFID/Proximity:**
- [ ] **Tag Families:** Know **Type 1-4**, **MIFARE Classic/Ultralight**; practice **cloning/replay** with **magic cards**.
- [ ] **Key Recovery:** Perform **nested/authentication attacks** on MIFARE Classic (mfoc/mfcuk) to recover keys.
- [ ] **Tooling:** Operate **Proxmark3, Flipper Zero** for read/write/sniff; understand range and legal limits.

**Infrared, IoT, and Proprietary RF:**
- [ ] **IR Replay:** Capture/replay IR signals for TVs, ACs, and legacy controls.
- [ ] **IoT Mesh:** Understand basics of **Zigbee/Z-Wave** joining, key sniffing, and common default-key issues.
- [ ] **LPWAN:** Know what **LoRa/LoRaWAN** is, join requests, and common misconfigurations.

**Physical Security Interfaces:**
- [ ] **Badge Systems:** Understand **magstripe vs. smart card vs. RFID** readers and tamper signs.
- [ ] **Tampering Detection:** Spot **taps/splitters** on cabling and evidence of hardware implants.
- [ ] **Side-Channels:** Recognize risks of **TEMPEST/emanations** and simple mitigations.

---

### 6. Application Suites & Cloud Vectors

**Office & Document Exploits:**
- [ ] **VBA & XLM 4.0 Macros:** Build payloads, sign macros, and abuse **template injection (remote DOTM)**.
- [ ] **DDE & Template Abuse:** Trigger code via **DDEAUTO**, external templates, and **Follina-style** URL template fetches.
- [ ] **OneNote/PDF/Embedded Files:** Weaponize **OneNote pages, PDF JS**, and embedded **LNK/ISO/IMG** loaders; understand **MOTW** bypasses.
- [ ] **Protected View/ATP Evasion:** Study **mark-of-the-web**, **protected view**, and common sandbox evasion tricks.

**Email Client Abuse:**
- [ ] **Outlook Rules & Forms:** Create **client-side rules** for auto-forwarding/persistence and malicious **custom forms/add-ins**.
- [ ] **MAPI/Extended MAPI:** Leverage **Redemption/Outlook interop** for covert access and exfil.

**Cloud & SaaS Persistence:**
- [ ] **OAuth Consent Phishing:** Steal **refresh tokens** via malicious app registration; understand **scopes** and consent screens.
- [ ] **Device Code & App Passwords:** Abuse **device code flow**, **legacy auth**, and **app passwords** for bypassing MFA.
- [ ] **Conditional Access Gaps:** Identify mis-scoped policies, **trusted locations**, and bypass paths.
- [ ] **Shared Mailboxes & Delegation:** Maintain access via **delegate rights** and mailbox rules.

**Data Exfiltration & Covert Channels:**
- [ ] **Cloud Storage APIs:** Use **Drive/OneDrive/Dropbox** APIs with **service accounts/tokens**; rotate tokens for persistence.
- [ ] **Covert Channels:** Exfil via **DNS-over-HTTPS**, **S3 pre-signed URLs**, **steganography in images/docs**, and throttled uploads.
- [ ] **Egress Controls:** Understand common **CASB/SWG** controls and how to mimic normal user traffic patterns.

**Logging, Forensics, and Cleanup:**
- [ ] **O365/Azure Audit:** Know where **Sign-In, Audit, Unified Audit** logs land; plan for artifacts.
- [ ] **Google Workspace Logs:** Review **Admin/Drive/Access Transparency** for trace evidence.
- [ ] **Artifact Hygiene:** Track **recent documents, registry keys, LNK files**, and clear only when within ROE.



---

## PART II: RED TEAM OPERATIONS & TRADECRAFT

_The professional skills required to execute and survive in the field._

### 7. Strategy & Core Operations

**Planning, ROE, and Safety:**
- [ ] Define **objectives, success criteria, scope, and exclusions**; align with **Rules of Engagement** and legal guardrails.
- [ ] Establish **comms plan, abort criteria, and blowout procedures**; document all operator actions for auditability.

**Infrastructure & C2:**
- [ ] Build **redirectors/frontends** (Nginx/Apache/Cloud/CDN) to shield C2 and rotate domains/certs.
- [ ] Operate multiple **C2 profiles** (HTTP(S)/DNS/SMB/MTLS) with **jitter, sleep, and OPSEC** tuning.
- [ ] Harden **VPS/cloud instances** with minimal services, **egress controls**, and per-op segregation.

**Initial Access & Payload Delivery:**
- [ ] Craft **phishing/pretexting** with **HTML smuggling, ISO/LNK/Shortcut** loaders, and **macro/OneNote** lures.
- [ ] Harden payloads with **AMSI evasion, ETW patching, obfuscation**, and staged vs. stageless choices.

**Privilege Escalation & Credential Access:**
- [ ] **Windows:** Exploit **UAC bypass, service misconfigs, token impersonation, vulnerable drivers**, and **LSASS/DPAPI/SAM** extraction.
- [ ] **Linux:** Abuse **sudo/suid/cap_setuid files, misconfigured services, kernel LPE**, and harvest **ssh keys/agent sockets**.
- [ ] Practice **pass-the-hash, pass-the-ticket, Kerberoasting/AS-REP roast**, and **vault/credential manager** theft.

**Lateral Movement & Persistence:**
- [ ] Move via **SMB/WinRM/WMI/RDP**, **SSH agent hijack**, and **PsExec/Impacket** equivalents.
- [ ] Persist with **services, scheduled tasks, WMI event consumers, startup scripts, cron/systemd timers, SSH authorized_keys**.

**Living Off the Land & Evasion:**
- [ ] Use **LOLBAS/GTFOBins** to blend in; prefer **native binaries** over custom tools.
- [ ] Evade **EDR/IDS** with **sideloading, DLL hijack, LOL drivers, memory-only beacons, timestomping, and log tampering**.
- [ ] Tune noise: minimize **parent/child process anomalies**, limit **PowerShell logs (ScriptBlock/Module)**, and watch **Sysmon** events.

**Logging, Monitoring, and Cleanup:**
- [ ] Track footprints in **Windows Event Logs, Sysmon, ETW, Prefetch, AmCache, SRUM**; on Linux in **auth.log, auditd, bash history, journalctl**.
- [ ] Plan **cleanup and restoration** per ROE; document **IOCs, timelines, and access paths** for reporting.

**Automation & Scripting Discipline:**
- [ ] Maintain fluency in **Bash, PowerShell, Python**; script **collection, parsing, and lateral movement** tasks.
- [ ] Template **checklists/playbooks** for repeatable ops; version control tooling and payloads.

---

## PART III: NETWORKING FUNDAMENTALS

### Layer 1: Physical (The Hardware Surface)

**Transmission Media & Cabling:**
- [ ] **Copper Cables:** Master **UTP, STP, and Coaxial** cables; understand **crosstalk**, **attenuation**, and **impedance**.
- [ ] **Fiber Optics:** Learn **Single-Mode (SMF)** vs. **Multi-Mode (MMF)**; understand **signal decay** and **dispersion**.
- [ ] **Wireless Transmission:** Master **RF propagation**, **antenna types**, **dBm measurements**, and **signal strength (RSSI)**.
- [ ] **Cable Standards:** Know **Cat5e, Cat6, Cat6A, Cat7** specifications and maximum distances.

**Network Topologies & Layout:**
- [ ] **Star Topology:** Central switch/hub; understand single point of failure and ease of management.
- [ ] **Ring Topology:** Sequential device connections; understand token-passing mechanisms (Token Ring).
- [ ] **Mesh Topology:** Full or partial redundancy; understand high availability and bandwidth costs.
- [ ] **Bus Topology:** Shared medium (legacy); understand collision domains and termination requirements.
- [ ] **Hybrid Topologies:** Understand modern mixed approaches combining multiple topology types.

**Wireless Standards & Frequencies:**
- [ ] **NFC (Near Field Communication):** 13.56 MHz, short range; understand **Type 1, 2, 3, 4 tags**.
- [ ] **Bluetooth:** 2.4 GHz ISM band; master **BLE (1 Mbps), Classic (3 Mbps), and Bluetooth 5.x speeds**.
- [ ] **WiFi (802.11):** Master **802.11a/b/g/n/ac/ax/be**; understand channel widths (20/40/80/160 MHz).
- [ ] **Cellular (4G/5G):** Understand **frequency bands**, **spectrum allocation**, and **base station architecture**.
- [ ] **Infrared (IR):** Understand line-of-sight requirements and usage in IoT/remote controls.

**Hardware Components & Connectors:**
- [ ] **RJ45 Connectors:** Understand **T568A/T568B wiring standards** and pin assignments.
- [ ] **Network Interface Cards (NICs):** Master **MAC addresses**, **promiscuous mode**, and **driver attacks**.
- [ ] **Repeaters & Hubs:** Understand Layer 1 devices and collision domain expansion.
- [ ] **Transceivers & Converters:** Master **SFP, QSFP, and media converters** for heterogeneous networks.

**Physical Layer Security & Attacks:**
- [ ] **Cable Interception:** Understand **fiber tapping**, **copper snooping**, and physical plant security.
- [ ] **Signal Jamming:** Learn frequency jamming techniques for wireless networks.
- [ ] **Rogue Access Points:** Understand **evil twin attacks** and hardware spoofing.
- [ ] **Physical Tampering:** Master detection of splitters, taps, and modifications.
    

---

### Layer 2: Data Link (The Local Target)

**MAC Addressing & Frame Structure:**
- [ ] **MAC Address Format:** Understand **OUI (Organizationally Unique Identifier)** and manufacturer identification.
- [ ] **Unicast vs. Multicast:** Master **FF:FF:FF:FF:FF:FF** (broadcast) and multicast MAC ranges.
- [ ] **Frame Structure:** Understand **Ethernet frames**, **VLAN tags (802.1Q)**, and **frame size (MTU)** constraints.
- [ ] **MAC Address Spoofing:** Learn tools like **macchanger** and implications for network security.

**ARP Protocol & Attacks:**
- [ ] **ARP Cache Mechanics:** Understand how **ARP tables** map IP addresses to MAC addresses.
- [ ] **ARP Spoofing:** Master **ARP Cache Poisoning** to position yourself for MITM attacks.
- [ ] **Gratuitous ARP:** Understand unsolicited ARP replies and their use in attacks.
- [ ] **ARP Scanning:** Learn to enumerate active hosts without traditional ICMP pings.
- [ ] **ARP Defense:** Understand **static ARP entries**, **ARP inspection (DAI)**, and detection mechanisms.

**VLAN & Virtual Networks:**
- [ ] **VLAN Tagging (802.1Q):** Master the 12-bit VLAN ID and priority bits.
- [ ] **VLAN Hopping:** Execute **double-tagging attacks** via trunk misconfigurations.
- [ ] **VLAN Segmentation:** Design and bypass network segmentation strategies.
- [ ] **Management VLANs:** Understand dangers of misconfigured management interfaces.
- [ ] **Private VLANs:** Learn secondary VLAN restrictions and bypass techniques.

**Switch Architecture & Attacks:**
- [ ] **CAM Tables:** Understand **Content Addressable Memory** and port learning mechanisms.
- [ ] **CAM Table Flooding:** Learn to force a switch into "hub mode" and flood traffic.
- [ ] **MAC Flooding Tools:** Master **macof** and similar attack tools.
- [ ] **Port Security:** Understand **sticky MAC**, **MAC aging**, and bypass vectors.
- [ ] **Spanning Tree Protocol (STP):** Understand BPDU manipulation and loop prevention bypass.

**Network Scope & Physical Reach:**
- [ ] **PAN (Personal Area Network):** Bluetooth/NFC range (meters); personal device networks.
- [ ] **LAN (Local Area Network):** Ethernet/WiFi; typically single building or campus.
- [ ] **WLAN (Wireless LAN):** 802.11 networks; understand coverage, roaming, and handoff.
- [ ] **MAN (Metropolitan Area Network):** City-level coverage; typically WiMAX or leased lines.
- [ ] **WAN (Wide Area Network):** Global reach via ISP connections, VPNs, and dedicated circuits.

**Layer 2 Protocols & Analysis:**
- [ ] **Spanning Tree Protocol (STP):** Understand topology changes and BPDU manipulation.
- [ ] **Link Aggregation (802.3ad):** Master **EtherChannel** and multi-link trunking.
- [ ] **LLDP (Link Layer Discovery Protocol):** Learn device discovery and topology mapping.
- [ ] **Packet Capture & Analysis:** Master **Wireshark** for Layer 2 frame analysis.
    

---

### Layer 3: Network (The Routing Logic)

**IP Addressing & Subnetting:**
- [ ] **IPv4 Addressing:** Master **dotted-decimal notation** and **binary conversion** for IP blocks.
- [ ] **Public vs. Private Space:** Know **10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16** and reserved ranges.
- [ ] **Subnet Masks:** Calculate **CIDR notation** (/8, /16, /24, /25, /26, /30, /31, /32).
- [ ] **Wildcard Masks:** Understand inverse notation for **ACL and routing** configurations.
- [ ] **Host Boundaries:** Calculate first host, last host, and broadcast address in any subnet.
- [ ] **IPv6 Addressing:** Master **IPv6 compression**, **link-local**, **ULA**, and **multicast** addressing.
- [ ] **IPv6 Shorthand:** Understand **::1, ::/128, fe80::/10** and common IPv6 patterns.

**Routing & Path Selection:**
- [ ] **Routing Tables:** Understand **route entries**, **metric**, and **next-hop** selection.
- [ ] **Static Routing:** Configure and exploit hardcoded route entries.
- [ ] **Default Route (0.0.0.0/0):** Understand the catch-all and its role in exfiltration.
- [ ] **Route Summarization:** Aggregate multiple subnets into single routing entries.
- [ ] **Longest Prefix Match:** Understand how routers select the most specific route.

**Dynamic Routing Protocols:**
- [ ] **OSPF (Open Shortest Path First):** Master **Areas, LSA, SPF algorithm**, and DR/BDR election.
- [ ] **BGP (Border Gateway Protocol):** Understand **AS numbers, path vectors, and route redistribution**.
- [ ] **EIGRP (Enhanced Interior Gateway Routing Protocol):** Master Cisco proprietary **DUAL algorithm** and metrics.
- [ ] **RIP (Routing Information Protocol):** Understand legacy distance-vector protocol and 15-hop limit.
- [ ] **Routing Protocol Vulnerabilities:** Learn **route injection, spoofing, and redistribution attacks**.

**NAT & PAT Mechanics:**
- [ ] **Static NAT:** Understand 1:1 IP mapping for incoming connections.
- [ ] **Dynamic NAT:** Learn pool-based translation with overloading.
- [ ] **PAT (Port Address Translation):** Master how thousands of internal hosts share one public IP.
- [ ] **NAT Bypass:** Use **port forwarding, UPnP, and SSDP** to bypass internal restrictions.
- [ ] **NAT Traversal:** Understand **STUN, TURN**, and techniques for P2P across NAT boundaries.
- [ ] **NAT Vulnerabilities:** Learn **ARP spoofing behind NAT** and dual-stack exploitation.

**Gateway & Border Security:**
- [ ] **Default Gateway:** Master the primary exit point for all non-local traffic.
- [ ] **Gateway Discovery:** Use **DHCP analysis** and **traceroute** to identify gateways.
- [ ] **Gateway Vulnerabilities:** Exploit **ICMP redirects** and **gateway impersonation**.
- [ ] **Firewall Positioning:** Understand **edge protection** and **DMZ** designs.
- [ ] **Exit Points:** Identify alternative exfiltration paths (secondary gateways, VPNs, proxies).

**ICMP & Diagnostics:**
- [ ] **Ping (Echo Request/Reply):** Understand ICMP type 8/0 and reachability testing.
- [ ] **Traceroute (TTL Exceeded):** Master hop-by-hop path discovery and **UDP/TCP variants**.
- [ ] **ICMP Redirects:** Learn type 5 redirects used in **MITM attacks**.
- [ ] **ICMP Tunneling:** Master data exfiltration via ICMP payloads.
- [ ] **ICMP Filtering:** Understand **ping blocking** and defensive implications.
    

---

### Layer 4: Transport (The Reliability Layer)

**TCP Protocol Mechanics:**
- [ ] **TCP Header Structure:** Master **source/destination ports, sequence numbers, acknowledgments**.
- [ ] **TCP Flags:** Understand **SYN, ACK, FIN, RST, PSH, URG** and their roles in connection states.
- [ ] **Three-Way Handshake:** Master **SYN, SYN-ACK, ACK** sequence for connection establishment.
- [ ] **TCP State Machine:** Understand **LISTEN, SYN_SENT, SYN_RECEIVED, ESTABLISHED, FIN_WAIT, CLOSE_WAIT, CLOSED**.
- [ ] **Window Scaling:** Master **TCP window size** and **flow control** mechanisms.
- [ ] **TCP Options:** Understand **MSS, SACK, Timestamps, and Window Scaling** negotiation.

**UDP Protocol & Characteristics:**
- [ ] **UDP Header:** Understand lightweight **source port, destination port, length, checksum**.
- [ ] **Connectionless Nature:** Learn stateless operation and lack of delivery guarantees.
- [ ] **UDP Use Cases:** Master applications for **DNS, DHCP, NTP, SNMP, RTP** (real-time media).
- [ ] **UDP Flooding:** Understand **bandwidth attacks** and amplification vectors.

**Port & Service Enumeration:**
- [ ] **Common Ports:** Memorize **SSH (22), RDP (3389), DNS (53), HTTP (80), HTTPS (443)**.
- [ ] **Mail Services:** Master **SMTP (25), POP3 (110), IMAP (143)** and secure variants.
- [ ] **Directory Services:** Understand **LDAP (389), Kerberos (88)** and **Active Directory** implications.
- [ ] **Database Ports:** Know **MySQL (3306), MSSQL (1433), PostgreSQL (5432), Oracle (1521)**.
- [ ] **Application Ports:** Understand **RPC (135), NetBIOS (139,445), VNC (5900)** and exploitation risks.

**Network Scanning & Reconnaissance:**
- [ ] **Nmap TCP Scan:** Master **-sS (SYN), -sT (connect), -sA (ACK)** scan types.
- [ ] **Nmap UDP Scan:** Understand **-sU** and **ICMP unreachable** responses.
- [ ] **FIN, NULL, Xmas Scans:** Learn **stealth techniques** and firewall evasion via flag combinations.
- [ ] **ACK Scan:** Understand mapping of **filtered vs. unfiltered** ports (firewall rules).
- [ ] **Idle/Zombie Scan:** Master source IP spoofing using **idle hosts** as proxy.
- [ ] **Timing Templates:** Understand **-T0 (paranoid) through -T5 (insane)** for evasion vs. speed.

**TCP/UDP Vulnerabilities & Attacks:**
- [ ] **SYN Flood:** Understand **half-open connections** and resource exhaustion.
- [ ] **TCP Sequence Prediction:** Learn **session hijacking** via predicted sequence numbers.
- [ ] **RST Injection:** Master connection termination attacks.
- [ ] **ACK Flooding:** Understand **bandwidth amplification** and detection evasion.
- [ ] **Port Knocking:** Learn **knock-based firewall bypass** sequences.
- [ ] **Source Port Spoofing:** Understand **DNS amplification** and **NTP reflection** attacks.

**Transport Layer Filtering:**
- [ ] **Stateless Firewalls:** Understand **ACL-based blocking** and bypass via fragmentation.
- [ ] **Stateful Firewalls:** Learn **connection state tracking** and evasion techniques.
- [ ] **IDS/IPS Evasion:** Master **packet fragmentation, timing delays, and payload obfuscation**.
    

---

### Layers 5-7: Application & Session (The Payload)

**DNS Protocol & Exploitation:**
- [ ] **DNS Record Types:** Master **A, AAAA, MX, CNAME, NS, SOA, TXT, SPF, DKIM**.
- [ ] **DNS Query Process:** Understand **recursive vs. iterative** queries and resolver chain.
- [ ] **DNS Caching:** Learn **TTL (Time-To-Live)** and cache timing implications.
- [ ] **DNS Poisoning:** Master **cache poisoning** to redirect traffic to attacker IPs.
- [ ] **DNS Amplification:** Understand **reflection attacks** using open resolvers.
- [ ] **DNS Exfiltration:** Learn data extraction via **DNS queries** (stealth covert channel).
- [ ] **DNSSEC:** Understand digital signing and validation of DNS responses.
- [ ] **DNS Tools:** Master **nslookup, dig, host** for reconnaissance and manipulation.

**DHCP Protocol & Attacks:**
- [ ] **DHCP Lease Cycle:** Understand **DISCOVER, OFFER, REQUEST, ACK** sequence.
- [ ] **DHCP Options:** Master **Option 3 (gateway), Option 6 (DNS), Option 15 (domain)**.
- [ ] **DHCP Starvation:** Learn **DHCP exhaustion** attacks to kill availability.
- [ ] **Rogue DHCP Server:** Understand **DHCP spoofing** to distribute attacker IPs as gateway.
- [ ] **DHCP Snooping:** Learn **DHCP filtering** and detection of rogue servers.
- [ ] **DHCP Relay:** Understand across-subnet DHCP and manipulation vectors.

**Authentication Protocols:**
- [ ] **Kerberos (Port 88):** Master **TGT, TGS, and mutual authentication** with Windows AD.
- [ ] **LDAP (Port 389):** Understand **directory queries** and **credential validation** against AD.
- [ ] **RADIUS (Port 1812):** Learn **shared secret** based remote authentication for dial-up/wireless.
- [ ] **TACACS+ (Port 49):** Understand **Cisco AAA** protocol with better encryption than RADIUS.
- [ ] **NTLM:** Master **challenge-response** authentication and hash passing attacks.
- [ ] **OAuth 2.0:** Understand **authorization code flow, tokens**, and **token theft** risks.
- [ ] **SAML:** Learn **XML-based** federated authentication and **assertion forgery**.

**SSL/TLS & Encryption:**
- [ ] **TLS Handshake:** Master **ClientHello, ServerHello, key exchange, finished messages**.
- [ ] **Certificate Chain:** Understand **root, intermediate, end-entity** certificates and validation.
- [ ] **Cipher Suites:** Master **key exchange (RSA, DH, ECDH), encryption (AES, 3DES), hash (SHA)**.
- [ ] **SSL Stripping:** Learn **downgrade attacks** to force HTTP over HTTPS.
- [ ] **HSTS (HTTP Strict-Transport-Security):** Understand pinning to prevent SSL stripping.
- [ ] **Certificate Pinning:** Learn **public key / certificate pinning** in applications.
- [ ] **TLS Vulnerabilities:** Understand **Heartbleed, POODLE, BEAST, CRIME** and mitigation.
- [ ] **Perfect Forward Secrecy (PFS):** Master **ephemeral key exchange** to limit past compromise.

**HTTP Protocol & Web Attacks:**
- [ ] **HTTP Methods:** Understand **GET, POST, PUT, DELETE, PATCH, OPTIONS, HEAD**.
- [ ] **HTTP Headers:** Master **Host, User-Agent, Authorization, Cookie, X-Forwarded-For**.
- [ ] **Status Codes:** Know **2xx (success), 3xx (redirect), 4xx (client), 5xx (server)**.
- [ ] **Session Cookies:** Understand **HttpOnly, Secure, SameSite** flags and cookie theft.
- [ ] **HTTP/2 & HTTP/3:** Master **multiplexing, server push**, and new vulnerability surfaces.
- [ ] **REST APIs:** Understand **resource endpoints, authentication, rate limiting** bypass.

**Session & Application Layer Attacks:**
- [ ] **Session Hijacking:** Steal cookies via **network sniffing, XSS, malware**.
- [ ] **Session Fixation:** Force victim into attacker-known session ID.
- [ ] **CSRF (Cross-Site Request Forgery):** Exploit **state-changing actions** without user knowledge.
- [ ] **SSRF (Server-Side Request Forgery):** Abuse **server trust** to access internal resources.
- [ ] **XXE (XML External Entity):** Parse **malicious XML** to read files or launch DOS.
- [ ] **Injection Attacks:** Understand **SQL, command, LDAP** injection for backend compromise.
- [ ] **Deserialization:** Learn **unsafe object unmarshaling** leading to RCE.

**VPN & Tunneling Protocols:**
- [ ] **IPSec (Layer 3):** Master **AH, ESP**, tunnel vs. transport modes, and key exchange.
- [ ] **GRE (Generic Routing Encapsulation):** Understand **stateless tunneling** and encapsulation.
- [ ] **OpenVPN (Layer 3/4):** Learn **SSL/TLS-based** VPN with UDP/TCP.
- [ ] **WireGuard:** Understand **lightweight, kernel-space** modern VPN protocol.
- [ ] **VPN Bypass:** Learn **DNS leaks, IPv6 leaks**, and split-tunneling exploitation.

**Network Monitoring & Analysis:**
- [ ] **Packet Capture (tcpdump/Wireshark):** Master **filter syntax** and protocol dissection.
- [ ] **NetFlow/sFlow:** Understand **flow-based monitoring** for traffic patterns without full capture.
- [ ] **Proxy Servers:** Master **transparent, forward** proxies and **man-in-the-middle** positioning.
- [ ] **IDS/IPS Systems:** Understand **signature-based detection** and evasion techniques.
- [ ] **SIEM Concepts:** Learn **log aggregation, correlation**, and **alert tuning**.
    

---

### Advanced Topics: Lab Progression & Professional Development

- [ ] **Lab Progression:** Move from **Packet Tracer** (Beginner) to **GNS3/EVE-NG** (Advanced) and **Wireshark**.
    
- [ ] **Virtualization:** Master Type-1 (**ESXi, Proxmox**) and Type-2 (**VMWare, VirtualBox**) hypervisors.
    
- [ ] **Cloud Assets:** Master **VPCs**, **Security Groups**, **Load Balancers**, and **IAM** in AWS/Azure/GCP.
    
- [ ] **Automation:** Use **Python, Bash, and PowerShell** for subnet discovery and log clearing.
    
- [ ] **Monitoring & Evasion:** Use **NetFlow, SNMP**, and packet analyzers to understand **Zero Trust** and **SIEM/SOAR** limits.
    
- [ ] **Certifications:** Focus on **CCNA** (Networking Core) or **CompTIA Network+** (Beginner Path).
    
- [ ] **Ethics & ROE:** Master the **Rules of Engagement (RoE)** and professional reporting.


	