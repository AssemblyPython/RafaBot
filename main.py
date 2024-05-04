import discord
from discord.ext import commands

Token = 'Your_Token_Here'
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

# Create a bot instance with the command prefix '!_RC'
bot = commands.Bot(command_prefix='!_RC', intents=intents)


@bot.event
async def on_ready():
    print('Bot is online!')
    channel = bot.get_channel(1231177776850145280)  # Use your specific channel ID
    if channel:
        await channel.send('Hello, I am now online!')
    else:
        print('Channel not found')


@bot.command(name='helloworld')  # Create a command in the bot
async def helloworld(ctx):
    await ctx.send('Olá')  # Sends 'Olá' back in the channel where the command was called


bot.run(Token)
