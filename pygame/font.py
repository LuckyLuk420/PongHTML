from browser import window, console
from .color import Color
from .surface import Surface
import pygame.draw

gamejs = window.gamejs

class UnsupportedMethod(Exception):
    pass

def init():
    pass

def quit():
    pass

def get_init():
    return True

def get_default_font():
    return "sans-serif"

# what do I return?
def get_fonts():
    return []

# yeah we're not supplying file paths
def match_font(name, bold=False, italic=False):
    return ""

# can support italicizing and bolding, but not metrics
class SysFont():
    
    def __init__(self, css, size=None, bold=False, italic=False, backgroundColor=None):
        self.originalCSS = css
        if size:
            css = str(size) + "px " + css
            self.tsize = size
        if bold:
            css = "bold " + css
            self.bold = True
        if italic:
            css = "italic" + css
            self.italic = True
        if not backgroundColor:
            backgroundColor = Color(255, 255, 255)
        self.underline = False
        self.background = backgroundColor
        self.css = css
        self.font = gamejs.font.Font.new(css, backgroundColor.getRGBA(), self.underline)
    
    def render(self, text, antialias, color, background=None):
        font = None
        if background:
            font = gamejs.font.Font.new(self.css, background.getRGBA(), self.underline)
        else:
            font = self.font
        
        return Surface(dimensions=(0,0), fromSurface=font.render(text, color.getRGBA()))

    def size(self, text):
        ret = Surface(dimensions=(0,0), fromSurface=self.font.render(text, color.getRGBA()))
        return ret.get_size()
    
    def set_underline(self, underline):
        self.underline = underline
        if self.underline:
            css = self.originalCSS
            if self.tsize:
                css = str(self.tsize) + "px " + css
            if self.bold:
                css = "bold " + css
            if self.italic:
                css = "italic " + css
            self.css = css
            if self.underline:
                self.font = gamejs.font.Font.new(css, self.backgroundColor.getRGBA(), True);
    
    def get_underline(self):
        return self.underline
    
    def set_bold(self, bold):
        self.bold = bold
        if self.bold:
            css = self.originalCSS
            if self.tsize:
                css = str(self.tsize) + "px " + css
            css = "bold " + css
            if self.italic:
                css = "italic" + css
            self.css = css
            self.font = gamejs.font.Font.new(css, self.backgroundColor.getRGBA(), self.underline)
    
    def get_bold(self):
        return self.bold
    
    def set_italic(self, italic):
        self.italic = italic
        if self.italic:
            css = self.originalCSS
            if self.tsize:
                css = str(self.tsize) + "px " + css
            if self.bold:
                css = "bold " + css
            css = "italic " + css
            self.css = css
            self.font = gamejs.font.Font.new(css, self.backgroundColor.getRGBA(), self.underline)
    
    def get_italic(self):
        return self.italic

    def metrics(self, text):
        # I'm not sure how I'd implement this from a CSS font
        return None
    
    def get_linesize(self):
        return self.font.fontHeight + 5
    
    def get_height(self):
        return self.font.fontHeight
    
    def get_ascent(self):
        # until TextMetrics supports is universal, this is futile
        return None
    
    def get_descent(self):
        # until TextMetrics supports is universal, this is futile
        return None
    
    # augmentation
    def set_background_color(self, backgroundColor):
        self.backgroundColor = backgroundColor
    
    def get_size(self):
        return self.tsize
    
    def set_size(self, size):
        self.tsize = size
        css = self.originalCSS
        if self.tsize:
            css = str(self.tsize) + "px " + css
        if self.bold:
            css = "bold " + css
        if self.italic:
            css = "italic" + css
        self.font = gamejs.font.Font.new(css, self.backgroundColor.getRGBA(), self.underline)

# if you want italics and boldness you'll have to supply a file
class Font():
    
    def __init__(self, name, size):
        self.background = Color(255, 255, 255)
        self.bold = False
        self.italic = False
        self.underline = False
        self.tsize = size
        self.font = gamejs.font.load(name)
        
    # augmentation
    def set_size(self, size):
        self.tsize = size
    
    def get_size(self):
        return self.tsize
    
    def size(self, text):
        height = self.font.getAdvanceWidth("M", self.tsize) * 1.5
        width = self.font.getAdvanceWidth(text, self.tsize)
        return (width, height)
    
    def render(self, text, antialias, color, background=None):
        size = self.size(text)
        surface = Surface(dimensions=(size[0], size[1]))
        ctx = surface.surface.context
        self.font.draw(ctx, text, 0, self.tsize, self.tsize)
        if self.underline:
            pygame.draw.line(surface, color, [0,self.tsize], [size[0], self.tsize])
        return surface
    
    def set_underline(self, underline):
        self.underline = underline
    
    def get_underline(self):
        return self.underline
    
    # supply a bold file instead
    def set_bold(self, bold):
        if bold:
            raise UnsupportedMethod("Font: set_bold is unsupported")
    
    def get_bold(self):
        return self.bold
    
    def set_italic(self, italic):
        if italic:
            raise UnsupportedMethod("Font: set_italic is unsupported")
    
    def get_italic(self):
        return self.italic
    
    def metrics(self, text):
        ret = []
        for char in text:
            glyph = self.font.charToGlyph(char)
            ret.append((glyph.xMin, glyph.xMax, glyph.yMin, glyph.yMax, glyph.advanceWidth))
        return ret
    
    def get_linesize(self):
        size = self.size("kj")
        size[1] += 5
        return size[1]
    
    def get_height(self):
        size = self.size("kj")
        return size[1]
    
    # these return font units, not pixels
    # I don't know how to convert them
    def get_ascent(self):
        return self.font.ascender
    
    def get_descent(self):
        return self.font.descender
    