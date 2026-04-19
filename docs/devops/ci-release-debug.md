# Secrets, Release Và Debug Workflow

Phần này tập trung vào secrets, release pipeline, debug và phần tự luyện cuối chương.

---

## Secrets

Secrets dĂ¹ng cho token, password, credentials.

VĂ­ dá»¥ dĂ¹ng secret trong step:

```yaml
- name: Deploy
  env:
    DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}
  run: ./deploy.sh
```

CĂ¡ch thĂªm secret:

- Repo â†’ **Settings**
- **Secrets and variables** â†’ **Actions**
- **New repository secret**

!!! danger "Quan trá»ng"
KhĂ´ng hardcode secrets trong YAML hoáº·c code. KhĂ´ng commit `.env` lĂªn Git.

---

## Build & Push Docker Image (theo tag)

Workflow: push tag `v*` â†’ build â†’ push Docker Hub (hoáº·c GHCR).

```yaml
# .github/workflows/docker.yml
name: Docker Build & Push

on:
  push:
    tags: ["v*"]

permissions:
  contents: read

jobs:
  build-and-push:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Login Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}

      - name: Build & Push
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: |
            myorg/internhub-api:latest
            myorg/internhub-api:${{ github.ref_name }}
```

**Best practice**

- chá»‰ build/push khi **tag** hoáº·c **merge main**
- tag theo version Ä‘á»ƒ rollback dá»…

---

## Debugging workflow

## 1) In thĂ´ng tin runner/event

```yaml
- name: Debug info
  run: |
    echo "Event: ${{ github.event_name }}"
    echo "Ref: ${{ github.ref }}"
    echo "SHA: ${{ github.sha }}"
    echo "Runner OS: ${{ runner.os }}"
```

## 2) Xem log

- Repo â†’ tab **Actions** â†’ chá»n run â†’ chá»n job/step bá»‹ fail

## 3) Re-run

- **Re-run jobs** khi lá»—i do network/flake

## 4) SSH debug (chá»‰ khi tháº­t cáº§n)

CĂ³ thá»ƒ dĂ¹ng `mxschmitt/action-tmate` Ä‘á»ƒ má»Ÿ session debug (cáº©n tháº­n quyá»n vĂ  secrets).

---

## Lá»—i thÆ°á»ng gáº·p

| Lá»—i                  | NguyĂªn nhĂ¢n                       | CĂ¡ch sá»­a                                           |
| -------------------- | --------------------------------- | -------------------------------------------------- |
| Workflow khĂ´ng cháº¡y  | sai `on:` hoáº·c filter branch/path | kiá»ƒm tra trigger, branch, YAML                     |
| `npm ci` fail        | lockfile lá»‡ch                     | cháº¡y `npm install`, commit `package-lock.json`     |
| Test DB fail         | service DB chÆ°a ready             | dĂ¹ng healthcheck hoáº·c retry                        |
| Secret rá»—ng          | sai tĂªn secret / chÆ°a set         | kiá»ƒm tra Settings â†’ Secrets                        |
| Cache khĂ´ng hiá»‡u quáº£ | cache key khĂ´ng Ä‘Ăºng              | dĂ¹ng cache built-in (`setup-node`, `setup-python`) |

---

## Checklist pipeline â€œÄ‘Ăºng chuáº©nâ€

- [ ] CI cháº¡y trĂªn **pull_request**
- [ ] dĂ¹ng `npm ci` / lockfile
- [ ] lint cháº¡y trÆ°á»›c test
- [ ] cache báº­t (npm/pip)
- [ ] khĂ´ng hardcode secrets
- [ ] PR nhá» â†’ CI nhanh

---

## BĂ i táº­p

1. Táº¡o workflow CI cho Node.js: **lint â†’ test â†’ build**
2. ThĂªm badge CI vĂ o README:

```markdown
![CI](https://github.com/<user>/<repo>/actions/workflows/ci.yml/badge.svg)
```

3. ThĂªm matrix build test Node.js 18 vĂ  20

---

## TĂ i liá»‡u tham kháº£o

- [https://docs.github.com/en/actions](https://docs.github.com/en/actions)
- [https://github.com/sdras/awesome-actions](https://github.com/sdras/awesome-actions)
