# Logging & Monitoring

## Má»¥c tiĂªu

Sau bĂ i nĂ y, báº¡n sáº½:

- Hiá»ƒu log levels vĂ  cĂ¡ch sá»­ dá»¥ng Ä‘Ăºng.
- Viáº¿t log cĂ³ cáº¥u trĂºc (structured logging).
- Giá»›i thiá»‡u stack monitoring: **Prometheus + Grafana**.
- Setup monitoring cÆ¡ báº£n báº±ng Docker Compose.

## Prerequisites

- [Docker Compose](../containers/docker-compose.md).

---

## Log Levels

| Level   | Khi nĂ o dĂ¹ng                          | VĂ­ dá»¥                                          |
| ------- | ------------------------------------- | ---------------------------------------------- |
| `DEBUG` | Chi tiáº¿t cho dev, khĂ´ng báº­t trĂªn prod | `DEBUG: Query result: {rows: 42}`              |
| `INFO`  | Sá»± kiá»‡n bĂ¬nh thÆ°á»ng                   | `INFO: Server started on port 3000`            |
| `WARN`  | Váº¥n Ä‘á» tiá»m áº©n, chÆ°a lá»—i              | `WARN: Disk usage at 85%`                      |
| `ERROR` | Lá»—i nhÆ°ng app váº«n cháº¡y                | `ERROR: Failed to send email to user@test.com` |
| `FATAL` | Lá»—i nghiĂªm trá»ng, app pháº£i dá»«ng       | `FATAL: Database connection failed`            |

!!! warning "Quy táº¯c" - **Production**: chá»‰ báº­t `INFO` trá»Ÿ lĂªn. - **Development**: báº­t `DEBUG`. - **KHĂ”NG** log sensitive data (password, token, PII).

---

## Structured Logging

### âŒ Log khĂ´ng tá»‘t

```
Error occurred while processing request
Something went wrong
User login failed
```

### âœ… Log cĂ³ cáº¥u trĂºc

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

### VĂ­ dá»¥ code

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

# Logs táº¥t cáº£ services (Compose)
docker compose logs -f

# Xem logs service cá»¥ thá»ƒ
docker compose logs -f web
```

---

## Prometheus + Grafana (Giá»›i thiá»‡u)

```mermaid
graph LR
    A[Your App] -->|metrics endpoint| B[Prometheus]
    B -->|query| C[Grafana]
    C -->|dashboard| D[You đŸ‘€]
```

| Tool              | Vai trĂ²                                        |
| ----------------- | ---------------------------------------------- |
| **Prometheus**    | Thu tháº­p metrics (CPU, memory, request countâ€¦) |
| **Grafana**       | Hiá»ƒn thá»‹ dashboard Ä‘áº¹p máº¯t                     |
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

### File cáº¥u hĂ¬nh Prometheus

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
# Cháº¡y stack monitoring
docker compose -f docker-compose.monitoring.yml up -d

# Truy cáº­p
# Prometheus: http://localhost:9090
# Grafana:    http://localhost:3001 (admin/admin)
```

---

## Metrics cÆ¡ báº£n cáº§n theo dĂµi

| Metric             | Ă nghÄ©a                        |
| ------------------ | ------------------------------ |
| **Request rate**   | Sá»‘ request / giĂ¢y              |
| **Error rate**     | % request lá»—i (4xx, 5xx)       |
| **Response time**  | Latency trung bĂ¬nh / P95 / P99 |
| **CPU usage**      | % CPU sá»­ dá»¥ng                  |
| **Memory usage**   | RAM sá»­ dá»¥ng                    |
| **Disk usage**     | Dung lÆ°á»£ng disk                |
| **DB connections** | Sá»‘ connection pool             |

---

## Lá»—i thÆ°á»ng gáº·p

| Lá»—i                      | NguyĂªn nhĂ¢n                 | CĂ¡ch sá»­a                            |
| ------------------------ | --------------------------- | ----------------------------------- |
| Log quĂ¡ nhiá»u â†’ disk Ä‘áº§y | Log level DEBUG trĂªn prod   | Äá»•i sang INFO, thĂªm log rotation    |
| Grafana khĂ´ng hiá»‡n data  | Prometheus chÆ°a scrape Ä‘Æ°á»£c | Kiá»ƒm tra target trong Prometheus UI |
| Metrics endpoint 404     | App chÆ°a expose /metrics    | ThĂªm metrics middleware             |

---

## TĂ i liá»‡u tham kháº£o

- [Prometheus Docs](https://prometheus.io/docs/)
- [Grafana Docs](https://grafana.com/docs/)
- [The Twelve-Factor App â€“ Logs](https://12factor.net/logs)
