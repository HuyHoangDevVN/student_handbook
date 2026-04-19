# Student IT Handbook

> Ban PDF tong hop duoc tao tu toan bo handbook theo thu tu dieu huong chinh.
> File nay duoc generate tu `scripts/generate_pdf_bundle.py`. Khong sua truc tiep.

<!-- Source: getting-started/start-here.md -->

# Start Here

Trang này là điểm vào chính của handbook. Mục tiêu của nó là giúp bạn xác định:

- handbook này có phù hợp với mình không
- nên đọc phần nào trước
- khi gặp một tình huống cụ thể thì mở phần nào

---

## Handbook này dành cho ai

- Sinh viên sắp đi thực tập nhưng chưa từng làm việc trong repo thật.
- Người đã học lập trình nhưng chưa quen workflow team.
- Fresher cần một bộ tài liệu để hệ thống hóa local setup, Git, database, Docker, API, CI/CD và troubleshooting.

Nếu bạn đang tìm một curriculum dạy code từ đầu, handbook này không phải tài liệu chính. Nó phù hợp hơn với vai trò **onboarding companion + reference handbook**.

---

## Bạn sẽ dùng handbook này như thế nào

### Trước khi vào team

Đọc:

1. Quickstart
2. Checklist sinh viên mới
3. Sample Project: InternHub API

Mục tiêu:

- biết cần cài gì
- tự kiểm tra được môi trường của mình
- biết case study xuyên suốt là gì

### Khi mới vào repo hoặc nhận task đầu tiên

Đọc:

1. Terminal & Shell
2. Git cơ bản
3. GitHub Workflow

Mục tiêu:

- đọc được command line cần thiết
- biết tạo branch, commit, push, mở Pull Request
- biết khi nào cần hỏi mentor hoặc teammate

### Khi bắt đầu làm task backend

Đọc:

1. SQL & PostgreSQL
2. HTTP & REST API
3. API Testing
4. Docker Compose

Mục tiêu:

- hiểu data model
- gọi và test API
- chạy stack bằng Docker

### Khi cần tra cứu nhanh

Đọc:

- Lỗi thường gặp
- các phần trong `Cheat Sheets`

---

## Cách đọc để không bị ngợp

- Không cần đọc tất cả theo thứ tự một cách máy móc.
- Mở chapter overview để xác định bạn đang cần phần nào.
- Chỉ đi sâu vào chương con khi bạn đã biết lý do phải học nó.
- Sau mỗi bài, tự gõ lại command hoặc query thay vì chỉ đọc.

---

## Dấu hiệu bạn đang dùng handbook đúng cách

- Bạn biết phần nào là kiến thức nền, phần nào là tra cứu nhanh.
- Bạn có thể nói rõ mình đang gặp vấn đề gì: setup, Git, DB, API, Docker, deploy hay debug.
- Bạn không copy-paste lệnh phá hủy mà không hiểu tác dụng.
- Bạn biết cần đọc phần nào trước khi hỏi mentor.

---

## Bước tiếp theo

- Nếu bạn chưa setup máy: đọc Quickstart
- Nếu bạn đang chuẩn bị đi thực tập: đọc Checklist sinh viên mới
- Nếu bạn muốn hiểu bối cảnh kỹ thuật chung: đọc Sample Project: InternHub API


<div class="pdf-page-break"></div>

<!-- Source: getting-started/quickstart.md -->

# Quickstart

Quickstart này chỉ giải quyết một việc: giúp bạn có **môi trường tối thiểu** để đọc handbook và thực hành với case study `InternHub API`.

Nó không cố gắng dạy đầy đủ Git, Python, Node.js hay Docker. Các chương chi tiết nằm ở những phần sau.

---

## Mục tiêu

Sau bài này, bạn cần làm được 4 việc:

- kiểm tra máy đã có Git và Docker
- clone repo handbook
- chạy PostgreSQL stack mẫu cho InternHub API
- tự xác minh kết nối database thành công

---

## Khi nào bạn cần bài này

- Bạn sắp đi thực tập và muốn kiểm tra lại môi trường.
- Bạn mới vào repo và chưa chắc máy mình đã sẵn sàng.
- Bạn muốn chạy được resource mẫu trước khi học SQL, API hoặc Docker Compose.

---

## Prerequisites

Bạn cần:

- máy Windows 10/11, macOS 12+, hoặc Ubuntu 22.04+
- kết nối Internet
- quyền cài tool trên máy của mình

---

## 1. Kiểm tra Git

```bash
git --version
```

Nếu lệnh chạy thành công, Git đã sẵn sàng.

Nếu máy chưa có Git:

- Windows: `winget install Git.Git`
- macOS: `xcode-select --install` hoặc `brew install git`
- Ubuntu: `sudo apt update && sudo apt install -y git`

### Cấu hình Git tối thiểu

```bash
git config --global user.name "Tên của bạn"
git config --global user.email "email@example.com"
git config --global init.defaultBranch main
```

---

## 2. Kiểm tra Docker

```bash
docker --version
docker compose version
```

Nếu máy chưa có Docker:

- Windows/macOS: cài Docker Desktop
- Ubuntu: `sudo apt update && sudo apt install -y docker.io docker-compose-plugin`

### Tự xác minh Docker

```bash
docker run --rm hello-world
```

Nếu container chạy xong và in thông báo thành công, Docker đã sẵn sàng.

---

## 3. Clone repository handbook

```bash
git clone https://github.com/<github-org>/student-it-handbook.git
cd student-it-handbook
```

Thay `<github-org>` bằng organization hoặc username GitHub thực tế.

---

## 4. Chạy PostgreSQL stack mẫu

Case study `InternHub API` dùng PostgreSQL làm datastore chính. Trong repo đã có stack mẫu để bạn thực hành.

```bash
cd resources/docker
docker compose -f postgres-compose.yml up -d
```

### Kiểm tra container đã lên chưa

```bash
docker ps
```

Bạn cần thấy container `postgres-dev` đang chạy.

---

## 5. Kiểm tra kết nối database

```bash
docker exec -it postgres-dev psql -U dev -d internhub -c "SELECT 1;"
```

### Expected result

Bạn sẽ thấy output có giá trị `1`, ví dụ:

```text
 ?column?
----------
        1
```

Nếu bạn thấy kết quả này, môi trường tối thiểu cho handbook đã sẵn sàng.

---

## 6. Bạn vừa setup xong gì

Sau quickstart, bạn **chưa** học xong Git, Docker hay SQL. Bạn mới chỉ:

- có repo handbook trên máy
- có Docker chạy được
- có PostgreSQL stack mẫu cho InternHub
- có điểm bắt đầu để học những chương sau

---

## Lỗi thường gặp

| Lỗi | Nguyên nhân thường gặp | Cách xử lý |
| --- | --- | --- |
| `git: command not found` | Git chưa cài hoặc chưa có trong PATH | Cài lại Git, mở terminal mới |
| `docker: permission denied` | User chưa thuộc docker group trên Linux | `sudo usermod -aG docker $USER`, đăng nhập lại |
| Docker Desktop không lên | WSL2/backend chưa bật | Kiểm tra lại Docker Desktop settings |
| `psql: could not connect` | Container chưa ready | `docker ps`, `docker logs postgres-dev` |

---

## Cách tự kiểm tra đã hoàn thành

- [ ] `git --version` chạy được
- [ ] `docker --version` và `docker compose version` chạy được
- [ ] clone được repo handbook
- [ ] `docker compose -f postgres-compose.yml up -d` chạy thành công
- [ ] `SELECT 1;` trong `psql` trả về giá trị `1`

---

## Bước tiếp theo

- Đọc Start Here nếu bạn muốn chọn đúng luồng đọc
- Đọc Checklist sinh viên mới nếu bạn đang chuẩn bị đi thực tập
- Đọc Sample Project: InternHub API để hiểu case study xuyên suốt


<div class="pdf-page-break"></div>

<!-- Source: getting-started/sample-project.md -->

# Sample Project: InternHub API

`InternHub API` là case study xuyên suốt của handbook này. Nó không nhằm thay thế một repo production thật. Vai trò của nó là giúp các chương trong handbook nối với nhau bằng một bối cảnh kỹ thuật chung.

---

## Mục tiêu

Sau khi đọc trang này, bạn cần hiểu:

- InternHub API đang mô tả hệ thống nào
- chapter nào trong handbook đụng vào phần nào của case study
- tại sao case study này được dùng để học workflow thực tập

---

## Bối cảnh nghiệp vụ

InternHub API là một backend service mô phỏng cho một team nội bộ:

- quản lý danh sách intern, developer, lead
- lưu bài viết nội bộ và ghi chú trong team
- gắn tag cho bài viết để phân loại
- cho phép tìm kiếm, xem danh sách, tạo mới và cập nhật dữ liệu

Case study này đủ đơn giản để người mới theo kịp, nhưng vẫn đủ cho SQL, API, Docker, CI/CD và vận hành.

---

## Thành phần chính

### Entities

- `users`
- `posts`
- `comments`
- `tags`

### Infrastructure mô phỏng

- PostgreSQL
- Redis
- Docker Compose
- CI pipeline
- Deployment flow
- Logs và metrics

---

## Contract mô phỏng mà handbook sẽ bám vào

Handbook giả định InternHub API có ít nhất:

- endpoint `GET /api/users`
- endpoint `POST /api/users`
- endpoint `GET /api/posts`
- health endpoint để smoke test sau deploy
- metrics endpoint để monitoring scrape
- log output có request, error và context tối thiểu

Điều quan trọng ở đây là **tính nhất quán** của ví dụ, không phải đầy đủ tất cả tính năng.

---

## User stories dùng để hiểu handbook

### User story 1

Một intern mới vào team cần xem danh sách user để biết ai đang thuộc team nào.

Tài liệu liên quan:

- HTTP & REST API
- API Testing

### User story 2

Một developer cần thêm bài viết nội bộ và gắn tag để chia sẻ tài liệu hướng dẫn.

Tài liệu liên quan:

- SQL CRUD
- Docker Compose

### User story 3

Một lead cần xác minh bản deploy mới không làm hỏng endpoint chính và có thể rollback nếu cần.

Tài liệu liên quan:

- CI/CD - GitHub Actions
- Deployment cơ bản
- Logging & Monitoring

---

## Bug scenarios mô phỏng

### Bug scenario 1

`GET /api/users` trả `500` sau khi sửa query.

Dùng để học:

- đọc log
- kiểm tra query
- reproduce request

### Bug scenario 2

Container `web` restart liên tục vì env sai.

Dùng để học:

- `docker compose logs`
- verify env
- healthcheck

### Bug scenario 3

Pull Request pass local nhưng fail CI.

Dùng để học:

- đọc workflow
- phân biệt local vs CI env
- cách sửa và push lại

---

## Incident scenarios mô phỏng

### Incident 1

Deploy xong thì endpoint chính trả timeout.

Cần nghĩ đến:

- rollback
- smoke test
- logs
- metrics

### Incident 2

Disk đầy vì log quá nhiều hoặc Docker không được dọn dẹp.

Cần nghĩ đến:

- log level
- docker disk usage
- thao tác dọn dẹp an toàn

---

## Tài nguyên trong repo

- Database schema: `resources/database/sample-schema.sql`
- PostgreSQL stack: `resources/docker/postgres-compose.yml`
- Redis stack: `resources/docker/redis-compose.yml`
- Postman collection: `resources/api/postman-collection.json`

---

## Mỗi chương sẽ chạm vào phần nào của InternHub

| Chương | Vai trò với case study |
| --- | --- |
| Quickstart | Chạy stack PostgreSQL mẫu |
| SQL & PostgreSQL | Đọc schema, viết query trên `users`, `posts`, `comments`, `tags` |
| HTTP & REST API | Hiểu request/response cho endpoint của InternHub |
| API Testing | Gọi và verify `/api/users`, `/api/posts` |
| Docker Compose | Đóng gói `web + db + redis` |
| CI/CD | Build/release `internhub-api` |
| Deployment | Hiểu staging, prod, smoke test, rollback |
| Logging & Monitoring | Đọc log và metrics của `internhub-api` |

---

## Cách dùng trang này

- Đọc trang này trước khi đi vào chương kỹ thuật để không mất bối cảnh.
- Khi thấy ví dụ `users`, `posts`, `internhub-api`, hãy map nó lại với case study này.
- Nếu một chương đang nói quá chung chung, quay lại đây để nhắc bạn chapter đó đang phục vụ tình huống nào.

---

## Bước tiếp theo

- Nếu bạn chưa chạy môi trường tối thiểu: đọc Quickstart
- Nếu bạn chuẩn bị vào team: đọc Checklist sinh viên mới
- Nếu bạn muốn học theo phần cần dùng ngay: đọc Start Here


<div class="pdf-page-break"></div>

<!-- Source: getting-started/checklist.md -->

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
- [ ] Đã đọc Quickstart

### Tự xác minh môi trường

- [ ] `git --version` chạy được
- [ ] `docker --version` chạy được
- [ ] `docker compose version` chạy được
- [ ] Chạy được PostgreSQL stack mẫu cho InternHub

---

## 2. Trong ngày đầu tiên

### Hiểu bối cảnh trước khi sửa code

- [ ] Đọc Start Here
- [ ] Đọc Sample Project: InternHub API
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
| Chưa quen command line | Terminal & Shell |
| Sắp tạo PR đầu tiên | GitHub Workflow |
| Bắt đầu làm việc với DB | SQL & PostgreSQL |
| Cần chạy stack local | Docker Compose |
| Gặp lỗi local / Docker / Git | Lỗi thường gặp |

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

- Nếu bạn chưa setup máy: quay lại Quickstart
- Nếu bạn muốn hiểu dự án mẫu: đọc Sample Project: InternHub API
- Nếu bạn sắp vào workflow team: đọc GitHub Workflow


<div class="pdf-page-break"></div>

<!-- Source: environment/terminal.md -->

# Terminal & Shell cơ bản

Trang này đóng vai trò mục lục cho cụm bài về terminal. Nội dung chi tiết đã được tách nhỏ để bạn học theo từng kỹ năng thay vì phải đọc một bài quá dài.

---

## Mục tiêu

Sau cụm bài này, bạn có thể:

- phân biệt terminal và shell
- di chuyển thư mục và làm việc với file bằng command line
- kết hợp lệnh bằng `pipe` và `redirect`
- tìm file, tìm text và quản lý biến môi trường

---

## Prerequisites

- Đã hoàn thành: Quickstart
- Đã có terminal để thực hành trên Windows, macOS hoặc Linux

---

## Lộ trình học

1. Điều hướng Terminal
2. Quản lý File trong Terminal
3. Pipe và Redirect
4. Tìm kiếm và Biến môi trường

---

## Gợi ý học

- Học theo đúng thứ tự từ trên xuống dưới
- Sau mỗi bài, mở terminal và tự gõ lại lệnh thay vì chỉ đọc
- Nếu dùng Windows, ưu tiên Windows Terminal + WSL để trải nghiệm sát với môi trường đi làm

---

## Tài liệu liên quan

- Linux (WSL / Ubuntu)
- VS Code
- Linux Cheat Sheet


<div class="pdf-page-break"></div>

<!-- Source: environment/terminal-navigation.md -->

﻿# Điều hướng Terminal

Phần này tập trung vào các thao tác điều hướng thư mục cơ bản trong terminal.

---

## Điều hướng thư mục

### In thư mục hiện tại

```bash
pwd
```

---

### Liệt kê file

```bash
ls
```

Xem chi tiết:

```bash
ls -la
```

---

### Di chuyển thư mục

```bash
cd folder
```

---

### Lên một cấp

```bash
cd ..
```

---

### Về home directory

```bash
cd ~
```

---

### Quay lại thư mục trước

```bash
cd -
```

---


<div class="pdf-page-break"></div>

<!-- Source: environment/terminal-files.md -->

