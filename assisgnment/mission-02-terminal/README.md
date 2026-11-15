# Mission 2: Become comfortable with the Terminal

## Task 2.1: Basic Terminal operations

| Operation / command name | What it does | What I observed |
|---|---|---|
| Current-directory display (pwd) | Shows the full path of the current folder | It give me the path of current folder |
| Directory listing (ls) | Lists files and folders | Give me list of files which is current folder |
| Detailed listing (ls -l) | Lists with size, date and permissions | List of file with permission |
| Change directory (cd ..) | Moves to the parent folder | Move back to one directory pervious |
| Create directory (mkdir) | Makes a new folder | Create new directory |
| Create empty file (touch) | Makes an empty file | Create new file |
| Copy file (cp) | Copies a file under a new name | Copy the file |
| Move / rename file (mv) | Renames or moves a file | Rename the file |
| Display file contents (cat) | Prints the file | No text display |

## Task 2.2: Practise file changes safely

Commands used: echo, cat, cp, mv.
Result: notes.txt has both lines, and a renamed backup copy exists.

Notes:
- Replacing vs adding: (> replaces the contents, >> adds to the end)
- Copying vs moving: (cp keeps the original, mv renames or moves it so the old name is gone)
- Detailed listing: (ls -l also shows permissions, owner, size and modified date)
- Why it is useful: (you can check what is in a folder and what changed before you edit anything)

## Tools and commands used

Git Bash, VS Code, Git.

## What I understood



## Difficulty faced

NO Difficulty faced.
## Task 2.3: Understand flags and pipes

Commands: ls, ls -lah, ls -lah | head -n 5

Comparison: ls shows only names. ls -lah also shows hidden files, sizes in a readable form, dates and permissions.

Pipe: in ls -lah | head -n 5, the left side makes the detailed listing and the right side keeps only the first 5 lines.

Output (private details replaced):
total 0
drwxr-xr-x@ 2 fvjvdjvjs staffs    64B Nov 12 22:59 .
drwxr-xr-x  4 fvjvdjvjs  staffs   128B Nov 12 23:07 .
etc

## Task 2.4: Understand package managers

Command used:brew --version, pip --version          
pip list | head -n 10
brew list | head -n 10
Result: Homebrew 7.0.13
abseil
ada-url
aws-c-auth
aws-c-cal
aws-c-common
aws-c-compression etc.

pip 26.2.2 (folder name where python is saved) python 3.15
Package         Version
--------------- -------
contourpy       1.4.0
cycler          0.12.1
fonttools       4.68.0
kiwisolver      1.5.1
matplotlib      3.11.2 etc

Why package managers are useful: It manage your system like install, update and remove software from one place, they track which version is installed, and they save you from downloading and setting up each program by hand.