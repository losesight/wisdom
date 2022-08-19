import json
from pyexpat.errors import messages
import discord
from discord.ext import commands
import os 



bot = commands.Bot(command_prefix = '.',owner_ids={901262705594351626,836104992359972924 },intents=discord.Intents.all())



#statues
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Matthew 6:33 ", url = 'https://www.twitch.tv/otknetwork'))
    print('On')


bot.load_extension("jishaku")

@bot.command()
async def ping(ctx):
    await ctx.send(f'pong {round(bot.latency * 1000)}ms')


@bot.command()
async def clear(ctx,amount=100):
    await ctx.channel.purge(limit=amount)
