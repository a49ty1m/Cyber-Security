# 🧠 Volatility 3: Complete Mastery Checklist

> **What is Volatility?** Volatility is the industry-standard open-source memory forensics framework. It analyses RAM captures (memory dumps) to extract running processes, network connections, loaded drivers, injected code, encryption keys, passwords, and evidence of malware that lives entirely in memory (fileless malware). Volatility 3 is the current version — rebuilt with Python 3, faster symbol table handling, and a plugin architecture that covers Windows, Linux, and macOS.
>
> **Why does it exist?** Disk forensics cannot see what is in RAM. Many modern attacks — fileless malware, process injection, credential theft via LSASS — leave minimal disk artifacts but leave extensive memory traces. Volatility bridges this gap.
>
> **When to use it:** Incident response — capture memory from a compromised host and analyse it offline. CTF memory forensics challenges. Malware analysis — identify injected shellcode, C2 beaconing processes, and rootkit hooks. Credential recovery — extract NTLM hashes and Kerberos tickets from LSASS memory.
>
> **What mastering Volatility unlocks:** Memory forensics investigations. Detection of fileless malware and process injection. Credential extraction from memory. Foundation for Phase 7 Part 27 Stage 3 (Memory Forensics Gate).
>
> **Roadmap Phase:** Phase 7 Part 27 (Digital Forensics) — Memory Forensics Gate

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Installation & Memory Acquisition | 4 | 1–2 hours |
| 2 | Core Process Analysis | 6 | 3–4 hours |
| 3 | Network & Connection Analysis | 4 | 2–3 hours |
| 4 | Code Injection & Malware Detection | 5 | 4–6 hours |
| 5 | Credential Extraction | 4 | 2–3 hours |
| 6 | Rootkit & Kernel Analysis | 4 | 3–4 hours |
| 7 | Practical Labs | 4 | 6–10 hours |
| | **Total** | **31** | **~21–32 hours** |

**Prerequisites:** OS internals (Phase 1 Part 1 Stage 2–3 complete). Understanding of Windows process model, virtual memory, and kernel/user space. Phase 7 Part 27 Stage 1–2 recommended.

---

# PHASE 1: INSTALLATION & MEMORY ACQUISITION

---

## 1.1 Installation

```bash
# Install Volatility 3
pip3 install volatility3

# Or from source (recommended for latest plugins)
git clone https://github.com/volatilityfoundation/volatility3.git
cd volatility3
pip3 install -e .

# Verify installation
python3 vol.py --help

# List all available plugins
python3 vol.py --help | grep -E "windows\.|linux\.|mac\."
```

- [ ] **Symbol Tables:** Volatility 3 uses symbol tables (ISF files) instead of profiles (Volatility 2). For Windows analysis, symbol tables are downloaded automatically from Microsoft's symbol server on first analysis. For offline environments, download the [Volatility 3 symbols pack](https://downloads.volatilityfoundation.org/volatility3/symbols/) manually.

- [ ] **Volatility 2 vs 3 Differences:** Volatility 3 uses `python3 vol.py windows.PLUGIN` syntax (not `--profile`). Profiles are auto-detected. Some Volatility 2 plugins have not been ported to V3 yet — know which ones you might need.

---

## 1.2 Memory Acquisition

- [ ] **Windows Acquisition Tools:** Use `WinPmem` (open-source, works on modern Windows), `Magnet RAM Capture` (free GUI), `FTK Imager` (see FTK_Imager.md) for live acquisition. Output to `.raw`, `.mem`, or `.dmp` format.

- [ ] **Linux Acquisition:** Use `LiME` (Linux Memory Extractor — a loadable kernel module). Build for target kernel version. `insmod lime.ko path=/tmp/memory.lime format=lime`. Volatility 3 supports LiME format.

- [ ] **VM Snapshots:** VMware `.vmem` and `.vmsn` files, VirtualBox `.sav` files, and Hyper-V checkpoint files are valid Volatility input. For lab practice, snapshot a VM at a known state.

- [ ] **Evidence Integrity:** Hash your memory image immediately after acquisition (`sha256sum memory.raw`). Document acquisition timestamp, tool version, and hash in chain of custody notes.

---

# PHASE 2: CORE PROCESS ANALYSIS

---

## 2.1 Process Listing

```bash
# Standard process list (from EPROCESS linked list)
python3 vol.py -f memory.raw windows.pslist

# Process tree view (parent-child relationships)
python3 vol.py -f memory.raw windows.pstree

# Scan for processes using pool tag scanning (finds hidden/unlinked processes)
python3 vol.py -f memory.raw windows.psscan

# Compare pslist vs psscan results (discrepancies = hidden processes)
python3 vol.py -f memory.raw windows.pslist > pslist.txt
python3 vol.py -f memory.raw windows.psscan > psscan.txt
```

