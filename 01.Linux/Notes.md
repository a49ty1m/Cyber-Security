# Linux Notes (Very Detailed)

---
tags: [linux, cli, sysadmin, networking, security, bash, hardening, notes]
type: study-notes
level: beginner-to-intermediate
last_updated: 2026-03-05
---

Purpose of this document:
- Long-form reference notes for Linux study and practice.
- Written for revision + lab execution.
- Focused on terminal-first Linux administration fundamentals.

How to use these notes:
- Read one section.
- Open a VM terminal.
- Execute the commands in that section.
- Break something safely, then recover it.

---

## Study Navigation (Organized View)

### Quick jump links
- [Part A - Foundation and Core Linux Mechanics](#part-a---foundation-and-core-linux-mechanics)
- [Part B - System Operations and Administration](#part-b---system-operations-and-administration)
- [Part C - Practice, Revision, and Applied Operations](#part-c---practice-revision-and-applied-operations)
- [Part D - Advanced Security and Infrastructure Context](#part-d---advanced-security-and-infrastructure-context)
- [Scenario-Based Runbook Index](#29-scenario-based-runbook-index-fast-lookup)
- [Troubleshooting Matrix](#31-troubleshooting-matrix-symptom-to-action)
- [Glossary](#32-glossary-fast-recall)
- [Missing Topics To Add Next](#33-important-linux-topics-not-covered-deeply-yet)

### Part-wise structure
- Part A: Foundation and Core Linux Mechanics
  - Sections: `1` to `7`
- Part B: System Operations and Administration
  - Sections: `8` to `17`
- Part C: Practice, Revision, and Applied Operations
  - Sections: `18` to `23`
- Part D: Advanced Security and Infrastructure Context
  - Sections: `24` to `28`

### Dependency order (what to study first)
1. Start with `1 -> 5` (platform, boot, filesystem, shell, navigation).
2. Move to `6 -> 7` (streams + text processing), because these are used everywhere.
3. Then `8 -> 11` (package/process/user/permission administration).
4. Then `12 -> 15` (networking, remote access, scheduling, archiving).
5. Then `16 -> 19` (editors, docs, desktop context).
6. Execute `20` labs.
7. Use `21` to `23` as revision and gap-finding.
8. Finish with `24` to `28` for virtualization/security/cloud hardening context.

### Detailed table of contents
- `1` Linux Landscape and Distribution Families
- `2` Boot Process (Diagnostics-Critical)
- `3` Filesystem Hierarchy Standard (FHS)
- `4` Shell Environments, Variables, and Startup Files
- `5` Navigation and Discovery at Scale
- `6` Standard Streams, Redirection, and Pipes
- `7` Text Processing Stack (`grep`, `sed`, `awk`, and friends)
- `8` Package Management (Safe Software Lifecycle)
- `9` Process and Resource Management
- `10` Users, Groups, UID/GID, and Privilege Boundaries
- `11` File Permissions and Ownership (Security Core)
- `12` Networking Fundamentals and Diagnostics
- `13` SSH, SCP, and Rsync
- `14` Job Control, Background Tasks, and Scheduling
- `15` Archiving and Compression
- `16` Editors in Terminal Workflows
- `17` Offline Documentation and Self-Service Help
- `18` Display Stack Note: X11 vs Wayland
- `19` GUI Topics Mentioned (Lower Priority for Server Ops)
- `20` Admin Mini-Labs (Do These, Do Not Just Read)
- `21` Command Reference (Grouped)
- `22` High-Value Pitfalls to Avoid
- `23` Suggested Daily Practice Routine (30-45 min)
- `24` Virtualization Sandbox and Network Topologies (Advanced)
- `25` Directory Traversal and Path Resolution Mechanics
- `26` Data Extraction and Stream Handling at Scale
- `27` Permission Matrix and Privilege Escalation Surface
- `28` Cloud VPS Operations and Initial Hardening

---

## Part A - Foundation and Core Linux Mechanics

## 1. Linux Landscape and Distribution Families

### 1.1 What Linux is (practical view)
Linux is not a single product. In real operations, "Linux" usually means:
- Linux kernel
- GNU/core userland tools
- Init system (`systemd` in most modern distros)
- Package manager and repos
- Desktop/server environment choices

### 1.2 Main distro families

#### Red Hat family
- Examples: `RHEL`, `CentOS` (legacy/community variants), `Fedora`
- Typical usage:
  - enterprise servers,
  - compliance-heavy environments,
  - paid support contracts (`RHEL`).
- Package stack:
  - low-level: `rpm`
  - high-level: `dnf` (older systems use `yum`)

#### Debian family
- Examples: `Debian`, `Ubuntu`, `Linux Mint`
- Typical usage:
  - cloud VMs,
  - web apps,
  - developer workstations.
- Package stack:
  - low-level: `dpkg`
  - high-level: `apt`, `apt-get`

#### SUSE family
- Examples: `openSUSE`, `SLES`
- Typical usage:
  - enterprise deployments (notably in some regions and sectors).
- Package stack:
  - low-level: `rpm`
  - high-level: `zypper`

### 1.3 Selection criteria (real-world)
Choose distro by:
- team familiarity,
- support requirements,
- package ecosystem,
- security update cadence,
- third-party software compatibility.

Do not choose based on internet "distro wars".

---

## 2. Boot Process (Diagnostics-Critical)

If a machine fails to boot, identify the exact stage of failure.

### 2.1 Boot chain
1. Power-on + firmware (`BIOS`/`UEFI`)
2. Bootloader (`GRUB`)
3. Kernel load + decompress into memory
4. `initramfs` handles early hardware/module needs
5. Kernel starts PID 1 (`systemd` or init)
6. Filesystems mount + services start + login target reached

### 2.2 Stage-by-stage meaning

#### Firmware stage
- Initializes hardware and detects boot device.
- Failures here can be hardware or firmware configuration issues.

#### Bootloader stage (GRUB)
- Presents kernel entries and boot parameters.
- Can be used to boot older kernels for recovery.

#### Kernel + initramfs
- Kernel needs access to storage drivers and filesystem modules early.
- `initramfs` provides these before real root filesystem is mounted.

#### PID 1 stage (`systemd`)
- Mounts filesystems (including entries from `/etc/fstab`).
- Starts targets and services, often in parallel.

### 2.3 Why `systemd` matters
- Service startup is dependency-driven and parallelized.
- Faster boot than old serial init systems.
- Better service introspection with `systemctl` and logs via `journalctl`.

### 2.4 Boot troubleshooting flow
1. Does GRUB appear?
2. Can any kernel entry boot?
3. Are root filesystem mounts failing?
4. Is a specific service blocking boot target?

Useful commands after recovery boot:
```bash
systemctl --failed
journalctl -b -p err
cat /etc/fstab
```

---

## 3. Filesystem Hierarchy Standard (FHS)

Linux uses one tree under `/`.

### 3.1 Core directories
- `/`: root of all paths.
- `/bin`: essential user commands.
- `/sbin`: essential system/admin commands.
- `/boot`: kernel, initramfs, bootloader files.
- `/dev`: device nodes (`/dev/sda`, `/dev/null`, `/dev/tty`).
- `/etc`: system config files.
- `/home`: user home directories.
- `/root`: root account home.
- `/lib`, `/lib64`: shared libraries.
- `/proc`: runtime process/kernel virtual data.
- `/sys`: kernel device and system representation.
- `/var`: variable data (`/var/log`, cache, spool, db files).
- `/tmp`: temporary files.
- `/usr`: userland applications and libraries.
- `/opt`: optional third-party software installs.

### 3.2 "Everything is a file" model
Examples:
- Device interfaces in `/dev`
- Process metadata in `/proc/<pid>/`
- Kernel settings in `/proc/sys`

### 3.3 Operational consequence
If you know FHS, you can quickly locate:
- configs in `/etc`,
- logs in `/var/log`,
- binaries in `/usr/bin` and `/bin`,
- service units in `/etc/systemd/system` or `/usr/lib/systemd/system`.

---

## 4. Shell Environments, Variables, and Startup Files

### 4.1 Shell startup order (bash)
Common order for login shell:
- `/etc/profile`
- `~/.bash_profile` or `~/.bash_login` or `~/.profile`

Interactive non-login shell:
- `~/.bashrc`

### 4.2 High-value environment variables
- `PATH`: directories searched for executables.
- `HOME`: user home path.
- `SHELL`: active shell binary.
- `PS1`: prompt format.

### 4.3 Variable scope
- Shell variable: visible only in current shell.
- Exported variable: inherited by child processes.

```bash
MYVAR="local"
export APP_ENV="dev"
echo "$PATH"
```

### 4.4 Common admin aliases
```bash
alias ll='ls -alF'
alias grep='grep --color=auto'
```

### 4.5 PATH safety
- `.` (current directory) should not be in `PATH` on secure systems.
- Prefer explicit execution for local binaries: `./script.sh`.

---

## 5. Navigation and Discovery at Scale

### 5.1 Core movement commands
```bash
pwd
ls -lah
cd /var/log
cd ~
cd -
```

### 5.2 `find` (live filesystem scan)
```bash
find /var/log -type f -name "*.log"
find /etc -type f -mtime -7
find /home -type f -size +100M
find / -type f -perm -4000 2>/dev/null
```

Important options:
- `-type f` regular files, `-type d` directories
- `-mtime` modified days
- `-size` by file size
- `-perm` by permission bits
- `-exec` run command on results

Example with `-exec`:
```bash
find /var/log -type f -name "*.log" -exec ls -lh {} \;
```

### 5.3 `locate` (database-backed)
```bash
locate sshd_config
sudo updatedb
```
- Very fast, but stale if database not updated.

---

## 6. Standard Streams, Redirection, and Pipes

### 6.1 Standard file descriptors
- `0` = stdin
- `1` = stdout
- `2` = stderr

### 6.2 Redirection patterns
```bash
cmd > out.txt
cmd >> out.txt
cmd 2> err.txt
cmd > all.txt 2>&1
cmd 1> out.txt 2> err.txt
```

### 6.3 Piping philosophy
The pipe (`|`) connects small tools into a processing chain.

```bash
grep -i "error" /var/log/syslog | sort | uniq -c | sort -nr
```

### 6.4 `tee`
```bash
ip addr | tee ip_snapshot.txt
```
- Displays output and writes to file at same time.

---

## 7. Text Processing Stack (`grep`, `sed`, `awk`, and friends)

### 7.1 Fast reading tools
- `cat`: print full file
- `tac`: reverse line order
- `less`: paged viewer
- `head`, `tail`, `tail -f`

```bash
head -n 30 /var/log/auth.log
tail -f /var/log/syslog
```

### 7.2 `grep` patterns
```bash
grep "Failed password" /var/log/auth.log
grep -i "error" app.log
grep -R "PermitRootLogin" /etc/ssh
grep -E "(error|failed|denied)" -i app.log
```

Useful flags:
- `-i` ignore case
- `-R` recursive
- `-n` line number
- `-v` invert match
- `-E` extended regex

### 7.3 `sed` replacements
```bash
sed 's/old/new/g' file.txt
sed -n '1,20p' file.txt
```

In-place edit carefully:
```bash
sed -i.bak 's/old/new/g' file.txt
```
- Keeps backup as `file.txt.bak`.

### 7.4 `awk` field extraction
```bash
awk -F: '{print $1}' /etc/passwd
awk '{print $1, $5}' access.log
```

### 7.5 Column and character tools
```bash
cut -d':' -f1 /etc/passwd
tr '[:lower:]' '[:upper:]' < names.txt
sort users.txt | uniq
sort users.txt | uniq -c | sort -nr
```

### 7.6 Compare and data merge tools
```bash
diff file_old file_new
paste file1 file2
join -1 1 -2 1 a.txt b.txt
split -b 1G big.iso part_
```

### 7.7 Binary string extraction
```bash
strings suspicious_binary | less
```
- Helps identify embedded text, URLs, paths, credentials hints.

---

## Part B - System Operations and Administration

## 8. Package Management (Safe Software Lifecycle)

Never default to random binaries when package manager can provide trusted packages.

### 8.1 Debian/Ubuntu
```bash
sudo apt update
sudo apt install nginx
sudo apt remove nginx
sudo apt purge nginx
sudo apt autoremove
sudo apt upgrade
```

### 8.2 RHEL/Fedora
```bash
sudo dnf check-update
sudo dnf install nginx
sudo dnf remove nginx
sudo dnf upgrade
```

### 8.3 Low-level package tools
- `dpkg -i package.deb`
- `rpm -ivh package.rpm`

Low-level tools do less dependency resolution than high-level tools.

### 8.4 Package query examples
```bash
apt list --installed | grep -i openssh
rpm -qa | grep -i openssh
```

---

## 9. Process and Resource Management

### 9.1 Process listing
```bash
ps aux
ps -ef
```

Read key columns:
- PID, PPID, USER
- `%CPU`, `%MEM`
- STAT (process state)
- CMD (command)

### 9.2 Real-time view
```bash
top
```
Interpret quickly:
- CPU usage split (user/system/idle)
- memory and swap pressure
- load average (1m, 5m, 15m)

### 9.3 Load average rule of thumb
If sustained load > number of CPU cores, runnable tasks are waiting.

### 9.4 Process priorities (`nice`)
- Range: `-20` (highest) to `19` (lowest)
- Lower number = higher scheduling priority

```bash
nice -n 10 long_task
renice -n -5 -p 1234
```

### 9.5 Signals and termination
```bash
kill 1234        # SIGTERM (15)
kill -9 1234     # SIGKILL (9)
pkill -f nginx
killall nginx
```

Use `SIGKILL` only when graceful stop fails.

### 9.6 Zombies
- Zombie = finished child process not reaped by parent.
- Usually solve by restarting/killing parent process, not zombie itself.

---

## 10. Users, Groups, UID/GID, and Privilege Boundaries

### 10.1 Identity primitives
- User identity is UID-based, not username-based.
- Root is UID `0`.

```bash
id
whoami
groups
```

### 10.2 Account creation and defaults
```bash
sudo useradd -m -s /bin/bash -c "Student User" student1
sudo passwd student1
```

Skeleton defaults are copied from `/etc/skel`.

### 10.3 Group management
```bash
sudo usermod -aG sudo student1
sudo usermod -aG docker student1
```

Critical warning:
- Missing `-a` with `-G` replaces group list and can break access.

### 10.4 Account deletion
```bash
sudo userdel student1
sudo userdel -r student1
```

### 10.5 Root vs sudo practice
- Prefer `sudo` for command-level privilege escalation.
- Better auditability and safer operational habits.

---

## 11. File Permissions and Ownership (Security Core)

### 11.1 Permission model
Three triplets:
- owner
- group
- others

Each triplet bits:
- `r = 4`
- `w = 2`
- `x = 1`

### 11.2 Octal examples
- `755` = owner `rwx`, group `r-x`, others `r-x`
- `700` = owner full only
- `644` = owner read/write, others read
- `600` = owner read/write only

### 11.3 Common secure usage
```bash
chmod 755 script.sh
chmod 644 /etc/myapp.conf
chmod 600 ~/.ssh/id_rsa
chown user:group file.txt
```

### 11.4 Permission inspection
```bash
ls -l file.txt
stat file.txt
```

### 11.5 Security pitfalls
- Avoid blanket `chmod -R 777`.
- Check ownership and parent directory permissions.
- Validate key files (`~/.ssh`, `authorized_keys`, private keys) are restrictive.

---

## 12. Networking Fundamentals and Diagnostics

### 12.1 Name resolution flow
1. `/etc/hosts`
2. DNS resolvers in `/etc/resolv.conf`

### 12.2 Interface and route inspection
```bash
ip addr show
ip route show
```

### 12.3 Connectivity checks
```bash
ping -c 4 8.8.8.8
ping -c 4 example.com
traceroute example.com
```

Interpretation:
- IP ping works but domain ping fails -> DNS issue likely.
- both fail -> routing/firewall/interface issue likely.

### 12.4 DNS query tools
```bash
dig example.com
nslookup example.com
```

### 12.5 Legacy/classful context
- Class A/B/C ranges are historical model.
- Modern operations use CIDR notation (`/24`, `/16`, etc.).

### 12.6 Socket/port visibility
```bash
ss -tulnp
netstat -r
```

---

## 13. SSH, SCP, and Rsync

### 13.1 SSH basics
```bash
ssh user@host
ssh -p 2222 user@host
```

### 13.2 Secure copy with `scp`
```bash
scp local.txt user@host:/tmp/
scp user@host:/var/log/syslog ./
scp -r project_dir user@host:/opt/
```

### 13.3 `rsync` over SSH
`rsync` is preferred for large/repeated sync because it transfers deltas.

```bash
rsync -avz -e ssh /local/dir/ user@host:/remote/dir/
rsync -avz -e ssh user@host:/remote/dir/ /local/dir/
rsync -avz --dry-run -e ssh /local/dir/ user@host:/remote/dir/
```

Flags:
- `-a` archive (recursive + preserve metadata)
- `-v` verbose
- `-z` compression
- `--dry-run` simulate first

Trailing slash behavior matters:
- `/src/` syncs contents
- `/src` syncs directory itself

---

## 14. Job Control, Background Tasks, and Scheduling

### 14.1 Shell job control
```bash
sleep 300 &
jobs
fg %1
bg %1
```

### 14.2 Recurring schedules with cron
Edit current user crontab:
```bash
crontab -e
```

List cron jobs:
```bash
crontab -l
```

Cron format:
`Minute Hour DayOfMonth Month DayOfWeek Command`

Example (daily 02:00):
```cron
0 2 * * * /opt/backup.sh
```

### 14.3 One-time scheduling with `at`
```bash
echo "/opt/once.sh" | at 22:00
atq
atrm <job_id>
```

### 14.4 Script timing helper
```bash
sleep 60
```

---

## 15. Archiving and Compression

### 15.1 `tar` concepts
- `tar` archives files into one bundle.
- Compression is optional and selected with flags.

### 15.2 Common compression modes
```bash
tar -czvf archive.tar.gz /target_dir
tar -cjvf archive.tar.bz2 /target_dir
tar -cJvf archive.tar.xz /target_dir
```

### 15.3 Extract archives
```bash
tar -xzvf archive.tar.gz
tar -xjvf archive.tar.bz2
tar -xJvf archive.tar.xz
```

### 15.4 Compression tradeoff summary
- `gzip`: faster, decent ratio
- `bzip2`: slower, often better ratio
- `xz`: slowest, often best ratio

---

## 16. Editors in Terminal Workflows

### 16.1 Why `vi`/`vim` is mandatory
- Usually present on nearly every Unix/Linux system.
- Essential when no GUI/editor packages are available.

### 16.2 Vim mode model
- Normal mode: navigation and commands
- Insert mode: text editing
- Command-line mode: save/quit/search commands

### 16.3 Vim survival set
```text
i          insert mode
Esc        normal mode
:w         write (save)
:q         quit
:wq        save + quit
:q!        quit without save
/keyword   search forward
n          next search match
```

### 16.4 Emacs basics
- Save: `Ctrl-x Ctrl-s`
- Exit: `Ctrl-x Ctrl-c`
- Kill line: `Ctrl-k`

---

## 17. Offline Documentation and Self-Service Help

### 17.1 Manual pages
```bash
man ssh
man chmod
```

Search by keyword:
```bash
man -k network
apropos archive
```

### 17.2 GNU info pages
```bash
info coreutils
```

Use docs first before random copy-paste from internet.

---

## Part C - Practice, Revision, and Applied Operations

## 18. Display Stack Note: X11 vs Wayland

### 18.1 Session type check
```bash
echo "$XDG_SESSION_TYPE"
```

### 18.2 Difference (high-level)
- X11: older design, weaker app isolation.
- Wayland: newer design with stronger isolation assumptions.

This matters mostly on desktop Linux, less on headless servers.

---

## 19. GUI Topics Mentioned (Lower Priority for Server Ops)

Covered but less critical for pure server administration:
- Desktop environments: GNOME, KDE
- GUI package/config tools: Synaptic, YaST
- GUI apps: LibreOffice, GIMP, VLC, Thunderbird

For server/infra path, prioritize CLI mastery first.

---

## 20. Admin Mini-Labs (Do These, Do Not Just Read)

### Lab 1: Filesystem and discovery
1. Create test tree under `/tmp/linux-lab`.
2. Generate files with different sizes and timestamps.
3. Use `find` filters (`-type`, `-size`, `-mtime`).

### Lab 2: Streams and redirection
1. Run command producing stdout + stderr.
2. Split outputs to separate files.
3. Merge with `2>&1` and log with `tee`.

### Lab 3: Text parsing
1. Pull usernames from `/etc/passwd` with `awk` and `cut`.
2. Search auth logs with `grep -Ei`.
3. Replace text safely with `sed -i.bak`.

### Lab 4: Processes
1. Start a long-running command (`sleep 9999`).
2. Inspect with `ps`, `top`.
3. Change priority via `renice`.
4. Stop with `SIGTERM`, then `SIGKILL` if needed.

### Lab 5: Permissions
1. Create script and restrict access (`700`, `755`, `644`, `600`).
2. Verify with `ls -l` and `stat`.
3. Change owner/group with `chown`.

### Lab 6: Networking
1. Check IP and routes.
2. Test IP vs DNS connectivity.
3. Compare `ping`, `traceroute`, `dig` results.

### Lab 7: Remote transfer
1. SSH into second machine/VM.
2. Copy files using `scp`.
3. Repeat with `rsync --dry-run`, then real sync.

### Lab 8: Scheduling
1. Add cron job writing timestamp to a log every minute.
2. Verify execution and job logs.
3. Remove cron entry after test.

---

## 21. Command Reference (Grouped)

### System identity and runtime
```bash
uname -a
hostnamectl
uptime
whoami
id
```

### Filesystem and disk
```bash
lsblk
df -h
du -sh *
mount
```

### Process and performance
```bash
ps aux
top
free -h
vmstat 1 5
```

### Service management (`systemd`)
```bash
systemctl status ssh
systemctl start ssh
systemctl enable ssh
systemctl --failed
journalctl -xe
journalctl -u ssh -b
```

### Networking
```bash
ip addr show
ip route show
ss -tulnp
ping -c 4 1.1.1.1
dig example.com
```

### Permissions and ownership
```bash
ls -l
chmod 755 script.sh
chmod 600 ~/.ssh/id_rsa
chown user:group file.txt
```

---

## 22. High-Value Pitfalls to Avoid

1. Blindly using `chmod 777` to silence errors.
2. Editing `/etc/fstab` without backup and validation.
3. Using `usermod -G` without `-a`.
4. Killing critical processes with `kill -9` first.
5. Running risky `sed -i` without backup suffix.
6. Forgetting trailing slash semantics in `rsync`.
7. Installing unknown binaries outside package manager.
8. Troubleshooting network without separating DNS vs routing tests.

---

## 23. Suggested Daily Practice Routine (30-45 min)

1. 10 min: run 10 core commands from memory.
2. 10 min: parse one log file with `grep`, `awk`, `sed`.
3. 10 min: process exercise (`ps` + `top` + kill flow).
4. 10 min: one networking diagnostic chain.
5. 5 min: read one `man` page and note 3 useful flags.

This routine builds execution speed and confidence for real incidents.

---

## Part D - Advanced Security and Infrastructure Context

## 24. Virtualization Sandbox and Network Topologies (Advanced)

Hypervisor setup is not just "install OS and boot". For security labs, network mode determines whether traffic can flow correctly for scanning, callbacks, and isolation.

### 24.1 NAT mode
- VM sits behind a virtual router created by the hypervisor.
- VM can usually access internet outbound.
- Inbound connections from external machines to VM are blocked unless explicit port forwarding is configured.

Operational implication:
- Useful for normal updates and browsing from VM.
- Not ideal when another machine must initiate direct connections back to your VM.

### 24.2 Bridged mode
- VM appears as a first-class host on your physical LAN.
- VM receives IP from physical router DHCP (same subnet as other LAN devices).
- Other local hosts can directly reach the VM.

Operational implication:
- Better for realistic network labs where peer machines must communicate both ways.

### 24.3 Host-only mode
- Creates isolated network between host and selected VMs.
- No default internet connectivity.
- Traffic stays in local lab boundary.

Operational implication:
- Strong choice for malware detonation and high-risk experiments.

### 24.4 Quick validation checklist
```bash
ip addr show
ip route show
ping -c 3 <gateway_ip>
ping -c 3 8.8.8.8
```
- If gateway ping works but internet ping fails, upstream/NAT path may be missing.
- If neither works, interface or route is likely wrong.

---

## 25. Directory Traversal and Path Resolution Mechanics

Understanding paths is essential for both administration and secure coding review.

### 25.1 Absolute paths
- Always begin at root `/`.
- Example: `/var/www/html/index.php`.
- Independent of current working directory.

### 25.2 Relative paths
- Evaluated from current working directory.
- `.` means current directory.
- `..` means parent directory.

Examples:
```bash
pwd
cat ../notes/todo.txt
cat ./config/app.conf
```

### 25.3 Why this matters in app security
- If user input is used in file include/read operations without validation, relative segments can escape intended directories.
- Defensive controls include:
  - canonical path resolution,
  - allowlisting expected filenames,
  - rejecting `../` patterns,
  - chroot/container boundaries,
  - least-privilege file permissions.

---

## 26. Data Extraction and Stream Handling at Scale

Large log files require streaming workflow, not full-file dumping.

### 26.1 Safer file viewing choices
```bash
less /var/log/auth.log
head -n 20 /var/log/auth.log
tail -n 20 /var/log/auth.log
tail -f /var/log/auth.log
```

Why:
- `less` pages data efficiently.
- `head` and `tail` sample file edges.
- `tail -f` follows live writes for real-time monitoring.

### 26.2 Fast filtering with `grep`
```bash
grep "Failed password" /var/log/auth.log
grep -Ei "(failed|invalid user|authentication failure)" /var/log/auth.log
```

### 26.3 Compound pipeline example
```bash
grep "Failed password" /var/log/auth.log \
  | awk '{print $(NF-3)}' \
  | sort | uniq -c | sort -nr
```

Use-case:
- Extract and count frequently seen source IPs from repeated failed login entries.

---

## 27. Permission Matrix and Privilege Escalation Surface

Permissions enforce kernel-level access control. Incorrect settings are common root cause of compromise.

### 27.1 Octal recap
- `r = 4`, `w = 2`, `x = 1`
- Example `755`:
  - owner: `7` (`rwx`)
  - group: `5` (`r-x`)
  - others: `5` (`r-x`)

```bash
chmod 755 script.sh
chmod 640 app.conf
chmod 600 ~/.ssh/id_rsa
```

### 27.2 Least privilege rule
- Grant only required access for function.
- Avoid blanket `777` permissions.

### 27.3 SUID concept (defensive and audit perspective)
- SUID causes executable to run with owner identity.
- If owner is `root`, process executes with elevated privilege.

Audit command:
```bash
find / -perm -4000 -type f 2>/dev/null
```

Defensive notes:
- Baseline expected SUID binaries.
- Investigate unusual additions.
- Remove risky custom SUID files unless explicitly required.

---

## 28. Cloud VPS Operations and Initial Hardening

Public VPS instances are exposed immediately after provisioning. Hardening should be done before deploying apps.

### 28.1 Why VPS is used
- Provides stable public endpoint for remote administration and testing.
- Separates lab infrastructure from home network.

### 28.2 Immediate baseline hardening
1. Create a non-root user.
2. Add user to privileged admin group (`sudo` or distro equivalent).
3. Configure SSH key authentication.
4. Disable password SSH authentication.
5. Disable direct root SSH login.
6. Restart SSH service and validate access from a second session.

### 28.3 Example account + SSH setup
```bash
sudo useradd -m -s /bin/bash opsuser
sudo passwd opsuser
sudo usermod -aG sudo opsuser

mkdir -p ~/.ssh && chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

### 28.4 SSH daemon policy (`/etc/ssh/sshd_config`)
Recommended minimum:
```text
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
```

Then reload/restart SSH daemon (distro-dependent):
```bash
sudo systemctl restart ssh
# or
sudo systemctl restart sshd
```

Safety procedure:
- Keep existing SSH session open while testing new session.
- Confirm key-based login works before closing original session.

---

## 29. Scenario-Based Runbook Index (Fast Lookup)

Use this section when you need immediate command flow by problem type.

### 29.1 System did not boot normally
1. Check whether GRUB menu is reachable.
2. Boot alternate kernel/recovery entry.
3. Inspect failed services and boot logs:
```bash
systemctl --failed
journalctl -b -p err
cat /etc/fstab
```
4. Validate mount entries, then reboot.

### 29.2 Server is slow or hanging
1. Check load and process pressure:
```bash
uptime
top
ps aux --sort=-%cpu | head
ps aux --sort=-%mem | head
```
2. Identify runaway process.
3. Gracefully terminate first (`SIGTERM`), force only if required.

### 29.3 "Permission denied" debugging
1. Inspect permissions and ownership:
```bash
ls -l <file>
stat <file>
id
groups
```
2. Confirm execute bit for scripts/binaries.
3. Fix owner/group/mode minimally (least privilege).

### 29.4 DNS or internet connectivity issue
1. Check IP assignment and route:
```bash
ip addr show
ip route show
```
2. Test by IP:
```bash
ping -c 4 8.8.8.8
```
3. Test by hostname:
```bash
ping -c 4 example.com
dig example.com
cat /etc/resolv.conf
cat /etc/hosts
```

### 29.5 Repeated SSH authentication failures
1. Follow auth logs live:
```bash
tail -f /var/log/auth.log
```
2. Extract failure patterns:
```bash
grep -Ei "(failed password|invalid user|authentication failure)" /var/log/auth.log
```
3. Count top source IPs:
```bash
grep "Failed password" /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr
```

### 29.6 Safe remote sync or migration
1. Dry-run first:
```bash
rsync -avz --dry-run -e ssh /src/ user@host:/dst/
```
2. Execute real sync after validation.
3. Re-run sync to transfer only deltas.

### 29.7 New VPS first 15 minutes checklist
1. Create non-root admin user.
2. Add to sudo group.
3. Configure SSH keys.
4. Disable root SSH login.
5. Disable password auth.
6. Restart SSH and test from second session.

---

## 30. Revision Modes (Use by Time Available)

Use this section to decide how to revise based on available time.

### 30.1 15-minute rapid refresh
1. Read Sections `21`, `22`, `29` only.
2. Run 5 commands from memory:
```bash
ip addr show
ps aux | head
find /etc -name "*.conf" | head
grep -Ei "error|failed" /var/log/syslog | head
ls -l ~/.ssh
```
3. Note one weak area to practice later.

### 30.2 60-minute practical revision
1. Review Sections `6`, `7`, `9`, `11`, `12`, `13`.
2. Execute mini-labs `2`, `3`, `4`, `6`, `7` from Section `20`.
3. Update a short log with:
  - what worked,
  - what failed,
  - exact command fixed issue.

### 30.3 3-hour deep session
1. End-to-end pass through Sections `1` to `29`.
2. Build one fresh VM and configure baseline hardening.
3. Perform full diagnostics drill:
  - process pressure,
  - permission issue,
  - DNS issue,
  - secure file sync.
4. Reproduce all runbooks from Section `29` without copy-paste.

---

## 31. Troubleshooting Matrix (Symptom to Action)

### 31.1 Boot and system startup
| Symptom | First checks | Commands |
|---|---|---|
| System hangs during boot | service failure, bad mount entry | `systemctl --failed`, `journalctl -b -p err`, `cat /etc/fstab` |
| Kernel boots but login target unavailable | target/service dependency issue | `systemctl get-default`, `systemctl list-dependencies multi-user.target` |

### 31.2 Performance and process issues
| Symptom | First checks | Commands |
|---|---|---|
| High CPU | top consumers | `top`, `ps aux --sort=-%cpu | head` |
| High memory | memory-heavy process | `free -h`, `ps aux --sort=-%mem | head` |
| System lag | sustained load vs core count | `uptime`, `vmstat 1 5` |

### 31.3 File and permission issues
| Symptom | First checks | Commands |
|---|---|---|
| Permission denied | owner, mode, user groups | `ls -l`, `stat`, `id`, `groups` |
| Script not executing | shebang, execute bit, line endings | `head -n 1 script.sh`, `chmod +x script.sh`, `file script.sh` |

### 31.4 Network and DNS issues
| Symptom | First checks | Commands |
|---|---|---|
| Can ping IP, not domain | DNS config path | `cat /etc/resolv.conf`, `dig example.com` |
| No connectivity at all | interface and default route | `ip addr show`, `ip route show`, `ping -c 4 8.8.8.8` |
| Service not reachable | listen socket and firewall | `ss -tulnp`, `sudo ufw status` |

### 31.5 SSH and remote access issues
| Symptom | First checks | Commands |
|---|---|---|
| SSH auth fails | logs + auth method | `tail -f /var/log/auth.log`, `ssh -v user@host` |
| Key ignored | permission mismatch | `chmod 700 ~/.ssh`, `chmod 600 ~/.ssh/authorized_keys` |
| Locked out after sshd change | validate daemon config before restart | `sudo sshd -t`, `sudo systemctl restart sshd` |

---

## 32. Glossary (Fast Recall)

- `BIOS/UEFI`: firmware that initializes hardware before bootloader.
- `GRUB`: common Linux bootloader.
- `Kernel`: core OS component handling hardware/process/memory.
- `initramfs`: temporary early userspace for boot-time module access.
- `systemd`: init/service manager (PID 1 on many distros).
- `FHS`: standard Linux filesystem layout conventions.
- `stdin/stdout/stderr`: standard input/output/error streams (`0/1/2`).
- `pipe (|)`: sends stdout of one command as stdin to next command.
- `UID/GID`: numeric user/group identities.
- `SUID`: executable runs with file owner identity.
- `least privilege`: grant minimum required permissions only.
- `NAT`: translated networking; inbound restrictions by default.
- `bridged`: VM appears directly on physical LAN.
- `host-only`: isolated virtual network with host + VMs.
- `CIDR`: classless subnet notation (e.g., `/24`).
- `daemon`: background service process.
- `cron`: recurring scheduler.
- `rsync`: delta-based file synchronization tool.

---

## 33. Important Linux Topics Not Covered Deeply Yet

These are high-value Linux areas that are only lightly touched (or not yet detailed) in this note and should be added next for stronger system administration depth.

### 33.1 Storage and filesystem administration
- Partition management: `lsblk`, `fdisk`, `parted`.
- Filesystem creation/check: `mkfs`, `fsck`, `tune2fs`.
- Mount lifecycle and persistence: `mount`, `umount`, `/etc/fstab` validation workflow.
- Logical Volume Manager (LVM): PV/VG/LV concepts, resize and snapshot basics.
- Filesystem usage analysis: `df`, `du`, inode exhaustion checks.

### 33.2 Service internals and startup control
- `systemd` unit anatomy (`.service`, `.target`, `.timer`).
- Service override files: `systemctl edit <service>`.
- Boot analysis: `systemd-analyze`, dependency graph reading.
- Persistent vs runtime service enablement and masking.

### 33.3 Security frameworks beyond chmod/chown
- ACLs (`setfacl`, `getfacl`) for fine-grained permissions.
- Linux capabilities (`getcap`, `setcap`) and least-privilege alternatives to SUID.
- Mandatory Access Control:
  - SELinux basics (`getenforce`, contexts, booleans),
  - AppArmor profile model.

### 33.4 Firewall and packet filtering
- `nftables`/`iptables` fundamentals (chains, rules, default policy).
- Host firewall workflows with `ufw` or `firewalld`.
- Service exposure validation with `ss -tulnp` + firewall rule checks.

### 33.5 Logging, auditing, and observability
- Deeper `journalctl` filters (`-u`, `--since`, priority levels).
- Traditional logs in `/var/log` and `logrotate` behavior.
- `auditd` basics for security event trail and rule design.

### 33.6 Authentication and account policy
- PAM basics and lockout policy concepts.
- Password aging and account expiry (`chage`).
- Sudo policy structure and `visudo` best practices.

### 33.7 Network services and troubleshooting depth
- DHCP client/server basics.
- DNS record types and resolver behavior (`A`, `AAAA`, `CNAME`, `MX`, `TXT`).
- TCP troubleshooting with `ss`, `tcpdump` basics, and route tracing depth.

### 33.8 Backup and recovery strategy
- Point-in-time backup patterns (tar + timestamped archives).
- Incremental sync strategy with `rsync` and retention model.
- Restore drills and integrity checks (backup is not valid until restore is tested).

### 33.9 Bash scripting reliability
- Safe script mode: `set -euo pipefail`.
- Exit code handling and trap/cleanup patterns.
- Parameter parsing (`getopts`) and input validation.

### 33.10 Time and scheduled operations
- NTP/time sync (`timedatectl`, chrony/ntpd concepts).
- `cron` vs `systemd timers`: when to use which.



