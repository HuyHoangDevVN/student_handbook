# Index, Transaction Và Tối Ưu SQL

Phần này đi qua index, transaction, psql cheat sheet và phần tự luyện cuối chương.

---

## Index

Index giĂºp **tÄƒng tá»‘c truy váº¥n**.

---

### Táº¡o index

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

### PhĂ¢n tĂ­ch query

```sql
EXPLAIN ANALYZE
SELECT * FROM users
WHERE email = 'a.nguyen@example.com';
```

---

## Transaction

Transaction Ä‘áº£m báº£o **atomic operations**.

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

Náº¿u cĂ³ lá»—i:

```sql
ROLLBACK;
```

---

## psql Cheat Sheet

| Command       | MĂ´ táº£                |
| ------------- | -------------------- |
| `\l`          | danh sĂ¡ch database   |
| `\dt`         | danh sĂ¡ch table      |
| `\d users`    | schema table         |
| `\x`          | toggle expanded view |
| `\q`          | exit                 |
| `\i file.sql` | cháº¡y file SQL        |

---

## Lá»—i thÆ°á»ng gáº·p

| Lá»—i                     | NguyĂªn nhĂ¢n          | CĂ¡ch sá»­a          |
| ----------------------- | -------------------- | ----------------- |
| connection refused      | PostgreSQL chÆ°a cháº¡y | start container   |
| relation does not exist | chÆ°a táº¡o table       | cháº¡y CREATE TABLE |
| duplicate key           | dá»¯ liá»‡u trĂ¹ng        | dĂ¹ng unique check |
| permission denied       | user thiáº¿u quyá»n     | GRANT permissions |

---

## BĂ i táº­p

### BĂ i 1

Táº¡o báº£ng:

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

### BĂ i 2

Insert 5 sáº£n pháº©m vĂ  query:

```
price > 100000
stock > 0
```

---

### BĂ i 3

JOIN:

```
users + posts
```

Ä‘áº¿m sá»‘ bĂ i viáº¿t má»—i user.

---

## TĂ i liá»‡u tham kháº£o

```
https://www.postgresqltutorial.com/
```

```
https://sqlbolt.com/
```
