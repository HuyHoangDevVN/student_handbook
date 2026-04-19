# Git Cheat Sheet

> Copy-paste nhanh các lệnh Git thường dùng.

---

## Setup

```bash
git config --global user.name "Tên"
git config --global user.email "email@example.com"
git config --global init.defaultBranch main
git config --global core.autocrlf input      # Linux/macOS
git config --global core.autocrlf true       # Windows
git config --list                            # Xem config
```

## Khởi tạo & Clone

```bash
git init                       # Tạo repo mới
git clone URL                  # Clone repo
git clone URL folder-name      # Clone vào folder cụ thể
```

## Cơ bản

```bash
git status                     # Xem trạng thái
git add file.txt               # Stage file
git add .                      # Stage tất cả
git commit -m "message"        # Commit
git commit --amend             # Sửa commit gần nhất
git push origin main           # Push
git pull origin main           # Pull (fetch + merge)
git fetch origin               # Fetch (không merge)
```

## Branch

```bash
git branch                     # Liệt kê branch
git branch -a                  # Liệt kê cả remote
git switch -c feature/login    # Tạo + chuyển branch
git switch main                # Chuyển branch
git branch -d feature/login    # Xoá branch đã merge
git branch -D feature/login    # Force xoá branch
```

## Merge & Rebase

```bash
git merge feature/login        # Merge branch vào hiện tại
git rebase main                # Rebase branch hiện tại lên main
git rebase --continue          # Tiếp tục rebase sau fix conflict
git rebase --abort             # Huỷ rebase
git merge --abort              # Huỷ merge
```

## Stash

```bash
git stash                      # Lưu tạm thay đổi
git stash list                 # Xem danh sách stash
git stash pop                  # Lấy lại stash gần nhất
git stash drop                 # Xoá stash gần nhất
git stash apply stash@{0}      # Apply stash cụ thể
```

## Undo & Recovery

```bash
git restore file.txt           # Bỏ thay đổi (chưa stage)
git restore --staged file.txt  # Unstage file
git reset --soft HEAD~1        # Undo commit (giữ staged)
git reset HEAD~1               # Undo commit (giữ unstaged)
git reset --hard HEAD~1        # Undo commit (MẤT code!)
git revert HEAD                # Tạo commit đảo ngược
git reflog                     # Xem mọi thao tác (emergency!)
```

## Log & Diff

```bash
git log --oneline              # Log ngắn gọn
git log --oneline --graph --all  # Log dạng graph
git log -5                     # 5 commit gần nhất
git diff                       # Xem thay đổi (chưa stage)
git diff --staged              # Xem thay đổi (đã stage)
git diff main..feature         # So sánh 2 branch
git show commit-hash           # Xem chi tiết commit
```

## Remote

```bash
git remote -v                  # Xem remote URLs
git remote add origin URL      # Thêm remote
git push -u origin branch      # Push + set upstream
git push --force-with-lease    # Force push (an toàn)
```

## Tag

```bash
git tag v1.0.0                 # Tạo tag
git tag -a v1.0.0 -m "msg"    # Tag kèm message
git push origin v1.0.0         # Push tag
git push origin --tags         # Push tất cả tags
```

## Commit Message Convention

```
feat:     Tính năng mới
fix:      Sửa bug
docs:     Thay đổi docs
style:    Format code
refactor: Tái cấu trúc
test:     Thêm/sửa test
chore:    Config, build tools

# Ví dụ
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
