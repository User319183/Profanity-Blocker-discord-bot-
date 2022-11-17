import discord

from discord.ext import commands

from discord import DMChannel, activity


import discord
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
















if os.path.exists(os.getcwd() + "/config.json"):
    
    
    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"Token": ""}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f) 

token = configData["Token"]

















intents = discord.Intents.default()
intents.members = True
intents.presences = False
intents.message_content = True

bot = commands.Bot(command_prefix="pb-", intents=intents, activity=discord.Activity(type=discord.ActivityType.watching, name=f"for profanity"))

bot.remove_command('help')

for fn in os.listdir('./cogs'):
	if fn.endswith('.py'):
		bot.load_extension(f"cogs.{fn[:-3]}")


@bot.listen()
async def on_ready():
    print(f'Bot has been activated! Modules loaded.')
    print(f'---------------------------------------')
    
    






























with open(".txt/basefilter.txt", encoding="utf8") as file:
    blacklist = file.read().split('\n')


with open(".txt/basefilterlatin.txt", encoding="utf8") as file:
    latinbasefilter = file.read().split('\n')
    
    
with open(".txt/basefilter2latin.txt", encoding="utf8") as file:
    latinbasefilter2 = file.read().split('\n')


    
    
with open(".txt/basefilterfonts.txt", encoding="utf8") as file:
    basefilterfonts = file.read().split('\n')
    

with open(".txt/basefilter2.txt") as file:
    blacklist2 = file.read().split('\n')
    
    
with open(".txt/basefiltergerman.txt", encoding="utf8") as file:
    basefiltergerman = file.read().split('\n')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    


symbols = string.punctuation + string.digits + "‎" + "ᆞ" + "͏" + "—" + "”" + "•" + "█" + "▲" + "…"  + "¿"  + "¡" + "’" + "‘" + "▬" + "★" + "‍"
letters = string.ascii_letters + "‎" + "ᆞ" + "͏" + "—" + "”" + "•" + "█" + "▲" + "…" + "¿"  + "¡" + "’" + "‘" + "▬" + "★" + "‍"



@bot.listen()
async def on_message(message):

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
    
    


    for word in blacklist2:
        regex_match_true = re.compile(fr"[{symbols}]*".join(list(word)), re.IGNORECASE)
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
                    embed.add_field(name="Filter", value=f"English", inline=False)
                    embed.timestamp = discord.utils.utcnow()
                    await the_channel.send(embed=embed)

            else:

                    embed = discord.Embed(title="Bad Word Blocked", description=f"{message.author.mention} sent a bad word", color=15158332)
                    embed.add_field(name="Blocked Message", value=f"{message.content}", inline=False)
                    embed.add_field(name="Channel", value=f"{message.channel.mention}", inline=False)
                    embed.add_field(name="Filter", value=f"English", inline=False)
                    embed.timestamp = discord.utils.utcnow()
                    await the_channel.send(embed=embed)
                    


















@bot.listen()
async def on_message_edit(before, after):
    after.content = after.content.lower()
    after.content = discord.utils.remove_markdown(after.content)
    bypassedRole = discord.utils.get(after.guild.roles, name="Bypassed")
    
    if after.author.bot:
        return
    
    
    try:
        if "Bypassed" in after.channel.topic:
            return
                
    except:
        pass

    if bypassedRole in after.author.roles:
        return


    for word in blacklist2:
        regex_match_true = re.compile(fr"[{symbols}]*".join(list(word)), re.IGNORECASE)
        regex_match_none = re.compile(fr"([{letters}]+{word})|({word}[{letters}]+)", re.IGNORECASE)
        if regex_match_true.search(after.content) and regex_match_none.search(after.content) is None:
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
                    embed.add_field(name="Filter", value=f"English", inline=False)
                    embed.timestamp = discord.utils.utcnow()
                    await the_channel.send(embed=embed)

            else:

                    embed = discord.Embed(title="Bad Word Blocked", description=f"{after.author.mention} sent a bad word", color=15158332)
                    embed.add_field(name="Blocked Message", value=f"{after.content}", inline=False)
                    embed.add_field(name="Channel", value=f"{after.channel.mention}", inline=False)
                    embed.add_field(name="Filter", value=f"English", inline=False)
                    embed.timestamp = discord.utils.utcnow()
                    await the_channel.send(embed=embed)







    