- [ ] **Normal vs Suspicious Processes:** Know what legitimate Windows processes look like — parent relationships, expected paths, expected counts:
  - `System` — PID 4, parent PID 0, one instance only
  - `smss.exe` — child of System, one instance, path `\Windows\System32\smss.exe`
  - `csrss.exe` — child of smss, one per session, path `\Windows\System32\csrss.exe`
  - `winlogon.exe` — one per interactive session, child of smss
  - `svchost.exe` — multiple instances, all children of `services.exe`, path `\Windows\System32\svchost.exe`
  - **Red flags:** wrong parent, wrong path, misspelled names (`scvhost`, `svhost`, `lsass` with wrong PID/parent)

- [ ] **Process Command Lines:** `windows.cmdline` — shows the full command line each process was started with. Malware often has suspicious command lines: encoded PowerShell (`-EncodedCommand`), unusual flags, paths in temp directories.

- [ ] **Process Environment Variables:** `windows.envars` — environment variables per process. Can reveal attacker staging paths, C2 addresses encoded in env vars, and unusual `COMSPEC` or `PATH` manipulations.

- [ ] **DLL Analysis:** `windows.dlllist --pid <PID>` — lists all DLLs loaded by a process. Unusual DLLs in temp/roaming paths, DLLs with no path (reflectively loaded), or known-malicious DLL names are significant.

- [ ] **Handles:** `windows.handles --pid <PID>` — lists open file, registry, process, thread, and event handles. A malicious process may have a handle to LSASS (credential theft attempt) or to other sensitive processes.

---

# PHASE 3: NETWORK & CONNECTION ANALYSIS

---

```bash
# Active TCP connections (current snapshot)
python3 vol.py -f memory.raw windows.netstat

# All TCP/UDP connections including closed (uses pool scanning)
python3 vol.py -f memory.raw windows.netscan

# Filter for established connections
python3 vol.py -f memory.raw windows.netscan | grep ESTABLISHED
```

- [ ] **Identify C2 Connections:** Look for established connections from unusual processes (e.g., `notepad.exe`, `svchost.exe` connecting to non-Microsoft IPs on unusual ports like 4444, 8080, 443 with suspicious certificate). Correlate process PID with `pslist` output.

- [ ] **Listening Services:** Filter for `LISTEN` state — identifies backdoors, reverse shells waiting for connection, or unusual local listeners.

- [ ] **Foreign Address Reputation:** Extract all foreign IPs from `netscan` output and check against threat intelligence (VirusTotal, Shodan, AbuseIPDB). Script this: `python3 vol.py -f memory.raw windows.netscan | awk '{print $4}' | sort -u`.

- [ ] **DNS Cache (Indirect):** `windows.registry.printkey --key "HKLM\SYSTEM\CurrentControlSet\Services\Dnscache\Parameters\Caches"` — or dump the DNS client cache from the relevant `svchost.exe` process memory to find recently resolved domains.

---

# PHASE 4: CODE INJECTION & MALWARE DETECTION

---

```bash
# Find VAD regions with suspicious protections (RWX memory, PAGE_EXECUTE_READWRITE)
python3 vol.py -f memory.raw windows.vadinfo --pid <PID>

# Memory mapped files and suspicious VAD entries
python3 vol.py -f memory.raw windows.malfind

# Scan all process memory for PE headers (injected code without disk presence)
python3 vol.py -f memory.raw windows.malfind --dump

# Check for DLL injection / process hollowing
python3 vol.py -f memory.raw windows.dlllist --pid <PID>
```

- [ ] **`windows.malfind`:** The primary injection detection plugin. Scans all process VAD (Virtual Address Descriptor) trees for regions that are executable, not backed by a file on disk, and contain PE headers. Each hit should be inspected — dump the region and analyse with strings/yara/IDA.

- [ ] **Process Hollowing Indicators:** The legitimate process image path in `pslist` does not match the executable content in the VAD region. The VAD region for the main executable has RWX protections instead of standard R-X.

- [ ] **Reflective DLL Injection:** A loaded DLL appears in `dlllist` output but has no file path (reflectively loaded into memory). The MZ header of the injected DLL is visible in the process memory VAD dump.

