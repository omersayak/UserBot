from pyrogram import filters
import asyncio

from config import admin_id



def saka_knk(app,prefix):
    #gnydn çalıştırıyor
    @app.on_message(filters.command("saka",prefixes=prefix) & filters.me & filters.user(admin_id))
    async def saka(client, message):
        ANIMASYON = [
            "`şaka knk`",
            "`şaka yaptık knk`",
            "`ğğğğğğğğğğğğğğğğğ`",
            "`ĞĞĞĞĞĞĞĞĞĞĞĞĞĞĞĞĞĞĞ `",
            "`Ne olcak ki `",
            "`hıhıhıhıhıhıhıhıhıhıh`",
            "`😂ŞAKA YAPTIK KNK😂`",
            "https://telegra.ph/file/0963be77d93d08534ff9d.mp4"
               
        ]
        for anim in ANIMASYON:
            await message.edit(anim)
            await asyncio.sleep(2)
        
        

         