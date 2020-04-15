import discord
from hello import hi_output, different_hi
from top_searches import google_output
from recent import recent_output
from helpers import check_input_value
import os

TOKEN = os.environ.get('DISCORD_TOKEN')  # env variable

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:  # To stop replying on own messages
        return

    if message.content.lower() in different_hi():  # Checking for different Greetings(Hi, Hello etc.)
        msg = hi_output()  # Response for a HI
        await message.channel.send(msg)

    if message.content.startswith('!google'):
        input_val = check_input_value(message.content, "!google")
        if input_val[1] is True:  # Check Input is right Formatted
            msgs = google_output(message.author.id, input_val[0], client.user.id)  # Output from Google Search
        else:
            msgs = [input_val[0]]  # Output Error if Input is not correctly formatted
        for msg in msgs:
            await message.channel.send(msg)

    if message.content.startswith('!recent'):
        input_val = check_input_value(message.content, "!recent")
        if input_val[1] is True:
            msgs = recent_output(message.author.id, input_val[0], client.user.id)
        else:
            msgs = [input_val[0]]
        for msg in msgs:
            await message.channel.send(msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)

