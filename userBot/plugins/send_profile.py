from pyrogram import filters
import asyncio
from config import admin_id
import os


# def profile_send2(app,prefix):
#     @app.on_message(filters.command(["profil2"], prefixes=prefix))
#     async def view_profile_photo(client, message):
#         await message.delete()
#         user_id = message.from_user.id if not message.reply_to_message else message.reply_to_message.from_user.id
#         user_profile_photo = await client.get_users(user_id)
#         if user_profile_photo.photo:
#             profile_photo_file_id = user_profile_photo.photo.big_file_id
#             await client.send_photo(chat_id=message.chat.id, photo=profile_photo_file_id)
#         else:
#             await client.send_message(chat_id=message.chat.id, text="Profil fotoğrafı bulunamadı.")
        

def profile_send(app,prefix):
    @app.on_message(filters.command(["profil"], prefixes=prefix))
    async def view_profile_photo(client, message):
        await message.delete()
        
        user_id = message.from_user.id
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
        
        user_profile_photo = await client.get_users(user_id)
        if user_profile_photo.photo:
            profile_photo_file_id = user_profile_photo.photo.big_file_id
            profile_photo_path = await client.download_media(profile_photo_file_id)
            
            await client.send_photo(chat_id=message.chat.id, photo=profile_photo_path)
            os.remove(profile_photo_path)  # İndirilen dosyayı temizleyelim
        else:
            await client.send_message(chat_id=message.chat.id, text="Profil fotoğrafı bulunamadı.")
