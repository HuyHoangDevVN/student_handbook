# Checklist sinh viên mới

Checklist này không phải để bạn tick cho vui. Nó được viết để giúp bạn không bỏ sót những việc quan trọng khi chuẩn bị đi thực tập, khi mới vào team, và khi bắt đầu nhận task thật.

---

## Mục tiêu

Sau trang này, bạn biết:

- cần chuẩn bị gì trước khi vào team
- ngày đầu tiên nên ưu tiên việc gì
- task đầu tiên cần tự kiểm tra những điểm nào
- khi nào nên hỏi mentor thay vì tự loay hoay quá lâu

---

## 1. Trước khi vào team

### Tài khoản và truy cập

- [ ] Có tài khoản GitHub dùng tên thật hoặc dễ nhận diện rõ ràng
- [ ] Bật **2FA** cho GitHub
- [ ] Có SSH key hoặc đã biết đăng nhập bằng HTTPS

### Công cụ tối thiểu

- [ ] Git chạy được
- [ ] Docker chạy được
- [ ] VS Code hoặc editor chính đã sẵn sàng
- [ ] Đã đọc [Quickstart](quickstart.md)

### Tự xác minh môi trường

- [ ] `git --version` chạy được
- [ ] `docker --version` chạy được
- [ ] `docker compose version` chạy được
- [ ] Chạy được PostgreSQL stack mẫu cho InternHub

---

## 2. Trong ngày đầu tiên

### Hiểu bối cảnh trước khi sửa code

- [ ] Đọc [Start Here](start-here.md)
- [ ] Đọc [Sample Project: InternHub API](sample-project.md)
- [ ] Biết repo này đang mô tả case study nào
- [ ] Biết mình đang ở phần nào của handbook: setup, Git, DB, API, Docker hay debug

### Hiểu workflow team

- [ ] Biết branch naming convention
- [ ] Biết cách mở Pull Request
- [ ] Biết CI có phải điều kiện bắt buộc trước khi merge không
- [ ] Biết khi nào cần ping mentor/teammate

### Ghi chú local

- [ ] Tạo file ghi chú riêng (`notes.md` hoặc app notes của bạn)
- [ ] Ghi lại command setup, port đang dùng, env biến quan trọng
- [ ] Ghi lại lỗi đã gặp và cách fix

---

## 3. Khi nhận task đầu tiên

### Trước khi code

- [ ] Đọc yêu cầu và có thể nói lại task bằng lời của mình
- [ ] Xác định done criteria có gì: output, API, query, test, UI, docs
- [ ] Biết task này liên quan đến phần nào của InternHub

### Trong khi làm

- [ ] Làm trên branch riêng
- [ ] Commit nhỏ, nội dung rõ ràng
- [ ] Tự chạy lại command / test / query liên quan
- [ ] Nếu gặp lỗi, thử reproduce và ghi lại các bước

### Trước khi mở PR

- [ ] Tự review lại thay đổi của mình
- [ ] Xóa debug log thừa
- [ ] Cập nhật docs nếu workflow thay đổi
- [ ] Viết mô tả PR rõ ràng: đã đổi gì, test gì, cần reviewer check gì

---

## 4. Khi nào cần hỏi mentor

Bạn nên hỏi sớm nếu gặp một trong các dấu hiệu sau:

- Bạn không hiểu task đang yêu cầu đầu ra gì
- Bạn không biết phần nào của hệ thống bị ảnh hưởng
- Bạn đã thử reproduce và debug nhưng vẫn không xác định được nguyên nhân
- Bạn sắp chạy lệnh phá hủy mà không chắc tác dụng
- Bạn không biết review comment đang yêu cầu sửa logic hay chỉ style

---

## 5. Tài liệu nên đọc tiếp theo theo tình huống

| Tình huống | Tài liệu nên đọc |
| --- | --- |
| Chưa quen command line | [Terminal & Shell](../environment/terminal.md) |
| Sắp tạo PR đầu tiên | [GitHub Workflow](../vcs/github-workflow.md) |
| Bắt đầu làm việc với DB | [SQL & PostgreSQL](../databases/sql-postgres.md) |
| Cần chạy stack local | [Docker Compose](../containers/docker-compose.md) |
| Gặp lỗi local / Docker / Git | [Lỗi thường gặp](../troubleshooting/common-errors.md) |

---

## Definition of done cho giai đoạn onboard

Bạn có thể coi mình đã đạt mức tối thiểu khi:

- [ ] setup được môi trường local
- [ ] đọc được README và biết handbook này dùng để làm gì
- [ ] biết `InternHub API` là case study xuyên suốt
- [ ] tạo được branch và mở được PR nhỏ
- [ ] gọi được một API hoặc chạy được một query có kết quả rõ ràng
- [ ] biết mở phần troubleshooting và tự kiểm tra trước khi hỏi

---

## Bước tiếp theo

- Nếu bạn chưa setup máy: quay lại [Quickstart](quickstart.md)
- Nếu bạn muốn hiểu dự án mẫu: đọc [Sample Project: InternHub API](sample-project.md)
- Nếu bạn sắp vào workflow team: đọc [GitHub Workflow](../vcs/github-workflow.md)
