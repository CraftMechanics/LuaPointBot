import economy

def return_command_response(message):
    return '{}, your balance is: {}'.format(message.author, economy.get_user_balance(message.author))