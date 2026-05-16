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
    channel = "DM" if message.guild is None else message.guild.id
    print(f'{message.author.name} (ID: {message.author.id}, DM/Guild: {channel}) : {message.content}')
    if message.author.id != DO_NOT_DELETE_FROM_ID and message.channel.id == CHANNEL_ID and message.guild.id == GUILD_ID:
        await message.delete()
    else:
        pass

bot.run(LOGIN_TOKEN_DO_NOT_SHARE_EVER)
