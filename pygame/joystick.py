from browser import window

gamejs = window.gamejs

class UnsupportedMethod(Exception):
    pass

def init():
    pass

def quit():
    pass

def get_init():
    return True

def get_count():
    return gamejs.gamepad.joystick.count()

class Joystick():
    
    def __init__(self, num):
        gamepad = gamejs.gamepad.joystick.gamepads[num]
        self.num = num
        self.init = False
        self.id = gamepad.index
        self.name = gamepad.id
        self.numaxes = len(gamepad.axes)
        self.numballs = 0 # we don't support balls
        self.numbuttons = len(gamepad.buttons)
        self.numhats = 0 # don't know how to support this
        
    def init(self):
        self.init = True
        pass
    
    # you can't ignore a gamepad in Gamepad API, decided to extend that
    # (AS FAR AS I KNOW)
    def quit(self):
        pass
    
    def get_init(self):
        return self.init
    
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name
    
    def get_numaxes(self):
        return self.numaxes
    
    def get_axis(self, num):
        gamepad = gamejs.gamepad.joystick.gamepads[self.num]
        return gamepad.axes[num]
    
    def get_numballs(self):
        return self.numballs
    
    def get_ball(self, num):
        raise UnsupportedMethod("joystick: ball not supported")
    
    def get_numbuttons(self):
        return self.numbuttons
    
    def get_button(self, num):
        gamepad = gamejs.gamepad.joystick.gamepads[self.num]
        return gamepad.buttons[num]
    
    def get_numhats(self):
        return self.numhats
    
    def get_hat(self, num):
        raise UnsupportedMethod("joystick: hat specific polling on device not supported, use event")
        