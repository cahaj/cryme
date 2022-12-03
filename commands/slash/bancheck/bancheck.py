import discord
from discord import CategoryChannel, option
from discord.ext import commands, tasks

import time
import datetime
import os
import json

import requests

from commands.slash.bancheck.daisuki import lastbans
from format.headers import setuprequests
from format.utils import ansi
from utils.uuid import usernameToUuid
from pprint import pprint

url, urlhyp, headers, headershyp = setuprequests()

class BanCheck(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.slash_command(
    name="bancheck",
    description="Tries to tell if a given player is banned",
)
    @option(
            name="ign",description="In game name of a given player",required=True, option_type=3
        )
    async def banchceck(self, ctx: discord.ApplicationContext, ign: str):
        r = requests.get(f"{urlhyp}/player?uuid={usernameToUuid(ign)}", headers=headershyp)
        data = r.json()
        with open("misc/testdump.json", "w") as f:
            json.dump(data, f)

        try:
            llunix = str(data["player"]["lastLogin"])
            llunix = int(llunix[:len(llunix) - 3])
            lastlogin = f"<t:{llunix}:R>"
        except:
            lastlogin = "No data"

        embed = discord.Embed(title=f"Ban check", description=f"""╰`•` target: **{ign}**""", color=discord.Color.from_rgb(47,49,54))
        embed.add_field(name="Last login", value=lastlogin, inline=False)
        embed.add_field(name="Ban logs", value="Scraping...", inline=False)
        embed.set_footer(text='Cryme • v2.0')
        embed.set_thumbnail(url="https://iili.io/Hf7Ovun.th.png")
        await ctx.respond(embed=embed)


        r = requests.get(f"{urlhyp}/player?uuid={usernameToUuid(ign)}", headers=headershyp)
        data = r.json()

        latestbans = lastbans(999)
        print(len(latestbans))
        bans = []
        for i in latestbans:
            split = i["ign"].split()
            if split[1] == ign:
                print(i)
                bans.append(i)

        dmsg = ""
        print(len(bans))
        print(bans)
        if len(bans) < 1:
            dmsg = f"No data"
        else:
            for i in bans:
                unix = i["unix"]
                if unix is not None:
                    dmsg = dmsg + f"╰`•` {unix}\n"
                else:
                    dmsg = dmsg + f"╰`•` Manually added, time unknown\n"


        embed = discord.Embed(title=f"Ban check", description=f"""╰`•` target: **{ign}**""", color=discord.Color.from_rgb(47,49,54))
        embed.add_field(name="Last login", value=lastlogin, inline=False)
        embed.add_field(name="Ban logs", value=dmsg, inline=False)
        embed.set_footer(text='Cryme • v2.0')
        embed.set_thumbnail(url="https://iili.io/Hf7Ovun.th.png")
        await ctx.edit(embed=embed)