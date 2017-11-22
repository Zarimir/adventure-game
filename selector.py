import config
from random import randint

def pick_in_range(minimum=0, maximum=None):
    if maximum != None:
        return pick_from_list(range(minimum, maximum))
    
def pick_from_list(items, minimum=None, maximum=None):
    if not items:
        return items
    else:
        if minimum == None:
            minimum = 0
        if maximum == None:
            maximum = len(items) - 1
        return items[randint(minimum, maximum)]

def pick_random(items):
    if not items:
        return items
    elif type(items) == dict:
        return pick_from_list([key for key in items])
    elif type(items) == int:
        return pick_in_range(maximum=items)
    else:
        return pick_from_list(items)

def pick_random_pair(items):
    key = pick_random(items)
    value = pick_random(items[key])
    return { "key" : key, "value" : value }
