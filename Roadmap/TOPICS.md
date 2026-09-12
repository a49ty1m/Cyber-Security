H A R D W A R E
CPU Architecture x86 / x64 ARM / ARM64 CPU Registers Instruction Sets RAM
Cache Storage HDD / SSD / NVMe BIOS UEFI TPM Secure Boot DMA I/O
PCIe USB Firmware Embedded Controllers
C O M P U T E R A R C H I T E C T U R E
Memory Addressing Virtual Memory Physical Memory Stack Heap Pointers
Processes Threads Context Switching Interrupts System Calls Privilege Rings
User Mode Kernel Mode IPC

NETWORKING: SEE THE INVISIBLE
A serious hacker must be able to look at network traffic and mentally reconstruct what is happening.
C O R E
Ethernet MAC ARP IPv4 IPv6 ICMP TCP UDP QUIC Ports Sockets
Routing Switching VLAN NAT PAT Subnetting CIDR MTU Fragmentation
P R O T O C O L S
DNS DHCP HTTP HTTPS TLS SSH FTP SFTP SMTP IMAP POP3 LDAP
SMB NFS SNMP RDP WinRM Kerberos NTLM SIP MQTT WebSocket gRPC
I N F R A S T R U C T U R E
Firewalls WAF IDS IPS Load Balancers Reverse Proxies Forward Proxies
VPN CDN DNS Providers API Gateways Network Segmentation Zero Trust
Service Mesh
P A C K E T - L E V E L S K I L L S
Packet Capture Packet Reconstruction TCP Stream Analysis DNS Analysis
TLS Analysis Protocol Fingerprinting Traffic Anomaly Detection Network Forensics
T O O L S
Wireshark tcpdump Nmap Masscan Netcat Socat Nmap Scripting Engine


LINUX: OWN THE OPERATING SYSTEM
L I N U X I N T E R N A L S
Kernel Processes Threads Syscalls Signals File Descriptors Sockets
Pipes IPC /proc /sys /dev /tmp /var /etc
S E C U R I T Y M O D E L
Users Groups Permissions ACL Capabilities SUID SGID sudo Namespaces
cgroups SELinux AppArmor
S E R V I C E S
systemd Cron SSH Services Daemons Startup Mechanisms
A D V A N C E D
Linux Privilege Escalation Kernel Security Kernel Modules Containers Namespaces
Container Escape Concepts Linux Forensics Linux Persistence Analysis
T O O L S
Bash strace ltrace gdb lsof ss ps top tmux

WINDOWS: UNDERSTAND THE ENTERPRISE MACHINE
W I N D O W S A R C H I T E C T U R E
Win32 Windows NT Processes Threads DLLs Handles Tokens Services
Registry NTFS ACLs Named Pipes WMI COM RPC
A U T H E N T I C A T I O N
NTLM Kerberos Windows Hello Credential Providers LSASS SAM LSA DPAPI
S E C U R I T Y
UAC Windows Defender Windows Firewall AppLocker WDAC AMSI ETW
Event Logging Security Policies
P O W E R S H E L L
PowerShell PowerShell Remoting Windows Automation Security Automation
PowerShell Logging
A D V A N C E D
Windows Internals Windows Privilege Escalation Token Security Service Security
DLL Search Order Scheduled Tasks WMI Security Windows Persistence Analysis
Windows Memory Forensics

ACTIVE DIRECTORY: THE ENTERPRISE BATTLEFIELD
If you want to operate against real enterprise environments, AD is not optional.
A R C H I T E C T U R E
Domain Forest Tree Domain Controller OU Users Groups GPO LDAP
DNS Trusts
A U T H E N T I C A T I O N
Kerberos NTLM Tickets SPNs Service Accounts Managed Service Accounts
A T T A C K S U R F A C E
Identity ACLs Delegation Group Membership GPO AD CS Certificate Templates
Trust Relationships Service Accounts
O F F E N S I V E S E C U R I T Y
Enumeration Credential Exposure Kerberos Abuse NTLM Abuse Delegation Abuse
ACL Abuse AD CS Abuse Privilege Escalation Lateral Movement Persistence
Domain-Level Attack Paths
D E F E N S I V E U N D E R S T A N D I N G
Identity Detection Kerberos Monitoring LDAP Monitoring Windows Event Analysis
Attack Path Analysis AD Hardening
T O O L S
BloodHound Impacket NetExec Rubeus Mimikatz Certipy PowerView

