# Linux Basics Commands

## 1. Access and Help Commands
- `sudo` = run command with elevated privileges
- `su` = switch user (often to root)
- `man <command>` = full manual page
- `info <command>` = detailed GNU documentation
- `tldr <command>` = short practical examples
- `whatis <command>` = one-line command description

## 2. Identity and System Basics
- `whoami` = current logged-in user
- `who` = currently logged-in users
- `w` = who is logged in and what they are doing
- `last` = login history
- `hostname` = system hostname
- `uname -a` = kernel and system details
- `lscpu` = CPU information
- `free -h` = RAM and swap usage
- `uptime` = system uptime and load averages
- `echo "text"` = print text or variable value
- `date` = current date and time
- `cal` = calendar view

## 3. Navigation and File Basics
- `pwd` = current working directory
- `cd <dir>` = change directory
- `cd -` = previous directory
- `ls` = list files/directories
- `ls -lah` = detailed listing with hidden files
- `clear` = clear terminal screen

## 4. File and Directory Operations
- `cat file` = print file content
- `less file` = view file page by page
- `head -n 20 file` = first 20 lines
- `tail -n 20 file` = last 20 lines
- `tail -f file` = follow file in real time
- `touch file` = create empty file
- `mkdir dir` = create directory
- `mktemp` = create temporary file
- `mktemp -d` = create temporary directory
- `cp src dst` = copy file
- `cp -r src dst` = copy directory recursively
- `mv old new` = move/rename file or directory
- `rm file` = remove file
- `rm -r dir` = remove directory recursively
- `rmdir dir` = remove empty directory
- `ln src dst` = hard link
- `ln -s src dst` = symbolic link
- `stat file` = detailed file metadata
- `file file` = detect file type
- `realpath file` = absolute path
- `wc -l file` = line count

## 5. Search and Discovery
- `find /path -name "name"` = find by name
- `find /path -type f -name "*.log"` = find log files
- `find . -type f -mtime -1` = files modified in last 24h
- `plocate name` or `locate name` = fast indexed search
- `updatedb` = refresh locate database
- `whereis cmd` = command location and man path
- `which cmd` = executable path in `PATH`
- `grep "pattern" file` = search pattern in file
- `grep -Rin "pattern" /path` = recursive case-sensitive search with line numbers
- `grep -E "error|fail|denied" file` = extended regex search

## 6. Text Processing
- `awk -F: '{print $1}' /etc/passwd` = first field extraction
- `sed 's/old/new/g' file` = replace text
- `cut -d: -f1 /etc/passwd` = cut first column by delimiter
- `sort file | uniq -c` = sort and count duplicates
- `tr '[:lower:]' '[:upper:]'` = lowercase to uppercase
- `xargs` = pass stdin as arguments to command
- `tee file` = write to file and stdout at the same time
- `diff file1 file2` = compare two files line by line
- `diff -u file1 file2` = unified diff format (easier to read)
- `column -t file` = align output into clean columns
- `paste file1 file2` = merge files side by side

## 7. Package Management
- `apt update && apt upgrade` = update and upgrade packages (Debian/Ubuntu)
- `apt install pkg` = install package
- `apt remove pkg` = remove package
- `dnf install pkg` = install package (RHEL/Fedora)
- `dnf upgrade` = upgrade packages (RHEL/Fedora)
- `dpkg -l | grep pkg` = list installed Debian package
- `rpm -qa | grep pkg` = list installed RPM package

## 8. Disk and Filesystem
- `df -h` = mounted filesystem usage
- `df -i` = inode usage
- `du -sh <path>` = directory/file size summary
- `lsblk -f` = block devices and filesystems
- `mount` = mounted filesystems
- `umount /mountpoint` = unmount filesystem
- `blkid` = UUID and filesystem type
- `ncdu` = interactive disk usage viewer
- `duf` = modern disk usage output

## 9. Processes and Performance
- `ps` = process snapshot
- `ps aux` = full process list
- `top` = real-time process monitor
- `htop` = interactive process viewer (better than top)
- `kill PID` = send terminate signal
- `kill -15 PID` = graceful stop
- `kill -9 PID` = force stop
- `pgrep name` = find process by name
- `pkill name` = kill process by name
- `nice -n 10 cmd` = run with lower CPU priority
- `renice -n -5 -p PID` = adjust priority of running process (negative values require root)
- `watch -n 2 cmd` = run command every 2 seconds
- `lsof -i :80` = list process using port 80
- `lsof -p PID` = files opened by process
- `vmstat 1 5` = CPU/memory/process sample stats
- `iostat -x 1` = disk I/O statistics per second

## 10. Users, Groups, and Permissions
- `id` = show UID, GID, groups
- `groups` = show group memberships
- `useradd` = create user
- `usermod -aG group user` = add user to group
- `userdel -r user` = delete user and home
- `passwd user` = set/change password
- `chmod` = change file permissions
- `chown user:group file` = change owner and group
- `chgrp group file` = change group
- `umask` = default permission mask
- `sudo -l` = show allowed sudo commands
- `visudo` = safe sudoers edit
- `getfacl file` = show ACLs
- `setfacl` = set ACLs

## 11. Networking
- `ip addr` = IP addresses and interfaces
- `ip route` = routing table
- `ping -c 4 host` = connectivity test
- `traceroute host` = route path to host
- `dig domain +short` = DNS lookup
- `nslookup domain` = DNS query
- `ss -tulnp` = listening ports and processes
- `curl -I https://example.com` = response headers
- `wget URL` = file download
- `tcpdump -ni any port 53` = DNS packet capture

## 12. Remote Access and Transfer
- `ssh user@host` = remote login
- `ssh -i key.pem user@host` = login with key file
- `scp file user@host:/path` = copy over SSH
- `rsync -avz --dry-run src/ user@host:/dst/` = test sync
- `rsync -avz src/ user@host:/dst/` = actual sync

## 13. Services and Logs
- `systemctl status service` = service status
- `systemctl enable --now service` = enable and start
- `systemctl list-units --type=service --state=running` = running services
- `journalctl -xe` = recent important logs
- `journalctl -u ssh -b` = SSH logs (current boot)
- `journalctl --since "1 hour ago"` = logs for time range

## 14. Archives, Integrity, and Scheduling
- `tar -czvf backup.tar.gz dir/` = create compressed archive
- `tar -xzvf backup.tar.gz` = extract archive
- `gzip file` and `gunzip file.gz` = compress/decompress gzip
- `xz file` and `unxz file.xz` = compress/decompress xz
- `sha256sum file` = checksum verification
- `history` = command history
- `!!` = rerun previous command
- `crontab -e` = edit cron jobs
- `crontab -l` = list cron jobs
- `at 10:30` = one-time scheduled job
- `systemctl list-timers` = list systemd timers

## 15. Environment and Shell
- `env` = print all environment variables
- `printenv VAR` = print value of a specific variable
- `export VAR=value` = set and export environment variable
- `unset VAR` = remove a variable
- `echo $PATH` = view current PATH
- `export PATH=$PATH:/new/dir` = add directory to PATH
- `alias ll='ls -lah'` = create command shortcut
- `unalias ll` = remove alias
- `source ~/.bashrc` or `. ~/.bashrc` = reload shell config
- `bash -x script.sh` = run script in debug mode (trace execution)
- `set -e` = exit script on first error
- `set -u` = treat unset variables as errors