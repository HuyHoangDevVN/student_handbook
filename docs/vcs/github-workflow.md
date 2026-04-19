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

- [Git cơ bản](git-basics.md)
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

- Nếu bạn chưa quen command line: đọc [Terminal & Shell](../environment/terminal.md)
- Nếu bạn sắp nhận task backend: đọc [HTTP & REST API](../backend/http-rest.md)
- Nếu bạn thường gặp lỗi local: đọc [Lỗi thường gặp](../troubleshooting/common-errors.md)
