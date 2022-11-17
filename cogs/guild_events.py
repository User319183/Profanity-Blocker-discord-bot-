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














if os.path.exists(os.getcwd() + "/config.json"):
    
    
    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"serverbanned": ""}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f) 

serverbanned = configData["serverbanned"]




if os.path.exists(os.getcwd() + "/config.json"):
    
    
    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"userbanned": ""}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f) 

userbanned = configData["userbanned"]


class guild_events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot





 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        if str(guild.owner) in userbanned:
            await guild.leave()
            
        else:
            async for entry in guild.audit_logs(action=discord.AuditLogAction.bot_add, limit = 1):
                if entry.user.id in userbanned:
                    await guild.leave()
                    
 
 
 
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        if guild.id in serverbanned:
            await guild.leave()








    @commands.Cog.listener()
    async def on_message(self, message:Message):
        if message.guild.id in serverbanned:
            await message.guild.leave()





            



 
 
 
 
 



    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        if guild.id in serverbanned:
            return
        
        else:
            
            async for entry in guild.audit_logs(action=discord.AuditLogAction.bot_add, limit = 1):
                channel = self.bot.get_channel(888570275426340905)


            
                total_users = len(guild.members)
                total_bots = len([member for member in guild.members if member.bot == True])
                total_humans = total_users - total_bots

                e = discord.Embed(title="I've joined a server.", color= 3447003)
                e.add_field(name="Server Name:", value=guild.name, inline=False)
                e.add_field(name="Guild ID", value=guild.id, inline=False)
                e.add_field(name="Guild Owner", value=str(guild.owner), inline=False) 
                e.add_field(name="Bot Inviter", value=f"({entry.user})\n({entry.user.id})\n{entry.user.mention}")
                e.add_field(name="Guild Users", value="{}".format(total_users))
                e.add_field(name="Humans", value=total_humans)
                e.add_field(name="Bots", value=total_bots)
                try:
                    e.set_thumbnail(url=guild.icon.url)

                except:
                    pass

                    
                e.timestamp = datetime.datetime.utcnow()

                await channel.send(embed=e)

 
 
 




    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        
        if guild.id in serverbanned:
            return
        
        else:
            
                channel = self.bot.get_channel(888570303930839100)

                total_users = len(guild.members)
                total_bots = len([member for member in guild.members if member.bot == True])
                total_humans = total_users - total_bots

                e = discord.Embed(title="I've left a server.", color=15158332)
                e.add_field(name="Server Name:", value=guild.name, inline=False)
                e.add_field(name="Guild ID", value=guild.id, inline=False)
                e.add_field(name="Guild Owner", value=str(guild.owner), inline=False)
                e.add_field(name="Guild Users", value="{}".format(total_users))
                e.add_field(name="Humans", value=total_humans)
                e.add_field(name="Bots", value=total_bots)
                try:
                    e.set_thumbnail(url=guild.icon.url)

                except:
                    pass

                e.timestamp = datetime.datetime.utcnow()
                await channel.send(embed=e)
    



    @commands.Cog.listener()
    async def on_ready(self):
        print('[READY] Cog "guild_events" has been loaded!')
        print(f'---------------------------------------')            
                    

    
def setup(bot):
    bot.add_cog(guild_events(bot))