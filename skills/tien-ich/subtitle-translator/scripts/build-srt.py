#!/usr/bin/env python3
"""
build-srt.py - Ghép subtitles đã dịch thành file SRT
Usage: python build-srt.py <original.srt> <translated.json> <output.srt>

- Lấy timecodes từ file SRT gốc
- Lấy text đã dịch từ JSON
- Xuất file SRT hoàn chỉnh
"""

import sys
import json
import re

def parse_srt_timecodes(filepath):
    """Đọc file SRT gốc, trả về dict {id: timecode}"""
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        content = f.read()

    content = content.replace('\r\n', '\n').replace('\r', '\n')
    blocks = re.split(r'\n\s*\n', content.strip())

    timecodes = {}
    for block in blocks:
        lines = block.strip().split('\n')
        if len(lines) < 2:
            continue
        try:
            sub_id = int(lines[0].strip())
            timecode = lines[1].strip()
            if '-->' in timecode:
                timecodes[sub_id] = timecode
        except (ValueError, IndexError):
            continue

    return timecodes


def build_srt(original_path, translated_json_path, output_path):
    # Đọc timecodes từ file gốc
    timecodes = parse_srt_timecodes(original_path)

    # Đọc translations
    with open(translated_json_path, 'r', encoding='utf-8') as f:
        translations = json.load(f)

    # Build SRT content
    lines = []
    for item in sorted(translations, key=lambda x: x['id']):
        sub_id = item['id']
        text = item['text']
        timecode = timecodes.get(sub_id, '')

        if not timecode:
            continue

        lines.append(str(sub_id))
        lines.append(timecode)
        lines.append(text)
        lines.append('')  # Dòng trống giữa blocks

    srt_content = '\n'.join(lines)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(srt_content)

    return len(translations)


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Usage: python build-srt.py <original.srt> <translated.json> <output.srt>', file=sys.stderr)
        sys.exit(1)

    original_path = sys.argv[1]
    translated_json_path = sys.argv[2]
    output_path = sys.argv[3]

    try:
        count = build_srt(original_path, translated_json_path, output_path)
        print(f'OK: {count} subtitles written to {output_path}')
    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
        sys.exit(1)
