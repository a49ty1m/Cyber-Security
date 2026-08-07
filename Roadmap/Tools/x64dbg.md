# 🪲 x64dbg: Complete Mastery Checklist

> **What is x64dbg?** x64dbg is a free, open-source x64/x32 debugger for Windows. It allows you to run a binary in a controlled way — pausing at any instruction (breakpoints), inspecting registers and memory at any point, stepping through code instruction by instruction, and modifying execution flow. Combined with Ghidra (static analysis), x64dbg provides the dynamic analysis layer: see actual runtime values, bypass anti-analysis tricks, unpack packed malware, and understand behavior that static analysis can't reveal.
>
> **Why does it exist?** OllyDbg was the classic 32-bit Windows debugger. x64dbg is its modern replacement — supports both x64 and x32, actively maintained, highly extensible via plugins (ScyllaHide for anti-anti-debug, xAnalyzer, etc.), and has a clean, intuitive UI.
>
> **When to use it:** Analyzing malware at runtime. Unpacking packed executables. Bypassing anti-debug tricks. Understanding obfuscated code that decompilers can't handle. Patching binaries. Dynamic CTF reversing when static analysis isn't enough.
>
> **What mastering x64dbg unlocks:** Dynamic malware analysis. Unpacking any packed executable. Runtime value inspection. Bypassing anti-analysis. Complete binary patching capability.

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals | 4 | 2–3 hours |
| 2 | Interface | 4 | 2–3 hours |
| 3 | Breakpoints | 4 | 2–3 hours |
| 4 | Memory Analysis | 4 | 3–4 hours |
| 5 | Anti-Debug | 3 | 2–3 hours |
| 6 | Unpacking | 3 | 3–5 hours |
| 7 | Practical Labs | 4 | 5–8 hours |
| 8 | Mastery Challenges | 3 | 4–6 hours |
| | **Total** | **29** | **~23–35 hours** |

**Prerequisites:** x86/x64 assembly. Windows PE format basics. Ghidra (static analysis). Run in a VM (malware analysis sandbox).

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — Static vs. Dynamic Analysis

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Static** | Ghidra. Read code without executing. Safe. Can't see runtime values, encrypted strings, or dynamic API calls. |
| **Dynamic** | x64dbg. Run the code, pause it, inspect it. Sees actual runtime values. Required for: packed malware, obfuscated code, encrypted strings decrypted at runtime. |
| **Combined** | Start with Ghidra for overview → switch to x64dbg for runtime verification of specific functions. Jump between both constantly. |

---

### Task 1.2 — Installation

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Download** | `x64dbg.com` → download. Extracts to a folder. No installer. |
| **x64dbg.exe** | 64-bit debugger. |
| **x32dbg.exe** | 32-bit debugger. Use when analyzing 32-bit binaries. |
| **VM** | ALWAYS analyze malware in an isolated VM (no host connectivity). Take a snapshot before debugging. |

---

### Task 1.3 — Plugins

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **ScyllaHide** | Anti-anti-debug plugin. Hides debugger presence from most detection techniques. Automatically applied. Essential for malware analysis. |
| **Scylla** | Imports fixer. Rebuilds import table for dumped executables. |
| **xAnalyzer** | Automatic analysis and annotation. |
| **Install** | Extract plugin DLL to x64dbg plugins directory. Appears in Plugins menu. |

---

### Task 1.4 — Debugger Concepts

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Breakpoint** | Tells debugger: pause execution when this instruction is about to execute. |
| **Step Into** | Execute one instruction. If it's a `call`: follow into the called function. |
| **Step Over** | Execute one instruction. If it's a `call`: run the whole function and pause on the next instruction. |
| **Step Out** | Run until the current function returns. Pause at the return instruction's destination. |
| **Run** | Execute until the next breakpoint (or program end). |

---

# PHASE 2: INTERFACE

---

### Task 2.1 — Main Windows

