#!/usr/bin/env python3
"""Convert a local source file to Markdown with Microsoft MarkItDown.

This wrapper keeps skill usage consistent and intentionally limits conversion
to local files. It does not install dependencies or fetch remote URLs.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from urllib.parse import urlparse


def is_remote_like(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https", "ftp", "ftps", "s3"}


def dependency_hint(extras: str) -> str:
    extras = extras.strip() or "all"
    return (
        "MarkItDown is not installed. Install it with:\n"
        f"  python3 -m pip install 'markitdown[{extras}]'"
    )


def load_markitdown(extras: str):
    try:
        from markitdown import MarkItDown  # type: ignore
    except ModuleNotFoundError as exc:
        if exc.name == "markitdown":
            raise RuntimeError(dependency_hint(extras)) from exc
        raise
    return MarkItDown


def resolve_output(input_path: Path, output: str | None) -> Path | None:
    if output == "-":
        return None
    if output:
        return Path(output).expanduser().resolve()
    return input_path.with_suffix(".md")


def extract_text(result: object) -> str:
    for attr in ("text_content", "markdown"):
        value = getattr(result, attr, None)
        if isinstance(value, str):
            return value
    raise RuntimeError("MarkItDown returned no text_content or markdown field.")


def convert(input_path: Path, output_path: Path | None, force: bool, extras: str) -> None:
    if not input_path.exists():
        raise RuntimeError(f"Input file not found: {input_path}")
    if not input_path.is_file():
        raise RuntimeError(f"Input is not a file: {input_path}")

    if output_path is not None:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        if output_path.exists() and not force:
            raise RuntimeError(f"Output exists; pass --force to overwrite: {output_path}")
        if output_path.resolve() == input_path.resolve():
            raise RuntimeError("Output path must differ from input path.")

    MarkItDown = load_markitdown(extras)
    converter = MarkItDown(enable_plugins=False)

    if hasattr(converter, "convert_local"):
        result = converter.convert_local(str(input_path))
    else:
        raise RuntimeError(
            "Installed MarkItDown does not expose convert_local(); upgrade MarkItDown."
        )

    markdown = extract_text(result)

    if output_path is None:
        sys.stdout.write(markdown)
        if markdown and not markdown.endswith("\n"):
            sys.stdout.write("\n")
        print(f"Converted {input_path} to stdout", file=sys.stderr)
        return

    output_path.write_text(markdown, encoding="utf-8")
    print(f"Converted {input_path} -> {output_path}", file=sys.stderr)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Convert a local file to Markdown using Microsoft MarkItDown."
    )
    parser.add_argument("input", help="Local input file to convert")
    parser.add_argument(
        "-o",
        "--output",
        help="Output Markdown path. Use '-' for stdout. Defaults to INPUT with .md suffix.",
    )
    parser.add_argument(
        "--extras",
        default="all",
        help="Install hint extras for missing dependency, e.g. all or pdf,docx,pptx,xlsx.",
    )
    parser.add_argument(
        "--local-only",
        action="store_true",
        help="Accepted for explicitness; remote inputs are always rejected.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing output file.",
    )
    args = parser.parse_args(argv)

    if is_remote_like(args.input):
        print(
            "Error: remote inputs are intentionally unsupported; download the file first.",
            file=sys.stderr,
        )
        return 2

    try:
        input_path = Path(args.input).expanduser().resolve()
        output_path = resolve_output(input_path, args.output)
        convert(input_path, output_path, args.force, args.extras)
        return 0
    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
