import discord
from discord import CategoryChannel, option
from discord.ext import commands, tasks

import requests
from aiohttp import request

from format.keys import setuprequests
from format.utils import ansi

from utils.antisniper import antisniper, seraphBlacklist
from utils.deleak import lookup, lookupByUsername
from utils.uuid import usernameToUuid
from utils.socials import disUsernameToID, linkedSocials

url, urlhyp, headers, headershyp = setuprequests()

class Blacklist(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.slash_command(
        name="blacklist",
        description="Blacklist information",
    )
    @option(
        name="ign",description="Ingame name",required=True, option_type=3
    )
    async def wse(self, ctx: discord.ApplicationContext, ign: str):
        uuid = usernameToUuid(ign)

        socials = linkedSocials(uuid)
        disc = socials["DISCORD"]
        if disc is not None:
            discsplit = disc.split("#")
            try:
                discid = discord.utils.get(self.bot.get_all_members(), name=discsplit[0], discriminator=discsplit[1]).id
                deleak = lookup(discid)
            except Exception:
                discid = None
                deleak = lookupByUsername(username=discsplit[0], discriminator=discsplit[1])
        else:
            discid = None
            deleak = None

        qexit = antisniper(uuid=uuid)
        seraph = seraphBlacklist(uuid=uuid)

        for i in qexit["data"]:
            print(i)
            if "queues" in qexit["data"][i]:
                total = qexit["data"][i]["queues"]["total"]
                last48 = qexit["data"][i]["queues"]["last_48_hours"]
                last24 = qexit["data"][i]["queues"]["last_24_hours"]
                last30m = qexit["data"][i]["queues"]["last_30_min"]
                last10m = qexit["data"][i]["queues"]["last_10_min"]

        botter = seraph["bot"]["tagged"]
        blacklist = seraph["blacklist"]["tagged"]
        thread_level = seraph["statistics"]["thread_level"]

        embed = discord.Embed(title=f"Blacklist", description=f"""╰`•` target: **{ign}**
╰`•` discord: **{disc}**
╰`•` discord id: **{discid}**
""", color=discord.Color.from_rgb(47,49,54))

        embed.add_field(name=f"Bedwars queue exit rates",value=f"""```ansi
{ansi(0, 33, 0)}Total\u001b[0m -> {ansi(0, 31, 0)}{total}
{ansi(0, 33, 0)}Last 48 hours\u001b[0m -> {ansi(0, 31, 0)}{last48}
{ansi(0, 33, 0)}Last 24 hours\u001b[0m -> {ansi(0, 31, 0)}{last24}    
{ansi(0, 33, 0)}Last 30 minutes\u001b[0m -> {ansi(0, 31, 0)}{last30m}
{ansi(0, 33, 0)}Last 10 minutes\u001b[0m -> {ansi(0, 31, 0)}{last10m}                              
```        
""", inline=False)

        embed.add_field(name=f"Seraph Blacklist v4", value=f"""```ansi
{ansi(0, 33, 0)}Bot\u001b[0m -> {ansi(0, 31, 0)}{botter}
{ansi(0, 33, 0)}Blacklist\u001b[0m -> {ansi(0, 31, 0)}{blacklist}
{ansi(0, 33, 0)}Thread level\u001b[0m -> {ansi(0, 31, 0)}{thread_level}                              
```        
""", inline=False)

        if deleak is not None:
            owned = ', '.join(deleak["owned"])
            wins = deleak["wins"]
            usernames = ', '.join(deleak["usernames"])
            embed.add_field(name=f"Botter! (data before 9-28-2022)", value=f"""```ansi
{ansi(0, 33, 0)}Bots owned\u001b[0m -> {ansi(0, 31, 0)}{owned}
{ansi(0, 33, 0)}Botted wins\u001b[0m -> {ansi(0, 31, 0)}{wins}
{ansi(0, 33, 0)}On usernames\u001b[0m -> {ansi(0, 31, 0)}{usernames}                              
```        
""", inline=False)

        embed.set_footer(text='Cryme • v2.0')
        embed.set_thumbnail(url="https://iili.io/Hf7Ovun.th.png")
        await ctx.respond(embed=embed)