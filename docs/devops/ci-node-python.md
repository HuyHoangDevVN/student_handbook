# CI Cho Node.js Và Python

Phần này gom workflow tối thiểu, pipeline Node.js, Python và matrix builds.

---

## CI cho Node.js

Mục tiêu: **install → lint → test → build** (dùng `npm ci` và cache).

```yaml
# .github/workflows/ci.yml
name: CI (Node.js)

on:
  pull_request:
    branches: [main]
  push:
    branches: [main, develop]

permissions:
  contents: read

jobs:
  node-ci:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: npm

      - name: Install deps
        run: npm ci

      - name: Lint
        run: npm run lint --if-present

      - name: Test
        run: npm test --if-present

      - name: Build
        run: npm run build --if-present
```

**Gợi ý chuẩn repo Node.js**

- `npm ci` (dùng lockfile) → build “reproducibleâ€
- dùng `--if-present` để workflow không fail nếu repo chưa có script đó

---

## CI cho Python

Mục tiêu: **install → lint → test**, có thể chạy kèm PostgreSQL service.

```yaml
# .github/workflows/ci-python.yml
name: CI (Python)

on:
  pull_request:
    branches: [main]
  push:
    branches: [main]

permissions:
  contents: read

jobs:
  py-test:
    runs-on: ubuntu-latest

    services:
      postgres:
        image: postgres:16-alpine
        env:
          POSTGRES_USER: test
          POSTGRES_PASSWORD: test
          POSTGRES_DB: testdb
        ports:
          - 5432:5432
        options: >-
          --health-cmd "pg_isready -U test -d testdb"
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
          cache: pip

      - name: Install deps
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          # nếu có file dev:
          # pip install -r requirements-dev.txt

      - name: Lint
        run: |
          # ví dụ (tuỳ project)
          # ruff check .
          # black --check .
          echo "Lint step"

      - name: Test
        env:
          DATABASE_URL: postgres://test:test@localhost:5432/testdb
        run: |
          # ví dụ:
          # pytest -q
          echo "Test step"
```

**Gợi ý:** Với Python hiện đại, team hay dùng `ruff + black + pytest`.

---

## Matrix builds (test nhiều phiên bản)

Khi team cần hỗ trợ nhiều Node/Python versions hoặc nhiều OS.

## Node.js matrix (18/20/22)

```yaml
name: CI (Node matrix)

on:
  pull_request:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        node: [18, 20, 22]

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node }}
          cache: npm

      - run: npm ci
      - run: npm test --if-present
```

## Multi-OS matrix (khi thật sự cần)

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest]
    node: [20]
runs-on: ${{ matrix.os }}
```

> Lưu ý: Multi-OS làm CI chậm và tốn runner minutes — chỉ dùng khi dự án cần.

---

