# Sample Project: InternHub API

InternHub API la sample app xuyen suot cua handbook nay. Muc tieu cua no la giup ban hoc mot case
study duy nhat, thay vi moi chuong lai dung mot vi du roi rac.

---

## Muc tieu

Sau khi di het handbook voi sample app nay, ban se thay duoc mot quy trinh trien khai thuc te:

- local setup
- terminal va Linux workflow
- Git va pull request
- PostgreSQL schema va truy van SQL
- Docker va Docker Compose
- API testing voi Postman va HTTP client
- CI/CD, release, monitoring va deployment

---

## InternHub API la gi

InternHub API la mot REST API don gian de quan ly user noi bo trong mot team:

- `users`: danh sach intern, developer, lead
- `posts`: bai viet va ghi chu noi bo
- `comments`: binh luan
- `tags`: gan nhan cho bai viet

Database mau, Postman collection va stack Docker deu da co san trong repo.

---

## Kien truc mau

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

## Tai nguyen trong repo

- Database schema: `resources/database/sample-schema.sql`
- PostgreSQL stack: `resources/docker/postgres-compose.yml`
- Redis stack: `resources/docker/redis-compose.yml`
- Postman collection: `resources/api/postman-collection.json`

---

## Ban se gap InternHub API o dau

- Quickstart: dung PostgreSQL stack de khoi dong moi truong hoc
- SQL/PostgreSQL: dung schema va seed data cua InternHub
- Docker Compose: dong goi web + db + redis cho InternHub API
- API Testing: import collection va test endpoint `/api/users`
- CI/CD: build image `internhub-api`
- Deployment: deploy InternHub API len VPS/PaaS
- Logging/Monitoring: theo doi logs va metrics cua `internhub-api`

---

## Goi y cach hoc

1. Khoi dong database mau truoc
2. Doc SQL va API testing de hieu data model
3. Chuyen sang Docker/Docker Compose de dong goi app
4. Cuoi cung moi hoc CI/CD, monitoring va deployment

---

## Tai lieu lien quan

- [Quickstart](quickstart.md)
- [SQL & PostgreSQL](../databases/sql-postgres.md)
- [Docker Compose](../containers/docker-compose.md)
- [API Testing](../backend/api-testing.md)
