# Pipe Và Redirect

Phần này giải thích cách kết hợp lệnh và điều hướng output trong shell.

---

## Pipe

Pipe cho phĂ©p **káº¿t ná»‘i output cá»§a lá»‡nh nĂ y sang input lá»‡nh khĂ¡c**.

---

### VĂ­ dá»¥

TĂ¬m process node:

```bash
ps aux | grep node
```

---

Äáº¿m file Python:

```bash
find . -name "*.py" | wc -l
```

---

Sort vĂ  loáº¡i trĂ¹ng:

```bash
cat names.txt | sort | uniq
```

---

## Redirect

Redirect cho phĂ©p **ghi output vĂ o file**.

---

### Ghi Ä‘Ă¨ file

```bash
echo "Hello" > output.txt
```

---

### Ghi thĂªm vĂ o file

```bash
echo "World" >> output.txt
```

---

### LÆ°u lá»—i

```bash
command 2> error.log
```

---

### LÆ°u cáº£ output vĂ  error

```bash
command > all.log 2>&1
```

---

