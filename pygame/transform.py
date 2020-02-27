from browser import window
import pygame.surfarray
from .color import Color

gamejs = window.gamejs

class UnsupportedFunction(Exception):
    pass

def flip(surface, xbool, ybool):
    return Surface(dimensions=(0,0), fromSurface=surface.surface.flip(xbool, ybool))

def scale(surface, dimensions, destsurface=None):
    ret = surface.resize(dimensions)
    if destsurface:
        destsurface.surface = ret.surface
        destsurface.colorkey = ret.colorkey
        destsurface.clip = ret.clip
    return ret

def rotate(surface, angle):
    return Surface(dimensions=(0,0), fromSurface=surface.surface.rotate(angle))

def rotozoom(surface, angle, scale):
    ret = surface.scale(scale)
    ret = rotate(ret, angle)
    return ret

# factor added as augmentation
def scale2x(surface, destsurface=None, factor=2):
    ret = surface.scale(factor)
    if destsurface:
        destsurface.surface = ret.surface
        destsurface.colorkey = ret.colorkey
        destsurface.clip = ret.clip
    return ret

def smoothscale(surface, dimensions, destsurface=None):
    ret = surface.resize(dimensions)
    if destsurface:
        destsurface.surface = ret.surface
        destsurface.colorkey = ret.colorkey
        destsurface.clip = ret.clip
    return ret

def get_smoothscale_backend():
    return "GENERIC"

def set_smoothscale_backend(backend):
    pass

# I don't understand what this function does
def chop(surface, rect):
    raise UnsupportedFunction("transform.chop: unsupported function")

# Not currently supported
def laplacian(surface, destsurface=None):
    raise UnsupportedFunction("transform.laplacian: unsupported function")

def average_surfaces(surfaces, destsurface=None, pallete_colors=1):
    raise UnsupportedFunction("transform.average_surfaces: unsupported function")

def average_color(surface, rect=None):
    surfarray = pygame.surfarray.get_surfacearray(surface)
    color = None
    if rect:
        color = surfarray.averageColor(rect.rect)
    else:
        color = surfarray.averageColor()
    return Color(color[0], color[1]. color[2]. color[3])

def threshold(destsurface, surface, color, threhold=(0,0,0,0), diff_color=(0,0,0,0), change_return=1, usurface=None, inverse=False):
    raise UnsupportedFunction("transform.threshold: unsupported funciton")
