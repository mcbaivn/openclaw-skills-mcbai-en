#!/usr/bin/env python3
"""
YouTube Scheduler Analyzer
Find golden posting hours from a channel's video history
Usage: python analyze_schedule.py <channel_url> [--limit N] [--tz timezone]
"""

import subprocess
import json
import sys
import os
import re
import argparse
from datetime import datetime, timezone
from collections import defaultdict

try:
    from zoneinfo import ZoneInfo
except ImportError:
    ZoneInfo = None

OUTPUT_DIR = "Youtube_Schedule"

def fetch_video_schedule(url, limit=50):
    """Fetch upload_date and stats from a channel"""
    cmd = [
        "yt-dlp",
        "--flat-playlist",
        "--playlist-end", str(limit),
        "--print", '{"title":"%(title)s","view_count":%(view_count)s,"like_count":%(like_count)s,"upload_date":"%(upload_date)s","timestamp":%(timestamp)s,"channel":"%(channel)s"}',
        url
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    videos = []
    for line in result.stdout.strip().split('\n'):
        if not line.strip():
            continue
        try:
            v = json.loads(line)
            videos.append(v)
        except:
            continue
    return videos

def safe_num(val):
    try:
        return float(val) if val not in (None, "None", "NA") else 0
    except:
        return 0

def to_local(ts, tz_name):
    """Convert timestamp to local time"""
    try:
        ts = int(ts)
        dt = datetime.fromtimestamp(ts, tz=timezone.utc)
        if tz_name and ZoneInfo:
            dt = dt.astimezone(ZoneInfo(tz_name))
        return dt
    except:
        return None

DAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def analyze(videos, tz_name):
    by_hour = defaultdict(list)   # hour -> [views]
    by_day = defaultdict(list)    # weekday -> [views]
    heatmap = defaultdict(list)   # (day, hour) -> [views]
    top_videos = []

    for v in videos:
        ts = v.get("timestamp")
        views = safe_num(v.get("view_count", 0))
        if not ts or ts in (None, "None"):
            continue
        dt = to_local(ts, tz_name)
        if not dt:
            continue
        h = dt.hour
        d = dt.weekday()
        by_hour[h].append(views)
        by_day[d].append(views)
        heatmap[(d, h)].append(views)
        top_videos.append((views, dt.strftime('%d/%m/%Y %H:%M'), v.get("title","?")))

    return by_hour, by_day, heatmap, sorted(top_videos, reverse=True)[:5]

def avg(lst):
    return sum(lst) / len(lst) if lst else 0

def build_report(channel, videos, tz_name):
    by_hour, by_day, heatmap, top5 = analyze(videos, tz_name)

    lines = [f"# ⏰ YouTube Schedule Report: {channel}"]
    lines.append(f"📅 {datetime.now().strftime('%d/%m/%Y %H:%M')} | Timezone: {tz_name or 'UTC'}")
    lines.append(f"📊 Analyzed from {len(videos)} videos\n")

    # Best days
    lines.append("## 📅 Best Posting Days (by avg views)")
    sorted_days = sorted(by_day.items(), key=lambda x: avg(x[1]), reverse=True)
    for d, views_list in sorted_days:
        bar = "█" * min(int(avg(views_list) / max(avg(v) for _, v in sorted_days) * 20), 20)
        lines.append(f"  {DAY_NAMES[d]:<12} {bar:<20} {avg(views_list):,.0f} avg views ({len(views_list)} videos)")

    # Golden hours
    lines.append("\n## ⏰ Golden Hours (by avg views)")
    sorted_hours = sorted(by_hour.items(), key=lambda x: avg(x[1]), reverse=True)[:8]
    for h, views_list in sorted_hours:
        bar = "█" * min(int(avg(views_list) / avg(sorted_hours[0][1]) * 15), 15)
        lines.append(f"  {h:02d}:00-{h+1:02d}:00  {bar:<15} {avg(views_list):,.0f} avg views")

    # Heatmap ASCII (simplified)
    lines.append("\n## 🗓️ Heatmap (day × time period)")
    lines.append("              Morning(6-12)  Afternoon(12-18)  Evening(18-24)  Night(0-6)")
    for d in range(7):
        morning = avg(sum([heatmap[(d,h)] for h in range(6,12)], []))
        afternoon = avg(sum([heatmap[(d,h)] for h in range(12,18)], []))
        evening = avg(sum([heatmap[(d,h)] for h in range(18,24)], []))
        night = avg(sum([heatmap[(d,h)] for h in range(0,6)], []))
        def star(v, max_v):
            return "⭐" * min(int(v / max_v * 3 + 1), 3) if max_v > 0 else "  "
        mx = max(morning, afternoon, evening, night, 1)
        lines.append(f"  {DAY_NAMES[d]:<12} {star(morning,mx):<15} {star(afternoon,mx):<18} {star(evening,mx):<16} {star(night,mx)}")

    # Top 5 videos
    lines.append("\n## 🏆 Top 5 Highest-View Videos")
    for views, date_str, title in top5:
        lines.append(f"  - [{date_str}] {title[:60]} — {views:,.0f} views")

    # Recommendation
    if sorted_days and sorted_hours:
        best_day = DAY_NAMES[sorted_days[0][0]]
        best_hour = sorted_hours[0][0]
        lines.append(f"\n## 💡 Recommendation")
        lines.append(f"  Post on **{best_day}**, time slot **{best_hour:02d}:00 - {best_hour+1:02d}:00** for best performance.")

    return "\n".join(lines)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YouTube Scheduler Analyzer")
    parser.add_argument("url", help="YouTube channel URL")
    parser.add_argument("--limit", type=int, default=50, help="Number of videos to analyze (default: 50)")
    parser.add_argument("--tz", default="Asia/Ho_Chi_Minh", help="Timezone (default: Asia/Ho_Chi_Minh)")
    args = parser.parse_args()

    print(f"[*] Fetching data from: {args.url}")
    videos = fetch_video_schedule(args.url, args.limit)
    if not videos:
        print("[!] Could not fetch data")
        sys.exit(1)

    channel = videos[0].get("channel", "Unknown")
    print(f"[+] Channel: {channel} | {len(videos)} videos")

    report = build_report(channel, videos, args.tz)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    date_str = datetime.now().strftime('%d_%m_%Y')
    safe_channel = re.sub(r'[^a-zA-Z0-9_]', '_', channel)[:30]
    out_path = os.path.join(OUTPUT_DIR, f"{safe_channel}_schedule_{date_str}.txt")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"\n{report}")
    print(f"\n[✓] Report saved to: {out_path}")
