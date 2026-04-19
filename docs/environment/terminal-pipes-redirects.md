# Pipe Và Redirect

Phần này giải thích cách kết hợp lệnh và điều hướng output trong shell.

---

## Pipe

Pipe cho phép **kết nối output của lệnh này sang input lệnh khác**.

---

### Ví dụ

Tìm process node:

```bash
ps aux | grep node
```

---

Đếm file Python:

```bash
find . -name "*.py" | wc -l
```

---

Sort và loại trùng:

```bash
cat names.txt | sort | uniq
```

---

## Redirect

Redirect cho phép **ghi output vào file**.

---

### Ghi đè file

```bash
echo "Hello" > output.txt
```

---

### Ghi thêm vào file

```bash
echo "World" >> output.txt
```

---

### Lưu lỗi

```bash
command 2> error.log
```

---

### Lưu cả output và error

```bash
command > all.log 2>&1
```

---

