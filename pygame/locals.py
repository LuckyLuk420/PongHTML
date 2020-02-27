from browser import window

gamejs = window.gamejs

# display constants
FULLSCREEN = -2147483648
DOUBLEBUF = 1073741824
HWSURFACE = 1
OPENGL = 2
RESIZABLE = 16
NOFRAME = 32

#event constants
NOEVENT = 0
ACTIVEEVENT = 1
KEYDOWN = 2
KEYUP = 3
MOUSEMOTION = 4
MOUSEBUTTONDOWN = 5
MOUSEBUTTONUP = 6
JOYAXISMOTION = 7
JOYBALLMOTION = 8
JOYHATMOTION = 9
JOYBUTTONDOWN = 10
JOYBUTTONUP = 11
QUIT = 12
VIDEORESIZE = 16
VIDEOEXPOSE = 17
USEREVENT = 24
# augmented this frankenstein
MOUSEWHEEL = 200
TOUCHDOWN = 201
TOUCHUP = 202
TOUCHMOTION = 203
ANIMATIONFRAME = 204
SOUNDEND = 205

def conv_event_type(eventType, touch=True):
    if eventType == gamejs.event.QUIT:
        return QUIT
    elif eventType == gamejs.event.DISPLAY_RESIZE:
        return VIDEORESIZE
    elif eventType == gamejs.event.DISPLAY_FULLSCREEN_ENABLED or eventType == gamejs.event.DISPLAY_FULLSCREEN_DISABLED:
        return VIDEOEXPOSE
    elif eventType == gamejs.event.KEY_DOWN:
        return KEYDOWN
    elif eventType == gamejs.event.KEY_UP:
        return KEYUP
    elif eventType == gamejs.event.MOUSE_MOTION:
        return MOUSEMOTION
    elif eventType == gamejs.event.MOUSE_UP:
        return MOUSEBUTTONUP
    elif eventType == gamejs.event.MOUSE_DOWN:
        return MOUSEBUTTONDOWN
    elif eventType == gamejs.event.MOUSE_WHEEL:
        return MOUSEWHEEL
    elif eventType == gamejs.event.TOUCH_UP:
        if touch:
            return TOUCHUP
        else:
            return MOUSEBUTTONUP
    elif eventType == gamejs.event.TOUCH_DOWN:
        if touch:
            return TOUCHDOWN
        else:
            return MOUSEBUTONDOWN
    elif eventType == gamejs.event.TOUCH_MOTION:
        if touch:
            return TOUCHMOTION
        else:
            return MOUSEMOTION
    elif eventType == gamejs.event.JOYSTICK_AXIS_MOTION:
        return JOYAXISMOTION
    elif eventType == gamejs.event.JOYSTICK_HAT_MOTION:
        return JOYHATMOTION
    elif eventType == gamejs.event.JOYSTICK_BUTTON_UP:
        return JOYBUTTONUP
    elif eventType == gamejs.event.JOYSTICK_BUTTON_DOWN:
        return JOYBUTTONDOWN
    elif eventType == gamejs.event.ANIMATIONFRAME:
        return ANIMATIONFRAME
    elif eventType == gamejs.event.USEREVENT:
        return USEREVENT

