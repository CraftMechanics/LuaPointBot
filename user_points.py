import random

user_balance_dict = {'Placeholder' : 0}

GAMBLING_OUTCOMES = {'lose' : 10, 'double' : 5, 'keep' : 6, 'quadruple' : 2, 'JACKPOT' : 1}
GAMBLING_BET_AMOUNT = 10

CAT_GIF_PRICE = 20
SLOTS_PRICE = 20
PIANO_PRICE = 100
PIANO_URL = 'http://i.imgur.com/lQAIUT8.gifv'

def get_user_balance(user):
    if str(user) in user_balance_dict:
        return user_balance_dict[str(user)]
    else:
        user_balance_dict[str(user)] = 0
        return get_user_balance(user)

def set_user_balance(user, balance):
    user_balance_dict[str(user)] = balance;

def get_random_from_dict_by_weight(outcome_dict):
    total_weight = 0

    for outcome,weight in outcome_dict.items():
        total_weight += weight

    choice = random.randint(1, total_weight)

    counter = 1
    for outcome,weight in outcome_dict.items():
        if choice >= counter and choice < counter+weight:
            return outcome
        else:
            counter += weight
