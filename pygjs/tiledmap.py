from browser import window
import pygame

gamejs = window.gamejs

# wrapper for gamejs/tiledmap

class Map():
    
    def __init__(self, url):
        self.map = gamejs.tiledmap.Map(url)
    
    def get_height(self):
        return self.map.height
    
    def get_layers(self):
        return self.map.layers
    
    def get_properties(self):
        return self.map.properties
    
    def get_tileheight(self):
        return self.map.tileHeight
    
    def get_tilewidth(self):
        return self.map.tileWidth
    
    def get_tiles(self):
        return self.map.tiles
    
    def get_width(self):
        return self.map.width
    
    height = property(get_height)
    layers = property(get_layers)
    properties = property(get_properties)
    tileheight = property(get_tileheight)
    tilewidth = property(get_tilewidth)
    tiles = property(get_tiles)
    width = property(get_width)

# this isn't well documented in gamejs
class MapView():
    
    def __init_(self, umap):
        self.mapview = gamejs.tiledmap.MapView(umap.map)
    
    def draw(self, surface, offset):
        self.mapview.draw(surface.surface, offset)
    
    def redraw(self):
        self.mapview.redraw()
    
    def get_image(self):
        return self.mapview.image
    
    def get_layerviews(self):
        return self.mapview.layerViews
    
    def get_mapimage(self):
        return self.mapview.mapImage
    
    def get_timeout(self):
        return self.mapview.timeout
    
    def get_viewrect(self):
        return pygame.Rect(obj=self.mapview.viewRect)
    
    image = property(get_image)
    layerviews = property(get_layerviews)
    mapimage = property(get_mapimage)
    timeout = property(get_timeout)
    viewrect = property(get_viewrect)
