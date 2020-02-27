from browser import window
from .rect import Rect
from .color import Color

gamejs = window.gamejs

class UnsupportedMethod(Exception):
    pass

class OutOfBounds(Exception):
    pass

USE_ORIGINAL = 1

class Surface():
    
    def __init__(self, dimensions, flags=0, depth=0, masks=None, fromSurface=None):
        if fromSurface == None:
            self.surface = gamejs.graphics.Surface.new(dimensions)
        else:
            self.surface = fromSurface
        self.colorkey = None
        dimensions = self.surface.getSize()
        self.clip = Rect(0, 0, dimensions[0], dimensions[1])
    
    def blit(self, source, dest=Rect(), area=None, special_flags=0):
        if not area:
            area = [0,0]
        self.surface.blit(source.surface, dest.rect, area, special_flags)
    
    def convert(self):
        pass
    
    def convert_alpha(self):
        pass
    
    def copy(self):
        return Surface(dimensions=(0,0), fromSurface=self.surface.copy())
    
    def fill(self, color, rect=None, special_flags=0):
        if isinstance(color, Color):
            color = color.getRGBA()
        elif type(color) is tuple or type(color) is list:
            if len(color) == 4:
                color = 'rgba(' + str(color[0]) + ', ' + str(color[1]) + ', ' + str(color[2]) + ', ' + str(color[3]) + ')'
            else:
                color = 'rgba(' + str(color[0]) + ', ' + str(color[1]) + ', ' + str(color[2]) + ', 1.0)'
        if not rect:
            dimensions = self.surface.getSize()
            rect = Rect(0, 0, dimensions[0], dimensions[1])
        self.surface.fill(color, rect.rect)
    
    # I don't understand what this is supposed to do, come back later
    def scroll(self):
        raise UnsupportedMethod("Surface: scroll() is unsupported")
    
    def get_colorkey(self):
        return self.colorkey
    
    # USE_ORIGINAL as flag so that 0-255 values aren't smudged during internal conversion
    # This MODIFIES the surface (not how pygame does it), provided for compatibility
    def set_colorkey(self, color, flags=0):
        if not color:
            self.colorkey = None
            return
        
        if isinstance(color, Color):
            if flags == USE_ORIGINAL:
                color = color.original
            else:
                color = color.rgb
        
        dimensions = self.surface.getSize()
        srfarray = gamejs.graphics.SurfaceArray.new(self.surface)
        self.surface = srfarray.setColorKey(color)
    
    def set_alpha(self, value=None, flags=0):
        if not value:
            self.surface.setAlpha(1)
        else:
            self.surface.setAlpha((value / 255))
    
    def get_alpha(self):
        return int(self.surface.getAlpha() * 255)
    
    def lock(self):
        pass
    
    def unlock(self):
        pass
    
    def mustlock(self):
        return False
    
    def get_locked(self):
        return False
    
    def get_locks(self):
        return ()
    
    def get_at(self, coords):
        x = coords[0]
        y = coords[1]
        
        dimensions = self.surface.getSize()
        if x < 0 or x > dimensions[0]:
            raise OutOfBounds("Surface: get_at() x out of bounds")
        if y < 0 or y > dimensions[1]:
            raise OutOfBounds("Surface: get_at() y out of bounds")
        srfarray = gamejs.graphics.SurfaceArray.new(self.surface)
        px = srfarray.get(x, y)
        return Color(px[0], px[1], px[2], px[3])
    
    def set_at(self, coords, color):
        if isinstance(color, Color):
            color = color.rgb + (color.alpha,)
        x = coords[0]
        y = coords[1]
        
        dimensions = self.surface.getSize()
        if x < 0 or x > dimensions[0]:
            raise OutOfBounds("Surface: set_at() x out of bounds")
        if y < 0 or y > dimensions[1]:
            raise OutOfBounds("Surface: set_at() y out of bounds")
        srfarray = gamejs.graphics.SurfaceArray.new(self.surface)
        srfarray.set(x, y, color)
        gamejs.graphics.blitArray(self.surface, srfarray)
    
    def get_at_mapped(self, coords):
        raise UnsupportedMethod("Surface: get_at_mapped() is unsupported")
    
    def get_clip(self):
        return self.clip
    
    # in canvas context a clip is a permanent state change here
    def set_clip(self, rect=None):
        dimensions = self.surface.getSize()
        
        if not rect:
            self.clip = Rect(0, 0, dimensions[0], dimensions[1])
        else:
            if rect.left < 0:
                rect.left = 0
            elif rect.left > dimensions[0]:
                return self.set_clip()
            if rect.top < 0:
                rect.top = 0
            elif rect.top > dimensions[1]:
                return self.set_clip()
            
            if rect.left + rect.width > dimensions[0]:
                rect.width = dimensions[0] - rect.left
            if rect.top + rect.height > dimensions[1]:
                rect.height = dimensions[1] - rect.top
            
            self.clip = rect
            
        context = self.surface.context
        r = context.rect(self.clip.left, self.clip.top, self.clip.width, self.clip.height)
        context.clip(r, 'nonzero')
    
    def get_size(self):
        return self.surface.getSize()
    
    def get_width(self):
        dimensions = self.surface.getSize()
        return dimensions[0]
    
    def get_height(self):
        dimensions = self.surface.getSize()
        return dimensions[1]
    
    def get_rect(self, **kwargs):
        dimensions = self.surface.getSize()
        ret = Rect(0, 0, dimensions[0], dimensions[1])
        for key, value in kwargs.items():
            setattr(ret, key, value)
        return ret
    
    def get_bitsize(self):
        return 32
    
    def get_bytesize(self):
        return 4
    
    def map_rgb(self, color):
        return (color.a << 24) | (color.b << 16) | (color.g << 8) | (color.r)
    
    def unmap_rgb(self, mapped_int):
        return Color(mapped_int & 0xFF,(mapped_int >> 8) & 0xFF,(mapped_int >> 16) & 0xFF,(mapped_int >> 24) & 0xFF)
    
    # added for this frankenstein
    def resize(self, dimensions):
        return Surface(dimensions=(0,0), fromSurface=self.surface.scale(dimensions))
    
    def scale(self, factor):
        return Surface(dimensions=(0,0), fromSurface=self.surface.resize(factor))
    
    # not supported at the moment
    def get_palette(self):
        return ()
    
    def get_palette_at(self, index):
        return (0, 0, 0)
    
    def set_palette(self, palette):
        return None
    
    def set_palette_at(self, index, rgb):
        return None
    
    def get_flags(self):
        return 0
    
    def get_pitch(self):
        return 0
    
    def get_masks(self):
        return (0, 0, 0, 0)
    
    def set_masks(self, masks):
        return None
    
    def get_shifts(self):
        return (0, 0, 0, 0)
    
    def set_shifts(self, shifts):
        return None
    
    def get_losses(self):
        return (0, 0, 0, 0)
    
    def get_bounding_rect(self):
        return self.get_rect()
    
    # subsurfaces can traditionally have alternative clipping and color keys
    # we don't support those
    def subsurface(self):
        raise UnsupportedMethod("Surface: subsurface() is unsupported")
    
    def get_parent(self):
        raise UnsupportedMethod("Surface: get_parent() is unsupported")
    
    def get_abs_parent(self):
        raise UnsupportedMethod("Surface: get_abs_parent() is unsupported")
    
    def get_offset(self):
        raise UnsupportedMethod("Surface: get_offset() is unsupported")
    
    def get_abs_offset(self):
        raise UnsupportedMethod("Surface: get_abs_offset() is unsupported")
    
    def get_view(self):
        raise UnsupportedMethod("Surface: get_view() is unsupported")
    
    def get_buffer(self):
        raise UnsupportedMethod("Surface: get_buffer() is unsupported")
    
    def get_pixels_address(self):
        raise UnsupportedMethod("Surface: _pixels_address is unsupported")
    
    _pixels_address = property(get_pixels_address)
    