#!/usr/bin/env python3
"""
YouTube Content Analyzer
Analyze content from SRT/TXT files or YouTube URL
Usage: python analyze_content.py --file <path> | --url <url> | --folder <dir>
"""

import argparse
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# Output directory
OUTPUT_DIR = "Youtube_Analysis"

def parse_srt(path):
    """Read SRT/TXT file and return plain text"""
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    if path.endswith(".srt") or path.endswith(".vtt"):
        content = re.sub(r'^\d+\s*\n', '', content, flags=re.MULTILINE)
        content = re.sub(r'\d{2}:\d{2}:\d{2}[,\.]\d{3} --> \d{2}:\d{2}:\d{2}[,\.]\d{3}\n', '', content)
        content = re.sub(r'<[^>]+>', '', content)
        content = re.sub(r'\n{3,}', '\n\n', content)
    return content.strip()

def chunk_text(text, max_chars=8000):
    """Split text into smaller chunks"""
    words = text.split()
    chunks, current = [], []
    count = 0
    for word in words:
        current.append(word)
        count += len(word) + 1
        if count >= max_chars:
            chunks.append(" ".join(current))
            current, count = [], 0
    if current:
        chunks.append(" ".join(current))
    return chunks

def analyze_text(text, title="Video"):
    """Generate analysis report from plain text"""
    chunks = chunk_text(text)
    word_count = len(text.split())
    char_count = len(text)
    
    # Basic stats
    stats = f"📊 Stats: {word_count} words | {char_count} characters | {len(chunks)} sections"
    
    # Write report (agent will fill in the AI analysis sections)
    report = f"""# 📊 Analysis: {title}
🕐 {datetime.now().strftime('%d/%m/%Y %H:%M')}
{stats}

---

## 📝 Summary
[Agent will summarize content below]

## 🔑 Key Points
[Agent will list main points]

## 🏷️ Main Topics
[Agent will assign topic tags]

## 💬 Notable Quotes
[Agent will quote important sentences]

---

## 📄 Original Content (for analysis)
{text[:12000]}{'...[truncated]' if len(text) > 12000 else ''}
"""
    return report

def process_file(path, out_dir):
    title = Path(path).stem
    text = parse_srt(path)
    report = analyze_text(text, title)
    
    os.makedirs(out_dir, exist_ok=True)
    date_str = datetime.now().strftime('%d_%m_%Y')
    out_path = os.path.join(out_dir, f"{title}_analysis_{date_str}.txt")
    
    # Avoid overwriting existing files
    if os.path.exists(out_path):
        i = 1
        while os.path.exists(out_path.replace('.txt', f'_{i}.txt')):
            i += 1
        out_path = out_path.replace('.txt', f'_{i}.txt')
    
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(report)
    
    print(f"[✓] Report: {out_path}")
    return out_path, text

def download_and_analyze(url, lang="vi,en", out_dir=OUTPUT_DIR):
    """Download subtitle from URL then analyze"""
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdir:
        cmd = [
            "yt-dlp", "--skip-download",
            "--write-subs", "--write-auto-subs",
            "--sub-langs", lang,
            "--convert-subs", "srt",
            "-o", os.path.join(tmpdir, "%(title)s.%(lang)s.%(ext)s"),
            url
        ]
        subprocess.run(cmd, check=False)
        
        srt_files = list(Path(tmpdir).glob("*.srt"))
        if not srt_files:
            print("[!] No subtitles found. Try --lang en or --auto")
            return
        
        for f in srt_files:
            process_file(str(f), out_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YouTube Content Analyzer")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", help="Path to SRT/VTT/TXT file")
    group.add_argument("--url", help="YouTube video URL")
    group.add_argument("--folder", help="Folder containing multiple SRT/TXT files")
    parser.add_argument("--lang", default="vi,en", help="Subtitle language when using --url")
    parser.add_argument("--out", default=OUTPUT_DIR, help="Output directory")
    args = parser.parse_args()

    if args.file:
        process_file(args.file, args.out)
    elif args.url:
        download_and_analyze(args.url, args.lang, args.out)
    elif args.folder:
        files = list(Path(args.folder).rglob("*.srt")) + list(Path(args.folder).rglob("*_plain.txt"))
        if not files:
            print(f"[!] No SRT/TXT files found in: {args.folder}")
            sys.exit(1)
        for f in files:
            process_file(str(f), args.out)
        print(f"\n[✓] Finished analyzing {len(files)} files!")
