import datetime
import random

import discord
from discord import member
from discord.ext import commands

Token = ''
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True

# Create a bot instance with the command prefix '!_RC'
bot = commands.Bot(command_prefix='!RC ', intents=intents)
Spammer = None
SpammerMessageSearchDepth = 100


@bot.command(name='GetSpammer')  # Vai buscar o maior spammer dos ultimos 5 minutos e guarda
async def GetSpammer(ctx):
    messageBlame = {}
    async for message in ctx.channel.history(limit=SpammerMessageSearchDepth):
        if message.author.name in messageBlame:
            messageBlame[message.author.name] += 1
        else:
            messageBlame[message.author.name] = 1

    Spammer = max(zip(messageBlame.values(), messageBlame.keys()))[1]
    await ctx.send('Tu tem cuidado que andas a esticar-te Wii dred ' + Spammer)


@bot.command(name='SpammerHandler')
async def SpammerHandler(ctx, arg):
    match arg:
        case 'Help':  #Help - Diz que comandos estao disponiveis
            ctx.send("Os comandos disponiveis são: ZipIt, Amnesia, Help, o atual alvo é " + Spammer)
            pass
        case 'ZipIt':  #ZipIt - Timeout durante 30 segundos
            await member.timeout(until=datetime.timedelta(seconds=30),reason="Spammer innnit")
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
