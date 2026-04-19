# Deployment cÆ¡ báº£n

## Má»¥c tiĂªu

Sau bĂ i nĂ y, báº¡n sáº½:

- Hiá»ƒu cĂ¡c khĂ¡i niá»‡m deploy: staging, production, rollback.
- Deploy á»©ng dá»¥ng Ä‘Æ¡n giáº£n lĂªn VPS hoáº·c PaaS.
- Hiá»ƒu cÆ¡ báº£n vá» reverse proxy (Nginx).

## Prerequisites

- [Docker cÆ¡ báº£n](../containers/docker.md).
- [CI/CD](cicd-github-actions.md).

---

## MĂ´i trÆ°á»ng Deploy

| MĂ´i trÆ°á»ng              | Má»¥c Ä‘Ă­ch                 | Ai truy cáº­p |
| ----------------------- | ------------------------ | ----------- |
| **Development** (local) | Code + test trĂªn mĂ¡y     | Developer   |
| **Staging**             | Test trÆ°á»›c khi lĂªn prod  | Team + QA   |
| **Production**          | NgÆ°á»i dĂ¹ng tháº­t truy cáº­p | End users   |

!!! tip "Quy táº¯c vĂ ng"
Staging pháº£i **giá»‘ng production nháº¥t cĂ³ thá»ƒ** (cĂ¹ng OS, database version, config).

---

## Deploy lĂªn VPS (Ä‘Æ¡n giáº£n)

### BÆ°á»›c 1 â€“ SSH vĂ o server

```bash
ssh user@your-server-ip
```

### BÆ°á»›c 2 â€“ Clone repo + Docker Compose

```bash
git clone https://github.com/<github-org>/internhub-api.git
cd internhub-api

# Táº¡o .env cho production
cp .env.example .env
nano .env   # Sá»­a giĂ¡ trá»‹ cho production

# Cháº¡y
docker compose -f docker-compose.prod.yml up -d
```

### BÆ°á»›c 3 â€“ Cáº¥u hĂ¬nh Nginx reverse proxy

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

## Deploy lĂªn PaaS (Ä‘Æ¡n giáº£n hÆ¡n)

### Railway / Render / Fly.io

```bash
# VĂ­ dá»¥ vá»›i Fly.io
fly launch
fly deploy
```

CĂ¡c PaaS thÆ°á»ng chá»‰ cáº§n:

- Dockerfile hoáº·c buildpack config.
- Biáº¿n mĂ´i trÆ°á»ng (set trĂªn dashboard).
- Git push â†’ tá»± deploy.

---

## Rollback

```bash
# Docker: quay láº¡i image version cÅ©
docker compose pull   # Pull latest
docker compose up -d  # Update

# Rollback: chá»‰ Ä‘á»‹nh image tag cÅ©
# Trong docker-compose.yml: image: internhub-api:v1.2.0
docker compose up -d
```

---

## Checklist trÆ°á»›c khi deploy Production

- [ ] Tests pass (CI green).
- [ ] Environment variables Ä‘Ă£ set Ä‘Ăºng.
- [ ] Database migration Ä‘Ă£ cháº¡y.
- [ ] KhĂ´ng cĂ³ secrets trong code.
- [ ] HTTPS Ä‘Ă£ cáº¥u hĂ¬nh (Let's Encrypt).
- [ ] Logs & monitoring Ä‘Ă£ setup.
- [ ] CĂ³ káº¿ hoáº¡ch rollback.

---

## TĂ i liá»‡u tham kháº£o

- [Nginx Docs](https://nginx.org/en/docs/)
- [Docker Compose in Production](https://docs.docker.com/compose/production/)
