import json
from pyrogram import Client
from config import api_id, api_hash
from plugins import register_plugins




app = Client(name="My_account", api_id=api_id, api_hash=api_hash)

# tüm filtreleri yükleyin
register_plugins(app)

if __name__ == '__main__':
    app.run()
