from browser import window
from .mixer import Sound
from pygame.locals import *
import pygame.event

gamejs = window.gamejs

playing = None
queue = None
endevent = None

def load(filenames):
    global playing
    
    if type(filenames) is str:
        filenames = [filenames]
    
    if playing:
        playing.stop()
    
    playing = Sound(filenames)

# loops if a boolean instead of a number
def play(loops=False, start=0.0):
    global playing, queue, endevent
    
    def lineUp():
        if endevent:
            pygame.event.post(pygame.event.Event(endevent, sound=playing))
        playing = queue
        queue = None
        if playing:
            playing.set_volume(self.volume)
            playing.play(onEnd=lineUp)
    
    if playing:
        if start:
            playing.sound.seek(start)
        playing.play(loops=loops, onEnd=lineUp)

def rewind():
    global playing
    
    if playing:
        playing.sound.seek(0.0)

def stop():
    global playing
    
    if playing:
        playing.stop()

def pause():
    global playing
    
    if playing:
        playing.pause()

def unpause():
    global playing
    
    if playing:
        playing.unpause()

def fadeout(ms):
    global playing
    
    if playing:
        playing.fade_out(ms)

def set_volume(volume):
    global playing
    
    if playing:
        playing.set_volume(volume)

def get_volume(volume):
    global playing
    
    if playing:
        playing.get_volume()

def get_busy():
    global playing
    
    if playing:
        return playing.sound.playing()

def queue(filename):
    global queue
    
    if type(filenames) is str:
        filenames = [filenames]
    
    queue = Sound(filenames)

def set_endevent(utype=SOUNDEND):
    global endevent
    
    endevent = utype
    
def get_endevent():
    global endevent
    
    return endevent
