---
name: youtube-content-analyzer
description: Phân tích nội dung video YouTube từ file SRT/VTT/TXT hoặc URL trực tiếp. Tóm tắt nội dung, extract key points, phân tích chủ đề chính, tạo báo cáo. Dùng khi user yêu cầu "Tóm tắt video X", "Analyze content từ SRT", "Key points từ [URL]", "Đọc nội dung video mà không cần xem", hoặc cần hiểu nhanh nội dung hàng loạt video.
---

# 🤖 YouTube Content Analyzer

Đọc phụ đề → tóm tắt nội dung, key points, phân tích chủ đề. Không cần xem video.

## Workflow

**Cách 1 — Từ file SRT/TXT có sẵn:**
```
python scripts/analyze_content.py --file path/to/subtitle.srt
```

**Cách 2 — Từ URL (tự tải subtitle rồi phân tích):**
```
python scripts/analyze_content.py --url https://youtu.be/xxxx [--lang vi]
```

**Cách 3 — Phân tích hàng loạt:**
```
python scripts/analyze_content.py --folder Youtube_Subtitles/ChannelName/
```

## Output

```
Youtube_Analysis/
└── [Channel]/
    └── [Video_Title]_analysis_DD_MM_YYYY.txt
```

**Mỗi file analysis gồm:**
- 📌 **Tóm tắt** (3-5 câu)
- 🔑 **Key Points** (bullet list)
- 🏷️ **Chủ đề chính** (tags)
- 💬 **Quotes đáng chú ý**
- 📊 **Thống kê**: độ dài, ngôn ngữ, mật độ thông tin

## Lưu ý
- Với video dài (>30 phút), script chia nhỏ thành chunks trước khi phân tích.
- Kết hợp với `youtube-subtitle-extractor` để pipeline đầy đủ.
- Xem `references/analysis-prompt.md` để tùy chỉnh prompt phân tích.
