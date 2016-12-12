import economy
import random

CAT_GIF_PRICE = 20

def return_command_response(message):
    author = message.author

    if economy.get_user_balance(author) >= CAT_GIF_PRICE:
        economy.set_user_balance(author, economy.get_user_balance(author) - CAT_GIF_PRICE)
        return 'Took {} from {}\n Have your cat gif:\n{}{}{}'.format(CAT_GIF_PRICE, author, 'http://www.catgifpage.com/gifs/', random.randint(1,310), '.gif')
    else:
        return '{}, you need {} to summon a cat'.format(author, CAT_GIF_PRICE)