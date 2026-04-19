# Checklist sinh viên mới

Checklist này giúp bạn kiểm tra xem mình đã **sẵn sàng tham gia vào một team phát triển phần mềm** hay chưa.

Danh sách được chia thành 3 giai đoạn:

- Trước ngày đầu tiên
- Ngày đầu tiên
- Tuần đầu tiên

---

## Trước ngày đầu tiên

Hãy hoàn thành các bước sau trước khi bắt đầu internship hoặc dự án.

### Tài khoản & truy cập

- [ ] Tạo tài khoản **GitHub**
- [ ] Bật **Two-Factor Authentication (2FA)** cho GitHub
- [ ] Cài đặt **SSH key** cho GitHub (khuyến nghị)

---

### Công cụ phát triển

- [ ] Cài đặt **Git**
- [ ] Cấu hình `user.name` và `user.email`
- [ ] Cài đặt **Docker Desktop**
- [ ] Cài đặt **VS Code**

Extensions nên cài:

- GitLens
- Docker
- Python
- ESLint / Prettier

---

### Môi trường lập trình

- [ ] Cài **Python 3.11+** hoặc **Anaconda**
- [ ] Cài **Node.js 20+** (nếu dự án sử dụng)
- [ ] Kiểm tra các lệnh sau chạy được:

```bash
git --version
docker --version
python --version
node --version
```

---

### Đọc tài liệu

- [ ] Đọc phần **Quickstart**
- [ ] Hiểu cách **clone repo và chạy project**

---

## Ngày đầu tiên

Mục tiêu của ngày đầu tiên là **setup môi trường và hiểu workflow của team**.

### Truy cập hệ thống

- [ ] Nhận invite vào **GitHub Organization**
- [ ] Nhận quyền truy cập repository

---

### Setup dự án

- [ ] Clone repository chính

```bash
git clone <repo-url>
```

- [ ] Chạy được project trên local

Ví dụ:

```bash
docker compose up
```

---

### Kiểm tra workflow Git

Tạo branch test:

```bash
git checkout -b feature/your-name-hello
```

Sau đó:

- [ ] Commit thay đổi
- [ ] Push branch
- [ ] Tạo Pull Request

---

### Làm quen với team

- [ ] Gặp **mentor / tech lead**
- [ ] Hỏi về **workflow code review**
- [ ] Hỏi về **quy trình deploy**

---

## Tuần đầu tiên

Trong tuần đầu, mục tiêu là **hiểu codebase và workflow làm việc**.

### Hiểu dự án

- [ ] Hiểu cấu trúc folder
- [ ] Đọc `README.md`
- [ ] Đọc `CONTRIBUTING.md`

---

### Chạy test

- [ ] Chạy test suite

Ví dụ:

```bash
npm test
```

hoặc

```bash
pytest
```

---

### Hoàn thành task đầu tiên

Một task nhỏ có thể là:

- sửa typo
- cập nhật documentation
- fix bug nhỏ

Mục tiêu: **hoàn thành ít nhất 1 Pull Request**.

---

### Tham gia hoạt động của team

- [ ] Tham gia **daily standup**
- [ ] Theo dõi **issue tracker**
- [ ] Hiểu **task board (Jira / GitHub Projects)**

---

## Kỹ năng cần nắm trong tháng đầu

| Kỹ năng          | Mục tiêu             | Tài liệu                                               |
| ---------------- | -------------------- | ------------------------------------------------------ |
| Terminal / Shell | Sử dụng thành thạo   | [Terminal](../environment/terminal.md)                 |
| Git branching    | Hiểu workflow branch | [Git](../vcs/git-basics.md)                            |
| Docker           | Chạy container       | [Docker](../containers/docker.md)                      |
| SQL cơ bản       | Viết query           | [SQL](../databases/sql-postgres.md)                    |
| Debug & logs     | Tìm lỗi cơ bản       | [Troubleshooting](../troubleshooting/common-errors.md) |

---

## Mẹo cho ngày đầu

!!! tip "Lời khuyên"
Đừng ngại hỏi khi chưa hiểu.
Ghi chép lại các hướng dẫn của mentor.

Bạn nên tạo một file riêng:

```bash
notes.md
```

để ghi lại:

- các lệnh thường dùng
- workflow của team
- các lỗi thường gặp
