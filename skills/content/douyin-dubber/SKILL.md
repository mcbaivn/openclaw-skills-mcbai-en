---
name: douyin-dubber
description: >
  Auto-dub Douyin/TikTok videos into any language using a fully local pipeline:
  download with Playwright Chromium + Douyin cookie → transcribe with Whisper → translate subtitles with the AI agent →
  generate TTS (gTTS / Edge TTS / ElevenLabs) → timing stretch with FFmpeg atempo →
  mix original audio at 10% + new TTS voice → burn ASS subtitle overlay (positioned over original sub area).
  Use when: (1) dubbing/translating a Douyin or TikTok video, (2) replacing original voice with
  translated TTS, (3) any "tải video douyin rồi dịch/lồng tiếng" request.
metadata:
  openclaw:
    credentials:
      - id: douyin_cookie
        label: Douyin Session Cookie
        kind: file
        path: skills/douyin-dubber/douyin_cookies.txt
        env: DOUYIN_COOKIE_FILE
        required: true
        sensitive: true
        description: >
          Exported Douyin session cookie (header string format). Required for downloading videos.
          Never share this file — it grants access to your Douyin account.
          Recommend using a throwaway/test account. Rotate cookies after use.
      - id: elevenlabs_api_key
        label: ElevenLabs API Key
        kind: secret
        env: ELEVENLABS_API_KEY
        required: false
        sensitive: true
        description: >
          Optional. Only needed if you choose ElevenLabs TTS (highest quality).
          Free tier: 10,000 chars/month. Create a scoped key at https://elevenlabs.io.
    requires:
      bins:
        - ffmpeg
        - python
      python_packages:
        - playwright
        - openai-whisper
      optional_packages:
        - gtts
        - edge-tts
---

# Douyin Auto Dubber

Full pipeline: Playwright download → Whisper transcribe → AI translate → TTS → FFmpeg ASS subtitle mix.

---

## ⚠️ Bảo Mật & Cookie

**Skill này chạy hoàn toàn local** — không upload video hay dữ liệu lên server nào ngoài các TTS provider bạn chọn.

### Credentials cần thiết

| Credential | Bắt buộc | Mô tả |
|-----------|----------|-------|
| `douyin_cookies.txt` | ✅ Có | Cookie Douyin để tải video |
| ElevenLabs API key | ❌ Không | Chỉ cần nếu chọn ElevenLabs TTS |

### Cookie Douyin — Lưu ý quan trọng

> ⚠️ **Cookie session = quyền truy cập tài khoản Douyin của bạn.** Không chia sẻ file này với ai.

**Khuyến nghị bảo mật:**
- 🔐 Dùng **tài khoản throwaway/test** — không dùng tài khoản chính
- 📁 Lưu cookie vào `skills/douyin-dubber/douyin_cookies.txt` (chỉ local, không được commit lên git)
- ♻️ **Rotate cookie** sau khi dùng xong (đăng xuất → đăng nhập lại → export lại)
- 🚫 Không paste cookie vào bất kỳ tool/website nào khác

**Override đường dẫn cookie bằng env var:**
```bash
export DOUYIN_COOKIE_FILE=/path/to/your/cookies.txt   # macOS/Linux
$env:DOUYIN_COOKIE_FILE = "C:\your\path\cookies.txt"  # Windows
```

### ElevenLabs API Key
- Tạo key **scoped** chỉ với permission "Text to Speech" tại https://elevenlabs.io
- Không hardcode key vào script — nhập interactive khi script hỏi
- Dùng gTTS hoặc Edge TTS nếu không muốn cung cấp API key

---

## ⚙️ CÀI ĐẶT (chỉ làm 1 lần)

### 1 — Python 3.11+

Đảm bảo Python 3.11+ đã cài và có trong PATH:
```bash
python --version   # Python 3.11.x hoặc cao hơn
```

> 💡 Tải tại https://www.python.org/downloads/ — tick **"Add Python to PATH"** khi cài

### 2 — Playwright Chromium (bắt buộc cho download)

```bash
pip install playwright
python -m playwright install chromium
```

### 3 — Whisper (bắt buộc cho transcribe)

```bash
pip install openai-whisper
```

> ⚠️ Cần FFmpeg trên PATH — tải tại https://ffmpeg.org/download.html

### 4 — TTS Providers (cài theo nhu cầu)

#### Option 1: gTTS — Mặc định ✅
```bash
pip install gtts
```
- Miễn phí hoàn toàn, không cần API key
- Không cần cấu hình thêm gì

