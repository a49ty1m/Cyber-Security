# Scanning — Detailed Notes (Module 6) 🔎

**Overview:** Network scanning is the active phase of intelligence gathering used to identify live hosts, open ports, running services, OS versions, and potential vulnerabilities. It converts raw network visibility into an actionable attack surface map for further testing.

**Key idea:** “Knowing your enemy is winning half the war.”

---

## Quick‑Revision Checklist ✅

- Identify scope and authorization.
- Discover live hosts (ICMP/ARP).
- Enumerate open TCP/UDP ports.
- Fingerprint services and OS.
- Correlate results to vulnerabilities.
- Validate findings with safe probes.
- Document evidence and next steps.

---

## Mini Glossary (Flags & Scan Types)

**TCP Flags:**
- **SYN:** Start connection
- **ACK:** Acknowledge
- **RST:** Reset/close
- **FIN:** Finish
- **URG:** Urgent data
- **PSH:** Push data immediately

**Scan Types:**
- **SYN scan (`-sS`):** Half‑open stealth scan
- **Connect scan (`-sT`):** Full TCP handshake
- **FIN/NULL/Xmas (`-sF`, `-sN`, `-sX`):** Inverse flag scans
- **ACK scan (`-sA`):** Firewall filtering discovery
- **UDP scan (`-sU`):** No handshake, relies on ICMP errors

---

## Which Scan Should I Use? (Decision Table)

| Goal | Recommended Scan | Why |
|---|---|---|
| Quick inventory (TCP) | `-sS` | Fast and stealthy |
| No root privileges | `-sT` | Works without raw sockets |
| Firewall rules check | `-sA` | Maps filtered vs unfiltered |
| UDP services | `-sU` | Only reliable UDP discovery |
| OS fingerprinting | `-O` / `-A` | Uses stack signatures |
| Service versions | `-sV` | Banner and probe‑based |

---

## Basics of Scanning

- Network scanning is performed actively against a target.
- It can be done internally (intranet) or from the Internet.
- Scanning helps locate vulnerable points that can be exploited.

---

## Objectives of Network Scanning

- Discover live hosts, IP addresses, and open ports.
- Identify operating systems and system architecture.
- Discover services running on hosts.
- Identify vulnerabilities in live hosts.

---

## Scanning Technology Chart

### **Scanning Techniques**

**Scanning TCP Network Services:**
- **Open TCP Scanning Methods**
  - TCP Connect / Full Open Scan (-sT)
  - Vanilla TCP Scanning

- **Stealth TCP Scanning Methods**
  - Half-open Scan (SYN Scan / -sS)
  - Stealth Port Scanning
  
  - Inverse TCP Flag Scanning
    - Xmas Scan (-sX)
    - FIN Scan (-sF)
    - NULL Scan (-sN)
  
  - ACK Flag Probe Scanning (-sA)
  - Firewall Rule Determination

- **Third Party and Spoofed TCP Scanning Methods**
  - IDLE / IP ID Header Scanning (-sI)
    - *Advantages:* Ultimate stealth (uses zombie host), attacker IP never appears in logs, can bypass IP-based access controls
    - *Disadvantages:* Requires finding suitable zombie host, complex to set up, slower than direct scans, zombie must have predictable IP ID sequence
  - Zombie Host Scanning
  - Decoy Scanning (-D)
    - *Advantages:* Hides real scanner IP among decoys, makes tracing back difficult, useful for evading IDS correlation
    - *Disadvantages:* Does not provide anonymity (real IP still visible), decoy IPs may trigger alerts, blocked by egress filtering

**Scanning UDP Network Services:**
- **UDP Scanning Methods**
  - UDP Scan (-sU)
  - ICMP Port Unreachable Detection
  - Service Detection

**Host Discovery & Enumeration:**
- **Ping Sweep** - ICMP Echo probes to range
- **ARP Scan** - ARP request to identify live hosts
  - *Advantages:* Cannot be blocked by firewalls (Layer 2), extremely fast, very reliable on local networks, works even if host blocks all IP traffic
  - *Disadvantages:* Only works on local subnet, limited to same broadcast domain, no use for remote targets
- **Banner Grabbing** - Service version enumeration
- **OS Fingerprinting** - Stack behavior analysis

