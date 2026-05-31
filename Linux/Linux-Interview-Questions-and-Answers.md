# Linux Interview Questions and Answers

> **Senior DevOps Interview Pack**
>
> **Domain:** Linux Administration, Troubleshooting, Performance, Security, and Operations  
> **Level:** Senior / Lead DevOps / SRE / Platform Engineering  
> **Format:** 100 real-interview-style questions with concise, practical answers  
> **Best for:** interview preparation, mock interviews, rapid revision, and PDF export

---

## Executive Summary

This guide is designed for senior-level Linux interviews where interviewers expect more than command recall. You should be able to explain fundamentals, diagnose production issues, justify trade-offs, and describe safe remediation steps.

### What this pack helps you demonstrate
- Strong Linux fundamentals
- Production troubleshooting mindset
- Operational decision-making under pressure
- Security and permissions awareness
- Clear, structured interview communication

---

## Navigation

| Section | Focus Area |
|---|---|
| [How to Use This Guide](#how-to-use-this-guide) | Best way to prepare with this file |
| [Interview Answer Framework](#interview-answer-framework) | How to answer like a senior engineer |
| [Core Linux Concepts](#core-linux-concepts) | Boot, kernel, processes, and system basics |
| [Processes, CPU, and Memory](#processes-cpu-and-memory) | Runtime behaviour and performance analysis |
| [Storage and Filesystems](#storage-and-filesystems) | Disk usage, mounts, filesystems, and diagnostics |
| [Services, Boot, and Scheduling](#services-boot-and-scheduling) | systemd, services, cron, and startup flow |
| [Permissions and Security](#permissions-and-security) | Ownership, access control, SELinux, and hardening |
| [Networking and Connectivity](#networking-and-connectivity) | Interfaces, routing, DNS, ports, and packet analysis |
| [Shell, Text Processing, and Utilities](#shell-text-processing-and-utilities) | Daily command-line productivity and troubleshooting |
| [Production Troubleshooting Mindset](#production-troubleshooting-mindset) | Senior-level incident handling approach |
| [Rapid Revision Sheet](#rapid-revision-sheet) | Last-minute interview refresh |
| [Final Interview Advice](#final-interview-advice) | What interviewers remember most |

---

## How to Use This Guide

### Recommended preparation flow
1. Read **10 to 15 questions per day**
2. Answer each question once **without looking**
3. Re-answer using a **production example**
4. Revise weak areas using the **Rapid Revision Sheet**

### What senior interviewers usually expect
- Correct fundamentals
- Clear explanation, not just keywords
- Real production context
- Safe troubleshooting sequence
- Awareness of impact, risk, and rollback

---

## Interview Answer Framework

Use this structure for most Linux interview answers:

| Step | What to say |
|---|---|
| 1. Define | Explain what the concept is |
| 2. Importance | Explain why it matters in production |
| 3. Practical example | Give a real or realistic scenario |
| 4. Troubleshooting angle | Mention commands, logs, or metrics you would check |
| 5. Safe action | Explain how you would mitigate without causing more impact |

### Example senior-style answer
> “Load average shows how many tasks are runnable or waiting over time. I do not interpret it in isolation. I compare it with CPU utilisation, I/O wait, run queue behaviour, and process state to determine whether the issue is compute saturation, blocked disk I/O, or application contention.”

---

## Core Linux Concepts

### 1) What happens when a Linux system boots?
**Answer:** The BIOS or UEFI initialises hardware, loads the bootloader, the kernel starts, mounts the root filesystem, launches `systemd`, and then starts configured services and targets.

### 2) What is the difference between BIOS and UEFI?
**Answer:** BIOS is older firmware with limited partition support, while UEFI is modern, faster, supports larger disks through GPT, and provides better boot flexibility and security features.

### 3) What is the role of GRUB?
**Answer:** GRUB is the bootloader that loads the Linux kernel and initramfs, and can present multiple boot options or recovery entries.

### 4) What is initramfs?
**Answer:** It is a temporary root filesystem loaded into memory during boot to help the kernel load drivers and mount the real root filesystem.

### 5) What is systemd?
**Answer:** `systemd` is the init system and service manager used by most modern Linux distributions to manage boot targets, services, timers, logs, and dependencies.

### 6) How do you check system boot time?
**Answer:** Use `systemd-analyze` for total boot time and `systemd-analyze blame` to identify slow services.

### 7) What is the difference between a process and a thread?
**Answer:** A process has its own memory space and resources, while threads share the same process memory and execute concurrently within that process.

### 8) How do you list running processes?
**Answer:** Use `ps -ef`, `ps aux`, `top`, or `htop` depending on whether you want a snapshot or live view.

### 9) How do you find the top CPU-consuming process?
**Answer:** Use `top`, `htop`, or `ps aux --sort=-%cpu | head`.

### 10) How do you find the top memory-consuming process?
**Answer:** Use `ps aux --sort=-%mem | head` or inspect live usage with `top` or `htop`.

---

## Processes, CPU, and Memory

### 11) What does load average mean?
**Answer:** It shows the average number of runnable or waiting tasks over 1, 5, and 15 minutes. High load with low CPU usage can indicate I/O wait or blocked processes.

### 12) How do you troubleshoot high CPU usage?
**Answer:** Identify the process with `top` or `ps`, inspect logs, recent deployments, thread behaviour, and decide whether to scale, restart, or roll back safely.

### 13) How do you troubleshoot high memory usage?
**Answer:** Use `free -m`, `top`, `vmstat`, and process inspection. Then determine whether usage is due to cache, leak, or workload growth.

### 14) What is swap?
**Answer:** Swap is disk space used as overflow memory when RAM is under pressure. Heavy swap usage usually indicates memory stress and can degrade performance.

### 15) How do you check swap usage?
**Answer:** Use `free -m`, `swapon --show`, or `vmstat`.

### 16) What is an OOM killer?
**Answer:** The Out Of Memory killer terminates processes when the system runs out of memory and cannot recover safely.

### 17) How do you check if OOM killer terminated a process?
**Answer:** Inspect `dmesg`, `journalctl -k`, or system logs for OOM-related messages.

### 18) What is the difference between virtual memory and physical memory?
**Answer:** Physical memory is actual RAM, while virtual memory is the logical address space seen by processes, backed by RAM and swap.

### 19) What is a zombie process?
**Answer:** A zombie is a terminated process whose exit status has not yet been collected by its parent.

### 20) What is an orphan process?
**Answer:** An orphan process is a child whose parent exited; it gets adopted by PID 1 or `systemd`.

### 21) How do you kill a process?
**Answer:** Use `kill PID`, `kill -9 PID` only if graceful termination fails, or `pkill` by process name.

### 22) What is the difference between SIGTERM and SIGKILL?
**Answer:** SIGTERM allows graceful shutdown, while SIGKILL forcefully stops the process and cannot be caught or ignored.

### 23) How do you inspect open files for a process?
**Answer:** Use `lsof -p PID`.

### 24) How do you check which process is listening on a port?
**Answer:** Use `ss -tulpn`, `netstat -tulpn`, or `lsof -i :PORT`.

---

## Storage and Filesystems

### 25) What is the difference between hard link and soft link?
**Answer:** A hard link points to the inode directly, while a soft link points to a path. Soft links can cross filesystems; hard links generally cannot.

### 26) How do you check disk usage?
**Answer:** Use `df -h` for filesystem usage and `du -sh` for directory-level usage.

### 27) How do you find large files quickly?
**Answer:** Use `find / -type f -size +500M 2>/dev/null` or combine `du`, `sort`, and `head`.

### 28) What is inode exhaustion?
**Answer:** It happens when a filesystem runs out of inodes even if disk space remains, usually due to too many small files.

### 29) How do you check inode usage?
**Answer:** Use `df -i`.

### 30) What is the difference between ext4 and XFS?
**Answer:** ext4 is widely used and stable, while XFS is strong for large filesystems and parallel I/O workloads.

### 31) How do you mount a filesystem?
**Answer:** Use `mount /dev/device /mountpoint`, and persist it in `/etc/fstab` if needed.

### 32) What is `/etc/fstab`?
**Answer:** It defines filesystems and mount options that should be mounted automatically at boot.

### 33) What happens if `/etc/fstab` is wrong?
**Answer:** The system may fail to boot properly or drop into emergency mode if a required mount cannot be completed.

### 34) How do you check filesystem errors?
**Answer:** Use `fsck` on unmounted filesystems or inspect logs for corruption warnings.

### 35) What is journaling in a filesystem?
**Answer:** Journaling records metadata changes before committing them, helping recovery after crashes.

### 36) How do you check memory and CPU trends historically?
**Answer:** Use `sar`, `atop`, monitoring agents, or central observability tools.

### 37) What is `vmstat` used for?
**Answer:** It shows process, memory, paging, block I/O, traps, and CPU activity.

### 38) What is `iostat` used for?
**Answer:** It helps analyse disk I/O performance, throughput, and device utilisation.

### 39) What is `iotop` used for?
**Answer:** It shows which processes are generating disk I/O in real time.

### 40) What is `strace`?
**Answer:** `strace` traces system calls and signals, useful for debugging hangs, permission issues, and missing files.

### 41) What is `ltrace`?
**Answer:** `ltrace` traces library calls made by a program, useful for debugging dynamically linked applications.

### 42) How do you troubleshoot a slow Linux server?
**Answer:** Check CPU, memory, disk I/O, network, logs, recent changes, and whether the issue is application, kernel, or infrastructure related.

---

## Services, Boot, and Scheduling

### 43) What is nice value?
**Answer:** Nice value influences process scheduling priority. Lower values mean higher priority.

### 44) What is the difference between nice and renice?
**Answer:** `nice` starts a process with a priority, while `renice` changes the priority of an existing process.

### 45) What is a daemon?
**Answer:** A daemon is a background service process, usually started during boot and managed by `systemd`.

### 46) How do you manage services in Linux?
**Answer:** Use `systemctl start`, `stop`, `restart`, `status`, `enable`, and `disable`.

### 47) How do you check service logs?
**Answer:** Use `journalctl -u service-name`.

### 48) What is the difference between `systemctl enable` and `start`?
**Answer:** `start` runs the service now, while `enable` configures it to start automatically at boot.

### 49) What is a target in systemd?
**Answer:** A target is a grouping of units representing a system state, similar to runlevels.

### 50) What are Linux runlevels?
**Answer:** Traditional runlevels define system modes like single-user, multi-user, and reboot. In modern systems, targets replace them.

### 51) How do you check current target?
**Answer:** Use `systemctl get-default` or `systemctl list-units --type=target`.

### 52) What is SELinux?
**Answer:** SELinux is a mandatory access control system that enforces security policies beyond standard Unix permissions.

### 53) How do you check SELinux status?
**Answer:** Use `getenforce` or `sestatus`.

### 54) What is AppArmor?
**Answer:** AppArmor is another Linux security framework that restricts application capabilities using profiles.

---

## Permissions and Security

### 55) What is the difference between chmod, chown, and chgrp?
**Answer:** `chmod` changes permissions, `chown` changes owner, and `chgrp` changes group ownership.

### 56) What does permission 755 mean?
**Answer:** Owner has read, write, execute; group and others have read and execute.

### 57) What does permission 644 mean?
**Answer:** Owner has read and write; group and others have read only.

### 58) What is umask?
**Answer:** Umask defines default permission bits removed when new files and directories are created.

### 59) How do you check current umask?
**Answer:** Use `umask`.

### 60) What is the difference between `/bin`, `/sbin`, `/usr/bin`, and `/usr/sbin`?
**Answer:** `/bin` and `/usr/bin` contain user commands, while `/sbin` and `/usr/sbin` contain system administration binaries.

### 61) What is `/proc`?
**Answer:** `/proc` is a virtual filesystem exposing kernel and process information.

### 62) What is `/sys`?
**Answer:** `/sys` is a virtual filesystem exposing kernel device and driver information.

### 63) How do you check CPU information?
**Answer:** Use `lscpu`, `cat /proc/cpuinfo`, or monitoring tools.

### 64) How do you check memory information?
**Answer:** Use `free -m`, `cat /proc/meminfo`, or `vmstat`.

### 65) How do you check kernel version?
**Answer:** Use `uname -r`.

### 66) What is the difference between `uname -r` and `uname -a`?
**Answer:** `uname -r` shows kernel release only, while `uname -a` shows full system information.

### 67) How do you schedule recurring jobs?
**Answer:** Use `cron` or `systemd timers`.

### 68) How do you edit cron jobs?
**Answer:** Use `crontab -e` for user jobs or edit system cron files under `/etc/cron*`.

### 69) What is the difference between cron and anacron?
**Answer:** Cron runs at fixed times, while anacron ensures missed jobs run later on systems not always powered on.

---

## Networking and Connectivity

### 70) How do you check network interfaces?
**Answer:** Use `ip addr`, `ip link`, or `nmcli` depending on the environment.

### 71) How do you check routing table?
**Answer:** Use `ip route`.

### 72) How do you test DNS resolution?
**Answer:** Use `dig`, `nslookup`, or `host`.

### 73) How do you test connectivity to a remote port?
**Answer:** Use `nc -zv host port`, `telnet`, or `curl` for HTTP-based services.

### 74) What is the difference between `curl` and `wget`?
**Answer:** `curl` is flexible for API and protocol testing, while `wget` is commonly used for downloading files recursively or non-interactively.

### 75) How do you inspect active network connections?
**Answer:** Use `ss -tunap`.

### 76) What is `tcpdump` used for?
**Answer:** It captures and analyses network packets for troubleshooting connectivity, latency, and protocol issues.

### 77) What is `rsync` used for?
**Answer:** `rsync` efficiently synchronises files and directories, transferring only changed blocks.

### 78) What is the difference between `scp` and `rsync`?
**Answer:** `scp` copies files directly, while `rsync` is more efficient for repeated syncs and supports compression and delta transfer.

---

## Shell, Text Processing, and Utilities

### 79) How do you compress files in Linux?
**Answer:** Use `tar`, `gzip`, `bzip2`, `xz`, or `zip` depending on the use case.

### 80) What is the difference between `tar` and `gzip`?
**Answer:** `tar` archives files, while `gzip` compresses data. They are often used together as `.tar.gz`.

### 81) How do you search text inside files?
**Answer:** Use `grep`, `egrep`, or `ripgrep` for faster recursive searches.

### 82) What is the difference between grep and awk?
**Answer:** `grep` is mainly for pattern matching, while `awk` is stronger for field-based text processing and reporting.

### 83) What is `sed` used for?
**Answer:** `sed` is used for stream editing, such as substitutions, deletions, and scripted text transformations.

### 84) How do you count lines, words, and bytes in a file?
**Answer:** Use `wc`.

### 85) How do you sort and deduplicate lines?
**Answer:** Use `sort | uniq` or `sort -u`.

### 86) What is the difference between `>` and `>>`?
**Answer:** `>` overwrites a file, while `>>` appends to it.

### 87) What does `2>` mean in shell?
**Answer:** It redirects standard error to a file.

### 88) What does `2>&1` mean?
**Answer:** It redirects standard error to the same destination as standard output.

### 89) What is a pipe in Linux?
**Answer:** A pipe passes the output of one command as input to another using `|`.

### 90) How do you find files modified in the last 24 hours?
**Answer:** Use `find /path -type f -mtime -1`.

### 91) How do you find files by name?
**Answer:** Use `find /path -name "filename"` or `locate` if the database is updated.

### 92) What is `nohup` used for?
**Answer:** It allows a command to continue running after the terminal session ends.

### 93) What is `screen` or `tmux` used for?
**Answer:** They provide persistent terminal sessions useful for long-running tasks and remote administration.

### 94) How do you check logged-in users?
**Answer:** Use `who`, `w`, or `users`.

### 95) How do you check system uptime?
**Answer:** Use `uptime`.

### 96) How do you check recent login history?
**Answer:** Use `last`.

### 97) How do you troubleshoot permission denied errors?
**Answer:** Check file ownership, mode bits, ACLs, SELinux/AppArmor context, mount options, and the effective user running the process.

### 98) What is an ACL in Linux?
**Answer:** Access Control Lists provide more granular permissions than standard owner-group-other permissions.

### 99) How do you check ACLs?
**Answer:** Use `getfacl`.

---

## Production Troubleshooting Mindset

### 100) What is your approach to Linux troubleshooting in production?
**Answer:** I follow a structured path: confirm impact, gather metrics and logs, isolate whether the issue is CPU, memory, disk, network, or permissions, mitigate safely, and then document root cause and prevention steps.

### Senior incident checklist
- Confirm business impact and affected scope
- Check recent deployments or configuration changes
- Validate CPU, memory, disk, and network health
- Review logs before restarting blindly
- Prefer low-risk mitigation first
- Capture root cause and preventive action after recovery

---

## Rapid Revision Sheet

### High-value commands to remember
| Area | Useful commands |
|---|---|
| Processes | `ps`, `top`, `htop`, `kill`, `pkill`, `lsof` |
| Memory | `free -m`, `vmstat`, `sar`, `dmesg` |
| Disk | `df -h`, `df -i`, `du -sh`, `iostat`, `iotop` |
| Services | `systemctl`, `journalctl`, `systemd-analyze` |
| Network | `ip addr`, `ip route`, `ss -tunap`, `tcpdump`, `dig`, `curl` |
| Files | `find`, `grep`, `awk`, `sed`, `wc`, `sort`, `uniq` |

### Last-minute revision reminders
- Explain commands in context, not in isolation
- Mention logs and metrics together
- Show safe mitigation thinking
- Highlight trade-offs where relevant
- Speak like an operator, not only like an exam candidate

---

## Final Interview Advice

> For senior Linux interviews, definitions are only the starting point.  
> Strong candidates explain **diagnosis, mitigation, trade-offs, and prevention** with calm, production-safe reasoning.