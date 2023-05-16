from pyrogram import filters
import asyncio

from config import admin_id



def send_gnydn_message(app,prefix):
    #gnydn çalıştırıyor
    @app.on_message(filters.command("gnydn",prefixes=prefix) & filters.me & filters.user(admin_id))
    async def komut_testx(client, message):
        ANIMASYON = ["Sen uyandıysan", "Gün aydı demektir🙃", "Günaydın canım❤️", "Nasılsın?", "Umarım iyisindir 😊", "Hep iyi ol inşallah", "Seviliyorsun❤️❤️❤️❤️"]
        for anim in ANIMASYON:
            await message.edit(anim)
            await asyncio.sleep(0.8)