**Evasion & Speed Control:**
- **Fragmentation** - Fragment probes to bypass filters
- **Timing Templates** - Slow (-T0/-T1) to IDS evasion
- **Decoy Scanning** - Mix real scan with dummy sources
- **Source Port Manipulation** - Use port 53/80 for bypass

---

## Scanning Methodology (Module 6)

1. **Checking for live systems**
2. **Understanding TCP 3‑way handshake**
3. **Port scanning to find open ports**
4. **Service fingerprinting and OS detection**
5. **Vulnerability scanning and mapping**

---

## 1. Checking for Live Systems

### Ping Scan

- Send ICMP ECHO requests to hosts.
- Live hosts respond with ICMP ECHO replies.
- Useful to determine whether ICMP is allowed through firewalls.

**Advantages:**
- Quick way to check if a single host is alive
- Very low resource consumption
- Simple and widely supported
- No special privileges needed for basic ping

**Disadvantages:**
- Blocked by many firewalls and security devices
- Host may be alive but not responding to ICMP
- Limited information (only alive/dead status)
- Can be logged and trigger alerts

### Ping Sweep

- Sends ICMP ECHO requests to multiple hosts in a range.
- Live hosts respond with ICMP ECHO replies.
- Subnet mask calculators help determine host counts.
- Builds an inventory of live systems in a subnet.

**Advantages:**
- Fast and efficient for host discovery
- Low network overhead
- Simple to implement and understand
- Works across routed networks
- Easy to script and automate

**Disadvantages:**
- ICMP is often blocked by firewalls
- Many hosts are configured to ignore ICMP requests
- High false-negative rate in secured environments
- Can miss hosts with ICMP disabled
- Easily detected by network monitoring tools

**Examples (authorized use only):**
- `nmap -sn 192.168.1.0/24`
- `fping -a -g 192.168.1.0/24`

---

## 2. TCP 3‑Way Handshake & Flags

### TCP Flags

- **URG (Urgent):** Data should be processed immediately
- **FIN (Finish):** No more transmissions
- **RST (Reset):** Resets a connection
- **PSH (Push):** Send all buffered data immediately
- **ACK (Acknowledgment):** Acknowledges receipt of a packet
- **SYN (Synchronize):** Initiates a connection between hosts

### Three‑Way Handshake

**SYN → SYN/ACK → ACK** establishes a TCP session.

---

## 3. Port Scanning & Port States

To exploit a system, attackers must identify services listening on publicly accessible ports.

**Port States:**
- **Open:** Actively accepting TCP connections, UDP datagrams, or SCTP associations
- **Closed:** Responds to probes but no application is listening
- **Filtered:** Packet filtering prevents determination (firewall/router)

---

## 4. Port Scanning Methodology & Tools

### Core Tools

- **Nmap:** Network inventory, service monitoring, OS detection, and firewall discovery
- **hping2/hping3:** Packet crafting, firewall testing, path MTU discovery, advanced traceroute, OS fingerprinting, uptime guessing

---

## 5. Scanning Techniques

### TCP Connect / Full Open Scan (`-sT`)

- Completes full TCP three‑way handshake
- Ends with a RST packet to tear down the connection
- Does not require super user privileges

**Advantages:**
- No root/admin privileges required
- Works on any system with socket API
- Highly accurate results (definitive open/closed)
- Works through proxies and SOCKS

**Disadvantages:**
- Easily detected and logged by target systems
- Slower than SYN scan (full handshake overhead)
- Leaves connection traces in application logs
- More likely to trigger IDS/IPS alerts

### Stealth / Half‑Open Scan (`-sS`)

- Sends SYN, receives SYN/ACK if open
- Sends RST before handshake completes
- If RST received from server → port is closed

**Advantages:**
- Faster than full connect scan
- Less likely to be logged (no full connection established)
- Can scan thousands of ports quickly
- Bypasses some older logging mechanisms
- Reliable results for most scenarios

**Disadvantages:**
- Requires root/admin privileges (raw sockets)
- Modern IDS can still detect SYN floods
- May be blocked by stateful firewalls
- Can crash older or unstable systems
- Leaves half-open connections that may timeout

### Inverse TCP Flag Scans (`-sF`, `-sN`)

