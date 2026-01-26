# Fundamentals
### **Red Team Fundamentals: Master Checklist**
### **1. Hardware, CPU & Pre-Boot Environment**

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

### **2. Operating System Internals**

_Understanding the resource manager to manipulate its logic._

- [ ] **Privilege Levels:** Master the **"Ring" architecture**; specifically the separation between **Ring 0** (Kernel) and **Ring 3** (User).
    
- [ ] **System Calls:** Trace syscall execution (e.g., **NtCreateFile** or **execve**) from user-space API calls through the Interrupt to the kernel handler.
    
- [ ] **Process & Thread Mechanics:** Understand the lifecycle of processes and threads, including scheduling and context switching.
    
- [ ] **Process Environment Block (PEB):** In Windows, master the **PEB structure** to find loaded DLLs or implement anti-debugging techniques.
    
- [ ] **Authorization & Tokens:** Master Windows **SIDs**, **Access Tokens**, and **Token Impersonation**; understand Linux **Namespaces** and **Cgroups** (the basis for containers).
    
- [ ] **File Systems (Linux):** Master the root directory structure, **Inodes**, and the **"Everything is a file"** philosophy.
    
- [ ] **File Systems (Windows):** Master **NTFS permissions**, **Registry hives**, and the usage of **Alternate Data Streams (ADS)** to hide payloads.
    

---

### **3. Memory Management & Exploitation**

_The primary surface for local code execution and privilege escalation._

- [ ] **Virtual Memory:** Learn how the OS maps physical RAM to virtual addresses to provide process isolation.
    
- [ ] **The Stack:** Master the **LIFO** (Last-In, First-Out) structure and the **Function Prologue/Epilogue** to understand how return addresses are stored.
    
- [ ] **The Heap:** Understand **dynamic memory allocation** and how applications request memory at runtime.
    
- [ ] **Buffer Overflows:** Master how data can overwrite adjacent memory to hijack the **EIP/Instruction Pointer**.
    
- [ ] **Exploit Mitigations:** Study **ASLR** (Address Space Layout Randomization) and **DEP/NX** (Data Execution Prevention); master **ROP** (Return Oriented Programming) to bypass them.
    

---

### **4. Strategy & Red Team Operations**

_The professional tradecraft required to execute and survive in the field._

- [ ] **Virtualization:** Master **Type-1** (ESXi, Proxmox) and **Type-2** (VMWare, VirtualBox) hypervisors for lab building and isolation.
    
- [ ] **Container Escape:** Learn the common misconfigurations that allow an attacker to **"escape"** a Docker container into the Host OS.
    
- [ ] **Living Off The Land (LotL):** Master the usage of **LOLBAS** (Windows) and **GTFOBins** (Linux) to use legitimate system binaries for malicious intent.
    
- [ ] **CLI & Automation:** Maintain total fluency in **Bash**, **PowerShell**, and **Python** to automate repetitive tasks and post-exploitation.
    
- [ ] **Log Management:** Master the location of **Event Logs** (Windows) and **/var/log** (Linux); learn to clear or modify them to hide presence.
    
- [ ] **Cloud Persistence:** Learn to use **OAuth tokens** and **App Passwords** to maintain access even if a victim's password is changed.
    
- [ ] **Data Representation & Logic:** Master fast conversion between **Binary, Decimal, and Hexadecimal**; understand **Boolean Logic** (XOR) for encryption/obfuscation.
    
- [ ] **File Signatures:** Identify file types (EXE, ELF, JPG) by their **"Magic Bytes"** instead of their file extensions.
---
#### **5. Wireless & Physical Connections**

- [ ] **NFC (Near Field Communication):** Learn the mechanics of intercepting or "cloning" badges and cards.
    
- [ ] **Bluetooth:** Master **BLE vs. Classic** protocols and attack types like **Bluejacking** and **Bluesnarfing**.
    
- [ ] **WiFi Hardware:** Master the hardware side—specifically **Monitor Mode** and **Packet Injection** capabilities.
    
- [ ] **Infrared (IR):** Understand its persistence in physical security and IoT devices.
    
- [ ] **Storage Media:** Understand physical data storage on HDDs vs. SSDs and why "deleting" isn't "wiping."
    

---
#### **6. Application Suites & Cloud Vectors**

- [ ] **MS Office Suite:** Master **VBA Macro exploits** to execute code via legitimate documents.
    
- [ ] **Cloud Persistence:** Learn how to use **OAuth tokens** or **App Passwords** in Google/iCloud to maintain access after password changes.
    
- [ ] **Data Exfiltration:** Learn to use legitimate services (Google Drive, iCloud) to sneak data out undetected.
    

---
#### **7. Data Representation & Logic**

- [ ] **Number Systems:** Be able to convert between **Binary, Decimal, and Hexadecimal** mentally.
    
- [ ] **Boolean Logic:** Master **AND, OR, NOT, and XOR** (the foundation of encryption and obfuscation).
    
