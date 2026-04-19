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
    parser.add_argument("--site-dir", default="site", help="Built MkDocs site directory.")
    parser.add_argument("--page", default="_generated/handbook-pdf/", help="Route to print, relative to site root.")
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
            print_background=True,
            margin={"top": "16mm", "right": "14mm", "bottom": "16mm", "left": "14mm"},
        )
        browser.close()

    print(f"PDF written to {output_path}")


if __name__ == "__main__":
    main()
