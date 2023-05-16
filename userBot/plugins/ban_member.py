from pyrogram import filters
from pyrogram.types import Message
from config import admin_id


def ban_member_chat(app, prefix):
    @app.on_message(filters.command('ban', prefixes=prefix) & filters.group & filters.user(admin_id))
    async def kick(client, message: Message):
        await message.delete()
        await client.ban_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)
        await client.send_message(chat_id=message.chat.id, text=f"{message.reply_to_message.from_user.mention} kicked")