PROGRAMMING: STOP BEING TOOL-DEPENDENT
The elite operator writes.
P Y T H O N
Automation Networking HTTP APIs Sockets Async Multithreading Parsing
Regex Exploit Research Security Tool Development Data Processing
B A S H
Automation Recon System Operations Pipeline Construction
P O W E R S H E L L
Windows Automation AD Automation Security Operations Administration
J A V A S C R I P T
Browser Internals DOM Events Fetch XHR WebSockets Node.js
Client-Side Security
C / C + +
Memory Pointers Structures Heap Stack Memory Management Native APIs
A D D I T I O N A L
Go Rust Java PHP SQL Assembly


WEB: THE MODERN APPLICATION ATTACK SURFACE
Do not stop at the OWASP Top 10.
W E B F U N D A M E N T A L S
HTTP HTTPS Requests Responses Headers Cookies Sessions Caching
Browser Security Same-Origin Policy CORS CSP WebSockets Webhooks
C O R E V U L N E R A B I L I T I E S
Broken Access Control Authentication Failures Injection SQL Injection
NoSQL Injection XSS CSRF SSRF XXE SSTI IDOR / BOLA BFLA
Path Traversal Command Injection File Upload Open Redirect Prototype Pollution
Deserialization Race Conditions Business Logic Bugs
M O D E R N W E B
HTTP Request Smuggling Web Cache Poisoning Web Cache Deception Host Header Attacks
Parser Confusion Request Splitting Client-Side Desync Browser Security
Service Workers WebAssembly WebRTC GraphQL gRPC Serverless Microservices
A R C H I T E C T U R E
Reverse Proxy CDN WAF API Gateway Load Balancer Microservice Communication
Internal APIs Service-to-Service Authentication

API SECURITY
Modern applications are API ecosystems.
R E S T
API Discovery Authentication Authorization Object-Level Authorization
Function-Level Authorization Rate Limits Pagination Filtering Mass Assignment
Versioning Error Handling
G R A P H Q L
Schema Queries Mutations Introspection Authorization Resolver Security
Complexity Batching
O T H E R
SOAP gRPC WebSockets Webhooks
I D E N T I T Y
API Keys OAuth OAuth 2.0 OpenID Connect JWT Access Tokens Refresh Tokens
SAML SSO


AUTHENTICATION & IDENTITY
Think beyond "login."
A U T H E N T I C A T I O N
Password Authentication MFA 2FA Passkeys Passwordless Biometrics
Device Authentication Session Management
I D E N T I T Y
OAuth OIDC SAML LDAP Kerberos Active Directory Entra ID
Identity Providers Federation
S E C U R I T Y
Account Recovery Session Fixation Session Hijacking Token Security
Authorization RBAC ABAC Privileged Access Identity Governance

JWT & TOKEN SECURITY
JWT Structure JWS JWE Signing Verification Algorithm Selection
Key Management Claims Expiration Audience Issuer Token Rotation
Refresh Tokens Token Revocation Authorization Boundaries

DATABASE SECURITY
S Q L
MySQL PostgreSQL MSSQL Oracle SQLite
N O S Q L
MongoDB Redis Elasticsearch
S E C U R I T Y
Injection Authentication Authorization Privilege Separation Secrets
Encryption Data Exposure Backup Security Logging Database Auditing


CRYPTOGRAPHY: KNOW WHY SECURITY WORKS
Encoding Hashing Encryption Symmetric Cryptography AES ChaCha20 RSA
ECC Diffie-Hellman Digital Signatures HMAC PKI Certificates TLS
Randomness Entropy Key Management Password Hashing bcrypt scrypt Argon2
Cryptographic Failures

