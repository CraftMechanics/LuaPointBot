import economy

MOTHERLOAD_AMOUNT = 100

def return_command_response(message):
    author = message.author
    economy.set_user_balance(author, economy.get_user_balance(author) + MOTHERLOAD_AMOUNT)
    return 'Congratulations {}! You have been awarded {} lua points!\nYour current balance is {}'.format(author, MOTHERLOAD_AMOUNT, economy.get_user_balance(author))