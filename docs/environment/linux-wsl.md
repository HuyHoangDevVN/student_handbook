# Cài Đặt WSL Và Làm Quen Linux

Phần này hướng dẫn cài WSL 2 và cách truy cập file giữa Windows và WSL.

---

## 1. Cài đặt WSL 2

Mở **PowerShell (Admin)**:

```powershell
wsl --install
```

WSL sẽ tự động:

- bật **Virtual Machine Platform**
- cài **Ubuntu**
- cấu hình **WSL 2**

---

### Chọn distro cụ thể

```powershell
wsl --install -d Ubuntu-22.04
```

---

### Kiểm tra WSL

```powershell
wsl -l -v
```

Ví dụ:

```text
NAME            STATE           VERSION
Ubuntu          Running         2
```

---

### Mở WSL

Cách dễ nhất:

Mở **Windows Terminal → chọn Ubuntu**

---

## Truy cập file Windows từ WSL

Trong WSL:

```bash
cd /mnt/c/Users/<your-user>
```

---

## Truy cập file WSL từ Windows

Trong Windows Explorer:

```text
\\wsl$\Ubuntu\home\<your-user>
```

---

