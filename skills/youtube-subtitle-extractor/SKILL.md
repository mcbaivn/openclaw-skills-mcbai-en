---
name: youtube-subtitle-extractor
description: Tải phụ đề (SRT/VTT/TXT) từ video YouTube bằng yt-dlp. Hỗ trợ auto-generated và manual subtitles, đa ngôn ngữ. Dùng khi user yêu cầu "Tải phụ đề video X", "Get subtitles from [URL]", "Extract SRT from @Channel", hoặc cần file phụ đề để phân tích nội dung.
---

# 📝 YouTube Subtitle Extractor

Tải phụ đề từ YouTube video hoặc toàn bộ kênh, xuất ra file `.srt` sạch.

## Cách dùng

```
python scripts/extract_subtitles.py <video_or_channel_url> [--lang vi,en] [--format srt] [--auto]
```

**Ví dụ:**
- `Get subtitles from https://youtu.be/xxxx` → `python scripts/extract_subtitles.py https://youtu.be/xxxx`
- `Tải phụ đề tiếng Việt` → thêm `--lang vi`
- Chỉ lấy auto-generated → thêm `--auto`

## Output

```
Youtube_Subtitles/
└── [Video_Title]/
    ├── [title].vi.srt
    ├── [title].en.srt
    └── [title]_plain.txt   ← text thuần, không có timestamp
```

## Lưu ý
- Ưu tiên manual subtitles trước, fallback sang auto-generated nếu không có.
- File `_plain.txt` dùng cho youtube-content-analyzer.
- Nếu URL là kênh, tải subtitle tất cả video trong kênh (giới hạn bằng `--limit N`).
