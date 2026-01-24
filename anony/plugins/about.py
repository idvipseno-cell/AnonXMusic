from pyrogram import filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from anony import app

ABOUT_TEXT = """
🤖 **معلومات البوت**

📌 **الاسم:** سورس سينو
🆔 **المعرف:** @YourBotUsername
📊 **الإصدار:** 2.0
🐍 **اللغة:** Python 3.10

━━━━━━━━━━━━━━━

👨‍💻 **المطور**
- الاسم: سينو
- المعرف: @idseno
- القناة: @senovip

━━━━━━━━━━━━━━━

⚡ **المميزات:**
✅ تشغيل في المكالمات
✅ تحميل MP3
✅ أوامر عربية
✅ بدون رموز
✅ سريع ومستقر

━━━━━━━━━━━━━━━

© 2026 - صُنع بـ ❤️ بواسطة @idseno
⚠️ جميع الحقوق محفوظة
"""

@app.on_callback_query(filters.regex("about"))
async def about_callback(client, callback_query: CallbackQuery):
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
        caption=ABOUT_TEXT,
        reply_markup=buttons
    )
