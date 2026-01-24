from pyrogram import filters
from pyrogram.types import Message
from anony import app
import re

# قاموس الكلمات المفتاحية العربية
PLAY_KEYWORDS = ["شغل", "تشغيل", "بلاي", "play"]
DOWNLOAD_KEYWORDS = ["تنزيل", "نزل", "حمل", "تحميل", "download"]
PAUSE_KEYWORDS = ["وقف", "إيقاف مؤقت", "بوز", "pause"]
RESUME_KEYWORDS = ["كمل", "استمر", "استئناف", "resume"]
SKIP_KEYWORDS = ["تخطي", "التالي", "سكب", "skip", "next"]
STOP_KEYWORDS = ["إيقاف", "توقف", "ستوب", "stop", "اطفي"]
QUEUE_KEYWORDS = ["القائمة", "الطابور", "queue", "قائمة"]
SHUFFLE_KEYWORDS = ["عشوائي", "خلط", "shuffle"]

def contains_keyword(text: str, keywords: list) -> bool:
    """التحقق من وجود كلمة مفتاحية في النص"""
    text_lower = text.lower().strip()
    for keyword in keywords:
        if text_lower.startswith(keyword):
            return True
    return False

def extract_query(text: str, keywords: list) -> str:
    """استخراج اسم الأغنية من النص"""
    text_lower = text.lower().strip()
    for keyword in keywords:
        if text_lower.startswith(keyword):
            # إزالة الكلمة المفتاحية واستخراج الاستعلام
            query = text_lower.replace(keyword, "", 1).strip()
            return query
    return ""

@app.on_message(
    filters.text 
    & filters.group 
    & ~filters.bot 
    & ~filters.via_bot
    & ~filters.forwarded
    & ~filters.command(["start", "help", "settings"])
)
async def arabic_command_handler(client, message: Message):
    """معالج ذكي للأوامر العربية بدون رموز"""
    
    text = message.text.strip()
    
    # تشغيل أغنية
    if contains_keyword(text, PLAY_KEYWORDS):
        query = extract_query(text, PLAY_KEYWORDS)
        if not query:
            await message.reply("❌ **اكتب اسم الأغنية!**\n\n📝 مثال:\n• شغل عمرو دياب\n• تشغيل فيروز")
            return
        
        # تعديل الرسالة لتصبح أمر /play لاستخدام الدالة الأصلية
        message.text = f"/play {query}"
        # استدعاء معالج التشغيل الأصلي
        from anony.plugins.play import play_command
        await play_command(client, message)
        
    # تحميل أغنية
    elif contains_keyword(text, DOWNLOAD_KEYWORDS):
        query = extract_query(text, DOWNLOAD_KEYWORDS)
        if not query:
            await message.reply("❌ **اكتب اسم الأغنية!**\n\n📝 مثال:\n• تنزيل عليك عيون\n• حمل كاظم الساهر")
            return
        
        await message.reply(f"⏬ **جاري التحميل...**\n\n🎵 {query}\n\nيرجى الانتظار...")
        # هنا يمكنك إضافة كود التحميل أو استدعاء دالة التحميل
        
    # إيقاف مؤقت
    elif contains_keyword(text, PAUSE_KEYWORDS):
        message.text = "/pause"
        from anony.plugins.pause import pause_command
        await pause_command(client, message)
        
    # استئناف
    elif contains_keyword(text, RESUME_KEYWORDS):
        message.text = "/resume"
        from anony.plugins.resume import resume_command
        await resume_command(client, message)
        
    # تخطي
    elif contains_keyword(text, SKIP_KEYWORDS):
        message.text = "/skip"
        from anony.plugins.skip import skip_command
        await skip_command(client, message)
        
    # إيقاف نهائي
    elif contains_keyword(text, STOP_KEYWORDS):
        message.text = "/stop"
        from anony.plugins.stop import stop_command
        await stop_command(client, message)
        
    # عرض القائمة
    elif contains_keyword(text, QUEUE_KEYWORDS):
        message.text = "/queue"
        from anony.plugins.queue import queue_command
        await queue_command(client, message)
        
    # خلط عشوائي
    elif contains_keyword(text, SHUFFLE_KEYWORDS):
        message.text = "/shuffle"
        from anony.plugins.misc import shuffle_command
        await shuffle_command(client, message)

@app.on_message(
    filters.text 
    & filters.private 
    & ~filters.bot
    & ~filters.command(["start", "help"])
)
async def arabic_private_handler(client, message: Message):
    """معالج الرسائل الخاصة"""
    
    text = message.text.strip()
    
    # البحث في الخاص
    if contains_keyword(text, PLAY_KEYWORDS) or contains_keyword(text, DOWNLOAD_KEYWORDS):
        query = extract_query(text, PLAY_KEYWORDS) or extract_query(text, DOWNLOAD_KEYWORDS)
        if query:
            await message.reply(
                "🔍 **جاري البحث عن:**\n"
                f"`{query}`\n\n"
                "ℹ️ **ملاحظة:**\n"
                "للتشغيل في المكالمات، أضفني لمجموعتك!"
            )
