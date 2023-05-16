from pyrogram import filters
from config import admin_id

commands_list = [
    "**Botun Prefixleri {'.', '!', ';'}**",
    "`help,commands`",
    "`alive`",
    "`afro`",
    "`about`",
    "`ban`",
    "`unban`",
    "`mute`",
    "`unmute`",
    "`dostum`",
    "`espiri`",
    "`fatiha`",
    "`gnydn`",
    "`hack`",
    "`hekır`",
    "`iplogger`",
    "`jinx`",
    "`ook`",
    "`pm`",
    "`dayı`",
    "`profil`",
    "`spam`",
    "`yuru`",
    "`saka`",
    "`oke`",
    "`tg`",
]
def commands_knowledge(app, prefix):
    @app.on_message(filters.command('commands', prefixes=prefix)& filters.me & filters.user(admin_id))
    async def aboute(client, message):
        await message.delete()
        text = "\n".join(commands_list)
        await client.send_message(message.chat.id, text)


    @app.on_message(filters.command('help', prefixes=prefix)& filters.me & filters.user(admin_id))
    async def aboutes(client, message):
        await message.delete()
        text = "\n".join(commands_list)
        await client.send_message(message.chat.id, text)