- [ ] **File Headers:** Identify file types (EXE, ELF, JPG) by their **"Magic Bytes"** instead of extensions.
    
- [ ] **Instruction Sets:** Basic familiarity with **Assembly** (MOV, PUSH, POP, CALL, JMP).

---

# Networking 

#### **Layer 1: Physical (The Hardware Surface)**

- [ ] **Media Mechanics:** Master the physical properties of Copper (electrical), Fiber (light), and Wireless (RF) transmission.
    
- [ ] **Network Topologies:** Understand the physical and logical layout of networks: **Star, Ring, Mesh, and Bus**.
    
- [ ] **Wireless Standards:** Master hardware constraints for **NFC (13.56 MHz)**, **Bluetooth (2.4 GHz)**, **Infrared**, and **WiFi 6E/7 (6 GHz)**.
    
- [ ] **I/O & DMA:** Understand how **Direct Memory Access** allows peripherals to read system RAM by bypassing the CPU.
    
- [ ] **Hardware Diagnostics:** Learn OS-independent troubleshooting to identify hardware failures vs. rootkits.
    
- [ ] **Storage Forensics:** Understand HDD (magnetic) vs. SSD (cells) and why "deleting" is not "wiping".
    

#### **Layer 2: Data Link (The Local Target)**

- [ ] **ARP Mechanics:** Master **ARP Cache Poisoning** to position yourself for MITM attacks.
    
- [ ] **MAC Analysis:** Use OUI to identify hardware manufacturers from captured MAC addresses.
    
- [ ] **VLAN Segmentation:** Master **802.1Q tagging** and execute **VLAN Hopping** via double-tagging or switch-spoofing.
    
- [ ] **Switching Logic:** Understand **CAM tables** and perform **CAM Table Flooding** to force a switch into "hub mode".
    
- [ ] **Network Scopes:** Differentiate between the reach of **PAN, LAN, WLAN, MAN, and WAN**.
    

#### **Layer 3: Network (The Routing Logic)**

- [ ] **IP Addressing (v4/v6):** Master Public/Private spaces, Subnet Masks, Classes (A, B, C), and **IPv6** compression.
    
- [ ] **Subnetting & CIDR:** Calculate subnets (/24, /25, /26), Wildcard masks, and host boundaries without a calculator.
    
- [ ] **Routing Protocols:** Master the logic of **OSPF** (Enterprise), **BGP** (Internet), and **EIGRP**.
    
- [ ] **NAT/PAT:** Understand how internal IPs are masked and how to bypass this via port forwarding or UPnP.
    
- [ ] **Gateway Identification:** Master the role of the **Default Gateway** as the primary exit point for exfiltration.
    

#### **Layer 4: Transport (The Reliability Layer)**

- [ ] **TCP/UDP Grammar:** Understand connection-oriented vs. connectionless protocols and the **3-Way Handshake**.
    
- [ ] **TCP Flags:** Master flags like **SYN, FIN, RST, and PSH** for OS fingerprinting.
    
- [ ] **Port Scanning:** Use **Nmap** for SYN, FIN, and Xmas scans to bypass firewall logging.
    
- [ ] **Port Mastery:** Memorize default ports for **SSH (22)**, **RDP (3389)**, **DNS (53)**, **FTP (21)**, and **SMB (445)**.
    

#### **Layers 5-7: Application & Session (The Payload)**

- [ ] **DNS & DHCP Exploitation:** Master **DNS Poisoning** for redirection and **DHCP Starvation** to kill availability.
    
- [ ] **Secure Communications:** Master the **SSL/TLS Handshake** and **SSL Stripping** to force cleartext.
    
- [ ] **Authentication:** Master **Kerberos, RADIUS, LDAP, SSO, and Certificates**.
    
- [ ] **Application Vectors:** Master **VBA Macro exploitation** (MS Office) and **OAuth token theft** (Cloud Suites).
    

#### **The Strategy Layer: Red Team Ops & Miscellaneous**

- [ ] **Lab Progression:** Move from **Packet Tracer** (Beginner) to **GNS3/EVE-NG** (Advanced) and **Wireshark**.
    
- [ ] **Virtualization:** Master Type-1 (**ESXi, Proxmox**) and Type-2 (**VMWare, VirtualBox**) hypervisors.
    
- [ ] **Cloud Assets:** Master **VPCs**, **Security Groups**, **Load Balancers**, and **IAM** in AWS/Azure/GCP.
    
- [ ] **Automation:** Use **Python, Bash, and PowerShell** for subnet discovery and log clearing.
    
- [ ] **Monitoring & Evasion:** Use **NetFlow, SNMP**, and packet analyzers to understand **Zero Trust** and **SIEM/SOAR** limits.
    
- [ ] **Certifications:** Focus on **CCNA** (Networking Core) or **CompTIA Network+** (Beginner Path).
    
- [ ] **Ethics & ROE:** Master the **Rules of Engagement (RoE)** and professional reporting.


	