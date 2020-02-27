from browser import window

gamejs = window.gamejs

# returns didn't make much sense, just return it?
def remove(item, array):
    returns = None
    gamejs.utils.arrays.remove(item, array, returns)
    return returns

# I don't know how effective this is
def shuffle(array):
    return gamejs.utils.arrays.shuffle(array)
