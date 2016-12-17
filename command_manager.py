import roll_cmd
import economy
import utilities

COMMAND_PREFIX = '!'

def is_command(message, label):
   return message.content.startswith('{}{}'.format(COMMAND_PREFIX, label))

def return_command_response(message):   
    user = message.author;

    if is_command(message, 'hello'):
        return 'Hello {}!'.format(user)

    if is_command(message, 'balance'):
        return '{}, your balance is {} {}'.format(user, economy.get_user_balance(user), economy.currency_name)

    if is_command(message, 'gift'):
        GIFT_AMOUNT = 15
        economy.add_to_user_balance(user, GIFT_AMOUNT)
        return '**MERRY CHRISTMAS** {}!\nHave a nice gift of {} {},\nand a merry christmas!'.format(user, GIFT_AMOUNT, economy.currency_name)

    if is_command(message, 'motherload'):
        MOTHERLOAD_AMOUNT = 100
        economy.add_to_user_balance(user, MOTHERLOAD_AMOUNT)
        return '__***MOTHERLOAD!***__\n{} received {} {}'.format(user, MOTHERLOAD_AMOUNT, economy.currency_name)

    if is_command(message, 'roll'):
        return roll_cmd.return_command_response(message)

    if is_command(message, 'cat'):
        CAT_GIF_PRICE = 25
        if economy.get_user_balance(user) >= CAT_GIF_PRICE:
            economy.withdraw_from_user_balance(user, CAT_GIF_PRICE)
            return 'Withdrawed {} {} from {}\nEnjoy your cat gif:\n{}'.format(CAT_GIF_PRICE, economy.currency_name, user, utilities.get_random_gif_by_tag('cat'))
        else:
            return '{}, you must have at least {} {} to summon a cat'.format(user, CAT_GIF_PRICE, economy.currency_name)

    if is_command(message, 'piano'):
        PIANO_PRICE = 100
        PIANO_URL = 'http://i.imgur.com/lQAIUT8.gifv'
        if economy.get_user_balance(user) >= PIANO_PRICE:
            economy.withdraw_from_user_balance(user, PIANO_PRICE)
            return 'Withdrawed {} from {}\nPlaying the piano:\n{}'.format(user, PIANO_PRICE, PIANO_URL)
        else:
            return '{}, you need {} for a piano'.format(user, PIANO_PRICE)

    if is_command(message, 'goat'):
        GOAT_GIF_PRICE = 40
        if economy.get_user_balance(user) >= GOAT_GIF_PRICE:
            economy.withdraw_from_user_balance(user, GOAT_GIF_PRICE)
            return 'Withdrawed {} {} from {}\nEnjoy your goat gif:\n{}'.format(GOAT_GIF_PRICE, economy.currency_name, user, utilities.get_random_gif_by_tag('goat'))
        else:
            return '{}, you must have at least {} {} to summon a goat'.format(user, GOAT_GIF_PRICE, economy.currency_name)
            
    if is_command(message, 'cube'):
        CUBE_GIF_PRICE = 70
        if economy.get_user_balance(user) >= CUBE_GIF_PRICE:
            economy.withdraw_from_user_balance(user, CUBE_GIF_PRICE)
            return 'Withdrawed {} {} from {}\nEnjoy your cube gif:\n{}'.format(CUBE_GIF_PRICE, economy.currency_name, user, utilities.get_random_gif_by_tag('cube'))
        else:
            return '{}, you must have at least {} {} to summon a cube'.format(user, CUBE_GIF_PRICE, economy.currency_name)

    return None
