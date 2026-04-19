# MongoDB & Redis

## Mục tiêu

Sau bài này, bạn sẽ:

- Hiểu khi nào dùng NoSQL (MongoDB) vs SQL.
- CRUD cơ bản với MongoDB.
- Sử dụng Redis làm cache / session store.
- Chạy cả hai bằng Docker.

## Prerequisites

- [Docker cơ bản](../containers/docker.md).

---

## MongoDB

### Chạy bằng Docker

```bash
docker run -d \
  --name mongo-dev \
  -e MONGO_INITDB_ROOT_USERNAME=admin \
  -e MONGO_INITDB_ROOT_PASSWORD=admin123 \
  -p 27017:27017 \
  -v mongodata:/data/db \
  mongo:7
```

### Kết nối bằng mongosh

```bash
docker exec -it mongo-dev mongosh -u admin -p admin123
```

### CRUD cơ bản

```javascript
// Chọn database
use internhub

// Insert
db.users.insertOne({ name: "Văn A", email: "a@test.com", age: 22 })
db.users.insertMany([
  { name: "Thị B", email: "b@test.com", age: 23 },
  { name: "Văn C", email: "c@test.com", age: 21 }
])

// Find
db.users.find()                           // Tất cả
db.users.find({ age: { $gte: 22 } })      // age >= 22
db.users.findOne({ email: "a@test.com" })  // 1 document

// Update
db.users.updateOne(
  { email: "a@test.com" },
  { $set: { age: 23, role: "intern" } }
)

// Delete
db.users.deleteOne({ email: "c@test.com" })

// Count
db.users.countDocuments({ age: { $gte: 22 } })
```

### Khi nào dùng MongoDB vs PostgreSQL?

|              | MongoDB               | PostgreSQL                |
| ------------ | --------------------- | ------------------------- |
| Schema       | Flexible (schemaless) | Fixed (strict schema)     |
| Relationship | Embedded documents    | Foreign keys + JOINs      |
| Phù hợp      | Logs, CMS, real-time  | E-commerce, finance, CRUD |
| Query        | Document-based        | SQL                       |
| Transaction  | Có (từ v4.0)          | Có (native, mạnh hơn)     |

---

## Redis

### Chạy bằng Docker

```bash
docker run -d \
  --name redis-dev \
  -p 6379:6379 \
  redis:7-alpine
```

### Lệnh cơ bản

```bash
# Kết nối redis-cli
docker exec -it redis-dev redis-cli

# String
SET user:1:name "Nguyen Van A"
GET user:1:name

# Expiry (TTL)
SET session:abc123 "user_data" EX 3600    # Hết hạn sau 1 giờ
TTL session:abc123                         # Xem thời gian còn lại

# Hash (object-like)
HSET user:1 name "Van A" email "a@test.com" role "intern"
HGETALL user:1
HGET user:1 email

# List
LPUSH queue:emails "email1" "email2"
RPOP queue:emails

# Set
SADD tags:post:1 "docker" "devops" "linux"
SMEMBERS tags:post:1

# Xoá key
DEL user:1:name

# Xem tất cả keys (chỉ dùng khi dev!)
KEYS *
```

### Use cases phổ biến

| Use case          | Cách dùng                             |
| ----------------- | ------------------------------------- |
| **Cache**         | Cache API response, giảm load DB      |
| **Session store** | Lưu session thay vì file/memory       |
| **Rate limiting** | Đếm request per IP bằng INCR + EXPIRE |
| **Queue**         | Task queue đơn giản (LPUSH/RPOP)      |
| **Real-time**     | Pub/Sub cho notifications             |

---

## Lỗi thường gặp

| Lỗi                                       | Nguyên nhân                    | Cách sửa                      |
| ----------------------------------------- | ------------------------------ | ----------------------------- |
| `MongoServerError: Authentication failed` | Sai user/password              | Kiểm tra biến MONGO_INITDB    |
| `WRONGTYPE Operation` (Redis)             | Dùng sai command cho data type | Kiểm tra type bằng `TYPE key` |
| Data mất sau restart                      | Không mount volume             | Thêm `-v` khi `docker run`    |

---

## Tài liệu tham khảo

- [MongoDB Manual](https://www.mongodb.com/docs/manual/)
- [Redis Commands](https://redis.io/commands)
- [Try Redis (interactive)](https://try.redis.io/)
