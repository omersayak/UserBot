from pyrogram import filters
import asyncio
from config import admin_id


def info_ook(app,prefix):
    @app.on_message(filters.command('ook', prefixes=prefix)& filters.user(admin_id))
    async def dostum(client, message):
        ANIMASYON = ["`Adamlar sen mesaj at diye`",
                     "`uzaya uydu göndersin`",
                     "`Baz istasyonu kursun... `",
                     "`telefon üretsin... `",
                     "`Senin gönderdiğin mesaja bak!!!`",
                     "`🤬OK🤬",
                     "`GÖTÜNE GİRSİN OK`",
                     "https://telegra.ph/file/a0f942a6e3e9118658c07.mp4"]
        
        for anim in ANIMASYON:
            await message.edit(anim)
            await asyncio.sleep(0.8)