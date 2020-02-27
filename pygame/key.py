from browser import window
from .locals import *

gamejs = window.gamejs

class UnsupportedFunction(Exception):
    pass

KEY_REPEAT = False

def get_focused():
    return gamejs.display._hasFocus()

def get_pressed():
    ret = []
    keys = gamejs.event.pressed_keys
    for key in keys:
        ret.append(conv_key_constant(key))
    return ret

def get_mods():
    keys = get_pressed()
    
    ret = 0
    
    if K_CAPSLOCK in keys:
        ret = ret + KMOD_CAPS
    if K_RSHIFT in keys:
        ret = ret + KMOD_RSHIFT
    if K_LSHIFT in keys:
        ret = ret + KMOD_LSHIFT
    if K__LALT in keys:
        ret = ret + KMOD_LALT
    if K_RALT in keys:
        ret = ret + KMOD_RALT
    if K_LCTRL in keys:
        ret = ret + KMOD_LCTRL
    if K_RCTRL in keys:
        ret = ret + KMOD_RCTRL
    if K_LMETA in keys:
        ret = ret + KMOD_LMETA
    if K_RMETA in keys:
        ret = ret + KMOD_RMETA
    
    return ret

def set_mods(mods):
    raise UnsupportedFunction("key.set_mods: function unsupported")

# this doesn't implement delay and interval, it just turns it on or off
def set_repeat(delay=None, interval=None):
    global KEY_REPEAT
    
    if delay or interval:
        KEY_REPEAT = True

def get_repeat():
    global KEY_REPEAT
    
    if KEY_REPEAT:
        return (1, 1)

def name(key):
    keys = {K_BACKSPACE: "backspace",
            K_TAB: "tab",
            K_CLEAR: "clear",
            K_RETURN: "return",
            K_PAUSE: "pause",
            K_ESCAPE: "escape",
            K_SPACE: "space",
            K_EXCLAIM: "!",
            K_QUOTEDBL: '"',
            K_HASH: "#",
            K_DOLLAR: "$",
            K_AMPERSAND: "&",
            K_QUOTE: "'",
            K_LEFTPAREN: "(",
            K_RIGHTPAREN: ")",
            K_ASTERISK: "*",
            K_PLUS: "+",
            K_COMMA: ",",
            K_MINUS: "-",
            K_PERIOD: ".",
            K_SLASH: "/",
            K_0: "0",
            K_1: "1",
            K_2: "2",
            K_3: "3",
            K_4: "4",
            K_5: "5",
            K_6: "6",
            K_7: "7",
            K_8: "8",
            K_9: "9",
            K_COLON: ":",
            K_SEMICOLON: ";",
            K_LESS: "<",
            K_EQUALS: "=",
            K_GREATER: ">",
            K_QUESTIONL: "?",
            K_AT: "@",
            K_LEFTBRACKET: "[",
            K_RIGHTBRACKET: "]",
            K_CARET: "^",
            K_UNDERSCORE: "_",
            K_BACKQUOTE: "`",
            K_a: "a",
            K_b: "b",
            K_c: "c",
            K_d: "d",
            K_e: "e",
            K_f: "f",
            K_g: "g",
            K_h: "h",
            K_i: "i",
            K_j: "j",
            K_k: "k",
            K_l: "l",
            K_m: "m",
            K_n: "n",
            K_o: "o",
            K_p: "p",
            K_q: "q",
            K_r: "r",
            K_s: "s",
            K_t: "t",
            K_u: "u",
            K_v: "v",
            K_w: "w",
            K_x: "x",
            K_y: "y",
            K_z: "z",
            K_DELETE: "delete",
            K_KP0: "[0]",
            K_KP1: "[1]",
            K_KP2: "[2]",
            K_KP3: "[3]",
            K_KP4: "[4]",
            K_KP5: "[5]",
            K_KP6: "[6]",
            K_KP7: "[7]",
            K_KP8: "[8]",
            K_KP9: "[9]",
            K_KP_PERIOD: "[.]",
            K_KP_DIVIDE: "[/]",
            K_KP_MULTIPLY: "[*]",
            K_KP_MINUS: "[-]",
            K_KP_PLUS: "[+]",
            K_KP_ENTER: "enter",
            K_KP_EQUALS: "[=]",
            K_UP: "up",
            K_DOWN: "down",
            K_RIGHT: "right",
            K_LEFT: "left",
            K_INSERT: "insert",
            K_HOME: "home",
            K_END: "end",
            K_PAGEUP: "page up",
            K_PAGEDOWN: "page down",
            K_F1: "f1",
            K_F2: "f2",
            K_F3: "f3",
            K_F4: "f4",
            K_F5: "f5",
            K_F6: "f6",
            K_F7: "f7",
            K_F8: "f8",
            K_F9: "f9",
            K_F10: "f10",
            K_F11: "f11",
            K_F12: "f12",
            K_F13: "f13",
            K_F14: "f14",
            K_F15: "f15",
            K_NUMLOCK: "numlock",
            K_CAPSLOCK: "caps lock",
            K_SCROLLOCK: "scroll lock",
            K_RSHIFT: "right shift",
            K_LSHIFT: "left shift",
            K_RCTRL: "right ctrl",
            K_LCTRL: "left ctrl",
            K_RALT: "right alt",
            K_LALT: "left alt",
            K_RMETA: "right meta",
            K_LMETA: "left meta",
            K_LSUPER: "left super",
            K_RSUPER: "right super",
            K_MODE: "alt gr",
            K_HELP: "help",
            K_PRINT: "print screen",
            K_SYSREQ: "sys req",
            K_BREAK: "break",
            K_MENU: "menu",
            K_POWER: "power",
            K_EURO: "euro"}
    
    return keys[key]

