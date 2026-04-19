# VS Code â€“ Editor cho Developer

**Visual Studio Code (VS Code)** lĂ  editor phá»• biáº¿n nháº¥t cho developer hiá»‡n nay.

VS Code há»— trá»£:

- nhiá»u ngĂ´n ngá»¯ láº­p trĂ¬nh
- há»‡ thá»‘ng **extensions**
- **debugging**
- **Git integration**
- **remote development** (WSL / SSH / Container)

---

## Má»¥c tiĂªu

Sau bĂ i nĂ y báº¡n cĂ³ thá»ƒ:

- cáº¥u hĂ¬nh VS Code cho development
- cĂ i extensions cáº§n thiáº¿t
- sá»­ dá»¥ng cĂ¡c **phĂ­m táº¯t quan trá»ng**
- lĂ m viá»‡c vá»›i **WSL / remote server**

---

## CĂ i Ä‘áº·t VS Code

Táº£i táº¡i:

```
https://code.visualstudio.com/
```

Sau khi cĂ i xong, kiá»ƒm tra lá»‡nh CLI:

```bash
code --version
```

---

## Extensions khuyĂªn dĂ¹ng

Extensions giĂºp VS Code há»— trá»£ thĂªm nhiá»u tĂ­nh nÄƒng.

---

## Extensions báº¯t buá»™c

| Extension    | Má»¥c Ä‘Ă­ch                      |
| ------------ | ----------------------------- |
| GitLens      | Hiá»ƒn thá»‹ git blame vĂ  history |
| Docker       | Quáº£n lĂ½ container             |
| Remote - WSL | LĂ m viá»‡c vá»›i WSL              |
| Remote - SSH | Code trĂªn server              |
| EditorConfig | Äá»“ng bá»™ format trong team     |

---

## Extensions theo ngĂ´n ngá»¯

| NgĂ´n ngá»¯                | Extension                        |
| ----------------------- | -------------------------------- |
| Python                  | Python, Pylance, Black Formatter |
| JavaScript / TypeScript | ESLint, Prettier                 |
| SQL                     | SQLTools                         |
| Markdown                | Markdown All in One              |

---

## PhĂ­m táº¯t quan trá»ng

| Windows / Linux    | macOS             | Chá»©c nÄƒng           |
| ------------------ | ----------------- | ------------------- |
| `Ctrl + Shift + P` | `Cmd + Shift + P` | Command Palette     |
| `Ctrl + P`         | `Cmd + P`         | Má»Ÿ file nhanh       |
| `Ctrl + Shift + F` | `Cmd + Shift + F` | Search toĂ n project |
| `Ctrl + ``         | `Cmd + ``         | Má»Ÿ terminal         |
| `Ctrl + /`         | `Cmd + /`         | Comment dĂ²ng        |
| `Alt + â†‘ / â†“`      | `Option + â†‘ / â†“`  | Di chuyá»ƒn dĂ²ng      |
| `Ctrl + D`         | `Cmd + D`         | Select occurrence   |
| `Ctrl + Shift + K` | `Cmd + Shift + K` | XoĂ¡ dĂ²ng            |
| `F2`               | `F2`              | Rename symbol       |

---

## Cáº¥u hĂ¬nh VS Code

Má»Ÿ **Command Palette**:

```
Ctrl + Shift + P
```

TĂ¬m:

```
Open User Settings (JSON)
```

VĂ­ dá»¥ cáº¥u hĂ¬nh:

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

CĂ¡c setting phá»• biáº¿n:

| Setting                  | Má»¥c Ä‘Ă­ch       |
| ------------------------ | -------------- |
| `formatOnSave`           | tá»± format code |
| `autoSave`               | tá»± lÆ°u file    |
| `trimTrailingWhitespace` | xoĂ¡ space thá»«a |
| `git.autofetch`          | tá»± fetch git   |

---

## VS Code + WSL

VS Code cĂ³ thá»ƒ má»Ÿ project trá»±c tiáº¿p trong WSL.

Trong terminal WSL:

```bash
cd ~/myproject
code .
```

VS Code sáº½ tá»± Ä‘á»™ng káº¿t ná»‘i qua **Remote â€“ WSL**.

---

### LÆ°u Ă½ hiá»‡u suáº¥t

KhĂ´ng nĂªn má»Ÿ project táº¡i:

```
/mnt/c/Users/...
```

Thay vĂ o Ä‘Ă³ nĂªn Ä‘áº·t project táº¡i:

```
~/projects
```

vĂ¬ filesystem WSL nhanh hÆ¡n nhiá»u.

---

## Workspace settings

VS Code cĂ³ hai loáº¡i settings.

| Loáº¡i               | Pháº¡m vi                   |
| ------------------ | ------------------------- |
| User settings      | Ă¡p dá»¥ng cho toĂ n há»‡ thá»‘ng |
| Workspace settings | chá»‰ project hiá»‡n táº¡i      |

---

### VĂ­ dá»¥ `.vscode/settings.json`

```json
{
  "python.defaultInterpreterPath": ".venv/bin/python",
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter"
  }
}
```

File nĂ y giĂºp **Ä‘á»“ng bá»™ cáº¥u hĂ¬nh giá»¯a cĂ¡c developer**.

---

## Debugging

VS Code há»— trá»£ debugging cho nhiá»u ngĂ´n ngá»¯.

---

### CĂ¡c bÆ°á»›c cÆ¡ báº£n

1. Má»Ÿ file code
2. Äáº·t **breakpoint**
3. Nháº¥n:

```
F5
```

Hoáº·c vĂ o tab:

```
Run and Debug
```

Sau Ä‘Ă³ chá»n runtime:

```
Python
Node.js
Go
...
```

---

## Lá»—i thÆ°á»ng gáº·p

| Lá»—i                       | NguyĂªn nhĂ¢n              | CĂ¡ch sá»­a                      |
| ------------------------- | ------------------------ | ----------------------------- |
| Extension khĂ´ng hoáº¡t Ä‘á»™ng | cháº¡y code trong WSL      | cĂ i extension trong WSL       |
| Terminal cháº­m             | dĂ¹ng PowerShell máº·c Ä‘á»‹nh | chuyá»ƒn sang WSL / Git Bash    |
| Format khĂ´ng cháº¡y         | chÆ°a set formatter       | set `editor.defaultFormatter` |

---

## TĂ i liá»‡u tham kháº£o

```
https://code.visualstudio.com/docs
```

```
https://code.visualstudio.com/docs/getstarted/tips-and-tricks
```
