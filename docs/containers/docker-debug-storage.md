# Debug, Logs Và Storage Trong Docker

Phần này gom quản lý image, debug container và volume.

---

## Quản lý images

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

## Dọn image không dùng

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

50 dòng cuối:

```bash
docker logs --tail 50 my-nginx
```

---

Logs với timestamp:

```bash
docker logs -t my-nginx
```

---

## Exec vào container

Mở shell:

```bash
docker exec -it my-nginx sh
```

---

Chạy lệnh nhanh:

```bash
docker exec my-nginx cat /etc/nginx/nginx.conf
```

---

Nếu container có bash:

```bash
docker exec -it container-name bash
```

---

## Inspect container

```bash
docker inspect my-nginx
```

---

Lấy IP container:

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

Volumes giúp **data không bị mất khi container xoá**.

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

## Quản lý volumes

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

### Khi nào dùng gì

| Type         | Use case        |
| ------------ | --------------- |
| Named volume | database data   |
| Bind mount   | source code dev |

---

