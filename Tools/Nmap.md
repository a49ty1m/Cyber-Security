# 🗺️ Nmap: Complete Mastery Checklist

> **What is Nmap?** Nmap (Network Mapper) is the industry-standard network discovery and security auditing tool. It identifies live hosts, open ports, running services, operating systems, and vulnerabilities on a network. It is the **first tool** used in nearly every penetration test.
>
> **Why does it exist?** Networks are opaque by default. Before attacking or defending anything, you must know what's there — what machines, what ports, what software, what versions. Nmap turns an unknown network into a detailed inventory.
>
> **When to use it:** Every engagement. Reconnaissance, scanning, enumeration, vulnerability assessment, network inventory, compliance auditing.
>
> **When to avoid it:** When you don't have authorization (scanning without permission is illegal in most jurisdictions). When stealth is paramount and even SYN scans are too noisy (use passive techniques instead).
>
> **What mastering Nmap unlocks:** The ability to map any network, identify attack surfaces, discover vulnerabilities before exploitation, and communicate findings professionally. Nmap mastery is a prerequisite for every offensive security certification (OSCP, CEH, PNPT, etc.).

---

## 🧭 Navigation

- 📋 [Master Roadmap](../Roadmap/README.md)
- 🐧 [Metasploitable 2 Lab](../Lab/Metasploitable_2/TASK_LIST.md)
- 🌐 [OWASP BWA Lab](../Lab/OWASP_Broken_WebApps/TASK_LIST.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals & Setup | 6 | 3–4 hours |
| 2 | Core Scanning Features | 10 | 6–8 hours |
| 3 | Intermediate Techniques | 7 | 5–7 hours |
| 4 | Advanced Usage | 6 | 6–8 hours |
| 5 | Tool Integration | 5 | 4–5 hours |
| 6 | Practical Labs | 5 | 6–10 hours |
| 7 | Real-World Methodology | 4 | 3–4 hours |
| 8 | Mastery Challenges | 4 | 8–12 hours |
| | **Total** | **47** | **~41–58 hours** |

**Prerequisites:** Basic TCP/IP networking (OSI model, IP addressing, ports, protocols). Linux command line basics. A lab environment with at least one target (Metasploitable 2 recommended).

**Alternatives & Competitors:** Masscan (speed-focused, less feature-rich), RustScan (fast port scanner that feeds into Nmap), Zmap (internet-scale scanning), Angry IP Scanner (GUI-based, simple), Netcat (manual port checking).

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — Understand What Nmap Actually Does

- [ ] **Completed** · ⭐ Beginner · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Explain in your own words what Nmap does, which pentest phase it belongs to (Reconnaissance/Scanning), and why it is used before any exploitation. |
| **Skills Learned** | PTES methodology awareness, scanning vs enumeration distinction, attack surface concept, why port scanning is the foundation of every engagement. |
| **Practical Exercise** | Write a one-paragraph explanation of Nmap as if explaining it to a non-technical manager. Then write a technical explanation for a fellow pentester. Compare the difference. |
| **Expected Output** | Two written explanations demonstrating understanding at both levels. A diagram showing where Nmap fits in the pentest lifecycle (Recon → **Scanning** → Enumeration → Exploitation → Post-Exploitation → Reporting). |
| **Common Mistakes** | Thinking Nmap is an exploitation tool (it's not — it finds targets, not exploits them). Confusing port scanning with vulnerability scanning (Nmap can do both, but they're different operations). Not understanding that Nmap is legal to install but illegal to use against unauthorized targets. |

---

### Task 1.2 — Installation & Version Verification

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Verify Nmap is installed, check its version, and understand the components that ship with it (Nmap, Ncat, Nping, Ndiff, NSE scripts). |
| **Skills Learned** | Tool version management, understanding that Nmap is a suite of tools (not just one binary), locating NSE script libraries. |
| **Practical Exercise** | Run: `nmap --version`, `locate *.nse | wc -l` (count available scripts), `ls /usr/share/nmap/scripts/ | head -20`, `which ncat nping ndiff`. |
| **Expected Output** | Nmap version number. Count of NSE scripts (600+). Confirmation of ncat, nping, ndiff locations. |
| **Common Mistakes** | Using an outdated version (some scripts and features require recent versions). Not knowing that Nmap includes Ncat (an improved netcat replacement). Not realizing NSE scripts are text files you can read and modify. |

---

### Task 1.3 — Understand Nmap's Permission Model (Root vs Non-Root)

- [ ] **Completed** · ⭐ Beginner · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand why many Nmap scan types require root/sudo privileges and what changes when you run Nmap as a regular user vs root. |
| **Skills Learned** | Raw socket access, why SYN scans need root (raw packets), what happens when Nmap falls back to TCP connect scans, the performance and stealth implications. |
| **Practical Exercise** | Run the same scan twice: `nmap <target>` as a regular user, then `sudo nmap <target>`. Compare the scan type used (check the output line "Nmap scan report" and timing). Use `--reason` flag to see why ports are classified as they are. |
| **Expected Output** | Non-root scan uses TCP connect (`-sT`). Root scan uses SYN stealth (`-sS`). Documentation of the differences in speed, stealth, and output. |
| **Common Mistakes** | Always running as root without understanding why. Not noticing that non-root scans are slower and noisier (full TCP handshake vs half-open SYN). Not using `--reason` to understand port state classifications. |

---

### Task 1.4 — Understand Port States

- [ ] **Completed** · ⭐ Beginner · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand all six Nmap port states: open, closed, filtered, unfiltered, open\|filtered, closed\|filtered. Know what network behavior produces each state. |
| **Skills Learned** | TCP/UDP response behavior, firewall interaction with scans, understanding ambiguous results, why "filtered" doesn't mean "safe." |
| **Practical Exercise** | Scan your target with `sudo nmap -sS -p 1-100 --reason <target>`. Find examples of open and closed ports. Then scan a port you know is firewalled. Document the reason for each state. |
| **Expected Output** | A reference table you create: Port State → Network Behavior → What It Means → Example. |
| **Common Mistakes** | Ignoring filtered ports (they may be open behind a firewall — worth further investigation). Assuming "closed" means "not useful" (closed ports confirm the host is alive and the IP is real). Not understanding that "open\|filtered" in UDP scans means "we didn't get a response, so we can't tell." |

---

### Task 1.5 — Output Formats & Saving Results

- [ ] **Completed** · ⭐ Beginner · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Master all Nmap output formats and understand when to use each. Always save scan results — never scan without saving output. |
| **Skills Learned** | Output format selection, result archival, importing results into other tools, professional documentation habits. |
| **Practical Exercise** | Run: `sudo nmap -sV <target> -oA scan_results`. Examine all three output files: `.nmap` (human-readable), `.gnmap` (grepable), `.xml` (structured). Parse the grepable file: `grep "open" scan_results.gnmap`. |
| **Expected Output** | Three output files created. Successful grep for open ports from the grepable format. Understanding of when to use each format (`.nmap` for reading, `.gnmap` for scripting, `.xml` for tool import). |
| **Common Mistakes** | Not saving output at all (you WILL need to reference scan results later). Using only `-oN` and missing the XML format (needed for importing into Metasploit, Burp, etc.). Not using `-oA` (saves all three formats with one flag). Overwriting previous scan results by using the same filename. |

---

### Task 1.6 — Nmap Help & Documentation Navigation

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Learn to navigate Nmap's built-in help, man page, and online documentation efficiently. Nobody memorizes all flags — knowing where to look is the skill. |
| **Skills Learned** | Self-guided learning, man page navigation, finding the right flag for a specific need. |
| **Practical Exercise** | Use `nmap -h | grep -i "script"` to find script-related flags. Use `man nmap` and search for "timing" (`/timing`). Find the NSE documentation: `nmap --script-help default`. |
| **Expected Output** | Ability to quickly find any Nmap option using help, man pages, and `--script-help`. |
| **Common Mistakes** | Trying to memorize every flag (there are hundreds — learn to search instead). Not reading `man nmap` (it's one of the best-written man pages in Linux). Not using `--script-help` to understand what a script does before running it. |

---

# PHASE 2: CORE SCANNING FEATURES

---

### Task 2.1 — Host Discovery (Ping Sweep)

- [ ] **Completed** · ⭐ Beginner · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Discover live hosts on a subnet without port scanning. Understand the multiple probe types Nmap uses for host discovery and why relying solely on ICMP ping is insufficient. |
| **Skills Learned** | Host discovery techniques (ICMP echo, TCP SYN to 443, TCP ACK to 80, ICMP timestamp), ARP discovery on local networks, why `-sn` is preferred over the deprecated `-sP`. |
| **Syntax** | `sudo nmap -sn 192.168.1.0/24` (discover hosts, no port scan). `sudo nmap -sn -PE -PP -PM 192.168.1.0/24` (all ICMP probe types). |
| **Real-World Scenario** | First step of any internal network assessment: "How many hosts are on this network?" Used for network inventory, rogue device detection, and scope validation. |
| **Expected Output** | List of live hosts with IP and MAC addresses (on local networks). Host count summary. |
| **Common Mistakes** | Relying only on ICMP echo (many hosts block ping but respond to TCP probes). Forgetting that `-sn` on a local subnet automatically uses ARP (which almost never fails). Scanning a /16 subnet without realizing it's 65,536 hosts (use smaller ranges). |

---

### Task 2.2 — TCP SYN Scan (Stealth Scan)

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Perform the default and most common scan type. Understand why it's called "stealth" (half-open — never completes the handshake) and its advantages over TCP connect scans. |
| **Skills Learned** | SYN scan mechanics (SYN → SYN-ACK → RST instead of ACK), why half-open is stealthier (some old logging only records completed connections), raw socket requirement, comparison with `-sT`. |
| **Syntax** | `sudo nmap -sS <target>` (SYN scan, default 1000 ports). `sudo nmap -sS -p- <target>` (all 65535 ports). |
| **Real-World Scenario** | Standard scan for every pentest. Fast, reliable, relatively quiet. The scan type used in ~90% of all Nmap usage. |
| **Expected Output** | Open/closed/filtered port list. Compare speed with `nmap -sT` (connect scan) — SYN is faster because it doesn't complete the handshake. |
| **Common Mistakes** | Not understanding the "stealth" claim is outdated (modern IDS/IPS detects SYN scans easily). Only scanning default 1000 ports instead of all 65535 (`-p-`). Not using `-sS` explicitly (Nmap defaults to it with root, but being explicit is good practice). |

---

### Task 2.3 — TCP Connect Scan

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand the TCP connect scan (`-sT`), when it's required (no root access, scanning through SOCKS proxies), and its trade-offs vs SYN scanning. |
| **Skills Learned** | Full TCP handshake scanning, when `-sT` is mandatory (non-root, proxychains), why it's slower and noisier but sometimes the only option. |
| **Syntax** | `nmap -sT <target>` (works without root). `proxychains nmap -sT -Pn <target>` (through a SOCKS proxy). |
| **Real-World Scenario** | Scanning through a SOCKS proxy or SSH tunnel during a pivot. Scanning from a compromised low-privilege host where you can't use raw sockets. |
| **Expected Output** | Same port results as SYN scan but slower. Understanding of why connect scans can't be used through proxychains with SYN scans. |
| **Common Mistakes** | Using `-sS` through proxychains (it will fail — raw sockets can't traverse SOCKS proxies). Not understanding why `-sT` is slower (full handshake + connection teardown per port). |

---

### Task 2.4 — Service Version Detection

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Identify exact software names and version numbers running on open ports. Understand that version detection sends probes and analyzes responses — it's not just reading banners. |
| **Skills Learned** | Service fingerprinting methodology, version intensity levels, how Nmap's `nmap-service-probes` database works, why version detection is critical for exploit matching. |
| **Syntax** | `sudo nmap -sV <target>`. `sudo nmap -sV --version-intensity 9 <target>` (maximum probing). `sudo nmap -sV --version-all <target>` (try every probe). |
| **Real-World Scenario** | After finding open ports, you need to know WHAT is running. "Port 80 is open" is less useful than "Apache httpd 2.4.7 on Ubuntu" — the version tells you which exploits to research. |
| **Expected Output** | Service name and version for each open port. Compare results with and without `--version-intensity` to see how deeper probing reveals more information. |
| **Common Mistakes** | Not using `-sV` at all (just seeing port numbers without service info). Not understanding that `-sV` sends additional probes (it's not passive). Using `--version-intensity 0` (only grabs banners, misses services that don't send banners automatically). Blindly trusting version output (services can be configured to lie about their version). |

---

### Task 2.5 — OS Detection

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Identify the target's operating system using TCP/IP stack fingerprinting. Understand how Nmap detects the OS and why results are sometimes uncertain. |
| **Skills Learned** | TCP/IP stack fingerprinting concept (different OSes implement TCP slightly differently), OS detection accuracy factors, why Nmap shows percentage confidence, CPE (Common Platform Enumeration) strings. |
| **Syntax** | `sudo nmap -O <target>`. `sudo nmap -O --osscan-guess <target>` (show best guesses even when uncertain). |
| **Real-World Scenario** | Determines whether a target is Windows or Linux (affects exploitation strategy, privilege escalation paths, and available tools). |
| **Expected Output** | OS family, version, and confidence percentage. CPE string. Network distance (hop count). |
| **Common Mistakes** | Trusting OS detection blindly (it can be wrong, especially with custom kernels or firewalls). Not understanding that OS detection requires at least one open and one closed port to work accurately. Running OS detection against a fully firewalled host (no useful data). |

---

### Task 2.6 — UDP Scanning

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Scan UDP ports and understand why UDP scanning is fundamentally different from TCP scanning: slower, less reliable, but essential for finding services like DNS, SNMP, DHCP, TFTP, and NTP. |
| **Skills Learned** | UDP protocol behavior (no handshake, no guaranteed response), why UDP scans are slow (waiting for timeouts), ICMP port unreachable as the only reliable "closed" indicator, combining UDP with version detection for better accuracy. |
| **Syntax** | `sudo nmap -sU --top-ports 50 <target>` (top 50 UDP ports). `sudo nmap -sU -sV -p 53,67,69,111,123,137,161,162,500,514,2049 <target>` (targeted with version detection). |
| **Real-World Scenario** | SNMP (port 161) with a default community string is one of the most common findings on internal networks. DNS (port 53) may allow zone transfers. NFS (port 2049) may expose shares. None of these are found without UDP scanning. |
| **Expected Output** | List of open/open\|filtered UDP ports. Understanding that "open\|filtered" means Nmap got no response (could be open or firewalled). |
| **Common Mistakes** | Scanning all 65535 UDP ports (takes hours — use `--top-ports` or target specific ports). Not combining `-sU` with `-sV` (version detection helps distinguish "open" from "open\|filtered"). Skipping UDP scans entirely (you miss critical services like SNMP). |

---

### Task 2.7 — Default Script Scan (NSE)

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Run Nmap's default NSE scripts (`-sC`) and understand what additional intelligence they provide beyond basic port/service detection. Learn the script categories: safe, intrusive, vuln, exploit, discovery, auth, brute, etc. |
| **Skills Learned** | NSE (Nmap Scripting Engine) architecture, default script behavior, script categories and their risk levels, how scripts provide actionable intelligence (anonymous FTP, SSL certificate info, SMB signing, etc.). |
| **Syntax** | `sudo nmap -sC <target>` (default scripts). `sudo nmap -sV -sC <target>` (version + default scripts — the most common combination). `nmap --script-help default` (list all default scripts). |
| **Real-World Scenario** | Default scripts reveal immediate wins: anonymous FTP access, SSH host keys, HTTP titles, SMB OS discovery, SSL certificate details. This is the scan that turns port numbers into actionable findings. |
| **Expected Output** | Script output under each port showing additional information. Examples: `ftp-anon: Anonymous FTP login allowed`, `http-title: Apache2 Ubuntu Default Page`, `ssl-cert: Subject:`. |
| **Common Mistakes** | Not using `-sC` (missing critical default intelligence). Confusing `-sC` with `--script vuln` (default scripts are safe; vuln scripts are more intrusive). Not reading script output carefully — it often reveals the first exploit path. |

---

### Task 2.8 — The Professional Scan Workflow

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 45 min

| Field | Detail |
|:---|:---|
| **Objective** | Learn the standard professional Nmap workflow: (1) discover hosts, (2) fast port scan all TCP, (3) targeted version + script scan on open ports, (4) targeted UDP scan. This avoids the mistake of running one giant slow scan. |
| **Skills Learned** | Efficient scanning methodology, why splitting scans is faster and more reliable than one monolithic scan, real-world time management during engagements. |
| **Syntax** | Step 1: `sudo nmap -sn 192.168.1.0/24 -oA discovery`. Step 2: `sudo nmap -sS -p- -T4 <target> -oA tcp-all`. Step 3: `sudo nmap -sV -sC -p <open-ports-from-step2> <target> -oA tcp-detailed`. Step 4: `sudo nmap -sU -sV --top-ports 50 <target> -oA udp-top50`. |
| **Real-World Scenario** | Every professional pentester uses this workflow. It's faster because Step 2 quickly finds open ports without the overhead of version detection, and Step 3 focuses version/script detection only on open ports. |
| **Expected Output** | Four sets of scan output files. A clean, merged service inventory. Understanding of why this approach takes less total time than `nmap -sV -sC -p- <target>`. |
| **Common Mistakes** | Running `nmap -A -p- <target>` as a single scan (extremely slow — combines OS detection, version detection, scripts, and traceroute across all 65535 ports). Not separating port discovery from service detection. Forgetting UDP entirely. |

---

### Task 2.9 — Timing Templates & Performance

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand Nmap's timing templates (`-T0` through `-T5`) and how they affect scan speed, accuracy, and detection risk. |
| **Skills Learned** | Timing template internals (parallelism, probe timeout, retry count), the speed/accuracy/stealth triangle, when to use each template, custom timing with `--min-rate` and `--max-rate`. |
| **Syntax** | `-T0` (paranoid — 5 min between probes), `-T1` (sneaky), `-T2` (polite), `-T3` (normal, default), `-T4` (aggressive — recommended for CTFs/labs), `-T5` (insane — may miss ports). `--min-rate 1000` (send at least 1000 packets/sec). |
| **Real-World Scenario** | Labs/CTFs: use `-T4`. Internal pentest with permission: `-T4`. External pentest with IDS concern: `-T2` or `-T3`. Red team engagement: `-T1` or custom timing. |
| **Expected Output** | Comparison of scan times using `-T3` vs `-T4` vs `-T5` on the same target. Note any ports missed at higher speeds. |
| **Common Mistakes** | Using `-T5` and missing open ports (packets get dropped). Using `-T0` unnecessarily (a full scan takes days). Not understanding that `-T4` is perfectly fine for authorized testing. |

---

### Task 2.10 — Target Specification Methods

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Master all the ways to specify targets in Nmap: single IP, CIDR ranges, hyphenated ranges, comma-separated lists, input files, and exclusions. |
| **Skills Learned** | CIDR notation, efficient target specification, using target lists for large engagements, excluding sensitive hosts from scans. |
| **Syntax** | Single: `nmap 192.168.1.10`. CIDR: `nmap 192.168.1.0/24`. Range: `nmap 192.168.1.1-50`. List: `nmap 192.168.1.1,2,3,10`. File: `nmap -iL targets.txt`. Exclude: `nmap 192.168.1.0/24 --exclude 192.168.1.1`. Exclude file: `--excludefile no-scan.txt`. |
| **Real-World Scenario** | Client gives you a scope document with IP ranges and exclusions. You need to scan exactly what's in scope and nothing else. Wrong target specification = out-of-scope scanning = legal liability. |
| **Expected Output** | Scans running against exactly the intended targets. Verification via scan output that exclusions are honored. |
| **Common Mistakes** | Scanning a /16 when you meant /24 (65536 vs 256 hosts). Not using `--exclude` for sensitive systems (production databases, medical devices). Not reading the target list file format correctly (one target per line). |

---

# PHASE 3: INTERMEDIATE TECHNIQUES

---

### Task 3.1 — NSE Script Categories & Targeted Scripting

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 45 min

| Field | Detail |
|:---|:---|
| **Objective** | Use specific NSE script categories and individual scripts for targeted enumeration. Understand script categories: `auth`, `broadcast`, `brute`, `discovery`, `dos`, `exploit`, `external`, `fuzzer`, `intrusive`, `malware`, `safe`, `version`, `vuln`. |
| **Skills Learned** | Targeted script selection, combining scripts with wildcards, script arguments, reading script help, understanding script risk levels. |
| **Syntax** | `nmap --script vuln <target>` (all vulnerability scripts). `nmap --script "smb-enum-*" <target>` (all SMB enumeration scripts). `nmap --script http-enum,http-headers <target>` (specific scripts). `nmap --script smb-brute --script-args userdb=users.txt,passdb=pass.txt <target>` (with arguments). |
| **Real-World Scenario** | After finding SMB on port 445, run `smb-enum-shares`, `smb-enum-users`, `smb-os-discovery` to gather intelligence without needing separate tools. |
| **Expected Output** | Targeted script results showing detailed service information. Understanding of which scripts are safe vs intrusive. |
| **Common Mistakes** | Running `--script all` (includes dangerous scripts like `dos` and `exploit` — never do this in production). Not using `--script-help <script>` before running an unfamiliar script. Not providing required script arguments (some scripts need credentials or wordlists). |

---

### Task 3.2 — Vulnerability Scanning with NSE

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Nmap's vulnerability detection scripts to identify known CVEs on discovered services. Understand the difference between Nmap's vuln scanning and dedicated vulnerability scanners (Nessus, OpenVAS). |
| **Skills Learned** | NSE vuln category scripts, `vulners` script (checks CVE databases), `vulscan` script (extended vulnerability matching), Nmap vs dedicated vulnerability scanners. |
| **Syntax** | `nmap --script vuln <target>` (built-in vuln scripts). `nmap --script vulners -sV <target>` (CVE lookup based on version strings). `nmap --script smb-vuln-ms17-010 <target>` (specific vulnerability check like EternalBlue). |
| **Real-World Scenario** | Quick vulnerability triage during a pentest when you don't have access to Nessus. Checking for specific high-severity vulnerabilities (EternalBlue, BlueKeep) across a network. |
| **Expected Output** | CVE identifiers associated with discovered service versions. Specific vulnerability confirmations (VULNERABLE / NOT VULNERABLE). |
| **Common Mistakes** | Treating Nmap vuln scanning as a replacement for Nessus/OpenVAS (Nmap checks fewer vulnerabilities). Not combining with `-sV` (vuln scripts need version information). Trusting negative results (Nmap may not have a script for every vulnerability). |

---

### Task 3.3 — Aggressive Scan & Combined Flags

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand the `-A` flag (enables OS detection, version detection, script scanning, and traceroute simultaneously) and when combining it with `-p-` is appropriate vs wasteful. |
| **Skills Learned** | Flag composition, understanding that `-A` is equivalent to `-O -sV -sC --traceroute`, performance trade-offs of combined scans, when all-in-one scans are appropriate. |
| **Syntax** | `sudo nmap -A <target>` (aggressive scan on top 1000 ports). `sudo nmap -A -p- <target>` (aggressive scan on ALL ports — very slow). |
| **Real-World Scenario** | Acceptable for CTF challenges with one target. Not recommended for real engagements with many targets — too slow. The split workflow (Task 2.8) is always more efficient. |
| **Expected Output** | Complete scan with OS, versions, scripts, and traceroute in one output. Timing comparison with the split workflow approach. |
| **Common Mistakes** | Using `-A -p-` on large networks (extremely slow). Using `-A` when you only need version detection (unnecessary overhead). Not understanding that `-A` includes traceroute (adds time with minimal security value in most cases). |

---

### Task 3.4 — Firewall & IDS Evasion Techniques

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 45 min

| Field | Detail |
|:---|:---|
| **Objective** | Learn Nmap's built-in evasion techniques for bypassing firewalls and IDS/IPS systems. Understand which techniques work against which defenses. |
| **Skills Learned** | Packet fragmentation (`-f`), decoy scanning (`-D`), source port manipulation (`--source-port`), idle/zombie scanning (`-sI`), custom TTL, data length randomization. |
| **Syntax** | Fragment packets: `sudo nmap -f <target>`. Decoys: `sudo nmap -D RND:10 <target>`. Source port 53 (looks like DNS): `sudo nmap --source-port 53 <target>`. Idle scan: `sudo nmap -sI <zombie-host> <target>`. |
| **Real-World Scenario** | Red team engagement where the target's IDS triggers alerts on standard scans. Bypassing firewall rules that allow traffic from port 53 (DNS) or port 80 (HTTP). |
| **Expected Output** | Successful scan results using evasion techniques where standard scans were blocked or detected. Understanding of which technique bypasses which defense. |
| **Common Mistakes** | Using evasion in a lab/CTF (unnecessary and slows scanning). Not understanding that modern IDS easily detects most evasion techniques. Using decoys with SYN scans (only works if decoy IPs are alive on the network). Idle scanning with a host that has unpredictable IP ID sequences. |

---

### Task 3.5 — Nmap Output Parsing & Automation

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | Parse Nmap output using grep, awk, and Python scripts. Extract specific information (open ports, service versions, hostnames) for feeding into other tools. |
| **Skills Learned** | Grepable output parsing, XML parsing with `xmlstarlet` or Python's `xml.etree`, building tool chains (Nmap → parser → next tool), automating multi-target workflows. |
| **Syntax** | Grepable: `grep "open" scan.gnmap | awk '{print $2}'` (extract IPs with open ports). `grep "/open/" scan.gnmap | awk -F'[ /]' '{print $5}'` (extract open port numbers). XML: `xmlstarlet sel -t -v "//port[@state='open']/@portid" scan.xml`. Python: `import xml.etree.ElementTree as ET`. |
| **Real-World Scenario** | Scanning 500 hosts, then extracting all hosts with port 445 open for targeted SMB enumeration. Building a list of all web servers for Burp Suite or Nikto processing. |
| **Expected Output** | Clean extracted lists of IPs, ports, and services from Nmap output. A simple Bash script that scans a network and generates a target list for the next tool. |
| **Common Mistakes** | Manually reading through thousands of lines of output instead of parsing. Not using `-oG` (grepable format is designed for exactly this use case). Writing complex parsers when simple grep/awk chains work fine. |

---

### Task 3.6 — Scanning Through Proxies & Pivots

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Nmap through SOCKS proxies (proxychains) and SSH tunnels to scan internal networks from a pivot host. Understand the limitations. |
| **Skills Learned** | Pivoting concepts, proxychains configuration, why only `-sT` works through proxies, SSH dynamic port forwarding (`-D`), scanning internal networks you can't directly reach. |
| **Syntax** | `ssh -D 1080 user@pivot-host` (create SOCKS proxy). Edit `/etc/proxychains4.conf` to use `socks5 127.0.0.1 1080`. `proxychains nmap -sT -Pn -p 22,80,445 <internal-target>`. |
| **Real-World Scenario** | You've compromised a host in the DMZ and need to scan the internal network. You set up a SOCKS proxy through the compromised host and scan internal IPs through it. |
| **Expected Output** | Scan results for internal hosts accessed through the proxy. Understanding of why `-sT -Pn` is required (no raw sockets through proxies, and ICMP ping doesn't work). |
| **Common Mistakes** | Using `-sS` through proxychains (fails — raw sockets can't traverse SOCKS). Not using `-Pn` (host discovery probes fail through proxies). Scanning too many ports through a proxy (very slow — target specific ports). |

---

### Task 3.7 — Ndiff: Comparing Scan Results Over Time

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Use `ndiff` to compare two Nmap scans taken at different times. Identify new hosts, new ports, changed services, and disappeared services. |
| **Skills Learned** | Network change detection, baseline comparison methodology, continuous monitoring with Nmap, why defenders schedule regular scans and diff the results. |
| **Syntax** | `ndiff scan-before.xml scan-after.xml`. Automated: create a cron job running `nmap -sV -oX /scans/scan-$(date +%F).xml <target>` and diff against the previous scan. |
| **Real-World Scenario** | Monthly network inventory assessment: comparing this month's scan to last month's to identify newly deployed services, removed hosts, or changed configurations. |
| **Expected Output** | Ndiff output showing `+` (new) and `-` (removed) entries. Documentation of what changed. |
| **Common Mistakes** | Comparing scans with different flags (results differ due to scan methodology, not actual changes). Not using XML format for ndiff (it requires XML input). Not baselining before changes occur (you need a "before" scan to compare against). |

---

# PHASE 4: ADVANCED USAGE

---

### Task 4.1 — Custom NSE Script Development

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 60 min

| Field | Detail |
|:---|:---|
| **Objective** | Read, understand, and modify an existing NSE script. Then write a simple custom NSE script. Understand the NSE API (host, port, and networking libraries). |
| **Skills Learned** | Lua programming basics, NSE API structure, script categories and rules, how Nmap scripts interact with services, extending Nmap's capabilities for specific engagement needs. |
| **Practical Exercise** | Read `/usr/share/nmap/scripts/http-title.nse` and understand its structure. Modify it to also extract the server header. Write a simple script that connects to a port and checks if a specific banner string is present. |
| **Expected Output** | A working custom NSE script that you can run with `--script /path/to/your/script.nse`. Understanding of the NSE script structure (description, categories, portrule/hostrule, action). |
| **Common Mistakes** | Trying to write complex scripts without first reading existing simple ones. Not understanding the portrule (determines which ports the script runs against). Not testing scripts in a lab before using in production. |

---

### Task 4.2 — IPv6 Scanning

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Scan IPv6 targets with Nmap. Understand why IPv6 scanning is different (no traditional network sweeping due to address space size) and the techniques used instead. |
| **Skills Learned** | IPv6 address formats in Nmap, `-6` flag usage, IPv6 host discovery challenges, multicast-based discovery, why IPv6 often has different firewall rules than IPv4. |
| **Syntax** | `sudo nmap -6 <ipv6-address>`. `sudo nmap -6 --script targets-ipv6-multicast-echo <interface>` (discover IPv6 hosts via multicast). |
| **Expected Output** | Scan results for IPv6 targets. Comparison with IPv4 scan results for the same host (often different ports are open on IPv6). |
| **Common Mistakes** | Ignoring IPv6 entirely (many hosts have IPv6 enabled with different, often less restrictive, firewall rules). Trying to sweep IPv6 subnets like IPv4 (the address space is too large). |

---

### Task 4.3 — Masscan + Nmap Combination Workflow

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Masscan for ultra-fast port discovery across large networks, then feed the results into Nmap for detailed service and script analysis. This is the professional workflow for large-scope engagements. |
| **Skills Learned** | Masscan usage, the speed vs depth trade-off, combining tools for efficiency, why Masscan finds ports and Nmap identifies services. |
| **Syntax** | `sudo masscan -p1-65535 192.168.1.0/24 --rate 10000 -oL masscan-results.txt`. Parse results and feed into Nmap: `nmap -sV -sC -p <ports-from-masscan> <hosts-from-masscan> -oA detailed-scan`. |
| **Expected Output** | Masscan completes a full-port scan of a /24 in seconds. Nmap provides detailed service analysis on discovered open ports. |
| **Common Mistakes** | Using Masscan's rate too high on small networks (overwhelms the target and misses ports). Not feeding Masscan results into Nmap (Masscan alone gives no service information). Running Masscan without authorization (it generates massive traffic volumes). |

---

### Task 4.4 — Nmap for Web Application Discovery

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Nmap's HTTP-specific NSE scripts to enumerate web applications, directories, technologies, and vulnerabilities before switching to dedicated web tools (Burp Suite, Nikto). |
| **Skills Learned** | HTTP-specific NSE scripts, web technology detection, HTTP method enumeration, web application discovery at scale. |
| **Syntax** | `nmap --script http-enum <target>` (directory/file enumeration). `nmap --script http-methods <target>` (allowed HTTP methods). `nmap --script http-title,http-headers,http-server-header <target>` (basic fingerprinting). `nmap --script http-shellshock --script-args uri=/cgi-bin/status <target>` (specific vuln check). |
| **Expected Output** | Web application directory listing. HTTP methods allowed. Technology stack identification. Any detected web vulnerabilities. |
| **Common Mistakes** | Using Nmap as a web vulnerability scanner (it's a good first pass but Burp Suite / Nikto are far more thorough). Not targeting the correct port (web apps on non-standard ports like 8080, 8443, 8888). |

---

### Task 4.5 — Idle (Zombie) Scanning

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| Field | Detail |
|:---|:---|
| **Objective** | Perform an idle scan using a third-party "zombie" host. Understand the IP ID side-channel technique that allows scanning without sending any packets from your own IP to the target. |
| **Skills Learned** | IP ID sequence prediction, side-channel attacks, truly anonymous scanning, finding suitable zombie hosts, understanding why this is the stealthiest Nmap scan type. |
| **Syntax** | Find zombie: `nmap --script ipidseq <candidate-zombie>` (look for "Incremental" IP ID). Idle scan: `sudo nmap -sI <zombie-ip> <target>`. |
| **Expected Output** | Port scan results attributed to the zombie host's IP, not yours. Understanding of the three-way IP ID inference: (1) probe zombie's IP ID, (2) send spoofed SYN to target from zombie's IP, (3) probe zombie's IP ID again — if it incremented by 2, the port is open. |
| **Common Mistakes** | Using a zombie with unpredictable IP IDs (scan fails). Not understanding the technique conceptually (it's one of the most elegant scanning techniques). Using this in CTFs (unnecessary complexity). |

---

### Task 4.6 — Performance Tuning for Large Networks

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Optimize Nmap for scanning large networks (thousands of hosts) efficiently without missing results. Tune parallelism, timeouts, and retry counts. |
| **Skills Learned** | `--min-hostgroup`, `--max-hostgroup` (scan hosts in parallel groups), `--min-parallelism`, `--max-parallelism` (concurrent probes), `--host-timeout` (skip slow hosts), `--max-retries` (reduce retries for speed). |
| **Syntax** | `sudo nmap -sS -p- --min-rate 5000 --max-retries 2 --host-timeout 5m -T4 -iL large-target-list.txt -oA large-scan`. |
| **Expected Output** | Scan completion in reasonable time for large networks. Understanding of the accuracy trade-offs for each tuning parameter. |
| **Common Mistakes** | Setting `--max-retries 0` (misses ports on congested networks). Setting `--host-timeout` too low (skips hosts that are alive but slow to respond). Not monitoring scan progress (`--stats-every 30s`). |

---

# PHASE 5: INTEGRATION WITH OTHER TOOLS

---

### Task 5.1 — Nmap → Metasploit Integration

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Import Nmap scan results into the Metasploit Framework database. Use Metasploit to search for exploits based on discovered services. |
| **Workflow** | `nmap -sV -sC -oX scan.xml <target>` → `msfconsole` → `db_import scan.xml` → `hosts` → `services` → `vulns` → `search type:exploit name:<service>`. |
| **Expected Output** | Metasploit database populated with hosts, ports, and services from your Nmap scan. Exploit candidates listed for discovered services. |

---

### Task 5.2 — Nmap → Searchsploit Pipeline

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Feed Nmap's service version output directly into `searchsploit` for automated exploit candidate identification. |
| **Workflow** | `nmap -sV -oX scan.xml <target>` → `searchsploit --nmap scan.xml`. This cross-references every detected service version against the local Exploit-DB database. |
| **Expected Output** | Exploit candidates for each service version found. Understanding of how to triage results (many will be false positives due to partial version matches). |

---

### Task 5.3 — Nmap → Nikto/Gobuster Web Pipeline

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Extract web server targets from Nmap results and feed them into web scanning tools (Nikto, Gobuster, Burp Suite). |
| **Workflow** | `grep "80/open\|443/open\|8080/open" scan.gnmap | awk '{print $2}'` → save to `web-targets.txt` → `nikto -h web-targets.txt` or `for ip in $(cat web-targets.txt); do gobuster dir -u http://$ip -w wordlist.txt; done`. |
| **Expected Output** | Automated web scanning pipeline from network discovery to web enumeration. |

---

### Task 5.4 — Nmap → Hydra Credential Testing Pipeline

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Extract hosts running authentication services (SSH, FTP, Telnet, RDP, SMB) from Nmap results and feed them into Hydra for credential testing. |
| **Workflow** | `grep "22/open" scan.gnmap | awk '{print $2}' > ssh-targets.txt` → `hydra -L users.txt -P passwords.txt -M ssh-targets.txt ssh`. |
| **Expected Output** | Automated credential testing against all SSH servers discovered by Nmap. |

---

### Task 5.5 — Nmap in Bash Automation Scripts

- [ ] **Completed** · ⭐⭐⭐⭐ Intermediate-Advanced · ⏱️ 45 min

| Field | Detail |
|:---|:---|
| **Objective** | Write a comprehensive Bash script that automates the full Nmap workflow: discovery → port scan → service detection → vulnerability check → output parsing → report generation. |
| **Practical Exercise** | Create a script that takes a target as input and performs: (1) ping sweep, (2) full TCP port scan, (3) version + script detection on open ports, (4) top 50 UDP scan, (5) vulnerability scan, (6) parses results into a clean markdown report. |
| **Expected Output** | A reusable scanning automation script. A clean markdown report generated from scan results. |

---

# PHASE 6: PRACTICAL LABS

---

### Lab 6.1 — Beginner: Map Metasploitable 2

- [ ] **Completed** · ⭐⭐ Beginner · ⏱️ 60 min

| Field | Detail |
|:---|:---|
| **Scenario** | You've been given the IP of a single target in a lab environment. Create a complete service inventory. |
| **Objective** | Discover all open TCP/UDP ports, identify every service and version, and create a professional service inventory document. |
| **Setup** | Metasploitable 2 VM on Host-Only network. |
| **Success Criteria** | All 23+ open TCP ports identified with correct service versions. At least 3 UDP services identified. Service inventory table complete with risk ratings. |

---

### Lab 6.2 — Intermediate: Subnet Discovery & Triage

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 90 min

| Field | Detail |
|:---|:---|
| **Scenario** | You're on an internal network assessment. Discover all hosts on the /24 subnet, identify services, and prioritize targets for exploitation. |
| **Objective** | Map the entire subnet, triage targets by attack surface (most services exposed = highest priority), and create an attack plan. |
| **Setup** | Multiple VMs on the same subnet (Metasploitable 2, OWASP BWA, a Windows VM if available). |
| **Success Criteria** | All hosts discovered. Top 3 targets prioritized with justification. Attack plan document created. |

---

### Lab 6.3 — Advanced: Firewall Bypass Scanning

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 90 min

| Field | Detail |
|:---|:---|
| **Scenario** | A target is behind a firewall that blocks standard scans. Use evasion techniques to discover open ports. |
| **Objective** | Identify open ports despite firewall filtering. Document which evasion techniques worked and which didn't. |
| **Setup** | Configure `iptables` on a target VM to block SYN scans but allow traffic from specific source ports. |
| **Success Criteria** | Open ports discovered using at least two evasion techniques. Filter bypass documented with evidence. |

---

### Lab 6.4 — Advanced: Scan-to-Exploit Pipeline

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 120 min

| Field | Detail |
|:---|:---|
| **Scenario** | Full pipeline exercise: Nmap scan → exploit research → Metasploit exploitation → root access. No prior knowledge of the target. |
| **Objective** | Use only Nmap output to identify an exploitable service, research the vulnerability, and exploit it. |
| **Setup** | Metasploitable 2 (any service). |
| **Success Criteria** | Root shell obtained using a vulnerability discovered entirely through Nmap scanning. Complete documentation of the scan-to-shell pipeline. |

---

### Lab 6.5 — Expert: Write a Custom Nmap Automation Framework

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 180 min

| Field | Detail |
|:---|:---|
| **Scenario** | Build a custom reconnaissance automation tool using Nmap as the engine. |
| **Objective** | Create a Python or Bash tool that: accepts a target range, performs staged scanning, parses results, identifies high-value targets, and generates a prioritized HTML or Markdown report. |
| **Setup** | Any lab network. |
| **Success Criteria** | Working automation script. Clean report output. Handling of edge cases (down hosts, filtered ports, timeouts). |

---

# PHASE 7: REAL PENETRATION TESTING METHODOLOGY

---

### Task 7.1 — Nmap in the PTES Framework

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Map Nmap's capabilities to each PTES phase: Intelligence Gathering (host discovery), Vulnerability Analysis (version detection + vuln scripts), Exploitation (no direct role, but informs exploit selection), Post-Exploitation (internal network scanning from compromised hosts), Reporting (scan evidence). |
| **Expected Output** | A mapping document showing where Nmap fits in each PTES phase with specific commands for each. |

---

### Task 7.2 — Nmap in the Cyber Kill Chain

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Map Nmap to the Lockheed Martin Cyber Kill Chain phases: Reconnaissance (external scanning), Delivery (no role), Exploitation (informs, doesn't execute), Installation (no role), C2 (detecting C2 channels via network scans), Actions on Objectives (internal network mapping during post-exploitation). |

---

### Task 7.3 — Nmap Limitations & When to Use Other Tools

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Document Nmap's limitations and identify when other tools are better choices. |
| **Key Limitations** | Slow for full-port scanning across many hosts (use Masscan). Not a web application scanner (use Burp Suite). Limited vulnerability detection compared to Nessus/OpenVAS. Version detection can be spoofed. Not designed for credential brute-forcing (use Hydra). OS detection requires specific conditions. No active exploitation capability. |

---

### Task 7.4 — Professional Nmap Reporting Standards

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Learn how to present Nmap findings in a professional penetration test report. Transform raw scan output into client-ready finding descriptions. |
| **Practical Exercise** | Take raw Nmap output and create: (1) an executive summary of findings, (2) a network diagram based on scan results, (3) a service inventory table, (4) specific findings with CVSS scores for risky services (e.g., "Anonymous FTP Access Allowed — CVSS 5.3"). |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — Blind Network Assessment

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 120 min

| Field | Detail |
|:---|:---|
| **Scenario** | You're dropped onto an unknown network with only your Kali VM. Discover the network range, find all hosts, identify all services, prioritize targets, and produce a professional report. No hints, no prior information. |
| **Success Criteria** | Network range identified. All hosts discovered. Complete service inventory. Top 3 attack targets prioritized with rationale. Professional report delivered. |

---

### Challenge 8.2 — Speed Assessment

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Scenario** | You have exactly 30 minutes to scan a /24 network and produce a prioritized target list. Optimize your scanning workflow for maximum coverage in minimum time. |
| **Success Criteria** | All live hosts found. Open ports identified on every host. Service versions on critical ports. Attack plan document produced — all within 30 minutes. |

---

### Challenge 8.3 — Teach Nmap

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 60 min

| Field | Detail |
|:---|:---|
| **Scenario** | Prepare and deliver a 20-minute Nmap tutorial for a junior colleague. Cover: what Nmap does, the professional workflow, scan types, output formats, and common mistakes. |
| **Success Criteria** | Clear, organized presentation. Live demonstration. Ability to answer questions about scan mechanics, port states, and timing. |

---

### Challenge 8.4 — Automation Portfolio Project

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 180 min

| Field | Detail |
|:---|:---|
| **Scenario** | Create a portfolio-worthy Nmap automation project: a Python/Bash tool that accepts a scope, performs intelligent scanning, and generates a professional report. Publish on GitHub. |
| **Success Criteria** | Clean code with documentation. Error handling. Report generation. README with usage instructions. Suitable for showing in job interviews. |

---

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
