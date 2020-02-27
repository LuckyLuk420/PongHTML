from browser import window
from .surface import Surface

gamejs = window.gamejs

class UnsupportedMethod(Exception):
    pass

"""
we don't have numpy array support, SO, the functionality of this module
does NOT match pygame exactly, here are differences:

1.  The returned array for array2d is a JavaScript Uint32Array
    The returned array for array_* is a JavaScript Uint8ClampedArray

2.  The returned array for array3d is a structure where:

    array[y][x][rgba] where rgba is 0 for red, 1 for green, 2, for blue, and 3 for alpha
    
3.  The returned array IS NOT linked to the Surface like it can be in pygame

4.  make_surface requires a tuple of dimensions

In the future, the functionality of this module may increase

In the meantime, these functions are SLOW and intensive... you'd be better served
using the augmented functions to interact with GameJS Surface Arrays

"""

def array2d(surface):
    array = gamejs.graphics.SurfaceArray.new(surface.surface)
    return array.buf32

def pixels2d(surface):
    raise UnsupportedMethod("surfarray: pixels2d() not supported")

def array3d(surface):
    array = gamejs.graphics.SurfaceArray.new(surface.surface)
    return array.array3d

def pixels3d(surface):
    raise UnsupportedMethod("surfarray: pixels3d() not supported")

def array_alpha(surface):
    array = gamejs.graphics.SurfaceArray.new(surface.surface)
    return array.alpha

def pixels_alpha(surface):
    raise UnsupportedMethod("surfarray: pixels_alpha() not supported")

def array_red(surface):
    array = gamejs.graphics.SurfaceArray.new(surface.surface)
    return array.red

def pixels_red(surface):
    raise UnsupportedMethod("surfarray: pixels_red() not supported")

def array_green(surface):
    array = gamejs.graphics.SurfaceArray.new(surface.surface)
    return array.green

def pixels_green(surface):
    raise UnsupportedMethod("surfarray: pixels_green() not supported")

def array_blue(surface):
    array = gamejs.graphics.SurfaceArray.new(surface.surface)
    return array.blue

def pixels_blue(surface):
    raise UnsupportedMethod("surfarray: pixels_blue() not supported")

def array_colorkey(surface):
    raise UnsupportedMethod("surfarray: array_colorkey() not supported")

# array must be a JavaScript Uint32Array, retrieved from array2d
# if array is retrieved from array3d set from3d=True
def make_surface(array, dimensions=None, from3d=False):
    if not dimensions:
        raise UnsupportedMethod("surfarray: make_surface() not supported without dimensions")
    surface = gamejs.graphics.Surface.new(dimensions[0], dimensions[1])
    surfarray = gamejs.graphics.SurfaceArray.new(surface)
    if not from3d:
        surfarray.makeSurface(array)
    else:
        surfarray.makeSurface3d(array)
    return Surface(dimensions=(0,0), fromSurface=surfarray.surface)

# does not offer optimization pygame does
def blit_array(surface, array, from3d=False):
    dimensions = surface.get_size()
    newSurface = make_surface(array, dimensions, from3d)
    surface.blit(newSurface)

def map_array(surface, array3d):
    surfarray = gamejs.graphics.SurfaceArray.new(surface.surface)
    return surfarray.mapArray(array3d)

# augmentation
def get_surfacearray(surface):
    return gamejs.graphics.SurfaceArray.new(surface.surface)

# deprecated functions, not really sure what they do

def use_arraytype():
    raise UnsupportedMethod("surfarray: use_arraytype() not supported [deprecated]")

def get_arraytype():
    raise UnsupportedMethod("surfarray: get_arraytype() not supported [deprecated]")

def get_arraytypes():
    raise UnsupportedMethod("surfarray: use_arraytypes() not supported [deprecated]")
