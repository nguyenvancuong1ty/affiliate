#!/usr/bin/env python3
"""Normalize the heading hierarchy of the crawled Module 1 Markdown."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


def normalize(markdown: str) -> str:
    output: list[str] = []
    in_overview = False
    in_types = False
    in_type = False
    in_part = False
    in_exercise = False

    for line in markdown.splitlines():
        match = HEADING.match(line)
        if not match:
            output.append(line)
            continue

        level = len(match.group(1))
        label = match.group(2)

        if level == 1 and label.startswith("I."):
            in_overview = True
            in_types = False
            in_type = False
            in_part = False
            in_exercise = False
            output.append(f"# {label}")
            continue
        if level == 1 and label.startswith("II."):
            in_overview = False
            in_types = True
            in_type = False
            in_part = False
            in_exercise = False
            output.append(f"# {label}")
            continue

        if in_overview:
            if label.startswith("A. Script body không phải quảng cáo"):
                label = "1. Script body không phải quảng cáo"
            output.append(f"{'#' * level} {label}")
            continue

        if in_types:
            if "LOẠI 1:" in label or "LOẠI 2:" in label or "LOẠI 3:" in label:
                in_type = True
                in_part = False
                in_exercise = False
                output.append(f"## {label}")
                continue
            if label.startswith("Bài Tập Thực Hành"):
                in_type = False
                in_part = False
                in_exercise = True
                output.append(f"## {label}")
                continue
            if in_exercise:
                if label.startswith("🎯") or level == 1:
                    output.append(f"### {label}")
                elif level >= 3:
                    output.append(f"#### {label}")
                else:
                    output.append(f"### {label}")
                continue
            if in_type:
                if level == 2 and label.startswith("PHẦN "):
                    in_part = True
                    output.append(f"### {label}")
                elif label == "Script mẫu":
                    output.append(f"### {label}")
                elif in_part and level >= 3:
                    if label.startswith("BƯỚC "):
                        output.append(f"##### {label}")
                    else:
                        output.append(f"#### {label}")
                elif level == 2:
                    in_part = False
                    output.append(f"### {label}")
                else:
                    output.append(f"### {label}")
                continue

        output.append(line)

    return "\n".join(output) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Normalize Module 1 Markdown headings.")
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    text = args.input.read_text(encoding="utf-8")
    args.output.write_text(normalize(text), encoding="utf-8")
    print(f"Đã chuẩn hóa heading: {args.output}")


if __name__ == "__main__":
    main()
