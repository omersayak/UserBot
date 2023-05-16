from pyrogram import filters
import asyncio



def fatiha_info(app,prefix):
    
    @app.on_message(filters.command('fatiha', prefixes=prefix) & filters.me)
    async def fatiha(client, message):
        if message.media:
            await message.delete()

        animation_interval = 1.0
        animation_ttl = range(0, 12)
        await message.edit("Bismillahirrahmanirrahim")
        animation_chars = ["_🕌_", "Elhamdulillâhi Rabbi’l-âlemîn.", 
                           "_🕌_", "Er-Rahmâni’r-Rahîm", 
                           "_🕌_", "Mâliki yevmi’d-dîn.", 
                           "_🕌_", "İyyâke na’budu ve iyyâke neste’în.", 
                           "_🕌_", "İhdine’s-sırata’l-mustakim.", "_🕌_", 
                           "Sırata’l-lezîne en’amte aleyhim. Ğayri’l-meğdubi aleyhim ve le’d-dallîn."]
        
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await message.edit(animation_chars[i % 12])