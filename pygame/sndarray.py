from browser import window
import pygame.mixer

gamejs = window.gamejs

class UnsupportedFunction(Exception):
    pass

def array(sound):
    return sound.getRaw()

# currently not supported, I don't know how I'd link an array
# Could be implemented in the future?
def samples(sound):
    raise UnsupportedFunction("sndarray.samples: unsupported function")

def make_sound(array):
    return pygame.mixer.Sound([array])

def use_arraytype(arrayType):
    raise UnsupportedFunction("sndarray.use_arraytype: unsupported function [DEPRECATED]")

def get_arraytype(arrayType):
    raise UnsupportedFunction("sndarray.get_arraytype: unsupported function [DEPRECATED]")

def get_arraytypes(arrayType):
    raise UnsupportedFunction("sndarray.get_arraytypes: unsupported function [DEPRECATED]")
