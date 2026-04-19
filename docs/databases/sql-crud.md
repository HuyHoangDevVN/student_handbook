# SQL CRUD Cơ Bản

Phần này gom các thao tác tạo bảng, thêm dữ liệu, truy vấn, cập nhật và xoá.

---

## SQL cơ bản

---

## Tạo bảng

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    role VARCHAR(50) DEFAULT 'intern',
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

```sql
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    content TEXT,
    published BOOLEAN DEFAULT false,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## INSERT

```sql
INSERT INTO users (name, email, role)
VALUES
('Nguyễn Văn A','a.nguyen@example.com','intern'),
('Trần Thị B','b.tran@example.com','developer'),
('Lê Văn C','c.le@example.com','lead');
```

---

```sql
INSERT INTO posts (user_id, title, content, published)
VALUES
(1,'First Post','Hello World!',true),
(2,'Docker Guide','Docker is awesome...',true),
(1,'Draft Post','Work in progress...',false);
```

---

## SELECT

---

### Lấy tất cả dữ liệu

```sql
SELECT * FROM users;
```

---

### Lấy cột cụ thể

```sql
SELECT name, email
FROM users
WHERE role = 'intern';
```

---

### Sắp xếp

```sql
SELECT *
FROM users
ORDER BY created_at DESC;
```

---

### Giới hạn kết quả

```sql
SELECT *
FROM users
LIMIT 10 OFFSET 0;
```

---

### GROUP BY

```sql
SELECT role, COUNT(*)
FROM users
GROUP BY role;
```

---

### Tìm kiếm text

```sql
SELECT *
FROM users
WHERE name ILIKE '%nguyen%';
```

---

## JOIN

JOIN giúp kết hợp dữ liệu từ nhiều bảng.

---

## INNER JOIN

```sql
SELECT u.name, p.title
FROM users u
INNER JOIN posts p
ON u.id = p.user_id;
```

---

## LEFT JOIN

```sql
SELECT u.name, COUNT(p.id) AS post_count
FROM users u
LEFT JOIN posts p
ON u.id = p.user_id
GROUP BY u.name;
```

---

## UPDATE

```sql
UPDATE users
SET role = 'developer'
WHERE id = 1;
```

---

## DELETE

```sql
DELETE FROM posts
WHERE id = 3;
```

---

!!! danger "Cảnh báo"
Luôn kiểm tra điều kiện trước khi chạy:

```sql
UPDATE
DELETE
```

Nên chạy:

```sql
SELECT
```

trước để đảm bảo query đúng.

---

