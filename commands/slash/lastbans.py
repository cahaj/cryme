import discord
from discord import CategoryChannel, option
from discord.ext import commands, tasks

import time
import datetime
import os

from utils.daisuki import lastbans

class LastBans(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.slash_command(
    name="lastbans",
    description="Shows recently banned players",
)
    @option(
            name="range",description="Lookup range",required=True, option_type=3
        )
    async def banchceck(self, ctx, range:int):

        st = time.time()

        msg = ""
        bans = lastbans(range)
        for i in bans:
            ign = i["ign"]
            unix = i["unix"]
            msg = msg + f"""╰`•` **{ign}** -> {unix}\n"""


        et = time.time()
        elapsed_time = et - st

        if len(msg) <= 4096:
            embed = discord.Embed(title=f"Recent bans lookup", description=f"""╰`•` range: **{range}**

{msg}
""", color=discord.Color.from_rgb(47,49,54))
            embed.set_thumbnail(url="https://iili.io/Hf7Ovun.th.png")
            embed.add_field(name=f"Time taken", value=f"""```{elapsed_time}```""", inline=False)
            embed.set_footer(text='Cryme • v2.0')
            await ctx.respond(embed=embed)

        else:
            longmsg = ""
            for i in bans:
                ign = i["ign"]
                unix = i["unix"]
                if unix is not None:
                    unix = unix.replace('<t:', '')
                    unix = unix.replace(':R>', '')
                    unix = int(unix)
                    longmsg = longmsg + f"[{datetime.datetime.fromtimestamp(unix)}] => {ign}\n"
                else:
                    longmsg = longmsg + f"[Manually added] => {ign}\n"
            print("larger")
            embed = discord.Embed(title=f"Recent bans lookup", description=f"╰`•` range: **{range}**", color=discord.Color.from_rgb(47,49,54))
            embed.set_thumbnail(url="https://iili.io/Hf7Ovun.th.png")
            await ctx.respond(embed=embed)

            with open("commands/slash/bancheck/result.txt", "xt", encoding='utf-8') as file:
                file.write(longmsg)
        
            await ctx.send(file=discord.File("commands/slash/bancheck/result.txt"))
            os.remove("commands/slash/bancheck/result.txt")
            embed = discord.Embed(title=f"Finished", color=discord.Color.from_rgb(47,49,54))
            embed.add_field(name=f"Time taken", value=f"""```{elapsed_time}```""", inline=False)
            embed.set_footer(text='Cryme • v2.0')
            await ctx.respond(embed=embed)