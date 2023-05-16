from pyrogram import filters
from pyrogram.types import Message,ChatPermissions
from datetime import datetime, timedelta
from config import admin_id


def unmute_member_chat(app, prefix):
    @app.on_message(filters.command('unmute', prefixes=prefix) & filters.group & filters.user(admin_id))
    async def kick(client, message: Message):
        await message.delete()
        await client.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=message.reply_to_message.from_user.id,
            permissions=ChatPermissions(can_send_messages=True),
            until_date=datetime.now() + timedelta(days=1)
        )
        await client.send_message(chat_id=message.chat.id, text=f"{message.reply_to_message.from_user.mention} Mute  Kaldırıldı")