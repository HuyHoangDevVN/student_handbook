# API Testing

## Má»¥c tiĂªu

Sau bĂ i nĂ y, báº¡n sáº½:

- Sá»­ dá»¥ng **Postman** / **Thunder Client** Ä‘á»ƒ test API.
- Viáº¿t test assertions cÆ¡ báº£n trong Postman.
- Sá»­ dá»¥ng **curl** vĂ  **httpie** tá»« terminal.

## Prerequisites

- [HTTP & REST API](http-rest.md).

---

## Postman

InternHub API la sample app xuyen suot trong handbook nay, vi vay ban co the import collection mau
va dung lai o cac bai Docker, SQL va deployment.

### CĂ i Ä‘áº·t

- Táº£i tá»« [https://www.postman.com/downloads/](https://www.postman.com/downloads/)
- Hoáº·c dĂ¹ng **Thunder Client** (VS Code extension) cho nháº¹ hÆ¡n.

### Táº¡o Request

1. Click **New â†’ HTTP Request**.
2. Chá»n method: `GET`, `POST`, â€¦
3. Nháº­p URL: `http://localhost:3000/api/users`.
4. Tab **Body** â†’ `raw` â†’ `JSON` (cho POST/PUT).
5. Click **Send**.

### Postman Collections

- NhĂ³m cĂ¡c request liĂªn quan vĂ o **Collection**.
- Export/import dÆ°á»›i dáº¡ng JSON (`resources/api/postman-collection.json`).
- Collection mau nay duoc dat ten **InternHub API** va dung `base_url=http://localhost:3000`.

### Biáº¿n mĂ´i trÆ°á»ng (Environment)

```json
// Táº¡o Environment "Development"
{
  "base_url": "http://localhost:3000",
  "token": "eyJhbGciOiJI..."
}
```

Sá»­ dá»¥ng trong request: `{{base_url}}/api/users`

### Viáº¿t Test trong Postman

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

## httpie (thay tháº¿ curl, dá»… Ä‘á»c hÆ¡n)

```bash
# CĂ i
pip install httpie

# GET
http GET localhost:3000/api/users

# POST JSON (tá»± detect Content-Type)
http POST localhost:3000/api/users name="John" email="john@test.com"

# Vá»›i header
http GET localhost:3000/api/users Authorization:"Bearer <token>"
```

---

## Test API tá»± Ä‘á»™ng

### Vá»›i pytest (Python)

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

## Lá»—i thÆ°á»ng gáº·p

| Lá»—i                              | NguyĂªn nhĂ¢n                        | CĂ¡ch sá»­a                                    |
| -------------------------------- | ---------------------------------- | ------------------------------------------- |
| Postman tráº£ vá» HTML thay vĂ¬ JSON | URL sai hoáº·c server tráº£ error page | Kiá»ƒm tra URL, xem server log                |
| `Could not send request`         | Server chÆ°a cháº¡y                   | Start server trÆ°á»›c                          |
| SSL certificate error            | Self-signed cert                   | Táº¯t SSL verification trong Postman settings |

---

## TĂ i liá»‡u tham kháº£o

- [Postman Learning Center](https://learning.postman.com/)
- [httpie Docs](https://httpie.io/docs)
