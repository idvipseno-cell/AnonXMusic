# Copyright (c) 2025 AnonymousX1025
# Licensed under the MIT License.
# This file is part of AnonXMusic


import asyncio
import time

from pyrogram import enums, errors, filters, types

from anony import anon, app, config, db, lang, queue, tasks, userbot, yt
from anony.helpers import buttons


@app.on_message(filters.video_chat_started, group=19)
@app.on_message(filters.video_chat_ended, group=20)
async def _watcher_vc(_, m: types.Message):
    await anon.stop(m.chat.id)


async def auto_leave():
    while True:
        await asyncio.sleep(1800)
        for ub in userbot.clients:
            left = 0
            try:
                for dialog in await ub.get_dialogs():
                    chat_id = dialog.chat.id
                    if left >= 20:
                        break
                    if chat_id in [app.logger, -1001686672798, -1001549206010]:
                        continue
                    if dialog.chat.type in [
                        enums.ChatType.GROUP,
                        enums.ChatType.SUPERGROUP,
                    ]:
                        if chat_id in db.active_calls:
                            continue
                        await ub.leave_chat(chat_id)
                        left += 1
                    await asyncio.sleep(5)
            except:
                continue


async def track_time():
    while True:
        await asyncio.sleep(1)
        for chat_id in list(db.active_calls):
            if not await db.playing(chat_id):
                continue
            media = queue.get_current(chat_id)
            if not media:
                continue
            media.time += 1


async def update_timer(length=10):
    while True:
        await asyncio.sleep(7)
        for chat_id in list(db.active_calls):
            if not await db.playing(chat_id):
                continue
            try:
                media = queue.get_current(chat_id)
                duration, message_id = media.duration_sec, media.message_id
                if not duration or not message_id or not media.time:
                    continue
                played = media.time
                remaining = duration - played
                pos = min(int((played / duration) * length), length - 1)
                timer = "—" * pos + "◉" + "—" * (length - pos - 1)

                if remaining <= 30:
                    next = queue.get_next(chat_id, check=True)
                    if next and not next.file_path:
                        next.file_path = await yt.download(next.id, video=next.video)

                if remaining < 10:
                    remove = True
                else:
                    remove = False
                    timer = f"{time.strftime('%M:%S', time.gmtime(played))} | {timer} | -{time.strftime('%M:%S', time.gmtime(remaining))}"

                await app.edit_message_reply_markup(
                    chat_id=chat_id,
                    message_id=message_id,
                    reply_markup=buttons.controls(
                        chat_id=chat_id, timer=timer, remove=remove
                    ),
                )
            except Exception:
                pass


async def vc_watcher(sleep=15):
    while True:
        await asyncio.sleep(sleep)
        for chat_id in list(db.active_calls):
            client = await db.get_assistant(chat_id)
            media = queue.get_current(chat_id)
            participants = await client.get_participants(chat_id)
            if len(participants) < 2 and media.time > 30:
                _lang = await lang.get_lang(chat_id)
                try:
                    sent = await app.edit_message_reply_markup(
                        chat_id=chat_id,
                        message_id=media.message_id,
                        reply_markup=buttons.controls(
                            chat_id=chat_id, status=_lang["stopped"], remove=True
                        ),
                    )
                    await anon.stop(chat_id)
                    await sent.reply_text(_lang["auto_left"])
                except errors.MessageIdInvalid:
                    pass


if config.AUTO_END:
    tasks.append(asyncio.create_task(vc_watcher()))
if config.AUTO_LEAVE:
    tasks.append(asyncio.create_task(auto_leave()))
tasks.append(asyncio.create_task(track_time()))
tasks.append(asyncio.create_task(update_timer()))
from pyrogram import filters
from pyrogram.types import Message
from anony import app

@app.on_message(filters.command("commands") & filters.group)
async def commands_list(client, message: Message):
    """عرض قائمة الأوامر المختصرة"""
    
    commands_text = """
📚 **الأوامر المختصرة (بدون رموز)**

🎵 **التشغيل:**
- شغل [اسم الأغنية]
- تشغيل [اسم الأغنية]
- play [song name]

⏬ **التحميل:**
- تنزيل [اسم الأغنية]
- حمل [اسم الأغنية]
- download [song name]

⏯ **التحكم:**
- وقف - إيقاف مؤقت
- كمل - استئناف
- تخطي - التالي
- إيقاف - إيقاف كامل

📝 **القوائم:**
- القائمة - عرض قائمة الانتظار
- عشوائي - خلط القائمة

━━━━━━━━━━━━━━━
💡 **جميع الأوامر بدون / أو .**
━━━━━━━━━━━━━━━
👨‍💻 المطور: @idseno
📢 القناة: @senovip
    """
    
    await message.reply(commands_text)
