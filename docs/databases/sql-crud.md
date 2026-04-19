# SQL CRUD Cơ Bản

Phần này gom các thao tác tạo bảng, thêm dữ liệu, truy vấn, cập nhật và xoá.

---

## SQL cÆ¡ báº£n

---

## Táº¡o báº£ng

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
('Nguyá»…n VÄƒn A','a.nguyen@example.com','intern'),
('Tráº§n Thá»‹ B','b.tran@example.com','developer'),
('LĂª VÄƒn C','c.le@example.com','lead');
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

### Láº¥y táº¥t cáº£ dá»¯ liá»‡u

```sql
SELECT * FROM users;
```

---

### Láº¥y cá»™t cá»¥ thá»ƒ

```sql
SELECT name, email
FROM users
WHERE role = 'intern';
```

---

### Sáº¯p xáº¿p

```sql
SELECT *
FROM users
ORDER BY created_at DESC;
```

---

### Giá»›i háº¡n káº¿t quáº£

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

### TĂ¬m kiáº¿m text

```sql
SELECT *
FROM users
WHERE name ILIKE '%nguyen%';
```

---

## JOIN

JOIN giĂºp káº¿t há»£p dá»¯ liá»‡u tá»« nhiá»u báº£ng.

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

!!! danger "Cáº£nh bĂ¡o"
LuĂ´n kiá»ƒm tra Ä‘iá»u kiá»‡n trÆ°á»›c khi cháº¡y:

```sql
UPDATE
DELETE
```

NĂªn cháº¡y:

```sql
SELECT
```

trÆ°á»›c Ä‘á»ƒ Ä‘áº£m báº£o query Ä‘Ăºng.

---

