import os
import threading
import subprocess
import time

import pyrogram
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton

import mdisk
import extras
import mediainfo
import split
from split import TG_SPLIT_SIZE


# app
bot_token = os.environ.get("TOKEN", "") 
api_hash = os.environ.get("HASH", "") 
api_id = os.environ.get("ID", "")
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# preiumum
from split import ss, temp_channel, isPremmium
if isPremmium: acc = Client("myacc", api_id=api_id, api_hash=api_hash, session_string=ss)

# optionals
auth = os.environ.get("AUTH", "")
ban = os.environ.get("BAN", "")
from mdisk import iswin

# start command
@app.on_message(filters.command(["start"]))
def echo(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):

    if not checkuser(message):
        app.send_message(message.chat.id,"""𝐻𝐸𝐿𝐿𝑂 👋 𝑌𝑂𝑈 𝑁𝐸𝐸𝐷 𝑇𝑂 𝐵𝑈𝑌 𝑆𝑈𝐵𝑆𝐶𝑅𝐼𝑃𝑇𝐼𝑂𝑁 𝑇𝑂 𝑈𝑆𝐸 𝑀𝐸👇\n

𝑇𝐻𝐼𝑆 𝐴𝑅𝐸 𝑀𝑌 𝑃𝐿𝐴𝑁𝑆 
₹80/1$ - 1 𝑤𝑒𝑒𝑘

₹120/2$ - 2 𝑤𝑒𝑒𝑘𝑠

₹140/3$ - 3 𝑤𝑒𝑒𝑘𝑠

₹160/4$ - 4 𝑤𝑒𝑒𝑘𝑠

𝑈 𝑊𝐴𝑁𝑇 𝐽𝑈𝑆𝑇 𝐷𝑀 𝑀𝐸 :@fligher""", reply_to_message_id=message.id,reply_markup=InlineKeyboardMarkup([[ InlineKeyboardButton("📦 Source Code", url="https://t.me/movie_time_botonly")]]))
        return

    app.send_message(message.chat.id, '**Hi, I am Mdisk Video Downloader, you can watch Videos without MX Player.\n__Send me a link to Start...__**',reply_to_message_id=message.id,
    reply_markup=InlineKeyboardMarkup([[ InlineKeyboardButton("🏆TRUMBOTS🏆", url="https://t.me/movie_time_botonly")]]))

