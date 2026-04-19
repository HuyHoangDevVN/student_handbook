# Student IT Handbook

Handbook này được xây dựng để giúp sinh viên chuẩn bị thực tập, intern, fresher developer và người mới vào dự án hiểu được cách tiếp cận môi trường làm việc thật.

Nó không cố gắng dạy mọi thứ. Mục tiêu của handbook là:

- hệ thống hóa những gì sinh viên cần biết trước khi vào team
- giải thích workflow làm việc phổ biến trong dự án backend/fullstack
- cung cấp checklist, cheatsheet và runbook có thể dùng ngay
- giữ một case study xuyên suốt để việc học không bị rời rạc: **InternHub API**

## Handbook này dành cho ai

- Sinh viên sắp đi thực tập nhưng chưa từng làm việc trong repo thật.
- Người đã biết code nhưng chưa quen workflow Git, PR, review, Docker, CI/CD.
- Người muốn có một tài liệu tham khảo để tra cứu nhanh trong giai đoạn đầu vào dự án.

Handbook này **không** thay thế mentor, review thực tế hay tài liệu nội bộ của từng công ty. Nó đóng vai trò một tài liệu định hướng và hỗ trợ tiếp cận.

## Handbook giúp gì

Sau khi đi hết handbook, người học cần nắm được:

- cần chuẩn bị gì trước khi vào internship hoặc dự án mới
- cách setup môi trường local ở mức tối thiểu và tự xác minh
- cách đọc repo, tạo branch, mở Pull Request và phản hồi review
- cách làm việc với PostgreSQL, HTTP API, Docker và Docker Compose
- cách đọc log, xử lý lỗi cơ bản, và hiểu tư duy deploy, monitoring, security

## Bắt đầu từ đâu

Nếu bạn chưa biết đọc phần nào trước, đi theo thứ tự này:

1. [Start Here](docs/getting-started/start-here.md)
2. [Quickstart](docs/getting-started/quickstart.md)
3. [Checklist sinh viên mới](docs/getting-started/checklist.md)
4. [Sample Project: InternHub API](docs/getting-started/sample-project.md)
5. [Terminal & Shell](docs/environment/terminal.md)
6. [Git cơ bản](docs/vcs/git-basics.md)
7. [GitHub Workflow](docs/vcs/github-workflow.md)
8. [SQL & PostgreSQL](docs/databases/sql-postgres.md)
9. [HTTP & REST API](docs/backend/http-rest.md)
10. [API Testing](docs/backend/api-testing.md)
11. [Docker cơ bản](docs/containers/docker.md)
12. [Docker Compose](docs/containers/docker-compose.md)
13. [CI/CD - GitHub Actions](docs/devops/cicd-github-actions.md)
14. [Deployment cơ bản](docs/devops/deployment-basics.md)
15. [Logging & Monitoring](docs/devops/logging-monitoring.md)
16. [Bảo mật cơ bản](docs/devops/security-basics.md)
17. [Lỗi thường gặp](docs/troubleshooting/common-errors.md)

## Đọc handbook theo tình huống

### Trước khi đi thực tập

- [Start Here](docs/getting-started/start-here.md)
- [Checklist sinh viên mới](docs/getting-started/checklist.md)
- [Quickstart](docs/getting-started/quickstart.md)

### Khi vừa vào team hoặc repo mới

- [Sample Project: InternHub API](docs/getting-started/sample-project.md)
- [Terminal & Shell](docs/environment/terminal.md)
- [Git cơ bản](docs/vcs/git-basics.md)
- [GitHub Workflow](docs/vcs/github-workflow.md)

### Khi bắt đầu nhận task backend

- [SQL & PostgreSQL](docs/databases/sql-postgres.md)
- [HTTP & REST API](docs/backend/http-rest.md)
- [API Testing](docs/backend/api-testing.md)
- [Docker Compose](docs/containers/docker-compose.md)

### Khi cần làm việc hiệu quả hơn

- [Deployment cơ bản](docs/devops/deployment-basics.md)
- [Logging & Monitoring](docs/devops/logging-monitoring.md)
- [Bảo mật cơ bản](docs/devops/security-basics.md)
- [Lỗi thường gặp](docs/troubleshooting/common-errors.md)
- các mục trong `Cheat Sheets`

## InternHub API dùng để làm gì

Handbook này được xây quanh `InternHub API`, một case study mô phỏng cho một backend service quản lý user, post, comment và tag trong một team nội bộ. Case study này được dùng để:

- giữ cho ví dụ SQL, API, Docker, CI/CD và deploy nối tiếp với nhau
- giúp người học thấy một workflow liền mạch thay vì mỗi chương một ví dụ riêng
- tạo bối cảnh để hiểu tại sao cần logs, monitoring, rollback và review workflow

Tài liệu liên quan:

- [Sample Project: InternHub API](docs/getting-started/sample-project.md)
- `resources/database/sample-schema.sql`
- `resources/docker/postgres-compose.yml`
- `resources/docker/redis-compose.yml`
- `resources/api/postman-collection.json`

## Cấu trúc chính

```text
docs/           Nội dung handbook
resources/      Schema SQL, docker compose, Postman collection
mkdocs.yml      Cấu hình web docs
mkdocs-pdf.yml  Cấu hình xuất PDF
README.md       Entry point cho người học
CONTRIBUTING.md Hướng dẫn cho contributor/maintainer
```

## Chạy docs local

### 1. Clone repo

```bash
git clone https://github.com/<github-org>/student-it-handbook.git
cd student-it-handbook
```

### 2. Tạo virtual environment

```bash
python -m venv .venv

# Linux / macOS
source .venv/bin/activate

# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

### 3. Cài dependencies

```bash
pip install -r requirements.txt
```

### 4. Chạy local

```bash
mkdocs serve
```

Mở `http://127.0.0.1:8000`.

### 5. Build static site

```bash
mkdocs build --strict
```

## Xuất PDF

PDF dùng profile riêng là `mkdocs-pdf.yml`. Profile này không cố giữ toàn bộ giao diện web, mà ưu tiên build ổn định cho handbook in/export.

### Linux / macOS / Bash

```bash
ENABLE_PDF_EXPORT=1 mkdocs build --strict -f mkdocs-pdf.yml
```

### Windows PowerShell

```powershell
$env:ENABLE_PDF_EXPORT = "1"
mkdocs build --strict -f mkdocs-pdf.yml
```

Trên Windows, nếu thiếu GTK/Pango cho WeasyPrint, dùng:

- `./scripts/export-pdf.ps1`
- hoặc workflow `.github/workflows/pdf-handbook.yml`

### GitHub Actions

Day la duong on dinh nhat cho PDF:

1. push code len GitHub
2. vao tab `Actions`
3. chon workflow `Build PDF Handbook`
4. chay `Run workflow`
5. tai artifact `student-it-handbook-pdf`

## Đóng góp

Contributor và maintainer nên đọc:

- [CONTRIBUTING.md](CONTRIBUTING.md)

## License

MIT License. Xem [LICENSE](LICENSE).
