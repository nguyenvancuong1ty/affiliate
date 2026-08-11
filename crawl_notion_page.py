#!/usr/bin/env python3
"""Export every text block from a public Notion page to Markdown."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.request import Request, urlopen


def page_id_from_url(url: str) -> str:
    match = re.search(r"([0-9a-f]{32})(?:[?#]|$)", url, re.IGNORECASE)
    if not match:
        raise ValueError("Khong tim thay page ID 32 ky tu trong URL Notion.")
    value = match.group(1).lower()
    return f"{value[:8]}-{value[8:12]}-{value[12:16]}-{value[16:20]}-{value[20:]}"


def load_chunk(host: str, page_id: str, cursor: dict, chunk_number: int) -> dict:
    payload = json.dumps(
        {
            "pageId": page_id,
            "limit": 100,
            "cursor": cursor,
            "chunkNumber": chunk_number,
            "verticalColumns": False,
        }
    ).encode("utf-8")
    request = Request(
        f"{host}/api/v3/loadCachedPageChunk",
        data=payload,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Notion document exporter)",
        },
        method="POST",
    )
    with urlopen(request, timeout=30) as response:
        return json.load(response)


def crawl_page(host: str, page_id: str) -> tuple[dict[str, dict], list[str], int]:
    cursor: dict = {"stack": []}
    seen_cursors: set[str] = set()
    blocks: dict[str, dict] = {}
    block_order: list[str] = []

    for chunk_number in range(100):
        response = load_chunk(host, page_id, cursor, chunk_number)
        for block_id, record in (response.get("recordMap", {}).get("block", {})).items():
            block = unwrap(record)
            if block is not None and block_id not in blocks:
                blocks[block_id] = block
                block_order.append(block_id)

        next_cursor = response.get("cursor")
        cursor_key = json.dumps(next_cursor, sort_keys=True, ensure_ascii=False)
        if not next_cursor or not next_cursor.get("stack") or cursor_key in seen_cursors:
            return blocks, block_order, chunk_number + 1
        seen_cursors.add(cursor_key)
        cursor = next_cursor

    raise RuntimeError("Notion page vuot qua 100 chunks; dung de tranh lap vo han.")


def unwrap(record: dict) -> dict | None:
    value = record.get("value", {})
    if isinstance(value, dict):
        value = value.get("value", value)
    return value if isinstance(value, dict) and value.get("alive", True) else None


def plain_text(value: object) -> str:
    if not isinstance(value, list):
        return ""
    parts: list[str] = []
    for fragment in value:
        if isinstance(fragment, list) and fragment and isinstance(fragment[0], str):
            parts.append(fragment[0])
    return "".join(parts).replace("\n", " ").strip()


def block_text(block: dict) -> str:
    properties = block.get("properties") or {}
    for key in ("title", "caption", "source"):
        text = plain_text(properties.get(key))
        if text:
            return text
    return ""


def render_block(block: dict, root_id: str) -> str:
    block_type = block.get("type", "text")
    text = block_text(block)
    if block.get("id") == root_id:
        return ""
    if block_type == "header":
        return f"# {text}" if text else ""
    if block_type == "sub_header":
        return f"## {text}" if text else ""
    if block_type == "sub_sub_header":
        return f"### {text}" if text else ""
    if block_type == "bulleted_list":
        return f"- {text}" if text else ""
    if block_type == "numbered_list":
        return f"1. {text}" if text else ""
    if block_type == "to_do":
        checked = (block.get("properties") or {}).get("checked")
        marker = "x" if checked == [["Yes"]] else " "
        return f"- [{marker}] {text}" if text else ""
    if block_type == "quote":
        return f"> {text}" if text else ""
    if block_type == "callout":
        return f"> **Luu y:** {text}" if text else ""
    if block_type == "toggle":
        return f"#### {text}" if text else ""
    if block_type == "divider":
        return "---"
    if block_type in {"code", "code_block"}:
        return f"```\n{text}\n```" if text else ""
    if block_type in {"image", "video", "embed", "bookmark", "pdf"}:
        return f"[{block_type}] {text}" if text else ""
    return text


def ordered_block_ids(blocks: dict[str, dict], root_id: str) -> tuple[list[str], set[str]]:
    ordered: list[str] = []
    missing: set[str] = set()
    visited: set[str] = {root_id}

    def visit(block_id: str) -> None:
        if block_id in visited:
            return
        block = blocks.get(block_id)
        if block is None:
            missing.add(block_id)
            return
        visited.add(block_id)
        ordered.append(block_id)
        for child_id in block.get("content") or []:
            visit(child_id)

    for child_id in blocks.get(root_id, {}).get("content") or []:
        visit(child_id)
    for block_id in blocks:
        visit(block_id)
    return ordered, missing


def main() -> None:
    parser = argparse.ArgumentParser(description="Crawl a public Notion page to Markdown.")
    parser.add_argument("url", help="Public Notion page URL")
    parser.add_argument("-o", "--output", type=Path, required=True, help="Markdown output path")
    args = parser.parse_args()

    page_id = page_id_from_url(args.url)
    host = args.url.split("/", 3)[:3]
    host = "/".join(host)
    blocks, _, chunk_count = crawl_page(host, page_id)
    expanded_pages: set[str] = set()

    # A Notion page can contain click-through child pages. Crawl every public
    # child page too, then include its blocks in the same Markdown export.
    while True:
        child_pages = [
            block_id
            for block_id, block in blocks.items()
            if block_id != page_id and block.get("type") == "page" and block_id not in expanded_pages
        ]
        if not child_pages:
            break
        for child_page_id in child_pages:
            expanded_pages.add(child_page_id)
            try:
                child_blocks, _, child_chunks = crawl_page(host, child_page_id)
            except Exception as error:
                print(f"Khong crawl duoc trang con {child_page_id}: {error}", file=sys.stderr)
                continue
            chunk_count += child_chunks
            for block_id, block in child_blocks.items():
                blocks.setdefault(block_id, block)

    fetched_references: set[str] = set()
    for _ in range(10):
        _, missing_blocks = ordered_block_ids(blocks, page_id)
        targets = sorted(missing_blocks - fetched_references)
        if not targets:
            break
        added_any = False
        for block_id in targets:
            fetched_references.add(block_id)
            try:
                child_blocks, _, child_chunks = crawl_page(host, block_id)
            except Exception as error:
                print(f"Khong crawl duoc block mo rong {block_id}: {error}", file=sys.stderr)
                continue
            chunk_count += child_chunks
            for child_id, block in child_blocks.items():
                if child_id not in blocks:
                    blocks[child_id] = block
                    added_any = True
        if not added_any:
            break

    root = blocks.get(page_id, {})
    title = block_text(root) or "Notion export"
    block_order, missing_blocks = ordered_block_ids(blocks, page_id)
    rendered = [render_block(blocks[block_id], page_id) for block_id in block_order]
    body = "\n\n".join(part for part in rendered if part)
    document = f"# {title}\n\nNguon: {args.url}\n\n---\n\n{body}\n"

    output = args.output.expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(document, encoding="utf-8")
    print(
        f"Da crawl {len(block_order)} blocks qua {chunk_count} chunks "
        f"({len(expanded_pages)} trang con, {len(missing_blocks)} block tham chieu thieu): {output}"
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Loi: {error}", file=sys.stderr)
        raise SystemExit(1)
