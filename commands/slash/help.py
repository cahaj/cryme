import discord
from discord import CategoryChannel, option
from discord.ext import commands, tasks

class Help(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.slash_command(
    name="help",
    description="Shows the list of availible commands",
)
    async def help(self, ctx):
        embeds = []
        embed = discord.Embed(title=f"List of commands")
        embed.set_author(name=f"v2", url=f"https://www.instagram.com/mr_rohland/", icon_url=f"https://i.pinimg.com/originals/bc/15/94/bc15940e31cd4e402dd50cbdba3503db.png")
        embed.add_field(name="v, i, version, info", value="Displays basic information about the bot", inline=False)
        embed.add_field(name="/wse {ign}", value="Winstreak estimation for specified player", inline=False)
        embed.add_field(name="/dn {nick}", value="Denicks targeted nick if its in database", inline=False)
        embed.add_field(name="/fdn {number}", value="Finds players that have specified number of final kills and could be possibly nicked", inline=False)
        embed.add_field(name="/bdn {number}", value="IN THE MAKING", inline=False)
        embed.add_field(name="/fn {ign}", value="Finds targeted players nick if its in database", inline=False)
        embed.add_field(name="/tablist {ign} {number}", value="Gets list of players that have been in the targets last specified number of games more than once. Used to find possible party members.", inline=False)
        embed.add_field(name="/track {ign}", value="Tracks live player activity with little to no delay (currently works only with hypixel status api).", inline=False)
        embed.add_field(name="/stop", value="Stops tracking process.", inline=False)
        await ctx.respond(embed=embed)