import discord
import asyncio
import chatlogging
client = discord.Client()

command_prefix = '!'
def is_command(message, label):
    return message.content.startswith('{}{}'.format(command_prefix, label))

@client.event
async def on_ready():
    chatlogging.cmdlog('', 'login')

@client.event
async def on_message(message):
    chatlogging.cmdlog(message)

    if is_command(message, 'hello'):
        await client.send_message(message.channel, 'Hello %s' % message.author)

client.run('MjU0MjU3MjIxMzYwMjg3NzQ1.CyMcHQ.NrTHeRYee9oDI5Tn8rQCghSArN8')
