import user_points
import random

def reply(command, message):
    author = message.author
    channel = message.channel

    if command == 'test':
        return ':ok_hand:'
    if command == 'hello':
        return 'Hello {}'.format(author)
    if command == 'balance':
        return '{}, your balance is: {}'.format(author, user_points.get_user_balance(author))
    if command == 'gift':
        user_points.set_user_balance(message.author, user_points.get_user_balance(message.author) + 10)
        return 'Congratulations {}! You have You have been awarded 10 lua points!\nYour current balance is {}'.format(author, user_points.get_user_balance(author))
    if command == 'motherload':
        user_points.set_user_balance(author, user_points.get_user_balance(author) + 100)
        return  'Congratulations {}! You have been awarded 100 lua points!\nYour current balance is {}'.format(author, user_points.get_user_balance(author))
    if command == 'roll':
        if user_points.get_user_balance(author) >= user_points.GAMBLING_BET_AMOUNT:
            replystr = 'You are gamble addicted {}!\nRolling a roulette for {} points...\n'.format(author,user_points.GAMBLING_BET_AMOUNT)
            roll = user_points.get_random_from_dict_by_weight(user_points.GAMBLING_OUTCOMES)
            user_points.set_user_balance(author, user_points.get_user_balance(author) - user_points.GAMBLING_BET_AMOUNT)
            if roll == 'double':
                user_points.set_user_balance(author, user_points.get_user_balance(author) + 2 * user_points.GAMBLING_BET_AMOUNT)
                print('double')
                return replystr+'Woah! {}, you doubled your points! Your total is now {}.'.format(author, user_points.get_user_balance(author))
            if roll == 'keep':
                user_points.set_user_balance(author, user_points.get_user_balance(author) + user_points.GAMBLING_BET_AMOUNT)
                print('keep')
                return replystr+'{}, you regained your points. Your total is now {}'.format(author, user_points.get_user_balance(author))
            if roll == 'lose':
                print('lose')
                return replystr+'{}, you totally lost your points.. Your total is now {}'.format(author, user_points.get_user_balance(author))
            if roll == 'quadruple':
                print('quad')
                user_points.set_user_balance(author, user_points.get_user_balance(author) + 4*user_points.GAMBLING_BET_AMOUNT)
                return replystr+'Incredible! {}, you just ***QUADRUPLED*** your points!! Your total is now {}'.format(author, user_points.get_user_balance(author))
            if roll == 'JACKPOT':
                print('jack')
                user_points.set_user_balance(author, user_points.get_user_balance(author) + 10*user_points.GAMBLING_BET_AMOUNT)
                return replystr+'***__JACKPOT!!__***\n{}, you are very lucky! Your points just got multiplied x10! Your total is now {}'.format(author, user_points.get_user_balance(author))
        else:
            return '{}, you do not have enough points to play a roulette.'.format(author)

    if command == 'cat':
        if user_points.get_user_balance(author) >= user_points.CAT_GIF_PRICE:
            user_points.set_user_balance(author, user_points.get_user_balance(author) - user_points.CAT_GIF_PRICE)
            return 'Took {} from {}\n Have your cat gif:\n{}{}{}'.format(user_points.CAT_GIF_PRICE, author, 'http://www.catgifpage.com/gifs/', random.randint(1,310), '.gif')
        else:
            return '{}, you need {} to summon a cat'.format(author, CAT_GIF_PRICE)

    if command == 'piano':
        if user_points.get_user_balance(author) >= user_points.PIANO_PRICE:
            user_points.set_user_balance(author, user_points.get_user_balance(author) - user_points.PIANO_PRICE)
            return 'Withdrew {} from {}\nPlaying the piano: {}'.format(user_points.PIANO_PRICE, author, user_points.PIANO_URL)
        else:
            return '{}, you need {} for a piano'.format(author, user_points.PIANO_PRICE)
