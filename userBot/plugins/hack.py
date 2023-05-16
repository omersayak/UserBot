from pyrogram import filters
import asyncio



def hack_info(app,prefix):
    @app.on_message(filters.command('hack', prefixes='.'))
    async def port_hack(client, message):
        if message.from_user.is_self:
            animation_interval = 2
            animation_ttl = range(0, 24)
            
            await message.edit("`Hazırlık sürüyor...`")

            animation_chars = [
        
            "`Programlar hazır !`",
            "`İşlem başlatılıyor \n(0%) ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`",
            "`Sistem özellikleri alınıyor. \n(5%) █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`",
            "`Sistem özellikleri alınıyor.. \n(10%) ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`",
            "`Sistem özellikleri alınıyor... \n(15%) ███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`",
            "`Betik yürütülüyor. \n(20%) ████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`",
            "`Betik yürütülüyor.. \n(25%) █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`",
            "`Betik yürütülüyor... \n(30%) ██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒`",
            "`IP adresi alınıyor. \n(35%) ███████▒▒▒▒▒▒▒▒▒▒▒▒▒`",
            "`IP adresi alınıyor.. \n(40%) ████████▒▒▒▒▒▒▒▒▒▒▒▒`",
            "`IP adresi alınıyor... \n(45%) █████████▒▒▒▒▒▒▒▒▒▒▒`",
            "`MAC adresi alınıyor. \n(50%) ██████████▒▒▒▒▒▒▒▒▒▒`",
            "`MAC adresi alınıyor.. \n(55%) ███████████▒▒▒▒▒▒▒▒▒`",
            "`MAC adresi alınıyor... \n(60%) ████████████▒▒▒▒▒▒▒▒`",
            "`Dosyalar yükleniyor. \n(65%) █████████████▒▒▒▒▒▒▒`",
            "`Dosyalar yükleniyor.. \n(70%) ██████████████▒▒▒▒▒▒`",
            "`Dosyalar yükleniyor... \n(75%) ███████████████▒▒▒▒▒`",
            "`Dosyalar yükleniyor. \n(80%) ████████████████▒▒▒▒`",
            "`Dosyalar yükleniyor.. \n(85%) █████████████████▒▒▒`",
            "`Dosyalar yükleniyor... \n(90%) ██████████████████▒▒`",
            "`Dosyalar yükleniyor. \n(95%) ███████████████████▒`",
            "`Temizleniyor.. \n(100%) ███████████████████`",
            "`İşlem Tamam... \n(100%) ███████████████████ `",
            "`Bilgisayar tarafımızca hacklendi.\nHack'i kaldırmak için 100$ ödeyin`"
        ]
            
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await message.edit(animation_chars[i % 24])