# Undo Và Recovery Trong Git

Phần này gom các kỹ thuật hoàn tác, phục hồi và phần tự luyện cuối chương.

---

## Undo & Recovery

---

### Bá» file khá»i staging

```bash
git restore --staged file.txt
```

---

### Bá» thay Ä‘á»•i

```bash
git restore file.txt
```

---

### Quay láº¡i commit trÆ°á»›c

```bash
git reset HEAD~1
```

---

### Reset máº¡nh

```bash
git reset --hard HEAD~1
```

---

### KhĂ´i phá»¥c báº±ng reflog

```bash
git reflog
git reset --hard HEAD@{2}
```

---

!!! tip "Máº¹o quan trá»ng"
`git reflog` lÆ°u láº¡i gáº§n nhÆ° má»i thao tĂ¡c Git.
Báº¡n cĂ³ thá»ƒ khĂ´i phá»¥c commit ká»ƒ cáº£ khi Ä‘Ă£ `reset --hard`.

---

## Lá»—i thÆ°á»ng gáº·p

| Lá»—i                  | NguyĂªn nhĂ¢n           | CĂ¡ch sá»­a            |
| -------------------- | --------------------- | ------------------- |
| not a git repository | chÆ°a init repo        | cháº¡y `git init`     |
| failed to push       | remote cĂ³ commit má»›i  | `git pull --rebase` |
| merge conflict       | 2 ngÆ°á»i sá»­a cĂ¹ng file | resolve thá»§ cĂ´ng    |
| detached HEAD        | checkout commit       | `git switch main`   |

---

## BĂ i táº­p

### BĂ i 1

Táº¡o repo má»›i vĂ  commit 3 láº§n.

---

### BĂ i 2

Táº¡o branch:

```
feature/hello
```

Merge vĂ o main.

---

### BĂ i 3

Táº¡o conflict vĂ  thá»±c hĂ nh resolve.

---

### BĂ i 4

Viáº¿t 5 commit message theo chuáº©n **Conventional Commits**.

---

## TĂ i liá»‡u tham kháº£o

```
https://git-scm.com/book
```

```
https://learngitbranching.js.org
```

```
https://www.conventionalcommits.org
```
