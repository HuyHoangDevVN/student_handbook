# Checklist sinh viĂªn má»›i

Checklist nĂ y giĂºp báº¡n kiá»ƒm tra xem mĂ¬nh Ä‘Ă£ **sáºµn sĂ ng tham gia vĂ o má»™t team phĂ¡t triá»ƒn pháº§n má»m** hay chÆ°a.

Danh sĂ¡ch Ä‘Æ°á»£c chia thĂ nh 3 giai Ä‘oáº¡n:

- TrÆ°á»›c ngĂ y Ä‘áº§u tiĂªn
- NgĂ y Ä‘áº§u tiĂªn
- Tuáº§n Ä‘áº§u tiĂªn

---

## TrÆ°á»›c ngĂ y Ä‘áº§u tiĂªn

HĂ£y hoĂ n thĂ nh cĂ¡c bÆ°á»›c sau trÆ°á»›c khi báº¯t Ä‘áº§u internship hoáº·c dá»± Ă¡n.

### TĂ i khoáº£n & truy cáº­p

- [ ] Táº¡o tĂ i khoáº£n **GitHub**
- [ ] Báº­t **Two-Factor Authentication (2FA)** cho GitHub
- [ ] CĂ i Ä‘áº·t **SSH key** cho GitHub (khuyáº¿n nghá»‹)

---

### CĂ´ng cá»¥ phĂ¡t triá»ƒn

- [ ] CĂ i Ä‘áº·t **Git**
- [ ] Cáº¥u hĂ¬nh `user.name` vĂ  `user.email`
- [ ] CĂ i Ä‘áº·t **Docker Desktop**
- [ ] CĂ i Ä‘áº·t **VS Code**

Extensions nĂªn cĂ i:

- GitLens
- Docker
- Python
- ESLint / Prettier

---

### MĂ´i trÆ°á»ng láº­p trĂ¬nh

- [ ] CĂ i **Python 3.11+** hoáº·c **Anaconda**
- [ ] CĂ i **Node.js 20+** (náº¿u dá»± Ă¡n sá»­ dá»¥ng)
- [ ] Kiá»ƒm tra cĂ¡c lá»‡nh sau cháº¡y Ä‘Æ°á»£c:

```bash
git --version
docker --version
python --version
node --version
```

---

### Äá»c tĂ i liá»‡u

- [ ] Äá»c pháº§n **Quickstart**
- [ ] Hiá»ƒu cĂ¡ch **clone repo vĂ  cháº¡y project**

---

## NgĂ y Ä‘áº§u tiĂªn

Má»¥c tiĂªu cá»§a ngĂ y Ä‘áº§u tiĂªn lĂ  **setup mĂ´i trÆ°á»ng vĂ  hiá»ƒu workflow cá»§a team**.

### Truy cáº­p há»‡ thá»‘ng

- [ ] Nháº­n invite vĂ o **GitHub Organization**
- [ ] Nháº­n quyá»n truy cáº­p repository

---

### Setup dá»± Ă¡n

- [ ] Clone repository chĂ­nh

```bash
git clone <repo-url>
```

- [ ] Cháº¡y Ä‘Æ°á»£c project trĂªn local

VĂ­ dá»¥:

```bash
docker compose up
```

---

### Kiá»ƒm tra workflow Git

Táº¡o branch test:

```bash
git checkout -b feature/your-name-hello
```

Sau Ä‘Ă³:

- [ ] Commit thay Ä‘á»•i
- [ ] Push branch
- [ ] Táº¡o Pull Request

---

### LĂ m quen vá»›i team

- [ ] Gáº·p **mentor / tech lead**
- [ ] Há»i vá» **workflow code review**
- [ ] Há»i vá» **quy trĂ¬nh deploy**

---

## Tuáº§n Ä‘áº§u tiĂªn

Trong tuáº§n Ä‘áº§u, má»¥c tiĂªu lĂ  **hiá»ƒu codebase vĂ  workflow lĂ m viá»‡c**.

### Hiá»ƒu dá»± Ă¡n

- [ ] Hiá»ƒu cáº¥u trĂºc folder
- [ ] Äá»c `README.md`
- [ ] Äá»c `CONTRIBUTING.md`

---

### Cháº¡y test

- [ ] Cháº¡y test suite

VĂ­ dá»¥:

```bash
npm test
```

hoáº·c

```bash
pytest
```

---

### HoĂ n thĂ nh task Ä‘áº§u tiĂªn

Má»™t task nhá» cĂ³ thá»ƒ lĂ :

- sá»­a typo
- cáº­p nháº­t documentation
- fix bug nhá»

Má»¥c tiĂªu: **hoĂ n thĂ nh Ă­t nháº¥t 1 Pull Request**.

---

### Tham gia hoáº¡t Ä‘á»™ng cá»§a team

- [ ] Tham gia **daily standup**
- [ ] Theo dĂµi **issue tracker**
- [ ] Hiá»ƒu **task board (Jira / GitHub Projects)**

---

## Ká»¹ nÄƒng cáº§n náº¯m trong thĂ¡ng Ä‘áº§u

| Ká»¹ nÄƒng          | Má»¥c tiĂªu             | TĂ i liá»‡u                                               |
| ---------------- | -------------------- | ------------------------------------------------------ |
| Terminal / Shell | Sá»­ dá»¥ng thĂ nh tháº¡o   | [Terminal](../environment/terminal.md)                 |
| Git branching    | Hiá»ƒu workflow branch | [Git](../vcs/git-basics.md)                            |
| Docker           | Cháº¡y container       | [Docker](../containers/docker.md)                      |
| SQL cÆ¡ báº£n       | Viáº¿t query           | [SQL](../databases/sql-postgres.md)                    |
| Debug & logs     | TĂ¬m lá»—i cÆ¡ báº£n       | [Troubleshooting](../troubleshooting/common-errors.md) |

---

## Máº¹o cho ngĂ y Ä‘áº§u

!!! tip "Lá»i khuyĂªn"
Äá»«ng ngáº¡i há»i khi chÆ°a hiá»ƒu.
Ghi chĂ©p láº¡i cĂ¡c hÆ°á»›ng dáº«n cá»§a mentor.

Báº¡n nĂªn táº¡o má»™t file riĂªng:

```bash
notes.md
```

Ä‘á»ƒ ghi láº¡i:

- cĂ¡c lá»‡nh thÆ°á»ng dĂ¹ng
- workflow cá»§a team
- cĂ¡c lá»—i thÆ°á»ng gáº·p
