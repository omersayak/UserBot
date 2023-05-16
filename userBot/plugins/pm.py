from pyrogram import filters
import asyncio


def send_pm_message(app,prefix):
    @app.on_message(filters.command("pm",prefixes=prefix))
    async def pm_message(client, message):
        if len(message.text.split(" ")) < 3:
            await message.reply("Kullanımı: .pm [kullanıcı adı/kullanıcı ID] [mesaj]")
            return

        chat_id = message.text.split(" ", 2)[1]
        text = message.text.split(" ", 2)[2]

        try:
            chat_id = int(chat_id)
        except ValueError:
            pass

        try:
            await client.send_message(chat_id, text)
            sent_message = await message.reply("Mesaj gönderildi")
            await asyncio.sleep(2)
            await sent_message.delete()
            await message.delete()
        except Exception as e:
            await message.reply("Mesaj gönderilemedi: " + str(e))
