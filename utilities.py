import random
import urllib
import json
import requests

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

def get_random_gif_by_tag(tag):    
    response = requests.get(url='http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag={}'.format(tag))
    data = response.json()
    gif = data['data']['url']
    return gif
