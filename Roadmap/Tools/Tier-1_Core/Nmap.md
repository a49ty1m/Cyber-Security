# 🗺️ Nmap: Complete Mastery Checklist

📝 [[Nmap_Notes|Notes]]

> **What is Nmap?** Nmap (Network Mapper) is the industry-standard network discovery and security auditing tool. It identifies live hosts, open ports, running services, operating systems, and vulnerabilities on a network. It is the **first tool** used in nearly every penetration test.
>
> **Why does it exist?** Networks are opaque by default. Before attacking or defending anything, you must know what's there — what machines, what ports, what software, what versions. Nmap turns an unknown network into a detailed inventory.
>
> **When to use it:** Every engagement. Reconnaissance, scanning, enumeration, vulnerability assessment, network inventory, compliance auditing.
>
> **When to avoid it:** When you don't have authorization (scanning without permission is illegal in most jurisdictions). When stealth is paramount and even SYN scans are too noisy (use passive techniques instead).
>
> **What mastering Nmap unlocks:** The ability to map any network, identify attack surfaces, discover vulnerabilities before exploitation, and communicate findings professionally. Nmap mastery is a prerequisite for every offensive security certification (OSCP, CEH, PNPT, etc.).
>
> **Roadmap Stage / Module:** Stage 2: Module 08 (Footprinting) & Module 09 (Scanning)

---

## 🧭 Navigation

> [[Cyber-Security/Roadmap/README|🏠 Master Roadmap]] · [[Cyber-Security/Roadmap/Tools/README|🔧 Tools Index]] · [[Cyber-Security/Lab/Metasploitable_2/TASK_LIST|🐧 Metasploitable 2 Lab]] · [[Cyber-Security/Lab/OWASP_Broken_WebApps/TASK_LIST|🌐 OWASP BWA Lab]]

| Recon & Scanning | Exploitation | Post-Exploitation | Web & Traffic |
|:-----------------|:-------------|:-------------------|:--------------|
| **🗺️ Nmap** (you are here) | [[Metasploit_Framework\|💀 Metasploit]] | [[LinPEAS\|🐉 LinPEAS]] | [[Burp_Suite\|🕷️ Burp Suite]] |
| [[Netcat\|🔌 Netcat]] | [[Impacket\|🐍 Impacket]] | [[BloodHound\|🩸 BloodHound]] | [[Wireshark\|🦈 Wireshark]] |
| | [[Hydra\|🔓 Hydra]] | [[Hashcat\|🔥 Hashcat]] | |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals & Setup | 6 | 3–4 hours |
| 2 | Core Scanning Features | 10 | 6–8 hours |
| 3 | Intermediate Techniques | 7 | 5–7 hours |
| 4 | Advanced Usage | 6 | 6–8 hours |
| 5 | Tool Integration | 3 | 2–3 hours |
| 6 | Practical Labs | 3 | 5–8 hours |
| 7 | Real-World Methodology | 4 | 3–4 hours |
| | **Total** | **39** | **~29–42 hours** |

**Prerequisites:** Basic TCP/IP networking (OSI model, IP addressing, ports, protocols). Linux command line basics. A lab environment with at least one target (Metasploitable 2 recommended).

**Alternatives & Competitors:** Masscan (speed-focused, less feature-rich), RustScan (fast port scanner that feeds into Nmap), Zmap (internet-scale scanning), Angry IP Scanner (GUI-based, simple), Netcat (manual port checking).

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — Understand What Nmap Actually Does

- [ ] **Completed** · ⭐ Beginner · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Explain what Nmap does, which pentest phase it belongs to (Reconnaissance/Scanning), and why it's used before exploitation. |
| **Skills Learned** | PTES methodology awareness, attack surface concept, why port scanning is the foundation of every engagement. |
| **Expected Output** | Diagram showing where Nmap fits in the pentest lifecycle (Recon → **Scanning** → Enumeration → Exploitation → Post-Exploitation → Reporting). |
| **Common Mistakes** | Thinking Nmap is an exploitation tool (it finds targets, not exploits them). Not understanding that Nmap requires authorization to use. |

---

