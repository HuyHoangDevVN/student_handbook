# Systemd Và Vận Hành Service

Phần này hướng dẫn quản lý service với systemd và phần tự luyện cuối chương.

---

## 6. Quáº£n lĂ½ service (systemd)

---

### Kiá»ƒm tra service

```bash
sudo systemctl status nginx
```

---

### Start / Stop

```bash
sudo systemctl start nginx
sudo systemctl stop nginx
```

---

### Restart

```bash
sudo systemctl restart nginx
```

---

### Auto start khi boot

```bash
sudo systemctl enable nginx
```

---

## Lá»—i thÆ°á»ng gáº·p

| Lá»—i                            | NguyĂªn nhĂ¢n               | CĂ¡ch kháº¯c phá»¥c            |
| ------------------------------ | ------------------------- | ------------------------- |
| `sudo: command not found`      | user khĂ´ng cĂ³ quyá»n sudo  | thĂªm user vĂ o group sudo  |
| `Unable to locate package`     | apt chÆ°a update           | cháº¡y `sudo apt update`    |
| WSL truy cáº­p `/mnt/c` ráº¥t cháº­m | filesystem cross-boundary | Ä‘áº·t project trong `/home` |
| Port conflict                  | service khĂ¡c dĂ¹ng port    | `lsof -i :PORT`           |

---

## BĂ i táº­p

### BĂ i 1

CĂ i `tree` vĂ  hiá»ƒn thá»‹ cáº¥u trĂºc thÆ° má»¥c:

```bash
tree ~ -L 2
```

---

### BĂ i 2

Táº¡o script:

```bash
touch hello.sh
```

Ná»™i dung:

```bash
echo "Hello from Linux!"
```

Cáº¥p quyá»n:

```bash
chmod +x hello.sh
```

Cháº¡y:

```bash
./hello.sh
```

---

### BĂ i 3

TĂ¬m process chiáº¿m port **8080**.

---

## TĂ i liá»‡u tham kháº£o

- [https://learn.microsoft.com/en-us/windows/wsl/](https://learn.microsoft.com/en-us/windows/wsl/)
- [https://linuxjourney.com/](https://linuxjourney.com/)

*
