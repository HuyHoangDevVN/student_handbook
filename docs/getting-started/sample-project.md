# Sample Project: InternHub API

`InternHub API` là case study xuyên suốt của handbook này. Nó không nhằm thay thế một repo production thật. Vai trò của nó là giúp các chương trong handbook nối với nhau bằng một bối cảnh kỹ thuật chung.

---

## Mục tiêu

Sau khi đọc trang này, bạn cần hiểu:

- InternHub API đang mô tả hệ thống nào
- chapter nào trong handbook đụng vào phần nào của case study
- tại sao case study này được dùng để học workflow thực tập

---

## Bối cảnh nghiệp vụ

InternHub API là một backend service mô phỏng cho một team nội bộ:

- quản lý danh sách intern, developer, lead
- lưu bài viết nội bộ và ghi chú trong team
- gắn tag cho bài viết để phân loại
- cho phép tìm kiếm, xem danh sách, tạo mới và cập nhật dữ liệu

Case study này đủ đơn giản để người mới theo kịp, nhưng vẫn đủ cho SQL, API, Docker, CI/CD và vận hành.

---

## Thành phần chính

### Entities

- `users`
- `posts`
- `comments`
- `tags`

### Infrastructure mô phỏng

- PostgreSQL
- Redis
- Docker Compose
- CI pipeline
- Deployment flow
- Logs và metrics

---

## Contract mô phỏng mà handbook sẽ bám vào

Handbook giả định InternHub API có ít nhất:

- endpoint `GET /api/users`
- endpoint `POST /api/users`
- endpoint `GET /api/posts`
- health endpoint để smoke test sau deploy
- metrics endpoint để monitoring scrape
- log output có request, error và context tối thiểu

Điều quan trọng ở đây là **tính nhất quán** của ví dụ, không phải đầy đủ tất cả tính năng.

---

## User stories dùng để hiểu handbook

### User story 1

Một intern mới vào team cần xem danh sách user để biết ai đang thuộc team nào.

Tài liệu liên quan:

- [HTTP & REST API](../backend/http-rest.md)
- [API Testing](../backend/api-testing.md)

### User story 2

Một developer cần thêm bài viết nội bộ và gắn tag để chia sẻ tài liệu hướng dẫn.

Tài liệu liên quan:

- [SQL CRUD](../databases/sql-crud.md)
- [Docker Compose](../containers/docker-compose.md)

### User story 3

Một lead cần xác minh bản deploy mới không làm hỏng endpoint chính và có thể rollback nếu cần.

Tài liệu liên quan:

- [CI/CD - GitHub Actions](../devops/cicd-github-actions.md)
- [Deployment cơ bản](../devops/deployment-basics.md)
- [Logging & Monitoring](../devops/logging-monitoring.md)

---

## Bug scenarios mô phỏng

### Bug scenario 1

`GET /api/users` trả `500` sau khi sửa query.

Dùng để học:

- đọc log
- kiểm tra query
- reproduce request

### Bug scenario 2

Container `web` restart liên tục vì env sai.

Dùng để học:

- `docker compose logs`
- verify env
- healthcheck

### Bug scenario 3

Pull Request pass local nhưng fail CI.

Dùng để học:

- đọc workflow
- phân biệt local vs CI env
- cách sửa và push lại

---

## Incident scenarios mô phỏng

### Incident 1

Deploy xong thì endpoint chính trả timeout.

Cần nghĩ đến:

- rollback
- smoke test
- logs
- metrics

### Incident 2

Disk đầy vì log quá nhiều hoặc Docker không được dọn dẹp.

Cần nghĩ đến:

- log level
- docker disk usage
- thao tác dọn dẹp an toàn

---

## Tài nguyên trong repo

- Database schema: `resources/database/sample-schema.sql`
- PostgreSQL stack: `resources/docker/postgres-compose.yml`
- Redis stack: `resources/docker/redis-compose.yml`
- Postman collection: `resources/api/postman-collection.json`

---

## Mỗi chương sẽ chạm vào phần nào của InternHub

| Chương | Vai trò với case study |
| --- | --- |
| Quickstart | Chạy stack PostgreSQL mẫu |
| SQL & PostgreSQL | Đọc schema, viết query trên `users`, `posts`, `comments`, `tags` |
| HTTP & REST API | Hiểu request/response cho endpoint của InternHub |
| API Testing | Gọi và verify `/api/users`, `/api/posts` |
| Docker Compose | Đóng gói `web + db + redis` |
| CI/CD | Build/release `internhub-api` |
| Deployment | Hiểu staging, prod, smoke test, rollback |
| Logging & Monitoring | Đọc log và metrics của `internhub-api` |

---

## Cách dùng trang này

- Đọc trang này trước khi đi vào chương kỹ thuật để không mất bối cảnh.
- Khi thấy ví dụ `users`, `posts`, `internhub-api`, hãy map nó lại với case study này.
- Nếu một chương đang nói quá chung chung, quay lại đây để nhắc bạn chapter đó đang phục vụ tình huống nào.

---

## Bước tiếp theo

- Nếu bạn chưa chạy môi trường tối thiểu: đọc [Quickstart](quickstart.md)
- Nếu bạn chuẩn bị vào team: đọc [Checklist sinh viên mới](checklist.md)
- Nếu bạn muốn học theo phần cần dùng ngay: đọc [Start Here](start-here.md)
