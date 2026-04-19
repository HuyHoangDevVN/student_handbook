# SQL Cheat Sheet

> Copy-paste nhanh các câu SQL thường dùng (PostgreSQL).

---

## Kiểu dữ liệu phổ biến

```
INT / INTEGER          Số nguyên
SERIAL                 Auto-increment integer
BIGSERIAL              Auto-increment big integer
VARCHAR(n)             Chuỗi giới hạn n ký tự
TEXT                   Chuỗi không giới hạn
BOOLEAN                true / false
TIMESTAMP              Ngày giờ
DATE                   Chỉ ngày
DECIMAL(10,2)          Số thập phân
JSON / JSONB           JSON data
UUID                   Unique identifier
```

## DDL – Tạo / Sửa bảng

```sql
-- Tạo bảng
CREATE TABLE users (
    id          SERIAL PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    email       VARCHAR(255) UNIQUE NOT NULL,
    role        VARCHAR(50) DEFAULT 'user',
    is_active   BOOLEAN DEFAULT true,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Thêm cột
ALTER TABLE users ADD COLUMN phone VARCHAR(20);

-- Đổi tên cột
ALTER TABLE users RENAME COLUMN phone TO phone_number;

-- Xoá cột
ALTER TABLE users DROP COLUMN phone_number;

-- Xoá bảng
DROP TABLE IF EXISTS users;

-- Tạo index
CREATE INDEX idx_users_email ON users(email);
```

## INSERT

```sql
-- Insert 1 row
INSERT INTO users (name, email) VALUES ('Văn A', 'a@test.com');

-- Insert nhiều rows
INSERT INTO users (name, email, role) VALUES
  ('Thị B', 'b@test.com', 'admin'),
  ('Văn C', 'c@test.com', 'user');

-- Insert nếu chưa tồn tại
INSERT INTO users (name, email)
VALUES ('Văn A', 'a@test.com')
ON CONFLICT (email) DO NOTHING;

-- Upsert
INSERT INTO users (name, email)
VALUES ('Văn A Updated', 'a@test.com')
ON CONFLICT (email) DO UPDATE SET name = EXCLUDED.name;
```

## SELECT

```sql
-- Cơ bản
SELECT * FROM users;
SELECT name, email FROM users;

-- Điều kiện
SELECT * FROM users WHERE role = 'admin';
SELECT * FROM users WHERE role IN ('admin', 'user');
SELECT * FROM users WHERE name LIKE '%nguyen%';     -- Case-sensitive
SELECT * FROM users WHERE name ILIKE '%nguyen%';    -- Case-insensitive (PG)
SELECT * FROM users WHERE created_at > '2025-01-01';
SELECT * FROM users WHERE is_active = true AND role = 'admin';

-- Sắp xếp
SELECT * FROM users ORDER BY created_at DESC;
SELECT * FROM users ORDER BY name ASC, id DESC;

-- Giới hạn & phân trang
SELECT * FROM users LIMIT 10;
SELECT * FROM users LIMIT 10 OFFSET 20;  -- Page 3

-- Đếm & Aggregate
SELECT COUNT(*) FROM users;
SELECT role, COUNT(*) FROM users GROUP BY role;
SELECT role, COUNT(*) FROM users GROUP BY role HAVING COUNT(*) > 5;
SELECT AVG(price), MIN(price), MAX(price), SUM(price) FROM products;

-- Distinct
SELECT DISTINCT role FROM users;
```

## UPDATE

```sql
UPDATE users SET role = 'admin' WHERE id = 1;
UPDATE users SET is_active = false WHERE created_at < '2024-01-01';

-- Update nhiều cột
UPDATE users SET name = 'New Name', role = 'senior' WHERE id = 1;
```

## DELETE

```sql
DELETE FROM users WHERE id = 1;
DELETE FROM users WHERE is_active = false;

-- â ï¸ Xoá tất cả (cẩn thận!)
DELETE FROM users;
TRUNCATE TABLE users;  -- Nhanh hơn DELETE, reset SERIAL
```

## JOIN

```sql
-- INNER JOIN
SELECT u.name, p.title
FROM users u
INNER JOIN posts p ON u.id = p.user_id;

-- LEFT JOIN (tất cả users, kể cả không có posts)
SELECT u.name, COUNT(p.id) as post_count
FROM users u
LEFT JOIN posts p ON u.id = p.user_id
GROUP BY u.name;

-- RIGHT JOIN
SELECT u.name, p.title
FROM users u
RIGHT JOIN posts p ON u.id = p.user_id;
```

## Subquery

```sql
-- Subquery trong WHERE
SELECT * FROM users
WHERE id IN (SELECT user_id FROM posts WHERE published = true);

-- Subquery trong FROM
SELECT avg_posts.name, avg_posts.cnt
FROM (
  SELECT u.name, COUNT(p.id) as cnt
  FROM users u
  LEFT JOIN posts p ON u.id = p.user_id
  GROUP BY u.name
) avg_posts
WHERE avg_posts.cnt > 3;
```

## Transaction

```sql
BEGIN;
  UPDATE accounts SET balance = balance - 100 WHERE id = 1;
  UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;

-- Nếu lỗi:
ROLLBACK;
```

## psql Commands

```bash
\l              # Liệt kê databases
\c dbname       # Kết nối database
\dt             # Liệt kê tables
\d tablename    # Cấu trúc bảng
\di             # Liệt kê indexes
\x              # Toggle expanded display
\q              # Thoát
\i file.sql     # Chạy file SQL
\timing         # Bật đo thời gian query
```

## Performance

```sql
-- Xem execution plan
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'a@test.com';

-- Tạo index
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_posts_user_published ON posts(user_id, published);
```
