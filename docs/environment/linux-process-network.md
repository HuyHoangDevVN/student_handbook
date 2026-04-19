# Process Và Network Cơ Bản

Phần này tập trung vào process, port và các lệnh network thiết yếu.

---

## 4. Quáº£n lĂ½ process

---

### Xem process

```bash
ps aux
```

---

### TĂ¬m process

```bash
ps aux | grep python
```

---

### Xem realtime

```bash
htop
```

hoáº·c

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

### Kill theo tĂªn

```bash
pkill -f "node server.js"
```

---

### Cháº¡y process background

```bash
python app.py &
```

---

### ÄÆ°a process vá» foreground

```bash
fg
```

---

## 5. Network cÆ¡ báº£n

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

### Kiá»ƒm tra káº¿t ná»‘i

```bash
ping google.com -c 4
```

---

### Xem port Ä‘ang má»Ÿ

Linux:

```bash
ss -tulnp
```

macOS:

```bash
lsof -i :8080
```

---

### Kiá»ƒm tra service

```bash
curl -I http://localhost:3000
```

---

### DNS lookup

```bash
nslookup example.com
```

hoáº·c

```bash
dig example.com
```

---

### Download file

```bash
wget https://example.com/file.zip
```

hoáº·c

```bash
curl -O https://example.com/file.zip
```

---

