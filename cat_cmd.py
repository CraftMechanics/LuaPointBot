import economy

CAT_GIF_PRICE = 20

def return_command_response(message):
    author = message.author

    if get_user_balance(author) >= CAT_GIF_PRICE:
        set_user_balance(author, get_user_balance(author) - CAT_GIF_PRICE)
        return 'Took {} from {}\n Have your cat gif:\n{}{}{}'.format(CAT_GIF_PRICE, author, 'http://www.catgifpage.com/gifs/', random.randint(1,310), '.gif')
    else:
        return '{}, you need {} to summon a cat'.format(author, CAT_GIF_PRICE)