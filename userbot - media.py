from pyrogram import Client
from pyrogram import filters
from apscheduler.schedulers.background import BackgroundScheduler

#---------------------------------+ Data
api_id=5282591
api_hash='d416fe4e323d0e2b4616fef68a8ddd63'
string = "AQCuTNr7BMHjwi7ZHLsl-zcSsLOhzbl0Onn_Tw-88oU-iGoEPllbOxlU0wEnlwAoFosK6ROAxqtUsZYbytf-M6z2aLRmgso48t6IHnLIOthU-oZHQjNtEQ1QA38TvY7c_kTEUBueYdWZ8LzcshYdQ5C97t2IdvLMQROBxzuufm6-ngVVdQhKHaFkagy7ljJWjhAitXy58jgMavVR0b4bOF7j0P4sPQtr2OjBTOtUrnn4WGmTDjjTWKamSQMg-WW_1547LXac_145Ss8xXM7EKfXtFKnP847kYWNzLEQwCW9OiyvVlhFEYjvXeTtvA5RJpjCgYBkeK2oYZG0PxJ9DiQx3QSNu3gA"
#------------------------------------end
idss = []
channel = -1001390839405

ub = Client(string, api_id=api_id, api_hash=api_hash, sleep_threshold=60)

    
    
def clean_data():
    print("checking media")
    for ids in ub.search_messages(chat_id=-1001241414282, filter="photo_video", limit=20):
        msg_id = ids.message_id
        idss.append(msg_id)
        ub.copy_message(chat_id=channel, from_chat_id=-1001241414282, message_id=msg_id)
        ub.delete_messages(chat_id=-1001241414282, message_ids=msg_id)
    else:
        if len(idss) == 0:
            print("no photos to delete")
            return
        else:
            c = len(idss)
            print(f"cleared almost {c} messages")
            idss.clear() 

    for ids in ub.search_messages(chat_id="acd321", filter="document", limit=5):
        msg_id = ids.message_id
        idss.append(msg_id)
        ub.copy_message(chat_id=channel, from_chat_id=-1001241414282, message_id=msg_id)
        ub.delete_messages(chat_id=-1001241414282, message_ids=msg_id)
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

    for ids in ub.search_messages(chat_id=channel, filter="document", limit=5):
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
    
scheduler = BackgroundScheduler()
scheduler.add_job(clean_data, 'interval' , seconds=15)


scheduler.start()   

scheduler = BackgroundScheduler()
scheduler.add_job(channel_delete, 'interval' , minutes=5)


scheduler.start()  





ub.run()