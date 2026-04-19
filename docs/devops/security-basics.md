# Bảo mật cơ bản

## Mục tiêu

Sau bài này, bạn sẽ:

- Quản lý **secrets** đúng cách (ENV, vault).
- Hiểu **password hashing** và tại sao không lưu plaintext.
- Hiểu cơ bản về **JWT** (JSON Web Token).
- Tránh các lỗi bảo mật phổ biến.

## Prerequisites

- [HTTP & REST API](../backend/http-rest.md).

---

## Quản lý Secrets

### Không bao giờ làm vậy

```python
# TUYỆT ĐỐI KHÔNG hardcode secrets trong code
DATABASE_URL = "postgres://admin:SuperSecret123@db.prod.com:5432/internhub"
API_KEY = "sk-1234567890abcdef"
```

### ✅ Sử dụng biến môi trường

```python
import os

DATABASE_URL = os.environ.get("DATABASE_URL")
API_KEY = os.environ.get("API_KEY")
```

```bash
# File .env (KHÔNG commit lên Git)
DATABASE_URL=postgres://admin:SuperSecret123@db.prod.com:5432/internhub
API_KEY=sk-1234567890abcdef
```

```gitignore
# .gitignore
.env
.env.local
.env.production
```

### Tạo file `.env.example`

```env
# .env.example (commit file này – không có giá trị thật)
DATABASE_URL=postgres://user:password@localhost:5432/dbname
API_KEY=your-api-key-here
JWT_SECRET=your-secret-here
```

!!! danger "Nếu lỡ commit secret" 1. **Rotate** (đổi) secret ngay lập tức. 2. Xoá khỏi Git history bằng `git filter-branch` hoặc BFG Repo Cleaner. 3. Thông báo team.

---

## Password Hashing

### Tại sao không lưu plaintext?

```text
[Sai] Database bị hack → hacker có tất cả password
   users table:
   | email              | password      |
   | user@test.com      | MyPassword123 |  <- Plaintext

[Đúng] Lưu hash → hacker không thể lấy password gốc
   users table:
   | email              | password_hash                        |
   | user@test.com      | $2b$12$LJ3m4ys3Gz...hashed...value |  <- Bcrypt hash
```

### Ví dụ code

=== "Python (bcrypt)"
```python
import bcrypt

    # Hash password khi đăng ký
    password = "MyPassword123"
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    # Lưu `hashed` vào database

    # Verify khi đăng nhập
    input_password = "MyPassword123"
    if bcrypt.checkpw(input_password.encode('utf-8'), hashed):
        print("Login thành công!")
    else:
        print("Sai mật khẩu!")
    ```

=== "Node.js (bcrypt)"
```javascript
const bcrypt = require('bcrypt');
const SALT_ROUNDS = 12;

    // Hash password khi đăng ký
    const hash = await bcrypt.hash("MyPassword123", SALT_ROUNDS);
    // Lưu `hash` vào database

    // Verify khi đăng nhập
    const isValid = await bcrypt.compare("MyPassword123", hash);
    if (isValid) {
      console.log("Login thành công!");
    }
    ```

---

## JWT (JSON Web Token)

### JWT là gì?

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

### Cấu trúc JWT

```json
// Header
{ "alg": "HS256", "typ": "JWT" }

// Payload (claims)
{
  "userId": 42,
  "email": "user@test.com",
  "role": "intern",
  "iat": 1700000000,        // Issued at
  "exp": 1700003600          // Expiry (1 giờ)
}

// Signature
HMACSHA256(base64(header) + "." + base64(payload), SECRET_KEY)
```

### Ví dụ code

=== "Node.js (jsonwebtoken)"
```javascript
const jwt = require('jsonwebtoken');
const SECRET = process.env.JWT_SECRET;

    // Tạo token khi login
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

    # Tạo token
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
        print("Token hết hạn!")
    except jwt.InvalidTokenError:
        print("Token không hợp lệ!")
    ```

!!! warning "Lưu ý JWT" - JWT **không mã hoá** payload, chỉ **ký** (sign). Nội dung ai cũng đọc được trên [jwt.io](https://jwt.io). - **KHÔNG** lưu thông tin nhạy cảm trong payload (password, credit card). - Đặt thời gian hết hạn ngắn (1h cho access token). - Dùng **refresh token** để lấy access token mới.

---

## Checklist bảo mật cho Fresher

- [ ] Không hardcode secrets trong code.
- [ ] `.env` đã thêm vào `.gitignore`.
- [ ] Password được hash bằng bcrypt (salt rounds â‰¥ 12).
- [ ] JWT có expiry time.
- [ ] Input validation cho tất cả API endpoints.
- [ ] HTTPS trên production.
- [ ] Dependencies được update, không có known vulnerabilities.
- [ ] Không expose debug/stack trace trên production.

---

## Lỗi thường gặp

| Lỗi                        | Nguyên nhân                              | Cách sửa                         |
| -------------------------- | ---------------------------------------- | -------------------------------- |
| Secret bị leak trên GitHub | Commit `.env`                            | Rotate secret, dùng `.gitignore` |
| JWT `invalid signature`    | Secret key khác nhau giữa sign và verify | Dùng cùng 1 secret               |
| `jwt expired`              | Token hết hạn                            | Implement refresh token flow     |
| SQL Injection              | Nối string trực tiếp vào query           | Dùng parameterized queries       |

---

## Tài liệu tham khảo

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [JWT.io](https://jwt.io/)
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
