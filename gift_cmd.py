import economy

GIFT_AMOUNT = 10

def return_command_response(message):
    author = message.author
    economy.set_user_balance(author, economy.get_user_balance(author) + GIFT_AMOUNT)
    return 'Congratulations {}! You have been awarded {} lua points!\nYour current balance is {}'.format(author, GIFT_AMOUNT, economy.get_user_balance(author))