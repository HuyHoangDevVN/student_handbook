# Deployment cơ bản

Trang này giới thiệu deployment ở mức onboarding: hiểu staging/prod, hiểu pre-deploy và post-deploy verification, và hiểu rollback ở mức tư duy. Nó không cố gắng thay thế runbook nội bộ của từng công ty.

---

## Mục tiêu

Sau bài này, bạn cần hiểu:

- khác nhau gì giữa local, staging và production
- deploy lên VPS/PaaS ở mức cơ bản diễn ra như thế nào
- cần kiểm tra gì trước và sau deploy
- rollback đúng lúc và đúng cách quan trọng thế nào

---

## Khi nào bạn cần phần này

- Bạn sắp nghe team nói về staging, prod, smoke test.
- Bạn đã học Docker/CI và muốn biết luồng deploy cơ bản.
- Bạn muốn hiểu production mindset trước khi động vào hệ thống thật.

---

## Prerequisites

- [Docker cơ bản](../containers/docker.md)
- [CI/CD - GitHub Actions](cicd-github-actions.md)

---

## Môi trường deploy

| Môi trường | Mục đích | Ai thường dùng |
| --- | --- | --- |
| Development | code và test local | developer |
| Staging | verify trước khi lên production | team, QA |
| Production | phục vụ người dùng thật | end users |

### Nguyên tắc quan trọng

Staging càng giống production thì deploy càng ít bất ngờ.

---

## Luồng deploy cơ bản

```text
Code merged -> CI xanh -> Build artifact/image -> Deploy staging -> Smoke test -> Approve -> Deploy production
```

Nếu handbook đang dùng case study `InternHub API`, bạn có thể hình dung:

- image: `internhub-api:<tag>`
- app cần database và env biến đúng
- sau deploy cần verify endpoint chính, logs và metrics

---

## Ví dụ deploy lên VPS

```bash
ssh user@your-server-ip
git clone https://github.com/<github-org>/internhub-api.git
cd internhub-api
cp .env.example .env
docker compose -f docker-compose.prod.yml up -d
```

### Lưu ý

Ví dụ trên chỉ để minh họa luồng thao tác. Repo handbook hiện không đóng gói sample app production-ready. Mục tiêu là hiểu:

- artifact đến từ đâu
- env nằm ở đâu
- lệnh deploy đang làm gì

---

## Reverse proxy ở mức tối thiểu

```nginx
server {
    listen 80;
    server_name api.internhub.local;

    location / {
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Bạn cần nhớ:

- app có thể chạy trên port nội bộ
- reverse proxy tiếp nhận request công khai
- HTTPS thường được xử lý tại proxy/load balancer

---

## Pre-deploy checklist

- [ ] CI xanh
- [ ] Biết artifact/image nào sẽ được deploy
- [ ] Env biến đã được xác nhận
- [ ] Migration, nếu có, đã được đánh giá tác động
- [ ] Có kế hoạch rollback
- [ ] Biết ai là người xác nhận deploy

---

## Post-deploy verification

Sau deploy, không được coi là xong chỉ vì container đã lên.

Cần kiểm tra tối thiểu:

- [ ] Service đang chạy
- [ ] Health endpoint trả kết quả đúng
- [ ] Endpoint chính không trả 5xx
- [ ] Log không có spike lỗi rõ ràng
- [ ] Metric có dấu hiệu bình thường tối thiểu

### Smoke test gợi ý

```bash
curl -v http://localhost:3000/health
curl -v http://localhost:3000/api/users
```

### Expected result

- health endpoint pass
- endpoint chính trả response hợp lệ
- không thấy log lỗi liên tục sau deploy

---

## Rollback mindset

Rollback không phải là đầu hàng. Rollback là cách đưa hệ thống về trạng thái an toàn khi deploy mới có dấu hiệu gây lỗi.

### Khi nào cần nghĩ đến rollback

- endpoint chính 5xx ngay sau deploy
- smoke test fail
- logs lỗi tăng mạnh
- metrics xấu rõ ràng và không tìm được cách fix nhanh

### Ví dụ rollback bằng image tag cũ

```bash
# Trong docker-compose.yml
# image: internhub-api:v1.2.0

docker compose up -d
```

### Guardrail

- Không rollback mù trong production nếu chưa xác nhận symptom thật
- Ghi lại lý do rollback và version đã rollback
- Sau rollback vẫn phải verify lại hệ thống

---

## Safe vs risky thao tác

### Tương đối an toàn ở local/staging

- kiểm tra logs
- curl health endpoint
- restart service khi đã hiểu lý do

### Cần thận trọng

- chạy migration
- đổi env biến production
- deploy image mới trong giờ cao điểm

### Không được làm nếu chưa được hướng dẫn

- sửa trực tiếp database production
- xóa data để “thử xem có hết lỗi không”
- restart hệ thống production hàng loạt khi chưa có người xác nhận

---

## Bước tiếp theo

- Đọc [Logging & Monitoring](logging-monitoring.md) để hiểu cần xem gì sau deploy
- Đọc [Bảo mật cơ bản](security-basics.md) để biết env và secrets cần được quản lý thế nào
- Đọc [Lỗi thường gặp](../troubleshooting/common-errors.md) để biết cách xử lý local trước khi nghĩ đến production
