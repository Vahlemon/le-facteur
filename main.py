import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.type == discord.ChannelType.private:
        channel = client.get_channel(872685839493251092)
        await channel.send('Message de : __**' + message.author.display_name + '**__\n> ' + message.content)

client.run(os.getenv('TOKEN'))