﻿# Quản lý File Trong Terminal

Phần này gom các thao tác làm việc với file, thư mục và đọc nội dung file.

---

## Quản lý file

---

## Tạo thư mục

```bash
mkdir project
```

Tạo nhiều cấp:

```bash
mkdir -p project/src/utils
```

---

## Tạo file

```bash
touch index.js
```

---

## Copy file

```bash
cp file.txt backup.txt
```

Copy folder:

```bash
cp -r src/ src_backup/
```

---

## Di chuyển / đổi tên

```bash
mv old.txt new.txt
```

---

## Xoá file

```bash
rm file.txt
```

---

## Xoá folder

```bash
rm -rf folder/
```

!!! danger "Cảnh báo"
Luôn kiểm tra kỹ path trước khi dùng `rm -rf`.

---

## Xem nội dung file

---

### In toàn bộ file

```bash
cat file.txt
```

---

### Xem 20 dòng đầu

```bash
head -20 file.txt
```

---

### Xem 20 dòng cuối

```bash
tail -20 file.txt
```

---

### Theo dõi log realtime

```bash
tail -f app.log
```

---

### Xem file theo trang

```bash
less file.txt
```

Thoát bằng:

```
q
```

---

### Đếm số dòng

```bash
wc -l file.txt
```

---


<div class="pdf-page-break"></div>

<!-- Source: environment/terminal-pipes-redirects.md -->

﻿# Pipe Và Redirect

Phần này giải thích cách kết hợp lệnh và điều hướng output trong shell.

---

## Pipe

Pipe cho phép **kết nối output của lệnh này sang input lệnh khác**.

---

### Ví dụ

Tìm process node:

```bash
ps aux | grep node
```

---

Đếm file Python:

```bash
find . -name "*.py" | wc -l
```

---

Sort và loại trùng:

```bash
cat names.txt | sort | uniq
```

---

## Redirect

Redirect cho phép **ghi output vào file**.

---

### Ghi đè file

```bash
echo "Hello" > output.txt
```

---

### Ghi thêm vào file

```bash
echo "World" >> output.txt
```

---

### Lưu lỗi

```bash
command 2> error.log
```

---

### Lưu cả output và error

```bash
command > all.log 2>&1
```

---


<div class="pdf-page-break"></div>

<!-- Source: environment/terminal-search-env.md -->

﻿# Tìm Kiếm Và Biến Môi Trường

Phần này gom các lệnh tìm kiếm, biến môi trường, mẹo hữu ích và phần tự luyện.

---

## Tìm kiếm file

---

### Tìm file theo tên

```bash
find . -name "*.js"
```

---

### Tìm text trong file

```bash
grep "TODO" -r src/
```

---

### Tìm kèm số dòng

```bash
grep -rn "error" .
```

---

### Tìm theo extension

```bash
grep -rn "error" --include="*.log" .
```

---

### Ripgrep (nhanh hơn)

```bash
rg "TODO" src/
```

---

## Biến môi trường

---

### Xem biến

```bash
echo $HOME
echo $PATH
```

---

### Tạo biến tạm

```bash
export MY_VAR="hello"
```

---

### Sử dụng

```bash
echo $MY_VAR
```

---

### Lưu vĩnh viễn

Thêm vào:

```
~/.bashrc
```

hoặc

```
~/.zshrc
```

Ví dụ:

```bash
echo 'export MY_VAR="hello"' >> ~/.bashrc
```

Sau đó reload:

```bash
source ~/.bashrc
```

---

## Lệnh hữu ích khác

```bash
which python
```

Đường dẫn binary.

---

```bash
whoami
```

User hiện tại.

---

```bash
df -h
```

Dung lượng disk.

---

```bash
du -sh folder/
```

Kích thước folder.

---

```bash
history | grep docker
```

Tìm lệnh trong history.

---

## Lỗi thường gặp

| Lỗi               | Nguyên nhân      | Cách sửa        |
| ----------------- | ---------------- | --------------- |
| command not found | chưa cài package | cài package     |
| permission denied | thiếu quyền      | dùng `sudo`     |
| no such file      | sai path         | kiểm tra `ls`   |
| ký tự lạ          | encoding sai     | kiểm tra locale |

---

## Bài tập

### Bài 1

Tạo cấu trúc thư mục:

```
myproject/
src/
tests/
docs/
```

bằng **một lệnh**.

---

### Bài 2

Tìm tất cả file `.md` và đếm số dòng.

---

### Bài 3

Tìm **10 lệnh gần nhất chứa `git`** trong history.

---

## Tài liệu tham khảo

```
https://linuxcommand.org/tlcl.php
```

```
https://explainshell.com/
```


<div class="pdf-page-break"></div>

<!-- Source: environment/linux.md -->

# Linux (WSL / Ubuntu)

Trang này là mục lục cho cụm bài Linux cơ bản. Nội dung đã được tách thành các bài nhỏ để dễ học, dễ tra cứu và dễ đưa vào bản PDF handbook.

---

## Mục tiêu

Sau cụm bài này, bạn có thể:

- cài WSL 2 và làm quen với Ubuntu trên Windows
- quản lý package và permissions trên Linux
- theo dõi process, port và các lệnh network căn bản
- vận hành service với `systemd`

---

## Prerequisites

- Đã hoàn thành: Quickstart
- Đã biết các thao tác terminal cơ bản: Terminal & Shell

---

## Lộ trình học

1. Cài đặt WSL và Làm quen Linux
2. Package và Permissions trên Linux
3. Process và Network cơ bản
4. Systemd và Vận hành Service

---

## Gợi ý học

- Nếu bạn dùng Windows, nên học WSL trước rồi mới sang package và permissions
- Vừa đọc vừa mở terminal Ubuntu để thực hành từng lệnh
- Giữ một file note riêng cho các lệnh hay dùng khi debug

---

## Tài liệu liên quan

- Terminal & Shell
- Lỗi thường gặp
- Linux Cheat Sheet


<div class="pdf-page-break"></div>

<!-- Source: environment/linux-wsl.md -->

﻿# Cài Đặt WSL Và Làm Quen Linux

Phần này hướng dẫn cài WSL 2 và cách truy cập file giữa Windows và WSL.

---

## 1. Cài đặt WSL 2

Mở **PowerShell (Admin)**:

```powershell
wsl --install
```

WSL sẽ tự động:

- bật **Virtual Machine Platform**
- cài **Ubuntu**
- cấu hình **WSL 2**

---

### Chọn distro cụ thể

```powershell
wsl --install -d Ubuntu-22.04
```

---

### Kiểm tra WSL

```powershell
wsl -l -v
```

Ví dụ:

```text
NAME            STATE           VERSION
Ubuntu          Running         2
```

---

### Mở WSL

Cách dễ nhất:

Mở **Windows Terminal → chọn Ubuntu**

---

## Truy cập file Windows từ WSL

Trong WSL:

```bash
cd /mnt/c/Users/<your-user>
```

---

## Truy cập file WSL từ Windows

Trong Windows Explorer:

```text
\\wsl$\Ubuntu\home\<your-user>
```

---


<div class="pdf-page-break"></div>

<!-- Source: environment/linux-packages-permissions.md -->

﻿# Package Và Permissions Trên Linux

Phần này gom các thao tác quản lý package và quyền truy cập trong Linux.

---

## 2. Quản lý package với apt

Ubuntu sử dụng **APT package manager**.

---

### Cập nhật package list

```bash
sudo apt update
```

---

### Nâng cấp hệ thống

```bash
sudo apt upgrade -y
```

---

### Cài package

```bash
sudo apt install -y curl wget htop tree jq
```

---

### Gỡ package

```bash
sudo apt remove package-name
```

---

### Tìm package

```bash
apt search keyword
```

---

## 3. Hệ thống quyền (Permissions)

Linux dùng **permission model**:

```text
owner | group | others
```

---

### Ví dụ `ls -la`

```text
-rw-r--r--  1 user group  4096 Jan 15 10:30 file.txt
drwxr-xr-x  2 user group  4096 Jan 15 10:30 folder/
```

Giải thích:

| Ký tự | Ă nghĩa |
| ----- | ------- |
| `r`   | read    |
| `w`   | write   |
| `x`   | execute |

---

### Giá trị số

| Permission | Value |
| ---------- | ----- |
| read       | 4     |
| write      | 2     |
| execute    | 1     |

---

### Ví dụ

```bash
chmod 755 script.sh
```

Giải thích:

```
7 = rwx
5 = r-x
5 = r-x
```

---

### Cấp quyền thực thi

```bash
chmod +x script.sh
```

---

### Đổi owner

```bash
chown user:group file.txt
```

---

### Ăp dụng đệ quy

```bash
chmod -R 755 folder/
chown -R user:group folder/
```

---


<div class="pdf-page-break"></div>

<!-- Source: environment/linux-process-network.md -->

﻿# Process Và Network Cơ Bản

Phần này tập trung vào process, port và các lệnh network thiết yếu.

---

## 4. Quản lý process

---

### Xem process

```bash
ps aux
```

---

### Tìm process

```bash
ps aux | grep python
```

---

### Xem realtime

```bash
htop
```

hoặc

```bash
top
```

---

### Kill process

```bash
kill 12345
```

Force kill:

```bash
kill -9 12345
```

---

### Kill theo tên

```bash
pkill -f "node server.js"
```

---

### Chạy process background

```bash
python app.py &
```

---

### Đưa process về foreground

```bash
fg
```

---

## 5. Network cơ bản

---

### Xem IP

Linux:

```bash
ip addr show
```

macOS:

```bash
ifconfig
```

---

### Kiểm tra kết nối

```bash
ping google.com -c 4
```

---

### Xem port đang mở

Linux:

```bash
ss -tulnp
```

macOS:

```bash
lsof -i :8080
```

---

### Kiểm tra service

```bash
curl -I http://localhost:3000
```

---

### DNS lookup

```bash
nslookup example.com
```

hoặc

```bash
dig example.com
```

---

### Download file

```bash
wget https://example.com/file.zip
```

hoặc

```bash
curl -O https://example.com/file.zip
```

---


<div class="pdf-page-break"></div>

<!-- Source: environment/linux-services.md -->

﻿# Systemd Và Vận Hành Service

Phần này hướng dẫn quản lý service với systemd và phần tự luyện cuối chương.

---

## 6. Quản lý service (systemd)

---

### Kiểm tra service

```bash
sudo systemctl status nginx
```

---

### Start / Stop

```bash
sudo systemctl start nginx
sudo systemctl stop nginx
```

---

### Restart

```bash
sudo systemctl restart nginx
```

---

### Auto start khi boot

```bash
sudo systemctl enable nginx
```

---

## Lỗi thường gặp

| Lỗi                            | Nguyên nhân               | Cách khắc phục            |
| ------------------------------ | ------------------------- | ------------------------- |
| `sudo: command not found`      | user không có quyền sudo  | thêm user vào group sudo  |
| `Unable to locate package`     | apt chưa update           | chạy `sudo apt update`    |
| WSL truy cập `/mnt/c` rất chậm | filesystem cross-boundary | đặt project trong `/home` |
| Port conflict                  | service khác dùng port    | `lsof -i :PORT`           |

---

## Bài tập

### Bài 1

Cài `tree` và hiển thị cấu trúc thư mục:

```bash
tree ~ -L 2
```

---

### Bài 2

Tạo script:

```bash
touch hello.sh
```

Nội dung:

```bash
echo "Hello from Linux!"
```

Cấp quyền:

```bash
chmod +x hello.sh
```

Chạy:

```bash
./hello.sh
```

---

### Bài 3

Tìm process chiếm port **8080**.

---

## Tài liệu tham khảo

