# maidbot.py
import os
import discord

intents = discord.Intents.default()
intents.members = True

BOT_TOKEN = os.environ["DISCORD_BOT_TOKEN"]
GUILD_NAME = os.environ["DISCORD_GUILD_NAME"]

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    for guild in client.guilds:
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})\n'
        )

        members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members}')

    # guild = discord.utils.get(client.guilds, name=GUILD)


@client.event
async def on_message(message):
    if message.author.id == client.user:
        return

    if message.content == "lucas":
        response = "standard is to use spaces <:pepega:538273570753871873>"
        await message.channel.send(response)


client.run(BOT_TOKEN)
