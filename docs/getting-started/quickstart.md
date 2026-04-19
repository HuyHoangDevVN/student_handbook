# Quickstart

Quickstart này chỉ giải quyết một việc: giúp bạn có **môi trường tối thiểu** để đọc handbook và thực hành với case study `InternHub API`.

Nó không cố gắng dạy đầy đủ Git, Python, Node.js hay Docker. Các chương chi tiết nằm ở những phần sau.

---

## Mục tiêu

Sau bài này, bạn cần làm được 4 việc:

- kiểm tra máy đã có Git và Docker
- clone repo handbook
- chạy PostgreSQL stack mẫu cho InternHub API
- tự xác minh kết nối database thành công

---

## Khi nào bạn cần bài này

- Bạn sắp đi thực tập và muốn kiểm tra lại môi trường.
- Bạn mới vào repo và chưa chắc máy mình đã sẵn sàng.
- Bạn muốn chạy được resource mẫu trước khi học SQL, API hoặc Docker Compose.

---

## Prerequisites

Bạn cần:

- máy Windows 10/11, macOS 12+, hoặc Ubuntu 22.04+
- kết nối Internet
- quyền cài tool trên máy của mình

---

## 1. Kiểm tra Git

```bash
git --version
```

Nếu lệnh chạy thành công, Git đã sẵn sàng.

Nếu máy chưa có Git:

- Windows: `winget install Git.Git`
- macOS: `xcode-select --install` hoặc `brew install git`
- Ubuntu: `sudo apt update && sudo apt install -y git`

### Cấu hình Git tối thiểu

```bash
git config --global user.name "Tên của bạn"
git config --global user.email "email@example.com"
git config --global init.defaultBranch main
```

---

## 2. Kiểm tra Docker

```bash
docker --version
docker compose version
```

Nếu máy chưa có Docker:

- Windows/macOS: cài Docker Desktop
- Ubuntu: `sudo apt update && sudo apt install -y docker.io docker-compose-plugin`

### Tự xác minh Docker

```bash
docker run --rm hello-world
```

Nếu container chạy xong và in thông báo thành công, Docker đã sẵn sàng.

---

## 3. Clone repository handbook

```bash
git clone https://github.com/<github-org>/student-it-handbook.git
cd student-it-handbook
```

Thay `<github-org>` bằng organization hoặc username GitHub thực tế.

---

## 4. Chạy PostgreSQL stack mẫu

Case study `InternHub API` dùng PostgreSQL làm datastore chính. Trong repo đã có stack mẫu để bạn thực hành.

```bash
cd resources/docker
docker compose -f postgres-compose.yml up -d
```

### Kiểm tra container đã lên chưa

```bash
docker ps
```

Bạn cần thấy container `postgres-dev` đang chạy.

---

## 5. Kiểm tra kết nối database

```bash
docker exec -it postgres-dev psql -U dev -d internhub -c "SELECT 1;"
```

### Expected result

Bạn sẽ thấy output có giá trị `1`, ví dụ:

```text
 ?column?
----------
        1
```

Nếu bạn thấy kết quả này, môi trường tối thiểu cho handbook đã sẵn sàng.

---

## 6. Bạn vừa setup xong gì

Sau quickstart, bạn **chưa** học xong Git, Docker hay SQL. Bạn mới chỉ:

- có repo handbook trên máy
- có Docker chạy được
- có PostgreSQL stack mẫu cho InternHub
- có điểm bắt đầu để học những chương sau

---

## Lỗi thường gặp

| Lỗi | Nguyên nhân thường gặp | Cách xử lý |
| --- | --- | --- |
| `git: command not found` | Git chưa cài hoặc chưa có trong PATH | Cài lại Git, mở terminal mới |
| `docker: permission denied` | User chưa thuộc docker group trên Linux | `sudo usermod -aG docker $USER`, đăng nhập lại |
| Docker Desktop không lên | WSL2/backend chưa bật | Kiểm tra lại Docker Desktop settings |
| `psql: could not connect` | Container chưa ready | `docker ps`, `docker logs postgres-dev` |

---

## Cách tự kiểm tra đã hoàn thành

- [ ] `git --version` chạy được
- [ ] `docker --version` và `docker compose version` chạy được
- [ ] clone được repo handbook
- [ ] `docker compose -f postgres-compose.yml up -d` chạy thành công
- [ ] `SELECT 1;` trong `psql` trả về giá trị `1`

---

## Bước tiếp theo

- Đọc [Start Here](start-here.md) nếu bạn muốn chọn đúng luồng đọc
- Đọc [Checklist sinh viên mới](checklist.md) nếu bạn đang chuẩn bị đi thực tập
- Đọc [Sample Project: InternHub API](sample-project.md) để hiểu case study xuyên suốt
