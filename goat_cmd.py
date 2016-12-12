import economy
import json
import requests
import utilities

GOAT_GIF_PRICE = 30

def return_command_response(message):
    author = message.author
    
    if economy.get_user_balance(author) >= GOAT_GIF_PRICE:
        economy.set_user_balance(author, economy.get_user_balance(author)-GOAT_GIF_PRICE)
        response = requests.get(url='http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=goat')
        data = response.json()
        gif = data['data']['url']

        return 'Took {} from {}.\nEnjoy your goat gif!\n{}'.format(GOAT_GIF_PRICE, author, gif)
    
    else:
        return '{}, you need {} for a goat gif'.format(author, GOAT_GIF_PRICE)