# keys
K_BACKSPACE = 8
K_TAB = 9
K_CLEAR = 12
K_RETURN = 13
K_PAUSE = 19
K_ESCAPE = 27
K_SPACE = 32
K_EXCLAIM = 33
K_QUOTEDBL = 34
K_HASH = 35
K_DOLLAR = 36
K_AMPERSAND = 38
K_QUOTE = 39
K_LEFTPAREN = 40
K_RIGHTPAREN = 41
K_ASTERISK = 42
K_PLUS = 43
K_COMMA = 44
K_MINUS = 45
K_PERIOD = 46
K_SLASH = 47
K_0 = 48
K_1 = 49
K_2 = 50
K_3 = 51
K_4 = 52
K_5 = 53
K_6 = 54
K_7 = 55
K_8 = 56
K_9 = 57
K_COLON = 58
K_SEMICOLON = 59
K_LESS = 60
K_EQUALS = 61
K_GREATER = 62
K_QUESTION = 63
K_AT = 64
K_LEFTBRACKET = 91
K_BACKSLASH = 92
K_RIGHTBRACKET = 93
K_CARET = 94
K_UNDERSCORE = 95
K_BACKQUOTE = 96
K_a = 97
K_b = 98
K_c = 99
K_d = 100
K_e = 101
K_f = 102
K_g = 103
K_h = 104
K_i = 105
K_j = 106
K_k = 107
K_l = 108
K_m = 109
K_n = 110
K_o = 111
K_p = 112
K_q = 113
K_r = 114
K_s = 115
K_t = 116
K_u = 117
K_v = 118
K_w = 119
K_x = 120
K_y = 121
K_z = 122
K_DELETE = 127
K_KP0 = 256
K_KP1 = 257
K_KP2 = 258
K_KP3 = 259
K_KP4 = 260
K_KP5 = 261
K_KP6 = 262
K_KP7 = 263
K_KP8 = 264
K_KP9 = 265
K_KP_PERIOD = 266
K_KP_DIVIDE = 267
K_KP_MULTIPLY = 268
K_KP_MINUS = 269
K_KP_PLUS = 270
K_KP_ENTER = 271
K_KP_EQUALS = 272
K_UP = 273
K_DOWN = 274
K_RIGHT = 275
K_LEFT = 276
K_INSERT = 277
K_HOME = 278
K_END = 279
K_PAGEUP = 280
K_PAGEDOWN = 281
K_F1 = 282
K_F2 = 283
K_F3 = 284
K_F4 = 285
K_F5 = 286
K_F6 = 287
K_F7 = 288
K_F8 = 289
K_F9 = 290
K_F10 = 291
K_F11 = 292
K_F12 = 293
K_F13 = 294
K_F14 = 295
K_F15 = 296
K_NUMLOCK = 300
K_CAPSLOCK = 301
K_SCROLLOCK = 302
K_RSHIFT = 303
K_LSHIFT = 304
K_RCTRL = 305
K_LCTRL = 306
K_RALT = 307
K_LALT = 308
K_RMETA = 309
K_LMETA = 310
K_LSUPER = 311
K_RSUPER = 312
K_MODE = 313
K_HELP = 315
K_PRINT = 316
K_SYSREQ = 317
K_BREAK  = 318
K_MENU = 319
K_POWER = 320
K_EURO  = 321