- [ ] **Completed** · ⭐ Beginner · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **CPU** | Main view: top-left = disassembly. Top-right = registers. Bottom-left = stack. Bottom-right = memory (hex dump). |
| **Graph** | Control flow graph of current function (similar to Ghidra's graph view). |
| **Log** | Debug log: API calls, breakpoints hit, exceptions. |
| **Breakpoints** | List of all set breakpoints. Enable/disable/delete. |
| **Memory Map** | All memory regions of the process: .text, .data, heap, stack, DLL sections. |
| **Symbols** | All functions/exports from loaded modules. |

---

### Task 2.2 — Opening a Binary

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Open** | File → Open → select binary. Or drag-drop. |
| **Attach** | File → Attach → select running process ID. Attach to a running process. |
| **Pause** | Binary paused at entry point on load. |
| **Arguments** | File → Change Command Line → set command line arguments before starting. |

---

### Task 2.3 — Registers Panel

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Registers** | RAX, RBX, RCX, RDX, RBP, RSP, RSI, RDI, R8-R15, RIP. Highlighted in red = changed since last step. |
| **Flags** | ZF (zero flag), CF (carry), SF (sign), OF (overflow). Used by conditional jumps. |
| **RIP** | Instruction pointer — current instruction address. |
| **Right-click** | Right-click register → "Follow in Dump" → see memory at that address. "Set Value" → modify register. |

---

### Task 2.4 — Stack Panel

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **View** | Stack grows downward. Top = current RSP value (most recently pushed). |
| **Function Args** | On a `call`: parameters pushed to stack (x86) or in registers (x64 — first 4 in RCX, RDX, R8, R9). |
| **Return Address** | After `call`, return address on top of stack. |
| **Right-click** | Follow value in dump, set breakpoint on stack address. |

---

# PHASE 3: BREAKPOINTS

---

### Task 3.1 — Software Breakpoints

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Set** | Click address in disassembly → press `F2`. Or right-click → Add Breakpoint. |
| **On Symbol** | Ctrl+G → type function name (e.g., `CreateProcessA`) → F2 to set breakpoint. |
| **Conditional** | Right-click → Add Conditional Breakpoint → only break when condition is true (e.g., `eax == 1`). |
| **Clear** | Click the red dot in disassembly → F2 again. Or: Breakpoints tab → delete. |

---

### Task 3.2 — Hardware Breakpoints

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Purpose** | Hardware breakpoints are set in CPU debug registers (DR0-DR3). Not modifiable by the program. Undetectable by most anti-debug checks (unlike software BP which writes 0xCC). |
| **Set** | Right-click address → Hardware Breakpoint → On Execute. |
| **Limit** | Maximum 4 hardware breakpoints simultaneously. |

---

### Task 3.3 — Memory Breakpoints

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Purpose** | Break when a memory address is read from or written to. |
| **Set** | In memory dump: select bytes → right-click → Breakpoint → Memory → Read/Write. |
| **Use** | Find what code accesses a specific buffer. Track when an encrypted string is decrypted. |

---

### Task 3.4 — API Breakpoints

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Find API** | Ctrl+G → type API name: `VirtualAlloc`, `CreateRemoteThread`, `WinExec`, `RegSetValue`. |
| **Set BP** | F2 on the API → break every time it's called. |
| **Inspect** | When hit: inspect registers for arguments. RCX = first arg, RDX = second arg (x64). |
| **Common BPs** | `VirtualAlloc` (memory allocation), `WriteProcessMemory` (injection), `CreateThread` (new thread), network functions, crypto functions. |

---

# PHASE 4: MEMORY ANALYSIS

---

### Task 4.1 — Dump Memory

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **View** | Memory Map → find interesting region (heap, newly allocated section) → right-click → Dump to File. |
| **Follow in Dump** | Right-click register/address → Follow in Dump → see memory at that address in hex dump. |
| **Search** | In dump: Ctrl+B → search for byte pattern. Ctrl+F → search for string. |

---

### Task 4.2 — Finding Decrypted Strings

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Approach** | Encrypted string in binary → breakpoint on decryption function → run → break → inspect destination buffer in dump → decrypted string visible. |
| **Memory Search** | After decryption: Ctrl+F in dump → search for expected plaintext. |

---

### Task 4.3 — Shellcode Analysis

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Find** | Breakpoint on `VirtualAlloc` → break → note returned memory address (RAX) → run → break on `memcpy`/`WriteProcessMemory` → observe shellcode being written → breakpoint on that address → step through shellcode. |
| **Annotate** | Follow shellcode in disassembly. Navigate to allocated address. |

---

### Task 4.4 — Modifying Registers and Memory

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Modify Register** | Right-click register → Set Value → enter new value. Change EAX return value to bypass a check. |
| **Modify Memory** | In dump → double-click byte → edit. Patch a byte to NOP out a check. |
| **Zero Flag** | Right-click ZF in flags → Toggle → change conditional jump outcome. |

---

# PHASE 5: ANTI-DEBUG

---

### Task 5.1 — IsDebuggerPresent

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Detection** | `IsDebuggerPresent` → checks PEB.BeingDebugged flag. Returns 1 if debugger present. |
| **Bypass** | ScyllaHide patches this automatically. Or: BP on `IsDebuggerPresent` → when hit → set RAX=0 → NOP the check. Or: PEB → manually set BeingDebugged byte to 0 (`fs:[30h]` in x86, `gs:[60h]` in x64). |

---

### Task 5.2 — Timing Checks

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Detection** | Malware records timestamp → executes code → records second timestamp → if elapsed time > threshold (debugger slows execution): exit. `GetTickCount`, `QueryPerformanceCounter`. |
| **Bypass** | ScyllaHide patches timing functions. Or: BP after timing check → set return value to 0. |

---

### Task 5.3 — ScyllaHide Plugin

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Enable** | Plugins → ScyllaHide → Options → enable all anti-anti-debug features. |
| **Covers** | IsDebuggerPresent, CheckRemoteDebuggerPresent, NtQueryInformationProcess, timing checks, heap flags, OutputDebugString trick, and more. |
| **Essential** | Always enable ScyllaHide when analyzing modern malware. Without it, many samples immediately exit on detecting the debugger. |

---

# PHASE 6: UNPACKING

---

### Task 6.1 — Identifying Packed Binaries

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Signs** | Small import table (only LoadLibrary, GetProcAddress). Encrypted/compressed sections. DetectItEasy identifies packer. UPX, MPRESS, custom packers. |
| **Ghidra** | Most code is a stub. Only unpacker code visible. Main payload absent. |

---

### Task 6.2 — OEP Finding and Dumping

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Concept** | Packer decompresses/decrypts original code to memory → jumps to OEP (Original Entry Point). Dump memory at that moment. |
| **Find OEP** | Set BP on `VirtualAlloc`/`VirtualProtect`. Run. When unpacked: often a `jmp` or `push retn` to OEP. Follow the tail call. Or: ESP trick (hardware BP on stack → run → break when stack returns to original value). |
| **Dump** | At OEP: Scylla plugin → Dump → saves process memory to file. |

---

### Task 6.3 — Import Table Reconstruction

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Problem** | Dumped binary has broken import table (packer hasn't restored it). |
| **Scylla** | Plugins → Scylla → IAT Autosearch → Find Imports → Fix Dump. Rebuilds the import table from the running process's resolved imports. |
| **Result** | Loadable, analyzable binary with correct imports. Open in Ghidra for further static analysis. |

---

# PHASE 7: PRACTICAL LABS

---

### Lab 7.1 — Crackme Debugging

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| **Scenario** | Open a crackme binary in x64dbg. Find the serial check function (identified in Ghidra). Set breakpoint. Enter a test serial. Step through the check logic. Find the comparison. Extract the expected value. |
| **Success Criteria** | Correct serial found via dynamic analysis. Check logic documented. |

---

### Lab 7.2 — Anti-Debug Bypass

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| **Scenario** | Binary with IsDebuggerPresent and timing checks. Without ScyllaHide: observe the binary exiting. Enable ScyllaHide. Binary runs normally. Identify where the anti-debug checks occur. Document each one and how ScyllaHide patches it. |
| **Success Criteria** | Anti-debug identified. Bypassed with ScyllaHide. Each check documented. |

---

### Lab 7.3 — Unpack and Analyze

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 60 min

| **Scenario** | UPX-packed malware sample. Identify packing (DIE). Debug → find OEP → dump with Scylla → fix imports → open unpacked binary in Ghidra. Compare pre/post unpacking analysis. |
| **Success Criteria** | Unpacked binary loaded in Ghidra. Import table reconstructed. Full analysis possible on unpacked binary. |

---

### Lab 7.4 — Runtime String Extraction

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| **Scenario** | Malware with encrypted strings. Use x64dbg to break after decryption. Extract decrypted strings from memory. Compare against Ghidra's static view (should be encrypted). Document the decryption routine. |
| **Success Criteria** | All encrypted strings decrypted at runtime. Decryption algorithm identified and documented. |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — Full Malware Analysis (Dynamic)

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 120 min

| **Scenario** | Real malware sample (in VM). Full dynamic analysis: unpack → bypass anti-debug → trace API calls → capture network strings → identify persistence mechanism → document C2 communication → extract IOCs. |
| **Success Criteria** | Professional malware analysis report combining Ghidra static + x64dbg dynamic findings. All IOCs listed. |

---

### Challenge 8.2 — Binary Patch

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| **Scenario** | Binary with a license check (`cmp result, 1; jne exit`). Patch the binary: change `jne` to `jmp` (always jump to success). Save patched binary. Verify it runs without the license check. |
| **Success Criteria** | Patched binary runs without license check. Patch location and technique documented. |

---

### Challenge 8.3 — Custom Packer Analysis

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 90 min

| **Scenario** | Malware with custom packer (not UPX, not standard). Use x64dbg to: identify the unpacking loop, locate the OEP, dump the unpacked binary, reconstruct the import table. Ghidra analysis of unpacked binary. |
| **Success Criteria** | Custom packer analyzed. Unpacked binary recovered and analyzable. Unpacking algorithm documented. |

---

# 📋 FINAL COMPETENCY MATRIX

| Competency | Self-Assessment |
|:---|:---:|
| Can open a binary, set breakpoints, and step through code | ☐ |
| Can read registers and inspect stack during execution | ☐ |
| Can set API breakpoints and inspect function arguments | ☐ |
| Can modify registers and memory to alter execution flow | ☐ |
| Can bypass IsDebuggerPresent and timing checks | ☐ |
| Can use ScyllaHide effectively | ☐ |
| Can unpack a UPX-packed binary with Scylla | ☐ |
| Can extract decrypted strings from runtime memory | ☐ |
| Can patch binary instructions to bypass checks | ☐ |
| Can combine Ghidra and x64dbg for complete malware analysis | ☐ |

---

## 🎯 Interview Questions

1. What is the difference between static and dynamic analysis?
2. How do hardware breakpoints differ from software breakpoints?
3. How do you bypass IsDebuggerPresent in x64dbg?
4. What is the OEP and why is it important for unpacking?
5. How do you dump a packed process and reconstruct its imports?
6. How do you find decrypted strings in runtime memory?
7. How do you patch a binary to bypass a license check?
8. What is ScyllaHide and what does it protect against?
9. What API calls do you break on first when analyzing malware?
10. How does x64dbg complement Ghidra in a malware analysis workflow?