RECON: FIND WHAT OTHERS DON'T SEE
I N F R A S T R U C T U R E R E C O N
Domains Subdomains DNS ASN IP Ranges Cloud Assets Certificates
Technology Stack Exposed Services Internet-Facing Infrastructure
A P P L I C A T I O N R E C O N
Endpoints Parameters APIs JavaScript Files Hidden Routes
Authentication Flows Third-Party Integrations Mobile Backends
O S I N T
Search Engines Public Documents Metadata Username Intelligence
Domain Intelligence Infrastructure Intelligence Social Intelligence
Threat Intelligence Dark Web Intelligence
T O O L S
Amass Subfinder Assetfinder httpx Naabu Nmap Nuclei Shodan Censys
Maltego SpiderFoot



VULNERABILITY RESEARCH
This is where the elite level begins.
Attack Surface Research Bug Discovery Root Cause Analysis Variant Analysis
Patch Diffing Fuzzing Protocol Research Parser Analysis Memory Corruption
Logic Bugs Race Conditions Authentication Research Authorization Research
Supply-Chain Research CVE Analysis CWE CVSS Exploitability Analysis
Responsible Disclosure


FUZZING
Black-Box Fuzzing White-Box Fuzzing Grey-Box Fuzzing Mutation-Based Fuzzing
Generation-Based Fuzzing Coverage-Guided Fuzzing Protocol Fuzzing
File Format Fuzzing API Fuzzing Web Fuzzing Binary Fuzzing Crash Triage
Corpus Management Sanitizers


REVERSE ENGINEERING
B I N A R Y F O R M A T S
PE ELF Mach-O DLL Shared Libraries
A N A L Y S I S
Static Analysis Dynamic Analysis Disassembly Decompilation Debugging
Control Flow Data Flow API Analysis Strings Imports Exports
A R C H I T E C T U R E
x86 x64 ARM ARM64
A D V A N C E D
Packing Obfuscation Anti-Debugging Anti-VM Control Flow Obfuscation
Binary Patching Hooking Runtime Analysis
T O O L S
Ghidra IDA Binary Ninja radare2 x64dbg WinDbg GDB


EXPLOIT DEVELOPMENT
M E M O R Y
Stack Heap Pointers Memory Corruption Information Disclosure
V U L N E R A B I L I T I E S
Buffer Overflow Heap Corruption Use-After-Free Double Free Integer Overflow
Format String Type Confusion Race Conditions
M I T I G A T I O N S
ASLR DEP / NX Stack Canaries PIE RELRO CFG CFI Sandboxing
A D V A N C E D
ROP JOP Memory Leaks Exploit Reliability Browser Exploitation Concepts
Kernel Exploitation Concepts


MALWARE
F A M I L I E S
Virus Worm Trojan RAT Stealer Loader Botnet Ransomware Rootkit
Spyware Infostealer
A N A L Y S I S
Static Analysis Dynamic Analysis Behavioral Analysis Configuration Extraction
Persistence C2 IOC Extraction Sandbox Analysis Memory Analysis
Network Analysis
D E T E C T I O N
YARA Sigma Behavioral Detection IOC IOA TTP Mapping


COMMAND & CONTROL
Understand how adversaries maintain communication.
C2 Architecture HTTP/S DNS WebSocket Custom Protocols Encrypted Channels
Beaconing Redirectors Infrastructure Domain Management Traffic Analysis
C2 Detection
F R A M E W O R K S / R E S E A R C H P L A T F O R M S
Sliver Mythic Cobalt Strike Metasploit Havoc Empire


RED TEAM OPERATIONS
A T T A C K L I F E C Y C L E
Reconnaissance Initial Access Execution Persistence Privilege Escalation
Defense Evasion Credential Access Discovery Lateral Movement Collection
Command & Control Exfiltration Impact
A D V A N C E D
Attack Path Development Adversary Emulation Identity Attack Paths
Cloud Attack Paths Hybrid Environment Attacks Detection Validation Purple Teaming
OPSEC Campaign Planning
F R A M E W O R K S
MITRE ATT&CK Cyber Kill Chain Diamond Model Atomic Red Team Caldera


