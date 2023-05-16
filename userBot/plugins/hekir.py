import asyncio
from pyrogram import filters




def hekir_info(app,prefix):
    @app.on_message(filters.command('hekır', prefixes=prefix) & filters.me)
    async def port_hack(client, message):
        if message.media:
            await message.delete()

        animation_interval = 3
        animation_ttl = range(0, 11)
        
        await message.edit("Kalbine giriyorum..")
        
        animation_chars = [
            "`Yine Aşık ettin Kendine Zalımın Kızı...`",
            "`Hazırım.`",
            "`Aha Şimdi Sıçtın... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 84%\n█████████████████████▒▒▒▒ `",
            "`Hacking... 100%\n█████████HACKED███████████ `",
            "`Girdim Sanki...\n\nPara ödemene gerek yok seni almışım yeter..`"
        ]

        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await message.edit(animation_chars[i % 11])