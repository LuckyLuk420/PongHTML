from browser import window

gamejs = window.gamejs

def init(seed):
    gamejs.math.random.init(seed)

def choose(items):
    return gamejs.math.random.choose(items)

def integer(umin, umax):
    return gamejs.math.random.integer(umin, umax)

def random():
    return gamejs.math.random.random()

def vector(minvector, maxvector):
    return gamejs.math.random.vector(minvector, maxvector)

class Alea():
    
    def __init__(self, seed):
        self.alea = gamejs.math.random.Alea.new(seed)
    
    def choose(self, items):
        return self.alea.choose(items)
    
    def integer(self, umin, umax):
        return self.alea.integer(umin, umax)
    
    def random(self):
        return self.alea.random()
    
    def vector(self, umin, umax):
        return self.alea.vector(umin, umax)
