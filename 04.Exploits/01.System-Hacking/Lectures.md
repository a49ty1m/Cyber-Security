# System Hacking — Credential Attack Tooling (Lecture Notes)

> Ethics + legality: Use these techniques only on systems you own or have explicit written permission to test.
> This file is written for learning, password auditing, and incident-response password recovery in controlled labs.

## What is System Hacking?

System hacking is the process of gaining access to a system (and potentially maintaining that access) by exploiting weaknesses such as poor credentials, misconfigurations, unpatched software, or unsafe user behavior.

In professional/security contexts, you study this to:

- Audit password strength and authentication controls
- Understand how attackers operate
- Improve defenses (MFA, rate-limits, logging, strong hashing, least privilege)

## Scope of this file

This document focuses on **credential attack tooling** (wordlist generation + offline hash recovery + online login testing in authorized scenarios).
For the full system-hacking methodology (phases, goals, persistence, defense evasion, etc.), see [Notes.md](Notes.md).

## Quick map (what to use, when)

- **Need candidate passwords?** → Crunch (generate wordlists / patterns)
- **Have hashes and want CPU cracking?** → John the Ripper
- **Have hashes and want GPU cracking?** → Hashcat
- **Testing a live login service (online)?** → Hydra (very noisy; lockouts are common)
- **Legacy unsalted hashes only?** → Rainbow tables (mostly obsolete today)

---

## Key concepts (short + exam-friendly)

- **Offline vs online attacks**
    - *Offline:* You already have hashes (from a dump / audit export). Cracking happens on your machine. Fast, stealthy.
    - *Online:* You send login attempts to a real service. Slow, noisy, triggers alerts/lockouts.
- **Hash vs encryption**
    - *Hash:* One-way (password storage). You “guess” and compare.
    - *Encryption:* Reversible with a key (different problem).
- **Salt**
    - Random value added before hashing. Defeats rainbow tables and forces per-password work.
- **Slow hashes**
    - bcrypt/scrypt/Argon2 intentionally slow down guessing (this is good defense).
- **Wordlist vs mask vs rules**
    - *Wordlist:* test known/common passwords first (fastest wins).
    - *Mask:* test structured guesses like `Word + 2 digits + symbol` without generating giant files.
    - *Rules:* transform wordlists to mimic human variations (capitalize, append years, leetspeak).
- **Password spraying vs brute-force (online)**
    - *Spraying:* one/few common passwords across many accounts (lower lockout risk).
    - *Brute-force:* many passwords against one account (higher lockout risk, more obvious).

---

## Quick workflow (practical)

### Offline password audit / recovery (hashes already obtained legally)

1. **Identify the hash type** (Hashcat `--identify`, John `--list=formats`, tool-specific docs).
2. Start with **wordlist + rules** (fast wins).
3. If you know the structure, use **masks/hybrids** (more targeted than full brute-force).
4. Use **sessions/restore** for long runs (Hashcat `--session/--restore`, John `--restore`).
5. Export results (`--show`) and write remediation notes (MFA, better hashing, lockouts, password policy).

### Where wordlists and rules often live (Linux)

- Common shared paths:
    - `/usr/share/wordlists/`
    - `/usr/share/john/`
    - `/usr/share/hashcat/`
- Helpful discovery commands:

```bash
ls -la /usr/share/wordlists 2>/dev/null
ls -la /usr/share/john 2>/dev/null
ls -la /usr/share/hashcat 2>/dev/null
```

### Placeholders used in commands (so you can copy/paste safely)

Anything inside `<...>` is a placeholder: replace it with your own value.

- `<HASHFILE>`: a file containing hashes (e.g., `hashes.txt`)
- `<WORDLIST>` / `<wordlist.txt>`: candidate passwords list (one per line)
- `<HASH_TYPE>`: Hashcat hash-mode ID (e.g., `1000` for NTLM, etc.)
- `<ATTACK_MODE>`: Hashcat attack mode (e.g., `0` dictionary, `3` mask, `6` wordlist+mask)
- `<mask>`: a structured pattern like `?l?l?l?d?d` (see the Hashcat section)
- `<rules.rule>`: a rules file used to transform wordlists
- `<FORMAT_NAME>`: John “format” name (use `john --list=formats`)
- `<NAME>`: a short session name (used by Hashcat `--session`)
- `<service>`: Hydra service/module name (shown by `hydra -U`)
- `<TARGET_HOST>`: a host/IP you are explicitly authorized to test

