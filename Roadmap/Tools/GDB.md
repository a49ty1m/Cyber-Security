# 🐛 GDB (pwndbg / GEF): Complete Mastery Checklist

> **What is GDB?** GDB (GNU Debugger) is the standard debugger for programs written in C, C++, Rust, and other compiled languages on Linux (and cross-platform via remote stub). It allows you to set breakpoints, step through code instruction-by-instruction, inspect memory and registers, disassemble functions, and observe program state at any point during execution. For exploit development and binary analysis, GDB is the primary dynamic analysis tool.
>
> **What are pwndbg and GEF?** pwndbg (by pwndbg team) and GEF (GDB Enhanced Features, by hugsy) are GDB plugins that dramatically improve the debugging experience for exploit development: better register display, heap visualization, ROP gadget search, pattern generation, context panel on every break, and dozens of exploit-dev-specific commands. You should never use vanilla GDB for exploitation work — always use one of these plugins.
>
> **Why does it exist?** Assembly-level debugging without GDB is like programming without an IDE — technically possible but insane in practice. GDB lets you understand exactly what a binary does at the machine code level, observe the state of the stack and heap during exploitation, and verify that your exploit payloads work correctly before sending them remotely.
>
> **When to use it:** Every binary exploitation task — understanding vulnerable functions, finding offsets, verifying exploit payloads, debugging crashes, heap analysis, and confirming code execution. Also used for reverse engineering binaries where Ghidra's static analysis isn't sufficient.
>
> **What mastering GDB unlocks:** Ability to debug any binary at the assembly level, the dynamic analysis foundation for all exploit development, complement to Ghidra's static analysis, and the core skill that makes pwntools exploits debuggable and reliable.
>
> **Roadmap Phase:** Phase 7 — Exploit Development & Reverse Engineering (Dynamic Debugging)

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](README.md)

| Dynamic Debugging | Binary Exploitation | Static Analysis |
|:-----------------|:-------------------|:----------------|
| **🐛 GDB** (you are here) | [🐍 pwntools](pwntools.md) | [🔭 Ghidra](Ghidra.md) |
| [🐛 x64dbg](x64dbg.md) | | |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | GDB Installation & pwndbg Setup | 4 | 1–2 hours |
| 2 | Core GDB Commands | 10 | 4–5 hours |
| 3 | pwndbg-Specific Features | 8 | 3–4 hours |
| 4 | Stack & Register Analysis for Exploitation | 8 | 4–6 hours |
| 5 | Heap Inspection | 6 | 4–5 hours |
| 6 | GDB Scripting & pwntools Integration | 5 | 3–4 hours |
| 7 | Practical Labs | 4 | 4–6 hours |
| | **Total** | **45** | **~23–32 hours** |

**Prerequisites:** Phase 7 Part 28 Stage 1 (x86-64 assembly fundamentals). Understanding of stack layout, calling conventions, and what a buffer overflow is conceptually. Linux CLI basics.

---

# PHASE 1: GDB INSTALLATION & PWNDBG SETUP

---

## 1.1 Installing GDB

```bash
# GDB is usually pre-installed on Linux
gdb --version

# If missing:
sudo apt install gdb

# Install gdb-multiarch (for cross-architecture debugging — ARM, MIPS, etc.)
sudo apt install gdb-multiarch
```

## 1.2 Installing pwndbg (Recommended for Exploit Dev)

```bash
# Install pwndbg
git clone https://github.com/pwndbg/pwndbg
cd pwndbg
./setup.sh

# pwndbg installs itself as a GDB extension in ~/.gdbinit
# Verify: start GDB and you should see the pwndbg context panel
gdb
# Should show: pwndbg> prompt and colored context panel
```

## 1.3 Installing GEF (Alternative to pwndbg)

```bash
# Install GEF
bash -c "$(curl -fsSL https://gef.blah.cat/sh)"

# Or manually:
wget -O ~/.gdbinit-gef.py https://gef.blah.cat/py
echo "source ~/.gdbinit-gef.py" >> ~/.gdbinit

# Verify: start GDB
gdb
# Should show: gef> prompt
```

> [!TIP]
> You can only have one GDB plugin active at a time. Most CTF players prefer **pwndbg** for its heap visualization and pwntools integration. GEF is more feature-rich for general debugging. Try both — choose based on workflow.

---

# PHASE 2: CORE GDB COMMANDS

---

## 2.1 Starting GDB

