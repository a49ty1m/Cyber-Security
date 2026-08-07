# 🔬 PEStudio: Complete Mastery Checklist

> **What is PEStudio?** PEStudio is a free Windows PE (Portable Executable) file analyzer for malware initial triage. It provides an instant, comprehensive static analysis view of a Windows executable or DLL without executing it — showing: file hashes, imported APIs, strings, sections, resources, certificates, entropy, VirusTotal results, and indicators of compromise. It is the tool every malware analyst opens first when they receive a suspicious file.
>
> **Why does it exist?** Before committing to a full Ghidra/x64dbg analysis session, analysts need to quickly understand a file: is it malicious? What does it likely do? Is it packed? PEStudio provides this 2-minute triage that tells you everything you need to know to prioritize and direct deeper analysis.
>
> **When to use it:** Initial malware triage — the first 2 minutes of analysis. Comparing suspicious files quickly. Automated pipeline triage of many files. Understanding PE structure before deeper analysis.
>
> **Platform:** Windows only. Free. No installation required.

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals | 4 | 1–2 hours |
| 2 | File Identification | 4 | 1–2 hours |
| 3 | Import Analysis | 4 | 2–3 hours |
| 4 | String Analysis | 3 | 1–2 hours |
| 5 | PE Structure | 4 | 2–3 hours |
| 6 | Indicators | 3 | 1–2 hours |
| 7 | Practical Labs | 3 | 2–4 hours |
| 8 | Mastery Challenges | 2 | 1–2 hours |
| | **Total** | **27** | **~11–20 hours** |

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — PE File Format Basics

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **PE** | Portable Executable format. All Windows .exe, .dll, .sys, .scr files. Defined structure that Windows loader uses to load and run the file. |
| **DOS Header** | `MZ` magic bytes. Historical DOS stub. |
| **PE Header** | Machine type (x86/x64). Number of sections. Timestamp (compilation time). |
| **Optional Header** | Entry point address. Image base. Section alignment. OS requirements. |
| **Section Table** | List of sections: `.text` (code), `.data` (initialized data), `.rdata` (read-only: strings, imports), `.bss` (uninitialized). |
| **Import Table** | List of DLLs and APIs the executable calls. |

---

### Task 1.2 — Installation

- [ ] **Completed** · ⭐ Beginner · ⏱️ 5 min

| Field | Detail |
|:---|:---|
| **Download** | `winitor.com` → PEStudio free download. |
| **Portable** | Extract zip. Run `pestudio.exe`. No installation. |
| **VM** | Use in your Windows analysis VM. |

---

### Task 1.3 — PEStudio Workflow

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Open** | File → Open or drag-drop. |
| **Sections** | Left sidebar: file, indicators, libraries, imports, exports, resources, strings, headers, sections, certificates. Each section = one analysis category. |
| **Indicators** | Red = high severity findings. Yellow = medium. Green = low. |
| **Workflow** | Open file → check indicators → check imports → check strings → check sections/entropy → check VirusTotal. |

---

### Task 1.4 — File Identification

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Hashes** | MD5, SHA1, SHA256. Use for: VirusTotal lookup, IOC reporting, de-duplicating samples. |
| **File Type** | Magic bytes. `MZ` = PE executable. |
| **Architecture** | x86 (32-bit) or x64 (64-bit). |
| **Compiler** | Compilation toolchain detected (MSVC, GCC, Delphi, .NET). Guides further analysis tool choice. |

---

# PHASE 2: FILE IDENTIFICATION

---

### Task 2.1 — Hashes and VirusTotal

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **SHA256** | Primary hash for malware identification. Copy → paste into VirusTotal. |
| **VT Integration** | PEStudio can query VirusTotal directly. File → Options → VirusTotal API key. Adds VT detection count to the file view. |
| **Result** | 50/70 AV engines detect → confirmed malware. 0/70 → clean or novel malware. |
| **Caution** | Don't upload samples to VT if they contain sensitive or proprietary data. Use hash lookup only. |

---

### Task 2.2 — Compilation Timestamp

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Header** | PE Optional Header → TimeDateStamp. |
| **Value** | Compilation time. If 1970 or far future: likely tampered. |
| **IOC** | Timestamp + compiler + language → part of threat actor fingerprint. |

---

### Task 2.3 — Rich Header

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **What** | MSVC-specific data embedded between DOS stub and PE header. Contains: linker version, object file IDs, compilation tool versions. |
| **Fingerprint** | Rich header hash is unique to builds from the same compilation environment. Multiple malware samples with the same Rich header → same author's environment. Attribution correlation. |

---

### Task 2.4 — Entropy Analysis

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Entropy** | Measure of randomness. Scale 0–8. |
| **Normal Code** | .text section: ~6–6.5. Predictable. |
| **Compressed/Encrypted** | Entropy > 7.0 → section is compressed, encrypted, or contains packed data. Strong indicator of packing or encrypted payload. |
| **PEStudio** | Shows entropy per section. Sections view → entropy column. Red highlight if high. |