# not all key constants are converted, only the ones GameJS defines at this time
def conv_key_constant(keyConstant, shift=False, ctrl=False, cmd=False, meta=False):
    if keyConstant == gamejs.event.K_UP:
        return K_UP
    elif keyConstant == gamejs.event.K_DOWN:
        return K_DOWN
    elif keyConstant == gamejs.event.K_RIGHT:
        return K_RIGHT
    elif keyConstant == gamejs.event.K_LEFT:
        return K_LEFT
    elif keyConstant == gamejs.event.K_SPACE:
        return K_SPACE
    elif keyConstant == gamejs.event.K_BACKSPACE:
        return K_BACKSPACE
    elif keyConstant == gamejs.event.K_TAB:
        return K_TAB
    elif keyConstant == gamejs.event.K_ENTER:
        return K_RETURN
    elif keyConstant == gamejs.event.K_SHIFT:
        return K_LSHIFT
    elif keyConstant == gamejs.event.K_CTRL:
        return K_LCTRL
    elif keyConstant == gamejs.event.K_ALT:
        return K_LMETA
    elif keyConstant == gamejs.event.K_ESC:
        return K_ESCAPE
    elif keyConstant == gamejs.event.K_0:
        if shift:
            return K_RIGHTPAREN
        else:
            return K_0
    elif keyConstant == gamejs.event.K_1:
        if shift:
            return K_EXCLAIM
        else:
            return K_1
    elif keyConstant == gamejs.event.K_2:
        if shift:
            return K_AT
        else:
            return K_2
    elif keyConstant == gamejs.event.K_3:
        if shift:
            return K_HASH
        else:
            return K_3
    elif keyConstant == gamejs.event.K_4:
        if shift:
            return K_DOLLAR
        else:
            return K_4
    elif keyConstant == gamejs.event.K_5:
        return K_5
    elif keyConstant == gamejs.event.K_6:
        if shift:
            return K_CARET
        else:
            return K_6
    elif keyConstant == gamejs.event.K_7:
        if shift:
            return K_AMPERSAND
        else:
            return K_7
    elif keyConstant == gamejs.event.K_8:
        if shift:
            return K_ASTERISK
        else:
            return K_8
    elif keyConstant == gamejs.event.K_9:
        if shift:
            return  K_LEFTPAREN
        else:
            return K_9
    elif keyConstant == gamejs.event.K_a:
        return K_a
    elif keyConstant == gamejs.event.K_b:
        return K_b
    elif keyConstant == gamejs.event.K_c:
        return K_c
    elif keyConstant == gamejs.event.K_d:
        return K_d
    elif keyConstant == gamejs.event.K_e:
        return K_e
    elif keyConstant == gamejs.event.K_f:
        return K_f
    elif keyConstant == gamejs.event.K_g:
        return K_g
    elif keyConstant == gamejs.event.K_h:
        return K_h
    elif keyConstant == gamejs.event.K_i:
        return K_i
    elif keyConstant == gamejs.event.K_j:
        return K_j
    elif keyConstant == gamejs.event.K_k:
        return K_k
    elif keyConstant == gamejs.event.K_l:
        return K_l
    elif keyConstant == gamejs.event.K_m:
        return K_m
    elif keyConstant == gamejs.event.K_n:
        return K_n
    elif keyConstant == gamejs.event.K_o:
        return K_o
    elif keyConstant == gamejs.event.K_p:
        return K_p
    elif keyConstant == gamejs.event.K_q:
        return K_q
    elif keyConstant == gamejs.event.K_r:
        return K_r
    elif keyConstant == gamejs.event.K_s:
        return K_s
    elif keyConstant == gamejs.event.K_t:
        return K_t
    elif keyConstant == gamejs.event.K_u:
        return K_u
    elif keyConstant == gamejs.event.K_v:
        return K_v
    elif keyConstant == gamejs.event.K_w:
        return K_w
    elif keyConstant == gamejs.event.K_x:
        return K_x
    elif keyConstant == gamejs.event.K_y:
        return K_y
    elif keyConstant == gamejs.event.K_z:
        return K_z
    elif keyConstant == gamejs.event.K_KP1:
        return K_KP1
    elif keyConstant == gamejs.event.K_KP2:
        return K_KP2
    elif keyConstant == gamejs.event.K_KP3:
        return K_KP3
    elif keyConstant == gamejs.event.K_KP4:
        return K_KP4
    elif keyConstant == gamejs.event.K_KP5:
        return K_KP5
    elif keyConstant == gamejs.event.K_KP6:
        return K_KP6
    elif keyConstant == gamejs.event.K_KP7:
        return K_KP7
    elif keyConstant == gamejs.event.K_KP8:
        return K_KP8
    elif keyConstant == gamejs.event.K_KP9:
        return K_KP9
    else:
        # these work for NW.js (Chromium)
        # US keyboard (Apple standard wireless)
        
        # backspace = 8, K_BACKSPACE = 8
        # tab = 9, K_TAB = 9
        # return = 13, K_RETURN = 13
        # escape = 27, K_ESCAPE = 27
        # space = 32, K_SPACE = 32
        
        if keyConstant == 222:
            if shift:
                return K_QUOTEDBL
            else:
                return K_QUOTE
        elif keyConstant == 187:
            if shift:
                return K_PLUS
            else:
                return K_EQUALS
        elif keyConstant == 188:
            if shift:
                return K_LESS
            else:
                return K_COMMA
        elif keyConstant == 189:
            if shift:
                return K_UNDERSCORE
            else:
                return K_MINUS
        elif keyConstant == 190:
            if shift:
                return K_GREATER
            else:
                return K_PERIOD
        elif keyConstant == 191:
            if shift:
                return K_QUESTION
            else:
                return K_SLASH
        elif keyConstant == 186:
            if shift:
                return K_COLON
            else:
                return K_SEMICOLON
        elif keyConstant == 219:
            return K_LEFTBRACKET
        elif keyConstant == 221:
            return K_RIGHTBRACKET
        elif keyConstant == 220:
            return K_BACKSLASH
        elif keyConstant == 192:
            return K_BACKQUOTE
        elif keyConstant == 46:
            return K_DELETE
        elif keyConstant == 112:
            return K_F1
        elif keyConstant == 113:
            return K_F2
        elif keyConstant == 114:
            return K_F3
        elif keyConstant == 115:
            return K_F4
        elif keyConstant == 116:
            return K_F5
        elif keyConstant == 117:
            return K_F6
        elif keyConstant == 118:
            return K_F7
        elif keyConstant == 119:
            return K_F8
        elif keyConstant == 120:
            return K_F9
        elif keyConstant == 121:
            return K_F10
        elif keyConstant == 122:
            return K_F11
        elif keyConstant == 123:
            return K_F12
        elif keyConstant == 20:
            return K_CAPSLOCK

LOADING = False
IDLE = False

KMOD_LSHIFT = 1
KMOD_RSHIFT = 2
KMOD_SHIFT = 3
KMOD_LCTRL = 64
KMOD_RCTRL = 128
KMOD_CTRL = 192
KMOD_LALT = 256
KMOD_RALT = 512
KMOD_ALT = 768
KMOD_LMETA = 1024
KMOD_RMETA = 2048
KMOD_META = 3072
KMOD_CAPS = 8192

STYLE_DEFAULT = 0
STYLE_NORMAL = 1
STYLE_UNDERLINE = 2
STYLE_OBLIQUE = 4
STYLE_STRONG = 8
STYLE_WIDE = 16
STYLE_DEFAULT = 32
