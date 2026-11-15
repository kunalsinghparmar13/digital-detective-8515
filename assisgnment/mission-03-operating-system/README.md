# Mission 3: Understand the operating system

## Task 3.1: Explore your operating system

Commands used: `uname -sr`, `cat /etc/os-release` (on Mac: `sw_vers`), `whoami`, `df -h /`, `ps aux | head -n 6`

| Information explored | What it tells you | My observation (privacy-safe) |
|---|---|---|
| Operating system / system details | Which OS and kernel version the computer is running | Ubuntu 24.04 (Linux kernel 6.18) |
| Current account identity | Which user account is logged in and running the commands | [redacted] |
| Available and used storage | How big the drive is, how much is used and how much is free | About 23% of the drive is used, the rest is free |
| System activity snapshot | Which programs (processes) are running right now | About 80 processes running, like the shell, system workers and the terminal itself |

## Task 3.2: Understand processes

Command used: `ps aux` (I also opened a browser and a text editor and then looked at the list again, and in Activity Monitor on Mac).

- **What is a process?** A process is a program that is currently running. When I open an app, the OS creates a process for it and gives it CPU time and memory.
- **What does the PID column represent?** PID means Process ID. It is a unique number the OS gives to each running process so it can track it (and so we can stop it with `kill PID`).
- **Two examples of processes running on my computer:**
  1. The web browser (application I opened myself)
  2. A background system process, like the system init process (PID 1) or the Finder / file indexing service

## Task 3.3: Understand paths and permissions

Commands used: `pwd`, `cd mission-03-operating-system`, `pwd`, `cd ..`, `ls -l notes.txt`

Observation: when I moved into the subfolder, `pwd` showed the same path with `/mission-03-operating-system` added at the end. After `cd ..` it went back to the assignment folder.

- **Absolute path:** the full path starting from the root `/`. It works from anywhere.
  Example: `/home/[redacted]/digital-detective-8515/assisgnment/notes.txt`
- **Relative path:** a path starting from the folder I am in right now.
  Example: `mission-03-operating-system/README.md` (from inside the assignment folder) or `../notes.txt` (from inside a mission folder)

Detailed listing of a file:

```
-rw-r--r-- 1 [redacted] [redacted] 47 Nov 15 17:10 notes.txt
```

The first part `-rw-r--r--` means: `-` it is a file, then `rw-` is for the **owner**, `r--` for the group and `r--` for others.
So the **owner can read and write** the file but **cannot execute** it. Others can only read it.

| Permission | Meaning | Example |
|---|---|---|
| r - Read | Allows a file's contents to be read | Opening a text file |
| w - Write | Allows a file to be changed | Editing a text file |
| x - Execute | Allows a file to be run; on a directory, allows access/traversal | Running a script |

## Task 3.4: Explain operating-system responsibilities

| OS responsibility | My explanation | Example |
|---|---|---|
| Process management | The OS starts and stops programs and shares the CPU between them so many apps can run at the same time | Playing music while browsing the web |
| Memory management | The OS gives RAM to each program and takes it back when the program closes, so programs don't overwrite each other | Closing Chrome frees up RAM for other apps |
| Device management | The OS talks to hardware using drivers and controls input and output devices | Plugging in a mouse or printer and it just works |
| File management | The OS organises files into folders and lets us create, open, copy, move and delete them | Saving notes.txt into the assignment folder |
| User interface / shell | The OS gives us a way to talk to the computer, either a GUI with windows and icons or a shell where we type commands | Using Terminal to type `ls`, or clicking icons in Finder |
| Security and permissions | The OS controls who can log in and who can read, write or run each file | notes.txt can be edited by its owner but only read by others |

## Tools and commands used

Terminal, VS Code, Git. Commands: `uname`, `whoami`, `df -h`, `ps aux`, `pwd`, `cd`, `ls -l`.

## What I understood

The operating system is the manager of the computer. It runs processes, gives them memory, talks to devices, keeps files organised and decides who is allowed to do what. Every running program is a process with its own PID, and every file has permissions for the owner, group and others. Absolute paths start from the root and relative paths start from where I am.

## Difficulty faced

Reading the permission letters like `-rw-r--r--` was confusing at first, until I split them into three groups of three.
