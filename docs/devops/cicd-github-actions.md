# CI/CD - GitHub Actions

Trang này là mục lục cho cụm bài CI/CD. Nội dung đã được tách ra để người học đi từ khái niệm và
quy tắc team, sang implementation cho Node/Python, rồi đến release và debugging.

---

## Mục tiêu

Sau cụm bài này, bạn có thể:

- hiểu CI/CD và vai trò của nó trong quy trình PR
- viết workflow cơ bản cho Node.js và Python
- quản lý secrets, matrix build và release workflow
- debug workflow khi fail

---

## Prerequisites

- Đã học: [GitHub Workflow](../vcs/github-workflow.md)
- Đã biết Docker cơ bản nếu cần build image: [Docker cơ bản](../containers/docker.md)

---

## Lộ trình học

1. [CI/CD Fundamentals](ci-basics.md)
2. [CI Cho Node.js Và Python](ci-node-python.md)
3. [Secrets, Release Và Debug Workflow](ci-release-debug.md)

---

## Gợi ý học

- Không nên học release pipeline trước khi đã chạy được workflow tối thiểu
- Tự tạo một repo demo nhỏ để tập `pull_request -> lint -> test -> build`
- Chỉ đưa thêm Docker release sau khi đã ổn định pipeline cơ bản

---

## Tài liệu liên quan

- [Deployment co ban](deployment-basics.md)
- [Bao mat co ban](security-basics.md)
- [GitHub Workflow](../vcs/github-workflow.md)
