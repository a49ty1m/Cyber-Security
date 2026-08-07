# 🧵 strings: Complete Reference

> **What is strings?** `strings` is a classic Unix command-line utility that extracts all printable character sequences (default: 4+ consecutive printable ASCII characters) from any binary file. No parsing, no format understanding — just raw byte extraction of readable text. In 30 seconds, it gives you a first look at what a binary contains: URLs, file paths, registry keys, error messages, API function names, hardcoded credentials, compiler artifacts, and more.
>
> **When to use it:** First-pass triage before opening a binary in PEStudio or Ghidra. Quick IOC extraction (domains, IPs, file paths). Extracting readable content from unknown files (firmware, PDFs, office docs). Finding hardcoded secrets in compiled binaries during code review or binary analysis. Identifying strings in memory dumps.
>
> **Tier 4 Reminder:** Know the command options well, understand what strings output tells you, and know its limitations.

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals | 3 | 45 min |
| 2 | Core Usage | 5 | 1–2 hours |
| 3 | Analysis Techniques | 4 | 1–2 hours |
| 4 | Limitations & Alternatives | 3 | 45 min |
| 5 | Mastery Check | 2 | 20 min |
| | **Total** | **17** | **~3.5–5.5 hours** |

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — What strings Does

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Mechanism** | Scans raw file bytes. Whenever it finds N consecutive printable ASCII characters (default N=4), it outputs that sequence. No file format awareness — works on any file type. |
| **What It Finds** | Hard-coded URLs, domains, IPs. File paths (`C:\Users\...`, `/etc/passwd`). Registry keys. Error messages and debug text. Function names (if dynamically resolved). Hardcoded credentials. Mutex names. PDB paths. Base64-encoded data. |
| **What It Misses** | Encrypted/obfuscated strings (they're not printable ASCII). Unicode strings (need `-el` or `-eu` flag). Strings shorter than 4 chars (need `-n` flag). |

---

### Task 1.2 — Installation

- [ ] **Completed** · ⭐ Beginner · ⏱️ 5 min

| Field | Detail |
|:---|:---|
| **Linux** | Pre-installed on most distributions (`binutils` package). `apt install binutils`. |
| **Windows Sysinternals** | `strings.exe` from Sysinternals (Microsoft). `strings64.exe` for 64-bit binaries on Windows. Download: `learn.microsoft.com/sysinternals/downloads/strings`. |
| **macOS** | Built-in: `strings`. |

---

### Task 1.3 — strings vs. PEStudio Strings

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **strings** | CLI. Fast. Works on any file type. No automatic filtering or indicator flagging. Raw output — you analyze it. |
| **PEStudio Strings** | GUI. PE-aware — knows which section each string came from. Automatically flags suspicious strings against its indicator database. More visual. Windows-only. |
| **Workflow** | `strings sample.exe | grep -i "http\|\.com\|passwd\|token"` → fast targeted extraction. PEStudio → comprehensive with automatic indicator matching. Use both. |

---

# PHASE 2: CORE USAGE

---

### Task 2.1 — Basic Extraction

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Command** | `strings sample.exe` — extract all ASCII strings (≥4 chars). |
| **Minimum Length** | `strings -n 8 sample.exe` — only strings 8+ chars (reduces noise). `strings -n 3 sample.exe` — catch shorter strings (more noise). |
| **With Offset** | `strings -t x sample.exe` — show hex file offset of each string. Useful for finding strings in a hex editor. `strings -t d` — decimal offset. |

---

### Task 2.2 — Unicode Strings

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Problem** | Default `strings` only finds ASCII. Windows strings are often Unicode (UTF-16 LE — every char has a null byte between). `Hello` in Unicode: `48 00 65 00 6C 00 6C 00 6F 00`. `strings` can't see this. |
| **Unicode Flag** | `strings -el sample.exe` — little-endian 16-bit (Windows UTF-16). `strings -eb sample.exe` — big-endian 16-bit. `strings -e S sample.exe` — UTF-8 multi-byte. |
| **Sysinternals strings** | `strings.exe -u sample.exe` — both ASCII and Unicode. Much better for Windows PE files. |
| **Best Practice** | Always run both: `strings sample.exe` AND `strings -el sample.exe`. Many Windows malware strings are Unicode-only. |

---

### Task 2.3 — Grep Filtering

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **URLs and Domains** | `strings sample.exe | grep -i "http\|\.com\|\.ru\|\.cn\|\.io"`. |
| **IPs** | `strings sample.exe | grep -E "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"`. |
| **Paths** | `strings sample.exe | grep -i "c:\\\\users\|appdata\|system32\|\\\\temp\\\\"`. |
| **Registry** | `strings sample.exe | grep -i "hkey\|hklm\|hkcu\|software\\\\microsoft"`. |
| **Passwords/Keys** | `strings sample.exe | grep -i "password\|passwd\|secret\|apikey\|token\|bearer"`. |
| **Base64** | `strings sample.exe | grep -E "[A-Za-z0-9+/]{20,}={0,2}"`. |

---

### Task 2.4 — Output to File

- [ ] **Completed** · ⭐ Beginner · ⏱️ 5 min

| Field | Detail |
|:---|:---|
| **Redirect** | `strings sample.exe > strings_output.txt`. |
| **Combined** | `strings sample.exe strings -el sample.exe | sort -u > all_strings.txt`. Sort + deduplicate. |
| **Grep + Save** | `strings sample.exe | grep -i "http" | tee network_strings.txt`. Displays and saves simultaneously. |

---

### Task 2.5 — Batch Analysis

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Multiple Files** | `strings /path/to/samples/*` — processes all files. Output includes filename headers. |
| **With grep** | `strings /path/to/samples/* | grep -i "evil-c2.com"` — find which samples reference a specific domain. |
| **Campaign Pivot** | Extract all strings from a sample set → grep for a unique C2 domain → find all related samples. |

---

# PHASE 3: ANALYSIS TECHNIQUES

---

### Task 3.1 — Finding C2 Infrastructure

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Workflow** | `strings -n 6 sample.exe | grep -iE "(https?://|\.com|\.ru|\.cn|:\d{2,5})" | sort -u`. |
| **What to Do With Hits** | Search each domain on VirusTotal, URLhaus, urlscan.io. Check WHOIS registration date. Check passive DNS. Add as IOC. |
| **Config Not Found** | If no URLs → C2 config likely encrypted. Proceed to dynamic analysis (x64dbg). |

---

### Task 3.2 — Hardcoded Credential Search

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Find hardcoded credentials, API keys, or secrets in compiled binaries. |
| **Pentest / Code Review** | `strings application.exe | grep -iE "password|passwd|secret|key|token|auth|credential"`. |
| **AWS Keys** | `strings binary | grep -E "AKIA[0-9A-Z]{16}"`. |
| **GitHub Tokens** | `strings binary | grep "ghp_"`. |

---

### Task 3.3 — PDB Path and Compiler Artifacts

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **PDB Path** | `strings sample.exe | grep -i "\.pdb"`. Full developer file system path: `C:\Users\alice\Projects\RAT\Release\payload.pdb`. |
| **Error Messages** | Unique error strings often identify the malware family or confirm open-source base code. |
| **Version Strings** | `strings | grep -i "version\|v[0-9]\."` — may reveal software version or campaign version. |

---

### Task 3.4 — Memory Dump Analysis

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Use Case** | Run `strings` on a memory dump (from Volatility, WinPmem, or dumped from x64dbg) to find decrypted strings not visible in the original binary. |
| **Command** | `strings memory_dump.raw | grep -i "http"` → find C2 URLs that were decrypted at runtime. |
| **Critical Insight** | If the binary's strings show no C2 (encrypted at load), the memory dump's strings will show them after decryption. |

---

# PHASE 4: LIMITATIONS & ALTERNATIVES

---

### Task 4.1 — What strings Misses

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Encrypted Strings** | XOR'd, AES-encrypted, or obfuscated strings appear as garbage bytes. Not extractable statically. |
| **Short Strings** | Strings shorter than 4 chars (default) are missed. Use `-n 3` or `-n 2` but expect noise. |
| **Dynamically Built Strings** | Strings constructed byte-by-byte at runtime (char arrays built in code). Not visible until execution. |
| **Non-Printable Encoding** | Custom encoding (shifted chars, bit manipulation). Appears as non-printable — missed by `strings`. |

---

### Task 4.2 — Better Alternatives for Windows PE

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **floss (FLARE Obfuscated String Solver)** | `github.com/mandiant/flare-floss`. Goes beyond `strings` — finds statically obfuscated strings (XOR-encoded, stack-based strings, encoding loops). Run after `strings` for additional coverage. |
| **PEStudio** | For PE files: better contextualized string analysis with automatic indicator matching. |
| **FLARE VM** | Mandiant's Windows malware analysis VM includes floss + dozens of other tools pre-installed. |

---

### Task 4.3 — floss Quick Usage

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Install** | `pip install flare-floss`. |
| **Run** | `floss sample.exe` — outputs static strings, stack strings, and decoded strings (XOR etc.). |
| **Comparison** | `strings sample.exe` → 15 interesting strings. `floss sample.exe` → 15 + 32 additional decoded strings (including C2 domain hidden by XOR encoding). |

---

# PHASE 5: MASTERY CHECK

---

### Task 5.1 — Competency Self-Assessment

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Competency | Self-Assessment |
|:---|:---:|
| Can extract ASCII and Unicode strings from a binary | ☐ |
| Can grep strings output for specific IOC types | ☐ |
| Can extract C2 URLs and file paths from malware strings | ☐ |
| Understands what strings misses and why | ☐ |
| Knows when to use floss instead of or alongside strings | ☐ |
| Can run strings on memory dumps for post-decryption analysis | ☐ |

---

### Task 5.2 — Interview Questions

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

1. What does the `strings` command do and where does it fit in a malware analysis workflow?
2. Why do you need the `-el` flag when analyzing Windows PE files?
3. What types of strings does `strings` miss?
4. What is floss and how does it extend what `strings` can find?
5. How would you use `strings` to find C2 infrastructure in a binary?
6. How do you use `strings` on a memory dump to recover encrypted strings?
