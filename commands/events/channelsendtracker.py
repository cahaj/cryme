import discord
from discord import CategoryChannel, option
from discord.ext import commands, tasks

import threading
import json
import asyncio

import requests

from format.keys import setuprequests
from format.utils import ansi
from utils.uuid import usernameToUuid
from utils.tracker.wins import duels, ForceEnd

class Tracker(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    async def sendduels(self, ctx, username, speed):
        wins = duels(uuid=usernameToUuid(username), speed=speed)
        for i in wins:
            time, status = i
            if status == "WIN":
                await ctx.channel.send(f":small_blue_diamond: `{username}` just **WON** a game of **DUELS**")
            if status == "LOSS":
                await ctx.channel.send(f":small_orange_diamond: `{username}` just **LOST** a game of **DUELS**")

    @commands.slash_command(
    name="start",
    description="start",
)
    @option(
            name="prompt",description="prompt",required=True, option_type=3
        )
    async def start(self, ctx: discord.ApplicationContext, prompt: str):
        if ctx.author.id == 673799940560125952:
            if prompt == "duels":
                #try:
                    with open("misc/tracklist.json", "r") as f:
                        tracklist = json.load(f)
                    for i in tracklist:
                        await self.sendduels(ctx=ctx, username=i, speed=6)


                #except Exception as e:
                #    print(e)
                #    await ctx.channel.send("Exception occured, stopping")
                #    self.run.off()
            else:
                await ctx.respond("Invalid argument", hidden=True)
        else:
            await ctx.respond("No permissions", hidden=True)

    @commands.slash_command(
    name="stop",
    description="stop",
)
    @option(
            name="prompt",description="prompt",required=True, option_type=3
        )
    async def stop(self, ctx: discord.ApplicationContext, prompt: str):
        if ctx.author.id == 673799940560125952:
            if prompt == "duels":
                await ctx.respond("Stopping...")
                raise ForceEnd()
            else:
                await ctx.respond("Invalid argument", hidden=True)
        else:
            await ctx.respond("No permissions", hidden=True)