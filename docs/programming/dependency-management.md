# Quản lý Dependencies

Dependencies là các **thư viện hoặc package bên ngoài** mà project sử dụng.

Quản lý dependencies đúng cách giúp:

- đảm bảo **mọi developer chạy cùng môi trường**
- tránh lỗi **"works on my machine"**
- giảm rủi ro **security vulnerabilities**

---

## Mục tiêu

Sau bài này bạn có thể:

- hiểu tầm quan trọng của dependency management
- sử dụng **lock file**
- hiểu **Semantic Versioning**
- cập nhật package an toàn

---

## Vì sao dependency management quan trọng

Một project có thể sử dụng **hàng chục đến hàng trăm thư viện**.

Nếu không quản lý đúng:

```text
Developer A: package v1.0
Developer B: package v1.2
CI server: package v2.0
```

Kết quả:

```text
Ứng dụng chạy khác nhau trên mỗi máy
```

---

## Lock File

Lock file ghi lại **chính xác phiên bản dependency** được cài.

Nhờ đó mọi developer và CI server đều cài **giống nhau 100%**.

---

## Lock file theo ngôn ngữ

| Ngôn ngữ        | Lock file         | Commit? |
| --------------- | ----------------- | ------- |
| Python          | requirements.txt  | Có      |
| Node.js         | package-lock.json | Có      |
| Node.js (yarn)  | yarn.lock         | Có      |
| Python (Poetry) | poetry.lock       | Có      |
| Conda           | environment.yml   | Có      |

---

!!! warning "Quy tắc quan trọng"
Luôn **commit lock file** vào repository.

Đây là cách duy nhất để đảm bảo:

```text
Reproducible builds
```

---

## Semantic Versioning (SemVer)

Hầu hết package sử dụng **Semantic Versioning**.

Format:

```text
MAJOR.MINOR.PATCH
```

Ví dụ:

```text
2.1.3
```

---

## Ă nghĩa version

| Phần  | Khi nào tăng     |
| ----- | ---------------- |
| MAJOR | breaking changes |
| MINOR | thêm feature     |
| PATCH | sửa bug          |

---

### Ví dụ

```text
1.2.3 → 2.0.0   breaking changes
2.0.0 → 2.1.0   new feature
2.1.0 → 2.1.1   bug fix
```

---

## Version ranges (Node.js)

Trong `package.json` thường thấy:

| Ký hiệu  | Ă nghĩa                |
| -------- | ---------------------- |
| `^1.2.3` | cho phép upgrade minor |
| `~1.2.3` | chỉ upgrade patch      |
| `1.2.3`  | version chính xác      |
| `*`      | bất kỳ version         |

---

### Ví dụ

```json
"express": "^4.18.2"
```

Range thực tế:

```text
>=4.18.2 <5.0.0
```

---

## Kiểm tra dependency outdated

---

## Node.js

Xem package cũ:

```bash
npm outdated
```

---

Cập nhật theo semver range:

```bash
npm update
```

---

Cập nhật major version:

```bash
npx npm-check-updates -u
npm install
```

---

Kiểm tra security:

```bash
npm audit
```

Fix tự động:

```bash
npm audit fix
```

---

## Python

Xem package outdated:

```bash
pip list --outdated
```

---

Cập nhật package:

```bash
pip install --upgrade flask
```

---

Kiểm tra security:

```bash
pip install safety
safety check
```

---

## Best Practices

---

## 1. Pin version trong production

Ví dụ Python:

```text
flask==2.3.3
```

---

## 2. Luôn commit lock file

Ví dụ:

```text
requirements.txt
package-lock.json
```

---

## 3. Review dependency changes

Khi dependency thay đổi:

- xem changelog
- kiểm tra breaking changes

---

## 4. Audit security thường xuyên

Ví dụ:

```bash
npm audit
safety check
```

---

## 5. Giảm số lượng dependency

Nguyên tắc:

```text
Chỉ cài dependency khi thực sự cần.
```

Mỗi dependency mới có thể mang theo:

- security risk
- performance overhead
- maintenance cost

---

## Lỗi thường gặp

| Lỗi                   | Nguyên nhân             | Cách sửa           |
| --------------------- | ----------------------- | ------------------ |
| Works on my machine   | dependency khác version | commit lock file   |
| Build fail trên CI    | thiếu dependency        | update lock file   |
| Vulnerable dependency | package cũ              | upgrade dependency |

---

## Bài tập

### Bài 1

Tạo project Node.js và:

```bash
npm install express
```

Sau đó xem:

```bash
npm outdated
```

---

### Bài 2

Tạo project Python:

```bash
pip install flask requests
```

Export:

```bash
pip freeze > requirements.txt
```

---

### Bài 3

Tìm một dependency có **security vulnerability** và cập nhật nó.

---

## Tài liệu tham khảo

```text
https://semver.org/
```

```text
https://docs.npmjs.com/cli/v10/commands/npm-audit
```
