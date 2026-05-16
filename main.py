import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from settings import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, status=discord.Status.online, command_prefix="%")


@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break
        print(f'Logged in as {bot.user} on {guild.name} (ID: {guild.id})!')


@bot.event
async def on_message(message):
    try:
        print(f'{message.author} ({message.author.id}), ({message.guild.id}) : {message.content}')
    except AttributeError:
        print(f'{message.author} (DM) : {message.content}')
    if message.author.id != DONOTDELETEFROMID and message.channel.id == CHANNELID and message.guild.id == GUILDID:
        await message.delete()
    else:
        pass

bot.run(LOGINTOKENDONOTSHAREEVER)
