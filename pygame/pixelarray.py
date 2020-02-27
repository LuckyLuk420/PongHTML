from browser import window

gamejs = window.gamejs

class UnsupportedClass(Exception):
    pass

class PixelArray():
    
    def __init__(self, surface):
        raise UnsupportedClass("PixelArray: This class is unsupported")
    
    surface = None
    itemsize = None
    ndim = None
    shape = None
    strides = None
    
    def make_surface(self):
        pass
    
    def replace(self, color, repcolor, distance=0, weights=(0.299, 0.587, 0.114)):
        pass
    
    def extract(self, array, distance=0, weights=(0.299, 0.587, 0.114)):
        pass
    
    def compare(self, array, distance=0, weights=(0.299, 0.587, 0.114)):
        pass
    
    def transpose(self):
        pass
