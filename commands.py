import discord
import asyncio
client = discord.Client()

@client.event
async def on_message(message):
    chatlogging.cmdlog(message)
    author = message.author
    channel = message.channel

    if is_command(message, 'hello'):
        await client.send_message(channel, 'Hello {}'.format(author))

    if is_command(message, 'balance'):
        await client.send_message(channel, '{}, your balance is: {}'.format(author, get_user_balance(author)))

    if is_command(message, 'gift'):
        set_user_balance(message.author, get_user_balance(message.author) + 10)
        await client.send_message(message.channel, 'Congratulations {}! You have been awarded 10 lua points!\nYour current balance is {}'.format(author, get_user_balance(author)))

    if is_command(message, 'motherload'):
        set_user_balance(author, get_user_balance(author) + 100)
        await client.send_message(channel, 'Congratulations {}! You have been awarded 100 lua points!\nYour current balance is {}'.format(author, get_user_balance(author)))

    if is_command(message, 'roll'):
        if get_user_balance(author) >= GAMBLING_BET_AMOUNT:
            roll = get_random_from_dict_by_weight(GAMBLING_OUTCOMES)
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

    if is_command(message, 'cat'):
        if get_user_balance(author) >= CAT_GIF_PRICE:
            set_user_balance(author, get_user_balance(author) - CAT_GIF_PRICE)
            await client.send_message(channel, 'Took %s from %s\n Have your cat gif:\n%s%s%s' % (CAT_GIF_PRICE, author, 'http://www.catgifpage.com/gifs/', random.randint(1,310), '.gif'))
        else:
            await client.send_message(channel, '%s, you need %s to summon a cat' % (author, CAT_GIF_PRICE))

    if is_command(message, 'piano'):
        if get_user_balance(author) >= PIANO_PRICE:
            set_user_balance(author, get_user_balance(author) - PIANO_PRICE)
            await client.send_message(channel, 'Withdrawed %s from %s\nPlaying the piano: %s' % (author, PIANO_PRICE, PIANO_URL))
        else:
            await client.send_message(channel, '%s, you need %s for a piano' % (author, PIANO_PRICE))
