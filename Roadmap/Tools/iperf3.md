# 📡 iperf3: Complete Reference

> **What is iperf3?** iperf3 is a network throughput testing tool. It measures the actual bandwidth available between two endpoints — TCP or UDP — by running one instance in server mode and another in client mode. The client pushes data to the server (or vice versa) and reports: throughput (Mbits/sec), jitter (for UDP), packet loss (for UDP), and TCP retransmission count. It tells you what the network link between two points can actually deliver.
>
> **When to use it:** Verifying network bandwidth between lab machines. Testing if firewall rules or network segmentation affect throughput. Measuring WAN link capacity. Testing network performance between a C2 server and implant host (in authorized red team labs). Baselining network capacity before and after infrastructure changes. Troubleshooting network performance issues.
>
> **Tier 4 Reminder:** iperf3 is a network engineering tool more than a security tool. Know how to run basic tests and interpret the output. Most security professionals use it for lab setup verification, not active assessments.

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals | 3 | 45 min |
| 2 | Core Usage | 5 | 1–2 hours |
| 3 | Advanced Tests | 4 | 2–3 hours |
| 4 | Security Context | 3 | 1 hour |
| 5 | Mastery Check | 2 | 20 min |
| | **Total** | **17** | **~5–7 hours** |

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — What iperf3 Measures

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Bandwidth** | How much data can flow between two points per second (Mbits/sec or Gbits/sec). The actual available throughput, not the theoretical link speed. |
| **TCP vs. UDP** | TCP: measures bandwidth, retransmissions. Shows impact of congestion control. UDP: measures bandwidth, jitter (variation in packet arrival timing), packet loss percentage. |
| **Jitter** | How consistently packets arrive. Low jitter = good for real-time traffic (VoIP, video). High jitter = packets arrive at irregular intervals → problems for latency-sensitive applications. |
| **Bidirectional** | iperf3 can measure upload (client→server), download (server→client), or both simultaneously. |

---

### Task 1.2 — Installation

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Linux** | `apt install iperf3`. |
| **macOS** | `brew install iperf3`. |
| **Windows** | Download from `iperf.fr`. Extract. Run from CMD/PowerShell. |
| **Verify** | `iperf3 --version`. |
| **Both Ends** | iperf3 must be installed on both machines — server and client. |

---

