#!/usr/bin/env python3
"""Render Mermaid files to HD SVG and PNG images using mermaid-cli."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET


PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def default_chrome_path() -> str | None:
    candidates = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "/usr/bin/google-chrome",
        "/usr/bin/chromium",
        "/usr/bin/chromium-browser",
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            return candidate
    return None


def write_install_script(path: Path) -> None:
    path.write_text(
        """#!/usr/bin/env bash
set -euo pipefail

if ! command -v npm >/dev/null 2>&1; then
  echo "npm is required. Install Node.js/npm first, then rerun this script." >&2
  exit 1
fi

if command -v mmdc >/dev/null 2>&1; then
  echo "mmdc already installed: $(mmdc --version)"
  exit 0
fi

echo "Installing @mermaid-js/mermaid-cli globally..."
npm install -g @mermaid-js/mermaid-cli

echo "Installed: $(mmdc --version)"
""",
    )
    path.chmod(0o755)


def validate_svg(path: Path) -> None:
    ET.parse(path)
    text = path.read_text(errors="replace")
    if "<svg" not in text:
        raise ValueError(f"{path} does not contain an <svg> root")


def validate_png(path: Path) -> None:
    if path.read_bytes()[:8] != PNG_SIGNATURE:
        raise ValueError(f"{path} does not have a PNG signature")


def run_mmdc(
    mmdc: str,
    source: Path,
    output: Path,
    width: int,
    height: int,
    scale: int,
    background: str,
    env: dict[str, str],
) -> None:
    cmd = [
        mmdc,
        "-i",
        str(source),
        "-o",
        str(output),
        "--backgroundColor",
        background,
        "--width",
        str(width),
        "--height",
        str(height),
        "--scale",
        str(scale),
    ]
    subprocess.run(cmd, check=True, env=env)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render Mermaid .mmd files to HD SVG and PNG outputs.")
    parser.add_argument("files", nargs="+", type=Path, help="Mermaid .mmd files to render")
    parser.add_argument("--output-dir", type=Path, required=True, help="Directory for generated images")
    parser.add_argument("--width", type=int, default=1920, help="Browser viewport width")
    parser.add_argument("--height", type=int, default=1080, help="Browser viewport height")
    parser.add_argument("--scale", type=int, default=2, help="Puppeteer scale factor for PNG/PDF output")
    parser.add_argument("--background", default="white", help="Mermaid background color")
    parser.add_argument("--mmdc", default=shutil.which("mmdc"), help="Path to mmdc")
    parser.add_argument("--chrome-path", default=os.environ.get("PUPPETEER_EXECUTABLE_PATH") or default_chrome_path())
    parser.add_argument(
        "--write-install-script",
        type=Path,
        help="Write a Mermaid CLI install script here when mmdc is unavailable",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    if not args.mmdc:
        if args.write_install_script:
            write_install_script(args.write_install_script)
            print(f"mmdc not found. Wrote install script: {args.write_install_script}", file=sys.stderr)
        else:
            print(
                "mmdc not found. Ask the user before installing globally, or rerun with "
                "--write-install-script /path/to/install_mermaid_cli.sh.",
                file=sys.stderr,
            )
        return 2

    args.output_dir.mkdir(parents=True, exist_ok=True)

    env = os.environ.copy()
    if args.chrome_path:
        env["PUPPETEER_EXECUTABLE_PATH"] = args.chrome_path

    results = []
    for source in args.files:
        if not source.is_file():
            raise FileNotFoundError(source)

        base = source.stem
        svg = args.output_dir / f"{base}.svg"
        png = args.output_dir / f"{base}.png"

        run_mmdc(args.mmdc, source, svg, args.width, args.height, args.scale, args.background, env)
        validate_svg(svg)

        run_mmdc(args.mmdc, source, png, args.width, args.height, args.scale, args.background, env)
        validate_png(png)

        results.append((source, svg, png))

    for source, svg, png in results:
        print(f"{source}:")
        print(f"  SVG {svg} {svg.stat().st_size} bytes")
        print(f"  PNG {png} {png.stat().st_size} bytes")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
