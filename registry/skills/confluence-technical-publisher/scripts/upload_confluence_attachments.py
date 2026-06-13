#!/usr/bin/env python3
"""Upload one or more attachments to a Confluence Cloud page.

The script intentionally prompts for the Atlassian API token at runtime unless
ATLASSIAN_API_TOKEN is set. Do not pass tokens as command-line arguments.
"""

from __future__ import annotations

import argparse
import base64
import getpass
import json
import mimetypes
import os
from pathlib import Path
import secrets
import sys
import urllib.error
import urllib.parse
import urllib.request


def build_multipart(fields: dict[str, str], file_path: Path) -> tuple[bytes, str]:
    boundary = f"----codex-atlassian-{secrets.token_hex(16)}"
    chunks: list[bytes] = []

    for name, value in fields.items():
        chunks.extend(
            [
                f"--{boundary}\r\n".encode(),
                f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode(),
                str(value).encode(),
                b"\r\n",
            ]
        )

    mime_type = mimetypes.guess_type(file_path.name)[0] or "application/octet-stream"
    chunks.extend(
        [
            f"--{boundary}\r\n".encode(),
            (
                'Content-Disposition: form-data; name="file"; '
                f'filename="{file_path.name}"\r\n'
            ).encode(),
            f"Content-Type: {mime_type}\r\n\r\n".encode(),
            file_path.read_bytes(),
            b"\r\n",
            f"--{boundary}--\r\n".encode(),
        ]
    )
    return b"".join(chunks), f"multipart/form-data; boundary={boundary}"


def request_json(
    method: str,
    url: str,
    email: str,
    token: str,
    body: bytes | None = None,
    content_type: str | None = None,
) -> tuple[int, dict]:
    auth = base64.b64encode(f"{email}:{token}".encode()).decode()
    headers = {
        "Authorization": f"Basic {auth}",
        "Accept": "application/json",
        "X-Atlassian-Token": "nocheck",
    }
    if content_type:
        headers["Content-Type"] = content_type

    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            payload = resp.read().decode()
            return resp.status, json.loads(payload) if payload else {}
    except urllib.error.HTTPError as exc:
        payload = exc.read().decode(errors="replace")
        try:
            parsed = json.loads(payload)
        except json.JSONDecodeError:
            parsed = {"error": payload}
        return exc.code, parsed


def upload_file(args: argparse.Namespace, token: str, file_path: Path) -> tuple[int, dict]:
    if not file_path.is_file():
        raise FileNotFoundError(file_path)

    site = args.site.rstrip("/")
    endpoint = f"{site}/wiki/rest/api/content/{urllib.parse.quote(args.page_id)}/child/attachment"
    fields = {
        "minorEdit": "true" if args.minor_edit else "false",
    }
    if args.comment:
        fields["comment"] = args.comment

    body, content_type = build_multipart(fields, file_path)
    return request_json(args.method, endpoint, args.email, token, body, content_type)


def summarize_attachment(result: dict) -> list[dict[str, str]]:
    rows = []
    for item in result.get("results", []):
        rows.append(
            {
                "title": item.get("title", ""),
                "id": item.get("id", ""),
                "mediaType": item.get("metadata", {}).get("mediaType", ""),
                "version": str(item.get("version", {}).get("number", "")),
                "download": item.get("_links", {}).get("download", ""),
            }
        )
    return rows


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Upload attachments to a Confluence Cloud page with runtime token prompting."
    )
    parser.add_argument("files", nargs="+", type=Path, help="Files to upload")
    parser.add_argument("--site", required=True, help="Atlassian site, e.g. https://example.atlassian.net")
    parser.add_argument("--page-id", required=True, help="Confluence page/content ID")
    parser.add_argument("--email", required=True, help="Atlassian account email")
    parser.add_argument(
        "--method",
        choices=("PUT", "POST"),
        default="PUT",
        help="PUT creates or updates same-named attachments; POST creates only",
    )
    parser.add_argument("--comment", default="", help="Attachment version comment")
    parser.add_argument("--minor-edit", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--response-dir", type=Path, help="Optional directory for raw JSON responses")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON summary")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    token = os.environ.get("ATLASSIAN_API_TOKEN") or getpass.getpass("Atlassian API token: ")
    if not token:
        print("error: token was empty", file=sys.stderr)
        return 2

    if args.response_dir:
        args.response_dir.mkdir(parents=True, exist_ok=True)

    summaries = []
    failures = []
    for file_path in args.files:
        status, result = upload_file(args, token, file_path)
        if args.response_dir:
            out = args.response_dir / f"{file_path.name}.response.json"
            out.write_text(json.dumps(result, indent=2, sort_keys=True))

        entry = {
            "file": str(file_path),
            "http_status": status,
            "attachments": summarize_attachment(result),
        }
        summaries.append(entry)
        if status < 200 or status >= 300:
            failures.append(entry)

    if args.json:
        print(json.dumps({"uploads": summaries, "failed": failures}, indent=2, sort_keys=True))
    else:
        for entry in summaries:
            print(f"{entry['file']}: HTTP {entry['http_status']}")
            for attachment in entry["attachments"]:
                print(
                    "  "
                    + "\t".join(
                        [
                            attachment["title"],
                            attachment["id"],
                            attachment["mediaType"],
                            f"version={attachment['version']}",
                            attachment["download"],
                        ]
                    )
                )

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
