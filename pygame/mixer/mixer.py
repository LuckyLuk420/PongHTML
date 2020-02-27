from browser import window, timer
from pygame import event
from pygame.locals import *

gamejs = window.gamejs

def init(frequency=22050, size=-16, channels=2, buffersize=4096):
    pass

def pre_init(frequency=22050, size=-16, channels=2, buffersize=4096):
    pass

def quit():
    pass

def get_init():
    return (22050, None, 2)

def stop():
    gamejs.audio.Howler.stop()

def pause():
    gamejs.audio.Howler.pause()

def unpause():
    gamejs.audio.Howler.unpause()

def fadeout():
    gamejs.audio.Howler.fadeout()

# with web audio, we have unlimited channels
def set_num_channels(count):
    pass

def get_num_channels():
    return 8

def set_reserved(count):
    pass

class Sound():
    
    # accepts a list of filenames for fallback compatibility
    # can also accept Uint8Array from sndarray
    def __init__(self, filenames):
        if type(filenames) is str:
            filenames = [filenames]
        self.sound = gamejs.audio.Howl.new({"src": filenames});
    
    # loops is either true or false, not a number
    def play(self, loops=False, maxtime=0, fade_ms=0, onEnd=None):
        self.sound.loop(loops)
        
        def stopSound():
            nonlocal self
            
            self.sound.stop()
        
        self.sound.play()
        
        if onEnd:
            self.sound.on("stop", onEnd)
        
        self.fadein(fade_ms)
        
        if maxtime:
            timer.set_timeout(stopSound, maxtime)
    
        # there's really only one channel
        return 0
    
    def fadein(self, ms):
        self.sound.fade(0.0, 1.0, ms)
    
    def stop(self):
        self.sound.stop()
    
    def fadeout(self, ms):
        self.sound.fade(0.0, 1.0, ms)
        self.sound.loop(False)
    
    def set_volume(self, volume):
        self.sound.volume(volume)
    
    def get_volume(self):
        return self.sound.volume()
    
    # not supported
    def get_num_channels(self):
        return 0
    
    def get_length(self):
        return self.sound.duration()
    
    def get_raw(self):
        return self.sound._buffer

class Channel():
    
    def __init__(self, uid):
        self.id = uid
        self.queue = None
        self.playing = None
        self.volume = 1.0
        self.endevent = None
    
    # loops is a boolean here
    def play(self, sound, loops=False, maxtime=0, fade_ms=0):
        def lineUp():
            if self.endevent:
                pygame.event.post(pygame.event.Event(self.endevent, sound=self.playing))
            self.playing = self.queue
            self.queue = None
            if self.playing:
                self.playing.set_volume(self.volume)
                self.playing.play(onEnd=lineUp)
        
        self.playing = sound
        self.playing.play(loops, maxtime, fade_ms, onEnd=lineUp)
        self.playing.set_volume(self.volume)
        
        if fade_ms:
            self.playing.fadein(fade_ms)
    
    def stop(self):
        if self.playing:
            self.playing.stop()
        self.queue = None
    
    def pause(self):
        if self.playing:
            self.playing.pause()
    
    def unpause(self):
        if self.playing:
            self.playing.play()
    
    def fadeout(self, time):
        if self.playing:
            self.playing.loop(False)
            self.playing.fadeout(5000)
    
    def set_volume(self, left, right=None):
        if self.playing:
            self.playing.set_volume(left)
        self.volume = left
    
    def get_volume(self):
        return self.volume
    
    def get_busy(self):
        return True if self.playing else False
    
    def get_sound(self):
        return self.playing
    
    def queue(self, sound):
        if not self.queue:
            self.queue = sound
        else:
            return self.queue
    
    def set_endevent(utype=SOUNDEND):
        self.endevent = utype
    
    def get_endevent():
        return self.endevent
