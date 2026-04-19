from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable

import yaml


ROOT = Path(__file__).resolve().parents[1]
MKDOCS_CONFIG = ROOT / "mkdocs.yml"
DOCS_DIR = ROOT / "docs"
OUTPUT_FILE = DOCS_DIR / "_generated" / "handbook-pdf.md"


def flatten_nav(nav: list) -> Iterable[str]:
    for item in nav:
        if isinstance(item, dict):
            for value in item.values():
                if isinstance(value, str):
                    yield value
                elif isinstance(value, list):
                    yield from flatten_nav(value)
        elif isinstance(item, str):
            yield item


def read_markdown_file(markdown_file: str) -> str:
    source = DOCS_DIR / markdown_file
    text = source.read_text(encoding="utf-8").strip()
    text = sanitize_markdown(text)
    return text


def sanitize_markdown(text: str) -> str:
    # Keep PDF content focused on text and commands, not web-only diagrams/images.
    text = re.sub(
        r"```mermaid\s+.*?```",
        "> So do duoc luoc bo trong ban PDF. Xem ban web neu can hinh minh hoa.",
        text,
        flags=re.DOTALL,
    )
    text = re.sub(
        r"!\[([^\]]*)\]\(([^)]+)\)",
        lambda match: f"*Hinh minh hoa duoc luoc bo trong ban PDF: {match.group(1) or match.group(2)}.*",
        text,
    )
    text = re.sub(r"\[([^\]]+)\]\(([^)]+\.md)\)", r"\1", text)
    text = re.sub(r"<div class=\"[^\"]+\">", "", text)
    text = text.replace("</div>", "")
    text = text.replace("<section>", "").replace("</section>", "")
    text = text.replace("<article>", "").replace("</article>", "")
    return text


def build_bundle(markdown_files: list[str]) -> str:
    lines = [
        "# Student IT Handbook",
        "",
        "> Ban PDF tong hop duoc tao tu toan bo handbook theo thu tu dieu huong chinh.",
        "> File nay duoc generate tu `scripts/generate_pdf_bundle.py`. Khong sua truc tiep.",
        "",
    ]

    for index, markdown_file in enumerate(markdown_files):
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

    markdown_files: list[str] = []
    seen: set[str] = set()

    for page in flatten_nav(nav):
        if not page.endswith(".md"):
            continue
        if page in {"index.md", "_generated/handbook-pdf.md"}:
            continue
        if page in seen:
            continue
        seen.add(page)
        markdown_files.append(page)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(build_bundle(markdown_files), encoding="utf-8")

    print(f"Generated PDF bundle: {OUTPUT_FILE}")
    print(f"Included {len(markdown_files)} markdown files.")


if __name__ == "__main__":
    main()
