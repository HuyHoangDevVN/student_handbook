# Package Và Permissions Trên Linux

Phần này gom các thao tác quản lý package và quyền truy cập trong Linux.

---

## 2. Quáº£n lĂ½ package vá»›i apt

Ubuntu sá»­ dá»¥ng **APT package manager**.

---

### Cáº­p nháº­t package list

```bash
sudo apt update
```

---

### NĂ¢ng cáº¥p há»‡ thá»‘ng

```bash
sudo apt upgrade -y
```

---

### CĂ i package

```bash
sudo apt install -y curl wget htop tree jq
```

---

### Gá»¡ package

```bash
sudo apt remove package-name
```

---

### TĂ¬m package

```bash
apt search keyword
```

---

## 3. Há»‡ thá»‘ng quyá»n (Permissions)

Linux dĂ¹ng **permission model**:

```text
owner | group | others
```

---

### VĂ­ dá»¥ `ls -la`

```text
-rw-r--r--  1 user group  4096 Jan 15 10:30 file.txt
drwxr-xr-x  2 user group  4096 Jan 15 10:30 folder/
```

Giáº£i thĂ­ch:

| KĂ½ tá»± | Ă nghÄ©a |
| ----- | ------- |
| `r`   | read    |
| `w`   | write   |
| `x`   | execute |

---

### GiĂ¡ trá»‹ sá»‘

| Permission | Value |
| ---------- | ----- |
| read       | 4     |
| write      | 2     |
| execute    | 1     |

---

### VĂ­ dá»¥

```bash
chmod 755 script.sh
```

Giáº£i thĂ­ch:

```
7 = rwx
5 = r-x
5 = r-x
```

---

### Cáº¥p quyá»n thá»±c thi

```bash
chmod +x script.sh
```

---

### Äá»•i owner

```bash
chown user:group file.txt
```

---

### Ăp dá»¥ng Ä‘á»‡ quy

```bash
chmod -R 755 folder/
chown -R user:group folder/
```

---

