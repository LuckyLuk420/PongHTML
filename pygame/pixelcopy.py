from browser import window
import pygame.surfarray

gamejs = window.gamejs

# opaque and clear are ignored
def surface_to_array(array, surface, kind='P', opaque=255, clear=0):
    surfarray = surfarray.get_surfacearray(surface)
    
    if kind == 'P':
        surfarray.arrayCopy(array, "p")
    elif kind == 'R':
        surfarray.arrayCopy(array, "r")
    elif kind == 'G':
        surfarray.arrayCopy(array, "g")
    elif kind == 'B':
        surfarray.arrayCopy(array, "b")
    elif kind == 'A':
        surfarray.arrayCopy(array, "a")
    elif kind == 'C' or kind == 'RGB':
        surfarray.arrayCopy(array, "c")

def array_to_surface(surface, array. from3d=False):
    dimensions = surface.get_size()
    newSurface = surfarray.make_surface(array, dimensions, from3d)
    surface.blit(newSurface)

def map_array(array3d, array2d, surface):
    surfarray = gamejs.graphics.SurfaceArray.new(surface.surface)
    surfarray.array3d = array3d
    surfarray.arrayCopy(array2d, 'm');

def make_surface(array, dimensions=None, from3d=False):
    return surfarray.make_surface(array, dimensions, from3d)
