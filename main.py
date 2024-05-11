import random

import discord
from discord.ext import commands

Token = ''
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True

# Create a bot instance with the command prefix '!_RC'
bot = commands.Bot(command_prefix='!RC ', intents=intents)
Spammer = None



@bot.event
async def on_ready():
    print('Bot is online!')
    channel = bot.get_channel(1231177776850145280)  # Use your specific channel ID
    user = bot.get_user(1231193596011741256)
    if channel:
        messages = channel.history(limit=500)
        for message in messages:
            message.delete()

        await channel.send('Hello, I am now online!')
    else:
        print('Channel not found')



@bot.command(name='GetSpammer')  # Vai buscar o maior spammer dos ultimos 5 minutos e guarda
async def GetSpammer(ctx):

    await ctx.send()

@bot.command(name='Spammer')
async def SpammerHandler(ctx, arg):
    match arg:
        case 'Help':  #Help - Diz que comandos estao disponiveis
            ctx.send("Os comandos disponiveis são: ZipIt, Amnesia, Help, o atual alvo é "+Spammer)
            pass
        case 'ZipIt':  #ZipIt - Timeout durante 30 segundos

            pass
        case 'Amnesia':  #Amnesia - Apagar as ultimas 10 mensagens do henrique no chat em questao

            pass

    pass


@bot.command(name='GifMeUp')  # Create a command in the bot
async def GifMeUp(ctx):
    randomgifs = 'https://tenor.com/view/firefly-honkai-star-rail-honkai-star-rail-spin-gif-388301994884493627'
    await ctx.send(randomgifs)


@bot.command(name='Palindrome')  # Create a command in the bot
async def Palindrome(ctx, arg):
    await ctx.send(arg[::-1])  # Sends 'Olá' back in the channel where the command was called


bot.run(Token)
