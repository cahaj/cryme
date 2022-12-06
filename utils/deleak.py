import json

def lookup(discordID):
    with open("misc/DEUsers_9-28-2022.json", "r", encoding='utf-8') as f:
        db = json.load(f)
    
    for i in db:
        if "discId" in i:
            if i["discId"] == discordID:
                return i
