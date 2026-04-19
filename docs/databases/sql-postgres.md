# SQL & PostgreSQL

Trang này là mục lục cho cụm bài SQL/PostgreSQL. Nội dung đã được tách thành 3 bài để phân biệt
rõ setup, CRUD và tối ưu/cơ chế giao dịch.

---

## Mục tiêu

Sau cụm bài này, bạn có thể:

- chạy PostgreSQL bằng Docker và kết nối bằng CLI/GUI
- viết truy vấn CRUD cơ bản
- hiểu index, transaction và một số công cụ `psql`

---

## Prerequisites

- Đã hoàn thành: [Quickstart](../getting-started/quickstart.md)
- Đã biết Docker cơ bản: [Docker cơ bản](../containers/docker.md)

---

## Lộ trình học

1. [Cài Đặt Và Kết Nối PostgreSQL](postgres-setup.md)
2. [SQL CRUD Cơ Bản](sql-crud.md)
3. [Index, Transaction Và Tối Ưu SQL](sql-advanced.md)

---

## Gợi ý học

- Chạy database mẫu trước khi học CRUD
- Tự gõ lại truy vấn thay vì chỉ copy/paste
- Dùng `EXPLAIN ANALYZE` ở phần nâng cao để tập đọc execution plan

---

## Tài liệu liên quan

- [MongoDB & Redis](mongodb-redis.md)
- [SQL Cheat Sheet](../cheatsheets/sql.md)
- File mẫu trong repo: `resources/database/sample-schema.sql`
