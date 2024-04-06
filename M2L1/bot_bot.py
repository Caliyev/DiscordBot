import discord
from bot_token import token
from bot_logic import *
from discord.ext import commands
import os
import requests

#yetki ayarları
intents = discord.Intents.default()
#message.content mesajın içeriğinin okunabilmesi için gerekli.
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def parola(ctx, pass_length = 8):
    password = gen_pass(pass_length)
    await ctx.send(str(pass_length) + "uzunlukta bir şifre:" + password)
    #await ctx.send("!parola varsy .... 8 uzunluk, bir sayı girerek ..... !parola 15")

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def mem(ctx):
    with open('M2L1\images\M2L1-T2-2_ksnyah.png', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send("Al sana mem!")
    await ctx.send(file=picture)

@bot.command()
async def random_mem(ctx):
    img_list = os.listdir('M2L1\images')
    img_name = random.choice(img_list)

    with open(f'M2L1/images/{img_name}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send("Al sana mem!")
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
    
bot.run(token)