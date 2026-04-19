# CI/CD Fundamentals

Phần này giới thiệu CI/CD, cấu trúc workflow và quy tắc pipeline cơ bản.

---

## CI/CD lĂ  gĂ¬?

```mermaid
graph LR
A[Developer Push / PR] --> B[CI: Lint + Test + Build]
B -->|Pass| C[CD: Deploy Staging]
C -->|Approve| D[CD: Deploy Production]
B -->|Fail| E[Notify + Fix]
```

| Thuáº­t ngá»¯                           | Ă nghÄ©a                                                      |
| ----------------------------------- | ------------------------------------------------------------ |
| CI (Continuous Integration)         | tá»± Ä‘á»™ng lint/test/build khi push/PR                          |
| CD (Continuous Delivery/Deployment) | tá»± Ä‘á»™ng deploy sau khi CI pass (tuá»³ má»©c tá»± Ä‘á»™ng)             |
| Workflow                            | file YAML mĂ´ táº£ pipeline                                     |
| Job                                 | nhĂ³m step cháº¡y trĂªn 1 runner                                 |
| Step                                | 1 hĂ nh Ä‘á»™ng trong job (checkout, setup runtime, run command) |

---

## Cáº¥u trĂºc thÆ° má»¥c chuáº©n

```text
.github/
â””â”€â”€ workflows/
    â”œâ”€â”€ ci.yml
    â”œâ”€â”€ docker.yml
    â”œâ”€â”€ deploy.yml
    â””â”€â”€ docs.yml
```

---

## Quy táº¯c CI â€œchuáº©n teamâ€

- CI cháº¡y trĂªn **Pull Request** lĂ  quan trá»ng nháº¥t
- PR chá»‰ Ä‘Æ°á»£c merge khi **CI xanh**
- Workflow nĂªn:
  - **nhanh**
  - **deterministic** (khĂ´ng phá»¥ thuá»™c mĂ¡y dev)
  - **cache tá»‘t**
  - **fail sá»›m** (lint trÆ°á»›c test)

---

## Quickstart: Workflow tá»‘i thiá»ƒu

Táº¡o file:

```text
.github/workflows/ci.yml
```

Máº«u skeleton:

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

