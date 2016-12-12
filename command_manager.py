import hello_cmd
import balance_cmd
import gift_cmd
import motherload_cmd
import roll_cmd
import cat_cmd
import piano_cmd

COMMAND_PREFIX = '!'

def is_command(message, label):
   return message.content.startswith('{}{}'.format(COMMAND_PREFIX, label))

def return_command_response(message):   
    
    if is_command(message, 'hello'):
        return hello_cmd.return_command_response(message)

    if is_command(message, 'balance'):
        return balance_cmd.return_command_response(message)

    if is_command(message, 'gift'):
        return gift_cmd.return_command_response(message)

    if is_command(message, 'motherload'):
        return motherload_cmd.return_command_response(message)

    if is_command(message, 'roll'):
        return roll_cmd.return_command_response

    if is_command(message, 'cat'):
        return cat_cmd.return_command_response(message)

    if is_command(message, 'piano'):
        return piano_cmd.return_command_response(message)

    return None
