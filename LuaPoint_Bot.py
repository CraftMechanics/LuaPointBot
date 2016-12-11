import discord
import asyncio
import chatlogging
import random
import logging
import commands
import slots
client = discord.Client()

#Display useful info in terminal
logging.basicConfig(level=logging.INFO)

command_prefix = '!'
def is_command(message, label):
   return message.content.startswith('{}{}'.format(command_prefix, label))

@client.event
async def on_message(message):
    chatlogging.cmdlog(message)
    channel = message.channel
    cmdlist = ['test', 'hello', 'balance', 'gift', 'motherload', 'roll', 'cat', 'piano']
    for i in range(0, len(cmdlist)):
        if is_command(message, cmdlist[i]):
            await client.send_message(channel, commands.reply(cmdlist[i], message))

    if is_command(message, "slots"):
        slots.createpic()
        with open('img.png', 'rb') as f:
            await client.send_file(channel, f)

@client.event
async def on_ready():
    chatlogging.cmdlog('', 'login')

client.run('MjU0MjU3MjIxMzYwMjg3NzQ1.CyMcHQ.NrTHeRYee9oDI5Tn8rQCghSArN8')
