import economy
import utilities

GAMBLING_OUTCOMES = {'lose' : 10, 'double' : 5, 'keep' : 6, 'quadruple' : 2, 'JACKPOT' : 1}
GAMBLING_BET_AMOUNT = 10

def return_command_response(message):
    author = message.author
    return_string = ""

    if economy.get_user_balance(author) >= GAMBLING_BET_AMOUNT:

        economy.set_user_balance(author, economy.get_user_balance(author) - GAMBLING_BET_AMOUNT)
        return_string = '{}You are gamble addicted {}!\nRolling a roulette for {} points...'.format(return_string, author , GAMBLING_BET_AMOUNT)

        roll = utilities.get_random_from_dict_by_weight(GAMBLING_OUTCOMES)

        if roll == 'double':
            economy.set_user_balance(author, economy.get_user_balance(author) + 2*GAMBLING_BET_AMOUNT)
            return_string += '{}Woah! {}, you doubled your points! Your total is {} now'.format(return_string, author, economy.get_user_balance(author))
        if roll == 'keep':
            economy.set_user_balance(author, economy.get_user_balance(author) + GAMBLING_BET_AMOUNT)
            return_string = '{}{}, you regained your points. Your total is {} now'.format(return_string, author, economy.get_user_balance(author))
        if roll == 'lose':
            return_string = '{}{}, you totally lost your points.. Your total is {} now'.format(return_string, author, economy.get_user_balance(author))
        if roll == 'quadruple':
            economy.set_user_balance(author, economy.get_user_balance(author) + 4*GAMBLING_BET_AMOUNT)
            return_string = '{}Incredible! {}, you just ***QUADRUPLED*** your points!! Your total is {} now'.format(return_string, author, economy.get_user_balance(author))
        if roll == 'JACKPOT':
            economy.set_user_balance(author, economy.get_user_balance(author) + 10*GAMBLING_BET_AMOUNT)
            return_string = '{}***__JACKPOT!!__***\n{}, you are very lucky! Your points just got multiplied x10! Your total is {} now'.format(return_string, author, economy.get_user_balance(author))
    else:
        return_string = '{}{}, you do not have enough points to play a roulette.'.format(return_string, author)

    return return_string
