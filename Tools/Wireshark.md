# 🦈 Wireshark: Complete Mastery Checklist

> **What is Wireshark?** Wireshark is the world's most widely used network protocol analyzer. It captures live network traffic and decodes it into human-readable format, allowing you to inspect every packet — every header, every payload, every handshake — at any layer of the OSI model.
>
> **Why does it exist?** Networks are invisible by default. Wireshark makes the invisible visible. It lets you see exactly what devices are saying to each other, debug network problems, verify security controls, detect malicious activity, and prove vulnerabilities with packet-level evidence.
>
> **When to use it:** Traffic analysis, protocol debugging, credential sniffing (on insecure protocols), verifying encryption, analyzing attacks, incident response, forensics, validating scan results, understanding how exploits work at the wire level.
>
> **When to avoid it:** When you need to modify traffic in transit (use Burp Suite or mitmproxy). When you need real-time alerting (use an IDS like Snort/Suricata). When you need automated large-scale analysis (use Zeek/Bro). When capturing on production networks without authorization (same legal rules as any network tool).
>
> **What mastering Wireshark unlocks:** Deep protocol understanding that makes you a better attacker AND defender. The ability to prove findings with evidence. Network forensics skills. The ability to debug any network issue. Understanding of how every tool you use (Nmap, Metasploit, Burp) actually works on the wire.

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md) · [🐧 Metasploitable 2 Lab](../Lab/Metasploitable_2/TASK_LIST.md) · [🌐 OWASP BWA Lab](../Lab/OWASP_Broken_WebApps/TASK_LIST.md)

| Recon & Scanning | Exploitation | Post-Exploitation | Web & Traffic |
|:-----------------|:-------------|:-------------------|:--------------|
| [🗺️ Nmap](Nmap.md) | [💀 Metasploit](Metasploit_Framework.md) | [🐉 LinPEAS](LinPEAS.md) | [🕷️ Burp Suite](Burp_Suite.md) |
| [🔌 Netcat](Netcat.md) | [🐍 Impacket](Impacket.md) | [🩸 BloodHound](BloodHound.md) | **🦈 Wireshark** (you are here) |
| | [🔓 Hydra](Hydra.md) | [🔥 Hashcat](Hashcat.md) | |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals & Interface | 6 | 3–4 hours |
| 2 | Core Capture & Display Filters | 8 | 5–7 hours |
| 3 | Intermediate Analysis | 7 | 5–7 hours |
| 4 | Advanced Analysis | 5 | 5–7 hours |
| 5 | Tool Integration | 4 | 3–4 hours |
| 6 | Practical Labs | 5 | 6–10 hours |
| 7 | Methodology & Forensics | 4 | 3–4 hours |
| 8 | Mastery Challenges | 4 | 6–10 hours |
| | **Total** | **43** | **~36–53 hours** |

**Prerequisites:** TCP/IP fundamentals (OSI model, ports, protocols). Basic understanding of HTTP, DNS, ARP, TCP handshake. A lab network with traffic to capture.

