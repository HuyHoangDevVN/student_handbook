# Node.js & npm

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
