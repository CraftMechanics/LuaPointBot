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

def get_random_from_dict_by_weight(outcome_dict):
    total_weight = 0
    
    for outcome,weight in outcome_dict.items():
        total_weight += weight

    choice = random.randint(1, total_weight)
    
    counter = 1
    for outcome,weight in outcome_dict.items():
        if choice < counter+weight:
            return outcome
        else:
            counter += + weight

@client.event
async def on_ready():
    chatlogging.cmdlog('', 'login')

@client.event
async def on_message(message):
    
    #    TODO
    #    Change all the .format() to %s
    #    because it is causing issues
    #    with chat logging.
    #    Make constants for cost of
    #    commands and gambling rewards.


    #    str(author) is not needed when calling
    #    user balance functions, or formating text
    
    chatlogging.cmdlog(message)

    author = message.author
    channel = message.channel

    GAMBLING_OUTCOMES = {'lose' : 4, 'double' : 1, 'keep' : 2}
    GAMBLING_BET_AMOUNT = 10

    
    if is_command(message, 'hello'):
        await client.send_message(channel, 'Hello {}'.format(author))

    if is_command(message, 'balance'):
        await client.send_message(channel, '{}, your balance is: {}'.format(author, get_user_balance(author)))

    if is_command(message, 'gift'):
        set_user_balance(message.author, get_user_balance(message.author) + 10)
        await client.send_message(message.channel, 'Congratulations {}! You have been awarded 10 lua points!\nYour current balance is {}'.format(author, get_user_balance(author)))

    if is_command(message, 'piano'):
        if(get_user_balance(author) > 99):
            await client.send_message(channel, '{}, 100 lua points were taken from you \n https://i.gyazo.com/9b786ec4c43c12d2c7406c91e0404501.gif'.format(author))
            set_user_balance(author, get_user_balance(author)-100)
        else:
            await client.send_message(channel, '{}, 100 lua points are needed for Anne to play the piano'.format(author))

    if is_command(message, 'motherload'):
        set_user_balance(author, get_user_balance(author) + 100)
        await client.send_message(channel, 'Congratulations {}! You have been awarded 100 lua points!\nYour current balance is {}'.format(author, get_user_balance(author)))

    if is_command(message, 'roll'):
        if get_user_balance(author) >= GAMBLING_BET_AMOUNT:
            roll = get_random_from_dict_by_weight(GAMBLING_OUTCOMES)
            #await client.send_message(channel, roll)
            
            set_user_balance(author, get_user_balance(author) - GAMBLING_BET_AMOUNT)
            await client.send_message(channel, 'You are gamble addicted %s!\nRolling a roulette for %s points...' % (author, GAMBLING_BET_AMOUNT))

            if roll == 'double':
                set_user_balance(author, get_user_balance(author) + 2*GAMBLING_BET_AMOUNT)
                await client.send_message(channel, 'Woah! %s, you doubled your points! Your total is %s now' % (author, get_user_balance(author)))

            if roll == 'keep':    
                set_user_balance(author, get_user_balance(author) + GAMBLING_BET_AMOUNT)
                await client.send_message(channel, '%s, you regained your points. Your total is %s now' % (author, get_user_balance(author)))

            if roll == 'lose':
                await client.send_message(channel, '%s, you totally lost your points.. Your total is %s now' % (author, get_user_balance(author)))

        else:
            await client.send_message(channel, '%s, you do not have enough points to play a roulette.' % author)

client.run('MjU0MjU3MjIxMzYwMjg3NzQ1.CyMcHQ.NrTHeRYee9oDI5Tn8rQCghSArN8')
