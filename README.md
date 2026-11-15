# Digital Detective

This is my Diwali independent learning assignment. In it I explore how a computer works from the inside: hardware and software, the Terminal, the operating system, how programs run, how numbers and text are stored, how Git and GitHub help me save and share work, and how computers talk to each other over a network.

Name: Kunal Singh Parmar
USN: N/A

## Missions

| Mission | Topic | Status |
|---|---|---|
| [Mission 0](mission-00-setup/README.md) | Setup of the repository and tools | Completed |
| [Mission 1](mission-01-computer-basics/README.md) | Computer basics, IPOS, hardware and software | Completed |
| [Mission 2](mission-02-terminal/README.md) | Terminal, file management, flags, pipes, package managers | Completed |
| [Mission 3](mission-03-operating-system/README.md) | Operating system, processes, paths and permissions | Completed |
| [Mission 4](mission-04-programs/README.md) | How programs run, compiler vs interpreter | Completed |
| [Mission 5](mission-05-numbers-data/README.md) | Binary, hexadecimal, number converter, text encoding | Completed |
| [Mission 6](mission-06-git-github/README.md) | Git workflow, branches and Pull Requests | Completed |
| [Mission 7](mission-07-networking/README.md) | Networks, DNS, routers and how a website opens | Completed |
| [Mission 8](mission-08-final-report/README.md) | Final report and submission | Completed |

## Topics explored

- Input, Processing, Output and Storage (IPOS)
- Hardware, operating system, application and utility software
- Terminal commands, file operations, flags, pipes and package managers
- Operating-system responsibilities, processes and PIDs, absolute and relative paths, file permissions
- Compilers and interpreters, running a Python program
- Decimal, binary and hexadecimal conversion, ASCII and UTF-8
- Git staging, commits, history, branches and Pull Requests
- LAN, MAN, WAN, DNS, routers, protocols, packet switching and client-server

## How to run the number converter

You need Python 3 installed.

```
cd mission-05-numbers-data
python3 number_converter.py
```

Type a positive whole number (for example `25`) and press Enter. The program prints the number in binary (`11001`) and hexadecimal (`19`).

## Repository structure

```
README.md
mission-00-setup/README.md
mission-01-computer-basics/README.md
mission-02-terminal/README.md            (+ notes.txt, notes-backup-renamed.txt)
mission-03-operating-system/README.md
mission-04-programs/README.md            (+ hello.py)
mission-05-numbers-data/README.md        (+ number_converter.py)
mission-06-git-github/README.md
mission-07-networking/README.md
mission-08-final-report/README.md
evidence/
```

## My Learning

- The operating system manages processes, memory, devices, files and permissions.
- Python is run by an interpreter, and numbers can be written in decimal, binary or hexadecimal.
- Git saves versions of my work, and branches let me try changes without breaking main.
- DNS turns website names into IP addresses so my browser (the client) can reach the server.

## Summary

I learned that a computer takes input, processes it, shows output and stores data, and the operating system manages all of this. Using the Terminal made me understand files, folders and permissions better than clicking. I wrote Python programs, converted numbers between number systems, used Git to track every mission and learned how my browser actually loads a website.

## Note

Each mission was documented in its own README and committed separately with its own meaningful commit message, so the commit history shows the work mission by mission.
