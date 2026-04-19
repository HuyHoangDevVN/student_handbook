# Package Và Permissions Trên Linux

Phần này gom các thao tác quản lý package và quyền truy cập trong Linux.

---

## 2. Quản lý package với apt

Ubuntu sử dụng **APT package manager**.

---

### Cập nhật package list

```bash
sudo apt update
```

---

### Nâng cấp hệ thống

```bash
sudo apt upgrade -y
```

---

### Cài package

```bash
sudo apt install -y curl wget htop tree jq
```

---

### Gỡ package

```bash
sudo apt remove package-name
```

---

### Tìm package

```bash
apt search keyword
```

---

## 3. Hệ thống quyền (Permissions)

Linux dùng **permission model**:

```text
owner | group | others
```

---

### Ví dụ `ls -la`

```text
-rw-r--r--  1 user group  4096 Jan 15 10:30 file.txt
drwxr-xr-x  2 user group  4096 Jan 15 10:30 folder/
```

Giải thích:

| Ký tự | Ă nghĩa |
| ----- | ------- |
| `r`   | read    |
| `w`   | write   |
| `x`   | execute |

---

### Giá trị số

| Permission | Value |
| ---------- | ----- |
| read       | 4     |
| write      | 2     |
| execute    | 1     |

---

### Ví dụ

```bash
chmod 755 script.sh
```

Giải thích:

```
7 = rwx
5 = r-x
5 = r-x
```

---

### Cấp quyền thực thi

```bash
chmod +x script.sh
```

---

### Đổi owner

```bash
chown user:group file.txt
```

---

### Ăp dụng đệ quy

```bash
chmod -R 755 folder/
chown -R user:group folder/
```

---

