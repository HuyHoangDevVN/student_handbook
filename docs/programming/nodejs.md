# Node.js & npm

Trang nĂ y giá»›i thiá»‡u cĂ¡ch thiáº¿t láº­p mĂ´i trÆ°á»ng **Node.js development** vĂ  quáº£n lĂ½ package vá»›i **npm**.

Node.js Ä‘Æ°á»£c dĂ¹ng phá»• biáº¿n Ä‘á»ƒ xĂ¢y dá»±ng:

- backend APIs
- CLI tools
- frontend tooling

---

## Má»¥c tiĂªu

Sau bĂ i nĂ y báº¡n cĂ³ thá»ƒ:

- cĂ i Node.js báº±ng **nvm**
- hiá»ƒu `npm`, `yarn`, `pnpm`
- sá»­ dá»¥ng **package.json**
- quáº£n lĂ½ **scripts**
- dĂ¹ng **biáº¿n mĂ´i trÆ°á»ng `.env`**

---

## YĂªu cáº§u

Báº¡n cáº§n cĂ³ **terminal**.

Náº¿u chÆ°a quen command line, xem:

```text
Terminal cÆ¡ báº£n
```

---

## CĂ i Ä‘áº·t Node.js

Khuyáº¿n nghá»‹ sá»­ dá»¥ng **nvm (Node Version Manager)** Ä‘á»ƒ quáº£n lĂ½ nhiá»u phiĂªn báº£n Node.js.

---

## Linux / macOS

CĂ i **nvm**:

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
source ~/.bashrc
```

CĂ i Node.js LTS:

```bash
nvm install --lts
nvm use --lts
```

Kiá»ƒm tra:

```bash
node --version
npm --version
```

VĂ­ dá»¥:

```text
v20.x.x
10.x.x
```

---

## Windows

Sá»­ dá»¥ng **nvm-windows**:

```text
https://github.com/coreybutler/nvm-windows
```

Sau khi cĂ i:

```powershell
nvm install 20
nvm use 20
```

Kiá»ƒm tra:

```powershell
node --version
npm --version
```

---

## npm cÆ¡ báº£n

npm lĂ  **package manager cá»§a Node.js**.

---

## Khá»Ÿi táº¡o project

```bash
npm init -y
```

Lá»‡nh nĂ y táº¡o file:

```text
package.json
```

---

## CĂ i package

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

### CĂ i tá»« package.json

```bash
npm install
```

Clean install:

```bash
npm ci
```

`npm ci` thÆ°á»ng dĂ¹ng trong **CI/CD pipelines**.

---

## Gá»¡ package

```bash
npm uninstall express
```

---

## package.json

File `package.json` chá»©a metadata cá»§a project.

---

## VĂ­ dá»¥

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

## CĂ¡c trÆ°á»ng quan trá»ng

| Field           | Ă nghÄ©a                       |
| --------------- | ----------------------------- |
| scripts         | cĂ¡c lá»‡nh cháº¡y project         |
| dependencies    | packages dĂ¹ng cho production  |
| devDependencies | packages dĂ¹ng khi development |

---

## Cháº¡y scripts

Scripts Ä‘Æ°á»£c cháº¡y báº±ng:

```bash
npm run <script-name>
```

VĂ­ dá»¥:

```bash
npm run dev
npm run lint
```

Má»™t sá»‘ script cĂ³ shortcut:

```bash
npm start
npm test
```

---

## Biáº¿n mĂ´i trÆ°á»ng (.env)

ThÆ° viá»‡n phá»• biáº¿n:

```bash
npm install dotenv
```

---

## VĂ­ dá»¥ `.env`

```env
PORT=3000
DATABASE_URL=postgres://user:pass@localhost:5432/mydb
JWT_SECRET=my-secret
NODE_ENV=development
```

---

## Sá»­ dá»¥ng trong code

```javascript
require("dotenv").config();

const port = process.env.PORT || 3000;

console.log(`Server running on port ${port}`);
```

---

!!! danger "Quan trá»ng"
KhĂ´ng commit file `.env`.

Thay vĂ o Ä‘Ă³ nĂªn táº¡o:

```text
.env.example
```

---

## npm vs yarn vs pnpm

|            | npm               | yarn      | pnpm           |
| ---------- | ----------------- | --------- | -------------- |
| Lock file  | package-lock.json | yarn.lock | pnpm-lock.yaml |
| Tá»‘c Ä‘á»™     | trung bĂ¬nh        | nhanh     | nhanh nháº¥t     |
| Disk usage | lá»›n               | lá»›n       | tiáº¿t kiá»‡m      |

---

### VĂ­ dá»¥ yarn

```bash
npm install -g yarn
yarn add express
```

---

### VĂ­ dá»¥ pnpm

```bash
npm install -g pnpm
pnpm add express
```

---

!!! tip "Best practice"
Trong má»™t project nĂªn **chá»‰ dĂ¹ng má»™t package manager**.

---

## Cáº¥u trĂºc project Node.js

Má»™t project backend thÆ°á»ng cĂ³ cáº¥u trĂºc:

```text
my-api/
â”œâ”€â”€ node_modules/
â”œâ”€â”€ src/
â”‚   â”œâ”€â”€ index.js
â”‚   â”œâ”€â”€ routes/
â”‚   â”œâ”€â”€ controllers/
â”‚   â”œâ”€â”€ models/
â”‚   â”œâ”€â”€ middleware/
â”‚   â””â”€â”€ utils/
â”œâ”€â”€ tests/
â”œâ”€â”€ .env
â”œâ”€â”€ .env.example
â”œâ”€â”€ .gitignore
â”œâ”€â”€ package.json
â””â”€â”€ README.md
```

---

## Lá»—i thÆ°á»ng gáº·p

| Lá»—i                      | NguyĂªn nhĂ¢n          | CĂ¡ch sá»­a             |
| ------------------------ | -------------------- | -------------------- |
| node command not found   | chÆ°a dĂ¹ng nvm        | `nvm use --lts`      |
| EACCES permission denied | cĂ i global báº±ng sudo | dĂ¹ng nvm             |
| Cannot find module       | thiáº¿u dependency     | cháº¡y `npm install`   |
| ENOSPC watchers          | Linux watcher limit  | tÄƒng `inotify` limit |
| Port Ä‘Ă£ dĂ¹ng             | process khĂ¡c chiáº¿m   | kill process         |

---

## BĂ i táº­p

### BĂ i 1

Táº¡o project Node.js má»›i.

CĂ i:

```text
express
```

Viáº¿t API:

```text
GET /hello
```

Tráº£:

```json
{
  "message": "Hello!"
}
```

---

### BĂ i 2

ThĂªm script:

```text
dev
```

sá»­ dá»¥ng `nodemon`.

---

### BĂ i 3

Táº¡o `.env` vá»›i biáº¿n:

```text
PORT
```

---

## TĂ i liá»‡u tham kháº£o

```text
https://nodejs.org/en/docs
```

```text
https://docs.npmjs.com/
```