---

# PHASE 3: IMPORT ANALYSIS

---

### Task 3.1 — Reading Imports

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Libraries** | PEStudio → Libraries. Lists all imported DLLs: kernel32, user32, advapi32, wininet, ws2_32, ntdll, etc. |
| **Imports** | PEStudio → Imports. All individual API functions called. Each tagged with a category and severity. |
| **Category Tags** | PEStudio auto-categorizes: `process` (CreateProcess, OpenProcess), `network` (InternetOpen, WSAConnect), `registry` (RegCreateKey), `file` (CreateFile), `injection` (VirtualAllocEx, WriteProcessMemory), `debug` (IsDebuggerPresent). |

---

### Task 3.2 — High-Risk Imports

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Process Injection** | `VirtualAllocEx`, `WriteProcessMemory`, `CreateRemoteThread`, `NtCreateThreadEx`. |
| **Credential Theft** | `CryptUnprotectData` (DPAPI — decrypt browser/system credentials). `SamConnect` / `LsaOpenPolicy`. |
| **Persistence** | `RegSetValue` (registry). `CreateService`. `ITaskService` (scheduled tasks). |
| **Network** | `InternetOpenUrl`, `WSAConnect`, `connect`, `send`, `recv`. |
| **Anti-Debug** | `IsDebuggerPresent`, `CheckRemoteDebuggerPresent`. |
| **Self-Delete** | `DeleteFile` called with own path. |

---

### Task 3.3 — Absent Import Table (Packed)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Sign** | Only imports: `LoadLibrary`, `GetProcAddress` (and maybe a few more). |
| **Meaning** | Packer loads its own imports dynamically. Original binary's imports hidden until unpacking. |
| **Action** | Use x64dbg to run and unpack. Analyze unpacked binary's imports. |

---

### Task 3.4 — Exports

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **DLL Exports** | DLLs export functions. PEStudio → Exports. |
| **Malicious DLL** | Common in DLL sideloading attacks. Malicious DLL exports same function names as the legitimate DLL it replaces. Check export names match the legitimate DLL. |

---

# PHASE 4: STRING ANALYSIS

---

### Task 4.1 — PEStudio Strings View

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Open** | Strings section. Lists all ASCII and Unicode strings. |
| **Filter** | PEStudio tags interesting strings: URLs, IPs, registry paths, file paths, commands. Red tag = high interest. |
| **Focus On** | URLs and IPs (C2). Command strings (`cmd.exe`, `powershell`). Registry paths. Base64 strings. File paths (payload drop locations). Error messages. |

---

### Task 4.2 — Key String Indicators

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **C2** | `http://`, `https://`, IP addresses → C2 candidates. |
| **Commands** | `cmd.exe /c`, `powershell -enc`, `reg add HKCU\...` → execution / persistence. |
| **Mutexes** | Mutex names → unique per malware family. Google the mutex name for family identification. |
| **Compile Artifacts** | PDB path: `C:\Users\hacker_name\project\malware.pdb` → developer name! Username and project path often visible. |
| **Obfuscated** | No meaningful strings → obfuscated or encrypted. Look for Base64 blocks or high-entropy byte sequences. |

---

### Task 4.3 — Version Info and Resources

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Version Info** | PE version strings: Product Name, File Description, Company Name. Malware often spoofs legitimate software (claims to be `svchost.exe` or `Microsoft Windows`). |
| **Resources** | PEStudio → Resources. Embedded files, icons, version info, dialog boxes. Malware may embed a payload as a resource (extracted at runtime). |
| **Suspicious** | Resource with high entropy → embedded packed/encrypted payload. |

---

# PHASE 5: PE STRUCTURE

---

### Task 5.1 — Sections Analysis

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Normal** | `.text` (code), `.data` (data), `.rdata` (read-only data, strings, import table). |
| **Suspicious** | Unusual section names (`.xyz`, `.packed`, `UPX0`, `UPX1`). Code in `.data` section (self-modifying code). Sections with write+execute permissions (shellcode). |
| **Virtual vs. Raw Size** | Large difference between virtual size and raw size → section expands at runtime (possibly unpacking). |

---

### Task 5.2 — PE Headers Detail

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Entry Point** | Where execution starts. Normally in `.text`. If entry point in `.data` or another unusual section → suspicious. |
| **Subsystem** | `CONSOLE` = command-line app. `WINDOWS` = GUI app. Malware claiming to be GUI but acting as console = suspicious. |
| **Characteristics** | `DLL` flag — is it a DLL? `EXECUTABLE` flag. `LARGE_ADDRESS_AWARE`. |

---

