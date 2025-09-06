# Git Commands Cheat Sheet

## Installation & Setup

### Install Git
```bash
# macOS
brew install git
# Ubuntu
sudo apt-get install git
```

### Configure User
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## Initialize & Clone

### Initialize Repository
```bash
git init
```

### Clone Repository
```bash
git clone https://github.com/user/repo.git
```

## Basic Workflow

### Add Files
```bash
git add filename
```

### Commit Changes
```bash
git commit -m "Commit message"
```

### Push to Remote
```bash
git push origin main
```

### Pull from Remote
```bash
git pull origin main
```

## Branches

### Create Branch
```bash
git branch new-branch
```

### Switch Branch
```bash
git checkout new-branch
```

### Merge Branch
```bash
git merge new-branch
```

## Logs & History

### View Log
```bash
git log
```

### View Status
```bash
git status
```

## Undo & Reset

### Undo Last Commit (keep changes)
```bash
git reset --soft HEAD~1
```

### Discard Changes in File
```bash
git checkout -- filename
```

## References
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Docs](https://docs.github.com/en/get-started/using-git)
