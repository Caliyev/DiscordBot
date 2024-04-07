import discord
from discord.ext import commands
from bot_token import token
import os
import random
import requests

# Botunuzun diğer tanımları...

# Mem nadirlik değerlerini yüklemek için bir fonksiyon
def mem_nadirlik_yukle():
    nadirlik_sozlugu = {}
    dosya_yolu = 'mem_nadirlikleri.txt'  # Dosyanın yolunu doğru veriyoruz.
    with open(dosya_yolu, 'r') as f:
        for satir in f:
            parcalar = satir.strip().split(',')
            if len(parcalar) == 2 and parcalar[1].isdigit():
                nadirlik_sozlugu[parcalar[0]] = int(parcalar[1])
    return nadirlik_sozlugu

# Yetki ayarları ve bot tanımlaması
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} adıyla Discord\'a bağlandık!')
    img_dizin = 'M2L1/images'  # İmajların bulunduğu dizin yolu.
    if os.path.exists(img_dizin):
        print(f"'{img_dizin}' dizini mevcut.")
    else:
        print(f"'{img_dizin}' dizini bulunamadı!")

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

# Botunuzun diğer komutları...

@bot.command()
async def random_mem(ctx):
    mem_nadirlikleri = mem_nadirlik_yukle()
    img_dizin = 'M2L1/images'  # İmajların bulunduğu dizin yolu.
    img_list = os.listdir(img_dizin)

    # Sadece nadirlik değerleri belirlenmiş memler üzerinde işlem yap
    secili_memler_ve_agirliklari = [(mem, mem_nadirlikleri.get(mem, 0)) for mem in img_list if mem in mem_nadirlikleri]
    if not secili_memler_ve_agirliklari:
        await ctx.send("Uygun mem bulunamadı.")
        return

    # Ağırlıklara göre rastgele bir mem seç
    secili_memler, agirliklar = zip(*secili_memler_ve_agirliklari)
    secilen_mem = random.choices(secili_memler, weights=agirliklar, k=1)[0]

    with open(os.path.join(img_dizin, secilen_mem), 'rb') as f:
        picture = discord.File(f)
    await ctx.send("Al sana nadir bir mem!", file=picture)

@bot.command()
async def animals(ctx):
    await ctx.send("Al sana mem!")

    img_dizin = 'M2L1/images'  # Fotoğrafların bulunduğu dizin.

    try:
        # "animal.jpg" fotoğrafını gönder
        with open(f'{img_dizin}/animal.jpg', 'rb') as file:
            animal_pic = discord.File(file)
            await ctx.send(file=animal_pic)
        
        # "images.png" fotoğrafını gönder
        with open(f'{img_dizin}/images.jpg', 'rb') as file:
            images_pic = discord.File(file)
            await ctx.send(file=images_pic)

    except FileNotFoundError as e:
        await ctx.send(f'Bir hata oluştu: {e}')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return  # Komut bulunamadıysa sessiz kal
    await ctx.send(f'Bir hata oluştu: {error}')


# Botu çalıştırma komutu
bot.run(token)
