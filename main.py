import discord

Token = '???'
intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('Bot is online!')


client.run(Token)
