# MongoDB & Redis

## Má»¥c tiĂªu

Sau bĂ i nĂ y, báº¡n sáº½:

- Hiá»ƒu khi nĂ o dĂ¹ng NoSQL (MongoDB) vs SQL.
- CRUD cÆ¡ báº£n vá»›i MongoDB.
- Sá»­ dá»¥ng Redis lĂ m cache / session store.
- Cháº¡y cáº£ hai báº±ng Docker.

## Prerequisites

- [Docker cÆ¡ báº£n](../containers/docker.md).

---

## MongoDB

### Cháº¡y báº±ng Docker

```bash
docker run -d \
  --name mongo-dev \
  -e MONGO_INITDB_ROOT_USERNAME=admin \
  -e MONGO_INITDB_ROOT_PASSWORD=admin123 \
  -p 27017:27017 \
  -v mongodata:/data/db \
  mongo:7
```

### Káº¿t ná»‘i báº±ng mongosh

```bash
docker exec -it mongo-dev mongosh -u admin -p admin123
```

### CRUD cÆ¡ báº£n

```javascript
// Chá»n database
use internhub

// Insert
db.users.insertOne({ name: "VÄƒn A", email: "a@test.com", age: 22 })
db.users.insertMany([
  { name: "Thá»‹ B", email: "b@test.com", age: 23 },
  { name: "VÄƒn C", email: "c@test.com", age: 21 }
])

// Find
db.users.find()                           // Táº¥t cáº£
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

### Khi nĂ o dĂ¹ng MongoDB vs PostgreSQL?

|              | MongoDB               | PostgreSQL                |
| ------------ | --------------------- | ------------------------- |
| Schema       | Flexible (schemaless) | Fixed (strict schema)     |
| Relationship | Embedded documents    | Foreign keys + JOINs      |
| PhĂ¹ há»£p      | Logs, CMS, real-time  | E-commerce, finance, CRUD |
| Query        | Document-based        | SQL                       |
| Transaction  | CĂ³ (tá»« v4.0)          | CĂ³ (native, máº¡nh hÆ¡n)     |

---

## Redis

### Cháº¡y báº±ng Docker

```bash
docker run -d \
  --name redis-dev \
  -p 6379:6379 \
  redis:7-alpine
```

### Lá»‡nh cÆ¡ báº£n

```bash
# Káº¿t ná»‘i redis-cli
docker exec -it redis-dev redis-cli

# String
SET user:1:name "Nguyen Van A"
GET user:1:name

# Expiry (TTL)
SET session:abc123 "user_data" EX 3600    # Háº¿t háº¡n sau 1 giá»
TTL session:abc123                         # Xem thá»i gian cĂ²n láº¡i

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

# XoĂ¡ key
DEL user:1:name

# Xem táº¥t cáº£ keys (chá»‰ dĂ¹ng khi dev!)
KEYS *
```

### Use cases phá»• biáº¿n

| Use case          | CĂ¡ch dĂ¹ng                             |
| ----------------- | ------------------------------------- |
| **Cache**         | Cache API response, giáº£m load DB      |
| **Session store** | LÆ°u session thay vĂ¬ file/memory       |
| **Rate limiting** | Äáº¿m request per IP báº±ng INCR + EXPIRE |
| **Queue**         | Task queue Ä‘Æ¡n giáº£n (LPUSH/RPOP)      |
| **Real-time**     | Pub/Sub cho notifications             |

---

## Lá»—i thÆ°á»ng gáº·p

| Lá»—i                                       | NguyĂªn nhĂ¢n                    | CĂ¡ch sá»­a                      |
| ----------------------------------------- | ------------------------------ | ----------------------------- |
| `MongoServerError: Authentication failed` | Sai user/password              | Kiá»ƒm tra biáº¿n MONGO_INITDB    |
| `WRONGTYPE Operation` (Redis)             | DĂ¹ng sai command cho data type | Kiá»ƒm tra type báº±ng `TYPE key` |
| Data máº¥t sau restart                      | KhĂ´ng mount volume             | ThĂªm `-v` khi `docker run`    |

---

## TĂ i liá»‡u tham kháº£o

- [MongoDB Manual](https://www.mongodb.com/docs/manual/)
- [Redis Commands](https://redis.io/commands)
- [Try Redis (interactive)](https://try.redis.io/)
