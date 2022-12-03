import requests

def uuidToUsername(uuid:str):
    r = requests.get(f"https://sessionserver.mojang.com/session/minecraft/profile/{uuid}")
    data = r.json()
    return data["name"]

def usernameToUuid(username:str):
    r = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}")
    data = r.json()
    return data["id"]