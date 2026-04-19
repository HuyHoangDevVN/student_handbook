# CI/CD - GitHub Actions

Trang nay la muc luc cho cum bai CI/CD. Noi dung da duoc tach ra de nguoi hoc di tu khai niem va
quy tac team, sang implementation cho Node/Python, roi den release va debugging.

---

## Muc tieu

Sau cum bai nay, ban co the:

- hieu CI/CD va vai tro cua no trong quy trinh PR
- viet workflow co ban cho Node.js va Python
- quan ly secrets, matrix build va release workflow
- debug workflow khi fail

---

## Prerequisites

- Da hoc: [GitHub Workflow](../vcs/github-workflow.md)
- Da biet Docker co ban neu can build image: [Docker co ban](../containers/docker.md)

---

## Lo trinh hoc

1. [CI/CD Fundamentals](ci-basics.md)
2. [CI Cho Node.js Va Python](ci-node-python.md)
3. [Secrets, Release Va Debug Workflow](ci-release-debug.md)

---

## Goi y hoc

- Khong nen hoc release pipeline truoc khi da chay duoc workflow toi thieu
- Tu tao mot repo demo nho de tap `pull_request -> lint -> test -> build`
- Chi dua them Docker release sau khi da on dinh pipeline co ban

---

## Tai lieu lien quan

- [Deployment co ban](deployment-basics.md)
- [Bao mat co ban](security-basics.md)
- [GitHub Workflow](../vcs/github-workflow.md)
