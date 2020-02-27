from browser import window, document

gamejs = window.gamejs

class UnsupportedFunction(Exception):
    pass

RAISE_EXCEPTIONS = True

current_cursor_css = "auto"

def get_pressed():
    buttons = gamejs.event.pressed_buttons
    
    button1 = False
    button2 = False
    button3 = False
    
    if 0 in buttons:
        button1 = True
    if 1 in buttons:
        button2 = True
    # THIS IS SUPER BUGGY DON'T RELY ON IT!
    if 2 in buttons:
        button3 = True
    
    return (button1, button2, button3)

def get_pos():
    return gamejs.event.mouse_pos

def get_rel():
    curpos = get_pos()
    relpos = [get_rel.mouse_pos[0]-curpos[0], get_rel.mouse_pos[1]-curpos[1]]
    get_rel.mouse_pos = curpos
    return relpos
get_rel.mouse_pos = [0,0]

# if you want mouse control look into pointer locking with GameJS
def set_pos(coords):
    global RAISE_EXCEPTIONS
    
    if RAISE_EXCEPTIONS:
        raise UnsupportedFunction("mouse.set_pos: function unsupported");

def set_visible(visibility):
    global current_cursor_css
    
    canvas = document.getElementById(gamejs.display.CANVAS_ID)
    if visibility:
        canvas.style.cursor = current_cursor_css
    else:
        canvas.style.cursor = "none"
    ret = set_visible.visibility
    set_visible.visibility = visibility
    return ret
set_visible.visibility = True

def get_focused():
    return gamejs.display._hasFocus()

# here you can set the cursor's CSS on the canvas, everything else fails
def set_cursor(sizeOrCSS, hotspot=None, xormasks=None, andmasks=None):
    global current_cursor_css
    
    if type(sizeOrCSS) is int or type(sizeOrCSS) is float:
        return
    elif type(sizeOrCSS) is str:
        canvas = document.getElementById(gamejs.display.CANVAS_ID)
        canvas.style.cursor = sizeOrCSS
        current_cursor_css - sizeOrCSS
    else:
        return

# returns CSS
def get_cursor():
    global current_cursor_css
    
    return (current_cursor_css, 0, 0, 0)