### Task 5.3 — TLS Callbacks

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **TLS** | Thread Local Storage callbacks execute BEFORE the entry point. Anti-debug checks here run before most debuggers break at entry point. |
| **PEStudio** | Shows TLS callbacks in the headers section. |
| **x64dbg** | Break on TLS callbacks: Options → Preferences → Events → Break on TLS callbacks. |

---

### Task 5.4 — Certificates

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Signed** | PEStudio → Certificates. Legitimate software is signed by a trusted CA. |
| **Self-signed** | Self-signed certificate → not from a CA → less trustworthy. |
| **Stolen/Leaked** | Malware signed with legitimate certificates stolen from vendors. Check: certificate issuer, subject, thumbprint against known malicious cert lists. |
| **Timestamp** | Countersignature timestamp — when the binary was signed. Compare to PE compilation timestamp. |

---

# PHASE 6: INDICATORS

---

### Task 6.1 — PEStudio Indicators Panel

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Panel** | Left sidebar → Indicators. Aggregated list of all findings categorized by severity. |
| **Red** | High severity: injection-related imports, anti-debug APIs, network + file + registry combo, encrypted sections. |
| **Workflow** | Start with Red indicators → investigate each → confirm. |

---

### Task 6.2 — Building an IOC List

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **IOCs** | Indicators of Compromise. From PEStudio: SHA256 hash, imported API pattern, mutex name, C2 URL/IP, PDB path, certificate thumbprint, specific string. |
| **Export** | PEStudio → File → Export XML → contains all findings. Import into SIEM or threat intel platform. |

---

### Task 6.3 — YARA Rule from PEStudio

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **YARA** | Pattern matching for malware detection. PEStudio findings → translate to YARA strings: specific import combinations, strings, byte patterns. |
| **Example** | `rule suspicious_injector { strings: $valloc = "VirtualAllocEx" $wpm = "WriteProcessMemory" $crt = "CreateRemoteThread" condition: all of them }`. |

---

# PHASE 7: PRACTICAL LABS

---

### Lab 7.1 — Triage a Malware Sample

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| **Scenario** | Download a known malware sample (MalwareBazaar). Open in PEStudio. Complete 2-minute triage: hash, VT result, imports behavioral profile, key strings, entropy, indicators. Write a one-page triage report. |
| **Success Criteria** | Triage report written in under 10 minutes. Correct behavioral profile from imports. |

---

### Lab 7.2 — Identify Packing

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| **Scenario** | UPX-packed binary. Open in PEStudio. Identify: import table (LoadLibrary/GetProcAddress only), high-entropy sections (>7.0), UPX section names. Confirm packing. Plan next steps (x64dbg). |
| **Success Criteria** | Packing correctly identified. All indicators documented. Next-step plan written. |

---

### Lab 7.3 — Compare Legitimate and Malicious

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| **Scenario** | Compare a legitimate `svchost.exe` and a malicious lookalike in PEStudio. Identify: import differences, string differences, entropy differences, signature status. Document all differences. |
| **Success Criteria** | All distinguishing indicators documented. Clear case for maliciousness made from static analysis alone. |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — Full Triage Report

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| **Scenario** | Malware sample of unknown family. Complete triage with PEStudio. Write a professional malware triage report: hash, VT, behavioral profile (what it likely does from imports), key strings, section analysis, indicators, YARA rule, recommended next steps. |
| **Success Criteria** | Professional report. YARA rule created and tested. Next-step analysis plan written. |

---

### Challenge 8.2 — DLL Sideloading Analysis

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| **Scenario** | Suspected DLL sideloading attack: malicious DLL in the same directory as a legitimate application. Use PEStudio to compare: legitimate DLL exports vs. malicious DLL exports, imports, entropy, code signatures. |
| **Success Criteria** | Sideloading confirmed. Malicious DLL fully characterized. Comparison documented. |

---

# 📋 FINAL COMPETENCY MATRIX

| Competency | Self-Assessment |
|:---|:---:|
| Can perform a complete 2-minute triage on any PE file | ☐ |
| Can read and categorize imports for behavioral profiling | ☐ |
| Can identify packed binaries from imports and entropy | ☐ |
| Can extract and prioritize key strings | ☐ |
| Can analyze PE sections for anomalies | ☐ |
| Can build an IOC list from PEStudio findings | ☐ |
| Can write a YARA rule from PEStudio findings | ☐ |
| Can write a professional malware triage report | ☐ |

---

## 🎯 Interview Questions

1. What is the PE format and what are its main components?
2. What imports indicate process injection?
3. What does high entropy in a PE section indicate?
4. How do you detect a packed binary in PEStudio?
5. What strings are highest priority to look for in malware?
6. What is a Rich header and why is it useful for attribution?
7. How do you use PEStudio findings to write a YARA rule?
8. What is DLL sideloading and how do you detect it in PEStudio?
