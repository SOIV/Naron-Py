import discord

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!ping'):
        await message.channel.send('pong')

client.run('token')