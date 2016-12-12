import economy

PIANO_PRICE = 100
PIANO_URL = 'http://i.imgur.com/lQAIUT8.gifv'

def return_command_response(message):
    author = message.author

    if economy.get_user_balance(author) >= PIANO_PRICE:
        economy.set_user_balance(author, economy.get_user_balance(author) - PIANO_PRICE)
        return 'Withdrawed {} from %s\nPlaying the piano: %s'.format(author, PIANO_PRICE, PIANO_URL)
    else:
        return '{}, you need {} for a piano'.format(author, PIANO_PRICE)