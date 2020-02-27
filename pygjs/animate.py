from browser import window
import pygame

gamejs = window.gamejs

class SpriteSheet():
    
    # width and height properties on options are required
    def __init__(self, surface, options):
        self.spritesheet = gamejs.animate.SpriteSheet.new(surface.surface, options)
    
    def get(self, index):
        return pygame.Surface(dimensions=(0,0), fromSurface=self.spritesheet.get(index))

# try combining this with a sprite class :-)
class Animation():
    
    def __init__(self, spritesheet, initialstate, animationspec):
        self.animation = gamejs.animate.Animation.new(spritesheet.spritesheet, initialstate, animationspec)
    
    def get_image(self):
        return pygame.Surface(dimensions=(0,0), fromSurface=self.animation.image)
    
    image = property(get_image)
    
    def is_finished(self):
        return self.animation.isFinished()
    
    def set_state(self, statename):
        self.animation.setState(state)
    
    def update(self, ms):
        self.aimation.update(ms)