PRIVILEGE ESCALATION
L I N U X
SUID SGID sudo Capabilities Cron Services PATH Permissions
Credentials Containers Kernel
W I N D O W S
Services Registry Tokens UAC Scheduled Tasks DLL Search Order WMI
Named Pipes Permissions Credentials Kernel


LATERAL MOVEMENT
SMB RDP SSH WinRM WMI RPC Remote Services Credential Reuse
Pass-the-Hash Pass-the-Ticket Overpass-the-Hash Kerberos Abuse
Remote Administration


CREDENTIAL ATTACKS & SECRETS
Password Security Password Policies Brute Force Concepts Password Spraying
Credential Stuffing Hash Analysis NTLM Kerberos Credential Stores
Browser Credentials SSH Keys API Keys Cloud Credentials Secrets Management
T O O L S
Hashcat John the Ripper Rubeus Mimikatz Secretsdump


WIRELESS
W I - F I
802.11 WEP WPA WPA2 WPA3 Enterprise Wi-Fi RADIUS Authentication
Association Handshake Analysis PMKID Rogue AP Concepts Wireless Recon
Wireless Monitoring
O T H E R
Bluetooth BLE RFID NFC IoT Wireless
T O O L S
Aircrack-ng Kismet Wireshark hcxtools


MOBILE SECURITY
A N D R O I D
Android Architecture APK Manifest Activities Services Broadcast Receivers
Content Providers Intents Permissions Deep Links WebViews SQLite
SharedPreferences Keystore Network Security Certificate Pinning Root Detection
IPC Static Analysis Dynamic Analysis Reverse Engineering
I O S
iOS Architecture IPA Swift Objective-C Keychain Sandbox Entitlements
URL Schemes Universal Links WebViews Network Security Certificate Pinning
Runtime Analysis Reverse Engineering Jailbreak Concepts
T O O L S
MobSF jadx apktool Frida Objection Burp Suite

CLOUD: THE NEW PERIMETER
Traditional perimeter security is not enough.
A W S
IAM EC2 S3 VPC Lambda ECS EKS Cognito KMS Secrets Manager
CloudTrail CloudWatch API Gateway Route 53 ECR
A Z U R E
Entra ID Azure IAM Virtual Machines Storage Functions Key Vault AKS
Defender
G C P
IAM Compute Cloud Storage GKE Cloud Functions Secret Manager
Cloud Logging
C L O U D S E C U R I T Y
IAM Misconfiguration Identity Attack Paths Storage Exposure Metadata Services
SSRF Cloud Credentials Role Abuse Privilege Escalation Cross-Account Access
Cloud Persistence Cloud Logging Cloud Detection


CONTAINERS & KUBERNETES
D O C K E R
Images Containers Dockerfile Registry Networking Volumes Capabilities
Privileges Secrets Docker Socket
K U B E R N E T E S
Pods Services Deployments Ingress API Server RBAC Service Accounts
Secrets ConfigMaps Network Policies Admission Controllers Namespaces
S E C U R I T Y
Container Escape Concepts Kubernetes Privilege Escalation Identity Abuse
Secret Exposure Supply Chain Image Security Cluster Security Runtime Detection


DEVSECOPS & SOFTWARE SUPPLY CHAIN
Secure SDLC Source Code Security SAST DAST SCA Secret Scanning
Dependency Security Package Security CI/CD Security Git Security
Container Security IaC Security SBOM Artifact Security Software Signing
Build Pipeline Security Dependency Confusion Supply Chain Attacks


AI SECURITY — THE 2026 BATTLEFIELD
AI is no longer a side topic.
A I F O U N D A T I O N S
Machine Learning Deep Learning Neural Networks Transformers LLMs Embeddings
Vector Databases RAG AI Agents Tool Calling Function Calling Model APIs
Agent Memory
L L M S E C U R I T Y
Prompt Injection Indirect Prompt Injection Jailbreaks
Sensitive Information Disclosure System Prompt Leakage Insecure Output Handling
Excessive Agency Data / Model Poisoning Vector / Embedding Weaknesses
Unbounded Consumption
These areas align with OWASP's current GenAI security work, including prompt injection,
supply chain, poisoning, excessive agency, system-prompt leakage, and vector/embedding
weaknesses.
A G E N T I C S E C U R I T Y
AI Agent Architecture Agent Identity Agent Permissions Tool Abuse
Context Poisoning Memory Poisoning Agent-to-Agent Security Tool Boundary Security
Human-in-the-Loop Agent Sandboxing Agent Supply Chain Autonomous Security Testing
AI Red Teaming|


