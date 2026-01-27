# Red Team Fundamentals: Master Checklist

## 📋 Quick Navigation

- [Part 1: Fundamentals](#part-1-fundamentals) (Hardware, OS, Memory, Data, Wireless, Applications)
- [Part 2: Networking Fundamentals](#part-2-networking-fundamentals) (Layers 1-7, Protocols, Tools)
- [Part 3: Footprinting & Reconnaissance](#part-3-footprinting-and-reconnaissance) (Passive → Active → Strategy)
- [Part 4: Scanning](#part-4-scanning) (Host Discovery → Port Enumeration → Defense Assessment)
- [Part 5: Enumeration](#part-5-enumeration) (Network Discovery → Service Profiling → Attack Mapping)
- [Part 6: System Hacking & Initial Compromise](#part-6-system-hacking--initial-compromise) (Breach → Escalation → Persistence → Evasion → Exfil → Reporting)
- [Part 7: Malware & Weaponization](#part-7-malware--weaponization) (Design → Weaponization → Evasion → Persistence → Anti-Forensics)
- [Part 8: Detection & Mitigation](#part-8-detection--mitigation) (Blue Team perspective for understanding defensive detection)
- [Part 9: Sniffing & Spoofing](#part-9-sniffing--spoofing) (Protocols → Sniffing → Spoofing → MITM → Defenses)
- [Part 10: Social Engineering](#part-10-social-engineering) (Recon → Digital → Human → Physical → Defense)
- [Part 11: Denial of Service](#part-11-denial-of-service) (Planning → Methods → Execution → Mitigation)
- [Part Extra: Red Team Operations & Tradecraft](#part-extra-red-team-operations--tradecraft) (Infrastructure, Discipline, Operations)

---

## Part 1: Fundamentals

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

### 5a. Mobile Security

**Android Security:**
- [ ] **APK Reverse Engineering:** Decompile **APK files** with **apktool/jadx**, analyze **smali code**, modify and repackage apps.

- [ ] **Root Detection Bypass:** Patch **SafetyNet, Magisk Hide** checks, hide **su binaries** from detection routines.

- [ ] **Certificate Pinning Bypass:** Hook **SSLContext/TrustManager** with **Frida/Xposed** to intercept **HTTPS traffic**.

- [ ] **Intent Exploitation:** Abuse **exported activities/services**, craft malicious **intents** for **privilege escalation/data theft**.

- [ ] **Storage Analysis:** Extract data from **shared preferences, SQLite databases, internal storage** on rooted devices.

**iOS Security:**
- [ ] **IPA Analysis:** Unpack **IPA files**, analyze **Mach-O binaries**, inspect **Info.plist** and embedded provisioning.

- [ ] **Jailbreak Detection Bypass:** Patch **integrity checks**, hide **Cydia/Sileo**, use **A-Bypass/Shadow** hooks.

- [ ] **SSL Pinning Bypass:** Use **SSL Kill Switch, Burp CA**, or **Frida scripts** to intercept encrypted traffic.

- [ ] **Keychain Extraction:** Dump **keychain items** on jailbroken devices using **keychain_dumper/Clutch**.

- [ ] **Runtime Manipulation:** Hook **Objective-C methods** with **Frida/Cycript** for dynamic analysis.

**Mobile Device Management (MDM) & Enterprise:**
- [ ] **MDM Bypass:** Exploit **enrollment gaps**, remove **configuration profiles**, escape **DEP/supervised mode**.

- [ ] **Enterprise App Abuse:** Sideload **unsigned apps** via **enterprise certificates**, exploit **provisioning misconfigs**.

- [ ] **Mobile Malware Delivery:** Craft **phishing campaigns** targeting **mobile users**, abuse **SMS/MMS** for payload delivery.

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

## Part 2: Networking Fundamentals

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


## Part 3: Footprinting and Reconnaissance

### **Phase 1: The "Ghost" Phase (Passive OSINT & Human Profiling)**

_Goal: Maximum data acquisition with zero target interaction._

- [ ] **Organizational Hierarchy:** Profile the **Audience** (Stakeholders, HR, Legal, Management) to understand who holds the keys and who is the weakest link.
    
- [ ] **Search Engine Hacking:** Use **Google Dorks** (`site:`, `filetype:`, `intitle:`) to find exposed documents and login portals.
    
- [ ] **Social Vector Mapping:** Scrape LinkedIn and professional sites to identify targets for **Phishing, Whishing, Whaling, or Smishing** based on reported tech stacks.
    
- [ ] **Physical Perimeter Assessment:** Evaluate the likelihood of **Shoulder Surfing, Tailgating, or Dumpster Diving** vulnerabilities.
    
- [ ] **Metadata & Leak Analysis:** Use **Wayback Machine** for historical paths and **GitHub/GitLab Dorking** for hardcoded API keys or internal naming conventions.
    
- [ ] **Domain & Ownership:** Perform **WHOIS Lookups** to identify registration dates, contact info, and associated subdomains.

- [ ] **Passive DNS & CT:** Pull **passive DNS** and **Certificate Transparency (crt.sh)** to surface shadow subdomains and SANs; cluster hosting/ASN/country.

- [ ] **Breach & Paste Monitoring:** Check **breach corpuses** (HIBP/Dehashed) and pastes/code search for leaked creds, API keys, or internal hostnames.

- [ ] **Mail Posture Recon:** Review **SPF/DMARC/DKIM** to assess spoofing risk and likely mail providers.
    

---

### **Phase 2: Semi-Passive Infrastructure Mapping**

_Goal: Querying third-party aggregators to see what the world already knows about them._

- [ ] **External Intel Scouring:** Query **VirusTotal, urlscan, any.run, Joe Sandbox, and urlvoid** for existing malware samples or documented domain behavior.
    
- [ ] **Third-Party Scans:** Use **Shodan & Censys** to find open ports, outdated services, and geographical distribution without scanning the target yourself.
    
- [ ] **Subdomain & DNS Enumeration:** Use **Sublist3r/Amass** for subdomains and check **DNS records** (MX, TXT, NS) to map mail providers and third-party integrations.
    
- [ ] **Protocol Audit:** Identify if the target is clinging to **Insecure Protocols** (FTP vs. SFTP, SSL vs. TLS).

- [ ] **WAF/CDN/TLS Fingerprinting:** Detect **WAF/CDN** fronting via **JA3/JA4, HTTP header quirks, TLS ALPN/HTTP2**, and favicon hashes.

- [ ] **VHost & Favicon Hunts:** Bruteforce **vhosts/domains** and use **favicon hash**/HTTP header diffs to find hidden apps.
    

---

### **Phase 3: Active Footprinting & Network Interrogation**

_Goal: Direct contact to map the live network fabric. Risk of detection is now ACTIVE._

- [ ] **Live Host Discovery:** Use **ping, arp, and hping** to identify which internal or external assets are actually breathing.
    
- [ ] **Network Path Analysis:** Use **tracert** to map the hops and identify **Perimeter vs. DMZ vs. Segmentation** boundaries.
    
- [ ] **Surgical Port Scanning:** Execute **Nmap Essentials** (starting with `-sS` stealth scans) to identify listening services and **OS Fingerprinting**.
    
- [ ] **Aggressive DNS Interrogation:** Use **nslookup and dig** to force the disclosure of hidden internal records or mail servers.
    
- [ ] **Web Content Discovery:** Run **ffuf or Gobuster** for directory brute-forcing and use **Wappalyzer** for technology profiling (CMS, frameworks, databases).

- [ ] **TLS Surface:** Harvest **cert SANs**, check **cipher/curve** support, **HTTP/2/ALPN** negotiation, and redirect/downgrade behavior.

- [ ] **Web Route Mapping:** Parse **robots.txt/sitemap.xml** and fuzz **parameters/paths** with status/length filters to uncover hidden routes.
    

---

### **Phase 4: Advanced Fingerprinting & Logic Analysis**

_Goal: Understand the defensive "brain" of the target._

- [ ] **Traffic Analysis:** If vantage is gained, use **Wireshark** to analyze **Packet Captures** and examine **Handshakes** for encryption/auth weaknesses.
    
- [ ] **Defensive Profiling:** Identify the presence of **IDS/IPS, SIEM, SOAR, and EDR/DLP**. If found, slow down your operation immediately.
    
- [ ] **Unintended Binary Research:** Map the target's OS to potential **LOLBAS, GTFOBINS, or WADCOMS** vectors for later movement.

- [ ] **Version-to-CVE Correlation:** Cluster hosts by **banners/JA3/favicons** and map exposed versions to **CVE** candidates before exploitation.
    

---

### **Phase 5: Strategy & Attack Mapping**

_Goal: Convert raw data into an execution plan._

- [ ] **Security Architecture Classification:** Determine if they are utilizing **Zero Trust** or standard **MFA & 2FA**.
    
- [ ] **Framework Alignment:** Map your findings against the **Cyber Kill Chain, Diamond Model, or MITRE ATT&CK**.
    
- [ ] **Vulnerability Finalization:** Decide the entry vector based on recon: **SQL Injection, MITM, or Brute Force**.

## Part 4: Scanning

### **Stage 1: Host Discovery & Network Topology (The "Roll Call")**

_Goal: Identify live assets without wasting time on dead IPs or triggering ICMP alarms._

- [ ] **ARP Discovery:** Use `arp-scan` or `nmap -PR` for local segment discovery to bypass host firewalls that drop ICMP.
    
- [ ] **ICMP & TCP/UDP Sweeps:** Perform standard `ping` sweeps or use `nmap -PS/-PU` (ports 80, 443, 53) to find external hosts that block standard pings.
    
- [ ] **Passive Traffic Capture:** Utilize **Wireshark** to capture broadcast traffic, revealing active hosts without sending a single packet.
    
- [ ] **Network Pathing & Perimeter Analysis:** Deploy `tracert` or `hping3 --traceroute` to map hops and define **Perimeter vs DMZ vs Segmentation** boundaries.

- [ ] **IPv6 Discovery:** Include **NDP/`nmap -6`** sweeps for dual-stack assets and SLAAC-derived hosts.
    

---

### **Stage 2: Port, Service & Protocol Enumeration (The "Door Check")**

_Goal: Determine exactly what applications are running and how they communicate._

- [ ] **Stealth SYN Scanning:** Use `nmap -sS` to identify open ports without completing the three-way **Handshake**, minimizing your footprint in application logs.
    
- [ ] **Version & OS Fingerprinting:** Deploy `nmap -sV` for service banners and `nmap -O` to analyze TCP/IP stack responses for **Operating System Hardening** clues.
    
- [ ] **Protocol Audit:** Analyze discovered services to determine if they use **Secure vs Insecure Protocols** (e.g., FTP vs SFTP, SSL vs TLS).
    
- [ ] **Connection Handshake Analysis:** Examine **Handshakes** to understand the specific authentication and encryption methods protecting the service.
    
- [ ] **UDP Surface Check:** Do not ignore `nmap -sU` for often-overlooked services like DNS (53), SNMP (161), and DHCP (67).

- [ ] **Timing & Hygiene:** Apply sane **-T profiles**, exclusion lists, and prefer **safe NSE** scripts before vuln categories to avoid tripping controls.

- [ ] **IPv6 Stack:** Mirror key scans with **`nmap -6`** for IPv6 services.
    

---

### **Stage 3: Defense & Configuration Assessment (The "Armor Check")**

_Goal: Identify security controls that will attempt to block or alert on your presence._

- [ ] **Firewall & ACL Enumeration:** Detect the presence of a **Firewall & Nextgen Firewall** or **Host Based Firewalls** by analyzing filtered ports and **ACL** (Access Control List) behavior.
    
- [ ] **IDS/IPS Probing:** Use fragmentation (`-f`) or timing decoys (`-D`) to identify active **NIDS, NIPS, or HIPS** systems that may block aggressive patterns.
    
- [ ] **Web Surface Discovery:** Use `ffuf` or `Gobuster` for **Directory Brute-forcing** to find hidden `/admin` or `/config` panels that are not linked publicly.

- [ ] **Service-Specific Enum:** Targeted checks for **SMB/RPC/WinRM**, **LDAP/Kerberos (AS-REP preauth, SPNs)**, **SNMP v1/v2c/v3**, **SMTP VRFY/EXPN**, **SSH KEX/ciphers**, **RDP/NLA**, **DBs (MySQL/MSSQL/Postgres)**, **Redis/Mongo/Elastic**.
    

---

### **Stage 4: Vulnerability Association & Attack Mapping**

_Goal: Convert raw scan data into actionable exploitation vectors._

- [ ] **Scripted Vulnerability Probing:** Use the **Nmap Scripting Engine (NSE)** (`--script vuln`) to check for known **Zero Day** or common exploits in identified versions.
    
- [ ] **Attack Surface Selection:** Match findings to your known **Common Attacks**—e.g., **SQL Injection** for web servers or **Buffer Overflows** for legacy binaries.
    
- [ ] **Unintended Tool Research:** For discovered OS versions, research **LOLBAS, GTFOBINS, or WADCOMS** to leverage existing system binaries for lateral movement.
    
- [ ] **Traffic Intelligence:** Finalize your plan by inspecting **Packet Captures** for cleartext protocols or weak encryption that allows for **MITM** or **Replay Attacks**.

- [ ] **Cluster & Correlate:** Group hosts by **banners/JA3/favicons** and map versions to likely **CVEs** before exploitation.

## Part 5: Enumeration

### **Phase 1: Foundations & Network Discovery (The "Ghost" Phase)**

_Goal: Build a theoretical base while mapping the live environment with zero noise._

- [ ] **Core Principles & Discovery:** Apply the **CIA Triad** and **Definition of Risk** to identify high-value targets. Use `ping` and `arp` for **Live Host Identification**.
    
- [ ] **Stealth Host Mapping:** Use `arp-scan` or `nmap -PR` for local segments to bypass **Host Based Firewalls**. Utilize **Wireshark** for passive traffic capture to reveal hosts without sending packets.
    
- [ ] **Pathing & Perimeter Analysis:** Deploy `tracert` or `hping3 --traceroute` to map network hops. Define the boundaries between **Perimeter vs DMZ vs Segmentation** to understand the **Concept of Isolation**.
    
- [ ] **Cryptographic Baseline:** Understand the **Basics of Cryptography**, specifically **Hashing** and **Salting**, to recognize how stored credentials might be protected.

- [ ] **TLS & Mail Recon:** Collect **cert SANs**, cipher/curve support, **SPF/DMARC/DKIM**, and note redirect/downgrade behaviors.
    

---

### **Phase 2: Service Enumeration & Defense Profiling (The "Door Check")**

_Goal: Interrogate listening services while identifying the target's "armor."_

- [ ] **Stealth Port Scanning:** Execute `nmap -sS` (SYN scan) to identify open ports without completing the **Handshake**, keeping your footprint out of application logs.
    
- [ ] **Service & OS Fingerprinting:** Use `nmap -sV` for banners and `nmap -O` for **Operating System Hardening** clues. Identify the use of **Antivirus**, **EDR**, or **HIPS**.
    
- [ ] **Protocol & Handshake Audit:** Analyze discovered services for **Secure vs Insecure Protocols** (e.g., FTP vs SFTP, SSL vs TLS). Examine connection **Handshakes** to understand authentication and encryption.
    
- [ ] **Defensive Technology Identification:** Map the presence of a **Firewall & Nextgen Firewall**, **IDS and IPS**, and **ACLs** by analyzing filtered ports and packet fragmentation.

- [ ] **IPv6 & Dual-Stack:** Repeat key enumeration over **IPv6** where present.
    

---

### **Phase 3: Vulnerability Association & Attack Mapping**

_Goal: Convert raw scan data into actionable exploitation vectors._

- [ ] **Scripted Probing & Zero-Days:** Use the **Nmap Scripting Engine (NSE)** (`--script vuln`) to check for **Known vs Unknown** vulnerabilities and **Zero Day** potential.
    
- [ ] **Attack Vector Selection:** Match findings to **Common Attacks**:
    
    - **Web:** Use `ffuf` or `Gobuster` for **Directory Traversal** and **SQL Injection**.
        
    - **Network:** Prep for **MITM** or **Replay Attacks** based on cleartext **Packet Captures**.
        
    - **System:** Research **LOLBAS**, **GTFOBINS**, or **WADCOMS** to leverage existing binaries for **Privilege Escalation**.
        
- [ ] **Identity Attack Prep:** If **Active Directory** is detected, plan for **Pass the Hash** or **Kerberoasting** by auditing **Authentication vs Authorization** protocols.

- [ ] **Service-Focused Deep Dives:** Enumerate **SMB/LDAP/Kerberos/WinRM**, **SNMP**, **SMTP**, **SSH/RDP**, and **databases** with safe scripts/banners before vuln scans.
    

---

### **Phase 4: Governance & Operational Response**

_Goal: Align offensive findings with industry standards and professional reporting._

- [ ] **Framework Alignment:** Map discovered vulnerabilities against the **Cyber Kill Chain**, **Diamond Model**, or **MITRE ATT&CK** framework.
    
- [ ] **Compliance & Reporting:** Tailor your findings for the correct **Audience** (Stakeholders, HR, Legal, or Management). Reference standards like **NIST**, **ISO**, or **CIS** to provide context for remediation.
    
- [ ] **Incident Response Integration:** Understand the **Incident Response Process** (Preparation to Lessons Learned) to anticipate how a **Blue Team** will react to your presence.


## Part 6: System Hacking & Initial Compromise

### **Phase 1: The Breach (Initial Access & Exploitation)**

_Goal: Weaponize theoretical vulnerabilities to bypass the perimeter and establish foothold._

**Application & Web Exploitation:**
- [ ] **SQL Injection:** Craft payloads for **error-based, blind, union-based, and time-based** exfiltration.

- [ ] **Buffer Overflow:** Target legacy binaries; craft **ROP chains** to bypass **ASLR/DEP**.

- [ ] **Directory/Path Traversal:** Abuse improper input validation to read **system files, configs, or keys**.

- [ ] **SSTI/Template Injection:** Exploit **Jinja2, Twig, ERB** misconfigs for **RCE**.

- [ ] **Deserialization:** Attack unsafe **Java/Python/PHP** unmarshaling for code execution.

- [ ] **SSRF:** Abuse server trust to pivot to **internal APIs, cloud metadata (IMDS), or localhost services**.

- [ ] **XXE/XML External Entity:** Parse malicious XML for **file read, XXE blind**, and **DOS**.

- [ ] **API Endpoint Abuse:** Exploit **BOLA/BFLA** (Broken Object/Function Level Auth) and **rate-limit bypass**.

- [ ] **Authentication Bypass:** Exploit **logic flaws** in login flows, abuse **password reset tokens**, manipulate **OAuth state parameters**.

- [ ] **Business Logic Flaws:** Identify **race conditions, insufficient workflow validation, price manipulation** in checkout/transaction flows.

- [ ] **File Upload Vulnerabilities:** Bypass **extension filters**, use **null bytes, double extensions, MIME type confusion** to upload **web shells**.

- [ ] **CAPTCHA Bypass:** Exploit **client-side validation**, reuse **tokens**, automate with **OCR/ML models**, abuse **audio alternatives**.

- [ ] **GraphQL Exploitation:** Perform **introspection queries**, abuse **batching/aliasing** for **DoS**, exploit **nested queries** and **IDOR**.

**Credential Assault:**
- [ ] **Brute Force:** Methodical password guessing with **wordlists, rule-based mangling**.

- [ ] **Password Spray:** Low-and-slow attacks across many accounts to avoid lockout.

- [ ] **Default Creds:** Enumerate and test **factory defaults** (admin/admin, root/root).

- [ ] **MFA Bypass:** Exploit **MFA fatigue, SIM-swap, push notification spoofing**.

- [ ] **Credential Stuffing:** Reuse leaked passwords from **breach corpuses** (HIBP/Dehashed).

**Human Vector & Social Engineering:**
- [ ] **Phishing:** Craft **HTML-smuggled payloads, ISO/LNK loaders, OneNote macros** with pretexting.

- [ ] **Whaling/Spear Phishing:** Target **executives** with personalized, researched lures.

- [ ] **Smishing/Vishing:** Use **SMS/voice** to deliver **URL shorteners, MFA prompts, or fake updates**.

- [ ] **Pretext:** Build **fake contractor, vendor, or IT support** persona to extract credentials verbally.

- [ ] **Watering Hole:** Compromise **public websites** frequented by targets to deliver **malware/tracker**.

**Network Interception & MITM:**
- [ ] **ARP Spoofing:** Poison **ARP tables** to intercept **unencrypted traffic**.

- [ ] **DNS Spoofing:** Redirect traffic via **cache poisoning or rogue DNS servers**.

- [ ] **SSL Stripping:** Downgrade **HTTPS to HTTP** when **HSTS** is weak or absent.

- [ ] **WiFi Evil Twin:** Build **rogue AP** with **karma/auto-join** to harvest credentials and inject payloads.

- [ ] **NGO Interception:** Capture traffic at **network gateways/bridges** with **tcpdump/Wireshark**.

---

### **Phase 2: The Ascension (Privilege Escalation)**

_Goal: Move from low-level foothold to administrative control by exploiting system logic._

**Windows Privilege Escalation:**
- [ ] **UAC Bypass:** Exploit **COM elevation, DLL hijack, token impersonation** to bypass **User Account Control**.

- [ ] **Service Misconfigs:** Abuse **weak service permissions, unquoted paths, service binaries** for **privilege hijack**.

- [ ] **Token Impersonation:** Steal **delegation tokens** from services to impersonate **SYSTEM/Domain Admin**.

- [ ] **DLL/DLL-Proxying:** Hijack **DLL search order** or use **sideloading** to execute arbitrary code at higher privilege.

- [ ] **Kernel Exploitation:** Target **unpatched zero-days** (MS21-1234) for **kernel-level code execution**.

- [ ] **Group Policy Exploitation:** Abuse **GPP passwords, startup scripts, scheduled tasks** for **privilege gain**.

**Active Directory Attacks:**
- [ ] **Kerberoasting:** Extract **TGS tickets** for **service accounts (SPNs)**, crack offline with **hashcat/JtR** to recover **plaintext passwords**.

- [ ] **AS-REP Roasting:** Target accounts with **pre-authentication disabled**, extract **AS-REP hashes** for offline cracking.

- [ ] **Golden/Silver Tickets:** Forge **TGT (Golden)** or **TGS (Silver)** tickets using **krbtgt hash** or **service account hash** for **persistent domain access**.

- [ ] **DCSync Attack:** Abuse **replication rights** to extract **password hashes** from **Domain Controller** without direct access.

- [ ] **BloodHound/SharpHound:** Map **AD trust relationships, ACLs, group memberships** to find **shortest path to Domain Admin**.

- [ ] **NTLM Relay:** Capture **NTLM authentication** and relay to **SMB/LDAP/HTTP** services for **lateral movement**.

- [ ] **Constrained/Unconstrained Delegation:** Abuse **delegation rights** to impersonate **privileged users** across domain services.

**Linux Privilege Escalation:**
- [ ] **setuid/setgid Abuse:** Exploit **vulnerable SUID binaries** (vim, cp, find) with **PATH manipulation**.

- [ ] **Capabilities Abuse:** Abuse **CAP_SETUID/CAP_SYS_ADMIN** for **shell execution as root**.

- [ ] **sudo Misconfigs:** Leverage **sudoers entries** (NOPASSWD, wildcard paths) for **privilege escalation**.

- [ ] **Kernel LPE:** Exploit **unpatched kernel vulnerabilities** (dirty cow, CVE-2016-5195) for **root shell**.

- [ ] **Cron/Systemd Abuse:** Hijack **cron jobs, systemd timers, .timer files** for **privilege execution**.

**Container & K8s Breakout:**
- [ ] **Mounted docker.sock:** Escape **container to host** via **Docker socket abuse**.

- [ ] **Privileged Containers:** Escape from **--privileged, CAP_SYS_ADMIN** containers.

- [ ] **hostPath Mounts:** Write to **host filesystem** via mounted volumes for **persistence**.

- [ ] **RBAC/CNI Misconfigs:** Abuse **Kubernetes role bindings** and **network policy gaps**.

**Cloud Platform Attacks:**
- [ ] **AWS IAM Exploitation:** Enumerate **overprivileged roles**, abuse **AssumeRole**, exploit **resource-based policies** for **privilege escalation**.

- [ ] **S3 Bucket Abuse:** Find **public buckets** via **bucket enumeration**, exploit **ACL misconfigs**, steal data from **pre-signed URLs**.

- [ ] **Cloud Metadata Services (IMDS):** Query **169.254.169.254** for **IAM credentials, instance metadata**, use **IMDSv2 bypass** techniques.

- [ ] **Azure AD Exploitation:** Abuse **service principals**, steal **access tokens**, exploit **OAuth consent grants** for lateral movement.

- [ ] **GCP Service Accounts:** Steal **service account keys**, abuse **IAM bindings**, exploit **Compute Engine metadata**.

- [ ] **Lambda/Function Abuse:** Inject code into **serverless functions**, abuse **environment variables**, exfil via **function logs**.

**LOLBAS & Living off the Land:**
- [ ] **Windows:** Abuse **PowerShell, WMI, certutil, bitsadmin, mshta** for **execution and evasion**.

- [ ] **Linux:** Leverage **bash, find, awk, sed, curl, wget** for **lateral movement and persistence**.

---

### **Phase 3: The Stronghold (Persistence & Lateral Movement)**

_Goal: Establish permanent presence and move horizontally across network._

**Credential Harvesting & Token Abuse:**
- [ ] **Pass-the-Hash:** Capture **NTLM hashes** and re-authenticate without cracking passwords.

- [ ] **Pass-the-Ticket:** Steal **Kerberos TGS tickets** to access **network services as compromised user**.

- [ ] **LSASS Dumping:** Extract **plaintext creds, hashes** via **mimikatz, procdump, comsvcs.dll**.

- [ ] **Browser/SSO Token Theft:** Harvest **OAuth/SAML tokens, session cookies** from **memory or storage**.

- [ ] **SSH Key Harvesting:** Steal **private keys** from **~/.ssh/id_rsa, agent sockets**.

**Malware & Backdoors:**
- [ ] **Rootkit Deployment:** Hide **files, processes, ports** via **kernel-mode rootkit** for **deep persistence**.

- [ ] **Trojan Backdoors:** Deploy **reverse shells, C2 beacons** disguised as **legitimate services**.

- [ ] **Bootkit/UEFI Implants:** Achieve **pre-OS persistence** via **bootloader compromise**.

- [ ] **Web Shell Placement:** Upload **ASP.NET, PHP, JSP** shells to **web-root** for **persistent access**.

- [ ] **Cron/Registry Backdoors:** Install **cron jobs, registry RunOnce** for **automatic re-execution**.

**Lateral Movement & Pivoting:**
- [ ] **SMB/WinRM:** Use **PsExec, Invoke-Command** to execute **commands on adjacent machines**.

- [ ] **SSH Agent Hijack:** Compromise **SSH forwarding** to move to **key-trusted hosts**.
 - [ ] **RDP Relay/NTLM Relay:** Exploit **weak signing** to relay **RDP/HTTP credentials** to **other systems**.

- [ ] **DNS Exfiltration:** Tunnel **data over DNS queries** to exfiltrate **files incrementally**.
 - [ ] **Printer/SNMP Abuse:** Exploit **print servers, SNMP v1/v2c** for **lateral access**.

---

### **Phase 4: The Shadow (Defense Evasion & Anti-Forensics)**

_Goal: Blind the Blue Team and minimize evidence of compromise._

**Log Manipulation & Cleanup:**
 - [ ] **Windows Event Log:** Delete or clear **Security, System, Application** logs; disable **audit logging**.

 - [ ] **Linux Auditd:** Disable **auditd**, flush **auth.log, syslog** via **log rotation abuse**.

 - [ ] **Firewall/SIEM:** Identify **log shipping** and poison **central logs** or syslog streams.

 - [ ] **Application Logs:** Scrub **web server logs, database audit trails, application-specific logs**.

**Defense Evasion:**

- [ ] **EDR Evasion:** Disable **Windows Defender, real-time protection**; abuse **exploit guard gaps**.

- [ ] **DLP Bypass:** Exfil via **covert channels, low-bandwidth tunnels, encryption obfuscation**.

- [ ] **IDS/NIDS Evasion:** Use **packet fragmentation, timing jitter, polymorphic payloads**.

- [ ] **AppArmor/SELinux Bypass:** Disable or escape **mandatory access controls**.

**Anti-Forensics:**
- [ ] **File Deletion:** Use **shred, srm, cipher /w** for **secure wiping** of tools and artifacts.

- [ ] **Timestomping:** Modify **file timestamps** (touch -t, $MFT, xattr) to **hide activity**.

- [ ] **Memory Wiping:** Clear **bash history, .zsh_history, PowerShell history** and environment variables.

- [ ] **Registry Cleanup:** Delete **run keys, browser history, recent documents, prefetch files**.

- [ ] **Obfuscation:** Use **base64, hex, ROT13** to hide **scripts, commands, strings** from pattern matching.

---

### **Phase 5: Data Exfiltration & Impact**

_Goal: Extract sensitive data and demonstrate business impact._

**Data Exfiltration Channels:**
- [ ] **DNS Tunneling:** Encode **data in DNS queries** and exfil via **recursive lookups**.

- [ ] **HTTPS Covert Channels:** Blend **exfil into normal HTTPS** streams with **size/timing variance**.

- [ ] **Cloud APIs:** Use **pre-signed S3/Blob URLs, Drive APIs** for **high-bandwidth exfil**.

- [ ] **ICMP/Ping Tunneling:** Tunnel **data over ping requests** when **TCP/UDP egress blocked**.

- [ ] **Dead-Drop Upload:** Stage **files to attacker-controlled sites** (GitHub gists, pastebin, etc.).

**Impact & Damage:**
- [ ] **Ransomware Deployment:** Encrypt **critical files** with **RSA/AES hybrid** and demand **ransom**.

- [ ] **Data Destruction:** Wipe **backups, system restore points** to prevent **recovery**.

- [ ] **Service Disruption:** Corrupt **databases, config files** to trigger **outages and chaos**.

---

### **Phase 6: The Professional (Governance & Reporting)**

_Goal: Execute within legal/ethical boundaries and deliver findings professionally._

**Rules of Engagement & Compliance:**
- [ ] **Scope Adherence:** Operate only within **authorized IP ranges, domains, systems** per engagement letter.

- [ ] **ROE Documentation:** Track **timeline, actions, access paths, artifacts discovered** for audit trail.

- [ ] **Escalation & Abort:** Know **when to stop, how to notify blue team, emergency procedures**.

- [ ] **Data Handling:** Secure **screenshots, credentials, exfiltrated files** with **encryption, access control**.

**Framework Alignment & Documentation:**
- [ ] **MITRE ATT&CK Mapping:** Correlate **every technique used** (T1234.567) to **documented tactics**.

- [ ] **Kill Chain Analysis:** Track the **Reconnaissance → Weaponization → Delivery → Exploitation → Installation → C2 → Actions** flow.

- [ ] **Vulnerability Timeline:** Document **discovery date, exploitation date, remediation deadline**.

**Audience-Centric Reporting:**
- [ ] **Executive Summary:** Non-technical **risk/impact narrative** for **board/C-suite**.

- [ ] **Technical Deep-Dive:** Detailed **attack chain, proof-of-concept, IOCs** for **security/engineering teams**.

- [ ] **Remediation Roadmap:** Prioritized **fixes by risk level** with **effort estimates and timelines**.

- [ ] **Metrics & KPIs:** Highlight **MTTD (Mean Time to Detect), MTTC (Mean Time to Contain), detection gaps**.

## Part 7: Malware & Weaponization

### **Phase 1: The Design & Logic (Architecture)**

_Goal: Design the malware's purpose using core security principles._

 - [ ] **Target the CIA Triad:** Define if your payload destroys **Integrity** (Wipers/Data modification) or denies **Availability** (Ransomware/DDoS).

 - [ ] **Weaponize Cryptography:** Implement **Public vs Private Keys** (Asymmetric Encryption) to lock files securely, ensuring only the attacker holds the decryption key.

 - [ ] **Cryptographic Attacks:** Understand **padding oracle attacks, timing attacks, weak random number generation** to break encryption implementations.

 - [ ] **Key Management Flaws:** Exploit **hardcoded keys, weak key derivation (KDF), insecure key storage** in applications.

 - [ ] **C2 Protocol Design:** Choose **Secure vs Insecure Protocols** for Command & Control. Will you hide inside **HTTPS** traffic or use **DNS** tunneling to evade **Firewall & Next-Gen Firewall** inspection?

 - [ ] **Risk Assessment:** Use the **Diamond Model** or **Cyber Kill Chain** to map out how your malware will move from **Reconnaissance** to **Actions on Objectives**.
    

---

### **Phase 2: The Payload & Mechanism (Weaponization)**

_Goal: Execute code on the target system._

 - [ ] **Memory Exploitation:** Leverage **Buffer Overflow** or **Memory Leak** vulnerabilities to inject shellcode into legitimate processes, bypassing file scanning.

 - [ ] **Delivery Vectors:** Utilize **Social Engineering** (Phishing/Whaling) or **Drive-by Attacks** to get the initial execution on the endpoint.

 - [ ] **Payload Staging:** Use **Common Exploit Frameworks** (like Metasploit/Cobalt Strike) to package the payload, but modify the signatures to avoid **Known vs Unknown** detection.

 - [ ] **Living off the Land:** Instead of dropping new binaries, use **LOLBAS**, **GTFOBINS**, or **WADCOMS** to execute malicious logic using trusted system tools (e.g., PowerShell, Bash).
    

---

### **Phase 3: Evasion & Defense Bypassing (Invisibility)**

_Goal: Blind the defensive stack._

 - [ ] **Defeat Static Analysis:** Apply **Obfuscation** (packing, encoding) to change the file hash and bypass traditional **Antivirus** signatures.

 - [ ] **Sandbox Detection:** Code the malware to detect **Sandboxing** environments (e.g., checking for specific drivers, lack of mouse movement) and go dormant to generate a **False Negative**.

 - [ ] **EDR/DLP Bypass:** Unhook API calls to hide from **EDR** (Endpoint Detection Response) and **DLP** monitors. Operate in memory (Fileless) to avoid leaving disk artifacts.

 - [ ] **Traffic Masking:** Encrypt C2 traffic to look like normal web browsing, defeating **NIDS/NIPS** (Network Intrusion Prevention Systems).
    

---

### **Phase 4: Persistence & Escalation (Entrenchment)**

_Goal: Survive reboots and gain total control._

 - [ ] **Privilege Escalation:** Exploit **Operating System Hardening** gaps or **Kernel** vulnerabilities (Zero Day) to escalate from User to **SYSTEM/Root**.

 - [ ] **Persistence Mechanisms:** Hide payload execution in **Scheduled Tasks**, **Registry Keys**, or **WMI** subscriptions to survive **Patching** and reboots.

 - [ ] **Lateral Movement:** Use **Pass the Hash** or compromised **MFA & 2FA** tokens to pivot to other systems within the **Perimeter**.

 - [ ] **Defense Disabling:** Actively terminate **Antimalware** or **Host Based Firewall** processes if privileges allow.
    

---

### **Phase 5: Counter-Forensics & Professionalism (The Cleanup)**

_Goal: Hide the tracks and adhere to engagement rules._

 - [ ] **Anti-Forensics:** Use secure deletion to scrub **RAM artifacts** and **Packet Captures** to frustrate the **Basics of Forensics** investigation.

 - [ ] **Log Manipulation:** Alter or clear **Event Logs** and **Syslogs** to blind **SIEM** and **SOAR** systems from correlating the attack.

 - [ ] **Reverse Engineering Resistance:** Strip binary symbols and use anti-debugging techniques to make **Basics of Reverse Engineering** difficult for the Blue Team.

 - [ ] **Rules of Engagement:** (For Red Teams) Ensure the malware's scope aligns with the **Penetration Testing Rules of Engagement**—do not destroy production data unless authorized.

---

## Part 8: Detection & Mitigation (Blue Team Perspective)

_Understand defensive detection to know what to evade._

### **Phase 1: Defensive Architecture**

- [ ] **Defense-In-Depth:** Layer **EDR, SIEM, CASB, firewall, WAF, IDS/IPS, DNS filtering** with **proper tuning** to reduce false positives and enable hunting.

- [ ] **Threat Hunting:** Proactively search for **suspicious patterns** (parent/child process anomalies, unsigned DLLs, scheduled task abuse, registry modifications) using **Sigma rules, YARA, KQL**.

- [ ] **Incident Response Plan:** Document **detection, containment, eradication, recovery, lessons learned** phases with **clear ownership and escalation paths**.

### **Phase 2: Offensive Indicators & TTPs**

- [ ] **IOC Identification:** Recognize **file hashes, domains, IPs, email patterns, behavioral signatures** that map to known attack frameworks (Cobalt Strike, Metasploit, custom).

- [ ] **MITRE ATT&CK Mapping:** Correlate **detected behaviors** to **tactics/techniques** to understand adversary intent and prioritize detection investment.

- [ ] **Artifact Analysis:** Understand forensic artifacts (prefetch, MFT, journal logs, browser history, registry hives, event logs) as **evidence of compromise**.

### **Phase 3: Evasion Detection & Hardening**

- [ ] **Living-off-the-Land Detection:** Monitor **native binary execution** (PowerShell, WMI, certutil, mshta, bitsadmin) with **process whitelisting, memory pattern analysis, and behavioral indicators**.

- [ ] **Obfuscation Analysis:** Detect **encoded payloads, packed executables, script obfuscation** via **entropy analysis, dynamic detonation, behavioral sandboxing**.

- [ ] **Anti-Forensics Detection:** Identify **log clearing, file timestomping, registry deletion, bash history removal** via **SIEM correlation and immutable audit logs**.

- [ ] **Command-Line Auditing:** Enable and monitor **PowerShell transcript logging, command-line audit logs (4688), script block logging** for obfuscated execution.

### **Phase 4: Detection Engineering & Response**

- [ ] **Alert Tuning:** Build **low false-positive alerts** for high-confidence indicators (e.g., AMSI evasion, direct syscalls, token theft patterns).

- [ ] **Playbook Development:** Create **runbooks** for common attack patterns (ransomware deployment, credential theft, lateral movement) with **clear triage and containment steps**.

- [ ] **Purple Teaming:** Partner with red teams to **validate detections, test response procedures, and measure MTTD (Mean Time to Detect) and MTTR (Mean Time to Respond)**.

---

## Part 9: Sniffing & Spoofing

### **Phase 1: The Environment & Fundamentals (The Setup)**

_Goal: Understand the battlefield. You cannot spoof what you cannot map._

 - [ ] **Protocol Hierarchy & Trust:** Differentiate between **MAC Addresses** (Layer 2 - Local Trust) and **IP Addresses** (Layer 3 - Routing). Spoofing relies on exploiting the trust mismatch between these layers.

 - [ ] **Secure vs. Insecure Protocols:** Identify targets using cleartext protocols like **HTTP, FTP, Telnet, DNS**. These are trivial to sniff. Encrypted protocols like **TLS/HTTPS** and **SSH** require advanced downgrade attacks or decryption to bypass.

 - [ ] **The Switch vs. Hub Reality:** Modern networks use switches which segment traffic by MAC. You cannot passively sniff; you must **ARP spoof, MAC flood**, or **VLAN hop** to bypass segmentation.

 - [ ] **Interface Configuration:** Configure NIC to **Promiscuous Mode** (tcpdump, Wireshark) to capture all traffic, not just destined to your MAC; practice with **monitor mode** on wireless cards.

 - [ ] **Handshake & Session Logic:** Study **TCP/TLS handshakes** (SYN/ACK, ClientHello/ServerHello) to identify session boundaries; understand **sequence numbers, window size, timestamps** for **replay and hijack** timing.
    

---

### **Phase 2: Sniffing & Passive Reconnaissance (The Ear)**

_Goal: Capture data without alerting the target. "Listen before act."_

 - [ ] **Passive Packet Capture:** Use **tcpdump/Wireshark** to capture broadcast/multicast traffic (ARP, DHCP, mDNS) to identify active hosts, gateways, and services without sending directed traffic.

 - [ ] **Wireless Interception:** Set wireless NIC to **monitor mode**; capture **WPA2/WPA3 4-way handshakes, PMKID** for offline cracking; identify **SSID, client MAC, AP MAC** patterns.

 - [ ] **Protocol Analysis:** Filter **pcap** by protocol (HTTP, FTP, SMTP, DNS); identify **cleartext credentials, API keys, session tokens**, and software **User-Agent/Server banners**.

 - [ ] **Stream Reassembly:** Use **tcpflow, Wireshark Follow TCP Stream** to reassemble files, images, emails, or form submissions from fragmented packets.
    

---

### **Phase 3: Spoofing & Active Deception (The Lie)**

_Goal: Inject false information into the network to redirect or manipulate traffic._

 - [ ] **ARP Spoofing:** Flood the network with **gratuitous ARP packets** linking your MAC to the **gateway IP**; forces the switch to route victim traffic through you; use **arpspoof, dsniff, bettercap**.

 - [ ] **DNS Spoofing:** Respond to **DNS queries faster than the legitimate server**; redirect victims to malicious login pages for **credential harvesting** or **malware distribution**.

 - [ ] **DHCP Starvation & Rogue DHCP:** Exhaust legitimate DHCP pools and serve your own **gateway/DNS** to all clients; enables **MITM and traffic redirection**.

 - [ ] **MAC Spoofing:** Change burned-in MAC to bypass **MAC filtering, NAC (Network Access Control), DHCP reservations**; use **macchanger** (Linux) or **SetMACAddress** (Windows).

 - [ ] **IP Spoofing:** Forge **source IP** in packet headers to **hide identity, impersonate trusted hosts**, or launch **reflection/amplification attacks** in DDoS.

 - [ ] **SSL Stripping & HTTP Downgrade:** Intercept **HTTPS traffic** and downgrade to **HTTP** by breaking the TLS handshake; use **sslstrip, mitmproxy** to expose encrypted traffic in cleartext.
    

---

### **Phase 4: Man-in-the-Middle & Exploitation (The Kill)**

_Goal: Intercept, modify, and relay traffic to extract or manipulate data._

 - [ ] **MITM Positioning:** Establish yourself between victim and gateway via **ARP spoofing, DNS redirection, rogue DHCP, or rogue AP**; use **ettercap, mitmproxy, Burp Suite** to intercept and modify traffic in real-time.

 - [ ] **Session Hijacking:** Extract **session cookies, JWT tokens, CSRF tokens** from sniffed **HTTP headers** and **POST bodies**; inject stolen tokens to impersonate user without password.

 - [ ] **Credential Sniffing:** Capture **cleartext logins** (FTP, Telnet, HTTP Basic Auth, SMTP); extract **form credentials** from unencrypted POST requests.

 - [ ] **Replay Attacks:** Capture valid **authentication tokens, API requests, or RF signals** and retransmit later to bypass time-based controls; works for **garage door openers, payment terminals, VoIP**.

 - [ ] **Rogue Access Point / Evil Twin:** Deploy **fake Wi-Fi AP** with legitimate SSID + stronger signal; force users to connect and route all traffic through your box for **MITM harvesting**.

 - [ ] **Traffic Injection & Modification:** Inject malicious **JavaScript, HTML, iframes** into unencrypted HTTP responses; modify **DNS responses** to redirect to attacker servers.
    

---

### **Phase 5: Defenses & Mitigation (The Shield)**

_Goal: Understand defensive controls to anticipate and evade them._

 - [ ] **Encryption & VPN:** Force all traffic through **TLS/HTTPS, IPSec VPN, or VPN tunneling**; renders sniffed payloads unreadable; watch for **HSTS, certificate pinning** as anti-bypass measures.

 - [ ] **Switch-Level Protection:** **Dynamic ARP Inspection (DAI)**, **DHCP Snooping**, **port security** reject malformed ARP/DHCP; **802.1X authentication** prevents rogue device connection.

 - [ ] **Network Segmentation:** **VLAN isolation, micro-segmentation, zero trust** limits sniffing scope per compromised segment; east-west traffic encryption adds extra layers.

 - [ ] **Detection Systems:** **IDS/IPS** flag high ARP packet volume, **MITM tools (ettercap signatures)**, SSL downgrade attempts; **Netflow/sFlow** detects unusual traffic patterns.

 - [ ] **User Awareness:** Train users to verify **SSL certificates**, recognize **phishing login pages**, and use **password managers** to avoid clipboard paste attacks.

## Part 10: Social Engineering

### **Stage 1: Intelligence & Reconnaissance (The Setup)**

_Goal: Know the target better than they know themselves._

- [ ] **Digital Recon:** Execute **OSINT** using **Google Dorks, LinkedIn scraping, GitHub dorking** to extract employee names, emails, roles, tech stacks, and company structure.
    
- [ ] **Physical Recon:** Perform **dumpster diving** to recover **org charts, vendor invoices, sticky notes** with passwords; observe **badge access patterns, delivery procedures**.
    
- [ ] **Domain & Infrastructure Prep:** Register **typo-squatting domains** (e.g., `companysupport.com`, `company-login.net`) that mimic target portals; prepare **phishing landing pages**.
    
- [ ] **Social Media Profiling:** Mine **LinkedIn, Twitter, GitHub, Glassdoor** for **personal details, relationships, job changes** to craft personalized lures.

### **Stage 2: The Digital Assault (Remote Vectors)**

_Goal: Compromise the target from a distance via electronic channels._

- [ ] **Mass Campaign:** Launch **broad phishing campaigns** with generic lures (password resets, package delivery) for large-scale **credential harvesting**.
    
- [ ] **Executive Targeting:** Execute **whaling attacks** against **C-suite/CFO** using deep **OSINT context** (recent news, personal interests, vendor relationships) to bypass skepticism.
    
- [ ] **Mobile Vector:** Deploy **SMS phishing (smishing)** with **MFA reset codes, delivery notifications, bank alerts**; use **VoIP/voice phishing (vishing)** to call employees directly.
    
- [ ] **Watering Hole:** Compromise **industry-specific forums, GitHub repos, or shared tools** to inject **malware/tracking code** that targets specific teams via **drive-by downloads**.

### **Stage 3: The Human Element (Direct Interaction)**

_Goal: Use psychology and social manipulation to bypass logic._

- [ ] **Voice Pretexting:** Call as **IT support, HR, vendor, auditor, law enforcement** using social engineering pretexts; use **authority, urgency, fear** to bypass critical thinking.
    
- [ ] **Authority & Compliance Trigger:** Leverage **IT/Security/Auditor/Legal persona** to demand compliance; abuse **helpfulness bias** to force password resets or system access.
    
- [ ] **Reciprocity & Obligation:** Provide small **favors (tech help, free tools)** to create sense of obligation; ask for credentials or access in return.

### **Stage 4: The Physical Breach (Boots on the Ground)**

_Goal: Gain physical access to networks and facilities._

- [ ] **Tailgating:** Follow **authorized employees** into secure zones using badges/access cards; use **coffee cup hold, uniform/vendor persona** to bypass visual checks.
    
- [ ] **Shoulder Surfing:** Observe **PIN entry, password typing, screen content** in public spaces (airports, coffee shops, open offices) to capture credentials.
    
- [ ] **Badge Cloning:** Capture **RFID badge data** using **Proxmark3, ACR122U** and clone to malicious card; bypass **magnetic stripe readers** via cloning.
    
- [ ] **Physical Device Placement:** Plant **USB drops, rogue access points, hardware keyloggers** in common areas for **auto-execution** when connected by unsuspecting users.

### **Stage 5: Defense & Awareness (The Shield)**

_Goal: Prevent the human hack through training and controls._

- [ ] **Authentication:** Enforce **MFA/2FA** (TOTP, hardware keys, push notifications) so password compromise alone doesn't grant access; watch for **MFA fatigue attacks**.
    
- [ ] **Verification Protocols:** Train staff to **challenge unknown callers** via **secondary channel callback**; never trust caller ID alone; verify requests through official channels.
    
- [ ] **Physical Security:** Enforce **no-tailgating policies, visitor escorts, badge display requirements, clean desk policies** to prevent **dumpster diving and shoulder surfing**.
    
- [ ] **Security Awareness:** Regular **phishing simulations, red team testing, security training** to build **skepticism and reporting culture**; reward **security-first behavior**.

## Part 11: Denial of Service

### **Stage 1: Objective & Strategy (The Planning)**

_Goal: Understand DoS/DDoS scope and firepower requirements._

- [ ] **Denial of Service (DoS):** Single attacker sends **crafted traffic** to overwhelm a target's **CPU, bandwidth, or connections**; from one IP; **relatively easy detection**.

- [ ] **Distributed Denial of Service (DDoS):** **Multiple sources** (botnet, amplification servers) send traffic **simultaneously**; harder to trace and block; **stronger firepower**.

- [ ] **Target Assessment:** Identify **critical services** (web, DNS, mail, VPN) and **upstream bottlenecks** (ISP bandwidth, DDoS mitigation capacity) to determine **attack viability**.

### **Stage 2: The Arsenal (Attack Methods)**

_Goal: Select the right DoS technique for target vulnerabilities._

- [ ] **Volumetric Attacks:** Consume **bandwidth** using **SYN floods, UDP floods, ICMP floods** to saturate network pipes; use **DNS amplification, NTP reflection** to multiply traffic (1 request → 1000× response).

- [ ] **Protocol Attacks:** Exploit **TCP/IP stack weaknesses** (malformed packets, fragment handling, connection states) using **Ping of Death, Teardrop, SYN floods** to crash systems or exhaust connection limits.

- [ ] **Application-Layer Attacks:** Target **specific services** with **HTTP floods (Slowloris), database queries (CPU spike), cached assets** to overwhelm **web servers, APIs, load balancers** at Layer 7.

- [ ] **IoT/Botnets:** Compromise **webcams, routers, smart devices** via **default creds, unpatched firmware** to join **Mirai, Dridex-style botnets** for DDoS-as-a-Service.

### **Stage 3: Infrastructure & Execution (The Assault)**

_Goal: Deploy and sustain the attack at scale._

- [ ] **Botnet Assembly:** Recruit **thousands of infected IoT/servers** or use **existing botnet services** (DDoS-as-a-Service, rent botnet time); establish **C&C control** via IRC/DNS/Peer-to-Peer.

- [ ] **Traffic Generation:** Use **tools like hping3, slowhttptest, LOIC, Colasoft PacketBuilder** to craft and blast custom packets; coordinate **multi-vector attacks** (volumetric + protocol + app-layer simultaneously).

- [ ] **Proxy/Spoofing:** Use **open reflectors/amplifiers** (DNS servers, NTP, SNMP) to amplify traffic; spoof **source IP addresses** to obscure attacker origin.

- [ ] **Duration & Monitoring:** Sustain attack for **hours/days** while monitoring **target availability, ISP response, filtering changes**; adjust payload/vector on-the-fly.

### **Stage 4: Defense & Mitigation (The Shield)**

_Goal: Detect, absorb, and neutralize DoS attacks._

- [ ] **Edge Defense:** Deploy **Cloudflare, Akamai, AWS Shield Standard** to absorb DDoS at **ISP/CDN level** before traffic reaches origin; filter **malformed packets, spoofed IPs** at network edge.

- [ ] **Rate Limiting & Throttling:** Implement **connection limits, request rate caps, CAPTCHAs, geo-blocking** to let legitimate users through while rejecting flood traffic.

- [ ] **Monitoring & Detection:** Deploy **NetFlow/sFlow analysis, IDS/IPS (Suricata, Zeek)** to detect **unusual traffic patterns, connection spikes, protocol anomalies**; alert on **RTO timeouts, CPU/bandwidth saturation**.

- [ ] **Architectural Resilience:** Use **anycast DNS, geographically distributed servers, auto-scaling, load balancing** to spread load; oversizing infrastructure to **absorb baseline attacks**; prepare **incident response playbooks**.

- [ ] **ISP/Carrier Coordination:** Work with **ISP's DDoS mitigation services** to scrub traffic upstream; establish **BGP blackholing** to discard attack traffic at border; maintain **redundant ISPs/circuits**.

## Part 12 : Session Hijacking
#### **Stage 1: Reconnaissance & Vulnerability Analysis**

_Goal: Find a target and identify its weaknesses._

- **[ ] Target Identification:** Use **Reconnaissance** and **OSINT** to identify target web applications.
    
- **[ ] Protocol Analysis:** Check if the application uses **Unsecure Protocols** (HTTP) for any part of the session, making it vulnerable to sniffing.
    
- **[ ] Vulnerability Scanning:** Test for **Web Based Attacks and OWASP10** vulnerabilities, specifically looking for **XSS**.
    

#### **Stage 2: Stealing the Session ID (The Attack Vectors)**

_Goal: Execute the attack to acquire the victim's session token._

- **[ ] Network Sniffing:** If HTTP is in use, launch **Sniffing** with **wireshark** on the local network or from a **Rogue Access Point** to capture the session cookie.
    
- **[ ] Client-Side Injection:** Craft and deliver an **XSS** payload (via **Phishing** or a stored vulnerability) to steal the `document.cookie` from the user's browser.
    
- **[ ] Man-in-the-Middle:** Execute a **MITM** attack, potentially using **Spoofing**, to intercept communication and steal the token, even if HTTPS is attempted (via SSL stripping).
    

#### **Stage 3: Execution & Impersonation**

_Goal: Use the stolen token to access the user's account._

- **[ ] Token Injection & Hijack:** Inject the stolen session ID into your browser to achieve **Impersonation** of the victim, bypassing the **Authentication** step.
    

#### **Stage 4: Defense & Mitigation (The Shield)**

_Goal: Prevent the attack from succeeding._

- **[ ] Enforce Encryption:** Mandate the use of **Secure Protocols** (**SSL vs TLS**) for all web traffic to prevent sniffing.
    
- **[ ] Secure Cookie Attributes:** Implement `HttpOnly` and `Secure` flags on cookies to mitigate **XSS** theft and network sniffing.
    
- **[ ] Multi-Factor Authentication:** Deploy **MFA & 2FA** to ensure that even a stolen session token is not enough to perform sensitive actions.
    
- **[ ] Network Monitoring:** Use **IDS and IPS** to detect signs of **Sniffing**, **Spoofing**, and **MITM** attacks on the network.

## Part 13 : Web Application Hacking 
#### **Stage 1: Reconnaissance & Mapping**

_Goal: Understand the target application's structure and technologies._

- **[ ] OSINT & Discovery:** Perform **Reconnaissance** using **Basics of Threat Intel, OSINT** to find subdomains and developer information.
    
- **[ ] Service Enumeration:** Use tools like `nmap` to identify web servers and other services running on the target IP.
    
- **[ ] Technology Fingerprinting:** Analyze HTTP headers and responses using `curl` to identify the backend technologies.
    

#### **Stage 2: Vulnerability Analysis & Probing**

_Goal: Find potential entry points and weaknesses._

- **[ ] Input Validation Testing:** Test every field for **Injection** vulnerabilities like **SQL Injection** and Command Injection.
    
- **[ ] Path Manipulation:** Probe for **Directory Traversal** flaws to access sensitive system files (e.g., `/etc/passwd`).
    
- **[ ] Logic Testing:** Analyze **Authentication vs Authorization** mechanisms to find broken access controls that allow privilege escalation.
    
- **[ ] Protocol Analysis:** Check for the use of **Unsecure Protocols** and assess the strength of **SSL vs TLS** configurations.
    

#### **Stage 3: Exploitation (The OWASP Focus)**

_Goal: Prove the vulnerability and gain access._

- **[ ] Database Compromise:** Execute **SQL Injection** to extract data, bypass authentication, or gain shell access.
    
- **[ ] Client-Side Compromise:** Deliver **XSS** payloads to steal session cookies or execute actions as another user.
    
- **[ ] Request Forgery:** Construct **CSRF** attacks to trick a victim's browser into performing unwanted actions.
    

#### **Stage 4: Defense & Mitigation (The Shield)**

_Goal: Prevent and detect these attacks._

- **[ ] WAF Deployment:** Implement a **Firewall & Nextgen Firewall** configured as a Web Application Firewall to block common attack patterns.
    
- **[ ] Secure Coding:** Validate all inputs to prevent injection attacks and encode outputs to prevent **XSS**.
    
- **[ ] Strong Authentication:** Require **MFA & 2FA** for all user accounts to mitigate the impact of credential theft.
    
- **[ ] Continuous Monitoring:** Use **IDS and IPS** and review web server logs to detect ongoing attack attempts.
## Part 14 : Web Server Hacking 
#### **Stage 1: Target Acquisition & Reconnaissance**

_Goal: Identify the target server and gather open-source intelligence._

- **[ ] OSINT Gathering:** Conduct **Reconnaissance** using **Basics of Threat Intel, OSINT** and tools like **WHOIS** to identify IP ranges and domain information.
    
- **[ ] Network Mapping:** Determine the server's network position, noting if it's in the **Perimeter vs DMZ vs Segmentation** zones.
    

#### **Stage 2: Scanning & Service Enumeration**

_Goal: Map out the server's attack surface by finding open ports and running services._

- **[ ] Port Scanning:** Use **nmap** to discover open ports and identify services (web server, SSH, database, etc.).
    
- **[ ] Banner Grabbing:** Use **curl** or netcat to grab service banners and identify software versions.
    
- **[ ] Protocol Audit:** Check for **Unsecure Protocols** and analyze the **SSL vs TLS** configuration for weak ciphers or outdated protocols.
    

#### **Stage 3: Vulnerability Assessment & Exploitation**

_Goal: Find and exploit flaws to gain initial access._

- **[ ] Patch Audit:** Check for missing **Patching** and a lack of **Operating System Hardening** on the identified services and OS.
    
- **[ ] Injection Attacks:** Attempt **SQL Injection** against web applications to compromise the underlying database server.
    
- **[ ] File System Attacks:** Test for **Directory Traversal** vulnerabilities to read sensitive files like `/etc/passwd`.
    
- **[ ] Service Exploitation:** Look for known **Buffer Overflow** exploits for the specific versions of services running on the server.
    
- **[ ] Credential Attacks:** Launch **Brute Force vs Password Spray** attacks against exposed services like SSH, FTP, or administration panels.
    

#### **Stage 4: Post-Exploitation & Persistence**

_Goal: Escalate privileges and maintain control over the server._

- **[ ] Privilege Escalation:** After gaining a low-privilege shell, use local exploit scripts or misconfigurations to achieve **Privilege Escalation** to root or SYSTEM.
    
- **[ ] Living off the Land:** Utilize **LOLBAS** (for Windows) or **GTFOBINS** (for Linux) to execute arbitrary commands and maintain persistence using built-in tools.
    
- **[ ] Covering Tracks:** Locate and modify **Event Logs** (Windows) or **syslogs** (Linux) to remove evidence of your intrusion.
## Part 15: IDS, FIrewalls and honeypots
#### **Stage 1: Foundational Strategy & Networking**

_Goal: Establish the theoretical base and network understanding._

- **[ ] Defense in Depth:** Adopt the `Understand Concept of Defense in Depth` philosophy, using multiple layers of security controls.
    
- **[ ] Network Segmentation:** Design the network with clear boundaries, utilizing `Perimeter vs DMZ vs Segmentation` to limit blast radius.
    
- **[ ] Protocol Knowledge:** Master networking fundamentals, including `Understand Handshakes` and identifying `Secure vs Unsecure Protocols`.
    

#### **Stage 2: Deploying Firewalls (The Shield)**

_Goal: Implement access control and segmentation._

- **[ ] Perimeter Defense:** Deploy a `Firewall & Nextgen Firewall` at the network edge, configuring `ACLs` for ingress and egress filtering.
    
- **[ ] Endpoint Protection:** Enable and configure `Host Based Firewall` on servers and workstations for granular `Port Blocking`.
    
- **[ ] Log Analysis:** Set up centralized collection for `Firewall Logs` to monitor policy violations and traffic patterns.
    

#### **Stage 3: Implementing IDS/IPS (The Watchers)**

_Goal: Detect and stop malicious traffic that bypasses firewalls._

- **[ ] Strategic Deployment:** Place `NIDS` sensors at critical network choke points to monitor east-west and north-south traffic.
    
- **[ ] Host Monitoring:** Install `HIPS` agents on critical servers to detect suspicious process execution and file changes.
    
- **[ ] Rule Tuning:** Continuously tune signature and anomaly rules to minimize `False Positives` while ensuring no `False Negatives` occur.
    
- **[ ] SIEM Integration:** Feed IDS/IPS alerts into a `SIEM` for correlation with other security events.
    

#### **Stage 4: Utilizing Deception (The Traps)**

_Goal: Gather threat intelligence and waste attacker time._

- **[ ] Honeypot Deployment:** Deploy `Honeypots` (both low and high interaction) in the DMZ and internal network to attract attackers.
    
- **[ ] Traffic Redirection:** Use `Sinkholes` to capture traffic destined for known malicious domains or IPs.
    
- **[ ] Intelligence Gathering:** Analyze logs and activity from deception tools to inform `Basics and Concepts of Threat Hunting`.
    

#### **Stage 5: Operations & Improvement**

_Goal: Integrate into daily security operations._

- **[ ] Incident Response:** Utilize these tools during the `Incident Response Process` for rapid `Identification` of threats and `Containment` of affected systems.
    
- **[ ] Zero Trust Alignment:** Ensure firewall and IPS policies align with `Core Concepts of Zero Trust`, verifying every connection attempt.

## Part 15 : Wireless Penstesting 
#### **Stage 1: RF Reconnaissance & Setup**

_Goal: Map the airspace and identify targets._

- **[ ] Monitor Mode:** Configure hardware to capture raw 802.11 frames.
    
- **[ ] Protocol Audit:** Identify the target's encryption: **WPA vs WPA2 vs WPA3 vs WEP**. Note that WEP is obsolete but trivial to crack; WPA3 is resistant to dictionary attacks.
    
- **[ ] WPS Check:** Scan for **WPS** enabled APs. If active, this is the primary high-value target for PIN brute-forcing (Pixie Dust).
    

#### **Stage 2: Access Point Assault (The Breaching of Keys)**

_Goal: Obtain the credentials to join the network._

- **[ ] Handshake Capture:** Execute a **Deauth Attack** against a connected client to force a reconnection and capture the 4-way handshake.
    
- **[ ] Replay Attacks:** (For legacy/WEP) Use **Replay Attack** techniques to generate traffic and accelerate IV collection for cracking.
    
- **[ ] Offline Cracking:** Run the captured handshake against wordlists using Hashcat/Aircrack-ng.
    

#### **Stage 3: Enterprise & Client Attacks (The Man-in-the-Middle)**

_Goal: Steal individual user identities or hijack connections._

- **[ ] Evil Twin Deployment:** Launch an **Evil Twin** attack to impersonate the target SSID. Use a captive portal to harvest credentials.
    
- **[ ] Enterprise Stripping:** Target **EAP vs PEAP** configurations. Downgrade encryption or crack the challenge-response hashes (MSCHAPv2) captured from the Evil Twin.
    
- **[ ] Rogue AP:** Plant a **Rogue Access Point** physically in the facility to create an unauthorized backdoor into the LAN.
    

#### **Stage 4: Defense & Hardening (The Shield)**

_Goal: Secure the airwaves._

- **[ ] Protocol Hardening:** Migrate all APs to **WPA3** (SAE) to mitigate handshake cracking and disable **WPS** immediately.
    
- **[ ] Certificate Enforcement:** For **EAP vs PEAP** networks, enforce server certificate validation on all client devices to neutralize **Evil Twin** attacks.
    
- **[ ] Wireless IPS:** Deploy **IDS and IPS** sensors tuned for RF to detect **Deauth Attack** signatures and triangular **Rogue Access Points**.

##  Part 16 : Mobile platform pentesting
#### **Stage 1: Lab Setup & Reconnaissance**

_Goal: Prepare the environment and understand the target._

- **[ ] Environment Prep:** Configure a Rooted (Android) or Jailbroken (iOS) device to bypass **Operating System Hardening**.
    
- **[ ] Binary Acquisition:** Extract the APK or IPA and perform **Basics of Reverse Engineering** using tools like `jadx` or `Ghidra`.
    
- **[ ] Reconnaissance:** Map the app's attack surface (activities, services, URL schemes) and identify backend endpoints.
    

#### **Stage 2: Static Analysis (Code Review)**

_Goal: Find hardcoded secrets and configuration flaws._

- **[ ] Manifest/Plist Audit:** Check for exported components or insecure permissions that violate **Zero Trust** principles.
    
- **[ ] Secret Hunting:** Search decompiled code for **Key Exchange** material, API tokens, or hardcoded credentials.
    
- **[ ] Crypto Audit:** Verify if the app uses weak **Hashing** or **Salting** algorithms for local storage.
    

#### **Stage 3: Dynamic Analysis (Runtime Manipulation)**

_Goal: Bypass client-side controls._

- **[ ] Security Control Bypass:** Use Frida to bypass Root Detection and SSL Pinning (breaking the **SSL vs TLS** trust chain).
    
- **[ ] Logic Manipulation:** Hook functions to bypass **Authentication vs Authorization** checks (e.g., bypassing a PIN screen).
    
- **[ ] Memory Dumping:** Analyze device memory for sensitive data that should have been cleared (violating **Confidentiality** in the **CIA Triad**).
    

#### **Stage 4: Network & API Attacks**

_Goal: Compromise the backend server._

- **[ ] Traffic Interception:** Proxy traffic to analyze **Secure vs Unsecure Protocols** and payload structures.
    
- **[ ] API Vulnerability Testing:** Test backend endpoints for **OWASP10** vulnerabilities like **SQL Injection**, **IDOR**, and **Broken Access Control**.
    
- **[ ] Session Management:** Test for weak **Session ID** generation or lack of **MFA & 2FA** on the mobile endpoints.
    

#### **Stage 5: Local Data Storage**

_Goal: Steal data at rest._

- **[ ] Insecure Storage Check:** Inspect local files (SQLite, XML, Plist) for unencrypted PII, violating **Basics of Cryptography** best practices.
    
- **[ ] Log Analysis:** Check system **logs** (Logcat/Syslog) for sensitive data leakage during app usage.
## Part 17 : Cryptography 
#### **Stage 1: Core Concepts & Algorithms**

_Goal: Understand the mathematical tools available._

- **[ ] CIA Alignment:** Map your crypto goals to the **Understand CIA Triad** (Confidentiality = Encryption, Integrity = Hashing).
    
- **[ ] Asymmetric Mastery:** Define the roles of **Private vs Public Keys**: Public to Encrypt/Verify, Private to Decrypt/Sign.
    
- **[ ] Integrity Checks:** Implement **Hashing** (SHA-256) to verify data integrity and detect **False Positives/Negatives** in file transfers.
    

#### **Stage 2: Secure Communication (Data in Transit)**

_Goal: Secure the pipe between two points._

- **[ ] Protocol Hardening:** Enforce **Secure Protocols** by disabling **SSL** (deprecated) and enforcing **TLS** 1.2/1.3.
    
- **[ ] Secure Transfer:** Replace cleartext protocols with encrypted alternatives: **FTP vs SFTP** (SSH-based) or **IPSEC** for VPNs.
    
- **[ ] Handshake Analysis:** Analyze the **Key Exchange** (Diffie-Hellman) within the **Understand Handshakes** process to ensure Forward Secrecy.
    

#### **Stage 3: Identity & Trust (PKI)**

_Goal: Prove that you are who you say you are._

- **[ ] Infrastructure:** Deploy **PKI** to manage digital certificates, ensuring the validity of public keys.
    
- **[ ] Email Security:** Implement **S/MIME** to sign and encrypt corporate email, preventing **Phishing** and spoofing.
    

#### **Stage 4: Data at Rest & Obfuscation**

_Goal: Secure stored data and understand evasion._

- **[ ] Password Storage:** Never store plain passwords. Use **Hashing** combined with **Salting** to defeat rainbow table attacks.
    
- **[ ] Code Analysis:** Recognize **Obfuscation** in malware analysis (Reverse Engineering) as a method to hide logic, distinct from actual encryption.

## Part 18: Cloud Computing 
#### **Stage 1: Architecture & Governance**

_Goal: Define the battlefield and the rules of engagement._

- **[ ] Model Selection:** Select the correct `Cloud Models` (`Public`, `Private`, `Hybrid`) based on data sensitivity.
    
- **[ ] Responsibility Mapping:** Apply the **Shared Responsibility Model** based on the service type (`IaaS`, `PaaS`, `SaaS`) to identify what you must secure vs. the provider.
    
- **[ ] Environment Setup:** Initialize the tenant in a `Common Cloud Environment` (`AWS`, `GCP`, or `Azure`) with a secure root account setup.
    

#### **Stage 2: Storage & Data Security**

_Goal: Lock down the data assets._

- **[ ] Object Storage Security:** Audit `S3` buckets and `Common Cloud Storage` (Drive, Box) for public access and enforce encryption.
    
- **[ ] Access Control:** Implement strict IAM policies ensuring only authorized identities can access storage blobs.
    

#### **Stage 3: Modern Infrastructure & Deployment**

_Goal: Secure the compute and the pipeline._

- **[ ] Code-Defined Security:** Use `Infrastructure as Code` (IaC) to template firewalls and permissions, preventing human configuration errors.
    
- **[ ] Serverless Hardening:** Secure `Serverless` functions by minimizing privileges and auditing dependencies for vulnerabilities.
    
- **[ ] Pipeline Security:** Audit the `general flow of deploying in the cloud` to ensure secrets (API keys) are not hardcoded in the deployment scripts.
    

#### **Stage 4: Automation & Scripting (The Glue)**

_Goal: Automate defense and auditing._

- **[ ] Cloud Automation:** Use `Python` (Boto3) or `Go` to write custom scripts that audit security groups and IAM roles automatically.
    
- **[ ] Admin Scripting:** Master `Bash` (Linux) and `Power Shell` (Windows) to manage instances and automate patch management via CLI.

## Part 19: Digital Forensics
#### **Stage 1: Preparation & First Response**

_Goal: Secure the scene without corrupting evidence._

- **[ ] Incident Identification:** Trigger the `Incident Response Process` upon `Identification` of a breach.
    
- **[ ] Volatile Collection:** Capture RAM immediately using `memdump` before the system is powered off or rebooted.
    
- **[ ] Static Acquisition:** Create a forensic image of hard drives using `FTK Imager` or `dd`, ensuring a write-blocker is used.
    

#### **Stage 2: Evidence Analysis (The Deep Dive)**

_Goal: Find the needle in the haystack._

- **[ ] Disk Analysis:** Load the evidence into `autopsy` to recover deleted files, analyze web history, and search for keywords.
    
- **[ ] Binary Inspection:** Use `winhex` to manually inspect file headers (signatures) to identify files with changed extensions (e.g., an EXE renamed to JPG).
    
- **[ ] Log Review:** Correlate actions by analyzing `Event Logs` (Login times, Service installs) and `syslogs`.
    

#### **Stage 3: Network Forensics**

_Goal: Trace the attacker's path._

- **[ ] Traffic Reconstruction:** Open `Packet Captures` in `wireshark` to find C2 communication, data exfiltration, or cleartext passwords.
    
- **[ ] Flow Analysis:** If full packets are missing, use `netflow` logs to identify connections to malicious IPs.
    

#### **Stage 4: Advanced Analysis & Reporting**

_Goal: Understand the "How" and tell the story._

- **[ ] Malware Reversing:** If a suspicious binary is found, use `Basics of Reverse Engineering` to determine its function and indicators of compromise (IOCs).
    
- **[ ] Anti-Forensics Check:** Look for signs of `Obfuscation` or log clearing that indicate a sophisticated attacker.
    
- **[ ] Final Report:** Document findings for `Legal`, `HR`, and `Management` stakeholders, translating technical artifacts into business risk.
## Part 20 : Bug Bounty and Pentration 
#### **Stage 1: Preparation & Scoping**

_Goal: Stay legal and define the target._

- **[ ] Legal Check:** Read and sign the `Penetration Testing Rules of Engagement` or the Bug Bounty Policy (Safe Harbor).
    
- **[ ] Scope Validation:** Confirm IP ranges and domains. Ensure you are not attacking "Out of Scope" assets.
    
- **[ ] Framework Selection:** Decide if you are testing against `NIST`, `ISO`, or `OWASP10` standards.
    

#### **Stage 2: Reconnaissance (The Wide Net)**

_Goal: Find what others missed._

- **[ ] Subdomain Enumeration:** Use **OSINT** tools to find `dev`, `stage`, or `test` subdomains.
    
- **[ ] Port Scanning:** Run `nmap` to identify non-standard ports (e.g., 8080, 8443) and running services.
    
- **[ ] Tech Stack Analysis:** Use `curl` or browser extensions to identify the server, framework (React, Angular), and backend (PHP, Python).
    

#### **Stage 3: Vulnerability Assessment (The Deep Dive)**

_Goal: Find the flaw._

- **[ ] Input Fuzzing:** Test all input fields for `SQL Injection`, `XSS`, and `Buffer Overflow`.
    
- **[ ] Access Control:** Test for `IDOR` (Insecure Direct Object Reference) and verify `Authentication vs Authorization` logic.
    
- **[ ] Configuration Check:** Look for `Directory Traversal`, exposed `.git` folders, or default credentials (`admin/admin`).
    

#### **Stage 4: Exploitation & Validation**

_Goal: Prove the risk without breaking the system._

- **[ ] PoC Development:** Create a non-destructive Proof of Concept. (e.g., `alert(1)` for XSS, `whoami` for RCE).
    
- **[ ] False Positive Check:** Verify the finding is a `True Positive` before reporting.
    
- **[ ] Lateral Movement:** (Pentest only) Attempt `Privilege Escalation` or `Pass the Hash` if internal access is achieved.
    

#### **Stage 5: Reporting & Triage**

_Goal: Get paid and get it fixed._

- **[ ] Impact Statement:** clearly explain the business risk to `Management` (e.g., "This allows full database theft").
    
- **[ ] Remediation:** Provide specific technical advice (e.g., "Implement Prepared Statements" or "Sanitize Input") for the `Stakeholders`.
## Part Extra: Red Team Operations & Tradecraft

### Strategy & Core Operations

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
