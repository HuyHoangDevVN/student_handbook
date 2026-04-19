# Debug, Logs Và Storage Trong Docker

Phần này gom quản lý image, debug container và volume.

---

## Quáº£n lĂ½ images

---

## Xem images

```bash
docker images
```

---

## Pull image

```bash
docker pull python:3.11-slim
```

---

## Remove image

```bash
docker rmi python:3.11-slim
```

---

## Dá»n image khĂ´ng dĂ¹ng

```bash
docker image prune -a
```

---

## Debug container

---

## Xem logs

```bash
docker logs my-nginx
```

---

Realtime logs:

```bash
docker logs -f my-nginx
```

---

50 dĂ²ng cuá»‘i:

```bash
docker logs --tail 50 my-nginx
```

---

Logs vá»›i timestamp:

```bash
docker logs -t my-nginx
```

---

## Exec vĂ o container

Má»Ÿ shell:

```bash
docker exec -it my-nginx sh
```

---

Cháº¡y lá»‡nh nhanh:

```bash
docker exec my-nginx cat /etc/nginx/nginx.conf
```

---

Náº¿u container cĂ³ bash:

```bash
docker exec -it container-name bash
```

---

## Inspect container

```bash
docker inspect my-nginx
```

---

Láº¥y IP container:

```bash
docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' my-nginx
```

---

Xem resource usage:

```bash
docker stats
```

---

## Volumes

Volumes giĂºp **data khĂ´ng bá»‹ máº¥t khi container xoĂ¡**.

---

## Named volume

```bash
docker volume create mydata
```

---

Mount volume:

```bash
docker run -v mydata:/app/data myimage
```

---

## Bind mount

Mount folder host:

```bash
docker run -v /home/user/data:/app/data myimage
```

---

## Quáº£n lĂ½ volumes

```bash
docker volume ls
```

---

Remove volume:

```bash
docker volume rm mydata
```

---

Remove unused volumes:

```bash
docker volume prune
```

---

### Khi nĂ o dĂ¹ng gĂ¬

| Type         | Use case        |
| ------------ | --------------- |
| Named volume | database data   |
| Bind mount   | source code dev |

---