- **FIN scan:** FIN flag set
- **NULL scan:** No flags set
- No response usually indicates open; RST indicates closed

**Advantages:**
- Can bypass non-stateful firewalls and packet filters
- More stealthy than SYN scan against some systems
- Avoids SYN-based IDS signatures
- Useful for firewall rule mapping

**Disadvantages:**
- Does not work against Windows systems (always sends RST)
- Cannot distinguish open from filtered ports reliably
- Slower due to waiting for timeouts
- Less accurate results overall
- Requires root/admin privileges

### Xmas Scan (`-sX`)

- Sends FIN, URG, and PSH flags set
- Used to infer OS stack behavior

**Advantages:**
- Can evade some non-stateful firewalls
- Useful for OS fingerprinting (stack behavior differs)
- Bypasses SYN-based packet filters
- Less common, may avoid signature-based IDS

**Disadvantages:**
- Does not work against Windows/Cisco/BSDI/IBM systems
- Generates unusual flag combinations (easy to detect if monitored)
- Cannot distinguish open from filtered ports
- Requires root/admin privileges
- Slower due to timeout reliance

### ACK Flag Probe Scan (`-sA`)

- Sends ACK probes and analyzes RST responses
- **TTL < 64** for RST implies open (per module guidance)
- **WINDOW value non‑zero** in RST implies open
- No response implies filtered

**Advantages:**
- Excellent for mapping firewall rules (filtered vs unfiltered)
- Can determine if firewall is stateful or stateless
- Hard to log since it appears as part of existing connection
- Useful for discovering firewall misconfigurations

**Disadvantages:**
- Cannot determine if a port is open or closed
- Only reveals filtering status
- Requires root/admin privileges
- Modern stateful firewalls block unsolicited ACK packets
- Results may be inconsistent across different firewall types

### UDP Scan (`-sU`)

- No three‑way handshake for UDP
- **Open UDP port:** Often no response
- **Closed UDP port:** ICMP port unreachable (type 3, code 3)
- Many spyware and Trojans use UDP ports

**Advantages:**
- Only reliable method to discover UDP services
- Identifies DNS, SNMP, DHCP, NTP, and other UDP services
- Essential for comprehensive port coverage
- Can reveal services invisible to TCP scans

