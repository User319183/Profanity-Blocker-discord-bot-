import discord

from discord.ext import commands

from discord import activity

from discord.commands import Option

import os
import sys

import json

import asyncio as asyncio



from discord.ext import *
from discord.ext.commands import *
from ctypes import *
from datetime import datetime



from contextlib import redirect_stdout
from discord.commands import slash_command

import random
import uuid

from discord.commands import permissions



if os.path.exists(os.getcwd() + "/config.json"):
    
    
    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"userbanned": ""}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f) 

userbanned = configData["userbanned"]





class Mod_Commands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot










	@slash_command(name="bypass", description="Bypass people for swearing.")
	@commands.has_guild_permissions(manage_roles=True)
	async def bypass(self, ctx, member: Option(discord.Member, "Specify the user to bypass." )): 


            
            
            if ctx.author.id in userbanned:
                return await ctx.respond("You have been banned from doing this command!", ephemeral=True)
            else:
                pass


                if member.bot:
                    return await ctx.respond("Bots are bypassed by default. Please try this on a member.")
                

                guild = ctx.guild
                bypassedRole = discord.utils.get(guild.roles, name="Bypassed")
                if bypassedRole in member.roles:

                    embed=discord.Embed(title="Error:", color=0xD708CC, description = "")
                    embed.add_field(name = "Member already bypassed", value = f"{member.mention} has already been bypassed.")
                    await ctx.respond(embed=embed)




            guild = ctx.guild
            bypassedRole = discord.utils.get(guild.roles, name="Bypassed")
            if bypassedRole not in member.roles:
                try:
                    await member.add_roles(bypassedRole)
                except:
                    pass
                

                guild = ctx.guild
                bypassedRole = discord.utils.get(guild.roles, name="Bypassed")
                if bypassedRole in member.roles:

                    embed=discord.Embed(title="Member Bypassed", color=0xD708CC, description = f"{member.mention} has been bypassed.")
                    await ctx.respond(embed=embed)





            if not bypassedRole:
                bypassedRole = await guild.create_role(name="Bypassed")
                await member.add_roles(bypassedRole)
                embed = discord.Embed(title="Member Bypassed", description=f"{member.mention} is now bypassed.", color=0xD708CC)
                embed.timestamp = discord.utils.utcnow()
                await ctx.respond(embed=embed)

            try:

                channel = discord.utils.get(ctx.guild.text_channels, name="mod-logs")

                embed = discord.Embed(title="Member Bypassed", description=f"{member.mention} is now bypassed.", color=0xD708CC)
                embed.add_field(name="Moderator", value=f"{ctx.author.mention}", inline=False)
                embed.timestamp = discord.utils.utcnow()
                await channel.send(embed=embed)
            except:
                pass










	@slash_command(name="unbypass", description="Remove the bypass from a specified user")
	@commands.has_guild_permissions(manage_roles=True)
	async def unbypass(self, ctx, member: Option(discord.Member, "Specify the user to unbypass.")):


            
            if ctx.author.id in userbanned:
                return await ctx.respond("You have been banned from doing this command!", ephemeral=True)
            else:
                pass
            
                if member.bot:
                    return await ctx.respond("Bots are bypassed by default and can not be removed from that. Please try this on a member.")

            try:

                bypassedRole = discord.utils.get(ctx.guild.roles, name="Bypassed")
                if bypassedRole not in member.roles:
                    embed = discord.Embed(title="Error", description="", color=0xD708CC)
                    embed.add_field(name = "Member already unbypassed", value = f"{member.mention} has been unbypassed.")
                    embed.timestamp = discord.utils.utcnow()
                    await ctx.respond(embed=embed)

            except:
                pass

                
            if bypassedRole in member.roles:
 
                bypassedRole = discord.utils.get(ctx.guild.roles, name="Bypassed")
                await member.remove_roles(bypassedRole)
                embed = discord.Embed(title="Member Unbypassed", description=f"{member.mention} has been unbypassed.", color=0xD708CC)
                embed.timestamp = discord.utils.utcnow()
                await ctx.respond(embed=embed)
            


            try:

                channel = discord.utils.get(ctx.guild.text_channels, name="mod-logs")

                embed = discord.Embed(title="Member Unbypassed", description=f"{member.mention} is now unbypassed.", color=0xD708CC)
                embed.add_field(name="Moderator", value=f"{ctx.author.mention}", inline=False)
                embed.timestamp = discord.utils.utcnow()
                await channel.send(embed=embed)
            except:
                pass



    
    
    
    
    

    
    
    
    
    
    
    
    

	@commands.Cog.listener()
	async def on_ready(self):
		print('[READY] Cog "Mod_Commands" has been loaded!')
		print(f'---------------------------------------')




def setup(bot):
	bot.add_cog(Mod_Commands(bot))