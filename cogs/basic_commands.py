import discord

from discord.ext import commands

from discord import activity

from discord.commands import Option

import os
import sys

import json

import asyncio as asyncio

import re
import string


from discord.ext import *
from discord.ext.commands import *
from ctypes import *
from datetime import datetime


import inspect
import io
import textwrap
import traceback
import aiohttp
from contextlib import redirect_stdout
from discord.commands import slash_command


import psutil

if os.path.exists(os.getcwd() + "/config.json"):
    
    
    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"userbanned": ""}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f) 

userbanned = configData["userbanned"]






class Basic_Commands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot





	@slash_command(name="info", description="Information about this bot")
	async def info(self, ctx):

            if ctx.author.id in userbanned:
                return await ctx.respond("You have been banned from doing this command!", ephemeral=True)
            else:
                pass
        
            self.bot_embed_guilds = []

            for t in self.bot.guilds:
                self.bot_embed_guilds.append(t)
            embed = discord.Embed(title="Bot Info", description="General information about Profanity Blocker", color=0xD708CC)
            embed.add_field(name="__Bot developers:__", value="User319183#3149\n TheWizz1338#6367\n AnonymousDev#3773", inline=True)
            embed.add_field(name="__Server Count:__", value=f"{len(self.bot_embed_guilds)}", inline=True)
            all_members_embed_list = []
            for x in self.bot.get_all_members():
                all_members_embed_list.append(x)
            embed.add_field(name="__Users being watched for profanity:__", value=f"{len(all_members_embed_list)}")
            embed.add_field(name="__Websocket Ping:__", value=f"{round(self.bot.latency * 1000)}")
            embed.add_field(name="__CPU Usage:__", value = f'{psutil.cpu_percent()}%', inline = False)
            embed.add_field(name="__Memory Usage:__", value = f'{psutil.virtual_memory().percent}%', inline = False)
            embed.timestamp = datetime.utcnow()
            await ctx.respond(embed=embed)














	@commands.Cog.listener()
	async def on_ready(self):
		print('[READY] Cog "Basic_Commands" has been loaded!')
		print(f'---------------------------------------')


def setup(bot):
	bot.add_cog(Basic_Commands(bot))