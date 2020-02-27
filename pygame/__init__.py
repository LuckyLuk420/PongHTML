from .locals import *
import pygame.time
from .rect import Rect
from .color import Color
from .surface import Surface
import pygame.draw
import pygame.font
import pygame.freetype
import pygame.image
import pygame.surfarray
import pygame.transform
from .pixelarray import PixelArray
from .bufferproxy import BufferProxy
from .overlay import Overlay
import pygame.display
import pygame.sprite
import pygame.mixer
import pygame.sndarray
import pygame.event
import pygame.key
import pygame.mouse
import pygame.joystick
from datetime import datetime

#unsupported as of now
import pygame.cursors

start_time = datetime.now()

def init():
    pass

def quit():
    for f in quit.callbacks:
        f()

quit.callbacks = []

class error(Exception):
    pass

def get_error():
    raise error("get_error() not supported")

def set_error():
    raise error("set_error() not supported")

# returns GameJS version
def get_sdl_version():
    return (2, 0, 3)

LIL_ENDIAN = 0
BIG_ENDIAN = 1

def get_sdl_byteorder():
    return -1

def register_quit(func):
    quit.callbacks.append(func)

def encode_string(obj, encoding=None, errors=None, etype=None):
    raise error("encode_string not supported, use other methods")

def encode_file_path(obj, etype=None):
    raise error("encode_file_path not supported, use other methods")

class Version():
    
    def __init__(self):
        self.ver = "1.0"
        self.vernum = (1)
        self.rev = "+"

version = Version()

from browser import window

gamejs = window.gamejs

def preload(resources):
    gamejs.preload(resources)
    