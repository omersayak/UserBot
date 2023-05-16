from pyrogram import filters
import asyncio
from config import admin_id
from random import choice as c



def info_Yuru(app,prefix):
    @app.on_message(filters.command('yuru', prefixes=prefix)& filters.user(admin_id))
    async def yuru(client, message):
        YAVSA = [
  
"**Eğer geceler seni düşündüğüm kadar uzun olsaydı asla sabah olmazdı.**",
"**Sen aklım ve kalbim arasında kalan en güzel çaresizliğimsin.**",
"**Aslında bütün insanları sevebilirdim sevmeye ilk senden başlamasaydım.**",
"**Nasıl göründüğünü sorma, en güzel benimle görünüyorsun.**",
"**Dua gibisin bana. Ne vakit seni ansam, bir huzurun içine düşüyorum.**",
"**Sen olmayınca buralar buz gibi. Sensizlik bir iklim adı şimdilerde…**",
"**Dünyadaki en güzel şeyi sana vermek isterdim ama seni sana veremem ki.**",
"**Bütün şairler sana mı aşıktı ki her okuduğum şiirde, dinlediğim ezgide sen vardın.**",
"**Burası gönül demliği yar. Dile dua, çaya dem, yüreğe kıdem. Aşk’a vefalı olan gelsin.**",
"**O senin neyin olur dediler. Uzaktan dedim uzaktan yandığım olur kendisi.**",
"**Yüreğini yasla bana sevgili, bir ömür birbirimize yük olalım.**",
"**Eğer geceler seni düşündüğüm kadar uzun olsaydı asla sabah olmazdı.**",
"**Sabahın güneşi sessiz doğsa da dünyama, senin gibi ısıtmıyor içimi bir tanem benim.❤️**",
"**Eğer adına eşlik edecekse soyadım, Allah için ahirete kadar senindir sol yanım.**",
"**Kalbimin çalar saati gibisin sevgilim. Ne zaman sevmek vaktim gelse sen düşersin gönlüme.**",
"**Seni anlatmak istesem anlatamam çünkü sen bu evrendeki her şeyden daha güzelsin.**",
"**Sen kışlarımda aylarımda yaz güneşi oldun, sen benim her mevsimi yaza döndüren tek güneşim olsun.**",
"**Bir gün cehennemde karsılaşabiliriz. Sen kalp hırsızı olduğun için, bense tanrıyı bırakıp sana taptığım için.**",
"**Gökyüzündeki bütün yıldızları toplasan bir tek sen etmez, fakat bir tek sen hepsine bedelsin.**",
"**Hatalı olduğumda beni sev. Korktuğumda beni sar. Ve gittiğimde tut. Çünkü ihtiyacım olan her şey sensin.**",
"**Öyle uzaktan seyretme adına hayran olduğum yar.Buyur gel ömrüme, ömrüm, ömrün olsun.**",
"**Ne kadar seviyorsun dersen nar kadar derim. Dışımda bir ben görünürüm içimde binlerce sen dökülür.**",
"**Gördüğüm en güzel manzaradır yüzün gözlerin bakışların. Duyduğum en güzel şarkıdır sesin.**",
"**Kalbimdeki aşka, dudaklarımdaki gülüşe, akan gözyaşlarıma, yalnızca sen layıksın. Çünkü benim için çok özelsin aşkım.**",
"**Canım benim bilir misin? Canım dediğimde içimden canım çıkıp sana koştuğunu duyarım hep.**",
"**Gözlerin benden başkasına bakmasın, sen var isen hayatımda ben varım senin için bu yalan olan hayatta bir tanem.**",
"**Bir hasret kadar uzak olsan da bir nefes kadar yakınsın yüreğime. Ömrüme ömür katan yarim.**",
"**Seni ne kadar sevdiğimi öğrenmek istersen vur kır kalbimi kalbimden akan kan yazacaktır ismini o zaman anlarsın sana olan sevgimi.❤️❤️**",
"**İki kişi birbirini severse; sevgi olur. Biri kaçar, diğeri kovalarsa: aşk olur. İkisi de sever lakin kavuşamazsa efsane olur.**",
"**Baştan yaşama şansım olsaydı eğer; kusursuz olmaya çalışmaz rahat bırakırdım yüreğimi korkmazdım çok riske girip sana aşık olmaktan.**",
"**Yalnızlık gecelerin, umut bekleyenlerin, hayal çaresizlerin, yağmur sokakların, tebessüm dudaklarının, sen ise yalnız benimsin!**",
"**Önce düştüğümde kalkmayı, sonra aleve dokunduğumda acıyı, sevmeyi öğrendim, sevilmeyi. Her şeyi öğrendim de yalnız seni unutmayı öğrenemedim.**",
"**Seni yıldızlara benzetiyorum onlar kadar etkileyici, çekici ve güzelsin ama aranızda tek fark var onlar milyonlarca sen bir tanesin.**",
"**Bir yağmur damlası seni seviyorum anlamını taşısaydı ve sen bana, seni ne kadar sevdiğimi soracak olsaydın, inan ki bir tanem her gün yağmur yağardı.**",
"**Korkma! Sakın sevmekten korkma. Kurşun sesi kadar hızlı geçer yaşamak ama öylesine zor ki kurşunu havada sevdayı sıcacık yürekte tutmak.**",
"**Ne zaman sağır bir ressam, kristal bir zemin üzerine düşen gülün sesinin resmini çizerse, işte o zaman seni unutur bir başkasını severim.**",
"**Sabah seni izlemesi için bir melek yolladım peşinden ama düşündüğümden de erken döndü. Ne oldu dedim? Bir melek asla başka bir meleği izleyemez dedi.**",
"**Seni düşününce ısınır soğuk gecelerim, sen aklıma gelince güler mutsuz yüzüm sevgilim, seninle hayat buldu bu bedenim sensiz bu yalan hayatı neyleyim.**",
"**Ne insanlar tanıdım yıldızlar gibiydiler. Hepsi göklerdeydi parlıyordu. Ama ben seni güneşi seçtim. Bir güneş için bin yıldızdan vazgeçtim.**",
"**Hasret kapımda nöbetler tutuyor. Sevgilim uzak bir şehirde gözlerim onu arıyor. Bir kuş olup gitsem aşsam şu enginleri varsam senin yanına öpsem doyasıya koklasam.**",
"**Her zaman adını andım nefesimde, her saniye seni düşünüp hayalini kurdum gözlerimde, sensiz bir hayatı kabullenemem ölürüm sensizlik ölüm gibi gelir hayata küser giderim sevgilim.**",
"**Düşüyorum seni gecenin karanlık yüzünde, düşünüyorum hayalini buz tutmuş odamın soğuk köşelerinde, sen varsan razıyım hayatın çilesine, sen yoksa ölürüm yalnızlığımın nöbetinde.**",
"**Yalanların içinde tek gerçeksin benim gözümde, sahte gülüşlerin içinde tek doğrusun sevdim seni bir kere, dünya dönse de inadına çevremde, ben sensiz nefes alamıyorum dünya kimin umurunda banane.**",
"**Bir gülüşünle hayata dönerim yeniden, sensiz buz tutan için alev alev olur gülüşünle, sensiz bir yalan olurum yalan hayatın içinde, seninle gerçekleri yaşarım gerçek olan aşkımın içinde.**",
"**Gülüşünle yalnızlığıma bir son veriyorum her gece, seni hayal edince mutlu oluyorum yalnızlığımın gölgesinde, seninle ölüme bile giderim düşünmem bir an bile, sensin benim tek sevdiğim bu can sana feda olsun her nefesimde.**",
"**Aşk bir su damlası olsaydı okyanusları, bir yaprak olsaydı bütün ormanları, bir yıldız olsaydı tüm kainatı sana vermek isterdim. Ama sadece seni seven kalbimi verebiliyorum.**",
"**Ne zaman batan güneşe baksam hüzünlenirim yanımda yoksun diye, ne zaman yıldızlara baksam üşürüm hayalinle ısınırım, ne zaman yanımda olsan işte bunların hepsini unuturum bir tanem benim.**",
"**Hayatta üç şeyi sevdim. Seni, kalbimi, ümit etmeyi. Seni sevdim, sensin diye. Kalbimi sevdim, seni sevdi diye. Ümit etmeyi sevdim, belki seversin diye.**",
  ]
        
        await message.edit(c(YAVSA))
