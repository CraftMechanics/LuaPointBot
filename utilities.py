import random
import urllib

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