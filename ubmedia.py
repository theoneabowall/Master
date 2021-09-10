from pyrogram import Client
from pyrogram import filters
from apscheduler.schedulers.background import BackgroundScheduler


import os
from os import getenv
from pyrogram.types.messages_and_media import message



#---------------------------------+ heroku
api_id = int(getenv("API_ID"))
api_hash = getenv("API_HASH")
string = getenv("SESSION_STRING")
g_time = int(getenv("GROUP_DELETE_TIME"))
c_time = int(getenv("CHANNEL_DELETE_TIME"))

#---------------------------------+ Data
api_id= api_id 
api_hash= api_hash 
string = string 
group = -1001241414282
channel = -1001179102851
#------------------------------------end
idss = []


ub = Client(string, api_id=api_id, api_hash=api_hash, sleep_threshold=60)

    
    
def clean_data():
    print("checking media")
    for ids in ub.search_messages(chat_id=group, filter="photo_video", limit=20):
        msg_id = ids.message_id
        idss.append(msg_id)
        ub.copy_message(chat_id=channel, from_chat_id=group, message_id=msg_id)
        ub.delete_messages(chat_id=group, message_ids=msg_id)
    else:
        if len(idss) == 0:
            print("no photos to delete")
            return
        else:
            c = len(idss)
            print(f"cleared almost {c} messages")
            idss.clear() 

    for ids in ub.search_messages(chat_id=group, filter="document", limit=5):
        msg_id = ids.message_id
        idss.append(msg_id)
        ub.copy_message(chat_id=channel, from_chat_id=group, message_id=msg_id)
        ub.delete_messages(chat_id=group, message_ids=msg_id)
    else:
        if len(idss) == 0:
            print("no photos to delete")
            return
        else:
            c = len(idss)
            print(f"almost {c} files deleted")
            idss.clear()     

def channel_delete():
    print("trying to delete channel messages")
    for ids in ub.search_messages(chat_id=channel, filter="photo_video"):
        msg_id = ids.message_id
        idss.append(msg_id)
        ub.delete_messages(chat_id=channel, message_ids=msg_id)
    else:
        if len(idss) == 0:
            print("no photos to delete")
            return
        else:
            c = len(idss)
            print(f"almost {c} files deleted")
            idss.clear() 

    for ids in ub.search_messages(chat_id=channel, filter="document", limit=5)
        msg_id = ids.message_id
        idss.append(msg_id)
        ub.delete_messages(chat_id=channel, message_ids=msg_id)
    else:
        if len(idss) == 0:
            print("no files to delete")
            return
        else:
            c = len(idss)
            print(f"almost {c} files deleted")
            idss.clear()  
    
scheduler = BackgroundScheduler(timezone="Asia/Kolkata")
scheduler.add_job(clean_data, 'interval' , seconds=g_time)


scheduler.start()   

scheduler = BackgroundScheduler(timezone="Asia/Kolkata")
scheduler.add_job(channel_delete, 'interval' , minutes=c_time)


scheduler.start()  





ub.run()
