# Mission 8 — Final report and submission

## 1. Task / objective

Review the complete repository, make the root README useful to a visitor, verify all mission commits and documentation, and submit the repository link.

## 2. Work completed

### Step 1 — Verify the repository structure

I checked that the repository follows the required structure and that every mission folder has its own README and work.

| Required path | Present? | Contents |
|---|---|---|
| README.md | Yes | Project overview, mission links, learning summary and navigation |
| mission-00-setup/README.md | Yes | Setup details and repository structure |
| mission-01-computer-basics/README.md | Yes | IPOS, hardware/software and everyday systems |
| mission-02-terminal/README.md | Yes | Terminal practice and explanations (+ notes files) |
| mission-03-operating-system/README.md | Yes | Operating-system notes and observations |
| mission-04-programs/README.md + hello.py | Yes | Program execution and comparison |
| mission-05-numbers-data/README.md + number_converter.py | Yes | Conversions, encoding and working converter |
| mission-06-git-github/README.md | Yes | Git, branch and Pull Request learning |
| mission-07-networking/README.md | Yes | Network concepts and observations |
| mission-08-final-report/README.md | Yes | Final verification and submission details (this file) |
| evidence/ | Yes | Kept for optional privacy-safe screenshots |

### Step 2 — Update the root README

The [root README](../README.md) now has: an introduction explaining the purpose of the assignment, a mission index with links, a list of topics explored, instructions to run the number converter, a summary of what I learned, and a note that each mission was committed separately.

### Step 3 — Final repository review

| Mission | Status | Corrections made in the final review |
|---|---|---|
| 0 — Setup | Completed | Rewritten in the required README format |
| 1 — Computer basics | Completed | Rewritten in the required README format |
| 2 — Terminal | Completed | Required README format; moved `notes.txt` and the backup into this mission's folder; replaced my username with [redacted] |
| 3 — Operating system | Completed | Required README format; updated the path examples after the folders moved |
| 4 — Programs | Completed | Required README format |
| 5 — Numbers and data | Completed | Required README format |
| 6 — Git and GitHub | Completed | Required README format; added PR / merge status |
| 7 — Networking | Completed | Written in the required README format; IP and network details redacted |
| 8 — Final report | Completed | This report |

Other corrections:
- Moved all mission folders from the `assisgnment/` folder to the top of the repository so the structure matches the required layout and GitHub shows the root README on the front page.
- Removed the macOS `.DS_Store` files and added a `.gitignore` so they are not committed again.
- Checked that no passwords, tokens, IP addresses, Wi-Fi names or usernames are in the repository.

### Step 4 — Final checklist

- [x] All mission folders are present and each has its own README.md.
- [x] Every mission README records the task, commands/tools used, understanding and difficulties.
- [x] Every mission has its own meaningful commit, and all required commits are pushed.
- [x] IPOS, hardware, software and computer-system examples are included.
- [x] Terminal operations, file management, flags and pipes are explained.
- [x] Operating system, processes, paths, storage and permissions are covered.
- [x] Compiler and interpreter are compared.
- [x] Number conversions include working and Python verification.
- [x] The number_converter.py program runs successfully with at least three test values.
- [x] Git commit history, branch and Pull Request activity are visible.
- [x] LAN, MAN, WAN, DNS, router, protocols and client-server are explained.
- [x] The root README explains the project and how to run the converter.
- [x] Personal information has been removed from screenshots and outputs.
- [x] All final changes are committed and pushed to GitHub.

### Step 5 — Submit the repository

1. Open the GitHub repository in a browser.
2. Confirm that the repository is public and all latest changes are pushed.
3. Copy the repository URL: https://github.com/kunalsinghparmar13/digital-detective-8515
4. Submit the URL using the Google Form shared by the instructor.
5. Be ready to explain any mission in my own words when classes resume.

## 3. Commands / tools used

| Command / tool | Purpose |
|---|---|
| `git mv` | Move the mission folders to the top of the repository without losing their history |
| `git status` | Check what changed before committing |
| `git log --oneline` | Verify that every mission has its own commit |
| `python3 number_converter.py` | Re-test the converter before submitting |
| GitHub website | Check that the files, README and commits are visible |
| VS Code | Edit the README files |

## 4. My understanding

A good repository is easy for someone else to understand: a clear root README, one folder per mission, the same README format everywhere and meaningful commit messages. Reviewing my own work also helped me find mistakes, like files in the wrong place and private details that should be hidden.

## 5. Difficulties faced

My missions were inside an extra `assisgnment/` folder, so GitHub showed "Add a README" on the front page and the structure did not match the required layout.

## 6. How I resolved them

I used `git mv` to move everything to the top level of the repository, so GitHub now shows the root README on the front page and Git keeps the history of each file.

## 7. Evidence / files

- `README.md` (this file) — final checklist and review
- [Root README](../README.md) — project overview and navigation
- The GitHub commit history showing one commit per mission

## 8. Commit details

Commit message: `Complete final report and verify assignment submission` — pushed to GitHub on the `main` branch.
