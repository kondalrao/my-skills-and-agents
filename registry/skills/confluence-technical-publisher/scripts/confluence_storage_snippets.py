#!/usr/bin/env python3
"""Generate Confluence storage-format snippets for common publishing patterns."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys
import xml.sax.saxutils as xml_escape


def cdata(text: str) -> str:
    return "<![CDATA[" + text.replace("]]>", "]]]]><![CDATA[>") + "]]>"


def attr(value: str) -> str:
    return xml_escape.escape(value, {'"': "&quot;"})


def toc(max_level: str) -> str:
    return (
        '<ac:structured-macro ac:name="toc">\n'
        f'  <ac:parameter ac:name="maxLevel">{attr(max_level)}</ac:parameter>\n'
        "</ac:structured-macro>"
    )


def code_macro(mermaid: str) -> str:
    return (
        '<ac:structured-macro ac:name="code" ac:schema-version="1">\n'
        '<ac:parameter ac:name="language">mermaid</ac:parameter>\n'
        f"<ac:plain-text-body>{cdata(mermaid)}</ac:plain-text-body>\n"
        "</ac:structured-macro>"
    )


def svg_two_pane(mermaid: str, svg: str, width: int) -> str:
    return f"""<table data-layout="wide"><tbody>
<tr><th><p>Mermaid source</p></th><th><p>Rendered SVG</p></th></tr>
<tr>
<td>
{code_macro(mermaid)}
</td>
<td>
<ac:image ac:width="{width}">
<ri:attachment ri:filename="{attr(svg)}" />
</ac:image>
</td>
</tr>
</tbody></table>"""


def png_svg_two_pane(mermaid: str, png: str, svg: str, width: int) -> str:
    return f"""<table data-layout="wide"><tbody>
<tr><th><p>Mermaid source</p></th><th><p>Rendered image</p></th></tr>
<tr>
<td>
{code_macro(mermaid)}
</td>
<td>
<ac:image ac:width="{width}">
<ri:attachment ri:filename="{attr(png)}" />
</ac:image>
<p>
<ac:link>
<ri:attachment ri:filename="{attr(svg)}" />
<ac:plain-text-link-body><![CDATA[Open SVG attachment]]></ac:plain-text-link-body>
</ac:link>
</p>
</td>
</tr>
</tbody></table>"""


def read_mermaid(path: str) -> str:
    return Path(path).read_text().strip()


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    toc_parser = subparsers.add_parser("toc", help="Print a Confluence TOC macro")
    toc_parser.add_argument("--max-level", default="3")

    svg = subparsers.add_parser("svg-two-pane", help="Print an SVG-only two-pane diagram table")
    svg.add_argument("--mermaid-file", required=True)
    svg.add_argument("--svg", required=True)
    svg.add_argument("--image-width", type=int, default=760)

    png_svg = subparsers.add_parser("png-svg-two-pane", help="Print a PNG preview plus SVG link table")
    png_svg.add_argument("--mermaid-file", required=True)
    png_svg.add_argument("--png", required=True)
    png_svg.add_argument("--svg", required=True)
    png_svg.add_argument("--image-width", type=int, default=760)

    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    if args.command == "toc":
        print(toc(args.max_level))
    elif args.command == "svg-two-pane":
        print(svg_two_pane(read_mermaid(args.mermaid_file), args.svg, args.image_width))
    elif args.command == "png-svg-two-pane":
        print(png_svg_two_pane(read_mermaid(args.mermaid_file), args.png, args.svg, args.image_width))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
