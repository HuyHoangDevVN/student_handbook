# Quản lý File Trong Terminal

Phần này gom các thao tác làm việc với file, thư mục và đọc nội dung file.

---

## Quản lý file

---

## Tạo thư mục

```bash
mkdir project
```

Tạo nhiều cấp:

```bash
mkdir -p project/src/utils
```

---

## Tạo file

```bash
touch index.js
```

---

## Copy file

```bash
cp file.txt backup.txt
```

Copy folder:

```bash
cp -r src/ src_backup/
```

---

## Di chuyển / đổi tên

```bash
mv old.txt new.txt
```

---

## Xoá file

```bash
rm file.txt
```

---

## Xoá folder

```bash
rm -rf folder/
```

!!! danger "Cảnh báo"
Luôn kiểm tra kỹ path trước khi dùng `rm -rf`.

---

## Xem nội dung file

---

### In toàn bộ file

```bash
cat file.txt
```

---

### Xem 20 dòng đầu

```bash
head -20 file.txt
```

---

### Xem 20 dòng cuối

```bash
tail -20 file.txt
```

---

### Theo dõi log realtime

```bash
tail -f app.log
```

---

### Xem file theo trang

```bash
less file.txt
```

Thoát bằng:

```
q
```

---

### Đếm số dòng

```bash
wc -l file.txt
```

---

