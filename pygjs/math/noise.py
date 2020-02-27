from browser import window

gamejs = window.gamejs

class Simplex():
    
    # currently I believe this randomNumberGenerator must be a javascript object
    def __init__(self, randomNumberGenerator):
        self.simplex = gamejs.math.noise.Simplex.new(randomNumberGenerator)
    
    def get(self, x, y):
        return self.simplex.get(x, y)
    
    def get3d(self, x, y, z):
        return self.simplex.get3d(x, y, z)
