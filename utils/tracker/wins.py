import requests
import time
from datetime import datetime

import json
from jsondiff import diff

from format.keys import setuprequests
url, urlhyp, headers, headershyp = setuprequests()

class ForceEnd(Exception): pass
 
def duels(uuid: str, speed: int):
    while True:
        try:
            r1 = requests.get(f"{urlhyp}/player?uuid={uuid}", headers = headershyp)
            data1 = r1.json()
            wins1 = data1["player"]["stats"]["Duels"]["wins"]
            losses1 = data1["player"]["stats"]["Duels"]["losses"]

            time.sleep(2)
            r2 = requests.get(f"{urlhyp}/player?uuid={uuid}", headers = headershyp)
            data2 = r2.json()
            wins2 = data2["player"]["stats"]["Duels"]["wins"]
            losses2 = data2["player"]["stats"]["Duels"]["losses"]

            wins = diff(wins1, wins2)
            losses = diff(losses1, losses2)
            if bool(wins):
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                yield current_time, "WIN"
            if bool(losses):
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                yield current_time, "LOSS"
        except ForceEnd:
            break