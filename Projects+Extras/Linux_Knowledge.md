# Some Basic Knowledge of Linux 
- the terminal is everything in linux   
## Linux Filesystem Hierarchy

| Directory | Description |
|-----------|-------------|
| `/`       | Root directory, the starting point of the filesystem. |
| `/bin`    | Essential user binaries (commands needed in single-user mode, e.g., `ls`, `cp`, `mv`). |
| `/boot`   | Boot loader files (kernels, initrd, boot configs). |
| `/dev`    | Device files (represents hardware and virtual devices). |
| `/etc`    | System-wide configuration files and scripts. |
| `/home`   | User home directories. Each user gets a subdirectory here. |
| `/lib`    | Essential shared libraries for `/bin` and `/sbin` programs. |
| `/media`  | Mount point for removable media (USBs, CDs, DVDs). |
| `/mnt`    | Temporary mount point (for manually mounted filesystems). |
| `/opt`    | Optional software and third-party packages. |
| `/proc`   | Virtual filesystem providing process and kernel info. |
| `/root`   | Home directory of the root user. |
| `/run`    | Runtime data (process IDs, sockets, temporary files). |
| `/sbin`   | System binaries (administrative commands, e.g., `fsck`, `reboot`). |
| `/srv`    | Data served by the system (like web, FTP). |
| `/sys`    | Virtual filesystem with information about devices and the kernel. |
| `/tmp`    | Temporary files (cleared on reboot, accessible to all users). |
| `/usr`    | Secondary hierarchy for user applications and files. |
| `/var`    | Variable files (logs, caches, spool, databases). |

---

 **Tip:**  
- Think of `/` as the **tree trunk**, and every directory as a branch.  
- `/etc` = configs, `/var` = logs + dynamic files, `/home` = personal space, `/bin & /sbin` = commands.  

- stdout < is default 
- stdin > is not  
means if we write `echo hi > hi.txt` it will give outpot in hi.txt file 
and `cat < hi.txt == cat hi.txt`

- ctrl c is use to exit any command execution
- we can make or run single command for multiple files by using brackets  
 touch file{1..100}.txt

- we take one step back by .. in cd command 
- we can target many files of similar name by using * example remove all file with name file = rm file*
- we can run previous command using up key without writing it again

