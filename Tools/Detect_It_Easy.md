# 🧬 Detect It Easy (DiE): Complete Reference

> **What is Detect It Easy?** Detect It Easy (DiE) is a free, cross-platform tool for identifying the packer, compiler, linker, and protector used to build a PE (or ELF/Mach-O) executable. It analyzes the binary's structure, sections, headers, and byte signatures to determine: "Was this compiled with Visual C++ 2019? Was it packed with UPX? Is it protected with Themida?" DiE answers these questions in seconds, using a large, community-maintained signature database plus heuristic analysis.
>
> **When to use it:** First step in any packed binary analysis — before attempting to unpack in x64dbg, know what packer you're dealing with. Identifying the compiler (helps narrow down the language and SDK). Understanding the protection layer. Prioritizing analysis effort: well-known packer → use existing unpackers. Custom packer → manual analysis required.
>
> **Tier 4 Reminder:** Understand the output, know the common packers/compilers, and be able to use DiE findings to guide your next steps.

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals | 4 | 1–2 hours |
| 2 | Using DiE | 5 | 2–3 hours |
| 3 | Interpreting Results | 4 | 2–3 hours |
| 4 | DiE in the Analysis Workflow | 3 | 1–2 hours |
| 5 | Mastery Check | 2 | 30 min |
| | **Total** | **18** | **~7–11 hours** |

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — What DiE Detects

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Compilers** | Visual C++ (MSVC), GCC, MinGW, Delphi, Borland, Go, Rust, Python (compiled), .NET/Mono. Each leaves distinct artifacts in the PE header and sections. |
| **Packers** | UPX, MPRESS, ASPack, PECompact, LZMA-based packers. Packers compress/encrypt the original code and add a stub that unpacks at runtime. |
| **Protectors** | Themida, VMProtect, Enigma Protector, Obsidium. More complex than packers — add anti-debug, virtualization, and code obfuscation layers. |
| **Linkers** | Microsoft Linker, LLVM Linker. |
| **Overlays and Certificates** | Detects embedded self-extractors, digital signature presence. |

---

### Task 1.2 — Installation

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Download** | `github.com/horsicq/Detect-It-Easy` → Releases → download for your platform. |
| **Versions** | `die.exe` — GUI. `diec.exe` — CLI (Windows). `diec` — CLI (Linux). Both available in the same release package. |
| **Linux** | `apt install detect-it-easy` (Kali). Or download AppImage. |

---

### Task 1.3 — DiE vs. PEStudio

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **PEStudio** | Full PE analysis: imports, strings, resources, sections, VirusTotal. Packer detection is one indicator among many. |
| **DiE** | Focused specifically on packer/compiler/linker identification. More accurate and comprehensive detection than PEStudio for this specific task. More signature database coverage. |
| **Use Together** | PEStudio → first pass analysis (imports, strings, VT score). DiE → definitive packer/compiler identification. Together = complete first-pass picture. |

---

### Task 1.4 — Detection Methodology

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Signatures** | DiE maintains `db/` directory of JavaScript signature scripts. Each script implements detection logic for one packer/compiler. Community-contributed and regularly updated. |
| **Heuristics** | Beyond signatures: entropy analysis, section name patterns, entry point code patterns, import table structure. |
| **Confidence** | DiE reports confidence: "UPX(3.95) [NRV2E, brute] 100%" = very certain. "Possible: compiler=MSVC" = less certain. |

---

# PHASE 2: USING DiE

---

### Task 2.1 — GUI Analysis

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Load File** | Drag and drop PE file onto DiE window. Or File → Open. Results appear immediately. |
| **Main Results** | Top area: packer/compiler/linker detected with confidence level. Tabs: Info (raw detection data), Sections (section entropy + characteristics), Memory map, Strings, Hex view. |
| **Entropy Graph** | Visualizes entropy per section — spikes indicate encrypted/compressed data. |

---

### Task 2.2 — CLI Analysis

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Single File** | `diec sample.exe` → prints detection result. |
| **Directory Scan** | `diec -r /path/to/samples/` — recursively scan all files. |
| **JSON Output** | `diec --json sample.exe` — machine-parseable output. |
| **CSV** | `diec --csv sample.exe`. |
| **Automation** | `diec --json sample.exe | python3 parse_die.py` — feed into analysis pipeline. |

---

### Task 2.3 — Batch Analysis

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Identify the packer distribution across a malware sample set. |
| **Command** | `for f in samples/*; do echo "$f: $(diec $f)"; done`. |
| **Use Case** | "Of 50 samples from this campaign, 35 used UPX and 15 used custom packers." Guides analysis prioritization — UPX-packed → quick unpack. Custom → harder analysis. |

---

### Task 2.4 — Entropy Tab

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **View** | GUI → Entropy tab → graph of entropy across the file. |
| **Interpretation** | High entropy throughout = packed/encrypted. High entropy in specific section only = that section contains encrypted data. Normal entropy with one spike = embedded payload or resource. |
| **Numbers** | 0–5: low entropy (text, normal code). 5–7: moderate (compiled code). 7–8: high (compressed/encrypted). |

---

