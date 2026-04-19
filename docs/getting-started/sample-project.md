# Sample Project: InternHub API

InternHub API là sample app xuyên suốt của handbook này. Mục tiêu của nó là giúp bạn học một case
study duy nhất, thay vì mỗi chương lại dùng một ví dụ rời rạc.

---

## Mục tiêu

Sau khi đi hết handbook với sample app này, bạn sẽ thấy được một quy trình triển khai thực tế:

- local setup
- terminal và Linux workflow
- Git và pull request
- PostgreSQL schema và truy vấn SQL
- Docker và Docker Compose
- API testing với Postman và HTTP client
- CI/CD, release, monitoring và deployment

---

## InternHub API là gì

InternHub API là một REST API đơn giản để quản lý user nội bộ trong một team:

- `users`: danh sách intern, developer, lead
- `posts`: bài viết và ghi chú nội bộ
- `comments`: bình luận
- `tags`: gắn nhãn cho bài viết

Database mẫu, Postman collection và stack Docker đều đã có sẵn trong repo.

---

## Kiến trúc mẫu

```text
InternHub API
|-- REST API service
|-- PostgreSQL
|-- Redis
|-- Docker Compose
|-- CI pipeline
`-- Monitoring stack
```

---

## Tài nguyên trong repo

- Database schema: `resources/database/sample-schema.sql`
- PostgreSQL stack: `resources/docker/postgres-compose.yml`
- Redis stack: `resources/docker/redis-compose.yml`
- Postman collection: `resources/api/postman-collection.json`

---

## Bạn sẽ gặp InternHub API ở đâu

- Quickstart: dùng PostgreSQL stack để khởi động môi trường học
- SQL/PostgreSQL: dùng schema và seed data của InternHub
- Docker Compose: đóng gói web + db + redis cho InternHub API
- API Testing: import collection và test endpoint `/api/users`
- CI/CD: build image `internhub-api`
- Deployment: deploy InternHub API lên VPS/PaaS
- Logging/Monitoring: theo dõi logs và metrics của `internhub-api`

---

## Gợi ý cách học

1. Khởi động database mẫu trước
2. Đọc SQL và API testing để hiểu data model
3. Chuyển sang Docker/Docker Compose để đóng gói app
4. Cuối cùng mới học CI/CD, monitoring và deployment

---

## Tài liệu liên quan

- [Quickstart](quickstart.md)
- [SQL & PostgreSQL](../databases/sql-postgres.md)
- [Docker Compose](../containers/docker-compose.md)
- [API Testing](../backend/api-testing.md)
