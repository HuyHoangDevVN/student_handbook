# Lá»—i thÆ°á»ng gáº·p & CĂ¡ch xá»­ lĂ½

## Má»¥c tiĂªu

Trang nĂ y tá»•ng há»£p cĂ¡c lá»—i phá»• biáº¿n nháº¥t mĂ  sinh viĂªn gáº·p khi thá»±c táº­p, kĂ¨m nguyĂªn nhĂ¢n vĂ  cĂ¡ch xá»­ lĂ½ nhanh.

---

## Git

| #   | Lá»—i                                              | NguyĂªn nhĂ¢n                      | CĂ¡ch sá»­a                                                                               |
| --- | ------------------------------------------------ | -------------------------------- | -------------------------------------------------------------------------------------- |
| 1   | `fatal: not a git repository`                    | ChÆ°a `git init` hoáº·c sai thÆ° má»¥c | `cd` vĂ o Ä‘Ăºng thÆ° má»¥c chá»©a `.git`                                                      |
| 2   | `error: failed to push some refs`                | Remote cĂ³ commit báº¡n chÆ°a pull   | `git pull --rebase origin main` rá»“i `git push`                                         |
| 3   | `CONFLICT (content): Merge conflict in file.txt` | 2 ngÆ°á»i sá»­a cĂ¹ng vá»‹ trĂ­          | Má»Ÿ file â†’ sá»­a conflict thá»§ cĂ´ng â†’ `git add` â†’ `git commit`                             |
| 4   | `Permission denied (publickey)`                  | SSH key chÆ°a setup               | [Táº¡o SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) |
| 5   | `detached HEAD state`                            | `git checkout` vĂ o commit hash   | `git switch main` Ä‘á»ƒ quay láº¡i branch                                                   |
| 6   | Commit nháº§m file lá»›n (>100MB)                    | File vÆ°á»£t giá»›i háº¡n GitHub        | `git reset HEAD~1`, thĂªm vĂ o `.gitignore`                                              |
| 7   | Commit nháº§m `.env` / secrets                     | QuĂªn `.gitignore`                | Rotate secrets, dĂ¹ng `git filter-branch` Ä‘á»ƒ xoĂ¡ khá»i history                           |

### Script khĂ´i phá»¥c Git

```bash
# Undo commit gáº§n nháº¥t (giá»¯ code)
git reset --soft HEAD~1

# Undo táº¥t cáº£ thay Ä‘á»•i chÆ°a commit (Cáº¨N THáº¬N!)
git checkout -- .

# Xem lá»‹ch sá»­ táº¥t cáº£ thao tĂ¡c (ká»ƒ cáº£ Ä‘Ă£ reset)
git reflog

# Quay láº¡i tráº¡ng thĂ¡i báº¥t ká»³
git reset --hard HEAD@{3}
```

---

## Docker

| #   | Lá»—i                                   | NguyĂªn nhĂ¢n                      | CĂ¡ch sá»­a                                       |
| --- | ------------------------------------- | -------------------------------- | ---------------------------------------------- |
| 1   | `Cannot connect to the Docker daemon` | Docker Desktop chÆ°a cháº¡y         | Má»Ÿ Docker Desktop                              |
| 2   | `port is already allocated`           | Port Ä‘Ă£ bá»‹ chiáº¿m                 | `docker ps` â†’ stop container cÅ©, hoáº·c Ä‘á»•i port |
| 3   | `no space left on device`             | Docker dĂ¹ng háº¿t disk             | `docker system prune -a --volumes`             |
| 4   | Container exit code 137               | Out of memory (OOM killed)       | TÄƒng RAM cho Docker Desktop                    |
| 5   | Container exit ngay láº­p tá»©c           | CMD/ENTRYPOINT lá»—i               | `docker logs <name>` Ä‘á»ƒ xem lá»—i                |
| 6   | `exec format error`                   | Image build cho sai architecture | ThĂªm `--platform linux/amd64`                  |
| 7   | Volume permission denied              | Container user khĂ¡c host user    | `chown` hoáº·c dĂ¹ng `user:` trong compose        |

