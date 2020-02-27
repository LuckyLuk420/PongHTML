from browser import window

gamejs = window.gamejs

class UnsupportedClass(Exception):
    pass

class BufferProxy():
    
    def __init__(self):
        raise UnsupportedClass("BufferProxy: This class is unsupported")
    
    parent = None
    length = None
    raw = None
    
    def write(self, buffer, offset=0):
        pass