WEB3 & BLOCKCHAIN
Blockchain Architecture Ethereum EVM Solidity Smart Contracts Wallets
Tokens DeFi Oracles Bridges Signatures
S E C U R I T Y
Reentrancy Access Control Integer Issues Oracle Manipulation
Flash Loan Concepts Signature Abuse Smart Contract Logic Wallet Security
Bridge Security Blockchain Forensics



IoT & EMBEDDED
Embedded Systems Firmware Bootloaders UART SPI I2C JTAG
Hardware Debugging Firmware Extraction Firmware Analysis Secure Boot
OTA Updates Device Authentication IoT Network Security


AUTOMOTIVE
CAN CAN Bus Analysis ECU Automotive Ethernet Telematics Infotainment
Keyless Systems Vehicle Networks Firmware Automotive Threat Modeling
Automotive Forensics


ICS / SCADA / OT
SCADA PLC HMI RTU ICS Architecture OT Networks Modbus DNP3 OPC
Industrial Protocols Safety Systems OT Monitoring ICS Threat Modeling
Industrial Incident Response


TELECOM SECURITY
GSM 3G 4G 5G SIM Security SS7 Diameter IMS VoLTE Telecom Signaling Cellular Security


DIGITAL FORENSICS
Disk Forensics Memory Forensics Network Forensics Windows Forensics
Linux Forensics Browser Forensics Email Forensics Mobile Forensics
Timeline Analysis Artifact Analysis Evidence Preservation
T O O L S
Volatility Autopsy FTK Wireshark



INCIDENT RESPONSE
Detection Triage Investigation Containment Eradication Recovery
Root Cause Analysis Threat Hunting IOC Analysis Timeline Construction
Malware Investigation Post-Incident Review


BLUE TEAM: LEARN TO HUNT YOURSELF
A strong attacker should understand what defenders can see.
SOC SIEM EDR XDR IDS IPS Firewall Logging Detection Engineering
Threat Hunting Sigma YARA MITRE ATT&CK Behavioral Detection
Endpoint Telemetry Network Telemetry


THREAT INTELLIGENCE
Threat Actors Campaigns Malware Families Infrastructure IOCs IOAs TTPs
Domains IPs Hashes Infrastructure Correlation Attribution Threat Reports
MITRE ATT&CK Mapping

OSINT & DIGITAL INVESTIGATION
Search Intelligence Domain Intelligence Username Intelligence Email Intelligence
Public Records Metadata Image Intelligence Video Intelligence
Social Media Intelligence Infrastructure Intelligence Breach Intelligence
Dark Web Intelligence Threat Actor Research Digital Footprinting



DARK WEB & UNDERGROUND ECOSYSTEM
Study the ecosystem.
Tor Onion Services Privacy Networks Underground Markets Cybercrime Ecosystems
Threat Actor Communities Leak Ecosystems Malware Ecosystems Initial Access Markets
Credential Markets Ransomware Ecosystems Cryptocurrency Intelligence
Dark Web OSINT

OPSEC
The attacker who leaves unnecessary evidence loses.
Personal OPSEC Infrastructure OPSEC Identity Separation Metadata Awareness
Compartmentalization Secure Communications Logging Awareness
Infrastructure Hygiene Operational Security Failures


SECURITY AUTOMATION
Build systems that work for you.
A U T O M A T I O N
Recon Automation Enumeration Asset Discovery API Testing Vulnerability Scanning
Log Processing Threat Intelligence Malware Triage Report Generation
D E V E L O P M E N T
Python Bash PowerShell Go APIs CLI Tools Custom Security Frameworks


