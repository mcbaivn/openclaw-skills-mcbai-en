# OpenClaw Skills - MCBAI

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

> **Bộ sưu tập Skills mở rộng cho OpenClaw** - được tuyển chọn và phát triển bởi [MCB AI](https://www.mcbai.vn)

Tất cả skills đều plug-and-play: tải về, copy vào `~/.agents/skills/`, dùng ngay.
Một skill có thể thuộc nhiều category.

---

## Danh sách tất cả Skills

| Skill | Mô tả | Category |
|-------|-------|----------|
| [download-aio](skills/tien-ich/download-aio/) | Tải video/audio từ 1000+ nền tảng | 🔧 Tiện Ích · 📱 Mạng XH · 🎬 YouTube |
| [subtitle-translator](skills/tien-ich/subtitle-translator/) | Dịch file SRT sang bất kỳ ngôn ngữ nào (AI cinematic) | 🔧 Tiện Ích · 📱 Mạng XH · 🎬 YouTube |
| [content-research](skills/content/content-research/) | Tìm bài viết & tin tức trending (Brave + Tavily) | ✍️ Content · 📱 Mạng XH |
| [content-writer](skills/content/content-writer/) | Viết post đa nền tảng (6 format, 8 tone, EN/VI) | ✍️ Content · 📱 Mạng XH |
| [youtube-subtitle-extractor](skills/youtube/youtube-subtitle-extractor/) | Tải phụ đề SRT/VTT từ video YouTube (auto + manual, đa ngôn ngữ) | 🎬 YouTube · 🔧 Tiện Ích |
| [youtube-content-analyzer](skills/youtube/youtube-content-analyzer/) | Đọc SRT/TXT → tóm tắt, key points, tags, quotes nổi bật | 🎬 YouTube · ✍️ Content |
| [youtube-channel-compare](skills/youtube/youtube-channel-compare/) | So sánh 2-5 kênh: views, engagement, trending score, tần suất đăng | 🎬 YouTube · 📊 Phân Tích |
| [youtube-scheduler](skills/youtube/youtube-scheduler/) | Phân tích 50 video gần nhất → tìm ngày/giờ vàng đăng, heatmap ASCII | 🎬 YouTube · 📊 Phân Tích |

> 🔄 Cập nhật thêm thường xuyên. **Star repo** để không bỏ lỡ nhé!

---

## Skills theo Category

### 🔧 Tiện Ích
*Công cụ hỗ trợ công việc hàng ngày*

| Skill | Mô tả |
|-------|-------|
| [download-aio](skills/tien-ich/download-aio/) | Tải video/audio từ 1000+ nền tảng (YouTube, TikTok, Facebook...) |
| [subtitle-translator](skills/tien-ich/subtitle-translator/) | Dịch file SRT phụ đề, tự detect encoding, hỗ trợ mọi ngôn ngữ |
| [youtube-subtitle-extractor](skills/youtube/youtube-subtitle-extractor/) | Tải phụ đề SRT/VTT/TXT từ YouTube (auto-generated + manual) |

---

### ✍️ Content
*Nghiên cứu, viết bài, tạo nội dung*

| Skill | Mô tả |
|-------|-------|
| [content-research](skills/content/content-research/) | Tìm bài viết & tin tức trending từ web (Brave + Tavily song song) |
| [content-writer](skills/content/content-writer/) | Viết post cho LinkedIn, Facebook, Twitter/X, TikTok, Threads |
| [youtube-content-analyzer](skills/youtube/youtube-content-analyzer/) | Phân tích SRT/TXT → tóm tắt nội dung, key points, tags gợi ý, quotes hay |

---

### 📱 Mạng Xã Hội
*Quản lý và tối ưu nội dung trên các nền tảng*

| Skill | Mô tả |
|-------|-------|
| [download-aio](skills/tien-ich/download-aio/) | Tải video/reels/shorts từ mọi nền tảng về máy |
| [subtitle-translator](skills/tien-ich/subtitle-translator/) | Dịch phụ đề video trước khi đăng lên mạng xã hội |
| [content-research](skills/content/content-research/) | Tìm nội dung trending để viết bài |
| [content-writer](skills/content/content-writer/) | Viết post Facebook, LinkedIn, TikTok caption... |

---

### 🎬 YouTube
*Công cụ dành riêng cho YouTube creators*

> [→ Xem hướng dẫn chi tiết category YouTube](skills/youtube/README.md)

| Skill | Mô tả | Dùng khi nào |
|-------|-------|--------------|
| [youtube-subtitle-extractor](skills/youtube/youtube-subtitle-extractor/) | Tải phụ đề SRT/VTT từ video YouTube | Cần file phụ đề để dịch hoặc phân tích |
| [youtube-content-analyzer](skills/youtube/youtube-content-analyzer/) | Đọc SRT/TXT → tóm tắt, key points, tags, quotes | Muốn hiểu nhanh nội dung video mà không cần xem |
| [youtube-channel-compare](skills/youtube/youtube-channel-compare/) | So sánh 2-5 kênh theo views, engagement, trending score | Nghiên cứu đối thủ, tìm kênh mạnh trong niche |
| [youtube-scheduler](skills/youtube/youtube-scheduler/) | Phân tích lịch đăng → tìm khung giờ vàng + heatmap ASCII | Muốn tối ưu thời điểm đăng video |
| [download-aio](skills/tien-ich/download-aio/) | Tải video YouTube, playlist, audio, phụ đề | Cần tải nội dung về máy |
| [subtitle-translator](skills/tien-ich/subtitle-translator/) | Dịch phụ đề tiếng Anh sang tiếng Việt (và ngược lại) | Dịch SRT sau khi tải về |

**Pipeline gợi ý:**
```
youtube-subtitle-extractor → youtube-content-analyzer → content-writer
youtube-channel-compare + youtube-scheduler → tối ưu lịch đăng
```

---

### 📊 Phân Tích
*Phân tích dữ liệu, đo lường hiệu quả*

| Skill | Mô tả |
|-------|-------|
| [youtube-channel-compare](skills/youtube/youtube-channel-compare/) | So sánh metrics 2-5 kênh: views, likes, comments, trending score, tần suất đăng |
| [youtube-scheduler](skills/youtube/youtube-scheduler/) | Heatmap ngày/giờ đăng video tối ưu dựa trên lịch sử 50 video gần nhất |

---

## Cách cài đặt

### Bước 1 - Clone repo
```powershell
git clone https://github.com/mcbaivn/openclaw-skills-mcbai.git
```

### Bước 2 - Copy skill vào OpenClaw
```powershell
# Windows - ví dụ cài youtube-content-analyzer
Copy-Item -Recurse openclaw-skills-mcbai\skills\youtube\youtube-content-analyzer $env:USERPROFILE\.agents\skills\

# macOS / Linux
cp -r openclaw-skills-mcbai/skills/youtube/youtube-content-analyzer ~/.agents/skills/
```

> Skill nằm trong folder nào cũng được - chỉ cần copy đúng folder skill vào `~/.agents/skills/`

### Bước 3 - Cài dependencies (nếu cần)
```powershell
powershell -ExecutionPolicy Bypass -File $env:USERPROFILE\.agents\skills\<tên-skill>\scripts\install.ps1
```

### Bước 4 - Dùng ngay!
Mở chat với OpenClaw agent, gọi skill theo hướng dẫn trong README của từng skill.

---

## Cấu trúc repo

```
openclaw-skills-mcbai/
├── README.md
└── skills/
    ├── tien-ich/                     🔧 Tiện Ích
    │   ├── download-aio/
    │   └── subtitle-translator/
    ├── content/                      ✍️ Content
    │   ├── content-research/
    │   └── content-writer/
    └── youtube/                      🎬 YouTube
        ├── README.md
        ├── youtube-subtitle-extractor/
        ├── youtube-content-analyzer/
        ├── youtube-channel-compare/
        └── youtube-scheduler/
```

> **Lưu ý:** Skill được đặt trong folder theo category chính. Skill có thể thuộc nhiều category (xem bảng ở trên).
> `SKILL.md` là file OpenClaw đọc để điều khiển agent - bạn chỉ cần đọc `README.md`.

---

## Về MCB AI

| | |
|--|--|
| 🌐 Website | [mcbai.vn](https://www.mcbai.vn/) |
| 📘 Fanpage | [facebook.com/mcb.ai.vn](https://www.facebook.com/mcb.ai.vn/) |
| 🎬 YouTube | [youtube.com/@mcbaivn](https://www.youtube.com/@mcbaivn) |
| 🗒️ OpenClaw Cheatsheet | [openclaw.mcbai.vn](https://openclaw.mcbai.vn/) |
| 📚 Khóa học OpenClaw 101 | [openclaw.mcbai.vn/openclaw101](https://openclaw.mcbai.vn/openclaw101) |
| 💬 Cộng đồng Facebook | [OpenClaw AI Kiếm Cơm](https://www.facebook.com/groups/openclawxvn) |
| 🎓 MCB AI Academy (Zalo) | [zalo.me/g/mmqkhi259](https://zalo.me/g/mmqkhi259) |

---

## Đóng góp

Có skill hay muốn chia sẻ? Tạo Pull Request hoặc liên hệ qua Fanpage MCB AI.

---

<p align="center">Made with ❤️ by <a href="https://www.mcbai.vn">MCB AI</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/@mcbaivn">YouTube</a> &nbsp;·&nbsp; <a href="https://openclaw.mcbai.vn/openclaw101">Học OpenClaw 101 </a> &nbsp;·&nbsp; <a href="https://zalo.me/g/mmqkhi259">MCB AI Academy</a></p>
