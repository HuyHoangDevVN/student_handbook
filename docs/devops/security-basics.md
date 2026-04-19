# Báº£o máº­t cÆ¡ báº£n

## Má»¥c tiĂªu

Sau bĂ i nĂ y, báº¡n sáº½:

- Quáº£n lĂ½ **secrets** Ä‘Ăºng cĂ¡ch (ENV, vault).
- Hiá»ƒu **password hashing** vĂ  táº¡i sao khĂ´ng lÆ°u plaintext.
- Hiá»ƒu cÆ¡ báº£n vá» **JWT** (JSON Web Token).
- TrĂ¡nh cĂ¡c lá»—i báº£o máº­t phá»• biáº¿n.

## Prerequisites

- [HTTP & REST API](../backend/http-rest.md).

---

## Quáº£n lĂ½ Secrets

### âŒ KHĂ”NG BAO GIá»œ

```python
# TUYá»†T Äá»I KHĂ”NG hardcode secrets trong code
DATABASE_URL = "postgres://admin:SuperSecret123@db.prod.com:5432/internhub"
API_KEY = "sk-1234567890abcdef"
```

### âœ… Sá»­ dá»¥ng biáº¿n mĂ´i trÆ°á»ng

```python
import os

DATABASE_URL = os.environ.get("DATABASE_URL")
API_KEY = os.environ.get("API_KEY")
```

```bash
# File .env (KHĂ”NG commit lĂªn Git)
DATABASE_URL=postgres://admin:SuperSecret123@db.prod.com:5432/internhub
API_KEY=sk-1234567890abcdef
```

```gitignore
# .gitignore
.env
.env.local
.env.production
```

### Táº¡o file `.env.example`

```env
# .env.example (commit file nĂ y â€“ khĂ´ng cĂ³ giĂ¡ trá»‹ tháº­t)
DATABASE_URL=postgres://user:password@localhost:5432/dbname
API_KEY=your-api-key-here
JWT_SECRET=your-secret-here
```

!!! danger "Náº¿u lá»¡ commit secret" 1. **Rotate** (Ä‘á»•i) secret ngay láº­p tá»©c. 2. XoĂ¡ khá»i Git history báº±ng `git filter-branch` hoáº·c BFG Repo Cleaner. 3. ThĂ´ng bĂ¡o team.

---

## Password Hashing

### Táº¡i sao khĂ´ng lÆ°u plaintext?

```
âŒ Database bá»‹ hack â†’ hacker cĂ³ táº¥t cáº£ password
   users table:
   | email              | password      |
   | user@test.com      | MyPassword123 |  â† Plaintext!

âœ… LÆ°u hash â†’ hacker khĂ´ng thá»ƒ láº¥y password gá»‘c
   users table:
   | email              | password_hash                          |
   | user@test.com      | $2b$12$LJ3m4ys3Gz...hashed...value   |  â† Bcrypt hash
```

### VĂ­ dá»¥ code

=== "Python (bcrypt)"
```python
import bcrypt

    # Hash password khi Ä‘Äƒng kĂ½
    password = "MyPassword123"
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    # LÆ°u `hashed` vĂ o database

    # Verify khi Ä‘Äƒng nháº­p
    input_password = "MyPassword123"
    if bcrypt.checkpw(input_password.encode('utf-8'), hashed):
        print("Login thĂ nh cĂ´ng!")
    else:
        print("Sai máº­t kháº©u!")
    ```

=== "Node.js (bcrypt)"
```javascript
const bcrypt = require('bcrypt');
const SALT_ROUNDS = 12;

    // Hash password khi Ä‘Äƒng kĂ½
    const hash = await bcrypt.hash("MyPassword123", SALT_ROUNDS);
    // LÆ°u `hash` vĂ o database

    // Verify khi Ä‘Äƒng nháº­p
    const isValid = await bcrypt.compare("MyPassword123", hash);
    if (isValid) {
      console.log("Login thĂ nh cĂ´ng!");
    }
    ```

---

## JWT (JSON Web Token)

### JWT lĂ  gĂ¬?

```
Header.Payload.Signature
eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjF9.signature_here
```

