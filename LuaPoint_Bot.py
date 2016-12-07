import discord
import asyncio
import chatlogging
import random
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

    if is_command(message, 'piano'):
        if(get_user_balance(message.author) > 99):
            await client.send_message(message.channel, '%s, 100 lua points were taken from you \n https://i.gyazo.com/9b786ec4c43c12d2c7406c91e0404501.gif' % str(message.author))
            set_user_balance(message.author, get_user_balance(message.author)-100)
        else:
            await client.send_message(message.channel, '%s, 100 lua points are needed for Anne to play the piano' % str(message.author))

    if is_command(message, 'motherload'):
        set_user_balance(message.author, get_user_balance(message.author) + 100)
        await client.send_message(message.channel, 'Congratulations %s! You have been awarded 100 lua points!\nYour current balance is %s' % (message.author, get_user_balance(message.author)))

    if is_command(message, 'roll'):
        if get_user_balance(message.author) < 10:
            await client.send_message(message.channel, '%s, you do not have enough points to play a roulette.' % str(message.author))
        else:
            set_user_balance(message.author, get_user_balance(message.author) - 10)
            await client.send_message(message.channel, 'You are gamble addicted %s!\nRolling a roulette...' % str(message.author))
            roll = random.randint(0, 100)
            if roll % 3 == 0:
                set_user_balance(message.author, get_user_balance(message.author) + 20)
                await client.send_message(message.channel, 'Woah! %s, you doubled your points!' % str(message.author))
            elif roll % 3 == 1:
                set_user_balance(message.author, get_user_balance(message.author) + 10)
                await client.send_message(message.channel, '%s, you regained your points.' % str(message.author))
            else:
                await client.send_message(message.channel, '%s, you totally lost your points..' % str(message.author))
        
client.run('MjU0MjU3MjIxMzYwMjg3NzQ1.CyMcHQ.NrTHeRYee9oDI5Tn8rQCghSArN8')
