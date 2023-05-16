from pyrogram import filters
import asyncio
from config import admin_id
from random import choice as c


def info_Jinx(app,prefix):
    @app.on_message(filters.command('jinx', prefixes=prefix)& filters.user(admin_id))
    async def dayı(client, message):
        JINX = [
            "``Evet deliyim, raporum bile var.`",
            "`Nerede kalmıştım? Ah evet, canını okuyordum`",
            "`Ay kusura bakma, isteyerek olduuğğ`",
            "`Dur dur, karizma bir şey söyleyeceğim`",
            "`Hadi, ateş edelim artık.`",
            "`Ben bum demeden öldürürüm`",
            "`Yarensiz bir yaşağmm olamaz`",
        ]

        await message.edit(c(JINX))