John “file extract” placeholders you’ll see:

- `<archive.zip>`: path to a protected archive you are auditing

Hydra placeholders you’ll see:

- `<USER>`: single username
- `<PASS>`: single password
- `<USERS.txt>`: list of usernames (one per line)
- `<PASSLIST.txt>`: list of passwords (one per line)
- `<COMBOS.txt>`: `user:pass` combos file (one per line)
- `<N>`: number of threads (parallel attempts)
- `<SEC>`: seconds (delay/timeout)
- `<PORT>`: port number (if non-default)
- `<OUT.txt>`: output file for results

Crunch placeholders you’ll see:

- `<min_len>` / `<max_len>`: minimum/maximum candidate length to generate

If you don’t have wordlists installed, use smaller, legal, curated lists first and/or build org-specific lists (names, seasons, years, patterns).

---

## 1) Crunch — targeted wordlist generator

### What it is

Crunch is a wordlist generator that creates password candidates by combining characters across a length range, or by generating **patterned** candidates (useful when you know the password structure/policy).

### When to use

- You need a **custom wordlist** based on a known policy (length/charset) or a known human pattern.
- You want to **generate candidates** for an audit without relying on generic wordlists.
- You want to quickly estimate **how big** a brute-force space is (Crunch will report size/line count in many cases).

### Why to use

- Gives you **precise control** over what gets generated (length range, charset, pattern templates).
- Useful when you have partial knowledge (prefix/suffix, year patterns, naming rules).

### How to use

1. Decide the **min/max length** you actually want to test.
2. Choose a **charset** (digits only, loweralpha, custom set, etc.).
3. If you know the structure, use **pattern mode** (`-t`) instead of full brute-force.
4. Think about feasibility: if the keyspace is huge, avoid writing it to disk.

Pattern mode placeholders (common ones):

- `@` lowercase, `,` uppercase, `%` digits, `^` symbols
- Any other character in the pattern is literal.

### Commands

Install + verify:

```bash
sudo apt update
sudo apt install -y crunch
crunch -h
```

General syntax:

```bash
crunch <min_len> <max_len> [charset] [options]
```

Generate a fixed-length set from a custom charset (writes to a file):

```bash
crunch 6 6 0123456789abcdef -o 6chars.txt
```

Generate a patterned set (example: literal prefix + 2 digits + 1 uppercase):

```bash
crunch 7 7 -t user%%,
```

### Why not to use

- **Exponential growth**: full keyspaces become impractical very fast (disk + time).
- **Disk/I/O cost**: writing huge lists wastes time; prefer mask/rule generation inside the cracking tool.
- **Pipeline bottlenecks**: piping Crunch into a fast cracker can be slower than native candidate generation.

---

## 2) John the Ripper (JtR) — offline CPU password cracking

### What it is

John the Ripper is an offline password auditing/recovery tool (primarily CPU-focused) that can test password guesses against captured hashes and supports many formats and converters.

### When to use

- You have **hashes offline** and want CPU-based auditing/recovery.
- You want quick wins using **single crack + rules** (human-pattern guessing).
- You need to handle many “weird” formats via `*2john` converters (ZIP/PDF/SSH keys/etc.).
- You’re in a constrained environment (no GPU / limited drivers).

### Why to use

- Very flexible and widely used for **password auditing**.
- Strong “smart” modes (especially single crack + rules).
- Large ecosystem of converters that turn protected files into John-readable hashes.

### How to use

1. Get the target data into a **hash file** John can load.
2. If format is ambiguous, identify/force it with `--list=formats` + `--format=...`.
3. Start with **wordlist + rules** (high ROI) before brute-force.
4. Resume long runs with `--restore`, and export results with `--show`.

