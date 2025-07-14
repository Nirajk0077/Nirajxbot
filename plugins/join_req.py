from pyrogram import Client, filters, enums
from pyrogram.types import ChatJoinRequest
from database.users_chats_db import db
from info import *

@Client.on_chat_join_request(filters.chat(AUTH_REQ_CHANNEL))
async def join_reqs(client, message: ChatJoinRequest):
  if not await db.find_join_req(message.from_user.id):
    await db.add_join_req(message.from_user.id)

@Client.on_chat_join_request(filters.chat(AUTH_CHANNELS))
async def join_reqss(client, message: ChatJoinRequest):
  user_id = message.from_user.id
  channel_id = message.chat.id
  if not await db.find_join_reqq(user_id, channel_id):
    await db.add_join_reqq(user_id, channel_id)

@Client.on_message(filters.command("delreq") & filters.private & filters.user(ADMINS))
async def del_requests(client, message):
    await db.del_join_req()    
    await message.reply("<b>⚙ ꜱᴜᴄᴄᴇꜱꜱғᴜʟʟʏ ᴄʜᴀɴɴᴇʟ ʟᴇғᴛ ᴜꜱᴇʀꜱ ᴅᴇʟᴇᴛᴇᴅ</b>")