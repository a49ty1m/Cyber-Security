# 👻 Ghidra: Complete Mastery Checklist

> **What is Ghidra?** Ghidra is a free, open-source software reverse engineering (SRE) framework developed and released by the NSA. It disassembles and decompiles binary executables — converting compiled machine code into readable assembly and pseudo-C code — enabling analysis of malware, finding vulnerabilities in closed-source software, and understanding how binaries behave. It supports x86, x64, ARM, MIPS, PowerPC, and many other architectures.
>
> **Why does it exist?** IDA Pro — the industry standard for reverse engineering — costs thousands of dollars. Ghidra fills the gap as a free, powerful alternative. While IDA Pro remains more mature for some workflows, Ghidra's decompiler output is excellent, it handles large binaries well, and it is scriptable in Java and Python.
>
> **When to use it:** Analyzing malware without running it (static analysis). Finding vulnerabilities in closed-source binaries. Reverse engineering firmware. CTF reverse engineering challenges. Understanding proprietary protocols from captured binaries.
>
> **What mastering Ghidra unlocks:** Static malware analysis. Vulnerability research in closed-source software. CTF reversing challenges. Understanding binary behavior without source code. The foundation of serious malware analysis and vulnerability research.
>
> **Roadmap Phase:** Phase 7 (Malware Analysis and Reverse Engineering)

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals | 4 | 2–3 hours |
| 2 | Ghidra Interface | 5 | 3–4 hours |
| 3 | Analysis | 5 | 4–6 hours |
| 4 | Decompiler | 4 | 3–4 hours |
| 5 | Scripting | 3 | 3–4 hours |
| 6 | Malware Analysis | 4 | 4–6 hours |
| 7 | Practical Labs | 4 | 5–8 hours |
| 8 | Mastery Challenges | 3 | 4–6 hours |
| | **Total** | **32** | **~28–41 hours** |

**Prerequisites:** x86/x64 assembly basics. C programming fundamentals. Understanding of calling conventions, stack frames, and binary formats (PE, ELF).

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — Binary Analysis Concepts

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Static Analysis** | Analyze binary without executing it. Safe. Ghidra is primarily a static analysis tool. |
| **Dynamic Analysis** | Execute and observe behavior. x64dbg, OllyDbg. Required for understanding runtime behavior, obfuscated code, packer analysis. |
| **Disassembly** | Convert machine code bytes → assembly instructions (mov, push, call, jmp). Shows the exact CPU instructions. |
| **Decompilation** | Convert assembly → pseudo-C/pseudocode. Higher-level, easier to understand. Not exact — compiler produces different-looking assembly. |
| **Binary Formats** | PE = Windows executables (.exe, .dll). ELF = Linux executables. Macho = macOS. Ghidra handles all. |

---

### Task 1.2 — Installation

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Download** | `ghidra.re` → Download → ghidra_X.X_PUBLIC.zip. |
| **Java** | Requires JDK 17+. `apt install openjdk-17-jdk`. |
| **Run** | `./ghidraRun` (Linux/macOS). `ghidraRun.bat` (Windows). |
| **Kali** | `apt install ghidra`. |

---

### Task 1.3 — Project and Program Concepts

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Project** | Container for all binaries and analysis under one engagement/investigation. Create one project per malware sample or CTF challenge. |
| **Program** | Individual binary loaded into a project. |
| **Analysis** | Ghidra automatically analyzes on import: identifies functions, strings, imports, cross-references. |

---

### Task 1.4 — x86-64 Assembly Crash Course

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Registers** | `rax/eax/ax` — return value, general purpose. `rdi/esi/edx/ecx/r8/r9` — function arguments (Linux). `rcx/rdx/r8/r9` — function arguments (Windows). `rsp` — stack pointer. `rbp` — base pointer. `rip` — instruction pointer. |
| **Common Instructions** | `mov dst, src` — copy. `push reg` — push to stack. `pop reg` — pop from stack. `call func` — call function (push return addr, jmp). `ret` — return (pop return addr, jmp). `cmp a, b` — compare. `jz/je` — jump if zero/equal. `jnz/jne` — jump if not zero. `lea dst, [addr]` — load effective address. |
| **Stack** | Stack grows down. Local variables below rbp. Parameters above rbp (or in registers on x64). |

---

# PHASE 2: GHIDRA INTERFACE

---

### Task 2.1 — Main Windows

