import discord
import asyncio

client = discord.Client()

command_prefix = 'lua'
user_balance_dict = dict()

def is_command(message, label):
    return message.content.startswith('%s %s' % (command_prefix, label))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(message):
    if is_command(message, 'hello'):
        await client.send_message(message.channel, 'Hello %s' % message.author)

    if is_command(message, 'balance'):
        if message.author not in user_balance_dict:
        user_balance_dict[message.author] = 0
        await client.send_message(message.channel, 'Your lua point balance is: ')
        await client.send_message(message.channel, user_balance_dict[message.author])

client.run('MjU0MjU3MjIxMzYwMjg3NzQ1.CyMcHQ.NrTHeRYee9oDI5Tn8rQCghSArN8')
