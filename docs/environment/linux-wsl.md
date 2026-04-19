# Cài Đặt WSL Và Làm Quen Linux

Phần này hướng dẫn cài WSL 2 và cách truy cập file giữa Windows và WSL.

---

## 1. CĂ i Ä‘áº·t WSL 2

Má»Ÿ **PowerShell (Admin)**:

```powershell
wsl --install
```

WSL sáº½ tá»± Ä‘á»™ng:

- báº­t **Virtual Machine Platform**
- cĂ i **Ubuntu**
- cáº¥u hĂ¬nh **WSL 2**

---

### Chá»n distro cá»¥ thá»ƒ

```powershell
wsl --install -d Ubuntu-22.04
```

---

### Kiá»ƒm tra WSL

```powershell
wsl -l -v
```

VĂ­ dá»¥:

```text
NAME            STATE           VERSION
Ubuntu          Running         2
```

---

### Má»Ÿ WSL

CĂ¡ch dá»… nháº¥t:

Má»Ÿ **Windows Terminal â†’ chá»n Ubuntu**

---

## Truy cáº­p file Windows tá»« WSL

Trong WSL:

```bash
cd /mnt/c/Users/<your-user>
```

---

## Truy cáº­p file WSL tá»« Windows

Trong Windows Explorer:

```text
\\wsl$\Ubuntu\home\<your-user>
```

---

