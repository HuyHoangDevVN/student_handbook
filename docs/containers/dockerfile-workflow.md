# Dockerfile Và Build Workflow

Phần này tập trung vào Dockerfile, build image, port mapping và phần tự luyện cuối chương.

---

## Dockerfile

Dockerfile dĂ¹ng Ä‘á»ƒ **build image**.

---

## VĂ­ dá»¥ Dockerfile

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

## Cháº¡y image

```bash
docker run -d -p 8000:8000 --name internhub-api internhub-api:1.0
```

---

## Best Practices Dockerfile

---

### 1. DĂ¹ng base image nhá»

```dockerfile
python:3.11-slim
```

---

### 2. Copy dependencies trÆ°á»›c

```dockerfile
COPY requirements.txt .
RUN pip install
```

---

### 3. Gá»™p RUN commands

```dockerfile
RUN apt update && apt install -y curl
```

---

### 4. DĂ¹ng `.dockerignore`

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

VĂ­ dá»¥:

```bash
docker run -p 8080:80 nginx
```

---

Random port:

```bash
docker run -P nginx
```

---

## Lá»—i thÆ°á»ng gáº·p

| Lá»—i                    | NguyĂªn nhĂ¢n      | CĂ¡ch sá»­a            |
| ---------------------- | ---------------- | ------------------- |
| port already allocated | port bá»‹ dĂ¹ng     | Ä‘á»•i port            |
| no space left          | docker Ä‘áº§y disk  | docker system prune |
| COPY failed            | sai path         | kiá»ƒm tra context    |
| container exit         | process crash    | docker logs         |
| exec format error      | sai architecture | build Ä‘Ăºng platform |

---

## Dá»n dáº¹p Docker

XoĂ¡ resources khĂ´ng dĂ¹ng:

```bash
docker system prune -a --volumes
```

---

Xem disk usage:

```bash
docker system df
```

---

## BĂ i táº­p

### BĂ i 1

Cháº¡y nginx:

```bash
docker run -p 8080:80 nginx:alpine
```

Má»Ÿ:

```
http://localhost:8080
```

---

### BĂ i 2

Viáº¿t Dockerfile cho Flask app.

---

### BĂ i 3

VĂ o container nginx:

```bash
docker exec -it nginx sh
```

sá»­a file:

```
/usr/share/nginx/html/index.html
```

---

## TĂ i liá»‡u tham kháº£o

```
https://docs.docker.com/get-started/
```

```
https://docs.docker.com/reference/dockerfile/
```
