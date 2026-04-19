# Systemd Và Vận Hành Service

Phần này hướng dẫn quản lý service với systemd và phần tự luyện cuối chương.

---

## 6. Quản lý service (systemd)

---

### Kiểm tra service

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

## Lỗi thường gặp

| Lỗi                            | Nguyên nhân               | Cách khắc phục            |
| ------------------------------ | ------------------------- | ------------------------- |
| `sudo: command not found`      | user không có quyền sudo  | thêm user vào group sudo  |
| `Unable to locate package`     | apt chưa update           | chạy `sudo apt update`    |
| WSL truy cập `/mnt/c` rất chậm | filesystem cross-boundary | đặt project trong `/home` |
| Port conflict                  | service khác dùng port    | `lsof -i :PORT`           |

---

## Bài tập

### Bài 1

Cài `tree` và hiển thị cấu trúc thư mục:

```bash
tree ~ -L 2
```

---

### Bài 2

Tạo script:

```bash
touch hello.sh
```

Nội dung:

```bash
echo "Hello from Linux!"
```

Cấp quyền:

```bash
chmod +x hello.sh
```

Chạy:

```bash
./hello.sh
```

---

### Bài 3

Tìm process chiếm port **8080**.

---

## Tài liệu tham khảo

- [https://learn.microsoft.com/en-us/windows/wsl/](https://learn.microsoft.com/en-us/windows/wsl/)
- [https://linuxjourney.com/](https://linuxjourney.com/)

*
