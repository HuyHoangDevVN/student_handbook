# Process Và Network Cơ Bản

Phần này tập trung vào process, port và các lệnh network thiết yếu.

---

## 4. Quản lý process

---

### Xem process

```bash
ps aux
```

---

### Tìm process

```bash
ps aux | grep python
```

---

### Xem realtime

```bash
htop
```

hoặc

```bash
top
```

---

### Kill process

```bash
kill 12345
```

Force kill:

```bash
kill -9 12345
```

---

### Kill theo tên

```bash
pkill -f "node server.js"
```

---

### Chạy process background

```bash
python app.py &
```

---

### Đưa process về foreground

```bash
fg
```

---

## 5. Network cơ bản

---

### Xem IP

Linux:

```bash
ip addr show
```

macOS:

```bash
ifconfig
```

---

### Kiểm tra kết nối

```bash
ping google.com -c 4
```

---

### Xem port đang mở

Linux:

```bash
ss -tulnp
```

macOS:

```bash
lsof -i :8080
```

---

### Kiểm tra service

```bash
curl -I http://localhost:3000
```

---

### DNS lookup

```bash
nslookup example.com
```

hoặc

```bash
dig example.com
```

---

### Download file

```bash
wget https://example.com/file.zip
```

hoặc

```bash
curl -O https://example.com/file.zip
```

---