### Commands

Install + verify:

```bash
sudo apt update
sudo apt install -y john
john --version
```

List formats and basic help:

```bash
john --help
john --list=formats
```

Common wordlists on many Linux installs (paths vary):

```bash
ls -la /usr/share/john 2>/dev/null
```

Combine Linux passwd+shadow for auditing (admin / lab only):

```bash
sudo unshadow /etc/passwd /etc/shadow > mypasswd
```

Run John (defaults pick a sensible sequence):

```bash
john <HASHFILE>
```

Wordlist + rules (common starting point):

```bash
john --wordlist=<WORDLIST> --rules <HASHFILE>
```

Force a format when needed:

```bash
john --format=<FORMAT_NAME> <HASHFILE>
```

Show recovered entries:

```bash
john --show <HASHFILE>
```

Resume an interrupted session:

```bash
john --restore
```

Extract hashes from protected files (example):

```bash
zip2john <archive.zip> > <HASHFILE>
```

### Why not to use

- CPU-only cracking is often **much slower** than GPU-based approaches for many hash types.
- Some modern hashes are intentionally slow (bcrypt/scrypt/Argon2): brute-force is usually a bad strategy.
- Jumbo/OpenCL setups can be finicky depending on distro/drivers (if you go the GPU route).

---

## 3) THC-Hydra — online login testing (very noisy)

### What it is

Hydra is an online login testing tool that attempts credential combinations against **live** network services (SSH/FTP/HTTP/etc.) to validate weak credentials in authorized scenarios.

### When to use

- You have explicit authorization to test a **live login service** for weak credentials.
- You’re validating **rate-limiting / lockout / monitoring** controls (defender-focused testing).
- You’re checking for **default credentials** on devices/services you own/manage.

### Why to use

- Supports many network authentication protocols and can run attempts in parallel.
- Useful for controlled verification of password-policy controls (lockouts, throttling, alerting).
- Offers session restore and result logging.

### How to use

1. Confirm scope + permission, and understand lockout policy (to avoid outages).
2. Identify the exact service/module (SSH/FTP/HTTP form/etc.) and required auth method.
3. Start **slow** (low parallelism, add delays) and monitor logs/alerts while testing.
4. Treat this as a **validation tool**: stop once you’ve proven a weakness and document it.

### Commands

Install + verify:

```bash
sudo apt update
sudo apt install -y hydra
hydra -h | head
```

See supported services and module-specific options:

```bash
hydra -U
hydra -U <service>
```

Useful flags to know (reference):

- `-t <N>` threads per target
- `-W <SEC>` delay between connects per thread (throttling)
- `-w <SEC>` response timeout
- `-s <PORT>` custom port
- `-o <OUT.txt>` write found pairs
- `-R` restore a previous session

Generic syntax template (authorized testing only):

```bash
hydra [[[-l <USER>|-L <USERS.txt>] [-p <PASS>|-P <PASSLIST.txt>]] | [-C <COMBOS.txt>]] -t <N> -W <SEC> -o <OUT.txt> <service>://<TARGET_HOST>
```

### Why not to use

- Extremely **noisy**: often triggers IDS/WAF/SIEM alerts.
- Can cause **account lockouts** and service disruption.
- Cannot bypass MFA, CAPTCHAs, or dynamic CSRF protections.
- High risk of misuse; only appropriate for explicitly authorized testing.

---

## 4) Hashcat — offline GPU password recovery

### What it is

Hashcat is an offline password recovery/auditing tool designed to run high-speed attacks against password hashes, usually accelerated by GPUs.

### When to use

- You have **hashes offline** and want fast auditing/recovery.
- You have a compatible GPU and need performance for large audits.
- You want structured attacks (masks/hybrids/rules) without generating massive wordlist files.

### Why to use

- Extremely fast on supported hardware (GPUs) and supports many hash types.
- Strong support for mask/hybrid/rule-based strategies.
- Good “quality-of-life” features for long runs (sessions, restore, status, potfile).

### How to use