```bash
# Debug a binary directly
gdb ./vulnerable_binary

# Debug with arguments
gdb --args ./binary arg1 arg2

# Attach to a running process by PID
gdb -p 1234

# Debug a core dump (crash dump)
gdb ./binary core

# Run binary with input from a file or pipe
(gdb) run < /tmp/input.txt

# Run and redirect stdin/stdout
(gdb) run < <(python3 -c "print('A'*200)")
```

## 2.2 Execution Control

```bash
# Start execution
(gdb) run                  # Start from beginning (or r)
(gdb) run arg1 arg2        # Start with arguments

# Step control
(gdb) continue             # Continue execution until next breakpoint (c)
(gdb) next                 # Next source line (steps over function calls) (n)
(gdb) step                 # Step into function calls (s)
(gdb) nexti                # Next instruction (machine code level) (ni)
(gdb) stepi                # Step into at instruction level (si)
(gdb) finish               # Run until current function returns
(gdb) until 50             # Run until source line 50

# Jump to a specific address (dangerous — skips instructions)
(gdb) jump *0x401234

# Kill the running process
(gdb) kill
```

## 2.3 Breakpoints

```bash
# Break at a function
(gdb) break main           # Break at main()
(gdb) break vulnerable_function
(gdb) break *0x401234      # Break at specific address

# Break with condition
(gdb) break vuln if $rdi == 0

# Watchpoints (break when memory changes)
(gdb) watch *0x7fff1234    # Break when this address is written
(gdb) rwatch *0x7fff1234   # Break when this address is read

# List breakpoints
(gdb) info breakpoints

# Delete breakpoints
(gdb) delete 1             # Delete breakpoint #1
(gdb) delete               # Delete all breakpoints
(gdb) disable 2            # Disable without deleting

# Temporary breakpoint (fires once then deletes itself)
(gdb) tbreak main
```

## 2.4 Inspecting Registers

```bash
# Show all registers
(gdb) info registers         # All registers (abbreviated)
(gdb) info registers rip rsp rbp rdi rsi rdx   # Specific registers

# In pwndbg: registers are displayed automatically in the context panel
# Individual register:
(gdb) print $rip             # Instruction pointer
(gdb) print $rsp             # Stack pointer
(gdb) print $rax             # Return value register

# Pwndbg: show registers after context
pwndbg> regs
```

## 2.5 Inspecting Memory

```bash
# Examine memory: x/[count][format][size] address
(gdb) x/20xg $rsp          # 20 8-byte hex values starting at RSP (stack dump)
(gdb) x/10xb 0x401234      # 10 bytes in hex at address
(gdb) x/s 0x401234         # String at address
(gdb) x/i $rip             # Instruction at current IP
(gdb) x/20i 0x401234       # 20 instructions disassembly

# Format letters: x=hex, d=decimal, s=string, i=instruction, c=char
# Size letters: b=byte(1), h=halfword(2), w=word(4), g=giant/8bytes(8)

# pwndbg enhanced memory inspection
pwndbg> telescope $rsp      # Dereference pointer chains on stack
pwndbg> telescope $rsp 30   # Show 30 stack frames
pwndbg> hexdump $rsp        # Hexdump format
```

## 2.6 Disassembly

```bash
# Disassemble current function
(gdb) disassemble

# Disassemble a specific function
(gdb) disassemble main
(gdb) disassemble vulnerable_function

# Disassemble around current instruction
(gdb) disassemble $rip,+50   # 50 bytes after current RIP

# Set disassembly flavor (Intel syntax is more readable)
(gdb) set disassembly-flavor intel
# Add to ~/.gdbinit to make permanent:
# echo "set disassembly-flavor intel" >> ~/.gdbinit

# pwndbg: use `disasm` for better output
pwndbg> disasm
pwndbg> nearpc 30           # Show instructions around current PC
```

---

# PHASE 3: PWNDBG-SPECIFIC FEATURES

---

## 3.1 Context Panel

pwndbg automatically displays a context panel on every break:
```
LEGEND: STACK | HEAP | CODE | DATA | RWX | RODATA

─────────── registers ────────────────────────
 RAX  0x0               RBX  0x0
 RCX  0x7ffff7f0a0f7    RDX  0x0
 ...
─────────── disasm ───────────────────────────
 ► 0x401234 <main+0>    push rbp
   0x401235 <main+1>    mov  rbp, rsp
─────────── stack ────────────────────────────
00:0000│ rsp 0x7fffffffe468 ◂— 0x1
01:0008│     0x7fffffffe470 —▸ 0x7fffffffe6a0 ◂— 0x616d2f2e ('am/.') 
─────────── backtrace ────────────────────────
 ► f 0   0x401234 main
```

