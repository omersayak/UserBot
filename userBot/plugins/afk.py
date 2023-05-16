from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
import logging
from config import api_id


afk_status = False
afk_reason = ""


def afk_info(app,prefix):
    # Code continuation

    

    logger = logging.getLogger(__name__)

    @app.on_message(filters.command("afk", prefixes=prefix))
    async def set_afk(client, message):
        global afk_status, afk_reason
        args = message.text.split(" ")
        if len(args) > 1:
            afk_reason = " ".join(args[1:])
        else:
            afk_reason = ""
        if afk_status:
            afk_status = False
            sent_message=await message.edit(f"AFK modundan çıktım.\nAFK Nedeni: {afk_reason}")
        else:
            afk_status = True
            await message.edit(f"AFK modunda.\nAFK Nedeni: {afk_reason}")

    @app.on_message(filters.private)
    async def check_afk(client, message):
        global afk_status, afk_reason
        if afk_status and message.from_user.id != api_id:
            try:
                if message.from_user.username:
                    sender = f"@{message.from_user.username}"
                else:
                    sender = message.from_user.first_name
                await message.reply(f"{sender}, şu anda AFK modunda olduğum için mesajınızı şimdi okuyamıyorum. En kısa sürede dönüş yapacağım."
                                    f"\nAFK Nedeni: {afk_reason}")
            except FloodWait as e:
                await message.reply(f"AFK modunda olduğum için mesajınızı şimdi okuyamıyorum. En kısa sürede dönüş yapacağım. FloodWait: {e.x} saniye."
                                    f"\nAFK Nedeni: {afk_reason}")


    @app.on_message(filters.group)
    async def check_afk_group(client, message):
        global afk_status, afk_reason
        if afk_status:
            reply_to_message = message.reply_to_message
            if reply_to_message and reply_to_message.from_user:
                user = reply_to_message.from_user
                me = await client.get_me()
                if user.id == me.id:
                    try:
                        if message.from_user.username:
                            sender = f"@{message.from_user.username}"
                        else:
                            sender = message.from_user.first_name
                    except FloodWait as e:
                        await message.reply(
                            f"AFK modunda olduğum için mesajınızı şimdi okuyamıyorum. En kısa sürede dönüş yapacağım. FloodWait: {e.x} saniye."
                            f"\nAFK Nedeni: {afk_reason}")

        else:
            if message.entities:
                mention_entities = [e for e in message.entities if e.type == "mention"]
                if mention_entities:
                    me = await client.get_me()
                    if me.id in [e.user.id for e in mention_entities]:
                        try:
                            if message.from_user.username:
                                sender = f"@{message.from_user.username}"
                            else:
                                sender = message.from_user.first_name
                        except FloodWait as e:
                            await message.reply(
                                f"AFK modunda olduğum için mesajınızı şimdi okuyamıyorum. En kısa sürede dönüş yapacağım. FloodWait: {e.x} saniye."
                                f"\nAFK Nedeni: {afk_reason}")