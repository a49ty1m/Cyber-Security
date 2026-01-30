# Scanning — Detailed Notes (Module 6) 🔎

**Overview:** Scanning is the active phase of reconnaissance used to discover live hosts, open ports, running services, OS versions, and potential vulnerabilities. It is used to convert raw network visibility into an actionable attack surface map and to plan follow-up testing.

---

## Objectives
- Discover live hosts and enumerate IP ranges.
- Identify open ports, services, and application versions for vulnerability mapping.
- Fingerprint operating systems and network topology to plan further action.

---

## 1. Checking for Live Systems
- **Ping / ICMP Echo:** Send ICMP ECHO requests to determine reachability; useful but often filtered by firewalls.
- **Ping sweep:** Scan a subnet (use subnet calculators to determine host counts) to build an inventory.
- **Commands:** `nmap -sn 192.168.1.0/24` (ping sweep); `fping -a -g 192.168.1.0/24`.

---

## 2. TCP 3‑Way Handshake & Flags
- **Three-way handshake:** SYN → SYN/ACK → ACK establishes normal TCP sessions.
- **TCP flags:** SYN, ACK, RST, FIN, URG, PSH — scanners use different flag combinations to infer port state and fingerprint stacks.

---

## 3. Port Scanning & States
- **Port states:** Open (service listening), Closed (no service but host responds), Filtered (firewall drops or blocks probes).
- **Why scan:** Enumerating ports and services is required to find potential CVEs and attack paths.

---

## 4. Port Scanning Methodology & Techniques
- **Tools:** `nmap` (primary), `hping3` (packet crafting), `masscan` (fast scanning across ranges).

**Common scan types and Nmap flags:**
- TCP Connect / Full Open (`-sT`): completes the full handshake (no root needed).
- Stealth / SYN Scan (`-sS`): half-open; less likely to be logged as a full connection.
- Xmas/FIN/NULL scans (`-sX`, `-sF`, `-sN`): use unusual flagsets to detect stack behavior (works on some OSes).
- ACK Scan (`-sA`): used to map firewall rules and determine whether ports are being filtered.
- UDP Scan (`-sU`): no handshake — closed ports often return ICMP port unreachable; open ports may not respond.

**Example commands (lab only):**
- Stealth SYN + service detection, all ports: `nmap -sS -sV -p- -T4 -oA scans/target 10.0.0.5`
- UDP targeting common services: `nmap -sU -p 53,67,123 -sV -T3 target` (UDP scans can be slow).
- Full scan + OS detection: `nmap -p- -A -T4 target` (invasive — use in controlled labs).
- Fast internet-scale scanning: `masscan -p0-65535 --rate=1000 target` (requires authorization and care).

**hping3 examples (packet-crafting, lab only):**
- SYN probe: `hping3 -S -p 80 target` (single SYN to port 80).
- Fragmentation tests for IDS evasion proofs-of-concept: `hping3 -f -S -p 80 target`.

---

## 5. Banner Grabbing & OS Fingerprinting
- **Active fingerprinting:** Send crafted packets and compare responses against known TCP/IP signatures (`nmap -O`, `p0f`).
- **Banner grabbing:** Connect to a service and read its banner string to get software and version info.
  - `nc -v target 80` then `HEAD / HTTP/1.0` or `curl -I http://target/`.
  - `nmap --script=banner -sV -p 80,443 target` automates banner retrieval.
- **Passive methods:** Sniff traffic for server error messages or file extensions (e.g., `.aspx` hints at IIS/Windows).

---

## 6. Evading IDS/Firewalls (for awareness/testing)
- **Techniques used by attackers:** Packet fragmentation, source spoofing, slow/low-and-slow scanning, using proxies or pivot hosts, and timing variations (`-T` with nmap).
- **Note:** These are detection/defense test techniques; they require explicit authorization.

---

## 7. Vulnerability Scanning & Visual Mapping
- **Vulnerability scanning:** Tools like OpenVAS, Nessus, and Nikto identify CVEs, weak ciphers, misconfigurations and known weaknesses.
- **Visual mapping:** Produce diagrams of network topology and trust boundaries using tools like LANSurveyor, Network Topology Mapper, OpManager.

---

## 8. Countermeasures & Hardening
- **Detect & block scans:** Use IDS/IPS signatures, rate-limiting, connection throttling, and behavior-based anomaly detection.
- **ICMP/Filtering:** Consider filtering or rate-limiting ICMP (ping) to reduce information leakage.
- **Service hardening:** Disable unnecessary services, change or obfuscate banners (`ServerSignature Off`, `ServerTokens Prod` for Apache), and keep firmware and software up to date.
- **Firewall rules:** Enforce default-deny (block-all) policies, implement anti-spoofing on edge routers, and tune anti-scanning rules.
- **Proactive testing:** Regularly run authorized scans and validate detection rules and incident playbooks.

---

### Lab-friendly commands & quick reference (Authorized use only)
- Host discovery (ping sweep): `nmap -sn 192.168.1.0/24`
- Quick stealth + service detection: `nmap -sS -sV -p- -T4 target`
- UDP reconnaissance: `nmap -sU -p 1-1024 -T3 target`
- Simple banner check: `curl -I http://target/` or `nc -v target 22`
- Fast scan (use with care): `masscan -p0-65535 --rate=1000 target`

---

## Detection & Operational Tips for Defenders
- Alert on high SYN rates, large numbers of half-open connections, and bursts of port probes from a single source.
- Use SIEM correlation to detect distributed scanning across sensors (low-and-slow techniques are easier to spot when correlated).
- Regularly test IDS/IPS signatures and update firewall rules; perform patch management and service hardening.

---

*Notes expanded from Module 6 (Scanning) on 2026-01-30.*