# help command
@app.on_message(filters.command(["help"]))
def help(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    
    if not checkuser(message):
        app.send_message(message.chat.id, '__You are either not **Authorized** or **Banned**__',reply_to_message_id=message.id)
        return
    
    helpmessage = """__**/start** - basic usage
**/help** - this message
**/mdisk mdisklink** - usage
**/thumb** - reply to a image document of size less than 200KB to set it as Thumbnail ( you can also send image as a photo to set it as Thumbnail automatically )
**/remove** - remove Thumbnail
**/show** - show Thumbnail
**/change** - change upload mode ( default mode is Document )__"""
    app.send_message(message.chat.id, helpmessage, reply_to_message_id=message.id)

# about command
@app.on_message(filters.command(["about"]))
def help(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    
    if not checkuser(message):
        app.send_message(message.chat.id, '__You are either not **Authorized** or **Banned**__',reply_to_message_id=message.id)
        return
    
    helpmessage = """╭───────────⍟
├🤖 𝙼𝚈 𝙽𝙰𝙼𝙴 : <a href =https://t.me/flash_urlBot>ᴍᴅɪsᴋ ᴅᴏᴡɴʟᴏᴅᴇʀ ʙᴏᴛ</a>
├👑 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁𝚂 : <a href=https://t.me/movie_time_botonly>𝗧𝗥𝗨𝗠𝗕𝗢𝗧𝗦</a> 
├👨‍💻 𝙿𝚁𝙾𝙶𝚁𝙰𝙼𝙴𝚁 : <a href=https://t.me/FLIGHER>FLIGHER</a>
├📕 𝙻𝙸𝙱𝚁𝙰𝚁𝚈 : <a href=https://github.com/pyrogram>𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼</a>
├✏️ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴 : <a href=https://www.python.org>𝙿𝚈𝚃𝙷𝙾𝙽 3</a>
├💾 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴 : <a href=https://cloud.mongodb.com>𝙼𝙾𝙽𝙶𝙾𝙳𝙱</a>
├🌀 𝙼𝚈 𝚂𝙴𝚁𝚅𝙴𝚁 : <a href=https://dashboard.heroku.com>𝙷𝙴𝚁𝙾𝙺𝚄</a>
├📊 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚄𝚂 : v3.6.8 [ 𝙼𝙰𝙹𝙾𝚁 ] """
    app.send_message(message.chat.id, helpmessage, reply_to_message_id=message.id)
    
    
# check for user access
def checkuser(message):
    if auth != "" or ban != "":
        valid = 1
        if auth != "":
            authusers = auth.split(",")
            if str(message.from_user.id) not in authusers:
                valid = 0
        if ban != "":
            bannedusers = ban.split(",")
            if str(message.from_user.id) in bannedusers:
                valid = 0
        return valid        
    else:
        return 1


# download status
def status(folder,message,fsize):
    fsize = fsize / pow(2,20)
    length = len(folder)
    # wait for the folder to create
    while True:
        if os.path.exists(folder + "/vid.mp4.part-Frag0") or os.path.exists(folder + "/vid.mp4.part"):
            break
    
    time.sleep(3)
    while os.path.exists(folder + "/" ):
        if iswin == "0":
            result = subprocess.run(["du", "-hs", f"{folder}/"], capture_output=True, text=True)
            size = result.stdout[:-(length+2)]
        else:
            os.system(f"dir /a/s {folder} > tempS-{message.id}.txt")
            size = str(int(open(f"tempS-{message.id}.txt","r").readlines()[-2].split()[2].replace(",","")) // 1000000) + "MB "

        try:
            app.edit_message_text(message.chat.id, message.id, f"{filename}\n\n__Downloaded__ : ᴛᴀᴋᴇ sᴏᴍᴇ ᴛɪᴍᴇ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ  ʙᴇ ᴘᴀᴛɪᴇɴᴛ  **{size} **__of__**  {fsize:.1f}M**")
            time.sleep(10)
        except:
            time.sleep(5)

    if iswin != "0": os.remove(f"tempS-{message.id}.txt")


# upload status
def upstatus(statusfile,message):
    while True:
        if os.path.exists(statusfile):
            break

    time.sleep(3)      
    while os.path.exists(statusfile):
        with open(statusfile,"r") as upread:
            txt = upread.read()
        try:
            app.edit_message_text(message.chat.id, message.id, f"{filename}\n\n__Uploaded__ : **{txt}**")
            time.sleep(10)
        except:
            time.sleep(5)


# progress writter
def progress(current, total, message):
    with open(f'{message.id}upstatus.txt',"w") as fileup:
        fileup.write(f"{current * 100 / total:.1f}%")


# download and upload
def down(message,link):

    # checking link and download with progress thread
    msg = app.send_message(message.chat.id, '__Downloading__', reply_to_message_id=message.id)
    size = mdisk.getsize(link)
    if size == 0:
        app.edit_message_text(message.chat.id, msg.id,"__**Invalid Link🧑‍💻 ɪɴᴠᴀʟɪᴅ ⛓ ʟɪɴᴋ ᴍᴇᴀɴ ᴛʜᴇ ғɪʟᴇ sʜᴀʀɪɴɢ ɪs ᴇxᴘɪʀᴇᴅ ᴏʀ ᴄᴏᴘʏʀɪɢʜᴛ 🖇**__")
        return
    sta = threading.Thread(target=lambda:status(str(message.id),msg,size),daemon=True)
    sta.start()

    # checking link and download and merge
    file,check,filename = mdisk.mdow(link,message)
    if file == None:
        app.edit_message_text(message.chat.id, msg.id,"__**Invalid Link Or The File in Mdisk may removed or sharing Cancelled**__")
        return

    # checking if its a link returned
    if check == -1:
        app.edit_message_text(message.chat.id, msg.id,f"__**Can't Download File but here is the Download Link : {file}**__")
        os.rmdir(str(message.id))
        return

    # checking size
    size = split.get_path_size(file)
    if(size > TG_SPLIT_SIZE):
        app.edit_message_text(message.chat.id, msg.id, "__More Than 2GB Splitting__")
        flist = split.split_file(file,size,file,".", TG_SPLIT_SIZE)
        os.remove(file) 
    else:
        flist = [file]
    app.edit_message_text(message.chat.id, msg.id, "__Uploading__")
    i = 1

    # checking thumbline
    if not os.path.exists(f'{message.from_user.id}-thumb.jpg'):
        thumbfile = None
    else:
        thumbfile = f'{message.from_user.id}-thumb.jpg'

    # upload thread
    upsta = threading.Thread(target=lambda:upstatus(f'{message.id}upstatus.txt',msg),daemon=True)
    upsta.start()
    info = extras.getdata(str(message.from_user.id))

    # uploading
    for ele in flist:

        # checking file existence
        if not os.path.exists(ele):
            app.send_message(message.chat.id,"**Error in Merging File**",reply_to_message_id=message.id)
            return
            
        # check if it's multi part
        if len(flist) == 1:
            partt = ""
        else:
            partt = f"__**part {i}**__\n"
            i = i + 1

        # actuall upload
        if info == "V":
            thumb,duration,width,height = mediainfo.allinfo(ele,thumbfile)
            if not isPremmium : app.send_video(message.chat.id, video=ele, caption=f"<a href ='https://t.me/movie_time_botonly'>{partt}**{filename}**</a>", thumb=thumb, duration=duration, height=height, width=width, reply_to_message_id=message.id, progress=progress, progress_args=[message])
            else:
                with acc: tmsg = acc.send_video(temp_channel, video=ele, caption=f"{partt}**{filename}**", thumb=thumb, duration=duration, height=height, width=width, progress=progress, progress_args=[message])
                app.copy_message(message.chat.id, temp_channel, tmsg.id, reply_to_message_id=message.id)
            if "-thumb.jpg" not in thumb: os.remove(thumb)
        else:
            if not isPremmium : app.send_document(message.chat.id, document=ele, caption=f"<a href ='https://t.me/movie_time_botonly'>{partt}**{filename}**</a>", thumb=thumbfile, force_document=True, reply_to_message_id=message.id, progress=progress, progress_args=[message])
            else:
                with acc: tmsg = acc.send_document(temp_channel, document=ele, thumb=thumbfile, caption=f"<a href ='https://t.me/movie_time_botonly'>{partt}**{filename}**</a>", force_document=True, progress=progress, progress_args=[message])
                app.copy_message(message.chat.id, temp_channel, tmsg.id, reply_to_message_id=message.id)
       
        # deleting uploaded file
        os.remove(ele)
        
    # checking if restriction is removed    
    if check == 0:
        app.send_message(message.chat.id,"__Can't remove the **restriction**, you have to use **MX player** to play this **video**\n\nThis happens because either the **file** length is **too small** or **video** doesn't have separate **audio layer**__",reply_to_message_id=message.id)
    if os.path.exists(f'{message.id}upstatus.txt'):
        os.remove(f'{message.id}upstatus.txt')
    app.delete_messages(message.chat.id,message_ids=[msg.id])


# mdisk command
@app.on_message(filters.command(["mdisk"]))
def mdiskdown(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    
    if not checkuser(message):
        app.send_message(message.chat.id, """𝐻𝐸𝐿𝐿𝑂 👋 𝑌𝑂𝑈 𝑁𝐸𝐸𝐷 𝑇𝑂 𝐵𝑈𝑌 𝑆𝑈𝐵𝑆𝐶𝑅𝐼𝑃𝑇𝐼𝑂𝑁 𝑇𝑂 𝑈𝑆𝐸 𝑀𝐸👇\n
𝑇𝐻𝐼𝑆 𝐴𝑅𝐸 𝑀𝑌 𝑃𝐿𝐴𝑁𝑆 
₹80/1$ - 1 𝑤𝑒𝑒𝑘
₹120/2$ - 2 𝑤𝑒𝑒𝑘𝑠
₹140/3$ - 3 𝑤𝑒𝑒𝑘𝑠
₹160/4$ - 4 𝑤𝑒𝑒𝑘𝑠
𝑈 𝑊𝐴𝑁𝑇 𝐽𝑈𝑆𝑇 𝐷𝑀 𝑀𝐸 :@fligher""",reply_to_message_id=message.id)
        return

    try:
        link = message.text.split("mdisk ")[1]
        if "https://mdisk.me/" in link:
            d = threading.Thread(target=lambda:down(message,link),daemon=True)
            d.start()
            return 
    except:
        pass

    app.send_message(message.chat.id, '**Send only __MDisk Link__ with command followed by the link**',reply_to_message_id=message.id)


# thumb command
@app.on_message(filters.command(["thumb"]))
def thumb(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    
    if not checkuser(message):
        app.send_message(message.chat.id, """𝐻𝐸𝐿𝐿𝑂 👋 𝑌𝑂𝑈 𝑁𝐸𝐸𝐷 𝑇𝑂 𝐵𝑈𝑌 𝑆𝑈𝐵𝑆𝐶𝑅𝐼𝑃𝑇𝐼𝑂𝑁 𝑇𝑂 𝑈𝑆𝐸 𝑀𝐸👇\n
𝑇𝐻𝐼𝑆 𝐴𝑅𝐸 𝑀𝑌 𝑃𝐿𝐴𝑁𝑆 
₹80/1$ - 1 𝑤𝑒𝑒𝑘
₹120/2$ - 2 𝑤𝑒𝑒𝑘𝑠
₹140/3$ - 3 𝑤𝑒𝑒𝑘𝑠
₹160/4$ - 4 𝑤𝑒𝑒𝑘𝑠
𝑈 𝑊𝐴𝑁𝑇 𝐽𝑈𝑆𝑇 𝐷𝑀 𝑀𝐸 :@fligher""",reply_to_message_id=message.id)
        return

    try:
        if int(message.reply_to_message.document.file_size) > 200000:
            app.send_message(message.chat.id, '**Thumbline size allowed is < 200 KB**',reply_to_message_id=message.id)
            return

        msg = app.get_messages(message.chat.id, int(message.reply_to_message.id))
        file = app.download_media(msg)
        os.rename(file,f'{message.from_user.id}-thumb.jpg')
        app.send_message(message.chat.id, '**Thumbnail is Set**',reply_to_message_id=message.id)

    except:
        app.send_message(message.chat.id, '**reply __/thumb__ to a image document of size less than 200KB**',reply_to_message_id=message.id)


# show thumb command
@app.on_message(filters.command(["show"]))
def showthumb(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    
    if not checkuser(message):
        app.send_message(message.chat.id, """𝐻𝐸𝐿𝐿𝑂 👋 𝑌𝑂𝑈 𝑁𝐸𝐸𝐷 𝑇𝑂 𝐵𝑈𝑌 𝑆𝑈𝐵𝑆𝐶𝑅𝐼𝑃𝑇𝐼𝑂𝑁 𝑇𝑂 𝑈𝑆𝐸 𝑀𝐸👇\n
𝑇𝐻𝐼𝑆 𝐴𝑅𝐸 𝑀𝑌 𝑃𝐿𝐴𝑁𝑆 
₹80/1$ - 1 𝑤𝑒𝑒𝑘
₹120/2$ - 2 𝑤𝑒𝑒𝑘𝑠
₹140/3$ - 3 𝑤𝑒𝑒𝑘𝑠
₹160/4$ - 4 𝑤𝑒𝑒𝑘𝑠
𝑈 𝑊𝐴𝑁𝑇 𝐽𝑈𝑆𝑇 𝐷𝑀 𝑀𝐸 :@fligher""",reply_to_message_id=message.id)
        return
    
    if os.path.exists(f'{message.from_user.id}-thumb.jpg'):
        app.send_photo(message.chat.id,photo=f'{message.from_user.id}-thumb.jpg',reply_to_message_id=message.id)
    else:
        app.send_message(message.chat.id, '**Thumbnail is not Set**',reply_to_message_id=message.id)


# remove thumbline command
@app.on_message(filters.command(["remove"]))
def removethumb(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    
    if not checkuser(message):
        app.send_message(message.chat.id, """𝐻𝐸𝐿𝐿𝑂 👋 𝑌𝑂𝑈 𝑁𝐸𝐸𝐷 𝑇𝑂 𝐵𝑈𝑌 𝑆𝑈𝐵𝑆𝐶𝑅𝐼𝑃𝑇𝐼𝑂𝑁 𝑇𝑂 𝑈𝑆𝐸 𝑀𝐸👇\n
𝑇𝐻𝐼𝑆 𝐴𝑅𝐸 𝑀𝑌 𝑃𝐿𝐴𝑁𝑆 
₹80/1$ - 1 𝑤𝑒𝑒𝑘
₹120/2$ - 2 𝑤𝑒𝑒𝑘𝑠
₹140/3$ - 3 𝑤𝑒𝑒𝑘𝑠
₹160/4$ - 4 𝑤𝑒𝑒𝑘𝑠
𝑈 𝑊𝐴𝑁𝑇 𝐽𝑈𝑆𝑇 𝐷𝑀 𝑀𝐸 :@fligher""",reply_to_message_id=message.id)
        return
    
    
    if os.path.exists(f'{message.from_user.id}-thumb.jpg'):
        os.remove(f'{message.from_user.id}-thumb.jpg')
        app.send_message(message.chat.id, '**Thumbnail is Removed**',reply_to_message_id=message.id)
    else:
        app.send_message(message.chat.id, '**Thumbnail is not Set**',reply_to_message_id=message.id)


# thumbline
@app.on_message(filters.photo)
def ptumb(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    
    if not checkuser(message):
        app.send_message(message.chat.id, """𝐻𝐸𝐿𝐿𝑂 👋 𝑌𝑂𝑈 𝑁𝐸𝐸𝐷 𝑇𝑂 𝐵𝑈𝑌 𝑆𝑈𝐵𝑆𝐶𝑅𝐼𝑃𝑇𝐼𝑂𝑁 𝑇𝑂 𝑈𝑆𝐸 𝑀𝐸👇\n
𝑇𝐻𝐼𝑆 𝐴𝑅𝐸 𝑀𝑌 𝑃𝐿𝐴𝑁𝑆 
₹80/1$ - 1 𝑤𝑒𝑒𝑘
₹120/2$ - 2 𝑤𝑒𝑒𝑘𝑠
₹140/3$ - 3 𝑤𝑒𝑒𝑘𝑠
₹160/4$ - 4 𝑤𝑒𝑒𝑘𝑠
𝑈 𝑊𝐴𝑁𝑇 𝐽𝑈𝑆𝑇 𝐷𝑀 𝑀𝐸 :@fligher""",reply_to_message_id=message.id)
        return
    
    file = app.download_media(message)
    os.rename(file,f'{message.from_user.id}-thumb.jpg')
    app.send_message(message.chat.id, '**Thumbnail is Set**',reply_to_message_id=message.id)
    

# change mode
@app.on_message(filters.command(["change"]))
def change(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    
    if not checkuser(message):
        app.send_message(message.chat.id, """𝐻𝐸𝐿𝐿𝑂 👋 𝑌𝑂𝑈 𝑁𝐸𝐸𝐷 𝑇𝑂 𝐵𝑈𝑌 𝑆𝑈𝐵𝑆𝐶𝑅𝐼𝑃𝑇𝐼𝑂𝑁 𝑇𝑂 𝑈𝑆𝐸 𝑀𝐸👇\n
𝑇𝐻𝐼𝑆 𝐴𝑅𝐸 𝑀𝑌 𝑃𝐿𝐴𝑁𝑆 
₹80/1$ - 1 𝑤𝑒𝑒𝑘
₹120/2$ - 2 𝑤𝑒𝑒𝑘𝑠
₹140/3$ - 3 𝑤𝑒𝑒𝑘𝑠
₹160/4$ - 4 𝑤𝑒𝑒𝑘𝑠
𝑈 𝑊𝐴𝑁𝑇 𝐽𝑈𝑆𝑇 𝐷𝑀 𝑀𝐸 :@fligher""",reply_to_message_id=message.id)
        return
    
    info = extras.getdata(str(message.from_user.id))
    extras.swap(str(message.from_user.id))
    if info == "V":
        app.send_message(message.chat.id, '__Mode changed from **Video** format to **Document** format__',reply_to_message_id=message.id)
    else:
        app.send_message(message.chat.id, '__Mode changed from **Document** format to **Video** format__',reply_to_message_id=message.id)

        
# multiple links handler
def multilinks(message,links):
    for link in links:
        d = threading.Thread(target=lambda:down(message,link),daemon=True)
        d.start()
        d.join()


# mdisk link in text
@app.on_message(filters.text)
def mdisktext(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    
    if isPremmium and message.chat.id == temp_channel: return

    if not checkuser(message):
        app.send_message(message.chat.id, """𝐻𝐸𝐿𝐿𝑂 👋 𝑌𝑂𝑈 𝑁𝐸𝐸𝐷 𝑇𝑂 𝐵𝑈𝑌 𝑆𝑈𝐵𝑆𝐶𝑅𝐼𝑃𝑇𝐼𝑂𝑁 𝑇𝑂 𝑈𝑆𝐸 𝑀𝐸👇\n
𝑇𝐻𝐼𝑆 𝐴𝑅𝐸 𝑀𝑌 𝑃𝐿𝐴𝑁𝑆 
₹80/1$ - 1 𝑤𝑒𝑒𝑘
₹120/2$ - 2 𝑤𝑒𝑒𝑘𝑠
₹140/3$ - 3 𝑤𝑒𝑒𝑘𝑠
₹160/4$ - 4 𝑤𝑒𝑒𝑘𝑠
𝑈 𝑊𝐴𝑁𝑇 𝐽𝑈𝑆𝑇 𝐷𝑀 𝑀𝐸 :@fligher""",reply_to_message_id=message.id)
        return

    if message.text[0] == "/":
        app.send_message(message.chat.id, '**See __/help__**',reply_to_message_id=message.id)
        return

    if "https://mdisk.me/" in message.text:
        links = message.text.split("\n")
        if len(links) == 1:
            d = threading.Thread(target=lambda:down(message,links[0]),daemon=True)
            d.start()
        else:
            d = threading.Thread(target=lambda:multilinks(message,links),daemon=True)
            d.start()   
    else:
        app.send_message(message.chat.id, '**Send only __MDisk Link__**',reply_to_message_id=message.id)


# polling
app.run()
