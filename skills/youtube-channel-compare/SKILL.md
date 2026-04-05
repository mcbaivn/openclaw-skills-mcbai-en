---
name: youtube-channel-compare
description: So sánh 2-5 kênh YouTube cùng niche: trending score, tần suất đăng, engagement rate, views trung bình, likes/comments ratio. Xuất bảng so sánh và báo cáo đánh giá. Dùng khi user yêu cầu "So sánh kênh A vs B", "Compare @ChannelA @ChannelB", "Kênh nào tốt hơn", hoặc muốn benchmark kênh đối thủ.
---

# 📊 YouTube Channel Compare

So sánh hiệu suất nhiều kênh YouTube, xuất báo cáo benchmark.

## Cách dùng

```
python scripts/compare_channels.py <url1> <url2> [url3...] [--limit N]
```

**Ví dụ:**
- `So sánh @MrBeast vs @PewDiePie` → `python scripts/compare_channels.py https://youtube.com/@MrBeast https://youtube.com/@PewDiePie --limit 20`

## Output

```
Youtube_Compare/
└── compare_[Chan1]_vs_[Chan2]_DD_MM_YYYY.txt
```

**Báo cáo gồm:**

| Metric | Kênh A | Kênh B |
|--------|--------|--------|
| Views TB | ... | ... |
| Likes TB | ... | ... |
| Comments TB | ... | ... |
| Trending Score TB | ... | ... |
| Tần suất đăng | ... | ... |
| Engagement Rate | ... | ... |

**Trending Score**: `(Views × 0.6) + (Likes × 0.3) + (Comments × 0.1)` chuẩn hóa 1-100

## Lưu ý
- Mặc định lấy 20 video gần nhất mỗi kênh (`--limit`).
- Kênh nào không public stats sẽ hiển thị N/A.
