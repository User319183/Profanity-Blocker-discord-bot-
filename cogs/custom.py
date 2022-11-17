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




if os.path.exists(os.getcwd() + "/config.json"):
    
    
    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"userbanned": ""}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f) 

userbanned = configData["userbanned"]






class Custom(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @message_command(name="Blacklist Message")
    @commands.has_permissions(manage_messages=True)
    async def blacklist_message(self, ctx, message: discord.Message):  # message commands return the message
        
        if ctx.author.id in userbanned:
            return await ctx.respond("You have been banned from doing this command!", ephemeral=True)
        else:
            pass 
            
        await ctx.respond(f"{ctx.author.name}, A message with the ID of: **{message.id}** is getting deleted as profanity.")
        await message.delete()
        embed = discord.Embed(title="Message Deleted", color=0xD708CC, description= f"{message.author.mention} You're not allowed to say that.")
        embed.timestamp = discord.utils.utcnow()
        await message.channel.send(embed=embed, delete_after=10)

        
        the_guild = message.guild
        the_channel = discord.utils.get(the_guild.text_channels, name="badword-logs")

            
        if len(message.content) > 1200:

                embed = discord.Embed(title="Bad Word Blocked", description=f"{message.author.mention} sent a bad word", color=15158332)
                embed.add_field(name="Blocked Message", value=f"System message: Message is too big to display..", inline=False)
                embed.add_field(name="Channel", value=f"{message.channel.mention}", inline=False)
                embed.add_field(name="Filter", value=f"Custom", inline=False)
                embed.add_field(name="Author", value=f"{ctx.author.mention}", inline=False)
                embed.timestamp = discord.utils.utcnow()
                await the_channel.send(embed=embed)

        else:

                embed = discord.Embed(title="Bad Word Blocked", description=f"{message.author.mention} sent a bad word", color=15158332)
                embed.add_field(name="Blocked Message", value=f"{message.content}", inline=False)
                embed.add_field(name="Channel", value=f"{message.channel.mention}", inline=False)
                embed.add_field(name="Filter", value=f"Custom", inline=False)
                embed.add_field(name="Author", value=f"{ctx.author.mention}", inline=False)
                embed.timestamp = discord.utils.utcnow()
                await the_channel.send(embed=embed)
          
          
          
    @commands.Cog.listener()
    async def on_ready(self):
        print('[READY] Cog "Custom" has been loaded!')
        print(f'---------------------------------------')
    
            
            
            
            
def setup(bot):
    bot.add_cog(Custom(bot))