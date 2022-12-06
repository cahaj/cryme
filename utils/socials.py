import requests


from format.headers import setuprequests

url, urlhyp, headers, headershyp = setuprequests()

def linkedSocials(uuid: str):
    r = requests.get(f"https://api.slothpixel.me/api/players/{uuid}", headers=headershyp)
    data = r.json()
    if r.status_code == 200:
        return data["links"]
    else:
        raise Exception(f"{r.status_code}: {data}")

def linkedToDiscord(name: str, number: int):
    r = requests.get(f"{url}/discord/query?name={name}&number={number}", headers=headers)
    data = r.json()
    if r.status_code == 200:
        return data["results"]
    else:
        raise Exception(f"{r.status_code}: {data}")

def disUsernameToID(discord, bot, name: str, number: int):
    return discord.utils.get(bot.get_all_members(), name=name, discriminator=str(number)).id