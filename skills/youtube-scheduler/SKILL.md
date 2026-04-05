---
name: youtube-scheduler
description: Phân tích lịch đăng video của kênh YouTube để tìm "khung giờ vàng" — thời điểm đăng có nhiều view và engagement nhất. Dùng khi user yêu cầu "Tìm giờ vàng đăng video @Channel", "Best time to post for @Channel", "Kênh này hay đăng lúc mấy giờ", hoặc muốn tối ưu lịch đăng nội dung.
---

# ⏰ YouTube Scheduler Analyzer

Phân tích lịch đăng video của kênh → tìm khung giờ và ngày có hiệu suất cao nhất.

## Cách dùng

```
python scripts/analyze_schedule.py <channel_url> [--limit N] [--tz Asia/Ho_Chi_Minh]
```

**Ví dụ:**
- `Tìm giờ vàng @MrBeast` → `python scripts/analyze_schedule.py https://youtube.com/@MrBeast --limit 50`
- Đổi timezone → `--tz Asia/Ho_Chi_Minh` (mặc định UTC)

## Output

```
Youtube_Schedule/
└── [Channel]_schedule_DD_MM_YYYY.txt
```

**Báo cáo gồm:**
- 📅 Ngày trong tuần tốt nhất (sắp xếp theo views TB)
- ⏰ Khung giờ vàng (0-23h, theo views TB)
- 📈 Heatmap ngày × giờ (ASCII)
- 🏆 Top 5 video có view cao nhất kèm ngày/giờ đăng
- 💡 Khuyến nghị lịch đăng tối ưu

## Lưu ý
- Phân tích dựa trên `--limit` video gần nhất (khuyến nghị 30-100 video).
- Timezone mặc định UTC; dùng `--tz` để chuyển sang giờ địa phương.
- Kết quả chỉ mang tính thống kê từ lịch sử, không đảm bảo tuyệt đối.
