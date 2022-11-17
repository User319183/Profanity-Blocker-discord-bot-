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
    
    
    
    
if os.path.exists(os.getcwd() + "/config.json"):
    
    
    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"basic_premium": ""}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f) 

basic_premium = configData["basic_premium"]
                

                

























with open(".txt/basefilterphrases.txt", encoding="utf8") as file:
    Phrases = file.read().split('\n')
    



letters = string.ascii_letters + "‎" + "ᆞ" + "͏" + "—" + "”" + "•" + "█" + "▲" + "…" + "¿"  + "¡" + "’" + "‘" + "▬" + "★"


sym = string.punctuation + string.digits + string.whitespace + "‎" + "ᆞ" + "͏" + "—" + "”" + "•" + "█" + "▲" + "…" + "¿"  + "¡" + "’" + "‘" + "▬" + "★"
fr"[{sym}]*"




class Phrase_Filter(commands.Cog):
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

            for word in Phrases:
                if message.content.count(word) > 0:
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
                            embed.add_field(name="Filter", value=f"Phrase", inline=False)
                            embed.timestamp = discord.utils.utcnow()
                            await the_channel.send(embed=embed)

                    else:

                            embed = discord.Embed(title="Bad Word Blocked", description=f"{message.author.mention} sent a bad word", color=15158332)
                            embed.add_field(name="Blocked Message", value=f"{message.content}", inline=False)
                            embed.add_field(name="Channel", value=f"{message.channel.mention}", inline=False)
                            embed.add_field(name="Filter", value=f"Phrase", inline=False)
                            embed.timestamp = discord.utils.utcnow()
                            await the_channel.send(embed=embed)
                

 
 



    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if after.guild.id in basic_premium:

            after.content = after.content.lower()
            after.content = discord.utils.remove_markdown(after.content)

            guild = after.guild
            bypassedRole = discord.utils.get(guild.roles, name="Bypassed")
            
            if after.author.bot:
                return
            
            
            
            try:
                if "Bypassed" in after.channel.topic:
                    return
                        
            except:
                pass


            if bypassedRole in after.author.roles:
                return

            for word in Phrases:
                if after.content.count(word) > 0:
                    await after.delete()
                    embed = discord.Embed(title="Message Deleted", color=0xD708CC, description= f"{after.author.mention} You're not allowed to say that.")
                    embed.timestamp = discord.utils.utcnow()
                    await after.channel.send(embed=embed, delete_after=10)


                    

                    the_guild = after.guild
                    the_channel = discord.utils.get(the_guild.text_channels, name="badword-logs")

                
                    if len(after.content) > 1200:

                            embed = discord.Embed(title="Bad Word Blocked", description=f"{after.author.mention} sent a bad word", color=15158332)
                            embed.add_field(name="Blocked Message", value=f"System message: Message is too big to display..", inline=False)
                            embed.add_field(name="Channel", value=f"{after.channel.mention}", inline=False)
                            embed.add_field(name="Filter", value=f"Phrase", inline=False)
                            embed.timestamp = discord.utils.utcnow()
                            await the_channel.send(embed=embed)

                    else:

                            embed = discord.Embed(title="Bad Word Blocked", description=f"{after.author.mention} sent a bad word", color=15158332)
                            embed.add_field(name="Blocked Message", value=f"{after.content}", inline=False)
                            embed.add_field(name="Channel", value=f"{after.channel.mention}", inline=False)
                            embed.add_field(name="Filter", value=f"Phrase", inline=False)
                            embed.timestamp = discord.utils.utcnow()
                            await the_channel.send(embed=embed)


























#string_whitespace filter



    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild.id in basic_premium:

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

            for word in Phrases:
                regex_match_true = re.compile(fr"[{sym}]*".join(list(word)), re.IGNORECASE)
                regex_match_none = re.compile(fr"([{letters}]+{word})|({word}[{letters}]+)", re.IGNORECASE)
                regex=regex_match_true.search(message.content) and regex_match_none.search(message.content) is None
                if regex:
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
                            embed.add_field(name="Filter", value=f"Phrase", inline=False)
                            embed.timestamp = discord.utils.utcnow()
                            await the_channel.send(embed=embed)

                    else:

                            embed = discord.Embed(title="Bad Word Blocked", description=f"{message.author.mention} sent a bad word", color=15158332)
                            embed.add_field(name="Blocked Message", value=f"{message.content}", inline=False)
                            embed.add_field(name="Channel", value=f"{message.channel.mention}", inline=False)
                            embed.add_field(name="Filter", value=f"Phrase", inline=False)
                            embed.timestamp = discord.utils.utcnow()
                            await the_channel.send(embed=embed)
                    
                    
                    













#string_whitespace filter



    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if after.guild.id in basic_premium:

            after.content = discord.utils.remove_markdown(after.content)

            guild = after.guild
            bypassedRole = discord.utils.get(guild.roles, name="Bypassed")


            if after.author.bot:
                return

            try:
                if "Bypassed" in after.channel.topic:
                    return
                        
            except:
                pass
            
            

            if bypassedRole in after.author.roles:
                return

            for word in Phrases:
                regex_match_true = re.compile(fr"[{sym}]*".join(list(word)), re.IGNORECASE)
                regex_match_none = re.compile(fr"([{letters}]+{word})|({word}[{letters}]+)", re.IGNORECASE)
                regex=regex_match_true.search(after.content) and regex_match_none.search(after.content) is None
                if regex:
                    await after.delete()
                    embed = discord.Embed(title="Message Deleted", color=0xD708CC, description= f"{after.author.mention} You're not allowed to say that.")
                    embed.timestamp = discord.utils.utcnow()
                    await after.channel.send(embed=embed, delete_after=10)


                        
                    the_guild = after.guild
                    the_channel = discord.utils.get(the_guild.text_channels, name="badword-logs")

                
                    if len(after.content) > 1200:

                            embed = discord.Embed(title="Bad Word Blocked", description=f"{after.author.mention} sent a bad word", color=15158332)
                            embed.add_field(name="Blocked Message", value=f"System message: Message is too big to display..", inline=False)
                            embed.add_field(name="Channel", value=f"{after.channel.mention}", inline=False)
                            embed.add_field(name="Filter", value=f"Phrase", inline=False)
                            embed.timestamp = discord.utils.utcnow()
                            await the_channel.send(embed=embed)

                    else:

                            embed = discord.Embed(title="Bad Word Blocked", description=f"{after.author.mention} sent a bad word", color=15158332)
                            embed.add_field(name="Blocked Message", value=f"{after.content}", inline=False)
                            embed.add_field(name="Channel", value=f"{after.channel.mention}", inline=False)
                            embed.add_field(name="Filter", value=f"Phrase", inline=False)
                            embed.timestamp = discord.utils.utcnow()
                            await the_channel.send(embed=embed)


























    @commands.Cog.listener()
    async def on_ready(self):
        print('[READY] Cog "Phrase_Filter" has been loaded!')
        print(f'---------------------------------------')            
                    

    
def setup(bot):
    bot.add_cog(Phrase_Filter(bot))