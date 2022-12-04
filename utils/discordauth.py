import requests
import json

class Auth():
    def __init__(self, email, password) -> None:
        self.email = email
        self.password = password

    def login(self):
        headers = {
            "Content-Type": "application/json"
        }

        payload = {
            "login": self.email,
            "password": self.password,
        }

        r = requests.post("https://discord.com/api/v9/auth/login", headers=headers, json=payload)
        data = r.json()

        return data["token"]