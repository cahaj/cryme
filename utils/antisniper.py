import requests

from format.keys import setuprequests

url, urlhyp, headers, headershyp = setuprequests()

urlseraph = "https://antisniper.seraph.si/api/v4/"
headersseraph = {
    "run-api-key": "public",
    "Content-Type": "application/json"
}

def seraphBlacklist(uuid):
    r = requests.get(f"{urlseraph}/blacklist?uuid={uuid}", headers=headersseraph)
    data = r.json()
    if data["success"] == True:
        return data["data"]
    else:
        raise Exception(f"{r.status_code}: {data}")

def antisniper(uuid):
    r = requests.get(f"{url}/antisniper?uuid={uuid}", headers=headers)
    data = r.json()
    return data