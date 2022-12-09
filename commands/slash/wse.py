import discord
from discord import CategoryChannel, option
from discord.ext import commands, tasks

import requests
from aiohttp import request

from format.keys import setuprequests

from format.utils import ansi

url, urlhyp, headers, headershyp = setuprequests()

class Wse(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.slash_command(
        name="wse",
        description="Winstreak estimation",
    )
    @option(
        name="ign",description="Ingame name",required=True, option_type=3
    )
    async def wse(self, ctx: discord.ApplicationContext, ign: str):
        ignLOW = ign.lower()
        try:
            embeds = []
            async with request("POST", f"{url}/winstreak", headers = headers, json =  {'igns': [f'{ignLOW}']}) as response:
                data = await response.json()
                uuidconvert = requests.get(f"{url}/convert?name={ignLOW}", headers = headers)
                getuuid = uuidconvert.json()
                uuid = getuuid[f'{ignLOW}']
                if uuid == None:
                    embed = discord.Embed(title=f"Winsteak estimation", description=f"╰`•` target: **{ign}**", color=discord.Color.from_rgb(47,49,54))
                    embed.add_field(name=f"ERROR",value=f"This is not a registered player.")
                    embed.set_footer(text='Cryme • v2.0')
                    embed.set_thumbnail(url="https://iili.io/Hf7Ovun.th.png")
                    await ctx.respond(embed=embed)
                if uuid is not None:
                    try:
                        overall_ws = data["data"]["uuids"][uuid]["data"]["overall_winstreak"]
                        fourvfour_ws = data["data"]["uuids"][uuid]["data"]["two_four_winstreak"]
                        solo_ws = data["data"]["uuids"][uuid]["data"]["eight_one_winstreak"]
                        doubles_ws = data["data"]["uuids"][uuid]["data"]["eight_two_winstreak"]
                        trio_ws = data["data"]["uuids"][uuid]["data"]["four_three_winstreak"]
                        squad_ws = data["data"]["uuids"][uuid]["data"]["four_four_winstreak"]
                        embed = discord.Embed(title=f"Winsteak estimation", description=f"╰`•` target: **{ign}**", color=discord.Color.from_rgb(47,49,54))
                        embed.add_field(name=f"**BEDWARS**", value=f"""```ansi
{ansi(0, 33, 0)}Overall\u001b[0m -> {ansi(0, 31, 0)}{overall_ws}                      
{ansi(0, 33, 0)}Solos\u001b[0m -> {ansi(0, 31, 0)}{solo_ws}
{ansi(0, 33, 0)}Doubles\u001b[0m -> {ansi(0, 31, 0)}{doubles_ws}
{ansi(0, 33, 0)}Trios\u001b[0m -> {ansi(0, 31, 0)}{trio_ws}
{ansi(0, 33, 0)}4v4v4v4\u001b[0m -> {ansi(0, 31, 0)}{squad_ws}
{ansi(0, 33, 0)}4v4\u001b[0m -> {ansi(0, 31, 0)}{fourvfour_ws}
```
""", inline=False)
                        embed.set_footer(text='Cryme • v2.0')
                        embed.set_thumbnail(url="https://iili.io/Hf7Ovun.th.png")
                        await ctx.respond(embed=embed)
                    except:
                        if data["data"]["no_winstreak_data"][uuid]["ign_lower"] is not None:
                            embed = discord.Embed(title=f"Winsteak estimation", description=f"╰`•` target: **{ign}**", color=discord.Color.from_rgb(47,49,54))
                            embed.add_field(name=f"ERROR",value=f"No data found")
                            embed.set_footer(text='Cryme • v2.0')
                            embed.set_thumbnail(url="https://iili.io/Hf7Ovun.th.png")
                            await ctx.respond(embed=embed)
        except Exception as e:
            await ctx.send(f"""Internal error.
    Exception: `{e}`""")