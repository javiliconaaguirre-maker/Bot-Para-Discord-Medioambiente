import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    assert bot.user is not None

    print('Hola estoy aqui para hablarte de el medio ambiente!!')
    print('usa el comando ! para activar comandos por ejemplo:')
    print('!Trashcan botella')

@bot.command()
async def Trashcan(ctx,cosa:str):
    plastico=['botella','bolsa',]
    reciclaje=['caja','papel','metales']
    organico=['comida','manzana','fruta']
    for i in plastico:
        if i == cosa:
            await ctx.send('Va en plastico')
    for i in reciclaje:
        if i == cosa:
            await ctx.send('Va en reciclaje')
    for i in organico:
        if i == cosa:
            await ctx.send('Va en organico')
    
bot.run('Pon tu codigo')