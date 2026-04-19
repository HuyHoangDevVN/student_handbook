# Lỗi thường gặp & Cách xử lý

Trang này không chỉ liệt kê error message. Mục tiêu của nó là giúp bạn debug có hệ thống và tránh thao tác phá hủy khi chưa hiểu vấn đề.

---

## Mục tiêu

Sau trang này, bạn cần:

- biết đọc lỗi theo nhóm vấn đề
- biết bắt đầu debug từ đâu
- biết lệnh nào an toàn, lệnh nào cần thận trọng
- biết khi nào cần hỏi mentor/teammate

---

## Quy tắc debug chung

1. Đọc kỹ error message.
2. Xác định đang lỗi gì: Git, Docker, DB, network, Python, CI.
3. Reproduce bằng bước ngắn nhất có thể.
4. Kiểm tra log, process, port, env.
5. Chỉ chạy lệnh phá hủy khi đã biết tại sao mình cần chạy nó.

---

## Nhãn mức độ lệnh

### An toàn

- đọc log
- xem process
- chạy lệnh kiểm tra kết nối
- chạy `SELECT 1;`

### Cần thận trọng

- `git rebase`
- `docker compose down`
- `docker compose down -v`
- xóa cache dependency

### Phá hủy / cảnh báo cao

- `git reset --hard`
- `git checkout -- .`
- `docker system prune -a --volumes`
- xóa volume/data mà chưa backup

Nếu bạn chưa hiểu tác dụng, dừng lại và hỏi mentor/teammate.

---

## Git

| Lỗi | Nguyên nhân thường gặp | Cách xử lý an toàn |
| --- | --- | --- |
| `fatal: not a git repository` | Sai thư mục | `cd` đúng repo, kiểm tra có `.git` không |
| `failed to push some refs` | Remote mới hơn local | `git pull --rebase origin main`, đọc conflict nếu có |
| `CONFLICT` khi merge/rebase | Hai thay đổi cùng chạm một chỗ | Đọc file conflict, sửa thủ công, commit tiếp |
| `Permission denied (publickey)` | SSH key chưa setup | Kiểm tra auth với GitHub |

### Guardrail

- Không dùng `git checkout -- .` để “cho nhanh” nếu bạn chưa chắc sẽ mất gì.
- Không dùng `git reset --hard` trên branch có thay đổi chưa backup.
- Trước lệnh rewrite history, chạy `git status` và `git log --oneline -5`.

---

## Docker

| Lỗi | Nguyên nhân thường gặp | Cách xử lý an toàn |
| --- | --- | --- |
| `Cannot connect to the Docker daemon` | Docker Desktop/service chưa chạy | Mở Docker Desktop hoặc start service |
| `port is already allocated` | Port đang bị chiếm | `docker ps`, kiểm tra process đang dùng port |
| Container exit ngay | CMD/ENTRYPOINT lỗi | `docker logs <name>` |
| `depends on ... not healthy` | Service phụ thuộc chưa ready | kiểm tra healthcheck và logs của DB/cache |

### Guardrail

- `docker compose down -v` sẽ xóa volume và có thể mất data local.
- `docker system prune -a --volumes` chỉ dùng khi bạn hiểu rõ mình đang mất cái gì.
- Trước khi dọn dẹp Docker, ưu tiên `docker system df` để biết cái gì đang tốn disk.

---

## Python / Environment

| Lỗi | Nguyên nhân thường gặp | Cách xử lý |
| --- | --- | --- |
| `ModuleNotFoundError` | Sai env hoặc thiếu package | kiểm tra env đang active, cài đúng package |
| `command not found: python` | Python chưa cài / alias sai | thử `python3`, kiểm tra PATH |
| `pip install` bị permission denied | Đang cài global | dùng virtualenv |
| `UnicodeDecodeError` | Encoding file không đúng | mở file với UTF-8 và kiểm tra encoding |

### Lệnh kiểm tra hữu ích

```bash
python --version
pip list
echo $VIRTUAL_ENV
echo $CONDA_DEFAULT_ENV
```

---

## Database (PostgreSQL)

| Lỗi | Nguyên nhân thường gặp | Cách xử lý |
| --- | --- | --- |
| `Connection refused` | DB chưa lên | kiểm tra container/process database |
| `password authentication failed` | Sai user/password/env | đối chiếu env và connection string |
| `relation does not exist` | Chưa tạo bảng hoặc chưa load schema | chạy schema/migration |
| `duplicate key` | Dữ liệu trùng unique constraint | kiểm tra data trước khi insert |

### Lệnh verify cơ bản

```bash
docker ps
docker exec -it postgres-dev psql -U dev -d internhub -c "SELECT 1;"
```

---

## Network / API

| Lỗi | Nguyên nhân thường gặp | Cách xử lý |
| --- | --- | --- |
| `ECONNREFUSED` | App chưa chạy hoặc sai port | kiểm tra service, process, port |
| `404 Not Found` | Sai endpoint | đối chiếu path và method |
| `401 Unauthorized` | Thiếu token / token sai | kiểm tra header |
| `ETIMEDOUT` | Service chậm hoặc không reach được | kiểm tra network, DNS, firewall |

### Lệnh verify cơ bản

```bash
curl -v http://localhost:3000/health
curl -v http://localhost:3000/api/users
```

---

## WSL / Windows

| Lỗi | Nguyên nhân thường gặp | Cách xử lý |
| --- | --- | --- |
| WSL rất chậm | Project nằm trong `/mnt/c/` | đưa project vào filesystem của WSL |
| Docker không chạy trong WSL | Chưa bật integration | bật WSL integration trong Docker Desktop |
| `chmod` không có tác dụng | Làm việc trên filesystem Windows | thao tác trong WSL filesystem |

---

## Quy trình debug gợi ý

```text
Gặp lỗi
-> đọc message
-> xác định nhóm vấn đề
-> reproduce
-> xem log / port / process / env
-> fix
-> verify lại
-> ghi chú
```

### Khi nào cần hỏi người khác

- Bạn đã reproduce được nhưng không xác định được nguyên nhân
- Bạn sắp dùng lệnh phá hủy
- Bạn nghĩ lỗi đến từ env chia sẻ, CI, staging hoặc production
- Bạn không chắc done criteria của fix là gì

---

## Bước tiếp theo

- Đọc [Docker Compose](../containers/docker-compose.md) nếu bạn thường gặp lỗi stack local
- Đọc [GitHub Workflow](../vcs/github-workflow.md) nếu vấn đề nằm ở branch/PR/review
- Đọc [Logging & Monitoring](../devops/logging-monitoring.md) nếu muốn chuyển từ debug local sang tư duy vận hành
