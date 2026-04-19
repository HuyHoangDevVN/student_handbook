# Docker Cheat Sheet

> Copy-paste nhanh cĂ¡c lá»‡nh Docker thÆ°á»ng dĂ¹ng.

---

## Container

```bash
docker run -d --name app -p 8080:80 nginx   # Cháº¡y container
docker ps                      # Liá»‡t kĂª Ä‘ang cháº¡y
docker ps -a                   # Liá»‡t kĂª táº¥t cáº£
docker stop app                # Dá»«ng container
docker start app               # Khá»Ÿi Ä‘á»™ng láº¡i
docker restart app             # Restart
docker rm app                  # XoĂ¡ container
docker rm -f app               # Force xoĂ¡
docker container prune         # XoĂ¡ táº¥t cáº£ Ä‘Ă£ dá»«ng
```

## Image

```bash
docker images                  # Liá»‡t kĂª images
docker pull nginx:alpine       # Táº£i image
docker build -t internhub-api:1.0 .    # Build image
docker rmi image-name          # XoĂ¡ image
docker image prune -a          # XoĂ¡ images khĂ´ng dĂ¹ng
docker tag internhub-api:1.0 user/internhub-api:1.0  # Tag image
docker push user/internhub-api:1.0    # Push lĂªn registry
```

## Logs & Debug

```bash
docker logs app                # Xem logs
docker logs -f app             # Follow logs
docker logs --tail 50 app      # 50 dĂ²ng cuá»‘i
docker exec -it app bash       # Shell vĂ o container
docker exec -it app sh         # Shell (Alpine)
docker exec app cat /etc/hosts # Cháº¡y lá»‡nh
docker inspect app             # Chi tiáº¿t container
docker stats                   # Resource usage
```

## Volume

```bash
docker volume create mydata    # Táº¡o volume
docker volume ls               # Liá»‡t kĂª
docker volume rm mydata        # XoĂ¡
docker volume prune            # XoĂ¡ khĂ´ng dĂ¹ng
docker run -v mydata:/app/data ...  # Mount named volume
docker run -v $(pwd):/app ...  # Bind mount
```

## Network

```bash
docker network ls              # Liá»‡t kĂª networks
docker network create mynet    # Táº¡o network
docker network inspect mynet   # Chi tiáº¿t
docker run --network mynet ... # Cháº¡y container trong network
```

## Docker Compose

```bash
docker compose up -d           # Start stack (background)
docker compose down            # Stop + remove
docker compose down -v         # Stop + remove + xoĂ¡ volumes
docker compose ps              # Tráº¡ng thĂ¡i
docker compose logs -f web     # Logs service
docker compose exec web bash   # Shell vĂ o service
docker compose build           # Build láº¡i images
docker compose up -d --build   # Build + start
docker compose pull            # Pull latest images
docker compose restart web     # Restart 1 service
```

## Dá»n dáº¹p

```bash
docker system df               # Xem disk usage
docker system prune            # Dá»n cÆ¡ báº£n
docker system prune -a --volumes  # Dá»n toĂ n bá»™ (â ï¸)
docker stop $(docker ps -q)    # Stop táº¥t cáº£ container
docker rm $(docker ps -aq)     # XoĂ¡ táº¥t cáº£ container
```

## Dockerfile Template

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "main.py"]
```

## docker-compose.yml Template

```yaml
services:
  web:
    build: .
    ports: ["3000:3000"]
    environment:
      - DATABASE_URL=postgres://dev:dev123@db:5432/internhub
    depends_on: [db]

  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: dev
      POSTGRES_PASSWORD: dev123
      POSTGRES_DB: internhub
    ports: ["5432:5432"]
    volumes: [pgdata:/var/lib/postgresql/data]

volumes:
  pgdata:
```

## Port Mapping

```
-p 8080:80    â†’ localhost:8080 â†’ container:80
-p 3000:3000  â†’ localhost:3000 â†’ container:3000
-p 127.0.0.1:5432:5432  â†’ chá»‰ bind localhost
```