- [ ] **Completed** · ⭐ Beginner · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Code Browser** | Main analysis window. Toolbar access all sub-windows. |
| **Listing (Disassembly)** | Assembly view. Address | bytes | instruction format. |
| **Decompiler** | Pseudo-C view. Shows alongside or separately. Updates as cursor moves in listing. |
| **Symbol Tree** | Left panel: namespace tree. Functions, imports, exports, labels. |
| **Program Trees** | Memory segments (.text, .data, .rdata, etc.). |
| **Data Type Manager** | Type library. Import VS header types, Windows API types. |

---

### Task 2.2 — Importing a Binary

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Import** | File → Import File → select binary. Or drag-drop. |
| **Format** | Ghidra auto-detects PE/ELF/Macho. Confirm format, language (x86 64-bit), compiler (Visual C++, GCC). |
| **Analyze** | After import: "Analyze?" dialog → Yes. Auto-analysis runs (function identification, string detection, type recovery). Takes 30–120 seconds. |

---

### Task 2.3 — Navigation

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Go To** | `G` key — enter address or symbol name. Navigate to any address instantly. |
| **Back/Forward** | Alt+← / Alt+→ — browser-like history navigation. |
| **Symbols** | Symbol Tree → Functions → double-click to navigate to function. |
| **Cross-References** | Right-click → References → Show References to Address. See all callers of a function. |
| **Keyboard** | `Space` — toggle between listing and decompiler. |

---

### Task 2.4 — Functions Window

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **List** | Window → Functions. All identified functions: name, address, size. |
| **Sort** | Sort by name, address, or size. Large functions = complex logic. |
| **Undefined** | Functions Ghidra couldn't name show as `FUN_00401234`. Rename as you understand them. |
| **Entry Point** | `entry` function — program start. Work from here for packed binaries. |

---

### Task 2.5 — Strings Window

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Open** | Window → Defined Strings. All ASCII and Unicode strings in the binary. |
| **Filter** | Type in filter box: search for `http`, `password`, `cmd`, `regkey`, `C2`, `.exe`. |
| **Navigate** | Double-click any string → navigate to it in listing. See cross-references → what code uses this string. |
| **High Value** | URLs (C2 addresses). Registry keys (persistence). Command strings. Error messages (reveal functionality). Encoded strings (suspicious — may be obfuscated). |

---

# PHASE 3: ANALYSIS

---

### Task 3.1 — Import and Export Analysis

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Imports** | Symbol Tree → Imports. What Windows API functions the binary calls. `CreateProcess` = process execution. `InternetConnect` = network connectivity. `RegCreateKey` = registry operations. `VirtualAlloc` = memory allocation (code injection). `WriteProcessMemory` = process injection. |
| **Exports** | Symbol Tree → Exports. Functions exported for use by other code. DLL analysis. |
| **Value** | Import list gives a high-level behavior profile before reading a single instruction. |

---

### Task 3.2 — Finding main() and WinMain()

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Entry Point** | `entry` function in Symbol Tree. For Windows: often `__start` → calls `__mainCRTStartup` → calls `WinMain`. |
| **Find main** | Search for the function that takes expected main arguments. Or: in the CRT startup code, the last `call` before `ExitProcess` is usually `main`/`WinMain`. |
| **Rename** | Double-click function name in listing or decompiler → rename to `main`. |

---

### Task 3.3 — Cross-References and Call Graph

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **XREFs to** | Right-click address/function → References → Show References to. See every place this is called/used. |
| **XREFs from** | Right-click → References → Show References from. See everything this function calls. |
| **Call Tree** | Window → Function Call Trees. Visual graph of function calls. |
| **Use** | Trace execution flow. Find who calls a suspicious function. Find all uses of a string. |

---

### Task 3.4 — Renaming and Commenting

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Rename Function** | Click function name → press `L` → enter new name. Propagates everywhere it's referenced. |
| **Rename Variable** | In decompiler: click variable → `L` → rename. |
| **Comment** | `Semicolon` key → add end-of-line comment. `;` at any address. |
| **Plate Comment** | Function header comment: `;` before function → plate comment (shows at top of function). |
| **Discipline** | Rename everything you understand. Add comments for behavior. Ghidra analysis is incremental — work through functions systematically. |

---

### Task 3.5 — Data Type Assignment

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Right-click → Data** | Right-click on data address → Data → apply type (DWORD, WORD, string, struct). |
| **Struct** | Create custom struct in Data Type Manager → apply to data region → Ghidra renders it as structured fields. |
| **Win32 Types** | Import Windows header types: Data Type Manager → Open File Archive → windows_vs12_32.gdt or similar. Apply `STARTUPINFOA`, `PROCESS_INFORMATION`, etc. |

---

# PHASE 4: DECOMPILER