### Script dá»n dáº¹p Docker

```bash
# Dá»n táº¥t cáº£ (containers dá»«ng, images orphan, volumes khĂ´ng dĂ¹ng)
docker system prune -a --volumes

# Xem disk usage
docker system df

# Kill táº¥t cáº£ container Ä‘ang cháº¡y
docker stop $(docker ps -q)

# XoĂ¡ táº¥t cáº£ container
docker rm $(docker ps -aq)
```

---

## Python

| #   | Lá»—i                                                | NguyĂªn nhĂ¢n                     | CĂ¡ch sá»­a                                          |
| --- | -------------------------------------------------- | ------------------------------- | ------------------------------------------------- |
| 1   | `ModuleNotFoundError: No module named 'xxx'`       | Package chÆ°a cĂ i trong env Ä‘Ăºng | `which python` â†’ kiá»ƒm tra env â†’ `pip install xxx` |
| 2   | `command not found: python`                        | Python chÆ°a cĂ i hoáº·c alias sai  | DĂ¹ng `python3`, hoáº·c cĂ i qua pyenv/conda          |
| 3   | `pip install` bá»‹ permission denied                 | CĂ i global trĂªn Linux           | KĂ­ch hoáº¡t venv trÆ°á»›c, hoáº·c dĂ¹ng `--user`          |
| 4   | `SyntaxError: invalid syntax`                      | Sai Python version (2 vs 3)     | Äáº£m báº£o dĂ¹ng Python 3.9+                          |
| 5   | `UnicodeDecodeError`                               | File encoding khĂ´ng pháº£i UTF-8  | `open(file, encoding='utf-8')`                    |
| 6   | `IndentationError`                                 | Trá»™n tab vĂ  space               | Cáº¥u hĂ¬nh editor dĂ¹ng 4 spaces                     |
| 7   | `RecursionError: maximum recursion depth exceeded` | Äá»‡ quy vĂ´ háº¡n                   | Kiá»ƒm tra base case                                |

### Debug nhanh Python

```bash
# Kiá»ƒm tra Python nĂ o Ä‘ang dĂ¹ng
which python
python --version

# Kiá»ƒm tra package Ä‘Ă£ cĂ i chÆ°a
pip list | grep flask

# Kiá»ƒm tra env Ä‘ang dĂ¹ng
echo $VIRTUAL_ENV     # venv
echo $CONDA_DEFAULT_ENV  # conda
```

---

## Database (PostgreSQL)

| #   | Lá»—i                                              | NguyĂªn nhĂ¢n                     | CĂ¡ch sá»­a                                                     |
| --- | ------------------------------------------------ | ------------------------------- | ------------------------------------------------------------ |
| 1   | `Connection refused`                             | PostgreSQL chÆ°a cháº¡y            | `docker start postgres-dev`                                  |
| 2   | `FATAL: password authentication failed`          | Sai password                    | Kiá»ƒm tra `POSTGRES_PASSWORD` trong docker env                |
| 3   | `relation "table" does not exist`                | ChÆ°a táº¡o báº£ng                   | Cháº¡y migration hoáº·c `CREATE TABLE`                           |
| 4   | `duplicate key value violates unique constraint` | Insert data trĂ¹ng unique column | Kiá»ƒm tra data, dĂ¹ng `ON CONFLICT`                            |
| 5   | `too many connections`                           | Connection pool cáº¡n             | Kiá»ƒm tra code khĂ´ng close connection, tÄƒng `max_connections` |

```bash
# Kiá»ƒm tra PostgreSQL Ä‘ang cháº¡y
docker ps | grep postgres

# Káº¿t ná»‘i test
docker exec -it postgres-dev psql -U dev -d internhub -c "SELECT 1;"
```

---

## Network / API

