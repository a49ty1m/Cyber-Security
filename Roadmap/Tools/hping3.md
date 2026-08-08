# 🏓 hping3: Complete Reference

> **What is hping3?** hping3 is a command-line TCP/IP packet assembler and analyzer. Unlike ping (which only sends ICMP echo requests), hping3 can craft and send TCP, UDP, ICMP, and RAW-IP packets with full control over every header field — source IP, port, flags, TTL, data payload. It is the Swiss Army knife of low-level network testing: port scanning, firewall rule testing, SYN flood DoS, traceroute with different protocols, and fragmentation testing.
>
> **When to use it:** Testing firewall rules (can ICMP get through? What about TCP on port 443?). Generating DoS traffic in lab environments for defensive testing. Custom traceroutes when ICMP is blocked but TCP isn't. Verifying network filtering behavior. TCP/IP packet crafting when Scapy is overkill for a simple task.
>
> **Tier 4 Reminder:** Understand what it does and how to run basic tests. You do not need to master the full feature set.
>
> **Roadmap Phase:** Phase 10 (DoS Awareness and Network Stress Testing)

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals | 4 | 1–2 hours |
| 2 | Core Usage | 5 | 2–3 hours |
| 3 | Network Testing | 4 | 2–3 hours |
| 4 | DoS Testing (Lab) | 3 | 1–2 hours |
| 5 | Mastery Check | 2 | 1 hour |
| | **Total** | **18** | **~7–11 hours** |

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — What hping3 Does

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Core Capability** | Send arbitrary TCP/UDP/ICMP/RAW-IP packets. Control every header field manually. Receive and display responses. |
| **vs. Nmap** | Nmap does discovery and service detection as a workflow. hping3 sends individual, fully-crafted packets for precision testing. |
| **vs. Scapy** | Scapy: scriptable, complex packet crafting in Python. hping3: quick CLI one-liners for common tasks. |
| **Use Cases** | Firewall testing. SYN flood (lab). Traceroute via TCP. Host discovery when ICMP is blocked. ACK scan to map firewall rules. |

---

### Task 1.2 — Installation

- [ ] **Completed** · ⭐ Beginner · ⏱️ 5 min

| Field | Detail |
|:---|:---|
| **Install** | `apt install hping3`. Pre-installed on Kali. Requires root for raw socket access. |
| **Verify** | `hping3 --version`. |

---

### Task 1.3 — Packet Modes

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **TCP (default)** | `hping3 target` — sends TCP SYN to port 0 by default. |
| **ICMP** | `hping3 -1 target` — sends ICMP echo (like ping). |
| **UDP** | `hping3 -2 target -p 53` — sends UDP to port 53. |
| **RAW-IP** | `hping3 -0 target` — raw IP packet. |

---

