# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective

Learn basic Terminal commands, practise changing files safely, understand flags and pipes, and understand package managers.

## 2. Work completed

### Task 2.1: Basic Terminal operations

| Operation / command name | What it does | What I observed |
|---|---|---|
| Current-directory display (pwd) | Shows the full path of the current folder | It gave me the path of the current folder |
| Directory listing (ls) | Lists files and folders | Gave me the list of files in the current folder |
| Detailed listing (ls -l) | Lists with size, date and permissions | List of files with permissions |
| Change directory (cd ..) | Moves to the parent folder | Moved back one directory |
| Create directory (mkdir) | Makes a new folder | Created a new directory |
| Create empty file (touch) | Makes an empty file | Created a new file |
| Copy file (cp) | Copies a file under a new name | Copied the file |
| Move / rename file (mv) | Renames or moves a file | Renamed the file |
| Display file contents (cat) | Prints the file | No text displayed (the file was empty) |

### Task 2.2: Practise file changes safely

Commands used: `echo`, `cat`, `cp`, `mv`.
Result: [notes.txt](notes.txt) has both lines, and a renamed backup copy [notes-backup-renamed.txt](notes-backup-renamed.txt) exists.

- Replacing vs adding: `>` replaces the contents, `>>` adds to the end.
- Copying vs moving: `cp` keeps the original, `mv` renames or moves it so the old name is gone.
- Detailed listing: `ls -l` also shows permissions, owner, size and modified date.
- Why it is useful: you can check what is in a folder and what changed before you edit anything.

### Task 2.3: Understand flags and pipes

Commands: `ls`, `ls -lah`, `ls -lah | head -n 5`

Comparison: `ls` shows only names. `ls -lah` also shows hidden files, sizes in a readable form, dates and permissions.

Pipe: in `ls -lah | head -n 5`, the left side makes the detailed listing and the right side keeps only the first 5 lines.

Output (private details replaced):

```
total 0
drwxr-xr-x@ 2 [redacted] staff    64B Nov 12 22:59 .
drwxr-xr-x  4 [redacted] staff   128B Nov 12 23:07 ..
```

### Task 2.4: Understand package managers

Commands used: `brew --version`, `pip --version`, `pip list | head -n 10`, `brew list | head -n 10`

Result: Homebrew 7.0.13 with packages such as abseil, ada-url, aws-c-auth, aws-c-cal, aws-c-common.
pip 26.2.2 (Python 3.15) with packages such as contourpy 1.4.0, cycler 0.12.1, fonttools 4.68.0, kiwisolver 1.5.1, matplotlib 3.11.2.

Why package managers are useful: they manage software from one place — install, update and remove. They track which version is installed, and save you from downloading and setting up each program by hand.

## 3. Commands / tools used

| Command / tool | Purpose |
|---|---|
| `pwd`, `ls`, `ls -l`, `ls -lah`, `cd` | See where I am and what is in a folder |
| `mkdir`, `touch` | Create folders and files |
| `cp`, `mv` | Copy, move and rename files |
| `echo`, `>`, `>>`, `cat` | Write text into a file and display it |
| `head -n 5` and the pipe `\|` | Show only the first lines of another command's output |
| `brew`, `pip` | Package managers for macOS programs and Python libraries |
| Git Bash / Terminal, VS Code, Git | Where I ran the commands, edited files and saved work |

## 4. My understanding

The Terminal lets me control the computer by typing commands. Flags like `-l` and `-a` change how a command behaves, and the pipe `|` sends the output of one command into another. Package managers install and update software for me.

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

- [notes.txt](notes.txt) — file with two lines written using `>` and `>>`
- [notes-backup-renamed.txt](notes-backup-renamed.txt) — copied and renamed backup

## 8. Commit details

Commit message: `Complete Terminal and file management mission` — pushed to GitHub.