**Disadvantages:**
- Very slow (ICMP rate limiting by most systems)
- High false-negative rate (open ports often don't respond)
- Hard to distinguish open from filtered
- Requires root/admin privileges
- Results are less reliable than TCP scans
- Can be blocked if ICMP unreachable messages are filtered

---

## Detection Signals by Scan Type (Defender View)

- **SYN Scan:** High SYN rate, many half‑open connections
- **Connect Scan:** Many completed TCP handshakes from a single source
- **FIN/NULL/Xmas:** Unusual flag combinations in logs
- **ACK Scan:** RST responses to ACK probes, often uniform across ports
- **UDP Scan:** Bursts of ICMP type 3 code 3 responses

---

## Limitations & False Positives

- **Filtered vs Closed:** Firewalls may drop probes, making closed ports appear filtered.
- **UDP Silence:** Open UDP services often do not respond, causing false negatives.
- **Rate Limits:** IDS/IPS rate‑limiting can hide live ports.
- **Stateful Firewalls:** Can affect ACK/FIN/NULL/Xmas accuracy.
- **NAT/Proxies:** May obscure real host responses and OS fingerprints.

---

## 6. Banner Grabbing & OS Fingerprinting

### Banner Grabbing

Determines OS or software version running on a remote system.

**Why it matters:** OS identification helps map vulnerabilities and exploit paths.

### Active Banner Grabbing

- Send crafted packets and compare responses to a database
- Responses differ across OSes due to TCP/IP stack variations

**Advantages:**
- Accurate and detailed service/OS information
- Works against most standard services
- Provides specific version numbers for vulnerability matching
- Quick turnaround for results

**Disadvantages:**
- Easily detected and logged
- Can trigger IDS/IPS alerts
- Banners can be spoofed or modified
- Reveals attacker's presence on the network

### Passive Banner Grabbing

- **Error messages:** Reveal server type, OS, and SSL tool
- **Traffic sniffing:** Analyze captured packets for OS hints
- **Page extensions:** `.aspx` suggests IIS/Windows, etc.

**Advantages:**
- Completely undetectable (no packets sent)
- Cannot be blocked by firewalls
- No direct interaction with target
- Works against any observable traffic

**Disadvantages:**
- Requires network access to sniff traffic
- May take longer to gather useful data
- Information may be incomplete or outdated
- Depends on available traffic (passive observation only)
- May require privileged access for packet capture

---

## 7. Evading IDS and Firewalls (Awareness Only)

- Fragment IP packets
- Spoof IP address and sniff responses
- Use source routing (if possible)
- Use proxy servers or compromised hosts to launch scans

---

## 8. Vulnerability Scanning

Identifies vulnerabilities and weaknesses for exploitation:

- Network vulnerabilities
- Open ports and running services
- Application and service vulnerabilities
- Application and service configuration errors

---

## 9. Network Visual Mapping

Visual mapping builds a network diagram to understand logical and physical paths.

**Network Discovery Tools:**
- LANSurveyor
- Network Topology Mapper
- OpManager
- NetworkView

---

## 10. Countermeasures

### Port Scanning Countermeasures

- Configure firewall and IDS rules to detect and block probes
- Regularly run port scanning tools internally to validate detection
- Ensure routing/filtering mechanisms cannot be bypassed via source ports or source routing
- Configure anti‑scanning and anti‑spoofing rules
- Keep router, IDS, and firewall firmware updated
- Use custom rule sets to lock down network and block unwanted ports
- Filter ICMP messages (inbound ICMP types and outbound ICMP type 3 unreachable)
- Perform periodic TCP/UDP scans and ICMP probes against your own IP ranges

### Banner Grabbing Countermeasures

- Disable or change banners
- Display false banners to mislead attackers
- Turn off unnecessary services to reduce information disclosure
- Use ServerMask or similar tools to modify server banners
- Use httpd.conf directives to change banner information
- Set `ServerSignature Off` in httpd.conf

---

### Lab‑friendly commands & quick reference (Authorized use only)

- Host discovery (ping sweep): `nmap -sn 192.168.1.0/24`
- Full open TCP scan: `nmap -sT -p 1-1024 target`
- Stealth SYN scan: `nmap -sS -p- -T3 target`
- UDP scan (common ports): `nmap -sU -p 53,67,123 target`
- Basic banner grab: `nc -v target 80` then `HEAD / HTTP/1.0`
- hping3 SYN probe: `hping3 -S -p 80 target`

---

## Detection & Operational Tips for Defenders

- Alert on high SYN rates, half‑open connections, and bursty port probes
- Correlate events across sensors to detect low‑and‑slow scans
- Regularly test IDS/IPS signatures and update firewall rule sets
- Continuously patch systems and remove unnecessary services

---

## Embedded slides & diagrams 🖼️

Below are selected slides from *Module 6 (Scanning)* — diagrams and slide summaries that visually illustrate the concepts in the notes.

- **Title / Overview (Slide 1):**

  ![Module 6 - Overview](images/module6-01.png)
  *Caption: High-level definition and objectives of scanning.*

- **Scanning techniques (Slide ~7):**

  ![Scanning techniques](images/module6-07.png)
  *Caption: Overview of TCP/UDP scan categories and common approaches.*

- **TCP scan behaviors (Slide ~19):**

  ![TCP scanning behaviors](images/module6-19.png)
  *Caption: SYN/Connect/Xmas/FIN/NULL scan differences and how they infer port states.*

- **Banner grabbing & fingerprinting (Slide ~30):**

  ![Banner grabbing](images/module6-30.png)
  *Caption: Active vs passive banner grabbing and OS fingerprinting notes.*

- **Evading IDS / Firewalls (Slide ~35):**

  ![Evasion techniques](images/module6-35.png)
  *Caption: Packet fragmentation, spoofing, and pivot/proxy strategies for bypass testing.*

- **Network visual mapping (Slide ~39):**

  ![Network mapping](images/module6-39.png)
  *Caption: Visual mapping tools and the value of topology diagrams for reconnaissance.*

- **Countermeasures summary (Slide ~43):**

  ![Countermeasures](images/module6-43.png)
  *Caption: Practical countermeasures for port scanning and banner-based information leakage.*

---

*Notes expanded from Module 6 (Scanning) on 2026-01-30.*