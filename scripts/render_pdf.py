from __future__ import annotations

import argparse
import contextlib
import socket
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread

from playwright.sync_api import sync_playwright


def get_free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


@contextlib.contextmanager
def serve_directory(directory: Path):
    port = get_free_port()
    handler = partial(SimpleHTTPRequestHandler, directory=str(directory))
    server = ThreadingHTTPServer(("127.0.0.1", port), handler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{port}"
    finally:
        server.shutdown()
        thread.join(timeout=5)
        server.server_close()


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a built MkDocs page to PDF with Chromium.")
    parser.add_argument("--site-dir", default="site", help="Directory containing the generated PDF HTML.")
    parser.add_argument("--page", default="pdf/handbook.html", help="Route to print, relative to site root.")
    parser.add_argument("--output", default="site/pdf/student-it-handbook.pdf", help="Output PDF path.")
    args = parser.parse_args()

    site_dir = Path(args.site_dir).resolve()
    output_path = Path(args.output).resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    route = args.page.lstrip("/")

    with serve_directory(site_dir) as base_url, sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()
        page.goto(f"{base_url}/{route}", wait_until="networkidle")
        page.emulate_media(media="print")
        page.add_style_tag(
            content="""
            * {
              animation: none !important;
              transition: none !important;
            }
            """
        )
        page.pdf(
            path=str(output_path),
            format="A4",
            print_background=False,
            prefer_css_page_size=True,
            display_header_footer=True,
            header_template="<div></div>",
            footer_template="""
            <div style="width:100%; font-size:9px; color:#6b7280; padding:0 14mm; font-family:Segoe UI, Arial, sans-serif;">
              <div style="width:100%; display:flex; justify-content:space-between; align-items:center;">
                <span>Student IT Handbook</span>
                <span><span class="pageNumber"></span> / <span class="totalPages"></span></span>
              </div>
            </div>
            """,
            margin={"top": "10mm", "right": "0", "bottom": "16mm", "left": "0"},
        )
        browser.close()

    print(f"PDF written to {output_path}")


if __name__ == "__main__":
    main()
