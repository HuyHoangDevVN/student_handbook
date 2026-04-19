# Docker Compose

## Má»¥c tiĂªu

Sau bĂ i nĂ y, báº¡n sáº½:

- Viáº¿t file `docker-compose.yml` cho multi-container app.
- Quáº£n lĂ½ stack: web + database + cache.
- Sá»­ dá»¥ng networks, volumes, environment variables.
- Ăp dá»¥ng cho mĂ´i trÆ°á»ng development.

## Prerequisites

- [Docker cÆ¡ báº£n](docker.md).

---

## Táº¡i sao cáº§n Docker Compose?

Thay vĂ¬ cháº¡y nhiá»u lá»‡nh `docker run`:

```bash
# KhĂ´ng dĂ¹ng Compose â€“ pháº£i cháº¡y tá»«ng container
docker run -d --name db -e POSTGRES_PASSWORD=secret postgres:16
docker run -d --name redis redis:7
docker run -d --name internhub-api -p 3000:3000 --link db --link redis internhub-api
```

DĂ¹ng Compose â€“ **1 file, 1 lá»‡nh**:

```bash
docker compose up -d
```

---

## Cáº¥u trĂºc docker-compose.yml

```yaml
# docker-compose.yml
services:
  # === Web Application ===
  web:
    build: . # Build tá»« Dockerfile á»Ÿ thÆ° má»¥c hiá»‡n táº¡i
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
      - "5432:5432" # Expose Ä‘á»ƒ connect báº±ng DBeaver
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

## Lá»‡nh Docker Compose

```bash
# Khá»Ÿi Ä‘á»™ng táº¥t cáº£ services (foreground)
docker compose up

# Khá»Ÿi Ä‘á»™ng á»Ÿ background
docker compose up -d

# Xem tráº¡ng thĂ¡i
docker compose ps

# Xem logs
docker compose logs
docker compose logs -f web         # Follow logs cá»§a service "web"

# Dá»«ng táº¥t cáº£
docker compose stop

# Dá»«ng + xoĂ¡ containers
docker compose down

# Dá»«ng + xoĂ¡ containers + volumes (Máº¤T DATA!)
docker compose down -v

# Rebuild images
docker compose build
docker compose up -d --build       # Build láº¡i rá»“i start

# Cháº¡y lá»‡nh trong service
docker compose exec web bash
docker compose exec db psql -U dev -d internhub

# Scale service (cháº¡y nhiá»u instance)
docker compose up -d --scale web=3
```

---

## VĂ­ dá»¥: Full Stack App

```yaml
# docker-compose.yml cho project thá»±c táº¿
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

- Compose tá»± táº¡o **default network** cho stack.
- CĂ¡c service giao tiáº¿p qua **tĂªn service**: `db`, `redis`, `web`.
- KhĂ´ng cáº§n IP, Docker DNS tá»± resolve.

```yaml
# web káº¿t ná»‘i db báº±ng hostname "db"
DATABASE_URL=postgres://dev:dev123@db:5432/internhub
#                                   ^^
#                              TĂªn service = hostname
```

---

## Environment Variables

### CĂ¡ch 1 â€“ Inline trong compose

```yaml
environment:
  - NODE_ENV=development
  - PORT=3000
```

### CĂ¡ch 2 â€“ DĂ¹ng file .env

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

### CĂ¡ch 3 â€“ Biáº¿n thay tháº¿ trong compose

```yaml
# docker-compose.yml
services:
  db:
    image: postgres:${POSTGRES_VERSION:-16}-alpine
```

```bash
# Cháº¡y vá»›i biáº¿n
POSTGRES_VERSION=15 docker compose up -d
```

---

## Lá»—i thÆ°á»ng gáº·p

| Lá»—i                                                  | NguyĂªn nhĂ¢n      | CĂ¡ch sá»­a                                                 |
| ---------------------------------------------------- | ---------------- | -------------------------------------------------------- |
| `service "web" depends on "db" which is not healthy` | DB chÆ°a sáºµn sĂ ng | ThĂªm healthcheck cho db                                  |
| `address already in use`                             | Port bá»‹ chiáº¿m    | Stop container/process cÅ©, Ä‘á»•i port                      |
| Volume data bá»‹ cÅ©                                    | Cache image cÅ©   | `docker compose down -v && docker compose up -d --build` |
| Container restart liĂªn tá»¥c                           | App crash loop   | Xem logs: `docker compose logs web`                      |

---

## BĂ i táº­p

1. Viáº¿t `docker-compose.yml` cho: Express API + PostgreSQL + Redis.
2. ThĂªm healthcheck cho PostgreSQL.
3. DĂ¹ng `docker compose exec` Ä‘á»ƒ cháº¡y `psql` vĂ  táº¡o báº£ng.

---

## TĂ i liá»‡u tham kháº£o

- [Docker Compose Overview](https://docs.docker.com/compose/)
- [Compose File Reference](https://docs.docker.com/compose/compose-file/)
