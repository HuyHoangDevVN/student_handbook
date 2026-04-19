# Handbook Refactor Plan

## Muc tieu

- Chuan hoa handbook theo dung quy tac `1 trang = 1 ky nang`.
- Giam tai trong nhan thuc cho sinh vien moi bat dau.
- Tao duong build PDF rieng, on dinh tren Ubuntu/CI va khong anh huong luong dev hang ngay.

## Refactor da lam

- Chuan hoa heading trong `docs/` ve mo hinh `1 H1 / page`; cac muc lon con lai duoc dua ve `##`.
- Tach cau hinh PDF sang `mkdocs-pdf.yml` thay vi bat plugin PDF trong `mkdocs.yml`.
- Them script `scripts/export-pdf.ps1` de build ban PDF handbook.
- Them workflow `.github/workflows/pdf-handbook.yml` de build artifact PDF tren GitHub Actions.
- Them `extra.version` trong `mkdocs.yml` de handbook co version ro rang.

## Refactor tiep theo theo 3 dot

### Dot 1 - Tach cac bai qua dai

Da thuc hien dot tach dau tien cho:

- `docs/environment/terminal.md`
- `docs/environment/linux.md`
- `docs/vcs/git-basics.md`
- `docs/containers/docker.md`
- `docs/databases/sql-postgres.md`
- `docs/devops/cicd-github-actions.md`

Moi file goc gio dong vai tro landing page, con noi dung chi tiet da duoc tach thanh cac bai con
va dua vao nav cho web/PDF.

Tac dong lon nhat den trai nghiem hoc:

- `docs/environment/terminal.md`
- `docs/environment/linux.md`
- `docs/vcs/git-basics.md`
- `docs/containers/docker.md`
- `docs/databases/sql-postgres.md`
- `docs/devops/cicd-github-actions.md`

Huong tach de xuat:

- `terminal.md` -> `navigation`, `files`, `pipes-redirects`, `search-env`
- `linux.md` -> `wsl-setup`, `permissions`, `process-network`, `systemd`
- `git-basics.md` -> `git-core`, `branching`, `history-recovery`
- `docker.md` -> `docker-runtime`, `docker-images`, `dockerfile-debug`
- `sql-postgres.md` -> `postgres-setup`, `sql-crud`, `joins-indexes-transactions`
- `cicd-github-actions.md` -> `ci-basics`, `node-ci`, `python-ci`, `docker-release`

### Dot 2 - Thong nhat khung bai hoc

Moi bai dang lesson nen co:

- `## Muc tieu`
- `## Prerequisites`
- `## Noi dung chinh`
- `## Loi thuong gap`
- `## Bai tap`
- `## Tai lieu tham khao`

Ngoai le:

- `index.md`
- cac file trong `docs/cheatsheets/`
- `getting-started/checklist.md`

### Dot 3 - Tao sample project xuyen suot

De handbook mach lac hon, nen dua toan bo vi du ve cung mot sample app:

- mot API mau
- PostgreSQL schema mau
- Postman collection mau
- Docker Compose mau
- workflow CI mau
- deployment mau

Muc tieu la de sinh vien di theo mot case study duy nhat tu local -> Git -> API -> DB -> Docker -> CI -> deploy.

Trang bat dau cho case study nay: `docs/getting-started/sample-project.md`

## Phuong an PDF handbook

### Cach build local

Windows:

```powershell
./scripts/export-pdf.ps1
```

Khuyen nghi dung WSL/Ubuntu neu may Windows chua co GTK/Pango.

Linux/macOS:

```bash
ENABLE_PDF_EXPORT=1 mkdocs build --strict -f mkdocs-pdf.yml
```

Output:

```text
site/pdf/student-it-handbook.pdf
```

### Cach build tren CI

- Workflow: `.github/workflows/pdf-handbook.yml`
- Trigger: `workflow_dispatch` hoac push tag `v*`
- Output: artifact `student-it-handbook-pdf`

### Chuan editorial cho ban PDF

De ban PDF doc duoc nhu mot cuon handbook, nen uu tien:

- muc luc ro rang va heading cap 2/3 nhat quan
- bat dau bang `index.md` nhu loi mo dau
- de `Cheat Sheets` o cuoi nhu phan appendix
- moi chuong lon khong qua dai; neu qua dai thi tach thanh chuong nho
- uu tien code block ngan, tranh dump qua nhieu lenh tren mot trang
