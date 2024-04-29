

import asyncio
import re
from pyrogram import Client
from pyrogram.errors import FloodWait
import os
from progressFun import print_progress

app = Client("my_account")
TARGET = -1002081762571
chat_id=-1002131315760


async def main():
    async with app:
        try:
            if os.path.exists('cache.txt') !=True:
                with open("cache.txt", "w+") as file: 
                    file.write("0")
                    file.close()

            channel = await app.get_chat(TARGET) # geting channel info 

            print(f"Channel Name : {channel.title}")
            print(f"Channel ID : {channel.id}")
            print(" ")

            mess=[ message async for message in app.get_chat_history(TARGET)] # storing message in list
           
            MessageProgress=len(mess)

            lastid=int(open("cache.txt","r").read())
            
            for i,message in enumerate(reversed(mess)): # reverse the data 
                # print_progress(i,MessageProgress)
                if lastid <=i:
                    if message.text!=None:
                       await app.send_message(chat_id,text=message.text,entities=message.entities)

                    elif message.video!=None:
                        file_id=message.video.file_id
                        file_name=message.video.file_name
                        if message.video.thumbs!=None:
                            thumbs=message.video.thumbs[0].file_id
                            if message.caption != None:
                                caption=message.caption.replace("\nYOUTUBE LINK :- CLICK HERE\n",'').replace("HOW TO OPEN LINK :- CLICK HERE","")
                            else:
                                caption=None
                        else:
                            thumbs=None
                        await app.send_video(chat_id,file_id,caption=caption,thumb=thumbs,file_name=file_name,caption_entities=message.entities)


                    elif message.document!=None:
                        file_id=message.document.file_id
                        if message.document.thumbs!=None:
                            thumbs=message.document.thumbs[0].file_id
                            if message.caption!=None:
                                caption=message.caption
                            else:
                                caption=None
                        else:
                            thumbs=None
                        
                        await app.send_document(chat_id,file_id,thumb=thumbs,caption=caption)
                    
                    elif message.sticker!=None:
                        file_id=message.sticker.file_id
                        await app.send_sticker(chat_id,file_id)
                        
                    with open("cache.txt", "w+") as file: 
                        file.write(str(i))
                        file.close()

            await app.stop()
            await os.remove("cache.txt")
        except FloodWait as e:
            await asyncio.sleep(e.value) 


app.run(main())