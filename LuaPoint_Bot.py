import discord
import asyncio

client = discord.Client()

command_prefix = 'lua'
user_balance_dict = {'CraftMechanics#7011' : 5}

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
        user_balance_dict[message.author] = 0   #Why the hell is the compiler
                                                #saying that there is an indentation
                                                #error on the letter 't' of user_balance_dict?
    user_balance = user_balance_dict[message.author]
    await client.send_message(message.channel, 'Your lua point balance is: %d' % user_balance)

client.run('MjU0MjU3MjIxMzYwMjg3NzQ1.CyMcHQ.NrTHeRYee9oDI5Tn8rQCghSArN8')
