# API Testing

## Mục tiêu

Sau bài này, bạn sẽ:

- Sử dụng **Postman** / **Thunder Client** để test API.
- Viết test assertions cơ bản trong Postman.
- Sử dụng **curl** và **httpie** từ terminal.

## Prerequisites

- [HTTP & REST API](http-rest.md).

---

## Postman

InternHub API là sample app xuyên suốt trong handbook này, vì vậy bạn có thể import collection mẫu
và dùng lại ở các bài Docker, SQL và deployment.

### Cài đặt

- Tải từ [https://www.postman.com/downloads/](https://www.postman.com/downloads/)
- Hoặc dùng **Thunder Client** (VS Code extension) cho nhẹ hơn.

### Tạo Request

1. Click **New → HTTP Request**.
2. Chọn method: `GET`, `POST`, …
3. Nhập URL: `http://localhost:3000/api/users`.
4. Tab **Body** → `raw` → `JSON` (cho POST/PUT).
5. Click **Send**.

### Postman Collections

- Nhóm các request liên quan vào **Collection**.
- Export/import dưới dạng JSON (`resources/api/postman-collection.json`).
- Collection mẫu này được đặt tên **InternHub API** và dùng `base_url=http://localhost:3000`.

### Biến môi trường (Environment)

```json
// Tạo Environment "Development"
{
  "base_url": "http://localhost:3000",
  "token": "eyJhbGciOiJI..."
}
```

Sử dụng trong request: `{{base_url}}/api/users`

### Viết Test trong Postman

```javascript
// Tab "Tests" trong Postman
pm.test("Status code is 200", function () {
  pm.response.to.have.status(200);
});

pm.test("Response has users array", function () {
  const body = pm.response.json();
  pm.expect(body).to.be.an("array");
  pm.expect(body.length).to.be.greaterThan(0);
});

pm.test("Response time < 500ms", function () {
  pm.expect(pm.response.responseTime).to.be.below(500);
});
```

---

## httpie (thay thế curl, dễ đọc hơn)

```bash
# Cài
pip install httpie

# GET
http GET localhost:3000/api/users

# POST JSON (tự detect Content-Type)
http POST localhost:3000/api/users name="John" email="john@test.com"

# Với header
http GET localhost:3000/api/users Authorization:"Bearer <token>"
```

---

## Test API tự động

### Với pytest (Python)

```python
import requests

BASE_URL = "http://localhost:3000/api"

def test_get_users():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_create_user():
    payload = {"name": "Test", "email": "test@test.com"}
    response = requests.post(f"{BASE_URL}/users", json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "Test"
```

```bash
pytest tests/test_api.py -v
```

---

## Lỗi thường gặp

| Lỗi                              | Nguyên nhân                        | Cách sửa                                    |
| -------------------------------- | ---------------------------------- | ------------------------------------------- |
| Postman trả về HTML thay vì JSON | URL sai hoặc server trả error page | Kiểm tra URL, xem server log                |
| `Could not send request`         | Server chưa chạy                   | Start server trước                          |
| SSL certificate error            | Self-signed cert                   | Tắt SSL verification trong Postman settings |

---

## Tài liệu tham khảo

- [Postman Learning Center](https://learning.postman.com/)
- [httpie Docs](https://httpie.io/docs)
