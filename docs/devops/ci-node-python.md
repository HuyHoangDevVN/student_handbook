# CI Cho Node.js Và Python

Phần này gom workflow tối thiểu, pipeline Node.js, Python và matrix builds.

---

## CI cho Node.js

Má»¥c tiĂªu: **install â†’ lint â†’ test â†’ build** (dĂ¹ng `npm ci` vĂ  cache).

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

**Gá»£i Ă½ chuáº©n repo Node.js**

- `npm ci` (dĂ¹ng lockfile) â†’ build â€œreproducibleâ€
- dĂ¹ng `--if-present` Ä‘á»ƒ workflow khĂ´ng fail náº¿u repo chÆ°a cĂ³ script Ä‘Ă³

---

## CI cho Python

Má»¥c tiĂªu: **install â†’ lint â†’ test**, cĂ³ thá»ƒ cháº¡y kĂ¨m PostgreSQL service.

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
          # náº¿u cĂ³ file dev:
          # pip install -r requirements-dev.txt

      - name: Lint
        run: |
          # vĂ­ dá»¥ (tuá»³ project)
          # ruff check .
          # black --check .
          echo "Lint step"

      - name: Test
        env:
          DATABASE_URL: postgres://test:test@localhost:5432/testdb
        run: |
          # vĂ­ dá»¥:
          # pytest -q
          echo "Test step"
```

**Gá»£i Ă½:** Vá»›i Python hiá»‡n Ä‘áº¡i, team hay dĂ¹ng `ruff + black + pytest`.

---

## Matrix builds (test nhiá»u phiĂªn báº£n)

Khi team cáº§n há»— trá»£ nhiá»u Node/Python versions hoáº·c nhiá»u OS.

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

## Multi-OS matrix (khi tháº­t sá»± cáº§n)

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest]
    node: [20]
runs-on: ${{ matrix.os }}
```

> LÆ°u Ă½: Multi-OS lĂ m CI cháº­m vĂ  tá»‘n runner minutes â€” chá»‰ dĂ¹ng khi dá»± Ă¡n cáº§n.

---

