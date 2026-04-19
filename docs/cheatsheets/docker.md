# Docker Cheat Sheet

> Copy-paste nhanh các lệnh Docker thường dùng.

---

## Container

```bash
docker run -d --name app -p 8080:80 nginx   # Chạy container
docker ps                      # Liệt kê đang chạy
docker ps -a                   # Liệt kê tất cả
docker stop app                # Dừng container
docker start app               # Khởi động lại
docker restart app             # Restart
docker rm app                  # Xoá container
docker rm -f app               # Force xoá
docker container prune         # Xoá tất cả đã dừng
```

## Image

```bash
docker images                  # Liệt kê images
docker pull nginx:alpine       # Tải image
docker build -t internhub-api:1.0 .    # Build image
docker rmi image-name          # Xoá image
docker image prune -a          # Xoá images không dùng
docker tag internhub-api:1.0 user/internhub-api:1.0  # Tag image
docker push user/internhub-api:1.0    # Push lên registry
```

## Logs & Debug

```bash
docker logs app                # Xem logs
docker logs -f app             # Follow logs
docker logs --tail 50 app      # 50 dòng cuối
docker exec -it app bash       # Shell vào container
docker exec -it app sh         # Shell (Alpine)
docker exec app cat /etc/hosts # Chạy lệnh
docker inspect app             # Chi tiết container
docker stats                   # Resource usage
```

## Volume

```bash
docker volume create mydata    # Tạo volume
docker volume ls               # Liệt kê
docker volume rm mydata        # Xoá
docker volume prune            # Xoá không dùng
docker run -v mydata:/app/data ...  # Mount named volume
docker run -v $(pwd):/app ...  # Bind mount
```

## Network

```bash
docker network ls              # Liệt kê networks
docker network create mynet    # Tạo network
docker network inspect mynet   # Chi tiết
docker run --network mynet ... # Chạy container trong network
```

## Docker Compose

```bash
docker compose up -d           # Start stack (background)
docker compose down            # Stop + remove
docker compose down -v         # Stop + remove + xoá volumes
docker compose ps              # Trạng thái
docker compose logs -f web     # Logs service
docker compose exec web bash   # Shell vào service
docker compose build           # Build lại images
docker compose up -d --build   # Build + start
docker compose pull            # Pull latest images
docker compose restart web     # Restart 1 service
```

## Dọn dẹp

```bash
docker system df               # Xem disk usage
docker system prune            # Dọn cơ bản
docker system prune -a --volumes  # Dọn toàn bộ (â ï¸)
docker stop $(docker ps -q)    # Stop tất cả container
docker rm $(docker ps -aq)     # Xoá tất cả container
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
-p 8080:80    → localhost:8080 → container:80
-p 3000:3000  → localhost:3000 → container:3000
-p 127.0.0.1:5432:5432  → chỉ bind localhost
```
