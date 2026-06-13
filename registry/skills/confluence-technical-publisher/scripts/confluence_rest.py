#!/usr/bin/env python3
"""Generic Confluence Cloud REST helper for storage updates and page properties."""

from __future__ import annotations

import argparse
import base64
import getpass
import json
import os
from pathlib import Path
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


def request_json(
    method: str,
    url: str,
    email: str,
    token: str,
    body: dict | None = None,
) -> tuple[int, dict]:
    auth = base64.b64encode(f"{email}:{token}".encode()).decode()
    data = json.dumps(body).encode() if body is not None else None
    headers = {
        "Authorization": f"Basic {auth}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
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


def property_url(site: str, page_id: str, key: str | None = None) -> str:
    base = f"{content_url(site, page_id)}/property"
    if key is None:
        return base
    return f"{base}/{urllib.parse.quote(key)}"


def print_result(payload: dict, status: int, json_output: bool) -> None:
    result = {"http_status": status, **payload}
    if json_output:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(json.dumps(result, indent=2, sort_keys=True))


def cmd_get_page(args: argparse.Namespace, token: str) -> int:
    url = content_url(args.site, args.page_id)
    if args.expand:
        url = f"{url}?expand={urllib.parse.quote(args.expand, safe=',.')}"
    status, payload = request_json("GET", url, args.email, token)
    print_result({"page": payload}, status, args.json)
    return 0 if 200 <= status < 300 else 1


def cmd_update_storage(args: argparse.Namespace, token: str) -> int:
    url = content_url(args.site, args.page_id)
    status, current = request_json("GET", f"{url}?expand=version", args.email, token)
    if status < 200 or status >= 300:
        print_result({"stage": "get", "response": current}, status, args.json)
        return 1

    storage = Path(args.storage_file).read_text()
    payload = {
        "id": args.page_id,
        "type": "page",
        "title": args.title,
        "space": {"key": args.space_key},
        "version": {
            "number": current["version"]["number"] + 1,
            "message": args.message,
        },
        "body": {"storage": {"value": storage, "representation": "storage"}},
    }
    update_status, update_payload = request_json("PUT", url, args.email, token, payload)
    print_result({"stage": "update", "response": update_payload}, update_status, args.json)
    return 0 if 200 <= update_status < 300 else 1


def cmd_list_attachments(args: argparse.Namespace, token: str) -> int:
    url = f"{content_url(args.site, args.page_id)}/child/attachment?expand=version,metadata"
    status, payload = request_json("GET", url, args.email, token)
    rows = []
    for item in payload.get("results", []):
        rows.append(
            {
                "title": item.get("title", ""),
                "id": item.get("id", ""),
                "mediaType": item.get("metadata", {}).get("mediaType", ""),
                "version": item.get("version", {}).get("number"),
                "download": item.get("_links", {}).get("download", ""),
            }
        )
    print_result({"attachments": rows}, status, args.json)
    return 0 if 200 <= status < 300 else 1


def cmd_upsert_property(args: argparse.Namespace, token: str) -> int:
    get_status, existing = request_json("GET", property_url(args.site, args.page_id, args.key), args.email, token)
    if get_status == 200:
        body = {
            "key": args.key,
            "value": args.value,
            "version": {"number": existing.get("version", {}).get("number", 0) + 1},
        }
        method = "PUT"
        write_status, write_payload = request_json(
            method, property_url(args.site, args.page_id, args.key), args.email, token, body
        )
    elif get_status == 404:
        body = {"key": args.key, "value": args.value}
        method = "POST"
        write_status, write_payload = request_json(
            method, property_url(args.site, args.page_id), args.email, token, body
        )
    else:
        print_result({"stage": "get", "response": existing}, get_status, args.json)
        return 1

    verify_status, verify = request_json("GET", property_url(args.site, args.page_id, args.key), args.email, token)
    ok = 200 <= write_status < 300 and verify_status == 200 and verify.get("value") == args.value
    print_result(
        {
            "method": method,
            "write_http_status": write_status,
            "verify_http_status": verify_status,
            "key": verify.get("key"),
            "value": verify.get("value"),
            "version": verify.get("version", {}).get("number"),
            "write_response": write_payload,
            "ok": ok,
        },
        write_status,
        args.json,
    )
    return 0 if ok else 1


def cmd_verify_property(args: argparse.Namespace, token: str) -> int:
    status, payload = request_json("GET", property_url(args.site, args.page_id, args.key), args.email, token)
    ok = status == 200 and payload.get("value") == args.expect
    print_result(
        {
            "key": payload.get("key"),
            "value": payload.get("value"),
            "expected": args.expect,
            "version": payload.get("version", {}).get("number"),
            "ok": ok,
        },
        status,
        args.json,
    )
    return 0 if ok else 1


def add_common(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--site", required=True, help="Atlassian site, e.g. https://example.atlassian.net")
    parser.add_argument("--page-id", required=True, help="Confluence page/content ID")
    parser.add_argument("--email", required=True, help="Atlassian account email")
    parser.add_argument("--stdin-token", action="store_true", help="Read API token from stdin")
    parser.add_argument("--json", action="store_true", help="Print JSON output")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    get_page = subparsers.add_parser("get-page", help="Fetch a page")
    add_common(get_page)
    get_page.add_argument("--expand", default="body.storage,version,space")
    get_page.set_defaults(func=cmd_get_page)

    update = subparsers.add_parser("update-storage", help="Replace a page storage body")
    add_common(update)
    update.add_argument("--title", required=True)
    update.add_argument("--space-key", required=True)
    update.add_argument("--storage-file", required=True)
    update.add_argument("--message", default="Update Confluence storage body")
    update.set_defaults(func=cmd_update_storage)

    attachments = subparsers.add_parser("list-attachments", help="List page attachments")
    add_common(attachments)
    attachments.set_defaults(func=cmd_list_attachments)

    upsert = subparsers.add_parser("upsert-property", help="Create or update a page property")
    add_common(upsert)
    upsert.add_argument("--key", required=True)
    upsert.add_argument("--value", required=True)
    upsert.set_defaults(func=cmd_upsert_property)

    verify = subparsers.add_parser("verify-property", help="Verify a page property value")
    add_common(verify)
    verify.add_argument("--key", required=True)
    verify.add_argument("--expect", required=True)
    verify.set_defaults(func=cmd_verify_property)

    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    token = read_token(args.stdin_token)
    return args.func(args, token)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
