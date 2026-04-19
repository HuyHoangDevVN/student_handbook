# Docker Runtime Cơ Bản

Phần này tập trung vào image, container và các thao tác chạy container.

---

## Khái niệm cốt lõi

```mermaid
graph TB
A[Dockerfile] -->|docker build| B[Image]
B -->|docker run| C[Container]
D[Registry] -->|docker pull| B
B -->|docker push| D
```

---

| Thành phần | Ă nghĩa                      |
| ---------- | ---------------------------- |
| Image      | template chỉ đọc chứa app    |
| Container  | instance đang chạy của image |
| Volume     | storage persistent           |
| Network    | mạng giữa containers         |

---

## Ví dụ dễ hiểu

| Docker    | Thực tế              |
| --------- | -------------------- |
| Image     | file cài đặt Windows |
| Container | máy đã cài Windows   |
| Volume    | ổ USB                |
| Network   | LAN                  |

---

## Chạy container

Ví dụ đơn giản nhất:

```bash
docker run hello-world
```

Docker sẽ:

1. pull image
2. tạo container
3. chạy container

---

## Chạy container với options

```bash
docker run -d \
--name my-nginx \
-p 8080:80 \
-v $(pwd)/html:/usr/share/nginx/html \
nginx:alpine
```

---

## Giải thích

| Option   | Ă nghĩa           |
| -------- | ----------------- |
| `-d`     | chạy background   |
| `--name` | đặt tên container |
| `-p`     | port mapping      |
| `-v`     | mount volume      |

---

Sau khi chạy:

```
http://localhost:8080
```

---

## Quản lý container

---

## Xem container

```bash
docker ps
```

---

Xem cả container đã stop:

```bash
docker ps -a
```

---

## Stop container

```bash
docker stop my-nginx
```

---

## Start container

```bash
docker start my-nginx
```

---

## Restart

```bash
docker restart my-nginx
```

---

## Remove container

```bash
docker rm my-nginx
```

---

Force remove:

```bash
docker rm -f my-nginx
```

---

