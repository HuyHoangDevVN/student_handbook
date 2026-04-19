from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable

import yaml


ROOT = Path(__file__).resolve().parents[1]
MKDOCS_CONFIG = ROOT / "mkdocs.yml"
DOCS_DIR = ROOT / "docs"
OUTPUT_FILE = DOCS_DIR / "_generated" / "handbook-pdf.md"


def flatten_nav(nav: list) -> Iterable[tuple[str, str]]:
    for item in nav:
        if isinstance(item, dict):
            for key, value in item.items():
                if isinstance(value, str):
                    yield key, value
                elif isinstance(value, list):
                    yield from flatten_nav(value)
        elif isinstance(item, str):
            yield Path(item).stem.replace("-", " ").title(), item


def read_markdown_file(markdown_file: str) -> str:
    source = DOCS_DIR / markdown_file
    text = source.read_text(encoding="utf-8").strip()
    return sanitize_markdown(text)


def sanitize_markdown(text: str) -> str:
    text = re.sub(
        r"```mermaid\s+.*?```",
        "> Sơ đồ được lược bỏ trong bản PDF. Xem bản web nếu cần hình minh họa.",
        text,
        flags=re.DOTALL,
    )
    text = re.sub(
        r"!\[([^\]]*)\]\(([^)]+)\)",
        lambda match: f"*Hình minh họa được lược bỏ trong bản PDF: {match.group(1) or match.group(2)}.*",
        text,
    )
    text = re.sub(r"\[([^\]]+)\]\(([^)]+\.md)\)", r"\1", text)
    text = re.sub(r"<div class=\"[^\"]+\">", "", text)
    text = text.replace("</div>", "")
    text = text.replace("<section>", "").replace("</section>", "")
    text = text.replace("<article>", "").replace("</article>", "")
    return text


def build_bundle(markdown_pages: list[tuple[str, str]]) -> str:
    toc_lines = [
        "## Mục lục",
        "",
    ]
    for index, (title, _) in enumerate(markdown_pages, start=1):
        toc_lines.append(f"{index}. {title}")

    lines = [
        "# Student IT Handbook",
        "",
        "> Bản PDF tổng hợp được tạo từ toàn bộ handbook theo thứ tự điều hướng chính.",
        "> File này được tạo tự động từ `scripts/generate_pdf_bundle.py`. Không sửa trực tiếp.",
        "",
        "Tài liệu này ưu tiên bản in gọn, dễ đọc và đủ nội dung cốt lõi cho việc tra cứu.",
        "",
        *toc_lines,
        "",
        '<div class="pdf-page-break"></div>',
        "",
    ]

    for index, (_, markdown_file) in enumerate(markdown_pages):
        if index > 0:
            lines.extend(["", '<div class="pdf-page-break"></div>', ""])

        lines.append(f"<!-- Source: {markdown_file} -->")
        lines.append("")
        lines.append(read_markdown_file(markdown_file))
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    config = yaml.unsafe_load(MKDOCS_CONFIG.read_text(encoding="utf-8"))
    nav = config.get("nav", [])

    markdown_pages: list[tuple[str, str]] = []
    seen: set[str] = set()

    for title, page in flatten_nav(nav):
        if not page.endswith(".md"):
            continue
        if page in {"index.md", "_generated/handbook-pdf.md"}:
            continue
        if page in seen:
            continue
        seen.add(page)
        markdown_pages.append((title, page))

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(build_bundle(markdown_pages), encoding="utf-8")

    print(f"Generated PDF bundle: {OUTPUT_FILE}")
    print(f"Included {len(markdown_pages)} markdown files.")


if __name__ == "__main__":
    main()
