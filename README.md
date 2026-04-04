# OpenClaw Skills — MCBAI

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

> **Bộ sưu tập Skills mở rộng cho OpenClaw** — được tuyển chọn và phát triển bởi [MCB AI](https://www.mcbai.vn)

Tất cả skills trong repo này đều plug-and-play: tải về, copy vào `~/.agents/skills/`, dùng ngay — không cần code, không cần cấu hình phức tạp.

---

## Danh sách Skills theo Category

### 🔧 Tiện Ích (`skills/tien-ich/`)
*Các công cụ hỗ trợ công việc hàng ngày*

| Skill | Mô tả | Platform |
|-------|-------|----------|
| [download-aio](skills/tien-ich/download-aio/) | Tải video/audio từ 1000+ nền tảng (YouTube, TikTok, Facebook...) | Windows |
| [subtitle-translator](skills/tien-ich/subtitle-translator/) | Dịch file SRT phụ đề sang bất kỳ ngôn ngữ nào (AI cinematic translation) | All |

---

### 📝 Content (`skills/content/`)
*Nghiên cứu, viết bài, tạo nội dung LinkedIn*

| Skill | Mô tả | Platform |
|-------|-------|----------|
| [content-research](skills/content/content-research/) | Tìm bài viết & tin tức trending từ web (Brave + Tavily song song) | All |
| [content-writer](skills/content/content-writer/) | Viết LinkedIn post từ nguồn bài (4 format, 6 tone, EN/VI) | All |

### 📊 Phân Tích (`skills/phan-tich/`) *(sắp ra mắt)*
*Phân tích dữ liệu, báo cáo, thống kê*

### 🤖 Tự Động Hóa (`skills/tu-dong-hoa/`) *(sắp ra mắt)*
*Automation, workflow, scheduling*

### 📱 Mạng Xã Hội (`skills/mang-xa-hoi/`) *(sắp ra mắt)*
*Quản lý Facebook, TikTok, Instagram, YouTube...*

---

> 🔄 Sẽ cập nhật thêm skills thường xuyên. **Star repo** để không bỏ lỡ 🌟

---

## Cách cài đặt skill

### Bước 1 — Clone repo

```powershell
git clone https://github.com/mcbaivn/openclaw-skills-mcbai.git
```

### Bước 2 — Copy skill muốn dùng vào OpenClaw

```powershell
# Windows (PowerShell)
# Cú pháp: skills\<category>\<tên-skill>
Copy-Item -Recurse openclaw-skills-mcbai\skills\tien-ich\download-aio $env:USERPROFILE\.agents\skills\

# macOS / Linux
cp -r openclaw-skills-mcbai/skills/tien-ich/download-aio ~/.agents/skills/
```

### Bước 3 — Chạy script cài đặt (nếu skill yêu cầu)

```powershell
powershell -ExecutionPolicy Bypass -File $env:USERPROFILE\.agents\skills\<tên-skill>\scripts\install.ps1
```

### Bước 4 — Dùng ngay!

Mở chat với OpenClaw agent và gọi skill theo hướng dẫn trong README của từng skill.

---

## Cấu trúc repo

```
openclaw-skills-mcbai/
├── README.md
└── skills/
    ├── tien-ich/                    ← 🔧 Tiện ích hàng ngày
    │   └── download-aio/            ← Tải video AIO
    │       ├── README.md
    │       ├── SKILL.md
    │       ├── scripts/
    │       └── references/
    ├── content/                     ← 📝 Content & viết bài
    ├── phan-tich/                   ← 📊 Phân tích dữ liệu
    ├── tu-dong-hoa/                 ← 🤖 Tự động hóa
    └── mang-xa-hoi/                 ← 📱 Mạng xã hội
```

> **Lưu ý:** `SKILL.md` là file OpenClaw đọc để điều khiển agent — bạn không cần đọc. Chỉ cần đọc `README.md` của từng skill là đủ.

---

## Yêu cầu

- [OpenClaw](https://openclaw.mcbai.vn/) đã cài đặt và cấu hình
- Mỗi skill có yêu cầu riêng — xem README của từng skill

---

## Về MCB AI

MCB AI là nền tảng AI content & marketing automation của người Việt, dành cho người Việt.

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
