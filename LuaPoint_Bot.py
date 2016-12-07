import discord
import asyncio
import chatlogging
import random
import logging
client = discord.Client()

#Display useful info in terminal
logging.basicConfig(level=logging.INFO)

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
        await client.send_message(message.channel, 'Hello {}'.format(message.author))

    if is_command(message, 'balance'):
        await client.send_message(message.channel, '{}, your balance is: {}'.format(message.author, get_user_balance(message.author)))

    if is_command(message, 'gift'):
        set_user_balance(message.author, get_user_balance(message.author) + 10)
        await client.send_message(message.channel, 'Congratulations {}! You have been awarded 10 lua points!\nYour current balance is {}'.format(message.author, get_user_balance(message.author)))

    if is_command(message, 'piano'):
        if(get_user_balance(message.author) > 99):
            await client.send_message(message.channel, '{}, 100 lua points were taken from you \n https://i.gyazo.com/9b786ec4c43c12d2c7406c91e0404501.gif'.format(message.author))
            set_user_balance(message.author, get_user_balance(message.author)-100)
        else:
            await client.send_message(message.channel, '{}, 100 lua points are needed for Anne to play the piano'.format(message.author))

    if is_command(message, 'motherload'):
        set_user_balance(message.author, get_user_balance(message.author) + 100)
        await client.send_message(message.channel, 'Congratulations {}! You have been awarded 100 lua points!\nYour current balance is {}'.format(message.author, get_user_balance(message.author)))

    if is_command(message, 'roll'):
        if get_user_balance(message.author) < 10:
            await client.send_message(message.channel, '{}, you do not have enough points to play a roulette.'.format(message.author))
        else:
            set_user_balance(message.author, get_user_balance(message.author) - 10)
            await client.send_message(message.channel, 'You are gamble addicted {}!\nRolling a roulette...'.format(message.author))
            roll = random.randint(0, 100)
            if roll % 3 == 0:
                set_user_balance(message.author, get_user_balance(message.author) + 20)
                await client.send_message(message.channel, 'Woah! {}, you doubled your points!'.format(message.author))
            elif roll % 3 == 1:
                set_user_balance(message.author, get_user_balance(message.author) + 10)
                await client.send_message(message.channel, '{}, you regained your points.'.format(message.author))
            else:
                await client.send_message(message.channel, '{}, you totally lost your points..'.format(message.author))

client.run('MjU0MjU3MjIxMzYwMjg3NzQ1.CyMcHQ.NrTHeRYee9oDI5Tn8rQCghSArN8')
