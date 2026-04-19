# SQL Cheat Sheet

> Copy-paste nhanh cĂ¡c cĂ¢u SQL thÆ°á»ng dĂ¹ng (PostgreSQL).

---

## Kiá»ƒu dá»¯ liá»‡u phá»• biáº¿n

```
INT / INTEGER          Sá»‘ nguyĂªn
SERIAL                 Auto-increment integer
BIGSERIAL              Auto-increment big integer
VARCHAR(n)             Chuá»—i giá»›i háº¡n n kĂ½ tá»±
TEXT                   Chuá»—i khĂ´ng giá»›i háº¡n
BOOLEAN                true / false
TIMESTAMP              NgĂ y giá»
DATE                   Chá»‰ ngĂ y
DECIMAL(10,2)          Sá»‘ tháº­p phĂ¢n
JSON / JSONB           JSON data
UUID                   Unique identifier
```

## DDL â€“ Táº¡o / Sá»­a báº£ng

```sql
-- Táº¡o báº£ng
CREATE TABLE users (
    id          SERIAL PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    email       VARCHAR(255) UNIQUE NOT NULL,
    role        VARCHAR(50) DEFAULT 'user',
    is_active   BOOLEAN DEFAULT true,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ThĂªm cá»™t
ALTER TABLE users ADD COLUMN phone VARCHAR(20);

-- Äá»•i tĂªn cá»™t
ALTER TABLE users RENAME COLUMN phone TO phone_number;

-- XoĂ¡ cá»™t
ALTER TABLE users DROP COLUMN phone_number;

-- XoĂ¡ báº£ng
DROP TABLE IF EXISTS users;

-- Táº¡o index
CREATE INDEX idx_users_email ON users(email);
```

## INSERT

```sql
-- Insert 1 row
INSERT INTO users (name, email) VALUES ('VÄƒn A', 'a@test.com');

-- Insert nhiá»u rows
INSERT INTO users (name, email, role) VALUES
  ('Thá»‹ B', 'b@test.com', 'admin'),
  ('VÄƒn C', 'c@test.com', 'user');

-- Insert náº¿u chÆ°a tá»“n táº¡i
INSERT INTO users (name, email)
VALUES ('VÄƒn A', 'a@test.com')
ON CONFLICT (email) DO NOTHING;

-- Upsert
INSERT INTO users (name, email)
VALUES ('VÄƒn A Updated', 'a@test.com')
ON CONFLICT (email) DO UPDATE SET name = EXCLUDED.name;
```

## SELECT

```sql
-- CÆ¡ báº£n
SELECT * FROM users;
SELECT name, email FROM users;

-- Äiá»u kiá»‡n
SELECT * FROM users WHERE role = 'admin';
SELECT * FROM users WHERE role IN ('admin', 'user');
SELECT * FROM users WHERE name LIKE '%nguyen%';     -- Case-sensitive
SELECT * FROM users WHERE name ILIKE '%nguyen%';    -- Case-insensitive (PG)
SELECT * FROM users WHERE created_at > '2025-01-01';
SELECT * FROM users WHERE is_active = true AND role = 'admin';

-- Sáº¯p xáº¿p
SELECT * FROM users ORDER BY created_at DESC;
SELECT * FROM users ORDER BY name ASC, id DESC;

-- Giá»›i háº¡n & phĂ¢n trang
SELECT * FROM users LIMIT 10;
SELECT * FROM users LIMIT 10 OFFSET 20;  -- Page 3

-- Äáº¿m & Aggregate
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

-- Update nhiá»u cá»™t
UPDATE users SET name = 'New Name', role = 'senior' WHERE id = 1;
```

## DELETE

```sql
DELETE FROM users WHERE id = 1;
DELETE FROM users WHERE is_active = false;

-- â ï¸ XoĂ¡ táº¥t cáº£ (cáº©n tháº­n!)
DELETE FROM users;
TRUNCATE TABLE users;  -- Nhanh hÆ¡n DELETE, reset SERIAL
```

## JOIN

```sql
-- INNER JOIN
SELECT u.name, p.title
FROM users u
INNER JOIN posts p ON u.id = p.user_id;

-- LEFT JOIN (táº¥t cáº£ users, ká»ƒ cáº£ khĂ´ng cĂ³ posts)
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

-- Náº¿u lá»—i:
ROLLBACK;
```

## psql Commands

```bash
\l              # Liá»‡t kĂª databases
\c dbname       # Káº¿t ná»‘i database
\dt             # Liá»‡t kĂª tables
\d tablename    # Cáº¥u trĂºc báº£ng
\di             # Liá»‡t kĂª indexes
\x              # Toggle expanded display
\q              # ThoĂ¡t
\i file.sql     # Cháº¡y file SQL
\timing         # Báº­t Ä‘o thá»i gian query
```

## Performance

```sql
-- Xem execution plan
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'a@test.com';

-- Táº¡o index
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_posts_user_published ON posts(user_id, published);
```
