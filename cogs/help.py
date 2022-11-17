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

import random
import uuid

from discord.commands import slash_command # Importing the decorator that makes slash commands.




if os.path.exists(os.getcwd() + "/config.json"):
    
    
    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"userbanned": ""}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f) 

userbanned = configData["userbanned"]






class Help_Commands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot






	@slash_command(name="help", description="Default help panel")
	async def help(self, ctx):

            if ctx.author.id in userbanned:
                return await ctx.respond("You have been banned from doing this command!", ephemeral=True)
            else:
                pass
            
		
            embed=discord.Embed(title="Help Panel", color=0xD708CC, description = "The command you need for help.", url="https://discord.gg/ecz2z36gkB")
            embed.add_field(name = "Commands", value = f"__1. info__ \n __2. helpme__ \n __3. bypass__ \n __4. unbypass__ \n ")
            embed.timestamp = datetime.utcnow()
            await ctx.respond(embed=embed)






	@commands.Cog.listener()
	async def on_ready(self):
		print('[READY] Cog "Help_Commands" has been loaded!')
		print(f'---------------------------------------')


def setup(bot):
	bot.add_cog(Help_Commands(bot))
	