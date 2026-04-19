# CI/CD Fundamentals

Phần này giới thiệu CI/CD, cấu trúc workflow và quy tắc pipeline cơ bản.

---

## CI/CD là gì?

```mermaid
graph LR
A[Developer Push / PR] --> B[CI: Lint + Test + Build]
B -->|Pass| C[CD: Deploy Staging]
C -->|Approve| D[CD: Deploy Production]
B -->|Fail| E[Notify + Fix]
```

| Thuật ngữ                           | Ý nghĩa                                                      |
| ----------------------------------- | ------------------------------------------------------------ |
| CI (Continuous Integration)         | tự động lint/test/build khi push/PR                          |
| CD (Continuous Delivery/Deployment) | tự động deploy sau khi CI pass (tuỳ mức tự động)             |
| Workflow                            | file YAML mô tả pipeline                                     |
| Job                                 | nhóm step chạy trên 1 runner                                 |
| Step                                | 1 hành động trong job (checkout, setup runtime, run command) |

---

## Cấu trúc thư mục chuẩn

```text
.github/
└── workflows/
    ├── ci.yml
    ├── docker.yml
    ├── deploy.yml
    └── docs.yml
```

---

## Quy tắc CI "chuẩn team"

- CI chạy trên **Pull Request** là quan trọng nhất
- PR chỉ được merge khi **CI xanh**
- Workflow nên:
  - **nhanh**
  - **deterministic** (không phụ thuộc máy dev)
  - **cache tốt**
  - **fail sớm** (lint trước test)

---

## Quickstart: Workflow tối thiểu

Tạo file:

```text
.github/workflows/ci.yml
```

Mẫu skeleton:

```yaml
name: CI

on:
  pull_request:
  push:
    branches: [main]

jobs:
  ci:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: CI placeholder
        run: echo "Hello CI"
```

---