### Task 1.2 — Installation & Version Verification

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Verify Nmap is installed, check version, understand components (Nmap, Ncat, Nping, Ndiff, NSE scripts). |
| **Skills Learned** | Tool version management, locating NSE script libraries. |
| **Practical Exercise** | Run: `nmap --version`, `locate *.nse | wc -l` (count scripts), `which ncat nping ndiff`. |
| **Expected Output** | Nmap version number. Count of NSE scripts (600+). Confirmation of ncat, nping, ndiff locations. |
| **Common Mistakes** | Using an outdated version. Not knowing that Nmap includes Ncat. |

---

### Task 1.3 — Understand Nmap's Permission Model (Root vs Non-Root)

- [ ] **Completed** · ⭐ Beginner · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand why many Nmap scan types require root/sudo and what changes when you run as regular user vs root. |
| **Skills Learned** | Raw socket access, why SYN scans need root, what happens when Nmap falls back to TCP connect scans. |
| **Practical Exercise** | Run: `nmap <target>` as user, then `sudo nmap <target>`. Compare scan types. Use `--reason` flag. |
| **Expected Output** | Non-root uses TCP connect (`-sT`). Root uses SYN stealth (`-sS`). Documentation of differences in speed and stealth. |
| **Common Mistakes** | Always running as root without understanding why. Not using `--reason` to understand port classifications. |

---

### Task 1.4 — Understand Port States

- [ ] **Completed** · ⭐ Beginner · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand all six Nmap port states: open, closed, filtered, unfiltered, open\|filtered, closed\|filtered. Know what network behavior produces each state. |
| **Skills Learned** | TCP/UDP response behavior, firewall interaction with scans, why "filtered" doesn't mean "safe." |
| **Practical Exercise** | Scan: `sudo nmap -sS -p 1-100 --reason <target>`. Document the reason for each state. |
| **Expected Output** | A reference table: Port State → Network Behavior → What It Means. |
| **Common Mistakes** | Ignoring filtered ports (they may be open behind a firewall). Assuming "closed" means "not useful." |

---

### Task 1.5 — Output Formats & Saving Results

- [ ] **Completed** · ⭐ Beginner · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Master all Nmap output formats. Always save scan results — never scan without saving output. |
| **Skills Learned** | Output format selection, result archival, professional documentation habits. |
| **Practical Exercise** | Run: `sudo nmap -sV <target> -oA scan_results`. Examine: `.nmap` (human-readable), `.gnmap` (grepable), `.xml` (structured). Parse grepable: `grep "open" scan_results.gnmap`. |
| **Expected Output** | Three output files created. Understanding of when to use each format. |
| **Common Mistakes** | Not saving output. Using only `-oN` and missing XML. Not using `-oA`. Overwriting previous scans. |

---

### Task 1.6 — Nmap Help & Documentation Navigation

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Learn to navigate Nmap's help, man page, and online documentation efficiently. |
| **Skills Learned** | Self-guided learning, man page navigation, finding the right flag quickly. |
| **Practical Exercise** | Use `nmap -h | grep -i "script"` to find script flags. Use `man nmap` and search for "timing" (`/timing`). Find NSE docs: `nmap --script-help default`. |
| **Expected Output** | Ability to quickly find any Nmap option using help and man pages. |
| **Common Mistakes** | Trying to memorize every flag. Not reading `man nmap`. |

---

# PHASE 2: CORE SCANNING FEATURES

---

### Task 2.1 — Host Discovery (Ping Sweep)

- [ ] **Completed** · ⭐ Beginner · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Discover live hosts on a subnet without port scanning. |
| **Skills Learned** | Host discovery techniques (ICMP, TCP, ARP), why `-sn` is preferred over deprecated `-sP`. |
| **Syntax** | `sudo nmap -sn 192.168.1.0/24` (discover hosts, no port scan). |
| **Real-World Scenario** | First step of any internal network assessment. Used for network inventory and scope validation. |
| **Expected Output** | List of live hosts with IP and MAC addresses. Host count summary. |
| **Common Mistakes** | Relying only on ICMP echo (many hosts block ping but respond to TCP probes). Scanning a /16 subnet without realizing it's 65,536 hosts. |

---