```mermaid
sequenceDiagram
    Client->>Server: POST /login {email, password}
    Server-->>Client: 200 {accessToken: "eyJ..."}
    Client->>Server: GET /api/users (Header: Authorization: Bearer eyJ...)
    Server-->>Client: 200 {users: [...]}
```

### Cáº¥u trĂºc JWT

```json
// Header
{ "alg": "HS256", "typ": "JWT" }

// Payload (claims)
{
  "userId": 42,
  "email": "user@test.com",
  "role": "intern",
  "iat": 1700000000,        // Issued at
  "exp": 1700003600          // Expiry (1 giá»)
}

// Signature
HMACSHA256(base64(header) + "." + base64(payload), SECRET_KEY)
```

### VĂ­ dá»¥ code

=== "Node.js (jsonwebtoken)"
```javascript
const jwt = require('jsonwebtoken');
const SECRET = process.env.JWT_SECRET;

    // Táº¡o token khi login
    const token = jwt.sign(
      { userId: 42, role: 'intern' },
      SECRET,
      { expiresIn: '1h' }
    );

    // Verify token trong middleware
    function authMiddleware(req, res, next) {
      const token = req.headers.authorization?.split(' ')[1];
      if (!token) return res.status(401).json({ error: 'No token' });

      try {
        const decoded = jwt.verify(token, SECRET);
        req.user = decoded;
        next();
      } catch (err) {
        return res.status(401).json({ error: 'Invalid token' });
      }
    }
    ```

=== "Python (PyJWT)"
```python
import jwt
import os
from datetime import datetime, timedelta

    SECRET = os.environ.get("JWT_SECRET")

    # Táº¡o token
    payload = {
        "userId": 42,
        "role": "intern",
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET, algorithm="HS256")

    # Verify token
    try:
        decoded = jwt.decode(token, SECRET, algorithms=["HS256"])
        print(decoded["userId"])  # 42
    except jwt.ExpiredSignatureError:
        print("Token háº¿t háº¡n!")
    except jwt.InvalidTokenError:
        print("Token khĂ´ng há»£p lá»‡!")
    ```

!!! warning "LÆ°u Ă½ JWT" - JWT **khĂ´ng mĂ£ hoĂ¡** payload, chá»‰ **kĂ½** (sign). Ná»™i dung ai cÅ©ng Ä‘á»c Ä‘Æ°á»£c trĂªn [jwt.io](https://jwt.io). - **KHĂ”NG** lÆ°u thĂ´ng tin nháº¡y cáº£m trong payload (password, credit card). - Äáº·t thá»i gian háº¿t háº¡n ngáº¯n (1h cho access token). - DĂ¹ng **refresh token** Ä‘á»ƒ láº¥y access token má»›i.

---

## Checklist báº£o máº­t cho Fresher

- [ ] KhĂ´ng hardcode secrets trong code.
- [ ] `.env` Ä‘Ă£ thĂªm vĂ o `.gitignore`.
- [ ] Password Ä‘Æ°á»£c hash báº±ng bcrypt (salt rounds â‰¥ 12).
- [ ] JWT cĂ³ expiry time.
- [ ] Input validation cho táº¥t cáº£ API endpoints.
- [ ] HTTPS trĂªn production.
- [ ] Dependencies Ä‘Æ°á»£c update, khĂ´ng cĂ³ known vulnerabilities.
- [ ] KhĂ´ng expose debug/stack trace trĂªn production.

---

## Lá»—i thÆ°á»ng gáº·p

| Lá»—i                        | NguyĂªn nhĂ¢n                              | CĂ¡ch sá»­a                         |
| -------------------------- | ---------------------------------------- | -------------------------------- |
| Secret bá»‹ leak trĂªn GitHub | Commit `.env`                            | Rotate secret, dĂ¹ng `.gitignore` |
| JWT `invalid signature`    | Secret key khĂ¡c nhau giá»¯a sign vĂ  verify | DĂ¹ng cĂ¹ng 1 secret               |
| `jwt expired`              | Token háº¿t háº¡n                            | Implement refresh token flow     |
| SQL Injection              | Ná»‘i string trá»±c tiáº¿p vĂ o query           | DĂ¹ng parameterized queries       |

---

## TĂ i liá»‡u tham kháº£o

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [JWT.io](https://jwt.io/)
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
