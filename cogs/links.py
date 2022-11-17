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


import pytesseract
import io
import pytesseract as tess
import requests
from PIL import Image
from PIL import ImageFilter








    
    
    
if os.path.exists(os.getcwd() + "/config.json"):
    
    
    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"basic_premium": ""}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f) 

basic_premium = configData["basic_premium"]
                

            



with open(".txt/basefilterlinks.txt") as file:
    links = file.read().split('\n')
    









import os  
import discord  
from discord.ext import commands

class Links(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
    @commands.Cog.listener()
    async def on_message(self, message:Message):

        if message.guild.id in basic_premium:
        


            message.content = message.content.lower()
            message.content = discord.utils.remove_markdown(message.content)

            guild = message.guild
            bypassedRole = discord.utils.get(guild.roles, name="Bypassed")
        
            if message.author.bot:
                return
            
            
            try:
                if "Bypassed" in message.channel.topic:
                    return
                        
            except:
                pass



            if bypassedRole in message.author.roles:
                return

            for word in links:
                if message.content.count(word) > 0:
                    await message.delete()
                    embed = discord.Embed(title="Message Deleted", color=0xD708CC, description= f"{message.author.mention} You're not allowed to say that.")
                    embed.timestamp = discord.utils.utcnow()
                    await message.channel.send(embed=embed, delete_after=10)                 


 
 










    @commands.Cog.listener()
    async def on_ready(self):
        print('[READY] Cog "LINKS" has been loaded!')
        print(f'---------------------------------------')            
                    

    
def setup(bot):
    bot.add_cog(Links(bot))