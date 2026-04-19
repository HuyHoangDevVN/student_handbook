# Secrets, Release Và Debug Workflow

Phần này tập trung vào secrets, release pipeline, debug và phần tự luyện cuối chương.

---

## Secrets

Secrets dùng cho token, password, credentials.

Ví dụ dùng secret trong step:

```yaml
- name: Deploy
  env:
    DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}
  run: ./deploy.sh
```

Cách thêm secret:

- Repo → **Settings**
- **Secrets and variables** → **Actions**
- **New repository secret**

!!! danger "Quan trọng"
Không hardcode secrets trong YAML hoặc code. Không commit `.env` lên Git.

---

## Build & Push Docker Image (theo tag)

Workflow: push tag `v*` → build → push Docker Hub (hoặc GHCR).

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

- chỉ build/push khi **tag** hoặc **merge main**
- tag theo version để rollback dễ

---

## Debugging workflow

## 1) In thông tin runner/event

```yaml
- name: Debug info
  run: |
    echo "Event: ${{ github.event_name }}"
    echo "Ref: ${{ github.ref }}"
    echo "SHA: ${{ github.sha }}"
    echo "Runner OS: ${{ runner.os }}"
```

## 2) Xem log

- Repo → tab **Actions** → chọn run → chọn job/step bị fail

## 3) Re-run

- **Re-run jobs** khi lỗi do network/flake

## 4) SSH debug (chỉ khi thật cần)

Có thể dùng `mxschmitt/action-tmate` để mở session debug (cẩn thận quyền và secrets).

---

## Lỗi thường gặp

| Lỗi                  | Nguyên nhân                       | Cách sửa                                           |
| -------------------- | --------------------------------- | -------------------------------------------------- |
| Workflow không chạy  | sai `on:` hoặc filter branch/path | kiểm tra trigger, branch, YAML                     |
| `npm ci` fail        | lockfile lệch                     | chạy `npm install`, commit `package-lock.json`     |
| Test DB fail         | service DB chưa ready             | dùng healthcheck hoặc retry                        |
| Secret rỗng          | sai tên secret / chưa set         | kiểm tra Settings → Secrets                        |
| Cache không hiệu quả | cache key không đúng              | dùng cache built-in (`setup-node`, `setup-python`) |

---

## Checklist pipeline “đúng chuẩnâ€

- [ ] CI chạy trên **pull_request**
- [ ] dùng `npm ci` / lockfile
- [ ] lint chạy trước test
- [ ] cache bật (npm/pip)
- [ ] không hardcode secrets
- [ ] PR nhỏ → CI nhanh

---

## Bài tập

1. Tạo workflow CI cho Node.js: **lint → test → build**
2. Thêm badge CI vào README:

```markdown
![CI](https://github.com/<user>/<repo>/actions/workflows/ci.yml/badge.svg)
```

3. Thêm matrix build test Node.js 18 và 20

---

## Tài liệu tham khảo

- [https://docs.github.com/en/actions](https://docs.github.com/en/actions)
- [https://github.com/sdras/awesome-actions](https://github.com/sdras/awesome-actions)
