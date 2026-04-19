# GitHub Workflow

GitHub Workflow mô tả cách các developer **làm việc nhóm với Git và GitHub**.

Quy trình phổ biến:

```text
Task → Branch → Commit → Pull Request → Code Review → Merge
```

---

## Mục tiêu

Sau bài này bạn có thể:

- tạo và quản lý **Pull Request**
- thực hiện **Code Review**
- sử dụng **GitHub Issues**
- áp dụng **branching strategy trong team**

---

## Yêu cầu

Bạn cần:

- hiểu **Git cơ bản**
- có tài khoản **GitHub**
- bật **2FA**

---

## GitHub Flow (Branching Strategy)

GitHub Flow là workflow phổ biến cho web application.

```mermaid
gitGraph
    commit id: "init"
    branch feature/user-api
    commit id: "add model"
    commit id: "add routes"
    checkout main
    merge feature/user-api id: "PR merged"
    branch bugfix/login
    commit id: "fix token validation"
    checkout main
    merge bugfix/login id: "PR merged"
```

---

## Nguyên tắc

1. `main` luôn **deployable**
2. mỗi task → **một branch**
3. push branch → tạo **Pull Request**
4. **review trước khi merge**
5. xoá branch sau khi merge

---

## Tạo Pull Request

---

## 1. Tạo branch

```bash
git switch -c feature/user-profile
```

Code xong:

```bash
git add .
git commit -m "feat(user): add profile page"
```

Push:

```bash
git push -u origin feature/user-profile
```

---

## 2. Tạo PR trên GitHub

Vào repo → **Pull requests → New Pull Request**

Chọn:

```text
base: main
compare: feature/user-profile
```

---

## Template Pull Request

```markdown
## Mô tả

Thêm trang profile cho user.

## Thay đổi

- thêm UserProfile component
- thêm API endpoint /users/profile
- thêm test

## Checklist

- [x] code đúng style
- [x] tests pass
- [x] docs cập nhật

Closes #15
```

---

## 3. Request Review

Sau khi tạo PR:

- assign **reviewer**
- thêm **labels**
- link **issue**

---

## Code Review

Code review giúp:

- phát hiện bug
- đảm bảo code quality
- chia sẻ kiến thức trong team

---

## Các loại review

| Action          | Ă nghĩa |
| --------------- | ------- |
| Approve         | code OK |
| Comment         | góp ý   |
| Request changes | cần sửa |

---

## Checklist review

Khi review code:

- [ ] logic đúng
- [ ] không có security issue
- [ ] có test cho feature mới
- [ ] tên biến rõ ràng
- [ ] không có `console.log` hoặc code thừa

---

## Khi nhận feedback

Khi reviewer comment:

1. đọc kỹ comment
2. sửa code
3. push commit mới

```bash
git add .
git commit -m "fix: address review comments"
git push
```

GitHub sẽ **tự cập nhật Pull Request**.

---

## Conflict trên Pull Request

Conflict xảy ra khi:

```text
branch của bạn quá cũ so với main
```

---

## Cách 1 – Rebase

```bash
git fetch origin
git rebase origin/main
```

Fix conflict nếu có:

```bash
git add .
git rebase --continue
```

Push:

```bash
git push --force-with-lease
```

---

## Cách 2 – Merge main

```bash
git merge origin/main
```

Sau đó:

```bash
git push
```

---

!!! tip "Mẹo"
Luôn dùng:

```text
--force-with-lease
```

thay vì:

```text
--force
```

---

## GitHub Issues

Issue dùng để **track bug hoặc task**.

---

## Ví dụ Issue

```markdown
Title: [BUG] Login fails with special characters

## Mô tả

Login lỗi khi password chứa ký tự đặc biệt.

## Steps to reproduce

1. Vào /login
2. nhập password chứa &
3. click Login

## Expected

Login thành công.

## Actual

Server trả 500 error.
```

---

## Labels phổ biến

| Label            | Ă nghĩa            |
| ---------------- | ------------------ |
| bug              | lỗi                |
| feature          | tính năng          |
| docs             | documentation      |
| good first issue | task cho người mới |
| priority: high   | ưu tiên cao        |

---

## `.gitignore` cơ bản

```gitignore
node_modules/
.venv/
__pycache__/

.env
.env.local

.vscode/settings.json
.idea/

.DS_Store
Thumbs.db

dist/
build/

*.log
```

---

!!! danger "Quan trọng"
Không commit:

- `.env`
- password
- API key
- secret token

Nếu lỡ commit, **phải rotate secret ngay lập tức**.

---

## Lỗi thường gặp

| Lỗi              | Nguyên nhân       | Cách sửa      |
| ---------------- | ----------------- | ------------- |
| PR bị conflict   | branch quá cũ     | rebase main   |
| push bị reject   | remote khác local | pull rồi push |
| commit nhầm main | quên tạo branch   | reset commit  |
| PR quá lớn       | nhiều thay đổi    | chia nhỏ PR   |

---

## Bài tập

### Bài 1

Fork repository handbook.

---

### Bài 2

Tạo branch:

```text
docs/fix-typo
```

Sửa 1 lỗi và tạo Pull Request.

---

### Bài 3

Review Pull Request của bạn khác.

---

### Bài 4

Tạo 1 Issue theo template.

---

## Tài liệu tham khảo

```text
https://docs.github.com/en/get-started/using-github/github-flow
```

```text
https://docs.github.com/en/pull-requests
```