#### Option 2: Edge TTS — Miễn phí, tự nhiên hơn
```bash
pip install edge-tts
```
- Miễn phí hoàn toàn, không cần API key
- Giọng Microsoft Neural, tự nhiên hơn gTTS nhiều
- ⚠️ Hay bị rate limit → script đã có delay 2-4s/segment + retry tự động
- Giọng Việt có sẵn:
  - `vi-VN-HoaiMyNeural` — Nữ, giọng Bắc
  - `vi-VN-NamMinhNeural` — Nam, giọng Bắc

#### Option 3: ElevenLabs — Chất lượng cao nhất, cần API key
- Không cần cài thêm package (dùng urllib built-in)
- Cần API key từ https://elevenlabs.io
- Free tier: 10,000 ký tự/tháng
- **Lấy API key:**
  1. Đăng ký tại https://elevenlabs.io
  2. Vào **Profile → API Keys → Create API Key**
  3. Trong Permissions → tick **"Text to Speech"** ✅
  4. Copy key (dạng `sk_xxxx...`)
- **Lấy Voice ID:**
  1. Vào **Voices** → chọn giọng muốn dùng
  2. Click voice → copy **Voice ID** (dạng `pNInz6obpgDQGcFmaJgB`)
  3. Hoặc dùng các giọng mặc định trong script (Rachel, Josh, Antoni, ...)

### 5 — Cookie Douyin (bắt buộc cho download)

Export cookies từ Chrome/Edge khi đang **đăng nhập Douyin**:

