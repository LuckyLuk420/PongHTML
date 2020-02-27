# this module is currently unimplemented, see pygame.mouse.set_cursor and such

RAISE_EXCEPTION = True

class UnsupportedFunction(Exception):
    pass

def compile(strings, black='x', white='.', xor='o'):
    global RAISE_EXCEPTION
    
    if RAISE_EXCEPTION:
        raise UnsupportedFunction("cursors module is unsupported")

def load_xbm(cursorfile, maskfile=None):
    global RAISE_EXCEPTION
    
    if RAISE_EXCEPTION:
        raise UnsupportedFunction("cursors module is unsupported")
