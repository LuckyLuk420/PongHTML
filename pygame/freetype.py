from browser import window
from .locals import *
from .color import Color

gamejs = window.gamejs

class UnsupportedFunction(Exception):
    pass

class UnsupportedClass(Exception):
    pass

def get_error():
    raise UnsupportedFunction("freetype.get_error: unsupported function")

def get_version():
    raise UnsupportedFunction("freetype.get_version: unsupported function")

def init(cache_size=64, resolution=72):
    raise UnsupportedFunction("freetype.init: unsupported function")

def quit():
    raise UnsupportedFunction("freetype.quit: unsupported function")

def was_init():
    raise UnsupportedFunction("freetype.was_init: unsupported function")

def get_cache_size():
    raise UnsupportedFunction("freetype.get_cache_size: unsupported function")

def get_default_resolution():
    raise UnsupportedFunction("freetype.get_default_resolution: unsupported function")

def set_default_resolution(resolution=72):
    raise UnsupportedFunction("freetype.set_default_resolution: unsupported function")

def get_default_font():
    raise UnsupportedFunction("freetype.get_default_font: unsupported function")

class Font():
    
    def __init__(self, ufile, size=0, font_index=0, resolution=0, ucs4=False):
        self.name = ""
        self.path = ""
        self.size = 0
        self.height = 0
        self.ascender = 0
        self.descender = 0
        self.underline = False
        self.strong = False
        self.oblique = False
        self.wide = False
        self.strength = 0.0
        self.underline_adjustment = 0.0
        self.fixed_width = False
        self.fixed_sizes = 0
        self.scalable = False
        self.use_bitmap_strikes = False
        self.antialiased = False
        self.kerning = False
        self.vertical = False
        self.rotation = False
        self.fgcolor = Color(0,0,0);
        self.origin = False
        self.pad = False
        self.ucs4 = False
        self.resolution = False
        raise UnsupportedClass("freetype.Font: unsupported class")
    
    def get_rect(self, text, style=STYLE_DEFAULT, rotation=0, size=0):
        pass
    
    def get_metrics(self, text, size=0):
        pass
    
    def get_sized_ascender(self, size=0):
        pass
    
    def get_sized_descender(self, size=0):
        pass
    
    def get_sized_height(self, size=0):
        pass
    
    def get_sized_glyph_height(self, size=0):
        pass
    
    def get_sizes(self):
        pass
    
    def render(self, surface, dest, text, fgcolor=None, bgcolor=None, style=STYLE_DEFAULT, rotation=0, size=0):
        pass
    
    def render_to(self, surface, dest, text, fgcolor=None, bgcolor=None, style=STYLE_DEFAULT, rotation=0, size=0):
        pass
    
    def render_raw(self, text, dest=None, style=STYLE_DEFAULT, rotation=0, size=0, invert=False):
        pass
    
    def render_raw_to(self, array, text, dest=None, style=STYLE_DEFAULT, rotation=0, size=0, invert=False):
        pass

class Sysfont(Font):
    
    def __init__(self, name, size, bold=False, italic=False):
        raise UnsupportedClass("freetype.SysFont: unsuppored classs")
    