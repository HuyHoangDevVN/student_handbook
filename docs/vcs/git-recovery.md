# Undo Và Recovery Trong Git

Phần này gom các kỹ thuật hoàn tác, phục hồi và phần tự luyện cuối chương.

---

## Undo & Recovery

---

### Bỏ file khỏi staging

```bash
git restore --staged file.txt
```

---

### Bỏ thay đổi

```bash
git restore file.txt
```

---

### Quay lại commit trước

```bash
git reset HEAD~1
```

---

### Reset mạnh

```bash
git reset --hard HEAD~1
```

---

### Khôi phục bằng reflog

```bash
git reflog
git reset --hard HEAD@{2}
```

---

!!! tip "Mẹo quan trọng"
`git reflog` lưu lại gần như mọi thao tác Git.
Bạn có thể khôi phục commit kể cả khi đã `reset --hard`.

---

## Lỗi thường gặp

| Lỗi                  | Nguyên nhân           | Cách sửa            |
| -------------------- | --------------------- | ------------------- |
| not a git repository | chưa init repo        | chạy `git init`     |
| failed to push       | remote có commit mới  | `git pull --rebase` |
| merge conflict       | 2 người sửa cùng file | resolve thủ công    |
| detached HEAD        | checkout commit       | `git switch main`   |

---

## Bài tập

### Bài 1

Tạo repo mới và commit 3 lần.

---

### Bài 2

Tạo branch:

```
feature/hello
```

Merge vào main.

---

### Bài 3

Tạo conflict và thực hành resolve.

---

### Bài 4

Viết 5 commit message theo chuẩn **Conventional Commits**.

---

## Tài liệu tham khảo

```
https://git-scm.com/book
```

```
https://learngitbranching.js.org
```

```
https://www.conventionalcommits.org
```
