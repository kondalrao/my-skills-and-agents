#!/usr/bin/env python3
"""Verify Confluence page state after a technical publishing update."""

from __future__ import annotations

import argparse
import base64
import getpass
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request


def read_token(stdin_token: bool) -> str:
    if stdin_token:
        token = sys.stdin.readline().strip()
    else:
        token = os.environ.get("ATLASSIAN_API_TOKEN") or getpass.getpass("Atlassian API token: ")
    if not token:
        raise SystemExit("error: token was empty")
    return token


def request_json(method: str, url: str, email: str, token: str) -> tuple[int, dict]:
    auth = base64.b64encode(f"{email}:{token}".encode()).decode()
    headers = {"Authorization": f"Basic {auth}", "Accept": "application/json"}
    req = urllib.request.Request(url, headers=headers, method=method)
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


def content_url(site: str, page_id: str) -> str:
    return f"{site.rstrip('/')}/wiki/rest/api/content/{urllib.parse.quote(page_id)}"


def parse_property_expectation(raw: str) -> tuple[str, str]:
    if "=" not in raw:
        raise argparse.ArgumentTypeError("property expectation must be KEY=VALUE")
    key, value = raw.split("=", 1)
    if not key:
        raise argparse.ArgumentTypeError("property key cannot be empty")
    return key, value


def attachment_titles(payload: dict) -> set[str]:
    return {item.get("title", "") for item in payload.get("results", [])}


def body_has_media_ref(body: str, filename: str) -> bool:
    return f'ri:filename="{filename}"' in body or f"ri:filename='{filename}'" in body


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", required=True, help="Atlassian site, e.g. https://example.atlassian.net")
    parser.add_argument("--page-id", required=True, help="Confluence page/content ID")
    parser.add_argument("--email", required=True, help="Atlassian account email")
    parser.add_argument("--stdin-token", action="store_true", help="Read API token from stdin")
    parser.add_argument("--expect-title", help="Expected page title")
    parser.add_argument("--expect-attachment", action="append", default=[], help="Attachment filename that must exist")
    parser.add_argument("--expect-body", action="append", default=[], help="Substring that must exist in storage body")
    parser.add_argument("--absent-body", action="append", default=[], help="Substring that must be absent in storage body")
    parser.add_argument(
        "--expect-property",
        action="append",
        default=[],
        type=parse_property_expectation,
        help="Expected page property in KEY=VALUE form",
    )
    parser.add_argument("--expect-media-ref", action="append", default=[], help="Attachment filename referenced in body")
    parser.add_argument("--json", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    token = read_token(args.stdin_token)
    checks: list[dict] = []

    page_status, page = request_json(
        "GET",
        f"{content_url(args.site, args.page_id)}?expand=body.storage,version,space",
        args.email,
        token,
    )
    body = page.get("body", {}).get("storage", {}).get("value", "")
    checks.append({"name": "fetch_page", "ok": 200 <= page_status < 300, "http_status": page_status})

    if args.expect_title:
        checks.append(
            {
                "name": "title",
                "ok": page.get("title") == args.expect_title,
                "expected": args.expect_title,
                "actual": page.get("title"),
            }
        )

    attachment_status, attachments = request_json(
        "GET",
        f"{content_url(args.site, args.page_id)}/child/attachment?expand=version,metadata",
        args.email,
        token,
    )
    titles = attachment_titles(attachments)
    checks.append({"name": "fetch_attachments", "ok": 200 <= attachment_status < 300, "http_status": attachment_status})
    for filename in args.expect_attachment:
        checks.append({"name": "attachment", "target": filename, "ok": filename in titles})

    for expected in args.expect_body:
        checks.append({"name": "body_contains", "target": expected, "ok": expected in body})
    for absent in args.absent_body:
        checks.append({"name": "body_absent", "target": absent, "ok": absent not in body})
    for filename in args.expect_media_ref:
        checks.append({"name": "media_ref", "target": filename, "ok": body_has_media_ref(body, filename)})

    for key, expected_value in args.expect_property:
        prop_status, prop = request_json(
            "GET",
            f"{content_url(args.site, args.page_id)}/property/{urllib.parse.quote(key)}",
            args.email,
            token,
        )
        checks.append(
            {
                "name": "property",
                "key": key,
                "expected": expected_value,
                "actual": prop.get("value"),
                "http_status": prop_status,
                "ok": prop_status == 200 and prop.get("value") == expected_value,
            }
        )

    ok = all(check["ok"] for check in checks)
    result = {"ok": ok, "page_id": args.page_id, "checks": checks}
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
