# Deployment cơ bản

## Mục tiêu

Sau bài này, bạn sẽ:

- Hiểu các khái niệm deploy: staging, production, rollback.
- Deploy ứng dụng đơn giản lên VPS hoặc PaaS.
- Hiểu cơ bản về reverse proxy (Nginx).

## Prerequisites

- [Docker cơ bản](../containers/docker.md).
- [CI/CD](cicd-github-actions.md).

---

## Môi trường Deploy

| Môi trường              | Mục đích                 | Ai truy cập |
| ----------------------- | ------------------------ | ----------- |
| **Development** (local) | Code + test trên máy     | Developer   |
| **Staging**             | Test trước khi lên prod  | Team + QA   |
| **Production**          | Người dùng thật truy cập | End users   |

!!! tip "Quy tắc vàng"
Staging phải **giống production nhất có thể** (cùng OS, database version, config).

---

## Deploy lên VPS (đơn giản)

### Bước 1 – SSH vào server

```bash
ssh user@your-server-ip
```

### Bước 2 – Clone repo + Docker Compose

```bash
git clone https://github.com/<github-org>/internhub-api.git
cd internhub-api

# Tạo .env cho production
cp .env.example .env
nano .env   # Sửa giá trị cho production

# Chạy
docker compose -f docker-compose.prod.yml up -d
```

### Bước 3 – Cấu hình Nginx reverse proxy

```nginx
# /etc/nginx/sites-available/internhub-api
server {
    listen 80;
    server_name api.internhub.local;

    location / {
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

```bash
sudo ln -s /etc/nginx/sites-available/internhub-api /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

---

## Deploy lên PaaS (đơn giản hơn)

### Railway / Render / Fly.io

```bash
# Ví dụ với Fly.io
fly launch
fly deploy
```

Các PaaS thường chỉ cần:

- Dockerfile hoặc buildpack config.
- Biến môi trường (set trên dashboard).
- Git push → tự deploy.

---

## Rollback

```bash
# Docker: quay lại image version cũ
docker compose pull   # Pull latest
docker compose up -d  # Update

# Rollback: chỉ định image tag cũ
# Trong docker-compose.yml: image: internhub-api:v1.2.0
docker compose up -d
```

---

## Checklist trước khi deploy Production

- [ ] Tests pass (CI green).
- [ ] Environment variables đã set đúng.
- [ ] Database migration đã chạy.
- [ ] Không có secrets trong code.
- [ ] HTTPS đã cấu hình (Let's Encrypt).
- [ ] Logs & monitoring đã setup.
- [ ] Có kế hoạch rollback.

---

## Tài liệu tham khảo

- [Nginx Docs](https://nginx.org/en/docs/)
- [Docker Compose in Production](https://docs.docker.com/compose/production/)