### Task 2.2 — TCP SYN Scan (Stealth Scan)

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Perform the default and most common scan type. Understand why it's called "stealth" (half-open — never completes the handshake) and its advantages over TCP connect scans. **⚠️ Reality Check:** The "stealth" label is outdated. Modern IDS/IPS systems detect SYN scans trivially. The term refers to old systems that only logged completed TCP connections. Against modern defenses, SYN scans are just as detectable as any other scan type. |
| **Skills Learned** | SYN scan mechanics (SYN → SYN-ACK → RST instead of ACK), why half-open was historically considered stealthier (some old logging only recorded completed connections), raw socket requirement, comparison with `-sT`, understanding modern detection capabilities. |
| **Syntax** | `sudo nmap -sS <target>` (SYN scan, default 1000 ports). `sudo nmap -sS -p- <target>` (all 65535 ports). |
| **Real-World Scenario** | Standard scan for every pentest. Fast, reliable, relatively quiet. The scan type used in ~90% of all Nmap usage. |
| **Expected Output** | Open/closed/filtered port list. Compare speed with `nmap -sT` (connect scan) — SYN is faster because it doesn't complete the handshake. |
| **Common Mistakes** | Not understanding the "stealth" claim is outdated (modern IDS/IPS detects SYN scans easily). Only scanning default 1000 ports instead of all 65535 (`-p-`). Not using `-sS` explicitly (Nmap defaults to it with root, but being explicit is good practice). |

---

### Task 2.3 — TCP Connect Scan

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand TCP connect scan (`-sT`), when it's required (no root access, scanning through SOCKS proxies), and its trade-offs vs SYN scanning. |
| **Skills Learned** | Full TCP handshake scanning, when `-sT` is mandatory (non-root, proxychains). |
| **Syntax** | `nmap -sT <target>` (works without root). `proxychains nmap -sT -Pn <target>` (through a proxy). |
| **Real-World Scenario** | Scanning through a SOCKS proxy during a pivot. Scanning from a compromised low-privilege host. |
| **Expected Output** | Same port results as SYN scan but slower. |
| **Common Mistakes** | Using `-sS` through proxychains (it will fail). Not understanding why `-sT` is slower. |

---

