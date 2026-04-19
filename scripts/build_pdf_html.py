from __future__ import annotations

from pathlib import Path

import markdown


ROOT = Path(__file__).resolve().parents[1]
BUNDLE_FILE = ROOT / "docs" / "_generated" / "handbook-pdf.md"
CSS_FILE = ROOT / "docs" / "assets" / "css" / "pdf.css"
OUTPUT_FILE = ROOT / "site" / "pdf" / "handbook.html"


def build_html(markdown_text: str, css_text: str) -> str:
    body = markdown.markdown(
        markdown_text,
        extensions=[
            "admonition",
            "tables",
            "fenced_code",
            "attr_list",
            "md_in_html",
            "pymdownx.details",
            "pymdownx.superfences",
            "pymdownx.tasklist",
            "pymdownx.inlinehilite",
            "pymdownx.tilde",
            "pymdownx.caret",
            "toc",
        ],
        extension_configs={
            "pymdownx.tasklist": {
                "custom_checkbox": True,
            }
        },
        output_format="html5",
    )

    return f"""<!DOCTYPE html>
<html lang="vi">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Student IT Handbook</title>
    <style>
{css_text}
    </style>
  </head>
  <body>
    <main class="pdf-document">
{body}
    </main>
  </body>
</html>
"""


def main() -> None:
    markdown_text = BUNDLE_FILE.read_text(encoding="utf-8")
    css_text = CSS_FILE.read_text(encoding="utf-8")

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(build_html(markdown_text, css_text), encoding="utf-8")

    print(f"Built standalone PDF HTML: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
