from browser import window
from .surface import Surface

gamejs = window.gamejs

class UnsupportedMethod(Exception):
    pass

class Mask():
    
    def __init__(self, width, height, fromSurface=None, threshold=255):
        if fromSurface:
            self.mask = gamejs.pixelcollision.Mask.new(fromSurface.surface, threshold)
        else:
            surface = Surface(dimensions=(width, height))
            self.mask = gamejs.pixelcollision.Mask.new(surface, threshold)
    
    # augmented
    def get_mask(self):
        return self.mask
    
    def get_size(self):
        return self.mask.getSize()
    
    def get_at(self, coord):
        return self.mask.getAt(coord[0], coord[1])
    
    def set_at(self, coord, value):
        self.mask.setAt(coord[0], coord[1], value)
    
    # I don't understand the offsets, so I hope this is ok
    def overlap(self, othermask, offset):
        ret = self.mask.overlapXY(othermask.mask, offset)
        
        if ret == False:
            return None
        else:
            return ret
    
    def overlap_area(self, othermask, offset):
        return self.mask.overlapArea(othermask.mask, offset)
    
    def overlap_mask(self, othermask, offset):
        size = self.get_size()
        ret = Mask(size[0], size[1])
        ret.mask = self.mask.overlapMask(othermask.mask, offset)
        return ret
    
    def invert(self):
        self.mask.invert()
    
    def clear(self):
        self.mask.clear()
    
    def fill(self):
        self.mask.fill()
    
    def scale(self, dimensions):
        self.mask = self.mask.scale(dimensions[0], dimensions[1])
    
    def draw(self, othermask, offset):
        self.mask.draw(othermask, offset)
    
    def erase(self, othermask, offset):
        self.mask.erase(othermask, offset)
    
    def count(self):
        return self.mask.countBits()
    
    def centroid(self):
        return self.mask.centroid()
    
    def angle(self):
        return self.mask.angle()
    
    def outline(self, every=1):
        return self.mask.outline(every)
    
    def convolve(self, othermask, outputmask=None, offset=[0,0]):
        if outputmask:
            outputmask.mask = self.mask.convolve(othermask, offset)
        else:
            size = self.get_size();
            ret = Mask(size[0], size[1])
            ret.mask = self.mask.convolve(othermask, offset)
            return ret
    
    def connected_component(self, coord=None):
        raise UnsupportedMethod("mask.connected_component: unsupported method")
    
    def connected_components(self, umin=0):
        raise UnsupportedMethod("mask.connected_components: unsupported method")
    
    def get_bounding_rects(self):
        raise UnsupportedMethod("mask.get_bounding_rects: unsupported method")
