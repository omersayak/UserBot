import os
import json
from .tg import owner_status
from .commands import commands_knowledge
from .about import about_info
from .send_profile import profile_send
from .gnydn import send_gnydn_message
from .ban_member import ban_member_chat
from .unban_member import unban_member_chat
from .mute_member import mute_member_chat
from .unmute_member import unmute_member_chat
from .spam import spam_message
from .pm import send_pm_message
from .iplogger import iplogger_info
from .afk import afk_info
from .dostum import info_dst
from .ramizDayi import info_Ramis
from .ook import info_ook 
from .espiri import info_Esp
from .yuru import info_Yuru
from .fatiha import fatiha_info
from .hekir import hekir_info
from .hack import hack_info
from .afrodisiyak import info_afro
from .jınx import info_Jinx
from .alive import bot_status
from .sakaknk import saka_knk



# prefix'leri yükle
config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "config.json")
with open(config_file, "r") as f:
    prefix = json.load(f)["prefix"]

def register_plugins(app):
    saka_knk(app,prefix)
    bot_status(app,prefix)
    info_Jinx(app,prefix)
    info_afro(app,prefix)
    hack_info(app,prefix)
    hekir_info(app,prefix)
    fatiha_info(app,prefix)
    info_Yuru(app,prefix)
    info_Esp(app,prefix)
    info_ook(app,prefix)
    info_Ramis(app,prefix)
    info_dst(app,prefix)
    owner_status(app,prefix)
    commands_knowledge(app,prefix)
    about_info(app,prefix)
    profile_send(app,prefix)
    send_gnydn_message(app,prefix)
    ban_member_chat(app,prefix)
    unban_member_chat(app,prefix)
    mute_member_chat(app,prefix)
    unmute_member_chat(app,prefix)
    spam_message(app,prefix)
    send_pm_message(app,prefix)
    iplogger_info(app,prefix)
    afk_info(app,prefix) 
    