@bot.listen()
async def on_message(message):


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

    for word in blacklist:
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
                    embed.add_field(name="Filter", value=f"English", inline=False)
                    embed.timestamp = discord.utils.utcnow()
                    await the_channel.send(embed=embed)

            else:

                    embed = discord.Embed(title="Bad Word Blocked", description=f"{message.author.mention} sent a bad word", color=15158332)
                    embed.add_field(name="Blocked Message", value=f"{message.content}", inline=False)
                    embed.add_field(name="Channel", value=f"{message.channel.mention}", inline=False)
                    embed.add_field(name="Filter", value=f"English", inline=False)
                    embed.timestamp = discord.utils.utcnow()
                    await the_channel.send(embed=embed)
                    










#string_whitespace filter bad words

sym = string.punctuation + string.digits + string.whitespace + "‎" + "ᆞ" + "͏" + "—" + "”" + "•" + "█" + "▲" + "…" + "¿"  + "¡" + "’" + "‘" + "▬" + "★" + "‍"
fr"[{symbols}]*"

with open(".txt/basefilter3.txt") as file:
    regular_expression = file.read().split('\n')

@bot.listen()
async def on_message(message):

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

    for word in regular_expression:
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
                    embed.add_field(name="Filter", value=f"English", inline=False)
                    embed.timestamp = discord.utils.utcnow()
                    await the_channel.send(embed=embed)

            else:

                    embed = discord.Embed(title="Bad Word Blocked", description=f"{message.author.mention} sent a bad word", color=15158332)
                    embed.add_field(name="Blocked Message", value=f"{message.content}", inline=False)
                    embed.add_field(name="Channel", value=f"{message.channel.mention}", inline=False)
                    embed.add_field(name="Filter", value=f"English", inline=False)
                    embed.timestamp = discord.utils.utcnow()
                    await the_channel.send(embed=embed)
                    
                    










#string_whitespace filter bad words message edit



sym = string.punctuation + string.digits + string.whitespace + "‎" + "ᆞ" + "͏" + "—" + "”" + "•" + "█" + "▲" + "…" + "¿"  + "¡" + "’" + "‘" + "▬" + "★" + "‍"
fr"[{symbols}]*"

with open(".txt/basefilter3.txt") as file:
    regular_expression = file.read().split('\n')

@bot.listen()
async def on_message_edit(before, after):

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

    for word in regular_expression:
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
                    embed.add_field(name="Filter", value=f"English", inline=False)
                    embed.timestamp = discord.utils.utcnow()
                    await the_channel.send(embed=embed)

            else:

                    embed = discord.Embed(title="Bad Word Blocked", description=f"{after.author.mention} sent a bad word", color=15158332)
                    embed.add_field(name="Blocked Message", value=f"{after.content}", inline=False)
                    embed.add_field(name="Channel", value=f"{after.channel.mention}", inline=False)
                    embed.add_field(name="Filter", value=f"English", inline=False)
                    embed.timestamp = discord.utils.utcnow()
                    await the_channel.send(embed=embed)
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    

       
                    
                    
# LATIN BASE FILTER                
                    
@bot.listen()
async def on_message(message):


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

    for word in latinbasefilter:
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
                    embed.add_field(name="Filter", value=f"English", inline=False)
                    embed.timestamp = discord.utils.utcnow()
                    await the_channel.send(embed=embed)

            else:

                    embed = discord.Embed(title="Bad Word Blocked", description=f"{message.author.mention} sent a bad word", color=15158332)
                    embed.add_field(name="Blocked Message", value=f"{message.content}", inline=False)
                    embed.add_field(name="Channel", value=f"{message.channel.mention}", inline=False)
                    embed.add_field(name="Filter", value=f"English", inline=False)
                    embed.timestamp = discord.utils.utcnow()
                    await the_channel.send(embed=embed)  
                    

                    
                    
               
                                   
           
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    

                    
                    
                    
                    
                    
                    
     
# (MESSAGE EDIT) LATIN BASE FILTER                
                    