### Task 1.3 — Client-Server Model

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Server Mode** | On machine A: `iperf3 -s`. Listens on port 5201 (default). Waits for connections. |
| **Client Mode** | On machine B: `iperf3 -c <server_IP>`. Connects to server. Sends data. Reports results. |
| **Direction** | Default: client sends → server receives (measures upload bandwidth from client's perspective). Reverse: add `-R` → server sends → client receives (measures download). |

---

# PHASE 2: CORE USAGE

---

### Task 2.1 — Basic TCP Test

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Server** | `iperf3 -s`. |
| **Client** | `iperf3 -c 192.168.1.100`. Default: 10-second TCP test. |
| **Output** | Interval-by-interval throughput + summary: `[ ID] Interval       Transfer     Bandwidth`. `[  4]  0.00-10.00 sec  1.12 GBytes   961 Mbits/sec    sender`. |
| **Key Line** | `sender` = data sent by client. `receiver` = data received by server. Compare both — difference = network loss. |

---

### Task 2.2 — Test Duration and Interval

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Duration** | `-t 30` — run for 30 seconds (default 10). Longer = more stable average. |
| **Interval** | `-i 1` — report every 1 second. Default 1 second. `-i 5` — every 5 seconds (less noise). |
| **Example** | `iperf3 -c 192.168.1.100 -t 60 -i 5` — 60-second test, report every 5 seconds. |

---

### Task 2.3 — UDP Test

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Server** | `iperf3 -s`. |
| **Client** | `iperf3 -c 192.168.1.100 -u -b 100M`. |
| **Flags** | `-u` — UDP mode. `-b 100M` — target bitrate (100 Mbps). UDP doesn't self-regulate like TCP — you must set the target rate. |
| **Output** | `Bandwidth`, `Jitter`, `Lost/Total Datagrams (%)`. Low jitter + 0% loss = excellent. High jitter + loss = congestion or link quality issues. |

---

### Task 2.4 — Reverse Test (Download)

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Command** | `iperf3 -c 192.168.1.100 -R`. |
| **What Changes** | Server sends data → client receives. Measures client's download bandwidth from the server. |
| **Use Case** | If you're benchmarking a server's ability to push data to clients (e.g., a file server), use `-R`. For measuring upload capacity, use the default direction. |

---

### Task 2.5 — Parallel Streams

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Command** | `iperf3 -c 192.168.1.100 -P 4`. |
| **What It Does** | Opens 4 parallel TCP streams simultaneously. Can help saturate a link that a single stream can't fill (due to TCP window size limits on high-latency links). |
| **Use Case** | Testing total available bandwidth across all flows (not just single-stream). High-latency WAN links benefit more from parallel streams. |

---

# PHASE 3: ADVANCED TESTS

---

### Task 3.1 — Custom Port

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Server** | `iperf3 -s -p 8080` — listen on port 8080. |
| **Client** | `iperf3 -c 192.168.1.100 -p 8080`. |
| **Use Case** | Test if specific ports have different throughput (firewall QoS). Test if port 443 is rate-limited vs. port 5201. Compare throughput on allowed vs. non-standard ports. |

---

### Task 3.2 — Buffer Size Tuning

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Socket Buffer** | `-w 256k` — set TCP socket buffer (window size). Larger window = can have more data in flight on high-latency links. |
| **Bandwidth-Delay Product** | BDP = Bandwidth × RTT. On a 1Gbps link with 100ms RTT: BDP = 100 Mbits = 12.5 MB. TCP window must be at least 12.5 MB to fully utilize the link. |
| **Test** | Compare default window size vs. `-w 8M` on a high-latency link. Often see significant throughput improvement. |

---

### Task 3.3 — JSON Output

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Command** | `iperf3 -c 192.168.1.100 -J > results.json`. |
| **Parse** | `cat results.json | python3 -c "import json,sys; d=json.load(sys.stdin); print(d['end']['sum_sent']['bits_per_second']/1e6, 'Mbps'"`. |
| **Use Case** | Automated network testing scripts. Log throughput over time. Compare before/after configuration changes programmatically. |

---

### Task 3.4 — Bidirectional Test

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Command** | `iperf3 -c 192.168.1.100 --bidir`. (iperf3 ≥ 3.7). |
| **What It Does** | Simultaneously sends in both directions — measures full-duplex throughput. |
| **Use Case** | Verify that simultaneous upload+download doesn't interfere (some network equipment degrades throughput when both directions saturated simultaneously). |

---

# PHASE 4: SECURITY CONTEXT

---

### Task 4.1 — Network Segmentation Verification

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Use Case** | Run iperf3 server in one network segment (e.g., DMZ). Run iperf3 client in another segment (e.g., corporate LAN). If you can connect: those segments are not properly isolated. |
| **Firewall Testing** | `iperf3 -c dmz_server -p 5201` — tests if port 5201 is allowed through the firewall. Try different ports to test which are permitted. |
| **Expected Result** | In a properly segmented network: connection refused (firewall blocks). |

---

### Task 4.2 — C2 Channel Bandwidth (Red Team Lab)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Use Case** | In an authorized red team lab: estimate how much data you can exfiltrate per second via a C2 channel. Run iperf3 over the same port and protocol as the C2 channel. |
| **Example** | C2 uses HTTPS to external server. `iperf3 -c c2-server -p 443` (if server configured to listen on 443). Throughput = max exfiltration rate. |

---

### Task 4.3 — QoS and Rate Limiting Validation

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Verify that network QoS policies are working as configured. |
| **Test** | Expected: port 80 limited to 10 Mbps by QoS policy. `iperf3 -c server -p 80 -t 30`. Result: if ≈10 Mbps → policy working. If much higher → policy not applied. Compare: `iperf3 -c server -p 443 -t 30` — should get different rate if different QoS class. |

---

# PHASE 5: MASTERY CHECK

---

### Task 5.1 — Competency Self-Assessment

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Competency | Self-Assessment |
|:---|:---:|
| Can start iperf3 in server and client mode | ☐ |
| Can run TCP and UDP tests | ☐ |
| Can interpret throughput, jitter, and packet loss metrics | ☐ |
| Can run reverse-direction and parallel-stream tests | ☐ |
| Can use iperf3 to verify network segmentation | ☐ |
| Knows when to use iperf3 vs. ab/wrk | ☐ |

---

### Task 5.2 — Interview Questions

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

1. What is the difference between iperf3 in TCP and UDP mode?
2. What does jitter measure and why is it important for certain traffic types?
3. How do you use iperf3 to verify network segmentation between two VLANs?
4. What is the Bandwidth-Delay Product and why does it affect TCP throughput on high-latency links?
5. When would you use iperf3 over ab or wrk for network testing?
6. How do you run a reverse test to measure download throughput?
