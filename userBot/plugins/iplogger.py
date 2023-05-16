from pyrogram import filters
import asyncio
import requests
from config import api_stack


def iplogger_info(app,prefix):
    @app.on_message(filters.command("iplogger",prefixes=prefix))
    async def iplogger(client, message):
        await message.delete()
        input_str = message.text.split(" ", 1)
        if len(input_str) < 2:
            await message.reply("<b>Kullanımı</b>: .iplogger [ipaddres]")
            return
        adress = input_str[1]
        token = api_stack
        api = "http://api.ipstack.com/" + adress + "?access_key=" + token + "&format=1"
        await message.delete()
        sent_message = await message.reply("IP Logger 🕵🏻‍♀️")
        await asyncio.sleep(1)
        sent1_message = await message.reply("IP Logger...")
        await asyncio.sleep(1)
        sent2_message = await message.reply("IP Logger 🕵🏻‍♀️")

        result = requests.get(api).json()

        a = result["type"]
        b = result["country_code"]
        c = result["country_name"]
        d = result["city"]
        e = result["zip"]
        f = result["latitude"]
        g = result["longitude"]
        s = result["ip"]
        await message.reply(
            f"<b><u>BAŞARIYLA TOPLANAN BİLGİLER</b></u>\n\n<b>IP tipi :-</b><code>{a}</code>\n<b>Ülke kodu:- "
            f"</b> <code>{b}</code>\n<b>Devlet adı :-</b><code>{c}</code>\n<b>Şehir İsmi :- </b><code>{d}</code>\n<b>zip "
            f":-</b><code>{e}</code>\n<b>Enlem:- </b> <code>{f}</code>\n<b>Boylam :- </b><code>{g}</code>\n"
            f"<b>Ip: :-</b><code>{s}</code>" )
        await sent_message.delete()
        await sent1_message.delete()
        await sent2_message.delete()