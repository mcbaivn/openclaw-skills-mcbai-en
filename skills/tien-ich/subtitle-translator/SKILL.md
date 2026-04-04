---
name: subtitle-translator
description: Translate SRT subtitle files into any target language using AI. Processes subtitles in batches to handle large files efficiently, preserves exact SRT format and timing, and outputs a new translated SRT file. Use this skill when the user wants to translate subtitles, translate an SRT file, dịch phụ đề, dịch file srt, translate movie subtitles, or asks to convert subtitles to another language. Triggers on phrases like "dịch phụ đề", "translate subtitles", "dịch file srt", "translate srt", "dịch sang tiếng Việt", or when user uploads/pastes an SRT file and asks for translation.
---

# Subtitle Translator Skill

Dịch file SRT sang bất kỳ ngôn ngữ nào. Xử lý theo lô (batch), giữ nguyên format và timing SRT, xuất file SRT mới.

## Workflow

### Step 1: Thu thập đầu vào

Hỏi user nếu chưa có:
1. **File SRT** — path đến file hoặc paste nội dung trực tiếp
2. **Ngôn ngữ đích** — ví dụ: "Vietnamese", "English", "Japanese" (default: Vietnamese)
3. **Batch size** — số dòng text mỗi lô API call (default: 50, max: 100)
4. **Output path** — mặc định: cùng thư mục file gốc, thêm `_vi` hoặc `_<lang>` vào tên file

### Step 2: Parse file SRT

Dùng `scripts/parse-srt.py` để đọc và parse file SRT thành danh sách objects:

```python
# Mỗi subtitle block:
{
  "id": 1,
  "timecode": "00:00:01,000 --> 00:00:03,000",
  "text": "Hello world"  # có thể nhiều dòng, join bằng \n
}
```

Chạy:
```powershell
python scripts/parse-srt.py "path/to/file.srt"
# Output: JSON array ra stdout
```

### Step 3: Dịch theo lô (batch)

Chia danh sách subtitle thành các lô `batch_size` dòng. Với mỗi lô:

**System prompt:**
```
You are a professional subtitle translator for movies and cinema.
Your ABSOLUTE task is to translate subtitle lines into {targetLanguage}.
STRICT RULES:
1. EVERY word must be translated into {targetLanguage}.
2. DO NOT include any original language text in the output.
3. Use natural, cinematic, and emotional language suitable for {targetLanguage} culture.
4. Keep the exact same ID for each line.
5. If a line is untranslatable, provide a creative interpretation in {targetLanguage} instead of leaving it as is.
6. Return a valid JSON array only: [{"id": 1, "text": "translation"}]
```

**User message (mỗi lô):**
```json
[
  {"id": 1, "text": "Hello world"},
  {"id": 2, "text": "How are you?"},
  ...
]
```

Gọi AI (dùng built-in LLM — không cần external API):
- Parse JSON response
- Nếu lỗi parse: retry lô đó 1 lần
- Map kết quả vào subtitle objects theo `id`

Báo tiến độ: `Đang dịch lô {n}/{total}... ({percent}%)`

### Step 4: Xuất file SRT mới

Dùng `scripts/build-srt.py` để ghép lại thành file SRT hoàn chỉnh:

```powershell
# Input: JSON array subtitles đã dịch + file gốc để lấy timecodes
python scripts/build-srt.py "original.srt" "translated.json" "output.srt"
```

Format SRT chuẩn:
```
1
00:00:01,000 --> 00:00:03,000
Xin chào thế giới

2
00:00:04,000 --> 00:00:06,000
Bạn có khỏe không?

```

### Step 5: Báo kết quả

- Thông báo file output đã tạo tại đâu
- Số subtitle blocks đã dịch
- Hỏi có muốn review hoặc chỉnh sửa không

## Lưu ý quan trọng

- Giữ nguyên **toàn bộ timecode** — không thay đổi `-->` timestamps
- Dòng trống giữa các block là bắt buộc trong SRT
- Subtitle text có thể nhiều dòng — join bằng `\n` khi gửi, split lại khi xuất
- HTML tags trong sub (như `<i>`, `<b>`, `<font>`) — giữ nguyên, chỉ dịch text bên trong
- Nếu file lớn (>500 dòng): báo user ước tính thời gian trước khi chạy

## Xử lý lỗi

- JSON parse error từ AI: retry lô đó, nếu vẫn lỗi thì giữ nguyên text gốc và báo user
- File SRT malformed: dùng `scripts/parse-srt.py` sẽ cố gắng recover, báo số dòng bị skip
- Encoding: luôn đọc/ghi UTF-8