SECURITY TOOL DEVELOPMENT
Do not become dependent on somebody else's tool. Learn to build:
Recon Tools Port Scanners HTTP Clients API Testing Tools Fuzzers Parsers
Enumeration Frameworks Log Analyzers Threat Intelligence Tools
Malware Analysis Utilities Custom Research Tools



BUG BOUNTY
M I N D S E T
Do not hunt for vulnerabilities.
Hunt for assumptions.
S K I L L S
Scope Analysis Recon Asset Discovery Endpoint Discovery API Analysis
Authentication Testing Authorization Testing Business Logic Race Conditions
Chaining Impact Analysis Report Writing Triage Communication
E L I T E B U G B O U N T Y
• Find unusual attack surfaces
• Understand application architecture
• Read JavaScript
• Understand APIs
• Analyze business workflows
• Chain low-severity weaknesses
• Discover novel logic flaws
• Research instead of blindly scanning


CTF / LAB DOMINATION
W E B
PortSwigger OWASP Juice Shop DVWA PentesterLab
N E T W O R K / S Y S T E M
Hack The Box TryHackMe VulnHub Proving Grounds
R E V E R S E / P W N
pwn challenges Reverse Engineering Challenges Binary Exploitation
C R Y P T O
Cryptography Challenges
F O R E N S I C S
Memory Disk Network Malware
O S I N T
Investigation Challenges
E N T E R P R I S E
Active Directory Labs Cloud Labs


SECURITY RESEARCHER MODE
This is the transition from practitioner to researcher. You should be able to:
Read source code Read technical papers Read CVEs Read advisories
Reproduce vulnerabilities Modify PoCs Debug crashes Perform patch diffing
Find variants Build fuzzers Analyze protocols Reverse binaries
Develop hypotheses Discover novel vulnerabilities Publish responsible research



EMERGING ATTACK SURFACES — 2026+
Never stop updating this section.
AI Agents Autonomous Coding Agents AI Tool Interfaces Agent Skills MCP Security
RAG Systems Vector Databases Cloud Identity Serverless Edge Computing
WebAssembly Supply Chain Software Signing Passkeys API Ecosystems
Microservices Service Mesh Kubernetes Browser Security Modern Authentication
Connected Devices Autonomous Systems



THE ELITE TOOLBOX
R E C O N
Nmap Amass Subfinder Assetfinder httpx Naabu Nuclei ffuf Gobuster
W E B
Burp Suite OWASP ZAP SQLMap
N E T W O R K
Wireshark tcpdump Netcat Socat
A C T I V E D I R E C T O R Y
BloodHound Impacket NetExec Rubeus Mimikatz Certipy
P A S S W O R D
Hashcat John the Ripper
R E V E R S E E N G I N E E R I N G
Ghidra IDA Binary Ninja x64dbg WinDbg GDB radare2
M A L W A R E
YARA REMnux FLARE-VM Volatility
M O B I L E
MobSF Frida Objection jadx apktool
C L O U D
AWS CLI Azure CLI gcloud Cloud-native security tooling


THE ELITE PROGRESSION
L E V E L 0 — U S E R
Understand: Computers · Internet · Operating Systems · Basic Security
L E V E L 1 — T E C H N I C I A N
Master: Linux · Windows · Networking · Basic Programming
L E V E L 2 — P E N T E S T E R
Master: Recon · Web · APIs · Network Pentesting · Privilege Escalation · Reporting
L E V E L 3 — O P E R A T O R
Master: Active Directory · Red Teaming · Identity · Cloud · Lateral Movement · OPSEC ·
Detection Awareness
L E V E L 4 — R E S E A R C H E R
Master: Reverse Engineering · Fuzzing · Vulnerability Research · Exploit Development · Source
Code Analysis · Protocol Research
L E V E L 5 — E L I T E
Can: Understand unfamiliar systems quickly · Discover attack surfaces · Build custom tooling ·
Chain vulnerabilities · Reverse engineer unknown software · Research novel attack paths ·
Analyze malware · Understand enterprise identity · Operate across cloud, endpoint and
network · Attack and defend AI systems · Develop original research



