import discord
import asyncio
import chatlogging
client = discord.Client()

command_prefix = '!'
user_balance_dict = {'Placeholder' : 0}

def is_command(message, label):
    return message.content.startswith('{}{}'.format(command_prefix, label))

def get_user_balance(user):
    if str(user) in user_balance_dict:
        return user_balance_dict[str(user)]
    else:
        user_balance_dict[str(user)] = 0
        return get_user_balance(user)

def set_user_balance(user, balance):
    user_balance_dict[str(user)] = balance;

@client.event
async def on_ready():
    chatlogging.cmdlog('', 'login')

@client.event
async def on_message(message):
    chatlogging.cmdlog(message)

    if is_command(message, 'hello'):
        await client.send_message(message.channel, 'Hello %s' % str(message.author))

    if is_command(message, 'balance'):
        await client.send_message(message.channel, '%s, your balance is: %s' % (str(message.author), get_user_balance(message.author)))

    if is_command(message, 'gift'):
        set_user_balance(message.author, get_user_balance(message.author) + 10)
        await client.send_message(message.channel, 'Congratulations %s! You have been awarded 10 lua points!\nYour current balance is %s' % (message.author, get_user_balance(message.author)))

client.run('MjU0MjU3MjIxMzYwMjg3NzQ1.CyMcHQ.NrTHeRYee9oDI5Tn8rQCghSArN8')