---

### Task 4.1 — Reading Decompiler Output

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Quality** | Ghidra's decompiler produces high-quality pseudo-C. Not exact — compiler transforms code significantly. Goal: understand behavior, not recover original source. |
| **Variables** | Local variables named `local_XX` initially. Rename after understanding. |
| **Types** | Initially `undefined4`, `undefined8`. Assign proper types after analysis. |
| **Casts** | Heavy casting is normal. Ghidra is conservative about types. |

---

### Task 4.2 — Common Patterns

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **String Decryption** | Loop over byte array with XOR, ROT, or AES → produces cleartext string. Common malware obfuscation. Identify the key and algorithm → decrypt manually or script. |
| **API Hashing** | Malware resolves API functions by hash rather than name to evade import analysis. See: iterate export table, compute hash, compare → call the resolved function. Identify the hash algorithm → find what API is being resolved. |
| **Process Injection** | `VirtualAllocEx` → `WriteProcessMemory` → `CreateRemoteThread`. Classic injection pattern. |
| **Registry Persistence** | `RegOpenKey(HKEY_LOCAL_MACHINE, ...)` → `RegSetValue(RunKey, ...)`. Startup persistence. |

---

### Task 4.3 — Handling Obfuscation

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Packing** | Packed binary: most code is a loader. Small import table. Compressed main code section. Strategy: run in a sandbox → dump unpacked binary from memory (Hollows Hunter). Then analyze dumped binary in Ghidra. |
| **String Encryption** | Find the decryption function (called repeatedly) → understand it → write Ghidra script to decrypt all strings. |
| **Control Flow Flattening** | Complex switch-statement-like control flow to confuse decompiler. Manual analysis of each case. |

---

### Task 4.4 — Debugging Assistance

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Ghidra Debugger** | Ghidra 10+ has a built-in debugger. Connect to a running process. Set breakpoints. Step through. Updates decompiler view in real time. |
| **DWARF Symbols** | If available (Linux binaries with debug symbols): Ghidra loads function names and variable types automatically. Much easier analysis. |

---

# PHASE 5: SCRIPTING

---

### Task 5.1 — Ghidra Script Basics

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Languages** | Java (native), Python 2 (via Jython). Python 3 not yet fully supported in built-in scripting (use GhidraScript bridge or external tools). |
| **Script Manager** | Window → Script Manager. Browse, run, create scripts. |
| **API** | `currentProgram` — current binary. `currentAddress` — cursor address. `getFunction(addr)` — get function at address. `getFunctionContaining(addr)` — function containing address. `createBookmark(addr, "type", "desc")`. |

---

### Task 5.2 — Decrypting Strings Automatically

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Goal** | Find XOR-encrypted string array → write script to decrypt all strings → annotate each with the cleartext. |
| **Approach** | Identify the XOR key from decompiler. Script: iterate over each call to decrypt function → get arguments (encrypted bytes + key) → decrypt → add comment at each call site. |

---

### Task 5.3 — pyhidra / Ghidrathon

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **pyhidra** | Python 3 bridge to Ghidra's Java API. `pip install pyhidra`. Full Python 3 ecosystem available (requests, capstone, pwntools) with Ghidra API access. |
| **Ghidrathon** | NSA's official Python 3 scripting extension for Ghidra. Replaces Jython. Install from GitHub. |
| **Use** | Write Python 3 scripts to automate bulk analysis: iterate all functions, apply types, decrypt strings, output reports. |

---

# PHASE 6: MALWARE ANALYSIS

---

### Task 6.1 — Initial Triage Workflow

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Step 1** | Check imports: what API families are called? (network, filesystem, registry, process, crypto). |
| **Step 2** | Strings window: URLs, IP addresses, commands, error messages, registry keys. |
| **Step 3** | Entry point → main function → core logic. |
| **Step 4** | Rename and annotate as you go. |
| **Output** | Behavioral profile: what the malware does, key IOCs, C2 addresses if visible. |

---

### Task 6.2 — C2 Communication Analysis

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Find Network Calls** | `InternetOpenUrl`, `HttpSendRequest`, `WSAConnect`, `connect` → trace back to find what URL/IP is used. |
| **Encoded Strings** | If URL is encrypted: find decryption routine → script to decrypt → reveal C2 address. |
| **Beacon Logic** | Find the sleep call → what interval? → what's sent to the C2 in each beacon? |

---

