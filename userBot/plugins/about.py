from pyrogram import filters
from config import admin_id


def about_info(app,prefix):
    @app.on_message(filters.command('about', prefixes=prefix)& filters.user(admin_id))
    async def aboute(client, message):
        #await message.delete()
        text = """
        Ben Professore_1 tarafından UserBot olarak geliştirildim.\nSahibimin Telegram Adresi  : https://t.me/Professore_1</b>
        """
        await client.send_message(message.chat.id, text)