## 3.2 pwndbg Key Commands

```bash
# Stack analysis
pwndbg> stack           # Show stack contents with pointer dereferences
pwndbg> telescope $rsp  # Dereference chain from RSP
pwndbg> telescope $rbp-0x50  # Inspect local variables area

# Heap analysis
pwndbg> heap            # Show heap chunks
pwndbg> bins            # Show freelist bins (tcache, fastbin, small/large bins)
pwndbg> arena           # Show malloc arena state
pwndbg> vis_heap_chunks # Visual heap layout

# ROP gadget search
pwndbg> rop --grep "pop rdi" -- ./binary    # Find pop rdi gadgets

# Pattern generation (alternative to cyclic in pwntools)
pwndbg> cyclic 200              # Generate 200-byte pattern
pwndbg> cyclic -l 0x6161616b   # Find offset of pattern bytes

# Process info
pwndbg> vmmap           # Memory map (shows regions, permissions, files)
pwndbg> libs            # Loaded shared libraries
pwndbg> checksec        # Security properties of the binary

# Search memory
pwndbg> search -s "/bin/sh"     # Search for string in all memory
pwndbg> search -8 0xdeadbeef   # Search for 8-byte value
```

---

# PHASE 4: STACK & REGISTER ANALYSIS FOR EXPLOITATION

---

## 4.1 Finding the Overflow Offset in GDB

```bash
# Method 1: pwntools cyclic
python3 -c "from pwn import *; print(cyclic(200).decode())" > pattern.txt
gdb ./vuln
(gdb) run < pattern.txt
# Binary crashes — pwndbg shows crash state
# In pwndbg, look for the pattern bytes in RIP/RSP/RBP

# Method 2: pwndbg cyclic
pwndbg> cyclic 200
# [OUTPUT: aaaaaaaabaaaaaaacaaaa...]
pwndbg> run <<< $(cyclic 200)
# Crash — check RSP
pwndbg> cyclic -l $rsp    # Find offset directly from crash register value

# Method 3: Manual observation
# Note the address that overwrote RIP and calculate the distance from buffer start
```

## 4.2 Verifying Exploit Payloads

```python
# Add gdb debugging to your pwntools exploit:
from pwn import *

p = process('./vuln')
gdb.attach(p, gdbscript='''
    break *0x401234
    continue
''')

p.sendlineafter(b'> ', payload)
p.interactive()
```

```bash
# When attached via gdb.attach, breakpoints fire and you can inspect state:
pwndbg> telescope $rsp     # Verify your payload is on the stack correctly
pwndbg> x/20xg $rsp        # Check stack contents
pwndbg> print $rip          # Verify RIP has been overwritten with your target
```

## 4.3 Understanding Stack Frame Layout

```bash
# x86-64 stack frame during a function call:
# Before call:  caller's return address is at [RSP]
# Inside function:
#   push rbp         → [RSP] = old RBP, RSP -= 8
#   mov rbp, rsp     → RBP = RSP (new frame base)
#   sub rsp, 0x40    → RSP -= 0x40 (allocate 64 bytes for locals)
#
# Stack layout at this point:
# [RBP - 0x40]  ← start of local buffer
# [RBP - 0x30]  ← more local vars
# ...
# [RBP - 0x08]  ← usually a saved callee register
# [RBP]         ← saved old RBP value
# [RBP + 0x08]  ← RETURN ADDRESS ← this is what buffer overflow overwrites

# To find buffer-to-ret address distance:
# Offset = (distance from buffer to RBP) + 8
#        = (e.g., 0x40) + 8 = 72 bytes
```

---

# PHASE 5: HEAP INSPECTION

---

