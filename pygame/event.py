from browser import window, timer, console
from .locals import *
import pygame.locals
import pygame.key
import pygame.time

gamejs = window.gamejs

_queue = []

_blocked_types = set()

class EventType():
    
    def __init__(self, eventType, event=None, **attributes):
        self.type = eventType
        for attr in attributes:
            setattr(self, attr, attributes[attr])
        
        # augmented
        self.event = event
    
    #augmented
    def get_event(self):
        return self.event
    
    def __cmp__(self, other):
        assert isinstance(other, Event)
        if self.type == other.type:
            if self.__dict__ == other.__dict__:
                return 0
        return 1

def pump(callback=None):
    if gamejs.time.reqAnimationFrame:
        if callback:
            gamejs.time.reqAnimationFrame(callback)

def get(types=None):
    global _queue
    
    if not types:
        ret = _queue.copy()
        _queue.clear()
        return ret
    elif type(types) is list or type(types) is tuple:
        ret = [e for e in _queue if e.type in types]
        _queue = [e for e in _queue if e.type not in types]
        return ret
    else:
        ret = [e for e in _queue if e.type == types]
        _queue = [e for e in _queue if e.type != types]
        return ret

# augmentation
def mainloop(eventFunc=None, updateFunc=None, drawFunc=None, loadingFunc=None):
    if not mainloop.addedFrame:
        add_animation_frame_to_queue(False)
        mainloop.addedFrame = True
    if not mainloop.eventFunc and eventFunc:
        mainloop.eventFunc = eventFunc
    if not mainloop.updateFunc and updateFunc:
        mainloop.updateFunc = updateFunc
    if not mainloop.drawFunc and drawFunc:
        mainloop.drawFunc = drawFunc
    if not mainloop.loadingFunc and loadingFunc:
        mainloop.loadingFunc = loadingFunc
    if not pygame.time.DELAYED or pygame.locals.IDLE:
        for event in get():
            if event.type == ANIMATIONFRAME:
                mainloop.ms += event.duration
                if mainloop.ms > 1000:
                    mainloop.ms = 0
                if pygame.time.clock.framerate > 0:
                    if mainloop.ms > (1000 / pygame.time.clock.framerate):
                        if mainloop.updateFunc:
                            mainloop.updateFunc(mainloop.ms)
                        if mainloop.drawFunc:
                            mainloop.drawFunc()
                        mainloop.ms = 0
                else:
                    if mainloop.updateFunc:
                        mainloop.updateFunc(mainloop.ms)
                    if mainloop.drawFunc:
                        mainloop.drawFunc()
                    mainloop.ms = 0
            if mainloop.eventFunc:
                mainloop.eventFunc(event)
    elif gamejs.image.isPreloading() or gamejs.font.isPreloading() or gamejs.audio.isPreloading():
        if mainloop.loadingFunc:
            mainloop.loadingFunc()
            clear()        
    else:
        clear()
    timer.set_timeout(mainloop, 1)
mainloop.ms = 0
mainloop.addedFrame = False
mainloop.eventFunc = None
mainloop.updateFunc = None
mainloop.drawFunc = None
mainloop.loadingFunc = None

def ready(func):
    gamejs.ready(func)

def poll():
    global _queue
    
    if _queue:
        ret = _queue[0]
        _queue = _queue[1:]
        return ret
    else:
        return NOEVENT

def wait():
    global _queue
    
    pygame.locals.IDLE = True
    
    if _queue:
        pygame.locals.IDLE = False
        wait.event = poll()
    else:
        timer.set_timeout(wait, 100)

wait.event = None

def peek(types):
    global _queue
    
    if type(types) is list or type(types) is tuple:
        check = [e for e in _queue if e.type in types]
        return bool(check)
    else:
        check = [e for e in _queue if e.type == types]
        return bool(check)

def clear():
    global _queue
    
    _queue.clear()

def event_name(eventType):
    table = {QUIT: 'Quit',
             ACTIVEEVENT: 'ActiveEvent',
             KEYDOWN: 'KeyDown',
             KEYUP: 'KeyUp',
             MOUSEMOTION: 'MouseMotion',
             MOUSEBUTTONDOWN: 'MouseButtonDown',
             MOUSEBUTTONUP: 'MouseButtonUp',
             JOYAXISMOTION: 'JoyAxisMotion',
             JOYBALLMOTION: 'JoyBallMotion',
             JOYHATMOTION: 'JoyHatMotion',
             JOYBUTTONDOWN: 'JoyButtonDown',
             JOYBUTTONUP: 'JoyButtonUp',
             VIDEORESIZE: 'VideoResize',
             VIDEOEXPOSE: 'VideoExpose',
             USEREVENT: 'UserEvent',
             MOUSEWHEEL: 'MouseWheel',
             TOUCHDOWN: 'TouchDown',
             TOUCHUP: 'TouchUp',
             TOUCHMOTION: 'TouchMotion',
             ANIMATIONFRAME: 'AnimationFrame'}
    
    return table[eventType]

def set_blocked(types):
    global _blocked_types
    
    if types is None:
        _blocked_types.clear()
    elif type(types) is list or type(types) is tuple:
        for t in types:
            _blocked_types.add(t)
    else:
        _blocked_types.add(t)