@bot.listen()
async def on_message_edit(before, after):


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

    for word in latinbasefilter:
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
                    embed.add_field(name="Filter", value=f"English", inline=False)
                    embed.timestamp = discord.utils.utcnow()
                    await the_channel.send(embed=embed)

            else:

                    embed = discord.Embed(title="Bad Word Blocked", description=f"{after.author.mention} sent a bad word", color=15158332)
                    embed.add_field(name="Blocked Message", value=f"{after.content}", inline=False)
                    embed.add_field(name="Channel", value=f"{after.channel.mention}", inline=False)
                    embed.add_field(name="Filter", value=f"English", inline=False)
                    embed.timestamp = discord.utils.utcnow()
                    await the_channel.send(embed=embed)     
                    

                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    

                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    




                    
                    
                    
                    
                    
# REGEX latinbasefilter2 FILTER                     
                    
with open(".txt/basefilter2latin.txt", encoding="utf8") as file:
    latinbasefilter2 = file.read().split('\n')

@bot.listen()
async def on_message(message):

    message.content = discord.utils.remove_markdown(message.content)

    guild = message.guild
    bypassedRole = discord.utils.get(guild.roles, name="Bypassed")
    
    
    
    
    try:
        if "Bypassed" in message.channel.topic:
            return
                
    except:
        pass

    
    if message.author.bot:
        return


    if bypassedRole in message.author.roles:
        return



    for word in latinbasefilter2:
        regex_match_true = re.compile(fr"[{symbols}]*".join(list(word)), re.IGNORECASE)
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
                    embed.add_field(name="Filter", value=f"English", inline=False)
                    embed.timestamp = discord.utils.utcnow()
                    await the_channel.send(embed=embed)

            else:

                    embed = discord.Embed(title="Bad Word Blocked", description=f"{message.author.mention} sent a bad word", color=15158332)
                    embed.add_field(name="Blocked Message", value=f"{message.content}", inline=False)
                    embed.add_field(name="Channel", value=f"{message.channel.mention}", inline=False)
                    embed.add_field(name="Filter", value=f"English", inline=False)
                    embed.timestamp = discord.utils.utcnow()
                    await the_channel.send(embed=embed)       
                    

                    
                    
                    
                    
                    
                    
                    
                    
                    
# REGEX latinbasefilter2 FILTER MESSAGE EDIT               
                    
@bot.listen()
async def on_message_edit(before, after):
    after.content = after.content.lower()
    after.content = discord.utils.remove_markdown(after.content)
    bypassedRole = discord.utils.get(after.guild.roles, name="Bypassed")
    
    if after.author.bot:
        return
    
    
    
    try:
        if "Bypassed" in after.channel.topic:
            return
                
    except:
        pass
    

    if bypassedRole in after.author.roles:
        return


    for word in latinbasefilter2:
        regex_match_true = re.compile(fr"[{symbols}]*".join(list(word)), re.IGNORECASE)
        regex_match_none = re.compile(fr"([{letters}]+{word})|({word}[{letters}]+)", re.IGNORECASE)
        if regex_match_true.search(after.content) and regex_match_none.search(after.content) is None:
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
                    embed.add_field(name="Filter", value=f"English", inline=False)
                    embed.timestamp = discord.utils.utcnow()
                    await the_channel.send(embed=embed)

            else:

                    embed = discord.Embed(title="Bad Word Blocked", description=f"{after.author.mention} sent a bad word", color=15158332)
                    embed.add_field(name="Blocked Message", value=f"{after.content}", inline=False)
                    embed.add_field(name="Channel", value=f"{after.channel.mention}", inline=False)
                    embed.add_field(name="Filter", value=f"English", inline=False)
                    embed.timestamp = discord.utils.utcnow()
                    await the_channel.send(embed=embed)
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    



























