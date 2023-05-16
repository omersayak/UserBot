from pyrogram import filters
import time



def spam_message(app,prefix):
    spam_running = False
    @app.on_message(filters.command(["spam"], prefixes=prefix))
    async def spam_message(client, message):
        global spam_running
        if len(message.text.split(" ")) == 1:
            await message.reply("Kullanım: /spam [mesaj sayısı] [mesaj]")
            return
        chat_id = message.chat.id
        text = message.text.split(" ", 2)[2]
        count = int(message.text.split(" ", 2)[1])
        spam_running = True
        for i in range(count):
            if spam_running:
                await client.send_message(chat_id=chat_id, text=text)
                time.sleep(0)
            else:
                break

    @app.on_message(filters.command(["stop"], prefixes=prefix))
    async def stop_spam(client, message):
        global spam_running
        spam_running = False

    