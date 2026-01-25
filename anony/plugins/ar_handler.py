from pyrogram import filters
from pyrogram.types import Message
from anony import app

# نظام الأوامر العربية بدون رموز
# المطور: @idseno

PLAY_KEYWORDS = ["شغل", "تشغيل", "play", "بلاي"]
PAUSE_KEYWORDS = ["وقف", "اوكف", "توقف"]
RESUME_KEYWORDS = ["كمل", "resume", "استمر"]
SKIP_KEYWORDS = ["تخطي", "skip", "التالي"]
STOP_KEYWORDS = ["إيقاف", "stop", "اطفي"]
QUEUE_KEYWORDS = ["القائمة", "queue"]

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
)
async def arabic_commands_handler(client, message: Message):
    """معالج الأوامر العربية"""
    
    cmd, query = get_command(message.text)
    
    if cmd:
        if cmd == "play" and query:
            message.text = f"/play {query}"
            message.command = ["play", query]
        else:
            message.text = f"/{cmd}"
            message.command = [cmd]
