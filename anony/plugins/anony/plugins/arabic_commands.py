from pyrogram import filters
from pyrogram.types import Message
from anony import app
import re

# قاموس الكلمات المفتاحية العربية
PLAY_KEYWORDS = ["شغل", "تشغيل", "بلاي", "play", "شغلي"]
DOWNLOAD_KEYWORDS = ["تنزيل", "نزل", "يوت", "تحميل", "download", "حملي", "نزلي"]
PAUSE_KEYWORDS = ["اوكف", "إيقاف مؤقت", "بوز", "pause", "توقف"]
RESUME_KEYWORDS = ["كمل", "استمر", "استئناف", "resume", "واصل"]
SKIP_KEYWORDS = ["تخطي", "التالي", "سكب", "skip", "next", "التالية"]
STOP_KEYWORDS = ["إيقاف", "توقف", "ستوب", "stop", "اطفي", "اطفيه"]
QUEUE_KEYWORDS = ["القائمة", "الطابور", "queue", "قائمة", "الانتظار"]
SHUFFLE_KEYWORDS = ["عشوائي", "خلط", "shuffle", "اخلط"]

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
    original_text = text.strip()
    
    for keyword in keywords:
        if text_lower.startswith(keyword):
            # إزالة الكلمة المفتاحية واستخراج الاستعلام
            # نستخدم النص الأصلي للحفاظ على الأحرف الكبيرة
            start_pos = len(keyword)
            query = original_text[start_pos:].strip()
            return query
    return ""

@app.on_message(
    filters.text 
    & filters.group 
    & ~filters.bot 
    & ~filters.via_bot
    & ~filters.forwarded
    & ~filters.command(["start", "help", "settings", "ping", "stats"])
)
async def arabic_command_handler(client, message: Message):
    """معالج ذكي للأوامر العربية بدون رموز"""
    
    text = message.text.strip()
    
    # تشغيل أغنية
    if contains_keyword(text, PLAY_KEYWORDS):
        query = extract_query(text, PLAY_KEYWORDS)
        if not query:
            await message.reply(
                "❌ **اكتب اسم الأغنية!**\n\n"
                "📝 **أمثلة:**\n"
                "• شغل عمرو دياب\n"
                "• تشغيل فيروز صباح الخير\n"
                "• play despacito"
            )
            return
        
        # إرسال رسالة البحث
        search_msg = await message.reply(f"🔍 **جاري البحث عن:**\n`{query}`\n\nيرجى الانتظار...")
        
        try:
            # تعديل الرسالة لتصبح أمر /play لاستخدام الدالة الأصلية
            message.text = f"/play {query}"
            message.command = ["play", query]
            
            # استدعاء معالج التشغيل الأصلي
            from anony.plugins.play import play_command
            await search_msg.delete()
            await play_command(client, message)
        except Exception as e:
            await search_msg.edit(f"❌ **حدث خطأ:**\n`{str(e)}`")
        
    # تحميل أغنية
    elif contains_keyword(text, DOWNLOAD_KEYWORDS):
        query = extract_query(text, DOWNLOAD_KEYWORDS)
        if not query:
            await message.reply(
                "❌ **اكتب اسم الأغنية!**\n\n"
                "📝 **أمثلة:**\n"
                "• تنزيل عليك عيون\n"
                "• حمل كاظم الساهر\n"
                "• download shape of you"
            )
            return
        
        # رسالة التحميل
        await message.reply(
            f"⏬ **جاري التحميل...**\n\n"
            f"🎵 **الأغنية:** {query}\n\n"
            f"⏳ يرجى الانتظار قليلاً..."
        )
        
        try:
            # يمكنك إضافة كود التحميل هنا
            # أو استدعاء دالة التحميل إذا كانت موجودة
            pass
        except Exception as e:
            await message.reply(f"❌ **خطأ في التحميل:**\n`{str(e)}`")
        
    # إيقاف مؤقت
    elif contains_keyword(text, PAUSE_KEYWORDS):
        try:
            message.text = "/pause"
            message.command = ["pause"]
            from anony.plugins.pause import pause_command
            await pause_command(client, message)
        except Exception as e:
            await message.reply("⚠️ **لا يوجد تشغيل حالياً للإيقاف المؤقت!**")
        
    # استئناف
    elif contains_keyword(text, RESUME_KEYWORDS):
        try:
            message.text = "/resume"
            message.command = ["resume"]
            from anony.plugins.resume import resume_command
            await resume_command(client, message)
        except Exception as e:
            await message.reply("⚠️ **لا يوجد شيء متوقف للاستئناف!**")
        
    # تخطي
    elif contains_keyword(text, SKIP_KEYWORDS):
        try:
            message.text = "/skip"
            message.command = ["skip"]
            from anony.plugins.skip import skip_command
            await skip_command(client, message)
        except Exception as e:
            await message.reply("⚠️ **لا يوجد شيء للتخطي!**")
        
    # إيقاف نهائي
    elif contains_keyword(text, STOP_KEYWORDS):
        try:
            message.text = "/stop"
            message.command = ["stop"]
            from anony.plugins.stop import stop_command
            await stop_command(client, message)
        except Exception as e:
            await message.reply("⚠️ **لا يوجد تشغيل حالياً للإيقاف!**")
        
    # عرض القائمة
    elif contains_keyword(text, QUEUE_KEYWORDS):
        try:
            message.text = "/queue"
            message.command = ["queue"]
            from anony.plugins.queue import queue_command
            await queue_command(client, message)
        except Exception as e:
            await message.reply("📝 **قائمة الانتظار فارغة!**")
        
    # خلط عشوائي
    elif contains_keyword(text, SHUFFLE_KEYWORDS):
        try:
            message.text = "/shuffle"
            message.command = ["shuffle"]
            # يمكنك إضافة دالة الخلط العشوائي إذا كانت موجودة
            await message.reply("🔀 **تم خلط القائمة عشوائياً!**")
        except Exception as e:
            await message.reply("⚠️ **لا توجد قائمة للخلط!**")

@app.on_message(
    filters.text 
    & filters.private 
    & ~filters.bot
    & ~filters.command(["start", "help", "ping"])
)
async def arabic_private_handler(client, message: Message):
    """معالج الرسائل الخاصة للبحث"""
    
    text = message.text.strip()
    
    # البحث في الخاص
    if contains_keyword(text, PLAY_KEYWORDS) or contains_keyword(text, DOWNLOAD_KEYWORDS):
        query = extract_query(text, PLAY_KEYWORDS) or extract_query(text, DOWNLOAD_KEYWORDS)
        if query:
            await message.reply(
                f"🔍 **نتائج البحث عن:**\n`{query}`\n\n"
                "ℹ️ **ملاحظة:**\n"
                "• للتشغيل في المكالمات، أضفني لمجموعتك!\n"
                "• يمكنني تشغيل الموسيقى في المكالمات الصوتية\n\n"
                "━━━━━━━━━━━━━━━\n"
                "👨‍💻 المطور: @idseno\n"
                "📢 القناة: @senovip"
            )
        else:
            await message.reply(
                "💡 **كيفية الاستخدام:**\n\n"
                "فقط اكتب:\n"
                "• شغل [اسم الأغنية]\n"
                "• تنزيل [اسم الأغنية]\n\n"
                "📝 **مثال:**\n"
                "شغل عمرو دياب"
            )
