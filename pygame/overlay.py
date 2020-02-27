from browser import window

gamejs = window.gamejs

class UnsupportedClass(Exception):
    pass

class Overlay():
    
    def __init__(self, formt, dimensions):
        raise UnsupportedClass("Overlay: This class is unsupported")
    
    def display(self, yuv=None):
        pass
    
    def set_location(self, rect):
        pass
    
    def get_hardware(self, rect):
        pass
