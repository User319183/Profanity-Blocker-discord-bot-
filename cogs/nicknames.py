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
import datetime

from discord import Message

import aiohttp








import os  
import discord  
from discord.ext import commands



with open(".txt/basefilter.txt", encoding="utf8") as file:
    nick = file.read().split('\n')

nick = tuple(nick)


class nicknames(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



 






    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if after.display_name in (nick):
            await after.edit(nick=f'Inappropriate Name')

 
 
 


    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.name in (nick):
            await member.edit(nick=f'Inappropriate Name')




    @commands.Cog.listener()
    async def on_ready(self):
        print('[READY] Cog "nicknames" has been loaded!')
        print(f'---------------------------------------')            
                    

    
def setup(bot):
    bot.add_cog(nicknames(bot))