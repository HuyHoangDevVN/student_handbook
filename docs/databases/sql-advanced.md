# Index, Transaction Và Tối Ưu SQL

Phần này đi qua index, transaction, psql cheat sheet và phần tự luyện cuối chương.

---

## Index

Index giúp **tăng tốc truy vấn**.

---

### Tạo index

```sql
CREATE INDEX idx_users_email
ON users(email);
```

---

```sql
CREATE INDEX idx_posts_user_id
ON posts(user_id);
```

---

### Phân tích query

```sql
EXPLAIN ANALYZE
SELECT * FROM users
WHERE email = 'a.nguyen@example.com';
```

---

## Transaction

Transaction đảm bảo **atomic operations**.

---

```sql
BEGIN;

UPDATE users
SET role = 'senior'
WHERE id = 1;

INSERT INTO posts (user_id,title)
VALUES (1,'Promoted!');

COMMIT;
```

---

Nếu có lỗi:

```sql
ROLLBACK;
```

---

## psql Cheat Sheet

| Command       | Mô tả                |
| ------------- | -------------------- |
| `\l`          | danh sách database   |
| `\dt`         | danh sách table      |
| `\d users`    | schema table         |
| `\x`          | toggle expanded view |
| `\q`          | exit                 |
| `\i file.sql` | chạy file SQL        |

---

## Lỗi thường gặp

| Lỗi                     | Nguyên nhân          | Cách sửa          |
| ----------------------- | -------------------- | ----------------- |
| connection refused      | PostgreSQL chưa chạy | start container   |
| relation does not exist | chưa tạo table       | chạy CREATE TABLE |
| duplicate key           | dữ liệu trùng        | dùng unique check |
| permission denied       | user thiếu quyền     | GRANT permissions |

---

## Bài tập

### Bài 1

Tạo bảng:

```
products
```

Columns:

```
id
name
price
stock
category
```

---

### Bài 2

Insert 5 sản phẩm và query:

```
price > 100000
stock > 0
```

---

### Bài 3

JOIN:

```
users + posts
```

đếm số bài viết mỗi user.

---

## Tài liệu tham khảo

```
https://www.postgresqltutorial.com/
```

```
https://sqlbolt.com/
```
