# 📘 Student IT Handbook

> Tài liệu hướng dẫn thực hành IT dành cho sinh viên thực tập và đi làm.
> Xây dựng bằng [MkDocs](https://www.mkdocs.org/) + [Material theme](https://squidfunk.github.io/mkdocs-material/).

---

## Mục lục

- [Yêu cầu hệ thống](#yêu-cầu-hệ-thống)
- [Cài đặt & Build local](#cài-đặt--build-local)
- [Deploy GitHub Pages](#deploy-github-pages)
- [Export PDF offline](#export-pdf-offline)
- [Style Guide – Quy ước viết docs](#style-guide--quy-ước-viết-docs)
- [Đóng góp](#đóng-góp)

---

## Yêu cầu hệ thống

| Công cụ         | Phiên bản tối thiểu | Ghi chú                |
| --------------- | ------------------- | ---------------------- |
| Python          | 3.9+                | Khuyên dùng 3.11+      |
| pip             | 23+                 | Đi kèm Python          |
| Git             | 2.30+               |                        |
| WeasyPrint deps | —                   | Chỉ cần khi export PDF |

---

## Cài đặt & Build local

### 1. Clone repo

```bash
git clone https://github.com/<github-org>/student-it-handbook.git
cd student-it-handbook
```

Thay `<github-org>` bằng GitHub organization hoặc username thực tế.

### 2. Tạo virtual environment (khuyên dùng)

```bash
# Tạo venv
python -m venv .venv

# Kích hoạt
# Linux / macOS
source .venv/bin/activate

# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
```

### 3. Cài dependencies

```bash
pip install -r requirements.txt
```

### 4. Chạy dev server

```bash
mkdocs serve
```

Truy cập [http://127.0.0.1:8000](http://127.0.0.1:8000) để xem docs.

### 5. Build static site

```bash
mkdocs build
```

Output nằm trong folder `site/`.

---

## Deploy GitHub Pages

### Cách 1 – Lệnh thủ công

```bash
mkdocs gh-deploy --force
```

Lệnh này sẽ build và push vào branch `gh-pages`.

### Cách 2 – GitHub Actions (tự động)

Tạo file `.github/workflows/docs.yml`:

```yaml
name: Deploy Docs

on:
  push:
    branches: [main]

permissions:
  contents: write

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -r requirements.txt
      - run: mkdocs gh-deploy --force
```

Sau khi push, vào **Settings → Pages → Source: Deploy from a branch → `gh-pages`**.

---

## Export PDF offline

Handbook dùng cấu hình riêng `mkdocs-pdf.yml` để export PDF. Cách này giữ cho
luồng `mkdocs serve` và `mkdocs build` hằng ngày vẫn nhẹ, đồng thời tách riêng
phần phụ thuộc native của WeasyPrint.

### Cài đặt WeasyPrint (dependency của plugin)

=== "Ubuntu / Debian"

```bash
sudo apt install -y libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 \
  libffi-dev libcairo2 libgirepository1.0-dev
```

=== "macOS"

```bash
brew install pango gdk-pixbuf libffi cairo gobject-introspection
```

=== "Windows"

```
# Cách dễ nhất: dùng WSL (Ubuntu) rồi làm theo bước Ubuntu.
# Hoặc cài GTK3 runtime: https://github.com/nickvdyck/weasyprint-win
```

### Build PDF

```bash
# Linux / macOS
ENABLE_PDF_EXPORT=1 mkdocs build --strict -f mkdocs-pdf.yml

# Windows (PowerShell)
./scripts/export-pdf.ps1
```

File PDF sẽ được tạo tại: **`site/pdf/student-it-handbook.pdf`**

> **Tip:** Nếu build PDF trên Windows bị lỗi GTK/Pango, hãy dùng WSL/Ubuntu
> hoặc GitHub Actions workflow `pdf-handbook.yml` để lấy artifact PDF.

---

## Style Guide – Quy ước viết docs

### 1. Tiêu đề

- H1 (`#`) – Chỉ **1 lần** đầu mỗi trang, là tên chủ đề.
- H2 (`##`) – Các phần chính.
- H3 (`###`) – Phần con.
- **Không dùng** H4 trở xuống nếu không cần thiết.

### 2. Code block

- Luôn ghi **ngôn ngữ** sau triple backtick:

````markdown
```bash
docker ps
```

```sql
SELECT * FROM users WHERE active = true;
```

```json
{ "name": "example" }
```
````

- Với lệnh terminal: dùng `bash` (không dùng `shell` hay `console`).
- Nếu lệnh khác nhau giữa OS, dùng **tab** (pymdownx.tabbed):

````markdown
=== "Linux / macOS"
`bash
    source .venv/bin/activate
    `

=== "Windows"
`powershell
    .\.venv\Scripts\Activate.ps1
    `
````

### 3. Admonitions

```markdown
!!! tip "Mẹo"
Nội dung mẹo ở đây.

!!! warning "Cảnh báo"
Nội dung cảnh báo.

!!! danger "Nguy hiểm"
Không bao giờ commit secret lên repo!

!!! note "Ghi chú"
Thông tin bổ sung.
```

### 4. Screenshot & Diagram

- Đặt ảnh trong `docs/assets/images/<section>/`.
- Đặt tên có nghĩa: `git-branch-workflow.png`, **không** dùng `img1.png`.
- Dùng Mermaid cho sơ đồ đơn giản (đã tích hợp trong config).
- Kích thước ảnh: tối đa **800px** chiều rộng.

### 5. Quy tắc "1 trang = 1 kỹ năng"

- Mỗi file `.md` chỉ nên dạy **một kỹ năng cụ thể**.
- Nếu nội dung dài hơn 5 màn hình, hãy **tách** thành nhiều trang.

### 6. Cấu trúc mỗi trang

```markdown
# Tiêu đề kỹ năng

## Mục tiêu

Sau bài này, bạn sẽ:

- …
- …

## Prerequisites

- Đã hoàn thành: [Tên bài trước](link)
- Đã cài: …

## Nội dung chính

### Bước 1 – …

### Bước 2 – …

## Lỗi thường gặp

| Lỗi | Nguyên nhân | Cách sửa |
| --- | ----------- | -------- |
| …   | …           | …        |

## Bài tập

1. …

## Tài liệu tham khảo

- [Link](url)
```

### 7. Version & Changelog

- Mỗi release ghi rõ phiên bản trong `mkdocs.yml` → `extra.version`.
- Cập nhật `CHANGELOG.md` (nếu có) khi thêm/sửa chương.

---

## Đóng góp

1. Fork repo.
2. Tạo branch: `docs/<tên-chủ-đề>`.
3. Viết / sửa nội dung theo style guide ở trên.
4. Chạy `mkdocs serve` để kiểm tra local.
5. Tạo Pull Request, ghi mô tả rõ ràng.

---

## License

MIT License – Xem file [LICENSE](LICENSE).
