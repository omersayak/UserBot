from pyrogram import filters, utils
from pyrogram.types import Message,ChatPermissions
from datetime import datetime, timedelta
from config import admin_id
import re



import re

def mute_member_chat(app, prefix):
    @app.on_message(filters.command('mute', prefixes=prefix) & filters.group & filters.user(admin_id))
    async def mute(client, message: Message):
        await message.delete()

        # Parse the time duration from the command
        try:
            duration_str = re.search(r'(\d+)([dhma])', message.command[1]).groups()
            duration_num = int(duration_str[0])
            duration_unit = duration_str[1]

            if duration_unit == 'm':
                duration = timedelta(minutes=duration_num)
            elif duration_unit == 'h':
                duration = timedelta(hours=duration_num)
            elif duration_unit == 'd':
                duration = timedelta(days=duration_num)
            elif duration_unit == 'a':
                duration = timedelta(days=365 * duration_num)
        except (IndexError, AttributeError):
            await client.send_message(chat_id=message.chat.id, text="Lütfen bir zaman periyodu belirtin. Örneğin: `.mute 4h`")
            return

        # Apply the mute
        await client.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=message.reply_to_message.from_user.id,
            permissions=ChatPermissions(),
            until_date=datetime.now() + duration
        )

        # Send a message to confirm the mute
        duration_str = re.search(r'(\d+[dhma])+', message.command[1]).group()
        await client.send_message(chat_id=message.chat.id, text=f"{message.reply_to_message.from_user.mention} {duration_str} boyunca mutelendi.")

