# Git Cheat Sheet

> Copy-paste nhanh cĂ¡c lá»‡nh Git thÆ°á»ng dĂ¹ng.

---

## Setup

```bash
git config --global user.name "TĂªn"
git config --global user.email "email@example.com"
git config --global init.defaultBranch main
git config --global core.autocrlf input      # Linux/macOS
git config --global core.autocrlf true       # Windows
git config --list                            # Xem config
```

## Khá»Ÿi táº¡o & Clone

```bash
git init                       # Táº¡o repo má»›i
git clone URL                  # Clone repo
git clone URL folder-name      # Clone vĂ o folder cá»¥ thá»ƒ
```

## CÆ¡ báº£n

```bash
git status                     # Xem tráº¡ng thĂ¡i
git add file.txt               # Stage file
git add .                      # Stage táº¥t cáº£
git commit -m "message"        # Commit
git commit --amend             # Sá»­a commit gáº§n nháº¥t
git push origin main           # Push
git pull origin main           # Pull (fetch + merge)
git fetch origin               # Fetch (khĂ´ng merge)
```

## Branch

```bash
git branch                     # Liá»‡t kĂª branch
git branch -a                  # Liá»‡t kĂª cáº£ remote
git switch -c feature/login    # Táº¡o + chuyá»ƒn branch
git switch main                # Chuyá»ƒn branch
git branch -d feature/login    # XoĂ¡ branch Ä‘Ă£ merge
git branch -D feature/login    # Force xoĂ¡ branch
```

## Merge & Rebase

```bash
git merge feature/login        # Merge branch vĂ o hiá»‡n táº¡i
git rebase main                # Rebase branch hiá»‡n táº¡i lĂªn main
git rebase --continue          # Tiáº¿p tá»¥c rebase sau fix conflict
git rebase --abort             # Huá»· rebase
git merge --abort              # Huá»· merge
```

## Stash

```bash
git stash                      # LÆ°u táº¡m thay Ä‘á»•i
git stash list                 # Xem danh sĂ¡ch stash
git stash pop                  # Láº¥y láº¡i stash gáº§n nháº¥t
git stash drop                 # XoĂ¡ stash gáº§n nháº¥t
git stash apply stash@{0}      # Apply stash cá»¥ thá»ƒ
```

## Undo & Recovery

```bash
git restore file.txt           # Bá» thay Ä‘á»•i (chÆ°a stage)
git restore --staged file.txt  # Unstage file
git reset --soft HEAD~1        # Undo commit (giá»¯ staged)
git reset HEAD~1               # Undo commit (giá»¯ unstaged)
git reset --hard HEAD~1        # Undo commit (Máº¤T code!)
git revert HEAD                # Táº¡o commit Ä‘áº£o ngÆ°á»£c
git reflog                     # Xem má»i thao tĂ¡c (emergency!)
```

## Log & Diff

```bash
git log --oneline              # Log ngáº¯n gá»n
git log --oneline --graph --all  # Log dáº¡ng graph
git log -5                     # 5 commit gáº§n nháº¥t
git diff                       # Xem thay Ä‘á»•i (chÆ°a stage)
git diff --staged              # Xem thay Ä‘á»•i (Ä‘Ă£ stage)
git diff main..feature         # So sĂ¡nh 2 branch
git show commit-hash           # Xem chi tiáº¿t commit
```

## Remote

```bash
git remote -v                  # Xem remote URLs
git remote add origin URL      # ThĂªm remote
git push -u origin branch      # Push + set upstream
git push --force-with-lease    # Force push (an toĂ n)
```

## Tag

```bash
git tag v1.0.0                 # Táº¡o tag
git tag -a v1.0.0 -m "msg"    # Tag kĂ¨m message
git push origin v1.0.0         # Push tag
git push origin --tags         # Push táº¥t cáº£ tags
```

## Commit Message Convention

```
feat:     TĂ­nh nÄƒng má»›i
fix:      Sá»­a bug
docs:     Thay Ä‘á»•i docs
style:    Format code
refactor: TĂ¡i cáº¥u trĂºc
test:     ThĂªm/sá»­a test
chore:    Config, build tools

# VĂ­ dá»¥
feat(auth): add JWT refresh token
fix(api): validate email before insert
docs: update README installation guide
```

## Branch Naming

```
feature/user-auth
bugfix/login-crash
hotfix/security-patch
docs/update-readme
refactor/clean-utils
```
