# Student IT Handbook

**Student IT Handbook** lĂ  tĂ i liá»‡u thá»±c hĂ nh dĂ nh cho sinh viĂªn CĂ´ng nghá»‡ thĂ´ng tin chuáº©n bá»‹ **thá»±c táº­p (intern)** hoáº·c **báº¯t Ä‘áº§u cĂ´ng viá»‡c Ä‘áº§u tiĂªn trong ngĂ nh pháº§n má»m**.

Handbook táº­p trung vĂ o **cĂ¡c cĂ´ng cá»¥ vĂ  workflow thá»±c táº¿ trong doanh nghiá»‡p**, giĂºp sinh viĂªn chuyá»ƒn tá»«:

```
Láº­p trĂ¬nh trong trÆ°á»ng â†’ Quy trĂ¬nh phĂ¡t triá»ƒn pháº§n má»m thá»±c táº¿
```

---

## Sample project xuyen suot

Toan bo handbook nay duoc xau chuoi quanh mot case study duy nhat: [InternHub API](getting-started/sample-project.md).

InternHub API la mot REST API don gian de quan ly user, bai viet noi bo, comment va tags. Khi hoc
theo handbook, ban se gap cung mot sample app o cac chuong:

- SQL va PostgreSQL
- Docker va Docker Compose
- API testing
- CI/CD
- Monitoring va deployment

Muc tieu la giup ban thay duoc mot quy trinh end-to-end thay vi nhieu vi du roi rac.

---

## Báº¡n sáº½ há»c Ä‘Æ°á»£c gĂ¬

Handbook táº­p trung vĂ o cĂ¡c **ká»¹ nÄƒng ká»¹ thuáº­t cÆ¡ báº£n mĂ  háº§u háº¿t cĂ´ng ty pháº§n má»m yĂªu cáº§u**:

- Linux vĂ  Terminal cÆ¡ báº£n
- Git vĂ  GitHub workflow lĂ m viá»‡c nhĂ³m
- Thiáº¿t láº­p mĂ´i trÆ°á»ng láº­p trĂ¬nh
- Database cÆ¡ báº£n (SQL / PostgreSQL)
- Docker vĂ  container hĂ³a á»©ng dá»¥ng
- CI/CD cÆ¡ báº£n
- Deployment vĂ  monitoring

Má»¥c tiĂªu lĂ  giĂºp sinh viĂªn hiá»ƒu **quy trĂ¬nh phĂ¡t triá»ƒn pháº§n má»m end-to-end**.

---

## Handbook nĂ y dĂ nh cho ai

TĂ i liá»‡u nĂ y phĂ¹ há»£p vá»›i:

- Sinh viĂªn IT **nÄƒm 3â€“4 chuáº©n bá»‹ Ä‘i thá»±c táº­p**
- **Fresher developer** má»›i Ä‘i lĂ m
- NgÆ°á»i muá»‘n há»c **DevOps workflow cÆ¡ báº£n**

YĂªu cáº§u kiáº¿n thá»©c:

- Biáº¿t Ă­t nháº¥t **má»™t ngĂ´n ngá»¯ láº­p trĂ¬nh**
- Biáº¿t sá»­ dá»¥ng **command line cÆ¡ báº£n**

---

## Lá»™ trĂ¬nh há»c táº­p

```mermaid
graph LR
    A[Terminal & Linux] --> B[Git & GitHub]
    B --> C[MĂ´i trÆ°á»ng láº­p trĂ¬nh]
    C --> D[Database]
    D --> E[Docker]
    E --> F[CI/CD]
    F --> G[Deployment & Monitoring]
```

Lá»™ trĂ¬nh nĂ y pháº£n Ă¡nh **quy trĂ¬nh phĂ¡t triá»ƒn pháº§n má»m phá»• biáº¿n trong doanh nghiá»‡p**:

```
Code â†’ Version Control â†’ Build â†’ Container â†’ CI/CD â†’ Deploy
```

---

## Báº¯t Ä‘áº§u nhanh

Náº¿u báº¡n má»›i báº¯t Ä‘áº§u, hĂ£y há»c theo thá»© tá»± sau:

1. Thiáº¿t láº­p mĂ´i trÆ°á»ng phĂ¡t triá»ƒn
2. LĂ m quen vá»›i Linux vĂ  Terminal
3. Há»c Git vĂ  GitHub workflow
4. Thiáº¿t láº­p mĂ´i trÆ°á»ng láº­p trĂ¬nh
5. Há»c SQL vĂ  database cÆ¡ báº£n
6. Há»c Docker vĂ  container
7. Hiá»ƒu CI/CD pipeline

Báº¡n cÅ©ng cĂ³ thá»ƒ **tĂ¬m nhanh ná»™i dung báº±ng thanh Search** hoáº·c má»Ÿ trá»±c tiáº¿p tá»«ng chÆ°Æ¡ng.

Neu muon di theo mot luong hoc co case study ro rang, hay mo [Sample Project: InternHub API](getting-started/sample-project.md)
ngay sau `Quickstart`.

---

## Cáº¥u trĂºc handbook

| Pháº§n            | Ná»™i dung                        |
| --------------- | ------------------------------- |
| Getting Started | Thiáº¿t láº­p mĂ´i trÆ°á»ng phĂ¡t triá»ƒn |
| Environment     | Terminal vĂ  Linux cÆ¡ báº£n        |
| Version Control | Git vĂ  GitHub                   |
| Programming     | Python / Node.js environment    |
| Databases       | SQL vĂ  PostgreSQL               |
| Containers      | Docker vĂ  Docker Compose        |
| DevOps          | CI/CD, logging, security        |

---

## VĂ¬ sao handbook nĂ y Ä‘Æ°á»£c táº¡o ra

Nhiá»u sinh viĂªn biáº¿t **viáº¿t code**, nhÆ°ng gáº·p khĂ³ khÄƒn khi:

- thiáº¿t láº­p mĂ´i trÆ°á»ng láº­p trĂ¬nh
- lĂ m viá»‡c nhĂ³m vá»›i Git
- cháº¡y á»©ng dá»¥ng báº±ng Docker
- hiá»ƒu pipeline CI/CD

Handbook nĂ y giĂºp **thu háº¹p khoáº£ng cĂ¡ch giá»¯a há»c táº­p trong trÆ°á»ng vĂ  mĂ´i trÆ°á»ng lĂ m viá»‡c thá»±c táº¿**.

---

## ÄĂ³ng gĂ³p ná»™i dung

Má»i Ä‘Ă³ng gĂ³p Ä‘á»u Ä‘Æ°á»£c hoan nghĂªnh.

Náº¿u báº¡n muá»‘n cáº£i thiá»‡n handbook:

1. Fork repository
2. Táº¡o branch má»›i
3. Commit thay Ä‘á»•i
4. Táº¡o Pull Request

---

## ThĂ´ng tin phiĂªn báº£n

| Thuá»™c tĂ­nh | GiĂ¡ trá»‹           |
| ---------- | ----------------- |
| PhiĂªn báº£n  | 1.1-draft         |
| Äá»‹nh dáº¡ng  | Markdown + MkDocs |
| Cáº­p nháº­t   | 2026              |

---
