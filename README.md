# OpenClaw Skills — MCBAI

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

> **Bộ sưu tập Skills mở rộng cho OpenClaw** — được tuyển chọn và phát triển bởi [MCB AI](https://www.mcbai.vn)

Tất cả skills đều plug-and-play: tải về, copy vào `~/.agents/skills/`, dùng ngay.
Một skill có thể thuộc nhiều category.

---

## Danh sách tất cả Skills

| Skill | Mô tả | Category |
|-------|-------|----------|
| [download-aio](skills/tien-ich/download-aio/) | Tải video/audio từ 1000+ nền tảng | 🔧 Tiện ích · 📱 Mạng XH · ▶️ YouTube |
| [subtitle-translator](skills/tien-ich/subtitle-translator/) | Dịch file SRT sang bất kỳ ngôn ngữ nào (AI cinematic) | 🔧 Tiện ích · 📱 Mạng XH · ▶️ YouTube |
| [content-research](skills/content/content-research/) | Tìm bài viết & tin tức trending (Brave + Tavily) | 📝 Content · 📱 Mạng XH |
| [content-writer](skills/content/content-writer/) | Viết post đa nền tảng (6 format, 8 tone, EN/VI) | 📝 Content · 📱 Mạng XH |

> 🔄 Cập nhật thêm thường xuyên. **Star repo** để không bỏ lỡ 🌟

---

## Skills theo Category

### 🔧 Tiện Ích
*Công cụ hỗ trợ công việc hàng ngày*

| Skill | Mô tả |
|-------|-------|
| [download-aio](skills/tien-ich/download-aio/) | Tải video/audio từ 1000+ nền tảng (YouTube, TikTok, Facebook...) |
| [subtitle-translator](skills/tien-ich/subtitle-translator/) | Dịch file SRT phụ đề, tự detect encoding, hỗ trợ mọi ngôn ngữ |

---

### 📝 Content
*Nghiên cứu, viết bài, tạo nội dung*

| Skill | Mô tả |
|-------|-------|
| [content-research](skills/content/content-research/) | Tìm bài viết & tin tức trending từ web (Brave + Tavily song song) |
| [content-writer](skills/content/content-writer/) | Viết post cho LinkedIn, Facebook, Twitter/X, TikTok, Threads |

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

### ▶️ YouTube
*Công cụ dành riêng cho YouTube creators*

| Skill | Mô tả |
|-------|-------|
| [download-aio](skills/tien-ich/download-aio/) | Tải video YouTube, playlist, channel, audio, subtitle |
| [subtitle-translator](skills/tien-ich/subtitle-translator/) | Dịch phụ đề tiếng Anh sang tiếng Việt (và ngược lại) |

---

### 📊 Phân Tích *(sắp ra mắt)*
### 🤖 Tự Động Hóa *(sắp ra mắt)*

---

## Cách cài đặt

### Bước 1 — Clone repo
```powershell
git clone https://github.com/mcbaivn/openclaw-skills-mcbai.git
```

### Bước 2 — Copy skill vào OpenClaw
```powershell
# Windows — ví dụ cài subtitle-translator
Copy-Item -Recurse openclaw-skills-mcbai\skills\tien-ich\subtitle-translator $env:USERPROFILE\.agents\skills\

# macOS / Linux
cp -r openclaw-skills-mcbai/skills/tien-ich/subtitle-translator ~/.agents/skills/
```

> Skill nằm trong folder nào cũng được — chỉ cần copy đúng folder skill vào `~/.agents/skills/`

### Bước 3 — Cài dependencies (nếu cần)
```powershell
powershell -ExecutionPolicy Bypass -File $env:USERPROFILE\.agents\skills\<tên-skill>\scripts\install.ps1
```

### Bước 4 — Dùng ngay!
Mở chat với OpenClaw agent, gọi skill theo hướng dẫn trong README của từng skill.

---

## Cấu trúc repo

```
openclaw-skills-mcbai/
├── README.md
└── skills/
    ├── tien-ich/                    ← 🔧 Tiện ích
    │   ├── download-aio/
    │   └── subtitle-translator/
    └── content/                     ← 📝 Content
        ├── content-research/
        └── content-writer/
```

> **Lưu ý:** Skill được đặt trong folder theo category chính. Skill có thể thuộc nhiều category (xem bảng ở trên).
> `SKILL.md` là file OpenClaw đọc để điều khiển agent — bạn chỉ cần đọc `README.md`.

---

## Về MCB AI

| | |
|--|--|
| 🌐 Website | [mcbai.vn](https://www.mcbai.vn/) |
| 📘 Fanpage | [facebook.com/mcb.ai.vn](https://www.facebook.com/mcb.ai.vn/) |
| 🎬 YouTube | [youtube.com/@mcbaivn](https://www.youtube.com/@mcbaivn) |
| 🛠️ OpenClaw Cheatsheet | [openclaw.mcbai.vn](https://openclaw.mcbai.vn/) |
| 🎓 Khoá học OpenClaw 101 | [openclaw.mcbai.vn/openclaw101](https://openclaw.mcbai.vn/openclaw101) |
| 👥 Cộng đồng Facebook | [OpenClaw AI Kiếm Cơm](https://www.facebook.com/groups/openclawxvn) |
| 📱 MCB AI Academy (Zalo) | [zalo.me/g/mmqkhi259](https://zalo.me/g/mmqkhi259) |

---

## Đóng góp

Có skill hay muốn chia sẻ? Tạo Pull Request hoặc liên hệ qua Fanpage MCB AI.

---

<p align="center">Made with ❤️ by <a href="https://www.mcbai.vn">MCB AI</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/@mcbaivn">YouTube</a> &nbsp;·&nbsp; <a href="https://openclaw.mcbai.vn/openclaw101">Học OpenClaw 101 →</a> &nbsp;·&nbsp; <a href="https://zalo.me/g/mmqkhi259">MCB AI Academy</a></p>