1. Put hashes into a file (`hashes.txt`) in the right format for the hash type.
2. Identify the **hash mode** (`-m`). If the mode is wrong, results will never match.
3. Start with **wordlist + rules**, then move to masks/hybrids if needed.
4. Use a named session so you can resume (`--session` + `--restore`).
5. Review recovered entries with `--show` and document findings.

### Commands

Install + verify:

```bash
sudo apt update
sudo apt install -y hashcat
hashcat -V
```

Check device detection + benchmark:

```bash
hashcat -I
hashcat -b
```

Help with hash modes / identification:

```bash
hashcat -h           # use -hh for the full list
hashcat --example-hashes
hashcat --identify <HASHFILE>
```

General syntax:

```bash
hashcat -m <HASH_TYPE> -a <ATTACK_MODE> <HASHFILE> (<WORDLIST> | <mask>) [options]
```

Useful “session” flags:

- `--session <NAME>` name a run
- `--restore` resume
- `--status --status-timer=5` periodic status output
- `--show` show recovered entries (from the potfile)
- `--left` show uncracked entries

Built-in mask charsets you’ll see a lot:

- `?l` lowercase, `?u` uppercase, `?d` digits, `?s` symbols, `?a` = `?l?u?d?s`

Example masks (structure only):

```text
?u?l?l?l?l?l?l?d?d     # 7 letters starting uppercase + 2 digits
?l?l?l?l?l?d?d?d?s     # 5 lowercase + 3 digits + 1 symbol
```

Attack templates (authorized auditing/recovery):

```bash
# Dictionary
hashcat -a 0 -m <HASH_TYPE> <HASHFILE> <WORDLIST>

# Dictionary + rules
hashcat -a 0 -m <HASH_TYPE> <HASHFILE> <WORDLIST> -r <rules.rule>

# Mask (structured brute-force)
hashcat -a 3 -m <HASH_TYPE> <HASHFILE> <mask>

# Hybrid (wordlist + mask suffix)
hashcat -a 6 -m <HASH_TYPE> <HASHFILE> <WORDLIST> <mask>
```

### Why not to use

- Requires correct `-m` and correct input formatting (steeper learning curve than some tools).
- GPU/driver issues can block you, and sustained runs can cause heat/throttling.
- Slow hashes (bcrypt/scrypt/Argon2) limit brute-force feasibility by design.

---

## 5) Rainbow tables — precomputation for legacy hashes

### What it is

Rainbow tables are precomputed lookup structures used to reverse certain **unsalted** hash types by trading very large storage for faster recovery time.

### When to use

- Only for **legacy, unsalted** hash scenarios where rainbow tables are known to exist (classic example: LM).
- Mostly relevant in historical cases, legacy systems, or training environments.

### Why to use

- Rainbow tables trade **storage for speed**: lookups can be much faster than generating candidates in real time.

### How to use

1. Confirm the target hash is **unsalted** and that a compatible table exists.
2. Pick a table that matches the hash algorithm + charset + length range.
3. Use a rainbow-table tool to look up the hash and recover the plaintext (if present).

High-level idea:

- Tables store **chains** using alternating hashing and “reduction” (hash → candidate) functions.
- This compresses storage vs storing every plaintext/hash pair.

### Commands

- There isn’t one universal rainbow-table command.
- Rainbow tables are used via specific tools (e.g., Ophcrack/RainbowCrack-style workflows), and the exact commands depend on the tool + table format.

### Why not to use

- **Salting defeats rainbow tables** (you’d need a separate precompute per salt value).
- Storage requirements are enormous for modern password policies.
- Modern defenses (salted + slow hashes) make rainbow tables largely obsolete.

---

## Defender takeaways (what stops these attacks)

- Enforce **long passphrases** + block common passwords.
- Use **MFA** for remote/admin access.
- Rate-limit logins and monitor authentication anomalies (sprays, distributed guessing).
- Store passwords with modern **salted + slow** hashes (Argon2id/bcrypt/scrypt) and strong parameters.
- Prefer password managers and rotate default credentials on devices/services.