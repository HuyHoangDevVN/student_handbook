# Quáº£n lĂ½ Dependencies

Dependencies lĂ  cĂ¡c **thÆ° viá»‡n hoáº·c package bĂªn ngoĂ i** mĂ  project sá»­ dá»¥ng.

Quáº£n lĂ½ dependencies Ä‘Ăºng cĂ¡ch giĂºp:

- Ä‘áº£m báº£o **má»i developer cháº¡y cĂ¹ng mĂ´i trÆ°á»ng**
- trĂ¡nh lá»—i **â€œworks on my machineâ€**
- giáº£m rá»§i ro **security vulnerabilities**

---

## Má»¥c tiĂªu

Sau bĂ i nĂ y báº¡n cĂ³ thá»ƒ:

- hiá»ƒu táº§m quan trá»ng cá»§a dependency management
- sá»­ dá»¥ng **lock file**
- hiá»ƒu **Semantic Versioning**
- cáº­p nháº­t package an toĂ n

---

## VĂ¬ sao dependency management quan trá»ng

Má»™t project cĂ³ thá»ƒ sá»­ dá»¥ng **hĂ ng chá»¥c Ä‘áº¿n hĂ ng trÄƒm thÆ° viá»‡n**.

Náº¿u khĂ´ng quáº£n lĂ½ Ä‘Ăºng:

```text
Developer A: package v1.0
Developer B: package v1.2
CI server: package v2.0
```

Káº¿t quáº£:

```text
á»¨ng dá»¥ng cháº¡y khĂ¡c nhau trĂªn má»—i mĂ¡y
```

---

## Lock File

Lock file ghi láº¡i **chĂ­nh xĂ¡c phiĂªn báº£n dependency** Ä‘Æ°á»£c cĂ i.

Nhá» Ä‘Ă³ má»i developer vĂ  CI server Ä‘á»u cĂ i **giá»‘ng nhau 100%**.

---

## Lock file theo ngĂ´n ngá»¯

| NgĂ´n ngá»¯        | Lock file         | Commit? |
| --------------- | ----------------- | ------- |
| Python          | requirements.txt  | CĂ³      |
| Node.js         | package-lock.json | CĂ³      |
| Node.js (yarn)  | yarn.lock         | CĂ³      |
| Python (Poetry) | poetry.lock       | CĂ³      |
| Conda           | environment.yml   | CĂ³      |

---

!!! warning "Quy táº¯c quan trá»ng"
LuĂ´n **commit lock file** vĂ o repository.

ÄĂ¢y lĂ  cĂ¡ch duy nháº¥t Ä‘á»ƒ Ä‘áº£m báº£o:

```text
Reproducible builds
```

---

## Semantic Versioning (SemVer)

Háº§u háº¿t package sá»­ dá»¥ng **Semantic Versioning**.

Format:

```text
MAJOR.MINOR.PATCH
```

VĂ­ dá»¥:

```text
2.1.3
```

---

## Ă nghÄ©a version

| Pháº§n  | Khi nĂ o tÄƒng     |
| ----- | ---------------- |
| MAJOR | breaking changes |
| MINOR | thĂªm feature     |
| PATCH | sá»­a bug          |

---

### VĂ­ dá»¥

```text
1.2.3 â†’ 2.0.0   breaking changes
2.0.0 â†’ 2.1.0   new feature
2.1.0 â†’ 2.1.1   bug fix
```

---

## Version ranges (Node.js)

Trong `package.json` thÆ°á»ng tháº¥y:

| KĂ½ hiá»‡u  | Ă nghÄ©a                |
| -------- | ---------------------- |
| `^1.2.3` | cho phĂ©p upgrade minor |
| `~1.2.3` | chá»‰ upgrade patch      |
| `1.2.3`  | version chĂ­nh xĂ¡c      |
| `*`      | báº¥t ká»³ version         |

---

### VĂ­ dá»¥

```json
"express": "^4.18.2"
```

Range thá»±c táº¿:

```text
>=4.18.2 <5.0.0
```

---

## Kiá»ƒm tra dependency outdated

---

## Node.js

Xem package cÅ©:

```bash
npm outdated
```

---

Cáº­p nháº­t theo semver range:

```bash
npm update
```

---

Cáº­p nháº­t major version:

```bash
npx npm-check-updates -u
npm install
```

---

Kiá»ƒm tra security:

```bash
npm audit
```

Fix tá»± Ä‘á»™ng:

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

Cáº­p nháº­t package:

```bash
pip install --upgrade flask
```

---

Kiá»ƒm tra security:

```bash
pip install safety
safety check
```

---

## Best Practices

---

## 1. Pin version trong production

VĂ­ dá»¥ Python:

```text
flask==2.3.3
```

---

## 2. LuĂ´n commit lock file

VĂ­ dá»¥:

```text
requirements.txt
package-lock.json
```

---

## 3. Review dependency changes

Khi dependency thay Ä‘á»•i:

- xem changelog
- kiá»ƒm tra breaking changes

---

## 4. Audit security thÆ°á»ng xuyĂªn

VĂ­ dá»¥:

```bash
npm audit
safety check
```

---

## 5. Giáº£m sá»‘ lÆ°á»£ng dependency

NguyĂªn táº¯c:

```text
Chá»‰ cĂ i dependency khi thá»±c sá»± cáº§n.
```

Má»—i dependency má»›i cĂ³ thá»ƒ mang theo:

- security risk
- performance overhead
- maintenance cost

---

## Lá»—i thÆ°á»ng gáº·p

| Lá»—i                   | NguyĂªn nhĂ¢n             | CĂ¡ch sá»­a           |
| --------------------- | ----------------------- | ------------------ |
| Works on my machine   | dependency khĂ¡c version | commit lock file   |
| Build fail trĂªn CI    | thiáº¿u dependency        | update lock file   |
| Vulnerable dependency | package cÅ©              | upgrade dependency |

---

## BĂ i táº­p

### BĂ i 1

Táº¡o project Node.js vĂ :

```bash
npm install express
```

Sau Ä‘Ă³ xem:

```bash
npm outdated
```

---

### BĂ i 2

Táº¡o project Python:

```bash
pip install flask requests
```

Export:

```bash
pip freeze > requirements.txt
```

---

### BĂ i 3

TĂ¬m má»™t dependency cĂ³ **security vulnerability** vĂ  cáº­p nháº­t nĂ³.

---

## TĂ i liá»‡u tham kháº£o

```text
https://semver.org/
```

```text
https://docs.npmjs.com/cli/v10/commands/npm-audit
```
