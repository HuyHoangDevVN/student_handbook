# Branching, Merge Và Rebase

Phần này tập trung vào branch workflow, merge, rebase và xử lý conflict.

---

## Branch

Branch giĂºp phĂ¡t triá»ƒn **nhiá»u tĂ­nh nÄƒng song song**.

---

### Xem branch

```bash
git branch
```

---

### Táº¡o branch

```bash
git branch feature/login
```

---

### Chuyá»ƒn branch

```bash
git checkout feature/login
```

hoáº·c:

```bash
git switch feature/login
```

---

### Táº¡o + chuyá»ƒn branch

```bash
git checkout -b feature/login
```

hoáº·c:

```bash
git switch -c feature/login
```

---

### XoĂ¡ branch

```bash
git branch -d feature/login
```

Force delete:

```bash
git branch -D feature/login
```

---

## Quy táº¯c Ä‘áº·t tĂªn branch

| Prefix    | Má»¥c Ä‘Ă­ch           |
| --------- | ------------------ |
| feature/  | tĂ­nh nÄƒng má»›i      |
| bugfix/   | sá»­a bug            |
| hotfix/   | sá»­a lá»—i production |
| docs/     | thay Ä‘á»•i docs      |
| refactor/ | tĂ¡i cáº¥u trĂºc code  |

---

### VĂ­ dá»¥

```
feature/user-auth
bugfix/login-crash
docs/update-readme
refactor/cleanup-utils
```

---

## Merge vs Rebase

---

## Merge

```bash
git checkout main
git merge feature/login
```

```mermaid
gitGraph
    commit id: "A"
    commit id: "B"
    branch feature
    commit id: "C"
    commit id: "D"
    checkout main
    commit id: "E"
    merge feature
```

Merge táº¡o **merge commit**.

---

## Rebase

```bash
git checkout feature/login
git rebase main
```

Sau Ä‘Ă³:

```bash
git checkout main
git merge feature/login
```

---

!!! warning "LÆ°u Ă½"
KhĂ´ng nĂªn **rebase branch Ä‘Ă£ push vĂ  Ä‘ang Ä‘Æ°á»£c nhiá»u ngÆ°á»i sá»­ dá»¥ng**.

---

## Giáº£i quyáº¿t conflict

Git sáº½ Ä‘Ă¡nh dáº¥u:

```
<<<<<<< HEAD
Code branch hiá»‡n táº¡i
=======
Code branch khĂ¡c
>>>>>>> feature/login
```

---

### CĂ¡ch xá»­ lĂ½

1. Má»Ÿ file bá»‹ conflict
2. Chá»n code Ä‘Ăºng
3. XoĂ¡ marker conflict
4. Stage file

```bash
git add file.txt
```

5. Tiáº¿p tá»¥c

```bash
git merge --continue
```

hoáº·c

```bash
git rebase --continue
```

---

## Commit message chuáº©n

NĂªn dĂ¹ng **Conventional Commits**.

---

### Format

```
type(scope): description
```

---

### CĂ¡c type phá»• biáº¿n

| Type     | Ă nghÄ©a        |
| -------- | -------------- |
| feat     | thĂªm feature   |
| fix      | sá»­a bug        |
| docs     | thay Ä‘á»•i docs  |
| style    | format code    |
| refactor | refactor code  |
| test     | test           |
| chore    | config / build |

---

### VĂ­ dá»¥

```
feat(auth): add JWT refresh token endpoint
```

---

