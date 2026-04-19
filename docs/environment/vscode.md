# VS Code – Editor cho Developer

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
