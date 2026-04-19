# GitHub Workflow

GitHub Workflow mĂ´ táº£ cĂ¡ch cĂ¡c developer **lĂ m viá»‡c nhĂ³m vá»›i Git vĂ  GitHub**.

Quy trĂ¬nh phá»• biáº¿n:

```text
Task â†’ Branch â†’ Commit â†’ Pull Request â†’ Code Review â†’ Merge
```

---

## Má»¥c tiĂªu

Sau bĂ i nĂ y báº¡n cĂ³ thá»ƒ:

- táº¡o vĂ  quáº£n lĂ½ **Pull Request**
- thá»±c hiá»‡n **Code Review**
- sá»­ dá»¥ng **GitHub Issues**
- Ă¡p dá»¥ng **branching strategy trong team**

---

## YĂªu cáº§u

Báº¡n cáº§n:

- hiá»ƒu **Git cÆ¡ báº£n**
- cĂ³ tĂ i khoáº£n **GitHub**
- báº­t **2FA**

---

## GitHub Flow (Branching Strategy)

GitHub Flow lĂ  workflow phá»• biáº¿n cho web application.

```mermaid
gitGraph
    commit id: "init"
    branch feature/user-api
    commit id: "add model"
    commit id: "add routes"
    checkout main
    merge feature/user-api id: "PR merged"
    branch bugfix/login
    commit id: "fix token validation"
    checkout main
    merge bugfix/login id: "PR merged"
```

---

## NguyĂªn táº¯c

1. `main` luĂ´n **deployable**
2. má»—i task â†’ **má»™t branch**
3. push branch â†’ táº¡o **Pull Request**
4. **review trÆ°á»›c khi merge**
5. xoĂ¡ branch sau khi merge

---

## Táº¡o Pull Request

---

## 1. Táº¡o branch

```bash
git switch -c feature/user-profile
```

Code xong:

```bash
git add .
git commit -m "feat(user): add profile page"
```

Push:

```bash
git push -u origin feature/user-profile
```

---

## 2. Táº¡o PR trĂªn GitHub

VĂ o repo â†’ **Pull requests â†’ New Pull Request**

Chá»n:

```text
base: main
compare: feature/user-profile
```

---

## Template Pull Request

```markdown
## MĂ´ táº£

ThĂªm trang profile cho user.

## Thay Ä‘á»•i

- thĂªm UserProfile component
- thĂªm API endpoint /users/profile
- thĂªm test

## Checklist

- [x] code Ä‘Ăºng style
- [x] tests pass
- [x] docs cáº­p nháº­t

Closes #15
```

---

## 3. Request Review

Sau khi táº¡o PR:

- assign **reviewer**
- thĂªm **labels**
- link **issue**

---

## Code Review

Code review giĂºp:

- phĂ¡t hiá»‡n bug
- Ä‘áº£m báº£o code quality
- chia sáº» kiáº¿n thá»©c trong team

---

## CĂ¡c loáº¡i review

| Action          | Ă nghÄ©a |
| --------------- | ------- |
| Approve         | code OK |
| Comment         | gĂ³p Ă½   |
| Request changes | cáº§n sá»­a |

---

## Checklist review

Khi review code:

- [ ] logic Ä‘Ăºng
- [ ] khĂ´ng cĂ³ security issue
- [ ] cĂ³ test cho feature má»›i
- [ ] tĂªn biáº¿n rĂµ rĂ ng
- [ ] khĂ´ng cĂ³ `console.log` hoáº·c code thá»«a

---

## Khi nháº­n feedback

Khi reviewer comment:

1. Ä‘á»c ká»¹ comment
2. sá»­a code
3. push commit má»›i

```bash
git add .
git commit -m "fix: address review comments"
git push
```

GitHub sáº½ **tá»± cáº­p nháº­t Pull Request**.

---

## Conflict trĂªn Pull Request

Conflict xáº£y ra khi:

```text
branch cá»§a báº¡n quĂ¡ cÅ© so vá»›i main
```

---

## CĂ¡ch 1 â€“ Rebase

```bash
git fetch origin
git rebase origin/main
```

Fix conflict náº¿u cĂ³:

```bash
git add .
git rebase --continue
```

Push:

```bash
git push --force-with-lease
```

---

## CĂ¡ch 2 â€“ Merge main

```bash
git merge origin/main
```

Sau Ä‘Ă³:

```bash
git push
```

---

!!! tip "Máº¹o"
LuĂ´n dĂ¹ng:

```text
--force-with-lease
```

thay vĂ¬:

```text
--force
```

---

## GitHub Issues

Issue dĂ¹ng Ä‘á»ƒ **track bug hoáº·c task**.

---

## VĂ­ dá»¥ Issue

```markdown
Title: [BUG] Login fails with special characters

## MĂ´ táº£

Login lá»—i khi password chá»©a kĂ½ tá»± Ä‘áº·c biá»‡t.

## Steps to reproduce

1. VĂ o /login
2. nháº­p password chá»©a &
3. click Login

## Expected

Login thĂ nh cĂ´ng.

## Actual

Server tráº£ 500 error.
```

---

## Labels phá»• biáº¿n

| Label            | Ă nghÄ©a            |
| ---------------- | ------------------ |
| bug              | lá»—i                |
| feature          | tĂ­nh nÄƒng          |
| docs             | documentation      |
| good first issue | task cho ngÆ°á»i má»›i |
| priority: high   | Æ°u tiĂªn cao        |

---

## `.gitignore` cÆ¡ báº£n

```gitignore
node_modules/
.venv/
__pycache__/

.env
.env.local

.vscode/settings.json
.idea/

.DS_Store
Thumbs.db

dist/
build/

*.log
```

---

!!! danger "Quan trá»ng"
KhĂ´ng commit:

- `.env`
- password
- API key
- secret token

Náº¿u lá»¡ commit, **pháº£i rotate secret ngay láº­p tá»©c**.

---

## Lá»—i thÆ°á»ng gáº·p

| Lá»—i              | NguyĂªn nhĂ¢n       | CĂ¡ch sá»­a      |
| ---------------- | ----------------- | ------------- |
| PR bá»‹ conflict   | branch quĂ¡ cÅ©     | rebase main   |
| push bá»‹ reject   | remote khĂ¡c local | pull rá»“i push |
| commit nháº§m main | quĂªn táº¡o branch   | reset commit  |
| PR quĂ¡ lá»›n       | nhiá»u thay Ä‘á»•i    | chia nhá» PR   |

---

## BĂ i táº­p

### BĂ i 1

Fork repository handbook.

---

### BĂ i 2

Táº¡o branch:

```text
docs/fix-typo
```

Sá»­a 1 lá»—i vĂ  táº¡o Pull Request.

---

### BĂ i 3

Review Pull Request cá»§a báº¡n khĂ¡c.

---

### BĂ i 4

Táº¡o 1 Issue theo template.

---

## TĂ i liá»‡u tham kháº£o

```text
https://docs.github.com/en/get-started/using-github/github-flow
```

```text
https://docs.github.com/en/pull-requests
```