### Task 2.5 — Signature Browsing

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand what signatures DiE uses so you can interpret results accurately. |
| **Location** | `db/PE/` — PE format signatures. `db/ELF/` — Linux. `db/MACH/` — macOS. Each `.js` file = one detector. |
| **Custom Signatures** | Write your own JavaScript signature file following DiE's API. Add to `db/PE/` → DiE picks it up. Useful for detecting custom in-house malware. |

---

# PHASE 3: INTERPRETING RESULTS

---

### Task 3.1 — Common Compilers and What They Mean

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **MSVC (Microsoft Visual C++)** | Most Windows malware. Rich reverse engineering resources. Ghidra decompiles well. |
| **GCC/MinGW** | Cross-platform malware. Also very common. |
| **Delphi/Borland** | Banking trojans frequently use Delphi. Different calling conventions — note in Ghidra. |
| **.NET** | DiE detects .NET assemblies. Use dnSpy/ILSpy instead of Ghidra for .NET — decompiles to near-original C#. |
| **Go** | Many modern C2 implants (Sliver, etc.) are written in Go. Large binary size. Standard library statically linked. |
| **Rust** | Emerging in malware. Rust binaries are harder to reverse. |
| **Python (compiled)** | PyInstaller, cx_Freeze. Extract `.pyc` files with pyinstxtractor. |

---

### Task 3.2 — Common Packers and Response

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **UPX** | Most common packer. `upx -d sample.exe` → instant unpack. Unpacked binary → open in Ghidra. |
| **MPRESS** | Simple unpacker available. `mpress -d` or use x64dbg (OEP approach). |
| **ASPack** | x64dbg unpack (find OEP + Scylla). |
| **Themida / VMProtect** | Commercial protectors. Very hard to unpack. Often requires: x64dbg + Anti-anti-debug → dump + manual import fix. Significant time investment — deprioritize if other samples are available. |
| **Custom / Unknown** | "Possible packer" or "Unknown". Requires manual dynamic analysis in x64dbg. Watch memory allocation → find OEP. |

---

### Task 3.3 — .NET Binary Handling

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **DiE Detects** | ".NET 4.8" or "Microsoft Visual C#" → it's a .NET assembly. |
| **Don't Use Ghidra First** | Ghidra can analyze .NET but it's harder. Use dnSpy or ILSpy — these decompile .NET IL (Intermediate Language) to near-perfect C# source code. |
| **If Obfuscated** | .NET obfuscators (ConfuserEx, de4dot targets). De4dot (`github.com/de4dot/de4dot`) deobfuscates many common .NET protectors. |

---

### Task 3.4 — When DiE Can't Identify

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Unknown Result** | DiE says "Unknown" or gives low-confidence results. |
| **Next Steps** | Check PEStudio entropy (high = packed). Manual entry point analysis in x64dbg. Submit to unpac.me or any.run sandbox — automated unpacking. Try generic unpackers (Universal PE Unpacker plugin for x64dbg). |
| **Accept Limitations** | Some custom packers/protectors will defeat DiE. Document "custom/unknown packer" and proceed with dynamic analysis. |

---

# PHASE 4: DiE IN THE ANALYSIS WORKFLOW

---

### Task 4.1 — Triage Integration

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Position in Workflow** | `strings` (30 sec) → PEStudio (3–5 min) → DiE (1 min) → decide: unpack → Ghidra → x64dbg. DiE tells you *how* to proceed to the next stage. |
| **Decision** | UPX detected → `upx -d` → Ghidra. Custom packer → x64dbg first. .NET detected → dnSpy. Python/PyInstaller → pyinstxtractor. |

---

### Task 4.2 — Family Clustering

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Use compiler/packer info to group related samples. |
| **Pattern** | "All samples in this campaign: MinGW compiled, UPX packed, version 3.95" → same build environment → likely same actor. Change in packer/compiler across campaigns → possible actor change or tool refresh. |

---

### Task 4.3 — Updating DiE Signatures

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Built-in Update** | DiE has an online update feature for its signature database. Settings → Update. |
| **Manual** | `git pull` in the DiE repository → copy updated `db/` directory. |
| **New Packers** | If you encounter a frequently recurring unknown packer, write a detection script and contribute to the DiE project. |

---

# PHASE 5: MASTERY CHECK

---

### Task 5.1 — Competency Self-Assessment

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Competency | Self-Assessment |
|:---|:---:|
| Can identify packer, compiler, and protector from DiE output | ☐ |
| Knows the appropriate unpack/analysis approach for common packers | ☐ |
| Can run DiE from CLI and parse JSON output | ☐ |
| Can interpret the entropy graph | ☐ |
| Knows when to use DiE vs. PEStudio for packer identification | ☐ |
| Understands how DiE fits in the malware analysis workflow | ☐ |

---

### Task 5.2 — Interview Questions

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

1. What does Detect It Easy identify and how does it differ from PEStudio?
2. What are packers and why do malware authors use them?
3. What is the difference between a packer and a protector (like Themida or VMProtect)?
4. How do you unpack a UPX-packed binary?
5. What should you use to analyze a .NET binary instead of Ghidra?
6. Where does DiE fit in a complete malware analysis workflow?
7. How do you use DiE for batch analysis of a malware sample collection?