**Alternatives:** tcpdump (CLI-based, lightweight, great for remote capture), tshark (Wireshark's CLI version), Zeek/Bro (network security monitoring), NetworkMiner (forensics-focused), Arkime/Moloch (full PCAP indexing at scale).

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — Understand Wireshark's Role in Security

- [ ] **Completed** · ⭐ Beginner · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Explain why Wireshark is essential for both offensive and defensive security. Understand it's a passive analysis tool — it captures and displays traffic but does not modify or inject packets. |
| **Skills Learned** | Packet analysis concept, passive vs active tools, where Wireshark fits in incident response, forensics, pentesting, and network debugging. Wireshark across PTES phases: Reconnaissance (sniffing credentials), Vulnerability Analysis (verifying insecure protocols), Post-Exploitation (capturing traffic from compromised hosts). |
| **Practical Exercise** | List five offensive and five defensive use cases for Wireshark. Map each to a pentest phase or IR phase. |
| **Expected Output** | Written document showing use cases for both red team and blue team perspectives. |
| **Common Mistakes** | Thinking Wireshark can modify packets (it can't — use Scapy or Ettercap for that). Thinking Wireshark is only for defenders (attackers use it extensively). Not understanding that Wireshark requires access to the network segment you want to capture (you can only see traffic that reaches your interface). |

---

### Task 1.2 — Interface Selection & Promiscuous Mode

- [ ] **Completed** · ⭐ Beginner · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Select the correct capture interface and understand promiscuous mode (captures all traffic on the segment, not just traffic addressed to your machine). |
| **Skills Learned** | Network interface identification, promiscuous vs normal mode, why you need promiscuous mode for security analysis, monitor mode for wireless (different from promiscuous). |
| **Practical Exercise** | Open Wireshark → identify your lab interface (look for the one with traffic activity graphs). Start a capture. Verify promiscuous mode is enabled: Edit → Preferences → Capture → check "Use promiscuous mode on all interfaces." |
| **Expected Output** | Capture running on the correct interface. Traffic from other devices visible (in a shared/hubbed network or with ARP spoofing). |
| **Common Mistakes** | Capturing on the wrong interface (loopback instead of eth0). Not enabling promiscuous mode (only seeing your own traffic). Not understanding that on switched networks, you only see broadcast traffic and your own traffic unless you ARP spoof or mirror a port. |

---

### Task 1.3 — Wireshark Interface Walkthrough

- [ ] **Completed** · ⭐ Beginner · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Navigate every panel of the Wireshark UI: Packet List (summary rows), Packet Details (protocol tree), Packet Bytes (hex dump), Display Filter bar, Capture Filter bar, Status Bar (packet counts), and coloring rules. |
| **Skills Learned** | UI fluency, understanding the three-pane layout, reading the protocol tree (Layer 2 → Layer 3 → Layer 4 → Layer 7), interpreting hex dumps, using coloring rules to spot anomalies. |
| **Practical Exercise** | Capture 60 seconds of lab traffic. Click on different packets and examine each pane. Expand every protocol layer in the Packet Details pane. Find the same bytes in the Hex Dump pane. Right-click a field → "Apply as Filter." |
| **Expected Output** | Comfortable navigation of all three panes. Ability to find any field in the protocol tree and correlate it to the hex dump. |
| **Common Mistakes** | Ignoring the Packet Bytes pane (it shows the raw truth — the other panes are Wireshark's interpretation). Not understanding the protocol tree hierarchy (Ethernet → IP → TCP → HTTP is Layer 2 → 3 → 4 → 7). Not using right-click → "Apply as Filter" (the fastest way to filter). |

---

### Task 1.4 — First Capture & Save

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Perform your first traffic capture, stop it, and save the file. Understand PCAP vs PCAPNG formats and when to use each. |
| **Skills Learned** | Starting/stopping captures, saving capture files, PCAP format (universal, compatible with all tools) vs PCAPNG (newer, supports annotations and multiple interfaces), file management. |
| **Practical Exercise** | Start a capture → generate traffic (ping, browse web, run Nmap scan) → stop capture → Save As `lab-capture-01.pcapng`. Also save as PCAP: File → Save As → select "Wireshark/tcpdump/... - pcap" format. |
| **Expected Output** | Two saved capture files (PCAPNG and PCAP). Understanding of when PCAPNG is better (annotations, multiple interfaces) and when PCAP is needed (compatibility with older tools). |
| **Common Mistakes** | Not saving captures (you will want to re-analyze later). Saving as PCAPNG when the target tool only supports PCAP. Capturing too long without filters (file becomes huge and unmanageable). |

---

### Task 1.5 — tshark: Command-Line Wireshark

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Use tshark (Wireshark's command-line equivalent) for headless captures on remote servers, automated analysis, and scripted processing. |
| **Skills Learned** | tshark capture syntax, display filters in CLI, field extraction with `-T fields -e`, why tshark is essential for capturing on servers without a GUI, piping tshark output into other tools. |
| **Practical Exercise** | Live capture: `sudo tshark -i eth0 -c 100`. With filter: `sudo tshark -i eth0 -f "port 80" -c 50`. Field extraction: `tshark -r capture.pcap -T fields -e ip.src -e ip.dst -e tcp.dstport`. Save to file: `sudo tshark -i eth0 -w /tmp/capture.pcap -c 1000`. |
| **Expected Output** | CLI-based capture and analysis output. Extracted fields piped into `sort | uniq -c | sort -rn` for frequency analysis. |
| **Common Mistakes** | Confusing capture filters (BPF syntax, applied during capture) with display filters (Wireshark syntax, applied after capture) — tshark uses `-f` for capture and `-Y` for display. Not using `-c` to limit packet count (capture runs forever). Not having root/sudo (required for live capture). |

---

### Task 1.6 — tcpdump for Remote Capture → Wireshark Analysis

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Capture traffic remotely using tcpdump (available on almost every Linux system), transfer the PCAP file, and analyze it in Wireshark. This is the standard workflow for analyzing traffic from servers. |
| **Skills Learned** | tcpdump capture syntax, remote capture workflow, PCAP file transfer, the tcpdump → Wireshark pipeline as the standard remote analysis pattern. |
| **Practical Exercise** | On target/server: `sudo tcpdump -i eth0 -w /tmp/remote-capture.pcap -c 500`. Transfer: `scp user@server:/tmp/remote-capture.pcap .`. Open in Wireshark: `wireshark remote-capture.pcap`. |
| **Expected Output** | PCAP captured remotely, transferred, and analyzed in Wireshark's GUI. |
| **Common Mistakes** | Forgetting `-w` (tcpdump prints to terminal by default — you need `-w` to save to file). Capturing without `-c` on a busy server (file grows to gigabytes quickly). Not having enough disk space on the remote server. |

---

# PHASE 2: CORE FEATURES — FILTERS & ANALYSIS

---

### Task 2.1 — Capture Filters (BPF Syntax)

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Apply Berkeley Packet Filter (BPF) capture filters to reduce capture volume. Capture filters are applied DURING capture — packets that don't match are never saved. |
| **Skills Learned** | BPF syntax, when to filter at capture time (high-traffic networks, specific protocols, long captures), the performance difference between capture and display filters. |
| **Syntax Examples** | Only HTTP: `tcp port 80`. Only DNS: `udp port 53`. Specific host: `host 192.168.1.10`. Exclude your IP: `not host 192.168.1.5`. Subnet: `net 192.168.1.0/24`. Combination: `host 192.168.1.10 and tcp port 80`. |
| **Real-World Scenario** | Capturing HTTP traffic on a busy network — without a capture filter, you get millions of irrelevant packets. With `tcp port 80`, you only capture what matters. |
| **Expected Output** | Focused captures containing only relevant traffic. Dramatically smaller file sizes compared to unfiltered captures. |
| **Common Mistakes** | Confusing capture filter syntax (BPF) with display filter syntax (Wireshark). Using `==` in capture filters (BPF uses `=` or just keywords). Filters too restrictive — missing related traffic (e.g., filtering only port 80 but missing the DNS lookup on port 53). Not being able to undo a capture filter (missed packets are gone forever). |

---

### Task 2.2 — Display Filters (Wireshark Syntax)

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 45 min

| Field | Detail |
|:---|:---|
| **Objective** | Master Wireshark's display filter language to isolate specific packets from a captured file. Display filters are applied AFTER capture — all packets are saved but only matching ones are shown. |
| **Skills Learned** | Display filter syntax (dot notation, comparison operators, logical operators), the difference between capture and display filters, building complex filter expressions, filter autocompletion. |
| **Essential Filters** | Protocol: `http`, `dns`, `tcp`, `arp`, `icmp`, `tls`. IP: `ip.addr == 192.168.1.10`, `ip.src == x`, `ip.dst == x`. Port: `tcp.port == 80`, `tcp.dstport == 443`. HTTP: `http.request.method == "GET"`, `http.response.code == 200`. DNS: `dns.qry.name contains "example"`. TCP flags: `tcp.flags.syn == 1`, `tcp.flags.reset == 1`. Negation: `!(arp or dns)`. Contains: `frame contains "password"`. |
| **Expected Output** | Ability to quickly isolate any traffic type from a large capture. A personal cheat sheet of your most-used display filters. |
| **Common Mistakes** | Using capture filter syntax in the display filter bar (e.g., `port 80` instead of `tcp.port == 80`). Not using `contains` for string searches (it's case-sensitive). Using `==` for IP addresses that appear in both src and dst (use `ip.addr ==` to match either direction). Overly complex filters when simple ones suffice. |

---

### Task 2.3 — Following TCP Streams

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Reconstruct complete TCP conversations using "Follow TCP Stream." This shows the full dialogue between client and server — the most powerful analysis feature in Wireshark. |
| **Skills Learned** | TCP stream concept (all packets in a single TCP connection), stream reconstruction, reading protocol conversations, identifying credentials in cleartext protocols, exporting stream data. |
| **Practical Exercise** | Capture an HTTP session (browse to a web page). Right-click any packet in the conversation → Follow → TCP Stream. Read the complete HTTP request/response conversation. Capture a Telnet login → Follow TCP Stream → observe the credentials in cleartext. |
| **Expected Output** | Complete HTTP conversation showing request headers, response headers, and body. Telnet session showing cleartext username and password. |
| **Common Mistakes** | Not following streams (looking at individual packets instead of the conversation). Not switching between ASCII and Hex view in the stream window. Not knowing that you can also follow UDP, TLS (if keys are available), and HTTP/2 streams. |

---

### Task 2.4 — Protocol Hierarchy & Statistics

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Wireshark's Statistics menu to get a high-level overview of captured traffic: protocol distribution, conversation pairs, endpoint statistics, and I/O graphs. |
| **Skills Learned** | Traffic profiling, protocol distribution analysis, identifying dominant protocols, spotting anomalies (unexpected protocols, unusual traffic volumes), statistical overview before deep analysis. |
| **Practical Exercise** | Open a capture → Statistics → Protocol Hierarchy (see percentage breakdown of all protocols). Statistics → Conversations → sort by bytes (find the heaviest talkers). Statistics → Endpoints (all unique IPs/MACs). Statistics → I/O Graphs (traffic volume over time). |
| **Expected Output** | Protocol hierarchy showing the percentage breakdown. Top talkers identified. Traffic timeline showing spikes or anomalies. |
| **Common Mistakes** | Diving into individual packets without first getting the statistical overview (always start with statistics to understand the big picture). Not sorting conversations by bytes (the heaviest conversations are often the most interesting). |

---

### Task 2.5 — Name Resolution & GeoIP

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Configure Wireshark's name resolution to translate IPs to hostnames, MAC addresses to vendor names, and ports to service names. Optionally add GeoIP databases for geographic location of IPs. |
| **Skills Learned** | DNS resolution in captures, MAC vendor lookup (OUI database), why resolution helps and when it hurts (performance on large captures), GeoIP for identifying traffic destinations. |
| **Practical Exercise** | View → Name Resolution → enable all three (MAC, Network, Transport). Notice IPs replaced with hostnames, MACs showing vendor prefixes. For GeoIP: Edit → Preferences → Name Resolution → MaxMind database paths. |
| **Expected Output** | Readable hostnames instead of IP addresses. Vendor names on MAC addresses (e.g., "VMware" reveals virtual machines). |
| **Common Mistakes** | Leaving resolution enabled on huge captures (slows Wireshark to a crawl with thousands of DNS lookups). Trusting resolved names blindly (DNS can be spoofed). Not enabling MAC resolution (missing easy identification of device vendors). |

---

### Task 2.6 — Coloring Rules & Custom Profiles

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand and customize Wireshark's coloring rules to visually highlight important traffic patterns. Create a custom profile for security analysis. |
| **Skills Learned** | Default coloring meanings (light green = TCP, light blue = UDP, black = TCP errors, red = bad checksum), creating custom rules, profile management for different analysis contexts. |
| **Practical Exercise** | View → Coloring Rules → examine each default rule. Create a custom rule: name "Cleartext Credentials," filter `telnet or ftp`, color bright red background. Create a security analysis profile: Edit → Configuration Profiles → New. |
| **Expected Output** | Custom coloring rules highlighting security-relevant traffic. A dedicated security analysis profile with optimized columns and filters. |
| **Common Mistakes** | Ignoring colors (they encode information — black rows usually indicate TCP problems). Creating too many custom rules (makes the display confusing). Not using profiles (switching between default and security-focused profiles saves time). |

---

### Task 2.7 — Exporting Objects & Files from Captures

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Extract transferred files from captured traffic: HTTP objects (images, downloads, HTML), SMB files, TFTP files, and DICOM images. This is a core forensics skill. |
| **Skills Learned** | File carving from network traffic, HTTP object export, SMB file extraction, evidence preservation, why this matters for forensics and incident response. |
| **Practical Exercise** | Capture HTTP traffic while downloading a file → File → Export Objects → HTTP → find and save the file. Repeat for SMB file transfers. Verify the extracted file matches the original (MD5 checksum). |
| **Expected Output** | Files successfully extracted from network captures. Verification that extracted files are intact and functional. |
| **Common Mistakes** | Not knowing this feature exists (one of Wireshark's most powerful capabilities). Trying to extract files from encrypted traffic (HTTPS/TLS — impossible without keys). Not verifying extracted file integrity. |

---

### Task 2.8 — Packet Searching & Marking

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Search for specific strings, hex patterns, or field values within captured packets. Mark important packets for reference. Add comments to packets for documentation. |
| **Skills Learned** | Packet searching (Edit → Find Packet), search types (display filter, hex value, string), packet marking (Ctrl+M), packet commenting, bookmarking important findings. |
| **Practical Exercise** | Search for the string "password" in packet bytes: Edit → Find Packet → String → "password." Mark all found packets (Ctrl+M). Add comments to key packets: right-click → Packet Comment. |
| **Expected Output** | Relevant packets located and marked. Comments added for documentation. Ability to navigate between marked packets. |
| **Common Mistakes** | Using display filters when string search is needed (display filters work on decoded fields; string search works on raw bytes). Not knowing Ctrl+M for marking (marks make it easy to jump between important packets). Case sensitivity in string searches (use "Case insensitive" option). |

---

# PHASE 3: INTERMEDIATE ANALYSIS

---

### Task 3.1 — TCP Handshake & Connection Analysis

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Identify and analyze TCP three-way handshakes (SYN → SYN-ACK → ACK), connection teardowns (FIN), and resets (RST). Understand what healthy and unhealthy connections look like. |
| **Skills Learned** | TCP state machine visualization, identifying successful connections, failed connections (RST), filtered ports (no response), half-open connections (SYN but no SYN-ACK), retransmissions indicating network issues. |
| **Practical Exercise** | Filter: `tcp.flags.syn == 1 && tcp.flags.ack == 0` (show all SYN packets — connection initiations). Run an Nmap SYN scan and capture simultaneously — see the half-open handshakes. |
| **Expected Output** | Identified handshakes for open ports (SYN → SYN-ACK → RST from Nmap). RST responses for closed ports. No response for filtered ports. |
| **Common Mistakes** | Not understanding that Nmap SYN scans send RST instead of ACK (that's the "stealth" — never completing the handshake). Confusing RST from the scanner (normal) with RST from the target (could indicate a firewall). |

---

### Task 3.2 — HTTP Traffic Analysis

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Analyze HTTP requests and responses in detail: methods, headers, status codes, cookies, POST data, and file transfers. Identify credentials, session tokens, and sensitive data transmitted over HTTP. |
| **Skills Learned** | HTTP protocol analysis, identifying authentication traffic, cookie extraction, POST body inspection, file download detection, why HTTP is a security risk (everything is visible). |
| **Practical Exercise** | Capture HTTP login traffic (DVWA login). Filter: `http.request.method == "POST"`. Follow the TCP stream → find the username and password in the POST body. Filter: `http.cookie contains "PHPSESSID"` → extract session cookies. |
| **Expected Output** | Credentials captured from HTTP login. Session cookies extracted. Demonstration of why HTTPS exists. |
| **Common Mistakes** | Trying to analyze HTTPS traffic the same way (it's encrypted — you need the server's private key or SSLKEYLOGFILE). Not expanding the HTTP layer in Packet Details (it shows parsed headers, not raw text). |

---

### Task 3.3 — DNS Traffic Analysis

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Analyze DNS queries and responses: identify resolved domains, detect DNS tunneling, spot DNS exfiltration, and identify unusual DNS behavior. |
| **Skills Learned** | DNS protocol structure (queries, responses, record types), detecting DNS tunneling (unusually long subdomain labels, high query volume), DNS cache poisoning indicators, identifying C2 domains. |
| **Practical Exercise** | Filter: `dns`. Examine query/response pairs. Filter for unusual TXT records: `dns.qry.type == 16`. Look for long subdomain names: `dns.qry.name matches ".*\..*\..*\..*\."` (more than 3 levels). Statistics → DNS → see query/response distribution. |
| **Expected Output** | DNS traffic profile showing normal resolution patterns. Identification of any anomalous DNS behavior (if present). |
| **Common Mistakes** | Ignoring DNS traffic (it reveals every domain the host contacted). Not correlating DNS queries with subsequent HTTP connections. Not recognizing DNS tunneling patterns (base64-encoded data in subdomain labels). |

---

### Task 3.4 — ARP Analysis & ARP Spoofing Detection

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Analyze ARP traffic to understand network topology and detect ARP spoofing (a common MITM attack technique). |
| **Skills Learned** | ARP protocol mechanics (who has this IP? → I have it, my MAC is...), normal ARP behavior, ARP spoofing indicators (duplicate IP-to-MAC mappings, gratuitous ARP floods), how to detect MITM attacks. |
| **Practical Exercise** | Filter: `arp`. Examine normal ARP request/response pairs. Look for Wireshark's built-in ARP alerts: Analyze → Expert Information → look for "Duplicate IP address" warnings. Filter for gratuitous ARP: `arp.opcode == 2 && arp.src.proto_ipv4 == arp.dst.proto_ipv4`. |
| **Expected Output** | Normal ARP traffic identified. Understanding of ARP spoofing detection indicators. |
| **Common Mistakes** | Dismissing ARP as "boring" (ARP spoofing is one of the most common network attacks). Not checking Expert Information for ARP anomalies (Wireshark detects them automatically). |

---

### Task 3.5 — TLS/SSL Handshake Analysis

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Analyze TLS handshakes to identify: TLS version, cipher suite negotiated, certificate details (CN, SAN, issuer, expiry), and potential weaknesses (old TLS versions, weak ciphers). |
| **Skills Learned** | TLS handshake structure (ClientHello → ServerHello → Certificate → KeyExchange → Finished), cipher suite interpretation, certificate analysis, identifying TLS downgrade attacks, JA3 fingerprinting concept. |
| **Practical Exercise** | Filter: `tls.handshake.type == 1` (ClientHello messages). Examine: TLS version, supported cipher suites, SNI (Server Name Indication — reveals the requested hostname even in encrypted traffic). Filter: `tls.handshake.type == 11` (Certificate messages — extract the server certificate). |
| **Expected Output** | TLS version and cipher suite for each connection identified. Server certificates extracted. SNI hostnames visible (even though the rest is encrypted). |
| **Common Mistakes** | Trying to decrypt TLS traffic without the private key (impossible without SSLKEYLOGFILE or the server's key). Not checking for TLS 1.0/1.1 (deprecated and insecure). Not extracting SNI (it reveals which website is being accessed even when the content is encrypted). |

---

### Task 3.6 — Decrypting TLS with SSLKEYLOGFILE

- [ ] **Completed** · ⭐⭐⭐⭐ Intermediate-Advanced · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Decrypt TLS traffic in Wireshark using pre-master secret keys logged by the browser. This is the primary method for analyzing encrypted web traffic in a controlled environment. |
| **Skills Learned** | SSLKEYLOGFILE environment variable, how browsers log TLS session keys, configuring Wireshark to use the key log file, the difference between this method and using server private keys. |
| **Practical Exercise** | Set environment variable: `export SSLKEYLOGFILE=/tmp/sslkeys.log`. Open browser and browse HTTPS sites. In Wireshark: Edit → Preferences → Protocols → TLS → "(Pre)-Master-Secret log filename" → `/tmp/sslkeys.log`. Capture HTTPS traffic → verify it's decrypted (you can see HTTP/2 frames inside TLS). |
| **Expected Output** | Decrypted HTTPS traffic visible in Wireshark showing HTTP headers, responses, and content inside TLS. |
| **Common Mistakes** | Setting SSLKEYLOGFILE after starting the browser (must be set before). File permissions preventing Wireshark from reading the key log. Not understanding that this only works for traffic from browsers that support SSLKEYLOGFILE (Chrome, Firefox — not curl by default). NEVER use this on production traffic without authorization. |

---

### Task 3.7 — Expert Information & Error Detection

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Wireshark's Expert Information system to quickly identify errors, warnings, and anomalies in captured traffic. |
| **Skills Learned** | Expert Information categories (Errors, Warnings, Notes, Chat), TCP retransmissions, duplicate ACKs, zero window events, RST floods, malformed packets, using Expert Info as a triage starting point. |
| **Practical Exercise** | Open a capture → Analyze → Expert Information. Sort by severity. Click on errors to jump to the offending packet. Common findings: TCP retransmissions (network congestion), RST packets (connection rejection), duplicate ACKs (packet loss). |
| **Expected Output** | Expert Information summary showing all anomalies. Understanding of what each error type indicates. |
| **Common Mistakes** | Ignoring Expert Information (it's the fastest way to find problems). Treating all warnings as critical (some are normal network behavior). Not correlating errors with specific conversations (a few retransmissions in a large capture may be normal). |

---

# PHASE 4: ADVANCED ANALYSIS

---

### Task 4.1 — Credential Extraction from Cleartext Protocols

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | Extract credentials from cleartext protocols: HTTP Basic/Form auth, FTP, Telnet, SMTP, POP3, IMAP. Understand why these protocols are security risks and what should replace them. |
| **Skills Learned** | Protocol-specific credential extraction, HTTP Basic auth (Base64 decoded from Authorization header), FTP USER/PASS, Telnet character-by-character capture, SMTP AUTH, professional evidence documentation. |
| **Practical Exercise** | Capture Telnet login to Metasploitable 2 → Follow TCP Stream → extract credentials. Capture FTP login → filter `ftp.request.command == "USER" or ftp.request.command == "PASS"`. Capture HTTP Basic auth → filter `http.authorization`. |
| **Expected Output** | Credentials extracted from at least three different cleartext protocols. Screenshots as evidence. Remediation recommendations (use SSH, SFTP, HTTPS). |
| **Common Mistakes** | Only checking HTTP for credentials (FTP, Telnet, SMTP are equally exposed). Not Base64-decoding HTTP Basic auth headers. Missing Telnet credentials (they're sent character-by-character, not as a single string — Follow TCP Stream to see the full conversation). |

---

### Task 4.2 — Network Forensics: Attack Reconstruction

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| Field | Detail |
|:---|:---|
| **Objective** | Given a PCAP file of an attack, reconstruct the entire attack timeline: reconnaissance (port scans), exploitation (exploit delivery), C2 communication, and data exfiltration. |
| **Skills Learned** | Attack timeline reconstruction, pattern recognition (scan patterns, exploit signatures, C2 beacons), evidence chain documentation, forensic report writing from PCAP evidence. |
| **Practical Exercise** | Capture your own Nmap scan + exploit + reverse shell against Metasploitable 2. Then analyze the PCAP: identify the scan phase, the exploitation attempt, the reverse shell establishment, and any post-exploitation commands. |
| **Expected Output** | Complete attack timeline with timestamps, source/destination IPs, ports, and a narrative description of each phase. |
| **Common Mistakes** | Starting with individual packets instead of the statistical overview (Protocol Hierarchy first, then drill down). Not establishing a timeline (timestamp correlation is critical in forensics). Missing the C2 channel (reverse shells are persistent TCP connections that look different from normal web traffic). |

---

### Task 4.3 — Wireshark Display Filter Expressions & Macros

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Build complex display filter expressions using logical operators, field comparisons, membership operators, and display filter macros for reusable analysis patterns. |
| **Skills Learned** | Advanced filter syntax: `in` operator, `matches` (regex), field slicing (`tcp.payload[0:4]`), display filter macros, creating filter buttons for one-click analysis. |
| **Syntax Examples** | Ports in range: `tcp.port in {80 443 8080 8443}`. Regex hostname: `http.host matches ".*admin.*"`. Payload starts with specific bytes: `tcp.payload[0:4] == 47:45:54:20` (GET in hex). Non-standard DNS: `dns && udp.port != 53`. |
| **Expected Output** | Complex filters that precisely isolate security-relevant traffic patterns. Custom filter buttons for common security checks. |
| **Common Mistakes** | Over-complicating filters when simpler ones work. Not using `in` for port lists (more readable than chaining `||`). Not using `matches` for regex patterns (more powerful than `contains`). |

---

### Task 4.4 — Wireless Traffic Analysis (802.11)

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Capture and analyze Wi-Fi traffic in monitor mode. Identify SSIDs, connected clients, authentication types, and deauthentication attacks. |
| **Skills Learned** | Monitor mode configuration, 802.11 frame types (management, control, data), beacon frame analysis, deauth detection, WPA handshake capture for offline cracking. |
| **Practical Exercise** | (Requires monitor-mode capable adapter) Set monitor mode: `sudo airmon-ng start wlan0`. Capture: `sudo wireshark -i wlan0mon`. Filter beacons: `wlan.fc.type_subtype == 0x08`. Filter deauths: `wlan.fc.type_subtype == 0x0c`. |
| **Expected Output** | List of visible SSIDs from beacon frames. Client device MAC addresses. Any deauthentication activity detected. |
| **Common Mistakes** | Not switching to monitor mode (normal mode only captures traffic for your connected network). Not having a compatible wireless adapter (not all adapters support monitor mode). Confusing management frames with data frames. |

---

### Task 4.5 — Lua Scripting & Custom Dissectors

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 60 min

| Field | Detail |
|:---|:---|
| **Objective** | Write a simple Wireshark Lua dissector to decode a custom protocol. Understand the dissector architecture and when custom dissectors are needed. |
| **Skills Learned** | Wireshark Lua API, protocol dissector creation, tree construction, field registration, when custom dissectors are needed (proprietary protocols, CTF challenges, IoT analysis). |
| **Practical Exercise** | Write a basic Lua dissector that identifies packets on a specific port and decodes a simple custom header format. Load it: Edit → Preferences → Protocols → Lua → add script path. |
| **Expected Output** | Custom protocol decoded and displayed in Wireshark's protocol tree. |
| **Common Mistakes** | Not testing the dissector incrementally (build one field at a time). Lua syntax errors crashing Wireshark (test with tshark first). Overcomplicating the dissector before the basics work. |

---

# PHASE 5: TOOL INTEGRATION

---

### Task 5.1 — Wireshark + Nmap: Verifying Scan Behavior

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| **Workflow** | Capture traffic while running Nmap → Analyze the scan packets to verify scan type, timing, and behavior. Filter: `ip.addr == <target> && tcp.flags.syn == 1 && tcp.flags.ack == 0` to see all SYN probes sent by Nmap. Verify SYN scan sends RST (not ACK) after receiving SYN-ACK. |

---

### Task 5.2 — Wireshark + Burp Suite: Comparing Proxy vs Wire

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| **Workflow** | Capture traffic while using Burp Suite → Compare what Burp shows (HTTP-level) with what Wireshark shows (packet-level). See the TLS termination at Burp, the re-encrypted connection to the server, and understand the MITM proxy architecture. |

---

### Task 5.3 — Wireshark + Metasploit: Exploit Traffic Analysis

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| **Workflow** | Capture while running a Metasploit exploit → Analyze the exploit payload delivery, shellcode execution trigger, and reverse shell establishment. See exactly what the exploit sends and how the target responds. |

---

### Task 5.4 — tshark + Bash: Automated Analysis Pipeline

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| **Workflow** | Use tshark for field extraction → pipe into Bash for processing. Example — extract all DNS queries: `tshark -r capture.pcap -T fields -e dns.qry.name -Y "dns.flags.response == 0" | sort | uniq -c | sort -rn | head -20`. Extract all HTTP hosts: `tshark -r capture.pcap -T fields -e http.host -Y "http" | sort -u`. |

---

# PHASE 6: PRACTICAL LABS

---

### Lab 6.1 — Beginner: Capture Your Own Nmap Scan

- [ ] **Completed** · ⭐⭐ Beginner · ⏱️ 45 min

| **Scenario** | Run an Nmap scan against Metasploitable 2 while capturing in Wireshark. Analyze the scan at the packet level. |
| **Success Criteria** | SYN scan packets identified. Open ports verified by SYN-ACK responses. Closed ports verified by RST responses. Service version probes identified. |

---

### Lab 6.2 — Intermediate: Credential Harvesting from Cleartext

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 60 min

| **Scenario** | Log into Telnet, FTP, and HTTP (DVWA) on Metasploitable 2. Capture all traffic. Extract credentials from the capture file using only Wireshark. |
| **Success Criteria** | Credentials extracted from all three protocols. Evidence screenshots. Written remediation recommendations (SSH, SFTP, HTTPS). |

---

### Lab 6.3 — Advanced: Attack Reconstruction

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 90 min

| **Scenario** | Perform a complete attack against Metasploitable 2 (scan → exploit → reverse shell → post-exploitation) while capturing. Give the PCAP to a partner (or analyze it yourself a week later) and reconstruct the attack from the PCAP alone. |
| **Success Criteria** | Complete attack timeline reconstructed from the PCAP. Every phase identified with timestamps and evidence. |

---

### Lab 6.4 — Advanced: Malicious PCAP Analysis (CTF-Style)

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 60 min

| **Scenario** | Download a malicious PCAP from public CTF repositories (e.g., Malware Traffic Analysis, SANS Holiday Hack). Analyze it to identify: the infection vector, C2 traffic, exfiltrated data, and IOCs (Indicators of Compromise). |
| **Success Criteria** | Infection vector identified. C2 server IP/domain extracted. At least three IOCs documented (IPs, domains, file hashes). |

---

### Lab 6.5 — Expert: Decrypt and Analyze HTTPS Traffic

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 60 min

| **Scenario** | Configure SSLKEYLOGFILE, capture HTTPS browsing traffic, decrypt it in Wireshark, and extract all HTTP/2 requests, responses, and cookies from an encrypted session. |
| **Success Criteria** | TLS traffic decrypted in Wireshark. HTTP/2 frames visible. Cookies and session tokens extracted. Documentation of the decryption setup. |

---

# PHASE 7: METHODOLOGY & FORENSICS

---

### Task 7.1 — Wireshark in Incident Response

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| **Objective** | Document the IR workflow: receive alert → capture traffic → analyze in Wireshark → identify IOCs → contain → document evidence. Understand chain of custody for PCAP evidence. |

---

### Task 7.2 — Wireshark in the Kill Chain (Defender View)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| **Objective** | Map Wireshark detection capabilities to each Kill Chain phase: Reconnaissance (detect port scans), Delivery (detect exploit payloads), C2 (detect beaconing patterns), Exfiltration (detect data leaving the network). |

---

### Task 7.3 — Wireshark Limitations

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| **Key Limitations** | Cannot modify packets in transit (use Scapy/Ettercap). Cannot decrypt TLS without keys. Only captures traffic visible to the capture interface (switch limitations). GUI struggles with very large captures (>100MB — use tshark). Not real-time alerting (use Snort/Suricata for IDS). No automated threat detection (manual analysis tool). |

---

### Task 7.4 — PCAP Evidence for Reports

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| **Objective** | Learn to use Wireshark captures as evidence in penetration test and incident response reports. Export specific packets, annotate streams, create timeline visualizations, and reference PCAP files in your documentation. |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — Identify the Attack

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 90 min

| **Scenario** | Analyze a provided PCAP (from Malware Traffic Analysis exercises or your own lab) and produce a complete forensic report: timeline, attack vector, IOCs, impacted systems, and remediation. |

---

### Challenge 8.2 — Live Traffic Monitoring Sprint

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 60 min

| **Scenario** | Monitor live traffic on your lab network for 30 minutes. Identify all active hosts, all protocols in use, any cleartext credentials, any anomalous behavior, and produce a network health assessment. |

---

### Challenge 8.3 — Build a tshark Analysis Toolkit

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 120 min

| **Scenario** | Create a collection of tshark one-liners and Bash scripts that automatically extract: top talkers, DNS queries, HTTP hosts, cleartext credentials, TLS versions/ciphers, and potential IOCs from any PCAP file. |

---

### Challenge 8.4 — Teach Wireshark

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 60 min

| **Scenario** | Prepare a 20-minute Wireshark workshop. Cover: interface overview, capture/display filters, following streams, credential extraction, and attack analysis. Include a live demo with a prepared PCAP. |

---

# 📋 FINAL COMPETENCY MATRIX

| Competency | Self-Assessment |
|:---|:---:|
| Can capture traffic on the correct interface | ☐ |
| Can write capture and display filters fluently | ☐ |
| Can follow and reconstruct TCP streams | ☐ |
| Can extract credentials from cleartext protocols | ☐ |
| Can analyze TCP handshakes and identify anomalies | ☐ |
| Can analyze TLS handshakes and extract certificate info | ☐ |
| Can decrypt TLS traffic using SSLKEYLOGFILE | ☐ |
| Can export files from captured traffic | ☐ |
| Can use tshark for CLI analysis and automation | ☐ |
| Can reconstruct an attack from a PCAP file | ☐ |
| Can produce forensic evidence from captures | ☐ |
| Can teach Wireshark to another person | ☐ |

---

## 🎯 Interview Questions

1. What is the difference between a capture filter and a display filter?
2. How do you extract credentials from a Telnet capture?
3. What information is visible in a TLS ClientHello even though the traffic is encrypted?
4. How would you detect ARP spoofing in a Wireshark capture?
5. How do you decrypt HTTPS traffic in Wireshark?
6. What is the Follow TCP Stream feature and when do you use it?
7. How would you analyze a PCAP to reconstruct a network attack?
8. What are Wireshark's limitations compared to an IDS like Snort?
9. How do you use tshark for automated field extraction?
10. How would you identify DNS tunneling in a capture?
