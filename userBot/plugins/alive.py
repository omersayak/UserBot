from pyrogram import filters
import asyncio

from config import admin_id



def bot_status(app,prefix):
    #gnydn çalıştırıyor
    @app.on_message(filters.command("alive",prefixes=prefix) & filters.me & filters.user(admin_id))
    async def status(client, message):
        ANIMASYON = [
            "I am ALİVE❤🧡",
            "PrOfEsOrUserBot Aktif Korkma yanındayım‼☢",
            "İyi Eğlenceler Güzel Dostum🎃",
               
        ]
        for anim in ANIMASYON:
            await message.edit(anim)
            await asyncio.sleep(2)

        await message.delete()   