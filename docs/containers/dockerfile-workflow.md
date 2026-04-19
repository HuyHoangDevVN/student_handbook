# Dockerfile Và Build Workflow

Phần này tập trung vào Dockerfile, build image, port mapping và phần tự luyện cuối chương.

---

## Dockerfile

Dockerfile dùng để **build image**.

---

## Ví dụ Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "main.py"]
```

---

## Build image

```bash
docker build -t internhub-api:1.0 .
```

---

## Chạy image

```bash
docker run -d -p 8000:8000 --name internhub-api internhub-api:1.0
```

---

## Best Practices Dockerfile

---

### 1. Dùng base image nhỏ

```dockerfile
python:3.11-slim
```

---

### 2. Copy dependencies trước

```dockerfile
COPY requirements.txt .
RUN pip install
```

---

### 3. Gộp RUN commands

```dockerfile
RUN apt update && apt install -y curl
```

---

### 4. Dùng `.dockerignore`

```
.git
node_modules
.venv
__pycache__
.env
```

---

## Port Mapping

```
Host                Container
localhost:8080 ---> container:80
```

---

Ví dụ:

```bash
docker run -p 8080:80 nginx
```

---

Random port:

```bash
docker run -P nginx
```

---

## Lỗi thường gặp

| Lỗi                    | Nguyên nhân      | Cách sửa            |
| ---------------------- | ---------------- | ------------------- |
| port already allocated | port bị dùng     | đổi port            |
| no space left          | docker đầy disk  | docker system prune |
| COPY failed            | sai path         | kiểm tra context    |
| container exit         | process crash    | docker logs         |
| exec format error      | sai architecture | build đúng platform |

---

## Dọn dẹp Docker

Xoá resources không dùng:

```bash
docker system prune -a --volumes
```

---

Xem disk usage:

```bash
docker system df
```

---

## Bài tập

### Bài 1

Chạy nginx:

```bash
docker run -p 8080:80 nginx:alpine
```

Mở:

```
http://localhost:8080
```

---

### Bài 2

Viết Dockerfile cho Flask app.

---

### Bài 3

Vào container nginx:

```bash
docker exec -it nginx sh
```

sửa file:

```
/usr/share/nginx/html/index.html
```

---

## Tài liệu tham khảo

```
https://docs.docker.com/get-started/
```

```
https://docs.docker.com/reference/dockerfile/
```
