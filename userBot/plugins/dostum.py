from pyrogram import filters
import asyncio
from config import admin_id


def info_dst(app,prefix):
    @app.on_message(filters.command('dostum', prefixes=prefix)& filters.user(admin_id))
    async def dostum(client, message):
        ANIMASYON = ["Andımızı okur musun? (Yükleniyor.)",
                     "Andımızı okur musun? (Yükleniyor..)",
                     "Andımızı okur musun? (Yükleniyor...)",
                     "Yükleme işleminiz başarısız oldu...",
                     "oNe lAn","Şeymi Dostum;","Yine Yangınlar...",
                     "Yine Ben... ",
                     "https://telegra.ph/file/56bcd6a4f8152962a08f8.mp4"]
        
        for anim in ANIMASYON:
            await message.edit(anim)
            await asyncio.sleep(0.8)