import asyncio

import discord
from discord.ext import commands

import skills.affiliate
import skills.song
import skills.bricolage

intents = discord.Intents.all()
bot = commands.Bot(command_prefix= "!", description = "Bot BCC", intents=intents)

async def setup(): 
    await bot.add_cog(skills.affiliate.affiliation(bot))
    await bot.add_cog(skills.song.Music(bot))
    await bot.add_cog(skills.bricolage.BCC(bot))

asyncio.run(setup())

with open("token", "r", encoding="utf-8") as f:
    token = f.read()

bot.run(token)