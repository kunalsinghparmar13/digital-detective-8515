# Mission 6 — Git and GitHub

## 1. Task / objective

Understand version control, stage and commit changes, create a branch, open a Pull Request and explain the collaboration workflow.

## 2. Work completed

### Task 6.1: Understand the basic Git workflow

Commands used: `git status`, `git add README.md`, `git commit -m "..."`, `git log --oneline`

| Git operation | What it does in my own words |
|---|---|
| Check repository status (`git status`) | Shows which branch I am on and which files are changed, staged or not tracked yet |
| Stage selected changes (`git add <file>`) | Picks the changes I want to put in the next commit, like putting items in a box before sealing it |
| Create a commit (`git commit -m "message"`) | Saves a snapshot of the staged changes in the history with a message saying what I did |
| View commit history (`git log --oneline`) | Shows the list of past commits with their short IDs and messages |

**Staging vs committing:** staging (`git add`) only selects which changes will go into the next save; nothing is saved in history yet and I can still change my mind. Committing (`git commit`) actually saves those staged changes as a permanent snapshot in the project history.

My recent history (`git log --oneline`):

```
37d097e Build number converter and practise data representation
f0feb1e Compare compilers and interpreters
9e35ae3 Document operating system and file management
6dbf49b Mark Mission 2 as completed in index
220f6f1 Complete Terminal and file management mission
```

### Task 6.2: Create and use a branch

Commands used:

```
git switch -c update-about
# added a "My Learning" section to the README
git status
git add README.md
git commit -m "Add My Learning section to README"
git push -u origin update-about
```

Change made: added a short **My Learning** section to the main [README](../README.md) with three things I learned so far (OS, Python/number systems, Git branches).

### Task 6.3: Create a Pull Request

Steps:
1. Opened my repository on GitHub.
2. Clicked **Compare & pull request** for the `update-about` branch.
3. Created a Pull Request from `update-about` into `main`.
4. Description: "Adds a My Learning section to the README describing what I learned in Missions 3 to 5."
5. Reviewed the changed file in the **Files changed** tab.
6. After merging, updated my local copy:

```
git switch main
git pull
```

PR status: the `update-about` branch was merged into `main` — the commit "Merge branch 'update-about'" is visible in the commit history.

**Branch:** a branch is a separate line of work. I can make changes on it without touching `main`, so if something goes wrong the main project is still safe.

**Pull Request:** a Pull Request is a request on GitHub to merge one branch into another. It shows exactly what changed so other people can review and comment before it is merged. These are useful when many people work on the same project because everyone can work on their own branch at the same time and changes are checked before they reach `main`.

### Task 6.4: Build your Git command glossary

| Command | What it does |
|---|---|
| `git init` | Starts a new Git repository in the current folder |
| `git status` | Shows the current branch and which files are changed or staged |
| `git add <file>` | Stages a file so it goes into the next commit |
| `git commit -m "msg"` | Saves the staged changes as a snapshot with a message |
| `git log --oneline` | Shows the commit history, one line per commit |
| `git branch` | Lists all branches (or creates one with `git branch <name>`) |
| `git switch <name>` | Moves to another branch (`-c` creates a new one first) |
| `git push -u origin <branch>` | Uploads my branch and commits to GitHub |
| `git pull` | Downloads the latest changes from GitHub and merges them into my branch |

## 3. Commands / tools used

Git, GitHub website, VS Code, Terminal. Commands: `git status`, `git add`, `git commit`, `git log`, `git switch -c`, `git push`, `git pull`.

## 4. My understanding

Git keeps a history of my project so I can go back to older versions. I first stage changes with `add`, then save them with `commit`, and send them to GitHub with `push`. Branches let me work on something separately, and a Pull Request lets others review the branch before it is merged into `main`.

## 5. Difficulties faced

Understanding the difference between staging and committing, and remembering to switch back to `main` and pull after the PR was merged.

## 6. How I resolved them

I used `git status` after every step to see what was staged and which branch I was on.

## 7. Evidence / files

- `README.md` (this file) with the Git workflow table, branch/PR steps and command glossary.
- The `My Learning` section in the [root README](../README.md), added on the `update-about` branch.

## 8. Commit details

Commit message: `Complete Git and GitHub collaboration mission` — pushed to GitHub.
