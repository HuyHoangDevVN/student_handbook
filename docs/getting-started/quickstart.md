# Quickstart

Thiáº¿t láº­p **mĂ´i trÆ°á»ng phĂ¡t triá»ƒn cÆ¡ báº£n trong ~30 phĂºt**.

Sau khi hoĂ n thĂ nh trang nĂ y, báº¡n sáº½ cĂ³ thá»ƒ:

- CĂ i Ä‘áº·t cĂ¡c cĂ´ng cá»¥ phĂ¡t triá»ƒn cáº§n thiáº¿t
- Clone repository handbook
- Cháº¡y thá»­ stack development cho sample app InternHub API

---

## Má»¥c tiĂªu

Sau bĂ i nĂ y báº¡n sáº½:

- CĂ i Ä‘áº·t **Git**
- CĂ i Ä‘áº·t **Docker**
- Thiáº¿t láº­p **Python environment**
- (Tuá»³ chá»n) cĂ i **Node.js**
- Cháº¡y thá»­ **Docker container**

Case study xuyen suot sau quickstart la [InternHub API](sample-project.md).

---

## YĂªu cáº§u trÆ°á»›c khi báº¯t Ä‘áº§u

Báº¡n cáº§n chuáº©n bá»‹:

- MĂ¡y tĂ­nh cháº¡y
  - **Windows 10/11**
  - **macOS 12+**
  - **Ubuntu 22.04+**

- Káº¿t ná»‘i Internet

- TĂ i khoáº£n **GitHub**

---

## 1. CĂ i Ä‘áº·t Git

Git lĂ  cĂ´ng cá»¥ **version control** dĂ¹ng Ä‘á»ƒ quáº£n lĂ½ source code.

### Windows

```bash
# CĂ i Git báº±ng winget
winget install Git.Git
```

Hoáº·c táº£i tá»«:

```
https://git-scm.com/download/win
```

---

### macOS

```bash
# CĂ i Git báº±ng Xcode tools
xcode-select --install

# hoáº·c dĂ¹ng Homebrew
brew install git
```

---

### Ubuntu

```bash
sudo apt update
sudo apt install -y git
```

---

### Kiá»ƒm tra cĂ i Ä‘áº·t

```bash
git --version
```

VĂ­ dá»¥:

```
git version 2.43.0
```

---

## Cáº¥u hĂ¬nh Git láº§n Ä‘áº§u

Thiáº¿t láº­p thĂ´ng tin commit:

```bash
git config --global user.name "TĂªn cá»§a báº¡n"
git config --global user.email "email@example.com"
```

Thiáº¿t láº­p branch máº·c Ä‘á»‹nh:

```bash
git config --global init.defaultBranch main
```

Thiáº¿t láº­p newline:

```bash
# macOS / Linux
git config --global core.autocrlf input

# Windows
git config --global core.autocrlf true
```

---

## 2. CĂ i Docker

Docker giĂºp cháº¡y á»©ng dá»¥ng trong **container**.

---

## Windows / macOS

Táº£i Docker Desktop:

```
https://www.docker.com/products/docker-desktop
```

### LÆ°u Ă½ (Windows)

Báº­t **WSL 2 backend** trong Docker Desktop.

---

## Ubuntu

```bash
sudo apt update
sudo apt install -y docker.io docker-compose-plugin

sudo usermod -aG docker $USER
```

Sau Ä‘Ă³ **logout vĂ  login láº¡i**.

---

### Kiá»ƒm tra Docker

```bash
docker --version
docker compose version
```

Cháº¡y container test:

```bash
docker run --rm hello-world
```

---

## 3. CĂ i Python

Python Ä‘Æ°á»£c dĂ¹ng cho nhiá»u project backend vĂ  data.

---

## CĂ¡ch 1 â€” Anaconda (khuyáº¿n nghá»‹)

Táº£i táº¡i:

```
https://www.anaconda.com/download
```

Táº¡o mĂ´i trÆ°á»ng:

```bash
conda create -n myproject python=3.11 -y
conda activate myproject
python --version
```

---

## CĂ¡ch 2 â€” Python thuáº§n

Táº£i Python:

```
https://www.python.org/downloads/
```

Táº¡o virtual environment:

```bash
python -m venv .venv
```

KĂ­ch hoáº¡t mĂ´i trÆ°á»ng:

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```bash
.\.venv\Scripts\Activate.ps1
```

Kiá»ƒm tra:

```bash
python --version
```

---

## 4. CĂ i Node.js (tuá»³ chá»n)

Náº¿u báº¡n lĂ m **frontend hoáº·c fullstack**, cáº§n Node.js.

KhuyĂªn dĂ¹ng **nvm** Ä‘á»ƒ quáº£n lĂ½ phiĂªn báº£n.

---

## Linux / macOS

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

source ~/.bashrc

nvm install 20
nvm use 20

node --version
```

---

## Windows

CĂ i **nvm-windows**:

```
https://github.com/coreybutler/nvm-windows
```

---

## 5. Clone repository

Clone repository cá»§a handbook Ä‘á»ƒ láº¥y toĂ n bá»™ docs vĂ  resources cho InternHub API:

```bash
git clone https://github.com/<github-org>/student-it-handbook.git

cd student-it-handbook
```

Thay `<github-org>` bằng organization hoặc username GitHub thực tế.

---

## 6. Cháº¡y thá»­ á»©ng dá»¥ng máº«u

Cháº¡y PostgreSQL stack cho InternHub API:

```bash
cd resources/docker

docker compose -f postgres-compose.yml up -d
```

Kiá»ƒm tra container:

```bash
docker ps
```

Kiem tra ket noi database:

```bash
docker exec -it postgres-dev psql -U dev -d internhub -c "SELECT 1;"
```

Neu command nay tra ve `1`, moi truong database cho sample app da san sang.

---

## Kiá»ƒm tra mĂ´i trÆ°á»ng

Cháº¡y cĂ¡c lá»‡nh sau:

```bash
git --version
docker --version
python --version
node --version
```

Náº¿u táº¥t cáº£ Ä‘á»u cháº¡y thĂ nh cĂ´ng, mĂ´i trÆ°á»ng Ä‘Ă£ sáºµn sĂ ng.

---

## Lá»—i thÆ°á»ng gáº·p

| Lá»—i                                 | NguyĂªn nhĂ¢n                      | CĂ¡ch kháº¯c phá»¥c                  |
| ----------------------------------- | -------------------------------- | ------------------------------- |
| `git: command not found`            | Git chÆ°a cĂ i hoáº·c chÆ°a thĂªm PATH | CĂ i láº¡i Git                     |
| `docker: permission denied`         | User chÆ°a thuá»™c group docker     | `sudo usermod -aG docker $USER` |
| `conda: command not found`          | ChÆ°a init conda                  | `conda init`                    |
| Docker Desktop khĂ´ng cháº¡y (Windows) | ChÆ°a báº­t WSL2                    | Báº­t trong Windows Features      |

---

## BÆ°á»›c tiáº¿p theo

Sau khi setup xong mĂ´i trÆ°á»ng:

- Äá»c **Sample Project: InternHub API**
- Äá»c **Checklist sinh viĂªn má»›i**
- Há»c **Terminal cÆ¡ báº£n**
- LĂ m quen vá»›i **Git workflow**
