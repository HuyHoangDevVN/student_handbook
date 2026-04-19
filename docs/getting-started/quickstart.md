# Quickstart

Thiết lập **môi trường phát triển cơ bản trong ~30 phút**.

Sau khi hoàn thành trang này, bạn sẽ có thể:

- Cài đặt các công cụ phát triển cần thiết
- Clone repository handbook
- Chạy thử stack development cho sample app InternHub API

---

## Mục tiêu

Sau bài này bạn sẽ:

- Cài đặt **Git**
- Cài đặt **Docker**
- Thiết lập **Python environment**
- (Tuỳ chọn) cài **Node.js**
- Chạy thử **Docker container**

Case study xuyên suốt sau quickstart là [InternHub API](sample-project.md).

---

## Yêu cầu trước khi bắt đầu

Bạn cần chuẩn bị:

- Máy tính chạy
  - **Windows 10/11**
  - **macOS 12+**
  - **Ubuntu 22.04+**

- Kết nối Internet

- Tài khoản **GitHub**

---

## 1. Cài đặt Git

Git là công cụ **version control** dùng để quản lý source code.

### Windows

```bash
# Cài Git bằng winget
winget install Git.Git
```

Hoặc tải từ:

```
https://git-scm.com/download/win
```

---

### macOS

```bash
# Cài Git bằng Xcode tools
xcode-select --install

# hoặc dùng Homebrew
brew install git
```

---

### Ubuntu

```bash
sudo apt update
sudo apt install -y git
```

---

### Kiểm tra cài đặt

```bash
git --version
```

Ví dụ:

```
git version 2.43.0
```

---

## Cấu hình Git lần đầu

Thiết lập thông tin commit:

```bash
git config --global user.name "Tên của bạn"
git config --global user.email "email@example.com"
```

Thiết lập branch mặc định:

```bash
git config --global init.defaultBranch main
```

Thiết lập newline:

```bash
# macOS / Linux
git config --global core.autocrlf input

# Windows
git config --global core.autocrlf true
```

---

## 2. Cài Docker

Docker giúp chạy ứng dụng trong **container**.

---

## Windows / macOS

Tải Docker Desktop:

```
https://www.docker.com/products/docker-desktop
```

### Lưu ý (Windows)

Bật **WSL 2 backend** trong Docker Desktop.

---

## Ubuntu

```bash
sudo apt update
sudo apt install -y docker.io docker-compose-plugin

sudo usermod -aG docker $USER
```

Sau đó **logout và login lại**.

---

### Kiểm tra Docker

```bash
docker --version
docker compose version
```

Chạy container test:

```bash
docker run --rm hello-world
```

---

## 3. Cài Python

Python được dùng cho nhiều project backend và data.

---

## Cách 1 — Anaconda (khuyến nghị)

Tải tại:

```
https://www.anaconda.com/download
```

Tạo môi trường:

```bash
conda create -n myproject python=3.11 -y
conda activate myproject
python --version
```

---

## Cách 2 — Python thuần

Tải Python:

```
https://www.python.org/downloads/
```

Tạo virtual environment:

```bash
python -m venv .venv
```

Kích hoạt môi trường:

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```bash
.\.venv\Scripts\Activate.ps1
```

Kiểm tra:

```bash
python --version
```

---

## 4. Cài Node.js (tuỳ chọn)

Nếu bạn làm **frontend hoặc fullstack**, cần Node.js.

Khuyên dùng **nvm** để quản lý phiên bản.

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

Cài **nvm-windows**:

```
https://github.com/coreybutler/nvm-windows
```

---

## 5. Clone repository

Clone repository của handbook để lấy toàn bộ docs và resources cho InternHub API:

```bash
git clone https://github.com/<github-org>/student-it-handbook.git

cd student-it-handbook
```

Thay `<github-org>` bằng organization hoặc username GitHub thực tế.

---

## 6. Chạy thử ứng dụng mẫu

Chạy PostgreSQL stack cho InternHub API:

```bash
cd resources/docker

docker compose -f postgres-compose.yml up -d
```

Kiểm tra container:

```bash
docker ps
```

Kiểm tra kết nối database:

```bash
docker exec -it postgres-dev psql -U dev -d internhub -c "SELECT 1;"
```

Nếu command này trả về `1`, môi trường database cho sample app đã sẵn sàng.

---

## Kiểm tra môi trường

Chạy các lệnh sau:

```bash
git --version
docker --version
python --version
node --version
```

Nếu tất cả đều chạy thành công, môi trường đã sẵn sàng.

---

## Lỗi thường gặp

| Lỗi                                 | Nguyên nhân                      | Cách khắc phục                  |
| ----------------------------------- | -------------------------------- | ------------------------------- |
| `git: command not found`            | Git chưa cài hoặc chưa thêm PATH | Cài lại Git                     |
| `docker: permission denied`         | User chưa thuộc group docker     | `sudo usermod -aG docker $USER` |
| `conda: command not found`          | Chưa init conda                  | `conda init`                    |
| Docker Desktop không chạy (Windows) | Chưa bật WSL2                    | Bật trong Windows Features      |

---

## Bước tiếp theo

Sau khi setup xong môi trường:

- Đọc **Sample Project: InternHub API**
- Đọc **Checklist sinh viên mới**
- Học **Terminal cơ bản**
- Làm quen với **Git workflow**
