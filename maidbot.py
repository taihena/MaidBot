# maidbot.py
import os
import discord

BOT_TOKEN = os.environ["DISCORD_BOT_TOKEN"]

client = discord.Client()


@client.event
async def on_ready():
    for guild in client.guilds:
        print(
            f'{client.user} is connected to the following guilds:\n'
            f'{guild.name}(id: {guild.id})'
        )

client.run(BOT_TOKEN)