| #   | Lá»—i                                   | NguyĂªn nhĂ¢n                           | CĂ¡ch sá»­a                                           |
| --- | ------------------------------------- | ------------------------------------- | -------------------------------------------------- |
| 1   | `ECONNREFUSED` / `Connection refused` | Server chÆ°a cháº¡y hoáº·c sai port        | Kiá»ƒm tra server, kiá»ƒm tra port                     |
| 2   | `CORS error` (browser)                | Server chÆ°a cho phĂ©p origin           | ThĂªm CORS middleware                               |
| 3   | `EADDRINUSE: address already in use`  | Port Ä‘Ă£ bá»‹ chiáº¿m                      | `lsof -i :PORT` â†’ `kill PID`, hoáº·c Ä‘á»•i port        |
| 4   | `ETIMEDOUT`                           | Server quĂ¡ cháº­m hoáº·c khĂ´ng reach Ä‘Æ°á»£c | Kiá»ƒm tra network, firewall, DNS                    |
| 5   | `SSL certificate problem`             | Self-signed cert hoáº·c cert expired    | Update cert, hoáº·c táº¡m táº¯t SSL verify (chá»‰ khi dev) |

```bash
# Kiá»ƒm tra port Ä‘ang má»Ÿ
lsof -i :3000          # macOS/Linux
netstat -ano | findstr :3000  # Windows

# Test connectivity
curl -v http://localhost:3000/api/health

# DNS check
nslookup api.example.com
```

---

## WSL / Windows

| #   | Lá»—i                                    | NguyĂªn nhĂ¢n                      | CĂ¡ch sá»­a                                    |
| --- | -------------------------------------- | -------------------------------- | ------------------------------------------- |
| 1   | WSL ráº¥t cháº­m                           | Project náº±m á»Ÿ `/mnt/c/`          | Chuyá»ƒn project sang `/home/user/` trong WSL |
| 2   | Line ending warning Git                | CRLF vs LF                       | `git config --global core.autocrlf input`   |
| 3   | Docker khĂ´ng cháº¡y trong WSL            | ChÆ°a báº­t WSL integration         | Docker Desktop â†’ Settings â†’ WSL Integration |
| 4   | `chmod` khĂ´ng hoáº¡t Ä‘á»™ng trĂªn `/mnt/c/` | Windows filesystem khĂ´ng support | LĂ m viá»‡c trong WSL filesystem (`/home/`)    |

---

## Quy trĂ¬nh debug chung

```mermaid
graph TB
    A[Gáº·p lá»—i] --> B{Äá»c error message}
    B --> C[Google / Stack Overflow]
    B --> D[Kiá»ƒm tra logs]
    D --> E{TĂ¬m Ä‘Æ°á»£c nguyĂªn nhĂ¢n?}
    C --> E
    E -->|CĂ³| F[Fix & Test]
    E -->|KhĂ´ng| G[Há»i Ä‘á»“ng nghiá»‡p / mentor]
    F --> H{Fix thĂ nh cĂ´ng?}
    H -->|CĂ³| I[Ghi chĂº láº¡i Ä‘á»ƒ láº§n sau]
    H -->|KhĂ´ng| G
```

**Tips debug:**

1. **Äá»c ká»¹ error message** â€“ 80% thĂ´ng tin á»Ÿ dĂ²ng cuá»‘i cĂ¹ng.
2. **Copy error message** â†’ tĂ¬m Google/Stack Overflow.
3. **Kiá»ƒm tra logs** â€“ `docker logs`, server log, browser console.
4. **Reproduce** â€“ viáº¿t láº¡i bÆ°á»›c gĂ¢y lá»—i.
5. **Isolate** â€“ comment bá»›t code Ä‘á»ƒ tĂ¬m dĂ²ng gĂ¢y lá»—i.
6. **Ghi chĂº** â€“ viáº¿t láº¡i cĂ¡ch fix Ä‘á»ƒ láº§n sau khĂ´ng máº¥t thá»i gian.

---

## TĂ i liá»‡u tham kháº£o

- [Stack Overflow](https://stackoverflow.com/)
- [DevDocs](https://devdocs.io/) â€“ Documentation cho má»i ngĂ´n ngá»¯