### Task 1.4 — Key Flags

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Port** | `-p 80` — destination port. |
| **Count** | `-c 5` — send 5 packets then stop. |
| **Interval** | `-i u1000` — send every 1000 microseconds (1ms). `-i 1` — every 1 second. |
| **Fast** | `-f` — fast mode (faster than `-i u1`). |
| **Flood** | `--flood` — send as fast as possible. |
| **Source IP** | `-a 1.2.3.4` — spoof source IP (requires root, doesn't affect responses). |
| **TCP Flags** | `-S` SYN, `-A` ACK, `-F` FIN, `-R` RST, `-P` PSH, `-U` URG. |
| **Verbose** | `-V` — verbose output. |

---

# PHASE 2: CORE USAGE

---

### Task 2.1 — Basic ICMP Ping

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Command** | `hping3 -1 -c 5 192.168.1.1`. |
| **Output** | Shows RTT per packet. Same as regular ping but with more control. |
| **When Useful** | When you need to send ICMP with specific TTL, size, or rate. `hping3 -1 --ttl 5 target` — set TTL to 5 (like traceroute step). |

---

### Task 2.2 — TCP SYN Ping (Host Discovery When ICMP Blocked)

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Command** | `hping3 -S -p 80 -c 3 target`. |
| **What Happens** | Sends TCP SYN to port 80. If host is up: SYN-ACK (port open) or RST (port closed — but host responded). If no response: host down or firewall drops. |
| **Use Case** | Discover hosts in environments where ICMP ping is blocked by firewall. |

---

### Task 2.3 — TCP Port Scan

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Scan Range** | `hping3 -S --scan 1-1000 target` — SYN scan ports 1–1000. |
| **Open Ports** | SYN-ACK response → open. RST → closed. No response → filtered. |
| **vs. Nmap** | Nmap is better for port scanning. Use hping3 scan for: bypassing some IDS signatures, or when you need fine-grained control over timing/flags. |

---

### Task 2.4 — ACK Scan (Firewall Rule Mapping)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Command** | `hping3 -A -p 80 target`. |
| **Logic** | An ACK packet is not a new connection. Stateless firewalls pass ACK through if port 80 is open. Stateful firewalls drop unsolicited ACKs. |
| **Result** | RST received: port is not filtered (firewall allows through). No response: port is filtered by firewall. |
| **Use Case** | Map which ports a firewall blocks vs. passes. Bypass simple ACL-based firewalls. |

---

### Task 2.5 — Custom Traceroute

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **ICMP Traceroute** | `hping3 -1 --traceroute target` — TTL increment, shows hop-by-hop path. |
| **TCP Traceroute** | `hping3 -S -p 80 --traceroute target` — traceroute using SYN packets to port 80. Bypasses firewalls that block ICMP-based traceroute. |
| **UDP Traceroute** | `hping3 -2 -p 53 --traceroute target` — traceroute via UDP to port 53. |

---

# PHASE 3: NETWORK TESTING

---

### Task 3.1 — Firewall Rule Verification

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Verify that firewall rules are working as intended. |
| **Method** | `hping3 -S -p 443 target` — should pass (HTTPS allowed). `hping3 -S -p 23 target` — should be blocked (Telnet). `hping3 -1 target` — ICMP allowed? Compare expected vs. actual. |
| **Evidence** | RST = port reached the host (not blocked by firewall). No reply + RST from firewall IP = blocked. |

---

### Task 3.2 — Bandwidth Testing

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Large Packets** | `hping3 -S -p 80 -d 1400 target` — 1400-byte payload per packet. |
| **Monitor** | Use Wireshark or tcpdump on the target to see incoming traffic. |
| **Note** | For proper bandwidth testing, use iperf3 instead. hping3 is better for functional testing, not throughput measurement. |

---

### Task 3.3 — Fragmentation Testing

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Fragment Packets** | `hping3 -S -p 80 -f target` — set "More Fragments" flag. Send fragmented packets. |
| **Use Case** | Test if firewalls/IDS handle fragmented packets correctly. Some old IDS reassemble incorrectly → evasion. |

---

### Task 3.4 — Source IP Spoofing

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Command** | `hping3 -S -p 80 -a 10.0.0.99 target` — spoof source IP as 10.0.0.99. |
| **Use Case** | Test whether target validates source IPs. Reflection attack research. |
| **Limitation** | Responses go to the spoofed IP — you won't see them. Useful only for one-way testing or when you control the spoofed IP's traffic too. |

---

# PHASE 4: DoS TESTING (LAB ONLY)

---

### Task 4.1 — SYN Flood (Lab Only)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

> [!CAUTION]
> **Lab only.** Never run against systems you don't own or have explicit written authorization to test. SYN floods can take down servers and disrupt other services.

| Field | Detail |
|:---|:---|
| **Command** | `hping3 --flood -S -p 80 --rand-source target`. |
| **What Happens** | Sends SYN packets as fast as possible from random spoofed source IPs. Target's SYN queue fills → legitimate connections drop. |
| **Defense** | SYN cookies (kernel feature). Rate limiting on the firewall. TCP connection limits per source IP. |

---

### Task 4.2 — ICMP Flood (Lab Only)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Command** | `hping3 --flood -1 target`. |
| **Effect** | Saturates target's ICMP processing. Less effective on modern systems. Useful for demonstrating ICMP-based DoS concepts. |

---

### Task 4.3 — Measuring DoS Resilience

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Test how many SYN packets per second are needed to saturate a target's connection table. |
| **Method** | Start with low rate: `hping3 -S -p 80 -i u1000 target` (1000 packets/sec). Increase rate. Monitor target: when does response time degrade? When does it stop responding? Document the threshold. |

---

# PHASE 5: MASTERY CHECK

---

### Task 5.1 — Competency Self-Assessment

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Competency | Self-Assessment |
|:---|:---:|
| Can perform ICMP, TCP SYN, and UDP packet tests | ☐ |
| Can use hping3 to discover hosts when ICMP is blocked | ☐ |
| Can use ACK scan to map firewall rules | ☐ |
| Can perform TCP traceroute via hping3 | ☐ |
| Can run a SYN flood in an isolated lab for DoS concept testing | ☐ |
| Knows when to use hping3 vs. Nmap vs. Scapy | ☐ |

---

### Task 5.2 — Interview Questions

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

1. How does hping3 differ from a standard `ping` command?
2. How do you use hping3 to discover hosts when ICMP is blocked?
3. What is an ACK scan and what does it reveal about firewall rules?
4. What is a SYN flood and how does hping3 facilitate it?
5. What defenses protect against SYN flood attacks?
6. When would you use hping3 over Nmap for port scanning?
7. How do you perform a TCP-based traceroute with hping3?
