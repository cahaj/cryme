import requests
import json
from pprint import pprint

from keys.discordauth import Auth

with open("keys/selflogins.json", "r") as f:
    json_object = json.load(f)

email = json_object["email"]
password = json_object["password"]

def format(content):
    content = content.replace('**', '')
    content = content.replace('`', '')
    content = content.replace('(', '')
    content = content.replace(')', '')
    content = content.replace('\n ', '')
    content = content.split()

    for i in content:
        if i in ["[VIP]", "[VIP+]", "[MVP]", "[MVP+]", "[MVP++]"]:
            content.remove(i)
        elif "manually" in i:
            content[5] = None
            content[7] = content[len(content)-1]

    content = {"ign": f"{content[0]} {content[1]}", "uuid": content[7], "unix": content[5]}

    return content

def lastbans(limit:int):
    if limit > 9999:
        raise ValueError("Limit higher than is 999 not supported")

    if limit > 999:
        times = int(str(limit)[:2])
    else:
        times = int(str(limit)[:1])


    auth = Auth(email, password)
    token = auth.login()

    headers = {
        "authorization": token
    }

    msges = []

    if limit <= 100:
        r = requests.get(f"https://discord.com/api/v9/channels/1028897716073402418/messages?limit={limit}", headers=headers)
        data = r.json()

        for msg in data:
            if msg["author"]["id"] == "1025367957712416768":
                content = msg["content"]
                msges.append(format(content))

    else:
        last2 = int(str(limit)[-2:])

        r1 = requests.get(f"https://discord.com/api/v9/channels/1028897716073402418/messages?limit=100", headers=headers)
        data1 = r1.json()
        
        for msg in data1:
            if msg["author"]["id"] == "1025367957712416768":
                content = msg["content"]
                msges.append(format(content))

        lastmsg = data1[-1]["id"]

        for n in range(times-1):
            r = requests.get(f"https://discord.com/api/v9/channels/1028897716073402418/messages?before={lastmsg}&limit=100", headers=headers)
            data = r.json()

            for msg in data:
                if msg["author"]["id"] == "1025367957712416768":
                    content = msg["content"]
                    msges.append(format(content))

            lastmsg = data[-1]["id"]
        
        if last2 != 0:
            r2 = requests.get(f"https://discord.com/api/v9/channels/1028897716073402418/messages?before={lastmsg}&limit={last2}", headers=headers)
            data2 = r2.json()

            for msg in data2:
                if msg["author"]["id"] == "1025367957712416768":
                    content = msg["content"]
                    msges.append(format(content))

    return msges



