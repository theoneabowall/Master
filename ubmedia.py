#Dangerprobot
from pyrogram import Client,filters
from collections.abc import MutableMapping
from apscheduler.schedulers.background import BackgroundScheduler
import os
from os import getenv
from pyrogram.types.messages_and_media import message



#---------------------------------+ heroku
api_id_pyrogram = int(getenv("API_ID"))
api_hash_pyrogram = getenv("API_HASH")
string_pyrogram = getenv("SESSION_STRING")
g_time = int(getenv("GROUP_DELETE_TIME"))
c_time = int(getenv("CHANNEL_DELETE_TIME"))
group = int(getenv("GROUP_ID"))
channel = int(getenv("CHANNEL_ID"))

#---------------------------------+ Data
api_id= api_id_pyrogram 
api_hash= api_hash_pyrogram 
session_string= string_pyrogram 
group = -1002120547379
channel = -1002025718840
#------------------------------------end
idss = []


app = Client(name="auto-delete",session_string =string_pyrogram, api_id=api_id_pyrogram, api_hash=api_hash_pyrogram, sleep_threshold=60)

    
    
def clean_data():
    print("checking media")
    idss = []
    for message in app.search_messages(chat_id=group, filter=filter.media, limit=20):
        msg_id = message.message.id
        idss.append(msg_id)
        app.copy_message(chat_id=channel, from_chat_id=group, message_id=msg_id)
        app.delete_messages(chat_id=group, message_ids=msg_id)
    try:
        if len(idss) == 0:
            print("no photos to delete")
            return
        else:
            c = len(idss)
            print(f"cleared almost {c} messages")
            idss.clear() 
    except Exception as e:
        print(e) 


def channel_delete():
    print("trying to delete channel messages")
    for message in app.search_messages(chat_id=channel, filter="media"):
        msg_id = message.message.id
        idss.append(msg_id)
        app.delete_messages(chat_id=channel, message_ids=msg_id)
    try:
        if len(idss) == 0:
            print("no photos to delete")
            return
        else:
            c = len(idss)
            print(f"almost {c} files deleted")
            idss.clear() 
    except Exception as e:
        print(e)
    
    
scheduler = BackgroundScheduler(timezone="Asia/Kolkata")
scheduler.add_job(clean_data, 'interval' , seconds=g_time)


scheduler.start()   

scheduler = BackgroundScheduler(timezone="Asia/Kolkata")
scheduler.add_job(channel_delete, 'interval' , minutes=c_time)


scheduler.start()  





app.run()
