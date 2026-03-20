#!/usr/bin/env python3
import argparse
import os
import re
import sys
from statistics import median

FILENAME_RE = re.compile(r'^(\d{4})-(.+)\.md$')
HEADER_RE = re.compile(r'^#\s*第(\d+)章\s+(.+?)\s*$')
CJK_RE = re.compile(r'[\u4e00-\u9fff]')
WORD_RE = re.compile(r"[A-Za-z0-9_']+")


def count_units(text: str) -> int:
    cjk = len(CJK_RE.findall(text))
    words = len(WORD_RE.findall(text))
    return cjk + words


def load_files(directory: str, start: int | None, end: int | None):
    items = []
    for name in sorted(os.listdir(directory)):
        m = FILENAME_RE.match(name)
        if not m:
            continue
        num = int(m.group(1))
        if start is not None and num < start:
            continue
        if end is not None and num > end:
            continue
        path = os.path.join(directory, name)
        if not os.path.isfile(path):
            continue
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()
        items.append((num, name, text))
    return items


def first_header(text: str):
    for line in text.splitlines():
        if line.strip():
            m = HEADER_RE.match(line.strip())
            return m
    return None


def main():
    ap = argparse.ArgumentParser(description='Check recut chapter sequence, headers, and approximate length consistency.')
    ap.add_argument('directory', help='Directory containing chapter markdown files')
    ap.add_argument('--start', type=int, default=None, help='Start chapter number, e.g. 94')
    ap.add_argument('--end', type=int, default=None, help='End chapter number, e.g. 107')
    ap.add_argument('--min-units', type=int, default=800, help='Warn when a chapter is shorter than this combined CJK+word count')
    ap.add_argument('--max-units', type=int, default=5000, help='Warn when a chapter is longer than this combined CJK+word count')
    args = ap.parse_args()

    items = load_files(args.directory, args.start, args.end)
    if not items:
        print('ERROR: no matching chapter files found', file=sys.stderr)
        sys.exit(2)

    nums = [num for num, _, _ in items]
    missing = []
    for expected in range(nums[0], nums[-1] + 1):
        if expected not in nums:
            missing.append(expected)

    print(f'Directory: {args.directory}')
    print(f'Files checked: {len(items)}')
    print()

    lengths = []
    errors = 0
    warnings = 0

    for num, name, text in items:
        units = count_units(text)
        lengths.append(units)
        header = first_header(text)
        status = []

        if header is None:
            status.append('ERROR no header')
            errors += 1
        else:
            h_num = int(header.group(1))
            h_title = header.group(2)
            if h_num != num:
                status.append(f'ERROR header number {h_num} != filename number {num}')
                errors += 1
            stem_title = FILENAME_RE.match(name).group(2)
            if h_title != stem_title:
                status.append(f'WARN header title != filename title ({h_title} vs {stem_title})')
                warnings += 1

        if units < args.min_units:
            status.append(f'WARN short ({units})')
            warnings += 1
        elif units > args.max_units:
            status.append(f'WARN long ({units})')
            warnings += 1
        else:
            status.append(f'OK len={units}')

        print(f'{name}: ' + ' | '.join(status))

    print()
    if missing:
        print('Missing chapter numbers: ' + ', '.join(str(x) for x in missing))
        warnings += 1
    else:
        print('Missing chapter numbers: none')

    med = int(median(lengths)) if lengths else 0
    print(f'Median length: {med}')
    print(f'Errors: {errors}')
    print(f'Warnings: {warnings}')

    if errors:
        sys.exit(1)


if __name__ == '__main__':
    main()