def set_allowed(types):
    global _blocked_types
    
    if types is None:
        _blocked_types = {QUIT, ACTIVEEVENT, KEYDOWN, KEYUP, MOUSEMOTION,
                        MOUSEBUTTONDOWN, MOUSEBUTTONUP, JOYAXISMOTION,
                        JOYBALLMOTION, JOYHATMOTION, JOYBUTTONDOWN,
                        JOYBUTTONUP, VIDEORESIZE, VIDEOEXPOSE, USEREVENT,
                        MOUSEWHEEL, TOUCHDOWN, TOUCHUP, TOUCHMOTION, ANIMATIONFRAME}
    elif type(types) is list or type(types) is tuple:
        for t in types:
            _blocked_types.discard(t)
    else:
        _blocked_types.discard(t)

def get_blocked(eventType):
    global _blocked_types
    
    return (eventType in _blocked_types)

def set_grab():
    pass

def get_grab():
    return False

def post(event):
    global _queue
    
    _queue.append(event)

def Event(eventType, attrs=None, event=None, **attributes):
    if attrs:
        return EventType(eventType, event=event, **attrs)
    else:
        return EventType(eventType, event=event, **attributes)

# gather gamejs events

# QUIT, ACTIVEEVENT, ?

keydowns = []

# this differs on mod attribute, here mod attribute is dictionary!
def _onKeyDown(event):
    global _queue, keydowns
    
    key = conv_key_constant(event.key, shift=event.shiftKey, ctrl=event.ctrlKey, meta=event.metaKey)
    
    if not pygame.key.KEY_REPEAT:
        if key in keydowns:
            return
        else:
            keydowns.append(key)
    
    _queue.append(Event(conv_event_type(event.type), event=event, key=key, mod={'shift': event.shiftKey, 'ctrl': event.ctrlKey, 'meta': event.metaKey}))

gamejs.event.onKeyDown(_onKeyDown)

# this differs on mod attribute, here mod attribute is dictionary!
def _onKeyUp(event):
    global _queue, keydowns
    
    key = conv_key_constant(event.key, shift=event.shiftKey, ctrl=event.ctrlKey, meta=event.metaKey)
    
    if not pygame.key.KEY_REPEAT:
        keydowns.remove(key)
    
    _queue.append(Event(conv_event_type(event.type), event=event, key=key, mod={'shift': event.shiftKey, 'ctrl': event.ctrlKey, 'meta': event.metaKey}))

gamejs.event.onKeyUp(_onKeyUp)

def _onMouseMotion(event):
    global _queue
    
    _queue.append(Event(conv_event_type(event.type), event=event, pos=event.pos, rel=event.rel, buttons=event.buttons))

gamejs.event.onMouseMotion(_onMouseMotion)

def _onMouseButtonDown(event):
    global _queue
    
    _queue.append(Event(conv_event_type(event.type), event=event, pos=event.pos, button=event.button))

gamejs.event.onMouseDown(_onMouseButtonDown)

def _onMouseButtonUp(event):
    global _queue
    
    _queue.append(Event(conv_event_type(event.type), event=event, pos=event.pos, button=event.button))

gamejs.event.onMouseUp(_onMouseButtonUp)

def _onMouseWheel(event):
    global _queue
    
    _queue.append(Event(conv_event_type(event.type), event=event, pos=event.pos, delta=event.delta))

gamejs.event.onMouseWheel(_onMouseWheel)

# joystick events

def _JoyAxisMotion(event):
    global _queue
    
    _queue.append(Event(conv_event_type(event.type), event=event, joy=event.gamepad.index, axis=event.axis, value=event.value))

gamejs.event.onJoystickAxisMotion(_JoyAxisMotion)

def _JoyHatMotion(event):
    global _queue
    
    _queue.append(Event(conv_event_type(event.type), event=event, joy=event.gamepad.index, hat=event.hat, value=event.value))

gamejs.event.onJoystickHatMotion(_JoyHatMotion)

def _JoyButtonDown(event):
    global _queue

    _queue.append(Event(conv_event_type(event.type), event=event, joy=event.gamepad.index, button=event.value))

gamejs.event.onJoystickButtonDown(_JoyButtonDown)

def _JoyButtonUp(event):
    global _queue
    
    _queue.append(Event(conv_event_type(event.type), event=event, joy=event.gamepad.index, button=event.value))

gamejs.event.onJoystickButtonUp(_JoyButtonUp)

def _onTouchDown(event):
    global _queue
    
    _queue.append(Event(conv_event_type(event.type), event=event, touches=event.touches))

gamejs.event.onTouchDown(_onTouchDown)

def _onTouchUp(event):
    global _queue
    
    _queue.append(Event(conv_event_type(event.type), event=event, touches=event.touches))

gamejs.event.onTouchUp(_onTouchUp)

def _onTouchMotion(event):
    global _queue
    
    _queue.append(Event(conv_event_type(event.type), event=event, touches=event.touches))

gamejs.event.onTouchMotion(_onTouchMotion)

def _onVideoResize(event):
    global _queue
    
    _queue.append(Event(conv_event_type(event.type), event=event, w=event.w, h=event.h, size=event.size))

gamejs.event.onDisplayResize(_onVideoResize)

def _onVideoExpose(event):
    global _queue
    
    _queue.append(Event(conv_event_type(event.type), event=event))

gamejs.event.onFullscreen(_onVideoExpose)

def add_animation_frame_to_queue(onlyOnce=True):
    def on_animation_frame(event):
        if onlyOnce:
            for e in _queue:
                etype = conv_event_type(e.type)
                if etype == ANIMATIONFRAME:
                    break
            else:
                _queue.append(Event(conv_event_type(event.type), event=event, duration=event.duration))
        else:
            _queue.append(Event(conv_event_type(event.type), event=event, duration=event.duration))
    
    gamejs.event.onAnimationFrame(on_animation_frame)