```bash
# After calling malloc/free in a vulnerable binary, inspect heap:

pwndbg> heap             # Show all allocated chunks
pwndbg> vis_heap_chunks  # Visual representation of heap

# A chunk header structure:
# prev_size (8 bytes) | size (8 bytes) | fd | bk | user data

# Chunk size field:
# - Actual size includes header, rounded up to 0x10 alignment
# - Lowest 3 bits are flags: PREV_INUSE (0x1), IS_MMAPPED (0x2), NON_MAIN_ARENA (0x4)

pwndbg> bins             # Show all freelist bins:
# tcache   (per-thread cache, 7 slots per size)
# fastbins (0x10–0x80 sized freed chunks)
# unsorted bin (recently freed larger chunks)
# small bins / large bins

# After a use-after-free or tcache poisoning exploit:
pwndbg> bins
# tcache[0x20]: 0x56789abc → 0x41414141 ← poisoned fd pointer

# Track a specific address
pwndbg> watch *0x56789abc   # Break when this chunk is accessed
```

---

# PHASE 6: GDB SCRIPTING & PWNTOOLS INTEGRATION

---

## 6.1 .gdbinit Configuration

```bash
# ~/.gdbinit — loaded automatically every time GDB starts
set disassembly-flavor intel        # Intel syntax (easier to read)
set pagination off                  # Don't pause on long output
set print pretty on                 # Pretty-print structures
set logging on                      # Log session to gdb.txt
set history save on                 # Save command history

# Source pwndbg (if not auto-loaded):
# source ~/pwndbg/gdbinit.py
```

## 6.2 GDB Scripts (Automate Debugging Steps)

```bash
# Inline gdbscript
gdb -x /tmp/debug.gdb ./vuln

# debug.gdb contents:
set disassembly-flavor intel
break main
run
telescope $rsp 20
continue
```

## 6.3 pwntools gdb.attach() Integration

```python
from pwn import *

elf = ELF('./vuln')
p = process('./vuln')

# Attach GDB to the running process with a startup script
gdb.attach(p, gdbscript=f'''
    set disassembly-flavor intel
    break *{elf.sym["vuln"]}
    continue
''')

# Your exploit code continues here — GDB opens in a new terminal
p.sendlineafter(b'> ', b'A' * 72 + p64(elf.sym['win']))
p.interactive()
```

---

# PHASE 7: PRACTICAL LABS

---

- [ ] **Lab 1 — GDB Fundamentals:** Take any compiled C program (write a simple one with a local variable, a loop, and a function call). Set 5 different types of breakpoints (address, function name, condition, watchpoint). Step through execution at both source and instruction level. Inspect registers, memory, and the call stack. Know every command needed from memory.

- [ ] **Lab 2 — Stack Overflow Debugging:** Take a vulnerable binary (protostar exercises, pwnable.kr, or compile your own). Run it with a cyclic pattern in GDB/pwndbg. Use `cyclic -l` to find the exact offset. Verify the payload overwrites RIP with your target address. Confirm code execution in the debugger before running against the remote target.

- [ ] **Lab 3 — Heap Visualization:** Write a C program that mallocs, frees, and mallocs again. Compile it and debug with pwndbg. Use `heap`, `vis_heap_chunks`, and `bins` to observe the heap state at each step. Manually trigger tcache to return a freed chunk and observe it in pwndbg.

- [ ] **Lab 4 — ret2libc with GDB:** Take the ret2libc exploit from pwntools.md Phase 4.2. Debug every step with GDB: confirm the ROP gadget addresses, verify the stack layout before `puts` is called, capture the leaked libc address, calculate the base, and confirm `system("/bin/sh")` executes. Write a paragraph explaining every step of the exploit in plain English.

---

## 📝 Operational Notes

- **pwndbg vs GEF choice:** pwndbg is better for heap exploitation (superior `vis_heap_chunks` and `bins` output). GEF has a better `got` command and more comprehensive format string analysis. For CTF binary exploitation, pwndbg is the community default.
- **`set follow-fork-mode child`:** When the binary forks (e.g., network services that fork per connection), GDB by default follows the parent. Set `follow-fork-mode child` to follow the child process that handles your connection.
- **PIE and ASLR:** With ASLR enabled, every run puts the binary at a different address. Disable for initial development: `echo 0 | sudo tee /proc/sys/kernel/randomize_va_space`. For PIE binaries, pwndbg shows the rebased addresses automatically after the binary loads.
- **`$rip` vs `$pc`:** `$pc` is the architecture-neutral alias for the program counter (works on x86, ARM, MIPS, etc.). `$rip` is x86-64 specific. Use `$pc` in portable scripts.
- **`info proc mappings`:** Shows the full virtual memory map of the running process — equivalent to `cat /proc/PID/maps`. Use this to find the base addresses of loaded libraries (essential for ret2libc when you don't have a leak primitive).
