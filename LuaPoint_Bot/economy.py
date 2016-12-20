user_balance_dict = {}
currency_name = 'lua points'

def get_user_balance(user):
    if str(user) in user_balance_dict:
        return user_balance_dict[str(user)]
    else:
        user_balance_dict[str(user)] = 0
        return get_user_balance(user)

def set_user_balance(user, balance):
    user_balance_dict[str(user)] = balance

def add_to_user_balance(user, amount):
    set_user_balance(user, get_user_balance(user)+amount)

def withdraw_from_user_balance(user, amount):
    set_user_balance(user, get_user_balance(user)-amount)