- [ ] **YARA Scanning:** `windows.yarascan --yara-rules yararules.yar` — scan all process memory against YARA rules. Use public malware signatures (ESET, Florian Roth's rule sets, MalwareBazaar signatures).

- [ ] **Strings from Process Memory:** `windows.memmap --dump --pid <PID>` → then `strings -n 8 pid.<PID>.dmp | grep -E 'http|cmd|powershell|base64'`. Useful for extracting C2 URLs, encoded commands, and hardcoded credentials from malware memory.

---

# PHASE 5: CREDENTIAL EXTRACTION

---

> [!IMPORTANT]
> Credential extraction from memory is a legitimate forensic technique — and also the primary offensive technique (Mimikatz). Understanding both sides is required for Phase 7.

```bash
# Extract NTLM hashes from LSASS (like Mimikatz, but offline)
python3 vol.py -f memory.raw windows.hashdump

# Extract Kerberos tickets from LSASS memory
python3 vol.py -f memory.raw windows.kerberos

# Cached domain credentials (DCC2 hashes)
python3 vol.py -f memory.raw windows.cachedump

# LSA secrets (service account passwords, DPAPI masterkey blobs)
python3 vol.py -f memory.raw windows.lsadump
```

- [ ] **NTLM Hash Format:** `hashdump` output format: `username:RID:LM_hash:NT_hash:::`. Pass-the-Hash uses the NT hash directly. Crack NT hashes with `hashcat -m 1000`.

- [ ] **Kerberos Tickets (ccache):** Extracted TGTs and service tickets can be passed directly (`Pass-the-Ticket`) or cracked offline (Kerberoasting — service ticket hash). Export with `--dump` flag.

- [ ] **DPAPI Masterkey Blobs:** `windows.dpapi.mastekeys` — extracts DPAPI masterkey blobs which protect browser saved passwords, Wi-Fi credentials, and Windows Credential Manager entries.

---

# PHASE 6: ROOTKIT & KERNEL ANALYSIS

---

```bash
# List kernel modules (drivers)
python3 vol.py -f memory.raw windows.modules

# Scan for unlinked kernel modules (hidden rootkit drivers)
python3 vol.py -f memory.raw windows.modscan

# System Service Descriptor Table (SSDT) hook detection
python3 vol.py -f memory.raw windows.ssdt

# Detect DKOM (Direct Kernel Object Manipulation) — process hiding
python3 vol.py -f memory.raw windows.pslist   # EPROCESS linked list
python3 vol.py -f memory.raw windows.psscan   # Pool tag scan — finds unlinked processes
```

- [ ] **`modules` vs `modscan`:** Discrepancies between linked module list and pool-scan results indicate hidden (unlinked) kernel drivers — a rootkit indicator. Any driver in `modscan` not in `modules` warrants immediate investigation.

- [ ] **SSDT Hook Detection:** `windows.ssdt` shows which function addresses in the SSDT have been overwritten (hooked). Hooked SSDT entries indicate kernel-level rootkit or AV/EDR driver (distinguish by driver signer).

- [ ] **Registry Analysis:** `windows.registry.hivelist` — lists all registry hives in memory. `windows.registry.printkey` — extracts specific registry keys (autorun entries, service configurations, network settings) from the in-memory registry snapshot.

---

# PHASE 7: PRACTICAL LABS

---

- [ ] **MemLabs Challenges:** Complete [MemLabs](https://github.com/stuxnet999/MemLabs) challenges 1–3 using Volatility 3. These are purpose-built CTF memory forensics exercises with increasing difficulty.

- [ ] **CyberDefenders Memory Forensics:** Complete one CyberDefenders memory forensics challenge (e.g., "Insider Threat", "Banking Troubles") with a full investigation report.

- [ ] **Malware Analysis Lab:** Download a memory capture of a known malware infection from [VirusBay](https://beta.virusbay.io) or produce your own by running a malware sample (safely, in an isolated VM) and dumping memory. Identify: injected processes, C2 connections, credential access attempts.

- [ ] **Full IR Lab:** Combine Autopsy (disk) + Volatility (memory) + Wireshark (network) on a single investigation scenario. Reconstruct the complete attack timeline across all three data sources.

---

## 📝 Operational Notes

- **Auto-profile detection:** Volatility 3 detects OS version automatically from memory — no `--profile` needed unlike V2.
- **Symbol table download failures:** On air-gapped systems, pre-download symbol packs from `downloads.volatilityfoundation.org/volatility3/symbols/`.
- **Large memory files:** 32 GB RAM dumps take time. Use `--pid` to scope to specific processes when you know your target.
- **Volatility 2 compatibility:** Some plugins (notably `mimikatz`) exist only in V2. Maintain a V2 install for these edge cases.
- **Combining with strings:** `strings -el` (for Unicode/little-endian) on dumped memory regions captures Windows-native string encoding.
