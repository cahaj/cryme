import requests
import asyncio
from aiohttp import request

import datetime

import discord
from discord import CategoryChannel, option
from discord.ext import commands, tasks

import json
from jsondiff import diff

from commands.cmds import setup

from format.utils import ansi, ansireset

bot = commands.Bot(command_prefix = ':')
bot.remove_command('help')
setup(bot)

@bot.event
async def on_ready():
    print('Bot online.')
    servers = str(len(bot.guilds))
    print(f"In: {servers} servers.")
    await bot.change_presence(activity=discord. Activity(type=discord.ActivityType.playing, name=f'v2'))

@bot.slash_command(
    name="test",
    description="test",
)
async def help(ctx):
    embed = discord.Embed(title=f"Winsteak estimation", description="╰`•` target: **azurim**", color=discord.Color.from_rgb(47,49,54))
    embed.add_field(name=f"**BEDWARS**", value=f"""```ansi
{ansi(0, 33, 0)}Solos\u001b[0m -> {ansi(0, 31, 0)}0
{ansi(0, 33, 0)}Doubles\u001b[0m -> {ansi(0, 31, 0)}4
{ansi(0, 33, 0)}Trios\u001b[0m -> {ansi(0, 31, 0)}2
{ansi(0, 33, 0)}Fours\u001b[0m -> {ansi(0, 31, 0)}8
```
""", inline=False)
    embed.set_footer(text='Cryme • v2.0')
    embed.set_thumbnail(url="https://iili.io/Hf7Ovun.th.png")
    await ctx.respond(embed=embed)


with open("keys/token.txt", "r") as f:
    token = f.read()

bot.run(token)