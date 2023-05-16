from pyrogram import filters
import asyncio
from config import admin_id


def info_afro(app,prefix):
    @app.on_message(filters.command('afro', prefixes=prefix)& filters.user(admin_id))
    async def dostum(client, message):
        await message.edit("`Sana Birşey Demek İstiyorum <(￣︶￣)>`")
        await asyncio.sleep(3)
        ANIMASYON = [
                    "❤️**Ben**❤️",
                    "❤️__Sana__❤️",
                    "❤️__Yürümek__🖤",
                    "🖤__İstiyorum__❤️",
                     "❤️__Aç Kalbinin Kapısını__🖤",
                     "🖤__Lütfen__❤️",
                     "**Kapı Açıldı Saldır Komutu Bekleniyor** 🐅 🐆",
                     "__Komut Geldi Bombalar Hazırlanıyor__ 🏹 🏹",
                     "**Saldırı Başlatıldı** 🏰 💣",
                     "__Bombaya Gerek yok, Gözlerindeki Derinlik İçimi Yıkmaya Yeter〽️__ (*˘︶˘*).｡*♡ ",
                     "`Bana şair diyorlar da senin şiir olduğunu göremiyorlar.`✍🏻",
                     "`Düşürme Tamamlandı...`",
                     "`Sosyal Medya Hesabı İsteniyor...`",
                     "`Özele Bekleniyorsunuz...`"
        ]
        
        for anim in ANIMASYON:
            await message.edit(anim)
            await asyncio.sleep(0.9)
