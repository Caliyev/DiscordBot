import discord
from discord.ext import commands
from bot_token import token
import random


spam_messages = [
    "JKDFSJLKDSFKJLSDLFKJSDLFJSDLFJSJLD",
    "AHKFDSKJDFSJDFSSKDFKHDSHFKHDSFKDFS",
    "ŞLKFDSKLDFSKŞLKLŞSDKŞLKŞLDFSKŞLFSD",
]

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yapıldı!')

@bot.command()
async def spam(ctx):
    # Rastgele bir spam mesajı seç ve gönder
    spam_message = random.choice(spam_messages)
    await ctx.send(spam_message)

bot.run(token)
