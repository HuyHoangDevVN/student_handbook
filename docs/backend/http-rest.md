# HTTP & REST API

HTTP lĂ  giao thá»©c ná»n táº£ng cá»§a web.
REST API lĂ  cĂ¡ch phá»• biáº¿n Ä‘á»ƒ xĂ¢y dá»±ng **backend services** cho web vĂ  mobile applications.

Trang nĂ y giá»›i thiá»‡u:

- HTTP request / response
- HTTP methods vĂ  status codes
- nguyĂªn táº¯c thiáº¿t káº¿ REST API
- cĂ¡ch gá»i API báº±ng `curl`

---

## Má»¥c tiĂªu

Sau bĂ i nĂ y báº¡n cĂ³ thá»ƒ:

- hiá»ƒu cĂ¡ch **HTTP hoáº¡t Ä‘á»™ng**
- sá»­ dá»¥ng cĂ¡c HTTP methods phá»• biáº¿n
- thiáº¿t káº¿ **REST API endpoints**
- test API báº±ng **curl**

---

## YĂªu cáº§u

Báº¡n cáº§n cĂ³ **terminal**.

Náº¿u chÆ°a quen command line:

```text
Terminal cÆ¡ báº£n
```

---

## HTTP hoáº¡t Ä‘á»™ng tháº¿ nĂ o

```mermaid
sequenceDiagram
    Client->>Server: HTTP Request (GET /api/users)
    Server-->>Client: HTTP Response (200 OK + JSON)
```

---

## Cáº¥u trĂºc HTTP Request

Má»™t request HTTP gá»“m:

```text
Method
URL
Headers
Body
```

VĂ­ dá»¥:

```http
POST /api/users HTTP/1.1
Host: api.internhub.local
Content-Type: application/json
Authorization: Bearer <token>
```

Body:

```json
{
  "name": "Minh Nguyen",
  "email": "minh@internhub.local"
}
```

---

## HTTP Methods

| Method | Má»¥c Ä‘Ă­ch          | Idempotent |
| ------ | ----------------- | ---------- |
| GET    | láº¥y dá»¯ liá»‡u       | CĂ³         |
| POST   | táº¡o má»›i           | KhĂ´ng      |
| PUT    | cáº­p nháº­t toĂ n bá»™  | CĂ³         |
| PATCH  | cáº­p nháº­t má»™t pháº§n | CĂ³         |
| DELETE | xoĂ¡               | CĂ³         |

---

### VĂ­ dá»¥

```text
GET    /api/users
POST   /api/users
PUT    /api/users/1
PATCH  /api/users/1
DELETE /api/users/1
```

---

## HTTP Status Codes

HTTP response luĂ´n cĂ³ **status code**.

---

## 2xx â€“ Success

| Code | Ă nghÄ©a    |
| ---- | ---------- |
| 200  | OK         |
| 201  | Created    |
| 204  | No Content |

---

## 3xx â€“ Redirect

| Code | Ă nghÄ©a           |
| ---- | ----------------- |
| 301  | Moved Permanently |
| 304  | Not Modified      |

---

## 4xx â€“ Client Error

| Code | Ă nghÄ©a      |
| ---- | ------------ |
| 400  | Bad Request  |
| 401  | Unauthorized |
| 403  | Forbidden    |
| 404  | Not Found    |

---

## 5xx â€“ Server Error

| Code | Ă nghÄ©a               |
| ---- | --------------------- |
| 500  | Internal Server Error |
| 503  | Service Unavailable   |

---

## REST API Design

REST API sá»­ dá»¥ng **resource-based URLs**.

---

## Endpoint chuáº©n

```text
GET    /api/users
GET    /api/users/42
POST   /api/users
PUT    /api/users/42
DELETE /api/users/42
```

---

### Resource nested

```text
GET /api/users/42/posts
```

---

## Quy táº¯c thiáº¿t káº¿ API

- dĂ¹ng **danh tá»« sá»‘ nhiá»u**

```text
/users
/products
/orders
```

---

- dĂ¹ng **kebab-case**

```text
/order-items
```

---

- khĂ´ng dĂ¹ng Ä‘á»™ng tá»« trong URL

âŒ Sai:

```text
/api/getUsers
/api/createUser
```

---

## Gá»i API báº±ng curl

`curl` lĂ  cĂ´ng cá»¥ CLI Ä‘á»ƒ gá»i HTTP API.

---

## GET request

```bash
curl http://localhost:3000/api/users
```

---

## GET vá»›i header

```bash
curl -H "Authorization: Bearer <token>" \
http://localhost:3000/api/users
```

---

## POST JSON

```bash
curl -X POST http://localhost:3000/api/users \
-H "Content-Type: application/json" \
-d '{"name":"Minh Nguyen","email":"minh@internhub.local"}'
```

---

## PUT request

```bash
curl -X PUT http://localhost:3000/api/users/1 \
-H "Content-Type: application/json" \
-d '{"name":"John Updated"}'
```

---

## DELETE request

```bash
curl -X DELETE http://localhost:3000/api/users/1
```

---

## Xem headers

```bash
curl -I http://localhost:3000/api/users
```

---

## Debug request

```bash
curl -v http://localhost:3000/api/users
```

---

## JSON Request / Response

---

## Request

```json
{
  "name": "Nguyá»…n VÄƒn A",
  "email": "a.nguyen@example.com",
  "role": "intern"
}
```

---

## Response

```json
{
  "id": 42,
  "name": "Nguyá»…n VÄƒn A",
  "email": "a.nguyen@example.com",
  "role": "intern",
  "createdAt": "2025-01-15T10:30:00Z"
}
```

---

## Error Response

Má»™t API tá»‘t nĂªn tráº£ lá»—i theo format thá»‘ng nháº¥t.

---

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Email is required",
    "details": [
      {
        "field": "email",
        "message": "must not be empty"
      }
    ]
  }
}
```

---

## Lá»—i thÆ°á»ng gáº·p

| Lá»—i                | NguyĂªn nhĂ¢n             | CĂ¡ch sá»­a        |
| ------------------ | ----------------------- | --------------- |
| connection refused | server chÆ°a cháº¡y        | kiá»ƒm tra port   |
| 401 Unauthorized   | thiáº¿u token             | kiá»ƒm tra header |
| 404 Not Found      | endpoint sai            | kiá»ƒm tra URL    |
| CORS error         | server chÆ°a enable CORS | thĂªm middleware |

---

## BĂ i táº­p

### BĂ i 1

DĂ¹ng `curl` gá»i API:

```text
GET /api/users
```

---

### BĂ i 2

Táº¡o request POST:

```text
POST /api/users
```

Body:

```json
{
  "name": "Test User"
}
```

---

### BĂ i 3

Test cĂ¡c status codes:

```text
200
404
500
```

---

## TĂ i liá»‡u tham kháº£o

```
https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
```

```
https://restfulapi.net/
```