### Task 2.4 — Service Version Detection

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Identify exact software names and version numbers running on open ports. |
| **Skills Learned** | Service fingerprinting, version intensity levels, why version detection is critical for exploit matching. |
| **Syntax** | `sudo nmap -sV <target>`. `sudo nmap -sV --version-intensity 9 <target>` (maximum probing). |
| **Real-World Scenario** | "Port 80 is open" is less useful than "Apache httpd 2.4.7 on Ubuntu" — the version tells you which exploits to research. |
| **Expected Output** | Service name and version for each open port. |
| **Common Mistakes** | Not using `-sV` at all. Not understanding that `-sV` sends additional probes (it's not passive). Blindly trusting version output (services can lie). |

---

### Task 2.5 — OS Detection

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Identify the target's operating system using TCP/IP stack fingerprinting. |
| **Skills Learned** | TCP/IP stack fingerprinting, why Nmap shows percentage confidence, CPE strings. |
| **Syntax** | `sudo nmap -O <target>`. `sudo nmap -O --osscan-guess <target>` (show best guesses). |
| **Real-World Scenario** | Determines whether a target is Windows or Linux (affects exploitation strategy and privilege escalation paths). |
| **Expected Output** | OS family, version, and confidence percentage. CPE string. |
| **Common Mistakes** | Trusting OS detection blindly (it can be wrong). Not understanding that OS detection requires at least one open and one closed port. |

---

### Task 2.6 — UDP Scanning

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Scan UDP ports. UDP scanning is slower and less reliable than TCP but essential for finding DNS, SNMP, DHCP, and TFTP services. |
| **Skills Learned** | UDP protocol behavior, why UDP scans are slow, combining UDP with version detection for better accuracy. |
| **Syntax** | `sudo nmap -sU --top-ports 50 <target>`. `sudo nmap -sU -sV -p 53,161,162 <target>` (targeted with version detection). |
| **Real-World Scenario** | SNMP (port 161) with default community strings is one of the most common findings on internal networks. None of these are found without UDP scanning. |
| **Expected Output** | List of open/open\|filtered UDP ports. Understanding that "open\|filtered" means no response (could be open or firewalled). |
| **Common Mistakes** | Scanning all 65535 UDP ports (takes hours — use `--top-ports`). Not combining `-sU` with `-sV`. Skipping UDP scans entirely. |

---

### Task 2.7 — Default Script Scan (NSE)

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Run Nmap's default NSE scripts (`-sC`) and understand what additional intelligence they provide. Learn script categories: safe, intrusive, vuln, brute, discovery, auth. |
| **Skills Learned** | NSE architecture, default script behavior, script categories and risk levels. |
| **Syntax** | `sudo nmap -sC <target>`. `sudo nmap -sV -sC <target>` (most common combination). `nmap --script-help default`. |
| **Real-World Scenario** | Default scripts reveal immediate wins: anonymous FTP, HTTP titles, SMB OS discovery, SSL certificates. |
| **Expected Output** | Script output under each port. Examples: `ftp-anon: Anonymous FTP login allowed`, `http-title: Apache2 Ubuntu Default Page`. |
| **Common Mistakes** | Not using `-sC` (missing critical intelligence). Confusing `-sC` with `--script vuln` (default scripts are safe). |

---

### Task 2.8 — The Professional Scan Workflow

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 45 min

| Field | Detail |
|:---|:---|
| **Objective** | Learn the standard professional Nmap workflow: (1) discover hosts, (2) fast port scan all TCP, (3) targeted version + script scan on open ports, (4) targeted UDP scan. |
| **Skills Learned** | Efficient scanning methodology, why splitting scans is faster than one monolithic scan. |
| **Syntax** | Step 1: `sudo nmap -sn 192.168.1.0/24 -oA discovery`. Step 2: `sudo nmap -sS -p- -T4 <target> -oA tcp-all`. Step 3: `sudo nmap -sV -sC -p <open-ports> <target> -oA tcp-detailed`. Step 4: `sudo nmap -sU --top-ports 50 <target> -oA udp-top50`. |
| **Real-World Scenario** | Every professional pentester uses this workflow. It's faster because Step 2 quickly finds open ports, and Step 3 focuses version/script detection only on open ports. |
| **Expected Output** | Four sets of scan output files. Understanding of why this approach takes less total time. |
| **Common Mistakes** | Running `nmap -A -p- <target>` as a single scan (extremely slow). Not separating port discovery from service detection. Forgetting UDP entirely. |

---

### Task 2.9 — Timing Templates & Performance

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand Nmap's timing templates (`-T0` through `-T5`) and how they affect scan speed and detection risk. |
| **Skills Learned** | Timing template internals, the speed/accuracy/stealth triangle, when to use each template. |
| **Syntax** | `-T0` (paranoid — 5 min between probes), `-T3` (normal, default), `-T4` (aggressive — recommended for labs/CTFs), `-T5` (insane — may miss ports). |
| **Real-World Scenario** | Labs/CTFs: use `-T4`. Internal pentest: `-T4`. External pentest: `-T2` or `-T3`. Red team: `-T1` or custom timing. |
| **Expected Output** | Comparison of scan times using different templates. Note any ports missed at higher speeds. |
| **Common Mistakes** | Using `-T5` and missing open ports. Using `-T0` unnecessarily. |

---

### Task 2.10 — Target Specification Methods

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Master all the ways to specify targets: single IP, CIDR, ranges, lists, input files, and exclusions. |
| **Skills Learned** | CIDR notation, efficient target specification, using target lists for large engagements. |
| **Syntax** | Single: `nmap 192.168.1.10`. CIDR: `nmap 192.168.1.0/24`. Range: `nmap 192.168.1.1-50`. File: `nmap -iL targets.txt`. Exclude: `nmap 192.168.1.0/24 --exclude 192.168.1.1`. |
| **Real-World Scenario** | Client gives you a scope document with IP ranges and exclusions. Wrong target specification = out-of-scope scanning = legal liability. |
| **Expected Output** | Scans running against exactly the intended targets. |
| **Common Mistakes** | Scanning a /16 when you meant /24 (65536 vs 256 hosts). Not using `--exclude` for sensitive systems. |

---

# PHASE 3: INTERMEDIATE TECHNIQUES

---

### Task 3.1 — NSE Script Categories & Targeted Scripting

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 45 min

| Field | Detail |
|:---|:---|
| **Objective** | Use specific NSE script categories and individual scripts for targeted enumeration. Script categories: `auth`, `brute`, `discovery`, `exploit`, `intrusive`, `safe`, `vuln`. |
| **Skills Learned** | Targeted script selection, combining scripts, script arguments, understanding script risk levels. |
| **Syntax** | `nmap --script vuln <target>`. `nmap --script "smb-enum-*" <target>`. `nmap --script smb-brute --script-args userdb=users.txt <target>`. |
| **Real-World Scenario** | After finding SMB on port 445, run `smb-enum-shares`, `smb-enum-users`, `smb-os-discovery` without needing separate tools. |
| **Expected Output** | Targeted script results. Understanding of which scripts are safe vs intrusive. |
| **Common Mistakes** | Running `--script all` (includes dangerous scripts — never do this in production). Not using `--script-help <script>` before running an unfamiliar script. |

---

### Task 3.2 — Vulnerability Scanning with NSE

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Nmap's vulnerability detection scripts to identify known CVEs. **⚠️ Warning:** Some vuln scripts can be destructive or trigger IDS alerts. Always check documentation first. |
| **Skills Learned** | NSE vuln category scripts, `vulners` script (CVE lookup), Nmap vs dedicated vulnerability scanners. |
| **Syntax** | `nmap --script vulners -sV <target>` (safer: CVE lookup based on versions). `nmap --script smb-vuln-ms17-010 <target>` (specific vuln check). Check first: `nmap --script-help smb-vuln-ms17-010`. |
| **Real-World Scenario** | Quick vulnerability triage during a pentest. Checking for specific high-severity vulnerabilities (EternalBlue, BlueKeep) across a network. |
| **Expected Output** | CVE identifiers and specific vulnerability confirmations. |
| **Common Mistakes** | Treating Nmap vuln scanning as a replacement for Nessus/OpenVAS. Not combining with `-sV`. |

---

### Task 3.3 — Aggressive Scan & Combined Flags

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand the `-A` flag (enables OS detection, version detection, script scanning, and traceroute simultaneously). |
| **Skills Learned** | Flag composition, understanding that `-A` equals `-O -sV -sC --traceroute`, performance trade-offs. |
| **Syntax** | `sudo nmap -A <target>` (aggressive scan on top 1000 ports). `sudo nmap -A -p- <target>` (all ports — very slow). |
| **Real-World Scenario** | Acceptable for CTF challenges with one target. Not recommended for real engagements — too slow. The split workflow (Task 2.8) is always more efficient. |
| **Expected Output** | Complete scan with OS, versions, scripts, and traceroute. Timing comparison with split workflow. |
| **Common Mistakes** | Using `-A -p-` on large networks. Using `-A` when you only need version detection. |

---

### Task 3.4 — Firewall & IDS Evasion Techniques

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 45 min

| Field | Detail |
|:---|:---|
| **Objective** | Learn Nmap's evasion techniques for bypassing firewalls and IDS/IPS systems. |
| **Skills Learned** | Packet fragmentation (`-f`), decoy scanning (`-D`), source port manipulation (`--source-port`), idle/zombie scanning (`-sI`). |
| **Syntax** | Fragment packets: `sudo nmap -f <target>`. Decoys: `sudo nmap -D RND:10 <target>`. Source port 53: `sudo nmap --source-port 53 <target>`. Idle scan: `sudo nmap -sI <zombie-host> <target>`. |
| **Real-World Scenario** | Red team engagement where the target's IDS triggers alerts on standard scans. Bypassing firewall rules that allow traffic from port 53 (DNS). |
| **Expected Output** | Successful scan results using evasion where standard scans were blocked. Understanding of which technique bypasses which defense. |
| **Common Mistakes** | Using evasion in a lab/CTF (unnecessary and slows scanning). Not understanding that modern IDS easily detects most evasion techniques. |

---

### Task 3.5 — Nmap Output Parsing & Automation

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | Parse Nmap output using grep and awk. Extract specific information (open ports, service versions) for feeding into other tools. |
| **Skills Learned** | Grepable output parsing, building tool chains (Nmap → parser → next tool). |
| **Syntax** | Extract IPs with open ports: `grep "open" scan.gnmap | awk '{print $2}'`. Extract port numbers: `grep "/open/" scan.gnmap | awk -F'[ /]' '{print $5}'`. |
| **Real-World Scenario** | Scanning 500 hosts, then extracting all hosts with port 445 open for targeted SMB enumeration. |
| **Expected Output** | Clean extracted lists of IPs, ports, and services. A simple Bash script that generates target lists for the next tool. |
| **Common Mistakes** | Manually reading through thousands of lines of output instead of parsing. Not using `-oG` grepable format. |

---

### Task 3.6 — Scanning Through Proxies & Pivots

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Nmap through SOCKS proxies (proxychains) to scan internal networks from a pivot host. |
| **Skills Learned** | Pivoting concepts, proxychains configuration, why only `-sT` works through proxies, SSH dynamic port forwarding (`-D`). |
| **Syntax** | `ssh -D 1080 user@pivot-host`. Edit `/etc/proxychains4.conf`: `socks5 127.0.0.1 1080`. `proxychains nmap -sT -Pn -p 22,80,445 <internal-target>`. |
| **Real-World Scenario** | You've compromised a DMZ host and need to scan the internal network through it. |
| **Expected Output** | Scan results for internal hosts accessed through the proxy. Understanding of why `-sT -Pn` is required. |
| **Common Mistakes** | Using `-sS` through proxychains (fails — raw sockets can't traverse SOCKS). Not using `-Pn`. Scanning too many ports through a proxy (very slow). |

---

### Task 3.7 — Ndiff: Comparing Scan Results Over Time

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Use `ndiff` to compare two Nmap scans taken at different times. Identify new hosts, new ports, changed services. |
| **Skills Learned** | Network change detection, baseline comparison methodology. |
| **Syntax** | `ndiff scan-before.xml scan-after.xml`. Automated: cron job running `nmap -sV -oX /scans/scan-$(date +%F).xml <target>`. |
| **Real-World Scenario** | Monthly network inventory: comparing this month's scan to last month's to identify newly deployed services or removed hosts. |
| **Expected Output** | Ndiff output showing `+` (new) and `-` (removed) entries. |
| **Common Mistakes** | Comparing scans with different flags. Not using XML format for ndiff. |

---

# PHASE 4: ADVANCED USAGE

---

### Task 4.1 — Custom NSE Script Development

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 60 min

| Field | Detail |
|:---|:---|
| **Objective** | Read, understand, and modify an existing NSE script. Then write a simple custom NSE script. |
| **Skills Learned** | Lua programming basics, NSE API structure, how Nmap scripts interact with services. |
| **Practical Exercise** | Read `/usr/share/nmap/scripts/http-title.nse`. Modify it to also extract the server header. Write a script that checks if a specific banner string is present. |
| **Expected Output** | A working custom NSE script runnable with `--script /path/to/your/script.nse`. |
| **Common Mistakes** | Trying to write complex scripts without reading existing ones first. Not understanding the portrule. |

---

### Task 4.2 — IPv6 Scanning

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Scan IPv6 targets. Understand why IPv6 scanning is different (no traditional network sweeping due to massive address space). |
| **Skills Learned** | IPv6 address formats in Nmap, `-6` flag usage, why IPv6 often has different firewall rules than IPv4. |
| **Syntax** | `sudo nmap -6 <ipv6-address>`. `sudo nmap -6 --script targets-ipv6-multicast-echo <interface>` (discover IPv6 hosts). |
| **Expected Output** | Scan results for IPv6 targets. Comparison with IPv4 scan results (often different ports are open on IPv6). |
| **Common Mistakes** | Ignoring IPv6 entirely (many hosts have IPv6 with less restrictive firewall rules). Trying to sweep IPv6 subnets like IPv4. |

---

### Task 4.3 — Masscan + Nmap Combination Workflow

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Masscan for ultra-fast port discovery, then feed results into Nmap for detailed service analysis. Professional workflow for large-scope engagements. |
| **Skills Learned** | Masscan usage, speed vs depth trade-off, tool combination for efficiency. |
| **Syntax** | `sudo masscan -p1-65535 192.168.1.0/24 --rate 10000 -oL masscan-results.txt`. Parse results: `nmap -sV -sC -p <ports> <hosts> -oA detailed-scan`. |
| **Expected Output** | Masscan completes full-port scan of /24 in seconds. Nmap provides detailed service analysis. |
| **Common Mistakes** | Using Masscan rate too high (overwhelms target). Not feeding Masscan results into Nmap. |

---

### Task 4.4 — Nmap for Web Application Discovery

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Use HTTP-specific NSE scripts to enumerate web applications before switching to dedicated tools (Burp, Nikto). |
| **Skills Learned** | HTTP-specific NSE scripts, web technology detection, web application discovery at scale. |
| **Syntax** | `nmap --script http-enum <target>`. `nmap --script http-methods <target>`. `nmap --script http-title,http-headers <target>`. |
| **Expected Output** | Web application directories, allowed HTTP methods, technology stack identification, web vulnerabilities. |
| **Common Mistakes** | Using Nmap as a web vulnerability scanner (it's a first pass; Burp/Nikto are more thorough). |

---

### Task 4.5 — Idle (Zombie) Scanning

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| Field | Detail |
|:---|:---|
| **Objective** | Perform an idle scan using a third-party "zombie" host. Understand the IP ID side-channel technique that allows scanning without sending packets from your own IP. |
| **Skills Learned** | IP ID sequence prediction, side-channel attacks, truly anonymous scanning, finding suitable zombie hosts. |
| **Syntax** | Find zombie: `nmap --script ipidseq <candidate-zombie>` (look for "Incremental" IP ID). Idle scan: `sudo nmap -sI <zombie-ip> <target>`. |
| **Expected Output** | Port scan results attributed to the zombie host's IP, not yours. |
| **Common Mistakes** | Using a zombie with unpredictable IP IDs (scan fails). Using this in CTFs (unnecessary complexity). |

---

### Task 4.6 — Performance Tuning for Large Networks

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Optimize Nmap for scanning large networks efficiently. Tune parallelism, timeouts, and retry counts. |
| **Skills Learned** | `--min-hostgroup`, `--max-parallelism`, `--host-timeout`, `--max-retries` (reduce retries for speed). |
| **Syntax** | `sudo nmap -sS -p- --min-rate 5000 --max-retries 2 --host-timeout 5m -T4 -iL large-targets.txt -oA large-scan`. |
| **Expected Output** | Reasonable scan completion time for large networks. Understanding of accuracy trade-offs. |
| **Common Mistakes** | Setting `--max-retries 0` (misses ports). Setting `--host-timeout` too low. |

---

# PHASE 5: INTEGRATION WITH OTHER TOOLS

---

### Task 5.1 — Nmap → Metasploit Integration

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Import Nmap scan results into Metasploit database. Use Metasploit to search for exploits based on discovered services. |
| **Workflow** | `nmap -sV -oX scan.xml <target>` → `msfconsole` → `db_import scan.xml` → `hosts` → `services` → `search type:exploit name:<service>`. |
| **Expected Output** | Metasploit database populated with hosts and services. Exploit candidates listed. |

---

### Task 5.2 — Nmap → Web/Credential Testing Pipeline

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Extract hosts running specific services and feed into specialized tools (Nikto, Hydra). |
| **Workflow** | Extract SSH hosts: `grep "22/open" scan.gnmap | awk '{print $2}' > ssh-targets.txt` → `hydra -L users.txt -P passwords.txt -M ssh-targets.txt ssh`. Extract web servers: `grep "80/open\|443/open" scan.gnmap | awk '{print $2}'` → `nikto -h targets.txt`. |
| **Expected Output** | Automated testing pipeline from network discovery to service-specific enumeration. |

---

### Task 5.3 — Nmap in Bash Automation Scripts

- [ ] **Completed** · ⭐⭐⭐⭐ Intermediate-Advanced · ⏱️ 45 min

| Field | Detail |
|:---|:---|
| **Objective** | Write a Bash script that automates the full Nmap workflow: discovery → port scan → service detection → vulnerability check → parsing → reporting. |
| **Practical Exercise** | Create a script that: (1) ping sweep, (2) full TCP port scan, (3) version + script detection on open ports, (4) top 50 UDP scan, (5) vulnerability scan, (6) parses results into a markdown report. |
| **Expected Output** | A reusable scanning automation script. Clean markdown report generated from scan results. |

---

# PHASE 6: PRACTICAL LABS

---

### Lab 6.1 — Beginner: Map Metasploitable 2

- [ ] **Completed** · ⭐⭐ Beginner · ⏱️ 60 min

**Objective:** Discover all open TCP/UDP ports on Metasploitable 2, identify every service and version, create a professional service inventory document.

**Success Criteria:** All 23+ open TCP ports identified with correct service versions. At least 3 UDP services identified. Service inventory table complete with risk ratings.

---

### Lab 6.2 — Intermediate: Subnet Discovery & Triage

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 90 min

**Objective:** Map an entire /24 subnet, triage targets by attack surface, and create an attack plan.

**Setup:** Multiple VMs on the same subnet (Metasploitable 2, OWASP BWA, Windows VM).

**Success Criteria:** All hosts discovered. Top 3 targets prioritized with justification. Attack plan document created.

---

### Lab 6.3 — Advanced: Scan-to-Exploit Pipeline

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 120 min

**Objective:** Full pipeline: Nmap scan → exploit research → Metasploit exploitation → root access.

**Success Criteria:** Root shell obtained using a vulnerability discovered entirely through Nmap scanning. Complete documentation of the scan-to-shell pipeline.

---

# PHASE 7: REAL PENETRATION TESTING METHODOLOGY

---

### Task 7.1 — Nmap in the PTES Framework

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

**Objective:** Map Nmap to PTES phases: Intelligence Gathering (host discovery), Vulnerability Analysis (version detection + vuln scripts), Post-Exploitation (internal network scanning from compromised hosts), Reporting (scan evidence).

**Expected Output:** Mapping document showing where Nmap fits in each PTES phase with specific commands.

---

### Task 7.2 — Nmap in the Cyber Kill Chain

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

**Objective:** Map Nmap to Cyber Kill Chain phases: Reconnaissance (external scanning), C2 (detecting C2 channels), Actions on Objectives (internal network mapping during post-exploitation).

---

### Task 7.3 — Nmap Limitations & When to Use Other Tools

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

**Objective:** Document Nmap's limitations and identify when other tools are better.

**Key Limitations:** Slow for full-port scanning across many hosts (use Masscan). Not a web application scanner (use Burp Suite). Limited vulnerability detection vs Nessus/OpenVAS. Not for credential brute-forcing (use Hydra). No active exploitation capability.

---

### Task 7.4 — Professional Nmap Reporting Standards

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

**Objective:** Transform raw Nmap output into client-ready report findings.

**Practical Exercise:** Create: (1) executive summary, (2) network diagram, (3) service inventory table, (4) specific findings with CVSS scores.



# 📋 FINAL COMPETENCY MATRIX

| Competency | Self-Assessment |
|:---|:---:|
| Can perform host discovery on any network | ☐ |
| Can perform full TCP and UDP port scanning | ☐ |
| Can identify services and versions accurately | ☐ |
| Can use NSE scripts for targeted enumeration | ☐ |
| Can use evasion techniques when needed | ☐ |
| Can parse and automate Nmap output | ☐ |
| Can integrate Nmap with Metasploit, Searchsploit, and other tools | ☐ |
| Can scan through proxies and pivots | ☐ |
| Can optimize scans for large networks | ☐ |
| Can write a professional report from Nmap findings | ☐ |
| Can teach Nmap to another person | ☐ |
| Can troubleshoot scan failures independently | ☐ |

---

## 🎯 Interview Questions to Test Yourself

1. What is the difference between `-sS` and `-sT`? When would you use each?
2. Why does Nmap need root privileges for SYN scanning?
3. What does the "filtered" port state mean, and how does it differ from "closed"?
4. Explain the professional Nmap workflow for scanning a /24 network.
5. How would you scan a network through a SOCKS proxy?
6. What is an idle scan and how does it work?
7. How do you import Nmap results into Metasploit?
8. What are the limitations of Nmap compared to a dedicated vulnerability scanner?
9. How would you detect if a service is intentionally misreporting its version?
10. Explain the `-A` flag. When would you use it and when would you avoid it?

---

## 🔄 Revision Schedule

| Milestone | Review |
|:---|:---|
| After completing Phase 2 | Review Phase 1 concepts |
| After completing Phase 4 | Redo Lab 6.1 from memory |
| After completing Phase 6 | Redo all labs with time constraints |
| Monthly ongoing | Run a blind assessment against a new target |
