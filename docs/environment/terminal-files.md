# Quản lý File Trong Terminal

Phần này gom các thao tác làm việc với file, thư mục và đọc nội dung file.

---

## Quáº£n lĂ½ file

---

## Táº¡o thÆ° má»¥c

```bash
mkdir project
```

Táº¡o nhiá»u cáº¥p:

```bash
mkdir -p project/src/utils
```

---

## Táº¡o file

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

## Di chuyá»ƒn / Ä‘á»•i tĂªn

```bash
mv old.txt new.txt
```

---

## XoĂ¡ file

```bash
rm file.txt
```

---

## XoĂ¡ folder

```bash
rm -rf folder/
```

!!! danger "Cáº£nh bĂ¡o"
LuĂ´n kiá»ƒm tra ká»¹ path trÆ°á»›c khi dĂ¹ng `rm -rf`.

---

## Xem ná»™i dung file

---

### In toĂ n bá»™ file

```bash
cat file.txt
```

---

### Xem 20 dĂ²ng Ä‘áº§u

```bash
head -20 file.txt
```

---

### Xem 20 dĂ²ng cuá»‘i

```bash
tail -20 file.txt
```

---

### Theo dĂµi log realtime

```bash
tail -f app.log
```

---

### Xem file theo trang

```bash
less file.txt
```

ThoĂ¡t báº±ng:

```
q
```

---

### Äáº¿m sá»‘ dĂ²ng

```bash
wc -l file.txt
```

---

