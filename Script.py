class script(object):

    START_TXT = """<b>ʜᴇʏ {}, <i>{}</i>
    
✭ ɪ ᴀᴍ ᴀ ᴘᴏᴡᴇʀꜰᴜʟ ᴀᴜᴛᴏꜰɪʟᴛᴇʀ ʙᴏᴛ.\n✭ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ.\n✭ ɪ ᴡɪʟʟ ɢɪᴠᴇ ᴍᴏᴠɪᴇs ᴏʀ sᴇʀɪᴇs ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ.\n✭ ɪ ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇ sᴇʀɪᴇs ᴀɴɪᴍᴇ ɪɴ ᴘᴍ\n<blockquote>🌿 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href="https://t.me/mslanders">ᗰՏᒪᗩᑎᗪEᖇՏ</a></blockquote></b>"""
    
    MY_ABOUT_TXT = """<b>★ Server: All Web
★ Database: MongoDB
★ Language: Python
★ Library: Pyrogram</b>"""

    MY_OWNER_TXT = """<b>★ Nᴀᴍᴇ : AMANI
★ Usᴇʀɴᴀᴍᴇ : @MSLANDERSTALK_BOT
★ Cᴏᴜɴᴛʀʏ : KYA KREGA JANKE</b>"""

    STATUS_TXT = """🗂 Total Files: <code>{}</code>
👤 Total Users: <code>{}</code>
👥 Total Chats: <code>{}</code>
✨ Used Storage: <code>{}</code>
🗳 Free Storage: <code>{}</code>
🚀 Bot Uptime: <code>{}</code>"""

    CHANNELS = """
<b>⚡ ɢʀᴏᴜᴘs & ᴄʜᴀɴɴᴇʟs ɪɴғᴏ ⚡ 

▫ ᴀʟʟ ɴᴇᴡ ᴍᴏᴠɪᴇs & sᴇʀɪᴇs.
▫ ғᴀsᴛᴇsᴛ ʙᴏᴛs ᴀʀᴇ ᴀᴅᴅᴇᴅ.
▫ ғʀᴇᴇ & ᴇᴀsʏ ᴛᴏ ᴜsᴇ.
▫ 𝟸𝟺x𝟽 sᴇʀᴠɪᴄᴇs ᴀᴠᴀɪʟᴀʙʟᴇ.</b>"""
    
    NEW_GROUP_TXT = """#NewGroup
Title - {}
ID - <code>{}</code>
Username - {}
Total - <code>{}</code>"""

    NEW_USER_TXT = """#NewUser
★ Name: {}
★ ID: <code>{}</code>"""

    NOT_FILE_TXT = """<b>👋 Hello {},

I can't find the {} in my database! 🥲

👉 Google Search and check your spelling is correct.
👉 Please read the Instructions to get better results.
👉 Or not been released yet.</b>"""
    
    EARN_TXT = """<blockquote><b>──────「 Eᴀʀɴ Mᴏɴᴇʏ 」─────

➥ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴇᴀʀɴ ʟᴏᴛs ᴏғ ᴍᴏɴᴇʏ ғʀᴏᴍ ᴛʜɪꜱ ʙᴏᴛ ᴡɪᴛʜ ғʀᴇᴇ ᴛᴏ ᴜsᴇ ʙᴏᴛ.

›› sᴛᴇᴘ 𝟷 : ʏᴏᴜ ᴍᴜsᴛ ʜᴀᴠᴇ ᴀᴛʟᴇᴀsᴛ ᴏɴᴇ ɢʀᴏᴜᴘ ᴡɪᴛʜ ᴍɪɴɪᴍᴜᴍ 20 ᴍᴇᴍʙᴇʀs.

›› sᴛᴇᴘ 𝟸 : ᴍᴀᴋᴇ ᴀᴄᴄᴏᴜɴᴛ ᴏɴ ᴍᴅɪꜱᴋʟɪɴᴋ.ʟɪɴᴋ. [ ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴜsᴇᴅ ᴏᴛʜᴇʀ sʜᴏʀᴛɴᴇʀ ᴡᴇʙsɪᴛᴇ ]

›› sᴛᴇᴘ 𝟹 : /set_caption - to set custom bot files caption.

/set_caption 📁 Title : {file_name} [To Original File Name]
📁 Title : {file_caption} [To Default Caption]
⚜️ File Size : {file_size} [To File Size]

➥ ᴛʜɪꜱ ʙᴏᴛ ғʀᴇᴇ ғᴏʀ ᴀʟʟ ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘs ғʀᴇᴇ ᴏғ ᴄᴏꜱᴛ.

➥ᴅᴏɴ'ᴛ ᴡᴀɪᴛ ᴀɴʏ ʟᴏɴɢᴇʀ ᴛᴏ ꜱᴛᴀʀᴛ ᴇᴀʀɴɪɴɢ ᴍᴏɴᴇʏ ғʀᴏᴍ ʏᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘ. ᴀᴅᴅ ᴏᴜʀ ʙᴏᴛ ᴛᴏᴅᴀʏ ᴀɴᴅ ꜱᴛᴀʀᴛ ᴍᴀᴋɪɴɢ ᴍᴏɴᴇʏ.</b></blockquote>"""

    HOW_TXT = """<blockquote><b>ʜᴏᴡ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ᴏᴡɴ sʜᴏʀᴛɴᴇʀ ‼️

➥ ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ᴏᴡɴ sʜᴏʀᴛɴᴇʀ ᴛʜᴇɴ ᴊᴜsᴛ sᴇɴᴅ ᴛʜᴇ ɢɪᴠᴇɴ ᴅᴇᴛᴀɪʟs ɪɴ ᴄᴏʀʀᴇᴄᴛ ꜰᴏʀᴍᴀᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ

➥ ғᴏʀᴍᴀᴛ ↓↓↓

<code>/set_shortlink sʜᴏʀᴛɴᴇʀ sɪᴛᴇ sʜᴏʀᴛɴᴇʀ ᴀᴘɪ</code>

➥ ᴇxᴀᴍᴘʟᴇ ↓↓↓

<code>/set_shortlink mdisklink.link 5843c3cc645f5077b2200a2c77e0344879880b3e</code>

➥ ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴄʜᴇᴄᴋ ᴡʜɪᴄʜ sʜᴏʀᴛᴇɴᴇʀ ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛʜᴇɴ sᴇɴᴅ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴛʜᴇ ɢʀᴏᴜᴘ /get_shortlink

📝 ɴᴏᴛᴇ:- ʏᴏᴜ sʜᴏᴜʟᴅ ɴᴏᴛ ʙᴇ ᴀɴ ᴀɴᴏɴʏᴍᴏᴜs ᴀᴅᴍɪɴ ɪɴ ɢʀᴏᴜᴘ. sᴇɴᴅ ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜᴏᴜᴛ ʙᴇɪɴɢ ᴀɴ ᴀɴᴏɴʏᴍᴜs ᴀᴅᴍɪɴ.</b></blockquote>"""

    IMDB_TEMPLATE = """✅ I Found: <code>{query}</code>

🏷 Title: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Year: <a href={url}/releaseinfo>{year}</a>
🌟 Rating: <a href={url}/ratings>{rating} / 10</a>
☀️ Languages: {languages}
📀 RunTime: {runtime} Minutes

🗣 Requested by: {message.from_user.mention}
©️ Powered by: <b>{message.chat.title}</b>"""

    FILE_CAPTION = """<b>{caption}

<blockquote>🚫 Tʜɪs Fɪʟᴇ Wɪʟʟ Bᴇ Dᴇʟᴇᴛᴇᴅ Iɴ Tʜᴇ Nᴇxᴛ 10 Mɪɴᴜᴛᴇs 🚫</blockquote></b>"""

    WELCOME_TEXT = """👋 Hello {mention}, Welcome to {title} group! 💞"""

    HELP_TXT = """<b>Note - ✤ Wᴇ Hᴀᴠᴇ Dᴇᴠɪᴅᴇᴅ Bᴏᴛ Cᴏᴍᴍᴀɴᴅꜱ Fᴏʀ Gʀᴏᴜᴘ Oᴡɴᴇʀꜱ Aɴᴅ Bᴏᴛ Aꜱᴇʀꜱ.\n✤ Tʀʏ Eᴀᴄʜ Cᴏᴍᴍᴀɴᴅ Wɪᴛʜᴏᴜᴛ Aɴʏ Aʀɢᴜᴍᴇɴᴛ Tᴏ Sᴇᴇ Mᴏʀᴇ Dᴇᴛᴀɪʟs. 👨‍💻</b>"""
    
    ADMIN_COMMAND_TXT = """<b>Here is bot admin commands 👇

/index_channels - to check how many index channel id added
/stats - to get bot status
/delete - to delete files using query
/delete_all - to delete all indexed file
/broadcast - to send message to all bot users
/grp_broadcast - to send message to all groups
/pin_broadcast - to send message as pin to all bot users.
/pin_grp_broadcast - to send message as pin to all groups.
/restart - to restart bot
/leave - to leave your bot from particular group
/unban_grp - to enable group
/ban_grp - to disable group
/ban_user - to ban a users from bot
/unban_user - to unban a users from bot
/users - to get all users details
/chats - to get all groups
/invite_link - to generate invite link
/index - to index bot accessible channels</b>"""
    
    USER_COMMAND_TXT = """<b>Here is bot user commands 👇

/start - to check bot alive or not
/gofile - upload file to gofile.io
/settings - to change group settings as your wish
/set_template - to set custom imdb template
/set_caption - to set custom bot files caption
/set_shortlink - group admin can set custom shortlink
/get_custom_settings - to get your group settings details
/set_welcome - to set custom new joined users welcome message for group
/set_tutorial - to set custom tutorial link in result page button
/id - to check group or channel id
/set_fsub - to set force subscribe channels
/remove_fsub - to remove all force subscribe channel</b>"""
    
