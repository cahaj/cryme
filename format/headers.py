import json

def setuprequests():
    with open("keys/keys.json", "r") as f:
        json_object = json.load(f)
    key = json_object["antisniper"]
    keyhyp = json_object["hypixel"]

    headers = {
    "Apikey": key,
    "Content-Type": "application/json"}
    headershyp = {
    "API-KEY": keyhyp,
    "Content-Type": "application/json"}

    return "https://api.antisniper.net", "https://api.hypixel.net", headers, headershyp