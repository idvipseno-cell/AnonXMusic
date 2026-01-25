from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from anony import app
from config import *

# رسالة البداية
START_TEXT = """
- **Hi?** {0}

- **Iam** بوت ميوزك تشغيل اغاني
- **تخصصي** تشغيل الميوزك في المكالمات
- **سريع وقوي** مع مميزات رائعة

- **منصات التشغيل المدعومة :**
يوتيوب - سبوتيفاي - ريسو - ابل ميوزك - ساوندكلود

**» لـ تصفح الاوامر افرغ زر قائمة الاوامر «**
"""
# رسالة المجموعة
GROUP_START_TEXT = """
✅ **تم تفعيل البوت بنجاح!**

🎵 **كيفية الاستخدام:**
فقط اكتب: `شغل اسم_الأغنية`

📝 **أمثلة:**
- شغل عليك عيون
- تنزيل كاظم الساهر
- وقف | كمل | تخطي

━━━━━━━━━━━━━━━
👨‍💻 المطور: @idseno
📢 القناة: @senovip
━━━━━━━━━━━━━━━
"""

# رسالة المساعدة
HELP_TEXT = """
📚 **دليل الاستخدام الكامل**

🎵 **أوامر التشغيل:**
- `شغل [اسم الأغنية]` - تشغيل أغنية
- `تنزيل [اسم الأغنية]` - تحميل MP3

⏯ **عناصر التحكم:**
- `وقف` - إيقاف مؤقت
- `كمل` - استئناف التشغيل
- `تخطي` - تخطي للأغنية التالية
- `إيقاف` - إيقاف كامل

📝 **أوامر إضافية:**
- `القائمة` - عرض قائمة الانتظار
- `عشوائي` - خلط القائمة

━━━━━━━━━━━━━━━

💡 **ملاحظة:**
جميع الأوامر بدون رموز (/ أو .)
فقط اكتب الكلمة مباشرة!

━━━━━━━━━━━━━━━
👨‍💻 المطور: @idseno
📢 القناة: @senovip
"""

# رسالة عن البوت
ABOUT_TEXT = """
🤖 **معلومات البوت**

📌 **الاسم:** سورس ميوزك سينو
🆔 **المعرف:** @{0}
📊 **الإصدار:** 3.0 عربي
🐍 **اللغة:** Python 3.11
⚡ **المكتبة:** Pyrogram

━━━━━━━━━━━━━━━

👨‍💻 **المطور:**
- الاسم: SENO
- المعرف: @idseno
- القناة: @senovip

━━━━━━━━━━━━━━━

⚡ **المميزات:**
✅ تشغيل في المكالمات الصوتية
✅ تحميل MP3 عالي الجودة
✅ أوامر عربية بدون رموز
✅ واجهة عربية 100%
✅ سريع ومستقر
✅ دعم فني مستمر

━━━━━━━━━━━━━━━

© 2026 - صُنع بـ ❤️ بواسطة @idseno
⚠️ جميع الحقوق محفوظة
"""

@app.on_message(filters.command("start") & filters.private)
async def start_private(client, message: Message):
    """معالج أمر البداية في الخاص"""
    
    # أزرار الخاص
    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "➕ أضفني لمجموعتك", 
                    url=f"https://t.me/{app.username}?startgroup=true"
                )
            ],
            [
                InlineKeyboardButton("📢 القناة", url="https://t.me/senovip"),
                InlineKeyboardButton("💬 المطور", url="https://t.me/idseno")
            ],
            [
                InlineKeyboardButton("📚 الأوامر", callback_data="help"),
                InlineKeyboardButton("ℹ️ عني", callback_data="about")
            ]
        ]
    )
    
    # إرسال الرسالة مع صورة
    await message.reply_photo(
        photo="https://i.imgur.com/QqtVbOz.jpeg",  # غيّر الرابط لصورتك
        caption=START_TEXT.format(message.from_user.mention),
        reply_markup=buttons
    )

@app.on_message(filters.command("start") & filters.group)
async def start_group(client, message: Message):
    """معالج أمر البداية في المجموعات"""
    
    # أزرار المجموعة
    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("📢 القناة", url="https://t.me/senovip"),
                InlineKeyboardButton("💬 المطور", url="https://t.me/idseno")
            ],
            [
                InlineKeyboardButton("📚 دليل الاستخدام", callback_data="help")
            ]
        ]
    )
    
    await message.reply(
        GROUP_START_TEXT,
        reply_markup=buttons
    )

# معالجات الأزرار
@app.on_callback_query(filters.regex("help"))
async def help_callback(client, callback_query):
    """عرض المساعدة"""
    
    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("📢 القناة", url="https://t.me/senovip"),
                InlineKeyboardButton("💬 المطور", url="https://t.me/idseno")
            ],
            [
                InlineKeyboardButton("🔙 رجوع", callback_data="home")
            ]
        ]
    )
    
    await callback_query.edit_message_caption(
        caption=HELP_TEXT,
        reply_markup=buttons
    )

@app.on_callback_query(filters.regex("about"))
async def about_callback(client, callback_query):
    """عرض معلومات البوت"""
    
    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("👨‍💻 المطور", url="https://t.me/idseno"),
                InlineKeyboardButton("📢 القناة", url="https://t.me/senovip")
            ],
            [
                InlineKeyboardButton("🔙 رجوع", callback_data="home")
            ]
        ]
    )
    
    await callback_query.edit_message_caption(
        caption=ABOUT_TEXT.format(app.username),
        reply_markup=buttons
    )

@app.on_callback_query(filters.regex("home"))
async def home_callback(client, callback_query):
    """الرجوع للرئيسية"""
    
    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "➕ أضفني لمجموعتك", 
                    url=f"https://t.me/{app.username}?startgroup=true"
                )
            ],
            [
                InlineKeyboardButton("📢 القناة", url="https://t.me/senovip"),
                InlineKeyboardButton("💬 المطور", url="https://t.me/idseno")
            ],
            [
                InlineKeyboardButton("📚 الأوامر", callback_data="help"),
                InlineKeyboardButton("ℹ️ عني", callback_data="about")
            ]
        ]
    )
    
    await callback_query.edit_message_caption(
        caption=START_TEXT.format(callback_query.from_user.mention),
        reply_markup=buttons
    )
