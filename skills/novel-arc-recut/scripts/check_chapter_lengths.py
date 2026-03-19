#!/usr/bin/env python3
import argparse, os, re, sys
from statistics import median
FILENAME_RE = re.compile(r'^(\d{4})-(.+)\.md$')
HEADER_RE = re.compile(r'^#\s*第(\d+)章\s+(.+?)\s*$')
CJK_RE = re.compile(r'[\u4e00-\u9fff]')
WORD_RE = re.compile(r"[A-Za-z0-9_']+")

def count_units(text):
    return len(CJK_RE.findall(text)) + len(WORD_RE.findall(text))

def first_header(text):
    for line in text.splitlines():
        if line.strip():
            return HEADER_RE.match(line.strip())
    return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('directory')
    ap.add_argument('--start', type=int, default=None)
    ap.add_argument('--end', type=int, default=None)
    ap.add_argument('--min-units', type=int, default=800)
    ap.add_argument('--max-units', type=int, default=5000)
    args = ap.parse_args()
    items = []
    for name in sorted(os.listdir(args.directory)):
        m = FILENAME_RE.match(name)
        if not m: continue
        num = int(m.group(1))
        if args.start is not None and num < args.start: continue
        if args.end is not None and num > args.end: continue
        path = os.path.join(args.directory, name)
        if not os.path.isfile(path): continue
        text = open(path, 'r', encoding='utf-8').read()
        items.append((num, name, text))
    if not items:
        print('ERROR: no matching chapter files found', file=sys.stderr)
        sys.exit(2)
    nums = [x[0] for x in items]
    missing = [n for n in range(nums[0], nums[-1] + 1) if n not in nums]
    lengths = []
    errors = 0
    warnings = 0
    print(f'Directory: {args.directory}')
    print(f'Files checked: {len(items)}\n')
    for num, name, text in items:
        units = count_units(text)
        lengths.append(units)
        status = []
        header = first_header(text)
        if header is None:
            status.append('ERROR no header'); errors += 1
        else:
            h_num = int(header.group(1))
            h_title = header.group(2)
            if h_num != num:
                status.append(f'ERROR header number {h_num} != filename number {num}'); errors += 1
            stem_title = FILENAME_RE.match(name).group(2)
            if h_title != stem_title:
                status.append(f'WARN header title != filename title ({h_title} vs {stem_title})'); warnings += 1
        if units < args.min_units:
            status.append(f'WARN short ({units})'); warnings += 1
        elif units > args.max_units:
            status.append(f'WARN long ({units})'); warnings += 1
        else:
            status.append(f'OK len={units}')
        print(f'{name}: ' + ' | '.join(status))
    print('\nMissing chapter numbers: ' + (', '.join(map(str, missing)) if missing else 'none'))
    print(f'Median length: {int(median(lengths)) if lengths else 0}')
    print(f'Errors: {errors}')
    print(f'Warnings: {warnings}')
    if errors:
        sys.exit(1)
if __name__ == '__main__':
    main()
