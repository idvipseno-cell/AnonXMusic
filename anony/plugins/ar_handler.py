from pyrogram import filters
from pyrogram.types import Message
from anony import app

# ═══════════════════════════════════════════════════════════
# نظام الأوامر العربية بدون رموز
# المطور: @idseno | القناة: @senovip
# ═══════════════════════════════════════════════════════════

# الكلمات المفتاحية
PLAY_KEYWORDS = ["شغل", "تشغيل", "ابدي", "بلاي", "شغلي"]
PAUSE_KEYWORDS = ["وقف", "اوكف", "بوز", "توقف"]
RESUME_KEYWORDS = ["كمل", "resume", "استمر", "واصل"]
SKIP_KEYWORDS = ["تخطي", "skip", "التالي", "next"]
STOP_KEYWORDS = ["إيقاف", "stop", "ستوب", "اطفي"]
QUEUE_KEYWORDS = ["القائمة", "queue", "الطابور"]

def get_command(text: str):
    """استخراج الأمر من النص"""
    if not text:
        return None, None
    
    text_lower = text.lower().strip()
    
    # تشغيل
    for keyword in PLAY_KEYWORDS:
        if text_lower.startswith(keyword):
            query = text[len(keyword):].strip()
            return "play", query
    
    # وقف
    for keyword in PAUSE_KEYWORDS:
        if text_lower.startswith(keyword):
            return "pause", None
    
    # كمل
    for keyword in RESUME_KEYWORDS:
        if text_lower.startswith(keyword):
            return "resume", None
    
    # تخطي
    for keyword in SKIP_KEYWORDS:
        if text_lower.startswith(keyword):
            return "skip", None
    
    # إيقاف
    for keyword in STOP_KEYWORDS:
        if text_lower.startswith(keyword):
            return "stop", None
    
    # القائمة
    for keyword in QUEUE_KEYWORDS:
        if text_lower.startswith(keyword):
            return "queue", None
    
    return None, None

@app.on_message(
    filters.text 
    & filters.group 
    & ~filters.bot 
    & ~filters.via_bot
    & ~filters.forwarded
    & ~filters.command(["start", "help", "settings", "ping", "play", "pause", "resume", "skip", "stop", "queue"])
)
async def arabic_commands_handler(client, message: Message):
    """معالج الأوامر العربية"""
    
    cmd, query = get_command(message.text)
    
    if cmd:
        # تحويل للأمر الأصلي
        if cmd == "play" and query:
            message.text = f"/play {query}"
            message.command = ["play", query]
        else:
            message.text = f"/{cmd}"
            message.command = [cmd]
```

---

## **2️⃣ حل مشكلة Health Check في Koyeb**

### **في Koyeb:**

**اذهب لـ:** Settings → Health checks

**اختر واحد من:**

### **خيار أ: تعطيل Health Check (الأسهل)**
- احذف Health Check تماماً
- أو اجعله **Disabled**

### **خيار ب: تغيير الإعدادات**
- **Type:** `HTTP`
- **Path:** `/`
- **Port:** `8080`
- **Grace Period:** `300` seconds

---

## **3️⃣ إصلاح مشكلة التحميل (YouTube Cookies)**

### **لاحظت الخطأ:**
```
Cookies are missing; downloads might fail
```

### **الحل (اختياري):**

**في Koyeb، أضف متغير:**
```
COOKIES_URL =
