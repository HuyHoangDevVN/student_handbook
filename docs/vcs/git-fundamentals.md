# Git Fundamentals

Phần này đi qua mô hình hoạt động của Git, khởi tạo repo, commit và đồng bộ remote.

---

## Git hoáº¡t Ä‘á»™ng tháº¿ nĂ o

```mermaid
graph LR
    A[Working Directory] -->|git add| B[Staging Area]
    B -->|git commit| C[Local Repository]
    C -->|git push| D[Remote Repository]
    D -->|git pull| A
```

---

## CĂ¡c vĂ¹ng trong Git

| VĂ¹ng              | Ă nghÄ©a              |
| ----------------- | -------------------- |
| Working Directory | code trĂªn mĂ¡y        |
| Staging Area      | file chuáº©n bá»‹ commit |
| Local Repository  | lá»‹ch sá»­ commit local |
| Remote Repository | repo trĂªn GitHub     |

---

## Khá»Ÿi táº¡o repository

---

## Clone repo

```bash
git clone https://github.com/user/repo.git
cd repo
```

---

## Táº¡o repo má»›i

```bash
mkdir myproject
cd myproject
git init
```

---

## Kiá»ƒm tra tráº¡ng thĂ¡i

---

### Tráº¡ng thĂ¡i file

```bash
git status
```

---

### Xem lá»‹ch sá»­ commit

```bash
git log --oneline --graph --all
```

---

### Xem thay Ä‘á»•i

```bash
git diff
```

---

### Xem thay Ä‘á»•i Ä‘Ă£ staged

```bash
git diff --staged
```

---

## Add & Commit

---

### ThĂªm file vĂ o staging

```bash
git add file.txt
```

---

### ThĂªm toĂ n bá»™ file

```bash
git add .
```

---

### Commit

```bash
git commit -m "feat: add login API"
```

---

### Sá»­a commit gáº§n nháº¥t

```bash
git commit --amend -m "feat: add login API endpoint"
```

---

## Push & Pull

---

### Push code

```bash
git push origin main
```

---

### Pull code

```bash
git pull origin main
```

Pull thá»±c cháº¥t lĂ :

```
fetch + merge
```

---

### Chá»‰ fetch

```bash
git fetch origin
```

---

