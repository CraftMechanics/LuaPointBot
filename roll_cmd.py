import economy
import utilities

GAMBLING_OUTCOMES = {'lose' : 10, 'double' : 5, 'keep' : 6, 'quadruple' : 2, 'JACKPOT' : 1}
GAMBLING_BET_AMOUNT = 10

def return_command_response(message):
    user = message.author
    return_string = ""

    if economy.get_user_balance(user) >= GAMBLING_BET_AMOUNT:

        economy.withdraw_from_user_balance(user, GAMBLING_BET_AMOUNT)
        return_string = '{}You are gamble addicted {}!\nRolling a roulette for {} points...'.format(return_string, user, GAMBLING_BET_AMOUNT)

        roll = utilities.get_random_from_dict_by_weight(GAMBLING_OUTCOMES)

        if roll == 'double':
            economy.add_to_user_balance(user, GAMBLING_BET_AMOUNT*2)
            return_string = '{}Woah! {}, you doubled your points! Your total is {} now'.format(return_string, user, economy.get_user_balance(user))
        if roll == 'keep':
            economy.add_to_user_balance(user, GAMBLING_BET_AMOUNT)
            return_string = '{}{}, you regained your points. Your total is {} now'.format(return_string, user, economy.get_user_balance(user))
        if roll == 'lose':
            return_string = '{}{}, you totally lost your points.. Your total is {} now'.format(return_string, user, economy.get_user_balance(user))
        if roll == 'quadruple':
            economy.add_to_user_balance(user, GAMBLING_BET_AMOUNT*4)
            return_string = '{}Incredible! {}, you just ***QUADRUPLED*** your points!! Your total is {} now'.format(return_string, user, economy.get_user_balance(user))
        if roll == 'JACKPOT':
            economy.add_to_user_balance(user, GAMBLING_BET_AMOUNT*10)
            return_string = '{}***__JACKPOT!!__***\n{}, you are very lucky! Your points just got multiplied x10! Your total is {} now'.format(return_string, user, economy.get_user_balance(userr))
    else:
        return_string = '{}{}, you do not have enough points to play a roulette.'.format(return_string, user)

    return return_string
