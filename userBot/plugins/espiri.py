from pyrogram import filters
import asyncio
from config import admin_id
from random import choice as c


def info_Esp(app,prefix):
    @app.on_message(filters.command('espiri', prefixes=prefix)& filters.user(admin_id))
    async def espri(client, message):
        ESPİRİ = [
  "**Sana bir kıllık yapayım, kıllarını koyarsın.**",
  "**Kim vurduya gittim birazdan geleceğim.**",
  "**Adamın biri güneşte yanmış, ay da düz.**",
  "**Geçen gün geçmiş günlerimi aradım ama meşguldü.🚬**",
  "**Tebrikler kazandınız, şimdi tencere oldunuz!😵**",
  "**Ben yürüyelim diyorum Gerard Depardieu.**",
  "**Sarımsağı havanda dövmüşsün, Ha Muş'ta.**",
  "**Bütün umutlarım suya düştü ama boğulmadılar. Çünkü onlara yüzme öğretmiştim**",
  "**Basamakta durmayın otomatik kapı çarpar, böler, karekökünü alır.**",
  "**Alinin selamı var\nHangi Ali?\nŞehirlerarası otobüs termin-ali**",
  "**Çok Makbule geçti, şimdi de Fatma geçiyor**",
  "**-Abi sana Sıla'nın selamı var.\nHangi Sıla?\n-Gayri Safi Milli HaSıla**",
  "**En güzel çay hangi dağda içilir?\nÇay bar-dağı’nda**",
  "**Geçen gün geçmiş günlerimi aradım ama meşguldü**",
  "**Masada hangi örtü kullanılmaz?\n- Bitki Örtüsü.**",
  "**Yağmur yağmış, kar peynir!**",
  "**Ben ekmek yedim Will Smith.**",
  "**Top ağlarda, ben ağlamaz mıyım?**",
  "**Adamın biri gülmüş, bahçeye dikmişler.**",
  "**Ben kahve içiyorum, Nurgül Yeşilçay.**",
  "**Adamın biri gülmüş, saksıya koymuşlar.**",
  "**Röntgen Filmi çektirdik, yakında sinemalarda.🤪**",
  "**Canın sıkıldıysa gevşet.**",
  "**İneklerin sevmediği element?\nAZ-OT**",
  "**Örümcek adam ağ atamıyormuş neden?\nÇÜNKÜ AĞ BAĞLANTISI KOPMUŞ.**",
  "**İngilizler kendi kıllarına ne der?\nMICHEAL**",
  "**Yıkanan ton balığına ne denir?\nWASHINGTON**",
  "**En ihtiyaç duyulan arı?\n- başARI.**",
  "**-Küçük su birikintisine ne denir?\n-Sucuk**",
  "**Yerin kulağı vardır benim de kulağım var. O zaman ben yer miyim?\nYemem.**",
  "**Gözlüklerin numaralı mı?\n-Yok kale arkası **",
  "**-Cin Ali mavi mürekkebe düşerse nolur?\n-Blue Jean**",
  "**Erkek ata ne denir?\nBayat**",
  "**Almanya'da Almanlar yaşıyorsa,\nSakarya'da sakarlar mı yaşar?**",
  "**-Fransız ihtilali neye karşı yapılmıştır\n-Sabaha karşı**",
  "**-Size bol etli makarna yapayım mı?\nSiz mi? yapın bakalım\nm@k@rn@**"
  ]
        await message.edit(c(ESPİRİ))