- [https://learn.microsoft.com/en-us/windows/wsl/](https://learn.microsoft.com/en-us/windows/wsl/)
- [https://linuxjourney.com/](https://linuxjourney.com/)

*


<div class="pdf-page-break"></div>

<!-- Source: environment/vscode.md -->

﻿# VS Code – Editor cho Developer

**Visual Studio Code (VS Code)** là editor phổ biến nhất cho developer hiện nay.

VS Code hỗ trợ:

- nhiều ngôn ngữ lập trình
- hệ thống **extensions**
- **debugging**
- **Git integration**
- **remote development** (WSL / SSH / Container)

---

## Mục tiêu

Sau bài này bạn có thể:

- cấu hình VS Code cho development
- cài extensions cần thiết
- sử dụng các **phím tắt quan trọng**
- làm việc với **WSL / remote server**

---

## Cài đặt VS Code

Tải tại:

```
https://code.visualstudio.com/
```

Sau khi cài xong, kiểm tra lệnh CLI:

```bash
code --version
```

---

## Extensions khuyên dùng

Extensions giúp VS Code hỗ trợ thêm nhiều tính năng.

---

## Extensions bắt buộc

| Extension    | Mục đích                      |
| ------------ | ----------------------------- |
| GitLens      | Hiển thị git blame và history |
| Docker       | Quản lý container             |
| Remote - WSL | Làm việc với WSL              |
| Remote - SSH | Code trên server              |
| EditorConfig | Đồng bộ format trong team     |

---

## Extensions theo ngôn ngữ

| Ngôn ngữ                | Extension                        |
| ----------------------- | -------------------------------- |
| Python                  | Python, Pylance, Black Formatter |
| JavaScript / TypeScript | ESLint, Prettier                 |
| SQL                     | SQLTools                         |
| Markdown                | Markdown All in One              |

---

## Phím tắt quan trọng

| Windows / Linux    | macOS             | Chức năng           |
| ------------------ | ----------------- | ------------------- |
| `Ctrl + Shift + P` | `Cmd + Shift + P` | Command Palette     |
| `Ctrl + P`         | `Cmd + P`         | Mở file nhanh       |
| `Ctrl + Shift + F` | `Cmd + Shift + F` | Search toàn project |
| `Ctrl + ``         | `Cmd + ``         | Mở terminal         |
| `Ctrl + /`         | `Cmd + /`         | Comment dòng        |
| `Alt + ↑ / ↓`      | `Option + ↑ / ↓`  | Di chuyển dòng      |
| `Ctrl + D`         | `Cmd + D`         | Select occurrence   |
| `Ctrl + Shift + K` | `Cmd + Shift + K` | Xoá dòng            |
| `F2`               | `F2`              | Rename symbol       |

---

## Cấu hình VS Code

Mở **Command Palette**:

```
Ctrl + Shift + P
```

Tìm:

```
Open User Settings (JSON)
```

Ví dụ cấu hình:

```json
{
  "editor.fontSize": 14,
  "editor.tabSize": 2,
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.minimap.enabled": false,
  "files.autoSave": "afterDelay",
  "files.trimTrailingWhitespace": true,
  "git.autofetch": true
}
```

Các setting phổ biến:

| Setting                  | Mục đích       |
| ------------------------ | -------------- |
| `formatOnSave`           | tự format code |
| `autoSave`               | tự lưu file    |
| `trimTrailingWhitespace` | xoá space thừa |
| `git.autofetch`          | tự fetch git   |

---

## VS Code + WSL

VS Code có thể mở project trực tiếp trong WSL.

Trong terminal WSL:

```bash
cd ~/myproject
code .
```

VS Code sẽ tự động kết nối qua **Remote – WSL**.

---

### Lưu ý hiệu suất

Không nên mở project tại:

```
/mnt/c/Users/...
```

Thay vào đó nên đặt project tại:

```
~/projects
```

vì filesystem WSL nhanh hơn nhiều.

---

## Workspace settings

VS Code có hai loại settings.

| Loại               | Phạm vi                   |
| ------------------ | ------------------------- |
| User settings      | áp dụng cho toàn hệ thống |
| Workspace settings | chỉ project hiện tại      |

---

### Ví dụ `.vscode/settings.json`

```json
{
  "python.defaultInterpreterPath": ".venv/bin/python",
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter"
  }
}
```

File này giúp **đồng bộ cấu hình giữa các developer**.

---

## Debugging

VS Code hỗ trợ debugging cho nhiều ngôn ngữ.

---

### Các bước cơ bản

1. Mở file code
2. Đặt **breakpoint**
3. Nhấn:

```
F5
```

Hoặc vào tab:

```
Run and Debug
```

Sau đó chọn runtime:

```
Python
Node.js
Go
...
```

---

## Lỗi thường gặp

| Lỗi                       | Nguyên nhân              | Cách sửa                      |
| ------------------------- | ------------------------ | ----------------------------- |
| Extension không hoạt động | chạy code trong WSL      | cài extension trong WSL       |
| Terminal chậm             | dùng PowerShell mặc định | chuyển sang WSL / Git Bash    |
| Format không chạy         | chưa set formatter       | set `editor.defaultFormatter` |

---

## Tài liệu tham khảo

```
https://code.visualstudio.com/docs
```

```
https://code.visualstudio.com/docs/getstarted/tips-and-tricks
```


<div class="pdf-page-break"></div>

<!-- Source: vcs/git-basics.md -->

# Git cơ bản

Trang này là điểm vào cho lộ trình Git. Nội dung đã được tách theo 3 nhóm kỹ năng: nền tảng, collaboration và recovery.

---

## Mục tiêu

Sau cụm bài này, bạn có thể:

- hiểu mô hình hoạt động của Git
- commit, push, pull và làm việc với branch
- dùng merge, rebase và xử lý conflict
- undo sai sót và phục hồi lịch sử khi cần

---

## Prerequisites

- Đã hoàn thành: Quickstart
- Đã quen với terminal: Terminal & Shell

---

## Lộ trình học

1. Git Fundamentals
2. Branching, Merge và Rebase
3. Undo và Recovery trong Git

---

## Gợi ý học

- Học fundamentals trước khi học workflow GitHub
- Tự tạo một repo nhỏ để tập branch, merge, conflict và reflog
- Khi học recovery, nên thực hành trên repo thử nghiệm thay vì repo thật

---

## Tài liệu liên quan

- GitHub Workflow
- Git Cheat Sheet
- Lỗi thường gặp


<div class="pdf-page-break"></div>

<!-- Source: vcs/git-fundamentals.md -->

﻿# Git Fundamentals

Phần này đi qua mô hình hoạt động của Git, khởi tạo repo, commit và đồng bộ remote.

---

## Git hoạt động thế nào

> So do duoc luoc bo trong ban PDF. Xem ban web neu can hinh minh hoa.

---

## Các vùng trong Git

| Vùng              | Ă nghĩa              |
| ----------------- | -------------------- |
| Working Directory | code trên máy        |
| Staging Area      | file chuẩn bị commit |
| Local Repository  | lịch sử commit local |
| Remote Repository | repo trên GitHub     |

---

## Khởi tạo repository

---

## Clone repo

```bash
git clone https://github.com/user/repo.git
cd repo
```

---

## Tạo repo mới

```bash
mkdir myproject
cd myproject
git init
```

---

## Kiểm tra trạng thái

---

### Trạng thái file

```bash
git status
```

---

### Xem lịch sử commit

```bash
git log --oneline --graph --all
```

---

### Xem thay đổi

```bash
git diff
```

---

### Xem thay đổi đã staged

```bash
git diff --staged
```

---

## Add & Commit

---

### Thêm file vào staging

```bash
git add file.txt
```

---

### Thêm toàn bộ file

```bash
git add .
```

---

### Commit

```bash
git commit -m "feat: add login API"
```

---

### Sửa commit gần nhất

```bash
git commit --amend -m "feat: add login API endpoint"
```

---

## Push & Pull

---

### Push code

```bash
git push origin main
```

---

### Pull code

```bash
git pull origin main
```

Pull thực chất là:

```
fetch + merge
```

---

### Chỉ fetch

```bash
git fetch origin
```

---


<div class="pdf-page-break"></div>

<!-- Source: vcs/git-branching.md -->

﻿# Branching, Merge Và Rebase

Phần này tập trung vào branch workflow, merge, rebase và xử lý conflict.

---

## Branch

Branch giúp phát triển **nhiều tính năng song song**.

---

### Xem branch

```bash
git branch
```

---

### Tạo branch

```bash
git branch feature/login
```

---

### Chuyển branch

```bash
git checkout feature/login
```

hoặc:

```bash
git switch feature/login
```

---

### Tạo + chuyển branch

```bash
git checkout -b feature/login
```

hoặc:

```bash
git switch -c feature/login
```

---

### Xoá branch

```bash
git branch -d feature/login
```

Force delete:

```bash
git branch -D feature/login
```

---

## Quy tắc đặt tên branch

| Prefix    | Mục đích           |
| --------- | ------------------ |
| feature/  | tính năng mới      |
| bugfix/   | sửa bug            |
| hotfix/   | sửa lỗi production |
| docs/     | thay đổi docs      |
| refactor/ | tái cấu trúc code  |

---

### Ví dụ

```
feature/user-auth
bugfix/login-crash
docs/update-readme
refactor/cleanup-utils
```

---

## Merge vs Rebase

---

## Merge

```bash
git checkout main
git merge feature/login
```

> So do duoc luoc bo trong ban PDF. Xem ban web neu can hinh minh hoa.

Merge tạo **merge commit**.

---

## Rebase

```bash
git checkout feature/login
git rebase main
```

Sau đó:

```bash
git checkout main
git merge feature/login
```

---

!!! warning "Lưu ý"
Không nên **rebase branch đã push và đang được nhiều người sử dụng**.

---

## Giải quyết conflict

Git sẽ đánh dấu:

```
<<<<<<< HEAD
Code branch hiện tại
=======
Code branch khác
>>>>>>> feature/login
```

---

### Cách xử lý

1. Mở file bị conflict
2. Chọn code đúng
3. Xoá marker conflict
4. Stage file

```bash
git add file.txt
```

5. Tiếp tục

```bash
git merge --continue
```

hoặc

```bash
git rebase --continue
```

---

## Commit message chuẩn

Nên dùng **Conventional Commits**.

---

### Format

```
type(scope): description
```

---

### Các type phổ biến

| Type     | Ă nghĩa        |
| -------- | -------------- |
| feat     | thêm feature   |
| fix      | sửa bug        |
| docs     | thay đổi docs  |
| style    | format code    |
| refactor | refactor code  |
| test     | test           |
| chore    | config / build |

---

### Ví dụ

```
feat(auth): add JWT refresh token endpoint
```

---


<div class="pdf-page-break"></div>

<!-- Source: vcs/git-recovery.md -->

﻿# Undo Và Recovery Trong Git

Phần này gom các kỹ thuật hoàn tác, phục hồi và phần tự luyện cuối chương.

---

## Undo & Recovery

---

### Bỏ file khỏi staging

```bash
git restore --staged file.txt
```

---

### Bỏ thay đổi

```bash
git restore file.txt
```

---

### Quay lại commit trước

```bash
git reset HEAD~1
```

---

### Reset mạnh

```bash
git reset --hard HEAD~1
```

---

### Khôi phục bằng reflog

```bash
git reflog
git reset --hard HEAD@{2}
```

---

!!! tip "Mẹo quan trọng"
`git reflog` lưu lại gần như mọi thao tác Git.
Bạn có thể khôi phục commit kể cả khi đã `reset --hard`.

---

## Lỗi thường gặp

| Lỗi                  | Nguyên nhân           | Cách sửa            |
| -------------------- | --------------------- | ------------------- |
| not a git repository | chưa init repo        | chạy `git init`     |
| failed to push       | remote có commit mới  | `git pull --rebase` |
| merge conflict       | 2 người sửa cùng file | resolve thủ công    |
| detached HEAD        | checkout commit       | `git switch main`   |

---

## Bài tập

### Bài 1

Tạo repo mới và commit 3 lần.

---

### Bài 2

Tạo branch:

```
feature/hello
```

Merge vào main.

---

### Bài 3

Tạo conflict và thực hành resolve.

---

### Bài 4

Viết 5 commit message theo chuẩn **Conventional Commits**.

---

## Tài liệu tham khảo

```
https://git-scm.com/book
```

```
https://learngitbranching.js.org
```

```
https://www.conventionalcommits.org
```


<div class="pdf-page-break"></div>

<!-- Source: vcs/github-workflow.md -->

# GitHub Workflow

Trang này mô tả workflow làm việc nhóm phổ biến với Git và GitHub. Nó được viết cho sinh viên mới vào dự án, nên ưu tiên sự rõ ràng và tính an toàn hơn là dạy tất cả tính năng của GitHub.

---

## Mục tiêu

Sau bài này, bạn cần làm được:

- tạo branch riêng cho task
- commit theo nhịp nhỏ và rõ ràng
- mở Pull Request để reviewer đọc dễ dàng
- đọc và phản hồi review comment
- biết khi nào cần hỏi mentor hoặc reviewer

---

## Khi nào bạn cần phần này

- Bạn sắp tạo branch đầu tiên trong repo team.
- Bạn vừa nhận task và cần mở PR.
- Bạn đã mở PR nhưng chưa quen cách phản hồi review.

---

## Prerequisites

- Git cơ bản
- Có tài khoản GitHub
- Đã bật 2FA nếu repo/team yêu cầu

---

## Workflow cơ bản

```text
Task -> Branch -> Commit -> Push -> Pull Request -> Review -> Merge
```

Nguyên tắc nên nhớ:

1. `main` phải luôn ở trạng thái có thể release hoặc deploy.
2. Mỗi task nên đi trên một branch riêng.
3. PR càng nhỏ thì review càng dễ.
4. Không merge khi chưa hiểu feedback.

---

## 1. Tạo branch cho task

```bash
git switch -c feature/user-profile
```

Tên branch nên nói rõ ý định:

- `feature/...`
- `fix/...`
- `docs/...`
- `chore/...`

### Pitfall

Không code trực tiếp trên `main` nếu repo đang dùng workflow review.

---

## 2. Commit nhỏ, có ý nghĩa

```bash
git add .
git commit -m "feat(user): add profile endpoint"
```

### Author checklist trước khi commit

- [ ] Biết mình đang sửa vì task nào
- [ ] Không commit file tạm, secret, log hoặc output build
- [ ] Có thể giải thích nhanh thay đổi này dùng để làm gì

---

## 3. Push branch và mở Pull Request

```bash
git push -u origin feature/user-profile
```

Khi mở PR, người đọc cần hiểu ngay:

- task này sửa cái gì
- ảnh hưởng đến phần nào
- đã tự test gì
- reviewer cần tập trung check điểm nào

### Template PR tối thiểu

```markdown
## Mô tả

Thêm endpoint profile cho user.

## Thay đổi

- thêm route `/api/users/profile`
- thêm query lấy dữ liệu user
- thêm test cơ bản

## Tự kiểm tra

- [x] test local đã chạy
- [x] không còn debug log
- [x] docs đã cập nhật nếu cần
```

### Expected result

PR mở ra có mô tả, có reviewer, và người khác có thể review mà không cần hỏi lại bạn task này là gì.

---

## 4. Request review

Sau khi tạo PR:

- assign reviewer nếu workflow team yêu cầu
- link issue/task nếu có
- nếu PR còn đang làm dở, để ở trạng thái draft

### Khi nào nên mở draft PR

- Bạn cần feedback sớm về hướng sửa
- Logic đã rõ nhưng chưa xong test
- Bạn muốn reviewer check approach trước khi viết tiếp

---

## 5. Cách review code

Code review không phải để “bắt lỗi cho vui”. Mục tiêu của nó là:

- bắt bug sớm
- giữ code dễ đọc
- giảm rủi ro trước khi merge
- chia sẻ bối cảnh và kiến thức trong team

### Reviewer checklist tối thiểu

- [ ] Logic có đúng với task không
- [ ] Có tác dụng phụ nào rõ ràng không
- [ ] Có test hoặc cách verify không
- [ ] Có security issue rõ ràng không
- [ ] Có command/nguy cơ nào cần cảnh báo thêm không

### Author checklist trước khi nhận review

- [ ] PR không quá lớn đến mức reviewer không thể đọc được
- [ ] Title/description dễ hiểu
- [ ] Đã tự đọc lại diff của mình
- [ ] Đã ghi rõ những chỗ còn mở hoặc cần reviewer xem kỹ

---

## 6. Cách phản hồi review comment

Khi reviewer để lại comment:

1. Đọc kỹ để phân biệt đó là bug, concern hay style feedback.
2. Nếu chưa hiểu, hỏi lại ngay trong thread.
3. Sửa code và push commit mới.
4. Reply ngắn gọn comment đã được xử lý như thế nào.

```bash
git add .
git commit -m "fix: address review comments"
git push
```

### Khi nào cần hỏi mentor

- Bạn không hiểu reviewer đang nói về bug logic hay preference
- Feedback làm thay đổi hướng implementation
- Bạn cần thêm bối cảnh domain để quyết định

---

## 7. Conflict và cập nhật branch

Nếu branch của bạn đã cũ hơn `main`, có 2 cách phổ biến:

### Rebase

```bash
git fetch origin
git rebase origin/main
```

Nếu có conflict:

```bash
git add .
git rebase --continue
git push --force-with-lease
```

### Merge main vào branch

```bash
git fetch origin
git merge origin/main
git push
```

### Guardrail

- Ưu tiên `--force-with-lease`, không dùng `--force` nếu không thực sự hiểu tác dụng.
- Nếu branch đang được nhiều người cùng sửa, cần thống nhất trước khi rewrite history.

---

## 8. Issues và task intake

Issue là nơi ghi rõ:

- vấn đề là gì
- cách reproduce
- expected vs actual
- mức ưu tiên

### Example

```markdown
Title: [BUG] GET /api/users returns 500 after query change

## Steps to reproduce
1. Start local stack
2. Call GET /api/users
3. Observe response

## Expected
200 OK with users array

## Actual
500 Internal Server Error
```

Nếu issue không đủ rõ:

- hỏi lại output mong đợi
- hỏi lý do business
- hỏi cách verify done

---

## Tự kiểm tra đã hiểu workflow này chưa

- [ ] Tạo được branch mới
- [ ] Commit có message rõ ràng
- [ ] Mở được PR có mô tả và checklist có nghĩa
- [ ] Biết cách phản hồi review comment
- [ ] Biết khi nào nên ping mentor hoặc reviewer

---

## Bước tiếp theo

- Nếu bạn chưa quen command line: đọc Terminal & Shell
- Nếu bạn sắp nhận task backend: đọc HTTP & REST API
- Nếu bạn thường gặp lỗi local: đọc Lỗi thường gặp


<div class="pdf-page-break"></div>

<!-- Source: programming/python-anaconda.md -->

﻿# Python & Anaconda

Trang này hướng dẫn cách **quản lý môi trường Python và package dependencies**.

Python projects thường sử dụng **virtual environments** để:

- tránh conflict package
- quản lý dependency theo project
- đảm bảo reproducible environment

---

## Mục tiêu

Sau bài này bạn có thể:

- tạo **virtual environment**
- quản lý package bằng **pip** hoặc **conda**
- chạy **Jupyter Notebook**
- xử lý lỗi phổ biến khi cài package

---

## Yêu cầu

Bạn cần cài:

- **Python 3.9+**
- hoặc **Anaconda**

Nếu chưa cài môi trường, xem:

```text
Quickstart
```

---

## pip vs conda

|             | pip               | conda                     |
| ----------- | ----------------- | ------------------------- |
| Quản lý     | Python packages   | Python + system libraries |
| Nguồn       | PyPI              | Anaconda / conda-forge    |
| Environment | venv / virtualenv | conda env                 |
| Lock file   | requirements.txt  | environment.yml           |

---

!!! tip "Quy tắc quan trọng"
Trong một environment nên **chỉ dùng pip hoặc conda làm package manager chính** để tránh conflict.

---

## Virtual Environment

Virtual environment giúp mỗi project có **dependencies riêng biệt**.

---

## Tạo environment với conda

---

### Tạo env

```bash
conda create -n myproject python=3.11 -y
```

---

### Kích hoạt

```bash
conda activate myproject
```

---

### Xem danh sách env

```bash
conda env list
```

---

### Cài package

```bash
conda install numpy pandas flask
```

---

### Export environment

```bash
conda env export > environment.yml
```

---

### Tạo env từ file

```bash
conda env create -f environment.yml
```

---

### Xoá env

```bash
conda env remove -n myproject
```

---

## Virtual Environment với venv

Python tích hợp sẵn **venv**.

---

### Tạo environment

```bash
python -m venv .venv
```

---

### Kích hoạt env

Linux / macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.\.venv\Scripts\Activate.ps1
```

---

### Cài package

```bash
pip install flask sqlalchemy
```

---

### Export dependencies

```bash
pip freeze > requirements.txt
```

---

### Cài từ file

```bash
pip install -r requirements.txt
```

---

### Thoát environment

```bash
deactivate
```

---

## Cấu trúc project Python

Một project Python thường có cấu trúc:

```text
myproject/
├── .venv/
├── src/
│   └── myproject/
│       ├── __init__.py
│       ├── main.py
│       └── utils.py
├── tests/
│   └── test_utils.py
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

## Jupyter Notebook

Jupyter cho phép chạy code Python **từng cell**.

---

### Cài Jupyter

```bash
pip install jupyter
```

hoặc:

```bash
conda install jupyter
```

---

### Chạy Jupyter

```bash
jupyter notebook
```

---

### JupyterLab (giao diện mới)

```bash
pip install jupyterlab
jupyter lab
```

---

## Kernel cho virtual environment

Để Jupyter nhận environment:

---

### Cài ipykernel

```bash
pip install ipykernel
```

---

### Đăng ký kernel

```bash
python -m ipykernel install --user --name myproject --display-name "Python (myproject)"
```

---

### Xem danh sách kernel

```bash
jupyter kernelspec list
```

---

### Xoá kernel

```bash
jupyter kernelspec remove myproject
```

---

## `.gitignore` cho Python

```gitignore
__pycache__/
*.pyc
*.pyo

.venv/

*.egg-info/
dist/
build/

.pytest_cache/
.mypy_cache/

.ipynb_checkpoints/

.env
```

---

!!! danger "Quan trọng"
Không commit:

```text
.env
.venv
API keys
password
```

---

## Lỗi thường gặp

| Lỗi                         | Nguyên nhân           | Cách sửa            |
| --------------------------- | --------------------- | ------------------- |
| ModuleNotFoundError         | package chưa cài      | kiểm tra env        |
| conda: command not found    | chưa init conda       | chạy `conda init`   |
| Could not build wheels      | thiếu build tools     | cài build-essential |
| Solving environment rất lâu | conflict dependencies | dùng conda-forge    |
| Jupyter kernel sai          | env chưa đăng ký      | cài ipykernel       |

---

## Bài tập

### Bài 1

Tạo conda env:

```text
practice
```

Cài:

```text
pandas
requests
```

Export:

```text
environment.yml
```

---

### Bài 2

Viết script Python:

- đọc file CSV
- in 5 dòng đầu

---

### Bài 3

Tạo Jupyter Notebook:

- import `matplotlib`
- vẽ biểu đồ đơn giản

---

## Tài liệu tham khảo

```text
https://packaging.python.org/
```

```text
https://docs.conda.io/projects/conda/en/latest/
```


<div class="pdf-page-break"></div>

<!-- Source: programming/nodejs.md -->

﻿# Node.js & npm

Trang này giới thiệu cách thiết lập môi trường **Node.js development** và quản lý package với **npm**.

Node.js được dùng phổ biến để xây dựng:

- backend APIs
- CLI tools
- frontend tooling

---

## Mục tiêu

Sau bài này bạn có thể:

- cài Node.js bằng **nvm**
- hiểu `npm`, `yarn`, `pnpm`
- sử dụng **package.json**
- quản lý **scripts**
- dùng **biến môi trường `.env`**

---

## Yêu cầu

Bạn cần có **terminal**.

Nếu chưa quen command line, xem:

```text
Terminal cơ bản
```

---

## Cài đặt Node.js

Khuyến nghị sử dụng **nvm (Node Version Manager)** để quản lý nhiều phiên bản Node.js.

---

## Linux / macOS

Cài **nvm**:

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
source ~/.bashrc
```

Cài Node.js LTS:

```bash
nvm install --lts
nvm use --lts
```

Kiểm tra:

```bash
node --version
npm --version
```

Ví dụ:

```text
v20.x.x
10.x.x
```

---

## Windows

Sử dụng **nvm-windows**:

```text
https://github.com/coreybutler/nvm-windows
```

Sau khi cài:

```powershell
nvm install 20
nvm use 20
```

Kiểm tra:

```powershell
node --version
npm --version
```

---

## npm cơ bản

npm là **package manager của Node.js**.

---

## Khởi tạo project

```bash
npm init -y
```

Lệnh này tạo file:

```text
package.json
```

---

## Cài package

---

### Production dependency

```bash
npm install express
```

---

### Development dependency

```bash
npm install --save-dev eslint prettier
```

---

### Global package

```bash
npm install -g nodemon
```

---

### Cài từ package.json

```bash
npm install
```

Clean install:

```bash
npm ci
```

`npm ci` thường dùng trong **CI/CD pipelines**.

---

## Gỡ package

```bash
npm uninstall express
```

---

## package.json

File `package.json` chứa metadata của project.

---

## Ví dụ

```json
{
  "name": "my-api",
  "version": "1.0.0",
  "main": "src/index.js",
  "scripts": {
    "start": "node src/index.js",
    "dev": "nodemon src/index.js",
    "test": "jest",
    "lint": "eslint src/",
    "build": "tsc"
  },
  "dependencies": {
    "express": "^4.18.2",
    "dotenv": "^16.3.1"
  },
  "devDependencies": {
    "eslint": "^8.50.0",
    "jest": "^29.7.0"
  }
}
```

---

## Các trường quan trọng

| Field           | Ă nghĩa                       |
| --------------- | ----------------------------- |
| scripts         | các lệnh chạy project         |
| dependencies    | packages dùng cho production  |
| devDependencies | packages dùng khi development |

---

## Chạy scripts

Scripts được chạy bằng:

```bash
npm run <script-name>
```

Ví dụ:

```bash
npm run dev
npm run lint
```

Một số script có shortcut:

```bash
npm start
npm test
```

---

## Biến môi trường (.env)

Thư viện phổ biến:

```bash
npm install dotenv
```

---

## Ví dụ `.env`

```env
PORT=3000
DATABASE_URL=postgres://user:pass@localhost:5432/mydb
JWT_SECRET=my-secret
NODE_ENV=development
```

---

## Sử dụng trong code

```javascript
require("dotenv").config();

const port = process.env.PORT || 3000;

console.log(`Server running on port ${port}`);
```

---

!!! danger "Quan trọng"
Không commit file `.env`.

Thay vào đó nên tạo:

```text
.env.example
```

---

## npm vs yarn vs pnpm

|            | npm               | yarn      | pnpm           |
| ---------- | ----------------- | --------- | -------------- |
| Lock file  | package-lock.json | yarn.lock | pnpm-lock.yaml |
| Tốc độ     | trung bình        | nhanh     | nhanh nhất     |
| Disk usage | lớn               | lớn       | tiết kiệm      |

---

### Ví dụ yarn

```bash
npm install -g yarn
yarn add express
```

---

### Ví dụ pnpm

```bash
npm install -g pnpm
pnpm add express
```

---

!!! tip "Best practice"
Trong một project nên **chỉ dùng một package manager**.

---

## Cấu trúc project Node.js

Một project backend thường có cấu trúc:

```text
my-api/
├── node_modules/
├── src/
│   ├── index.js
│   ├── routes/
│   ├── controllers/
│   ├── models/
│   ├── middleware/
│   └── utils/
├── tests/
├── .env
├── .env.example
├── .gitignore
├── package.json
└── README.md
```

---

## Lỗi thường gặp

| Lỗi                      | Nguyên nhân          | Cách sửa             |
| ------------------------ | -------------------- | -------------------- |
| node command not found   | chưa dùng nvm        | `nvm use --lts`      |
| EACCES permission denied | cài global bằng sudo | dùng nvm             |
| Cannot find module       | thiếu dependency     | chạy `npm install`   |
| ENOSPC watchers          | Linux watcher limit  | tăng `inotify` limit |
| Port đã dùng             | process khác chiếm   | kill process         |

---

## Bài tập

### Bài 1

Tạo project Node.js mới.

Cài:

```text
express
```

Viết API:

```text
GET /hello
```

Trả:

```json
{
  "message": "Hello!"
}
```

---

### Bài 2

Thêm script:

```text
dev
```

sử dụng `nodemon`.

---

### Bài 3

Tạo `.env` với biến:

```text
PORT
```

---

## Tài liệu tham khảo

```text
https://nodejs.org/en/docs
```

```text
https://docs.npmjs.com/
```


<div class="pdf-page-break"></div>

<!-- Source: programming/dependency-management.md -->

﻿# Quản lý Dependencies

Dependencies là các **thư viện hoặc package bên ngoài** mà project sử dụng.

Quản lý dependencies đúng cách giúp:

- đảm bảo **mọi developer chạy cùng môi trường**
- tránh lỗi **"works on my machine"**
- giảm rủi ro **security vulnerabilities**

---

## Mục tiêu

Sau bài này bạn có thể:

- hiểu tầm quan trọng của dependency management
- sử dụng **lock file**
- hiểu **Semantic Versioning**
- cập nhật package an toàn

---

## Vì sao dependency management quan trọng

Một project có thể sử dụng **hàng chục đến hàng trăm thư viện**.

Nếu không quản lý đúng:

```text
Developer A: package v1.0
Developer B: package v1.2
CI server: package v2.0
```

Kết quả:

```text
Ứng dụng chạy khác nhau trên mỗi máy
```

---

## Lock File

Lock file ghi lại **chính xác phiên bản dependency** được cài.

Nhờ đó mọi developer và CI server đều cài **giống nhau 100%**.

---

## Lock file theo ngôn ngữ

| Ngôn ngữ        | Lock file         | Commit? |
| --------------- | ----------------- | ------- |
| Python          | requirements.txt  | Có      |
| Node.js         | package-lock.json | Có      |
| Node.js (yarn)  | yarn.lock         | Có      |
| Python (Poetry) | poetry.lock       | Có      |
| Conda           | environment.yml   | Có      |

---

!!! warning "Quy tắc quan trọng"
Luôn **commit lock file** vào repository.

Đây là cách duy nhất để đảm bảo:

```text
Reproducible builds
```

---

## Semantic Versioning (SemVer)

Hầu hết package sử dụng **Semantic Versioning**.

Format:

```text
MAJOR.MINOR.PATCH
```

Ví dụ:

```text
2.1.3
```

---

## Ý nghĩa version

| Phần  | Khi nào tăng     |
| ----- | ---------------- |
| MAJOR | breaking changes |
| MINOR | thêm feature     |
| PATCH | sửa bug          |

---

### Ví dụ

```text
1.2.3 → 2.0.0   breaking changes
2.0.0 → 2.1.0   new feature
2.1.0 → 2.1.1   bug fix
```

---

## Version ranges (Node.js)

Trong `package.json` thường thấy:

| Ký hiệu  | Ý nghĩa                |
| -------- | ---------------------- |
| `^1.2.3` | cho phép upgrade minor |
| `~1.2.3` | chỉ upgrade patch      |
| `1.2.3`  | version chính xác      |
| `*`      | bất kỳ version         |

---

### Ví dụ

```json
"express": "^4.18.2"
```

Range thực tế:

```text
>=4.18.2 <5.0.0
```

---

## Kiểm tra dependency outdated

---

## Node.js

Xem package cũ:

```bash
npm outdated
```

---

Cập nhật theo semver range:

```bash
npm update
```

---

Cập nhật major version:

```bash
npx npm-check-updates -u
npm install
```

---

Kiểm tra security:

```bash
npm audit
```

Fix tự động:

```bash
npm audit fix
```

---

## Python

Xem package outdated:

```bash
pip list --outdated
```

---

Cập nhật package:

```bash
pip install --upgrade flask
```

---

Kiểm tra security:

```bash
pip install safety
safety check
```

---

## Best Practices

---

## 1. Pin version trong production

Ví dụ Python:

```text
flask==2.3.3
```

---

## 2. Luôn commit lock file

Ví dụ:

```text
requirements.txt
package-lock.json
```

---

## 3. Review dependency changes

Khi dependency thay đổi:

- xem changelog
- kiểm tra breaking changes

---

## 4. Audit security thường xuyên

Ví dụ:

```bash
npm audit
safety check
```

---

## 5. Giảm số lượng dependency

Nguyên tắc:

```text
Chỉ cài dependency khi thực sự cần.
```

Mỗi dependency mới có thể mang theo:

- security risk
- performance overhead
- maintenance cost

---

## Lỗi thường gặp

| Lỗi                   | Nguyên nhân             | Cách sửa           |
| --------------------- | ----------------------- | ------------------ |
| Works on my machine   | dependency khác version | commit lock file   |
| Build fail trên CI    | thiếu dependency        | update lock file   |
| Vulnerable dependency | package cũ              | upgrade dependency |

---

## Bài tập

### Bài 1

Tạo project Node.js và:

```bash
npm install express
```

Sau đó xem:

```bash
npm outdated
```

---

### Bài 2

Tạo project Python:

```bash
pip install flask requests
```

Export:

```bash
pip freeze > requirements.txt
```

---

### Bài 3

Tìm một dependency có **security vulnerability** và cập nhật nó.

---

## Tài liệu tham khảo

```text
https://semver.org/
```

```text
https://docs.npmjs.com/cli/v10/commands/npm-audit
```


<div class="pdf-page-break"></div>

<!-- Source: backend/http-rest.md -->

﻿# HTTP & REST API

HTTP là giao thức nền tảng của web.
REST API là cách phổ biến để xây dựng **backend services** cho web và mobile applications.

Trang này giới thiệu:

- HTTP request / response
- HTTP methods và status codes
- nguyên tắc thiết kế REST API
- cách gọi API bằng `curl`

---

## Mục tiêu

Sau bài này bạn có thể:

- hiểu cách **HTTP hoạt động**
- sử dụng các HTTP methods phổ biến
- thiết kế **REST API endpoints**
- test API bằng **curl**

---

## Yêu cầu

Bạn cần có **terminal**.

Nếu chưa quen command line:

```text
Terminal cơ bản
```

---

## HTTP hoạt động thế nào

> So do duoc luoc bo trong ban PDF. Xem ban web neu can hinh minh hoa.

---

## Cấu trúc HTTP Request

Một request HTTP gồm:

```text
Method
URL
Headers
Body
```

Ví dụ:

```http
POST /api/users HTTP/1.1
Host: api.internhub.local
Content-Type: application/json
Authorization: Bearer <token>
```

Body:

```json
{
  "name": "Minh Nguyen",
  "email": "minh@internhub.local"
}
```

---

## HTTP Methods

| Method | Mục đích          | Idempotent |
| ------ | ----------------- | ---------- |
| GET    | lấy dữ liệu       | Có         |
| POST   | tạo mới           | Không      |
| PUT    | cập nhật toàn bộ  | Có         |
| PATCH  | cập nhật một phần | Có         |
| DELETE | xoá               | Có         |

---

### Ví dụ

```text
GET    /api/users
POST   /api/users
PUT    /api/users/1
PATCH  /api/users/1
DELETE /api/users/1
```

---

## HTTP Status Codes

HTTP response luôn có **status code**.

---

## 2xx – Success

| Code | Ă nghĩa    |
| ---- | ---------- |
| 200  | OK         |
| 201  | Created    |
| 204  | No Content |

---

## 3xx – Redirect

| Code | Ă nghĩa           |
| ---- | ----------------- |
| 301  | Moved Permanently |
| 304  | Not Modified      |

---

## 4xx – Client Error

| Code | Ă nghĩa      |
| ---- | ------------ |
| 400  | Bad Request  |
| 401  | Unauthorized |
| 403  | Forbidden    |
| 404  | Not Found    |

---

## 5xx – Server Error

| Code | Ă nghĩa               |
| ---- | --------------------- |
| 500  | Internal Server Error |
| 503  | Service Unavailable   |

---

## REST API Design

REST API sử dụng **resource-based URLs**.

---

## Endpoint chuẩn

```text
GET    /api/users
GET    /api/users/42
POST   /api/users
PUT    /api/users/42
DELETE /api/users/42
```

---

### Resource nested

```text
GET /api/users/42/posts
```

---

## Quy tắc thiết kế API

- dùng **danh từ số nhiều**

```text
/users
/products
/orders
```

---

- dùng **kebab-case**

```text
/order-items
```

---

- không dùng động từ trong URL

âŒ Sai:

```text
/api/getUsers
/api/createUser
```

---

## Gọi API bằng curl

`curl` là công cụ CLI để gọi HTTP API.

---

## GET request

```bash
curl http://localhost:3000/api/users
```

---

## GET với header

```bash
curl -H "Authorization: Bearer <token>" \
http://localhost:3000/api/users
```

---

## POST JSON

```bash
curl -X POST http://localhost:3000/api/users \
-H "Content-Type: application/json" \
-d '{"name":"Minh Nguyen","email":"minh@internhub.local"}'
```

---

## PUT request

```bash
curl -X PUT http://localhost:3000/api/users/1 \
-H "Content-Type: application/json" \
-d '{"name":"John Updated"}'
```

---

## DELETE request

```bash
curl -X DELETE http://localhost:3000/api/users/1
```

---

## Xem headers

```bash
curl -I http://localhost:3000/api/users
```

---

## Debug request

```bash
curl -v http://localhost:3000/api/users
```

---

## JSON Request / Response

---

## Request

```json
{
  "name": "Nguyễn Văn A",
  "email": "a.nguyen@example.com",
  "role": "intern"
}
```

---

## Response

```json
{
  "id": 42,
  "name": "Nguyễn Văn A",
  "email": "a.nguyen@example.com",
  "role": "intern",
  "createdAt": "2025-01-15T10:30:00Z"
}
```

---

## Error Response

Một API tốt nên trả lỗi theo format thống nhất.

---

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Email is required",
    "details": [
      {
        "field": "email",
        "message": "must not be empty"
      }
    ]
  }
}
```

---

## Lỗi thường gặp

| Lỗi                | Nguyên nhân             | Cách sửa        |
| ------------------ | ----------------------- | --------------- |
| connection refused | server chưa chạy        | kiểm tra port   |
| 401 Unauthorized   | thiếu token             | kiểm tra header |
| 404 Not Found      | endpoint sai            | kiểm tra URL    |
| CORS error         | server chưa enable CORS | thêm middleware |

---

## Bài tập

### Bài 1

Dùng `curl` gọi API:

```text
GET /api/users
```

---

### Bài 2

Tạo request POST:

```text
POST /api/users
```

Body:

```json
{
  "name": "Test User"
}
```

---

### Bài 3

Test các status codes:

```text
200
404
500
```

---

## Tài liệu tham khảo

```
https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
```

```
https://restfulapi.net/
```


<div class="pdf-page-break"></div>

<!-- Source: backend/api-testing.md -->

﻿# API Testing

## Mục tiêu

Sau bài này, bạn sẽ:

- Sử dụng **Postman** / **Thunder Client** để test API.
- Viết test assertions cơ bản trong Postman.
- Sử dụng **curl** và **httpie** từ terminal.

## Prerequisites

- HTTP & REST API.

---

## Postman

InternHub API là sample app xuyên suốt trong handbook này, vì vậy bạn có thể import collection mẫu
và dùng lại ở các bài Docker, SQL và deployment.

### Cài đặt

- Tải từ [https://www.postman.com/downloads/](https://www.postman.com/downloads/)
- Hoặc dùng **Thunder Client** (VS Code extension) cho nhẹ hơn.

### Tạo Request

1. Click **New → HTTP Request**.
2. Chọn method: `GET`, `POST`, …
3. Nhập URL: `http://localhost:3000/api/users`.
4. Tab **Body** → `raw` → `JSON` (cho POST/PUT).
5. Click **Send**.

### Postman Collections

- Nhóm các request liên quan vào **Collection**.
- Export/import dưới dạng JSON (`resources/api/postman-collection.json`).
- Collection mẫu này được đặt tên **InternHub API** và dùng `base_url=http://localhost:3000`.

### Biến môi trường (Environment)

```json
// Tạo Environment "Development"
{
  "base_url": "http://localhost:3000",
  "token": "eyJhbGciOiJI..."
}
```

Sử dụng trong request: `{{base_url}}/api/users`

### Viết Test trong Postman

```javascript
// Tab "Tests" trong Postman
pm.test("Status code is 200", function () {
  pm.response.to.have.status(200);
});

pm.test("Response has users array", function () {
  const body = pm.response.json();
  pm.expect(body).to.be.an("array");
  pm.expect(body.length).to.be.greaterThan(0);
});

pm.test("Response time < 500ms", function () {
  pm.expect(pm.response.responseTime).to.be.below(500);
});
```

---

## httpie (thay thế curl, dễ đọc hơn)

```bash
# Cài
pip install httpie

# GET
http GET localhost:3000/api/users

# POST JSON (tự detect Content-Type)
http POST localhost:3000/api/users name="John" email="john@test.com"

# Với header
http GET localhost:3000/api/users Authorization:"Bearer <token>"
```

---

## Test API tự động

### Với pytest (Python)

```python
import requests

BASE_URL = "http://localhost:3000/api"

def test_get_users():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_create_user():
    payload = {"name": "Test", "email": "test@test.com"}
    response = requests.post(f"{BASE_URL}/users", json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "Test"
```

```bash
pytest tests/test_api.py -v
```

---

## Lỗi thường gặp

| Lỗi                              | Nguyên nhân                        | Cách sửa                                    |
| -------------------------------- | ---------------------------------- | ------------------------------------------- |
| Postman trả về HTML thay vì JSON | URL sai hoặc server trả error page | Kiểm tra URL, xem server log                |
| `Could not send request`         | Server chưa chạy                   | Start server trước                          |
| SSL certificate error            | Self-signed cert                   | Tắt SSL verification trong Postman settings |

---

## Tài liệu tham khảo

- [Postman Learning Center](https://learning.postman.com/)
- [httpie Docs](https://httpie.io/docs)


<div class="pdf-page-break"></div>

<!-- Source: databases/sql-postgres.md -->

# SQL & PostgreSQL

Trang này là mục lục cho cụm bài SQL/PostgreSQL. Nội dung đã được tách thành 3 bài để phân biệt rõ setup, CRUD và tối ưu/cơ chế giao dịch.

---

## Mục tiêu

Sau cụm bài này, bạn có thể:

- chạy PostgreSQL bằng Docker và kết nối bằng CLI/GUI
- viết truy vấn CRUD cơ bản
- hiểu index, transaction và một số công cụ `psql`

---

## Prerequisites

- Đã hoàn thành: Quickstart
- Đã biết Docker cơ bản: Docker cơ bản

---

## Lộ trình học

1. Cài đặt và Kết nối PostgreSQL
2. SQL CRUD cơ bản
3. Index, Transaction và Tối ưu SQL

---

## Gợi ý học

- Chạy database mẫu trước khi học CRUD
- Tự gõ lại truy vấn thay vì chỉ copy/paste
- Dùng `EXPLAIN ANALYZE` ở phần nâng cao để tập đọc execution plan

---

## Tài liệu liên quan

- MongoDB & Redis
- SQL Cheat Sheet
- File mẫu trong repo: `resources/database/sample-schema.sql`


<div class="pdf-page-break"></div>

<!-- Source: databases/postgres-setup.md -->

﻿# Cài Đặt Và Kết Nối PostgreSQL

Phần này hướng dẫn chạy PostgreSQL bằng Docker và kết nối bằng CLI hoặc GUI.

---

## Chạy PostgreSQL bằng Docker

Cách nhanh nhất để chạy PostgreSQL là dùng container.

```bash
docker run -d \
--name postgres-dev \
-e POSTGRES_USER=dev \
-e POSTGRES_PASSWORD=dev123 \
-e POSTGRES_DB=internhub \
-p 5432:5432 \
-v pgdata:/var/lib/postgresql/data \
postgres:16-alpine
```

---

### Kiểm tra container

```bash
docker ps
```

---

### Kết nối bằng psql

```bash
docker exec -it postgres-dev psql -U dev -d internhub
```

---

## Kết nối bằng GUI

Developer thường dùng GUI tool để quản lý database.

---

## DBeaver

Tải:

```
https://dbeaver.io/download/
```

---

### Tạo connection

Thông tin kết nối:

| Field    | Value     |
| -------- | --------- |
| Host     | localhost |
| Port     | 5432      |
| Database | internhub |
| User     | dev       |
| Password | dev123    |

---


<div class="pdf-page-break"></div>

<!-- Source: databases/sql-crud.md -->

﻿# SQL CRUD Cơ Bản

Phần này gom các thao tác tạo bảng, thêm dữ liệu, truy vấn, cập nhật và xoá.

---

## SQL cơ bản

---

## Tạo bảng

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    role VARCHAR(50) DEFAULT 'intern',
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

```sql
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    content TEXT,
    published BOOLEAN DEFAULT false,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## INSERT

```sql
INSERT INTO users (name, email, role)
VALUES
('Nguyễn Văn A','a.nguyen@example.com','intern'),
('Trần Thị B','b.tran@example.com','developer'),
('Lê Văn C','c.le@example.com','lead');
```

---

```sql
INSERT INTO posts (user_id, title, content, published)
VALUES
(1,'First Post','Hello World!',true),
(2,'Docker Guide','Docker is awesome...',true),
(1,'Draft Post','Work in progress...',false);
```

---

## SELECT

---

### Lấy tất cả dữ liệu

```sql
SELECT * FROM users;
```

---

### Lấy cột cụ thể

```sql
SELECT name, email
FROM users
WHERE role = 'intern';
```

---

### Sắp xếp

```sql
SELECT *
FROM users
ORDER BY created_at DESC;
```

---

### Giới hạn kết quả

```sql
SELECT *
FROM users
LIMIT 10 OFFSET 0;
```

---

### GROUP BY

```sql
SELECT role, COUNT(*)
FROM users
GROUP BY role;
```

---

### Tìm kiếm text

```sql
SELECT *
FROM users
WHERE name ILIKE '%nguyen%';
```

---

## JOIN

JOIN giúp kết hợp dữ liệu từ nhiều bảng.

---

## INNER JOIN

```sql
SELECT u.name, p.title
FROM users u
INNER JOIN posts p
ON u.id = p.user_id;
```

---

## LEFT JOIN

```sql
SELECT u.name, COUNT(p.id) AS post_count
FROM users u
LEFT JOIN posts p
ON u.id = p.user_id
GROUP BY u.name;
```

---

## UPDATE

```sql
UPDATE users
SET role = 'developer'
WHERE id = 1;
```

---

## DELETE

```sql
DELETE FROM posts
WHERE id = 3;
```

---

!!! danger "Cảnh báo"
Luôn kiểm tra điều kiện trước khi chạy:

```sql
UPDATE
DELETE
```

Nên chạy:

```sql
SELECT
```

trước để đảm bảo query đúng.

---


<div class="pdf-page-break"></div>

<!-- Source: databases/sql-advanced.md -->

﻿# Index, Transaction Và Tối Ưu SQL

Phần này đi qua index, transaction, psql cheat sheet và phần tự luyện cuối chương.

---

## Index

Index giúp **tăng tốc truy vấn**.

---

### Tạo index

```sql
CREATE INDEX idx_users_email
ON users(email);
```

---

```sql
CREATE INDEX idx_posts_user_id
ON posts(user_id);
```

---

### Phân tích query

```sql
EXPLAIN ANALYZE
SELECT * FROM users
WHERE email = 'a.nguyen@example.com';
```

---

## Transaction

Transaction đảm bảo **atomic operations**.

---

```sql
BEGIN;

UPDATE users
SET role = 'senior'
WHERE id = 1;

INSERT INTO posts (user_id,title)
VALUES (1,'Promoted!');

COMMIT;
```

---

Nếu có lỗi:

```sql
ROLLBACK;
```

---

## psql Cheat Sheet

| Command       | Mô tả                |
| ------------- | -------------------- |
| `\l`          | danh sách database   |
| `\dt`         | danh sách table      |
| `\d users`    | schema table         |
| `\x`          | toggle expanded view |
| `\q`          | exit                 |
| `\i file.sql` | chạy file SQL        |

---

## Lỗi thường gặp

| Lỗi                     | Nguyên nhân          | Cách sửa          |
| ----------------------- | -------------------- | ----------------- |
| connection refused      | PostgreSQL chưa chạy | start container   |
| relation does not exist | chưa tạo table       | chạy CREATE TABLE |
| duplicate key           | dữ liệu trùng        | dùng unique check |
| permission denied       | user thiếu quyền     | GRANT permissions |

---

## Bài tập

### Bài 1

Tạo bảng:

```
products
```

Columns:

```
id
name
price
stock
category
```

---

### Bài 2

Insert 5 sản phẩm và query:

```
price > 100000
stock > 0
```

---

### Bài 3

JOIN:

```
users + posts
```

đếm số bài viết mỗi user.

---

## Tài liệu tham khảo

```
https://www.postgresqltutorial.com/
```

```
https://sqlbolt.com/
```


<div class="pdf-page-break"></div>

<!-- Source: databases/mongodb-redis.md -->

﻿# MongoDB & Redis

## Mục tiêu

Sau bài này, bạn sẽ:

- Hiểu khi nào dùng NoSQL (MongoDB) vs SQL.
- CRUD cơ bản với MongoDB.
- Sử dụng Redis làm cache / session store.
- Chạy cả hai bằng Docker.

## Prerequisites

- Docker cơ bản.

---

## MongoDB

### Chạy bằng Docker

```bash
docker run -d \
  --name mongo-dev \
  -e MONGO_INITDB_ROOT_USERNAME=admin \
  -e MONGO_INITDB_ROOT_PASSWORD=admin123 \
  -p 27017:27017 \
  -v mongodata:/data/db \
  mongo:7
```

### Kết nối bằng mongosh

```bash
docker exec -it mongo-dev mongosh -u admin -p admin123
```

### CRUD cơ bản

```javascript
// Chọn database
use internhub

// Insert
db.users.insertOne({ name: "Văn A", email: "a@test.com", age: 22 })
db.users.insertMany([
  { name: "Thị B", email: "b@test.com", age: 23 },
  { name: "Văn C", email: "c@test.com", age: 21 }
])

// Find
db.users.find()                           // Tất cả
db.users.find({ age: { $gte: 22 } })      // age >= 22
db.users.findOne({ email: "a@test.com" })  // 1 document

// Update
db.users.updateOne(
  { email: "a@test.com" },
  { $set: { age: 23, role: "intern" } }
)

// Delete
db.users.deleteOne({ email: "c@test.com" })

// Count
db.users.countDocuments({ age: { $gte: 22 } })
```

### Khi nào dùng MongoDB vs PostgreSQL?

|              | MongoDB               | PostgreSQL                |
| ------------ | --------------------- | ------------------------- |
| Schema       | Flexible (schemaless) | Fixed (strict schema)     |
| Relationship | Embedded documents    | Foreign keys + JOINs      |
| Phù hợp      | Logs, CMS, real-time  | E-commerce, finance, CRUD |
| Query        | Document-based        | SQL                       |
| Transaction  | Có (từ v4.0)          | Có (native, mạnh hơn)     |

---

## Redis

### Chạy bằng Docker

```bash
docker run -d \
  --name redis-dev \
  -p 6379:6379 \
  redis:7-alpine
```

### Lệnh cơ bản

```bash
# Kết nối redis-cli
docker exec -it redis-dev redis-cli

# String
SET user:1:name "Nguyen Van A"
GET user:1:name

# Expiry (TTL)
SET session:abc123 "user_data" EX 3600    # Hết hạn sau 1 giờ
TTL session:abc123                         # Xem thời gian còn lại

# Hash (object-like)
HSET user:1 name "Van A" email "a@test.com" role "intern"
HGETALL user:1
HGET user:1 email

# List
LPUSH queue:emails "email1" "email2"
RPOP queue:emails

# Set
SADD tags:post:1 "docker" "devops" "linux"
SMEMBERS tags:post:1

# Xoá key
DEL user:1:name

# Xem tất cả keys (chỉ dùng khi dev!)
KEYS *
```

### Use cases phổ biến

| Use case          | Cách dùng                             |
| ----------------- | ------------------------------------- |
| **Cache**         | Cache API response, giảm load DB      |
| **Session store** | Lưu session thay vì file/memory       |
| **Rate limiting** | Đếm request per IP bằng INCR + EXPIRE |
| **Queue**         | Task queue đơn giản (LPUSH/RPOP)      |
| **Real-time**     | Pub/Sub cho notifications             |

---

## Lỗi thường gặp

| Lỗi                                       | Nguyên nhân                    | Cách sửa                      |
| ----------------------------------------- | ------------------------------ | ----------------------------- |
| `MongoServerError: Authentication failed` | Sai user/password              | Kiểm tra biến MONGO_INITDB    |
| `WRONGTYPE Operation` (Redis)             | Dùng sai command cho data type | Kiểm tra type bằng `TYPE key` |
| Data mất sau restart                      | Không mount volume             | Thêm `-v` khi `docker run`    |

---

## Tài liệu tham khảo

- [MongoDB Manual](https://www.mongodb.com/docs/manual/)
- [Redis Commands](https://redis.io/commands)
- [Try Redis (interactive)](https://try.redis.io/)


<div class="pdf-page-break"></div>

<!-- Source: containers/docker.md -->

# Docker cơ bản

Trang này là mục lục cho cụm bài Docker. Nội dung được tách thành các bài nhỏ để người học đi từng bước từ runtime, sang debug/storage, rồi đến Dockerfile/build.

---

## Mục tiêu

Sau cụm bài này, bạn có thể:

- hiểu image, container, volume và network
- chạy và quản lý container bằng `docker run`
- đọc logs, debug container và làm việc với volume
- build image bằng Dockerfile

---

## Prerequisites

- Đã hoàn thành: Quickstart
- Đã biết terminal cơ bản: Terminal & Shell

---

## Lộ trình học

1. Docker Runtime cơ bản
2. Debug, Logs và Storage trong Docker
3. Dockerfile và Build Workflow
4. Docker Compose

---

## Gợi ý học

- Mỗi bài nên được thực hành bằng terminal và Docker Desktop/WSL
- Sau khi học xong phần runtime, chạy lại các lệnh debug trên container thật
- Chỉ chuyển sang Dockerfile sau khi đã quen với image và container

---

## Tài liệu liên quan

- Docker Compose
- Docker Cheat Sheet
- Deployment cơ bản


<div class="pdf-page-break"></div>

<!-- Source: containers/docker-runtime.md -->

﻿# Docker Runtime Cơ Bản

Phần này tập trung vào image, container và các thao tác chạy container.

---

## Khái niệm cốt lõi

> So do duoc luoc bo trong ban PDF. Xem ban web neu can hinh minh hoa.

---

| Thành phần | Ă nghĩa                      |
| ---------- | ---------------------------- |
| Image      | template chỉ đọc chứa app    |
| Container  | instance đang chạy của image |
| Volume     | storage persistent           |
| Network    | mạng giữa containers         |

---

## Ví dụ dễ hiểu

| Docker    | Thực tế              |
| --------- | -------------------- |
| Image     | file cài đặt Windows |
| Container | máy đã cài Windows   |
| Volume    | ổ USB                |
| Network   | LAN                  |

---

## Chạy container

Ví dụ đơn giản nhất:

```bash
docker run hello-world
```

Docker sẽ:

1. pull image
2. tạo container
3. chạy container

---

## Chạy container với options

```bash
docker run -d \
--name my-nginx \
-p 8080:80 \
-v $(pwd)/html:/usr/share/nginx/html \
nginx:alpine
```

---

## Giải thích

| Option   | Ă nghĩa           |
| -------- | ----------------- |
| `-d`     | chạy background   |
| `--name` | đặt tên container |
| `-p`     | port mapping      |
| `-v`     | mount volume      |

---

Sau khi chạy:

```
http://localhost:8080
```

---

## Quản lý container

---

## Xem container

```bash
docker ps
```

---

Xem cả container đã stop:

```bash
docker ps -a
```

---

## Stop container

```bash
docker stop my-nginx
```

---

## Start container

```bash
docker start my-nginx
```

---

## Restart

```bash
docker restart my-nginx
```

---

## Remove container

```bash
docker rm my-nginx
```

---

Force remove:

```bash
docker rm -f my-nginx
```

---


<div class="pdf-page-break"></div>

<!-- Source: containers/docker-debug-storage.md -->

﻿# Debug, Logs Và Storage Trong Docker

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


<div class="pdf-page-break"></div>

<!-- Source: containers/dockerfile-workflow.md -->

﻿# Dockerfile Và Build Workflow

Phần này tập trung vào Dockerfile, build image, port mapping và phần tự luyện cuối chương.

---

## Dockerfile

Dockerfile dùng để **build image**.

---

## Ví dụ Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "main.py"]
```

---

## Build image

```bash
docker build -t internhub-api:1.0 .
```

---

## Chạy image

```bash
docker run -d -p 8000:8000 --name internhub-api internhub-api:1.0
```

---

## Best Practices Dockerfile

---

### 1. Dùng base image nhỏ

```dockerfile
python:3.11-slim
```

---

### 2. Copy dependencies trước

```dockerfile
COPY requirements.txt .
RUN pip install
```

---

### 3. Gộp RUN commands

```dockerfile
RUN apt update && apt install -y curl
```

---

### 4. Dùng `.dockerignore`

```
.git
node_modules
.venv
__pycache__
.env
```

---

## Port Mapping

```
Host                Container
localhost:8080 ---> container:80
```

---

Ví dụ:

```bash
docker run -p 8080:80 nginx
```

---

Random port:

```bash
docker run -P nginx
```

---

## Lỗi thường gặp

| Lỗi                    | Nguyên nhân      | Cách sửa            |
| ---------------------- | ---------------- | ------------------- |
| port already allocated | port bị dùng     | đổi port            |
| no space left          | docker đầy disk  | docker system prune |
| COPY failed            | sai path         | kiểm tra context    |
| container exit         | process crash    | docker logs         |
| exec format error      | sai architecture | build đúng platform |

---

## Dọn dẹp Docker

Xoá resources không dùng:

```bash
docker system prune -a --volumes
```

---

Xem disk usage:

```bash
docker system df
```

---

## Bài tập

### Bài 1

Chạy nginx:

```bash
docker run -p 8080:80 nginx:alpine
```

Mở:

```
http://localhost:8080
```

---

### Bài 2

Viết Dockerfile cho Flask app.

---

### Bài 3

Vào container nginx:

```bash
docker exec -it nginx sh
```

sửa file:

```
/usr/share/nginx/html/index.html
```

---

## Tài liệu tham khảo

```
https://docs.docker.com/get-started/
```

```
https://docs.docker.com/reference/dockerfile/
```


<div class="pdf-page-break"></div>

<!-- Source: containers/docker-compose.md -->

﻿# Docker Compose

## Mục tiêu

Sau bài này, bạn sẽ:

- Viết file `docker-compose.yml` cho multi-container app.
- Quản lý stack: web + database + cache.
- Sử dụng networks, volumes, environment variables.
- Áp dụng cho môi trường development.

## Prerequisites

- Docker cơ bản.

---

## Tại sao cần Docker Compose?

Thay vì chạy nhiều lệnh `docker run`:

```bash
# Không dùng Compose – phải chạy từng container
docker run -d --name db -e POSTGRES_PASSWORD=secret postgres:16
docker run -d --name redis redis:7
docker run -d --name internhub-api -p 3000:3000 --link db --link redis internhub-api
```

Dùng Compose – **1 file, 1 lệnh**:

```bash
docker compose up -d
```

---

## Cấu trúc docker-compose.yml

```yaml
# docker-compose.yml
services:
  # === Web Application ===
  web:
    build: . # Build từ Dockerfile ở thư mục hiện tại
    ports:
      - "3000:3000" # Map port
    environment:
      - DATABASE_URL=postgres://dev:dev123@db:5432/internhub
      - REDIS_URL=redis://redis:6379
      - NODE_ENV=development
    volumes:
      - ./src:/app/src # Bind mount cho live reload
    depends_on:
      - db
      - redis
    restart: unless-stopped

  # === Database ===
  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: dev
      POSTGRES_PASSWORD: dev123
      POSTGRES_DB: internhub
    ports:
      - "5432:5432" # Expose để connect bằng DBeaver
    volumes:
      - pgdata:/var/lib/postgresql/data
      - ./resources/database/sample-schema.sql:/docker-entrypoint-initdb.d/init.sql

  # === Cache ===
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redisdata:/data

# Named volumes
volumes:
  pgdata:
  redisdata:
```

---

## Lệnh Docker Compose

```bash
# Khởi động tất cả services (foreground)
docker compose up

# Khởi động ở background
docker compose up -d

# Xem trạng thái
docker compose ps

# Xem logs
docker compose logs
docker compose logs -f web         # Follow logs của service "web"

# Dừng tất cả
docker compose stop

# Dừng + xoá containers
docker compose down

# Dừng + xoá containers + volumes (MẤT DATA!)
docker compose down -v

# Rebuild images
docker compose build
docker compose up -d --build       # Build lại rồi start

# Chạy lệnh trong service
docker compose exec web bash
docker compose exec db psql -U dev -d internhub

# Scale service (chạy nhiều instance)
docker compose up -d --scale web=3
```

---

## Ví dụ: Full Stack App

```yaml
# docker-compose.yml cho project thực tế
services:
  # Frontend (React)
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile.dev
    ports:
      - "5173:5173"
    volumes:
      - ./frontend/src:/app/src
    environment:
      - VITE_API_URL=http://localhost:3000

  # Backend (Node.js)
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile.dev
    ports:
      - "3000:3000"
    volumes:
      - ./backend/src:/app/src
    environment:
      - DATABASE_URL=postgres://dev:dev123@db:5432/internhub
      - REDIS_URL=redis://redis:6379
      - JWT_SECRET=dev-secret-key
    depends_on:
      db:
        condition: service_healthy

  # Database
  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: dev
      POSTGRES_PASSWORD: dev123
      POSTGRES_DB: internhub
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U dev -d internhub"]
      interval: 5s
      timeout: 5s
      retries: 5

  # Cache
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

  # Admin tool (pgAdmin)
  pgadmin:
    image: dpage/pgadmin4
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@admin.com
      PGADMIN_DEFAULT_PASSWORD: admin
    ports:
      - "5050:80"
    depends_on:
      - db

volumes:
  pgdata:
```

---

## Network trong Compose

- Compose tự tạo **default network** cho stack.
- Các service giao tiếp qua **tên service**: `db`, `redis`, `web`.
- Không cần IP, Docker DNS tự resolve.

```yaml
# web kết nối db bằng hostname "db"
DATABASE_URL=postgres://dev:dev123@db:5432/internhub
#                                   ^^
#                              Tên service = hostname
```

---

## Environment Variables

### Cách 1 – Inline trong compose

```yaml
environment:
  - NODE_ENV=development
  - PORT=3000
```

### Cách 2 – Dùng file .env

```yaml
# docker-compose.yml
services:
  web:
    env_file:
      - .env
```

```env
# .env
NODE_ENV=development
PORT=3000
DATABASE_URL=postgres://dev:dev123@db:5432/internhub
```

### Cách 3 – Biến thay thế trong compose

```yaml
# docker-compose.yml
services:
  db:
    image: postgres:${POSTGRES_VERSION:-16}-alpine
```

```bash
# Chạy với biến
POSTGRES_VERSION=15 docker compose up -d
```

---

## Lỗi thường gặp

| Lỗi                                                  | Nguyên nhân      | Cách sửa                                                 |
| ---------------------------------------------------- | ---------------- | -------------------------------------------------------- |
| `service "web" depends on "db" which is not healthy` | DB chưa sẵn sàng | Thêm healthcheck cho db                                  |
| `address already in use`                             | Port bị chiếm    | Stop container/process cũ, đổi port                      |
| Volume data bị cũ                                    | Cache image cũ   | `docker compose down -v && docker compose up -d --build` |
| Container restart liên tục                           | App crash loop   | Xem logs: `docker compose logs web`                      |

---

## Bài tập

1. Viết `docker-compose.yml` cho: Express API + PostgreSQL + Redis.
2. Thêm healthcheck cho PostgreSQL.
3. Dùng `docker compose exec` để chạy `psql` và tạo bảng.

---

## Tài liệu tham khảo

- [Docker Compose Overview](https://docs.docker.com/compose/)
- [Compose File Reference](https://docs.docker.com/compose/compose-file/)


<div class="pdf-page-break"></div>

<!-- Source: devops/cicd-github-actions.md -->

# CI/CD - GitHub Actions

Trang này là mục lục cho cụm bài CI/CD. Nội dung đã được tách ra để người học đi từ khái niệm và quy tắc team, sang implementation cho Node/Python, rồi đến release và debugging.

---

## Mục tiêu

Sau cụm bài này, bạn có thể:

- hiểu CI/CD và vai trò của nó trong quy trình PR
- viết workflow cơ bản cho Node.js và Python
- quản lý secrets, matrix build và release workflow
- debug workflow khi fail

---

## Prerequisites

- Đã học: GitHub Workflow
- Đã biết Docker cơ bản nếu cần build image: Docker cơ bản

---

## Lộ trình học

1. CI/CD Fundamentals
2. CI cho Node.js và Python
3. Secrets, Release và Debug Workflow

---

## Gợi ý học

- Không nên học release pipeline trước khi đã chạy được workflow tối thiểu
- Tự tạo một repo demo nhỏ để tập `pull_request -> lint -> test -> build`
- Chỉ đưa thêm Docker release sau khi đã ổn định pipeline cơ bản

---

## Tài liệu liên quan

- Deployment cơ bản
- Bảo mật cơ bản
- GitHub Workflow


<div class="pdf-page-break"></div>

<!-- Source: devops/ci-basics.md -->

﻿# CI/CD Fundamentals

Phần này giới thiệu CI/CD, cấu trúc workflow và quy tắc pipeline cơ bản.

---

## CI/CD là gì?

> So do duoc luoc bo trong ban PDF. Xem ban web neu can hinh minh hoa.

| Thuật ngữ                           | Ý nghĩa                                                      |
| ----------------------------------- | ------------------------------------------------------------ |
| CI (Continuous Integration)         | tự động lint/test/build khi push/PR                          |
| CD (Continuous Delivery/Deployment) | tự động deploy sau khi CI pass (tuỳ mức tự động)             |
| Workflow                            | file YAML mô tả pipeline                                     |
| Job                                 | nhóm step chạy trên 1 runner                                 |
| Step                                | 1 hành động trong job (checkout, setup runtime, run command) |

---

## Cấu trúc thư mục chuẩn

```text
.github/
└── workflows/
    ├── ci.yml
    ├── docker.yml
    ├── deploy.yml
    └── docs.yml
```

---

## Quy tắc CI "chuẩn team"

- CI chạy trên **Pull Request** là quan trọng nhất
- PR chỉ được merge khi **CI xanh**
- Workflow nên:
  - **nhanh**
  - **deterministic** (không phụ thuộc máy dev)
  - **cache tốt**
  - **fail sớm** (lint trước test)

---

## Quickstart: Workflow tối thiểu

Tạo file:

```text
.github/workflows/ci.yml
```

Mẫu skeleton:

```yaml
name: CI

on:
  pull_request:
  push:
    branches: [main]

jobs:
  ci:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: CI placeholder
        run: echo "Hello CI"
```

---


<div class="pdf-page-break"></div>

<!-- Source: devops/ci-node-python.md -->

﻿# CI Cho Node.js Và Python

Phần này gom workflow tối thiểu, pipeline Node.js, Python và matrix builds.

---

## CI cho Node.js

Mục tiêu: **install → lint → test → build** (dùng `npm ci` và cache).

```yaml
# .github/workflows/ci.yml
name: CI (Node.js)

on:
  pull_request:
    branches: [main]
  push:
    branches: [main, develop]

permissions:
  contents: read

jobs:
  node-ci:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: npm

      - name: Install deps
        run: npm ci

      - name: Lint
        run: npm run lint --if-present

      - name: Test
        run: npm test --if-present

      - name: Build
        run: npm run build --if-present
```

**Gợi ý chuẩn repo Node.js**

- `npm ci` (dùng lockfile) → build “reproducibleâ€
- dùng `--if-present` để workflow không fail nếu repo chưa có script đó

---

## CI cho Python

Mục tiêu: **install → lint → test**, có thể chạy kèm PostgreSQL service.

```yaml
# .github/workflows/ci-python.yml
name: CI (Python)

on:
  pull_request:
    branches: [main]
  push:
    branches: [main]

permissions:
  contents: read

jobs:
  py-test:
    runs-on: ubuntu-latest

    services:
      postgres:
        image: postgres:16-alpine
        env:
          POSTGRES_USER: test
          POSTGRES_PASSWORD: test
          POSTGRES_DB: testdb
        ports:
          - 5432:5432
        options: >-
          --health-cmd "pg_isready -U test -d testdb"
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
          cache: pip

      - name: Install deps
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          # nếu có file dev:
          # pip install -r requirements-dev.txt

      - name: Lint
        run: |
          # ví dụ (tuỳ project)
          # ruff check .
          # black --check .
          echo "Lint step"

      - name: Test
        env:
          DATABASE_URL: postgres://test:test@localhost:5432/testdb
        run: |
          # ví dụ:
          # pytest -q
          echo "Test step"
```

**Gợi ý:** Với Python hiện đại, team hay dùng `ruff + black + pytest`.

---

## Matrix builds (test nhiều phiên bản)

Khi team cần hỗ trợ nhiều Node/Python versions hoặc nhiều OS.

## Node.js matrix (18/20/22)

```yaml
name: CI (Node matrix)

on:
  pull_request:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        node: [18, 20, 22]

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node }}
          cache: npm

      - run: npm ci
      - run: npm test --if-present
```

## Multi-OS matrix (khi thật sự cần)

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest]
    node: [20]
runs-on: ${{ matrix.os }}
```

> Lưu ý: Multi-OS làm CI chậm và tốn runner minutes — chỉ dùng khi dự án cần.

---


<div class="pdf-page-break"></div>

<!-- Source: devops/ci-release-debug.md -->

﻿# Secrets, Release Và Debug Workflow

Phần này tập trung vào secrets, release pipeline, debug và phần tự luyện cuối chương.

---

## Secrets

Secrets dùng cho token, password, credentials.

Ví dụ dùng secret trong step:

```yaml
- name: Deploy
  env:
    DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}
  run: ./deploy.sh
```

Cách thêm secret:

- Repo → **Settings**
- **Secrets and variables** → **Actions**
- **New repository secret**

!!! danger "Quan trọng"
Không hardcode secrets trong YAML hoặc code. Không commit `.env` lên Git.

---

## Build & Push Docker Image (theo tag)

Workflow: push tag `v*` → build → push Docker Hub (hoặc GHCR).

```yaml
# .github/workflows/docker.yml
name: Docker Build & Push

on:
  push:
    tags: ["v*"]

permissions:
  contents: read

jobs:
  build-and-push:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Login Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}

      - name: Build & Push
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: |
            myorg/internhub-api:latest
            myorg/internhub-api:${{ github.ref_name }}
```

**Best practice**

- chỉ build/push khi **tag** hoặc **merge main**
- tag theo version để rollback dễ

---

## Debugging workflow

## 1) In thông tin runner/event

```yaml
- name: Debug info
  run: |
    echo "Event: ${{ github.event_name }}"
    echo "Ref: ${{ github.ref }}"
    echo "SHA: ${{ github.sha }}"
    echo "Runner OS: ${{ runner.os }}"
```

## 2) Xem log

- Repo → tab **Actions** → chọn run → chọn job/step bị fail

## 3) Re-run

- **Re-run jobs** khi lỗi do network/flake

## 4) SSH debug (chỉ khi thật cần)

Có thể dùng `mxschmitt/action-tmate` để mở session debug (cẩn thận quyền và secrets).

---

## Lỗi thường gặp

| Lỗi                  | Nguyên nhân                       | Cách sửa                                           |
| -------------------- | --------------------------------- | -------------------------------------------------- |
| Workflow không chạy  | sai `on:` hoặc filter branch/path | kiểm tra trigger, branch, YAML                     |
| `npm ci` fail        | lockfile lệch                     | chạy `npm install`, commit `package-lock.json`     |
| Test DB fail         | service DB chưa ready             | dùng healthcheck hoặc retry                        |
| Secret rỗng          | sai tên secret / chưa set         | kiểm tra Settings → Secrets                        |
| Cache không hiệu quả | cache key không đúng              | dùng cache built-in (`setup-node`, `setup-python`) |

---

## Checklist pipeline “đúng chuẩnâ€

- [ ] CI chạy trên **pull_request**
- [ ] dùng `npm ci` / lockfile
- [ ] lint chạy trước test
- [ ] cache bật (npm/pip)
- [ ] không hardcode secrets
- [ ] PR nhỏ → CI nhanh

---

## Bài tập

1. Tạo workflow CI cho Node.js: **lint → test → build**
2. Thêm badge CI vào README:

```markdown
*Hinh minh hoa duoc luoc bo trong ban PDF: CI.*
```

3. Thêm matrix build test Node.js 18 và 20

---

## Tài liệu tham khảo

- [https://docs.github.com/en/actions](https://docs.github.com/en/actions)
- [https://github.com/sdras/awesome-actions](https://github.com/sdras/awesome-actions)


<div class="pdf-page-break"></div>

<!-- Source: devops/deployment-basics.md -->

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

- Docker cơ bản
- CI/CD - GitHub Actions

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

- Đọc Logging & Monitoring để hiểu cần xem gì sau deploy
- Đọc Bảo mật cơ bản để biết env và secrets cần được quản lý thế nào
- Đọc Lỗi thường gặp để biết cách xử lý local trước khi nghĩ đến production


<div class="pdf-page-break"></div>

<!-- Source: devops/logging-monitoring.md -->

﻿# Logging & Monitoring

## Mục tiêu

Sau bài này, bạn sẽ:

- Hiểu log levels và cách sử dụng đúng.
- Viết log có cấu trúc (structured logging).
- Giới thiệu stack monitoring: **Prometheus + Grafana**.
- Setup monitoring cơ bản bằng Docker Compose.

## Prerequisites

- Docker Compose.

---

## Log Levels

| Level   | Khi nào dùng                          | Ví dụ                                          |
| ------- | ------------------------------------- | ---------------------------------------------- |
| `DEBUG` | Chi tiết cho dev, không bật trên prod | `DEBUG: Query result: {rows: 42}`              |
| `INFO`  | Sự kiện bình thường                   | `INFO: Server started on port 3000`            |
| `WARN`  | Vấn đề tiềm ẩn, chưa lỗi              | `WARN: Disk usage at 85%`                      |
| `ERROR` | Lỗi nhưng app vẫn chạy                | `ERROR: Failed to send email to user@test.com` |
| `FATAL` | Lỗi nghiêm trọng, app phải dừng       | `FATAL: Database connection failed`            |

!!! warning "Quy tắc"
    - **Production**: chỉ bật `INFO` trở lên.
    - **Development**: bật `DEBUG`.
    - **KHÔNG** log sensitive data như password, token, hoặc PII.

---

## Structured Logging

### Log không tốt

```
Error occurred while processing request
Something went wrong
User login failed
```

### Log có cấu trúc

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

> So do duoc luoc bo trong ban PDF. Xem ban web neu can hinh minh hoa.

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

| Metric             | Ý nghĩa                        |
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


<div class="pdf-page-break"></div>

<!-- Source: devops/security-basics.md -->

﻿# Bảo mật cơ bản

## Mục tiêu

Sau bài này, bạn sẽ:

- Quản lý **secrets** đúng cách (ENV, vault).
- Hiểu **password hashing** và tại sao không lưu plaintext.
- Hiểu cơ bản về **JWT** (JSON Web Token).
- Tránh các lỗi bảo mật phổ biến.

## Prerequisites

- HTTP & REST API.

---

## Quản lý Secrets

### Không bao giờ làm vậy

```python
# TUYỆT ĐỐI KHÔNG hardcode secrets trong code
DATABASE_URL = "postgres://admin:SuperSecret123@db.prod.com:5432/internhub"
API_KEY = "sk-1234567890abcdef"
```

### ✅ Sử dụng biến môi trường

```python
import os

DATABASE_URL = os.environ.get("DATABASE_URL")
API_KEY = os.environ.get("API_KEY")
```

```bash
# File .env (KHÔNG commit lên Git)
DATABASE_URL=postgres://admin:SuperSecret123@db.prod.com:5432/internhub
API_KEY=sk-1234567890abcdef
```

```gitignore
# .gitignore
.env
.env.local
.env.production
```

### Tạo file `.env.example`

```env
# .env.example (commit file này – không có giá trị thật)
DATABASE_URL=postgres://user:password@localhost:5432/dbname
API_KEY=your-api-key-here
JWT_SECRET=your-secret-here
```

!!! danger "Nếu lỡ commit secret"
    1. **Rotate** (đổi) secret ngay lập tức.
    2. Xóa khỏi Git history bằng `git filter-branch` hoặc BFG Repo Cleaner.
    3. Thông báo team.

---

## Password Hashing

### Tại sao không lưu plaintext?

```text
[Sai] Database bị hack → hacker có tất cả password
   users table:
   | email              | password      |
   | user@test.com      | MyPassword123 |  <- Plaintext

[Đúng] Lưu hash → hacker không thể lấy password gốc
   users table:
   | email              | password_hash                        |
   | user@test.com      | $2b$12$LJ3m4ys3Gz...hashed...value |  <- Bcrypt hash
```

### Ví dụ code

=== "Python (bcrypt)"
```python
import bcrypt

    # Hash password khi đăng ký
    password = "MyPassword123"
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    # Lưu `hashed` vào database

    # Verify khi đăng nhập
    input_password = "MyPassword123"
    if bcrypt.checkpw(input_password.encode('utf-8'), hashed):
        print("Login thành công!")
    else:
        print("Sai mật khẩu!")
    ```

=== "Node.js (bcrypt)"
```javascript
const bcrypt = require('bcrypt');
const SALT_ROUNDS = 12;

    // Hash password khi đăng ký
    const hash = await bcrypt.hash("MyPassword123", SALT_ROUNDS);
    // Lưu `hash` vào database

    // Verify khi đăng nhập
    const isValid = await bcrypt.compare("MyPassword123", hash);
    if (isValid) {
      console.log("Login thành công!");
    }
    ```

---

## JWT (JSON Web Token)

### JWT là gì?

```
Header.Payload.Signature
eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjF9.signature_here
```

> So do duoc luoc bo trong ban PDF. Xem ban web neu can hinh minh hoa.

### Cấu trúc JWT

```json
// Header
{ "alg": "HS256", "typ": "JWT" }

// Payload (claims)
{
  "userId": 42,
  "email": "user@test.com",
  "role": "intern",
  "iat": 1700000000,        // Issued at
  "exp": 1700003600          // Expiry (1 giờ)
}

// Signature
HMACSHA256(base64(header) + "." + base64(payload), SECRET_KEY)
```

### Ví dụ code

=== "Node.js (jsonwebtoken)"
```javascript
const jwt = require('jsonwebtoken');
const SECRET = process.env.JWT_SECRET;

    // Tạo token khi login
    const token = jwt.sign(
      { userId: 42, role: 'intern' },
      SECRET,
      { expiresIn: '1h' }
    );

    // Verify token trong middleware
    function authMiddleware(req, res, next) {
      const token = req.headers.authorization?.split(' ')[1];
      if (!token) return res.status(401).json({ error: 'No token' });

      try {
        const decoded = jwt.verify(token, SECRET);
        req.user = decoded;
        next();
      } catch (err) {
        return res.status(401).json({ error: 'Invalid token' });
      }
    }
    ```

=== "Python (PyJWT)"
```python
import jwt
import os
from datetime import datetime, timedelta

    SECRET = os.environ.get("JWT_SECRET")

    # Tạo token
    payload = {
        "userId": 42,
        "role": "intern",
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET, algorithm="HS256")

    # Verify token
    try:
        decoded = jwt.decode(token, SECRET, algorithms=["HS256"])
        print(decoded["userId"])  # 42
    except jwt.ExpiredSignatureError:
        print("Token hết hạn!")
    except jwt.InvalidTokenError:
        print("Token không hợp lệ!")
    ```

!!! warning "Lưu ý JWT"
    - JWT **không mã hóa** payload, chỉ **ký** (sign). Nội dung ai cũng đọc được trên [jwt.io](https://jwt.io).
    - **KHÔNG** lưu thông tin nhạy cảm trong payload như password hay credit card.
    - Đặt thời gian hết hạn ngắn, ví dụ 1 giờ cho access token.
    - Dùng **refresh token** để lấy access token mới.

---

## Checklist bảo mật cho Fresher

- [ ] Không hardcode secrets trong code.
- [ ] `.env` đã thêm vào `.gitignore`.
- [ ] Password được hash bằng bcrypt (salt rounds >= 12).
- [ ] JWT có expiry time.
- [ ] Input validation cho tất cả API endpoints.
- [ ] HTTPS trên production.
- [ ] Dependencies được update, không có known vulnerabilities.
- [ ] Không expose debug/stack trace trên production.

---

## Lỗi thường gặp

| Lỗi                        | Nguyên nhân                              | Cách sửa                         |
| -------------------------- | ---------------------------------------- | -------------------------------- |
| Secret bị leak trên GitHub | Commit `.env`                            | Rotate secret, dùng `.gitignore` |
| JWT `invalid signature`    | Secret key khác nhau giữa sign và verify | Dùng cùng 1 secret               |
| `jwt expired`              | Token hết hạn                            | Implement refresh token flow     |
| SQL Injection              | Nối string trực tiếp vào query           | Dùng parameterized queries       |

---

## Tài liệu tham khảo

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [JWT.io](https://jwt.io/)
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)


<div class="pdf-page-break"></div>

<!-- Source: troubleshooting/common-errors.md -->

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

- Đọc Docker Compose nếu bạn thường gặp lỗi stack local
- Đọc GitHub Workflow nếu vấn đề nằm ở branch/PR/review
- Đọc Logging & Monitoring nếu muốn chuyển từ debug local sang tư duy vận hành


<div class="pdf-page-break"></div>

<!-- Source: cheatsheets/linux.md -->

﻿# Linux Cheat Sheet

> Copy-paste nhanh các lệnh Linux thường dùng.

---

## Di chuyển & File

```bash
pwd                           # Thư mục hiện tại
ls -la                        # Liệt kê chi tiết + file ẩn
cd /path/to/dir               # Di chuyển
cd ..                         # Lên 1 cấp
cd ~                          # Về home
cd -                          # Quay lại thư mục trước

mkdir -p dir/subdir            # Tạo folder lồng nhau
touch file.txt                 # Tạo file rỗng
cp -r src/ dest/               # Copy folder
mv old new                     # Di chuyển / đổi tên
rm -rf folder/                 # Xoá folder (â ï¸ cẩn thận!)
```

## Xem & Tìm kiếm

```bash
cat file.txt                   # In nội dung file
head -20 file.txt              # 20 dòng đầu
tail -f app.log                # Follow log realtime
less file.txt                  # Xem từng trang
wc -l file.txt                 # Đếm dòng

grep -rn "pattern" .           # Tìm text trong file
find . -name "*.py" -type f    # Tìm file theo tên
```

## Quyền (Permissions)

```bash
chmod +x script.sh             # Cấp quyền thực thi
chmod 755 file                 # rwxr-xr-x
chmod 644 file                 # rw-r--r--
chown user:group file          # Đổi owner
```

## Process

```bash
ps aux                         # Liệt kê process
ps aux | grep node             # Tìm process
kill PID                       # Dừng process
kill -9 PID                    # Force kill
pkill -f "pattern"             # Kill theo tên
htop                           # Monitor realtime
```

## Network

```bash
ip addr show                   # Xem IP
ss -tulnp                      # Xem port đang mở
lsof -i :8080                  # Ai dùng port 8080
curl -I http://localhost:3000   # Test HTTP
ping google.com -c 4           # Test connectivity
wget URL                       # Tải file
```

## Pipe & Redirect

```bash
cmd1 | cmd2                    # Pipe output
echo "text" > file             # Ghi đè file
echo "text" >> file            # Ghi thêm cuối file
cmd 2> error.log               # Redirect stderr
cmd > all.log 2>&1             # Redirect cả stdout + stderr
```

## Package (Ubuntu/Debian)

```bash
sudo apt update                # Cập nhật danh sách
sudo apt install -y pkg        # Cài package
sudo apt remove pkg            # Gỡ package
apt search keyword             # Tìm package
```

## Disk & System

```bash
df -h                          # Disk usage
du -sh folder/                 # Kích thước folder
free -h                        # RAM usage
uname -a                       # Thông tin hệ thống
whoami                         # User hiện tại
history | grep cmd             # Lịch sử lệnh
```

## Biến môi trường

```bash
echo $PATH                     # Xem PATH
export MY_VAR="value"          # Set biến (session)
echo 'export VAR="val"' >> ~/.bashrc  # Set cố định
source ~/.bashrc               # Reload config
```

## Nén & Giải nén

```bash
tar -czf archive.tar.gz dir/   # Nén
tar -xzf archive.tar.gz        # Giải nén
zip -r archive.zip dir/        # Nén zip
unzip archive.zip              # Giải nén zip
```


<div class="pdf-page-break"></div>

<!-- Source: cheatsheets/git.md -->

﻿# Git Cheat Sheet

> Copy-paste nhanh các lệnh Git thường dùng.

---

## Setup

```bash
git config --global user.name "Tên"
git config --global user.email "email@example.com"
git config --global init.defaultBranch main
git config --global core.autocrlf input      # Linux/macOS
git config --global core.autocrlf true       # Windows
git config --list                            # Xem config
```

## Khởi tạo & Clone

```bash
git init                       # Tạo repo mới
git clone URL                  # Clone repo
git clone URL folder-name      # Clone vào folder cụ thể
```

## Cơ bản

```bash
git status                     # Xem trạng thái
git add file.txt               # Stage file
git add .                      # Stage tất cả
git commit -m "message"        # Commit
git commit --amend             # Sửa commit gần nhất
git push origin main           # Push
git pull origin main           # Pull (fetch + merge)
git fetch origin               # Fetch (không merge)
```

## Branch

```bash
git branch                     # Liệt kê branch
git branch -a                  # Liệt kê cả remote
git switch -c feature/login    # Tạo + chuyển branch
git switch main                # Chuyển branch
git branch -d feature/login    # Xoá branch đã merge
git branch -D feature/login    # Force xoá branch
```

## Merge & Rebase

```bash
git merge feature/login        # Merge branch vào hiện tại
git rebase main                # Rebase branch hiện tại lên main
git rebase --continue          # Tiếp tục rebase sau fix conflict
git rebase --abort             # Huỷ rebase
git merge --abort              # Huỷ merge
```

## Stash

```bash
git stash                      # Lưu tạm thay đổi
git stash list                 # Xem danh sách stash
git stash pop                  # Lấy lại stash gần nhất
git stash drop                 # Xoá stash gần nhất
git stash apply stash@{0}      # Apply stash cụ thể
```

## Undo & Recovery

```bash
git restore file.txt           # Bỏ thay đổi (chưa stage)
git restore --staged file.txt  # Unstage file
git reset --soft HEAD~1        # Undo commit (giữ staged)
git reset HEAD~1               # Undo commit (giữ unstaged)
git reset --hard HEAD~1        # Undo commit (MẤT code!)
git revert HEAD                # Tạo commit đảo ngược
git reflog                     # Xem mọi thao tác (emergency!)
```

## Log & Diff

```bash
git log --oneline              # Log ngắn gọn
git log --oneline --graph --all  # Log dạng graph
git log -5                     # 5 commit gần nhất
git diff                       # Xem thay đổi (chưa stage)
git diff --staged              # Xem thay đổi (đã stage)
git diff main..feature         # So sánh 2 branch
git show commit-hash           # Xem chi tiết commit
```

## Remote

```bash
git remote -v                  # Xem remote URLs
git remote add origin URL      # Thêm remote
git push -u origin branch      # Push + set upstream
git push --force-with-lease    # Force push (an toàn)
```

## Tag

```bash
git tag v1.0.0                 # Tạo tag
git tag -a v1.0.0 -m "msg"    # Tag kèm message
git push origin v1.0.0         # Push tag
git push origin --tags         # Push tất cả tags
```

## Commit Message Convention

```
feat:     Tính năng mới
fix:      Sửa bug
docs:     Thay đổi docs
style:    Format code
refactor: Tái cấu trúc
test:     Thêm/sửa test
chore:    Config, build tools

# Ví dụ
feat(auth): add JWT refresh token
fix(api): validate email before insert
docs: update README installation guide
```

## Branch Naming

```
feature/user-auth
bugfix/login-crash
hotfix/security-patch
docs/update-readme
refactor/clean-utils
```


<div class="pdf-page-break"></div>

<!-- Source: cheatsheets/docker.md -->

﻿# Docker Cheat Sheet

> Copy-paste nhanh các lệnh Docker thường dùng.

---

## Container

```bash
docker run -d --name app -p 8080:80 nginx   # Chạy container
docker ps                      # Liệt kê đang chạy
docker ps -a                   # Liệt kê tất cả
docker stop app                # Dừng container
docker start app               # Khởi động lại
docker restart app             # Restart
docker rm app                  # Xoá container
docker rm -f app               # Force xoá
docker container prune         # Xoá tất cả đã dừng
```

## Image

```bash
docker images                  # Liệt kê images
docker pull nginx:alpine       # Tải image
docker build -t internhub-api:1.0 .    # Build image
docker rmi image-name          # Xoá image
docker image prune -a          # Xoá images không dùng
docker tag internhub-api:1.0 user/internhub-api:1.0  # Tag image
docker push user/internhub-api:1.0    # Push lên registry
```

## Logs & Debug

```bash
docker logs app                # Xem logs
docker logs -f app             # Follow logs
docker logs --tail 50 app      # 50 dòng cuối
docker exec -it app bash       # Shell vào container
docker exec -it app sh         # Shell (Alpine)
docker exec app cat /etc/hosts # Chạy lệnh
docker inspect app             # Chi tiết container
docker stats                   # Resource usage
```

## Volume

```bash
docker volume create mydata    # Tạo volume
docker volume ls               # Liệt kê
docker volume rm mydata        # Xoá
docker volume prune            # Xoá không dùng
docker run -v mydata:/app/data ...  # Mount named volume
docker run -v $(pwd):/app ...  # Bind mount
```

## Network

```bash
docker network ls              # Liệt kê networks
docker network create mynet    # Tạo network
docker network inspect mynet   # Chi tiết
docker run --network mynet ... # Chạy container trong network
```

## Docker Compose

```bash
docker compose up -d           # Start stack (background)
docker compose down            # Stop + remove
docker compose down -v         # Stop + remove + xoá volumes
docker compose ps              # Trạng thái
docker compose logs -f web     # Logs service
docker compose exec web bash   # Shell vào service
docker compose build           # Build lại images
docker compose up -d --build   # Build + start
docker compose pull            # Pull latest images
docker compose restart web     # Restart 1 service
```

## Dọn dẹp

```bash
docker system df               # Xem disk usage
docker system prune            # Dọn cơ bản
docker system prune -a --volumes  # Dọn toàn bộ (â ï¸)
docker stop $(docker ps -q)    # Stop tất cả container
docker rm $(docker ps -aq)     # Xoá tất cả container
```

## Dockerfile Template

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "main.py"]
```

## docker-compose.yml Template

```yaml
services:
  web:
    build: .
    ports: ["3000:3000"]
    environment:
      - DATABASE_URL=postgres://dev:dev123@db:5432/internhub
    depends_on: [db]

  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: dev
      POSTGRES_PASSWORD: dev123
      POSTGRES_DB: internhub
    ports: ["5432:5432"]
    volumes: [pgdata:/var/lib/postgresql/data]

volumes:
  pgdata:
```

## Port Mapping

```
-p 8080:80    → localhost:8080 → container:80
-p 3000:3000  → localhost:3000 → container:3000
-p 127.0.0.1:5432:5432  → chỉ bind localhost
```


<div class="pdf-page-break"></div>

<!-- Source: cheatsheets/sql.md -->

﻿# SQL Cheat Sheet

> Copy-paste nhanh các câu SQL thường dùng (PostgreSQL).

---

## Kiểu dữ liệu phổ biến

```
INT / INTEGER          Số nguyên
SERIAL                 Auto-increment integer
BIGSERIAL              Auto-increment big integer
VARCHAR(n)             Chuỗi giới hạn n ký tự
TEXT                   Chuỗi không giới hạn
BOOLEAN                true / false
TIMESTAMP              Ngày giờ
DATE                   Chỉ ngày
DECIMAL(10,2)          Số thập phân
JSON / JSONB           JSON data
UUID                   Unique identifier
```

## DDL – Tạo / Sửa bảng

```sql
-- Tạo bảng
CREATE TABLE users (
    id          SERIAL PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    email       VARCHAR(255) UNIQUE NOT NULL,
    role        VARCHAR(50) DEFAULT 'user',
    is_active   BOOLEAN DEFAULT true,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Thêm cột
ALTER TABLE users ADD COLUMN phone VARCHAR(20);

-- Đổi tên cột
ALTER TABLE users RENAME COLUMN phone TO phone_number;

-- Xoá cột
ALTER TABLE users DROP COLUMN phone_number;

-- Xoá bảng
DROP TABLE IF EXISTS users;

-- Tạo index
CREATE INDEX idx_users_email ON users(email);
```

## INSERT

```sql
-- Insert 1 row
INSERT INTO users (name, email) VALUES ('Văn A', 'a@test.com');

-- Insert nhiều rows
INSERT INTO users (name, email, role) VALUES
  ('Thị B', 'b@test.com', 'admin'),
  ('Văn C', 'c@test.com', 'user');

-- Insert nếu chưa tồn tại
INSERT INTO users (name, email)
VALUES ('Văn A', 'a@test.com')
ON CONFLICT (email) DO NOTHING;

-- Upsert
INSERT INTO users (name, email)
VALUES ('Văn A Updated', 'a@test.com')
ON CONFLICT (email) DO UPDATE SET name = EXCLUDED.name;
```

## SELECT

```sql
-- Cơ bản
SELECT * FROM users;
SELECT name, email FROM users;

-- Điều kiện
SELECT * FROM users WHERE role = 'admin';
SELECT * FROM users WHERE role IN ('admin', 'user');
SELECT * FROM users WHERE name LIKE '%nguyen%';     -- Case-sensitive
SELECT * FROM users WHERE name ILIKE '%nguyen%';    -- Case-insensitive (PG)
SELECT * FROM users WHERE created_at > '2025-01-01';
SELECT * FROM users WHERE is_active = true AND role = 'admin';

-- Sắp xếp
SELECT * FROM users ORDER BY created_at DESC;
SELECT * FROM users ORDER BY name ASC, id DESC;

-- Giới hạn & phân trang
SELECT * FROM users LIMIT 10;
SELECT * FROM users LIMIT 10 OFFSET 20;  -- Page 3

-- Đếm & Aggregate
SELECT COUNT(*) FROM users;
SELECT role, COUNT(*) FROM users GROUP BY role;
SELECT role, COUNT(*) FROM users GROUP BY role HAVING COUNT(*) > 5;
SELECT AVG(price), MIN(price), MAX(price), SUM(price) FROM products;

-- Distinct
SELECT DISTINCT role FROM users;
```

## UPDATE

```sql
UPDATE users SET role = 'admin' WHERE id = 1;
UPDATE users SET is_active = false WHERE created_at < '2024-01-01';

-- Update nhiều cột
UPDATE users SET name = 'New Name', role = 'senior' WHERE id = 1;
```

## DELETE

```sql
DELETE FROM users WHERE id = 1;
DELETE FROM users WHERE is_active = false;

-- â ï¸ Xoá tất cả (cẩn thận!)
DELETE FROM users;
TRUNCATE TABLE users;  -- Nhanh hơn DELETE, reset SERIAL
```

## JOIN

```sql
-- INNER JOIN
SELECT u.name, p.title
FROM users u
INNER JOIN posts p ON u.id = p.user_id;

-- LEFT JOIN (tất cả users, kể cả không có posts)
SELECT u.name, COUNT(p.id) as post_count
FROM users u
LEFT JOIN posts p ON u.id = p.user_id
GROUP BY u.name;

-- RIGHT JOIN
SELECT u.name, p.title
FROM users u
RIGHT JOIN posts p ON u.id = p.user_id;
```

## Subquery

```sql
-- Subquery trong WHERE
SELECT * FROM users
WHERE id IN (SELECT user_id FROM posts WHERE published = true);

-- Subquery trong FROM
SELECT avg_posts.name, avg_posts.cnt
FROM (
  SELECT u.name, COUNT(p.id) as cnt
  FROM users u
  LEFT JOIN posts p ON u.id = p.user_id
  GROUP BY u.name
) avg_posts
WHERE avg_posts.cnt > 3;
```

## Transaction

```sql
BEGIN;
  UPDATE accounts SET balance = balance - 100 WHERE id = 1;
  UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;

-- Nếu lỗi:
ROLLBACK;
```

## psql Commands

```bash
\l              # Liệt kê databases
\c dbname       # Kết nối database
\dt             # Liệt kê tables
\d tablename    # Cấu trúc bảng
\di             # Liệt kê indexes
\x              # Toggle expanded display
\q              # Thoát
\i file.sql     # Chạy file SQL
\timing         # Bật đo thời gian query
```

## Performance

```sql
-- Xem execution plan
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'a@test.com';

-- Tạo index
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_posts_user_published ON posts(user_id, published);
```
