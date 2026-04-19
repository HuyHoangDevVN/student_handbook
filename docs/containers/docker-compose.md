# Docker Compose

## Mục tiêu

Sau bài này, bạn sẽ:

- Viết file `docker-compose.yml` cho multi-container app.
- Quản lý stack: web + database + cache.
- Sử dụng networks, volumes, environment variables.
- Áp dụng cho môi trường development.

## Prerequisites

- [Docker cơ bản](docker.md).

---

## Tại sao cần Docker Compose?

Thay vì chạy nhiều lệnh `docker run`:

```bash
# Không dùng Compose – phải chạy từng container
docker run -d --name db -e POSTGRES_PASSWORD=secret postgres:16
docker run -d --name redis redis:7
docker run -d --name internhub-api -p 3000:3000 --link db --link redis internhub-api
```

Dùng Compose – **1 file, 1 lệnh**:

```bash
docker compose up -d
```

---

## Cấu trúc docker-compose.yml

```yaml
# docker-compose.yml
services:
  # === Web Application ===
  web:
    build: . # Build từ Dockerfile ở thư mục hiện tại
    ports:
      - "3000:3000" # Map port
    environment:
      - DATABASE_URL=postgres://dev:dev123@db:5432/internhub
      - REDIS_URL=redis://redis:6379
      - NODE_ENV=development
    volumes:
      - ./src:/app/src # Bind mount cho live reload
    depends_on:
      - db
      - redis
    restart: unless-stopped

  # === Database ===
  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: dev
      POSTGRES_PASSWORD: dev123
      POSTGRES_DB: internhub
    ports:
      - "5432:5432" # Expose để connect bằng DBeaver
    volumes:
      - pgdata:/var/lib/postgresql/data
      - ./resources/database/sample-schema.sql:/docker-entrypoint-initdb.d/init.sql

  # === Cache ===
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redisdata:/data

# Named volumes
volumes:
  pgdata:
  redisdata:
```

---

## Lệnh Docker Compose

```bash
# Khởi động tất cả services (foreground)
docker compose up

# Khởi động ở background
docker compose up -d

# Xem trạng thái
docker compose ps

# Xem logs
docker compose logs
docker compose logs -f web         # Follow logs của service "web"

# Dừng tất cả
docker compose stop

# Dừng + xoá containers
docker compose down

# Dừng + xoá containers + volumes (MẤT DATA!)
docker compose down -v

# Rebuild images
docker compose build
docker compose up -d --build       # Build lại rồi start

# Chạy lệnh trong service
docker compose exec web bash
docker compose exec db psql -U dev -d internhub

# Scale service (chạy nhiều instance)
docker compose up -d --scale web=3
```

---

## Ví dụ: Full Stack App

```yaml
# docker-compose.yml cho project thực tế
services:
  # Frontend (React)
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile.dev
    ports:
      - "5173:5173"
    volumes:
      - ./frontend/src:/app/src
    environment:
      - VITE_API_URL=http://localhost:3000

  # Backend (Node.js)
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile.dev
    ports:
      - "3000:3000"
    volumes:
      - ./backend/src:/app/src
    environment:
      - DATABASE_URL=postgres://dev:dev123@db:5432/internhub
      - REDIS_URL=redis://redis:6379
      - JWT_SECRET=dev-secret-key
    depends_on:
      db:
        condition: service_healthy

  # Database
  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: dev
      POSTGRES_PASSWORD: dev123
      POSTGRES_DB: internhub
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U dev -d internhub"]
      interval: 5s
      timeout: 5s
      retries: 5

  # Cache
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

  # Admin tool (pgAdmin)
  pgadmin:
    image: dpage/pgadmin4
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@admin.com
      PGADMIN_DEFAULT_PASSWORD: admin
    ports:
      - "5050:80"
    depends_on:
      - db

volumes:
  pgdata:
```

---

## Network trong Compose

- Compose tự tạo **default network** cho stack.
- Các service giao tiếp qua **tên service**: `db`, `redis`, `web`.
- Không cần IP, Docker DNS tự resolve.

```yaml
# web kết nối db bằng hostname "db"
DATABASE_URL=postgres://dev:dev123@db:5432/internhub
#                                   ^^
#                              Tên service = hostname
```

---

## Environment Variables

### Cách 1 – Inline trong compose

```yaml
environment:
  - NODE_ENV=development
  - PORT=3000
```

### Cách 2 – Dùng file .env

```yaml
# docker-compose.yml
services:
  web:
    env_file:
      - .env
```

```env
# .env
NODE_ENV=development
PORT=3000
DATABASE_URL=postgres://dev:dev123@db:5432/internhub
```

### Cách 3 – Biến thay thế trong compose

```yaml
# docker-compose.yml
services:
  db:
    image: postgres:${POSTGRES_VERSION:-16}-alpine
```

```bash
# Chạy với biến
POSTGRES_VERSION=15 docker compose up -d
```

---

## Lỗi thường gặp

| Lỗi                                                  | Nguyên nhân      | Cách sửa                                                 |
| ---------------------------------------------------- | ---------------- | -------------------------------------------------------- |
| `service "web" depends on "db" which is not healthy` | DB chưa sẵn sàng | Thêm healthcheck cho db                                  |
| `address already in use`                             | Port bị chiếm    | Stop container/process cũ, đổi port                      |
| Volume data bị cũ                                    | Cache image cũ   | `docker compose down -v && docker compose up -d --build` |
| Container restart liên tục                           | App crash loop   | Xem logs: `docker compose logs web`                      |

---

## Bài tập

1. Viết `docker-compose.yml` cho: Express API + PostgreSQL + Redis.
2. Thêm healthcheck cho PostgreSQL.
3. Dùng `docker compose exec` để chạy `psql` và tạo bảng.

---

## Tài liệu tham khảo

- [Docker Compose Overview](https://docs.docker.com/compose/)
- [Compose File Reference](https://docs.docker.com/compose/compose-file/)
