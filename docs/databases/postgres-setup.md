# Cài Đặt Và Kết Nối PostgreSQL

Phần này hướng dẫn chạy PostgreSQL bằng Docker và kết nối bằng CLI hoặc GUI.

---

## Chạy PostgreSQL bằng Docker

Cách nhanh nhất để chạy PostgreSQL là dùng container.

```bash
docker run -d \
--name postgres-dev \
-e POSTGRES_USER=dev \
-e POSTGRES_PASSWORD=dev123 \
-e POSTGRES_DB=internhub \
-p 5432:5432 \
-v pgdata:/var/lib/postgresql/data \
postgres:16-alpine
```

---

### Kiểm tra container

```bash
docker ps
```

---

### Kết nối bằng psql

```bash
docker exec -it postgres-dev psql -U dev -d internhub
```

---

## Kết nối bằng GUI

Developer thường dùng GUI tool để quản lý database.

---

## DBeaver

Tải:

```
https://dbeaver.io/download/
```

---

### Tạo connection

Thông tin kết nối:

| Field    | Value     |
| -------- | --------- |
| Host     | localhost |
| Port     | 5432      |
| Database | internhub |
| User     | dev       |
| Password | dev123    |

---