**Cách 1 — Extension EditThisCookie:**
1. Cài [EditThisCookie](https://chrome.google.com/webstore/detail/editthiscookie) trên Chrome
2. Vào **www.douyin.com** → đăng nhập
3. Click icon extension → **Export** → chọn format **"Header String"**
4. Copy toàn bộ → lưu vào file `skills\douyin-dubber\douyin_cookies.txt`

**Cách 2 — DevTools (không cần extension):**
1. Vào **www.douyin.com** → đăng nhập → F12
2. Tab **Application** → **Cookies** → `www.douyin.com`
3. Copy các cookie quan trọng: `sessionid`, `sid_tt`, `ttwid`, `uid_tt`, `odin_tt`
4. Ghép thành dạng: `sessionid=xxx; sid_tt=yyy; ttwid=zzz; ...`
5. Lưu vào `skills\douyin-dubber\douyin_cookies.txt`

**Format file cookie (1 dòng duy nhất):**
```
sessionid=abc123; sid_tt=def456; ttwid=1|xxx|...; uid_tt=yyy; odin_tt=zzz; ...
```

> ⚠️ Cookie hết hạn sau ~60 ngày → export lại khi bị lỗi download

---

## 🚀 Chạy Pipeline

**Windows (PowerShell):**
```powershell
$env:PYTHONIOENCODING = "utf-8"
python skills/douyin-dubber/scripts/dubber.py `
  "https://www.douyin.com/video/XXXXX" `
  --lang Vietnamese `
  --outdir "./dubbed_output"
```

**macOS / Linux:**
```bash
PYTHONIOENCODING=utf-8 python skills/douyin-dubber/scripts/dubber.py \
  "https://www.douyin.com/video/XXXXX" \
  --lang Vietnamese \
  --outdir "./dubbed_output"
```

Script sẽ hỏi chọn TTS provider:

```
═══════════════════════════════════════════════════════
  🔊 CHỌN GIỌNG ĐỌC (TTS PROVIDER)
═══════════════════════════════════════════════════════

  1️⃣   gTTS  (Google TTS)          ← Mặc định
  2️⃣   ElevenLabs                  ← Chất lượng cao nhất
  3️⃣   Edge TTS (Microsoft Neural) ← Tự nhiên, miễn phí

  👉 Nhập 1, 2 hoặc 3 (mặc định = 1):
```

**Nhập số tương ứng và Enter:**
- `1` → gTTS, tự động chạy, không hỏi thêm
- `2` → hỏi chọn giọng ElevenLabs (có sẵn hoặc nhập Voice ID tùy chỉnh) + API key
- `3` → hỏi chọn giọng (HoaiMy Nữ hoặc NamMinh Nam)

---

## 🔊 Chi Tiết TTS Providers

### Option 1: gTTS (Mặc định)

**Khi nào dùng:** Test nhanh, không cần chất lượng cao, không có API key

**Pipe input (non-interactive):**
```powershell
echo 1 | python dubber.py "URL" --lang Vietnamese --outdir "./output"
```

**Đặc điểm:**
- ✅ Miễn phí hoàn toàn
- ✅ Không rate limit
- ✅ Hỗ trợ 67 ngôn ngữ
- ⚠️ Giọng hơi robot, không có ngữ điệu

---

### Option 2: Edge TTS (Microsoft Neural)

**Khi nào dùng:** Muốn giọng tự nhiên hơn gTTS mà không cần API key

**Pipe input (non-interactive):**
```powershell
# Giọng nữ HoaiMy (option 1)
"3`n1" | python dubber.py "URL" --lang Vietnamese --outdir "./output"

# Giọng nam NamMinh (option 2)
"3`n2" | python dubber.py "URL" --lang Vietnamese --outdir "./output"

# Nhập voice tùy chỉnh (option 3)
"3`n3`nvi-VN-HoaiMyNeural" | python dubber.py "URL" --lang Vietnamese --outdir "./output"
```

**Danh sách giọng Việt:**
| Voice ID | Giới tính | Phong cách |
|----------|-----------|------------|
| `vi-VN-HoaiMyNeural` | Nữ | Giọng Bắc, tự nhiên |
| `vi-VN-NamMinhNeural` | Nam | Giọng Bắc, trầm |

**Xem tất cả giọng Edge TTS:**
```powershell
python -c "import asyncio, edge_tts; asyncio.run(edge_tts.list_voices())" | Select-String "vi-"
```

**Đặc điểm:**
- ✅ Miễn phí hoàn toàn
- ✅ Giọng tự nhiên (Microsoft Neural TTS)
- ⚠️ Rate limit → script đã có delay 2-4s/segment + retry 5 lần tự động
- ⏱️ Chậm hơn gTTS (~7-10 phút cho video 1 phút)

---

### Option 3: ElevenLabs

**Khi nào dùng:** Cần chất lượng giọng cao nhất, video quan trọng

**Pipe input (non-interactive):**
```powershell
# Dùng giọng có sẵn (Rachel = option 1)
"2`n1`nAPI_KEY_HERE" | python dubber.py "URL" --lang Vietnamese --outdir "./output"

# Dùng Voice ID tùy chỉnh (option 7)
"2`n7`nVOICE_ID_HERE`nAPI_KEY_HERE" | python dubber.py "URL" --lang Vietnamese --outdir "./output"
```

**Giọng có sẵn trong script:**
| # | Tên | Giới tính | Phong cách |
|---|-----|-----------|------------|
| 1 | Rachel | Nữ | Tự nhiên, chuyên nghiệp |
| 2 | Bella | Nữ | Nhẹ nhàng |
| 3 | Antoni | Nam | Trầm ấm |
| 4 | Josh | Nam | Rõ ràng |
| 5 | Arnold | Nam | Mạnh mẽ |
| 6 | Elli | Nữ | Trẻ trung |
| 7 | Custom | — | Nhập Voice ID tùy chỉnh |

**Lấy Voice ID từ ElevenLabs:**
```
https://elevenlabs.io/app/voice-library → chọn voice → copy Voice ID
```

**Kiểm tra API key còn credits:**
```powershell
$headers = @{ "xi-api-key" = "sk_YOUR_KEY" }
Invoke-RestMethod "https://api.elevenlabs.io/v1/user" -Headers $headers | Select-Object -ExpandProperty subscription
```

**Đặc điểm:**
- ✅ Giọng AI tự nhiên nhất hiện tại
- ✅ Hỗ trợ đa ngôn ngữ tốt
- ⚠️ Free tier: 10,000 ký tự/tháng (hết nhanh với video dài)
- ⚠️ API key phải có permission "Text to Speech"
- ❌ Lỗi 401 = key sai hoặc thiếu permission TTS
- ❌ Lỗi 402 = hết credits

---

## 📋 Pipeline Steps

### Step 1 — Download (Playwright)
- Inject cookie → mở trang → bắt video response từ zjcdn.com/amemv.com
- Download qua `ctx.request.get()` (browser context, tự đính kèm session cookie)
- Output: `{outdir}/dubber_work/original.mp4`

### Step 2 — Transcribe (Whisper)
```powershell
whisper original.mp4 --model medium --output_format srt
```
- Auto-detect ngôn ngữ
- Output: `dubber_work/original.srt`

### Step 3 — Translate (AI Agent)
- Script ghi prompt → `%TEMP%\dubber_translate_prompt.txt`
- Agent đọc → dịch → ghi JSON → `%TEMP%\dubber_translated.json`
- Format JSON: `[{"index": "1", "text": "bản dịch"}, ...]`
- Script tự poll và tiếp tục khi file xuất hiện

### Step 4 — TTS (4 sub-steps)
- **[4a]** Render từng segment theo provider đã chọn
- **[4b]** Stretch/compress khớp timestamp (FFmpeg atempo)
- **[4c]** Tạo silence base track
- **[4d]** Ghép clips vào đúng timestamp

### Step 5 — Mix + ASS Subtitle
- Audio gốc giảm 10%, overlay TTS track
- Burn ASS subtitle đè vùng sub gốc (67-79% chiều cao)
- Output: `{outdir}/dubbed_original.mp4`

---

## ⚡ Arguments

| Arg | Default | Description |
|-----|---------|-------------|
| `url` | required | Douyin/TikTok URL |
| `--lang` | Vietnamese | Target language |
| `--voice` | vi-VN-HoaiMyNeural | Edge-TTS voice (chỉ khi chọn option 3) |
| `--whisper-model` | medium | tiny/base/small/medium/large |
| `--outdir` | `.` | Output directory |
| `--original-vol` | 0.10 | Volume audio gốc (0–1) |
| `--skip-download` | — | Dùng video có sẵn, bỏ qua step 1 |
| `--skip-transcribe` | — | Dùng SRT có sẵn, bỏ qua step 2 |
| `--translated-srt` | — | Dùng SRT đã dịch, bỏ qua step 3 |

---

## ⏭️ Skip Flags (Resume khi bị ngắt)

```powershell
# Chỉ chạy từ transcribe trở đi
python dubber.py URL --skip-download .\work\original.mp4

# Chỉ chạy từ TTS trở đi
python dubber.py URL --skip-download video.mp4 --skip-transcribe original.srt

# Chỉ chạy TTS + mix (đã có bản dịch)
python dubber.py URL --skip-download video.mp4 --translated-srt translated.srt
```

---

## 🐛 Troubleshooting

| Lỗi | Nguyên nhân | Fix |
|-----|-------------|-----|
| `UnicodeEncodeError: charmap` | Terminal CP1252 không encode CJK | Set `$env:PYTHONIOENCODING="utf-8"` |
| `No video URL found` | Cookie hết hạn | Export lại cookie từ browser |
| `403 Forbidden` download | Không dùng browser context | Script đã fix, nếu vẫn lỗi → cookie hết hạn |
| Whisper không tạo SRT | UnicodeError khi print | Set `PYTHONIOENCODING=utf-8` |
| `401 Unauthorized` ElevenLabs | API key sai hoặc thiếu permission | Tạo key mới với permission TTS |
| `402 Payment Required` ElevenLabs | Hết credits | Nạp thêm hoặc dùng account khác |
| Edge TTS retry nhiều lần | Rate limit | Bình thường, script tự retry với delay 2-4s |
| ASS subtitle không hiển thị | Font path sai | Cần Arial font tại `C:/Windows/Fonts` |

---

## 📁 Output Structure

```
dubbed_output/
├── dubbed_original.mp4          ← Video output cuối cùng
└── dubber_work/
    ├── original.mp4             ← Video gốc
    ├── original.srt             ← Transcript gốc (Whisper)
    ├── translated.srt           ← SRT đã dịch
    ├── subtitle.ass             ← ASS subtitle file
    ├── tts_track.mp3            ← TTS track hoàn chỉnh
    ├── seg_001.mp3              ← TTS từng segment
    ├── seg_001_stretched.mp3    ← TTS đã stretch
    └── silence.mp3              ← Base silence track
```

---

## 📊 So Sánh TTS Providers

| | gTTS | Edge TTS | ElevenLabs |
|--|------|----------|------------|
| **Chi phí** | Miễn phí | Miễn phí | 10k chars free/tháng |
| **Chất lượng** | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Tốc độ** | Nhanh | Chậm (rate limit) | Nhanh |
| **API key** | Không | Không | Có |
| **Rate limit** | Không | Có (script tự xử lý) | Không |
| **Tiếng Việt** | Tốt | Rất tốt | Xuất sắc |
| **Khuyến nghị** | Test nhanh | Dùng thường xuyên | Video quan trọng |
