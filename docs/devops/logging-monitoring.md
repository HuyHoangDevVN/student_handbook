# Logging & Monitoring

## Mục tiêu

Sau bài này, bạn sẽ:

- Hiểu log levels và cách sử dụng đúng.
- Viết log có cấu trúc (structured logging).
- Giới thiệu stack monitoring: **Prometheus + Grafana**.
- Setup monitoring cơ bản bằng Docker Compose.

## Prerequisites

- [Docker Compose](../containers/docker-compose.md).

---

## Log Levels

| Level   | Khi nào dùng                          | Ví dụ                                          |
| ------- | ------------------------------------- | ---------------------------------------------- |
| `DEBUG` | Chi tiết cho dev, không bật trên prod | `DEBUG: Query result: {rows: 42}`              |
| `INFO`  | Sự kiện bình thường                   | `INFO: Server started on port 3000`            |
| `WARN`  | Vấn đề tiềm ẩn, chưa lỗi              | `WARN: Disk usage at 85%`                      |
| `ERROR` | Lỗi nhưng app vẫn chạy                | `ERROR: Failed to send email to user@test.com` |
| `FATAL` | Lỗi nghiêm trọng, app phải dừng       | `FATAL: Database connection failed`            |

!!! warning "Quy tắc" - **Production**: chỉ bật `INFO` trở lên. - **Development**: bật `DEBUG`. - **KHÔNG** log sensitive data (password, token, PII).

---

## Structured Logging

### âŒ Log không tốt

```
Error occurred while processing request
Something went wrong
User login failed
```

### ✅ Log có cấu trúc

```json
{
  "timestamp": "2025-01-15T10:30:00Z",
  "level": "ERROR",
  "message": "User login failed",
  "userId": "user_123",
  "reason": "invalid_password",
  "ip": "192.168.1.100",
  "requestId": "req_abc456"
}
```

### Ví dụ code

=== "Python"
```python
import logging
import json

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s'
    )
    logger = logging.getLogger(__name__)

    logger.info("User logged in", extra={"userId": "user_123"})
    logger.error("Database connection failed", exc_info=True)
    ```

=== "Node.js (winston)"
```javascript
const winston = require('winston');

    const logger = winston.createLogger({
      level: 'info',
      format: winston.format.json(),
      transports: [
        new winston.transports.Console(),
        new winston.transports.File({ filename: 'app.log' })
      ]
    });

    logger.info('User logged in', { userId: 'user_123' });
    logger.error('Database connection failed', { error: err.message });
    ```

---

## Docker Logs

```bash
# Xem logs container
docker logs internhub-api
docker logs -f --tail 100 internhub-api

# Logs tất cả services (Compose)
docker compose logs -f

# Xem logs service cụ thể
docker compose logs -f web
```

---

## Prometheus + Grafana (Giới thiệu)

```mermaid
graph LR
    A[Your App] -->|metrics endpoint| B[Prometheus]
    B -->|query| C[Grafana]
    C -->|dashboard| D[You đŸ‘€]
```

| Tool              | Vai trò                                        |
| ----------------- | ---------------------------------------------- |
| **Prometheus**    | Thu thập metrics (CPU, memory, request count…) |
| **Grafana**       | Hiển thị dashboard đẹp mắt                     |
| **Node Exporter** | Expose system metrics                          |

### Docker Compose cho Monitoring Stack

```yaml
# docker-compose.monitoring.yml
services:
  prometheus:
    image: prom/prometheus:latest
    ports:
      - "9090:9090"
    volumes:
      - ./monitoring/prometheus.yml:/etc/prometheus/prometheus.yml
    command:
      - "--config.file=/etc/prometheus/prometheus.yml"

  grafana:
    image: grafana/grafana:latest
    ports:
      - "3001:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
    volumes:
      - grafana-data:/var/lib/grafana
    depends_on:
      - prometheus

  node-exporter:
    image: prom/node-exporter:latest
    ports:
      - "9100:9100"

volumes:
  grafana-data:
```

### File cấu hình Prometheus

```yaml
# monitoring/prometheus.yml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: "node-exporter"
    static_configs:
      - targets: ["node-exporter:9100"]

  - job_name: "internhub-api"
    static_configs:
      - targets: ["web:3000"]
    metrics_path: /metrics
```

```bash
# Chạy stack monitoring
docker compose -f docker-compose.monitoring.yml up -d

# Truy cập
# Prometheus: http://localhost:9090
# Grafana:    http://localhost:3001 (admin/admin)
```

---

## Metrics cơ bản cần theo dõi

| Metric             | Ă nghĩa                        |
| ------------------ | ------------------------------ |
| **Request rate**   | Số request / giây              |
| **Error rate**     | % request lỗi (4xx, 5xx)       |
| **Response time**  | Latency trung bình / P95 / P99 |
| **CPU usage**      | % CPU sử dụng                  |
| **Memory usage**   | RAM sử dụng                    |
| **Disk usage**     | Dung lượng disk                |
| **DB connections** | Số connection pool             |

---

## Lỗi thường gặp

| Lỗi                      | Nguyên nhân                 | Cách sửa                            |
| ------------------------ | --------------------------- | ----------------------------------- |
| Log quá nhiều → disk đầy | Log level DEBUG trên prod   | Đổi sang INFO, thêm log rotation    |
| Grafana không hiện data  | Prometheus chưa scrape được | Kiểm tra target trong Prometheus UI |
| Metrics endpoint 404     | App chưa expose /metrics    | Thêm metrics middleware             |

---

## Tài liệu tham khảo

- [Prometheus Docs](https://prometheus.io/docs/)
- [Grafana Docs](https://grafana.com/docs/)
- [The Twelve-Factor App – Logs](https://12factor.net/logs)
