# Contributing Guide

Tài liệu này dành cho contributor và maintainer của `Student IT Handbook`.

Nếu bạn là người học, hãy bắt đầu ở [README.md](README.md) và phần `Start Here` trong handbook.

## Mục tiêu của repo

Repo này không chỉ là tập hợp markdown. Mục tiêu của nó là giúp sinh viên:

- biết cần chuẩn bị gì trước khi đi thực tập
- hiểu workflow làm việc thật trong dự án
- có tài liệu tra cứu khi mới vào team

Mọi thay đổi cần giữ vững 3 vai trò trên.

## Nguyên tắc viết nội dung

Mỗi bài học nên trả lời rõ:

- học để làm gì
- dùng khi nào
- có prerequisite gì
- ví dụ nào gắn với `InternHub API`
- tự xác minh thế nào
- lỗi thường gặp là gì
- học tiếp gì sau bài này

Khung ưu tiên:

```text
Mục tiêu
Khi nào bạn cần phần này
Prerequisites
Nội dung chính
Expected result / How to verify
Lỗi thường gặp / Pitfall
Bước tiếp theo
```

## Chapter template tối thiểu

```md
# Tên bài

Mô tả ngắn 1-2 câu.

## Mục tiêu

- ...

## Khi nào bạn cần phần này

- ...

## Prerequisites

- ...

## Nội dung chính

## Expected result

## Lỗi thường gặp

## Bước tiếp theo
```

## Review checklist cho docs

Trước khi merge, reviewer cần kiểm tra:

- [ ] Bài viết có phục vụ đúng đối tượng handbook
- [ ] Scope rõ, không dạy quá nhiều thứ trong một bài
- [ ] Ví dụ bám vào `InternHub API` nếu chủ đề có liên quan
- [ ] Command có context, không để copy-paste nguy hiểm
- [ ] Có warning rõ cho lệnh phá hủy hoặc thao tác production-sensitive
- [ ] Có expected result hoặc cách tự verify
- [ ] Link nội bộ đúng và file tham chiếu tồn tại
- [ ] Fenced code block có language

## Quy tắc cho lệnh nguy hiểm

Nếu một lệnh có thể:

- xóa dữ liệu
- reset git
- prune Docker
- ghi đè môi trường chia sẻ

thì bắt buộc phải có:

- nhãn cảnh báo rõ
- giải thích khi nào được dùng
- hệ quả nếu dùng sai
- ghi chú không dùng trên staging/prod nếu phù hợp

## Build và kiểm tra

Chạy tối thiểu:

```bash
mkdocs build --strict
```

Nếu repo có thêm quality gate cho docs, PR cần xanh trước khi merge.

## Xử lý nội dung lỗi thời

Nếu ví dụ, version, hoặc workflow đã cũ:

- ưu tiên cập nhật
- nếu chưa cập nhật được ngay, đánh dấu là outdated/deprecated
- không để lại thông tin có nguy cơ gây hiểu nhầm mà không cảnh báo
