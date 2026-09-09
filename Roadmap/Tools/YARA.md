# 🦠 YARA: Complete Mastery Checklist

> **What is YARA?** YARA is an open-source pattern matching tool designed to identify and classify malware. It works by matching binary patterns (byte sequences, strings, regex) against files, directories, or memory. A YARA rule describes the characteristics of a malware family or suspicious artifact — and YARA scans anything you point it at to find matches. YARA is the standard tool for malware analysts, threat intelligence teams, and incident responders worldwide.
>
> **Why does it exist?** Hash-based detection (matching a file's MD5/SHA256) breaks the moment malware recompiles or modifies a single byte. YARA's pattern-based approach is more resilient — a rule targeting the malware's algorithm, string constants, or bytecode patterns can survive minor modifications and catch entire malware families.
>
> **When to use it:** Malware analysis (identify a sample's family), memory forensics (scan RAM dumps for injected code), threat hunting (scan file systems for IOCs), incident response (check all files on a compromised host), and SIEM integration (Splunk, Wazuh, and Elastic all support YARA scanning).
>
> **When to avoid it:** YARA is slow on large filesystems without optimizations. For scanning billions of files at scale, use commercial platforms (VirusTotal, Malwarebytes Intelligence) that run YARA in parallel. For network-level detection of live malware traffic, Suricata with its YARA-like rule language is more appropriate.
>
> **What mastering YARA unlocks:** Malware family identification, threat hunting capability, memory forensics integration with Volatility, the ability to write high-fidelity IOC signatures that resist malware evasion, and contribution to threat intelligence sharing platforms (MISP, VirusTotal).
>
> **Roadmap Stage / Module:** Stage 3: Side-Track A (Detection Engineering) & Shelf: Module S05

---

## 🧭 Navigation

> [🏠 Master Roadmap](../README.md) · [🔧 Tools Index](README.md)

| Detection Rules | Malware Analysis | Memory Forensics | SIEM |
|:---------------|:----------------|:-----------------|:-----|
| [🔎 Sigma](Sigma.md) | **🦠 YARA** (you are here) | [🧠 Volatility](Volatility.md) | [📊 Splunk](Splunk.md) |
| | [🔬 Ghidra](Ghidra.md) | [🔬 Autopsy](Autopsy.md) | [🐺 Wazuh](Wazuh.md) |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Installation & First Scan | 4 | 1 hour |
| 2 | Rule Syntax & String Types | 8 | 3–4 hours |
| 3 | Conditions & Modifiers | 8 | 3–4 hours |
| 4 | Writing Rules from Malware Samples | 7 | 4–6 hours |
| 5 | Memory Scanning & Volatility Integration | 5 | 3–4 hours |
| 6 | Advanced Techniques & Evasion | 5 | 3–4 hours |
| 7 | Practical Labs | 4 | 5–8 hours |
| | **Total** | **41** | **~22–31 hours** |

**Prerequisites:** Phase 1 complete (Linux CLI, hex fundamentals). Phase 3 Sigma basics recommended. Phase 7 reverse engineering basics helpful for writing malware-specific rules.

---

# PHASE 1: INSTALLATION & FIRST SCAN

---

## 1.1 Installation

```bash
# Debian/Ubuntu
sudo apt install yara

# Install with all modules (recommended — enables PE, ELF, math, hash modules)
sudo apt install yara libyara-dev

# From source (latest version)
sudo apt install automake libtool make gcc pkg-config libssl-dev libjansson-dev libmagic-dev
git clone https://github.com/VirusTotal/yara.git
cd yara
./bootstrap.sh && ./configure --with-crypto --enable-magic --enable-cuckoo
make && sudo make install

# Python bindings (for scripting)
pip3 install yara-python

# Verify
yara --version
```

## 1.2 Running YARA

```bash
# Scan a single file with a rule file
yara rule.yar malware_sample.exe

# Scan a directory recursively
yara -r rule.yar /path/to/scan/

# Scan with multiple rule files
yara rule1.yar rule2.yar target.exe

# Scan a compiled ruleset (faster for large rule sets)
yarac rules/*.yar compiled.rules
yara compiled.rules target.exe

# Print only matching strings (verbose output)
yara -s rule.yar target.exe

# Scan all running processes
yara rule.yar $(ls /proc | grep "^[0-9]" | xargs)
# Or more cleanly:
sudo yara -r rules.yar /proc/*/mem 2>/dev/null
```

---

# PHASE 2: RULE SYNTAX & STRING TYPES

---

## 2.1 Basic Rule Structure

```yara
rule RuleName : tag1 tag2
{
    meta:
        author      = "Your Name"
        description = "Detects XYZ malware family"
        date        = "2024-01-01"
        reference   = "https://example.com/analysis"
        hash1       = "abc123..."          // Known sample hash
        mitre       = "T1059.001"

    strings:
        $string1 = "malicious_string"
        $string2 = { 4D 5A 90 00 }        // Hex bytes (MZ header)
        $regex1  = /mal[a-z]{3}re/         // Regular expression

    condition:
        $string1 or $string2
}
```

## 2.2 String Types

### Text Strings

```yara
strings:
    // Simple case-sensitive string
    $s1 = "CreateRemoteThread"

    // Case-insensitive (catches CreateRemoteThread, createremotethread, etc.)
    $s2 = "powershell" nocase

    // Wide string (UTF-16 — how Windows stores most strings)
    $s3 = "mimikatz" wide

    // Both ASCII and wide variants
    $s4 = "cmd.exe" ascii wide

    // Full word match (won't match "CreateRemoteThreadEx")
    $s5 = "VirtualAlloc" fullword

    // XOR-obfuscated strings (YARA 4.0+ — tries XOR with keys 0x01–0xFF)
    $s6 = "http://" xor

    // Combine modifiers
    $s7 = "sekurlsa" nocase wide fullword
```

### Hex Byte Patterns

```yara
strings:
    // Exact byte sequence
    $h1 = { 4D 5A 90 00 03 00 00 00 }     // PE/MZ header

    // Wildcards (any single byte)
    $h2 = { 8B 45 ?? 89 45 ?? }           // MOV pattern with variable offsets

    // Range wildcards (between N and M bytes)
    $h3 = { 90 [2-4] 90 }                  // NOP, 2-4 bytes, NOP

    // Alternatives (OR between bytes)
    $h4 = { ( 6A 40 | 68 00 10 00 00 ) }   // Either PUSH 0x40 or PUSH 0x1000

    // Combination
    $h5 = { 55 8B EC 83 EC ?? 56 57 }      // Common function prologue
```

### Regular Expressions

```yara
strings:
    // IPv4 address pattern
    $r1 = /\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/

    // Base64 encoded payload (high-entropy block)
    $r2 = /[A-Za-z0-9+\/]{50,}={0,2}/

    // Windows registry path
    $r3 = /HKEY_[A-Z_]+\\[\\a-zA-Z0-9 ]+/

    // Hex-encoded shellcode prefix
    $r4 = /\\x[0-9a-fA-F]{2}(\\x[0-9a-fA-F]{2}){10,}/
```

---

# PHASE 3: CONDITIONS & MODIFIERS

---

## 3.1 Core Condition Operators

```yara
condition:
    // All strings must match
    $s1 and $s2 and $s3

    // Any string matches
    $s1 or $s2

    // File must NOT contain this string
    not $badstring

    // Counting: at least 2 of these strings
    2 of ($s1, $s2, $s3)

    // All strings from a set
    all of ($suspicious_*)

    // Any string from a set
    any of ($indicator_*)

    // Count how many times a string appears
    #s1 > 5     // String $s1 appears more than 5 times

    // File size constraints
    filesize < 1MB
    filesize > 500KB
```

## 3.2 Position-Based Conditions

```yara
condition:
    // String must appear at a specific offset
    $mz_header at 0

    // String must appear within first 1024 bytes
    $shellcode in (0..1024)

    // String must appear in last 512 bytes
    $footer in (filesize-512..filesize)

    // Offset arithmetic: string at position of another string + offset
    $s1 at @s2 + 10
```

## 3.3 PE Module (For Windows Executables)

```yara
import "pe"

rule SuspiciousPE
{
    condition:
        // PE file with no sections
        pe.number_of_sections == 0

        // Unsigned PE (no valid Authenticode signature)
        and not pe.is_signed

        // PE imports CreateRemoteThread
        and pe.imports("kernel32.dll", "CreateRemoteThread")

        // PE has suspicious section names
        and for any section in pe.sections : (
            section.name == ".text" and
            section.characteristics & pe.SECTION_MEM_EXECUTE and
            section.characteristics & pe.SECTION_MEM_WRITE
        )

        // Compilation timestamp is 0 (stripped) or far in the past
        and (pe.timestamp == 0 or pe.timestamp < 1000000000)
}
```

## 3.4 Math & Hash Modules

```yara
import "math"
import "hash"

rule HighEntropySection
{
    condition:
        // File section has high entropy (likely packed/encrypted)
        for any section in pe.sections : (
            math.entropy(section.raw_data_offset, section.raw_data_size) > 7.5
        )
}

rule KnownBadHash
{
    condition:
        // MD5 matches a known-bad hash
        hash.md5(0, filesize) == "d41d8cd98f00b204e9800998ecf8427e"
}
```

---

# PHASE 4: WRITING RULES FROM MALWARE SAMPLES

---

## 4.1 Rule Writing Methodology

1. **Get the sample safely:** Download from MalwareBazaar, theZoo, ANY.RUN (sandboxed). Always work in an isolated VM.
2. **Static analysis first:** Run `strings`, `file`, `readpe`, `exiftool`. Identify unique strings, imports, sections.
3. **Identify distinguishing features:** What makes this malware unique? Hard-coded C2 domains, mutex names, registry keys, unique bytecode patterns.
4. **Write the rule targeting unique features:** Avoid generic Windows API strings that would fire on clean files.
5. **Test against clean files:** Run against `C:\Windows\System32\` — it should produce zero matches.
6. **Test against malware family samples:** Run against other variants of the same family — it should catch them all.

## 4.2 Extracting Indicators with `strings`

```bash
# Extract printable strings (min 8 chars)
strings -n 8 malware.exe

# Extract Unicode strings (Windows PE is often UTF-16)
strings -el -n 8 malware.exe

# Filter for interesting patterns
strings malware.exe | grep -E "(https?://|\.onion|cmd\.exe|powershell|CreateRemoteThread|VirtualAlloc|\\\\PIPE\\\\)"

# View imports (what DLLs/functions the PE uses)
objdump -p malware.exe | grep "DLL Name\|Name:"
# Or use readpe
readpe --imports malware.exe
```

## 4.3 Example: Mimikatz Detection

```yara
rule Mimikatz_Generic
{
    meta:
        description = "Detects Mimikatz credential dumper by unique strings"
        author      = "Example"
        reference   = "https://github.com/gentilkiwi/mimikatz"
        tags        = "credential_access, T1003.001"

    strings:
        $s1 = "sekurlsa::logonpasswords" nocase ascii wide
        $s2 = "lsadump::dcsync" nocase ascii wide
        $s3 = "kerberos::golden" nocase ascii wide
        $s4 = "mimikatz" nocase ascii wide fullword
        $s5 = "gentilkiwi" nocase ascii wide     // Author's name — in the binary
        $s6 = { 6D 69 6D 69 6B 61 74 7A }        // "mimikatz" in hex

        // LSASS credential extraction pattern
        $h1 = { 33 FF 45 85 C0 41 89 75 00 4C 8B E3 }

    condition:
        2 of ($s*) or $h1
}
```

---

# PHASE 5: MEMORY SCANNING & VOLATILITY INTEGRATION

---

## 5.1 Scanning Memory Dumps with YARA

```bash
# Scan a full RAM dump with YARA rules
yara -r malware_rules.yar /path/to/memory.raw

# Scan only the first 1GB of a large dump
yara malware_rules.yar memory.raw --max-process-memory-chunk=1000000000

# Scan a specific process memory dump (from Volatility malfind output)
yara malware_rules.yar pid_1234.dmp
```

## 5.2 Volatility + YARA Integration

```bash
# Scan all process memory in a Volatility dump with YARA rules
python3 vol.py -f memory.raw windows.yarascan --yara-rules malware.yar

# Scan for a specific string pattern across all process memory
python3 vol.py -f memory.raw windows.yarascan --yara-string "sekurlsa"

# Scan only specific process by PID
python3 vol.py -f memory.raw windows.yarascan --yara-file mimikatz.yar --pid 1234
```

## 5.3 Live Process Memory Scanning

```bash
# Scan all running processes on a live Linux system
sudo yara -r rules.yar /proc/ --scan-list <(ls /proc | grep "^[0-9]" | while read pid; do echo "/proc/$pid/mem"; done) 2>/dev/null

# Faster: using yara directly on process IDs
for pid in $(ls /proc | grep "^[0-9]"); do
  sudo yara rules.yar /proc/$pid/mem 2>/dev/null && echo "HIT in PID $pid"
done
```

---

# PHASE 6: ADVANCED TECHNIQUES & EVASION

---

## 6.1 YARA Rule Performance Optimization

```yara
// Fast rules — put cheap conditions first
rule FastRule
{
    strings:
        $mz = { 4D 5A }           // Check MZ header first (cheap)
        $s  = "CreateRemoteThread" // String match (expensive)
    condition:
        $mz at 0 and $s            // MZ check eliminates non-PE files immediately
}
```

## 6.2 Anti-Evasion Techniques

```yara
// XOR-obfuscated strings (YARA 4.0+ xor modifier)
rule XorObfuscatedC2
{
    strings:
        // Tries all XOR keys 0x01–0xFF automatically
        $url = "http://" xor(0x01-0xff)
        $ps  = "powershell" xor(0x01-0xff) nocase
    condition:
        any of them
}

// Packed/encrypted binary detection (entropy-based)
rule PackedBinary
{
    condition:
        // PE file where the first section has entropy > 7.5 (very high — likely packed)
        pe.number_of_sections >= 1
        and math.entropy(pe.sections[0].raw_data_offset, pe.sections[0].raw_data_size) > 7.5
        and filesize < 5MB    // Small packed stub
}
```

---

# PHASE 7: PRACTICAL LABS

---

- [ ] **Lab 1 — MalwareBazaar Hunt:** Download 5 malware samples from MalwareBazaar (in an isolated VM). Run `strings` on each. Identify unique identifying strings for each sample. Write a YARA rule for each. Verify each rule matches its target sample but produces no hits on `C:\Windows\System32\` or `/usr/bin/`.

- [ ] **Lab 2 — Family Rule:** Download 3 variants of the same malware family (e.g., 3 different Emotet samples). Write a single YARA rule that matches all 3 variants but none of the clean reference set. Document what shared characteristic your rule targets (bytecode pattern, string, import pattern).

- [ ] **Lab 3 — Volatility + YARA:** Take a memory dump (from one of your lab attack simulations or a public CTF memory image). Write a YARA rule targeting a known running process (e.g., Meterpreter's staged stager pattern). Use `vol.py windows.yarascan` to find the rule match and identify the infected process.

- [ ] **Lab 4 — Wazuh/Splunk Integration:** Deploy your custom YARA rules in Wazuh's Active Response or the Splunk YARA app. Trigger a detection by placing a file matching one of your rules in a monitored directory. Confirm the alert fires with the correct YARA rule name and file path.

---

## 📝 Operational Notes

- **YARA is not AV:** YARA requires you to write the rules. It won't detect anything you haven't explicitly described. It is a *precision tool*, not a broad-spectrum scanner.
- **False positive management:** Generic rules (matching common API strings) will fire on clean software. Always test against a clean reference set before deployment. The quality of a YARA rule is measured by its specificity.
- **Rule sets to study:** Florian Roth's `signature-base` repository (3000+ rules), THOR YARA rules, ESET malware detection rules, Mandiant's public rules. Study how professional analysts write rules.
- **`yarGen`:** A tool that automatically suggests YARA string candidates from malware samples by comparing against a clean baseline. Not a replacement for manual analysis, but a good starting point: `python3 yarGen.py -m malware/ --excludegood --minscore 70`.
- **VirusTotal YARA hunt:** VirusTotal's Hunting feature allows running YARA rules across all newly submitted samples in real-time. This is how threat intelligence teams catch new malware matching known family patterns before public disclosure.
