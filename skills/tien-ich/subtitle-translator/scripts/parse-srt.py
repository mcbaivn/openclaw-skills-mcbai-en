#!/usr/bin/env python3
"""
parse-srt.py - Parse SRT file thành JSON array
Usage: python parse-srt.py <file.srt>
Output: JSON array ra stdout
"""

import sys
import json
import re

def parse_srt(filepath):
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        content = f.read()

    # Normalize line endings
    content = content.replace('\r\n', '\n').replace('\r', '\n')

    # Split thành blocks bằng dòng trống
    blocks = re.split(r'\n\s*\n', content.strip())

    subtitles = []
    for block in blocks:
        lines = block.strip().split('\n')
        if len(lines) < 3:
            continue

        # Line 1: ID
        try:
            sub_id = int(lines[0].strip())
        except ValueError:
            continue

        # Line 2: Timecode
        timecode_line = lines[1].strip()
        if '-->' not in timecode_line:
            continue

        # Lines 3+: Text (có thể nhiều dòng)
        text_lines = lines[2:]
        text = '\n'.join(line.strip() for line in text_lines if line.strip())

        if not text:
            continue

        subtitles.append({
            'id': sub_id,
            'timecode': timecode_line,
            'text': text
        })

    return subtitles


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python parse-srt.py <file.srt>', file=sys.stderr)
        sys.exit(1)

    filepath = sys.argv[1]
    try:
        result = parse_srt(filepath)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except FileNotFoundError:
        print(f'Error: File not found: {filepath}', file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
        sys.exit(1)
