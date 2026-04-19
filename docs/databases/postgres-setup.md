# Cài Đặt Và Kết Nối PostgreSQL

Phần này hướng dẫn chạy PostgreSQL bằng Docker và kết nối bằng CLI hoặc GUI.

---

## Cháº¡y PostgreSQL báº±ng Docker

CĂ¡ch nhanh nháº¥t Ä‘á»ƒ cháº¡y PostgreSQL lĂ  dĂ¹ng container.

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

### Kiá»ƒm tra container

```bash
docker ps
```

---

### Káº¿t ná»‘i báº±ng psql

```bash
docker exec -it postgres-dev psql -U dev -d internhub
```

---

## Káº¿t ná»‘i báº±ng GUI

Developer thÆ°á»ng dĂ¹ng GUI tool Ä‘á»ƒ quáº£n lĂ½ database.

---

## DBeaver

Táº£i:

```
https://dbeaver.io/download/
```

---

### Táº¡o connection

ThĂ´ng tin káº¿t ná»‘i:

| Field    | Value     |
| -------- | --------- |
| Host     | localhost |
| Port     | 5432      |
| Database | internhub |
| User     | dev       |
| Password | dev123    |

---

