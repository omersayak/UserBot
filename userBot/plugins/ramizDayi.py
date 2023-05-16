from pyrogram import filters
import asyncio
from config import admin_id
from random import choice as c


def info_Ramis(app,prefix):
    @app.on_message(filters.command('dayı', prefixes=prefix)& filters.user(admin_id))
    async def dayı(client, message):
        RAMİZ = [
    "**Unuttum demek bile hatırlamaktır.\n💥@Professore_1💥**",
    "**Bir yankı… Durmadan yalnızsınız.\n💥@Professore_1💥**",
    "**Ölüm çekip gitmek değildir.\n💥@Professore_1💥**",
    "**Silemiyorsan karalayacaksın.\n💥@Professore_1💥**",
    "**Ve son sözü hep alın yazısı söyler.\n💥@Professore_1💥**",
    "**Herkes öldürür sevdiğini.\n💥@Professore_1💥**",
    "**Elinden bir şey gelmeyince kabullenmek kolaydır.\n💥@Professore_1💥**",
    "**Kim kazanmışki ben kazanacaktım seni bu şehri.\n💥@Professore_1💥**",
    "**Affetmek ve unutmak iyi insanların intikamıdır.\n💥@Professore_1💥**",
    "**Bir hata, gözden kaçan bir söz; her şeyi kaybetmektir.\n💥@Professore_1💥**",
    "**En büyük arkadaştan en büyük düşman olur.\n💥@Professore_1💥**",
    "**Delikanlı adamın silahı yüreğidir,oda tutukluk yapmaz...\n💥@Professore_1💥**",
    "**Bazen hayat seni öyle zorlarki yolun başında kimdin unutursun.\n💥@Professore_1💥**",
    "**Küfür şeytana mahsustur, tövbe insana! Aşk kadına yakışır, sevmek adama.\n💥@Professore_1💥**",
    "**Kiminle güldüğünü belki unutabilirsin,ama kiminle ağladığını asla !\n💥@Professore_1💥**",
    "**Naparsanız yapın,iyi bir adamın yüreğindeki iyiliği söküp alamazsınız!\n💥@Professore_1💥**",
    "**Sadakat sır saklamak mıdır? Sessiz kalmak mıdır? Kıyametin kopacağını bile bile.\n💥@Professore_1💥**",
    "**Bir babanın çaresizliği, çaresizliklerin en korkuncudur.\n💥@Professore_1💥**",
    "**Kaygılanma çocuk, herkes ölür! Kimi toprağa, kimi yüreğe gömülür.\n💥@Professore_1💥**",
    "**Bu alemde en mühimi adaletin terazisini doğru tutmaktır.\n💥@Professore_1💥**",
    "**Asıl çaresizlik kendine elimden geleni yaptım mı diye sormaktır.\n💥@Professore_1💥**",
    "**Acı çekmiş hiç kimse,artık eskisi gibi değildir.\n💥@Professore_1💥**",
    "**Herkesin bir geçmişi vardır, bir de geçmemişi.\n💥@Professore_1💥**",
    "**Unutma insan paranın sahtesini yapar,parada insanın.\n💥@Professore_1💥**",
    "**Seni ölüme götürse de, Doğrudan asla şaşmayacaksın.\n💥@Professore_1💥**",
    "**Bir ihtimal daha var o da ölmek mi dersin?\n💥@Professore_1💥**",
    "**Ne umutlar fısıldarsa fısıldasın sana hayat,çeker gider sadık kalmaz sonunda.\n💥@Professore_1💥**",
    "**Portakalı soymadan içinin iyi olup olmadığını anlayamazsın.\n💥@Professore_1💥**",
    "**Düşmanı affetmek kolay,zor olan dostu affetmektir.\n💥@Professore_1💥**",
    "**Biz işimizi yapar geçeriz. Eleştirilere neden kızayım ki? Herkes istediğini düşünebilir.\n💥@Professore_1💥**",
    "**Bazen sevdiğin insanları korumanın tek yolu onlardan uzak durmaktır...\n💥@Professore_1💥**",
    "**Paranla şeref kazanma,şerefinle para kazanki;paran bittiğinde,şerefinde bitmesin.\n💥@Professore_1💥**",
    "**Dostunu yanınada alsan,karşınada alsan,o her zaman seni vurucak bir pozisyon bulur.\n💥@Professore_1💥**",
    "**Bir dönemi masalsı bir anlatım içinde anlatmasına rağmen içindeki acı gerçek bıçak gibi saplanıyo insana.\n💥@Professore_1💥**",
    "**Gerçek niyetini kimse bilmeyecek.Kaderin sırrındır kaderini kimseyle paylaşmayacaksın...\n💥@Professore_1💥**",
    "**Aynada kendine tahammül edemeyen adam yalnızdır.\n💥@Professore_1💥**",
    "**Yalnızlığına iyi bak ve çok iyi sahip çık,kaç kişinin emeği var onda.\n💥@Professore_1💥**",
    "**Bir avuç kömür için, bir ömür verenlere. Dualarımız sizinle.\n💥@Professore_1💥**",
    "**Bir şey olmuyorsa ya daha iyisi olacağı için, ya da gerçekten de olmaması gerektiği için olmuyordur.\n💥@Professore_1💥**",
    "**Artık kaybedecek hiçbir şeyinin kalmaması, özgürlük olsa gerek.\n💥@Professore_1💥**",
    "**Uykun gelmiyor diye gözlerini suçlama, Belkide o beklediğin uyku değildir.\n💥@Professore_1💥**",
    "**Öldürmek için gelen öldürmeden dönebilir ama ölmek için gelen.. Ölmeden dönmez.\n💥@Professore_1💥**",
    "**Dön bak arkana yeğen. Gitmez” dediğin kaç kişi yanında?\n💥@Professore_1💥**",
    "**Kendinizi unutmayın paşa hazretleri bazı insanlar vardır ki kendi kendilerine zarar verirler.\n💥@Professore_1💥**",
    "**Gecenin bir yarısı sorgun bitti diyip açarlarsa kapını aslında niye açtıklarınıda bilirsin evlat.\n💥@Professore_1💥**",
    "**Silemiyorsan karalayacaksın.\n💥@Professore_1💥**",
    "**İntikam ölümden güçlüdür.\n💥@Professore_1💥**",
    "**Teslim olunmadan, sadık olunmaz.\n💥@Professore_1💥**",
    "**Affetmek ve unutmak, iyi insanların intikamıdır.\n💥@Professore_1💥**",
    "**Yalnızlığına iyi bak ve çok iyi sahip çık, kaç kişinin emeği var onda.\n💥@Professore_1💥**"

        ]
        await message.edit(c(RAMİZ))
        