# BASEFILTER basefilterfonts BASE FILTER                
                    
@bot.listen()
async def on_message(message):


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

    for word in basefilterfonts:
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
                    embed.add_field(name="Filter", value=f"Font", inline=False)
                    embed.timestamp = discord.utils.utcnow()
                    await the_channel.send(embed=embed)

            else:

                    embed = discord.Embed(title="Bad Word Blocked", description=f"{message.author.mention} sent a bad word", color=15158332)
                    embed.add_field(name="Blocked Message", value=f"{message.content}", inline=False)
                    embed.add_field(name="Channel", value=f"{message.channel.mention}", inline=False)
                    embed.add_field(name="Filter", value=f"Font", inline=False)
                    embed.timestamp = discord.utils.utcnow()
                    await the_channel.send(embed=embed)
                    

                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
# (MESSAGE EDIT) basefilterfonts BASE FILTER
                    
@bot.listen()
async def on_message_edit(before, after):

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

    for word in basefilterfonts:
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
                    embed.add_field(name="Filter", value=f"Font", inline=False)
                    embed.timestamp = discord.utils.utcnow()
                    await the_channel.send(embed=embed)

            else:

                    embed = discord.Embed(title="Bad Word Blocked", description=f"{after.author.mention} sent a bad word", color=15158332)
                    embed.add_field(name="Blocked Message", value=f"{after.content}", inline=False)
                    embed.add_field(name="Channel", value=f"{after.channel.mention}", inline=False)
                    embed.add_field(name="Filter", value=f"Font", inline=False)
                    embed.timestamp = discord.utils.utcnow()
                    await the_channel.send(embed=embed)













































                    
                    
                    
                    
                    
                    
                    
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
                    
                    

                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    

















































































































































































#BASEFILTER1 GERMAN

@bot.listen()
async def on_message(message):


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

    for word in basefiltergerman:
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
                    embed.add_field(name="Filter", value=f"German", inline=False)
                    embed.timestamp = discord.utils.utcnow()
                    await the_channel.send(embed=embed)

            else:

                    embed = discord.Embed(title="Bad Word Blocked", description=f"{message.author.mention} sent a bad word", color=15158332)
                    embed.add_field(name="Blocked Message", value=f"{message.content}", inline=False)
                    embed.add_field(name="Channel", value=f"{message.channel.mention}", inline=False)
                    embed.add_field(name="Filter", value=f"German", inline=False)
                    embed.timestamp = discord.utils.utcnow()
                    await the_channel.send(embed=embed)
                    
                    
                    
                    
                    
                    
                    
                    
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           

                    
                    
                    
# (MESSAGE EDIT) BASE FILTER GERMAN
                    
@bot.listen()
async def on_message_edit(before, after):


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

        for word in basefiltergerman:
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
                        embed.add_field(name="Filter", value=f"German", inline=False)
                        embed.timestamp = discord.utils.utcnow()
                        await the_channel.send(embed=embed)

                else:

                        embed = discord.Embed(title="Bad Word Blocked", description=f"{after.author.mention} sent a bad word", color=15158332)
                        embed.add_field(name="Blocked Message", value=f"{after.content}", inline=False)
                        embed.add_field(name="Channel", value=f"{after.channel.mention}", inline=False)
                        embed.add_field(name="Filter", value=f"German", inline=False)
                        embed.timestamp = discord.utils.utcnow()
                        await the_channel.send(embed=embed)









  
  
# @bot.slash_command()
# @commands.has_guild_permissions(manage_channels=True)
# async def language(ctx, lang: Option(str, "The language.", choices=["Spanish", "English"])):
#     with open('language.json', 'r') as f:
#         logs = json.load(f)

#     logs[str(ctx.guild.id)] = lang

#     with open('language.json', 'w') as f:
#         json.dump(logs, f, indent=4)

#     await ctx.respond(f":white_check_mark: The default language of this bot has been set to {lang}!")

  
  
  

  
  
  
  
  
  

  

    
bot.run(token)