# 🎬 YouTube

Các skills phân tích, khai thác và tối ưu hóa nội dung YouTube — từ tải phụ đề đến phân tích lịch đăng và so sánh kênh.

| Skill | Mô tả |
|-------|-------|
| [youtube-subtitle-extractor](youtube-subtitle-extractor/) | Tải phụ đề SRT/VTT từ video YouTube (auto-generated + manual, đa ngôn ngữ) |
| [youtube-content-analyzer](youtube-content-analyzer/) | Đọc SRT/TXT → tóm tắt, key points, tags, quotes nổi bật |
| [youtube-channel-compare](youtube-channel-compare/) | So sánh 2-5 kênh: views, engagement, trending score, tần suất đăng |
| [youtube-scheduler](youtube-scheduler/) | Phân tích 50 video gần nhất → tìm ngày/giờ vàng đăng, heatmap ASCII |

## Pipeline gợi ý

```
youtube-subtitle-extractor  →  youtube-content-analyzer  →  content-writer
         ↓
youtube-channel-compare  +  youtube-scheduler  →  tối ưu lịch đăng
```

## Ví dụ workflow

**Nghiên cứu nội dung đối thủ:**
1. Dùng `youtube-channel-compare` → tìm kênh mạnh nhất trong niche
2. Dùng `youtube-subtitle-extractor` → tải SRT các video top của kênh đó
3. Dùng `youtube-content-analyzer` → phân tích key points, quotes, cấu trúc
4. Dùng `content-writer` → tạo bài viết từ insight thu thập được

**Tối ưu lịch đăng:**
1. Dùng `youtube-scheduler` → phân tích kênh của bạn (hoặc đối thủ)
2. Xem heatmap → chọn khung giờ vàng
3. Lên lịch đăng theo khuyến nghị

---
[← Về trang chủ](../../README.md)
