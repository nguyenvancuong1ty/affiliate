#!/usr/bin/env python3
"""Convert the crawled Module 1 Markdown into a lossless mind-map tree."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


def make_node(node_id: str, label: str, level: int) -> dict:
    return {"id": node_id, "label": label, "level": level, "content": [], "children": []}


def build_tree(markdown: str) -> tuple[dict, int]:
    lines = markdown.splitlines()
    first_heading = next((HEADING.match(line) for line in lines if HEADING.match(line)), None)
    title = first_heading.group(2) if first_heading else "Module 1"
    root = make_node("root", title, 0)
    stack = [root]
    next_id = 1
    skipped_title = False

    for line in lines:
        match = HEADING.match(line)
        if match:
            level = len(match.group(1))
            label = match.group(2)
            if not skipped_title and level == 1 and label == title:
                skipped_title = True
                continue
            while stack[-1]["level"] >= level:
                stack.pop()
            node = make_node(f"node-{next_id}", label, level)
            next_id += 1
            stack[-1]["children"].append(node)
            stack.append(node)
        else:
            stack[-1]["content"].append(line)

    def finalize(node: dict) -> None:
        node["content"] = "\n".join(node["content"]).strip()
        for child in node["children"]:
            finalize(child)

    finalize(root)
    return root, next_id


def main() -> None:
    parser = argparse.ArgumentParser(description="Build data for the Module 1 canvas mind map.")
    parser.add_argument("source", type=Path, help="Crawled Markdown source")
    parser.add_argument("output", type=Path, help="JavaScript data output")
    args = parser.parse_args()

    source = args.source.resolve()
    markdown = source.read_text(encoding="utf-8")
    tree, node_count = build_tree(markdown)
    payload = {
        "source": source.name,
        "sourceCharacters": len(markdown),
        "tree": tree,
    }
    output = args.output.resolve()
    output.write_text(
        "window.MODULE_1_MINDMAP = "
        + json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
        + ";\n",
        encoding="utf-8",
    )
    print(f"Đã tạo {node_count - 1} node từ {len(markdown)} ký tự: {output}")


if __name__ == "__main__":
    main()
