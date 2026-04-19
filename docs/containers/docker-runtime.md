# Docker Runtime Cơ Bản

Phần này tập trung vào image, container và các thao tác chạy container.

---

## KhĂ¡i niá»‡m cá»‘t lĂµi

```mermaid
graph TB
A[Dockerfile] -->|docker build| B[Image]
B -->|docker run| C[Container]
D[Registry] -->|docker pull| B
B -->|docker push| D
```

---

| ThĂ nh pháº§n | Ă nghÄ©a                      |
| ---------- | ---------------------------- |
| Image      | template chá»‰ Ä‘á»c chá»©a app    |
| Container  | instance Ä‘ang cháº¡y cá»§a image |
| Volume     | storage persistent           |
| Network    | máº¡ng giá»¯a containers         |

---

## VĂ­ dá»¥ dá»… hiá»ƒu

| Docker    | Thá»±c táº¿              |
| --------- | -------------------- |
| Image     | file cĂ i Ä‘áº·t Windows |
| Container | mĂ¡y Ä‘Ă£ cĂ i Windows   |
| Volume    | á»• USB                |
| Network   | LAN                  |

---

## Cháº¡y container

VĂ­ dá»¥ Ä‘Æ¡n giáº£n nháº¥t:

```bash
docker run hello-world
```

Docker sáº½:

1. pull image
2. táº¡o container
3. cháº¡y container

---

## Cháº¡y container vá»›i options

```bash
docker run -d \
--name my-nginx \
-p 8080:80 \
-v $(pwd)/html:/usr/share/nginx/html \
nginx:alpine
```

---

## Giáº£i thĂ­ch

| Option   | Ă nghÄ©a           |
| -------- | ----------------- |
| `-d`     | cháº¡y background   |
| `--name` | Ä‘áº·t tĂªn container |
| `-p`     | port mapping      |
| `-v`     | mount volume      |

---

Sau khi cháº¡y:

```
http://localhost:8080
```

---

## Quáº£n lĂ½ container

---

## Xem container

```bash
docker ps
```

---

Xem cáº£ container Ä‘Ă£ stop:

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

