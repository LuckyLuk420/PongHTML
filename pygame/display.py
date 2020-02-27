from browser import window
from .surface import Surface

gamejs = window.gamejs

DISABLE_SMOOTHING = gamejs.display.DISABLE_SMOOTHING

def init():
    gamejs.display.init()

def quit():
    pass

def get_surface():
    return Surface(dimensions=(0,0), fromSurface=gamejs.display.getSurface())

def set_mode(resolution=(0,0), flags=0, depth=0):
    gamejs.display.setMode(resolution, flags, depth)
    return get_surface()

def flip():
    pass

def update():
    pass

def get_driver():
    return "gamejs"

def Info():
    class Info():
        def __init__(self):
            self.hw = False
            self.wm = gamejs.display.isFullScreen()
            self.video_mem = 0
            self.bitsize = 32 if gamejs.display.DEPTH == 32 else 8
            self.bytesize = 4 if gamejs.display.DEPTH == 32 else 1
            # I put these as None until I learn more about how canvases work
            self.masks = None
            self.shifts = None
            self.losses = None
            # I have no idea what is accelerated, so these are all False
            self.blit_hw = False
            self.blit_hw_CC = False
            self.blit_hw_A = False
            self.blit_sw = False
            self.blit_sw_CC = False
            self.blit_sw_A = False
            # These are the width and height of the display surface
            size = gamejs.display.getSurface().getSize()
            self.current_w = size[0]
            self.current_h = size[1]
    
    return Info()

def get_wm_info():
    return {}

def list_modes(depth=0, flags=None):
    return -1

def mode_ok(resolution=(0,0), flags=None, depth=0):
    if not depth:
        return 32
    if depth == 8:
        return 8
    return 0

# Might be useful in the future with WebGL?
def gl_get_attribute(flag):
    return None

def gl_set_attribute(flag, value):
    return None

def get_active():
    return not gamejs.display.minimized

def iconify():
    gamejs.display.minimize()

# toggles windows fullscreen mode in NW.js
def toggle_fullscreen():
    gamejs.display.toggleFullScreen()

def set_gamma(red, green=None, blue=None):
    return False

def set_gamma_ramp(red, green, blue):
    return False

# Could use nw.js Tray?
def set_icon(surface):
    pass

def set_caption(title, icontitle=None):
    gamejs.display.setTitle(title)

def get_caption():
    return (gamejs.display.getTitle(), None)

def set_palette(palette=None):
    pass