### Task 6.3 — Persistence Mechanisms

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Registry** | Cross-reference `RegSetValue` calls → find which key. `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` = user-level startup. `HKLM\...Run` = system-level. |
| **Scheduled Task** | `ITaskService`, `COM` calls to Task Scheduler. |
| **Service** | `CreateService`, `OpenSCManager` calls. |
| **Startup Folder** | Writes to `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup`. |

---

### Task 6.4 — Evasion Techniques

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Anti-Debug** | `IsDebuggerPresent`, `CheckRemoteDebuggerPresent`, timing checks, `OutputDebugString` trick. Find these → understand how the malware detects analysis. |
| **Anti-VM** | CPUID checks, registry key checks for VMware/VirtualBox artifacts (`HKLM\SOFTWARE\VMware, Inc.`), MAC address checks. |
| **API Unhooking** | Reads NTDLL from disk to get clean (unhooked) copy of syscall stubs. Bypasses EDR hooks. |

---

# PHASE 7: PRACTICAL LABS

---

### Lab 7.1 — Analyze a Crackme

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 45 min

| **Scenario** | Download a "crackme" binary (from crackmes.one). Load into Ghidra. Find the correct password or serial number using static analysis only. Identify the check function. Understand the algorithm. |
| **Success Criteria** | Correct input found via Ghidra static analysis. Check algorithm documented. |

---

### Lab 7.2 — Analyze Simple Malware

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 60 min

| **Scenario** | Analyze a known malware sample (from MalwareBazaar or a CTF). Identify: C2 addresses, persistence mechanism, main payload functionality. Write a malware analysis report. |
| **Success Criteria** | C2 addresses extracted. Persistence mechanism identified. Behavior report written. |

---

### Lab 7.3 — CTF Reversing Challenge

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 45 min

| **Scenario** | CTF reversing challenge (HTB, picoCTF, CryptoHack). Use Ghidra exclusively for static analysis. Find the flag. |
| **Success Criteria** | Flag found via Ghidra. Complete methodology documented. |

---

### Lab 7.4 — String Decryption Script

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 60 min

| **Scenario** | Malware sample with XOR-encrypted strings. Write a Ghidra script that: identifies the decryption function, extracts all encrypted string arguments, decrypts them, and annotates each call site with the cleartext string. |
| **Success Criteria** | All encrypted strings decrypted and annotated automatically. Script reusable. |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — Full Malware Report

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 120 min

| **Scenario** | Analyze a real-world malware sample end-to-end. Write a professional malware analysis report covering: file metadata, imports analysis, string analysis, behavioral analysis (functionality, C2, persistence, evasion), IOCs, and YARA signature. |
| **Success Criteria** | Professional report suitable for a security team. YARA signature created and tested. |

---

### Challenge 8.2 — Vulnerability Discovery

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 120 min

| **Scenario** | Analyze a closed-source binary for vulnerabilities. Find: buffer overflows, format string bugs, integer overflows. Write a PoC demonstrating the vulnerability. |
| **Success Criteria** | Vulnerability identified statically. PoC written and tested. |

---

### Challenge 8.3 — Unpack and Analyze

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 90 min

| **Scenario** | Packed malware sample. Identify the packer. Unpack (in sandbox → dump from memory). Analyze the unpacked binary. Compare what's visible before vs. after unpacking. |
| **Success Criteria** | Successfully unpacked. Full analysis of unpacked binary. Comparison documented. |

---

# 📋 FINAL COMPETENCY MATRIX

| Competency | Self-Assessment |
|:---|:---:|
| Can import a binary and run analysis in Ghidra | ☐ |
| Can navigate the interface: listing, decompiler, symbol tree, strings | ☐ |
| Can identify imports and build a behavioral profile | ☐ |
| Can find and rename main(), functions, and variables | ☐ |
| Can trace cross-references to understand code flow | ☐ |
| Can identify common malware patterns in decompiler output | ☐ |
| Can write a Ghidra script to automate analysis | ☐ |
| Can identify C2, persistence, and evasion in malware | ☐ |
| Can solve CTF reversing challenges using Ghidra | ☐ |
| Can write a professional malware analysis report | ☐ |

---

## 🎯 Interview Questions

1. What is the difference between disassembly and decompilation?
2. What does the import table tell you about malware behavior?
3. How do you find the main() function in a compiled Windows binary?
4. What is API hashing and why do malware authors use it?
5. How do you decrypt XOR-encrypted strings in Ghidra?
6. What are cross-references and how do you use them in analysis?
7. What are the signs of a packed binary and how do you handle it?
8. How do you identify process injection in a binary's disassembly?
9. What scripting languages does Ghidra support and what can you automate?
10. How would you write a YARA rule based on a Ghidra analysis?
