# Tìm Kiếm Và Biến Môi Trường

Phần này gom các lệnh tìm kiếm, biến môi trường, mẹo hữu ích và phần tự luyện.

---

## Tìm kiếm file

---

### Tìm file theo tên

```bash
find . -name "*.js"
```

---

### Tìm text trong file

```bash
grep "TODO" -r src/
```

---

### Tìm kèm số dòng

```bash
grep -rn "error" .
```

---

### Tìm theo extension

```bash
grep -rn "error" --include="*.log" .
```

---

### Ripgrep (nhanh hơn)

```bash
rg "TODO" src/
```

---

## Biến môi trường

---

### Xem biến

```bash
echo $HOME
echo $PATH
```

---

### Tạo biến tạm

```bash
export MY_VAR="hello"
```

---

### Sử dụng

```bash
echo $MY_VAR
```

---

### Lưu vĩnh viễn

Thêm vào:

```
~/.bashrc
```

hoặc

```
~/.zshrc
```

Ví dụ:

```bash
echo 'export MY_VAR="hello"' >> ~/.bashrc
```

Sau đó reload:

```bash
source ~/.bashrc
```

---

## Lệnh hữu ích khác

```bash
which python
```

Đường dẫn binary.

---

```bash
whoami
```

User hiện tại.

---

```bash
df -h
```

Dung lượng disk.

---

```bash
du -sh folder/
```

Kích thước folder.

---

```bash
history | grep docker
```

Tìm lệnh trong history.

---

## Lỗi thường gặp

| Lỗi               | Nguyên nhân      | Cách sửa        |
| ----------------- | ---------------- | --------------- |
| command not found | chưa cài package | cài package     |
| permission denied | thiếu quyền      | dùng `sudo`     |
| no such file      | sai path         | kiểm tra `ls`   |
| ký tự lạ          | encoding sai     | kiểm tra locale |

---

## Bài tập

### Bài 1

Tạo cấu trúc thư mục:

```
myproject/
src/
tests/
docs/
```

bằng **một lệnh**.

---

### Bài 2

Tìm tất cả file `.md` và đếm số dòng.

---

### Bài 3

Tìm **10 lệnh gần nhất chứa `git`** trong history.

---

## Tài liệu tham khảo

```
https://linuxcommand.org/tlcl.php
```

```
https://explainshell.com/
```
