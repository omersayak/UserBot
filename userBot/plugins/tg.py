from pyrogram import filters
from config import admin_id

def owner_status(app,prefix):
    @app.on_message(filters.command('tg', prefixes=prefix)& filters.me & filters.user(admin_id))
    async def site(client, message):
        await message.delete()
        text = """<b>Merhaba, Hoşgeldiniz , Sahibimin Telegram Adresi.\nTelegram  : https://t.me/Professore_1</b>"""
        await client.send_message(message.chat.id, text)