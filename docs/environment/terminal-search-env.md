# Tìm Kiếm Và Biến Môi Trường

Phần này gom các lệnh tìm kiếm, biến môi trường, mẹo hữu ích và phần tự luyện.

---

## TĂ¬m kiáº¿m file

---

### TĂ¬m file theo tĂªn

```bash
find . -name "*.js"
```

---

### TĂ¬m text trong file

```bash
grep "TODO" -r src/
```

---

### TĂ¬m kĂ¨m sá»‘ dĂ²ng

```bash
grep -rn "error" .
```

---

### TĂ¬m theo extension

```bash
grep -rn "error" --include="*.log" .
```

---

### Ripgrep (nhanh hÆ¡n)

```bash
rg "TODO" src/
```

---

## Biáº¿n mĂ´i trÆ°á»ng

---

### Xem biáº¿n

```bash
echo $HOME
echo $PATH
```

---

### Táº¡o biáº¿n táº¡m

```bash
export MY_VAR="hello"
```

---

### Sá»­ dá»¥ng

```bash
echo $MY_VAR
```

---

### LÆ°u vÄ©nh viá»…n

ThĂªm vĂ o:

```
~/.bashrc
```

hoáº·c

```
~/.zshrc
```

VĂ­ dá»¥:

```bash
echo 'export MY_VAR="hello"' >> ~/.bashrc
```

Sau Ä‘Ă³ reload:

```bash
source ~/.bashrc
```

---

## Lá»‡nh há»¯u Ă­ch khĂ¡c

```bash
which python
```

ÄÆ°á»ng dáº«n binary.

---

```bash
whoami
```

User hiá»‡n táº¡i.

---

```bash
df -h
```

Dung lÆ°á»£ng disk.

---

```bash
du -sh folder/
```

KĂ­ch thÆ°á»›c folder.

---

```bash
history | grep docker
```

TĂ¬m lá»‡nh trong history.

---

## Lá»—i thÆ°á»ng gáº·p

| Lá»—i               | NguyĂªn nhĂ¢n      | CĂ¡ch sá»­a        |
| ----------------- | ---------------- | --------------- |
| command not found | chÆ°a cĂ i package | cĂ i package     |
| permission denied | thiáº¿u quyá»n      | dĂ¹ng `sudo`     |
| no such file      | sai path         | kiá»ƒm tra `ls`   |
| kĂ½ tá»± láº¡          | encoding sai     | kiá»ƒm tra locale |

---

## BĂ i táº­p

### BĂ i 1

Táº¡o cáº¥u trĂºc thÆ° má»¥c:

```
myproject/
src/
tests/
docs/
```

báº±ng **má»™t lá»‡nh**.

---

### BĂ i 2

TĂ¬m táº¥t cáº£ file `.md` vĂ  Ä‘áº¿m sá»‘ dĂ²ng.

---

### BĂ i 3

TĂ¬m **10 lá»‡nh gáº§n nháº¥t chá»©a `git`** trong history.

---

## TĂ i liá»‡u tham kháº£o

```
https://linuxcommand.org/tlcl.php
```

```
https://explainshell.com/
```
