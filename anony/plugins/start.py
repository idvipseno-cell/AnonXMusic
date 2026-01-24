from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from AnonXMusic import app

START_TEXT = """
👋 **أهلاً {0}!**

🎵 أنا **بوت الموسيقى العربي**
بوت متطور لتشغيل الأغاني في المكالمات الصوتية

✨ **ببساطة اكتب:**
- `شغل عمرو دياب`
- `تنزيل فيروز`
- `وقف` - `كمل` - `تخطي`

**بدون أي رموز! فقط اكتب واستمتع** 🎶

━━━━━━━━━━━━━━━
👨‍💻 **المطور:** @{1}
📢 **القناة:** @{2}
━━━━━━━━━━━━━━━

© 2026 - جميع الحقوق محفوظة
"""

@app.on_message(filters.command("start") & filters.private)
async def start_private(client, message):
    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("➕ أضفني لمجموعتك", 
                    url=f"https://t.me/{app.username}?startgroup=true")
            ],
            [
                InlineKeyboardButton("📢 القناة", url="https://t.me/YourChannel"),
                InlineKeyboardButton("💬 المجموعة", url="https://t.me/YourGroup")
            ],
            [
                InlineKeyboardButton("📚 الأوامر", callback_data="help"),
                InlineKeyboardButton("ℹ️ عني", callback_data="about")
            ]
        ]
    )
    
    await message.reply_photo(
        photo="https://i.imgur.com/02bXwDW.jpeg",  # ضع صورة خاصة بك
        caption=START_TEXT.format(
            message.from_user.mention,
            "idseno",  # معرفك
            "senovip"    # قناتك
        ),
        reply_markup=buttons
    )

# رسالة لما يضيفوه للمجموعة
@app.on_message(filters.command("start") & filters.group)
async def start_group(client, message):
    await message.reply(
        "✅ **تم تفعيل البوت بنجاح!**\n\n"
        "🎵 ببساطة اكتب: `شغل اسم_الأغنية`\n\n"
        "━━━━━━━━━━━━━━━\n"
        f"👨‍💻 المطور: @idseno\n"
        f"📢 القناة: @senovip"
    )
