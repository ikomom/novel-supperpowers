#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path

CHAPTER_RE = re.compile(r'^(第[\d一二三四五六七八九十百千万兩零〇○]+[章节回集部卷篇幕]\s*.*)$')


def detect_encoding_read(path: Path) -> str:
    for enc in ("utf-8", "utf-8-sig", "gb18030", "big5", "latin-1"):
        try:
            return path.read_text(encoding=enc)
        except Exception:
            continue
    raise RuntimeError(f"Unable to read file with common encodings: {path}")


def split_chapters(text: str):
    lines = text.splitlines()
    chapters = []
    current = None
    preface = []

    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        if CHAPTER_RE.match(stripped):
            if current is not None:
                chapters.append(current)
            current = {
                "title": stripped,
                "start_line": idx,
                "lines": [],
            }
        else:
            if current is None:
                preface.append(line)
            else:
                current["lines"].append(line)

    if current is not None:
        chapters.append(current)

    return preface, chapters


def summarize_text(lines, max_chars=120):
    text = " ".join(x.strip() for x in lines if x.strip())
    text = re.sub(r'\s+', ' ', text)
    return text[:max_chars] + ("..." if len(text) > max_chars else "")


def main():
    ap = argparse.ArgumentParser(description="Build chapter index/story map for long-form novel txt files.")
    ap.add_argument("input", help="Path to source txt file")
    ap.add_argument("--out", help="Output JSON path; defaults next to input", default=None)
    ap.add_argument("--preview-chars", type=int, default=120)
    args = ap.parse_args()

    path = Path(args.input).expanduser().resolve()
    text = detect_encoding_read(path)
    preface, chapters = split_chapters(text)

    data = {
        "source": str(path),
        "preface_preview": summarize_text(preface, args.preview_chars),
        "chapter_count": len(chapters),
        "chapters": [],
    }

    for i, ch in enumerate(chapters, start=1):
        body_lines = ch["lines"]
        data["chapters"].append({
            "index": i,
            "title": ch["title"],
            "start_line": ch["start_line"],
            "line_count": len(body_lines),
            "preview": summarize_text(body_lines, args.preview_chars),
        })

    out_path = Path(args.out).expanduser().resolve() if args.out else path.with_suffix(path.suffix + ".story-map.json")
    out_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(out_path)


if __name__ == "__main__":
    main()
